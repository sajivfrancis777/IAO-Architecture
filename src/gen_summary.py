"""gen_summary.py — Generate L0 / L1 / Program Summary Roll-Up Documents.

Aggregates capability-level (L2) flow data into higher-level summary views:
  L1: Per process group within a tower (aggregates all L2 capabilities)
  L0: Per tower (aggregates all L1 process groups)
  Program: Program-level (aggregates all towers) — not an L-level

Usage:
    python -m src.gen_summary --tower FPR --level L1
    python -m src.gen_summary --tower FPR --level L0
    python -m src.gen_summary --level Program
    python -m src.gen_summary --all
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.csv_parser import FlowSet, FlowHop, parse_flow_csv
from src.iapm_lookup import IAPMLookup
from src.doc_format import DocFormatter, PAGE_BREAK
from src.gen_systems_arch import (
    WORKSPACE, TOWERS_DIR, IAPM_CSV,
    load_tower_config, find_capability_dir, TowerConfig,
    build_system_inventory, mermaid_live_url,
    extract_data_flows, extract_integration_patterns, extract_tech_platforms,
    DataFlowRow, IntegrationPatternRow, TechPlatformRow,
    _inject_mermaid_live_links,
)
from src.xlsx_loader import load_workbook as load_xlsx_workbook, find_workbook as find_xlsx_workbook
from src.mermaid_builder import (
    ARCHIMATE_CLASSDEFS, LAYER_STYLES, EMOJI,
    build_data_arch_mermaid, build_platform_arch_mermaid,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CONFIG_DIR = WORKSPACE / "config"
CAPABILITY_MASTER = CONFIG_DIR / "capability_master.yaml"


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class SystemEdge:
    """An aggregated edge between two systems across multiple capabilities."""
    source: str
    target: str
    interface_techs: set = field(default_factory=set)
    capabilities: set = field(default_factory=set)
    hop_count: int = 0


@dataclass
class SummaryData:
    """Aggregated data for a summary level."""
    label: str
    scope: str  # "L0", "L1", "L2"
    all_flows: list[FlowSet] = field(default_factory=list)
    systems: set = field(default_factory=set)
    edges: dict = field(default_factory=dict)  # (src, tgt) -> SystemEdge
    capabilities: list[dict] = field(default_factory=list)   # [{id, name, l1, hop_count}]
    total_hops: int = 0
    # Aggregated D/A/T data across capabilities
    data_flows: list[DataFlowRow] = field(default_factory=list)
    integration_patterns: list[IntegrationPatternRow] = field(default_factory=list)
    tech_platforms: list[TechPlatformRow] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Flow aggregation
# ---------------------------------------------------------------------------
def _collect_capability_flows(
    tower_dir: Path,
    tower_cfg: TowerConfig,
    cap_id: str,
) -> tuple[Optional[FlowSet], Optional[FlowSet]]:
    """Load current and future FlowSets for a capability."""
    cap_dir = find_capability_dir(tower_dir, cap_id)
    if not cap_dir:
        return None, None

    input_data = cap_dir / "input" / "data"
    if not input_data.is_dir():
        return None, None

    release_id = tower_cfg.release.release_id

    # Find capability config from tower.yaml (or use defaults)
    cap_cfg = next((c for c in tower_cfg.capabilities if c.cap_id == cap_id), None)
    cur_label = cap_cfg.current_view.label if cap_cfg else "Current-State"
    fut_label = cap_cfg.future_view.label if cap_cfg else "Future-State"

    # xlsx takes precedence, fall back to CSV
    current_xlsx = find_xlsx_workbook(input_data, release_id, "CurrentFlows")
    future_xlsx = find_xlsx_workbook(input_data, release_id, "FutureFlows")

    current = None
    future = None

    if current_xlsx:
        wb = load_xlsx_workbook(str(current_xlsx), cur_label)
        if wb.has_flows:
            current = wb.flows
    if not current:
        csv_path = _find_flow_csv(input_data, release_id, "CurrentFlows")
        if csv_path:
            current = parse_flow_csv(str(csv_path), cur_label)

    if future_xlsx:
        wb = load_xlsx_workbook(str(future_xlsx), fut_label)
        if wb.has_flows:
            future = wb.flows
    if not future:
        csv_path = _find_flow_csv(input_data, release_id, "FutureFlows")
        if csv_path:
            future = parse_flow_csv(str(csv_path), fut_label)

    return current, future


def _find_flow_csv(data_dir: Path, release_id: str, stem: str) -> Optional[Path]:
    """Locate a flow CSV, trying release-prefixed then plain."""
    for prefix in [f"{release_id}_", ""]:
        candidate = data_dir / f"{prefix}{stem}.csv"
        if candidate.exists():
            return candidate
    return None


# ---------------------------------------------------------------------------
# Multi-release helpers
# ---------------------------------------------------------------------------
def _discover_releases(cap_dir: Path) -> list[str]:
    """Discover available release IDs (R1, R2, R3, ...) for a capability."""
    input_data = cap_dir / "input" / "data"
    if not input_data.is_dir():
        return []
    releases: set[str] = set()
    for p in input_data.iterdir():
        # Match R1_FutureFlows.xlsx, R2_CurrentFlows.csv, etc.
        m = re.match(r'^(R\d+)_(?:Current|Future)Flows\.(?:xlsx|csv)$', p.name)
        if m:
            releases.add(m.group(1))
    return sorted(releases, key=lambda r: int(r[1:]))


def _collect_release_futures(
    tower_dir: Path,
    tower_cfg: TowerConfig,
    cap_ids: list[str],
) -> dict[str, SummaryData]:
    """For each discovered release, load FutureFlows across all given capabilities.

    Returns {release_id: SummaryData} with only future-state data per release.
    """
    # Discover releases available across all capabilities
    all_releases: set[str] = set()
    for cid in cap_ids:
        cap_dir = find_capability_dir(tower_dir, cid)
        if cap_dir:
            all_releases.update(_discover_releases(cap_dir))

    if len(all_releases) < 2:
        return {}  # Nothing to diff

    releases = sorted(all_releases, key=lambda r: int(r[1:]))
    result: dict[str, SummaryData] = {}

    for rel in releases:
        flows = []
        for cid in cap_ids:
            cap_dir = find_capability_dir(tower_dir, cid)
            if not cap_dir:
                continue
            input_data = cap_dir / "input" / "data"
            if not input_data.is_dir():
                continue

            # Try xlsx first, then csv
            fut_xlsx = find_xlsx_workbook(input_data, rel, "FutureFlows")
            if fut_xlsx:
                wb = load_xlsx_workbook(str(fut_xlsx), f"R{rel} Future")
                if wb.has_flows:
                    flows.append(wb.flows)
            else:
                csv_path = _find_flow_csv(input_data, rel, "FutureFlows")
                if csv_path:
                    flows.append(parse_flow_csv(str(csv_path), f"{rel} Future"))

        if flows:
            result[rel] = _aggregate_flows(flows)

    return result


@dataclass
class ReleaseDelta:
    """Delta between two adjacent releases."""
    from_rel: str
    to_rel: str
    new_apps: set = field(default_factory=set)
    retired_apps: set = field(default_factory=set)
    new_dbs: set = field(default_factory=set)
    retired_dbs: set = field(default_factory=set)
    new_platforms: set = field(default_factory=set)
    retired_platforms: set = field(default_factory=set)


def _compute_release_deltas(release_data: dict[str, SummaryData]) -> list[ReleaseDelta]:
    """Compare adjacent releases and compute app/DB/platform deltas."""
    releases = sorted(release_data.keys(), key=lambda r: int(r[1:]))
    deltas = []

    def _extract_dbs(summary: SummaryData) -> set[str]:
        dbs = set()
        for fs in summary.all_flows:
            for hop in fs.hops:
                if hop.source_db_platform:
                    dbs.add(hop.source_db_platform)
                if hop.target_db_platform:
                    dbs.add(hop.target_db_platform)
        return dbs

    def _extract_platforms(summary: SummaryData) -> set[str]:
        plats = set()
        for fs in summary.all_flows:
            for hop in fs.hops:
                if hop.source_tech_platform:
                    plats.add(hop.source_tech_platform)
                if hop.target_tech_platform:
                    plats.add(hop.target_tech_platform)
        return plats

    for i in range(len(releases) - 1):
        prev_rel = releases[i]
        next_rel = releases[i + 1]
        prev = release_data[prev_rel]
        nxt = release_data[next_rel]

        prev_dbs = _extract_dbs(prev)
        next_dbs = _extract_dbs(nxt)
        prev_plats = _extract_platforms(prev)
        next_plats = _extract_platforms(nxt)

        delta = ReleaseDelta(
            from_rel=prev_rel,
            to_rel=next_rel,
            new_apps=nxt.systems - prev.systems,
            retired_apps=prev.systems - nxt.systems,
            new_dbs=next_dbs - prev_dbs,
            retired_dbs=prev_dbs - next_dbs,
            new_platforms=next_plats - prev_plats,
            retired_platforms=prev_plats - next_plats,
        )
        deltas.append(delta)

    return deltas


def _aggregate_flows(flows_list: list[FlowSet]) -> SummaryData:
    """Merge multiple FlowSets into aggregated system-level edges + extended D/A/T data."""
    summary = SummaryData(label="", scope="")

    for fs in flows_list:
        if not fs or not fs.hops:
            continue
        summary.all_flows.append(fs)
        for hop in fs.hops:
            src = hop.source_system.strip()
            tgt = hop.target_system.strip()
            if not src or not tgt:
                continue
            summary.systems.add(src)
            summary.systems.add(tgt)
            key = (src, tgt)
            if key not in summary.edges:
                summary.edges[key] = SystemEdge(source=src, target=tgt)
            edge = summary.edges[key]
            edge.hop_count += 1
            if hop.interface_tech:
                edge.interface_techs.add(hop.interface_tech.strip())
            edge.capabilities.add(hop.flow_chain.split("-")[0] if "-" in hop.flow_chain else hop.flow_chain)
            summary.total_hops += 1

    # Aggregate extended data/tech columns across all FlowSets.
    # Build a merged "all hops" FlowSet for the extractors.
    merged = FlowSet(label="merged", source_file="")
    for fs in summary.all_flows:
        merged.hops.extend(fs.hops)
    empty = FlowSet(label="empty", source_file="")

    summary.data_flows = extract_data_flows(merged, empty)
    summary.integration_patterns = extract_integration_patterns(merged, empty)
    summary.tech_platforms = extract_tech_platforms(merged, empty)

    return summary


# ---------------------------------------------------------------------------
# Summary Mermaid diagram builders
# ---------------------------------------------------------------------------
def _safe_id(name: str) -> str:
    """Create a safe Mermaid node ID from a system name."""
    return re.sub(r'[^a-zA-Z0-9]', '_', name)


def build_summary_integration_map(summary: SummaryData, prefix: str = "S") -> str:
    """Build a system integration map showing all systems and their connections.

    This is a high-level view: each system is a node, each unique connection
    is an edge labeled with interface technologies and hop count.
    """
    if not summary.edges:
        return ""

    lines = ["graph LR"]

    # Collect all systems and assign node IDs
    node_ids = {}
    for sys_name in sorted(summary.systems):
        nid = f"{prefix}_{_safe_id(sys_name)}"
        node_ids[sys_name] = nid
        lines.append(f'    {nid}["{EMOJI.get("app", "📦")} {sys_name}"]')

    lines.append("")

    # Add edges with labels
    for (src, tgt), edge in sorted(summary.edges.items()):
        src_id = node_ids.get(src, _safe_id(src))
        tgt_id = node_ids.get(tgt, _safe_id(tgt))
        # Label: interface tech(s) + hop count
        techs = sorted(edge.interface_techs - {""})
        label_parts = []
        if techs:
            label_parts.append(" / ".join(techs[:3]))  # max 3 techs
        label_parts.append(f"{edge.hop_count} flow{'s' if edge.hop_count > 1 else ''}")
        label = " | ".join(label_parts)
        lines.append(f'    {src_id} -->|"{label}"| {tgt_id}')

    return "\n".join(lines)


def build_summary_archimate(summary: SummaryData, iapm: IAPMLookup, prefix: str = "SA") -> str:
    """Build an ArchiMate-inspired summary diagram with Application + Technology layers.

    Groups systems by IAPM status and shows connections between them.
    """
    if not summary.edges:
        return ""

    lines = ["graph TB"]
    lines.append(ARCHIMATE_CLASSDEFS)
    lines.append("")

    # Classify systems
    apps = {}  # name -> (status, node_id)
    for sys_name in sorted(summary.systems):
        nid = f"{prefix}_{_safe_id(sys_name)}"
        app = iapm.resolve(sys_name) if iapm else None
        status = app.status_label if app else "N/A"
        apps[sys_name] = (status, nid)

    # Application Layer subgraph
    lines.append(f'    subgraph AL["📦 Application Layer — Systems Integration"]')
    lines.append(f'        direction LR')
    for sys_name, (status, nid) in apps.items():
        emoji = EMOJI.get("eol", "⛔") if status in ("End of Life", "Canceled") else EMOJI.get("app", "📦")
        lines.append(f'        {nid}["{emoji} {sys_name}"]')
    lines.append(f'    end')
    lines.append("")

    # Edges
    for (src, tgt), edge in sorted(summary.edges.items()):
        src_id = apps.get(src, ("", _safe_id(src)))[1]
        tgt_id = apps.get(tgt, ("", _safe_id(tgt)))[1]
        techs = sorted(edge.interface_techs - {""})
        label = " / ".join(techs[:2]) if techs else f"{edge.hop_count}×"
        lines.append(f'    {src_id} -->|"{label}"| {tgt_id}')

    lines.append("")

    # Apply classes based on status
    for sys_name, (status, nid) in apps.items():
        if status in ("End of Life", "Canceled"):
            lines.append(f"    class {nid} eol")
        elif status in ("Developing", "Planning"):
            lines.append(f"    class {nid} middleware")
        else:
            lines.append(f"    class {nid} app")

    lines.append(LAYER_STYLES)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Summary document renderer
# ---------------------------------------------------------------------------
def _render_summary_doc(
    level: str,
    title: str,
    scope_label: str,
    current_summary: SummaryData,
    future_summary: SummaryData,
    iapm: IAPMLookup,
    capabilities_info: list[dict],
    tower_name: str = "",
    tower_short: str = "",
    l1_group: str = "",
    release_deltas: list[ReleaseDelta] | None = None,
    output_filepath: Path | None = None,
) -> str:
    """Render a lean summary Markdown document — diagrams only, links to L2 for detail."""
    fmt = DocFormatter(
        doc_type=f"{level} Architecture Summary",
        subtitle="TOGAF BDAT — Aggregated Architecture View",
    )

    md = fmt.title_page(
        title=title,
        context_lines=[scope_label],
        output_filepath=output_filepath,
    )

    # ── Table of Contents ────────────────────────────────────────
    has_release_diff = bool(release_deltas)
    sections = [
        {"number": "1", "title": "Executive Summary", "level": 1},
        {"number": "2", "title": "Capability Inventory", "level": 1},
        {"number": "3", "title": "Current-State Architecture", "level": 1},
        {"number": "3.1", "title": "Application Architecture", "level": 2},
        {"number": "3.2", "title": "Data Architecture", "level": 2},
        {"number": "3.3", "title": "Technology Architecture", "level": 2},
        {"number": "4", "title": "Future-State Architecture", "level": 1},
        {"number": "4.1", "title": "Application Architecture", "level": 2},
        {"number": "4.2", "title": "Data Architecture", "level": 2},
        {"number": "4.3", "title": "Technology Architecture", "level": 2},
        {"number": "5", "title": "Transformation Analysis", "level": 1},
        {"number": "5.1", "title": "System Landscape Changes", "level": 2},
        {"number": "5.2", "title": "Integration Complexity Delta", "level": 2},
    ]
    if has_release_diff:
        sections.append({"number": "5.3", "title": "Release-over-Release Changes", "level": 2})
    sections.append({"number": "6", "title": "Capability Detail Reference", "level": 1})
    md += fmt.toc(sections)

    # ── Metrics ──────────────────────────────────────────────────
    cur_sys = len(current_summary.systems)
    fut_sys = len(future_summary.systems)
    cur_edges = len(current_summary.edges)
    fut_edges = len(future_summary.edges)
    cur_hops = current_summary.total_hops
    fut_hops = future_summary.total_hops

    # ── §1  Executive Summary ────────────────────────────────────
    md += fmt.section_heading("1", "Executive Summary")
    md += f"This **{level}** summary aggregates architecture diagrams from "
    md += f"**{len(capabilities_info)}** L2 capabilities across **{scope_label}**.\n\n"
    md += f"The diagrams below show the consolidated current-state and future-state "
    md += f"system landscape **without duplicates** — each system and connection appears "
    md += f"only once even when shared across capabilities. "
    md += f"For detailed data flows, integration patterns, technology stacks, and business "
    md += f"architecture, refer to the individual L2 capability documents linked in "
    md += f"[§6 Capability Detail Reference](#6-capability-detail-reference).\n\n"

    md += "| Metric | Current-State | Future-State | Delta |\n"
    md += "|--------|:---:|:---:|:---:|\n"
    md += f"| **Unique Systems** | {cur_sys} | {fut_sys} | {fut_sys - cur_sys:+d} |\n"
    md += f"| **System Connections** | {cur_edges} | {fut_edges} | {fut_edges - cur_edges:+d} |\n"
    md += f"| **Total Flow Hops** | {cur_hops} | {fut_hops} | {fut_hops - cur_hops:+d} |\n"
    md += f"| **Capabilities Covered** | {len(capabilities_info)} | {len(capabilities_info)} | — |\n"
    md += "\n"

    # ── §2  Capability Inventory ─────────────────────────────────
    md += fmt.section_heading("2", "Capability Inventory")
    md += f"The following **{len(capabilities_info)}** capabilities are aggregated in this summary.\n"
    md += "Click a capability ID to view its full TOGAF BDAT architecture document.\n\n"
    md += "| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |\n"
    md += "|:---:|:---:|---|---|:---:|:---:|\n"
    for i, cap in enumerate(capabilities_info, 1):
        cid = cap['id']
        cap_link = _build_cap_link(cid, cap.get("tower_short", tower_short) or "")
        md += f"| {i} | {cap_link} | {cap['name']} | {cap.get('l1', '')} | {cap.get('cur_hops', 0)} | {cap.get('fut_hops', 0)} |\n"
    md += "\n"

    # ── Helper: build merged FlowSet for DB-to-DB and Platform diagrams ──
    def _merged_flowset(summary: SummaryData, label: str) -> FlowSet:
        merged = FlowSet(label=label, source_file="")
        for fs in summary.all_flows:
            merged.hops.extend(fs.hops)
        return merged

    # ── §3  Current-State Architecture ─────────────────────────────
    md += fmt.section_heading("3", "Current-State Architecture")
    if current_summary.systems:
        md += f"Aggregated current-state: **{cur_sys}** systems, **{cur_edges}** connections, "
        md += f"**{cur_hops}** flow hops.\n\n"

        md += fmt.section_heading("3.1", "Application Architecture", level=3)
        md += "> System-to-system integration flows. Color indicates IAPM lifecycle status "
        md += "(green = deployed, blue = developing, red = end-of-life).\n\n"
        cur_archi = build_summary_archimate(current_summary, iapm, prefix="SCA")
        if cur_archi:
            md += f"```mermaid\n{cur_archi}\n```\n\n"

        md += fmt.section_heading("3.2", "Data Architecture", level=3)
        md += "> Applications (blue) sit above their hosting databases (green cylinders). "
        md += "Thick arrows show data movement between databases.\n\n"
        cur_merged = _merged_flowset(current_summary, "Current")
        cur_data_arch = build_data_arch_mermaid(cur_merged, iapm, prefix="SCD")
        if cur_data_arch:
            md += f"```mermaid\n{cur_data_arch}\n```\n\n"
        else:
            md += "*DB platform data not yet populated — see [§6](#6-capability-detail-reference) L2 docs.*\n\n"

        md += fmt.section_heading("3.3", "Technology Architecture", level=3)
        md += "> Applications grouped by hosting platform. Cloud platforms marked with ☁️.\n\n"
        cur_platform = build_platform_arch_mermaid(cur_merged, iapm, prefix="SCP")
        if cur_platform:
            md += f"```mermaid\n{cur_platform}\n```\n\n"
        else:
            md += "*Platform data not yet populated — see [§6](#6-capability-detail-reference) L2 docs.*\n\n"
    else:
        md += "*No current-state flow data available.*\n\n"

    # ── §4  Future-State Architecture ──────────────────────────────
    md += fmt.section_heading("4", "Future-State Architecture")
    if future_summary.systems:
        md += f"Aggregated future-state: **{fut_sys}** systems, **{fut_edges}** connections, "
        md += f"**{fut_hops}** flow hops.\n\n"

        md += fmt.section_heading("4.1", "Application Architecture", level=3)
        md += "> System-to-system integration flows. Color indicates IAPM lifecycle status "
        md += "(green = deployed, blue = developing, red = end-of-life).\n\n"
        fut_archi = build_summary_archimate(future_summary, iapm, prefix="SFA")
        if fut_archi:
            md += f"```mermaid\n{fut_archi}\n```\n\n"

        md += fmt.section_heading("4.2", "Data Architecture", level=3)
        md += "> Applications (blue) sit above their hosting databases (green cylinders). "
        md += "Thick arrows show data movement between databases.\n\n"
        fut_merged = _merged_flowset(future_summary, "Future")
        fut_data_arch = build_data_arch_mermaid(fut_merged, iapm, prefix="SFD")
        if fut_data_arch:
            md += f"```mermaid\n{fut_data_arch}\n```\n\n"
        else:
            md += "*DB platform data not yet populated — see [§6](#6-capability-detail-reference) L2 docs.*\n\n"

        md += fmt.section_heading("4.3", "Technology Architecture", level=3)
        md += "> Applications grouped by hosting platform. Cloud platforms marked with ☁️.\n\n"
        fut_platform = build_platform_arch_mermaid(fut_merged, iapm, prefix="SFP")
        if fut_platform:
            md += f"```mermaid\n{fut_platform}\n```\n\n"
        else:
            md += "*Platform data not yet populated — see [§6](#6-capability-detail-reference) L2 docs.*\n\n"
    else:
        md += "*No future-state flow data available.*\n\n"

    # ── §5  Transformation Analysis ──────────────────────────────
    md += fmt.section_heading("5", "Transformation Analysis")

    md += fmt.section_heading("5.1", "System Landscape Changes", level=3)
    new_systems = future_summary.systems - current_summary.systems
    retired_systems = current_summary.systems - future_summary.systems
    common_systems = current_summary.systems & future_summary.systems

    md += "| Category | Count | Systems |\n"
    md += "|----------|:---:|---|\n"
    md += f"| **New Systems** | {len(new_systems)} | {', '.join(sorted(new_systems)) if new_systems else '—'} |\n"
    md += f"| **Retiring Systems** | {len(retired_systems)} | {', '.join(sorted(retired_systems)) if retired_systems else '—'} |\n"
    md += f"| **Continuing Systems** | {len(common_systems)} | — |\n"
    md += "\n"

    # New / removed connections
    cur_conn = set(current_summary.edges.keys())
    fut_conn = set(future_summary.edges.keys())
    new_conn = fut_conn - cur_conn
    removed_conn = cur_conn - fut_conn

    if new_conn:
        md += f"**New Connections ({len(new_conn)}):**\n\n"
        md += "| Source | Target |\n|---|---|\n"
        for src, tgt in sorted(new_conn):
            md += f"| {src} | {tgt} |\n"
        md += "\n"

    if removed_conn:
        md += f"**Removed Connections ({len(removed_conn)}):**\n\n"
        md += "| Source | Target |\n|---|---|\n"
        for src, tgt in sorted(removed_conn):
            md += f"| {src} | {tgt} |\n"
        md += "\n"

    md += fmt.section_heading("5.2", "Integration Complexity Delta", level=3)
    cur_degree: dict[str, int] = defaultdict(int)
    for (src, tgt) in current_summary.edges:
        cur_degree[src] += 1
        cur_degree[tgt] += 1
    fut_degree: dict[str, int] = defaultdict(int)
    for (src, tgt) in future_summary.edges:
        fut_degree[src] += 1
        fut_degree[tgt] += 1

    # Show only systems with changes or high connectivity (top 20)
    all_sys = sorted(current_summary.systems | future_summary.systems)
    changed_sys = [s for s in all_sys if cur_degree.get(s, 0) != fut_degree.get(s, 0)]
    unchanged_high = sorted(
        [s for s in all_sys if s not in changed_sys and cur_degree.get(s, 0) >= 3],
        key=lambda s: -cur_degree.get(s, 0))
    display_sys = changed_sys + unchanged_high[:10]

    if display_sys:
        md += "Systems with connectivity changes (and top hub systems):\n\n"
        md += "| System | Current Connections | Future Connections | Delta |\n"
        md += "|---|:---:|:---:|:---:|\n"
        for s in sorted(display_sys):
            c = cur_degree.get(s, 0)
            f = fut_degree.get(s, 0)
            delta = f - c
            delta_str = f"**{delta:+d}**" if delta != 0 else "—"
            md += f"| {s} | {c} | {f} | {delta_str} |\n"
        md += "\n"

    # ── §5.3  Release-over-Release Changes ───────────────────────
    if has_release_diff:
        md += fmt.section_heading("5.3", "Release-over-Release Changes", level=3)
        md += "Changes between adjacent releases — additions and retirements of applications, "
        md += "databases, and technology platforms.\n\n"

        for delta in release_deltas:
            md += f"#### {delta.from_rel} -> {delta.to_rel}\n\n"

            has_changes = any([
                delta.new_apps, delta.retired_apps,
                delta.new_dbs, delta.retired_dbs,
                delta.new_platforms, delta.retired_platforms,
            ])

            if not has_changes:
                md += "*No changes detected between releases.*\n\n"
                continue

            # Applications
            if delta.new_apps or delta.retired_apps:
                md += "**Applications:**\n\n"
                md += "| Change | Applications |\n|---|---|\n"
                if delta.new_apps:
                    md += f"| **Added** | {', '.join(sorted(delta.new_apps))} |\n"
                if delta.retired_apps:
                    md += f"| **Retired** | {', '.join(sorted(delta.retired_apps))} |\n"
                md += "\n"

            # Databases
            if delta.new_dbs or delta.retired_dbs:
                md += "**Databases:**\n\n"
                md += "| Change | Databases |\n|---|---|\n"
                if delta.new_dbs:
                    md += f"| **Added** | {', '.join(sorted(delta.new_dbs))} |\n"
                if delta.retired_dbs:
                    md += f"| **Retired** | {', '.join(sorted(delta.retired_dbs))} |\n"
                md += "\n"

            # Technology Platforms
            if delta.new_platforms or delta.retired_platforms:
                md += "**Technology Platforms:**\n\n"
                md += "| Change | Platforms |\n|---|---|\n"
                if delta.new_platforms:
                    md += f"| **Added** | {', '.join(sorted(delta.new_platforms))} |\n"
                if delta.retired_platforms:
                    md += f"| **Retired** | {', '.join(sorted(delta.retired_platforms))} |\n"
                md += "\n"

    # ── §6  Capability Detail Reference ──────────────────────────
    md += fmt.section_heading("6", "Capability Detail Reference")
    md += "For detailed architecture information, navigate to the individual L2 capability documents.\n"
    md += "Each L2 document contains the full TOGAF BDAT analysis including:\n\n"
    md += "- **Business Architecture** — BPMN process flows, business drivers, success criteria\n"
    md += "- **Data Architecture** — Source-to-target data flows with DB platforms\n"
    md += "- **Application Architecture** — Integration patterns, middleware, protocols\n"
    md += "- **Technology Architecture** — Platform inventory, deployment topology\n"
    md += "- **RICEFW / Clean Core** — SAP development object tracking\n\n"
    md += "| # | Capability | L1 Process | Architecture Doc |\n"
    md += "|:---:|---|---|---|\n"
    for i, cap in enumerate(capabilities_info, 1):
        cid = cap['id']
        cap_link = _build_cap_link(cid, cap.get("tower_short", tower_short) or "")
        md += f"| {i} | {cap['name']} | {cap.get('l1', '')} | {cap_link} |\n"
    md += "\n"

    # Inject footers
    md = fmt.inject_footers(md)

    # Inject mermaid live editor links (same as L2 documents)
    md = _inject_mermaid_live_links(md)

    return md


def _build_cap_link(cap_id: str, tower_short: str) -> str:
    """Build a relative link to an L2 capability's HTML doc, or plain text fallback."""
    if not tower_short:
        return cap_id
    tower_dir = TOWERS_DIR / tower_short
    cap_dir = find_capability_dir(tower_dir, cap_id)
    if cap_dir:
        html_name = f"{cap_id}-Architecture.html"
        html_path = cap_dir / "output" / "docs" / "systems-architecture" / html_name
        if html_path.exists():
            rel = html_path.relative_to(WORKSPACE)
            return f"[{cap_id}]({rel.as_posix()})"
    return cap_id


# ---------------------------------------------------------------------------
# Level-specific generators
# ---------------------------------------------------------------------------
def generate_l1_summaries(
    tower_short: str,
    iapm: IAPMLookup,
    release_label: str = "R1 – R5",
) -> list[str]:
    """Generate L1 summaries: one per process group within a tower."""
    tower_dir = TOWERS_DIR / tower_short
    if not tower_dir.is_dir():
        for d in TOWERS_DIR.iterdir():
            if d.is_dir() and d.name.upper() == tower_short.upper():
                tower_dir = d
                break
        else:
            print(f"Tower directory not found: {tower_short}")
            return []

    tower_cfg = load_tower_config(tower_dir)
    print(f"\n{'='*60}")
    print(f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) — L1 Summaries")
    print(f"{'='*60}")

    # Load capability_master to get L1-grouped capabilities
    cap_master = _load_capability_master()
    tower_caps = cap_master.get(tower_short, {}).get("capabilities", [])
    if not tower_caps:
        # Fall back to tower.yaml capabilities
        tower_caps = [{"id": c.cap_id, "name": c.name, "l1": c.l1}
                      for c in tower_cfg.capabilities]

    # Group by L1
    l1_groups: dict[str, list[dict]] = defaultdict(list)
    for cap in tower_caps:
        l1 = cap.get("l1", "Ungrouped")
        l1_groups[l1].append(cap)

    print(f"  L1 groups: {len(l1_groups)}")
    outputs = []

    for l1_name, caps_in_group in sorted(l1_groups.items()):
        print(f"\n  L1: {l1_name} ({len(caps_in_group)} capabilities)")
        current_flows = []
        future_flows = []
        cap_info = []

        for cap in caps_in_group:
            cid = cap["id"]
            cur, fut = _collect_capability_flows(tower_dir, tower_cfg, cid)
            cur_hops = len(cur.hops) if cur else 0
            fut_hops = len(fut.hops) if fut else 0
            if cur:
                current_flows.append(cur)
            if fut:
                future_flows.append(fut)
            cap_info.append({
                "id": cid,
                "name": cap.get("name", cid),
                "l1": l1_name,
                "tower_short": tower_cfg.shortcode,
                "cur_hops": cur_hops,
                "fut_hops": fut_hops,
            })
            if cur or fut:
                print(f"    {cid}: {cur_hops} current + {fut_hops} future hops")

        if not current_flows and not future_flows:
            print(f"    SKIP: no flow data")
            continue

        cur_summary = _aggregate_flows(current_flows)
        fut_summary = _aggregate_flows(future_flows)

        # Compute release-over-release deltas
        group_cap_ids = [cap["id"] for cap in caps_in_group]
        release_data = _collect_release_futures(tower_dir, tower_cfg, group_cap_ids)
        deltas = _compute_release_deltas(release_data) if release_data else []

        # Render document
        l1_short = re.sub(r'[^a-zA-Z0-9 ]', '', l1_name).strip().replace(' ', '-')[:40]
        output_dir = tower_dir / "output" / "docs" / "summaries"
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"L1-{l1_short}-Summary.md"
        output_path = output_dir / filename
        doc = _render_summary_doc(
            level="L1",
            title=f"{l1_name}",
            scope_label=f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) · Process: {l1_name} · {release_label}",
            current_summary=cur_summary,
            future_summary=fut_summary,
            iapm=iapm,
            capabilities_info=cap_info,
            tower_name=tower_cfg.name,
            tower_short=tower_cfg.shortcode,
            l1_group=l1_name,
            release_deltas=deltas,
            output_filepath=output_path,
        )
        output_path = output_dir / filename
        output_path.write_text(doc, encoding="utf-8")
        print(f"    DONE: {output_path.name} ({len(doc):,} chars)")
        outputs.append(str(output_path))

    return outputs


def generate_l0_summary(
    tower_short: str,
    iapm: IAPMLookup,
    release_label: str = "R1 – R5",
) -> Optional[str]:
    """Generate L0 summary: tower-level aggregation of all capabilities."""
    tower_dir = TOWERS_DIR / tower_short
    if not tower_dir.is_dir():
        for d in TOWERS_DIR.iterdir():
            if d.is_dir() and d.name.upper() == tower_short.upper():
                tower_dir = d
                break
        else:
            print(f"Tower directory not found: {tower_short}")
            return None

    tower_cfg = load_tower_config(tower_dir)
    print(f"\n{'='*60}")
    print(f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) — L0 Summary")
    print(f"{'='*60}")

    # Collect all capabilities
    cap_master = _load_capability_master()
    tower_caps = cap_master.get(tower_short, {}).get("capabilities", [])
    if not tower_caps:
        tower_caps = [{"id": c.cap_id, "name": c.name, "l1": c.l1}
                      for c in tower_cfg.capabilities]

    current_flows = []
    future_flows = []
    cap_info = []

    for cap in tower_caps:
        cid = cap["id"]
        cur, fut = _collect_capability_flows(tower_dir, tower_cfg, cid)
        cur_hops = len(cur.hops) if cur else 0
        fut_hops = len(fut.hops) if fut else 0
        if cur:
            current_flows.append(cur)
        if fut:
            future_flows.append(fut)
        cap_info.append({
            "id": cid,
            "name": cap.get("name", cid),
            "l1": cap.get("l1", ""),
            "tower_short": tower_cfg.shortcode,
            "cur_hops": cur_hops,
            "fut_hops": fut_hops,
        })
        if cur or fut:
            print(f"  {cid}: {cur_hops} current + {fut_hops} future hops")

    if not current_flows and not future_flows:
        print("  SKIP: no flow data for tower")
        return None

    cur_summary = _aggregate_flows(current_flows)
    fut_summary = _aggregate_flows(future_flows)

    # Compute release-over-release deltas
    all_cap_ids = [cap["id"] for cap in tower_caps]
    release_data = _collect_release_futures(tower_dir, tower_cfg, all_cap_ids)
    deltas = _compute_release_deltas(release_data) if release_data else []

    output_dir = tower_dir / "output" / "docs" / "summaries"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"L0-{tower_cfg.shortcode}-Summary.md"
    output_path = output_dir / filename
    doc = _render_summary_doc(
        level="L0",
        title=f"{tower_cfg.name} ({tower_cfg.shortcode})",
        scope_label=f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) \u00b7 {release_label}",
        current_summary=cur_summary,
        future_summary=fut_summary,
        iapm=iapm,
        capabilities_info=cap_info,
        tower_name=tower_cfg.name,
        tower_short=tower_cfg.shortcode,
        release_deltas=deltas,
        output_filepath=output_path,
    )
    output_path = output_dir / filename
    output_path.write_text(doc, encoding="utf-8")
    print(f"  DONE: {output_path.name} ({len(doc):,} chars)")
    return str(output_path)


def generate_program_summary(iapm: IAPMLookup, release_label: str = "R1 – R5") -> Optional[str]:
    """Generate Program summary: program-level aggregation across all towers."""
    print(f"\n{'='*60}")
    print(f"IAO Program Summary")
    print(f"{'='*60}")

    all_current_flows = []
    all_future_flows = []
    all_cap_info = []

    for tower_dir in sorted(TOWERS_DIR.iterdir()):
        if not tower_dir.is_dir():
            continue
        tower_cfg = load_tower_config(tower_dir)
        tower_short = tower_cfg.shortcode

        cap_master = _load_capability_master()
        tower_caps = cap_master.get(tower_short, {}).get("capabilities", [])
        if not tower_caps:
            tower_caps = [{"id": c.cap_id, "name": c.name, "l1": c.l1}
                          for c in tower_cfg.capabilities]

        tower_cur_count = 0
        tower_fut_count = 0
        for cap in tower_caps:
            cid = cap["id"]
            cur, fut = _collect_capability_flows(tower_dir, tower_cfg, cid)
            cur_hops = len(cur.hops) if cur else 0
            fut_hops = len(fut.hops) if fut else 0
            if cur:
                all_current_flows.append(cur)
                tower_cur_count += cur_hops
            if fut:
                all_future_flows.append(fut)
                tower_fut_count += fut_hops
            all_cap_info.append({
                "id": cid,
                "name": cap.get("name", cid),
                "l1": f"{tower_short} · {cap.get('l1', '')}",
                "tower_short": tower_short,
                "cur_hops": cur_hops,
                "fut_hops": fut_hops,
            })

        if tower_cur_count or tower_fut_count:
            print(f"  {tower_short}: {tower_cur_count} current + {tower_fut_count} future hops")

    if not all_current_flows and not all_future_flows:
        print("  SKIP: no flow data across any tower")
        return None

    cur_summary = _aggregate_flows(all_current_flows)
    fut_summary = _aggregate_flows(all_future_flows)

    # Compute release-over-release deltas across all towers
    all_deltas: list[ReleaseDelta] = []
    for tower_dir in sorted(TOWERS_DIR.iterdir()):
        if not tower_dir.is_dir():
            continue
        tower_cfg = load_tower_config(tower_dir)
        cap_master = _load_capability_master()
        tower_caps = cap_master.get(tower_cfg.shortcode, {}).get("capabilities", [])
        if not tower_caps:
            tower_caps = [{"id": c.cap_id, "name": c.name, "l1": c.l1}
                          for c in tower_cfg.capabilities]
        cap_ids = [c["id"] for c in tower_caps]
        rd = _collect_release_futures(tower_dir, tower_cfg, cap_ids)
        if rd:
            all_deltas.extend(_compute_release_deltas(rd))

    # Merge deltas by release pair
    merged_deltas: dict[tuple[str, str], ReleaseDelta] = {}
    for d in all_deltas:
        key = (d.from_rel, d.to_rel)
        if key not in merged_deltas:
            merged_deltas[key] = ReleaseDelta(from_rel=d.from_rel, to_rel=d.to_rel)
        m = merged_deltas[key]
        m.new_apps |= d.new_apps
        m.retired_apps |= d.retired_apps
        m.new_dbs |= d.new_dbs
        m.retired_dbs |= d.retired_dbs
        m.new_platforms |= d.new_platforms
        m.retired_platforms |= d.retired_platforms
    program_deltas = sorted(merged_deltas.values(), key=lambda d: d.from_rel)

    output_dir = WORKSPACE / "output" / "docs" / "summaries"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = "Program-Summary.md"
    output_path = output_dir / filename
    doc = _render_summary_doc(
        level="Program",
        title="IAO Program Architecture Summary",
        scope_label=f"IDM 2.0 — All Towers ({release_label})",
        current_summary=cur_summary,
        future_summary=fut_summary,
        iapm=iapm,
        capabilities_info=all_cap_info,
        release_deltas=program_deltas,
        output_filepath=output_path,
    )
    output_path = output_dir / filename
    output_path.write_text(doc, encoding="utf-8")
    print(f"  DONE: {output_path.name} ({len(doc):,} chars)")
    return str(output_path)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _load_capability_master() -> dict:
    """Load capability_master.yaml as {tower_code: {capabilities: [...]}}."""
    if not CAPABILITY_MASTER.exists():
        return {}
    with open(CAPABILITY_MASTER, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("towers", {})


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Generate L0/L1/Program Summary Documents")
    parser.add_argument("--tower", type=str, help="Tower shortcode (e.g. FPR)")
    parser.add_argument("--level", type=str, choices=["L0", "L1", "Program"],
                        help="Summary level: L1=process, L0=tower, Program=all towers")
    parser.add_argument("--release", type=str, help="Filter by release (e.g. R3, R4)")
    parser.add_argument("--all", action="store_true",
                        help="Generate all levels for all towers")
    parser.add_argument("--iapm-csv", type=str, default=str(IAPM_CSV),
                        help="Path to IAPM_All_Solutions.csv")
    args = parser.parse_args()

    if not args.level and not args.all:
        parser.error("Specify --level (L0|L1|Program) or --all")

    release_label = args.release or "R1 \u2013 R5"

    # Load IAPM
    print("Loading IAPM lookup...")
    iapm = IAPMLookup()
    if Path(args.iapm_csv).exists():
        iapm.load_csv(args.iapm_csv)
        print(f"  Loaded {iapm.app_count:,} applications")
    else:
        print(f"  WARNING: IAPM CSV not found \u2014 status lookups disabled")

    outputs = []

    if args.all:
        # Generate everything: L1 (process) + L0 (tower) + Program
        towers = sorted(d.name for d in TOWERS_DIR.iterdir() if d.is_dir())
        for t in towers:
            outputs.extend(generate_l1_summaries(t, iapm, release_label=release_label))
            result = generate_l0_summary(t, iapm, release_label=release_label)
            if result:
                outputs.append(result)
        result = generate_program_summary(iapm, release_label=release_label)
        if result:
            outputs.append(result)
    elif args.level == "Program":
        result = generate_program_summary(iapm, release_label=release_label)
        if result:
            outputs.append(result)
    elif args.level == "L0":
        if not args.tower:
            parser.error("--tower required for L0 (tower) summary")
        result = generate_l0_summary(args.tower, iapm, release_label=release_label)
        if result:
            outputs.append(result)
    elif args.level == "L1":
        if not args.tower:
            parser.error("--tower required for L1 (process) summaries")
        outputs = generate_l1_summaries(args.tower, iapm, release_label=release_label)

    print(f"\n{'='*60}")
    print(f"TOTAL: {len(outputs)} summary documents generated")


if __name__ == "__main__":
    main()
