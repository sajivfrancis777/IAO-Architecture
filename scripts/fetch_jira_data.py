"""fetch_jira_data.py — Fetch JIRA defect and test data into local JSON cache.

Creates data/jira/ with cached JIRA data for offline report generation.
Self-contained (no mcp dependency) — safe to run in CI.

Reuses the same field IDs and tower mapping as mcp_servers/jira_server.py.

Usage:
    python scripts/fetch_jira_data.py          # fetch all
    python scripts/fetch_jira_data.py --tower FPR   # one tower only
    python scripts/fetch_jira_data.py --dry-run      # preview only
"""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
import urllib3
from dotenv import load_dotenv

# ── Bootstrap ────────────────────────────────────────────────────
WORKSPACE = Path(__file__).resolve().parent.parent
load_dotenv(WORKSPACE / ".env")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_PAT = os.environ.get("JIRA_PAT", "")
PROJECT_KEY = "IAODTM"
DEFAULT_TIMEOUT = 60

OUTPUT_DIR = WORKSPACE / "data" / "jira"

# ── Field IDs (mirror jira_server.py) ────────────────────────────
F_EXTERNAL_ID = "customfield_10808"
F_SEVERITY = "customfield_12125"
F_PHASE_DISCOVERED = "customfield_14621"
F_ACTUAL_RELEASE = "customfield_18400"
JQL_ACTUAL_RELEASE = "Actual Release"
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

# Only "Release 3" exists currently; extend when R4/R5 created
JIRA_ACTIVE_RELEASES = ('"Release 3"',)
ACTIVE_RELEASES = {"R3", "R4", "R5", "Release 3", "Release 4", "Release 5"}

# ── Tower mapping ────────────────────────────────────────────────
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

CLOSED_STATUSES = frozenset((
    "closed", "resolved", "done", "verified", "completed",
    "retest", "canceled", "deferred", "invalid bug/issue creation",
))


# ── HTTP helpers ─────────────────────────────────────────────────

def _headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {JIRA_PAT}", "Accept": "application/json"}


def _jira_get(endpoint: str, params: dict | None = None) -> dict | list:
    if not JIRA_BASE_URL or not JIRA_PAT:
        raise RuntimeError("JIRA not configured. Set JIRA_BASE_URL and JIRA_PAT in .env")
    resp = requests.get(
        JIRA_BASE_URL + endpoint,
        headers=_headers(),
        params=params,
        verify=False,
        timeout=DEFAULT_TIMEOUT,
    )
    ct = resp.headers.get("content-type", "")
    if "json" not in ct:
        raise RuntimeError(f"Non-JSON response ({resp.status_code}) from {endpoint}")
    resp.raise_for_status()
    return resp.json()


def _extract_option_value(field_data) -> str:
    if field_data is None:
        return ""
    if isinstance(field_data, str):
        return field_data
    if isinstance(field_data, dict):
        return field_data.get("value", field_data.get("name", str(field_data)))
    if isinstance(field_data, list):
        return ", ".join(_extract_option_value(v) for v in field_data)
    return str(field_data)


def _resolve_tower_from_jira_team(team_value: str) -> str:
    if not team_value:
        return ""
    for key, tower in _TEAM_TO_TOWER.items():
        if key.lower() in team_value.lower():
            return tower
    return ""


def _resolve_tower_from_subteam(sub_team: str) -> str:
    if not sub_team:
        return ""
    for key, tower in _SUB_TEAM_TO_TOWER.items():
        if key.lower() in sub_team.lower():
            return tower
    return ""


def _is_active_release(release_str: str) -> bool:
    if not release_str:
        return True
    r = release_str.strip()
    if r in ACTIVE_RELEASES:
        return True
    m = re.search(r"(\d+)", r)
    if m:
        return int(m.group(1)) >= 3
    return True


# ── Data fetchers ────────────────────────────────────────────────

def fetch_all_defects() -> list[dict]:
    """Paginate through all R3+ bugs in IAODTM."""
    rel_clause = " OR ".join(f'"{JQL_ACTUAL_RELEASE}" = {r}' for r in JIRA_ACTIVE_RELEASES)
    jql = (
        f"project = {PROJECT_KEY} AND issuetype = Bug AND "
        f'({rel_clause} OR "{JQL_ACTUAL_RELEASE}" IS EMPTY) '
        f"ORDER BY created DESC"
    )

    all_issues: list[dict] = []
    start = 0
    page_size = 200

    while True:
        print(f"  Fetching defects {start}–{start + page_size}...")
        data = _jira_get(
            "/rest/api/2/search",
            params={"jql": jql, "maxResults": page_size, "startAt": start, "fields": BUG_FIELDS},
        )
        issues = data.get("issues", [])
        total = data.get("total", 0)

        for issue in issues:
            f = issue.get("fields", {})
            bug_severity = _extract_option_value(f.get(F_SEVERITY))
            bug_team = _extract_option_value(f.get(F_ASSIGNED_TEAM))
            bug_subteam = _extract_option_value(f.get(F_ASSIGNED_SUBTEAM))
            bug_release = _extract_option_value(f.get(F_ACTUAL_RELEASE))
            affected = _extract_option_value(f.get(F_AFFECTED_PRODUCTS))
            bug_tower = (
                _resolve_tower_from_jira_team(bug_subteam)
                or _resolve_tower_from_jira_team(bug_team)
                or _resolve_tower_from_jira_team(affected)
            )
            bug_status = f.get("status", {})

            all_issues.append({
                "key": issue.get("key", ""),
                "summary": f.get("summary", ""),
                "status": bug_status.get("name", "") if isinstance(bug_status, dict) else str(bug_status),
                "priority": _extract_option_value(f.get("priority")),
                "severity": bug_severity,
                "release": bug_release,
                "tower": bug_tower or "Unmapped",
                "external_id": f.get(F_EXTERNAL_ID, "") or "",
                "assigned_team": bug_team,
                "subteam": bug_subteam,
                "phase_discovered": _extract_option_value(f.get(F_PHASE_DISCOVERED)),
                "defect_type": _extract_option_value(f.get(F_DEFECT_TYPE)),
                "environment": _extract_option_value(f.get(F_ENV_FOUND)),
                "assignee": (f.get("assignee") or {}).get("displayName", ""),
                "created": (f.get("created", "") or "")[:10],
                "updated": (f.get("updated", "") or "")[:10],
            })

        if not issues or start + len(issues) >= total:
            break
        start += len(issues)

    print(f"  Total defects fetched: {len(all_issues)} (JIRA total: {total})")
    return all_issues


def fetch_all_test_cases(max_pages: int = 40) -> list[dict]:
    """Paginate through all Zephyr Scale test cases, filter to R3+."""
    all_cases: list[dict] = []
    start = 0
    batch = 50
    page = 0

    while page < max_pages:
        print(f"  Fetching test cases {start}–{start + batch}...")
        try:
            data = _jira_get(
                "/rest/atm/1.0/testcase/search",
                params={
                    "query": f"projectKey = {PROJECT_KEY}",
                    "maxResults": batch,
                    "startAt": start,
                },
            )
        except Exception as exc:
            print(f"  WARNING: Test case fetch stopped at offset {start}: {exc}")
            break
        if not isinstance(data, list) or len(data) == 0:
            break

        for tc in data:
            cf = tc.get("customFields", {})
            tc_release = cf.get("Release", "")
            tc_subteam = cf.get("Sub Team", "")
            tc_l3id = cf.get("L3 ID (ERP) / L4 ID (SCP)", "")
            tc_tower = _resolve_tower_from_subteam(tc_subteam)
            tc_phase = cf.get("Test Phase", "")

            if not _is_active_release(tc_release):
                continue

            all_cases.append({
                "key": tc.get("key", ""),
                "name": tc.get("name", ""),
                "status": tc.get("status", ""),
                "priority": tc.get("priority", ""),
                "release": tc_release,
                "tower": tc_tower or "Unmapped",
                "l3_l4_id": tc_l3id,
                "test_phase": tc_phase,
                "test_type": cf.get("Test Type", ""),
                "team": cf.get("Team", ""),
                "sub_team": tc_subteam,
            })

        if len(data) < batch:
            break
        start += batch
        page += 1

    print(f"  Total R3+ test cases fetched: {len(all_cases)}")
    return all_cases


# ── Summary computation ──────────────────────────────────────────

def compute_defect_summary(defects: list[dict], tower: str = "") -> dict:
    """Compute the defect summary structure expected by the template."""
    bugs = [d for d in defects if d["tower"] == tower] if tower else defects

    total = len(bugs)
    open_count = 0
    in_progress_count = 0
    resolved_count = 0
    critical_count = 0

    by_severity: dict[str, dict[str, int]] = {}
    by_status: dict[str, int] = {}
    by_tower: dict[str, int] = {}

    now = datetime.now(timezone.utc).date()
    aging_buckets: dict[str, dict[str, int]] = {
        "0–7 days": {"Critical": 0, "High": 0, "Medium": 0, "Low": 0},
        "8–14 days": {"Critical": 0, "High": 0, "Medium": 0, "Low": 0},
        "15–30 days": {"Critical": 0, "High": 0, "Medium": 0, "Low": 0},
        "31–60 days": {"Critical": 0, "High": 0, "Medium": 0, "Low": 0},
        "60+ days": {"Critical": 0, "High": 0, "Medium": 0, "Low": 0},
    }

    open_defects: list[dict] = []

    for d in bugs:
        status_lower = d["status"].lower()
        sev = d["severity"] or "Unknown"
        is_closed = status_lower in CLOSED_STATUSES

        # Status buckets
        if is_closed:
            resolved_count += 1
        elif "in progress" in status_lower or "in review" in status_lower:
            in_progress_count += 1
            open_count += 1
        else:
            open_count += 1

        if "critical" in sev.lower():
            critical_count += 1

        # Severity breakdown
        sev_key = sev if sev in ("Critical", "High", "Medium", "Low") else "Unknown"
        if sev_key not in by_severity:
            by_severity[sev_key] = {"open": 0, "in_progress": 0, "resolved": 0, "total": 0}
        by_severity[sev_key]["total"] += 1
        if is_closed:
            by_severity[sev_key]["resolved"] += 1
        elif "in progress" in status_lower or "in review" in status_lower:
            by_severity[sev_key]["in_progress"] += 1
        else:
            by_severity[sev_key]["open"] += 1

        # Status summary
        by_status[d["status"]] = by_status.get(d["status"], 0) + 1

        # Tower summary
        tw = d["tower"]
        by_tower[tw] = by_tower.get(tw, 0) + 1

        # Aging for open defects
        if not is_closed:
            days_open = 0
            if d.get("created"):
                try:
                    created_date = datetime.strptime(d["created"][:10], "%Y-%m-%d").date()
                    days_open = (now - created_date).days
                except ValueError:
                    pass

            open_defects.append({
                "id": d["key"],
                "severity": sev,
                "summary": d["summary"],
                "status": d["status"],
                "assignee": d.get("assignee", ""),
                "days_open": days_open,
            })

            # Aging bucket
            if sev_key in ("Critical", "High", "Medium", "Low"):
                if days_open <= 7:
                    aging_buckets["0–7 days"][sev_key] += 1
                elif days_open <= 14:
                    aging_buckets["8–14 days"][sev_key] += 1
                elif days_open <= 30:
                    aging_buckets["15–30 days"][sev_key] += 1
                elif days_open <= 60:
                    aging_buckets["31–60 days"][sev_key] += 1
                else:
                    aging_buckets["60+ days"][sev_key] += 1

    # Sort open defects: critical first, then by days_open descending
    sev_order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
    open_defects.sort(key=lambda d: (sev_order.get(d["severity"], 9), -d["days_open"]))

    # Build defect_by_severity list (sorted: Critical, High, Medium, Low, Unknown)
    severity_order = ["Critical", "High", "Medium", "Low", "Unknown"]
    defect_by_severity = []
    for s in severity_order:
        if s in by_severity:
            defect_by_severity.append({"severity": s, **by_severity[s]})

    # Build defect_aging list
    defect_aging = [
        {"bucket": k, "critical": v["Critical"], "high": v["High"],
         "medium": v["Medium"], "low": v["Low"]}
        for k, v in aging_buckets.items()
    ]

    return {
        "defect_summary": {
            "total": total,
            "open": open_count,
            "in_progress": in_progress_count,
            "resolved": resolved_count,
            "critical": critical_count,
        },
        "defect_by_severity": defect_by_severity,
        "defect_aging": defect_aging,
        "open_defects": open_defects[:50],  # top 50
        "by_status": dict(sorted(by_status.items())),
        "by_tower": dict(sorted(by_tower.items())),
    }


def compute_test_summary(test_cases: list[dict], tower: str = "") -> dict:
    """Compute test summary from Zephyr Scale test case statuses."""
    cases = [tc for tc in test_cases if tc["tower"] == tower] if tower else test_cases
    total = len(cases)
    passed = sum(1 for tc in cases if tc["status"] and "approved" in tc["status"].lower())
    failed = sum(1 for tc in cases if tc["status"] and "deprecated" in tc["status"].lower())
    # Zephyr Scale test case statuses: Approved, Draft, Deprecated
    # Map: Approved → passed, Draft → not_run, Deprecated → blocked
    draft = sum(1 for tc in cases if tc["status"] and "draft" in tc["status"].lower())
    blocked = failed  # Use deprecated as blocked proxy
    not_run = draft

    return {
        "total": total,
        "passed": passed,
        "failed": 0,
        "blocked": blocked,
        "not_run": not_run,
        "pass_pct": round(passed / total * 100) if total else 0,
        "fail_pct": 0,
        "blocked_pct": round(blocked / total * 100) if total else 0,
        "not_run_pct": round(not_run / total * 100) if total else 0,
    }


def compute_readiness(defects: list[dict], tower: str = "") -> dict:
    """Compute release readiness for go/no-go."""
    bugs = [d for d in defects if d["tower"] == tower] if tower else defects
    total = len(bugs)
    open_count = 0
    closed_count = 0
    critical_open = 0
    high_open = 0

    for d in bugs:
        is_closed = d["status"].lower() in CLOSED_STATUSES
        if is_closed:
            closed_count += 1
        else:
            open_count += 1
            sev = d.get("severity", "").lower()
            if "critical" in sev:
                critical_open += 1
            elif "high" in sev:
                high_open += 1

    closure_rate = f"{closed_count / total * 100:.0f}%" if total else "N/A"

    go_nogo = "GO"
    if critical_open > 0:
        go_nogo = "NO-GO (critical defects open)"
    elif high_open > 5:
        go_nogo = "CONDITIONAL (>5 high defects open)"
    elif total and open_count > total * 0.2:
        go_nogo = "CONDITIONAL (>20% defects open)"

    return {
        "total_defects": total,
        "open": open_count,
        "closed": closed_count,
        "closure_rate": closure_rate,
        "critical_open": critical_open,
        "high_open": high_open,
        "go_nogo_indicator": go_nogo,
    }


# ── Main ─────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch JIRA data for testing reports")
    parser.add_argument("--tower", type=str, help="Tower shortcode (e.g. FPR)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    if not JIRA_BASE_URL or not JIRA_PAT:
        print("ERROR: JIRA_BASE_URL and JIRA_PAT must be set in .env")
        print("  Skipping JIRA data fetch — reports will use Smartsheet fallback.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Fetch defects ────────────────────────────────────────────
    print("Fetching defects from JIRA...")
    defects = fetch_all_defects()

    # ── Fetch test cases ─────────────────────────────────────────
    print("\nFetching test cases from Zephyr Scale...")
    test_cases = fetch_all_test_cases()

    # ── Compute summaries ────────────────────────────────────────
    towers = sorted({d["tower"] for d in defects} | {tc["tower"] for tc in test_cases})
    tower_summaries: dict[str, dict] = {}

    for tower in towers:
        tower_summaries[tower] = {
            "defect": compute_defect_summary(defects, tower),
            "test": compute_test_summary(test_cases, tower),
            "readiness": compute_readiness(defects, tower),
        }

    cross_tower = {
        "defect": compute_defect_summary(defects),
        "test": compute_test_summary(test_cases),
        "readiness": compute_readiness(defects),
    }

    # ── Compute sub-tower summaries ──────────────────────────────
    # Group defects by JIRA subteam (maps to Smartsheet Sub-Tower Name)
    subtower_summaries: dict[str, dict] = {}
    for d in defects:
        st = d.get("subteam", "").strip()
        if not st:
            st = d.get("assigned_team", "").strip()
        if st:
            subtower_summaries.setdefault(st, []).append(d)

    subtower_data: dict[str, dict] = {}
    for st, st_defects in subtower_summaries.items():
        subtower_data[st] = {
            "defect": compute_defect_summary(st_defects),
            "readiness": compute_readiness(st_defects),
        }

    # ── Build capability mapping ─────────────────────────────────
    cap_map_path = WORKSPACE / "config" / "subtower_capability_map.json"
    capability_summaries: dict[str, dict] = {}
    if cap_map_path.exists():
        with open(cap_map_path, encoding="utf-8") as f:
            cap_map = json.load(f)
        for tower_key, st_map in cap_map.items():
            if tower_key.startswith("_"):
                continue
            for sub_tower, cap_ids in st_map.items():
                st_data = subtower_data.get(sub_tower, {})
                for cap_id in cap_ids:
                    capability_summaries[cap_id] = {
                        "sub_tower": sub_tower,
                        "defect": st_data.get("defect", {}),
                        "readiness": st_data.get("readiness", {}),
                    }
        print(f"  Mapped {len(capability_summaries)} capabilities from {len(subtower_data)} sub-towers")

    # ── Save JSON ────────────────────────────────────────────────
    payload = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "release": "Release 3",
        "defects": defects,
        "test_cases": test_cases,
        "cross_tower_summary": cross_tower,
        "tower_summaries": tower_summaries,
        "subtower_summaries": subtower_data,
        "capability_summaries": capability_summaries,
    }

    if args.dry_run:
        print(f"\n[DRY-RUN] Would write {len(defects)} defects + {len(test_cases)} test cases")
        print(f"  Towers: {', '.join(towers)}")
        for t in towers:
            ts = tower_summaries[t]
            ds = ts["defect"]["defect_summary"]
            print(f"  {t}: {ds['total']} bugs ({ds['critical']} critical, {ds['open']} open)")
        return

    out_path = OUTPUT_DIR / "jira_cache.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote: {out_path} ({out_path.stat().st_size:,} bytes)")

    # Also write a compact summary for quick loading
    summary_path = OUTPUT_DIR / "jira_summary.json"
    summary_payload = {
        "fetched_at": payload["fetched_at"],
        "release": "Release 3",
        "total_defects": len(defects),
        "total_test_cases": len(test_cases),
        "cross_tower_summary": cross_tower,
        "tower_summaries": tower_summaries,
        "subtower_summaries": subtower_data,
        "capability_summaries": capability_summaries,
    }
    summary_path.write_text(json.dumps(summary_payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote: {summary_path} ({summary_path.stat().st_size:,} bytes)")

    # Print summary
    print(f"\n{'='*60}")
    print(f"JIRA Data Fetch Complete")
    print(f"  Defects: {len(defects)}")
    print(f"  Test Cases: {len(test_cases)}")
    print(f"  Towers: {', '.join(towers)}")
    ds = cross_tower["defect"]["defect_summary"]
    print(f"  Critical: {ds['critical']}, Open: {ds['open']}, "
          f"Resolved: {ds['resolved']}, Total: {ds['total']}")
    rd = cross_tower["readiness"]
    print(f"  Readiness: {rd['go_nogo_indicator']} (closure rate: {rd['closure_rate']})")


if __name__ == "__main__":
    main()
