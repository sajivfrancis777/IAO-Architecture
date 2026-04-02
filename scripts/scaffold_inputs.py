"""scaffold_inputs.py — Deploy input templates + upgrade flow CSVs across all capabilities.

Performs three operations for every capability with an input/data/ folder:

1. UPGRADE FLOW CSVs: Extends existing 25-column CurrentFlows/FutureFlows CSVs to the
   full 47-column extended schema by appending the 22 missing column headers.
   Existing data rows are preserved with blank values padded for new columns.

2. DEPLOY SUPPLEMENTARY CSVs: Copies template CSVs from templates/ into each
   capability's input/data/ folder IF they don't already exist:
     - BusinessDrivers.csv, SuccessCriteria.csv, NFRs.csv
     - SecurityControls.csv, SAPDevStatus.csv, Recommendations.csv

3. DEPLOY PROCESSFLOWS CSV: Copies ProcessFlows_TEMPLATE.csv as ProcessFlows.csv
   into each capability's input/data/ folder IF it doesn't already exist.
   This provides the manual BPMN-alternative for business process flow entry.

Usage:
    python scaffold_inputs.py                    # all towers, all capabilities
    python scaffold_inputs.py --tower FPR        # single tower
    python scaffold_inputs.py --tower FPR --cap DS-020   # single capability
    python scaffold_inputs.py --dry-run          # preview only, no writes
    python scaffold_inputs.py --upgrade-only     # only upgrade flow CSVs
    python scaffold_inputs.py --deploy-only      # only deploy supplementary CSVs
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WORKSPACE = Path(__file__).resolve().parent.parent
TOWERS_DIR = WORKSPACE / "towers"
TEMPLATES_DIR = WORKSPACE / "templates"

# ---------------------------------------------------------------------------
# Schema: the 47-column extended header
# ---------------------------------------------------------------------------
FULL_HEADER = [
    # Base 25 columns (cols 1-25)
    "Flow Chain", "Hop #", "Source System", "Source Lane",
    "Target System", "Target Lane", "Interface / Technology", "Direction",
    "Frequency", "Data Description", "Flow Purpose", "Notes / Corrections",
    "Process/System Owner", "Data Owner", "Applicable Scope",
    "Src Web Address", "Src Business Owner", "Src Product Owner",
    "Src Product Owner Email", "Src IAPM URL",
    "Tgt Web Address", "Tgt Business Owner", "Tgt Product Owner",
    "Tgt Product Owner Email", "Tgt IAPM URL",
    # Extended: Data Architecture (cols 26-31)
    "Data Entity", "Data Format", "Data Classification",
    "Data Volume", "Master/Transaction", "Data Lineage Notes",
    # Extended: Technology Architecture (cols 32-37)
    "Integration Pattern", "Middleware / Platform", "Protocol",
    "Auth Method", "Environment Scope", "SLA / Latency",
    # Extended: Interface Architecture (cols 38-41)
    "Interface ID", "Interface Type", "Error Handling", "Monitoring",
    # Extended: Endpoint-level (cols 42-47)
    "Source DB Platform", "Target DB Platform",
    "Source Schema/Object", "Target Schema/Object",
    "Source Tech Platform", "Target Tech Platform",
]

BASE_COL_COUNT = 25
EXTENDED_COL_COUNT = len(FULL_HEADER)  # 47

# Supplementary template files → target filenames
SUPPLEMENTARY_TEMPLATES = {
    "BusinessDrivers_TEMPLATE.csv": "BusinessDrivers.csv",
    "SuccessCriteria_TEMPLATE.csv": "SuccessCriteria.csv",
    "NFRs_TEMPLATE.csv": "NFRs.csv",
    "SecurityControls_TEMPLATE.csv": "SecurityControls.csv",
    "SAPDevStatus_TEMPLATE.csv": "SAPDevStatus.csv",
    "Recommendations_TEMPLATE.csv": "Recommendations.csv",
    "ProcessFlows_TEMPLATE.csv": "ProcessFlows.csv",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _is_cap_id(name: str) -> bool:
    """Check if a directory name looks like a capability ID (e.g. DS-020, E2E-80)."""
    return bool(re.match(r"^[A-Z]+-\d+$", name, re.IGNORECASE))


def discover_capabilities(tower_dir: Path) -> list[Path]:
    """Find all capability dirs (with input/data/) under a tower."""
    caps = []
    for d in sorted(tower_dir.rglob("*")):
        if d.is_dir() and _is_cap_id(d.name) and (d / "input" / "data").is_dir():
            caps.append(d)
    return caps


def count_csv_columns(csv_path: Path) -> int:
    """Read the header row and return column count."""
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, [])
    return len(header)


# ---------------------------------------------------------------------------
# Operation 1: Upgrade flow CSVs from 25-col to 47-col
# ---------------------------------------------------------------------------
def upgrade_flow_csv(csv_path: Path, dry_run: bool = False) -> str:
    """Upgrade a flow CSV from 25 columns to 47 columns.

    Returns a status string: 'upgraded', 'already-47', 'skipped-unknown', or 'error'.
    """
    col_count = count_csv_columns(csv_path)

    if col_count >= EXTENDED_COL_COUNT:
        return "already-47"

    if col_count < BASE_COL_COUNT:
        return f"skipped-{col_count}-cols"

    if dry_run:
        return f"would-upgrade-{col_count}-to-{EXTENDED_COL_COUNT}"

    # Read all rows
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return "skipped-empty"

    # Replace header with full 47-column header
    rows[0] = FULL_HEADER

    # Pad data rows to 47 columns
    for i in range(1, len(rows)):
        current_len = len(rows[i])
        if current_len < EXTENDED_COL_COUNT:
            rows[i].extend([""] * (EXTENDED_COL_COUNT - current_len))

    # Write back
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    return f"upgraded-{col_count}-to-{EXTENDED_COL_COUNT}"


# ---------------------------------------------------------------------------
# Operation 2: Deploy supplementary template CSVs
# ---------------------------------------------------------------------------
def deploy_templates(data_dir: Path, dry_run: bool = False) -> list[str]:
    """Copy template CSVs into a capability's input/data/ folder.

    Only copies files that don't already exist. Returns list of actions taken.
    """
    actions = []
    for template_name, target_name in SUPPLEMENTARY_TEMPLATES.items():
        template_path = TEMPLATES_DIR / template_name
        target_path = data_dir / target_name

        if target_path.exists():
            actions.append(f"  EXISTS  {target_name}")
            continue

        if not template_path.exists():
            actions.append(f"  MISSING template: {template_name}")
            continue

        if dry_run:
            actions.append(f"  WOULD DEPLOY  {target_name}")
        else:
            shutil.copy2(template_path, target_path)
            actions.append(f"  DEPLOYED  {target_name}")

    return actions


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------
def scaffold_capability(cap_dir: Path, dry_run: bool = False,
                        upgrade_only: bool = False,
                        deploy_only: bool = False) -> dict:
    """Run all scaffold operations on a single capability."""
    data_dir = cap_dir / "input" / "data"
    result = {
        "cap_id": cap_dir.name,
        "path": str(cap_dir),
        "flow_upgrades": [],
        "template_deploys": [],
    }

    # Operation 1: Upgrade flow CSVs
    if not deploy_only:
        flow_patterns = ["CurrentFlows.csv", "FutureFlows.csv",
                         "R3_CurrentFlows.csv", "R3_FutureFlows.csv",
                         "R4_CurrentFlows.csv", "R4_FutureFlows.csv",
                         "R5_CurrentFlows.csv", "R5_FutureFlows.csv"]
        for pattern in flow_patterns:
            csv_path = data_dir / pattern
            if csv_path.exists():
                status = upgrade_flow_csv(csv_path, dry_run)
                result["flow_upgrades"].append(f"  {pattern}: {status}")

    # Operation 2: Deploy supplementary templates
    if not upgrade_only:
        result["template_deploys"] = deploy_templates(data_dir, dry_run)

    return result


def main():
    parser = argparse.ArgumentParser(description="Scaffold input templates across tower capabilities")
    parser.add_argument("--tower", help="Single tower shortcode (e.g. FPR)")
    parser.add_argument("--cap", help="Single capability ID (e.g. DS-020)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no file writes")
    parser.add_argument("--upgrade-only", action="store_true", help="Only upgrade flow CSVs to 47 cols")
    parser.add_argument("--deploy-only", action="store_true", help="Only deploy supplementary CSVs")
    args = parser.parse_args()

    # Determine tower directories to process
    if args.tower:
        tower_dirs = [TOWERS_DIR / args.tower]
        if not tower_dirs[0].is_dir():
            # Case-insensitive fallback
            for d in TOWERS_DIR.iterdir():
                if d.is_dir() and d.name.upper() == args.tower.upper():
                    tower_dirs = [d]
                    break
            else:
                print(f"ERROR: Tower directory not found: {args.tower}")
                sys.exit(1)
    else:
        tower_dirs = sorted([d for d in TOWERS_DIR.iterdir() if d.is_dir()])

    # Process
    total_caps = 0
    total_upgrades = 0
    total_deploys = 0

    for tower_dir in tower_dirs:
        print(f"\n{'='*70}")
        print(f"TOWER: {tower_dir.name}")
        print(f"{'='*70}")

        caps = discover_capabilities(tower_dir)
        if args.cap:
            caps = [c for c in caps if c.name == args.cap]

        if not caps:
            print("  No capabilities found.")
            continue

        for cap_dir in caps:
            total_caps += 1
            print(f"\n  {cap_dir.name}:")
            result = scaffold_capability(
                cap_dir, dry_run=args.dry_run,
                upgrade_only=args.upgrade_only,
                deploy_only=args.deploy_only,
            )

            if result["flow_upgrades"]:
                print("    Flow CSV upgrades:")
                for line in result["flow_upgrades"]:
                    print(f"    {line}")
                    if "upgraded" in line and "would" not in line.lower():
                        total_upgrades += 1

            if result["template_deploys"]:
                print("    Supplementary templates:")
                for line in result["template_deploys"]:
                    print(f"    {line}")
                    if "DEPLOYED" in line:
                        total_deploys += 1

    # Summary
    mode = "DRY RUN" if args.dry_run else "COMPLETE"
    print(f"\n{'='*70}")
    print(f"SCAFFOLD {mode}")
    print(f"  Capabilities processed: {total_caps}")
    print(f"  Flow CSVs upgraded:     {total_upgrades}")
    print(f"  Templates deployed:     {total_deploys}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
