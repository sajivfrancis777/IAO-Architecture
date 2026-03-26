"""bic_server.py — MCP server for SAP BIC (Signavio) process design queries.

Placeholder — ready to implement when BIC API access is stable.
BIC is the GBTEC-based process design platform hosting BPMN 2.0 models.

Expected tools:
  - get_process_models(cap_id)     → list BPMN models for a capability
  - get_process_detail(model_id)   → full process detail (steps, lanes, gateways)
  - search_processes(keyword)      → search by name or description
  - export_bpmn(model_id)         → export BPMN XML for a model

Known API endpoints:
  - /process-design/frontend/api   (token auth — UI session)
  - /process-design/v3/api-docs    (basic auth — OpenAPI spec)
  - SIREN hypermedia API via Spring Boot backend

Run:
    python -m mcp_servers.bic_server
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
    "IAO SAP BIC",
    instructions=(
        "Provides access to SAP BIC (Signavio) process design platform. "
        "Queries BPMN 2.0 process models, swim lanes, tasks, and gateways. "
        "NOT YET IMPLEMENTED — requires BIC API token provisioning."
    ),
)

BIC_AUTH_TOKEN = os.environ.get("BIC_AUTH_TOKEN", "")


def _not_configured() -> str:
    return json.dumps({
        "error": "BIC integration not yet configured.",
        "action_required": [
            "Set BIC_AUTH_TOKEN in .env (from browser F12 > Network > Authorization header)",
            "BIC uses Spring Boot SIREN API — token expires frequently",
            "Consider OAuth2 flow for stable access",
        ],
    })


@mcp.tool()
def get_process_models(
    tower: str = "",
    capability_name: str = "",
) -> str:
    """List BPMN process models for a tower or capability from BIC.

    Args:
        tower: Optional tower shortcode filter
        capability_name: Optional capability name filter

    Returns:
        JSON with process model names, IDs, and metadata.
    """
    if not BIC_AUTH_TOKEN:
        return _not_configured()

    # TODO: Implement BIC SIREN API call
    return json.dumps({"status": "not_implemented", "tower": tower})


@mcp.tool()
def get_process_detail(model_id: str) -> str:
    """Get full detail for a BPMN process model — steps, lanes, gateways.

    Args:
        model_id: BIC process model ID

    Returns:
        JSON with process structure (lanes, tasks, gateways, flows).
    """
    if not BIC_AUTH_TOKEN:
        return _not_configured()

    # TODO: Implement BIC SIREN API call
    return json.dumps({"status": "not_implemented", "model_id": model_id})


@mcp.tool()
def search_processes(keyword: str, max_results: int = 20) -> str:
    """Search BIC process models by keyword.

    Args:
        keyword: Search term
        max_results: Maximum results to return

    Returns:
        JSON with matching process models.
    """
    if not BIC_AUTH_TOKEN:
        return _not_configured()

    # TODO: Implement BIC search API
    return json.dumps({"status": "not_implemented", "keyword": keyword})


@mcp.tool()
def export_bpmn(model_id: str) -> str:
    """Export BPMN 2.0 XML for a process model.

    Args:
        model_id: BIC process model ID

    Returns:
        BPMN XML string or JSON error.
    """
    if not BIC_AUTH_TOKEN:
        return _not_configured()

    # TODO: Implement BIC export API
    return json.dumps({"status": "not_implemented", "model_id": model_id})


if __name__ == "__main__":
    mcp.run(transport="stdio")
