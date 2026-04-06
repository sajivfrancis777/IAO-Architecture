"""bpmn_parser.py — Parse BPMN 2.0 XML files and convert to Mermaid flowcharts.

Reads standard BPMN 2.0 files (Signavio/BIC exports) and produces:
  - Structured BPMNProcess data with lanes, tasks, gateways, events, flows
  - Mermaid flowchart rendering with lane subgraphs and gateway logic

Supported BPMN elements:
  - Pools / Participants / Lanes
  - userTask, serviceTask, task (generic)
  - startEvent, endEvent, intermediateThrowEvent, intermediateCatchEvent
  - exclusiveGateway, parallelGateway, inclusiveGateway
  - sequenceFlow (with optional condition names)
  - subProcess (rendered as a grouped block)
  - textAnnotation (included as notes where linked)
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# BPMN 2.0 namespace
NS = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class BPMNNode:
    """A single BPMN element (task, event, or gateway)."""
    id: str
    name: str
    type: str          # 'userTask', 'serviceTask', 'startEvent', 'exclusiveGateway', etc.
    lane: str = ""     # Lane name this node belongs to

    @property
    def display_name(self) -> str:
        """Clean name for Mermaid label — strip step ID prefixes, escape special chars."""
        import re
        name = self.name.strip() if self.name else ""
        # Escape characters that break Mermaid syntax
        name = name.replace('"', "'").replace('|', '/').replace('\n', ' ')
        name = name.replace('&', ' and ').replace('#', 'No.')
        name = name.replace('<', '').replace('>', '')
        name = name.replace('[', '(').replace(']', ')')
        name = name.replace('{', '(').replace('}', ')')
        # Strip step-ID prefixes like "DS-020-030-010 " or "PM-070-010-040 "
        name = re.sub(r'^[A-Z][A-Z0-9]*-\d{3}(?:-\d{3}){0,2}\s*', '', name).strip()
        # Collapse multiple spaces
        name = re.sub(r'\s{2,}', ' ', name)
        # Truncate at word boundary
        if len(name) > 80:
            truncated = name[:77]
            last_space = truncated.rfind(' ')
            if last_space > 50:
                truncated = truncated[:last_space]
            name = truncated + "..."
        return name or self.type

    @property
    def is_gateway(self) -> bool:
        return 'Gateway' in self.type

    @property
    def is_event(self) -> bool:
        return 'Event' in self.type

    @property
    def is_task(self) -> bool:
        return 'ask' in self.type or self.type == 'task'

    @property
    def mermaid_shape(self) -> str:
        """Return Mermaid node definition with appropriate shape."""
        label = self.display_name
        if self.type == 'startEvent':
            return f'{self.id}(["fa:fa-play {label}"])'
        elif self.type == 'endEvent':
            return f'{self.id}(["fa:fa-stop {label}"])'
        elif self.is_gateway:
            gw_icon = 'fa:fa-code-branch' if 'exclusive' in self.type.lower() else 'fa:fa-arrows-alt'
            return f'{self.id}{{{{"{gw_icon} {label}"}}}}'
        elif self.type == 'serviceTask':
            return f'{self.id}[["fa:fa-cog {label}"]]'
        elif self.type == 'userTask':
            return f'{self.id}["fa:fa-user {label}"]'
        elif 'subProcess' in self.type:
            return f'{self.id}[["fa:fa-folder-open {label}"]]'
        else:
            return f'{self.id}["{label}"]'


@dataclass
class BPMNFlow:
    """A sequence flow connecting two nodes."""
    id: str
    source_ref: str
    target_ref: str
    name: str = ""     # Condition label (e.g. "Yes", "No")


@dataclass
class BPMNProcess:
    """A parsed BPMN process with all its elements."""
    file_name: str
    process_name: str
    process_id: str = ""
    lanes: list[str] = field(default_factory=list)
    nodes: dict[str, BPMNNode] = field(default_factory=dict)
    flows: list[BPMNFlow] = field(default_factory=list)

    @property
    def step_id(self) -> str:
        """Extract step ID from filename (e.g. 'DS-020-020' from 'DS-020-020 Perform Cumulative...')."""
        stem = Path(self.file_name).stem
        parts = stem.split(' ', 1)
        return parts[0] if parts else stem

    @property
    def step_name(self) -> str:
        """Extract step name from filename."""
        stem = Path(self.file_name).stem
        parts = stem.split(' ', 1)
        return parts[1] if len(parts) > 1 else stem

    @property
    def task_count(self) -> int:
        return sum(1 for n in self.nodes.values() if n.is_task)

    @property
    def gateway_count(self) -> int:
        return sum(1 for n in self.nodes.values() if n.is_gateway)

    @property
    def node_count(self) -> int:
        """Total number of nodes (tasks + gateways + events)."""
        return len(self.nodes)


# ---------------------------------------------------------------------------
# Lane resolution
# ---------------------------------------------------------------------------
def _build_lane_map(process_elem) -> dict[str, str]:
    """Build a mapping of node_id → lane_name from laneSet."""
    lane_map: dict[str, str] = {}
    for lane in process_elem.findall('.//bpmn:lane', NS):
        lane_name = lane.get('name', '')
        for flow_ref in lane.findall('bpmn:flowNodeRef', NS):
            if flow_ref.text:
                lane_map[flow_ref.text.strip()] = lane_name
    return lane_map


# ---------------------------------------------------------------------------
# BPMN XML Parser
# ---------------------------------------------------------------------------
def parse_bpmn(file_path: str) -> Optional[BPMNProcess]:
    """Parse a BPMN 2.0 XML file into a BPMNProcess.

    Returns None if the file can't be parsed or has no process.
    """
    path = Path(file_path)
    if not path.exists():
        return None

    try:
        tree = ET.parse(str(path))
    except ET.ParseError:
        return None

    root = tree.getroot()
    proc_elem = root.find('.//bpmn:process', NS)
    if proc_elem is None:
        return None

    proc = BPMNProcess(
        file_name=path.name,
        process_name=proc_elem.get('name', ''),
        process_id=proc_elem.get('id', ''),
    )

    # Build lane mapping
    lane_map = _build_lane_map(proc_elem)
    proc.lanes = sorted(set(lane_map.values())) if lane_map else []

    # Parse all node types
    node_tags = [
        'task', 'userTask', 'serviceTask', 'sendTask', 'receiveTask',
        'scriptTask', 'manualTask', 'businessRuleTask',
        'startEvent', 'endEvent',
        'intermediateThrowEvent', 'intermediateCatchEvent',
        'exclusiveGateway', 'parallelGateway', 'inclusiveGateway',
        'eventBasedGateway', 'subProcess', 'callActivity',
    ]
    for tag in node_tags:
        for elem in proc_elem.findall(f'.//bpmn:{tag}', NS):
            node_id = elem.get('id', '')
            if not node_id:
                continue
            node = BPMNNode(
                id=node_id,
                name=elem.get('name', ''),
                type=tag,
                lane=lane_map.get(node_id, ''),
            )
            proc.nodes[node_id] = node

    # Parse sequence flows
    for sf in proc_elem.findall('.//bpmn:sequenceFlow', NS):
        flow = BPMNFlow(
            id=sf.get('id', ''),
            source_ref=sf.get('sourceRef', ''),
            target_ref=sf.get('targetRef', ''),
            name=sf.get('name', ''),
        )
        if flow.source_ref and flow.target_ref:
            proc.flows.append(flow)

    return proc


# ---------------------------------------------------------------------------
# BPMN → Mermaid conversion
# ---------------------------------------------------------------------------
def bpmn_to_mermaid(proc: BPMNProcess, direction: str = "TD") -> str:
    """Convert a BPMNProcess to a Mermaid flowchart string.

    Args:
        proc: Parsed BPMN process
        direction: Mermaid direction — "TD" (top-down) or "LR" (left-right)

    Returns:
        Mermaid flowchart string (without ```mermaid fences)
    """
    lines: list[str] = []
    # Mermaid init with professional theming
    lines.append("%%{init: {'theme': 'base', 'themeVariables': {"
                 "'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial, sans-serif',"
                 "'primaryColor': '#e8f0fe', 'primaryBorderColor': '#0071c5',"
                 "'lineColor': '#37474F', 'secondaryColor': '#f5f8fc'"
                 "}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'curve': 'basis', 'nodeSpacing': 40, 'rankSpacing': 50}} }%%")
    lines.append(f"flowchart {direction}")

    # Class definitions — polished look
    lines.append("    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20")
    lines.append("    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20")
    lines.append("    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1")
    lines.append("    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C")
    lines.append("    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100")
    lines.append("    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C")

    # Sanitize node IDs for Mermaid (replace hyphens in UUIDs)
    id_map: dict[str, str] = {}
    counter = 0
    for nid in proc.nodes:
        counter += 1
        safe_id = f"n{counter}"
        id_map[nid] = safe_id

    # Group nodes by lane (subgraphs)
    if proc.lanes:
        nodes_by_lane: dict[str, list[BPMNNode]] = {}
        no_lane_nodes: list[BPMNNode] = []
        for node in proc.nodes.values():
            if node.lane:
                nodes_by_lane.setdefault(node.lane, []).append(node)
            else:
                no_lane_nodes.append(node)

        # De-duplicate lane names (some BPMNs have duplicate lane names)
        seen_lanes: list[str] = []
        for lane_name in proc.lanes:
            if lane_name not in seen_lanes:
                seen_lanes.append(lane_name)

        for lane_idx, lane_name in enumerate(seen_lanes):
            nodes = nodes_by_lane.get(lane_name, [])
            if not nodes:
                continue
            safe_lane = lane_name.replace('"', "'").replace('\n', ' ')
            lines.append(f'    subgraph lane_{lane_idx}["{safe_lane}"]')
            for node in nodes:
                sid = id_map[node.id]
                lines.append(f"        {sid}{_shape(node)}")
            lines.append("    end")

        # Nodes without a lane
        for node in no_lane_nodes:
            sid = id_map[node.id]
            lines.append(f"    {sid}{_shape(node)}")
    else:
        # No lanes — render flat
        for node in proc.nodes.values():
            sid = id_map[node.id]
            lines.append(f"    {sid}{_shape(node)}")

    # Sequence flows (edges)
    for flow in proc.flows:
        src = id_map.get(flow.source_ref)
        tgt = id_map.get(flow.target_ref)
        if not src or not tgt:
            continue
        label = flow.name.strip().replace('"', "'") if flow.name else ""
        if label:
            lines.append(f'    {src} -->|"{label}"| {tgt}')
        else:
            lines.append(f"    {src} --> {tgt}")

    # Apply styles — distinguish start from end events
    for nid, node in proc.nodes.items():
        sid = id_map[nid]
        if node.type == 'startEvent':
            lines.append(f"    class {sid} startEvt")
        elif node.type == 'endEvent':
            lines.append(f"    class {sid} endEvt")
        elif node.is_event:
            lines.append(f"    class {sid} startEvt")
        elif node.type == 'userTask':
            lines.append(f"    class {sid} userTask")
        elif node.type == 'serviceTask':
            lines.append(f"    class {sid} serviceTask")
        elif node.is_gateway:
            lines.append(f"    class {sid} gateway")
        elif 'subProcess' in node.type or 'callActivity' in node.type:
            lines.append(f"    class {sid} subProc")

    return "\n".join(lines)


def _shape(node: BPMNNode) -> str:
    """Return the Mermaid shape suffix for a node (without the ID prefix)."""
    label = node.display_name
    if node.type == 'startEvent':
        return f'(["fa:fa-play {label}"])'
    elif node.type == 'endEvent':
        return f'(["fa:fa-stop {label}"])'
    elif node.is_gateway:
        gw_icon = 'fa:fa-code-branch' if 'exclusive' in node.type.lower() else 'fa:fa-arrows-alt'
        return '{{"' + f'{gw_icon} {label}' + '"}}'
    elif node.type == 'serviceTask':
        return f'[["fa:fa-cog {label}"]]'
    elif node.type == 'userTask':
        return f'["fa:fa-user {label}"]'
    elif 'subProcess' in node.type or 'callActivity' in node.type:
        return f'[["fa:fa-folder-open {label}"]]'
    else:
        return f'["{label}"]'


# ---------------------------------------------------------------------------
# Multi-BPMN loader for a capability
# ---------------------------------------------------------------------------
def load_capability_bpmns(bpmn_dir: Path) -> list[BPMNProcess]:
    """Load and deduplicate all BPMN files from a capability's input/bpmn/ directory.

    Deduplication: when both space-named and underscore-named variants exist,
    keeps only the space-named version.

    Returns:
        List of BPMNProcess sorted by step_id.
    """
    if not bpmn_dir.is_dir():
        return []

    # Collect all BPMN files
    all_files = sorted(bpmn_dir.glob('*.bpmn'))
    if not all_files:
        return []

    # Deduplicate (space vs underscore naming)
    seen_stems: dict[str, Path] = {}
    for f in all_files:
        norm_stem = f.stem.replace('_', ' ')
        if norm_stem not in seen_stems:
            seen_stems[norm_stem] = f
        else:
            # Prefer space-named over underscore-named
            existing = seen_stems[norm_stem]
            if ' ' in f.stem and '_' in existing.stem:
                seen_stems[norm_stem] = f

    # Parse each unique file
    processes: list[BPMNProcess] = []
    for path in sorted(seen_stems.values(), key=lambda p: p.name):
        proc = parse_bpmn(str(path))
        if proc and proc.nodes:
            processes.append(proc)

    return processes


def build_process_inventory_table(processes: list[BPMNProcess]) -> str:
    """Build a Markdown table summarizing all processes for the capability."""
    if not processes:
        return ""
    lines = [
        "| # | Step ID | Process Name | Lanes | Tasks | Gateways |",
        "|---|---------|--------------|-------|-------|----------|",
    ]
    for i, proc in enumerate(processes, 1):
        lanes_str = ", ".join(proc.lanes) if proc.lanes else "—"
        lines.append(
            f"| {i} | {proc.step_id} | {proc.step_name} | {lanes_str} | {proc.task_count} | {proc.gateway_count} |"
        )
    return "\n".join(lines)
