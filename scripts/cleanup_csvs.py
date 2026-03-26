"""cleanup_csvs.py — Remove individual CSV input files now consolidated into xlsx workbooks.

After migration to multi-tab xlsx, each capability's input/data/ folder should contain
only xlsx workbooks. This script removes:
  - Flow CSVs: CurrentFlows.csv, FutureFlows.csv, R3_CurrentFlows.csv, etc.
  - Supplementary CSVs: BusinessDrivers.csv, SuccessCriteria.csv, NFRs.csv,
    SecurityControls.csv, SAPDevStatus.csv, Recommendations.csv, ProcessFlows.csv

Safety: Only removes a CSV if a corresponding xlsx workbook exists in the same folder.

Usage:
    python cleanup_csvs.py --dry-run          # preview (no deletes)
    python cleanup_csvs.py                    # clean all towers
    python cleanup_csvs.py --tower FPR        # single tower
    python cleanup_csvs.py --tower FPR --cap DS-020   # single capability
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"

# CSVs that are safe to remove once xlsx exists
SUPPLEMENTARY_CSVS = [
    "BusinessDrivers.csv",
    "SuccessCriteria.csv",
    "NFRs.csv",
    "SecurityControls.csv",
    "SAPDevStatus.csv",
    "Recommendations.csv",
    "ProcessFlows.csv",
]


def _is_cap_id(name: str) -> bool:
    return bool(re.match(r"^[A-Z]+-\d+$", name, re.IGNORECASE))


def discover_capabilities(tower_dir: Path) -> list[Path]:
    caps = []
    for d in sorted(tower_dir.rglob("*")):
        if d.is_dir() and _is_cap_id(d.name) and (d / "input" / "data").is_dir():
            caps.append(d)
    return caps


def cleanup_capability(cap_dir: Path, dry_run: bool = False) -> dict:
    data_dir = cap_dir / "input" / "data"
    result = {"cap_id": cap_dir.name, "removed": [], "kept": [], "skipped": []}

    # 1. Remove flow CSVs if matching xlsx exists
    for csv_file in sorted(data_dir.glob("*Flows*.csv")):
        xlsx_file = csv_file.with_suffix(".xlsx")
        if xlsx_file.exists():
            if dry_run:
                result["removed"].append(f"WOULD REMOVE {csv_file.name}")
            else:
                csv_file.unlink()
                result["removed"].append(f"REMOVED {csv_file.name}")
        else:
            result["skipped"].append(f"KEPT {csv_file.name} (no xlsx)")

    # 2. Remove supplementary CSVs (now embedded as xlsx tabs)
    for csv_name in SUPPLEMENTARY_CSVS:
        csv_path = data_dir / csv_name
        if csv_path.exists():
            if dry_run:
                result["removed"].append(f"WOULD REMOVE {csv_name}")
            else:
                csv_path.unlink()
                result["removed"].append(f"REMOVED {csv_name}")

    # 3. Report what remains
    for f in sorted(data_dir.iterdir()):
        if f.is_file():
            result["kept"].append(f.name)

    return result


def main():
    parser = argparse.ArgumentParser(description="Remove individual CSVs after xlsx migration")
    parser.add_argument("--tower", help="Single tower shortcode")
    parser.add_argument("--cap", help="Single capability ID")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    if args.tower:
        tower_dirs = [TOWERS_DIR / args.tower]
        if not tower_dirs[0].is_dir():
            for d in TOWERS_DIR.iterdir():
                if d.is_dir() and d.name.upper() == args.tower.upper():
                    tower_dirs = [d]
                    break
            else:
                print(f"ERROR: Tower not found: {args.tower}")
                sys.exit(1)
    else:
        tower_dirs = sorted([d for d in TOWERS_DIR.iterdir() if d.is_dir()])

    total_caps = 0
    total_removed = 0
    total_skipped = 0

    for tower_dir in tower_dirs:
        print(f"\n{'='*60}")
        print(f"TOWER: {tower_dir.name}")
        print(f"{'='*60}")

        caps = discover_capabilities(tower_dir)
        if args.cap:
            caps = [c for c in caps if c.name == args.cap]

        for cap_dir in caps:
            total_caps += 1
            result = cleanup_capability(cap_dir, args.dry_run)

            if result["removed"] or result["skipped"]:
                print(f"\n  {result['cap_id']}:")
                for line in result["removed"]:
                    print(f"    {line}")
                    total_removed += 1
                for line in result["skipped"]:
                    print(f"    {line}")
                    total_skipped += 1
                print(f"    Remaining: {', '.join(result['kept'])}")

    mode = "DRY RUN" if args.dry_run else "COMPLETE"
    print(f"\n{'='*60}")
    print(f"CLEANUP {mode}")
    print(f"  Capabilities: {total_caps}")
    print(f"  Files removed: {total_removed}")
    print(f"  Files skipped: {total_skipped}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
