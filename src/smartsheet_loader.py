"""smartsheet_loader.py — Load RICEFW, RAID, and timeline data from Object Tracker CSV.

Parses the S4 R3 Object Tracker (1,635 × 212 cols) to extract per-tower/capability:
  - RICEFW objects (Reports, Interfaces, Conversions, Enhancements, Forms, Workflows)
  - RAID entries (from RAID column + Category)
  - Timeline milestones (FS, TDD, Build, FUT dates with % complete)

Extraction mode pivot:
  POC  — reads from data/smartsheet/object_trackers/s4_r3_object_tracker.csv
  Prod — will call Smartsheet API via src/smartsheet_client.py (not yet built)
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class RICEFWObject:
    """A single RICEFW object from the Object Tracker."""
    object_id: str
    object_type: str          # R, I, C, E, F, W
    description: str
    tower_name: str
    sub_tower: str
    status: str
    source_system: str = ""
    target_system: str = ""
    middleware: str = ""
    boundary_app: str = ""
    boundary_app_iapm_id: str = ""
    interface_approach: str = ""
    fiori_app_type: str = ""
    technical_complexity: str = ""
    technical_effort: str = ""
    fs_pct: str = ""
    build_pct: str = ""
    fut_pct: str = ""
    release: str = ""
    rev_trac_id: str = ""

    @property
    def type_code(self) -> str:
        """Normalize object_type to single-letter RICEFW code."""
        _CODE_MAP = {
            "01.report": "R", "report": "R",
            "02.interface": "I", "interface": "I",
            "03.conversion": "C", "conversion": "C",
            "12.manual conversion": "C", "manual conversion": "C",
            "04.enhancement": "E", "enhancement": "E",
            "05.form": "F", "form": "F",
            "06.workflow": "W", "workflow": "W",
        }
        key = self.object_type.strip().lower()
        return _CODE_MAP.get(key, key[:1].upper() if key else "?")

    @property
    def type_label(self) -> str:
        labels = {
            "R": "Report", "I": "Interface", "C": "Conversion",
            "E": "Enhancement", "F": "Form", "W": "Workflow",
        }
        return labels.get(self.type_code, self.object_type)


@dataclass
class RAIDEntry:
    """A RAID log entry extracted from Object Tracker."""
    object_id: str
    raid_text: str
    category: str
    tower_name: str
    status: str
    created_date: str = ""
    assigned_to: str = ""


@dataclass
class TimelineMilestone:
    """Timeline milestone for a RICEFW object."""
    object_id: str
    description: str
    tower_name: str
    fs_end: str = ""
    fs_pct: str = ""
    tdd_end: str = ""
    tdd_pct: str = ""
    build_end: str = ""
    build_pct: str = ""
    fut_end: str = ""
    fut_pct: str = ""
    overall_status: str = ""


@dataclass
class SmartsheetData:
    """Aggregated Smartsheet data for a tower or capability."""
    ricefw: list[RICEFWObject] = field(default_factory=list)
    raid: list[RAIDEntry] = field(default_factory=list)
    timeline: list[TimelineMilestone] = field(default_factory=list)

    def ricefw_by_type(self, type_code: str) -> list[RICEFWObject]:
        return [r for r in self.ricefw if r.type_code == type_code.upper()]

    @property
    def report_count(self) -> int:
        return len(self.ricefw_by_type("R"))

    @property
    def interface_count(self) -> int:
        return len(self.ricefw_by_type("I"))

    @property
    def conversion_count(self) -> int:
        return len(self.ricefw_by_type("C"))

    @property
    def enhancement_count(self) -> int:
        return len(self.ricefw_by_type("E"))

    @property
    def form_count(self) -> int:
        return len(self.ricefw_by_type("F"))

    @property
    def workflow_count(self) -> int:
        return len(self.ricefw_by_type("W"))

    @property
    def ricefw_summary(self) -> str:
        parts = []
        for code, label in [("R", "Reports"), ("I", "Interfaces"), ("C", "Conversions"),
                            ("E", "Enhancements"), ("F", "Forms"), ("W", "Workflows")]:
            n = len(self.ricefw_by_type(code))
            if n:
                parts.append(f"{n} {label}")
        return ", ".join(parts) if parts else "No RICEFW objects"


# Tower name normalization — uses centralized registry
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.tower_registry import normalize_tower as _normalize_tower_central


def _normalize_tower(raw: str) -> str:
    """Normalize a Smartsheet tower name to shortcode."""
    result = _normalize_tower_central(raw)
    return result if result else raw.strip()


def _normalize_release(raw: str) -> str:
    """Normalize release names like '03.R3' → 'R3', '04.R4' → 'R4'."""
    import re
    m = re.search(r'R(\d)', raw, re.IGNORECASE)
    return f"R{m.group(1)}" if m else "Unknown"


class SmartsheetLoader:
    """Load and filter Object Tracker data."""

    def __init__(self) -> None:
        self._rows: list[dict[str, str]] = []
        self._loaded = False

    @property
    def total_rows(self) -> int:
        return len(self._rows)

    def load_csv(self, csv_path: str) -> None:
        """Load the Object Tracker CSV."""
        path = Path(csv_path)
        if not path.exists():
            raise FileNotFoundError(f"Object Tracker CSV not found: {csv_path}")

        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            self._rows = [row for row in reader]
        self._loaded = True

    def filter_by_release(self, release: str) -> int:
        """Filter internal rows to only those matching the given release (e.g. 'R3').

        Returns the number of rows removed. Subsequent get_tower_data / get_capability_data
        calls will only see rows for this release.
        """
        before = len(self._rows)
        self._rows = [
            r for r in self._rows
            if _normalize_release((r.get("Release Name") or "").strip()) == release
        ]
        return before - len(self._rows)

    def get_tower_data(self, tower_short: str) -> SmartsheetData:
        """Extract RICEFW, RAID, and timeline for a specific tower."""
        tower_rows = [r for r in self._rows
                      if _normalize_tower(r.get("Tower Name", "")) == tower_short]
        return self._build_data(tower_rows)

    def get_capability_data(self, tower_short: str, cap_name: str = "", cap_id: str = "") -> SmartsheetData:
        """Extract data filtered to a tower + capability.

        Matching strategy (in priority order):
        1. cap_id prefix match on Object ID (e.g. 'DS-020' matches 'FPRE0887')  — not useful here
        2. cap_name fuzzy match against Sub-Tower Name descriptive part
           e.g. 'Perform Product Costing and Inventory Valuation' matches
                '3.7 FPR - Product Costing and Inventory Valuation'
        3. Fallback: empty result (caller falls back to tower-level)
        """
        rows = [r for r in self._rows
                if _normalize_tower(r.get("Tower Name", "")) == tower_short]
        if not rows:
            return SmartsheetData()

        # Try fuzzy matching cap_name against sub-tower descriptive text
        if cap_name:
            matched = self._match_subtower_rows(rows, cap_name)
            if matched:
                return self._build_data(matched)

        return SmartsheetData()

    @staticmethod
    def _extract_subtower_desc(raw_subtower: str) -> str:
        """Extract descriptive part from sub-tower name.

        '3.7 FPR - Product Costing and Inventory Valuation'
          → 'product costing and inventory valuation'
        """
        import re
        # Strip leading number and tower abbreviation: "3.7 FPR - "
        cleaned = re.sub(r'^\d+[A-Za-z]?\.\d*\s+[\w-]+\s*-\s*', '', raw_subtower)
        return cleaned.strip().lower()

    @staticmethod
    def _match_subtower_rows(rows: list[dict[str, str]], cap_name: str) -> list[dict[str, str]]:
        """Match rows by fuzzy-comparing cap_name to sub-tower descriptive text."""
        cap_lower = cap_name.strip().lower()
        # Remove common prefixes like "Perform ", "Manage ", "Execute "
        cap_core = cap_lower
        for prefix in ("perform ", "manage ", "execute ", "process ", "run ", "create ", "handle "):
            if cap_core.startswith(prefix):
                cap_core = cap_core[len(prefix):]
                break

        best_rows: list[dict[str, str]] = []
        best_score = 0

        # Group rows by sub-tower
        subtower_groups: dict[str, list[dict[str, str]]] = {}
        for r in rows:
            st = (r.get("Sub-Tower Name") or "").strip()
            subtower_groups.setdefault(st, []).append(r)

        for st_name, st_rows in subtower_groups.items():
            desc = SmartsheetLoader._extract_subtower_desc(st_name)
            if not desc:
                continue

            # Score: check containment both ways
            score = 0
            if cap_core in desc or desc in cap_core:
                score = 3  # Strong match
            elif cap_core in desc.replace("&", "and") or desc.replace("&", "and") in cap_core:
                score = 3
            else:
                # Word overlap score
                cap_words = set(cap_core.split())
                desc_words = set(desc.split())
                common = cap_words & desc_words
                if len(common) >= 2:
                    score = len(common)

            if score > best_score:
                best_score = score
                best_rows = st_rows

        return best_rows if best_score >= 2 else []

    def _build_data(self, rows: list[dict[str, str]]) -> SmartsheetData:
        data = SmartsheetData()
        for row in rows:
            obj = self._parse_ricefw(row)
            if obj:
                data.ricefw.append(obj)

            raid = self._parse_raid(row)
            if raid:
                data.raid.append(raid)

            tl = self._parse_timeline(row)
            if tl:
                data.timeline.append(tl)

        return data

    def _parse_ricefw(self, row: dict[str, str]) -> Optional[RICEFWObject]:
        obj_id = (row.get("Object ID") or "").strip()
        obj_type = (row.get("Object Type") or "").strip()
        if not obj_id:
            return None
        return RICEFWObject(
            object_id=obj_id,
            object_type=obj_type,
            description=(row.get("Description") or "").strip(),
            tower_name=(row.get("Tower Name") or "").strip(),
            sub_tower=(row.get("Sub-Tower Name") or "").strip(),
            status=(row.get("Object Status") or "").strip(),
            source_system=(row.get("Source System") or "").strip(),
            target_system=(row.get("Target System") or "").strip(),
            middleware=(row.get("Middleware") or "").strip(),
            boundary_app=(row.get("Boundary Application Name") or "").strip(),
            boundary_app_iapm_id=(row.get("Boundary App. IAPM ID") or "").strip(),
            interface_approach=(row.get("Interface – Approach / Clean Core adherence") or
                               row.get("Interface - Approach / Clean Core adherence") or "").strip(),
            fiori_app_type=(row.get("Fiori application type") or "").strip(),
            technical_complexity=(row.get("Technical Complexity") or "").strip(),
            technical_effort=(row.get("Technical Effort (hours)") or "").strip(),
            fs_pct=(row.get("FS % Complete") or "").strip(),
            build_pct=(row.get("S/4 Build & TUT % Complete") or "").strip(),
            fut_pct=(row.get("FUT % Complete") or "").strip(),
            release=(row.get("Release Name") or "").strip(),
            rev_trac_id=(row.get("Rev-Trac ID") or "").strip(),
        )

    def _parse_raid(self, row: dict[str, str]) -> Optional[RAIDEntry]:
        raid_text = (row.get("RAID") or "").strip()
        if not raid_text:
            return None
        return RAIDEntry(
            object_id=(row.get("Object ID") or "").strip(),
            raid_text=raid_text,
            category=(row.get("Category") or "").strip(),
            tower_name=(row.get("Tower Name") or "").strip(),
            status=(row.get("Object Status") or "").strip(),
            created_date=(row.get("RAID Created Date") or "").strip(),
            assigned_to=(row.get("RAID Assigned To") or "").strip(),
        )

    def _parse_timeline(self, row: dict[str, str]) -> Optional[TimelineMilestone]:
        obj_id = (row.get("Object ID") or "").strip()
        if not obj_id:
            return None
        return TimelineMilestone(
            object_id=obj_id,
            description=(row.get("Description") or "").strip(),
            tower_name=(row.get("Tower Name") or "").strip(),
            fs_end=(row.get("FS Plan Finish Date") or "").strip(),
            fs_pct=(row.get("FS % Complete") or "").strip(),
            tdd_end=(row.get("S/4 TDD Plan Finish Date") or "").strip(),
            tdd_pct=(row.get("S/4 TDD % Complete") or "").strip(),
            build_end=(row.get("S/4 Build & TUT Plan Finish Date") or "").strip(),
            build_pct=(row.get("S/4 Build & TUT % Complete") or "").strip(),
            fut_end=(row.get("FUT Plan Finish Date") or "").strip(),
            fut_pct=(row.get("FUT % Complete") or "").strip(),
            overall_status=(row.get("FUT On Track/ Off Track") or "").strip(),
        )
