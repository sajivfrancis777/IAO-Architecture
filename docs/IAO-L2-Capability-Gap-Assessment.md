# IAO L2 Capability Gap Assessment

**Date:** June 2025  
**Author:** Sajiv Francis — Enterprise Architect  
**Scope:** IDM 2.0 / JIRA Project IAODTM — All Towers  

---

## Executive Summary

This assessment identifies gaps in L2 capability mapping efficiency across the IAO testing pillar (JIRA test cases and defects). The goal is to improve capability-level visibility, enable tower-filtered dashboards, and ensure every test case and defect traces back to a business capability (L3/L4 ID).

**Key Finding:** While 61% of test cases carry an L3/L4 ID, **zero defects** have this mapping. Three towers (OTC-IP, FTS-IP, PTP) have no test cases at all. These gaps prevent accurate capability-level quality assessment and Go/No-Go decisions at the L2 level.

---

## 1. Tower Coverage Gaps

### Test Case Coverage by Tower

| Tower | Test Cases | Defects | TC:Defect Ratio | Status |
|-------|-----------|---------|-----------------|--------|
| FPR | 1,283 | 1,469 | 0.87:1 | ✅ Covered |
| OTC-IF | 1,297 | 1,849 | 0.70:1 | ✅ Covered |
| OTC-IP | **0** | 216 | 0:1 | ❌ **No Test Cases** |
| FTS-IF | 384 | 568 | 0.68:1 | ✅ Covered |
| FTS-IP | **0** | 115 | 0:1 | ❌ **No Test Cases** |
| PTP | **0** | 15 | 0:1 | ❌ **No Test Cases** |
| MDM | 1,033 | 707 | 1.46:1 | ✅ Covered |
| E2E | 314 | 361 | 0.87:1 | ✅ Covered |
| Unmapped | 389 | 37 | — | ⚠️ **Needs Classification** |

### Gap Analysis

- **3 towers with ZERO test cases:** OTC-IP, FTS-IP, PTP — these towers have active defects but no Zephyr Scale test cases. This means:
  - Quality metrics (pass rate, execution status) cannot be calculated
  - Go/No-Go assessment is impossible at tower level
  - Dashboard testing pillar shows incomplete data for these towers

- **389 unmapped test cases** — These belong to SCP (Supply Chain Planning) sub-towers that don't map to the standard 8-tower classification:
  - 18.3 SCP IF Supply Planning (98 TCs)
  - 18.4 SCP IP Supply Planning (94 TCs)
  - 18.2 SCP IP Demand Planning (92 TCs)
  - 18.2 SCP IP Demand Planning → B-App Supply Demand Planning (45 TCs)
  - 18.1 SCP IF Demand Planning (39 TCs)
  - 18.4 SCP IP Supply Planning → B-App Supply Demand Planning (21 TCs)

### Recommendation

1. **OTC-IP, FTS-IP, PTP:** Verify with tower leads whether test cases exist in a different JIRA project or under a different classification. If testing is in progress, ensure Zephyr Scale test cases are created and tagged with the correct tower.
2. **SCP Unmapped TCs:** Extend the tower mapping in `jira_server.py` to classify SCP sub-towers (18.x series) into the appropriate parent towers (FTS-IF/FTS-IP).

---

## 2. L3/L4 Capability ID Coverage

The L3/L4 ID (field: "L3 ID (ERP) / L4 ID (SCP)") links test cases to specific business capabilities, enabling drill-down from tower → process lane → capability.

### Test Case L3/L4 Coverage by Tower

| Tower | Has L3/L4 ID | Total TCs | Coverage % | Status |
|-------|-------------|-----------|-----------|--------|
| FPR | 988 | 1,283 | **77%** | ✅ Good |
| MDM | 745 | 1,033 | **72%** | ✅ Good |
| OTC-IF | 801 | 1,297 | **62%** | ⚠️ Moderate |
| FTS-IF | 142 | 384 | **37%** | ❌ Low |
| E2E | 6 | 314 | **2%** | ❌ Critical |
| OTC-IP | 0 | 0 | — | ❌ No Data |
| FTS-IP | 0 | 0 | — | ❌ No Data |
| PTP | 0 | 0 | — | ❌ No Data |

**Overall:** 2,682 / 4,700 = **57%** coverage (excluding N/A and QA values)

### Defect L3/L4 Coverage

| Metric | Value |
|--------|-------|
| Defects with L3/L4 ID | **0** |
| Total Defects | 5,337 |
| Coverage | **0%** |

**Root Cause:** Defects are standard JIRA issues (issuetype = Bug), not Zephyr Scale entities. The "L3 ID (ERP) / L4 ID (SCP)" field exists only on Zephyr Scale test cases, not on Bug issue types. Defects therefore cannot be mapped to capabilities via this field.

### Gap Impact

Without L3/L4 mapping on defects:
- Cannot show "defects per capability" in architecture drill-down
- Cannot correlate test failures with specific business processes
- Go/No-Go decision at capability level relies solely on test execution status, not defect severity

### Recommendations for Improving L3/L4 Efficiency

1. **Test Cases (short-term):** Run a bulk update in Zephyr Scale to populate L3/L4 IDs for the 1,845 unmapped test cases (39% gap), prioritizing:
   - FTS-IF (37% coverage → target 80%)
   - E2E (2% coverage → target 50%)
   - OTC-IF (62% coverage → target 80%)

2. **Defects (medium-term):** Add a custom field `L3_L4_ID` to the IAODTM Bug issue type in JIRA. Populate via:
   - Workflow post-function: auto-inherit L3/L4 ID from the linked test case when a defect is raised from a test execution
   - Bulk update: for existing 5,337 defects, map via the `external_id` or `assigned_team`/`subteam` fields as proxies

3. **Automation (long-term):** Modify `fetch_jira_data.py` to:
   - Cross-reference defects with linked test cases (JIRA issue links)
   - Inherit the L3/L4 ID from the linked test case to the defect record in `jira_cache.json`
   - This enables capability-level defect reporting without JIRA schema changes

---

## 3. Test Execution Status

| Status | Count | % |
|--------|-------|---|
| Pass | 4,314 | 91.8% |
| Not Applicable | 258 | 5.5% |
| Not Executed | 78 | 1.7% |
| Fail | 41 | 0.9% |
| Blocked | 9 | 0.2% |

**Program Pass Rate:** 91.8% (below 95% GO threshold)

### Active Defect Summary

| Severity | Open | Total | Open % |
|----------|------|-------|--------|
| Critical | 25 | 338 | 7.4% |
| High | 154 | 2,163 | 7.1% |
| Medium | 113 | 2,443 | 4.6% |
| Low | 22 | 393 | 5.6% |
| **Total** | **314** | **5,337** | **5.9%** |

**Go/No-Go:** NO-GO (pass rate 91.8% < 95%, 25 critical defects open)

---

## 4. Dashboard Filter Effectiveness

### Current State (after this fix)

| Pillar | Tower Chip Filtering | Release Filtering | KPI Updates | Status |
|--------|---------------------|-------------------|-------------|--------|
| Architecture | ✅ Client-side | N/A | ✅ Dynamic | Working |
| Development | ✅ Client-side | ✅ Drop-down | ✅ Dynamic | Working |
| Testing | ✅ Client-side (NEW) | N/A | ✅ Dynamic (NEW) | **Fixed** |

### What Changed
- Testing charts now filter from raw test case/defect arrays (`RAW_TESTS`, `RAW_DEFECTS`)
- KPIs (pass rate, total defects, critical open, Go/No-Go) recalculate when tower chips are toggled
- Defect aging computed client-side from `created` dates
- "Open Defects by Tower" chart now uses horizontal bars (better readability)

### Remaining Limitations
- Testing pillar does not support release-based filtering (test cases in JIRA cache don't have a reliable release field for R1/R2/R3 segmentation)
- Towers with zero test cases (OTC-IP, FTS-IP, PTP) will show empty testing charts when selected individually

---

## 5. Daily CI Data Refresh

### Current Configuration
- **Workflow:** `.github/workflows/data-refresh.yml`
- **Schedule:** Mon–Fri at 06:00 UTC
- **Secrets Required:** `JIRA_PAT`, `JIRA_BASE_URL`, `SMARTSHEET_TOKEN`

### Gap: CI Cannot Reach Internal JIRA
GitHub Actions runners cannot reach `jira.devtools.intel.com` (Intel internal network). The JIRA fetch step fails silently with `|| echo "::warning::JIRA fetch failed (non-fatal)"`.

### Options for Daily JIRA Refresh

| Option | Effort | Reliability | Recommendation |
|--------|--------|-------------|----------------|
| **A. Self-hosted runner** on Intel network | High (IT approval) | ✅ High | Best long-term |
| **B. Manual refresh + commit** | Low | ⚠️ Manual | Current workaround |
| **C. Local scheduled task** (Windows Task Scheduler) | Medium | ✅ Reliable | **Recommended short-term** |
| **D. GitHub Actions + VPN tunnel** | High (security review) | ✅ High | Requires IT approval |

### Recommended: Option C — Local Scheduled Task

Create a Windows scheduled task that:
1. Runs `python scripts/fetch_jira_data.py` daily at 06:00 local time
2. Commits and pushes updated `data/jira/jira_cache.json` to GitHub
3. This triggers the existing `data-refresh.yml` → `deploy-pages.yml` chain

Script path: `scripts/local_jira_refresh.ps1` (to be created)

---

## 6. Action Items

| # | Action | Owner | Priority | Target |
|---|--------|-------|----------|--------|
| 1 | Populate L3/L4 IDs for FTS-IF, E2E, OTC-IF test cases | Tower Leads | High | 2 weeks |
| 2 | Add L3/L4 custom field to Bug issue type in JIRA | JIRA Admin | Medium | 4 weeks |
| 3 | Create test cases for OTC-IP, FTS-IP, PTP towers | Tower Leads | High | 2 weeks |
| 4 | Map SCP unmapped TCs to FTS-IF/FTS-IP in tower registry | EA (Sajiv) | Low | 1 week |
| 5 | Set up local scheduled task for daily JIRA refresh | EA (Sajiv) | Medium | 1 week |
| 6 | Cross-reference defects ↔ test cases for L3/L4 inheritance | EA (Sajiv) | Medium | 3 weeks |

---

*Generated from `data/jira/jira_cache.json` analysis — 4,700 test cases, 5,337 defects*
