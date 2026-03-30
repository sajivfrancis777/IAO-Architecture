"""gen_testing_report.py — Generate Testing & Quality Reports per tower and capability.

Sources data from:
  - Smartsheet Object Tracker (build/FUT completion percentages) — always available
  - JIRA (test cases, defects, sprints) — when JIRA_* credentials are provisioned

Usage:
    python scripts/gen_testing_report.py --all
    python scripts/gen_testing_report.py --tower FPR
    python scripts/gen_testing_report.py --tower FPR --cap DS-020
    python scripts/gen_testing_report.py --all --dry-run
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"
TEMPLATES_DIR = WORKSPACE / "templates"
OBJECT_TRACKER_CSV = WORKSPACE / "data" / "smartsheet" / "object_trackers" / "s4_r3_object_tracker.csv"
RAID_CSV = WORKSPACE / "data" / "smartsheet" / "raid" / "master_raid_log.csv"

TESTING_TEMPLATE = "testing_report.md.j2"

_COMPLETED_STATUSES = {"10. object complete", "10. Object Complete"}
_REJECTED_STATUSES = {"99. rejected/cancelled/on hold", "99. Rejected/Cancelled/On Hold"}

# Tower normalization
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


def _pct_display(val: str) -> str:
    pct = _safe_float(val)
    return f"{int(pct)}%" if pct > 0 else "—"


def _fut_status(pct_val: str, overall: str) -> str:
    pct = _safe_float(pct_val)
    if pct >= 100:
        return "Complete"
    if overall.lower() in ("off track", "off-track"):
        return "Off Track"
    if pct > 0:
        return "In Progress"
    return "Not Started"


# ---------------------------------------------------------------------------
# Data loading (reuses same CSV as RICEFW tracker)
# ---------------------------------------------------------------------------
def _load_objects(csv_path: Path) -> list[dict]:
    if not csv_path.exists():
        return []
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            tower = _normalize_tower(r.get("Tower Name", ""))
            obj_id = r.get("Object ID", "").strip()
            if not tower or not obj_id:
                continue
            otype = r.get("Object Type", "").strip()
            rows.append({
                "object_id": obj_id,
                "type_code": _type_code(otype),
                "description": r.get("Description", "").strip(),
                "tower": tower,
                "sub_tower": r.get("Sub-Tower Name", "").strip(),
                "status": r.get("Object Status", "").strip(),
                "source_system": r.get("Source System", "").strip(),
                "target_system": r.get("Target System", "").strip(),
                "fs_pct": r.get("FS % Complete", "").strip(),
                "tdd_pct": r.get("S/4 TDD % Complete", "").strip(),
                "build_pct": r.get("S/4 Build & TUT % Complete", "").strip(),
                "fut_pct": r.get("FUT % Complete", "").strip(),
                "overall_status": r.get("FUT On Track/ Off Track", "").strip(),
            })
    return rows


def _load_raids(csv_path: Path) -> list[dict]:
    if not csv_path.exists():
        return []
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
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
# Build context
# ---------------------------------------------------------------------------
def build_context(
    tower_short: str,
    all_objects: list[dict],
    all_raids: list[dict],
    cap_id: str = "",
    cap_name: str = "",
    l1_process: str = "",
) -> dict:
    """Build Jinja2 context for a Testing Report."""

    # Check JIRA connectivity
    jira_connected = bool(
        os.environ.get("JIRA_BASE_URL")
        and os.environ.get("JIRA_USER_EMAIL")
        and os.environ.get("JIRA_API_TOKEN")
    )

    # Filter objects
    tower_objs = [o for o in all_objects if o["tower"] == tower_short]

    # Capability-level filtering (best-effort: prefix match or sub_tower match)
    if cap_id:
        cap_prefix = cap_id.replace("-", "")[:4].upper()
        cap_objs = [
            o for o in tower_objs
            if o["object_id"].replace("-", "").upper().startswith(cap_prefix)
            or cap_id.lower() in o.get("sub_tower", "").lower()
        ]
        # Fall back to full tower data if no capability-specific match
        if cap_objs:
            tower_objs = cap_objs

    total = len(tower_objs)
    completed = [o for o in tower_objs if o["status"] in _COMPLETED_STATUSES]
    rejected = [o for o in tower_objs if o["status"] in _REJECTED_STATUSES]

    # Phase averages
    def _avg(key: str) -> int:
        vals = [_safe_float(o[key]) for o in tower_objs]
        return round(sum(vals) / len(vals)) if vals else 0

    def _started_count(key: str) -> int:
        return sum(1 for o in tower_objs if _safe_float(o[key]) > 0)

    avg_fs_pct = _avg("fs_pct")
    avg_tdd_pct = _avg("tdd_pct")
    avg_build_pct = _avg("build_pct")
    avg_fut_pct = _avg("fut_pct")

    fs_started = _started_count("fs_pct")
    tdd_started = _started_count("tdd_pct")
    build_started = _started_count("build_pct")
    fut_started = _started_count("fut_pct")

    # Type coverage (how many of each type have started FUT)
    type_groups = {}
    for o in tower_objs:
        tc = o["type_code"]
        if tc not in type_groups:
            type_groups[tc] = []
        type_groups[tc].append(o)

    type_coverage = []
    for code in ["I", "C", "E", "R", "F", "W"]:
        objs = type_groups.get(code, [])
        if not objs:
            continue
        fut_vals = [_safe_float(o["fut_pct"]) for o in objs]
        build_vals = [_safe_float(o["build_pct"]) for o in objs]
        type_coverage.append({
            "label": _TYPE_LABEL.get(code, code),
            "total": len(objs),
            "fut_started": sum(1 for v in fut_vals if v > 0),
            "fut_avg": round(sum(fut_vals) / len(fut_vals)) if fut_vals else 0,
            "build_avg": round(sum(build_vals) / len(build_vals)) if build_vals else 0,
        })

    # FUT objects (active with some FUT progress)
    fut_objects = []
    for o in tower_objs:
        if o["status"] in _COMPLETED_STATUSES or o["status"] in _REJECTED_STATUSES:
            continue
        fut_objects.append({
            "object_id": o["object_id"],
            "type_code": o["type_code"],
            "description": o["description"],
            "fut_display": _pct_display(o["fut_pct"]),
            "fut_status": _fut_status(o["fut_pct"], o["overall_status"]),
            "build_display": _pct_display(o["build_pct"]),
        })

    # RAID items for this tower
    tower_raids = [r for r in all_raids if r["tower"] == tower_short]

    # Title
    tower_display = _TOWER_DISPLAY.get(tower_short, tower_short)
    if cap_id:
        title = f"{cap_id} — {cap_name or cap_id}" if cap_name else cap_id
        scope_label = "capability"
        cover_banner_path = "../../../../../../../templates/assets/cover_banner.svg"
    else:
        title = f"{tower_display} ({tower_short})"
        scope_label = "tower"
        cover_banner_path = "../../templates/assets/cover_banner.svg"

    ctx = {
        "title": title,
        "tower_name": tower_display,
        "tower_short": tower_short,
        "cap_id": cap_id,
        "cap_name": cap_name,
        "l1_process": l1_process,
        "release_name": "Release 3",
        "generated_date": datetime.now().strftime("%B %Y"),
        "author": "Sajiv Francis",
        "cover_banner_path": cover_banner_path,
        "scope_label": scope_label,
        "jira_connected": jira_connected,
        "total_objects": total,
        "completed_count": len(completed),
        "completed_pct": round(len(completed) / total * 100) if total else 0,
        "tested_count": fut_started,
        "tested_pct": round(fut_started / total * 100) if total else 0,
        "avg_fs_pct": avg_fs_pct,
        "avg_tdd_pct": avg_tdd_pct,
        "avg_build_pct": avg_build_pct,
        "avg_fut_pct": avg_fut_pct,
        "fs_started_count": fs_started,
        "tdd_started_count": tdd_started,
        "build_started_count": build_started,
        "fut_started_count": fut_started,
        "type_coverage": type_coverage,
        "fut_objects": fut_objects,
        "raid_items": tower_raids,
        "raid_count": len(tower_raids),
        # JIRA placeholders (populated when connected)
        "test_summary": {"total": 0, "passed": 0, "failed": 0, "blocked": 0,
                         "not_run": 0, "pass_pct": 0, "fail_pct": 0,
                         "blocked_pct": 0, "not_run_pct": 0},
        "defect_summary": {"total": 0, "open": 0, "in_progress": 0,
                           "resolved": 0, "critical": 0},
        "defect_by_severity": [],
        "defect_aging": [],
        "open_defects": [],
        "integration_tests": [],
        "uat_tests": [],
        "sprints": [],
        "uat_signoff_status": "⏳ Pending",
        "blocker_count": 0,
    }

    return ctx


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------
def generate_tower_report(
    tower_short: str,
    all_objects: list[dict],
    all_raids: list[dict],
    jinja_env: Environment,
    cap_filter: str = "",
    dry_run: bool = False,
) -> list[Path]:
    tower_dir = TOWERS_DIR / tower_short
    if not tower_dir.exists():
        for d in TOWERS_DIR.iterdir():
            if d.is_dir() and d.name.upper().startswith(tower_short):
                tower_dir = d
                break
        else:
            print(f"  SKIP: Tower directory not found for {tower_short}")
            return []

    template = jinja_env.get_template(TESTING_TEMPLATE)
    outputs = []

    # Tower-level report
    if not cap_filter:
        ctx = build_context(tower_short, all_objects, all_raids)
        rendered = template.render(**ctx)

        out_dir = tower_dir / "output" / "docs" / "testing-report"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{tower_short}-Testing-Report.md"

        if dry_run:
            print(f"  [DRY-RUN] Would write: {out_path} ({len(rendered):,} chars)")
        else:
            out_path.write_text(rendered, encoding="utf-8")
            print(f"  Wrote: {out_path}")
        outputs.append(out_path)

    # Capability-level reports (scan tower directory for L1/cap structure)
    for l1_dir in sorted(tower_dir.iterdir()):
        if not l1_dir.is_dir() or l1_dir.name.startswith(("output", ".", "_")):
            continue
        for cap_dir in sorted(l1_dir.iterdir()):
            if not cap_dir.is_dir():
                continue
            cid = cap_dir.name
            if cap_filter and cid != cap_filter:
                continue

            ctx = build_context(
                tower_short, all_objects, all_raids,
                cap_id=cid,
                cap_name=cid,
                l1_process=l1_dir.name,
            )

            rendered = template.render(**ctx)

            out_dir = cap_dir / "output" / "docs" / "testing-report"
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{cid}-Testing-Report.md"

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
    parser = argparse.ArgumentParser(description="Generate Testing & Quality Reports")
    parser.add_argument("--tower", type=str, help="Tower shortcode (e.g. FPR)")
    parser.add_argument("--cap", type=str, help="Single capability ID")
    parser.add_argument("--all", action="store_true", help="Generate for all towers")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    if not args.tower and not args.all:
        parser.error("Specify --tower SHORTCODE or --all")

    print("Loading Object Tracker...")
    all_objects = _load_objects(OBJECT_TRACKER_CSV)
    print(f"  Loaded {len(all_objects):,} objects")

    print("Loading RAID Log...")
    all_raids = _load_raids(RAID_CSV)
    print(f"  Loaded {len(all_raids):,} open RAID items")

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

    if args.all:
        towers = sorted(d.name for d in TOWERS_DIR.iterdir() if d.is_dir())
        all_outputs = []
        for t in towers:
            print(f"\n{'='*60}")
            print(f"Tower: {t}")
            outputs = generate_tower_report(t, all_objects, all_raids, jinja_env,
                                            dry_run=args.dry_run)
            all_outputs.extend(outputs)
        print(f"\n{'='*60}")
        print(f"TOTAL: {len(all_outputs)} testing report(s) generated")
    else:
        generate_tower_report(args.tower, all_objects, all_raids, jinja_env,
                              cap_filter=args.cap or "", dry_run=args.dry_run)


if __name__ == "__main__":
    main()
