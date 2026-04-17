"""process_readiness.py — Process Readiness data for SAD §3.4.

Loads L2/L3 Repository, Config Tracker, User Stories, RICEFW Object Tracker,
SAP stale builds, and QA exports to produce per-capability readiness metrics
and risk flags for the Systems Architecture Document.

Usage:
    from src.process_readiness import ProcessReadinessLoader
    pr = ProcessReadinessLoader(tower_short="FPR")
    pr.load()
    readiness = pr.readiness  # ProcessReadiness dataclass
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import pandas as pd


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class RiskFlag:
    l2: str
    flag: str
    detail: str
    severity: str  # HIGH, MEDIUM, LOW


@dataclass
class CapabilityReadiness:
    """Readiness metrics for a single L2 capability."""
    l2_code: str
    l2_desc: str
    l3_total: int = 0
    l3_in_scope: int = 0
    l4_total: int = 0
    l4_in_scope: int = 0
    config_required: int = 0
    config_complete: int = 0
    config_pct: float = 0.0
    us_total: int = 0
    us_fit: int = 0
    us_gap: int = 0
    fit_pct: float = 0.0
    ricefw_total: int = 0
    ricefw_complete: int = 0
    flags: list[RiskFlag] = field(default_factory=list)

    @property
    def ricefw_pct(self) -> float:
        return self.ricefw_complete / self.ricefw_total * 100 if self.ricefw_total else 0.0

    @property
    def overall_status(self) -> str:
        """Simple RAG: RED if any HIGH flag, AMBER if any MEDIUM, else GREEN."""
        severities = {f.severity for f in self.flags}
        if "HIGH" in severities:
            return "RED"
        if "MEDIUM" in severities:
            return "AMBER"
        return "GREEN"

    @property
    def overall_icon(self) -> str:
        return {"RED": "🔴", "AMBER": "🟡", "GREEN": "🟢"}.get(self.overall_status, "⚪")


@dataclass
class TransportSummary:
    """Transport / stale build summary for a SAP system."""
    system: str
    queued: int = 0
    unreleased: int = 0
    released: int = 0
    customizing: int = 0
    workbench: int = 0
    z_objects: int = 0


@dataclass
class QAVerification:
    """QA cross-verification for a dev→QA system pair."""
    label: str  # e.g. "BI0→BC0"
    dev_buffered: int = 0
    qa_imported: int = 0
    landed: int = 0
    missing: int = 0

    @property
    def promotion_pct(self) -> float:
        return self.landed / self.dev_buffered * 100 if self.dev_buffered else 0.0


@dataclass
class ProcessReadiness:
    """Aggregated process readiness for a tower."""
    tower_short: str
    capabilities: list[CapabilityReadiness] = field(default_factory=list)
    transports: list[TransportSummary] = field(default_factory=list)
    qa_verifications: list[QAVerification] = field(default_factory=list)
    flags: list[RiskFlag] = field(default_factory=list)

    @property
    def has_data(self) -> bool:
        return len(self.capabilities) > 0

    @property
    def active_capabilities(self) -> list[CapabilityReadiness]:
        return [c for c in self.capabilities if c.l3_total > 0]

    @property
    def total_flags(self) -> int:
        return len(self.flags)

    @property
    def high_flags(self) -> int:
        return sum(1 for f in self.flags if f.severity == "HIGH")

    @property
    def medium_flags(self) -> int:
        return sum(1 for f in self.flags if f.severity == "MEDIUM")

    @property
    def low_flags(self) -> int:
        return sum(1 for f in self.flags if f.severity == "LOW")

    @property
    def has_transports(self) -> bool:
        return len(self.transports) > 0

    @property
    def has_qa(self) -> bool:
        return len(self.qa_verifications) > 0


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

# Tower → config tracker filename pattern
_CONFIG_TRACKER_MAP = {
    "FPR": "New FPR Configuration Tracker.xlsx",
    "OTC-IF": "New OTC IF Config Tracker.xlsx",
    "OTC-IP": "New OTC IP Config Tracker.xlsx",
    "FTS-IF": "New FTS IF Config Tracker.xlsx",
    "FTS-IP": "New FTS IP Config Tracker.xlsx",
    "PTP": "New PTP Config Tracker.xlsx",
    "MDM": "New Master Data Config Tracker.xlsx",
}

# Tower → user story filename pattern
_USERSTORY_MAP = {
    "FPR": "IDM 2.0 R3 User Story Tracker - 03. FPR.xlsx",
    "OTC-IF": "IDM 2.0 R3 User Story Tracker - 04. OTC IF.xlsx",
    "OTC-IP": "IDM 2.0 R3 User Story Tracker - 05. OTC IP.xlsx",
    "FTS-IF": "IDM 2.0 R3 User Story Tracker - 06. FTS IF.xlsx",
    "FTS-IP": "IDM 2.0 R3 User Story Tracker - 07. FTS IP.xlsx",
    "PTP": "IDM 2.0 R3 User Story Tracker - 02. PTP.xlsx",
    "MDM": "IDM 2.0 R3 User Story Tracker - 08. MDM.xlsx",
}

# SAP system → QA system mapping
_SAP_LANDSCAPE = {
    "BI0": {"label": "BI0→BC0", "qa": "BC0"},
    "DI0": {"label": "DI0→DC0", "qa": "DC0"},
}

# SE16N column name normalization — map human-readable to technical
_QA_COL_MAP = {
    "REQUEST/TASK": "TRKORR",
    "STATUS": "TRSTATUS",
    "TRANSPORT TARGET": "TARSYSTEM",
    "SHORT DESCRIPTION": "AS4TEXT",
    "DATE": "AS4DATE",
    "TIME": "AS4TIME",
    "TYPE": "TRFUNCTION",
    "CATEGORY": "KORRDEV",
    "OWNER": "AS4USER",
    "PARENT REQUEST": "STRKORR",
}


class ProcessReadinessLoader:
    """Load and compute process readiness metrics for a tower."""

    def __init__(self, tower_short: str, workspace: Optional[Path] = None):
        self.tower = tower_short.upper()
        self.ws = workspace or Path(__file__).resolve().parent.parent
        self.data_dir = self.ws / "data"
        self.readiness = ProcessReadiness(tower_short=self.tower)

    def load(self) -> ProcessReadiness:
        """Load all data sources and compute readiness."""
        df_repo = self._load_repo()
        df_config = self._load_config()
        df_us = self._load_user_stories()
        df_obj = self._load_object_tracker()
        stale = self._load_stale_builds()

        if df_repo is not None:
            self._compute_capabilities(df_repo, df_config, df_us, df_obj)

        if stale:
            self._compute_transports(stale)

        self._load_qa_verification(stale)
        self._compute_tower_flags()

        return self.readiness

    # ── Data loaders ─────────────────────────────────────────────────

    def _load_repo(self) -> Optional[pd.DataFrame]:
        repo_dir = self.data_dir / "smartsheet" / "Repository Mapping"
        path = repo_dir / "Consolidated Final - Intel IAO L2 L3 Repository.xlsx"
        if not path.exists():
            return None
        df = pd.read_excel(path, sheet_name=0)
        df.columns = [c.strip() for c in df.columns]
        # Filter to this tower
        if "Team" in df.columns:
            tower_filter = df["Team"].str.upper().str.contains(
                self.tower.replace("-", ""), case=False, na=False
            )
            df = df[tower_filter].copy()
        return df

    def _load_config(self) -> Optional[pd.DataFrame]:
        filename = _CONFIG_TRACKER_MAP.get(self.tower)
        if not filename:
            return None
        path = self.data_dir / "smartsheet" / "Configuration" / filename
        if not path.exists():
            return None
        df = pd.read_excel(path, sheet_name=0)
        df.columns = [c.strip() for c in df.columns]
        return df

    def _load_user_stories(self) -> Optional[pd.DataFrame]:
        us_dir = self.data_dir / "smartsheet" / "User Stories"
        filename = _USERSTORY_MAP.get(self.tower)
        if not filename:
            # Try to find any matching file
            candidates = list(us_dir.glob(f"*{self.tower}*.xlsx"))
            if not candidates:
                return None
            filename = candidates[0].name
        path = us_dir / filename
        if not path.exists():
            return None
        df = pd.read_excel(path, sheet_name=0)
        df.columns = [c.strip() for c in df.columns]
        return df

    def _load_object_tracker(self) -> Optional[pd.DataFrame]:
        # Try CSV first (from manual download), then xlsx
        csv_path = self.data_dir / "smartsheet" / "manual" / "s4_r3_object_tracker.csv"
        if csv_path.exists():
            df = pd.read_csv(csv_path, encoding="utf-8-sig")
        else:
            candidates = list((self.data_dir / "smartsheet" / "manual").glob("*object*tracker*.csv"))
            if not candidates:
                return None
            df = pd.read_csv(candidates[0], encoding="utf-8-sig")
        df.columns = [c.strip() for c in df.columns]
        if "Tower Name" in df.columns:
            norm = df["Tower Name"].str.upper().str.replace(" ", "", regex=False)
            tower_nospace = self.tower.replace("-", "")
            df = df[norm.str.contains(tower_nospace, case=False, na=False)].copy()
        return df

    def _load_stale_builds(self) -> Optional[dict]:
        sap_dir = self.data_dir / "sap_odata"
        candidates = sorted(sap_dir.glob("stale_builds_*.json"))
        if not candidates:
            return None
        with open(candidates[-1], "r", encoding="utf-8") as f:
            return json.load(f)

    # ── Computation ──────────────────────────────────────────────────

    def _compute_capabilities(
        self,
        df_repo: pd.DataFrame,
        df_config: Optional[pd.DataFrame],
        df_us: Optional[pd.DataFrame],
        df_obj: Optional[pd.DataFrame],
    ) -> None:
        """Build per-L2 capability readiness from all data sources."""
        # Load subtower→capability mapping
        map_path = self.ws / "config" / "subtower_capability_map.json"
        cap_to_subtower: dict[str, list[str]] = {}
        if map_path.exists():
            with open(map_path, "r", encoding="utf-8") as f:
                raw = json.load(f)
            # Invert: subtower → [cap_ids] to cap_id → [subtower_names]
            for cap_id, subtowers in raw.items():
                if isinstance(subtowers, list):
                    cap_to_subtower[cap_id] = subtowers
                elif isinstance(subtowers, str):
                    cap_to_subtower[cap_id] = [subtowers]

        # Get unique L2 codes
        l2_codes = sorted(df_repo["L2 Code"].dropna().unique()) if "L2 Code" in df_repo.columns else []

        for l2 in l2_codes:
            l2_rows = df_repo[df_repo["L2 Code"] == l2]
            l2_desc = l2_rows["L2 Desc"].iloc[0] if "L2 Desc" in l2_rows.columns and len(l2_rows) > 0 else ""

            cap = CapabilityReadiness(l2_code=str(l2), l2_desc=str(l2_desc))

            # L3 / L4 counts
            if "L3 Code" in l2_rows.columns:
                l3_all = l2_rows["L3 Code"].dropna().unique()
                cap.l3_total = len(l3_all)
            if "Scope" in l2_rows.columns:
                in_scope = l2_rows[l2_rows["Scope"].str.upper().str.contains("IN", na=False)]
                cap.l3_in_scope = len(in_scope["L3 Code"].dropna().unique()) if "L3 Code" in in_scope.columns else 0
            if "L4 Code" in l2_rows.columns:
                cap.l4_total = len(l2_rows["L4 Code"].dropna().unique())
                if "Scope" in l2_rows.columns:
                    cap.l4_in_scope = len(in_scope["L4 Code"].dropna().unique()) if "L4 Code" in in_scope.columns else 0

            # Config tracker
            if df_config is not None and "L2 Code*" in df_config.columns:
                cfg_rows = df_config[df_config["L2 Code*"].astype(str).str.strip() == str(l2)]
                if "Config Not Required" in cfg_rows.columns:
                    needed = cfg_rows[cfg_rows["Config Not Required"].astype(str).str.upper() != "YES"]
                else:
                    needed = cfg_rows
                cap.config_required = len(needed)
                if "Actual Config Completion %" in needed.columns:
                    pcts = pd.to_numeric(needed["Actual Config Completion %"], errors="coerce").fillna(0)
                    cap.config_complete = int((pcts >= 1.0).sum())
                    cap.config_pct = float(pcts.mean()) if len(pcts) > 0 else 0.0

            # User stories
            if df_us is not None:
                l2_col = "L2 Process Code" if "L2 Process Code" in df_us.columns else None
                if l2_col:
                    us_rows = df_us[df_us[l2_col].astype(str).str.strip() == str(l2)]
                    if "Scope*" in us_rows.columns:
                        us_rows = us_rows[us_rows["Scope*"].str.upper().str.contains("IN", na=False)]
                    cap.us_total = len(us_rows)
                    if "Fit / Gap*" in us_rows.columns:
                        cap.us_fit = int(us_rows["Fit / Gap*"].str.upper().str.contains("FIT", na=False).sum())
                        cap.us_gap = int(us_rows["Fit / Gap*"].str.upper().str.contains("GAP", na=False).sum())
                    cap.fit_pct = cap.us_fit / cap.us_total * 100 if cap.us_total else 0.0

            # RICEFW objects (matched via subtower mapping)
            if df_obj is not None and "Sub-Tower Name" in df_obj.columns:
                subtowers = cap_to_subtower.get(str(l2), [])
                if subtowers:
                    obj_match = df_obj[df_obj["Sub-Tower Name"].isin(subtowers)]
                    cap.ricefw_total = len(obj_match)
                    if "Object Status" in obj_match.columns:
                        cap.ricefw_complete = int(
                            obj_match["Object Status"].str.upper().str.contains("COMPLETE|DEPLOY", na=False, regex=True).sum()
                        )

            # Per-capability risk flags
            self._flag_capability(cap)
            self.readiness.capabilities.append(cap)

    def _flag_capability(self, cap: CapabilityReadiness) -> None:
        """Generate risk flags for a single L2 capability."""
        l2 = cap.l2_code

        if cap.l3_in_scope > 0 and cap.config_required == 0 and cap.ricefw_total == 0:
            cap.flags.append(RiskFlag(
                l2=l2, flag="Uncovered Process",
                detail=f"{cap.l3_in_scope} L3 in-scope but no config and no RICEFW",
                severity="HIGH",
            ))

        if cap.config_required > 0 and cap.config_pct < 0.8:
            sev = "HIGH" if cap.config_pct < 0.5 else "MEDIUM"
            cap.flags.append(RiskFlag(
                l2=l2, flag="Config Incomplete",
                detail=f"Config at {cap.config_pct:.0%} ({cap.config_complete}/{cap.config_required})",
                severity=sev,
            ))

        incomplete = cap.ricefw_total - cap.ricefw_complete
        if incomplete > 0:
            cap.flags.append(RiskFlag(
                l2=l2, flag="RICEFW Incomplete",
                detail=f"{incomplete}/{cap.ricefw_total} objects not complete",
                severity="MEDIUM",
            ))

        if cap.us_total > 5 and cap.fit_pct < 50:
            cap.flags.append(RiskFlag(
                l2=l2, flag="Low Fit-to-Standard",
                detail=f"Only {cap.fit_pct:.0f}% Fit ({cap.us_fit}/{cap.us_total})",
                severity="MEDIUM",
            ))

        # Gaps without RICEFW linkage — need user story + object tracker
        if cap.us_gap > 0 and cap.ricefw_total == 0:
            cap.flags.append(RiskFlag(
                l2=l2, flag="Gap Without RICEFW",
                detail=f"{cap.us_gap} Gap user stories with no linked RICEFW",
                severity="HIGH" if cap.us_gap > 3 else "MEDIUM",
            ))

        # Propagate to tower-level flags
        self.readiness.flags.extend(cap.flags)

    def _compute_transports(self, stale: dict) -> None:
        """Extract transport summary from stale builds JSON."""
        for sys_name in ["BI0", "DI0"]:
            if sys_name not in stale:
                continue
            sys_data = stale[sys_name]
            ts = TransportSummary(system=sys_name)
            ts.unreleased = int(sys_data.get("E070_Unreleased", {}).get("total_rows", 0) or 0)
            ts.released = int(sys_data.get("E070_Released_All", {}).get("total_rows", 0) or 0)
            ts.customizing = int(sys_data.get("E070_Customizing", {}).get("total_rows", 0) or 0)
            ts.workbench = int(sys_data.get("E070_Workbench", {}).get("total_rows", 0) or 0)
            ts.z_objects = int(sys_data.get("E071_Z_Objects", {}).get("total_rows", 0) or 0)
            ts.queued = int(sys_data.get("TMSBUFFER_Queue", {}).get("total_rows", 0) or 0)
            self.readiness.transports.append(ts)

    def _load_qa_verification(self, stale: Optional[dict]) -> None:
        """Cross-reference QA exports against TMSBUFFER data."""
        qa_dir = self.data_dir / "sap_odata" / "qa_exports"
        if not qa_dir.exists() or not stale:
            return

        for sys_name, info in _SAP_LANDSCAPE.items():
            if sys_name not in stale:
                continue

            # Load QA export
            qa_prefix = info["qa"]
            df_qa = self._load_qa_export(qa_dir, qa_prefix)
            if df_qa is None:
                continue

            # Get TMSBUFFER transport IDs from dev
            buf_data = stale[sys_name].get("TMSBUFFER_Queue", {})
            dev_trkorrs = set()
            for row in buf_data.get("rows", []):
                trkorr = (row.get("TRKORR") or "").strip()
                if trkorr:
                    dev_trkorrs.add(trkorr)

            qa_trkorrs = set()
            if "TRKORR" in df_qa.columns:
                qa_trkorrs = set(df_qa["TRKORR"].astype(str).str.strip())

            landed = dev_trkorrs & qa_trkorrs
            missing = dev_trkorrs - qa_trkorrs

            qv = QAVerification(
                label=info["label"],
                dev_buffered=len(dev_trkorrs),
                qa_imported=len(qa_trkorrs),
                landed=len(landed),
                missing=len(missing),
            )
            self.readiness.qa_verifications.append(qv)

            if missing:
                ratio = len(missing) / max(len(dev_trkorrs), 1)
                self.readiness.flags.append(RiskFlag(
                    l2="TOWER",
                    flag=f"Not Promoted to QA ({info['label']})",
                    detail=f"{len(missing)}/{len(dev_trkorrs)} buffered transports not in QA",
                    severity="HIGH" if ratio > 0.5 else "MEDIUM",
                ))

    @staticmethod
    def _load_qa_export(qa_dir: Path, prefix: str) -> Optional[pd.DataFrame]:
        """Load an SE16N export — tries multiple filename patterns and formats.

        Patterns tried (in order):
          1. {prefix}_E070*.{ext}      e.g. BC0_E070.xlsx
          2. {prefix}{dev}*.{ext}      e.g. BC0BI0.xlsx  (QA+dev SID)
          3. {prefix}*.{ext}           e.g. BC0_transports.xlsx
        """
        # Derive the dev SID from landscape mapping
        dev_sid = ""
        for dev, info in _SAP_LANDSCAPE.items():
            if info["qa"] == prefix:
                dev_sid = dev
                break

        patterns = [
            f"{prefix}_E070*",
            f"{prefix}{dev_sid}*" if dev_sid else None,
            f"{prefix}*",
        ]

        df = None
        for ext in ["xlsx", "csv", "txt"]:
            for pat in patterns:
                if not pat:
                    continue
                candidates = sorted(qa_dir.glob(f"{pat}.{ext}"))
                if candidates:
                    f = candidates[-1]
                    if ext == "xlsx":
                        df = pd.read_excel(f, sheet_name=0)
                    elif ext == "csv":
                        df = pd.read_csv(f, encoding="utf-8-sig")
                    else:
                        df = pd.read_csv(f, sep="\t", encoding="utf-8-sig")
                    break
            if df is not None:
                break

        if df is None:
            return None

        # Normalize columns: strip whitespace, uppercase
        df.columns = [c.strip().upper() for c in df.columns]
        # Map SE16N human-readable names to technical names
        df.rename(columns=_QA_COL_MAP, inplace=True)
        return df

    def _compute_tower_flags(self) -> None:
        """Add tower-level transport flags."""
        for ts in self.readiness.transports:
            if ts.queued > 0:
                self.readiness.flags.append(RiskFlag(
                    l2="TOWER",
                    flag=f"Transports Queued ({ts.system})",
                    detail=f"{ts.queued} transports in TMSBUFFER on {ts.system}",
                    severity="MEDIUM" if ts.queued < 500 else "HIGH",
                ))
