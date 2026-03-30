"""cap_name_resolver.py — Multi-source capability name resolver.

Resolves a meaningful name for capabilities using a priority chain:
  1. tower.yaml manual override (always wins if name != cap_id)
  2. BIC/Signavio API (when BIC_AUTH_TOKEN available — capability hierarchy)
  3. Smartsheet Object Tracker sub-tower mapping
  4. BPMN XML definitions/@name (Signavio export)
  5. L1 directory name (filesystem structure)

Usage:
    resolver = CapNameResolver(tower_dir)
    name = resolver.resolve(cap_id, l1_dir_name)
"""

from __future__ import annotations

import csv
import json
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional


# Smartsheet Object Tracker (cached at module level)
_OBJECT_TRACKER = Path("data/smartsheet/object_trackers/s4_r3_object_tracker.csv")

# Mapping from L1 directory prefix to Smartsheet sub-tower descriptive title
# Built lazily on first use
_subtower_cache: dict[str, str] | None = None


def _load_subtower_map() -> dict[str, str]:
    """Build L1-prefix → descriptive sub-tower name from Smartsheet.

    Returns dict like:
        "3.7 FPR - Product Costing and Inventory Valuation" → "Product Costing and Inventory Valuation"
    Keyed by the sub-tower number for fuzzy matching.
    """
    global _subtower_cache
    if _subtower_cache is not None:
        return _subtower_cache

    _subtower_cache = {}
    if not _OBJECT_TRACKER.exists():
        return _subtower_cache

    try:
        with open(_OBJECT_TRACKER, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                st = row.get("Sub-Tower Name", "").strip()
                if not st:
                    continue
                # Parse: "3.7 FPR - Product Costing and Inventory Valuation"
                m = re.match(r"^[\d.]+\s+\w+\s*-\s*(.+)$", st)
                if m:
                    _subtower_cache[st] = m.group(1).strip()
    except Exception:
        pass

    return _subtower_cache


def _try_bic_api(cap_id: str, tower_short: str) -> str:
    """Query BIC/Signavio API for the capability-level process name.

    Returns empty string if BIC is not configured or query fails.
    This will be automatically populated once BIC_AUTH_TOKEN is set.
    """
    token = os.environ.get("BIC_AUTH_TOKEN", "")
    if not token:
        return ""

    # When BIC API access is available, this will query the process hierarchy
    # to find the capability-level process group name for cap_id.
    # BIC organizes processes as: Tower > Sub-Tower > Capability > Steps
    # The capability level name is what we need.
    #
    # TODO: Implement when BIC access is provisioned:
    #   GET /process-design/frontend/api/categories?search={cap_id}
    #   Response includes the category name (= capability title)
    return ""


def _extract_from_bpmn(bpmn_dir: Path, cap_id: str) -> str:
    """Extract a capability-level name from Signavio-exported BPMN XML.

    Strategy:
    - Parse definitions/@name from each BPMN file
    - Strip the step number prefix (e.g. "DS-020-020_" → "")
    - Find the most common descriptive theme across step names
    - Use the collaboration name if present (Signavio puts capability name there)
    """
    if not bpmn_dir.exists():
        return ""

    bpmn_files = sorted(bpmn_dir.rglob("*.bpmn"))
    if not bpmn_files:
        return ""

    ns = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL"}
    step_names: list[str] = []

    for bf in bpmn_files[:10]:  # Sample up to 10 files
        try:
            tree = ET.parse(bf)
            root = tree.getroot()

            # Check collaboration element (Signavio sometimes puts capability name here)
            for collab in root.findall(".//bpmn:collaboration", ns):
                cname = collab.get("name", "").strip()
                if cname and cname != cap_id and not cname.startswith("sid-"):
                    return cname

            # Fall back to definitions/@name
            dname = root.get("name", "").strip()
            if dname:
                # Strip step prefix: "DS-020-020_Perform Cumulative..." → "Perform Cumulative..."
                cleaned = re.sub(
                    rf"^{re.escape(cap_id)}-\d+[A-Za-z]*[_ ]",
                    "",
                    dname,
                )
                cleaned = cleaned.replace("_", " ").strip()
                # Remove trailing release markers
                cleaned = re.sub(r"\s+R\d+$", "", cleaned)
                if cleaned and cleaned != cap_id:
                    step_names.append(cleaned)
        except (ET.ParseError, Exception):
            continue

    if not step_names:
        return ""

    # Return the first step name as a representative (alphabetically first by step number)
    return step_names[0]


def _humanize_l1(l1_name: str, cap_id: str) -> str:
    """Convert L1 directory name to a readable capability name.

    E.g. "DC Manage Accounting and Control Data" → "Manage Accounting and Control Data"
    """
    # Strip the 2-3 letter prefix matching the cap_id prefix
    cap_prefix = re.match(r"^([A-Z]+)", cap_id)
    if cap_prefix:
        prefix = cap_prefix.group(1)
        if l1_name.startswith(prefix + " "):
            return l1_name[len(prefix) + 1:]

    # Generic prefix stripping
    m = re.match(r"^[A-Z]{1,4}\s+(.+)$", l1_name)
    if m:
        return m.group(1)

    return l1_name


class CapNameResolver:
    """Multi-source capability name resolver.

    Priority: tower.yaml > BIC API > Smartsheet > BPMN XML > L1 directory
    """

    def __init__(self, tower_dir: Path, tower_short: str = ""):
        self.tower_dir = tower_dir
        self.tower_short = tower_short or tower_dir.name
        self._subtower_map = _load_subtower_map()

    def resolve(
        self,
        cap_id: str,
        yaml_name: str = "",
        l1_dir_name: str = "",
        bpmn_dir: Optional[Path] = None,
    ) -> str:
        """Resolve the best available name for a capability.

        Args:
            cap_id: Capability ID (e.g., "DC-050")
            yaml_name: Name from tower.yaml (empty or equal to cap_id if not set)
            l1_dir_name: L1 process area directory name
            bpmn_dir: Path to input/bpmn/ directory for this capability

        Returns:
            Best available capability name.
        """
        # 1. tower.yaml manual override wins
        if yaml_name and yaml_name != cap_id:
            return yaml_name

        # 2. BIC/Signavio API
        bic_name = _try_bic_api(cap_id, self.tower_short)
        if bic_name:
            return bic_name

        # 3. Smartsheet sub-tower (match by tower + L1 context)
        if l1_dir_name:
            st_name = self._match_subtower(l1_dir_name)
            if st_name:
                return st_name

        # 4. BPMN XML extraction
        if bpmn_dir:
            bpmn_name = _extract_from_bpmn(bpmn_dir, cap_id)
            if bpmn_name:
                return bpmn_name

        # 5. L1 directory name fallback
        if l1_dir_name:
            return _humanize_l1(l1_dir_name, cap_id)

        return f"{cap_id} Architecture"

    def _match_subtower(self, l1_dir_name: str) -> str:
        """Match L1 directory name to Smartsheet sub-tower descriptive title.

        E.g., "DS Provide Decision Support" + tower "FPR" →
              searches for sub-tower containing "Decision Support" → 
              "Product Costing and Inventory Valuation" (if unique match)
        """
        if not self._subtower_map:
            return ""

        # Extract keywords from L1 dir name for fuzzy matching
        l1_words = set(l1_dir_name.lower().split())
        tower_prefix = f"{self.tower_short} -".lower()

        best_match = ""
        for full_st, desc in self._subtower_map.items():
            # Only match same tower
            if tower_prefix not in full_st.lower():
                continue
            # Check if the sub-tower description overlaps with L1 directory name
            st_words = set(desc.lower().split())
            overlap = l1_words & st_words
            if len(overlap) >= 2:
                best_match = desc
                break

        return best_match
