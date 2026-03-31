# IAO Architecture — Data Mapping Mismatch Assessment

**Date:** March 31, 2026  
**Prepared by:** IAO Architecture Office  
**Purpose:** Outline key data mapping gaps across JIRA, Smartsheet, and Zephyr Scale that prevent end-to-end project progress tracking, and recommend alignment actions for all project teams.

---

## Executive Summary

The IAO Architecture team has built an automated portal that tracks **RICEFW development objects** (Smartsheet), **defects** (JIRA), and **test cases** (Zephyr Scale) across all 8 towers and 189 capabilities. During integration, we identified **significant data mapping gaps** that prevent accurate tracking at the sub-tower and capability level. Only **32%** of defects can be mapped to a tower today, and **0%** of defects can be directly linked to their associated RICEFW development objects.

Resolving these gaps requires **consistent tagging** of every development object, defect, and test case by **Tower**, **Sub-Tower**, and **Capability**. This is a one-time data hygiene exercise that will unlock real-time, capability-level progress visibility for the entire program.

---

## Key Findings

### 1. JIRA Defect Tower Mapping — 68% Unmapped

| Tower | Defects | % of Total |
|-------|---------|-----------|
| **Unmapped** | **719** | **68%** |
| FPR | 325 | 31% |
| PTP | 8 | 1% |
| **Total** | **1,052** | 100% |

**Root cause:** The tower-mapping logic relies on the JIRA `Assigned Sub Team` field. While 100% of defects have a subteam value, many subteam values use naming conventions that don't match the 8 recognized tower codes:

- `7.10 FTS IF – PDF SMH` (259 defects) — uses em dash (–) instead of hyphen (-), and "PDF SMH" is not a recognized suffix
- `10.10 Analytics - DARC` (97 defects) — "Analytics" is not a recognized tower
- `17.2 B-App- OTC IP` (32 defects) — "B-App" prefix prevents tower extraction
- `15.1 Cutover – Cutover All` (12 defects) — cross-tower function, not assigned to a delivery tower
- `11.1 Technology - ALL` (12 defects) — infrastructure team, not a delivery tower

**Impact:** 719 of 1,052 R3 defects cannot be attributed to any tower, making tower-level defect dashboards incomplete.

### 2. Sub-Tower Name Inconsistency — 25 of 48 Match

The `Sub-Tower Name` in Smartsheet Object Tracker and the `Assigned Sub Team` in JIRA are the **primary shared key** between the two systems. However:

| Metric | Count |
|--------|-------|
| JIRA unique subteam values | 48 |
| Smartsheet unique Sub-Tower values | 55 |
| **Exact matches** | **25** |
| Only in JIRA | 23 |
| Only in Smartsheet | 30 |

**Character encoding mismatches (false negatives):**

| JIRA Value | Smartsheet Value | Issue |
|-----------|-----------------|-------|
| `3.1 FPR – GL Close & Consolidate` | `3.1 FPR - GL Close & Consolidate` | Em dash (–) vs hyphen (-) |
| `7.10 FTS IF – PDF SMH` | *(not present)* | Non-standard sub-tower |
| `8.8 FTS IP – PDF SMH` | *(not present)* | Non-standard sub-tower |

**JIRA-only subteam categories (not in Smartsheet):**

| Category | Subteam Values | Defects |
|----------|---------------|---------|
| Analytics | 10.1, 10.3A, 10.6, 10.9, 10.10 | 139+ |
| Technology | 11.1, 11.2, 11.3 | 12+ |
| Security | 13.1, 13.2 | — |
| Cutover | 15.1, 15.2 | 12+ |
| B-App | 17.1, 17.2, 17.5, 17.8 | 32+ |
| Misc | 32.1 OTC IF, ALL towers | 67+ |

These represent **cross-functional teams** (Analytics, Technology, Security, Cutover, B-App) that don't exist as sub-towers in the Object Tracker. Their defects need to be attributed to the correct delivery tower.

### 3. External ID / Object ID — 0% Direct Linkage

| Metric | Count |
|--------|-------|
| JIRA defects with External ID | 317 (30%) |
| Smartsheet Object IDs | 1,635 |
| **Direct matches** | **0** |

**The naming schemes are completely different:**

| System | Pattern | Examples |
|--------|---------|---------|
| **JIRA External ID** | ALM numbers, plain integers | `ALM 4971`, `ALM 6367`, `3684` |
| **Smartsheet Object ID** | Tower+Type+Sequence+BU | `FPRW0367_IP`, `FPRI0195_IF`, `PTPE0220` |

**Impact:** There is no way to link a specific JIRA defect to the RICEFW object it was found in. This means we cannot answer: *"How many defects are associated with object FPRI0195_IF?"*

### 4. Zephyr Scale Test Cases — 0 R3 Test Cases Exist

| Release | Test Cases | Status |
|---------|-----------|--------|
| R1 | All existing | Approved |
| R2 | — | — |
| **R3** | **0** | **Not created** |

All existing test cases in Zephyr Scale are tagged as R1. No R3 test cases have been created yet, which means:
- Test execution progress cannot be tracked per tower or capability
- There is no visibility into FUT (Functional Unit Testing) readiness for Release 3

### 5. Sub-Tower → Capability Mapping — 69% Unmapped

| Status | Sub-Towers | Details |
|--------|-----------|---------|
| Fully mapped | 11 | FPR tower only |
| Empty (scaffolded) | 24 | OTC-IF, OTC-IP, PTP, FTS-IF, FTS-IP, MDM, E2E |
| **Total** | **35** | |

Only the **FPR tower** has complete sub-tower-to-capability mapping (11 sub-towers → 19 capabilities). The remaining 7 towers have sub-tower entries but no capability assignments.

---

## Current State vs. Desired State

```
CURRENT STATE                                DESIRED STATE
─────────────                                ─────────────
JIRA Defect ──(subteam)──→ ???               JIRA Defect ──(subteam)──→ Tower ──→ Sub-Tower ──→ Capability
                                                          ──(ext_id)───→ RICEFW Object ID
Smartsheet ──(Sub-Tower)──→ Tower (OK)       Smartsheet ──(Sub-Tower)──→ Tower ──→ Capability (all mapped)
Zephyr TC ──(no R3 data)──→ ???              Zephyr TC ──(release=R3)──→ Tower ──→ Sub-Tower ──→ Capability
```

---

## Recommendations

### Priority 1: Standardize Sub-Tower Names (All Teams)

**Action:** Align JIRA `Assigned Sub Team` values to match Smartsheet `Sub-Tower Name` exactly.

- Fix em dash (–) vs hyphen (-) inconsistencies
- Map cross-functional teams (Analytics, Technology, Security, Cutover, B-App) to their delivery tower
- Remove "ALL" suffix sub-teams — assign to specific sub-towers
- Ensure every JIRA defect has a valid sub-tower value matching the Smartsheet master list

**Owner:** Tower leads + JIRA administrators  
**Effort:** Low (field value standardization)  
**Impact:** Immediately maps 719 unmapped defects to towers

### Priority 2: Link JIRA External ID to Smartsheet Object ID (Testing Teams)

**Action:** When logging a defect against a RICEFW object, populate the JIRA `External ID` field with the **Smartsheet Object ID** (e.g., `FPRI0195_IF`), not the ALM number.

- Update defect logging guidance to reference Object Tracker IDs
- Backfill existing 317 External IDs where the corresponding Object ID is known
- Consider making External ID a required field for R3 defects

**Owner:** Testing leads  
**Effort:** Medium (process change + backfill)  
**Impact:** Enables defect-to-object traceability

### Priority 3: Create R3 Test Cases in Zephyr Scale (Testing Teams)

**Action:** Create test cases for Release 3 in Zephyr Scale with proper tagging:

- Set `Release` = `R3` (not `Release 3` — verify Zephyr field format)
- Set `Sub Team` to match the standardized Smartsheet sub-tower name
- Set `L3 ID` to the capability ID where applicable (e.g., `DC-040`)

**Owner:** Testing leads per tower  
**Effort:** High (test case creation)  
**Impact:** Enables test execution tracking per tower and capability

### Priority 4: Complete Sub-Tower → Capability Mapping (Architecture + Tower Leads)

**Action:** For each tower, map every sub-tower name to one or more Signavio capability IDs in `config/subtower_capability_map.json`.

| Tower | Sub-Towers | Status | Owner |
|-------|-----------|--------|-------|
| FPR | 11 | ✅ Complete | — |
| OTC-IF | 5 | ❌ Empty | OTC-IF lead |
| OTC-IP | 4 | ❌ Empty | OTC-IP lead |
| PTP | 2 | ❌ Empty | PTP lead |
| FTS-IF | 5 | ❌ Empty | FTS-IF lead |
| FTS-IP | 4 | ❌ Empty | FTS-IP lead |
| MDM | 3 | ❌ Empty | MDM lead |
| E2E | 0 | ❌ Empty | E2E lead |

**Owner:** Tower leads + Architecture team  
**Effort:** Low (one-time mapping exercise)  
**Impact:** Enables capability-level dashboards for all towers

---

## What Gets Unlocked

Once these 4 actions are completed, the IAO Architecture Portal will automatically provide:

1. **Tower-level dashboards** — RICEFW progress, defect counts, test execution status per tower
2. **Sub-tower summary badges** — At-a-glance RICEFW complete/pending + defect critical/open per L1 process group
3. **Capability landing pages** — Per-capability view with links to SAD, RICEFW Tracker, and Testing Report, plus defect and RICEFW object detail
4. **Defect-to-object traceability** — Which RICEFW objects have the most defects, which are clean
5. **Test execution tracking** — R3 test case pass/fail/blocked rates per capability
6. **Release readiness indicators** — Go/No-Go signals based on critical open defects and test pass rates

All of this is automated and refreshes with every pipeline run — **no manual report assembly required**.

---

## Data Sources & Systems

| System | Data | Current Records | Key Field |
|--------|------|----------------|-----------|
| **JIRA** (jira.devtools.intel.com) | R3 defects | 1,052 | `Assigned Sub Team` |
| **Smartsheet** (Object Tracker) | RICEFW objects | 1,635 | `Sub-Tower Name` |
| **Zephyr Scale** (JIRA plugin) | Test cases | 0 (R3) | `Release`, `Sub Team` |
| **Signavio** (BIC) | Capabilities | 189 | Capability ID (e.g., DC-040) |

---

## Appendix: Sub-Tower Master List

The following 55 sub-tower names from the Smartsheet Object Tracker serve as the **canonical reference**. JIRA subteam values and Zephyr test case tags should match these exactly.

<details>
<summary>View complete Sub-Tower list (57 entries)</summary>

| # | Sub-Tower Name | Tower |
|---|---------------|-------|
| 1 | 3.1 FPR - GL Close & Consolidate | FPR |
| 2 | 3.10 FPR - Accounts Receivable & Collections | FPR |
| 3 | 3.11 FPR - Project Accounting | FPR |
| 4 | 3.2 FPR - Tax | FPR |
| 5 | 3.3 FPR - Revenue Recognition & Reporting | FPR |
| 6 | 3.4 FPR - Intercompany | FPR |
| 7 | 3.5 FPR - Fixed Assets | FPR |
| 8 | 3.6 FPR - Cost and Profitability Analysis | FPR |
| 9 | 3.7 FPR - Product Costing and Inventory Valuation | FPR |
| 10 | 3.8 FPR - Financial Planning & Analysis | FPR |
| 11 | 3.9 FPR - Treasury and Cash Management | FPR |
| 12 | 4.10 OTC IF - Logistics Management Outbound | OTC-IF |
| 13 | 4.11 OTC IF - Order Management | OTC-IF |
| 14 | 4.12 OTC IF - TM | OTC-IF |
| 15 | 4.3 OTC IF - Billing and Rebates | OTC-IF |
| 16 | 4.6 OTC IF - Credit and Collections | OTC-IF |
| 17 | 4.8 OTC IF - EWM | OTC-IF |
| 18 | 4.9 OTC IF - GTS | OTC-IF |
| 19 | 5.1 OTC IP - ALL | OTC-IP |
| 20 | 5.10 OTC IP - Logistics Management Outbound | OTC-IP |
| 21 | 5.11 OTC IP - Order Management | OTC-IP |
| 22 | 5.12 OTC IP - TM | OTC-IP |
| 23 | 5.13 OTC IP - Returns (Logistics Management) | OTC-IP |
| 24 | 5.3 OTC IP - Billing and Rebates | OTC-IP |
| 25 | 5.4 OTC IP - Returns | OTC-IP |
| 26 | 5.6 OTC IP - Credit and Collections | OTC-IP |
| 27 | 5.8 OTC IP - EWM | OTC-IP |
| 28 | 5.9 OTC IP - GTS | OTC-IP |
| 29 | 6.2 PTP - Procurement | PTP |
| 30 | 6.3 PTP - EWM | PTP |
| 31 | 6.4 PTP - Logistics Management Inbound | PTP |
| 32 | 6.5 PTP - TM | PTP |
| 33 | 6.6 PTP - GTS | PTP |
| 34 | 6.7 PTP - Enable Payments | PTP |
| 35 | 6.8 PTP - QM | PTP |
| 36 | 7.1 FTS IF - ALL | FTS-IF |
| 37 | 7.4 FTS IF - EWM | FTS-IF |
| 38 | 7.5 FTS IF - TM | FTS-IF |
| 39 | 7.6 FTS IF - Logistics & Inventory Management | FTS-IF |
| 40 | 7.7 FTS IF - Manufacturing & MES Integration | FTS-IF |
| 41 | 7.8 FTS IF - MRP & Planning Integration | FTS-IF |
| 42 | 7.9 FTS IF - Plant Maintenance | FTS-IF |
| 43 | 8.1 FTS IP - ALL | FTS-IP |
| 44 | 8.4 FTS IP - Logistics & Inventory Management | FTS-IP |
| 45 | 8.5 FTS IP - Manufacturing | FTS-IP |
| 46 | 8.6 FTS IP - MRP & Planning Integration | FTS-IP |
| 47 | 8.7 FTS IP - TM | FTS-IP |
| 48 | 9A.1 Master Data - ALL | MDM |
| 49 | 9A.2 Master Data - BOM | MDM |
| 50 | 9A.3 Master Data - Customer | MDM |
| 51 | 9A.4 Master Data - Vendor | MDM |
| 52 | 9A.5 Master Data - Finance | MDM |
| 53 | 9A.6 Master Data - Material | MDM |
| 54 | 9A.7 Master Data - Reference | MDM |
| 55 | 9A.8 Master Data - HR Mini Master | MDM |

**Note:** Sub-towers ending in "- ALL" (e.g., `7.1 FTS IF - ALL`) should be avoided. Objects and defects should be assigned to their specific sub-tower for accurate tracking.

</details>

---

*This assessment was generated by the IAO Architecture Pipeline using live data from JIRA, Smartsheet, and Zephyr Scale APIs. Statistics are as of March 31, 2026.*
