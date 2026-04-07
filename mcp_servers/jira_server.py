"""jira_server.py — MCP server for JIRA test management & defect queries.

Connects to Intel Jira Server at jira.devtools.intel.com with PAT auth.
Queries the IAODTM project for test cases (Zephyr Scale), defects, and
issue searches.  Focuses on Release 3+ data by default.

Data model:
  - Zephyr Scale test cases:  /rest/atm/1.0/testcase/search
    Custom fields: Release, Sub Team, L3 ID, Test Phase, Test Type, etc.
  - JIRA issues (bugs):       /rest/api/2/search
    Key fields: customfield_10808 (External ID), customfield_18400 (Release),
    customfield_44402 (Assigned Team), customfield_50501 (Subteam),
    customfield_12125 (Severity), customfield_14621 (Phase Discovered)

Tools:
  - get_test_cases       → Zephyr Scale test cases with tower/capability mapping
  - get_defects          → Bugs with severity/status/tower breakdown
  - get_defect_summary   → High-level defect metrics (no individual details)
  - get_test_execution_results → Pass/fail execution results
  - search_issues        → Flexible JQL or structured search
  - get_release_readiness → Go/no-go metrics for a release

Run:
    python -m mcp_servers.jira_server
"""

from __future__ import annotations

import json
import os
import re
import urllib3
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# ── Bootstrap ───────────────────────────────────────────────────────
_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")

# Suppress InsecureRequestWarning (Intel self-signed certs)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ── Constants ───────────────────────────────────────────────────────
JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_PAT = os.environ.get("JIRA_PAT", "")
PROJECT_KEY = "IAODTM"
DEFAULT_TIMEOUT = 30

# All desired releases — validated at runtime against JIRA
ACTIVE_RELEASES = {"R1", "R2", "R3", "R4", "R5", "Release 1", "Release 2", "Release 3", "Release 4", "Release 5"}
JIRA_DESIRED_RELEASES = ('"Release 1"', '"Release 2"', '"Release 3"', '"Release 4"', '"Release 5"',)

_validated_releases: tuple[str, ...] | None = None

# ── Tower mapping: Sub Team field → tower shortcode ─────────────────
_SUB_TEAM_TO_TOWER: dict[str, str] = {
    "FPR": "FPR",
    "OTC-IF": "OTC-IF", "OTC IF": "OTC-IF",
    "OTC-IP": "OTC-IP", "OTC IP": "OTC-IP",
    "FTS-IF": "FTS-IF", "FTS IF": "FTS-IF",
    "FTS-IP": "FTS-IP", "FTS IP": "FTS-IP",
    "PTP": "PTP",
    "MDM": "MDM",
    "E2E": "E2E",
    "Analytics": "FPR",
}

_TEAM_TO_TOWER: dict[str, str] = {
    "3.5 FPR": "FPR", "FPR": "FPR",
    "10. Analytics": "FPR", "10A. Analytics": "FPR",
    "OTC-IF": "OTC-IF", "OTC-IP": "OTC-IP",
    "FTS-IF": "FTS-IF", "FTS-IP": "FTS-IP",
    "PTP": "PTP", "MDM": "MDM", "E2E": "E2E",
}

# ── Bug field IDs ───────────────────────────────────────────────────
F_EXTERNAL_ID = "customfield_10808"
F_SEVERITY = "customfield_12125"
F_PHASE_DISCOVERED = "customfield_14621"
F_ACTUAL_RELEASE = "customfield_18400"  # Field ID (for reading response data)
JQL_ACTUAL_RELEASE = "Actual Release"     # Field name (for JQL queries)
F_AFFECTED_PRODUCTS = "customfield_19900"
F_TEST_CYCLE = "customfield_22002"
F_ENV_FOUND = "customfield_22600"
F_ASSIGNED_TEAM = "customfield_44402"
F_ASSIGNED_SUBTEAM = "customfield_50501"
F_DETECTED_SUBTEAM = "customfield_50502"
F_DEFECT_TYPE = "customfield_37612"

BUG_FIELDS = (
    "key,summary,status,priority,created,updated,assignee,reporter,"
    f"{F_EXTERNAL_ID},{F_SEVERITY},{F_PHASE_DISCOVERED},{F_ACTUAL_RELEASE},"
    f"{F_AFFECTED_PRODUCTS},{F_TEST_CYCLE},{F_ENV_FOUND},{F_ASSIGNED_TEAM},"
    f"{F_ASSIGNED_SUBTEAM},{F_DETECTED_SUBTEAM},{F_DEFECT_TYPE}"
)

# ── MCP Server ──────────────────────────────────────────────────────
mcp = FastMCP(
    "IAO JIRA",
    instructions=(
        "Provides live access to Intel JIRA (IAODTM project) for test case "
        "status, defect tracking, and release readiness across IDM 2.0 towers. "
        "Covers Zephyr Scale test cases and JIRA bugs. Default scope is R3+."
    ),
)


# ── HTTP helpers ────────────────────────────────────────────────────

def _headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {JIRA_PAT}", "Accept": "application/json"}


def _jira_get(endpoint: str, params: dict | None = None) -> Any:
    """GET against JIRA REST API with error handling."""
    if not JIRA_BASE_URL or not JIRA_PAT:
        raise RuntimeError(
            "JIRA not configured. Set JIRA_BASE_URL and JIRA_PAT in .env"
        )
    resp = requests.get(
        JIRA_BASE_URL + endpoint,
        headers=_headers(),
        params=params,
        verify=False,
        timeout=DEFAULT_TIMEOUT,
    )
    ct = resp.headers.get("content-type", "")
    if "json" not in ct:
        raise RuntimeError(
            f"Non-JSON response ({resp.status_code}) from {endpoint}"
        )
    resp.raise_for_status()
    return resp.json()


def _discover_valid_releases() -> tuple[str, ...]:
    """Probe JIRA to find which 'Actual Release' options exist."""
    rel_clause = " OR ".join(
        f'"{JQL_ACTUAL_RELEASE}" = {r}' for r in JIRA_DESIRED_RELEASES
    )
    jql = f"project = {PROJECT_KEY} AND issuetype = Bug AND ({rel_clause})"
    resp = requests.get(
        JIRA_BASE_URL + "/rest/api/2/search",
        headers=_headers(),
        params={"jql": jql, "maxResults": 0},
        verify=False,
        timeout=DEFAULT_TIMEOUT,
    )
    if resp.status_code == 200:
        return JIRA_DESIRED_RELEASES
    if resp.status_code == 400:
        try:
            errors = resp.json().get("errorMessages", [])
        except Exception:
            errors = []
        invalid: set[str] = set()
        for msg in errors:
            m = re.search(r"The option '(.+?)' for field", msg)
            if m:
                invalid.add(m.group(1))
        if invalid:
            return tuple(
                r for r in JIRA_DESIRED_RELEASES
                if not any(inv in r for inv in invalid)
            )
    return JIRA_DESIRED_RELEASES


def _get_valid_releases() -> tuple[str, ...]:
    """Return cached validated release options (probes JIRA once per run)."""
    global _validated_releases
    if _validated_releases is None:
        _validated_releases = _discover_valid_releases()
    return _validated_releases


def _not_configured() -> str:
    return json.dumps({
        "error": "JIRA integration not configured.",
        "action_required": [
            "Set JIRA_BASE_URL in .env (https://jira.devtools.intel.com)",
            "Set JIRA_PAT in .env (personal access token)",
        ],
    })


# ── Mapping helpers ─────────────────────────────────────────────────

def _resolve_tower_from_subteam(sub_team: str) -> str:
    """Extract tower shortcode from Zephyr Sub Team value."""
    if not sub_team:
        return ""
    for key, tower in _SUB_TEAM_TO_TOWER.items():
        if key.lower() in sub_team.lower():
            return tower
    return ""


def _resolve_tower_from_jira_team(team_value: str) -> str:
    """Extract tower shortcode from JIRA Assigned Team / Affected Products."""
    if not team_value:
        return ""
    for key, tower in _TEAM_TO_TOWER.items():
        if key.lower() in team_value.lower():
            return tower
    return ""


def _extract_option_value(field_data: Any) -> str:
    """Extract display value from JIRA custom field (option, string, or list)."""
    if field_data is None:
        return ""
    if isinstance(field_data, str):
        return field_data
    if isinstance(field_data, dict):
        return field_data.get("value", field_data.get("name", str(field_data)))
    if isinstance(field_data, list):
        return ", ".join(_extract_option_value(v) for v in field_data)
    return str(field_data)


def _is_active_release(release_str: str) -> bool:
    """Check if a release string matches R3+."""
    if not release_str:
        return True  # Include items with no release tag
    r = release_str.strip()
    if r in ACTIVE_RELEASES:
        return True
    m = re.search(r"(\d+)", r)
    if m:
        return int(m.group(1)) >= 3
    return True


# ── TOOLS ───────────────────────────────────────────────────────────


@mcp.tool()
def get_test_cases(
    tower: str = "",
    capability_id: str = "",
    release: str = "",
    test_phase: str = "",
    max_results: int = 200,
) -> str:
    """Get Zephyr Scale test cases for a tower or capability (R3+ by default).

    Args:
        tower: Tower shortcode (FPR, OTC-IF, OTC-IP, FTS-IF, FTS-IP, PTP, MDM, E2E). Optional.
        capability_id: L3/L4 capability ID to filter (e.g. "DS-020", "MR-010-020"). Optional.
        release: Release filter (R3, R4, R5). Defaults to R3+ if empty.
        test_phase: Test phase filter (ITC1, ITC2, TUT, E2E, etc.). Optional.
        max_results: Max test cases to return (default 200).

    Returns:
        JSON with test cases, summary counts, and tower/capability breakdown.
    """
    if not JIRA_BASE_URL or not JIRA_PAT:
        return _not_configured()

    try:
        all_cases: list[dict] = []
        start = 0
        batch = min(max_results, 50)

        while start < max_results:
            data = _jira_get(
                "/rest/atm/1.0/testcase/search",
                params={
                    "query": f"projectKey = {PROJECT_KEY}",
                    "maxResults": batch,
                    "startAt": start,
                },
            )
            if not isinstance(data, list) or len(data) == 0:
                break
            all_cases.extend(data)
            if len(data) < batch:
                break
            start += batch

        results: list[dict] = []
        for tc in all_cases:
            cf = tc.get("customFields", {})
            tc_release = cf.get("Release", "")
            tc_subteam = cf.get("Sub Team", "")
            tc_l3id = cf.get("L3 ID (ERP) / L4 ID (SCP)", "")
            tc_tower = _resolve_tower_from_subteam(tc_subteam)
            tc_phase = cf.get("Test Phase", "")

            if not _is_active_release(tc_release):
                continue
            if release and release.upper() != tc_release.upper():
                continue
            if tower and tc_tower != tower.strip().upper():
                continue
            if capability_id and capability_id.upper() not in (tc_l3id or "").upper():
                continue
            if test_phase and test_phase.upper() != tc_phase.upper():
                continue

            results.append({
                "key": tc.get("key", ""),
                "name": tc.get("name", ""),
                "objective": (tc.get("objective", "") or "")[:200],
                "status": tc.get("status", ""),
                "priority": tc.get("priority", ""),
                "release": tc_release,
                "tower": tc_tower,
                "l3_l4_id": tc_l3id,
                "test_phase": tc_phase,
                "test_type": cf.get("Test Type", ""),
                "method": cf.get("Method", ""),
                "team": cf.get("Team", ""),
                "sub_team": tc_subteam,
                "environment": cf.get("Environment", ""),
                "application": cf.get("Application", ""),
            })

        by_tower: dict[str, int] = {}
        by_phase: dict[str, int] = {}
        by_status: dict[str, int] = {}
        for r in results:
            t = r["tower"] or "Unmapped"
            by_tower[t] = by_tower.get(t, 0) + 1
            p = r["test_phase"] or "Unknown"
            by_phase[p] = by_phase.get(p, 0) + 1
            s = r["status"] or "Unknown"
            by_status[s] = by_status.get(s, 0) + 1

        return json.dumps({
            "filters": {
                "tower": tower or "(all)",
                "capability_id": capability_id or "(all)",
                "release": release or "R3+",
                "test_phase": test_phase or "(all)",
            },
            "total": len(results),
            "by_tower": dict(sorted(by_tower.items())),
            "by_phase": dict(sorted(by_phase.items())),
            "by_status": dict(sorted(by_status.items())),
            "test_cases": results[:max_results],
            "source": "live_jira_zephyr_scale",
        }, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def get_defects(
    tower: str = "",
    severity: str = "",
    status: str = "",
    release: str = "",
    max_results: int = 200,
) -> str:
    """Get defects/bugs from JIRA for a tower (R3+ by default).

    Args:
        tower: Tower shortcode (FPR, OTC-IF, OTC-IP, FTS-IF, FTS-IP, PTP, MDM, E2E). Optional.
        severity: Severity filter (Critical, High, Medium, Low). Optional.
        status: JIRA status filter (Open, In Progress, Resolved, Closed). Optional.
        release: Release filter (Release 3, Release 4). Defaults to R3+.
        max_results: Max defects to return (default 200).

    Returns:
        JSON with defects, severity breakdown, and status summary.
    """
    if not JIRA_BASE_URL or not JIRA_PAT:
        return _not_configured()

    try:
        jql_parts = [f"project = {PROJECT_KEY}", "issuetype = Bug"]

        if release:
            jql_parts.append(f'"{JQL_ACTUAL_RELEASE}" = "{release}"')
        else:
            valid_releases = _get_valid_releases()
            rel_clause = " OR ".join(f'"{JQL_ACTUAL_RELEASE}" = {r}' for r in valid_releases)
            jql_parts.append(f'({rel_clause} OR "{JQL_ACTUAL_RELEASE}" IS EMPTY)')

        if status:
            jql_parts.append(f'status = "{status}"')

        jql = " AND ".join(jql_parts)
        max_results = min(max_results, 500)

        data = _jira_get(
            "/rest/api/2/search",
            params={
                "jql": jql,
                "maxResults": max_results,
                "fields": BUG_FIELDS,
            },
        )

        issues = data.get("issues", [])
        results: list[dict] = []

        for issue in issues:
            f = issue.get("fields", {})
            bug_severity = _extract_option_value(f.get(F_SEVERITY))
            bug_team = _extract_option_value(f.get(F_ASSIGNED_TEAM))
            bug_subteam = _extract_option_value(f.get(F_ASSIGNED_SUBTEAM))
            bug_release = _extract_option_value(f.get(F_ACTUAL_RELEASE))
            bug_tower = (
                _resolve_tower_from_jira_team(bug_subteam)
                or _resolve_tower_from_jira_team(bug_team)
                or _resolve_tower_from_jira_team(
                    _extract_option_value(f.get(F_AFFECTED_PRODUCTS))
                )
            )

            if tower and bug_tower != tower.strip().upper():
                continue
            if severity and severity.lower() not in bug_severity.lower():
                continue

            bug_status = f.get("status", {})
            results.append({
                "key": issue.get("key", ""),
                "summary": f.get("summary", ""),
                "status": bug_status.get("name", "") if isinstance(bug_status, dict) else str(bug_status),
                "priority": _extract_option_value(f.get("priority")),
                "severity": bug_severity,
                "release": bug_release,
                "tower": bug_tower,
                "external_id": f.get(F_EXTERNAL_ID, ""),
                "assigned_team": bug_team,
                "subteam": bug_subteam,
                "phase_discovered": _extract_option_value(f.get(F_PHASE_DISCOVERED)),
                "defect_type": _extract_option_value(f.get(F_DEFECT_TYPE)),
                "environment": _extract_option_value(f.get(F_ENV_FOUND)),
                "assignee": (f.get("assignee") or {}).get("displayName", ""),
                "created": (f.get("created", ""))[:10],
                "updated": (f.get("updated", ""))[:10],
            })

        by_severity: dict[str, int] = {}
        by_status_sum: dict[str, int] = {}
        by_tower_sum: dict[str, int] = {}
        for r in results:
            s = r["severity"] or "Unknown"
            by_severity[s] = by_severity.get(s, 0) + 1
            st = r["status"] or "Unknown"
            by_status_sum[st] = by_status_sum.get(st, 0) + 1
            t = r["tower"] or "Unmapped"
            by_tower_sum[t] = by_tower_sum.get(t, 0) + 1

        return json.dumps({
            "filters": {
                "tower": tower or "(all)",
                "severity": severity or "(all)",
                "status": status or "(all)",
                "release": release or "R3+",
            },
            "total_matching": data.get("total", 0),
            "returned": len(results),
            "by_severity": dict(sorted(by_severity.items())),
            "by_status": dict(sorted(by_status_sum.items())),
            "by_tower": dict(sorted(by_tower_sum.items())),
            "defects": results,
            "source": "live_jira_api",
        }, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def get_defect_summary(tower: str = "") -> str:
    """Get a high-level defect summary — counts by severity, status, and tower (R3+).

    Args:
        tower: Tower shortcode. Optional — omit for cross-tower summary.

    Returns:
        JSON summary with severity/status/tower breakdowns. No individual defect details.
    """
    if not JIRA_BASE_URL or not JIRA_PAT:
        return _not_configured()

    try:
        jql_parts = [
            f"project = {PROJECT_KEY}",
            "issuetype = Bug",
            "(" + " OR ".join(f'"{JQL_ACTUAL_RELEASE}" = {r}' for r in _get_valid_releases())
            + f' OR "{JQL_ACTUAL_RELEASE}" IS EMPTY)',
        ]
        jql = " AND ".join(jql_parts)

        data = _jira_get(
            "/rest/api/2/search",
            params={
                "jql": jql,
                "maxResults": 500,
                "fields": f"status,priority,{F_SEVERITY},{F_ACTUAL_RELEASE},"
                          f"{F_ASSIGNED_TEAM},{F_ASSIGNED_SUBTEAM},{F_AFFECTED_PRODUCTS}",
            },
        )

        total_in_jira = data.get("total", 0)
        issues = data.get("issues", [])

        by_severity: dict[str, int] = {}
        by_status: dict[str, int] = {}
        by_tower: dict[str, int] = {}
        by_release: dict[str, int] = {}

        for issue in issues:
            f = issue.get("fields", {})
            sev = _extract_option_value(f.get(F_SEVERITY)) or "Unknown"
            st = (f.get("status") or {}).get("name", "Unknown")
            rel = _extract_option_value(f.get(F_ACTUAL_RELEASE)) or "No Release"
            team = _extract_option_value(f.get(F_ASSIGNED_SUBTEAM)) or _extract_option_value(f.get(F_ASSIGNED_TEAM))
            affected = _extract_option_value(f.get(F_AFFECTED_PRODUCTS))
            tw = _resolve_tower_from_jira_team(team) or _resolve_tower_from_jira_team(affected) or "Unmapped"

            if tower and tw != tower.strip().upper():
                continue

            by_severity[sev] = by_severity.get(sev, 0) + 1
            by_status[st] = by_status.get(st, 0) + 1
            by_tower[tw] = by_tower.get(tw, 0) + 1
            by_release[rel] = by_release.get(rel, 0) + 1

        total_filtered = sum(by_severity.values())

        return json.dumps({
            "filter": {"tower": tower or "(all)", "release": "R3+"},
            "total_bugs_in_project": total_in_jira,
            "total_filtered": total_filtered,
            "by_severity": dict(sorted(by_severity.items())),
            "by_status": dict(sorted(by_status.items())),
            "by_tower": dict(sorted(by_tower.items())),
            "by_release": dict(sorted(by_release.items())),
            "source": "live_jira_api",
        }, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def get_test_execution_results(
    test_case_key: str = "",
    capability_id: str = "",
    max_results: int = 100,
) -> str:
    """Get test execution results from Zephyr Scale.

    Args:
        test_case_key: Specific test case key (e.g. "IAODTM-T157"). Optional.
        capability_id: L3/L4 capability ID to find test cases for. Optional.
        max_results: Max results (default 100).

    Returns:
        JSON with execution results (pass/fail/blocked/not-run).
    """
    if not JIRA_BASE_URL or not JIRA_PAT:
        return _not_configured()

    try:
        tc_keys: list[str] = []
        if test_case_key:
            tc_keys = [test_case_key]
        elif capability_id:
            cases = _jira_get(
                "/rest/atm/1.0/testcase/search",
                params={
                    "query": f"projectKey = {PROJECT_KEY}",
                    "maxResults": 50,
                },
            )
            if isinstance(cases, list):
                for tc in cases:
                    cf = tc.get("customFields", {})
                    l3id = cf.get("L3 ID (ERP) / L4 ID (SCP)", "")
                    if capability_id.upper() in (l3id or "").upper():
                        tc_keys.append(tc.get("key", ""))

        if not tc_keys:
            return json.dumps({
                "error": "No test cases found. Provide test_case_key or capability_id.",
                "hint": "Use get_test_cases() first to find relevant test case keys.",
            })

        all_results: list[dict] = []
        for key in tc_keys[:20]:
            try:
                execs = _jira_get(
                    "/rest/atm/1.0/testresult/search",
                    params={
                        "query": f"testCase = '{key}'",
                        "maxResults": max_results,
                    },
                )
                if isinstance(execs, list):
                    for ex in execs:
                        all_results.append({
                            "test_case_key": key,
                            "execution_key": ex.get("key", ""),
                            "status": ex.get("status", ""),
                            "environment": ex.get("environment", ""),
                            "executed_by": ex.get("executedBy", ""),
                            "execution_date": (ex.get("executionDate", "") or "")[:10],
                            "comment": (ex.get("comment", "") or "")[:200],
                        })
            except Exception:
                continue

        by_status: dict[str, int] = {}
        for r in all_results:
            s = r["status"] or "Unknown"
            by_status[s] = by_status.get(s, 0) + 1

        return json.dumps({
            "test_cases_queried": len(tc_keys),
            "total_executions": len(all_results),
            "by_status": dict(sorted(by_status.items())),
            "results": all_results[:max_results],
            "source": "live_jira_zephyr_scale",
        }, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def search_issues(
    jql: str = "",
    tower: str = "",
    issue_type: str = "Bug",
    text: str = "",
    max_results: int = 50,
) -> str:
    """Search JIRA issues with JQL or structured filters.

    Args:
        jql: Raw JQL query. If provided, other filters are ignored.
        tower: Tower shortcode for team-based filtering. Optional.
        issue_type: Issue type (Bug, Task, Issue, Sub-task). Default: Bug.
        text: Free text search in summary/description. Optional.
        max_results: Max results (default 50, max 200).

    Returns:
        JSON with matching issues.
    """
    if not JIRA_BASE_URL or not JIRA_PAT:
        return _not_configured()

    try:
        if not jql:
            parts = [f"project = {PROJECT_KEY}"]
            if issue_type:
                parts.append(f"issuetype = '{issue_type}'")
            if text:
                safe_text = text.replace('"', '\\"')
                parts.append(f'text ~ "{safe_text}"')
            jql = " AND ".join(parts)

        max_results = min(max(1, max_results), 200)

        data = _jira_get(
            "/rest/api/2/search",
            params={
                "jql": jql,
                "maxResults": max_results,
                "fields": BUG_FIELDS,
            },
        )

        issues = data.get("issues", [])
        results: list[dict] = []

        for issue in issues:
            f = issue.get("fields", {})
            team = _extract_option_value(f.get(F_ASSIGNED_SUBTEAM)) or _extract_option_value(f.get(F_ASSIGNED_TEAM))
            tw = _resolve_tower_from_jira_team(team)

            if tower and tw != tower.strip().upper():
                continue

            bug_status = f.get("status", {})
            results.append({
                "key": issue.get("key", ""),
                "summary": f.get("summary", ""),
                "type": _extract_option_value(f.get("issuetype")),
                "status": bug_status.get("name", "") if isinstance(bug_status, dict) else str(bug_status),
                "priority": _extract_option_value(f.get("priority")),
                "severity": _extract_option_value(f.get(F_SEVERITY)),
                "tower": tw,
                "external_id": f.get(F_EXTERNAL_ID, ""),
                "assignee": (f.get("assignee") or {}).get("displayName", ""),
                "created": (f.get("created", ""))[:10],
            })

        return json.dumps({
            "jql": jql,
            "total_matching": data.get("total", 0),
            "returned": len(results),
            "issues": results,
            "source": "live_jira_api",
        }, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def get_release_readiness(tower: str = "", release: str = "Release 3") -> str:
    """Get release readiness metrics — open vs closed defects, go/no-go indicator.

    Args:
        tower: Tower shortcode. Optional — omit for cross-tower view.
        release: Release name (default "Release 3").

    Returns:
        JSON with readiness metrics: open/closed defects, severity breakdown,
        and go/no-go indicators.
    """
    if not JIRA_BASE_URL or not JIRA_PAT:
        return _not_configured()

    try:
        jql = (
            f'project = {PROJECT_KEY} AND issuetype = Bug AND '
            f'"{JQL_ACTUAL_RELEASE}" = "{release}"'
        )

        data = _jira_get(
            "/rest/api/2/search",
            params={
                "jql": jql,
                "maxResults": 500,
                "fields": f"status,{F_SEVERITY},{F_ASSIGNED_TEAM},{F_ASSIGNED_SUBTEAM},{F_AFFECTED_PRODUCTS}",
            },
        )

        total = data.get("total", 0)
        issues = data.get("issues", [])

        open_count = 0
        closed_count = 0
        critical_open = 0
        high_open = 0
        by_tower: dict[str, dict[str, int]] = {}

        for issue in issues:
            f = issue.get("fields", {})
            st = (f.get("status") or {}).get("name", "")
            sev = _extract_option_value(f.get(F_SEVERITY))
            team = _extract_option_value(f.get(F_ASSIGNED_SUBTEAM)) or _extract_option_value(f.get(F_ASSIGNED_TEAM))
            affected = _extract_option_value(f.get(F_AFFECTED_PRODUCTS))
            tw = _resolve_tower_from_jira_team(team) or _resolve_tower_from_jira_team(affected) or "Unmapped"

            if tower and tw != tower.strip().upper():
                continue

            is_closed = st.lower() in (
                "closed", "resolved", "done", "verified", "completed",
                "retest", "canceled", "deferred", "invalid bug/issue creation",
            )
            if is_closed:
                closed_count += 1
            else:
                open_count += 1
                if "critical" in sev.lower():
                    critical_open += 1
                elif "high" in sev.lower():
                    high_open += 1

            if tw not in by_tower:
                by_tower[tw] = {"open": 0, "closed": 0}
            by_tower[tw]["closed" if is_closed else "open"] += 1

        total_filtered = open_count + closed_count
        closure_rate = f"{closed_count / total_filtered * 100:.0f}%" if total_filtered else "N/A"

        go_nogo = "GO"
        if critical_open > 0:
            go_nogo = "NO-GO (critical defects open)"
        elif high_open > 5:
            go_nogo = "CONDITIONAL (>5 high defects open)"
        elif total_filtered and open_count > total_filtered * 0.2:
            go_nogo = "CONDITIONAL (>20% defects open)"

        return json.dumps({
            "release": release,
            "tower": tower or "(all)",
            "total_defects": total_filtered,
            "open": open_count,
            "closed": closed_count,
            "closure_rate": closure_rate,
            "critical_open": critical_open,
            "high_open": high_open,
            "go_nogo_indicator": go_nogo,
            "by_tower": dict(sorted(by_tower.items())),
            "source": "live_jira_api",
        }, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


# ── Entry Point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run(transport="stdio")
