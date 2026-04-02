"""gen_summary.py — Generate L0 / L1 / L2 Summary Roll-Up Documents.

Aggregates capability-level (L3) flow data into higher-level summary views:
  L2: Per L1 process group (aggregates all L3 capabilities within an L1 group)
  L1: Per tower (aggregates all L1 groups)
  L0: Program-level (aggregates all towers)

Usage:
    python -m src.gen_summary --tower FPR --level L2
    python -m src.gen_summary --tower FPR --level L1
    python -m src.gen_summary --level L0
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
)
from src.xlsx_loader import load_workbook as load_xlsx_workbook, find_workbook as find_xlsx_workbook
from src.mermaid_builder import ARCHIMATE_CLASSDEFS, LAYER_STYLES, EMOJI

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


def _aggregate_flows(flows_list: list[FlowSet]) -> SummaryData:
    """Merge multiple FlowSets into aggregated system-level edges."""
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
    l1_group: str = "",
) -> str:
    """Render a summary Markdown document."""
    fmt = DocFormatter(
        doc_type=f"{level} Architecture Summary",
        subtitle="TOGAF BDAT — Systems Integration Summary",
    )

    md = fmt.title_page(
        title=title,
        context_lines=[scope_label],
    )

    # Define sections
    sections = [
        {"number": "1", "title": "Executive Summary", "level": 1},
        {"number": "2", "title": "Capability Inventory", "level": 1},
        {"number": "3", "title": "Current-State Systems Integration", "level": 1},
        {"number": "3.1", "title": "System Integration Map", "level": 2},
        {"number": "3.2", "title": "ArchiMate Application View", "level": 2},
        {"number": "4", "title": "Future-State Systems Integration", "level": 1},
        {"number": "4.1", "title": "System Integration Map", "level": 2},
        {"number": "4.2", "title": "ArchiMate Application View", "level": 2},
        {"number": "5", "title": "Transformation Analysis", "level": 1},
        {"number": "5.1", "title": "System Landscape Changes", "level": 2},
        {"number": "5.2", "title": "Integration Complexity", "level": 2},
        {"number": "6", "title": "System Inventory", "level": 1},
    ]
    md += fmt.toc(sections)

    # §1 — Executive Summary
    md += fmt.section_heading("1", "Executive Summary")
    md += f"This document provides a **{level}** summary view of the systems architecture "
    md += f"for **{scope_label}**.\n\n"

    cur_sys = len(current_summary.systems)
    fut_sys = len(future_summary.systems)
    cur_edges = len(current_summary.edges)
    fut_edges = len(future_summary.edges)
    cur_hops = current_summary.total_hops
    fut_hops = future_summary.total_hops

    md += "| Metric | Current-State | Future-State | Delta |\n"
    md += "|--------|:---:|:---:|:---:|\n"
    md += f"| **Unique Systems** | {cur_sys} | {fut_sys} | {fut_sys - cur_sys:+d} |\n"
    md += f"| **System Connections** | {cur_edges} | {fut_edges} | {fut_edges - cur_edges:+d} |\n"
    md += f"| **Total Flow Hops** | {cur_hops} | {fut_hops} | {fut_hops - cur_hops:+d} |\n"
    md += f"| **Capabilities Covered** | {len(capabilities_info)} | {len(capabilities_info)} | — |\n"
    md += "\n"

    # §2 — Capability Inventory
    md += fmt.section_heading("2", "Capability Inventory")
    md += f"The following **{len(capabilities_info)}** capabilities are aggregated in this summary:\n\n"
    md += "| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |\n"
    md += "|:---:|:---:|---|---|:---:|:---:|\n"
    for i, cap in enumerate(capabilities_info, 1):
        md += f"| {i} | {cap['id']} | {cap['name']} | {cap.get('l1', '')} | {cap.get('cur_hops', 0)} | {cap.get('fut_hops', 0)} |\n"
    md += "\n"

    # §3 — Current-State
    md += fmt.section_heading("3", "Current-State Systems Integration")
    if current_summary.systems:
        md += f"Aggregated view of **{cur_sys}** systems with **{cur_edges}** unique connections "
        md += f"across **{cur_hops}** flow hops.\n\n"

        md += fmt.section_heading("3.1", "System Integration Map", level=3)
        cur_map = build_summary_integration_map(current_summary, prefix="SC")
        if cur_map:
            md += f"```mermaid\n{cur_map}\n```\n\n"

        md += fmt.section_heading("3.2", "ArchiMate Application View", level=3)
        cur_archi = build_summary_archimate(current_summary, iapm, prefix="SCA")
        if cur_archi:
            md += f"```mermaid\n{cur_archi}\n```\n\n"
    else:
        md += "*No current-state flow data available.*\n\n"

    # §4 — Future-State
    md += fmt.section_heading("4", "Future-State Systems Integration")
    if future_summary.systems:
        md += f"Aggregated view of **{fut_sys}** systems with **{fut_edges}** unique connections "
        md += f"across **{fut_hops}** flow hops.\n\n"

        md += fmt.section_heading("4.1", "System Integration Map", level=3)
        fut_map = build_summary_integration_map(future_summary, prefix="SF")
        if fut_map:
            md += f"```mermaid\n{fut_map}\n```\n\n"

        md += fmt.section_heading("4.2", "ArchiMate Application View", level=3)
        fut_archi = build_summary_archimate(future_summary, iapm, prefix="SFA")
        if fut_archi:
            md += f"```mermaid\n{fut_archi}\n```\n\n"
    else:
        md += "*No future-state flow data available.*\n\n"

    # §5 — Transformation Analysis
    md += fmt.section_heading("5", "Transformation Analysis")

    # §5.1 — System Landscape Changes
    md += fmt.section_heading("5.1", "System Landscape Changes", level=3)
    new_systems = future_summary.systems - current_summary.systems
    retired_systems = current_summary.systems - future_summary.systems
    common_systems = current_summary.systems & future_summary.systems

    if new_systems:
        md += f"**New Systems ({len(new_systems)}):** {', '.join(sorted(new_systems))}\n\n"
    if retired_systems:
        md += f"**Retiring Systems ({len(retired_systems)}):** {', '.join(sorted(retired_systems))}\n\n"
    md += f"**Continuing Systems:** {len(common_systems)}\n\n"

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

    # §5.2 — Integration Complexity
    md += fmt.section_heading("5.2", "Integration Complexity", level=3)
    # Count unique interfaces per system
    cur_degree = defaultdict(int)
    for (src, tgt) in current_summary.edges:
        cur_degree[src] += 1
        cur_degree[tgt] += 1
    fut_degree = defaultdict(int)
    for (src, tgt) in future_summary.edges:
        fut_degree[src] += 1
        fut_degree[tgt] += 1

    all_sys = sorted(current_summary.systems | future_summary.systems)
    if all_sys:
        md += "| System | Current Connections | Future Connections | Delta |\n"
        md += "|---|:---:|:---:|:---:|\n"
        for s in all_sys:
            c = cur_degree.get(s, 0)
            f = fut_degree.get(s, 0)
            delta = f - c
            delta_str = f"{delta:+d}" if delta != 0 else "—"
            md += f"| {s} | {c} | {f} | {delta_str} |\n"
        md += "\n"

    # §6 — System Inventory
    md += fmt.section_heading("6", "System Inventory")
    # Merge all flow data for inventory
    all_current = FlowSet(label="Current", source_file="")
    all_future = FlowSet(label="Future", source_file="")
    for fs in current_summary.all_flows:
        all_current.hops.extend(fs.hops)
    for fs in future_summary.all_flows:
        all_future.hops.extend(fs.hops)

    inventory = build_system_inventory(all_current, all_future, iapm)
    if inventory:
        md += "| # | System | IAPM ID | Status |\n"
        md += "|:---:|---|---|---|\n"
        for i, sys_entry in enumerate(inventory, 1):
            md += f"| {i} | {sys_entry.name} | {sys_entry.iapm_id} | {sys_entry.status} |\n"
        md += "\n"

    # Inject footers
    md = fmt.inject_footers(md)

    return md


# ---------------------------------------------------------------------------
# Level-specific generators
# ---------------------------------------------------------------------------
def generate_l2_summaries(
    tower_short: str,
    iapm: IAPMLookup,
    release_label: str = "R1 \u2013 R5",
) -> list[str]:
    """Generate L2 summaries: one per L1 process group within a tower."""
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
    print(f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) — L2 Summaries")
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

        # Render document
        l1_short = re.sub(r'[^a-zA-Z0-9 ]', '', l1_name).strip().replace(' ', '-')[:40]
        doc = _render_summary_doc(
            level="L2",
            title=f"{l1_name}",
            scope_label=f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) · L1 Process: {l1_name} · {release_label}",
            current_summary=cur_summary,
            future_summary=fut_summary,
            iapm=iapm,
            capabilities_info=cap_info,
            tower_name=tower_cfg.name,
            l1_group=l1_name,
        )

        # Write to towers/<TOWER>/output/docs/summaries/
        output_dir = tower_dir / "output" / "docs" / "summaries"
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"L2-{l1_short}-Summary.md"
        output_path = output_dir / filename
        output_path.write_text(doc, encoding="utf-8")
        print(f"    DONE: {output_path.name} ({len(doc):,} chars)")
        outputs.append(str(output_path))

    return outputs


def generate_l1_summary(
    tower_short: str,
    iapm: IAPMLookup,
    release_label: str = "R1 \u2013 R5",
) -> Optional[str]:
    """Generate L1 summary: tower-level aggregation of all capabilities."""
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
    print(f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) — L1 Summary")
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

    doc = _render_summary_doc(
        level="L1",
        title=f"{tower_cfg.name} ({tower_cfg.shortcode})",
        scope_label=f"Tower: {tower_cfg.name} ({tower_cfg.shortcode}) \u00b7 {release_label}",
        current_summary=cur_summary,
        future_summary=fut_summary,
        iapm=iapm,
        capabilities_info=cap_info,
        tower_name=tower_cfg.name,
    )

    output_dir = tower_dir / "output" / "docs" / "summaries"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"L1-{tower_cfg.shortcode}-Summary.md"
    output_path = output_dir / filename
    output_path.write_text(doc, encoding="utf-8")
    print(f"  DONE: {output_path.name} ({len(doc):,} chars)")
    return str(output_path)


def generate_l0_summary(iapm: IAPMLookup, release_label: str = "R1 \u2013 R5") -> Optional[str]:
    """Generate L0 summary: program-level aggregation across all towers."""
    print(f"\n{'='*60}")
    print(f"Program-Level — L0 Summary")
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

    doc = _render_summary_doc(
        level="L0",
        title="IAO Program Architecture Summary",
        scope_label=f"IDM 2.0 — All Towers ({release_label})",
        current_summary=cur_summary,
        future_summary=fut_summary,
        iapm=iapm,
        capabilities_info=all_cap_info,
    )

    output_dir = WORKSPACE / "output" / "docs" / "summaries"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = "L0-Program-Summary.md"
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
    parser = argparse.ArgumentParser(description="Generate L0/L1/L2 Summary Documents")
    parser.add_argument("--tower", type=str, help="Tower shortcode (e.g. FPR)")
    parser.add_argument("--level", type=str, choices=["L0", "L1", "L2"],
                        help="Summary level to generate")
    parser.add_argument("--release", type=str, help="Filter by release (e.g. R3, R4)")
    parser.add_argument("--all", action="store_true",
                        help="Generate all levels for all towers")
    parser.add_argument("--iapm-csv", type=str, default=str(IAPM_CSV),
                        help="Path to IAPM_All_Solutions.csv")
    args = parser.parse_args()

    if not args.level and not args.all:
        parser.error("Specify --level (L0|L1|L2) or --all")

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
        # Generate everything
        towers = sorted(d.name for d in TOWERS_DIR.iterdir() if d.is_dir())
        for t in towers:
            outputs.extend(generate_l2_summaries(t, iapm, release_label=release_label))
            result = generate_l1_summary(t, iapm, release_label=release_label)
            if result:
                outputs.append(result)
        result = generate_l0_summary(iapm, release_label=release_label)
        if result:
            outputs.append(result)
    elif args.level == "L0":
        result = generate_l0_summary(iapm, release_label=release_label)
        if result:
            outputs.append(result)
    elif args.level == "L1":
        if not args.tower:
            parser.error("--tower required for L1 summary")
        result = generate_l1_summary(args.tower, iapm, release_label=release_label)
        if result:
            outputs.append(result)
    elif args.level == "L2":
        if not args.tower:
            parser.error("--tower required for L2 summaries")
        outputs = generate_l2_summaries(args.tower, iapm, release_label=release_label)

    print(f"\n{'='*60}")
    print(f"TOTAL: {len(outputs)} summary documents generated")


if __name__ == "__main__":
    main()
