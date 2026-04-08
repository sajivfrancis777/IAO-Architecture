"""enrich_flows.py — Expand simplified 14-column flow input to full 47-column CSV.

Usage:
    python -m scripts.enrich_flows <input_xlsx_or_csv> [--output <path>] [--iapm <csv>]

Reads the architect-friendly simplified input (14 columns) and:
  1. Looks up each Source/Target System in IAPM to auto-fill:
     - IAPM URL, Product Owner, Product Owner Email, Business Owner,
       Tech Platform (from hosting type), Application Status
  2. Infers from the Interface / Technology column:
     - Integration Pattern, Middleware / Platform, Protocol, Auth Method
  3. Sets sensible defaults for remaining columns:
     - Direction → "→", Data Classification → "Intel Confidential",
       Environment Scope → "DEV,QAS,PRD"
  4. Writes the full 47-column CSV compatible with csv_parser.py / xlsx_loader.py

If a column is already filled by the architect, the enrichment will NOT overwrite it.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# Add project root to path so we can import src modules
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

from src.iapm_lookup import IAPMLookup, IAPMApp  # noqa: E402

# ---------------------------------------------------------------------------
# Full 47 columns in the order csv_parser.py expects
# ---------------------------------------------------------------------------
FULL_COLUMNS = [
    "Flow Chain", "Hop #", "Source System", "Source Lane",
    "Target System", "Target Lane", "Interface / Technology",
    "Direction", "Frequency", "Data Description", "Flow Purpose",
    "Notes / Corrections", "Process/System Owner", "Data Owner",
    "Applicable Scope", "Src Web Address", "Src Business Owner",
    "Src Product Owner", "Src Product Owner Email", "Src IAPM URL",
    "Tgt Web Address", "Tgt Business Owner", "Tgt Product Owner",
    "Tgt Product Owner Email", "Tgt IAPM URL",
    # Extended columns (26-47)
    "Data Entity", "Data Format", "Data Classification", "Data Volume",
    "Master/Transaction", "Data Lineage Notes", "Integration Pattern",
    "Middleware / Platform", "Protocol", "Auth Method",
    "Environment Scope", "SLA / Latency", "Interface ID",
    "Interface Type", "Error Handling", "Monitoring",
    "Source DB Platform", "Target DB Platform",
    "Source Schema/Object", "Target Schema/Object",
    "Source Tech Platform", "Target Tech Platform",
]

# ---------------------------------------------------------------------------
# Inference rules
# ---------------------------------------------------------------------------
_INTERFACE_TO_PATTERN: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\b(IDoc|ALE)\b", re.I),          "Hub-Spoke"),
    (re.compile(r"\bRFC\b", re.I),                  "Point-to-Point"),
    (re.compile(r"\bBAPI\b", re.I),                 "Point-to-Point"),
    (re.compile(r"\b(REST|OData)\b", re.I),         "API Gateway"),
    (re.compile(r"\bSOAP\b", re.I),                 "API Gateway"),
    (re.compile(r"\b(Kafka|Event)\b", re.I),        "Publish-Subscribe"),
    (re.compile(r"\b(SFTP|FTP|File)\b", re.I),      "Batch File"),
    (re.compile(r"\bDB\s*Link\b", re.I),            "Database Link"),
    (re.compile(r"\b(CPI|PI|PO|MuleSoft)\b", re.I), "Hub-Spoke"),
]

_INTERFACE_TO_MIDDLEWARE: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\bIDoc\b", re.I),                  "SAP PI/PO"),
    (re.compile(r"\bALE\b", re.I),                   "SAP PI/PO"),
    (re.compile(r"\bCPI\b", re.I),                   "SAP CPI"),
    (re.compile(r"\b(PI|PO)\b", re.I),               "SAP PI/PO"),
    (re.compile(r"\bMuleSoft\b", re.I),              "MuleSoft"),
    (re.compile(r"\bKafka\b", re.I),                 "Kafka"),
    (re.compile(r"\b(REST|OData|SOAP|API)\b", re.I), ""),  # direct — no middleware
]

_INTERFACE_TO_PROTOCOL: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\bIDoc\b", re.I),      "RFC"),
    (re.compile(r"\bRFC\b", re.I),       "RFC"),
    (re.compile(r"\bBAPI\b", re.I),      "RFC"),
    (re.compile(r"\bREST\b", re.I),      "HTTPS"),
    (re.compile(r"\bOData\b", re.I),     "HTTPS"),
    (re.compile(r"\bSOAP\b", re.I),      "HTTP/SOAP"),
    (re.compile(r"\bSFTP\b", re.I),      "SFTP"),
    (re.compile(r"\bFTP\b", re.I),       "FTP"),
    (re.compile(r"\bKafka\b", re.I),     "TCP/Kafka"),
    (re.compile(r"\bJDBC\b", re.I),      "JDBC"),
]

_INTERFACE_TO_AUTH: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\b(RFC|BAPI|IDoc)\b", re.I),      "SAP Logon"),
    (re.compile(r"\b(REST|OData)\b", re.I),          "OAuth / API Key"),
    (re.compile(r"\bSOAP\b", re.I),                  "WS-Security"),
    (re.compile(r"\bSFTP\b", re.I),                  "SSH Key"),
    (re.compile(r"\bKafka\b", re.I),                 "mTLS / SASL"),
]

# SAP-known systems for tech platform inference
_SAP_SYSTEMS = re.compile(
    r"\b(S/4\s*HANA|SAP|ECC|BW|BPC|GRC|MDG|Ariba|Concur|SuccessFactors|Fiori)\b", re.I
)


def _first_match(interface: str, rules: list[tuple[re.Pattern, str]]) -> str:
    for pattern, value in rules:
        if pattern.search(interface):
            return value
    return ""


def _infer_tech_platform(system_name: str, iapm_app: IAPMApp | None) -> str:
    """Infer tech platform from IAPM hosting type or system name heuristics."""
    if iapm_app and iapm_app.hosting_type:
        ht = iapm_app.hosting_type.lower()
        if "cloud" in ht:
            return f"Cloud ({iapm_app.hosting_type})"
        if "on-prem" in ht or "on prem" in ht:
            return f"On-Premise ({iapm_app.hosting_type})"
        return iapm_app.hosting_type
    # Heuristic fallback
    if _SAP_SYSTEMS.search(system_name):
        return "SAP HANA (On-Premise)"
    return ""


def _safe(val: str) -> str:
    return (val or "").strip()


# ---------------------------------------------------------------------------
# Main enrichment
# ---------------------------------------------------------------------------
def enrich(rows: list[dict[str, str]], iapm: IAPMLookup) -> list[dict[str, str]]:
    """Enrich simplified rows into full 47-column rows."""
    enriched = []
    for row in rows:
        out: dict[str, str] = {col: "" for col in FULL_COLUMNS}

        # Copy all architect-provided values first (never overwrite)
        for k, v in row.items():
            k_stripped = k.strip()
            if k_stripped in out:
                out[k_stripped] = _safe(v)

        interface = out["Interface / Technology"]

        # --- IAPM enrichment for Source ---
        src_name = out["Source System"]
        src_app = iapm.resolve(src_name, out.get("Src IAPM URL", ""))
        if src_app:
            if not out["Src IAPM URL"]:
                out["Src IAPM URL"] = src_app.url
            if not out["Src Product Owner"]:
                out["Src Product Owner"] = src_app.product_owner
            if not out["Src Product Owner Email"]:
                out["Src Product Owner Email"] = src_app.product_owner_email
            if not out["Src Business Owner"]:
                out["Src Business Owner"] = src_app.business_owner

        # --- IAPM enrichment for Target ---
        tgt_name = out["Target System"]
        tgt_app = iapm.resolve(tgt_name, out.get("Tgt IAPM URL", ""))
        if tgt_app:
            if not out["Tgt IAPM URL"]:
                out["Tgt IAPM URL"] = tgt_app.url
            if not out["Tgt Product Owner"]:
                out["Tgt Product Owner"] = tgt_app.product_owner
            if not out["Tgt Product Owner Email"]:
                out["Tgt Product Owner Email"] = tgt_app.product_owner_email
            if not out["Tgt Business Owner"]:
                out["Tgt Business Owner"] = tgt_app.business_owner

        # --- Tech platform inference ---
        if not out["Source Tech Platform"]:
            out["Source Tech Platform"] = _infer_tech_platform(src_name, src_app)
        if not out["Target Tech Platform"]:
            out["Target Tech Platform"] = _infer_tech_platform(tgt_name, tgt_app)

        # --- Interface-based inference ---
        if not out["Integration Pattern"]:
            out["Integration Pattern"] = _first_match(interface, _INTERFACE_TO_PATTERN)
        if not out["Middleware / Platform"]:
            out["Middleware / Platform"] = _first_match(interface, _INTERFACE_TO_MIDDLEWARE)
        if not out["Protocol"]:
            out["Protocol"] = _first_match(interface, _INTERFACE_TO_PROTOCOL)
        if not out["Auth Method"]:
            out["Auth Method"] = _first_match(interface, _INTERFACE_TO_AUTH)

        # --- Defaults ---
        if not out["Direction"]:
            out["Direction"] = "→"
        if not out["Data Classification"]:
            out["Data Classification"] = "Intel Confidential"
        if not out["Environment Scope"]:
            out["Environment Scope"] = "DEV,QAS,PRD"

        enriched.append(out)
    return enriched


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------
def _read_input(path: Path) -> list[dict[str, str]]:
    """Read simplified input from .xlsx or .csv."""
    if path.suffix.lower() in (".xlsx", ".xls"):
        try:
            import openpyxl
        except ImportError:
            print("ERROR: openpyxl required for .xlsx input. pip install openpyxl", file=sys.stderr)
            sys.exit(1)
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb.active
        rows_iter = ws.iter_rows(values_only=True)
        headers = [str(h or "").strip() for h in next(rows_iter)]
        data = []
        for row in rows_iter:
            d = {}
            for i, val in enumerate(row):
                if i < len(headers) and headers[i]:
                    d[headers[i]] = str(val) if val is not None else ""
            if any(d.values()):
                data.append(d)
        wb.close()
        return data
    else:
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            return [row for row in reader if any(row.values())]


def _write_output(rows: list[dict[str, str]], path: Path) -> None:
    """Write full 47-column CSV."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FULL_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  ✓ Wrote {len(rows)} enriched rows → {path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enrich simplified flow input to full 47-column CSV"
    )
    parser.add_argument("input", type=Path, help="Simplified input (.xlsx or .csv)")
    parser.add_argument("--output", "-o", type=Path, default=None,
                        help="Output CSV path (default: <input>_enriched.csv)")
    parser.add_argument("--iapm", type=Path,
                        default=_ROOT / "data" / "iapm" / "IAPM_All_Solutions.csv",
                        help="Path to IAPM_All_Solutions.csv")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    # Load IAPM
    iapm = IAPMLookup()
    if args.iapm.exists():
        iapm.load_csv(str(args.iapm))
        print(f"  ✓ Loaded {iapm.app_count:,} IAPM applications")
    else:
        print(f"  ⚠ IAPM CSV not found at {args.iapm} — skipping IAPM enrichment")

    # Read input
    rows = _read_input(args.input)
    print(f"  ✓ Read {len(rows)} rows from {args.input.name}")

    # Enrich
    enriched = enrich(rows, iapm)

    # Write output
    out_path = args.output or args.input.with_name(args.input.stem + "_enriched.csv")
    _write_output(enriched, out_path)

    # Summary
    src_systems = {r["Source System"] for r in enriched if r["Source System"]}
    tgt_systems = {r["Target System"] for r in enriched if r["Target System"]}
    all_systems = src_systems | tgt_systems
    matched = sum(1 for s in all_systems if iapm.find_by_name(s))
    print(f"\n  Systems: {len(all_systems)} unique, {matched} matched in IAPM, "
          f"{len(all_systems) - matched} unmatched")
    if len(all_systems) - matched > 0:
        unmatched = sorted(s for s in all_systems if not iapm.find_by_name(s))
        print(f"  Unmatched: {', '.join(unmatched)}")


if __name__ == "__main__":
    main()
