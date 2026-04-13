"""gen_tower_pages.py — Generate enhanced tower landing + capability landing pages.

Produces:
  _site/tower-{TOWER}.html   — tower page with sub-tower RICEFW + JIRA summaries
  _site/cap/{CAP_ID}.html     — capability landing page with 4 document buttons

Data sources:
  - towers/*/tower.yaml (capabilities, L1 process groups)
  - data/smartsheet/object_trackers/s4_r3_object_tracker.csv (RICEFW objects)
  - data/jira/jira_summary.json (defect + test summaries per sub-tower)
  - config/tower_registry.json (tower display metadata)
  - config/subtower_capability_map.json (sub-tower → capability mapping)
  - config/abap_ricefw_map.yaml (ABAP program → RICEFW object mapping)

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
from urllib.parse import quote as url_quote

# ── Paths ────────────────────────────────────────────────────────
WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"
SITE_DIR = WORKSPACE / "_site"
CONFIG_DIR = WORKSPACE / "config"
DATA_DIR = WORKSPACE / "data"

REGISTRY_PATH = CONFIG_DIR / "tower_registry.json"
CAP_MAP_PATH = CONFIG_DIR / "subtower_capability_map.json"
ABAP_RICEFW_MAP_PATH = CONFIG_DIR / "abap_ricefw_map.yaml"
OBJECT_TRACKER_PATH = DATA_DIR / "smartsheet" / "manual" / "object_trackers" / "s4_r3_object_tracker.csv"
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
                "description": (r.get("Description") or "").strip(),
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
    """Build tower:cap_id -> sub_tower reverse map.

    Uses 'TOWER:CAP_ID' keys so the same capability ID in different
    towers (e.g. L-040 in FTS-IF and PTP) doesn't collide.
    Also stores plain 'CAP_ID' as fallback for backward compatibility.
    """
    result = {}
    for tower_key, st_map in cap_map.items():
        if tower_key.startswith("_"):
            continue
        for sub_tower, cap_ids in st_map.items():
            for cap_id in cap_ids:
                result[f"{tower_key}:{cap_id}"] = sub_tower
                # Only set plain key if not already claimed by another tower
                if cap_id not in result:
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


# ── ABAP-RICEFW mapping loader ───────────────────────────────────

def _load_abap_ricefw_map() -> list[dict]:
    """Load ABAP-to-RICEFW mapping from config/abap_ricefw_map.yaml."""
    import yaml
    if not ABAP_RICEFW_MAP_PATH.exists():
        return []
    data = yaml.safe_load(ABAP_RICEFW_MAP_PATH.read_text(encoding="utf-8")) or {}
    return data.get("assessments", [])


def _abap_assessments_for_tower(tower: str, abap_map: list[dict]) -> list[dict]:
    """Return ABAP assessment entries for a given tower, with resolved deploy paths."""
    results = []
    abap_dir = TOWERS_DIR / tower / "output" / "docs" / "abap-assessments"
    for entry in abap_map:
        if entry.get("tower", "").upper() != tower.upper():
            continue
        prefix = entry.get("abap_prefix", "")
        html_path = None
        if abap_dir.exists():
            matches = sorted(abap_dir.glob(f"{prefix}*-ABAP-Assessment.html"))
            if matches:
                raw = str(matches[0].relative_to(WORKSPACE)).replace("\\", "/")
                html_path = raw.replace(" ", "-")
        results.append({
            "ricefw_id": entry.get("ricefw_id", prefix),
            "abap_prefix": prefix,
            "capability": entry.get("capability", ""),
            "description": entry.get("description", ""),
            "source": entry.get("source", "manual"),
            "href": html_path,
        })
    return results


def _build_abap_ricefw_lookup(abap_entries: list[dict]) -> dict[str, dict]:
    """Build a lookup dict keyed by ricefw_id for quick assessment link resolution."""
    return {e["ricefw_id"]: e for e in abap_entries}


# ── Doc finder ───────────────────────────────────────────────────

def _find_cap_docs(tower: str, l1_name: str, cap_id: str) -> dict[str, str]:
    """Find SAD, RICEFW, Testing, and ABAP Assessment HTML files for a capability."""
    cap_dir = TOWERS_DIR / tower / l1_name / cap_id / "output" / "docs"
    docs: dict[str, str] = {}

    def _deploy_path(p: Path) -> str:
        """Return workspace-relative path with spaces replaced by hyphens.

        The deploy-pages.yml copies files into _site/ using
        ``sed 's/ /-/g'`` on directory names, so all deployed URLs
        use hyphens instead of spaces.
        """
        raw = str(p.relative_to(WORKSPACE)).replace("\\", "/")
        return raw.replace(" ", "-")

    sad_dir = cap_dir / "systems-architecture"
    if sad_dir.exists():
        files = list(sad_dir.glob("*-Architecture.html"))
        if files:
            docs["sad"] = _deploy_path(files[0])

    ricefw_dir = cap_dir / "ricefw-tracker"
    if ricefw_dir.exists():
        files = list(ricefw_dir.glob("*-RICEFW-Tracker.html"))
        if files:
            docs["ricefw"] = _deploy_path(files[0])

    testing_dir = cap_dir / "testing-report"
    if testing_dir.exists():
        files = list(testing_dir.glob("*-Testing-Report.html"))
        if files:
            docs["testing"] = _deploy_path(files[0])

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
    abap_map: list[dict] | None = None,
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
.topbar img{{height:28px;width:28px;object-fit:contain;margin-right:12px;border-radius:4px}}
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
.sidebar .proc-label{{font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.5px;padding:8px 16px 4px;margin-top:4px;cursor:pointer;user-select:none}}
.sidebar .proc-label:hover{{color:#00285a}}
.sidebar .proc-label .l1-arrow{{font-size:9px;margin-right:4px;display:inline-block;transition:transform .2s;color:#aaa}}
.sidebar .proc-label.open .l1-arrow{{transform:rotate(90deg)}}
.sidebar .l1-children{{display:none;margin-left:8px}}
.sidebar .proc-label.open+.l1-children{{display:block}}
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
.hero::after{{content:"";position:absolute;top:0;right:0;width:300px;height:100%;background:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 300 200%27%3E%3Cpath d=%27M0 100L80 100L120 60L200 60L240 100L300 100%27 stroke=%27rgba(255,255,255,.08)%27 fill=%27none%27 stroke-width=%272%27/%3E%3Cpath d=%27M0 140L60 140L100 180L180 180L220 140L300 140%27 stroke=%27rgba(255,255,255,.06)%27 fill=%27none%27 stroke-width=%272%27/%3E%3C/svg%3E") no-repeat center;opacity:.5;pointer-events:none}}
.hero h2{{font-size:32px;margin:0 0 8px;font-weight:700;position:relative}}
.hero p{{font-size:16px;opacity:.85;margin:0;position:relative}}
.hero .badge{{display:inline-block;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:4px 14px;font-size:12px;margin-top:12px;position:relative}}
.hero-btn{{display:inline-block;padding:8px 20px;border-radius:8px;color:#fff;text-decoration:none;font-weight:600;font-size:14px;transition:background .15s}}
.hero-btn-primary{{background:rgba(255,255,255,.25);border:1px solid rgba(255,255,255,.45)}}
.hero-btn-secondary{{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35)}}
.hero-btn-tertiary{{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.85);font-weight:500}}
@media(hover:hover){{.hero-btn-primary:hover{{background:rgba(255,255,255,.35)}}.hero-btn-secondary:hover{{background:rgba(255,255,255,.3)}}.hero-btn-tertiary:hover{{background:rgba(255,255,255,.2)}}}}
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
  .topbar{{padding:0 12px}}
  .topbar .sidebar-toggle{{display:block}}
  .topbar h1{{font-size:14px}}
  .sidebar{{transform:translateX(-100%)}}
  .sidebar.open{{transform:translateX(0);box-shadow:4px 0 16px rgba(0,0,0,.15)}}
  .page-body{{margin-left:0}}
  .hero{{padding:28px 20px;text-align:center}}
  .hero h2{{font-size:24px}}
  .hero div{{flex-direction:column;align-items:center}}
}}
</style>
</head><body>
<div class="topbar">
  <button class="sidebar-toggle" aria-label="Toggle navigation">☰</button>
  <img src="favicon.ico" alt="IAO">
  <h1>IAO Architecture Portal</h1>
  <select id="release-filter" style="margin-left:auto;margin-right:12px;padding:6px 12px;border-radius:6px;border:1px solid rgba(255,255,255,.3);background:#fff;color:#00285a;font-size:13px;font-weight:600;cursor:pointer;outline:none" title="Filter by Release">
    <option value="All">All Releases</option>
    <option value="R1">R1</option>
    <option value="R2">R2</option>
    <option value="R3">R3</option>
    <option value="R4">R4</option>
    <option value="R5">R5</option>
  </select>
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
  <span class="badge">{cap_count} capabilities · R1 – R5</span>
  <div style="margin-top:16px;display:flex;gap:12px;flex-wrap:wrap;justify-content:center;position:relative;z-index:1">
    <a href="towers/{tower}/output/docs/summaries/L0-{tower}-Summary.html" class="hero-btn hero-btn-primary">📐 L0 Architecture Summary</a>
    <a href="dashboard/{tower}/index.html" class="hero-btn hero-btn-secondary">📊 Tower Dashboard</a>
    <a href="dashboard/index.html" class="hero-btn hero-btn-tertiary">📊 Program Dashboard</a>
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
            st = cap_to_subtower.get(f"{tower}:{cap['id']}", cap_to_subtower.get(cap["id"], ""))
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

        # L1 summary slug — must match gen_summary.py naming convention
        l1_slug = re.sub(r'[^a-zA-Z0-9 ]', '', l1_name.replace('-', ' ')).strip()
        l1_slug = re.sub(r' +', ' ', l1_slug).replace(' ', '-')[:40]
        l1_summary_href = f"towers/{tower}/output/docs/summaries/L1-{l1_slug}-Summary.html"

        html_parts.append(f'<h2 class="section-title">{l1_name} '
                          f'<span style="font-size:14px;color:#666;font-weight:400">'
                          f'({len(caps)} capabilities)</span>'
                          f'<a href="{l1_summary_href}" style="font-size:13px;font-weight:500;'
                          f'color:#0071c5;text-decoration:none;margin-left:12px;padding:3px 10px;'
                          f'border:1px solid #0071c5;border-radius:6px;vertical-align:middle"'
                          f' title="View aggregated architecture diagrams for this process group">'
                          f'📐 L1 Summary</a></h2>')

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

    # ── ABAP Code Assessments section ─────────────────────────
    now = datetime.now(timezone.utc).strftime("%B %Y")
    abap_entries = _abap_assessments_for_tower(tower, abap_map or [])
    if abap_entries:
        html_parts.append('<h2 class="section-title">🔍 ABAP Code Assessments</h2>')
        html_parts.append('<table>\n<tr><th style="width:130px">RICEFW ID</th>'
                          '<th>ABAP Object</th><th>Description</th>'
                          '<th style="width:90px">Source</th>'
                          '<th style="width:100px">View</th></tr>')
        for ae in abap_entries:
            link = (f'<a href="{ae["href"]}">Open →</a>' if ae["href"]
                    else '<span style="color:#999">Pending HTML</span>')
            src_badge = ('<span style="display:inline-block;padding:2px 8px;border-radius:10px;'
                         'font-size:11px;font-weight:600;'
                         + ('background:#dbeafe;color:#1e40af">abapGit'
                            if ae["source"] == "abapgit"
                            else 'background:#fef3cd;color:#6e4b00">manual')
                         + '</span>')
            html_parts.append(
                f'<tr><td><strong>{ae["ricefw_id"]}</strong></td>'
                f'<td><code>{ae["abap_prefix"]}</code></td>'
                f'<td>{ae["description"]}</td>'
                f'<td>{src_badge}</td>'
                f'<td>{link}</td></tr>'
            )
        html_parts.append('</table>')

    # ── Footer ───────────────────────────────────────────────────
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
    abap_lookup: dict[str, dict] | None = None,
) -> str:
    """Generate capability landing page with 3 document buttons + per-RICEFW assessment links."""
    cap_id = cap["id"]
    cap_name = cap.get("name", cap_id)
    info = registry.get(tower, {})
    icon = info.get("icon", "📄")

    docs = _find_cap_docs(tower, l1_name, cap_id)

    # Get RICEFW data for this capability — multi-tier matching
    sub_tower = cap_to_subtower.get(f"{tower}:{cap_id}", cap_to_subtower.get(cap_id, ""))
    tower_objs = [o for o in ricefw_objects if o["tower"] == tower]
    cap_objs = []

    # Tier 1: Explicit sub-tower mapping from config
    if sub_tower:
        cap_objs = [o for o in tower_objs if o["sub_tower"] == sub_tower]

    # Inject synthetic RICEFW rows for ABAP assessments mapped to this capability
    if abap_lookup:
        existing_ids = {o["object_id"] for o in cap_objs}
        for rid, entry in abap_lookup.items():
            if entry.get("capability", "").upper() == cap_id.upper() and rid not in existing_ids:
                cap_objs.append({
                    "object_id": rid,
                    "tower": tower,
                    "sub_tower": sub_tower or "",
                    "type": "Report",
                    "description": entry.get("description", ""),
                    "status": "ABAP Assessment Available",
                })

    # Tier 2: Object ID prefix match (e.g. DS-020 → FPRDS020*)
    if not cap_objs:
        cap_prefix = cap_id.replace("-", "")[:4].upper()
        if cap_prefix:
            cap_objs = [o for o in tower_objs
                        if o["object_id"].upper().replace("-", "").replace("_", "").startswith(cap_prefix)]

    # Tier 3: Sub-tower name contains capability ID
    if not cap_objs:
        cap_objs = [o for o in tower_objs if cap_id.lower() in o["sub_tower"].lower()]

    # Tier 4: Fuzzy match — capability name keywords against sub-tower name
    if not cap_objs and cap_name:
        # Extract meaningful words from capability name (drop short/common words)
        stop = {"and", "the", "of", "for", "in", "to", "a", "an", "fts", "if", "ip"}
        cap_words = {w.lower() for w in re.findall(r'[A-Za-z]{3,}', cap_name)} - stop
        if cap_words:
            best_st, best_score = "", 0
            seen_sts = {o["sub_tower"] for o in tower_objs if o["sub_tower"]}
            for st in seen_sts:
                st_words = {w.lower() for w in re.findall(r'[A-Za-z]{3,}', st)} - stop
                score = len(cap_words & st_words)
                if score > best_score:
                    best_score = score
                    best_st = st
            if best_score >= 2:
                sub_tower = best_st
                cap_objs = [o for o in tower_objs if o["sub_tower"] == best_st]

    cap_ricefw = {"total": 0, "completed": 0, "pending": 0}
    for o in cap_objs:
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
.topbar img{{height:28px;width:28px;object-fit:contain;margin-right:12px;border-radius:4px}}
.topbar h1{{color:#fff;font-size:18px;font-weight:600;margin:0;letter-spacing:.5px;flex:1;text-align:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.topbar a.back-link{{color:rgba(255,255,255,.85);text-decoration:none;font-size:14px;white-space:nowrap}}
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
.sidebar .proc-label{{font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.5px;padding:8px 16px 4px;margin-top:4px;cursor:pointer;user-select:none}}
.sidebar .proc-label:hover{{color:#00285a}}
.sidebar .proc-label .l1-arrow{{font-size:9px;margin-right:4px;display:inline-block;transition:transform .2s;color:#aaa}}
.sidebar .proc-label.open .l1-arrow{{transform:rotate(90deg)}}
.sidebar .l1-children{{display:none;margin-left:8px}}
.sidebar .proc-label.open+.l1-children{{display:block}}
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
  .topbar{{padding:0 12px}}
  .topbar .sidebar-toggle{{display:block}}
  .topbar h1{{font-size:14px}}
  .sidebar{{transform:translateX(-100%)}}
  .sidebar.open{{transform:translateX(0);box-shadow:4px 0 16px rgba(0,0,0,.15)}}
  .page-body{{margin-left:0}}
}}
</style>
</head><body>
<div class="topbar">
  <button class="sidebar-toggle" aria-label="Toggle navigation">☰</button>
  <img src="../favicon.ico" alt="IAO">
  <h1>IAO Architecture Portal</h1>
  <select id="release-filter" style="margin-left:auto;margin-right:12px;padding:6px 12px;border-radius:6px;border:1px solid rgba(255,255,255,.3);background:#fff;color:#00285a;font-size:13px;font-weight:600;cursor:pointer;outline:none" title="Filter by Release">
    <option value="All">All Releases</option>
    <option value="R1">R1</option>
    <option value="R2">R2</option>
    <option value="R3">R3</option>
    <option value="R4">R4</option>
    <option value="R5">R5</option>
  </select>
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
<tr><th>Object ID</th><th>Type</th><th>Description</th><th>Status</th><th>Assessment</th></tr>
"""
        for obj in sorted(cap_objs, key=lambda o: o["object_id"]):
            status_color = "#1a7f37" if "complete" in obj["status"].lower() else "#9a6700"
            desc = obj.get("description", "")
            if len(desc) > 80:
                desc = desc[:77] + "..."
            # Check if this RICEFW object has an ABAP assessment
            assess_cell = "—"
            if abap_lookup and obj["object_id"] in abap_lookup:
                ae = abap_lookup[obj["object_id"]]
                if ae.get("href"):
                    assess_cell = f'<a href="../{ae["href"]}" style="color:#7b2d8e;font-weight:600;text-decoration:none" title="ABAP Assessment">📝 View</a>'
                else:
                    assess_cell = '<span style="color:#999">pending</span>'
            html += (f'<tr><td><strong>{obj["object_id"]}</strong></td>'
                     f'<td>{obj["type"]}</td>'
                     f'<td style="font-size:12px;color:#555">{desc}</td>'
                     f'<td style="color:{status_color}">{obj["status"]}</td>'
                     f'<td style="text-align:center">{assess_cell}</td></tr>\n')
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

    // Program Summary link at the very top
    if(data.length>0 && data[0]._program_summary){
      var pa=document.createElement("a");pa.className="cap-link";pa.href=base+data[0]._program_summary;
      pa.innerHTML="<span class=\\"cap-id\\" style=\\"background:#fef3cd;color:#6e4b00\\">📐</span> Program Architecture Summary";
      pa.style.fontWeight="700";pa.style.padding="8px 16px";pa.dataset.search="program summary architecture";
      tree.appendChild(pa);
      var hr=document.createElement("hr");hr.style.cssText="border:0;border-top:1px solid #e4e8ed;margin:6px 12px";
      tree.appendChild(hr);
    }

    data.forEach(function(t){
      if(t._program_summary && !t.tower) return; // skip program-only entry
      var tg=document.createElement("div");tg.className="tower-group";tg.dataset.tower=t.tower;
      var th=document.createElement("div");th.className="tower-header";
      th.innerHTML="<span class=\\"arrow\\">▶</span><span class=\\"icon\\">"+t.icon+"</span><a href=\\""+base+"tower-"+t.tower+".html\\">"+t.tower+"</a>";
      th.addEventListener("click",function(e){if(e.target.tagName!=="A"){th.classList.toggle("open")}});
      tg.appendChild(th);

      // L0 summary link under tower header (inside a proc-group so it collapses with tower)
      var pg=document.createElement("div");pg.className="proc-group";
      if(t.l0_summary){
        var l0=document.createElement("a");l0.className="cap-link";l0.href=base+t.l0_summary;
        l0.innerHTML="<span class=\\"cap-id\\" style=\\"background:#e0e7ff;color:#3730a3\\">L0</span> Tower Architecture Summary";
        l0.style.fontWeight="600";l0.dataset.search=(t.tower+" l0 summary architecture").toLowerCase();
        pg.appendChild(l0);
      }

      t.groups.forEach(function(g){
        // Collapsible L1 proc-label header
        var pl=document.createElement("div");pl.className="proc-label";
        pl.innerHTML="<span class=\\"l1-arrow\\">▶</span> "+g.group;
        pl.style.cursor="pointer";
        pl.addEventListener("click",function(){pl.classList.toggle("open")});
        pg.appendChild(pl);

        // L1 child container (hidden by default, revealed on click)
        var lc=document.createElement("div");lc.className="l1-children";

        // L1 summary link under process group label
        if(g.l1_summary){
          var l1=document.createElement("a");l1.className="cap-link";l1.href=base+g.l1_summary;
          l1.innerHTML="<span class=\\"cap-id\\" style=\\"background:#dbeafe;color:#1e40af\\">L1</span> Process Architecture Summary";
          l1.style.fontWeight="600";l1.dataset.search=(g.group+" l1 summary architecture").toLowerCase();
          lc.appendChild(l1);
        }
        g.caps.forEach(function(c){
          var a=document.createElement("a");a.className="cap-link";a.href=base+(c.href||("cap/"+t.tower+"-"+c.id+".html"));
          a.innerHTML="<span class=\\"cap-id\\">"+c.id+"</span> "+c.name;
          a.dataset.search=(c.id+" "+c.name+" "+g.group+" "+t.tower+" "+t.name).toLowerCase();
          if(currentPage.indexOf(t.tower+"-"+c.id)!==-1||currentPage.indexOf(c.id)!==-1){
            a.classList.add("active");th.classList.add("open");pl.classList.add("open");
          }
          lc.appendChild(a);
        });
        pg.appendChild(lc);
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
          if(q){lbl.classList.add("open")} // expand while searching
          var childBlock=lbl.nextElementSibling;
          if(childBlock&&childBlock.classList.contains("l1-children")){
            var caps=childBlock.querySelectorAll(".cap-link");
            var hasVisible=false;
            caps.forEach(function(c){if(c.style.display!=="none")hasVisible=true});
            lbl.style.display=hasVisible?"block":"none";
            childBlock.style.display=hasVisible?"block":"none";
          }
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
      var nr=document.querySelector(".no-results");
      if(nr){nr.style.display=anyVisible?"none":"block"}
    });
  }
  // ── Release filter persistence + document link rewriting ──
  var sel=document.getElementById("release-filter");
  if(sel){
    var saved=localStorage.getItem("iao-release-filter");
    if(saved){sel.value=saved}

    function rewriteDocLinks(){
      var r=sel.value;
      // Rewrite doc-btn and summary links: when a release is selected, prefix href with /Rx/
      // Targets: doc-btn links, hero summary links, sidebar summary links, and Program Summary
      var linkSel="a.doc-btn, a[href*='Summary.html'], a[href*='summaries/']";
      document.querySelectorAll(linkSel).forEach(function(a){
        var orig=a.getAttribute("data-orig-href")||a.getAttribute("href");
        a.setAttribute("data-orig-href",orig);
        if(r&&r!=="All"){
          // towers/... paths: insert Rx/ prefix before towers/
          var pat=new RegExp("(\\.\\.\\/)?towers\\/");
          var newHref=orig;
          if(pat.test(orig)){
            newHref=orig.replace(pat,"$1"+r+"/towers/");
          }
          // summaries/... paths (Program Summary): insert Rx/ prefix before summaries/
          else if(orig.indexOf("summaries/")!==-1){
            newHref=orig.replace("summaries/",r+"/summaries/");
          }
          a.setAttribute("href",newHref);
        }else{
          a.setAttribute("href",orig);
        }
      });
    }

    sel.addEventListener("change",function(){
      localStorage.setItem("iao-release-filter",sel.value);
      rewriteDocLinks();
    });
    // Rewrite on initial load if a release was saved
    rewriteDocLinks();

    document.querySelectorAll("a[href*='dashboard']").forEach(function(a){
      a.addEventListener("click",function(e){
        var r=sel.value;
        if(r&&r!=="All"){
          e.preventDefault();
          var url=a.href;
          url+=(url.indexOf("?")>-1?"&":"?")+"release="+r;
          location.href=url;
        }
      });
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
    abap_map = _load_abap_ricefw_map()

    print(f"Loaded: {len(ricefw_objects)} RICEFW objects, "
          f"{len(jira_data.get('subtower_summaries', {}))} JIRA sub-tower summaries, "
          f"{len(cap_to_subtower)} capability->sub-tower mappings, "
          f"{len(abap_map)} ABAP-RICEFW mappings")

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
            tower, registry, ricefw_objects, jira_data, cap_map, cap_to_subtower, abap_map
        )
        tower_page = SITE_DIR / f"tower-{tower}.html"
        tower_page.write_text(tower_html, encoding="utf-8")
        total_tower_pages += 1
        print(f"  [OK] tower-{tower}.html")

        # Generate capability landing pages
        import yaml
        tower_data = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        capabilities = tower_data.get("capabilities", [])

        # Build L1 lookup and ABAP assessment lookup for this tower
        l1_lookup = {}
        for cap in capabilities:
            l1_lookup[cap["id"]] = cap.get("l1", "Other")

        abap_entries = _abap_assessments_for_tower(tower, abap_map)
        abap_ricefw_lookup = _build_abap_ricefw_lookup(abap_entries)

        for cap in capabilities:
            cap_id = cap["id"]
            l1_name = l1_lookup[cap_id]

            cap_html = generate_capability_page(
                tower, cap, l1_name, registry, ricefw_objects, jira_data, cap_to_subtower,
                abap_lookup=abap_ricefw_lookup,
            )
            cap_page = cap_dir / f"{tower}-{cap_id}.html"
            cap_page.write_text(cap_html, encoding="utf-8")
            total_cap_pages += 1

        print(f"    -> {len(capabilities)} capability pages")

    # ── Generate nav.json for sidebar ────────────────────────────
    _generate_nav_json(towers, registry)

    print(f"\nGenerated: {total_tower_pages} tower pages, {total_cap_pages} capability pages")
    print(f"Output: {SITE_DIR}")


def _generate_nav_json(towers: list[str], registry: dict) -> None:
    """Generate nav.json for sidebar navigation — mirrors deploy-pages.yml logic."""
    import yaml as _yaml

    nav_data: list[dict] = []

    # Check for Program Summary
    program_summary_path = WORKSPACE / "output" / "docs" / "summaries" / "Program-Summary.html"
    program_href = ""
    if program_summary_path.exists():
        program_href = "summaries/Program-Summary.html"

    for tower in towers:
        yaml_path = TOWERS_DIR / tower / "tower.yaml"
        if not yaml_path.exists():
            continue
        tower_data = _yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        capabilities = tower_data.get("capabilities", [])
        info = registry.get(tower, {})
        icon = info.get("icon", "📄")
        full_name = info.get("name", tower)

        # L0 summary
        l0_file = TOWERS_DIR / tower / "output" / "docs" / "summaries" / f"L0-{tower}-Summary.html"
        l0_href = f"towers/{tower}/output/docs/summaries/L0-{tower}-Summary.html" if l0_file.exists() else ""

        # Group capabilities by L1
        l1_groups: dict[str, list[dict]] = {}
        for cap in capabilities:
            l1 = cap.get("l1", "Other")
            l1_groups.setdefault(l1, []).append(cap)

        groups = []
        for l1_name, caps in sorted(l1_groups.items()):
            # Check for any architecture HTML
            has_docs = False
            cap_entries = []
            for cap in caps:
                cap_id = cap["id"]
                cap_name = cap.get("name", cap_id)
                # Check if generated arch doc exists
                cap_dir = _find_cap_dir(TOWERS_DIR / tower, l1_name, cap_id)
                if cap_dir:
                    html_files = list((cap_dir / "output" / "docs" / "systems-architecture").glob("*-Architecture.html")) if (cap_dir / "output" / "docs" / "systems-architecture").exists() else []
                    if html_files:
                        # Extract real title from HTML
                        title = _extract_title_from_html(html_files[0])
                        if title:
                            # Strip "DS-020 — " prefix to get just the name
                            name_part = re.sub(rf'^{re.escape(cap_id)}\s*[—–-]\s*', '', title)
                            if name_part:
                                cap_name = name_part
                        has_docs = True
                cap_entries.append({"id": cap_id, "name": cap_name, "href": f"cap/{tower}-{cap_id}.html"})

            if not has_docs:
                continue

            # L1 summary
            l1_slug = re.sub(r'[^a-zA-Z0-9 ]', '', l1_name.replace('-', ' ')).strip()
            l1_slug = re.sub(r' +', ' ', l1_slug).replace(' ', '-')[:40]
            l1_file = TOWERS_DIR / tower / "output" / "docs" / "summaries" / f"L1-{l1_slug}-Summary.html"
            l1_href = f"towers/{tower}/output/docs/summaries/L1-{l1_slug}-Summary.html" if l1_file.exists() else ""

            groups.append({
                "group": l1_name,
                "l1_summary": l1_href,
                "caps": cap_entries,
            })

        entry: dict = {
            "tower": tower,
            "name": full_name,
            "icon": icon,
            "l0_summary": l0_href,
            "groups": groups,
        }
        # Attach program summary to first tower entry for the JS to pick up
        if nav_data == [] and program_href:
            entry["_program_summary"] = program_href
        nav_data.append(entry)

    nav_path = SITE_DIR / "nav.json"
    nav_path.write_text(json.dumps(nav_data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  [OK] nav.json ({len(nav_data)} towers)")


def _find_cap_dir(tower_dir: Path, l1_name: str, cap_id: str) -> Path | None:
    """Find capability directory under tower — tries L1/cap_id then scans."""
    direct = tower_dir / l1_name / cap_id
    if direct.is_dir():
        return direct
    # Scan all subdirs for cap_id
    for d in tower_dir.iterdir():
        if d.is_dir() and not d.name.startswith((".", "_", "output")):
            candidate = d / cap_id
            if candidate.is_dir():
                return candidate
    return None


if __name__ == "__main__":
    main()
