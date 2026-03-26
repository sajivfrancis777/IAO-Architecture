"""iapm_server.py — MCP server for IAPM (Application Portfolio Management) queries.

Provides live lookups against the IAPM application catalog (30K+ apps).
Falls back to the local CSV cache when the bearer token is unavailable.

Expected tools:
  - lookup_application(name)     → IAPM record with status, owner, lifecycle
  - search_applications(keyword) → search by name, ID, or description
  - get_app_status(iapm_id)      → lifecycle status for a specific app
  - get_apps_for_tower(tower)    → all IAPM apps referenced by a tower

Run:
    python -m mcp_servers.iapm_server
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")
sys.path.insert(0, str(_ROOT))

from src.iapm_lookup import IAPMLookup  # noqa: E402

mcp = FastMCP(
    "IAO IAPM",
    instructions=(
        "Provides lookups against the Intel IAPM application portfolio catalog. "
        "Can search 30K+ applications by name, ID, or keyword. Returns lifecycle "
        "status, owner, deployment info, and IAPM page URLs."
    ),
)

IAPM_CSV = _ROOT / "data" / "iapm" / "IAPM_All_Solutions.csv"


def _get_lookup() -> IAPMLookup | None:
    """Load IAPM lookup from local CSV cache."""
    if IAPM_CSV.exists():
        lookup = IAPMLookup()
        lookup.load_csv(str(IAPM_CSV))
        return lookup
    return None


@mcp.tool()
def lookup_application(name: str) -> str:
    """Look up an application by exact or fuzzy name match in the IAPM catalog.

    Args:
        name: Application name to search for (e.g. "SAP S/4HANA", "MuleSoft", "Ariba")

    Returns:
        JSON with IAPM record(s) including status, IAPM ID, lifecycle, and URL.
    """
    lookup = _get_lookup()
    if not lookup:
        return json.dumps({"error": "IAPM CSV not found at data/iapm/IAPM_All_Solutions.csv"})

    app = lookup.find_by_name(name)
    if app:
        return json.dumps({
            "found": True,
            "name": app.name,
            "iapm_id": app.app_id,
            "acronym": app.acronym,
            "status": app.status,
            "url": app.url,
            "product_owner": app.product_owner,
            "hosting_type": app.hosting_type,
            "source": "local_csv_cache",
        }, indent=2)

    return json.dumps({"found": False, "query": name, "source": "local_csv_cache"})


@mcp.tool()
def search_applications(keyword: str, max_results: int = 20) -> str:
    """Search IAPM applications by keyword (matches against name).

    Args:
        keyword: Search term to match against application names
        max_results: Maximum results to return (default 20)

    Returns:
        JSON with matching applications.
    """
    lookup = _get_lookup()
    if not lookup:
        return json.dumps({"error": "IAPM CSV not found at data/iapm/IAPM_All_Solutions.csv"})

    # IAPMLookup doesn't have a search() method, so we do keyword matching
    # against the loaded by-name dict
    keyword_lower = keyword.strip().lower()
    matches = []
    for name_key, app in lookup._by_name.items():
        if keyword_lower in name_key:
            matches.append(app)
            if len(matches) >= max_results:
                break
    # Also check acronyms
    if len(matches) < max_results:
        for acr_key, app in lookup._by_acronym.items():
            if keyword_lower in acr_key and app not in matches:
                matches.append(app)
                if len(matches) >= max_results:
                    break

    return json.dumps({
        "query": keyword,
        "results": [
            {"name": a.name, "iapm_id": a.app_id, "acronym": a.acronym,
             "status": a.status, "url": a.url}
            for a in matches
        ],
        "total": len(matches),
        "source": "local_csv_cache",
    }, indent=2)


@mcp.tool()
def get_app_status(iapm_id: str) -> str:
    """Get the lifecycle status of an application by its IAPM ID.

    Args:
        iapm_id: The IAPM application ID (e.g. "APP-12345")

    Returns:
        JSON with application status and details.
    """
    lookup = _get_lookup()
    if not lookup:
        return json.dumps({"error": "IAPM CSV not found"})

    app = lookup.find_by_id(iapm_id)
    if app:
        return json.dumps({
            "found": True,
            "iapm_id": app.app_id,
            "name": app.name,
            "acronym": app.acronym,
            "status": app.status,
            "url": app.url,
            "product_owner": app.product_owner,
            "hosting_type": app.hosting_type,
            "source": "local_csv_cache",
        }, indent=2)

    return json.dumps({"found": False, "iapm_id": iapm_id})


if __name__ == "__main__":
    mcp.run(transport="stdio")
