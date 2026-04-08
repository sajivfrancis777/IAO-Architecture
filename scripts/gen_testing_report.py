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
import json
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"
TEMPLATES_DIR = WORKSPACE / "templates"
OBJECT_TRACKER_CSV = WORKSPACE / "data" / "smartsheet" / "manual" / "object_trackers" / "s4_r3_object_tracker.csv"
RAID_CSV = WORKSPACE / "data" / "smartsheet" / "api" / "raid" / "master_raid_log.csv"
JIRA_CACHE = WORKSPACE / "data" / "jira" / "jira_cache.json"

TESTING_TEMPLATE = "testing_report.md.j2"

_COMPLETED_STATUSES = {"10. object complete", "10. Object Complete"}
_REJECTED_STATUSES = {"99. rejected/cancelled/on hold", "99. Rejected/Cancelled/On Hold"}

# Tower metadata loaded from centralized registry (config/tower_registry.json)
import sys as _sys
_sys.path.insert(0, str(WORKSPACE))
from src.tower_registry import normalize_tower as _normalize_tower_reg, TOWER_DISPLAY as _TOWER_DISPLAY

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
    return _normalize_tower_reg(raw)


def _type_code(raw: str) -> str:
    return _TYPE_CODE.get(raw.strip().lower(), raw[:1].upper() if raw else "?")


def _normalize_release(raw: str) -> str:
    """Normalize release names like '03.R3' → 'R3', '04.R4' → 'R4'."""
    m = re.search(r'R(\d)', raw, re.IGNORECASE)
    return f"R{m.group(1)}" if m else "Unknown"


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
                "release": _normalize_release(r.get("Release Name", "").strip()),
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
# JIRA data loading
# ---------------------------------------------------------------------------
_JIRA_DATA: dict | None = None


def _load_jira_data() -> dict | None:
    """Load cached JIRA data from data/jira/jira_cache.json."""
    global _JIRA_DATA
    if _JIRA_DATA is not None:
        return _JIRA_DATA if _JIRA_DATA else None
    if not JIRA_CACHE.exists():
        _JIRA_DATA = {}  # sentinel: tried but not found
        return None
    try:
        with open(JIRA_CACHE, encoding="utf-8") as f:
            _JIRA_DATA = json.load(f)
        print(f"  Loaded JIRA cache: {len(_JIRA_DATA.get('defects', []))} defects, "
              f"{len(_JIRA_DATA.get('test_cases', []))} test cases")
        return _JIRA_DATA
    except Exception as exc:
        print(f"  WARNING: Failed to load JIRA cache: {exc}")
        _JIRA_DATA = {}
        return None


def _jira_defects_for_tower(jira_data: dict, tower: str) -> list[dict]:
    """Filter defects to a specific tower."""
    return [d for d in jira_data.get("defects", []) if d.get("tower") == tower]


def _jira_tests_for_tower(jira_data: dict, tower: str) -> list[dict]:
    """Filter test cases to a specific tower."""
    return [tc for tc in jira_data.get("test_cases", []) if tc.get("tower") == tower]


def _normalize_jira_release(raw: str) -> str:
    """Normalize JIRA release names like 'Release 3' → 'R3'."""
    m = re.search(r'(\d)', raw)
    return f"R{m.group(1)}" if m else "Unknown"


def _filter_jira_by_release(jira_data: dict, release: str) -> dict:
    """Return a copy of jira_data with defects and test_cases filtered to the given release."""
    filtered = dict(jira_data)
    filtered["defects"] = [
        d for d in jira_data.get("defects", [])
        if _normalize_jira_release(d.get("release", "")) == release
    ]
    filtered["test_cases"] = [
        tc for tc in jira_data.get("test_cases", [])
        if _normalize_jira_release(tc.get("release", "")) == release
    ]
    # Invalidate pre-aggregated summaries so they get rebuilt from filtered data
    filtered.pop("tower_summaries", None)
    filtered.pop("capability_summaries", None)
    filtered.pop("subtower_summaries", None)
    return filtered


def _build_defect_summary(defects: list[dict]) -> dict:
    """Build defect summary metrics from a list of raw defects."""
    _RESOLVED = {"Closed", "Done", "Resolved", "Verified", "Won't Fix", "Duplicate"}
    _IN_PROGRESS = {"In Progress", "In Review", "In Development"}
    total = len(defects)
    resolved = sum(1 for d in defects if d.get("status", "") in _RESOLVED)
    in_progress = sum(1 for d in defects if d.get("status", "") in _IN_PROGRESS)
    open_count = total - resolved - in_progress
    critical = sum(1 for d in defects
                   if (d.get("severity", "") or d.get("priority", "")).lower()
                   in ("critical", "blocker", "1-critical", "s1"))
    return {
        "total": total,
        "open": open_count,
        "in_progress": in_progress,
        "resolved": resolved,
        "critical": critical,
    }


def _build_test_summary(test_cases: list[dict]) -> dict:
    """Build test summary metrics from a list of raw test cases."""
    total = len(test_cases)
    passed = sum(1 for tc in test_cases if tc.get("status", "").lower() in ("pass", "passed"))
    failed = sum(1 for tc in test_cases if tc.get("status", "").lower() in ("fail", "failed"))
    blocked = sum(1 for tc in test_cases if tc.get("status", "").lower() == "blocked")
    not_run = total - passed - failed - blocked
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "blocked": blocked,
        "not_run": not_run,
        "pass_pct": round(passed / total * 100) if total else 0,
        "fail_pct": round(failed / total * 100) if total else 0,
        "blocked_pct": round(blocked / total * 100) if total else 0,
        "not_run_pct": round(not_run / total * 100) if total else 0,
    }


def _get_tower_summary(jira_data: dict, tower: str) -> dict | None:
    """Get pre-computed tower summary from JIRA cache."""
    return jira_data.get("tower_summaries", {}).get(tower)


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
    release_filter: str = "",
) -> dict:
    """Build Jinja2 context for a Testing Report."""

    # Check JIRA data availability (cached JSON from fetch_jira_data.py)
    jira_data = _load_jira_data()
    jira_connected = jira_data is not None and len(jira_data.get("defects", [])) > 0

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
        cover_banner_path = "../../../../../../../templates/assets/testing_banner.svg"
    else:
        title = f"{tower_display} ({tower_short})"
        scope_label = "tower"
        cover_banner_path = "../../templates/assets/testing_banner.svg"

    ctx = {
        "title": title,
        "tower_name": tower_display,
        "tower_short": tower_short,
        "cap_id": cap_id,
        "cap_name": cap_name,
        "l1_process": l1_process,
        "release_name": "R1 – R5",
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
        # JIRA data (populated from cached JSON when available)
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

    # ── Populate JIRA data from cache ────────────────────────────
    if jira_connected and jira_data:
        # Filter JIRA data by release if specified
        jd = _filter_jira_by_release(jira_data, release_filter) if release_filter else jira_data

        jira_sum = None

        if cap_id:
            # Capability-level: try capability_summaries first, then sub-tower match
            jira_sum = jd.get("capability_summaries", {}).get(cap_id)
            if not jira_sum:
                # Try matching by sub-tower name from the objects we found
                sub_towers_found = {o.get("sub_tower", "") for o in tower_objs if o.get("sub_tower")}
                st_summaries = jd.get("subtower_summaries", {})
                for st in sub_towers_found:
                    if st in st_summaries:
                        jira_sum = st_summaries[st]
                        break
        else:
            # Tower-level: use tower_summaries
            jira_sum = _get_tower_summary(jd, tower_short)

        # If release filter removed pre-aggregated summaries, rebuild from raw defects
        if not jira_sum and release_filter:
            tower_defects = _jira_defects_for_tower(jd, tower_short)
            tower_tests = _jira_tests_for_tower(jd, tower_short)
            if tower_defects or tower_tests:
                jira_sum = {
                    "defect": {
                        "defect_summary": _build_defect_summary(tower_defects),
                        "open_defects": [d for d in tower_defects
                                         if d.get("status", "") not in
                                         {"Closed", "Done", "Resolved", "Verified", "Won't Fix", "Duplicate"}],
                    },
                    "test": _build_test_summary(tower_tests),
                }

        if jira_sum:
            # Defect data
            ds = jira_sum.get("defect", {})
            if ds:
                ctx["defect_summary"] = ds.get("defect_summary", ctx["defect_summary"])
                ctx["defect_by_severity"] = ds.get("defect_by_severity", [])
                ctx["defect_aging"] = ds.get("defect_aging", [])
                ctx["open_defects"] = ds.get("open_defects", [])

            # Test case data
            ts = jira_sum.get("test", {})
            if ts:
                ctx["test_summary"] = ts

            # Readiness data
            rd = jira_sum.get("readiness", {})
            if rd:
                ctx["blocker_count"] = rd.get("critical_open", 0)
                if rd.get("critical_open", 0) == 0:
                    ctx["uat_signoff_status"] = "⏳ Pending"
                else:
                    ctx["uat_signoff_status"] = f"❌ {rd['critical_open']} critical blockers"

    # Flag for template: does this capability have any RICEFW or defect data?
    ctx["has_data"] = (total > 0 or ctx["defect_summary"]["total"] > 0
                       or ctx["test_summary"]["total"] > 0)

    return ctx


def _load_cap_names(tower_dir: Path) -> dict[str, str]:
    """Load capability ID → name mapping from tower.yaml."""
    if yaml is None:
        return {}
    yaml_path = tower_dir / "tower.yaml"
    if not yaml_path.exists():
        return {}
    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        caps = data.get("capabilities", [])
        return {c["id"]: c.get("name", c["id"]) for c in caps if "id" in c}
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Page footer injection (matches gen_systems_arch.py pattern)
# ---------------------------------------------------------------------------
_PAGE_BREAK = '<div style="page-break-before: always;"></div>'


def _inject_page_footers(rendered: str, title: str) -> str:
    """Insert page-numbered footers with Back-to-TOC links at every page break."""
    parts = rendered.split(_PAGE_BREAK)
    if len(parts) <= 1:
        return rendered
    result = []
    for i, part in enumerate(parts[:-1]):
        page = i + 1
        footer = (
            f'<div class="page-footer">'
            f'<span>Page {page}</span>'
            f'<span><a href="#toc">\u2191 Back to TOC</a></span>'
            f'<span>{title}</span>'
            f'</div>\n'
            f'{_PAGE_BREAK}'
        )
        result.append(part + footer)
    result.append(parts[-1])
    return "".join(result)


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
    release_label: str = "R1 \u2013 R5",
    release_filter: str = "",
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
    cap_names = _load_cap_names(tower_dir)
    outputs = []

    # Tower-level report
    if not cap_filter:
        ctx = build_context(tower_short, all_objects, all_raids, release_filter=release_filter)
        ctx["release_name"] = release_label
        rendered = template.render(**ctx)
        rendered = _inject_page_footers(rendered, f"{ctx['title']} — Testing Report")

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

            resolved_name = cap_names.get(cid, cid)

            ctx = build_context(
                tower_short, all_objects, all_raids,
                cap_id=cid,
                cap_name=resolved_name,
                l1_process=l1_dir.name,
                release_filter=release_filter,
            )
            ctx["release_name"] = release_label

            rendered = template.render(**ctx)
            rendered = _inject_page_footers(rendered, f"{cid} \u2014 {resolved_name}")

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
    parser.add_argument("--release", type=str, help="Filter by release (e.g. R3, R4)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    if not args.tower and not args.all:
        parser.error("Specify --tower SHORTCODE or --all")

    print("Loading Object Tracker...")
    all_objects = _load_objects(OBJECT_TRACKER_CSV)
    print(f"  Loaded {len(all_objects):,} objects")

    # Filter by release if specified
    if args.release:
        all_objects = [o for o in all_objects if o.get("release") == args.release]
        print(f"  Filtered to {len(all_objects):,} objects for release {args.release}")

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
                                            dry_run=args.dry_run,
                                            release_label=args.release or "R1 \u2013 R5",
                                            release_filter=args.release or "")
            all_outputs.extend(outputs)
        print(f"\n{'='*60}")
        print(f"TOTAL: {len(all_outputs)} testing report(s) generated")
    else:
        generate_tower_report(args.tower, all_objects, all_raids, jinja_env,
                              cap_filter=args.cap or "", dry_run=args.dry_run,
                              release_label=args.release or "R1 \u2013 R5",
                              release_filter=args.release or "")


if __name__ == "__main__":
    main()
