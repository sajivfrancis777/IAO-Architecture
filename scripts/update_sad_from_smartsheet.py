"""update_sad_from_smartsheet.py — Update all SAD documents with live Smartsheet data.

Updates:
- Section 7.1 Project Roadmap: compact 7-column layout (ID, Description, FS, TDD, Build, FUT, Status)
- Section 6.2 SAP Development Object Status: capability-specific RICEFW status summary
- Section 7.2 RAID Log: capability-specific RAID items (3-tier matching)

RAID Matching Strategy (3 tiers):
  1. Object ID reference — RAID title/description names a RICEFW object in this capability
  2. Sub-Team match — RAID "Assigned To (Sub-Team)" matches the capability's sub-tower
  3. Tower-level fallback — RAID impacts the tower (shown in a separate "Other Tower RAIDs" group)

Run:
    python update_sad_from_smartsheet.py [--dry-run] [--tower FPR]
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from src.smartsheet_loader import SmartsheetLoader, _normalize_tower

TOWERS_DIR = ROOT / "towers"
OBJ_TRACKER_CSV = ROOT / "data" / "smartsheet" / "object_trackers" / "s4_r3_object_tracker.csv"
RAID_CSV = ROOT / "data" / "smartsheet" / "raid" / "master_raid_log.csv"
E2E_RAID_CSV = ROOT / "data" / "smartsheet" / "raid" / "e2e_raid_log.csv"

# Regex to find RICEFW Object IDs in text
_OBJ_ID_RE = re.compile(r'[A-Z]{2,5}[RICEFWXVM]\d{3,5}(?:_[A-Z]+)?', re.IGNORECASE)

_PAGE_BREAK = '<div style="page-break-before: always;"></div>'

_FOOTER_CSS = """\
.page-footer {
  padding-top: 8px;
  border-top: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: #888;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 6px 20px;
  background: #fff;
}
@media print {
  .page-footer { position: fixed; bottom: 0; left: 0.75in; right: 0.75in; }
}
.page-footer a { color: #00aeef; text-decoration: none; font-weight: 500; }
.page-footer a:hover { color: #0071c5; text-decoration: underline; }"""


# ══════════════════════════════════════════════════════════════
# Page footer injection
# ══════════════════════════════════════════════════════════════

def _extract_doc_title(content: str) -> str:
    """Extract cap_id and cap_name from the document's H1 tag."""
    m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if m:
        title = m.group(1).replace("\n", " ").strip()
        title = re.sub(r'<[^>]+>', '', title)  # strip any inner HTML
        return title
    return ""


def inject_page_footers(content: str) -> str:
    """Add TOC anchor, footer CSS, and page footers to a SAD document."""
    title = _extract_doc_title(content)

    # Add TOC anchor if missing
    if '<a id="toc"></a>' not in content:
        content = content.replace(
            "## Table of Contents",
            '<a id="toc"></a>\n\n## Table of Contents',
            1,
        )

    # Replace the entire <style> block with a clean, canonical version
    _CANONICAL_STYLE = (
        '<style>\n'
        '@media print {\n'
        '  @page { margin: 0.75in; }\n'
        '  .mermaid { page-break-inside: avoid; overflow: visible; }\n'
        '  pre, table { page-break-inside: avoid; }\n'
        '  h2, h3, h4 { page-break-after: avoid; }\n'
        '}\n'
        '.mermaid { overflow: visible; }\n'
        '.mermaid svg { max-width: 100%; height: auto !important; }\n'
        + _FOOTER_CSS + '\n'
        '</style>'
    )
    content = re.sub(r'<style>.*?</style>', _CANONICAL_STYLE, content, flags=re.DOTALL, count=1)

    # Remove any existing footers (idempotent re-run)
    content = re.sub(r'<div class="page-footer">.*?</div>\n?', '', content)

    # Inject footers at each page break
    parts = content.split(_PAGE_BREAK)
    if len(parts) <= 1:
        return content

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


# Also remove the old footer::after CSS rule if present
def _clean_legacy_footer_css(content: str) -> str:
    return re.sub(
        r'\s*footer::after\s*\{[^}]*\}\s*',
        '\n  ',
        content,
    )


def update_title_page(content: str, filepath: Path) -> str:
    """Add cover banner image and author line to the title page."""
    # Compute relative path from doc to SVG
    rel_svg = os.path.relpath(
        ROOT / "templates" / "assets" / "cover_banner.svg",
        filepath.parent,
    ).replace("\\", "/")

    # Add cover image if not already present
    if "cover_banner.svg" not in content:
        # Replace the opening div to include image and reduced top padding
        content = re.sub(
            r'<div style="text-align:center;\s*padding-top:\d+px;">',
            f'<div style="text-align:center; padding-top:20px;">\n'
            f'  <img src="{rel_svg}" alt="IAO Architecture" '
            f'style="width:100%; border-radius:8px;" />',
            content,
            count=1,
        )
    else:
        # Update existing image style (remove max-width cap, update alt text)
        content = re.sub(
            r'<img src="[^"]*cover_banner\.svg"[^/]*/?>',
            f'<img src="{rel_svg}" alt="IAO Architecture" '
            f'style="width:100%; border-radius:8px;" />',
            content,
            count=1,
        )

    # Add author name if not present
    if "Sajiv Francis" not in content:
        content = content.replace(
            "Generated: March 2026</p>",
            "Generated: March 2026<br/>\n  Sajiv Francis</p>",
            1,
        )
        # Also handle the Jinja2 variable form for future-proofing
        content = re.sub(
            r'(Generated:\s*[^<]+)(</p>)',
            r'\1<br/>\n  Sajiv Francis\2',
            content,
            count=1,
        ) if "Sajiv Francis" not in content else content

    return content

# ══════════════════════════════════════════════════════════════
# Data loaders
# ══════════════════════════════════════════════════════════════

def load_object_tracker() -> list[dict[str, str]]:
    with open(OBJ_TRACKER_CSV, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def load_raid_log(csv_path: Path) -> list[dict[str, str]]:
    if not csv_path.exists():
        return []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


# ══════════════════════════════════════════════════════════════
# Tower-level matching (for Impacted Teams)
# ══════════════════════════════════════════════════════════════
_RAID_TOWER_MAP = {
    "fpr": "FPR", "finance": "FPR",
    "fts ip": "FTS-IP", "fts-ip": "FTS-IP",
    "fts if": "FTS-IF", "fts-if": "FTS-IF",
    "otc ip": "OTC-IP", "otc-ip": "OTC-IP",
    "otc if": "OTC-IF", "otc-if": "OTC-IF",
    "ptp": "PTP", "procure to pay": "PTP",
    "master data": "MDM", "mdm": "MDM",
    "e2e": "E2E", "scp if": "FTS-IF", "scp ip": "FTS-IP",
}


def raid_impacts_tower(impacted_teams: str, tower: str) -> bool:
    if not impacted_teams:
        return False
    teams_lower = impacted_teams.lower()
    tower_keys = [k for k, v in _RAID_TOWER_MAP.items() if v == tower]
    return any(key in teams_lower for key in tower_keys)


# ══════════════════════════════════════════════════════════════
# Capability-level RAID mapping (3-tier)
# ══════════════════════════════════════════════════════════════

def extract_section55_object_ids(content: str) -> set[str]:
    """Extract Object IDs from section 5.5 RICEFW Inventory only."""
    obj_ids = set()
    in_section = False
    for line in content.split("\n"):
        if re.match(r'^### 5\.5\s+RICEFW Inventory', line):
            in_section = True
            continue
        if in_section and re.match(r'^###?\s', line) and '5.5' not in line:
            break
        if in_section and "|" in line:
            cells = [c.strip() for c in line.split("|")]
            for cell in cells:
                if _OBJ_ID_RE.match(cell) and not cell.startswith("---"):
                    obj_ids.add(cell)
    return obj_ids


def get_subtowers_for_objects(obj_ids: set[str], obj_rows: list[dict]) -> set[str]:
    """Map Object IDs to their Object Tracker sub-tower names."""
    subtowers = set()
    for r in obj_rows:
        oid = r.get("Object ID", "").strip()
        if oid in obj_ids:
            st = r.get("Sub-Tower Name", "").strip()
            if st:
                subtowers.add(st)
    return subtowers


def normalize_subtower_key(subtower: str) -> str:
    """Extract descriptive part: '3.7 FPR - Product Costing...' -> 'product costing...'"""
    cleaned = re.sub(r'^\d+[A-Za-z]?\.\d*\s+[\w-]+\s*-\s*', '', subtower)
    return cleaned.strip().lower()


def raid_subteam_matches_subtowers(sub_team: str, subtower_keys: set[str]) -> bool:
    """Check if RAID sub-team matches any capability sub-tower key."""
    if not sub_team:
        return False
    for part in sub_team.split("\n"):
        part = part.strip()
        m = re.match(r'[\w\s/-]+:\s*(.*)', part)
        if m:
            desc = m.group(1).strip().lower().replace("&", "and")
            for stk in subtower_keys:
                stk_n = stk.replace("&", "and")
                if desc == stk_n or desc in stk_n or stk_n in desc:
                    return True
    return False


def raid_references_objects(raid_row: dict, obj_ids: set[str]) -> bool:
    """Check if RAID title/description references any of the capability's Object IDs."""
    title = (raid_row.get("Title", "") or "")
    desc = (raid_row.get("Description", "") or "")
    found = _OBJ_ID_RE.findall(title + " " + desc)
    upper_ids = {o.upper() for o in obj_ids}
    return any(ref.upper() in upper_ids for ref in found)


def classify_raid_for_capability(
    raid_row: dict, tower: str, cap_obj_ids: set[str], subtower_keys: set[str],
) -> str:
    """Classify: 'direct', 'subtower', 'tower', 'closed', or 'none'."""
    status = (raid_row.get("Status") or "").strip()
    if status in ("Complete", "Cancelled"):
        return "closed"

    impacted = raid_row.get("Impacted Teams", "")
    assigned_team = raid_row.get("Assigned To (Team)", "")
    if not raid_impacts_tower(impacted, tower) and not raid_impacts_tower(assigned_team, tower):
        return "none"

    # Tier 1: Object ID reference (strongest)
    if cap_obj_ids and raid_references_objects(raid_row, cap_obj_ids):
        return "direct"

    # Tier 2: Sub-team matches sub-tower
    sub_team = raid_row.get("Assigned To (Sub-Team)", "")
    if subtower_keys and raid_subteam_matches_subtowers(sub_team, subtower_keys):
        return "subtower"

    # Tier 3: Tower-level
    return "tower"


def get_capability_raid_items(
    raid_rows: list[dict], tower: str, cap_obj_ids: set[str], subtower_keys: set[str],
) -> dict:
    result = {"direct": [], "subtower": [], "tower": []}
    closed_count = 0
    sev_order = {"P0 - Showstopper": 0, "P1 - High": 1, "P2 - Medium": 2, "P3 - Low": 3}

    for r in raid_rows:
        cls = classify_raid_for_capability(r, tower, cap_obj_ids, subtower_keys)
        if cls in ("direct", "subtower", "tower"):
            result[cls].append(r)
        elif cls == "closed":
            impacted = r.get("Impacted Teams", "")
            if raid_impacts_tower(impacted, tower):
                closed_count += 1

    for key in ("direct", "subtower", "tower"):
        result[key].sort(key=lambda x: sev_order.get(x.get("RAID Severity", ""), 99))

    result["closed_count"] = closed_count
    return result


# ══════════════════════════════════════════════════════════════
# Section builders
# ══════════════════════════════════════════════════════════════

def get_ricefw_status_summary(objects: list[dict]) -> dict:
    statuses = Counter()
    types = Counter()
    complexities = Counter()
    type_map = {
        "01.report": "R", "report": "R", "02.interface": "I", "interface": "I",
        "03.conversion": "C", "conversion": "C", "12.manual conversion": "C",
        "04.enhancement": "E", "enhancement": "E", "05.form": "F", "form": "F",
        "06.workflow": "W", "workflow": "W",
    }
    for r in objects:
        s = r.get("Object Status", "") or "(blank)"
        statuses[s] += 1
        obj_type = r.get("Object Type", "").strip().lower()
        code = type_map.get(obj_type, obj_type[:1].upper() if obj_type else "?")
        types[code] += 1
        c = r.get("Technical Complexity", "")
        if c:
            complexities[c] += 1
    return {"statuses": statuses, "types": types, "complexities": complexities, "total": len(objects)}


def _phase_cell(date_str: str, pct_str: str) -> str:
    """Format a phase cell combining date and completion %."""
    if not date_str:
        return "\u2014"
    try:
        dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
        short = dt.strftime("%b-%y")
    except ValueError:
        short = date_str.strip()
    try:
        pct = float(pct_str)
        p = f"{int(pct * 100)}%"
    except (ValueError, TypeError):
        p = ""
    return f"{short} ({p})" if p else short


def _sanitize_cell(value: str, max_len: int = 0) -> str:
    """Sanitize a value for markdown table cell."""
    if not value:
        return ""
    s = str(value).replace("\r\n", " ").replace("\n", " ").replace("|", "/")
    s = " ".join(s.split())
    if max_len and len(s) > max_len:
        s = s[:max_len - 3] + "..."
    return s


def build_roadmap_section(
    tower: str, cap_obj_ids: set[str], obj_rows: list[dict],
) -> list[str]:
    """Build section 7.1 — compact 7-column layout with full descriptions."""
    if cap_obj_ids:
        cap_rows = [r for r in obj_rows if r.get("Object ID", "").strip() in cap_obj_ids]
    else:
        cap_rows = []
    if not cap_rows:
        cap_rows = [r for r in obj_rows if _normalize_tower(r.get("Tower Name", "")) == tower]

    # Filter to rows that have at least some timeline data
    timeline_rows = [r for r in cap_rows if (r.get("FS Plan Finish Date") or
                                              r.get("S/4 TDD Plan Finish Date") or
                                              r.get("S/4 Build & TUT Plan Finish Date") or
                                              r.get("FUT Plan Finish Date"))]

    lines = ["### 7.1 Project Roadmap & Go-Live Plan\n", "\n"]

    if not timeline_rows:
        lines.append("*No timeline data available for this capability.*\n")
        lines.append("\n")
        return lines

    lines.append(f"*{len(timeline_rows)} objects with timeline data (source: Object Tracker)*\n")
    lines.append("\n")
    lines.append("| ID | Description | FS | TDD | Build | FUT | Status |\n")
    lines.append("|----|-------------|----|-----|-------|-----|--------|\n")

    show_rows = timeline_rows[:30]
    for r in show_rows:
        oid = r.get("Object ID", "")
        desc = _sanitize_cell(r.get("Description", ""))
        fs = _phase_cell(r.get("FS Plan Finish Date", ""), r.get("FS % Complete", ""))
        tdd = _phase_cell(r.get("S/4 TDD Plan Finish Date", ""), r.get("S/4 TDD % Complete", ""))
        build = _phase_cell(r.get("S/4 Build & TUT Plan Finish Date", ""), r.get("S/4 Build & TUT % Complete", ""))
        fut = _phase_cell(r.get("FUT Plan Finish Date", ""), r.get("FUT % Complete", ""))
        status = _sanitize_cell(r.get("FUT On Track/ Off Track", ""), 20)
        lines.append(f"| {oid} | {desc} | {fs} | {tdd} | {build} | {fut} | {status} |\n")

    if len(timeline_rows) > 30:
        lines.append(f"\n*... and {len(timeline_rows) - 30} more objects (see full Object Tracker)*\n")
    lines.append("\n")
    return lines


def build_ricefw_status_section(
    tower: str, cap_obj_ids: set[str], obj_rows: list[dict],
) -> list[str]:
    """Build section 6.2 — capability-specific if possible, else tower-level."""
    if cap_obj_ids:
        cap_rows = [r for r in obj_rows if r.get("Object ID", "").strip() in cap_obj_ids]
    else:
        cap_rows = []

    tower_rows = [r for r in obj_rows if _normalize_tower(r.get("Tower Name", "")) == tower]
    scope_rows = cap_rows if cap_rows else tower_rows
    summary = get_ricefw_status_summary(scope_rows)
    tower_summary = get_ricefw_status_summary(tower_rows)

    lines = ["### 6.2 SAP Development Object Status\n", "\n"]

    if cap_rows:
        lines.append(f"**Capability RICEFW Status** ({summary['total']} objects)\n")
    else:
        lines.append(f"**RICEFW Status Summary** — {tower} Tower ({summary['total']} objects)\n")
    lines.append(f"*Data source: Smartsheet Object Tracker (cached {datetime.now().strftime('%Y-%m-%d')})*\n")
    lines.append("\n")

    lines.append("| Status | Count | % |\n")
    lines.append("|--------|------:|----:|\n")
    for status, cnt in sorted(summary["statuses"].items(), key=lambda x: -x[1]):
        pct = cnt / summary["total"] * 100 if summary["total"] else 0
        lines.append(f"| {status} | {cnt} | {pct:.1f}% |\n")
    lines.append(f"| **Total** | **{summary['total']}** | **100%** |\n")

    lines.append("\n**RICEFW by Type:**\n\n")
    lines.append("| Type | Count |\n")
    lines.append("|------|------:|\n")
    type_labels = {"R": "Report", "I": "Interface", "C": "Conversion", "E": "Enhancement", "F": "Form", "W": "Workflow"}
    for code in ["R", "I", "C", "E", "F", "W"]:
        cnt = summary["types"].get(code, 0)
        if cnt:
            lines.append(f"| {type_labels.get(code, code)} ({code}) | {cnt} |\n")
    lines.append(f"| **Total** | **{summary['total']}** |\n")

    if summary["complexities"]:
        lines.append("\n**Technical Complexity:**\n\n")
        lines.append("| Complexity | Count |\n")
        lines.append("|------------|------:|\n")
        for c, cnt in sorted(summary["complexities"].items()):
            lines.append(f"| {c} | {cnt} |\n")

    active_statuses = {s for s in summary["statuses"]
                       if "Complete" not in s and "Rejected" not in s and "Cancelled" not in s}
    if active_statuses:
        active_rows = [r for r in scope_rows if r.get("Object Status", "") in active_statuses]
        if active_rows:
            lines.append("\n**Active (Non-Complete) Objects:**\n\n")
            lines.append("| Object ID | Type | Description | Status | Complexity |\n")
            lines.append("|-----------|------|-------------|--------|------------|\n")
            for r in active_rows[:50]:
                oid = r.get("Object ID", "")
                otype = r.get("Object Type", "")
                desc = (r.get("Description", "") or "")[:80]
                st = r.get("Object Status", "")
                cx = r.get("Technical Complexity", "")
                el = "..." if len(r.get("Description", "") or "") > 80 else ""
                lines.append(f"| {oid} | {otype} | {desc}{el} | {st} | {cx} |\n")

    if cap_rows and tower_summary["total"] > summary["total"]:
        complete = tower_summary["statuses"].get("10. Object Complete", 0)
        lines.append(f"\n**Tower Context:** {tower} has {tower_summary['total']} total RICEFW objects ")
        lines.append(f"({complete} complete, {tower_summary['total'] - complete} active/other)\n")

    lines.append("\n")
    return lines


def _raid_table_row(r: dict) -> str:
    raid_id = r.get("RAID ID", "")
    rtype = r.get("RAID Type", "")
    sev = r.get("RAID Severity", "")
    title = (r.get("Title", "") or "").replace("\n", " ")[:60]
    status = r.get("Status", "")
    assigned = (r.get("Assigned To (Team)", "") or "")[:25]
    due = r.get("Due Date", "")
    el = "..." if len((r.get("Title", "") or "").replace("\n", " ")) > 60 else ""
    return f"| {raid_id} | {rtype} | {sev} | {title}{el} | {status} | {assigned} | {due} |\n"


def build_raid_section(
    tower: str, cap_obj_ids: set[str], subtower_keys: set[str],
    subtower_names: set[str], raid_rows: list[dict], e2e_raid_rows: list[dict],
) -> list[str]:
    classified = get_capability_raid_items(raid_rows, tower, cap_obj_ids, subtower_keys)
    direct = classified["direct"]
    subtower = classified["subtower"]
    tower_level = classified["tower"]
    closed_count = classified["closed_count"]

    total_cap = len(direct) + len(subtower)
    total_tower = len(tower_level)
    total_open = total_cap + total_tower

    lines = [
        "### 7.2 RAID Log\n", "\n",
        f"*Live data from Smartsheet Master RAID Log — extracted {datetime.now().strftime('%Y-%m-%d')}*\n",
        "\n",
    ]

    if subtower_names:
        lines.append(f"**Mapped sub-tower(s):** {', '.join(sorted(subtower_names))}\n\n")

    lines.append(f"**RAID Summary:** {total_open} open items ({total_cap} capability-specific, {total_tower} tower-level), {closed_count} closed\n\n")

    all_open = direct + subtower + tower_level
    if all_open:
        cap_sev = Counter(r.get("RAID Severity", "") for r in direct + subtower)
        twr_sev = Counter(r.get("RAID Severity", "") for r in tower_level)
        lines.append("| Severity | Capability | Tower-Wide | Total Open |\n")
        lines.append("|----------|----------:|-----------:|-----------:|\n")
        for sev in ["P0 - Showstopper", "P1 - High", "P2 - Medium", "P3 - Low"]:
            c = cap_sev.get(sev, 0)
            t = twr_sev.get(sev, 0)
            if c + t:
                lines.append(f"| {sev} | {c} | {t} | {c + t} |\n")
        lines.append(f"| **Total** | **{total_cap}** | **{total_tower}** | **{total_open}** |\n\n")

    cap_items = direct + subtower
    if cap_items:
        lines.append("**Capability-Specific RAID Items:**\n\n")
        lines.append("| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |\n")
        lines.append("|---------|------|----------|-------|--------|-------------|----------|\n")
        for r in cap_items:
            lines.append(_raid_table_row(r))
        lines.append("\n")

    if tower_level:
        lines.append(f"**Other {tower} Tower RAID Items** ({len(tower_level)} open):\n\n")
        lines.append("| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |\n")
        lines.append("|---------|------|----------|-------|--------|-------------|----------|\n")
        for r in tower_level[:30]:
            lines.append(_raid_table_row(r))
        if len(tower_level) > 30:
            lines.append(f"| | | | *... and {len(tower_level) - 30} more tower-level items* | | | |\n")
        lines.append("\n")

    if not all_open:
        lines.append("**No open RAID items for this capability or tower.**\n\n")

    return lines


# ══════════════════════════════════════════════════════════════
# Document updater
# ══════════════════════════════════════════════════════════════

def update_sad_document(
    filepath: Path, tower: str, obj_rows: list[dict],
    raid_rows: list[dict], e2e_raid_rows: list[dict],
    dry_run: bool = False,
) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    lines_nl = [line + "\n" for line in content.split("\n")]

    # Extract capability's RICEFW Object IDs from section 5.5
    cap_obj_ids = extract_section55_object_ids(content)
    subtower_names = get_subtowers_for_objects(cap_obj_ids, obj_rows)
    subtower_keys = {normalize_subtower_key(st) for st in subtower_names}

    changes = {}
    cap_label = f"{len(cap_obj_ids)} objects, {len(subtower_names)} sub-tower(s)"

    # ── Update 7.1 Project Roadmap & Go-Live Plan ──
    s71_start, s71_end = find_section(lines_nl, r'^### 7\.1\s+Project Roadmap')
    if s71_start >= 0:
        new_71 = build_roadmap_section(tower, cap_obj_ids, obj_rows)
        lines_nl[s71_start:s71_end] = new_71
        changes["7.1"] = "roadmap (compact 7-col)"
        content_after = "".join(lines_nl)
        lines_nl = [line if line.endswith("\n") else line + "\n" for line in content_after.split("\n")]

    # ── Update 6.2 SAP Development Object Status ──
    s62_start, s62_end = find_section(lines_nl, r'^### 6\.2\s+SAP Development Object Status')
    if s62_start >= 0:
        new_62 = build_ricefw_status_section(tower, cap_obj_ids, obj_rows)
        lines_nl[s62_start:s62_end] = new_62
        changes["6.2"] = f"capability RICEFW ({cap_label})"
        content_after = "".join(lines_nl)
        lines_nl = [line if line.endswith("\n") else line + "\n" for line in content_after.split("\n")]

    # ── Update 7.2 RAID Log ──
    s72_start, s72_end = find_section(lines_nl, r'^### 7\.2\s+RAID Log')
    if s72_start >= 0:
        classified = get_capability_raid_items(raid_rows, tower, cap_obj_ids, subtower_keys)
        cap_count = len(classified["direct"]) + len(classified["subtower"])
        tower_count = len(classified["tower"])
        new_72 = build_raid_section(tower, cap_obj_ids, subtower_keys, subtower_names,
                                     raid_rows, e2e_raid_rows)
        lines_nl[s72_start:s72_end] = new_72
        changes["7.2"] = f"RAID ({cap_count} cap-specific + {tower_count} tower)"

    if not dry_run:
        new_content = "".join(lines_nl)
        while "\n\n\n" in new_content:
            new_content = new_content.replace("\n\n\n", "\n\n")
        # Update title page (cover image + author)
        new_content = update_title_page(new_content, filepath)
        changes["title"] = "cover image + author"
        # Inject page footers (page number, back-to-TOC, doc title)
        new_content = _clean_legacy_footer_css(new_content)
        new_content = inject_page_footers(new_content)
        changes["footer"] = "page footers"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return changes


# ══════════════════════════════════════════════════════════════
# Document section finder
# ══════════════════════════════════════════════════════════════

def find_section(lines: list[str], heading_pattern: str) -> tuple[int, int]:
    start = -1
    for i, line in enumerate(lines):
        if re.search(heading_pattern, line):
            start = i
            break
    if start < 0:
        return -1, -1
    heading_level = len(re.match(r'^(#+)', lines[start]).group(1))
    end = len(lines)
    for i in range(start + 1, len(lines)):
        m = re.match(r'^(#+)\s', lines[i])
        if m and len(m.group(1)) <= heading_level:
            end = i
            break
    return start, end


# ══════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Update SAD documents with Smartsheet data")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--tower", type=str, help="Only update a specific tower")
    args = parser.parse_args()

    print("Loading data sources...")
    obj_rows = load_object_tracker()
    print(f"  Object Tracker: {len(obj_rows)} rows")
    raid_rows = load_raid_log(RAID_CSV)
    print(f"  Master RAID Log: {len(raid_rows)} rows")
    e2e_raid_rows = load_raid_log(E2E_RAID_CSV)
    print(f"  E2E RAID Log: {len(e2e_raid_rows)} rows")

    sad_files = sorted(TOWERS_DIR.rglob("*-Architecture.md"))
    print(f"\nFound {len(sad_files)} SAD documents")

    if args.tower:
        tf = args.tower.strip().upper()
        sad_files = [f for f in sad_files if f.relative_to(TOWERS_DIR).parts[0].upper() == tf]
        print(f"  Filtered to tower {tf}: {len(sad_files)} files")

    updated = errors = 0
    for filepath in sad_files:
        rel = filepath.relative_to(TOWERS_DIR)
        tower = rel.parts[0].upper()
        tower_norm = {"FTS-IF": "FTS-IF", "FTS-IP": "FTS-IP", "OTC-IF": "OTC-IF",
                      "OTC-IP": "OTC-IP", "FPR": "FPR", "PTP": "PTP", "MDM": "MDM", "E2E": "E2E"}
        tower = tower_norm.get(tower, tower)

        try:
            changes = update_sad_document(filepath, tower, obj_rows, raid_rows, e2e_raid_rows,
                                          dry_run=args.dry_run)
            if changes:
                updated += 1
                pfx = "[DRY RUN] " if args.dry_run else ""
                print(f"  {pfx}{rel}: {', '.join(f'{k}={v}' for k, v in changes.items())}")
        except Exception as e:
            errors += 1
            print(f"  ERROR {rel}: {e}")

    print(f"\n{'='*60}")
    print(f"{'DRY RUN ' if args.dry_run else ''}SUMMARY: Updated={updated}, Errors={errors}, Total={len(sad_files)}")


if __name__ == "__main__":
    main()
