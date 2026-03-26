"""sap_odata_server.py — MCP server for SAP S/4HANA OData queries.

Placeholder — ready to implement when SAP OData API access
(BI0/DI0 gateways) is provisioned with S_SERVICE authorization.

Expected tools:
  - get_dev_objects(system, package)  → custom code object counts
  - get_transport_status(system)      → transport request status
  - get_cds_views(package)            → CDS view definitions
  - get_fiori_apps(package)           → registered Fiori apps

Run:
    python -m mcp_servers.sap_odata_server
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")

mcp = FastMCP(
    "IAO SAP OData",
    instructions=(
        "Provides access to SAP S/4HANA development objects via OData/ADT APIs. "
        "Queries custom code, transports, CDS views, and Fiori apps from the "
        "BI0 (Intel Foundry) and DI0 (Intel Products) systems. "
        "NOT YET IMPLEMENTED — requires SAP gateway access provisioning."
    ),
)

SAP_BI0_HOST = os.environ.get("SAP_BI0_HOST", "")
SAP_DI0_HOST = os.environ.get("SAP_DI0_HOST", "")


def _not_configured() -> str:
    return json.dumps({
        "error": "SAP OData integration not yet configured.",
        "action_required": [
            "Provision SAP_BI0_USER / SAP_BI0_PASS in .env",
            "Request S_SERVICE role for OData catalog access",
            "Verify gateway connectivity to sapbi0ci.intel.com:8220",
        ],
    })


@mcp.tool()
def get_dev_objects(
    system: str = "BI0",
    package: str = "",
) -> str:
    """Get custom development object counts from an SAP system.

    Args:
        system: SAP system ID (BI0 or DI0)
        package: Optional ABAP package filter (e.g. "ZIDM_FPR")

    Returns:
        JSON with object type counts (programs, classes, function modules, etc.)
    """
    if not SAP_BI0_HOST:
        return _not_configured()

    # TODO: Implement SAP ADT REST API call
    # GET /sap/bc/adt/repository/informationsystem/objecttypes
    return json.dumps({"status": "not_implemented", "system": system, "package": package})


@mcp.tool()
def get_transport_status(
    system: str = "BI0",
    owner: str = "",
) -> str:
    """Get transport request status from an SAP system.

    Args:
        system: SAP system ID (BI0 or DI0)
        owner: Optional transport owner filter

    Returns:
        JSON with transport requests and their release status.
    """
    if not SAP_BI0_HOST:
        return _not_configured()

    # TODO: Implement SAP OData call
    # GET /sap/opu/odata/sap/ZIDM_TRANSPORT_SRV/TransportSet
    return json.dumps({"status": "not_implemented", "system": system})


@mcp.tool()
def get_cds_views(package: str = "") -> str:
    """Get CDS view definitions from SAP S/4HANA.

    Args:
        package: Optional ABAP package filter

    Returns:
        JSON with CDS view names and their descriptions.
    """
    if not SAP_BI0_HOST:
        return _not_configured()

    # TODO: Implement SAP ADT call
    return json.dumps({"status": "not_implemented", "package": package})


@mcp.tool()
def get_fiori_apps(tower: str = "") -> str:
    """Get registered Fiori applications.

    Args:
        tower: Optional tower filter to scope results

    Returns:
        JSON with Fiori app IDs, titles, and BSP components.
    """
    if not SAP_BI0_HOST:
        return _not_configured()

    # TODO: Implement Fiori Launchpad API call
    return json.dumps({"status": "not_implemented", "tower": tower})


if __name__ == "__main__":
    mcp.run(transport="stdio")
