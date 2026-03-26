"""jira_server.py — MCP server for JIRA test management queries.

Placeholder — ready to implement when JIRA API access is provisioned.

Expected tools:
  - get_test_cases(cap_id)     → test case list with pass/fail status
  - get_defects(cap_id)        → defect list by severity
  - get_sprint_status(tower)   → sprint burn-down / release readiness
  - search_issues(jql)         → raw JQL search

Run:
    python -m mcp_servers.jira_server
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
    "IAO JIRA",
    instructions=(
        "Provides live access to JIRA for test execution status, defect tracking, "
        "and sprint/release readiness across IDM 2.0 towers. "
        "NOT YET IMPLEMENTED — tools return placeholder responses."
    ),
)

JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "")
JIRA_TOKEN = os.environ.get("JIRA_API_TOKEN", "")
JIRA_USER = os.environ.get("JIRA_USER_EMAIL", "")


def _not_configured() -> str:
    return json.dumps({
        "error": "JIRA integration not yet configured.",
        "action_required": [
            "Set JIRA_BASE_URL in .env (e.g. https://jira.intel.com)",
            "Set JIRA_USER_EMAIL in .env",
            "Set JIRA_API_TOKEN in .env (personal access token)",
        ],
    })


@mcp.tool()
def get_test_cases(
    tower: str,
    capability_name: str = "",
    status_filter: str = "",
) -> str:
    """Get test case execution status for a tower or capability.

    Args:
        tower: Tower shortcode (FPR, OTC-IF, OTC-IP, FTS-IF, FTS-IP, PTP, MDM, E2E)
        capability_name: Optional capability name to filter
        status_filter: Optional filter (Pass, Fail, Blocked, Not Run)

    Returns:
        JSON with test cases, pass/fail counts, and coverage percentage.
    """
    if not JIRA_BASE_URL or not JIRA_TOKEN:
        return _not_configured()

    # TODO: Implement JIRA REST API call
    # GET /rest/api/2/search?jql=project={tower} AND issuetype=Test ...
    return json.dumps({"status": "not_implemented", "tower": tower})


@mcp.tool()
def get_defects(
    tower: str,
    capability_name: str = "",
    severity: str = "",
) -> str:
    """Get defects/bugs for a tower or capability.

    Args:
        tower: Tower shortcode
        capability_name: Optional capability name to filter
        severity: Optional severity filter (Critical, High, Medium, Low)

    Returns:
        JSON with defects grouped by severity and status.
    """
    if not JIRA_BASE_URL or not JIRA_TOKEN:
        return _not_configured()

    # TODO: Implement JIRA REST API call
    # GET /rest/api/2/search?jql=project={tower} AND issuetype=Bug ...
    return json.dumps({"status": "not_implemented", "tower": tower})


@mcp.tool()
def get_sprint_status(tower: str) -> str:
    """Get current sprint status and release readiness for a tower.

    Args:
        tower: Tower shortcode

    Returns:
        JSON with sprint name, velocity, burn-down, and go-live readiness metrics.
    """
    if not JIRA_BASE_URL or not JIRA_TOKEN:
        return _not_configured()

    # TODO: Implement JIRA Agile REST API call
    # GET /rest/agile/1.0/board/{boardId}/sprint?state=active
    return json.dumps({"status": "not_implemented", "tower": tower})


@mcp.tool()
def search_issues(jql: str, max_results: int = 50) -> str:
    """Execute a raw JQL search against JIRA.

    Args:
        jql: JIRA Query Language string
        max_results: Maximum results to return (default 50)

    Returns:
        JSON with matching issues.
    """
    if not JIRA_BASE_URL or not JIRA_TOKEN:
        return _not_configured()

    # TODO: Implement JIRA REST API call
    # GET /rest/api/2/search?jql={jql}&maxResults={max_results}
    return json.dumps({"status": "not_implemented", "jql": jql})


if __name__ == "__main__":
    mcp.run(transport="stdio")
