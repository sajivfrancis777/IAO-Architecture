"""gen_systems_arch.py — Generate Systems Architecture Documents for capabilities.

Orchestrates: csv_parser → iapm_lookup → mermaid_builder → diff_engine → Jinja2 render.
Reads tower.yaml to discover capabilities and their view labels.
Produces one Markdown file per capability in the output/docs/systems-architecture/ folder.

Usage (single capability):
    python -m src.gen_systems_arch --tower FPR --cap DS-020

Usage (full tower):
    python -m src.gen_systems_arch --tower FPR

Usage (all towers):
    python -m src.gen_systems_arch --all
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re as _re
import shutil
import subprocess
import sys
import zlib
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Optional

import yaml
from jinja2 import Environment, FileSystemLoader

# Add parent to path for imports when run as script
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.csv_parser import FlowSet, FlowHop, parse_flow_csv
from src.iapm_lookup import IAPMLookup
from src.mermaid_builder import build_mermaid, build_archimate_mermaid, build_data_flow_mermaid, build_data_arch_mermaid, build_platform_arch_mermaid
from src.diff_engine import diff_flows, DiffResult
from src.smartsheet_loader import SmartsheetLoader, SmartsheetData
from src.context_loader import load_capability_context, CapabilityContext
from src.bpmn_parser import load_capability_bpmns, bpmn_to_mermaid, build_process_inventory_table, BPMNProcess
from src.xlsx_loader import load_workbook as load_xlsx_workbook, find_workbook as find_xlsx_workbook
from src.cap_name_resolver import CapNameResolver


# ---------------------------------------------------------------------------
# Mermaid Live Editor URL encoder
# ---------------------------------------------------------------------------
def mermaid_live_url(mermaid_code: str) -> str:
    """Encode mermaid code into a mermaid.live editor URL.

    Uses the same pako-deflate + base64url encoding that mermaid.live expects.
    """
    if not mermaid_code or not mermaid_code.strip():
        return ""
    state = json.dumps({
        "code": mermaid_code.strip(),
        "mermaid": {"theme": "default"},
        "autoSync": True,
        "updateDiagram": True,
    }, separators=(",", ":"))
    compressed = zlib.compress(state.encode("utf-8"), level=9)
    encoded = base64.urlsafe_b64encode(compressed).decode("ascii")
    return f"https://mermaid.live/view#pako:{encoded}"


# ---------------------------------------------------------------------------
# SVG pre-rendering via mmdc (mermaid CLI)
# ---------------------------------------------------------------------------
_MMDC = shutil.which("mmdc") or shutil.which("npx")


def _render_mermaid_svgs(rendered: str, output_dir: Path, cap_id: str) -> str:
    """Find mermaid code blocks in rendered markdown, render each to SVG,
    and add a 'View full-size SVG' link below each block.

    Non-destructive: the mermaid fenced block is kept as-is for inline rendering.
    Falls back gracefully if mmdc is unavailable or rendering fails.
    """
    mmdc = shutil.which("mmdc")
    use_npx = False
    if not mmdc:
        npx = shutil.which("npx")
        if npx:
            mmdc = npx
            use_npx = True
        else:
            return rendered  # no CLI available — skip SVG generation

    svg_dir = output_dir / "svg"
    svg_dir.mkdir(parents=True, exist_ok=True)

    pattern = _re.compile(r"(```mermaid\n)(.*?)(```)", _re.DOTALL)
    svg_count = 0

    def _replace_block(match: _re.Match) -> str:
        nonlocal svg_count
        svg_count += 1
        fence_open = match.group(1)
        mermaid_code = match.group(2)
        fence_close = match.group(3)

        svg_name = f"{cap_id}-diagram-{svg_count}.svg"
        svg_path = svg_dir / svg_name
        mmd_path = svg_dir / f"_tmp_{svg_count}.mmd"

        try:
            mmd_path.write_text(mermaid_code, encoding="utf-8")
            cmd = ([mmdc, "--yes", "@mermaid-js/mermaid-cli", "-i"] if use_npx
                   else [mmdc, "-i"])
            cmd += [str(mmd_path), "-o", str(svg_path),
                    "-b", "transparent", "--width", "2400"]
            subprocess.run(cmd, capture_output=True, timeout=30, check=True)
        except Exception:
            # Cleanup and return original block unchanged
            mmd_path.unlink(missing_ok=True)
            return match.group(0)
        finally:
            mmd_path.unlink(missing_ok=True)

        if not svg_path.exists():
            return match.group(0)

        # Build relative link from .md to svg/ directory
        rel_svg = f"svg/{svg_name}"
        live_url = mermaid_live_url(mermaid_code)
        link_line = (
            f'\n\n<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;">'
            f'<a href="{rel_svg}" title="Open full-size SVG">&#128269; View full-size SVG</a>'
        )
        if live_url:
            link_line += (
                f' &nbsp;|&nbsp; '
                f'<a href="{live_url}" title="View full diagram">&#128065; View Diagram</a>'
            )
        link_line += '</div>\n'

        return fence_open + mermaid_code + fence_close + link_line

    result = pattern.sub(_replace_block, rendered)
    if svg_count:
        print(f"    SVG: rendered {svg_count} diagrams to {svg_dir.name}/")
    return result


# ---------------------------------------------------------------------------
# BPMN orientation heuristic
# ---------------------------------------------------------------------------
def _bpmn_direction(proc: BPMNProcess) -> str:
    """Choose TD (top-down) or LR (left-right) based on process shape.

    Portrait PDF page (~6.5" usable width, ~9" usable height at 0.75" margins):
    - TD uses the full page height (9") — good for sequential deep flows
    - LR uses the full page width (6.5") — good for wide multi-lane flows

    Heuristic: estimate the "aspect ratio" of the flowchart.
    - Many nodes in few lanes → tall/narrow → TD fits better
    - Many lanes with moderate nodes each → wide/short → LR fits better
    - High gateway count creates branching (widens the graph) → prefer TD
    """
    total_nodes = len(proc.nodes)
    lane_count = len(proc.lanes) if proc.lanes else 1
    gw_count = sum(1 for n in proc.nodes.values() if n.is_gateway)

    # Estimate depth (longest chain) vs width (lanes × branching)
    depth_estimate = total_nodes / max(lane_count, 1)
    width_factor = lane_count + (gw_count * 0.5)

    # Very small processes — TD always fits on one page
    if total_nodes <= 10:
        return "TD"

    # Many lanes (3+) with moderate depth — LR to spread horizontally
    if lane_count >= 3 and depth_estimate <= 15:
        return "LR"

    # 2 lanes: LR only if not too deep and not too many gateways
    if lane_count == 2 and depth_estimate <= 12 and gw_count <= 8:
        return "LR"

    # High gateway counts cause wide branching — TD keeps it contained
    if gw_count > 10:
        return "TD"

    # Large single-lane process — TD uses portrait height efficiently
    if lane_count == 1:
        return "TD"

    # Default: TD is safer for portrait PDF
    return "TD"

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"
TEMPLATES_DIR = WORKSPACE / "templates"
IAPM_CSV = WORKSPACE / "data" / "iapm" / "IAPM_All_Solutions.csv"
OBJECT_TRACKER_CSV = WORKSPACE / "data" / "smartsheet" / "object_trackers" / "s4_r3_object_tracker.csv"

# Banner SVG as base64 data URI (self-contained — works in any deployment context)
_BANNER_SVG_PATH = TEMPLATES_DIR / "assets" / "cover_banner.svg"
_BANNER_DATA_URI = ""
if _BANNER_SVG_PATH.exists():
    _svg_bytes = _BANNER_SVG_PATH.read_bytes()
    _BANNER_DATA_URI = "data:image/svg+xml;base64," + base64.b64encode(_svg_bytes).decode("ascii")

# New template (TOGAF D+A+T)
BDAT_TEMPLATE = "systems_architecture.md.j2"
# Legacy template (application-only, kept for backward compat)
LEGACY_TEMPLATE = "capability_architecture.md.j2"


# ---------------------------------------------------------------------------
# Config data classes
# ---------------------------------------------------------------------------
@dataclass
class ViewConfig:
    label: str = "Current-State"
    description: str = ""


@dataclass
class CapabilityConfig:
    cap_id: str = ""
    name: str = ""
    l1: str = ""
    status: str = "active"
    current_view: ViewConfig = field(default_factory=ViewConfig)
    future_view: ViewConfig = field(default_factory=lambda: ViewConfig(label="Future-State"))


@dataclass
class ReleaseConfig:
    release_id: str = "R1-R5"
    name: str = "R1 – R5"
    go_live: str = ""


@dataclass
class TowerConfig:
    shortcode: str = ""
    name: str = ""
    capabilities: list[CapabilityConfig] = field(default_factory=list)
    release: ReleaseConfig = field(default_factory=ReleaseConfig)


@dataclass
class SystemEntry:
    """For the §6 system inventory table."""
    name: str
    iapm_id: str
    status: str


# ---------------------------------------------------------------------------
# YAML parsing
# ---------------------------------------------------------------------------
def load_tower_config(tower_dir: Path) -> TowerConfig:
    """Parse tower.yaml from a tower directory."""
    yaml_path = tower_dir / "tower.yaml"
    if not yaml_path.exists():
        return TowerConfig(shortcode=tower_dir.name, name=tower_dir.name)

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    tower_data = data.get("tower", {})
    tc = TowerConfig(
        shortcode=tower_data.get("shortcode", tower_dir.name),
        name=tower_data.get("name", tower_dir.name),
    )

    # Parse releases
    releases = data.get("releases", [])
    if releases:
        r = releases[0]
        tc.release = ReleaseConfig(
            release_id=str(r.get("id", "R1-R5")),
            name=r.get("name", "R1 – R5"),
            go_live=str(r.get("go_live", "")),
        )

    # Parse capabilities
    for cap in data.get("capabilities", []):
        views = cap.get("views", {})
        cur_view = views.get("current", {})
        fut_view = views.get("future", {})
        cc = CapabilityConfig(
            cap_id=cap.get("id", ""),
            name=cap.get("name", ""),
            l1=cap.get("l1", ""),
            status=cap.get("status", "active"),
            current_view=ViewConfig(
                label=cur_view.get("label", "Current-State"),
                description=cur_view.get("description", ""),
            ),
            future_view=ViewConfig(
                label=fut_view.get("label", "Future-State"),
                description=fut_view.get("description", ""),
            ),
        )
        tc.capabilities.append(cc)

    return tc


# ---------------------------------------------------------------------------
# Capability directory discovery
# ---------------------------------------------------------------------------
def find_capability_dir(tower_dir: Path, cap_id: str) -> Optional[Path]:
    """Search tower_dir recursively for a subfolder named exactly cap_id.

    Structure: towers/FPR/DS Provide Decision Support/DS-020/
    """
    for d in tower_dir.rglob(cap_id):
        if d.is_dir():
            return d
    return None


def discover_all_caps(tower_dir: Path, tower_cfg: "TowerConfig | None" = None) -> list[str]:
    """Find all capability dirs under a tower.

    Uses two strategies:
    1. Pattern match (XX-NNN) for standard cap IDs
    2. tower.yaml cap IDs for non-standard names (e.g. Order_to_Cash_IF)
    """
    caps = set()
    # Strategy 1: regex pattern match
    for d in tower_dir.rglob("*"):
        if d.is_dir() and _is_cap_id(d.name) and (d / "input").is_dir():
            caps.add(d.name)
    # Strategy 2: check tower.yaml cap IDs that don't match pattern
    if tower_cfg:
        for cc in tower_cfg.capabilities:
            if cc.cap_id and not _is_cap_id(cc.cap_id):
                # Search for matching dir
                for d in tower_dir.rglob(cc.cap_id):
                    if d.is_dir() and (d / "input").is_dir():
                        caps.add(cc.cap_id)
                        break
    return sorted(caps)


def _is_cap_id(name: str) -> bool:
    """Check if a directory name looks like a capability ID (e.g. DS-020, E2E-80)."""
    import re
    return bool(re.match(r"^[A-Z]+-\d+$", name, re.IGNORECASE))


# ---------------------------------------------------------------------------
# Find best flow CSV
# ---------------------------------------------------------------------------
def _find_flow_csv(input_data_dir: Path, release_id: str, flow_type: str) -> Optional[Path]:
    """Find the best flow CSV/Excel file.

    Priority: {Release}_{Type}.csv → {Release}_{Type}.xlsx → {Type}.csv → {Type}.xlsx
    Where Type is 'CurrentFlows' or 'FutureFlows'.
    """
    candidates = [
        f"{release_id}_{flow_type}.csv",
        f"{release_id}_{flow_type}.xlsx",
        f"{flow_type}.csv",
        f"{flow_type}.xlsx",
    ]
    for name in candidates:
        p = input_data_dir / name
        if p.exists():
            return p
    return None


# ---------------------------------------------------------------------------
# System inventory builder
# ---------------------------------------------------------------------------
def build_system_inventory(current: FlowSet, future: FlowSet,
                           iapm: IAPMLookup) -> list[SystemEntry]:
    """Build the §6 system inventory from both flow sets."""
    systems: dict[str, SystemEntry] = {}

    for flow_set in [current, future]:
        for hop in flow_set.hops:
            for sys_name, url in [(hop.source_system, hop.src_iapm_url),
                                  (hop.target_system, hop.tgt_iapm_url)]:
                if sys_name and sys_name not in systems:
                    app = iapm.resolve(sys_name, url)
                    systems[sys_name] = SystemEntry(
                        name=sys_name,
                        iapm_id=app.app_id if app else "-",
                        status=app.status if app else "N/A",
                    )

    return sorted(systems.values(), key=lambda s: s.name)


# ---------------------------------------------------------------------------
# Data Architecture extractors (from extended CSV columns 26-47)
# ---------------------------------------------------------------------------
@dataclass
class DataEntityRow:
    """For §3.1 Data Entities & Ownership table."""
    entity: str
    source: str
    target: str
    owner: str
    classification: str
    volume: str
    master_transaction: str


@dataclass
class DataLineageRow:
    """For §3.3 Data Lineage table."""
    source_sys: str
    source_obj: str
    target_sys: str
    target_obj: str
    notes: str


@dataclass
class IntegrationPatternRow:
    """For §4.6 Integration Patterns table."""
    pattern: str
    flow_chain: str
    middleware: str
    protocol: str
    auth: str


@dataclass
class TechPlatformRow:
    """For §5.1 Platform & Infrastructure table."""
    name: str
    type: str
    systems: str
    environment: str


def extract_data_entities(current: FlowSet, future: FlowSet) -> list[DataEntityRow]:
    """Extract unique data entities from extended CSV cols 26-31."""
    seen: dict[str, DataEntityRow] = {}
    for fs in [current, future]:
        for hop in fs.hops:
            if hop.data_entity and hop.data_entity not in seen:
                seen[hop.data_entity] = DataEntityRow(
                    entity=hop.data_entity,
                    source=hop.source_system,
                    target=hop.target_system,
                    owner=hop.data_owner or "TBD",
                    classification=hop.data_classification or "Internal",
                    volume=hop.data_volume or "TBD",
                    master_transaction=hop.master_transaction or "TBD",
                )
    return sorted(seen.values(), key=lambda x: x.entity)


def extract_data_lineage(current: FlowSet, future: FlowSet) -> list[DataLineageRow]:
    """Extract data lineage from extended CSV cols 44-45."""
    rows: list[DataLineageRow] = []
    seen: set[str] = set()
    for fs in [current, future]:
        for hop in fs.hops:
            if hop.source_schema_object or hop.target_schema_object:
                key = f"{hop.source_system}:{hop.source_schema_object}:{hop.target_system}:{hop.target_schema_object}"
                if key not in seen:
                    seen.add(key)
                    rows.append(DataLineageRow(
                        source_sys=hop.source_system,
                        source_obj=hop.source_schema_object or "—",
                        target_sys=hop.target_system,
                        target_obj=hop.target_schema_object or "—",
                        notes=hop.data_lineage_notes or "",
                    ))
    return rows


def extract_integration_patterns(current: FlowSet, future: FlowSet) -> list[IntegrationPatternRow]:
    """Extract integration patterns from extended CSV cols 32-37."""
    rows: list[IntegrationPatternRow] = []
    seen: set[str] = set()
    for fs in [current, future]:
        for hop in fs.hops:
            if hop.integration_pattern or hop.middleware_platform:
                key = f"{hop.flow_chain}:{hop.integration_pattern}:{hop.middleware_platform}"
                if key not in seen:
                    seen.add(key)
                    rows.append(IntegrationPatternRow(
                        pattern=hop.integration_pattern or "Point-to-Point",
                        flow_chain=hop.flow_chain,
                        middleware=hop.middleware_platform or "Direct",
                        protocol=hop.protocol or "—",
                        auth=hop.auth_method or "—",
                    ))
    return rows


def extract_tech_platforms(current: FlowSet, future: FlowSet) -> list[TechPlatformRow]:
    """Extract technology platforms from extended CSV cols 42-47."""
    plats: dict[str, TechPlatformRow] = {}
    for fs in [current, future]:
        for hop in fs.hops:
            for plat_name, sys_name, db_name, env in [
                (hop.source_tech_platform, hop.source_system, hop.source_db_platform, hop.environment_scope),
                (hop.target_tech_platform, hop.target_system, hop.target_db_platform, hop.environment_scope),
            ]:
                if plat_name and plat_name not in plats:
                    is_cloud = any(k in plat_name.lower() for k in ("saas", "aws", "azure", "gcp", "cloud"))
                    plats[plat_name] = TechPlatformRow(
                        name=plat_name,
                        type="Cloud / SaaS" if is_cloud else "On-Premise",
                        systems=sys_name,
                        environment=env or "DEV,QAS,PRD",
                    )
                elif plat_name and sys_name not in plats[plat_name].systems:
                    plats[plat_name].systems += f", {sys_name}"
    return sorted(plats.values(), key=lambda x: x.name)


# ---------------------------------------------------------------------------
# Single capability generation
# ---------------------------------------------------------------------------
_PAGE_BREAK = '<div style="page-break-before: always;"></div>'


def _ensure_blank_line_before_tables(text: str) -> str:
    """Ensure a blank line precedes every Markdown table.

    Jinja2's trim_blocks=True strips the newline after block tags ({% endif %},
    {% endfor %}), which can merge a preceding paragraph with the table's first
    row.  Python-Markdown's TableExtension requires a blank line before the table
    header for it to be parsed as a proper <table>.

    Also ensures a blank line AFTER a table's last row if followed by non-table
    Markdown content (e.g., **Change Summary**: ...).
    """
    lines = text.split('\n')
    result: list[str] = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        is_table_row = stripped.startswith('|')
        prev_stripped = result[-1].strip() if result else ''
        prev_is_table = prev_stripped.startswith('|')

        # Insert blank line before a table row if previous line is non-blank,
        # non-table, and not an HTML tag
        if is_table_row and not prev_is_table and prev_stripped and not prev_stripped.startswith('<'):
            result.append('')

        # Insert blank line after a table row if this line is non-table, non-blank,
        # and not an HTML tag
        if not is_table_row and prev_is_table and stripped and not stripped.startswith('<'):
            result.append('')

        result.append(line)
    return '\n'.join(result)


def _inject_page_footers(rendered: str, cap_id: str, cap_name: str) -> str:
    """Insert footer HTML before each page break.

    IMPORTANT: Does NOT wrap in <div class="page-section"> — that would
    break Python-Markdown processing (MD inside block-level HTML is treated
    as raw text).  The page-section wrapping is done later in gen_pdf.py
    during the HTML post-processing stage.
    """
    parts = rendered.split(_PAGE_BREAK)
    if len(parts) <= 1:
        return rendered
    title = f"{cap_id} — {cap_name}"
    result = []
    for i, part in enumerate(parts):
        page = i + 1
        footer = (
            f'\n<div class="page-footer">'
            f'<span>Page {page}</span>'
            f'<span><a href="#toc">\u2191 Back to TOC</a></span>'
            f'<span>{title}</span>'
            f'</div>\n'
        )
        result.append(part + footer)
        if i < len(parts) - 1:
            result.append(f'{_PAGE_BREAK}\n')
    return "".join(result)


def _inject_mermaid_live_links(rendered: str) -> str:
    """Add Mermaid Live Editor links to any mermaid block that doesn't already have one."""
    pattern = _re.compile(r"(```mermaid\n)(.*?)(```)", _re.DOTALL)
    # Pre-scan: find positions of all existing live link divs
    existing_divs = {m.start() for m in _re.finditer(r'mermaid\.live/edit', rendered)}

    def _add_link(match: _re.Match) -> str:
        full = match.group(0)
        end_pos = match.end()
        # Check if any existing mermaid.live link appears within 1000 chars after this block
        for div_pos in existing_divs:
            if end_pos <= div_pos <= end_pos + 1000:
                return full  # already has a live link

        mermaid_code = match.group(2)
        url = mermaid_live_url(mermaid_code)
        if not url:
            return full

        link_line = (
            f'\n\n<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;">'
            f'<a href="{url}" title="View full diagram">&#128065; View Diagram</a>'
            f'</div>\n'
        )
        return full + link_line

    return pattern.sub(_add_link, rendered)


def generate_capability(
    tower_dir: Path,
    cap_id: str,
    tower_cfg: TowerConfig,
    iapm: IAPMLookup,
    jinja_env: Environment,
    smartsheet: Optional[SmartsheetData] = None,
    dry_run: bool = False,
    render_svg: bool = False,
) -> Optional[str]:
    """Generate a Systems Architecture Document for one capability.

    Returns the output file path, or None if no flow CSVs found.
    """
    cap_dir = find_capability_dir(tower_dir, cap_id)
    if not cap_dir:
        print(f"  SKIP {cap_id}: directory not found under {tower_dir.name}")
        return None

    input_data = cap_dir / "input" / "data"
    if not input_data.is_dir():
        print(f"  SKIP {cap_id}: no input/data directory")
        return None

    # Find capability config from tower.yaml (or use defaults)
    cap_cfg = next((c for c in tower_cfg.capabilities if c.cap_id == cap_id), None)
    if not cap_cfg:
        cap_cfg = CapabilityConfig(cap_id=cap_id, name=cap_id)

    # Resolve capability name from multiple sources (BIC > Smartsheet > BPMN > L1)
    resolver = CapNameResolver(tower_dir, tower_cfg.shortcode)
    l1_dir_name = cap_dir.parent.name if cap_dir.parent.name != cap_id else ""
    bpmn_dir = cap_dir / "input" / "bpmn"
    cap_cfg.name = resolver.resolve(
        cap_id=cap_id,
        yaml_name=cap_cfg.name,
        l1_dir_name=l1_dir_name,
        bpmn_dir=bpmn_dir if bpmn_dir.exists() else None,
    )
    if not cap_cfg.l1 and l1_dir_name:
        cap_cfg.l1 = l1_dir_name

    # Locate flow files — prefer multi-tab xlsx over individual CSVs
    current_xlsx = find_xlsx_workbook(input_data, tower_cfg.release.release_id, "CurrentFlows")
    future_xlsx = find_xlsx_workbook(input_data, tower_cfg.release.release_id, "FutureFlows")
    current_csv = _find_flow_csv(input_data, tower_cfg.release.release_id, "CurrentFlows")
    future_csv = _find_flow_csv(input_data, tower_cfg.release.release_id, "FutureFlows")

    if not current_csv and not future_csv and not current_xlsx and not future_xlsx:
        print(f"  SKIP {cap_id}: no CurrentFlows or FutureFlows found")
        return None

    # Load data — xlsx workbooks contain flows + context + business processes in tabs
    current_wb_data = None
    future_wb_data = None
    if current_xlsx:
        current_wb_data = load_xlsx_workbook(str(current_xlsx), cap_cfg.current_view.label)
        print(f"    XLSX: loaded {current_xlsx.name} (flows={current_wb_data.has_flows}, ctx={current_wb_data.has_context}, biz={current_wb_data.has_processes})")
    if future_xlsx:
        future_wb_data = load_xlsx_workbook(str(future_xlsx), cap_cfg.future_view.label)
        print(f"    XLSX: loaded {future_xlsx.name} (flows={future_wb_data.has_flows}, ctx={future_wb_data.has_context}, biz={future_wb_data.has_processes})")

    # Parse flows — xlsx takes precedence, fall back to CSV
    if current_wb_data and current_wb_data.has_flows:
        current_flows = current_wb_data.flows
    elif current_csv:
        current_flows = parse_flow_csv(str(current_csv), cap_cfg.current_view.label)
    else:
        current_flows = FlowSet(label=cap_cfg.current_view.label, source_file="")

    if future_wb_data and future_wb_data.has_flows:
        future_flows = future_wb_data.flows
    elif future_csv:
        future_flows = parse_flow_csv(str(future_csv), cap_cfg.future_view.label)
    else:
        future_flows = FlowSet(label=cap_cfg.future_view.label, source_file="")

    # Build Mermaid diagrams — lane-grouped (original style)
    prefix_cur = cap_id.replace("-", "") + "C"
    prefix_fut = cap_id.replace("-", "") + "F"
    current_mermaid = build_mermaid(current_flows, iapm, prefix_cur) if current_flows.hops else ""
    future_mermaid = build_mermaid(future_flows, iapm, prefix_fut) if future_flows.hops else ""

    # Build ArchiMate-inspired diagrams (3-layer: App + Tech)
    current_archimate_mermaid = build_archimate_mermaid(current_flows, iapm, prefix_cur) if current_flows.hops else ""
    future_archimate_mermaid = build_archimate_mermaid(future_flows, iapm, prefix_fut) if future_flows.hops else ""

    # Data flow diagram (Data + App layers only) — kept for backward-compat
    data_flow_mermaid = build_data_flow_mermaid(future_flows, iapm, prefix_fut + "D") if future_flows.hops else ""

    # Data Architecture diagrams — DB-to-DB flows (current + future)
    current_data_arch_mermaid = build_data_arch_mermaid(current_flows, iapm, prefix_cur + "DA") if current_flows.hops else ""
    future_data_arch_mermaid = build_data_arch_mermaid(future_flows, iapm, prefix_fut + "DA") if future_flows.hops else ""

    # Platform Architecture diagrams (current + future)
    current_platform_mermaid = build_platform_arch_mermaid(current_flows, iapm, prefix_cur + "PL") if current_flows.hops else ""
    future_platform_mermaid = build_platform_arch_mermaid(future_flows, iapm, prefix_fut + "PL") if future_flows.hops else ""

    # ── Release-specific flows ──────────────────────────────────
    # When a specific release is active (e.g. R3), look for Rx_CurrentFlows / Rx_FutureFlows
    # These are separate from the universal flows and provide release-scoped detail
    rel_id = tower_cfg.release.name  # "R3" when --release R3, "R1 – R5" otherwise
    has_release_flows = False
    rel_current_mermaid = ""
    rel_future_mermaid = ""
    rel_current_archimate = ""
    rel_future_archimate = ""
    rel_current_flows = FlowSet(label="", source_file="")
    rel_future_flows = FlowSet(label="", source_file="")
    rel_diff = None

    # Only look for release-specific files if a single release is active
    if rel_id and "–" not in rel_id and "-" not in rel_id:
        rel_cur_xlsx = find_xlsx_workbook(input_data, rel_id, "CurrentFlows")
        rel_fut_xlsx = find_xlsx_workbook(input_data, rel_id, "FutureFlows")
        rel_cur_csv = _find_flow_csv(input_data, rel_id, "CurrentFlows")
        rel_fut_csv = _find_flow_csv(input_data, rel_id, "FutureFlows")

        # Only proceed if we found release-specific files (not the universal fallback)
        rel_cur_file = rel_cur_xlsx or rel_cur_csv
        rel_fut_file = rel_fut_xlsx or rel_fut_csv
        # Check that the file actually has the release prefix in its name
        def _is_release_specific(p: Optional[Path]) -> bool:
            return p is not None and p.name.startswith(rel_id)

        if _is_release_specific(rel_cur_file) or _is_release_specific(rel_fut_file):
            has_release_flows = True
            rel_label_cur = f"{rel_id} Current State"
            rel_label_fut = f"{rel_id} Future State"
            rprefix_cur = cap_id.replace("-", "") + "RC"
            rprefix_fut = cap_id.replace("-", "") + "RF"

            # Load release-specific flows
            if rel_cur_xlsx and _is_release_specific(rel_cur_xlsx):
                rel_cur_wb = load_xlsx_workbook(str(rel_cur_xlsx), rel_label_cur)
                rel_current_flows = rel_cur_wb.flows if rel_cur_wb.has_flows else FlowSet(label=rel_label_cur, source_file="")
                print(f"    REL-XLSX: loaded {rel_cur_xlsx.name}")
            elif rel_cur_csv and _is_release_specific(rel_cur_csv):
                rel_current_flows = parse_flow_csv(str(rel_cur_csv), rel_label_cur)
                print(f"    REL-CSV: loaded {rel_cur_csv.name}")

            if rel_fut_xlsx and _is_release_specific(rel_fut_xlsx):
                rel_fut_wb = load_xlsx_workbook(str(rel_fut_xlsx), rel_label_fut)
                rel_future_flows = rel_fut_wb.flows if rel_fut_wb.has_flows else FlowSet(label=rel_label_fut, source_file="")
                print(f"    REL-XLSX: loaded {rel_fut_xlsx.name}")
            elif rel_fut_csv and _is_release_specific(rel_fut_csv):
                rel_future_flows = parse_flow_csv(str(rel_fut_csv), rel_label_fut)
                print(f"    REL-CSV: loaded {rel_fut_csv.name}")

            # Build diagrams for release-specific flows
            if rel_current_flows.hops:
                rel_current_mermaid = build_mermaid(rel_current_flows, iapm, rprefix_cur)
                rel_current_archimate = build_archimate_mermaid(rel_current_flows, iapm, rprefix_cur)
            if rel_future_flows.hops:
                rel_future_mermaid = build_mermaid(rel_future_flows, iapm, rprefix_fut)
                rel_future_archimate = build_archimate_mermaid(rel_future_flows, iapm, rprefix_fut)

            # Release-specific diff
            if rel_current_flows.hops or rel_future_flows.hops:
                rel_diff = diff_flows(rel_current_flows, rel_future_flows)

    # Diff
    diff = diff_flows(current_flows, future_flows)

    # System inventory
    inventory = build_system_inventory(current_flows, future_flows, iapm)

    # Count statuses
    deployed = sum(1 for s in inventory if s.status == "Deployed")
    developing = sum(1 for s in inventory if s.status in ("Developing", "Planning"))
    eol = sum(1 for s in inventory if s.status in ("End of Life", "Canceled"))
    no_match = sum(1 for s in inventory if s.status == "N/A")

    # Extract extended architecture data (from cols 26-47)
    data_entities = extract_data_entities(current_flows, future_flows)
    data_lineage = extract_data_lineage(current_flows, future_flows)
    integration_patterns = extract_integration_patterns(current_flows, future_flows)
    tech_platforms = extract_tech_platforms(current_flows, future_flows)

    # Load supplementary context — merge xlsx tabs with CSV fallback
    # Priority: xlsx embedded tabs > individual CSVs in input/data/
    ctx = CapabilityContext()
    xlsx_ctx_sources = [wb.context for wb in [current_wb_data, future_wb_data] if wb]
    if xlsx_ctx_sources:
        # Merge context from xlsx workbook(s) — future overrides current if both present
        for wb_ctx in xlsx_ctx_sources:
            if wb_ctx.has_drivers:
                ctx.business_drivers = wb_ctx.business_drivers
            if wb_ctx.has_criteria:
                ctx.success_criteria = wb_ctx.success_criteria
            if wb_ctx.has_nfrs:
                ctx.nfrs = wb_ctx.nfrs
            if wb_ctx.has_security:
                ctx.security_controls = wb_ctx.security_controls
            if wb_ctx.has_sap_status:
                ctx.sap_dev_status = wb_ctx.sap_dev_status
            if wb_ctx.has_recommendations:
                ctx.recommendations = wb_ctx.recommendations
    if not ctx.has_drivers and not ctx.has_criteria:
        # Fall back to individual CSVs
        ctx = load_capability_context(input_data)

    # Load BPMN process diagrams (Business Architecture §3)
    # Priority: BPMN XML files > xlsx "Business Architecture" tab > ProcessFlows.csv
    bpmn_dir = cap_dir / "input" / "bpmn"
    bpmn_processes = load_capability_bpmns(bpmn_dir)
    if not bpmn_processes:
        # Try xlsx "Business Architecture" tabs
        for wb_data in [current_wb_data, future_wb_data]:
            if wb_data and wb_data.has_processes:
                bpmn_processes = wb_data.business_processes
                print(f"    XLSX-BIZ: {len(bpmn_processes)} processes from {Path(wb_data.source_file).name}")
                break
    bpmn_mermaids = [bpmn_to_mermaid(proc, _bpmn_direction(proc)) for proc in bpmn_processes]
    bpmn_inventory_table = build_process_inventory_table(bpmn_processes)
    if bpmn_processes and bpmn_dir.is_dir():
        print(f"    BPMN: {len(bpmn_processes)} processes loaded from {bpmn_dir.name}/")

    # Render template (TOGAF BDAT)
    template = jinja_env.get_template(BDAT_TEMPLATE)
    rendered = template.render(
        banner_src=_BANNER_DATA_URI,
        cap_id=cap_id,
        cap_name=cap_cfg.name,
        tower_name=tower_cfg.name,
        tower_short=tower_cfg.shortcode,
        l1_process=cap_cfg.l1 or "",
        release_name=tower_cfg.release.name,
        gen_date=date.today().strftime("%B %Y"),
        # View labels
        current_label=cap_cfg.current_view.label,
        future_label=cap_cfg.future_view.label,
        current_desc=cap_cfg.current_view.description,
        future_desc=cap_cfg.future_view.description,
        current_csv_name=current_csv.name if current_csv else "",
        future_csv_name=future_csv.name if future_csv else "",
        # Flow data
        current_flows=current_flows,
        future_flows=future_flows,
        # Mermaid diagrams — both styles
        current_mermaid=current_mermaid,
        future_mermaid=future_mermaid,
        current_archimate_mermaid=current_archimate_mermaid,
        future_archimate_mermaid=future_archimate_mermaid,
        data_flow_mermaid=data_flow_mermaid,
        # Data Architecture diagrams — DB-to-DB (§4.2)
        current_data_arch_mermaid=current_data_arch_mermaid,
        future_data_arch_mermaid=future_data_arch_mermaid,
        # Platform Architecture diagrams (§6.1)
        current_platform_mermaid=current_platform_mermaid,
        future_platform_mermaid=future_platform_mermaid,
        # Diff
        diff=diff,
        # System inventory
        system_inventory=inventory,
        total_systems=len(inventory),
        deployed_count=deployed,
        developing_count=developing,
        eol_count=eol,
        no_match_count=no_match,
        # Business Architecture (§3)
        bpmn_processes=bpmn_processes,
        bpmn_mermaids=bpmn_mermaids,
        bpmn_inventory_table=bpmn_inventory_table,
        # Data Architecture (§4)
        data_entities=data_entities,
        data_lineage=data_lineage,
        # Application Architecture (§5)
        integration_patterns=integration_patterns,
        # Technology Architecture (§6)
        tech_platforms=tech_platforms,
        # Smartsheet data — RICEFW, RAID, Timeline (§5.5, §7)
        ricefw=smartsheet,
        # Supplementary context CSVs (§2.2, §2.3, §5.2, §5.3, §5.4, §6.3)
        ctx=ctx,
        # Release-specific flows (§4.x, §5.x) — only when --release is active
        has_release_flows=has_release_flows,
        release_id=rel_id if has_release_flows else "",
        rel_current_flows=rel_current_flows,
        rel_future_flows=rel_future_flows,
        rel_current_mermaid=rel_current_mermaid,
        rel_future_mermaid=rel_future_mermaid,
        rel_current_archimate=rel_current_archimate,
        rel_future_archimate=rel_future_archimate,
        rel_diff=rel_diff,
    )

    if dry_run:
        print(f"  DRY RUN {cap_id}: would write {len(rendered)} chars")
        return None

    # Fix Jinja2 trim_blocks side-effect: ensure blank lines before tables
    # trim_blocks=True strips the newline after {% endif %}/{% endfor %}, which
    # can merge a paragraph with the next table row. Python-Markdown requires a
    # blank line before a table for the TableExtension to process it.
    rendered = _ensure_blank_line_before_tables(rendered)

    # Inject page footers (page number, back-to-TOC link, doc title)
    rendered = _inject_page_footers(rendered, cap_id, cap_cfg.name)

    # Write output
    output_dir = cap_dir / "output" / "docs" / "systems-architecture"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Pre-render mermaid diagrams to SVG + inject live editor links
    if render_svg:
        rendered = _render_mermaid_svgs(rendered, output_dir, cap_id)

    # For any mermaid blocks that didn't get SVG links, add live editor links only
    rendered = _inject_mermaid_live_links(rendered)

    output_path = output_dir / f"{cap_id}-Architecture.md"
    output_path.write_text(rendered, encoding="utf-8")
    print(f"  DONE {cap_id}: {output_path} ({len(rendered):,} chars)")
    return str(output_path)


# ---------------------------------------------------------------------------
# Tower-level generation
# ---------------------------------------------------------------------------
def generate_tower(tower_short: str, iapm: IAPMLookup, jinja_env: Environment,
                   ss_loader: Optional[SmartsheetLoader] = None,
                   cap_filter: Optional[str] = None, dry_run: bool = False,
                   render_svg: bool = False,
                   release_override: str = "R1 \u2013 R5") -> list[str]:
    """Generate SADs for all (or filtered) capabilities in a tower."""
    tower_dir = TOWERS_DIR / tower_short
    if not tower_dir.is_dir():
        # Try case-insensitive search
        for d in TOWERS_DIR.iterdir():
            if d.is_dir() and d.name.upper() == tower_short.upper():
                tower_dir = d
                break
        else:
            print(f"Tower directory not found: {tower_short}")
            return []

    tower_cfg = load_tower_config(tower_dir)
    # Override release label if a specific release was requested
    if release_override and release_override != "R1 \u2013 R5":
        tower_cfg.release.name = release_override
        tower_cfg.release.release_id = release_override  # e.g. "R3" → finds R3_CurrentFlows.xlsx
    print(f"\n{'='*60}")
    print(f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) \u2014 {tower_cfg.release.name}")
    print(f"{'='*60}")

    # Load tower-level Smartsheet data once
    smartsheet: Optional[SmartsheetData] = None
    if ss_loader:
        smartsheet = ss_loader.get_tower_data(tower_cfg.shortcode)
        if smartsheet:
            print(f"  Smartsheet: {len(smartsheet.ricefw)} RICEFW objects, {len(smartsheet.raid)} RAID entries")

    if cap_filter:
        cap_ids = [cap_filter]
    else:
        cap_ids = discover_all_caps(tower_dir, tower_cfg)

    print(f"Capabilities found: {len(cap_ids)}")
    outputs = []
    for cid in cap_ids:
        # Resolve capability name from tower.yaml for Smartsheet matching
        cap_cfg = next((c for c in tower_cfg.capabilities if c.cap_id == cid), None)
        cap_name_for_match = cap_cfg.name if cap_cfg else cid

        # Try capability-level Smartsheet data first; fall back to tower-level
        cap_ss = None
        if ss_loader:
            cap_ss = ss_loader.get_capability_data(
                tower_cfg.shortcode, cap_name=cap_name_for_match, cap_id=cid)
        if not cap_ss or not cap_ss.ricefw:
            cap_ss = smartsheet

        result = generate_capability(tower_dir, cid, tower_cfg, iapm, jinja_env,
                                     smartsheet=cap_ss, dry_run=dry_run,
                                     render_svg=render_svg)
        if result:
            outputs.append(result)

    print(f"\nGenerated: {len(outputs)} / {len(cap_ids)} capabilities")
    return outputs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Systems Architecture Documents")
    parser.add_argument("--tower", type=str, help="Tower shortcode (e.g. FPR)")
    parser.add_argument("--cap", type=str, help="Single capability ID (e.g. DS-020)")
    parser.add_argument("--all", action="store_true", help="Generate for all towers")
    parser.add_argument("--release", type=str, help="Filter by release (e.g. R3, R4)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't write files")
    parser.add_argument("--svg", action="store_true", help="Pre-render mermaid diagrams to SVG files (slower)")
    parser.add_argument("--iapm-csv", type=str, default=str(IAPM_CSV),
                        help="Path to IAPM_All_Solutions.csv")
    parser.add_argument("--tracker-csv", type=str, default=str(OBJECT_TRACKER_CSV),
                        help="Path to s4_r3_object_tracker.csv")
    args = parser.parse_args()

    if not args.tower and not args.all:
        parser.error("Specify --tower SHORTCODE or --all")

    # Load IAPM lookup
    print("Loading IAPM lookup...")
    iapm = IAPMLookup()
    if Path(args.iapm_csv).exists():
        iapm.load_csv(args.iapm_csv)
        print(f"  Loaded {iapm.app_count:,} applications")
    else:
        print(f"  WARNING: IAPM CSV not found at {args.iapm_csv} — status lookups disabled")

    # Load Smartsheet Object Tracker
    ss_loader: Optional[SmartsheetLoader] = None
    tracker_path = Path(args.tracker_csv)
    if tracker_path.exists():
        print("Loading Smartsheet Object Tracker...")
        ss_loader = SmartsheetLoader()
        ss_loader.load_csv(str(tracker_path))
        print(f"  Loaded {len(ss_loader._rows):,} tracker rows")
        if args.release:
            removed = ss_loader.filter_by_release(args.release)
            print(f"  Filtered to {len(ss_loader._rows):,} rows for release {args.release} ({removed:,} excluded)")
    else:
        print(f"  WARNING: Object Tracker not found at {tracker_path} — RICEFW/RAID disabled")

    release_label = args.release or "R1 \u2013 R5"

    # Setup Jinja2
    jinja_env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    def _tablecell(value: str, max_len: int = 80) -> str:
        """Sanitize a value for use inside a Markdown table cell."""
        if not value:
            return ""
        s = str(value).replace("\r\n", " ").replace("\n", " ").replace("|", "/")
        s = " ".join(s.split())  # collapse whitespace
        if len(s) > max_len:
            s = s[:max_len - 3] + "..."
        return s

    jinja_env.filters["tc"] = _tablecell

    def _phase_cell(date_str: str, pct_str: str) -> str:
        """Format a phase cell combining date and completion %."""
        if not date_str:
            return "\u2014"
        try:
            dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            short = dt.strftime("%b-%y")
        except ValueError:
            short = date_str.strip()
        try:
            pct = float(pct_str)
            p = f"{int(pct * 100)}%"
        except (ValueError, TypeError):
            p = ""
        return f"{short} ({p})" if p else short

    jinja_env.globals["phase_cell"] = _phase_cell

    if args.all:
        towers = sorted(d.name for d in TOWERS_DIR.iterdir() if d.is_dir())
        all_outputs = []
        for t in towers:
            outputs = generate_tower(t, iapm, jinja_env, ss_loader=ss_loader,
                                    dry_run=args.dry_run, render_svg=args.svg,
                                    release_override=release_label)
            all_outputs.extend(outputs)
        print(f"\n{'='*60}")
        print(f"TOTAL: {len(all_outputs)} documents generated across {len(towers)} towers")
    else:
        generate_tower(args.tower, iapm, jinja_env, ss_loader=ss_loader,
                       cap_filter=args.cap, dry_run=args.dry_run,
                       render_svg=args.svg, release_override=release_label)


if __name__ == "__main__":
    main()
