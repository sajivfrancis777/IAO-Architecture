"""fetch_smartsheet_data.py — Extract all accessible Smartsheet data to CSV cache.

Fetches sheets via the Smartsheet REST API (PAT auth). Sheets blocked by
MFA policy are skipped with a warning — use manual CSV export for those.

Outputs:
  data/smartsheet/raid/master_raid_log.csv
  data/smartsheet/raid/e2e_raid_log.csv
  data/smartsheet/object_trackers/s4_r3_object_tracker.csv  (if accessible)
  data/smartsheet/boundary_apps/boundary_app_tracker.csv     (if accessible)
  data/smartsheet/_extraction_metadata.json                  (log)

Usage:
    python scripts/fetch_smartsheet_data.py              # all sheets
    python scripts/fetch_smartsheet_data.py --dry-run    # preview only
    python scripts/fetch_smartsheet_data.py --sheet raid  # just RAID sheets

CI-safe: no GUI, no MCP dependency, reads .env for token.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import urllib3
from dotenv import load_dotenv

# ── Bootstrap ────────────────────────────────────────────────────
WORKSPACE = Path(__file__).resolve().parent.parent
load_dotenv(WORKSPACE / ".env")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SMARTSHEET_API = "https://api.smartsheet.com/2.0"
TOKEN = os.environ.get("SMARTSHEET_TOKEN", "")
TIMEOUT = 30

# ── Sheet registry ───────────────────────────────────────────────

SHEETS = {
    "object_tracker": {
        "id": "5077868279189380",
        "output": "data/smartsheet/object_trackers/s4_r3_object_tracker.csv",
        "description": "S4 R3 Object Tracker (RICEFW master)",
        "group": "ricefw",
    },
    "master_raid_log": {
        "id": "2062365868642180",
        "output": "data/smartsheet/raid/master_raid_log.csv",
        "description": "Master RAID Log (all towers)",
        "group": "raid",
    },
    "e2e_raid_log": {
        "id": "2147893813137284",
        "output": "data/smartsheet/raid/e2e_raid_log.csv",
        "description": "E2E RAID Log",
        "group": "raid",
    },
    "deliverables_tracker": {
        "id": "8568208059486084",
        "output": "data/smartsheet/boundary_apps/boundary_app_tracker.csv",
        "description": "Deliverables / Boundary App Tracker",
        "group": "other",
    },
    "change_request_log": {
        "id": "8701667910307716",
        "output": "data/smartsheet/change_requests/change_request_log.csv",
        "description": "Change Request Log",
        "group": "other",
    },
    "ricefw_request_console": {
        "id": "216957114601348",
        "output": "data/smartsheet/request_console/ricefw_request_console.csv",
        "description": "RICEFW Request Console",
        "group": "other",
    },
}


def api_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}


def fetch_sheet_to_csv(
    sheet_name: str,
    sheet_id: str,
    output_path: Path,
    dry_run: bool = False,
) -> dict:
    """Fetch a Smartsheet sheet and write to CSV. Returns extraction metadata."""
    result = {
        "sheet": sheet_name,
        "sheet_id": sheet_id,
        "output": str(output_path),
        "status": "unknown",
        "rows": 0,
        "columns": 0,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    try:
        # Fetch sheet metadata + all rows (paginated)
        url = f"{SMARTSHEET_API}/sheets/{sheet_id}"
        all_rows = []
        columns = []
        page = 1
        page_size = 500  # Smartsheet max per page
        total_row_count = None

        while True:
            resp = requests.get(
                url,
                headers=api_headers(),
                params={"pageSize": page_size, "page": page},
                timeout=TIMEOUT,
            )

            if resp.status_code == 403:
                msg = resp.json().get("message", "Access denied")
                if "MFA" in msg:
                    result["status"] = "mfa_blocked"
                    result["error"] = msg
                    print(f"  ⚠ {sheet_name}: MFA-blocked — use manual CSV export")
                    return result
                result["status"] = "forbidden"
                result["error"] = msg
                print(f"  ✗ {sheet_name}: 403 — {msg}")
                return result

            if not resp.ok:
                result["status"] = "error"
                result["error"] = f"HTTP {resp.status_code}"
                print(f"  ✗ {sheet_name}: HTTP {resp.status_code}")
                return result

            data = resp.json()

            # Get columns and total from first page
            if not columns:
                columns = [c["title"] for c in data.get("columns", [])]
                total_row_count = data.get("totalRowCount", 0)

            # Extract row cell values
            for row in data.get("rows", []):
                cells = row.get("cells", [])
                row_values = {}
                for i, cell in enumerate(cells):
                    if i < len(columns):
                        val = cell.get("displayValue") or cell.get("value", "")
                        row_values[columns[i]] = str(val) if val is not None else ""
                all_rows.append(row_values)

            # Calculate pagination from totalRowCount
            rows_fetched = len(all_rows)
            if total_row_count and rows_fetched < total_row_count:
                page += 1
                time.sleep(0.3)  # Rate limit courtesy
            else:
                break

        result["rows"] = len(all_rows)
        result["columns"] = len(columns)

        if dry_run:
            result["status"] = "dry_run"
            print(f"  ✓ {sheet_name}: {len(all_rows)} rows × {len(columns)} cols (dry run)")
            return result

        # Write CSV
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(all_rows)

        result["status"] = "ok"
        print(f"  ✓ {sheet_name}: {len(all_rows)} rows × {len(columns)} cols → {output_path}")
        return result

    except requests.exceptions.Timeout:
        result["status"] = "timeout"
        result["error"] = "Request timed out"
        print(f"  ✗ {sheet_name}: timeout")
        return result
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)[:200]
        print(f"  ✗ {sheet_name}: {e}")
        return result


def main():
    parser = argparse.ArgumentParser(description="Fetch Smartsheet data to CSV cache")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't write files")
    parser.add_argument(
        "--sheet",
        choices=["all", "raid", "ricefw", "other"],
        default="all",
        help="Which sheet group to fetch (default: all)",
    )
    args = parser.parse_args()

    if not TOKEN:
        print("ERROR: SMARTSHEET_TOKEN not set in .env")
        sys.exit(1)

    # Verify token
    me_resp = requests.get(
        f"{SMARTSHEET_API}/users/me", headers=api_headers(), timeout=15
    )
    if not me_resp.ok:
        print(f"ERROR: Token validation failed ({me_resp.status_code})")
        sys.exit(1)
    user = me_resp.json()
    print(f"Authenticated as: {user.get('email', '?')}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"Group: {args.sheet}")
    print()

    # Filter sheets by group
    targets = {
        name: info
        for name, info in SHEETS.items()
        if args.sheet == "all" or info["group"] == args.sheet
    }

    results = []
    ok_count = 0
    skip_count = 0

    for name, info in targets.items():
        output = WORKSPACE / info["output"]
        result = fetch_sheet_to_csv(name, info["id"], output, dry_run=args.dry_run)
        results.append(result)
        if result["status"] == "ok" or result["status"] == "dry_run":
            ok_count += 1
        else:
            skip_count += 1

    # Write metadata log
    meta_path = WORKSPACE / "data" / "smartsheet" / "_extraction_metadata.json"
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "extraction_time": datetime.now(timezone.utc).isoformat(),
        "user": user.get("email"),
        "mode": "dry_run" if args.dry_run else "live",
        "sheets": results,
        "summary": {"ok": ok_count, "skipped": skip_count, "total": len(results)},
    }
    if not args.dry_run:
        meta_path.write_text(json.dumps(meta, indent=2))

    print(f"\nDone: {ok_count} extracted, {skip_count} skipped")


if __name__ == "__main__":
    main()
