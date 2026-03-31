"""gen_tower_pages.py — Generate enhanced tower landing + capability landing pages.

Produces:
  _site/tower-{TOWER}.html   — tower page with sub-tower RICEFW + JIRA summaries
  _site/cap/{CAP_ID}.html     — capability landing page with 3 document buttons

Data sources:
  - towers/*/tower.yaml (capabilities, L1 process groups)
  - data/smartsheet/object_trackers/s4_r3_object_tracker.csv (RICEFW objects)
  - data/jira/jira_summary.json (defect + test summaries per sub-tower)
  - config/tower_registry.json (tower display metadata)
  - config/subtower_capability_map.json (sub-tower → capability mapping)

Usage:
    python scripts/gen_tower_pages.py                # generate all
    python scripts/gen_tower_pages.py --tower FPR    # one tower only
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────
WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"
SITE_DIR = WORKSPACE / "_site"
CONFIG_DIR = WORKSPACE / "config"
DATA_DIR = WORKSPACE / "data"

REGISTRY_PATH = CONFIG_DIR / "tower_registry.json"
CAP_MAP_PATH = CONFIG_DIR / "subtower_capability_map.json"
OBJECT_TRACKER_PATH = DATA_DIR / "smartsheet" / "object_trackers" / "s4_r3_object_tracker.csv"
JIRA_SUMMARY_PATH = DATA_DIR / "jira" / "jira_summary.json"


# ── Tower registry ───────────────────────────────────────────────

def _load_tower_registry() -> dict:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8")).get("towers", {})
    return {}


def _normalize_tower(raw: str) -> str:
    """Normalize Smartsheet tower names like '03. FPR' to 'FPR'."""
    cleaned = re.sub(r"^\d+[A-Za-z]?\.\s*", "", raw.strip())
    parts = re.split(r"\s*[-–—]\s*", cleaned, maxsplit=1)
    code = parts[0].strip().upper()
    alias_map = {
        "FPR": "FPR", "OTC IF": "OTC-IF", "OTC-IF": "OTC-IF",
        "OTC IP": "OTC-IP", "OTC-IP": "OTC-IP",
        "FTS IF": "FTS-IF", "FTS-IF": "FTS-IF",
        "FTS IP": "FTS-IP", "FTS-IP": "FTS-IP",
        "PTP": "PTP", "MDM": "MDM", "MASTER DATA": "MDM",
        "E2E": "E2E",
    }
    return alias_map.get(code, code)


# ── RICEFW loader ────────────────────────────────────────────────

def _load_ricefw_objects() -> list[dict]:
    """Load Object Tracker CSV, return simplified rows."""
    if not OBJECT_TRACKER_PATH.exists():
        return []
    rows = []
    with open(OBJECT_TRACKER_PATH, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            obj_id = (r.get("Object ID") or "").strip()
            if not obj_id:
                continue
            status_raw = (r.get("Object Status") or "").strip()
            rows.append({
                "object_id": obj_id,
                "tower": _normalize_tower(r.get("Tower Name", "")),
                "sub_tower": (r.get("Sub-Tower Name") or "").strip(),
                "status": status_raw,
                "type": (r.get("Object Type") or "").strip(),
            })
    return rows


def _ricefw_sub_tower_summary(objects: list[dict], tower: str) -> dict[str, dict]:
    """Compute RICEFW counts per sub-tower for a given tower."""
    tower_objs = [o for o in objects if o["tower"] == tower]
    result: dict[str, dict] = {}
    for o in tower_objs:
        st = o["sub_tower"] or "Unknown"
        if st not in result:
            result[st] = {"total": 0, "completed": 0, "pending": 0, "types": defaultdict(int)}
        result[st]["total"] += 1
        if "complete" in o["status"].lower():
            result[st]["completed"] += 1
        else:
            result[st]["pending"] += 1
        # Extract type code (first char of "06.Workflow" → "W")
        type_raw = o.get("type", "")
        type_code = type_raw.strip()[:1].upper() if type_raw else "?"
        type_map = {"0": type_raw.split(".")[-1].strip() if "." in type_raw else type_raw}
        result[st]["types"][type_code] += 1
    # Convert defaultdict to dict for JSON safety
    for st in result:
        result[st]["types"] = dict(result[st]["types"])
    return result


# ── JIRA loader ──────────────────────────────────────────────────

def _load_jira_summary() -> dict:
    if JIRA_SUMMARY_PATH.exists():
        return json.loads(JIRA_SUMMARY_PATH.read_text(encoding="utf-8"))
    return {}


# ── Capability map loader ────────────────────────────────────────

def _load_cap_map() -> dict:
    if CAP_MAP_PATH.exists():
        return json.loads(CAP_MAP_PATH.read_text(encoding="utf-8"))
    return {}


# ── Reverse map: capability → sub-tower ──────────────────────────

def _build_cap_to_subtower(cap_map: dict) -> dict[str, str]:
    result = {}
    for tower_key, st_map in cap_map.items():
        if tower_key.startswith("_"):
            continue
        for sub_tower, cap_ids in st_map.items():
            for cap_id in cap_ids:
                result[cap_id] = sub_tower
    return result


# ── Tower YAML loader ────────────────────────────────────────────

def _load_tower_yaml(tower: str) -> dict:
    import yaml
    yaml_path = TOWERS_DIR / tower / "tower.yaml"
    if not yaml_path.exists():
        return {}
    with open(yaml_path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ── Doc finder ───────────────────────────────────────────────────

def _find_cap_docs(tower: str, l1_name: str, cap_id: str) -> dict[str, str]:
    """Find SAD, RICEFW, and Testing HTML files for a capability."""
    cap_dir = TOWERS_DIR / tower / l1_name / cap_id / "output" / "docs"
    docs: dict[str, str] = {}

    sad_dir = cap_dir / "systems-architecture"
    if sad_dir.exists():
        files = list(sad_dir.glob("*-Architecture.html"))
        if files:
            docs["sad"] = str(files[0].relative_to(WORKSPACE)).replace("\\", "/")

    ricefw_dir = cap_dir / "ricefw-tracker"
    if ricefw_dir.exists():
        files = list(ricefw_dir.glob("*-RICEFW-Tracker.html"))
        if files:
            docs["ricefw"] = str(files[0].relative_to(WORKSPACE)).replace("\\", "/")

    testing_dir = cap_dir / "testing-report"
    if testing_dir.exists():
        files = list(testing_dir.glob("*-Testing-Report.html"))
        if files:
            docs["testing"] = str(files[0].relative_to(WORKSPACE)).replace("\\", "/")

    return docs


# ── HTML generators ──────────────────────────────────────────────

def _badge(text: str, color: str = "#0071c5", bg: str = "#e8f4fd") -> str:
    return (f'<span style="display:inline-block;padding:2px 10px;border-radius:12px;'
            f'font-size:12px;font-weight:600;color:{color};background:{bg};'
            f'margin-right:6px">{text}</span>')


def _summary_bar(ricefw: dict, defects: dict) -> str:
    """Render a compact sub-tower summary bar."""
    parts = []

    total = ricefw.get("total", 0)
    completed = ricefw.get("completed", 0)
    pending = ricefw.get("pending", 0)
    if total:
        pct = round(completed / total * 100) if total else 0
        parts.append(_badge(f"RICEFW: {total} total", "#00285a", "#e8f4fd"))
        parts.append(_badge(f"✅ {completed} complete", "#1a7f37", "#ddf4e4"))
        if pending:
            parts.append(_badge(f"⏳ {pending} pending", "#9a6700", "#fff8c5"))

    ds = defects.get("defect_summary", {})
    d_total = ds.get("total", 0)
    d_open = ds.get("open", 0)
    d_critical = ds.get("critical", 0)
    if d_total:
        parts.append(_badge(f"🐛 {d_total} defects", "#6e4b00", "#fef3cd"))
        if d_critical:
            parts.append(_badge(f"🔴 {d_critical} critical", "#d1242f", "#ffebe9"))
        if d_open:
            parts.append(_badge(f"{d_open} open", "#bf8700", "#fff8c5"))

    ts = defects.get("test", {})
    t_total = ts.get("total", 0)
    if t_total:
        t_passed = ts.get("passed", 0)
        parts.append(_badge(f"🧪 {t_total} tests ({t_passed} passed)", "#0550ae", "#ddf4ff"))

    if not parts:
        parts.append(_badge("Standard solution — no custom RICEFW", "#666", "#f0f2f5"))

    return f'<div style="margin:8px 0 4px;display:flex;flex-wrap:wrap;gap:4px">{"".join(parts)}</div>'


def _extract_title_from_html(html_path: Path) -> str:
    """Extract capability title from generated Architecture HTML <h1>."""
    if not html_path.exists():
        return ""
    try:
        content = html_path.read_text(encoding="utf-8", errors="replace")[:4096]
        m = re.search(r'<h1[^>]*>([^<]+)', content)
        return m.group(1).strip() if m else ""
    except Exception:
        return ""


def generate_tower_page(
    tower: str,
    registry: dict,
    ricefw_objects: list[dict],
    jira_data: dict,
    cap_map: dict,
    cap_to_subtower: dict[str, str],
) -> str:
    """Generate the HTML for a tower landing page."""
    info = registry.get(tower, {})
    full_name = info.get("name", tower)
    desc = info.get("description", "Architecture documents")
    icon = info.get("icon", "📄")

    tower_yaml = _load_tower_yaml(tower)
    capabilities = tower_yaml.get("capabilities", [])

    # Group capabilities by L1 process
    l1_groups: dict[str, list[dict]] = {}
    for cap in capabilities:
        l1 = cap.get("l1", "Other")
        l1_groups.setdefault(l1, []).append(cap)

    # Get RICEFW summaries per sub-tower
    ricefw_by_st = _ricefw_sub_tower_summary(ricefw_objects, tower)

    # Get JIRA subtower_summaries
    jira_st = jira_data.get("subtower_summaries", {})
    jira_tower = jira_data.get("tower_summaries", {}).get(tower, {})

    # Build sub-tower → L1 mapping using cap_map
    tower_cap_map = cap_map.get(tower, {})

    # ── Build HTML ───────────────────────────────────────────────
    cap_count = len(capabilities)
    html_parts = [f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="base-path" content="">
<title>{tower} — IAO Architecture</title>
<link rel="icon" type="image/x-icon" href="favicon.ico">
<style>
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;font-family:"Segoe UI",system-ui,-apple-system,sans-serif;background:#f0f2f5;color:#1a1a2e}}
.topbar{{background:linear-gradient(135deg,#00285a 0%,#0071c5 100%);padding:0 32px;display:flex;align-items:center;height:56px;box-shadow:0 2px 8px rgba(0,0,0,.15);position:fixed;top:0;left:0;right:0;z-index:100}}
.topbar img{{height:36px;margin-right:16px;border-radius:4px}}
.topbar h1{{color:#fff;font-size:18px;font-weight:600;margin:0;letter-spacing:.5px}}
.topbar a.back-link{{color:rgba(255,255,255,.85);text-decoration:none;font-size:14px;margin-left:auto}}
.topbar a.back-link:hover{{color:#fff}}
.topbar .sidebar-toggle{{display:none;background:none;border:none;color:#fff;font-size:22px;cursor:pointer;margin-right:12px;padding:4px 8px}}
.sidebar{{position:fixed;top:56px;left:0;bottom:0;width:280px;background:#fff;border-right:1px solid #e4e8ed;overflow-y:auto;z-index:90;transition:transform .25s ease;padding-bottom:24px}}
.sidebar .search-box{{padding:12px 16px;border-bottom:1px solid #e4e8ed;position:sticky;top:0;background:#fff;z-index:1}}
.sidebar .search-box input{{width:100%;padding:8px 12px 8px 34px;border:1px solid #d0d5dd;border-radius:8px;font-size:13px;outline:none;background:#f8f9fb url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2716%27 height=%2716%27 fill=%27%23999%27 viewBox=%270 0 16 16%27%3E%3Cpath d=%27M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85zm-5.242.156a5 5 0 1 1 0-10 5 5 0 0 1 0 10z%27/%3E%3C/svg%3E") 10px center no-repeat}}
.sidebar .search-box input:focus{{border-color:#0071c5;box-shadow:0 0 0 2px rgba(0,113,197,.15)}}
.sidebar .nav-tree{{padding:8px 0}}
.sidebar .tower-group{{margin-bottom:2px}}
.sidebar .tower-header{{display:flex;align-items:center;padding:8px 16px;font-size:14px;font-weight:600;color:#00285a;cursor:pointer;user-select:none}}
.sidebar .tower-header:hover{{background:#f5f8fc}}
.sidebar .tower-header .arrow{{font-size:10px;margin-right:8px;transition:transform .2s;color:#999}}
.sidebar .tower-header.open .arrow{{transform:rotate(90deg)}}
.sidebar .tower-header .icon{{margin-right:6px}}
.sidebar .tower-header a{{color:inherit;text-decoration:none;flex:1}}
.sidebar .proc-group{{margin-left:16px;display:none}}
.sidebar .tower-header.open+.proc-group,.sidebar .proc-group.search-open{{display:block}}
.sidebar .proc-label{{font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.5px;padding:8px 16px 4px;margin-top:4px}}
.sidebar .cap-link{{display:block;padding:4px 16px 4px 24px;font-size:13px;color:#444;text-decoration:none;border-radius:4px;margin:1px 8px}}
.sidebar .cap-link:hover{{background:#e8f4fd;color:#0071c5}}
.sidebar .cap-link.active{{background:#0071c5;color:#fff;font-weight:600}}
.sidebar .cap-id{{font-weight:600;color:#00285a;margin-right:4px}}
.sidebar .cap-link.active .cap-id{{color:#fff}}
.sidebar .no-results{{padding:16px;font-size:13px;color:#999;text-align:center;font-style:italic}}
.page-body{{margin-top:56px;margin-left:280px;transition:margin-left .25s ease}}
.container{{max-width:1120px;margin:0 auto;padding:24px 24px 48px}}
.breadcrumb{{font-size:13px;color:#666;margin-bottom:20px}}
.breadcrumb a{{color:#0071c5;text-decoration:none}}
.breadcrumb a:hover{{text-decoration:underline}}
.hero{{background:linear-gradient(135deg,#00285a,#0060a9);color:#fff;border-radius:12px;padding:48px 40px;margin-bottom:32px;position:relative;overflow:hidden}}
.hero::after{{content:"";position:absolute;top:0;right:0;width:300px;height:100%;background:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 300 200%27%3E%3Cpath d=%27M0 100L80 100L120 60L200 60L240 100L300 100%27 stroke=%27rgba(255,255,255,.08)%27 fill=%27none%27 stroke-width=%272%27/%3E%3Cpath d=%27M0 140L60 140L100 180L180 180L220 140L300 140%27 stroke=%27rgba(255,255,255,.06)%27 fill=%27none%27 stroke-width=%272%27/%3E%3C/svg%3E") no-repeat center;opacity:.5}}
.hero h2{{font-size:32px;margin:0 0 8px;font-weight:700;position:relative}}
.hero p{{font-size:16px;opacity:.85;margin:0;position:relative}}
.hero .badge{{display:inline-block;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:4px 14px;font-size:12px;margin-top:12px;position:relative}}
.section-title{{font-size:20px;font-weight:700;color:#00285a;margin:32px 0 8px;padding-bottom:8px;border-bottom:2px solid #e4e8ed}}
table{{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.06);border:1px solid #e4e8ed}}
th{{background:#00285a;color:#fff;padding:12px 16px;font-size:13px;font-weight:600;text-align:left;text-transform:uppercase;letter-spacing:.5px}}
td{{padding:10px 16px;border-bottom:1px solid #f0f2f5;font-size:14px}}
tr:last-child td{{border-bottom:none}}
tr:hover td{{background:#f5f8fc}}
td a{{color:#0071c5;text-decoration:none;font-weight:500}}
td a:hover{{text-decoration:underline}}
.footer{{text-align:center;padding:32px 0;font-size:12px;color:#999;border-top:1px solid #e4e8ed;margin-top:48px}}
.doc-btn{{display:inline-flex;align-items:center;gap:6px;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:14px;transition:all .15s;border:1px solid transparent}}
.doc-btn:hover{{transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,.1)}}
.doc-btn.sad{{background:#0071c5;color:#fff;border-color:#0060a9}}
.doc-btn.sad:hover{{background:#0060a9}}
.doc-btn.ricefw{{background:#34a853;color:#fff;border-color:#2d9249}}
.doc-btn.ricefw:hover{{background:#2d9249}}
.doc-btn.testing{{background:#ea4335;color:#fff;border-color:#d33628}}
.doc-btn.testing:hover{{background:#d33628}}
.doc-btn.disabled{{background:#e4e8ed;color:#999;cursor:default;border-color:#d0d5dd}}
.doc-btn.disabled:hover{{transform:none;box-shadow:none}}
.cap-hero{{background:#fff;border:1px solid #e4e8ed;border-radius:12px;padding:32px;margin-bottom:24px;box-shadow:0 1px 4px rgba(0,0,0,.06)}}
.cap-hero h2{{margin:0 0 8px;color:#00285a;font-size:26px}}
.cap-hero p{{color:#666;margin:0 0 16px}}
.summary-panel{{background:#f8f9fb;border:1px solid #e4e8ed;border-radius:10px;padding:16px 20px;margin-bottom:20px}}
.summary-panel h4{{margin:0 0 8px;font-size:14px;color:#00285a;text-transform:uppercase;letter-spacing:.5px}}
@media(max-width:768px){{
  .topbar .sidebar-toggle{{display:block}}
  .sidebar{{transform:translateX(-100%)}}
  .sidebar.open{{transform:translateX(0);box-shadow:4px 0 16px rgba(0,0,0,.15)}}
  .page-body{{margin-left:0}}
  .hero{{padding:28px 20px}}
  .hero h2{{font-size:24px}}
}}
</style>
</head><body>
<div class="topbar">
  <button class="sidebar-toggle" aria-label="Toggle navigation">☰</button>
  <img src="templates/assets/cover_banner.svg" alt="IAO">
  <h1>IAO Architecture Portal</h1>
  <a class="back-link" href="index.html">← All Towers</a>
</div>
<nav class="sidebar">
  <div style="padding:12px 16px 0">
    <a href="index.html" style="display:block;padding:8px 14px;background:#f5f8fc;color:#00285a;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;text-align:center;margin-bottom:4px;border:1px solid #e4e8ed">🏠 Portal Home</a>
    <a href="dashboard/index.html" style="display:block;padding:8px 14px;background:linear-gradient(135deg,#00285a,#0060a9);color:#fff;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;text-align:center;margin-bottom:8px;transition:opacity .15s" onmouseover="this.style.opacity='0.85'" onmouseout="this.style.opacity='1'">📊 Program Dashboard</a>
  </div>
  <div class="search-box"><input type="text" placeholder="Search capabilities..." aria-label="Search capabilities"></div>
  <div class="nav-tree"></div>
  <div class="no-results" style="display:none">No matching capabilities</div>
</nav>
<div class="page-body">
<div class="container">
<div class="breadcrumb"><a href="index.html">Home</a> / <strong>{tower}</strong></div>
<div class="hero">
  <h2>{icon} {tower} — {full_name}</h2>
  <p>{desc}</p>
  <span class="badge">{cap_count} capabilities · Release 3</span>
  <div style="margin-top:16px;display:flex;gap:12px;flex-wrap:wrap">
    <a href="dashboard/{tower}/index.html" style="display:inline-block;padding:8px 20px;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);border-radius:8px;color:#fff;text-decoration:none;font-weight:600;font-size:14px;transition:background .15s" onmouseover="this.style.background='rgba(255,255,255,.3)'" onmouseout="this.style.background='rgba(255,255,255,.18)'">📊 Tower Dashboard</a>
    <a href="dashboard/index.html" style="display:inline-block;padding:8px 20px;background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.25);border-radius:8px;color:rgba(255,255,255,.85);text-decoration:none;font-weight:500;font-size:14px;transition:background .15s" onmouseover="this.style.background='rgba(255,255,255,.2)'" onmouseout="this.style.background='rgba(255,255,255,.1)'">📊 Program Dashboard</a>
  </div>
</div>
"""]

    # ── Tower-level summary ──────────────────────────────────────
    tower_ricefw_total = sum(s["total"] for s in ricefw_by_st.values())
    tower_ricefw_complete = sum(s["completed"] for s in ricefw_by_st.values())
    tower_ricefw_pending = sum(s["pending"] for s in ricefw_by_st.values())
    tower_defect = jira_tower.get("defect", {}).get("defect_summary", {})
    tower_test = jira_tower.get("test", {})

    html_parts.append('<div class="summary-panel">')
    html_parts.append('<h4>Tower Summary</h4>')
    html_parts.append('<div style="display:flex;flex-wrap:wrap;gap:6px">')
    if tower_ricefw_total:
        pct = round(tower_ricefw_complete / tower_ricefw_total * 100) if tower_ricefw_total else 0
        html_parts.append(_badge(f"📋 {tower_ricefw_total} RICEFW objects", "#00285a", "#e8f4fd"))
        html_parts.append(_badge(f"✅ {tower_ricefw_complete} complete ({pct}%)", "#1a7f37", "#ddf4e4"))
        if tower_ricefw_pending:
            html_parts.append(_badge(f"⏳ {tower_ricefw_pending} pending", "#9a6700", "#fff8c5"))
    else:
        html_parts.append(_badge("No RICEFW objects tracked", "#666", "#f0f2f5"))

    d_total = tower_defect.get("total", 0)
    if d_total:
        d_open = tower_defect.get("open", 0)
        d_crit = tower_defect.get("critical", 0)
        html_parts.append(_badge(f"🐛 {d_total} defects", "#6e4b00", "#fef3cd"))
        if d_crit:
            html_parts.append(_badge(f"🔴 {d_crit} critical", "#d1242f", "#ffebe9"))
        if d_open:
            html_parts.append(_badge(f"{d_open} open", "#bf8700", "#fff8c5"))

    t_total = tower_test.get("total", 0)
    if t_total:
        t_passed = tower_test.get("passed", 0)
        html_parts.append(_badge(f"🧪 {t_total} tests ({t_passed} passed)", "#0550ae", "#ddf4ff"))

    html_parts.append('</div></div>')

    # ── Process groups ───────────────────────────────────────────
    for l1_name, caps in l1_groups.items():
        # Find matching sub-towers for this L1 group
        l1_subtowers = set()
        for cap in caps:
            st = cap_to_subtower.get(cap["id"], "")
            if st:
                l1_subtowers.add(st)

        # Aggregate RICEFW for this L1 group
        l1_ricefw = {"total": 0, "completed": 0, "pending": 0}
        l1_defects: dict = {}
        for st in l1_subtowers:
            if st in ricefw_by_st:
                l1_ricefw["total"] += ricefw_by_st[st]["total"]
                l1_ricefw["completed"] += ricefw_by_st[st]["completed"]
                l1_ricefw["pending"] += ricefw_by_st[st]["pending"]
            if st in jira_st:
                # Merge defect counts
                if not l1_defects:
                    l1_defects = jira_st[st]
                else:
                    # Aggregate defect summaries
                    prev_ds = l1_defects.get("defect", {}).get("defect_summary", {})
                    new_ds = jira_st[st].get("defect", {}).get("defect_summary", {})
                    for k in ("total", "open", "in_progress", "resolved", "critical"):
                        prev_ds[k] = prev_ds.get(k, 0) + new_ds.get(k, 0)

        # If no subtower match, try tower-level JIRA data split
        if not l1_defects and not l1_subtowers:
            l1_defects = jira_tower

        html_parts.append(f'<h2 class="section-title">{l1_name} '
                          f'<span style="font-size:14px;color:#666;font-weight:400">'
                          f'({len(caps)} capabilities)</span></h2>')

        # Sub-tower summary bar
        html_parts.append(_summary_bar(l1_ricefw, l1_defects))

        # Capability table
        html_parts.append('<table>\n<tr><th style="width:120px">ID</th><th>Capability</th>'
                          '<th style="width:100px">View</th></tr>')

        for cap in caps:
            cap_id = cap["id"]
            cap_name = cap.get("name", cap_id)
            html_parts.append(
                f'<tr><td><strong>{cap_id}</strong></td>'
                f'<td>{cap_name}</td>'
                f'<td><a href="cap/{tower}-{cap_id}.html">Open →</a></td></tr>'
            )

        html_parts.append('</table>')

    # ── Footer ───────────────────────────────────────────────────
    now = datetime.now(timezone.utc).strftime("%B %Y")
    html_parts.append(f"""
<div style="margin-top:24px"><a href="index.html" style="color:#0071c5;text-decoration:none;font-weight:600">← Back to All Towers</a></div>
<div class="footer">
  IAO Architecture Pipeline · Intel IDM 2.0 · {tower} Tower · Intel Confidential<br>
  Generated: {now}
</div>
</div></div>
""")

    # ── Sidebar JS ─────────────────────────────────────────────
    html_parts.append(_sidebar_js())
    html_parts.append("</body></html>")

    return "\n".join(html_parts)


def generate_capability_page(
    tower: str,
    cap: dict,
    l1_name: str,
    registry: dict,
    ricefw_objects: list[dict],
    jira_data: dict,
    cap_to_subtower: dict[str, str],
) -> str:
    """Generate capability landing page with 3 document buttons."""
    cap_id = cap["id"]
    cap_name = cap.get("name", cap_id)
    info = registry.get(tower, {})
    icon = info.get("icon", "📄")

    docs = _find_cap_docs(tower, l1_name, cap_id)

    # Get RICEFW data for this capability's sub-tower
    sub_tower = cap_to_subtower.get(cap_id, "")
    cap_ricefw = {"total": 0, "completed": 0, "pending": 0}
    cap_objs = []
    if sub_tower:
        for o in ricefw_objects:
            if o["tower"] == tower and o["sub_tower"] == sub_tower:
                cap_objs.append(o)
                cap_ricefw["total"] += 1
                if "complete" in o["status"].lower():
                    cap_ricefw["completed"] += 1
                else:
                    cap_ricefw["pending"] += 1

    # Get JIRA data
    jira_st = jira_data.get("subtower_summaries", {})
    cap_jira = jira_st.get(sub_tower, {}) if sub_tower else {}
    # Fallback to tower level
    if not cap_jira:
        cap_jira = jira_data.get("tower_summaries", {}).get(tower, {})

    now = datetime.now(timezone.utc).strftime("%B %Y")

    # ── Build HTML ───────────────────────────────────────────────
    sad_link = docs.get("sad", "")
    ricefw_link = docs.get("ricefw", "")
    testing_link = docs.get("testing", "")

    def _doc_button(label: str, href: str, cls: str, emoji: str) -> str:
        if href:
            return f'<a href="../{href}" class="doc-btn {cls}">{emoji} {label}</a>'
        return f'<span class="doc-btn disabled">{emoji} {label} (not yet generated)</span>'

    html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="base-path" content="../">
<title>{cap_id} — {cap_name}</title>
<link rel="icon" type="image/x-icon" href="../favicon.ico">
<style>
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;font-family:"Segoe UI",system-ui,-apple-system,sans-serif;background:#f0f2f5;color:#1a1a2e}}
.topbar{{background:linear-gradient(135deg,#00285a 0%,#0071c5 100%);padding:0 32px;display:flex;align-items:center;height:56px;box-shadow:0 2px 8px rgba(0,0,0,.15);position:fixed;top:0;left:0;right:0;z-index:100}}
.topbar img{{height:36px;margin-right:16px;border-radius:4px}}
.topbar h1{{color:#fff;font-size:18px;font-weight:600;margin:0;letter-spacing:.5px}}
.topbar a.back-link{{color:rgba(255,255,255,.85);text-decoration:none;font-size:14px;margin-left:auto}}
.topbar a.back-link:hover{{color:#fff}}
.topbar .sidebar-toggle{{display:none;background:none;border:none;color:#fff;font-size:22px;cursor:pointer;margin-right:12px;padding:4px 8px}}
.sidebar{{position:fixed;top:56px;left:0;bottom:0;width:280px;background:#fff;border-right:1px solid #e4e8ed;overflow-y:auto;z-index:90;transition:transform .25s ease;padding-bottom:24px}}
.sidebar .search-box{{padding:12px 16px;border-bottom:1px solid #e4e8ed;position:sticky;top:0;background:#fff;z-index:1}}
.sidebar .search-box input{{width:100%;padding:8px 12px 8px 34px;border:1px solid #d0d5dd;border-radius:8px;font-size:13px;outline:none;background:#f8f9fb url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2716%27 height=%2716%27 fill=%27%23999%27 viewBox=%270 0 16 16%27%3E%3Cpath d=%27M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85zm-5.242.156a5 5 0 1 1 0-10 5 5 0 0 1 0 10z%27/%3E%3C/svg%3E") 10px center no-repeat}}
.sidebar .search-box input:focus{{border-color:#0071c5;box-shadow:0 0 0 2px rgba(0,113,197,.15)}}
.sidebar .nav-tree{{padding:8px 0}}
.sidebar .tower-group{{margin-bottom:2px}}
.sidebar .tower-header{{display:flex;align-items:center;padding:8px 16px;font-size:14px;font-weight:600;color:#00285a;cursor:pointer;user-select:none}}
.sidebar .tower-header:hover{{background:#f5f8fc}}
.sidebar .tower-header .arrow{{font-size:10px;margin-right:8px;transition:transform .2s;color:#999}}
.sidebar .tower-header.open .arrow{{transform:rotate(90deg)}}
.sidebar .tower-header .icon{{margin-right:6px}}
.sidebar .tower-header a{{color:inherit;text-decoration:none;flex:1}}
.sidebar .proc-group{{margin-left:16px;display:none}}
.sidebar .tower-header.open+.proc-group,.sidebar .proc-group.search-open{{display:block}}
.sidebar .proc-label{{font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.5px;padding:8px 16px 4px;margin-top:4px}}
.sidebar .cap-link{{display:block;padding:4px 16px 4px 24px;font-size:13px;color:#444;text-decoration:none;border-radius:4px;margin:1px 8px}}
.sidebar .cap-link:hover{{background:#e8f4fd;color:#0071c5}}
.sidebar .cap-link.active{{background:#0071c5;color:#fff;font-weight:600}}
.sidebar .cap-id{{font-weight:600;color:#00285a;margin-right:4px}}
.sidebar .cap-link.active .cap-id{{color:#fff}}
.sidebar .no-results{{padding:16px;font-size:13px;color:#999;text-align:center;font-style:italic}}
.page-body{{margin-top:56px;margin-left:280px;transition:margin-left .25s ease}}
.container{{max-width:1120px;margin:0 auto;padding:24px 24px 48px}}
.breadcrumb{{font-size:13px;color:#666;margin-bottom:20px}}
.breadcrumb a{{color:#0071c5;text-decoration:none}}
.breadcrumb a:hover{{text-decoration:underline}}
.cap-hero{{background:#fff;border:1px solid #e4e8ed;border-radius:12px;padding:32px;margin-bottom:24px;box-shadow:0 1px 4px rgba(0,0,0,.06)}}
.cap-hero h2{{margin:0 0 8px;color:#00285a;font-size:26px}}
.cap-hero p{{color:#666;margin:0 0 16px}}
.doc-btn{{display:inline-flex;align-items:center;gap:6px;padding:12px 24px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;transition:all .15s;border:1px solid transparent;margin:6px 8px 6px 0}}
.doc-btn:hover{{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.12)}}
.doc-btn.sad{{background:#0071c5;color:#fff;border-color:#0060a9}}
.doc-btn.sad:hover{{background:#0060a9}}
.doc-btn.ricefw{{background:#34a853;color:#fff;border-color:#2d9249}}
.doc-btn.ricefw:hover{{background:#2d9249}}
.doc-btn.testing{{background:#ea4335;color:#fff;border-color:#d33628}}
.doc-btn.testing:hover{{background:#d33628}}
.doc-btn.disabled{{background:#e4e8ed;color:#999;cursor:default;border-color:#d0d5dd}}
.doc-btn.disabled:hover{{transform:none;box-shadow:none}}
.summary-panel{{background:#f8f9fb;border:1px solid #e4e8ed;border-radius:10px;padding:16px 20px;margin-bottom:20px}}
.summary-panel h4{{margin:0 0 8px;font-size:14px;color:#00285a;text-transform:uppercase;letter-spacing:.5px}}
.footer{{text-align:center;padding:32px 0;font-size:12px;color:#999;border-top:1px solid #e4e8ed;margin-top:48px}}
table{{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.06);border:1px solid #e4e8ed;margin-bottom:20px}}
th{{background:#00285a;color:#fff;padding:10px 16px;font-size:12px;font-weight:600;text-align:left;text-transform:uppercase;letter-spacing:.5px}}
td{{padding:8px 16px;border-bottom:1px solid #f0f2f5;font-size:13px}}
tr:last-child td{{border-bottom:none}}
tr:hover td{{background:#f5f8fc}}
@media(max-width:768px){{
  .topbar .sidebar-toggle{{display:block}}
  .sidebar{{transform:translateX(-100%)}}
  .sidebar.open{{transform:translateX(0);box-shadow:4px 0 16px rgba(0,0,0,.15)}}
  .page-body{{margin-left:0}}
}}
</style>
</head><body>
<div class="topbar">
  <button class="sidebar-toggle" aria-label="Toggle navigation">☰</button>
  <img src="../templates/assets/cover_banner.svg" alt="IAO">
  <h1>IAO Architecture Portal</h1>
  <a class="back-link" href="../tower-{tower}.html">← {tower} Tower</a>
</div>
<nav class="sidebar">
  <div style="padding:12px 16px 0">
    <a href="../index.html" style="display:block;padding:8px 14px;background:#f5f8fc;color:#00285a;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;text-align:center;margin-bottom:4px;border:1px solid #e4e8ed">🏠 Portal Home</a>
    <a href="../dashboard/index.html" style="display:block;padding:8px 14px;background:linear-gradient(135deg,#00285a,#0060a9);color:#fff;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;text-align:center;margin-bottom:8px;transition:opacity .15s" onmouseover="this.style.opacity='0.85'" onmouseout="this.style.opacity='1'">📊 Program Dashboard</a>
  </div>
  <div class="search-box"><input type="text" placeholder="Search capabilities..." aria-label="Search capabilities"></div>
  <div class="nav-tree"></div>
  <div class="no-results" style="display:none">No matching capabilities</div>
</nav>
<div class="page-body">
<div class="container">
<div class="breadcrumb">
  <a href="../index.html">Home</a> / <a href="../tower-{tower}.html">{tower}</a> / <strong>{cap_id}</strong>
</div>

<div class="cap-hero">
  <h2>{icon} {cap_id} — {cap_name}</h2>
  <p>{l1_name}</p>
  <div style="margin-top:16px;display:flex;flex-wrap:wrap">
    {_doc_button("Systems Architecture Document", sad_link, "sad", "📄")}
    {_doc_button("RICEFW Tracker", ricefw_link, "ricefw", "📋")}
    {_doc_button("Testing Report", testing_link, "testing", "🧪")}
  </div>
</div>
"""

    # ── RICEFW summary ─────────────────────────────────────────
    if cap_ricefw["total"]:
        pct = round(cap_ricefw["completed"] / cap_ricefw["total"] * 100) if cap_ricefw["total"] else 0
        html += f"""<div class="summary-panel">
  <h4>RICEFW Objects ({sub_tower})</h4>
  <div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px">
    {_badge(f"📋 {cap_ricefw['total']} objects", "#00285a", "#e8f4fd")}
    {_badge(f"✅ {cap_ricefw['completed']} complete ({pct}%)", "#1a7f37", "#ddf4e4")}
    {'{}'.format(_badge(f"⏳ {cap_ricefw['pending']} pending", "#9a6700", "#fff8c5")) if cap_ricefw['pending'] else ''}
  </div>
  <div style="background:#e4e8ed;border-radius:6px;height:8px;overflow:hidden">
    <div style="background:#34a853;height:100%;width:{pct}%;border-radius:6px;transition:width .5s"></div>
  </div>
</div>
"""

        # Object detail table
        html += """<table>
<tr><th>Object ID</th><th>Type</th><th>Status</th></tr>
"""
        for obj in sorted(cap_objs, key=lambda o: o["object_id"]):
            status_color = "#1a7f37" if "complete" in obj["status"].lower() else "#9a6700"
            html += (f'<tr><td><strong>{obj["object_id"]}</strong></td>'
                     f'<td>{obj["type"]}</td>'
                     f'<td style="color:{status_color}">{obj["status"]}</td></tr>\n')
        html += "</table>\n"

    # ── Defect summary ─────────────────────────────────────────
    ds = cap_jira.get("defect", {}).get("defect_summary", {})
    if ds.get("total", 0):
        html += f"""<div class="summary-panel">
  <h4>Defects (JIRA)</h4>
  <div style="display:flex;flex-wrap:wrap;gap:6px">
    {_badge(f"🐛 {ds['total']} total", "#6e4b00", "#fef3cd")}
    {_badge(f"🔴 {ds.get('critical', 0)} critical", "#d1242f", "#ffebe9") if ds.get('critical') else ''}
    {_badge(f"{ds.get('open', 0)} open", "#bf8700", "#fff8c5") if ds.get('open') else ''}
    {_badge(f"{ds.get('resolved', 0)} resolved", "#1a7f37", "#ddf4e4") if ds.get('resolved') else ''}
  </div>
</div>
"""

    # ── Standard solution message if no data ─────────────────
    if not cap_ricefw["total"] and not ds.get("total", 0):
        html += """<div class="summary-panel" style="text-align:center">
  <h4 style="margin:0">✅ Standard Solution</h4>
  <p style="color:#666;margin:8px 0 0;font-size:14px">
    This capability is met by standard SAP S/4HANA functionality.<br>
    No custom RICEFW objects or tracked defects.
  </p>
</div>
"""

    html += f"""
<div style="margin-top:24px;display:flex;gap:12px">
  <a href="../tower-{tower}.html" style="color:#0071c5;text-decoration:none;font-weight:600">← Back to {tower} Tower</a>
  <a href="../index.html" style="color:#0071c5;text-decoration:none;font-weight:500;margin-left:auto">Home</a>
</div>
<div class="footer">
  IAO Architecture Pipeline · Intel IDM 2.0 · {tower} / {cap_id} · Intel Confidential<br>
  Generated: {now}
</div>
</div></div>
"""
    html += _sidebar_js()
    html += "</body></html>"

    return html


def _sidebar_js() -> str:
    """Shared sidebar JS for nav.json loading."""
    return """<script>
(function(){
  var sidebar=document.querySelector(".sidebar");
  var toggle=document.querySelector(".sidebar-toggle");
  if(toggle){toggle.addEventListener("click",function(){sidebar.classList.toggle("open")})}
  var basePath=document.querySelector("meta[name=base-path]");
  var base=basePath?basePath.content:"";
  fetch(base+"nav.json").then(function(r){return r.json()}).then(function(data){
    var tree=document.querySelector(".nav-tree");
    if(!tree)return;
    var currentPage=location.pathname;
    data.forEach(function(t){
      var tg=document.createElement("div");tg.className="tower-group";tg.dataset.tower=t.tower;
      var th=document.createElement("div");th.className="tower-header";
      th.innerHTML="<span class=\\"arrow\\">▶</span><span class=\\"icon\\">"+t.icon+"</span><a href=\\""+base+"tower-"+t.tower+".html\\">"+t.tower+"</a>";
      th.addEventListener("click",function(e){if(e.target.tagName!=="A"){th.classList.toggle("open")}});
      tg.appendChild(th);
      var pg=document.createElement("div");pg.className="proc-group";
      t.groups.forEach(function(g){
        var pl=document.createElement("div");pl.className="proc-label";pl.textContent=g.group;
        pg.appendChild(pl);
        g.caps.forEach(function(c){
          var a=document.createElement("a");a.className="cap-link";a.href=base+"cap/"+t.tower+"-"+c.id+".html";
          a.innerHTML="<span class=\\"cap-id\\">"+c.id+"</span> "+c.name;
          a.dataset.search=(c.id+" "+c.name+" "+g.group+" "+t.tower+" "+t.name).toLowerCase();
          if(currentPage.indexOf(t.tower+"-"+c.id)!==-1||currentPage.indexOf(c.id)!==-1){a.classList.add("active");th.classList.add("open")}
          pg.appendChild(a);
        });
      });
      tg.appendChild(pg);
      tree.appendChild(tg);
    });
    var m=currentPage.match(/tower-([A-Z0-9-]+)\\.html/);
    if(m){var hdr=tree.querySelector("[data-tower=\\""+m[1]+"\\"] .tower-header");if(hdr)hdr.classList.add("open")}
  }).catch(function(){});
  var input=document.querySelector(".sidebar .search-box input");
  if(input){
    input.addEventListener("input",function(){
      var q=input.value.trim().toLowerCase();
      var groups=document.querySelectorAll(".tower-group");
      var anyVisible=false;
      groups.forEach(function(tg){
        var links=tg.querySelectorAll(".cap-link");
        var towerVisible=false;
        links.forEach(function(a){
          var match=!q||a.dataset.search.indexOf(q)!==-1;
          a.style.display=match?"block":"none";
          if(match)towerVisible=true;
        });
        var labels=tg.querySelectorAll(".proc-label");
        labels.forEach(function(lbl){
          var next=lbl.nextElementSibling;
          var hasVisible=false;
          while(next&&!next.classList.contains("proc-label")){
            if(next.classList.contains("cap-link")&&next.style.display!=="none")hasVisible=true;
            next=next.nextElementSibling;
          }
          lbl.style.display=hasVisible?"block":"none";
        });
        tg.style.display=towerVisible?"block":"none";
        var pg=tg.querySelector(".proc-group");
        if(q&&towerVisible){pg.classList.add("search-open")}else{pg.classList.remove("search-open")}
        if(towerVisible)anyVisible=true;
      });
      var nr=document.querySelector(".no-results");
      if(nr){nr.style.display=anyVisible?"none":"block"}
    });
  }
})();
</script>"""


# ── Main ─────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate tower + capability landing pages")
    parser.add_argument("--tower", type=str, help="Single tower shortcode to generate")
    args = parser.parse_args()

    registry = _load_tower_registry()
    ricefw_objects = _load_ricefw_objects()
    jira_data = _load_jira_summary()
    cap_map = _load_cap_map()
    cap_to_subtower = _build_cap_to_subtower(cap_map)

    print(f"Loaded: {len(ricefw_objects)} RICEFW objects, "
          f"{len(jira_data.get('subtower_summaries', {}))} JIRA sub-tower summaries, "
          f"{len(cap_to_subtower)} capability→sub-tower mappings")

    # Determine which towers to process
    if args.tower:
        towers = [args.tower]
    else:
        towers = sorted([d.name for d in TOWERS_DIR.iterdir()
                        if d.is_dir() and not d.name.startswith((".", "_"))])

    SITE_DIR.mkdir(parents=True, exist_ok=True)
    cap_dir = SITE_DIR / "cap"
    cap_dir.mkdir(parents=True, exist_ok=True)

    total_tower_pages = 0
    total_cap_pages = 0

    for tower in towers:
        yaml_path = TOWERS_DIR / tower / "tower.yaml"
        if not yaml_path.exists():
            print(f"  SKIP {tower} — no tower.yaml")
            continue

        # Generate tower page
        tower_html = generate_tower_page(
            tower, registry, ricefw_objects, jira_data, cap_map, cap_to_subtower
        )
        tower_page = SITE_DIR / f"tower-{tower}.html"
        tower_page.write_text(tower_html, encoding="utf-8")
        total_tower_pages += 1
        print(f"  ✓ tower-{tower}.html")

        # Generate capability landing pages
        import yaml
        tower_data = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        capabilities = tower_data.get("capabilities", [])

        # Build L1 lookup
        l1_lookup = {}
        for cap in capabilities:
            l1_lookup[cap["id"]] = cap.get("l1", "Other")

        for cap in capabilities:
            cap_id = cap["id"]
            l1_name = l1_lookup[cap_id]

            cap_html = generate_capability_page(
                tower, cap, l1_name, registry, ricefw_objects, jira_data, cap_to_subtower
            )
            cap_page = cap_dir / f"{tower}-{cap_id}.html"
            cap_page.write_text(cap_html, encoding="utf-8")
            total_cap_pages += 1

        print(f"    → {len(capabilities)} capability pages")

    print(f"\nGenerated: {total_tower_pages} tower pages, {total_cap_pages} capability pages")
    print(f"Output: {SITE_DIR}")


if __name__ == "__main__":
    main()
