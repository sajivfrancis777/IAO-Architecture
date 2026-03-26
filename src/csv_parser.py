"""csv_parser.py — Parse CurrentFlows / FutureFlows CSVs into structured flow data.

Handles both 25-column (base) and 47-column (extended) schemas.
Missing extended columns are padded with blanks for downstream compatibility.
Also supports Excel (.xlsx) inputs when openpyxl is available.
"""

from __future__ import annotations

import csv
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Schema constants
# ---------------------------------------------------------------------------
BASE_COLUMNS = [
    "Flow Chain", "Hop #", "Source System", "Source Lane",
    "Target System", "Target Lane", "Interface / Technology", "Direction",
    "Frequency", "Data Description", "Flow Purpose", "Notes / Corrections",
    "Process/System Owner", "Data Owner", "Applicable Scope",
    "Src Web Address", "Src Business Owner", "Src Product Owner",
    "Src Product Owner Email", "Src IAPM URL",
    "Tgt Web Address", "Tgt Business Owner", "Tgt Product Owner",
    "Tgt Product Owner Email", "Tgt IAPM URL",
]

EXTENDED_COLUMNS = [
    # Data Architecture (26-31)
    "Data Entity", "Data Format", "Data Classification",
    "Data Volume", "Master/Transaction", "Data Lineage Notes",
    # Technology Architecture (32-37)
    "Integration Pattern", "Middleware / Platform", "Protocol",
    "Auth Method", "Environment Scope", "SLA / Latency",
    # Interface Architecture (38-41)
    "Interface ID", "Interface Type", "Error Handling", "Monitoring",
    # Endpoint-level (42-47)
    "Source DB Platform", "Target DB Platform",
    "Source Schema/Object", "Target Schema/Object",
    "Source Tech Platform", "Target Tech Platform",
]

ALL_COLUMNS = BASE_COLUMNS + EXTENDED_COLUMNS  # 47 total


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class FlowHop:
    """A single hop in a flow chain (one row in the CSV)."""
    flow_chain: str
    hop_num: int
    source_system: str
    source_lane: str
    target_system: str
    target_lane: str
    interface_tech: str
    direction: str
    frequency: str
    data_description: str
    flow_purpose: str
    notes: str
    process_owner: str
    data_owner: str
    scope: str
    src_web_address: str
    src_business_owner: str
    src_product_owner: str
    src_product_owner_email: str
    src_iapm_url: str
    tgt_web_address: str
    tgt_business_owner: str
    tgt_product_owner: str
    tgt_product_owner_email: str
    tgt_iapm_url: str
    # Extended columns (default blank)
    data_entity: str = ""
    data_format: str = ""
    data_classification: str = ""
    data_volume: str = ""
    master_transaction: str = ""
    data_lineage_notes: str = ""
    integration_pattern: str = ""
    middleware_platform: str = ""
    protocol: str = ""
    auth_method: str = ""
    environment_scope: str = ""
    sla_latency: str = ""
    interface_id: str = ""
    interface_type: str = ""
    error_handling: str = ""
    monitoring: str = ""
    source_db_platform: str = ""
    target_db_platform: str = ""
    source_schema_object: str = ""
    target_schema_object: str = ""
    source_tech_platform: str = ""
    target_tech_platform: str = ""


@dataclass
class FlowChain:
    """A named chain of hops (one logical end-to-end flow)."""
    name: str
    hops: list[FlowHop] = field(default_factory=list)

    @property
    def path_str(self) -> str:
        """Compressed path: collapses consecutive duplicate systems.

        e.g. 'MES 300 → XEUS → PDF-SMH → IF S/4 HANA'
        Instead of 'IF PDH Raw → IP PDH Raw → IF PDH Raw → IP PDH Raw → ...'
        produces  'IF PDH Raw / IP PDH Raw → IF PDH Foundational / IP PDH Foundational → ...'
        """
        if not self.hops:
            return ""
        raw = [self.hops[0].source_system]
        for h in self.hops:
            raw.append(h.target_system)
        # Collapse consecutive duplicates
        compressed: list[str] = [raw[0]]
        for s in raw[1:]:
            if s != compressed[-1]:
                compressed.append(s)
        # Group consecutive alternating pairs (A/B pattern) into "A / B"
        result: list[str] = []
        i = 0
        while i < len(compressed):
            # Detect A → B → A → B pattern (alternating pair)
            if (i + 3 < len(compressed)
                    and compressed[i] == compressed[i + 2]
                    and compressed[i + 1] == compressed[i + 3]):
                pair = f"{compressed[i]} / {compressed[i + 1]}"
                # Skip all repetitions of this pair
                while (i + 3 < len(compressed)
                       and compressed[i] == compressed[i + 2]
                       and compressed[i + 1] == compressed[i + 3]):
                    i += 2
                result.append(pair)
                # Add the last occurrence of B
                i += 2  # skip past final A → B
            else:
                result.append(compressed[i])
                i += 1
        return " → ".join(result)

    @property
    def interface_str(self) -> str:
        """Compressed interface chain: collapses consecutive identical interfaces."""
        if not self.hops:
            return ""
        raw = [h.interface_tech or "-" for h in self.hops]
        # Collapse consecutive duplicates, showing count for runs > 1
        compressed: list[str] = []
        i = 0
        while i < len(raw):
            j = i + 1
            while j < len(raw) and raw[j] == raw[i]:
                j += 1
            count = j - i
            if count > 1:
                compressed.append(f"{raw[i]} (×{count})")
            else:
                compressed.append(raw[i])
            i = j
        return " → ".join(compressed)

    @property
    def frequency(self) -> str:
        freqs = {h.frequency for h in self.hops if h.frequency}
        return " / ".join(sorted(freqs)) if freqs else "-"


@dataclass
class FlowSet:
    """All flows parsed from one CSV (current or future state)."""
    label: str                      # e.g. "ICOST" or "S/4 HANA"
    source_file: str                # path to the CSV
    hops: list[FlowHop] = field(default_factory=list)
    chains: list[FlowChain] = field(default_factory=list)

    @property
    def total_hops(self) -> int:
        return len(self.hops)

    @property
    def total_chains(self) -> int:
        return len(self.chains)

    def unique_systems(self) -> set[str]:
        systems: set[str] = set()
        for h in self.hops:
            systems.add(h.source_system)
            systems.add(h.target_system)
        return systems


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------
def _normalize_header(h: str) -> str:
    """Normalize a CSV header for comparison."""
    return re.sub(r"\s+", " ", h.strip().strip("\ufeff"))


def _row_to_hop(row: dict[str, str]) -> Optional[FlowHop]:
    """Convert a CSV row dict into a FlowHop. Returns None if row is empty."""
    flow_chain = (row.get("Flow Chain") or "").strip()
    source = (row.get("Source System") or "").strip()
    target = (row.get("Target System") or "").strip()
    if not flow_chain and not source and not target:
        return None  # skip blank rows

    hop_raw = (row.get("Hop #") or "0").strip()
    try:
        hop_num = int(hop_raw)
    except ValueError:
        hop_num = 0

    return FlowHop(
        flow_chain=flow_chain,
        hop_num=hop_num,
        source_system=source,
        source_lane=(row.get("Source Lane") or "").strip(),
        target_system=target,
        target_lane=(row.get("Target Lane") or "").strip(),
        interface_tech=(row.get("Interface / Technology") or "").strip(),
        direction=(row.get("Direction") or "->").strip(),
        frequency=(row.get("Frequency") or "").strip(),
        data_description=(row.get("Data Description") or "").strip(),
        flow_purpose=(row.get("Flow Purpose") or "").strip(),
        notes=(row.get("Notes / Corrections") or "").strip(),
        process_owner=(row.get("Process/System Owner") or "").strip(),
        data_owner=(row.get("Data Owner") or "").strip(),
        scope=(row.get("Applicable Scope") or "").strip(),
        src_web_address=(row.get("Src Web Address") or "").strip(),
        src_business_owner=(row.get("Src Business Owner") or "").strip(),
        src_product_owner=(row.get("Src Product Owner") or "").strip(),
        src_product_owner_email=(row.get("Src Product Owner Email") or "").strip(),
        src_iapm_url=(row.get("Src IAPM URL") or "").strip(),
        tgt_web_address=(row.get("Tgt Web Address") or "").strip(),
        tgt_business_owner=(row.get("Tgt Business Owner") or "").strip(),
        tgt_product_owner=(row.get("Tgt Product Owner") or "").strip(),
        tgt_product_owner_email=(row.get("Tgt Product Owner Email") or "").strip(),
        tgt_iapm_url=(row.get("Tgt IAPM URL") or "").strip(),
        # Extended columns — gracefully default to ""
        data_entity=(row.get("Data Entity") or "").strip(),
        data_format=(row.get("Data Format") or "").strip(),
        data_classification=(row.get("Data Classification") or "").strip(),
        data_volume=(row.get("Data Volume") or "").strip(),
        master_transaction=(row.get("Master/Transaction") or "").strip(),
        data_lineage_notes=(row.get("Data Lineage Notes") or "").strip(),
        integration_pattern=(row.get("Integration Pattern") or "").strip(),
        middleware_platform=(row.get("Middleware / Platform") or "").strip(),
        protocol=(row.get("Protocol") or "").strip(),
        auth_method=(row.get("Auth Method") or "").strip(),
        environment_scope=(row.get("Environment Scope") or "").strip(),
        sla_latency=(row.get("SLA / Latency") or "").strip(),
        interface_id=(row.get("Interface ID") or "").strip(),
        interface_type=(row.get("Interface Type") or "").strip(),
        error_handling=(row.get("Error Handling") or "").strip(),
        monitoring=(row.get("Monitoring") or "").strip(),
        source_db_platform=(row.get("Source DB Platform") or "").strip(),
        target_db_platform=(row.get("Target DB Platform") or "").strip(),
        source_schema_object=(row.get("Source Schema/Object") or "").strip(),
        target_schema_object=(row.get("Target Schema/Object") or "").strip(),
        source_tech_platform=(row.get("Source Tech Platform") or "").strip(),
        target_tech_platform=(row.get("Target Tech Platform") or "").strip(),
    )


def _group_chains(hops: list[FlowHop]) -> list[FlowChain]:
    """Group hops by Flow Chain name, sorted by Hop #."""
    chain_map: dict[str, list[FlowHop]] = {}
    for h in hops:
        chain_map.setdefault(h.flow_chain, []).append(h)
    chains = []
    for name, hop_list in chain_map.items():
        hop_list.sort(key=lambda x: x.hop_num)
        chains.append(FlowChain(name=name, hops=hop_list))
    chains.sort(key=lambda c: c.name)
    return chains


def parse_flow_csv(csv_path: str, label: str = "") -> FlowSet:
    """Parse a CurrentFlows.csv or FutureFlows.csv into a FlowSet.

    Supports:
    - 25-column (base) CSVs — extended cols default to ""
    - 47-column (extended) CSVs — fully populated
    - Excel (.xlsx) files — requires openpyxl
    """
    path = Path(csv_path)
    if not path.exists():
        return FlowSet(label=label or path.stem, source_file=str(path))

    ext = path.suffix.lower()
    if ext in (".xlsx", ".xls"):
        return _parse_excel(str(path), label)

    # CSV parsing
    hops: list[FlowHop] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            hop = _row_to_hop(row)
            if hop:
                hops.append(hop)

    chains = _group_chains(hops)
    return FlowSet(
        label=label or path.stem,
        source_file=str(path),
        hops=hops,
        chains=chains,
    )


def _parse_excel(xlsx_path: str, label: str) -> FlowSet:
    """Parse an Excel flow file. Requires openpyxl."""
    try:
        import openpyxl
    except ImportError:
        raise ImportError("openpyxl is required to read Excel flow files. pip install openpyxl")

    wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    ws = wb.active
    rows_iter = ws.iter_rows(values_only=True)
    header_row = next(rows_iter, None)
    if not header_row:
        return FlowSet(label=label or Path(xlsx_path).stem, source_file=xlsx_path)

    headers = [_normalize_header(str(h or "")) for h in header_row]
    hops: list[FlowHop] = []
    for row in rows_iter:
        row_dict = {headers[i]: str(row[i] or "") for i in range(min(len(headers), len(row)))}
        hop = _row_to_hop(row_dict)
        if hop:
            hops.append(hop)
    wb.close()

    chains = _group_chains(hops)
    return FlowSet(label=label or Path(xlsx_path).stem, source_file=xlsx_path, hops=hops, chains=chains)


# ---------------------------------------------------------------------------
# Capability directory discovery
# ---------------------------------------------------------------------------
def find_flow_csvs(
    cap_dir: str,
    release: Optional[str] = None,
) -> tuple[Optional[str], Optional[str]]:
    """Find the best current/future flow CSV pair for a capability directory.

    Priority (per build plan §5.1):
      1. {release}_CurrentFlows.csv / {release}_FutureFlows.csv
      2. CurrentFlows.csv / FutureFlows.csv
      3. .xlsx variants of the above

    Returns (current_path, future_path) — either may be None.
    """
    data_dir = os.path.join(cap_dir, "input", "data")
    if not os.path.isdir(data_dir):
        return None, None

    def _find(prefix: str) -> Optional[str]:
        # Release-scoped first
        if release:
            for ext in (".csv", ".xlsx"):
                p = os.path.join(data_dir, f"{release}_{prefix}{ext}")
                if os.path.isfile(p):
                    return p
        # Base
        for ext in (".csv", ".xlsx"):
            p = os.path.join(data_dir, f"{prefix}{ext}")
            if os.path.isfile(p):
                return p
        return None

    return _find("CurrentFlows"), _find("FutureFlows")
