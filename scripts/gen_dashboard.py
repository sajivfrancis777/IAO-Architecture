"""gen_dashboard.py — Generate program-level and per-tower dashboard summaries.

Aggregates data from the Smartsheet Object Tracker + RAID logs to produce:
  - All-towers program dashboard (top-level summary)
  - Per-tower dashboard (one per tower)

Usage:
    python scripts/gen_dashboard.py
    python scripts/gen_dashboard.py --tower FPR
    python scripts/gen_dashboard.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"
TEMPLATES_DIR = WORKSPACE / "templates"
OBJECT_TRACKER_CSV = WORKSPACE / "data" / "smartsheet" / "object_trackers" / "s4_r3_object_tracker.csv"
RAID_CSV = WORKSPACE / "data" / "smartsheet" / "raid" / "master_raid_log.csv"

DASHBOARD_TEMPLATE = "dashboard.md.j2"

_COMPLETED_STATUSES = {"10. object complete", "10. Object Complete"}
_REJECTED_STATUSES = {"99. rejected/cancelled/on hold", "99. Rejected/Cancelled/On Hold"}

_TOWER_MAP = {
    "fpr": "FPR", "finance plan to report": "FPR", "finance": "FPR",
    "fts-if": "FTS-IF", "fts - if": "FTS-IF", "fts if": "FTS-IF",
    "forecast to stock - if": "FTS-IF",
    "fts-ip": "FTS-IP", "fts - ip": "FTS-IP", "fts ip": "FTS-IP",
    "forecast to stock - ip": "FTS-IP",
    "otc-if": "OTC-IF", "otc - if": "OTC-IF", "otc if": "OTC-IF",
    "order to cash - if": "OTC-IF",
    "otc-ip": "OTC-IP", "otc - ip": "OTC-IP", "otc ip": "OTC-IP",
    "order to cash - ip": "OTC-IP",
    "ptp": "PTP", "procure to pay": "PTP",
    "mdm": "MDM", "master data management": "MDM",
    "e2e": "E2E", "end to end": "E2E", "end-to-end": "E2E",
}

_TOWER_DISPLAY = {
    "FPR": "Finance Plan To Report",
    "FTS-IF": "Forecast to Stock — Intel Foundry",
    "FTS-IP": "Forecast to Stock — Intel Products",
    "OTC-IF": "Order to Cash — Intel Foundry",
    "OTC-IP": "Order to Cash — Intel Products",
    "PTP": "Procure to Pay",
    "MDM": "Master Data Management",
    "E2E": "End-to-End",
}

_TOWER_ORDER = ["FPR", "OTC-IF", "OTC-IP", "FTS-IF", "FTS-IP", "PTP", "MDM", "E2E"]

_TYPE_CODE = {
    "01.report": "R", "report": "R",
    "02.interface": "I", "interface": "I",
    "03.conversion": "C", "conversion": "C",
    "12.manual conversion": "C",
    "04.enhancement": "E", "enhancement": "E",
    "05.form": "F", "form": "F",
    "06.workflow": "W", "workflow": "W",
}

_TYPE_LABEL = {
    "R": "Report", "I": "Interface", "C": "Conversion",
    "E": "Enhancement", "F": "Form", "W": "Workflow",
}


def _normalize_tower(raw: str) -> str:
    key = re.sub(r"^\d{1,2}[A-Za-z]?\.\s*", "", raw.strip()).lower()
    return _TOWER_MAP.get(key, "")


def _type_code(raw: str) -> str:
    return _TYPE_CODE.get(raw.strip().lower(), raw[:1].upper() if raw else "?")


def _safe_float(val: str) -> float:
    try:
        v = float(val)
        return v * 100 if v <= 1.0 else v
    except (ValueError, TypeError):
        return 0.0


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def _load_objects(csv_path: Path) -> list[dict]:
    if not csv_path.exists():
        return []
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            tower = _normalize_tower(r.get("Tower Name", ""))
            obj_id = r.get("Object ID", "").strip()
            if not tower or not obj_id:
                continue
            otype = r.get("Object Type", "").strip()
            rows.append({
                "object_id": obj_id,
                "type_code": _type_code(otype),
                "tower": tower,
                "status": r.get("Object Status", "").strip(),
                "fs_pct": r.get("FS % Complete", "").strip(),
                "tdd_pct": r.get("S/4 TDD % Complete", "").strip(),
                "build_pct": r.get("S/4 Build & TUT % Complete", "").strip(),
                "fut_pct": r.get("FUT % Complete", "").strip(),
            })
    return rows


def _load_raids(csv_path: Path) -> list[dict]:
    if not csv_path.exists():
        return []
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            status = r.get("Status", "").strip()
            if status.lower() in ("complete", "closed", "cancelled"):
                continue
            tower = _normalize_tower(r.get("Assigned To (Team)", ""))
            rows.append({
                "raid_id": r.get("RAID ID", r.get("Original RAID ID", "")).strip(),
                "title": r.get("Title", "").strip(),
                "category": r.get("RAID Type", "").strip(),
                "severity": r.get("RAID Severity", "").strip(),
                "status": status,
                "tower": tower,
                "due_date": r.get("Due Date", "").strip(),
            })
    return rows


# ---------------------------------------------------------------------------
# Compute tower stats
# ---------------------------------------------------------------------------
def _tower_stats(tower_short: str, objects: list[dict], raids: list[dict]) -> dict:
    tower_objs = [o for o in objects if o["tower"] == tower_short]
    tower_raids = [r for r in raids if r["tower"] == tower_short]

    total = len(tower_objs)
    completed = sum(1 for o in tower_objs if o["status"] in _COMPLETED_STATUSES)
    rejected = sum(1 for o in tower_objs if o["status"] in _REJECTED_STATUSES)
    active = total - completed - rejected

    type_counts = Counter(o["type_code"] for o in tower_objs)

    def _avg(key: str) -> int:
        vals = [_safe_float(o[key]) for o in tower_objs]
        return round(sum(vals) / len(vals)) if vals else 0

    # RICEFW summary string
    parts = []
    for code, label in [("I", "Interfaces"), ("C", "Conversions"), ("E", "Enhancements"),
                        ("R", "Reports"), ("F", "Forms"), ("W", "Workflows")]:
        n = type_counts.get(code, 0)
        if n:
            parts.append(f"{n} {label}")

    # Highest severity RAID
    severity_order = {"p0": 0, "p1": 1, "p2": 2, "p3": 3}
    highest = None
    for r in tower_raids:
        sev = r["severity"].lower()
        if sev in severity_order:
            if highest is None or severity_order[sev] < severity_order.get(highest.lower(), 99):
                highest = r["severity"]

    # Count documents
    tower_dir = TOWERS_DIR / tower_short
    sad_count = 0
    ricefw_doc_count = 0
    testing_doc_count = 0
    if tower_dir.exists():
        for p in tower_dir.rglob("*-Architecture.md"):
            sad_count += 1
        for p in tower_dir.rglob("*-RICEFW-Tracker.md"):
            ricefw_doc_count += 1
        for p in tower_dir.rglob("*-Testing-Report.md"):
            testing_doc_count += 1

    return {
        "short": tower_short,
        "name": _TOWER_DISPLAY.get(tower_short, tower_short),
        "total": total,
        "completed": completed,
        "active": active,
        "rejected": rejected,
        "completed_pct": round(completed / total * 100) if total else 0,
        "interfaces": type_counts.get("I", 0),
        "conversions": type_counts.get("C", 0),
        "enhancements": type_counts.get("E", 0),
        "reports": type_counts.get("R", 0),
        "forms": type_counts.get("F", 0),
        "workflows": type_counts.get("W", 0),
        "ricefw_summary": ", ".join(parts) if parts else "No RICEFW objects",
        "avg_fs": _avg("fs_pct"),
        "avg_tdd": _avg("tdd_pct"),
        "avg_build": _avg("build_pct"),
        "avg_fut": _avg("fut_pct"),
        "raid_count": len(tower_raids),
        "highest_severity": highest or "",
        "sad_count": sad_count,
        "ricefw_doc_count": ricefw_doc_count,
        "testing_doc_count": testing_doc_count,
    }


# ---------------------------------------------------------------------------
# Build context
# ---------------------------------------------------------------------------
def build_dashboard_context(
    objects: list[dict],
    raids: list[dict],
    tower_filter: str = "",
) -> dict:
    """Build the Jinja2 context for a dashboard."""

    towers_to_process = [tower_filter] if tower_filter else _TOWER_ORDER
    tower_data = []
    for t in towers_to_process:
        stats = _tower_stats(t, objects, raids)
        if stats["total"] > 0 or tower_filter:
            tower_data.append(stats)

    # Program-level aggregation
    total_objects = sum(t["total"] for t in tower_data)
    completed_count = sum(t["completed"] for t in tower_data)
    active_count = sum(t["active"] for t in tower_data)
    rejected_count = sum(t["rejected"] for t in tower_data)

    type_totals = Counter()
    for t in tower_data:
        for code in ["I", "C", "E", "R", "F", "W"]:
            type_totals[code] += t.get(code.lower() + "s" if code != "I" else "interfaces", 0)
    # Fix: map codes to stat keys
    type_totals = {"I": 0, "C": 0, "E": 0, "R": 0, "F": 0, "W": 0}
    for t in tower_data:
        type_totals["I"] += t["interfaces"]
        type_totals["C"] += t["conversions"]
        type_totals["E"] += t["enhancements"]
        type_totals["R"] += t["reports"]
        type_totals["F"] += t["forms"]
        type_totals["W"] += t["workflows"]

    # Type-level rows
    type_rows = []
    for code in ["I", "C", "E", "R", "F", "W"]:
        code_objs = [o for o in objects if o["type_code"] == code
                     and (not tower_filter or o["tower"] == tower_filter)]
        if not code_objs:
            continue
        tc = len(code_objs)
        tc_completed = sum(1 for o in code_objs if o["status"] in _COMPLETED_STATUSES)
        tc_rejected = sum(1 for o in code_objs if o["status"] in _REJECTED_STATUSES)
        tc_active = tc - tc_completed - tc_rejected
        type_rows.append({
            "label": _TYPE_LABEL.get(code, code),
            "total": tc,
            "completed": tc_completed,
            "active": tc_active,
            "rejected": tc_rejected,
            "completed_pct": round(tc_completed / tc * 100) if tc else 0,
        })

    # Count capabilities from directory structure
    cap_count = 0
    for t in towers_to_process:
        tower_dir = TOWERS_DIR / t
        if tower_dir.exists():
            for l1 in tower_dir.iterdir():
                if l1.is_dir() and not l1.name.startswith(("output", ".", "_")):
                    for cap in l1.iterdir():
                        if cap.is_dir():
                            cap_count += 1

    # Avg phase completion
    def _program_avg(key: str) -> int:
        vals = [_safe_float(o[key]) for o in objects
                if not tower_filter or o["tower"] == tower_filter]
        return round(sum(vals) / len(vals)) if vals else 0

    # Top RAID items (P0/P1)
    top_raids = [r for r in raids if r["severity"].lower() in ("p0", "p1")
                 and (not tower_filter or r["tower"] == tower_filter)]

    # Title
    if tower_filter:
        title_text = f"{_TOWER_DISPLAY.get(tower_filter, tower_filter)} ({tower_filter})"
        cover_path = "../../templates/assets/cover_banner.svg"
    else:
        title_text = "IDM 2.0 — All Towers"
        cover_path = "templates/assets/cover_banner.svg"

    return {
        "title": title_text,
        "cover_banner_path": cover_path,
        "release_name": "Release 3",
        "generated_date": datetime.now().strftime("%B %Y"),
        "author": "Sajiv Francis",
        "towers": tower_data,
        "program": {
            "total_objects": total_objects,
            "completed_count": completed_count,
            "completed_pct": round(completed_count / total_objects * 100) if total_objects else 0,
            "active_count": active_count,
            "rejected_count": rejected_count,
            "tower_count": len(tower_data),
            "capability_count": cap_count,
            "avg_fs": _program_avg("fs_pct"),
            "avg_build": _program_avg("build_pct"),
            "avg_fut": _program_avg("fut_pct"),
            "raid_count": sum(t["raid_count"] for t in tower_data),
            "type_totals": type_totals,
            "type_rows": type_rows,
            "total_sads": sum(t["sad_count"] for t in tower_data),
            "total_ricefw_docs": sum(t["ricefw_doc_count"] for t in tower_data),
            "total_testing_docs": sum(t["testing_doc_count"] for t in tower_data),
        },
        "top_raids": top_raids,
    }


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------
def generate_dashboard(
    objects: list[dict],
    raids: list[dict],
    jinja_env: Environment,
    tower_filter: str = "",
    dry_run: bool = False,
) -> list[Path]:
    template = jinja_env.get_template(DASHBOARD_TEMPLATE)
    outputs = []

    # All-towers dashboard
    if not tower_filter:
        ctx = build_dashboard_context(objects, raids)
        rendered = template.render(**ctx)

        out_dir = WORKSPACE / "output" / "docs" / "dashboard"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "Program-Dashboard.md"

        if dry_run:
            print(f"  [DRY-RUN] Would write: {out_path} ({len(rendered):,} chars)")
        else:
            out_path.write_text(rendered, encoding="utf-8")
            print(f"  Wrote: {out_path}")
        outputs.append(out_path)

    # Per-tower dashboards
    towers = [tower_filter] if tower_filter else _TOWER_ORDER
    for t in towers:
        tower_dir = TOWERS_DIR / t
        if not tower_dir.exists():
            continue

        ctx = build_dashboard_context(objects, raids, tower_filter=t)
        rendered = template.render(**ctx)

        out_dir = tower_dir / "output" / "docs" / "dashboard"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{t}-Dashboard.md"

        if dry_run:
            print(f"  [DRY-RUN] Would write: {out_path} ({len(rendered):,} chars)")
        else:
            out_path.write_text(rendered, encoding="utf-8")
            print(f"  Wrote: {out_path}")
        outputs.append(out_path)

    return outputs


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Program Dashboard")
    parser.add_argument("--tower", type=str, help="Tower shortcode (single tower only)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    print("Loading Object Tracker...")
    objects = _load_objects(OBJECT_TRACKER_CSV)
    print(f"  Loaded {len(objects):,} objects")

    print("Loading RAID Log...")
    raids = _load_raids(RAID_CSV)
    print(f"  Loaded {len(raids):,} open RAID items")

    # Jinja2
    jinja_env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    def _tablecell(value, max_len: int = 80) -> str:
        if not value:
            return ""
        s = str(value).replace("\r\n", " ").replace("\n", " ").replace("|", "/")
        s = " ".join(s.split())
        if len(s) > max_len:
            s = s[: max_len - 3] + "..."
        return s

    jinja_env.filters["tc"] = _tablecell

    outputs = generate_dashboard(objects, raids, jinja_env,
                                 tower_filter=args.tower or "", dry_run=args.dry_run)
    print(f"\nGenerated {len(outputs)} dashboard(s)")


if __name__ == "__main__":
    main()
