"""gen_dashboard.py — Generate interactive HTML dashboards with Plotly charts.

Aggregates data from the Smartsheet Object Tracker + RAID logs to produce:
  - All-towers program dashboard (Plotly bar/pie/sankey/line charts)
  - Per-tower dashboard with capability drill-down
  - Click-through navigation to SAD, RICEFW Tracker, and Testing Report docs

Usage:
    python scripts/gen_dashboard.py
    python scripts/gen_dashboard.py --tower FPR
    python scripts/gen_dashboard.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import json
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
OBJECT_TRACKER_CSV = WORKSPACE / "data" / "smartsheet" / "manual" / "object_trackers" / "s4_r3_object_tracker.csv"
RAID_CSV = WORKSPACE / "data" / "smartsheet" / "api" / "raid" / "master_raid_log.csv"

DASHBOARD_TEMPLATE = "dashboard.html.j2"

_COMPLETED_STATUSES = {"10. object complete", "10. Object Complete"}
_REJECTED_STATUSES = {"99. rejected/cancelled/on hold", "99. Rejected/Cancelled/On Hold"}

# Tower metadata loaded from centralized registry (config/tower_registry.json)
import sys as _sys
_sys.path.insert(0, str(WORKSPACE))
from src.tower_registry import normalize_tower as _normalize_tower_reg, TOWER_ORDER as _TOWER_ORDER, TOWER_DISPLAY as _TOWER_DISPLAY

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
    import re as _re
    m = _re.search(r'R(\d)', raw, _re.IGNORECASE)
    return f"R{m.group(1)}" if m else "Unknown"


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
                "sub_tower": r.get("Sub-Tower Name", "").strip(),
                "status": r.get("Object Status", "").strip(),
                "release": _normalize_release(r.get("Release Name", "").strip()),
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
# Architecture data — scan tower dirs for flows, lanes, capabilities, SADs
# ---------------------------------------------------------------------------
JIRA_CACHE = WORKSPACE / "data" / "jira" / "jira_cache.json"


def _load_architecture_data(towers: list[str]) -> dict:
    """Derive architecture metrics from the tower directory structure."""
    tower_stats = {}
    all_patterns: Counter = Counter()

    for t in towers:
        tower_dir = TOWERS_DIR / t
        if not tower_dir.exists():
            continue
        flows = 0
        lanes = 0
        caps = 0
        systems = 0
        sads = 0
        for l1_dir in tower_dir.iterdir():
            if not l1_dir.is_dir() or l1_dir.name.startswith(("output", ".", "_")):
                continue
            lanes += 1  # each L1 directory = a process lane
            for cap_dir in l1_dir.iterdir():
                if not cap_dir.is_dir():
                    continue
                caps += 1
                bpmn_dir = cap_dir / "input" / "bpmn"
                data_dir = cap_dir / "input" / "data"
                if bpmn_dir.exists():
                    flows += len(list(bpmn_dir.glob("*.bpmn")))
                if data_dir.exists():
                    systems += len(list(data_dir.glob("*Flows.xlsx")))
                sad_dir = cap_dir / "output" / "docs" / "systems-architecture"
                if sad_dir and sad_dir.exists():
                    sads += len(list(sad_dir.glob("*-Architecture.*")))
        tower_stats[t] = {
            "flows": flows,
            "lanes": lanes,
            "capabilities": caps,
            "systems": systems,
            "sads": sads,
        }

    # Derive integration patterns from object tracker type codes
    # (will be enriched with actual objects in build_dashboard_context)
    return {
        "towers": tower_stats,
        "patterns": dict(all_patterns) if all_patterns else {},
        "total_flows": sum(s["flows"] for s in tower_stats.values()),
        "total_systems": sum(s["systems"] for s in tower_stats.values()),
        "total_lanes": sum(s["lanes"] for s in tower_stats.values()),
        "total_caps": sum(s["capabilities"] for s in tower_stats.values()),
        "total_sads": sum(s["sads"] for s in tower_stats.values()),
    }


# ---------------------------------------------------------------------------
# JIRA / Testing data — load from jira_cache.json
# ---------------------------------------------------------------------------
def _load_jira_data(tower_filter: str = "") -> dict:
    """Load JIRA defect + test case data for the Testing pillar."""
    if not JIRA_CACHE.exists():
        return {}
    with open(JIRA_CACHE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    # Pick the right summary level
    if tower_filter and tower_filter in cache.get("tower_summaries", {}):
        summary = cache["tower_summaries"][tower_filter]
    else:
        summary = cache.get("cross_tower_summary", {})

    defect = summary.get("defect", {})
    ds = defect.get("defect_summary", {})

    total_defects = ds.get("total", 0)
    open_count = ds.get("open", 0) + ds.get("in_progress", 0)
    resolved = ds.get("resolved", 0)
    critical_open = 0

    # Severity breakdown for stacked bar — tower-level
    defects_by_severity: dict[str, dict[str, int]] = {}
    tower_keys = list(cache.get("tower_summaries", {}).keys()) if not tower_filter else [tower_filter]
    for sev_row in defect.get("defect_by_severity", []):
        sev = sev_row.get("severity", "")
        if sev == "Critical":
            critical_open += sev_row.get("open", 0) + sev_row.get("in_progress", 0)
        if sev not in defects_by_severity:
            defects_by_severity[sev] = {}
        if tower_filter:
            defects_by_severity[sev][tower_filter] = sev_row.get("open", 0) + sev_row.get("in_progress", 0)
        else:
            # Cross-tower: populate per tower
            for tw in cache.get("tower_summaries", {}):
                tw_sev = [s for s in cache["tower_summaries"][tw].get("defect", {}).get("defect_by_severity", [])
                          if s.get("severity") == sev]
                if tw_sev:
                    defects_by_severity[sev][tw] = tw_sev[0].get("open", 0) + tw_sev[0].get("in_progress", 0)

    # Aging buckets
    aging = {}
    for a_row in defect.get("defect_aging", []):
        bucket = a_row.get("bucket", "")
        aging[bucket] = sum(a_row.get(s, 0) for s in ("critical", "high", "medium", "low"))

    # Test execution (from test_cases if available)
    test_cases = cache.get("test_cases", [])
    if tower_filter:
        test_cases = [tc for tc in test_cases if tc.get("tower") == tower_filter]
    execution: Counter = Counter()
    total_tests = len(test_cases)
    for tc in test_cases:
        status = tc.get("status", "Not Executed") or "Not Executed"
        execution[status] += 1
    pass_count = execution.get("Pass", 0)

    # Go/No-Go logic: GO if pass rate >= 95% AND critical_open == 0
    if total_tests > 0:
        pass_pct = round(pass_count / total_tests * 100)
    else:
        pass_pct = 0
    closure_rate = f"{round(resolved / total_defects * 100)}%" if total_defects else "N/A"
    go_nogo = "GO" if (pass_pct >= 95 and critical_open == 0) else "NO-GO"

    # Open defects list (Critical + High)
    open_defects = defect.get("open_defects", [])

    # Defects by tower (open only)
    defects_by_tower = {}
    if not tower_filter:
        for tw, tw_data in cache.get("tower_summaries", {}).items():
            tw_ds = tw_data.get("defect", {}).get("defect_summary", {})
            defects_by_tower[tw] = tw_ds.get("open", 0) + tw_ds.get("in_progress", 0)

    return {
        "total_defects": total_defects,
        "total_tests": total_tests,
        "pass_pct": pass_pct,
        "critical_open": critical_open,
        "closure_rate": closure_rate,
        "go_nogo": go_nogo,
        "defects_by_severity": defects_by_severity,
        "towers": tower_keys if not tower_filter else [tower_filter],
        "execution": dict(execution) if execution else {"Not Executed": total_tests or 1},
        "aging": aging,
        "open_defects": open_defects,
        "defects_by_tower": defects_by_tower,
    }


_CLOSED_DEFECT_STATUSES = {"completed", "canceled", "invalid bug/issue creation"}


def _load_raw_jira(tower_filter: str = "") -> tuple[list[dict], list[dict]]:
    """Load compact raw test-case & defect arrays for client-side filtering."""
    if not JIRA_CACHE.exists():
        return [], []
    with open(JIRA_CACHE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    raw_tests = []
    for tc in cache.get("test_cases", []):
        tw = tc.get("tower", "Unmapped")
        if tower_filter and tw != tower_filter:
            continue
        raw_tests.append({"t": tw, "s": tc.get("status", "Not Executed") or "Not Executed"})

    raw_defects = []
    for d in cache.get("defects", []):
        tw = d.get("tower", "Unmapped")
        if tower_filter and tw != tower_filter:
            continue
        st = d.get("status", "")
        is_open = 0 if st.lower() in _CLOSED_DEFECT_STATUSES else 1
        raw_defects.append({
            "t": tw,
            "v": d.get("severity", "Unknown"),
            "o": is_open,
            "c": d.get("created", ""),
        })

    return raw_tests, raw_defects


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
# Document inventory — scan for 3 docs per capability
# ---------------------------------------------------------------------------
def _scan_doc_inventory(tower_short: str, base_url: str = "") -> list[dict]:
    """Scan a tower directory for SAD, RICEFW, and Testing docs per capability."""
    tower_dir = TOWERS_DIR / tower_short
    if not tower_dir.exists():
        return []
    rows = []
    for l1_dir in sorted(tower_dir.iterdir()):
        if not l1_dir.is_dir() or l1_dir.name.startswith(("output", ".", "_")):
            continue
        for cap_dir in sorted(l1_dir.iterdir()):
            if not cap_dir.is_dir():
                continue
            cap_id = cap_dir.name
            doc_base = cap_dir / "output" / "docs"

            # SAD
            sad_path = None
            sad_dir = doc_base / "systems-architecture"
            if sad_dir.exists():
                sads = list(sad_dir.glob("*-Architecture.html"))
                if not sads:
                    sads = list(sad_dir.glob("*-Architecture.md"))
                if sads:
                    sad_path = sads[0]
            # RICEFW
            ricefw_path = None
            ricefw_dir = doc_base / "ricefw-tracker"
            if ricefw_dir.exists():
                ricefws = list(ricefw_dir.glob("*-RICEFW-Tracker.*"))
                if ricefws:
                    ricefw_path = ricefws[0]
            # Testing
            testing_path = None
            testing_dir = doc_base / "testing-report"
            if testing_dir.exists():
                tests = list(testing_dir.glob("*-Testing-Report.*"))
                if tests:
                    testing_path = tests[0]

            def _page_url(p: Path | None) -> str:
                """Convert a local file path to a Pages-relative URL."""
                if p is None:
                    return ""
                try:
                    rel = p.relative_to(WORKSPACE)
                except ValueError:
                    return ""
                # Pages URLs: from /dashboard/ or /dashboard/TOWER/
                # Tower docs live at /towers/TOWER/...
                # Spaces replaced with hyphens to match deploy-pages.yml sed 's/ /-/g'
                parts = str(rel).replace("\\", "/").replace(" ", "-")
                if base_url:
                    # From /dashboard/TOWER/ -> need ../../towers/...
                    return f"../../{parts}"
                else:
                    # From /dashboard/ -> need ../towers/...
                    return f"../{parts}"

            rows.append({
                "tower": tower_short,
                "cap_id": cap_id,
                "sad_url": _page_url(sad_path),
                "ricefw_url": _page_url(ricefw_path),
                "testing_url": _page_url(testing_path),
            })
    return rows


# ---------------------------------------------------------------------------
# Sankey data builder
# ---------------------------------------------------------------------------
def _build_sankey(towers_data: list[dict], objects: list[dict], tower_filter: str = "") -> dict:
    """Build Sankey node/link data: Towers → RICEFW Types → Statuses."""
    tower_colors = [
        "#0071c5", "#00395d", "#00aeef", "#34a853",
        "#fbbc04", "#ea4335", "#8e44ad", "#e67e22",
    ]
    type_colors = {
        "I": "#0071c5", "C": "#00aeef", "E": "#34a853",
        "R": "#fbbc04", "F": "#8e44ad", "W": "#e67e22",
    }
    status_colors = {"Completed": "#34a853", "Active": "#0071c5", "Rejected": "#ea4335"}

    # Nodes: towers + types + statuses
    tower_labels = [t["short"] for t in towers_data]
    type_labels_ordered = ["Interface", "Conversion", "Enhancement", "Report", "Form", "Workflow"]
    status_labels = ["Completed", "Active", "Rejected"]

    all_labels = tower_labels + type_labels_ordered + status_labels
    all_colors = (
        [tower_colors[i % len(tower_colors)] for i in range(len(tower_labels))]
        + [type_colors.get(l[0], "#999") for l in type_labels_ordered]
        + [status_colors[s] for s in status_labels]
    )

    # Index maps
    idx = {label: i for i, label in enumerate(all_labels)}

    # Links: tower → type
    links_source, links_target, links_value, links_color = [], [], [], []
    filtered = [o for o in objects if not tower_filter or o["tower"] == tower_filter]

    for t in towers_data:
        t_objs = [o for o in filtered if o["tower"] == t["short"]]
        type_counts = Counter(o["type_code"] for o in t_objs)
        for code, label in [("I", "Interface"), ("C", "Conversion"), ("E", "Enhancement"),
                            ("R", "Report"), ("F", "Form"), ("W", "Workflow")]:
            cnt = type_counts.get(code, 0)
            if cnt:
                links_source.append(idx[t["short"]])
                links_target.append(idx[label])
                links_value.append(cnt)
                links_color.append(type_colors.get(code, "#ccc") + "55")

    # Links: type → status
    for label, code in [("Interface", "I"), ("Conversion", "C"), ("Enhancement", "E"),
                        ("Report", "R"), ("Form", "F"), ("Workflow", "W")]:
        type_objs = [o for o in filtered if o["type_code"] == code]
        completed = sum(1 for o in type_objs if o["status"] in _COMPLETED_STATUSES)
        rejected = sum(1 for o in type_objs if o["status"] in _REJECTED_STATUSES)
        active = len(type_objs) - completed - rejected
        for status_label, count, color in [
            ("Completed", completed, "#34a85355"),
            ("Active", active, "#0071c555"),
            ("Rejected", rejected, "#ea433555"),
        ]:
            if count:
                links_source.append(idx[label])
                links_target.append(idx[status_label])
                links_value.append(count)
                links_color.append(color)

    return {
        "node": {"label": all_labels, "color": all_colors},
        "link": {"source": links_source, "target": links_target,
                 "value": links_value, "color": links_color},
    }


# ---------------------------------------------------------------------------
# Build context
# ---------------------------------------------------------------------------
def build_dashboard_context(
    objects: list[dict],
    raids: list[dict],
    tower_filter: str = "",
) -> dict:
    """Build the Jinja2 context for an interactive HTML dashboard."""

    towers_to_process = [tower_filter] if tower_filter else _TOWER_ORDER
    tower_data = []
    for t in towers_to_process:
        stats = _tower_stats(t, objects, raids)
        if stats["total"] > 0 or tower_filter:
            tower_data.append(stats)

    # Architecture & Testing data
    arch_data = _load_architecture_data(towers_to_process)
    # Enrich architecture patterns from objects
    pattern_counts = Counter(o["type_code"] for o in objects
                             if not tower_filter or o["tower"] == tower_filter)
    arch_data["patterns"] = {_TYPE_LABEL.get(k, k): v for k, v in pattern_counts.items() if v}

    testing_data = _load_jira_data(tower_filter)
    raw_tests, raw_defects = _load_raw_jira(tower_filter)

    # Program-level aggregation
    total_objects = sum(t["total"] for t in tower_data)
    completed_count = sum(t["completed"] for t in tower_data)
    active_count = sum(t["active"] for t in tower_data)
    rejected_count = sum(t["rejected"] for t in tower_data)

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

    # Count capabilities
    cap_count = 0
    for t in towers_to_process:
        tower_dir = TOWERS_DIR / t
        if tower_dir.exists():
            for l1 in tower_dir.iterdir():
                if l1.is_dir() and not l1.name.startswith(("output", ".", "_")):
                    for cap in l1.iterdir():
                        if cap.is_dir():
                            cap_count += 1

    def _program_avg(key: str) -> int:
        vals = [_safe_float(o[key]) for o in objects
                if not tower_filter or o["tower"] == tower_filter]
        return round(sum(vals) / len(vals)) if vals else 0

    # Top RAID items (P0/P1)
    top_raids = [r for r in raids if r["severity"].lower() in ("p0", "p1")
                 and (not tower_filter or r["tower"] == tower_filter)]

    # Document inventory (per-capability)
    doc_inventory = []
    for t in towers_to_process:
        doc_inventory.extend(_scan_doc_inventory(t, base_url="" if not tower_filter else t))

    # Sankey data
    sankey = _build_sankey(tower_data, objects, tower_filter)

    # Navigation URLs — use flat Pages structure: /dashboard/, /dashboard/FPR/
    if tower_filter:
        program_url = "../index.html"
    else:
        program_url = ""

    nav_towers = []
    for t_short in _TOWER_ORDER:
        if tower_filter:
            url = f"../{t_short}/index.html"
        else:
            url = f"{t_short}/index.html"
        nav_towers.append({"short": t_short, "dashboard_url": url})

    tower_urls = {}
    for t in nav_towers:
        tower_urls[t["short"]] = t["dashboard_url"]

    # Capability click URLs (map cap_id → its dashboard or first doc)
    cap_urls = {}
    for row in doc_inventory:
        first_url = row.get("sad_url") or row.get("ricefw_url") or row.get("testing_url") or ""
        if first_url:
            cap_urls[row["cap_id"]] = first_url

    # Raw objects for client-side filtering (compact: t=tower, tc=type, s=status, r=release)
    # s: 0=active, 1=completed, 2=rejected
    raw_objects_compact = []
    for o in objects:
        if tower_filter and o["tower"] != tower_filter:
            continue
        s = 1 if o["status"] in _COMPLETED_STATUSES else (2 if o["status"] in _REJECTED_STATUSES else 0)
        raw_objects_compact.append({
            "t": o["tower"], "tc": o["type_code"], "s": s, "r": o.get("release", "Unknown"),
        })

    # Always show R1-R5 in the dropdown; data may only have a subset
    available_releases = ["R1", "R2", "R3", "R4", "R5"]

    # Title
    if tower_filter:
        title_text = f"{_TOWER_DISPLAY.get(tower_filter, tower_filter)} ({tower_filter})"
    else:
        title_text = "IDM 2.0 — All Towers"

    return {
        "title": title_text,
        "release_name": "R1 – R5",
        "available_releases": available_releases,
        "available_releases_json": json.dumps(available_releases),
        "generated_date": datetime.now().strftime("%B %Y"),
        "author": "Sajiv Francis",
        "tower_filter": tower_filter,
        "program_dashboard_url": program_url,
        "nav_towers": nav_towers,
        "towers": tower_data,
        "towers_json": json.dumps(tower_data),
        "type_data_json": json.dumps(type_rows),
        "sankey_json": json.dumps(sankey),
        "tower_urls_json": json.dumps(tower_urls),
        "cap_urls_json": json.dumps(cap_urls),
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
        "doc_inventory": doc_inventory,
        "raw_objects_json": json.dumps(raw_objects_compact),
        "doc_inventory_json": json.dumps(doc_inventory),
        "arch": arch_data,
        "arch_json": json.dumps(arch_data),
        "testing": testing_data,
        "testing_json": json.dumps(testing_data),
        "raw_tests_json": json.dumps(raw_tests),
        "raw_defects_json": json.dumps(raw_defects),
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
        out_path = out_dir / "Program-Dashboard.html"

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
        out_path = out_dir / f"{t}-Dashboard.html"

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
    parser = argparse.ArgumentParser(description="Generate Interactive Program Dashboard")
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
