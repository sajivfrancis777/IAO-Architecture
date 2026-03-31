"""gen_ricefw_tracker.py — Generate RICEFW Tracker documents per tower and capability.

Reads from the Smartsheet Object Tracker CSV + RAID logs and produces per-tower
(and optionally per-capability) RICEFW tracker documents in Markdown format.

Usage:
    python scripts/gen_ricefw_tracker.py --all
    python scripts/gen_ricefw_tracker.py --tower FPR
    python scripts/gen_ricefw_tracker.py --tower FPR --cap DS-020
    python scripts/gen_ricefw_tracker.py --all --dry-run
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass, field
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
OBJECT_TRACKER_CSV = WORKSPACE / "data" / "smartsheet" / "object_trackers" / "s4_r3_object_tracker.csv"
RAID_CSV = WORKSPACE / "data" / "smartsheet" / "raid" / "master_raid_log.csv"

RICEFW_TEMPLATE = "ricefw_tracker.md.j2"

# Status buckets
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
    """Normalize Smartsheet tower names to shortcodes."""
    return _normalize_tower_reg(raw)


def _type_code(raw: str) -> str:
    return _TYPE_CODE.get(raw.strip().lower(), raw[:1].upper() if raw else "?")


def _safe_float(val: str) -> float:
    try:
        v = float(val)
        return v * 100 if v <= 1.0 else v
    except (ValueError, TypeError):
        return 0.0


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class ObjRow:
    object_id: str
    object_type: str
    type_code: str
    description: str
    tower: str
    sub_tower: str
    status: str
    source_system: str
    target_system: str
    middleware: str
    technical_complexity: str
    build_pct: str
    fs_end: str
    fs_pct: str
    tdd_end: str
    tdd_pct: str
    build_end: str
    build_pct_raw: str
    fut_end: str
    fut_pct: str
    overall_status: str
    boundary_app: str
    interface_approach: str


@dataclass
class RAIDRow:
    raid_id: str
    title: str
    description: str
    category: str
    severity: str
    status: str
    assigned_to: str
    tower: str
    sub_team: str
    due_date: str
    object_id: str = ""


@dataclass
class PhaseStats:
    on_track: int = 0
    off_track: int = 0
    not_started: int = 0
    avg_pct: int = 0


# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
def load_object_tracker(csv_path: Path) -> list[ObjRow]:
    """Parse the object tracker CSV into ObjRow records."""
    if not csv_path.exists():
        print(f"  WARNING: Object Tracker not found at {csv_path}")
        return []
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            tower = _normalize_tower(r.get("Tower Name", ""))
            if not tower:
                continue
            obj_id = r.get("Object ID", "").strip()
            if not obj_id:
                continue
            otype = r.get("Object Type", "").strip()
            rows.append(ObjRow(
                object_id=obj_id,
                object_type=otype,
                type_code=_type_code(otype),
                description=r.get("Description", "").strip(),
                tower=tower,
                sub_tower=r.get("Sub-Tower Name", "").strip(),
                status=r.get("Object Status", "").strip(),
                source_system=r.get("Source System", "").strip(),
                target_system=r.get("Target System", "").strip(),
                middleware=r.get("Middleware", "").strip(),
                technical_complexity=r.get("Technical Complexity", "").strip(),
                build_pct=r.get("S/4 Build & TUT % Complete", "").strip(),
                fs_end=r.get("FS Plan Finish Date", "").strip(),
                fs_pct=r.get("FS % Complete", "").strip(),
                tdd_end=r.get("S/4 TDD Plan Finish Date", "").strip(),
                tdd_pct=r.get("S/4 TDD % Complete", "").strip(),
                build_end=r.get("S/4 Build & TUT Plan Finish Date", "").strip(),
                build_pct_raw=r.get("S/4 Build & TUT % Complete", "").strip(),
                fut_end=r.get("FUT Plan Finish Date", "").strip(),
                fut_pct=r.get("FUT % Complete", "").strip(),
                overall_status=r.get("FUT On Track/ Off Track", "").strip(),
                boundary_app=r.get("Boundary Application Name", "").strip(),
                interface_approach=r.get("Interface \u2013 Approach / Clean Core adherence",
                                       r.get("Interface - Approach / Clean Core adherence", "")).strip(),
            ))
    return rows


def load_raid_log(csv_path: Path) -> list[RAIDRow]:
    """Parse the RAID log CSV into RAIDRow records."""
    if not csv_path.exists():
        print(f"  WARNING: RAID log not found at {csv_path}")
        return []
    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            status = r.get("Status", "").strip()
            if status.lower() in ("complete", "closed", "cancelled"):
                continue
            tower_raw = r.get("Assigned To (Team)", "").strip()
            tower = _normalize_tower(tower_raw)
            rows.append(RAIDRow(
                raid_id=r.get("RAID ID", r.get("Original RAID ID", "")).strip(),
                title=r.get("Title", "").strip(),
                description=r.get("Description", "").strip(),
                category=r.get("RAID Type", "").strip(),
                severity=r.get("RAID Severity", "").strip(),
                status=status,
                assigned_to=r.get("Assigned to Name(s)", "").strip(),
                tower=tower,
                sub_team=r.get("Assigned To (Sub-Team)", "").strip(),
                due_date=r.get("Due Date", "").strip(),
            ))
    return rows


# ---------------------------------------------------------------------------
# Build context
# ---------------------------------------------------------------------------
def build_context(
    tower_short: str,
    obj_rows: list[ObjRow],
    raid_rows: list[RAIDRow],
    cap_id: str = "",
    cap_name: str = "",
    l1_process: str = "",
) -> dict:
    """Build the Jinja2 template context for a RICEFW tracker."""

    # Filter objects for this tower
    tower_objs = [o for o in obj_rows if o.tower == tower_short]

    # If capability-level, further filter by sub-tower fuzzy match or object ID pattern
    if cap_id:
        cap_objs = []
        cap_prefix = cap_id.replace("-", "")[:4].upper()
        for o in tower_objs:
            oid = o.object_id.upper().replace("-", "").replace("_", "")
            if cap_prefix and oid.startswith(cap_prefix):
                cap_objs.append(o)
            elif cap_id.lower() in o.sub_tower.lower():
                cap_objs.append(o)
        if cap_objs:
            tower_objs = cap_objs

    # Classify by status
    completed = [o for o in tower_objs if o.status in _COMPLETED_STATUSES]
    rejected = [o for o in tower_objs if o.status in _REJECTED_STATUSES]
    active = [o for o in tower_objs if o not in completed and o not in rejected]

    total = len(tower_objs)

    # Type summary
    type_counter = Counter(o.type_code for o in tower_objs)
    type_order = ["I", "C", "E", "R", "F", "W"]
    type_summary = []
    for code in type_order:
        count = type_counter.get(code, 0)
        if count:
            type_summary.append({
                "code": code,
                "label": _TYPE_LABEL.get(code, code),
                "count": count,
                "pct": round(count / total * 100) if total else 0,
            })

    # Status summary
    status_counter = Counter()
    for o in tower_objs:
        if o.status in _COMPLETED_STATUSES:
            status_counter["Completed"] += 1
        elif o.status in _REJECTED_STATUSES:
            status_counter["Rejected / Cancelled"] += 1
        else:
            status_counter[o.status or "Unknown"] += 1
    status_summary = [
        {"label": label, "count": count, "pct": round(count / total * 100) if total else 0}
        for label, count in status_counter.most_common()
    ]

    # RICEFW summary string
    parts = []
    for code in type_order:
        n = type_counter.get(code, 0)
        if n:
            parts.append(f"{n} {_TYPE_LABEL.get(code, code)}s")
    ricefw_summary = ", ".join(parts) if parts else "No RICEFW objects"

    # Type sections for detailed listing (active only to keep document focused)
    type_sections = []
    for code in type_order:
        label = _TYPE_LABEL.get(code, code)
        section_objs = [o for o in active if o.type_code == code]
        type_sections.append({"code": code, "label": label, "objects": section_objs})

    # Timeline items (active only)
    timeline_items = [o for o in active if o.fs_end or o.build_end or o.fut_end]

    # Phase statistics
    def _phase_stats(pct_attr: str) -> PhaseStats:
        stats = PhaseStats()
        pcts = []
        for o in active:
            pct = _safe_float(getattr(o, pct_attr, ""))
            if pct >= 100:
                stats.on_track += 1
            elif pct > 0:
                stats.on_track += 1  # in progress = on track for now
            else:
                stats.not_started += 1
            pcts.append(pct)
        stats.avg_pct = round(sum(pcts) / len(pcts)) if pcts else 0
        return stats

    phase_stats = {
        "fs": _phase_stats("fs_pct"),
        "tdd": _phase_stats("tdd_pct"),
        "build": _phase_stats("build_pct_raw"),
        "fut": _phase_stats("fut_pct"),
    }

    # Avg completion percentages
    def _avg(attr: str) -> int:
        vals = [_safe_float(getattr(o, attr, "")) for o in tower_objs]
        return round(sum(vals) / len(vals)) if vals else 0

    avg_fs_pct = _avg("fs_pct")
    avg_build_pct = _avg("build_pct_raw")
    avg_fut_pct = _avg("fut_pct")

    # RAID items for this tower
    tower_raids = [r for r in raid_rows if r.tower == tower_short]

    # Generate title
    tower_display = _TOWER_DISPLAY.get(tower_short, tower_short)
    if cap_id:
        title = f"{cap_id} — {cap_name or cap_id}" if cap_name else cap_id
        scope_label = "capability"
    else:
        title = f"{tower_display} ({tower_short})"
        scope_label = "tower"

    # Cover banner path
    if cap_id:
        cover_banner_path = "../../../../../../../templates/assets/ricefw_banner.svg"
    else:
        cover_banner_path = "../../templates/assets/ricefw_banner.svg"

    return {
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
        "total_objects": total,
        "active_count": len(active),
        "completed_count": len(completed),
        "rejected_count": len(rejected),
        "ricefw_summary": ricefw_summary,
        "type_summary": type_summary,
        "status_summary": status_summary,
        "type_sections": type_sections,
        "timeline_items": timeline_items,
        "phase_stats": phase_stats,
        "avg_fs_pct": avg_fs_pct,
        "avg_build_pct": avg_build_pct,
        "avg_fut_pct": avg_fut_pct,
        "raid_items": tower_raids,
    }


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
def generate_tower_tracker(
    tower_short: str,
    obj_rows: list[ObjRow],
    raid_rows: list[RAIDRow],
    jinja_env: Environment,
    cap_filter: str = "",
    dry_run: bool = False,
) -> list[Path]:
    """Generate RICEFW tracker(s) for a tower. Returns list of output paths."""
    tower_dir = TOWERS_DIR / tower_short
    if not tower_dir.exists():
        # Try matching by display name in directory listing
        for d in TOWERS_DIR.iterdir():
            if d.is_dir() and d.name.upper().startswith(tower_short):
                tower_dir = d
                break
        else:
            print(f"  SKIP: Tower directory not found for {tower_short}")
            return []

    template = jinja_env.get_template(RICEFW_TEMPLATE)
    cap_names = _load_cap_names(tower_dir)
    outputs = []

    # Tower-level tracker
    if not cap_filter:
        ctx = build_context(tower_short, obj_rows, raid_rows)
        rendered = template.render(**ctx)
        rendered = _inject_page_footers(rendered, f"{ctx['title']} — RICEFW Tracker")

        out_dir = tower_dir / "output" / "docs" / "ricefw-tracker"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{tower_short}-RICEFW-Tracker.md"

        if dry_run:
            print(f"  [DRY-RUN] Would write: {out_path} ({len(rendered):,} chars)")
        else:
            out_path.write_text(rendered, encoding="utf-8")
            print(f"  Wrote: {out_path}")
        outputs.append(out_path)

    # Capability-level trackers (scan tower directory for L1/cap structure)
    for l1_dir in sorted(tower_dir.iterdir()):
        if not l1_dir.is_dir() or l1_dir.name.startswith(("output", ".", "_")):
            continue
        for cap_dir in sorted(l1_dir.iterdir()):
            if not cap_dir.is_dir():
                continue
            cap_id = cap_dir.name
            if cap_filter and cap_id != cap_filter:
                continue

            resolved_name = cap_names.get(cap_id, cap_id)

            ctx = build_context(
                tower_short, obj_rows, raid_rows,
                cap_id=cap_id,
                cap_name=resolved_name,
                l1_process=l1_dir.name,
            )
            # Skip capabilities with no RICEFW data
            if ctx["total_objects"] == 0 and not cap_filter:
                continue

            rendered = template.render(**ctx)
            rendered = _inject_page_footers(rendered, f"{cap_id} \u2014 {resolved_name}")

            out_dir = cap_dir / "output" / "docs" / "ricefw-tracker"
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{cap_id}-RICEFW-Tracker.md"

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
    parser = argparse.ArgumentParser(description="Generate RICEFW Tracker Documents")
    parser.add_argument("--tower", type=str, help="Tower shortcode (e.g. FPR)")
    parser.add_argument("--cap", type=str, help="Single capability ID (e.g. DS-020)")
    parser.add_argument("--all", action="store_true", help="Generate for all towers")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--tracker-csv", type=str, default=str(OBJECT_TRACKER_CSV))
    parser.add_argument("--raid-csv", type=str, default=str(RAID_CSV))
    args = parser.parse_args()

    if not args.tower and not args.all:
        parser.error("Specify --tower SHORTCODE or --all")

    # Load data
    print("Loading Object Tracker...")
    obj_rows = load_object_tracker(Path(args.tracker_csv))
    print(f"  Loaded {len(obj_rows):,} objects")

    print("Loading RAID Log...")
    raid_rows = load_raid_log(Path(args.raid_csv))
    print(f"  Loaded {len(raid_rows):,} open RAID items")

    # Setup Jinja2
    jinja_env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    def _tablecell(value: str, max_len: int = 80) -> str:
        if not value:
            return ""
        s = str(value).replace("\r\n", " ").replace("\n", " ").replace("|", "/")
        s = " ".join(s.split())
        if len(s) > max_len:
            s = s[: max_len - 3] + "..."
        return s

    jinja_env.filters["tc"] = _tablecell

    def _phase_cell(date_str: str, pct_str: str) -> str:
        if not date_str:
            return "\u2014"
        try:
            dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            short = dt.strftime("%b-%y")
        except ValueError:
            short = date_str.strip()
        try:
            pct = float(pct_str)
            p = f"{int(pct * 100)}%" if pct <= 1.0 else f"{int(pct)}%"
        except (ValueError, TypeError):
            p = ""
        return f"{short} ({p})" if p else short

    jinja_env.globals["phase_cell"] = _phase_cell

    # Generate
    if args.all:
        towers = sorted(d.name for d in TOWERS_DIR.iterdir() if d.is_dir())
        all_outputs = []
        for t in towers:
            print(f"\n{'='*60}")
            print(f"Tower: {t}")
            outputs = generate_tower_tracker(t, obj_rows, raid_rows, jinja_env, dry_run=args.dry_run)
            all_outputs.extend(outputs)
        print(f"\n{'='*60}")
        print(f"TOTAL: {len(all_outputs)} RICEFW tracker(s) generated across {len(towers)} towers")
    else:
        generate_tower_tracker(args.tower, obj_rows, raid_rows, jinja_env,
                               cap_filter=args.cap or "", dry_run=args.dry_run)


if __name__ == "__main__":
    main()
