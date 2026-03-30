#!/usr/bin/env python3
"""
build_capability_master.py
──────────────────────────
Parses the Signavio BPMN manifest CSV to extract the authoritative
L1 / L2 / L3 hierarchy and writes:

  1. config/capability_master.yaml  — single source of truth
  2. Updates each tower's tower.yaml  — fills in missing capabilities

The Signavio Path column encodes the hierarchy as:
  /<Tower>/<L1 group>/<CapID Name>/<StepID StepName>/...          (FPR, PTP, MDM)
  /<Tower>/<Variant (IF|IP)>/<L1 group>/<CapID Name>/<StepID>/... (FTS, OTC)

Usage:
    python build_capability_master.py                 # dry-run (preview)
    python build_capability_master.py --apply         # write changes
    python build_capability_master.py --apply --force # overwrite existing names
"""
import argparse, csv, html, json, os, re, sys
from pathlib import Path

import yaml

# ── Constants ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "data" / "bic or signavio" / "signavio-bpmn-manifest.csv"
MASTER_OUT = ROOT / "config" / "capability_master.yaml"
TOWERS_DIR = ROOT / "towers"
REGISTRY_PATH = ROOT / "config" / "tower_registry.json"


def _load_signavio_map() -> dict[str, str]:
    """Build Signavio folder name → shortcode map from tower_registry.json.

    Falls back to auto-discovery from manifest paths if the registry
    doesn't cover a folder name (logs a warning for manual follow-up).
    """
    smap: dict[str, str] = {}
    if REGISTRY_PATH.exists():
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            reg = json.load(f)
        for sc, info in reg.get("towers", {}).items():
            for sname in info.get("signavio_names", []):
                smap[sname] = sc
    return smap


# Load once at module level; can be augmented at runtime if manifest has new towers
SIGNAVIO_MAP: dict[str, str] = _load_signavio_map()

# Regex: capability line like "DC-010 Perform Transaction Processing"
CAP_RE = re.compile(r"^([A-Za-z]{1,4}-\d{2,4})\s+(.+)$")
# Regex: step line like "DC-010-010 Translate/Map External Transaction Data"
STEP_RE = re.compile(r"^([A-Za-z]{1,4}-\d{2,4}-\d{2,4})\s+(.+)$")


def parse_manifest(manifest_path: Path) -> dict:
    """Return {shortcode: {cap_id: {name, l1, steps: [(step_id, step_name)]}}}"""
    result = {}
    unmapped_warnings: set[str] = set()
    with open(manifest_path, encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            pass  # skip to count total
    with open(manifest_path, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            path = row[0]
            if path.startswith("/Archive"):
                continue
            parts = [p for p in path.split("/") if p]
            if len(parts) < 3:
                continue

            # Determine tower variant and offset
            tower_raw = parts[0]
            if len(parts) >= 4 and re.search(r"\((IF|IP)\)", parts[1]):
                variant = parts[1]
                l1 = parts[2]
                l2_idx = 3
                l3_idx = 4
            else:
                variant = tower_raw
                l1 = parts[1]
                l2_idx = 2
                l3_idx = 3

            # Resolve via centralized registry map
            shortcode = SIGNAVIO_MAP.get(variant) or SIGNAVIO_MAP.get(tower_raw)
            if not shortcode:
                if variant not in unmapped_warnings:
                    unmapped_warnings.add(variant)
                    print(f"  [WARN] Unmapped Signavio folder: '{variant}' — add to config/tower_registry.json signavio_names")
                continue

            # Parse L2 (capability)
            if l2_idx >= len(parts):
                continue
            l2_raw = parts[l2_idx]
            m = CAP_RE.match(l2_raw)
            if not m:
                continue
            cap_id = m.group(1).upper()
            cap_name = html.unescape(m.group(2).strip())

            if shortcode not in result:
                result[shortcode] = {}
            if cap_id not in result[shortcode]:
                result[shortcode][cap_id] = {
                    "name": cap_name,
                    "l1": l1,
                    "steps": [],
                }

            # Parse L3 (step) if present
            if l3_idx < len(parts):
                l3_raw = parts[l3_idx]
                ms = STEP_RE.match(l3_raw)
                if ms:
                    step_id = ms.group(1).upper()
                    step_name = html.unescape(ms.group(2).strip())
                    existing_steps = result[shortcode][cap_id]["steps"]
                    if (step_id, step_name) not in existing_steps:
                        existing_steps.append((step_id, step_name))

    # Sort steps
    for sc in result:
        for cid in result[sc]:
            result[sc][cid]["steps"].sort()

    return result


def write_master(master: dict, out_path: Path, dry_run: bool):
    """Write config/capability_master.yaml"""
    doc = {
        "_meta": {
            "source": "signavio-bpmn-manifest.csv",
            "description": "Authoritative L1/L2/L3 capability hierarchy extracted from Signavio/BIC BPMN export manifest.",
            "generated_by": "build_capability_master.py",
        },
        "towers": {},
    }
    for sc in sorted(master):
        caps = []
        for cid in sorted(master[sc]):
            entry = master[sc][cid]
            cap_entry = {
                "id": cid,
                "name": entry["name"],
                "l1": entry["l1"],
            }
            if entry["steps"]:
                cap_entry["steps"] = [
                    {"id": sid, "name": sname}
                    for sid, sname in entry["steps"]
                ]
            caps.append(cap_entry)
        doc["towers"][sc] = {"capabilities": caps}

    if dry_run:
        print(f"\n[DRY-RUN] Would write {out_path}")
        print(f"  Towers: {list(doc['towers'].keys())}")
        for sc in sorted(doc["towers"]):
            print(f"  {sc}: {len(doc['towers'][sc]['capabilities'])} capabilities")
    else:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("# Capability Master — generated from Signavio BPMN manifest\n")
            f.write("# Source: data/bic or signavio/signavio-bpmn-manifest.csv\n")
            f.write("# Re-generate: python build_capability_master.py --apply\n\n")
            yaml.dump(doc, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print(f"[WRITTEN] {out_path}")
        for sc in sorted(doc["towers"]):
            print(f"  {sc}: {len(doc['towers'][sc]['capabilities'])} capabilities")


def update_tower_yaml(shortcode: str, manifest_caps: dict, force: bool, dry_run: bool):
    """Update a tower's tower.yaml with capabilities from the manifest."""
    tower_yaml = TOWERS_DIR / shortcode / "tower.yaml"
    if not tower_yaml.exists():
        print(f"  [SKIP] {tower_yaml} not found")
        return 0

    with open(tower_yaml, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        cfg = yaml.safe_load(content)
    except yaml.YAMLError as e:
        print(f"  [ERROR] Cannot parse {tower_yaml}: {e}")
        return 0

    if cfg is None:
        cfg = {}

    existing_caps = cfg.get("capabilities", [])
    if existing_caps is None:
        existing_caps = []

    existing_ids = {c.get("id"): c for c in existing_caps}
    added = 0
    updated = 0

    for cap_id, info in sorted(manifest_caps.items()):
        if cap_id in existing_ids:
            # Cap exists — update name if force or if name == cap_id (placeholder)
            existing = existing_ids[cap_id]
            old_name = existing.get("name", cap_id)
            if force or old_name == cap_id or old_name == "":
                if old_name != info["name"]:
                    if dry_run:
                        print(f"    [UPDATE] {cap_id}: '{old_name}' → '{info['name']}'")
                    existing["name"] = info["name"]
                    updated += 1
            # Update L1 if missing
            if not existing.get("l1") or force:
                existing["l1"] = info["l1"]
        else:
            # New capability — add it
            new_entry = {
                "id": cap_id,
                "name": info["name"],
                "l1": info["l1"],
                "status": "active" if shortcode in ("FPR", "E2E") else "planned",
            }
            existing_caps.append(new_entry)
            if dry_run:
                print(f"    [ADD]    {cap_id}: '{info['name']}' (l1: {info['l1']})")
            added += 1

    if added > 0 or updated > 0:
        # Sort capabilities by id for consistency
        existing_caps.sort(key=lambda c: c.get("id", ""))
        cfg["capabilities"] = existing_caps

        if not dry_run:
            # Write back preserving the header comment
            header_lines = []
            for line in content.split("\n"):
                if line.startswith("#") or line.strip() == "":
                    header_lines.append(line)
                else:
                    break

            with open(tower_yaml, "w", encoding="utf-8") as f:
                if header_lines:
                    f.write("\n".join(header_lines) + "\n")
                yaml.dump(cfg, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    return added, updated


def main():
    parser = argparse.ArgumentParser(description="Build capability master from Signavio manifest")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing capability names")
    args = parser.parse_args()
    dry_run = not args.apply

    if not MANIFEST.exists():
        print(f"ERROR: Manifest not found: {MANIFEST}")
        sys.exit(1)

    print(f"{'DRY-RUN' if dry_run else 'APPLYING'} — Source: {MANIFEST.name}")
    print("=" * 70)

    # 1. Parse manifest
    master = parse_manifest(MANIFEST)
    total_caps = sum(len(caps) for caps in master.values())
    print(f"\nParsed {total_caps} capabilities across {len(master)} towers")

    # 2. Write capability_master.yaml
    print(f"\n{'─' * 70}")
    print("STEP 1: Write config/capability_master.yaml")
    write_master(master, MASTER_OUT, dry_run)

    # 3. Update each tower.yaml
    print(f"\n{'─' * 70}")
    print("STEP 2: Update tower.yaml files")
    grand_added = 0
    grand_updated = 0
    for sc in sorted(master):
        print(f"\n  Tower: {sc}")
        result = update_tower_yaml(sc, master[sc], args.force, dry_run)
        if isinstance(result, tuple):
            a, u = result
            grand_added += a
            grand_updated += u
            if a == 0 and u == 0:
                print(f"    (no changes needed)")
            elif not dry_run:
                print(f"    Added: {a}, Updated: {u}")
        else:
            print(f"    (skipped)")

    # 4. Summary
    print(f"\n{'=' * 70}")
    print(f"SUMMARY: {grand_added} added, {grand_updated} updated")
    if dry_run:
        print("Run with --apply to write changes.")
    else:
        print("Done. Verify with: python build_capability_master.py")


if __name__ == "__main__":
    main()
