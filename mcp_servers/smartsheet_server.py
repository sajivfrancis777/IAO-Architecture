"""smartsheet_server.py — MCP server for live Smartsheet API queries.

Exposes tools for querying RICEFW objects, RAID items, timelines,
and raw sheet data from the Smartsheet API.  Falls back to local CSV
cache when the API token is missing or the sheet is MFA-blocked.

Run:
    python -m mcp_servers.smartsheet_server

Or register in VS Code settings.json as an MCP server (stdio transport).
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# ── Bootstrap ───────────────────────────────────────────────────────
_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")
sys.path.insert(0, str(_ROOT))

from src.smartsheet_loader import SmartsheetLoader, SmartsheetData  # noqa: E402

# ── Constants ───────────────────────────────────────────────────────
SMARTSHEET_API = "https://api.smartsheet.com/2.0"
OBJECT_TRACKER_SHEET_ID = "5077868279189380"
OBJECT_TRACKER_CSV = _ROOT / "data" / "smartsheet" / "manual" / "object_trackers" / "s4_r3_object_tracker.csv"

# Key sheet IDs discovered during probing
KNOWN_SHEETS: dict[str, str] = {
    "object_tracker": "5077868279189380",
    "master_raid_log": "2062365868642180",
    "e2e_raid_log": "2147893813137284",
    "deliverables_tracker": "8568208059486084",
    "change_request_log": "8701667910307716",
    "ricefw_request_console": "216957114601348",
}

# ── MCP Server ──────────────────────────────────────────────────────
mcp = FastMCP(
    "IAO Smartsheet",
    instructions=(
        "Provides live access to Intel IAO Smartsheet data — RICEFW objects, "
        "RAID logs, timelines, and raw sheet reads.  Use these tools to answer "
        "questions about current project status, object counts, blockers, and "
        "delivery milestones across IDM 2.0 towers."
    ),
)


def _token() -> str:
    return os.environ.get("SMARTSHEET_TOKEN", "")


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {_token()}",
        "Content-Type": "application/json",
    }


def _api_get(endpoint: str, params: dict | None = None) -> dict[str, Any]:
    """Call Smartsheet API with error handling."""
    if not _token():
        raise RuntimeError(
            "SMARTSHEET_TOKEN not set in .env — cannot make live API calls. "
            "Falling back to cached CSV."
        )
    url = f"{SMARTSHEET_API}{endpoint}"
    resp = requests.get(url, headers=_headers(), params=params, timeout=30)
    if resp.status_code == 403:
        data = resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {}
        code = data.get("errorCode", 0)
        if code == 1362:
            raise RuntimeError(f"MFA policy blocks access to this sheet (error 1362)")
        raise RuntimeError(f"Access denied: {resp.status_code} — {data.get('message', resp.text[:200])}")
    resp.raise_for_status()
    return resp.json()


def _get_loader() -> SmartsheetLoader:
    """Return a SmartsheetLoader populated from the local CSV cache."""
    loader = SmartsheetLoader()
    if OBJECT_TRACKER_CSV.exists():
        loader.load_csv(str(OBJECT_TRACKER_CSV))
    return loader


def _smartsheet_data_to_dict(data: SmartsheetData) -> dict[str, Any]:
    """Serialize SmartsheetData to a JSON-friendly dict."""
    return {
        "ricefw": [
            {
                "object_id": r.object_id,
                "type": r.type_label,
                "type_code": r.type_code,
                "description": r.description,
                "tower": r.tower_name,
                "sub_tower": r.sub_tower,
                "status": r.status,
                "source_system": r.source_system,
                "target_system": r.target_system,
                "middleware": r.middleware,
                "complexity": r.technical_complexity,
                "fs_pct": r.fs_pct,
                "build_pct": r.build_pct,
                "fut_pct": r.fut_pct,
            }
            for r in data.ricefw
        ],
        "raid": [
            {
                "object_id": r.object_id,
                "category": r.category,
                "text": r.raid_text,
                "status": r.status,
                "assigned_to": r.assigned_to,
                "created_date": r.created_date,
            }
            for r in data.raid
        ],
        "timeline": [
            {
                "object_id": t.object_id,
                "description": t.description,
                "fs_end": t.fs_end,
                "fs_pct": t.fs_pct,
                "tdd_end": t.tdd_end,
                "tdd_pct": t.tdd_pct,
                "build_end": t.build_end,
                "build_pct": t.build_pct,
                "fut_end": t.fut_end,
                "fut_pct": t.fut_pct,
                "overall_status": t.overall_status,
            }
            for t in data.timeline
        ],
        "summary": data.ricefw_summary,
        "total_ricefw": len(data.ricefw),
        "total_raid": len(data.raid),
    }


# ── TOOLS ───────────────────────────────────────────────────────────


@mcp.tool()
def get_ricefw_objects(
    tower: str,
    capability_name: str = "",
    object_type: str = "",
) -> str:
    """Get RICEFW objects for a tower or capability.

    Args:
        tower: Tower shortcode (FPR, OTC-IF, OTC-IP, FTS-IF, FTS-IP, PTP, MDM, E2E)
        capability_name: Optional capability name to filter (e.g. "Provide Decision Support")
        object_type: Optional RICEFW type filter (R=Report, I=Interface, C=Conversion, E=Enhancement, F=Form, W=Workflow)

    Returns:
        JSON with matching RICEFW objects, counts, and summary.
    """
    loader = _get_loader()
    tower_upper = tower.strip().upper()

    if capability_name:
        data = loader.get_capability_data(tower_upper, cap_name=capability_name)
    else:
        data = loader.get_tower_data(tower_upper)

    result = _smartsheet_data_to_dict(data)

    # Apply type filter if specified
    if object_type:
        code = object_type.strip().upper()[:1]
        result["ricefw"] = [r for r in result["ricefw"] if r["type_code"] == code]
        result["total_ricefw"] = len(result["ricefw"])

    # Only return RICEFW portion
    return json.dumps(
        {
            "tower": tower_upper,
            "capability": capability_name or "(all)",
            "ricefw": result["ricefw"],
            "total": result["total_ricefw"],
            "summary": result["summary"],
            "source": "local_csv_cache",
        },
        indent=2,
    )


@mcp.tool()
def get_raid_items(
    tower: str,
    capability_name: str = "",
    status_filter: str = "",
) -> str:
    """Get RAID (Risk, Assumption, Issue, Dependency) items for a tower or capability.

    Args:
        tower: Tower shortcode (FPR, OTC-IF, OTC-IP, FTS-IF, FTS-IP, PTP, MDM, E2E)
        capability_name: Optional capability name to filter
        status_filter: Optional status filter (e.g. "Open", "In Progress")

    Returns:
        JSON with matching RAID entries.
    """
    loader = _get_loader()
    tower_upper = tower.strip().upper()

    if capability_name:
        data = loader.get_capability_data(tower_upper, cap_name=capability_name)
    else:
        data = loader.get_tower_data(tower_upper)

    result = _smartsheet_data_to_dict(data)
    raid = result["raid"]

    if status_filter:
        sf = status_filter.strip().lower()
        raid = [r for r in raid if sf in r["status"].lower()]

    return json.dumps(
        {
            "tower": tower_upper,
            "capability": capability_name or "(all)",
            "raid_items": raid,
            "total": len(raid),
            "source": "local_csv_cache",
        },
        indent=2,
    )


@mcp.tool()
def get_timeline(
    tower: str,
    capability_name: str = "",
) -> str:
    """Get delivery timeline milestones (FS, TDD, Build, FUT dates) for a tower or capability.

    Args:
        tower: Tower shortcode (FPR, OTC-IF, OTC-IP, FTS-IF, FTS-IP, PTP, MDM, E2E)
        capability_name: Optional capability name to filter

    Returns:
        JSON with timeline milestones per RICEFW object.
    """
    loader = _get_loader()
    tower_upper = tower.strip().upper()

    if capability_name:
        data = loader.get_capability_data(tower_upper, cap_name=capability_name)
    else:
        data = loader.get_tower_data(tower_upper)

    result = _smartsheet_data_to_dict(data)

    return json.dumps(
        {
            "tower": tower_upper,
            "capability": capability_name or "(all)",
            "timeline": result["timeline"],
            "total": len(result["timeline"]),
            "source": "local_csv_cache",
        },
        indent=2,
    )


@mcp.tool()
def get_tower_summary(tower: str) -> str:
    """Get a high-level summary for a tower — RICEFW counts by type, RAID count, phase completion averages.

    Args:
        tower: Tower shortcode (FPR, OTC-IF, OTC-IP, FTS-IF, FTS-IP, PTP, MDM, E2E)

    Returns:
        JSON summary with counts and completion percentages.
    """
    loader = _get_loader()
    tower_upper = tower.strip().upper()
    data = loader.get_tower_data(tower_upper)

    # Compute average completion percentages
    def _avg_pct(values: list[str]) -> str:
        nums = []
        for v in values:
            v = v.strip().rstrip("%")
            try:
                nums.append(float(v))
            except ValueError:
                pass
        return f"{sum(nums) / len(nums):.0f}%" if nums else "N/A"

    return json.dumps(
        {
            "tower": tower_upper,
            "total_ricefw": len(data.ricefw),
            "reports": data.report_count,
            "interfaces": data.interface_count,
            "conversions": data.conversion_count,
            "enhancements": data.enhancement_count,
            "forms": data.form_count,
            "workflows": data.workflow_count,
            "total_raid": len(data.raid),
            "avg_fs_completion": _avg_pct([r.fs_pct for r in data.ricefw]),
            "avg_build_completion": _avg_pct([r.build_pct for r in data.ricefw]),
            "avg_fut_completion": _avg_pct([r.fut_pct for r in data.ricefw]),
            "summary": data.ricefw_summary,
            "source": "local_csv_cache",
        },
        indent=2,
    )


@mcp.tool()
def read_sheet_live(
    sheet_id: str = "",
    sheet_name: str = "",
    max_rows: int = 50,
) -> str:
    """Read rows from a Smartsheet sheet via the live API.

    Requires SMARTSHEET_TOKEN in .env. Use for real-time queries when
    cached data may be stale.

    Args:
        sheet_id: Smartsheet sheet ID (numeric string). If omitted, uses sheet_name lookup.
        sheet_name: Friendly name to look up (e.g. "object_tracker", "master_raid_log")
        max_rows: Maximum rows to return (default 50, max 500)

    Returns:
        JSON with column names and row data from the live sheet.
    """
    # Resolve sheet ID
    if not sheet_id:
        sheet_id = KNOWN_SHEETS.get(sheet_name.strip().lower(), "")
    if not sheet_id:
        available = ", ".join(sorted(KNOWN_SHEETS.keys()))
        return json.dumps({"error": f"Unknown sheet. Available: {available}"})

    max_rows = min(max(1, max_rows), 500)

    try:
        data = _api_get(f"/sheets/{sheet_id}", params={"pageSize": max_rows})
    except RuntimeError as e:
        return json.dumps({"error": str(e), "fallback": "Use cached tools instead (get_ricefw_objects, get_raid_items)"})

    columns = {c["id"]: c["title"] for c in data.get("columns", [])}
    rows_out = []
    for row in data.get("rows", [])[:max_rows]:
        row_data = {}
        for cell in row.get("cells", []):
            col_name = columns.get(cell.get("columnId"), "?")
            row_data[col_name] = cell.get("displayValue") or cell.get("value", "")
        rows_out.append(row_data)

    return json.dumps(
        {
            "sheet_id": sheet_id,
            "sheet_name": data.get("name", ""),
            "total_rows": data.get("totalRowCount", 0),
            "returned_rows": len(rows_out),
            "columns": list(columns.values()),
            "rows": rows_out,
            "source": "live_api",
        },
        indent=2,
    )


@mcp.tool()
def list_known_sheets() -> str:
    """List all known Smartsheet sheet IDs and their friendly names.

    Returns:
        JSON with sheet name to ID mapping.
    """
    return json.dumps(
        {
            "sheets": {name: sid for name, sid in sorted(KNOWN_SHEETS.items())},
            "note": "Use sheet_name or sheet_id with read_sheet_live() for real-time data.",
        },
        indent=2,
    )


# ── Entry Point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run(transport="stdio")
