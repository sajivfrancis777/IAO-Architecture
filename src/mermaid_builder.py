"""mermaid_builder.py — Generate Mermaid flowchart LR diagrams from FlowSet data.

Produces Mermaid syntax matching the DS-020 reference:
  - Subgraphs grouped by lane (Source Lane / Target Lane)
  - Nodes labeled with system name + optional status annotation
  - Edges labeled with Interface / Technology
  - Click events linking to IAPM URLs
  - classDef styling for Deployed/Developing/EOL/NoMatch
  - Legend subgraph
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

from .csv_parser import FlowHop, FlowSet
from .iapm_lookup import IAPMLookup, IAPMApp


# ---------------------------------------------------------------------------
# Node / Edge structures
# ---------------------------------------------------------------------------
@dataclass
class MermaidNode:
    """A unique system node in the diagram."""
    node_id: str
    display_name: str
    lane: str
    iapm_app: Optional[IAPMApp] = None

    @property
    def label(self) -> str:
        """Node label with optional status annotation."""
        if self.iapm_app and self.iapm_app.status_label:
            return f'{self.display_name} ({self.iapm_app.status_label})'
        return self.display_name

    @property
    def style_class(self) -> str:
        if self.iapm_app:
            return self.iapm_app.style_class
        return "noMatch"


@dataclass
class MermaidEdge:
    source_id: str
    target_id: str
    label: str


# ---------------------------------------------------------------------------
# ID sanitization
# ---------------------------------------------------------------------------
def _make_node_id(prefix: str, system_name: str) -> str:
    """Create a Mermaid-safe node ID from a prefix and system name."""
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", system_name)
    clean = re.sub(r"_+", "_", clean).strip("_")
    return f"{prefix}_{clean}"


def _sanitize_lane_id(prefix: str, lane: str) -> str:
    """Create a Mermaid-safe subgraph ID from a lane name."""
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", lane)
    clean = re.sub(r"_+", "_", clean).strip("_")
    return f"{prefix}_{clean}"


def _truncate_label(label: str, max_len: int = 30) -> str:
    """Truncate long edge labels for readability."""
    if len(label) <= max_len:
        return label
    return label[: max_len - 3] + "..."


# ---------------------------------------------------------------------------
# Subgraph style colors (rotate for visual variety)
# ---------------------------------------------------------------------------
_SUBGRAPH_COLORS = [
    ("fill:#E8F5E9", "stroke:#388E3C"),
    ("fill:#E3F2FD", "stroke:#1976D2"),
    ("fill:#FFF3E0", "stroke:#E65100"),
    ("fill:#FFFDE7", "stroke:#F57F17"),
    ("fill:#FCE4EC", "stroke:#C62828"),
    ("fill:#E8EAF6", "stroke:#283593"),
    ("fill:#F3E5F5", "stroke:#7B1FA2"),
    ("fill:#E0F2F1", "stroke:#00695C"),
    ("fill:#FBE9E7", "stroke:#BF360C"),
    ("fill:#F1F8E9", "stroke:#558B2F"),
    ("fill:#FFF8E1", "stroke:#FF8F00"),
    ("fill:#E1F5FE", "stroke:#0277BD"),
]


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------
class MermaidBuilder:
    """Builds a Mermaid flowchart LR string from a FlowSet + IAPM lookup."""

    def __init__(self, flow_set: FlowSet, iapm: IAPMLookup, prefix: str = ""):
        self.flow_set = flow_set
        self.iapm = iapm
        self.prefix = prefix or self._auto_prefix()
        self._nodes: dict[str, MermaidNode] = {}
        self._edges: list[MermaidEdge] = []
        self._lanes: dict[str, list[str]] = {}  # lane -> [node_ids]

    def _auto_prefix(self) -> str:
        label = self.flow_set.label
        clean = re.sub(r"[^a-zA-Z0-9]", "", label)
        return clean[:6] if clean else "FW"

    def build(self) -> str:
        """Build the complete Mermaid diagram string."""
        self._collect_nodes_and_edges()
        lines = self._render()
        return "\n".join(lines)

    # -- Collection ----------------------------------------------------------

    def _collect_nodes_and_edges(self) -> None:
        for hop in self.flow_set.hops:
            src_id = self._ensure_node(hop.source_system, hop.source_lane,
                                       hop.src_iapm_url)
            tgt_id = self._ensure_node(hop.target_system, hop.target_lane,
                                       hop.tgt_iapm_url)
            edge_label = _truncate_label(hop.interface_tech) if hop.interface_tech else ""
            self._edges.append(MermaidEdge(src_id, tgt_id, edge_label))

    def _ensure_node(self, system: str, lane: str, iapm_url: str) -> str:
        node_id = _make_node_id(self.prefix, system)
        if node_id not in self._nodes:
            iapm_app = self.iapm.resolve(system, iapm_url) if self.iapm else None
            self._nodes[node_id] = MermaidNode(
                node_id=node_id,
                display_name=system,
                lane=lane or "Other",
                iapm_app=iapm_app,
            )
            self._lanes.setdefault(lane or "Other", []).append(node_id)
        return node_id

    # -- Rendering -----------------------------------------------------------

    def _render(self) -> list[str]:
        lines: list[str] = []
        lines.append('%%{init: {"theme": "base", "securityLevel": "loose", '
                      '"themeVariables": {"fontSize": "14px", '
                      '"fontFamily": "Segoe UI, Arial, sans-serif", '
                      '"primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5", '
                      '"lineColor": "#37474F", "secondaryColor": "#f5f8fc", '
                      '"tertiaryColor": "#fff"}, '
                      '"flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%')
        lines.append("flowchart LR")
        lines.append("")

        # Swim lanes: wrap all lanes in a container, each lane is a horizontal band
        sorted_lanes = sorted(self._lanes.keys())
        for lane in sorted_lanes:
            sg_id = _sanitize_lane_id(self.prefix, lane)
            lines.append(f'    subgraph {sg_id}[" ⬛ {lane}"]')
            lines.append(f'        direction LR')
            for nid in sorted(self._lanes[lane]):
                node = self._nodes[nid]
                lines.append(f'        {nid}["{node.label}"]')
            lines.append("    end")
            lines.append("")

        # Edges
        seen_edges: set[tuple[str, str, str]] = set()
        for edge in self._edges:
            key = (edge.source_id, edge.target_id, edge.label)
            if key in seen_edges:
                continue
            seen_edges.add(key)
            if edge.label:
                lines.append(f'    {edge.source_id} -->|"{edge.label}"| {edge.target_id}')
            else:
                lines.append(f'    {edge.source_id} --> {edge.target_id}')
        lines.append("")

        # Click events (IAPM links)
        for nid in sorted(self._nodes.keys()):
            node = self._nodes[nid]
            if node.iapm_app and node.iapm_app.url:
                tooltip = f'{node.display_name} -- IAPM #{node.iapm_app.app_id}'
                if node.iapm_app.status_label:
                    tooltip += f' ({node.iapm_app.status_label})'
                lines.append(f'    click {nid} href "{node.iapm_app.url}" '
                             f'"{tooltip}" _blank')
        lines.append("")

        # Legend
        lines.append(f'    %% ── Legend ──')
        legend_id = f"LEGEND_{self.prefix}"
        lines.append(f'    subgraph {legend_id}["Legend"]')
        lines.append(f'        direction TB')
        lines.append(f'        {self.prefix}_L_DEP["Deployed"]')
        lines.append(f'        {self.prefix}_L_DEV["Developing"]')
        lines.append(f'        {self.prefix}_L_EOL["End of Life"]')
        lines.append(f'        {self.prefix}_L_NA["No IAPM Match"]')
        lines.append(f'    end')
        lines.append("")

        # ClassDefs — professional look with clear status distinction
        lines.append("    classDef deployedStyle fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20")
        lines.append("    classDef devStyle fill:#E3F2FD,stroke:#1565C0,stroke-width:3px,color:#0D47A1")
        lines.append("    classDef eolStyle fill:#FFCDD2,stroke:#C62828,stroke-width:3px,color:#B71C1C")
        lines.append("    classDef noMatchStyle fill:#ECEFF1,stroke:#78909C,stroke-width:2px,color:#37474F,stroke-dasharray:5 3")
        lines.append("    classDef deployedLegend fill:#C8E6C9,stroke:#388E3C,stroke-width:2px,color:#1B5E20")
        lines.append("    classDef devLegend fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1")
        lines.append("    classDef eolLegend fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C")
        lines.append("    classDef naLegend fill:#ECEFF1,stroke:#78909C,stroke-width:2px,color:#37474F,stroke-dasharray:5 3")
        lines.append("")

        # Apply classes to nodes
        deployed_nodes = []
        dev_nodes = []
        eol_nodes = []
        no_match_nodes = []
        for nid in sorted(self._nodes.keys()):
            cls = self._nodes[nid].style_class
            if cls == "deployed":
                deployed_nodes.append(nid)
            elif cls == "developing":
                dev_nodes.append(nid)
            elif cls == "eol":
                eol_nodes.append(nid)
            elif cls == "noMatch":
                no_match_nodes.append(nid)

        if deployed_nodes:
            lines.append(f"    class {','.join(deployed_nodes)} deployedStyle")
        if dev_nodes:
            lines.append(f"    class {','.join(dev_nodes)} devStyle")
        if eol_nodes:
            lines.append(f"    class {','.join(eol_nodes)} eolStyle")
        if no_match_nodes:
            lines.append(f"    class {','.join(no_match_nodes)} noMatchStyle")

        # Legend node classes
        lines.append(f"    class {self.prefix}_L_DEP deployedLegend")
        lines.append(f"    class {self.prefix}_L_DEV devLegend")
        lines.append(f"    class {self.prefix}_L_EOL eolLegend")
        lines.append(f"    class {self.prefix}_L_NA naLegend")
        lines.append("")

        # Subgraph styles
        for i, lane in enumerate(sorted_lanes):
            sg_id = _sanitize_lane_id(self.prefix, lane)
            fill, stroke = _SUBGRAPH_COLORS[i % len(_SUBGRAPH_COLORS)]
            lines.append(f"    style {sg_id} {fill},{stroke}")
        lines.append(f"    style {legend_id} fill:#FFFFFF,stroke:#BDBDBD")

        return lines


def build_mermaid(flow_set: FlowSet, iapm: IAPMLookup, prefix: str = "") -> str:
    """Convenience function: build Mermaid diagram string from a FlowSet."""
    return MermaidBuilder(flow_set, iapm, prefix).build()


# ---------------------------------------------------------------------------
# ArchiMate-Inspired 3-Layer Diagram Builder
# ---------------------------------------------------------------------------
ARCHIMATE_CLASSDEFS = """\
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000"""

LAYER_STYLES = """\
    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px"""

EMOJI = {
    "app": "📦", "middleware": "🔗", "data": "📄",
    "database": "🗄️", "platform": "🖥️", "cloud": "☁️", "eol": "⛔",
}

# ---------------------------------------------------------------------------
# Well-known system → database / platform inference
# Used when extended columns (42-47) are not populated in the flow CSVs.
# ---------------------------------------------------------------------------
_SYSTEM_DB_MAP: dict[str, str] = {
    "SAP S/4HANA": "SAP HANA",  "S/4 HANA": "SAP HANA",
    "IF S/4 HANA": "SAP HANA",  "Corp / IP S/4 HANA": "SAP HANA",
    "Corp / IP S/4": "SAP HANA",  "CFIN S/4 HANA": "SAP HANA",
    "SAP ECC": "Oracle DB",  "SAP ICX": "Oracle DB",
    "SAP S/4 MDG": "SAP HANA",  "SAP PAPM": "SAP HANA",
    "SAP BOBJ": "SAP HANA",  "SAP IBP": "SAP HANA",
    "SAP SAC": "SAP HANA Cloud",  "SAP Ariba": "SAP HANA Cloud",
    "Finance HANA": "SAP HANA",  "SideCar": "SAP HANA",
    "ECA-SnowFlake": "Snowflake",  "ECA-DataBricks": "Delta Lake",
    "ECA-ADLS": "Azure Data Lake",  "ECA": "Snowflake",
    "Power BI (DARC)": "Snowflake",  "Power BI": "Snowflake",
    "MES 300": "PostgreSQL",  "XEUS": "PostgreSQL",
    "PEGA": "PostgreSQL",  "PDF-SMH": "MSSQL",
    "EDW": "Teradata",  "BOBJ": "SAP HANA",
    "ICOST": "Oracle DB",  "COMPASS": "Oracle DB",
    "CIBR": "Oracle DB",  "FCA": "Oracle DB",
    "DCS": "Oracle DB",  "EATS": "Oracle DB",
    "SPEED": "Oracle DB",  "WorkStream": "MSSQL",
    "MARS": "MSSQL",  "WSPW": "MSSQL",
    "GraphiteConnect": "MSSQL",
}

_SYSTEM_PLATFORM_MAP: dict[str, str] = {
    "SAP S/4HANA": "SAP HEC (On-Prem)",  "S/4 HANA": "SAP HEC (On-Prem)",
    "IF S/4 HANA": "SAP HEC (On-Prem)",  "Corp / IP S/4 HANA": "SAP HEC (On-Prem)",
    "Corp / IP S/4": "SAP HEC (On-Prem)",  "CFIN S/4 HANA": "SAP HEC (On-Prem)",
    "SAP ECC": "SAP On-Prem (Linux)",  "SAP ICX": "SAP On-Prem (Linux)",
    "SAP S/4 MDG": "SAP HEC (On-Prem)",  "SAP PAPM": "SAP BTP",
    "SAP BOBJ": "SAP On-Prem (Linux)",  "SAP IBP": "SAP BTP",
    "SAP SAC": "SAP BTP",  "SAP Ariba": "SAP Cloud (SaaS)",
    "Finance HANA": "SAP HEC (On-Prem)",  "SideCar": "SAP HEC (On-Prem)",
    "ECA-SnowFlake": "Azure Cloud",  "ECA-DataBricks": "Azure Cloud",
    "ECA-ADLS": "Azure Cloud",  "ECA": "Azure Cloud",
    "Power BI (DARC)": "Azure Cloud",  "Power BI": "Azure Cloud",
    "MES 300": "On-Prem (Linux)",  "XEUS": "On-Prem (Linux)",
    "PEGA": "On-Prem (Linux)",  "PDF-SMH": "On-Prem (Windows)",
    "EDW": "On-Prem (Linux)",  "BOBJ": "SAP On-Prem (Linux)",
    "ICOST": "On-Prem (Linux)",  "COMPASS": "On-Prem (Linux)",
    "CIBR": "On-Prem (Linux)",  "FCA": "On-Prem (Linux)",
    "DCS": "On-Prem (Windows)",  "EATS": "On-Prem (Linux)",
    "SPEED": "On-Prem (Linux)",  "WorkStream": "On-Prem (Windows)",
    "MARS": "On-Prem (Windows)",  "WSPW": "On-Prem (Windows)",
    "GraphiteConnect": "Azure Cloud",
    "MuleSoft": "MuleSoft Anypoint (Cloud)",
    "APIGEE": "Google Cloud (SaaS)",
    "IF Blue Yonder": "Azure Cloud",  "IP Blue Yonder": "Azure Cloud",
}


def _infer_db(system_name: str) -> str:
    """Return the inferred database technology for a system, or empty string."""
    return _SYSTEM_DB_MAP.get(system_name, "")


def _infer_platform(system_name: str) -> str:
    """Return the inferred platform for a system, or empty string."""
    return _SYSTEM_PLATFORM_MAP.get(system_name, "")


def build_archimate_mermaid(
    flow_set: FlowSet, iapm: IAPMLookup, prefix: str = "",
    view: str = "full",
) -> str:
    """Generate an ArchiMate-inspired 3-layer Mermaid diagram.

    Views:
      'full'  — Business + Application + Technology layers
      'app'   — Application layer only (lane-grouped, like original)
      'data'  — Data + Application layers
      'tech'  — Technology layer only
    """
    if not flow_set.hops:
        return ""
    pfx = prefix or "A"

    # Collect unique elements
    apps: dict[str, dict] = {}       # node_id → {name, lane, iapm_app, status}
    middlewares: dict[str, str] = {}  # node_id → name
    data_entities: dict[str, str] = {}  # node_id → label
    edges: list[tuple[str, str, str]] = []

    for hop in flow_set.hops:
        src_id = _make_node_id(pfx, hop.source_system)
        tgt_id = _make_node_id(pfx, hop.target_system)

        # Application nodes
        for sys_name, sys_url, nid, lane in [
            (hop.source_system, hop.src_iapm_url, src_id, hop.source_lane),
            (hop.target_system, hop.tgt_iapm_url, tgt_id, hop.target_lane),
        ]:
            if nid not in apps:
                ia = iapm.resolve(sys_name, sys_url) if iapm else None
                apps[nid] = {"name": sys_name, "lane": lane, "iapm_app": ia,
                             "status": ia.status if ia else "N/A"}

        # Middleware nodes (from extended col 33)
        mw_name = hop.middleware_platform
        if mw_name:
            mw_id = _make_node_id(pfx + "MW", mw_name)
            middlewares[mw_id] = mw_name
            edges.append((src_id, mw_id, _truncate_label(hop.interface_tech)))
            edges.append((mw_id, tgt_id, ""))
        else:
            label = _truncate_label(hop.interface_tech) if hop.interface_tech else ""
            edges.append((src_id, tgt_id, label))

        # Data entities (from extended col 26)
        if hop.data_entity:
            de_id = _make_node_id(pfx + "DE", hop.data_entity)
            fmt = f"<br/><i>{hop.data_format}</i>" if hop.data_format else ""
            data_entities[de_id] = f"{hop.data_entity}{fmt}"

    # Render
    lines: list[str] = []
    lines.append('%%{init: {"theme": "base", "securityLevel": "loose", '
                  '"themeVariables": {"fontSize": "16px", "fontFamily": "Segoe UI, Arial, sans-serif"}, '
                  '"flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%')
    lines.append("flowchart TB")
    lines.append(ARCHIMATE_CLASSDEFS)
    lines.append("")

    # Application Layer — swim lanes by Source/Target Lane
    if view in ("full", "app", "data"):
        # Group apps by their lane
        lane_groups: dict[str, list[str]] = {}
        for nid, info in apps.items():
            lane = info.get("lane") or "Other"
            lane_groups.setdefault(lane, []).append(nid)

        lines.append('    subgraph AL["🔵 APPLICATION LAYER"]')
        lines.append("        direction LR")

        # Create swim lane subgraphs within the application layer
        for lane_name in sorted(lane_groups.keys()):
            lane_id = _sanitize_lane_id(pfx + "LN", lane_name)
            lines.append(f'        subgraph {lane_id}[" ⬛ {lane_name}"]')
            lines.append(f'            direction LR')
            for nid in sorted(lane_groups[lane_name]):
                info = apps[nid]
                ia = info["iapm_app"]
                status_str = ""
                if ia and ia.status_label:
                    status_str = f"<br/><i>{ia.status_label}</i>"
                cls = "eol" if (ia and ia.style_class == "eol") else "app"
                lines.append(f'            {nid}["{EMOJI["app"]} {info["name"]}{status_str}"]:::{cls}')
            lines.append(f'        end')

        # Middleware and data entities (not in lanes)
        for mw_id, mw_name in sorted(middlewares.items()):
            lines.append(f'        {mw_id}["{EMOJI["middleware"]} {mw_name}"]:::middleware')
        for de_id, de_label in sorted(data_entities.items()):
            lines.append(f'        {de_id}>"{EMOJI["data"]} {de_label}"]:::data')
        lines.append("    end")
        lines.append("")

    # Edges (application level flows)
    seen: set[tuple[str, str, str]] = set()
    for src, tgt, label in edges:
        key = (src, tgt, label)
        if key in seen:
            continue
        seen.add(key)
        if label:
            lines.append(f'    {src} -->|"{label}"| {tgt}')
        else:
            lines.append(f"    {src} --> {tgt}")
    lines.append("")

    # IAPM click events
    for nid, info in sorted(apps.items()):
        ia = info["iapm_app"]
        if ia and ia.url:
            tooltip = f'{info["name"]} -- IAPM #{ia.app_id}'
            lines.append(f'    click {nid} href "{ia.url}" "{tooltip}" _blank')
    lines.append("")

    # Layer styles
    lines.append(LAYER_STYLES)
    lines.append("")

    # Legend
    lines.append('    subgraph Legend["📐 LEGEND"]')
    lines.append("        direction LR")
    lines.append(f'        L_APP["{EMOJI["app"]} Application"]:::app')
    lines.append(f'        L_MW["{EMOJI["middleware"]} Middleware"]:::middleware')
    lines.append(f'        L_DE>"{EMOJI["data"]} Data Entity"]:::data')
    lines.append(f'        L_EOL["{EMOJI["eol"]} End-of-Life"]:::eol')
    lines.append("    end")
    lines.append("    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px")

    return "\n".join(lines)


def build_data_flow_mermaid(flow_set: FlowSet, iapm: IAPMLookup, prefix: str = "") -> str:
    """Generate a data-focused Mermaid diagram (Data + Application layers only)."""
    return build_archimate_mermaid(flow_set, iapm, prefix, view="data")


# ---------------------------------------------------------------------------
# Data Architecture Diagram — DB-to-DB flows with apps above
# ---------------------------------------------------------------------------
def build_data_arch_mermaid(
    flow_set: FlowSet, iapm: IAPMLookup, prefix: str = "",
) -> str:
    """Generate a Data Architecture diagram showing database-to-database flows.

    Layout (top-down):
      Application Layer (blue boxes) — apps grouped above their databases
      Data Layer (green cylinders) — databases with data flow edges between them
    """
    if not flow_set.hops:
        return ""
    pfx = prefix or "DA"

    # Collect unique app→db mappings and db→db edges
    apps: dict[str, dict] = {}          # app_nid → {name, iapm_app}
    dbs: dict[str, str] = {}            # db_nid → db_label
    app_to_db: dict[str, str] = {}      # app_nid → db_nid
    db_edges: list[tuple[str, str, str]] = []  # (src_db, tgt_db, label)

    for hop in flow_set.hops:
        src_id = _make_node_id(pfx + "A", hop.source_system)
        tgt_id = _make_node_id(pfx + "A", hop.target_system)

        # Register apps
        for sys_name, sys_url, nid in [
            (hop.source_system, hop.src_iapm_url, src_id),
            (hop.target_system, hop.tgt_iapm_url, tgt_id),
        ]:
            if nid not in apps:
                ia = iapm.resolve(sys_name, sys_url) if iapm else None
                apps[nid] = {"name": sys_name, "iapm_app": ia}

        # Resolve databases (explicit or inferred)
        src_db_name = hop.source_db_platform or _infer_db(hop.source_system)
        tgt_db_name = hop.target_db_platform or _infer_db(hop.target_system)
        src_db_id = _make_node_id(pfx + "D", src_db_name) if src_db_name else None
        tgt_db_id = _make_node_id(pfx + "D", tgt_db_name) if tgt_db_name else None

        if src_db_name and src_db_id not in dbs:
            dbs[src_db_id] = src_db_name
        if tgt_db_name and tgt_db_id not in dbs:
            dbs[tgt_db_id] = tgt_db_name

        # Map app → db
        if src_db_id:
            app_to_db[src_id] = src_db_id
        if tgt_db_id:
            app_to_db[tgt_id] = tgt_db_id

        # DB-to-DB edge (the actual data flow)
        if src_db_id and tgt_db_id and src_db_id != tgt_db_id:
            edge_label = _truncate_label(hop.interface_tech) if hop.interface_tech else ""
            db_edges.append((src_db_id, tgt_db_id, edge_label))

    # Group apps by their database
    db_to_apps: dict[str, list[str]] = {}
    orphan_apps: list[str] = []
    for app_nid, db_nid in app_to_db.items():
        db_to_apps.setdefault(db_nid, []).append(app_nid)
    for app_nid in apps:
        if app_nid not in app_to_db:
            orphan_apps.append(app_nid)

    # Render
    lines: list[str] = []
    lines.append('%%{init: {"theme": "base", "securityLevel": "loose", '
                  '"themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, '
                  '"flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%')
    lines.append("flowchart TB")
    lines.append("    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B")
    lines.append("    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20")
    lines.append("    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000")
    lines.append("")

    # Render each DB cluster: app(s) above → DB cylinder below
    for db_nid in sorted(dbs.keys()):
        db_label = dbs[db_nid]
        cluster_apps = sorted(set(db_to_apps.get(db_nid, [])))
        sg_id = _make_node_id(pfx + "CL", db_label)
        lines.append(f'    subgraph {sg_id}[" "]')
        lines.append(f"        direction TB")
        # Apps above
        for a_nid in cluster_apps:
            info = apps[a_nid]
            ia = info["iapm_app"]
            cls = "eolBox" if (ia and ia.style_class == "eol") else "appBox"
            lines.append(f'        {a_nid}["{info["name"]}"]:::{cls}')
        # DB cylinder
        lines.append(f'        {db_nid}[("{EMOJI["database"]} {db_label}")]:::dbCyl')
        # App → DB realization links
        for a_nid in cluster_apps:
            lines.append(f"        {a_nid} -.-> {db_nid}")
        lines.append("    end")
        lines.append(f"    style {sg_id} fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px")
        lines.append("")

    # Orphan apps (no known DB)
    for a_nid in orphan_apps:
        info = apps[a_nid]
        ia = info["iapm_app"]
        cls = "eolBox" if (ia and ia.style_class == "eol") else "appBox"
        lines.append(f'    {a_nid}["{info["name"]}"]:::{cls}')
    if orphan_apps:
        lines.append("")

    # DB-to-DB data flow edges (the key part)
    seen: set[tuple[str, str, str]] = set()
    for src, tgt, label in db_edges:
        key = (src, tgt, label)
        if key in seen:
            continue
        seen.add(key)
        if label:
            lines.append(f'    {src} ==>|"{label}"| {tgt}')
        else:
            lines.append(f"    {src} ==> {tgt}")
    lines.append("")

    # Legend
    lines.append('    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]')
    lines.append("        direction LR")
    lines.append('        L_A["Application"]:::appBox')
    lines.append(f'        L_D[("{EMOJI["database"]} Database")]:::dbCyl')
    lines.append('        L_E["End-of-Life"]:::eolBox')
    lines.append("    end")
    lines.append("    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Platform / Technology Architecture Diagram
# ---------------------------------------------------------------------------
def build_platform_arch_mermaid(
    flow_set: FlowSet, iapm: IAPMLookup, prefix: str = "",
) -> str:
    """Generate a Platform Architecture diagram.

    Layout (top-down):
      Applications (blue boxes) sit inside their hosting platforms (green boxes).
      Platform-to-platform integration edges shown.
    """
    if not flow_set.hops:
        return ""
    pfx = prefix or "PL"

    apps: dict[str, dict] = {}          # app_nid → {name, iapm_app}
    platforms: dict[str, str] = {}      # plat_nid → label
    app_to_plat: dict[str, str] = {}    # app_nid → plat_nid
    plat_edges: list[tuple[str, str, str]] = []

    for hop in flow_set.hops:
        src_id = _make_node_id(pfx + "A", hop.source_system)
        tgt_id = _make_node_id(pfx + "A", hop.target_system)

        for sys_name, sys_url, nid in [
            (hop.source_system, hop.src_iapm_url, src_id),
            (hop.target_system, hop.tgt_iapm_url, tgt_id),
        ]:
            if nid not in apps:
                ia = iapm.resolve(sys_name, sys_url) if iapm else None
                apps[nid] = {"name": sys_name, "iapm_app": ia}

        # Resolve platforms
        src_plat = hop.source_tech_platform or _infer_platform(hop.source_system)
        tgt_plat = hop.target_tech_platform or _infer_platform(hop.target_system)
        src_pl_id = _make_node_id(pfx + "P", src_plat) if src_plat else None
        tgt_pl_id = _make_node_id(pfx + "P", tgt_plat) if tgt_plat else None

        if src_plat and src_pl_id:
            is_cloud = any(k in src_plat.lower() for k in ("saas", "aws", "azure", "gcp", "cloud", "btp"))
            lbl = f"{EMOJI['cloud']} {src_plat}" if is_cloud else f"{EMOJI['platform']} {src_plat}"
            if src_pl_id not in platforms:
                platforms[src_pl_id] = lbl
            app_to_plat[src_id] = src_pl_id

        if tgt_plat and tgt_pl_id:
            is_cloud = any(k in tgt_plat.lower() for k in ("saas", "aws", "azure", "gcp", "cloud", "btp"))
            lbl = f"{EMOJI['cloud']} {tgt_plat}" if is_cloud else f"{EMOJI['platform']} {tgt_plat}"
            if tgt_pl_id not in platforms:
                platforms[tgt_pl_id] = lbl
            app_to_plat[tgt_id] = tgt_pl_id

        # Platform-to-platform flow
        if src_pl_id and tgt_pl_id and src_pl_id != tgt_pl_id:
            edge_label = _truncate_label(hop.interface_tech) if hop.interface_tech else ""
            plat_edges.append((src_pl_id, tgt_pl_id, edge_label))

    # Group apps by platform
    plat_to_apps: dict[str, list[str]] = {}
    orphan_apps: list[str] = []
    for a_nid, p_nid in app_to_plat.items():
        plat_to_apps.setdefault(p_nid, []).append(a_nid)
    for a_nid in apps:
        if a_nid not in app_to_plat:
            orphan_apps.append(a_nid)

    # Render
    lines: list[str] = []
    lines.append('%%{init: {"theme": "base", "securityLevel": "loose", '
                  '"themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"},'
                  ' "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%')
    lines.append("flowchart TB")
    lines.append("    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B")
    lines.append("    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20")
    lines.append("    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000")
    lines.append("")

    # Render each platform cluster with its apps inside
    for pl_nid in sorted(platforms.keys()):
        pl_label = platforms[pl_nid]
        cluster_apps = sorted(set(plat_to_apps.get(pl_nid, [])))
        lines.append(f'    subgraph {pl_nid}["{pl_label}"]')
        lines.append(f"        direction LR")
        for a_nid in cluster_apps:
            info = apps[a_nid]
            ia = info["iapm_app"]
            cls = "eolBox" if (ia and ia.style_class == "eol") else "appBox"
            lines.append(f'        {a_nid}["{info["name"]}"]:::{cls}')
        lines.append("    end")
        lines.append(f"    style {pl_nid} fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20")
        lines.append("")

    # Orphan apps — group into an "Unassigned" platform subgraph to avoid vertical sprawl
    if orphan_apps:
        lines.append(f'    subgraph {pfx}P_Unassigned["📋 Other / Unassigned Platform"]')
        lines.append(f"        direction LR")
        for a_nid in orphan_apps:
            info = apps[a_nid]
            ia = info["iapm_app"]
            cls = "eolBox" if (ia and ia.style_class == "eol") else "appBox"
            lines.append(f'        {a_nid}["{info["name"]}"]:::{cls}')
        lines.append("    end")
        lines.append(f"    style {pfx}P_Unassigned fill:#FFF9C4,stroke:#F9A825,stroke-width:2px,color:#5D4037")
        lines.append("")

    # Platform-to-platform edges
    seen: set[tuple[str, str, str]] = set()
    for src, tgt, label in plat_edges:
        key = (src, tgt, label)
        if key in seen:
            continue
        seen.add(key)
        if label:
            lines.append(f'    {src} ==>|"{label}"| {tgt}')
        else:
            lines.append(f"    {src} ==> {tgt}")
    lines.append("")

    # Legend — rendered as an HTML block below the diagram instead
    # (Mermaid inline subgraph legends overlap flows on complex diagrams)

    return "\n".join(lines)
