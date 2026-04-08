"""convert_smartsheet_xlsx.py — Convert manually-exported Smartsheet .xlsx files to CSV.

Scans data/smartsheet/manual/ for .xlsx files and converts each to the pipeline's
expected .csv file.  Mapping is by folder:
  manual/object_trackers/*.xlsx  → s4_r3_object_tracker.csv
  manual/boundary_apps/*.xlsx    → boundary_app_tracker.csv
  manual/change_requests/*.xlsx  → change_request_log.csv
  manual/request_console/*.xlsx  → ricefw_request_console.csv
  manual/timelines/*.xlsx        → integrated_plan.csv

Usage:
    python scripts/convert_smartsheet_xlsx.py           # convert all
    python scripts/convert_smartsheet_xlsx.py --dry-run # preview only
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

try:
    import openpyxl
except ImportError:
    print("openpyxl not installed — run: pip install openpyxl")
    sys.exit(1)

WORKSPACE = Path(__file__).resolve().parent.parent
SS_DIR = WORKSPACE / "data" / "smartsheet" / "manual"

# Map: (subdirectory) → target CSV name
FOLDER_MAP = {
    "object_trackers": "s4_r3_object_tracker.csv",
    "boundary_apps": "boundary_app_tracker.csv",
    "change_requests": "change_request_log.csv",
    "request_console": "ricefw_request_console.csv",
    "timelines": "integrated_plan.csv",
}


def convert_xlsx_to_csv(xlsx_path: Path, csv_path: Path, dry_run: bool = False) -> int:
    """Convert first sheet of xlsx to CSV. Returns row count."""
    wb = openpyxl.load_workbook(str(xlsx_path), read_only=True, data_only=True)
    ws = wb.active

    rows = []
    headers = []
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i == 0:
            headers = [str(c) if c is not None else "" for c in row]
            continue
        row_dict = {}
        for j, val in enumerate(row):
            if j < len(headers):
                row_dict[headers[j]] = str(val) if val is not None else ""
        rows.append(row_dict)
    wb.close()

    if dry_run:
        print(f"  DRY RUN: {xlsx_path.name} → {csv_path.name} ({len(rows)} rows × {len(headers)} cols)")
        return len(rows)

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"  ✓ {xlsx_path.name} → {csv_path.name} ({len(rows)} rows × {len(headers)} cols)")
    return len(rows)


def resolve_csv_target(xlsx_path: Path) -> Path | None:
    """Determine the target CSV path for a given xlsx file."""
    parent_name = xlsx_path.parent.name

    if parent_name in FOLDER_MAP:
        mapping = FOLDER_MAP[parent_name]
        if isinstance(mapping, str):
            return xlsx_path.parent / mapping
    return None


def main():
    parser = argparse.ArgumentParser(description="Convert Smartsheet .xlsx exports to CSV")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    print("Scanning for .xlsx files in data/smartsheet/manual/...")
    xlsx_files = list(SS_DIR.rglob("*.xlsx"))

    if not xlsx_files:
        print("  No .xlsx files found. Export from Smartsheet and place in:")
        for folder in FOLDER_MAP:
            print(f"    data/smartsheet/manual/{folder}/")
        return

    converted = 0
    for xlsx in sorted(xlsx_files):
        target = resolve_csv_target(xlsx)
        if target:
            convert_xlsx_to_csv(xlsx, target, dry_run=args.dry_run)
            converted += 1
        else:
            print(f"  SKIP: {xlsx} (not in a recognized folder)")

    print(f"\nConverted: {converted} files")
    if not args.dry_run and converted:
        print("CSV files updated — run pipeline to regenerate docs.")


if __name__ == "__main__":
    main()
