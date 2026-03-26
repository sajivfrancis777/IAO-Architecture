"""context_loader.py — Load supplementary input CSVs for Systems Architecture generation.

Each capability's `input/data/` folder may contain optional CSVs alongside the flow CSVs.
These provide architect-supplied context that eliminates manual placeholders in the output.

Supported files (all optional — the template renders defaults when absent):
  - BusinessDrivers.csv      → §2.2 Business Drivers
  - SuccessCriteria.csv       → §2.3 Success Criteria
  - NFRs.csv                  → §5.3 Non-Functional Requirements
  - SecurityControls.csv      → §5.4 Security & Governance
  - SAPDevStatus.csv          → §5.2 SAP Development Object Status
  - Recommendations.csv       → §6.3 Recommendations & Next Steps
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Data classes for each input type
# ---------------------------------------------------------------------------
@dataclass
class BusinessDriver:
    number: str
    name: str
    description: str
    strategic_alignment: str = ""
    priority: str = ""


@dataclass
class SuccessCriterion:
    metric: str
    target: str
    measure: str
    baseline: str = ""
    owner: str = ""


@dataclass
class NFRequirement:
    category: str
    requirement: str
    target_sla: str = ""
    priority: str = ""
    notes: str = ""


@dataclass
class SecurityControl:
    concern: str
    approach: str
    standard_policy: str = ""
    owner: str = ""
    notes: str = ""


@dataclass
class SAPDevStatusRow:
    object_type: str
    object_name: str
    environment: str
    count: str = ""
    status: str = ""
    notes: str = ""


@dataclass
class Recommendation:
    number: str
    category: str
    recommendation: str
    priority: str = ""
    owner: str = ""
    target_date: str = ""
    status: str = ""


@dataclass
class CapabilityContext:
    """All supplementary context for a capability."""
    business_drivers: list[BusinessDriver] = field(default_factory=list)
    success_criteria: list[SuccessCriterion] = field(default_factory=list)
    nfrs: list[NFRequirement] = field(default_factory=list)
    security_controls: list[SecurityControl] = field(default_factory=list)
    sap_dev_status: list[SAPDevStatusRow] = field(default_factory=list)
    recommendations: list[Recommendation] = field(default_factory=list)

    @property
    def has_drivers(self) -> bool:
        return any(d.name for d in self.business_drivers)

    @property
    def has_criteria(self) -> bool:
        return any(c.metric for c in self.success_criteria)

    @property
    def has_nfrs(self) -> bool:
        return any(n.requirement for n in self.nfrs)

    @property
    def has_security(self) -> bool:
        return any(s.approach for s in self.security_controls)

    @property
    def has_sap_status(self) -> bool:
        return any(s.count for s in self.sap_dev_status)

    @property
    def has_recommendations(self) -> bool:
        return any(r.recommendation for r in self.recommendations)

    def sap_pivot(self) -> dict[str, dict[str, str]]:
        """Pivot SAP dev status rows into {object_type: {env: count}} for the template."""
        pivot: dict[str, dict[str, str]] = {}
        for row in self.sap_dev_status:
            if row.object_type and row.count:
                pivot.setdefault(row.object_type, {})
                pivot[row.object_type][row.environment.strip().upper()] = row.count
        return pivot


# ---------------------------------------------------------------------------
# CSV loading helpers
# ---------------------------------------------------------------------------
def _read_csv(path: Path) -> list[dict[str, str]]:
    """Read a CSV into a list of dicts — tolerant of UTF-8 BOM."""
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _find_csv(data_dir: Path, name: str) -> Optional[Path]:
    """Find a context CSV by name (case-insensitive)."""
    for p in data_dir.iterdir():
        if p.is_file() and p.stem.lower() == name.lower() and p.suffix.lower() == ".csv":
            return p
    return None


# ---------------------------------------------------------------------------
# Main loader
# ---------------------------------------------------------------------------
def load_capability_context(data_dir: Path) -> CapabilityContext:
    """Load all supplementary CSVs from a capability's input/data/ directory."""
    ctx = CapabilityContext()

    # §2.2 Business Drivers
    csv_path = _find_csv(data_dir, "BusinessDrivers")
    if csv_path:
        for row in _read_csv(csv_path):
            name = (row.get("Driver Name") or "").strip()
            if name:
                ctx.business_drivers.append(BusinessDriver(
                    number=(row.get("Driver #") or "").strip(),
                    name=name,
                    description=(row.get("Description") or "").strip(),
                    strategic_alignment=(row.get("Strategic Alignment") or "").strip(),
                    priority=(row.get("Priority") or "").strip(),
                ))

    # §2.3 Success Criteria
    csv_path = _find_csv(data_dir, "SuccessCriteria")
    if csv_path:
        for row in _read_csv(csv_path):
            metric = (row.get("Metric") or "").strip()
            if metric:
                ctx.success_criteria.append(SuccessCriterion(
                    metric=metric,
                    target=(row.get("Target") or "").strip(),
                    measure=(row.get("Measure") or "").strip(),
                    baseline=(row.get("Baseline") or "").strip(),
                    owner=(row.get("Owner") or "").strip(),
                ))

    # §5.3 NFRs
    csv_path = _find_csv(data_dir, "NFRs")
    if csv_path:
        for row in _read_csv(csv_path):
            req = (row.get("Requirement") or "").strip()
            if req:
                ctx.nfrs.append(NFRequirement(
                    category=(row.get("Category") or "").strip(),
                    requirement=req,
                    target_sla=(row.get("Target / SLA") or "").strip(),
                    priority=(row.get("Priority") or "").strip(),
                    notes=(row.get("Notes") or "").strip(),
                ))

    # §5.4 Security Controls
    csv_path = _find_csv(data_dir, "SecurityControls")
    if csv_path:
        for row in _read_csv(csv_path):
            approach = (row.get("Approach") or "").strip()
            if approach:
                ctx.security_controls.append(SecurityControl(
                    concern=(row.get("Concern") or "").strip(),
                    approach=approach,
                    standard_policy=(row.get("Standard / Policy") or "").strip(),
                    owner=(row.get("Owner") or "").strip(),
                    notes=(row.get("Notes") or "").strip(),
                ))

    # §5.2 SAP Dev Status
    csv_path = _find_csv(data_dir, "SAPDevStatus")
    if csv_path:
        for row in _read_csv(csv_path):
            obj_type = (row.get("Object Type") or "").strip()
            if obj_type:
                ctx.sap_dev_status.append(SAPDevStatusRow(
                    object_type=obj_type,
                    object_name=(row.get("Object Name") or "").strip(),
                    environment=(row.get("Environment") or "").strip(),
                    count=(row.get("Count") or "").strip(),
                    status=(row.get("Status") or "").strip(),
                    notes=(row.get("Notes") or "").strip(),
                ))

    # §6.3 Recommendations
    csv_path = _find_csv(data_dir, "Recommendations")
    if csv_path:
        for row in _read_csv(csv_path):
            rec = (row.get("Recommendation") or "").strip()
            if rec:
                ctx.recommendations.append(Recommendation(
                    number=(row.get("#") or "").strip(),
                    category=(row.get("Category") or "").strip(),
                    recommendation=rec,
                    priority=(row.get("Priority") or "").strip(),
                    owner=(row.get("Owner") or "").strip(),
                    target_date=(row.get("Target Date") or "").strip(),
                    status=(row.get("Status") or "").strip(),
                ))

    return ctx
