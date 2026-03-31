# FPR Tower — BPMN Capability-Level Mapping Integration Guide

**Date:** March 31, 2026  
**Tower:** FPR — Finance Plan to Report  
**Purpose:** Demonstrate how BPMN capability-level mapping should be integrated across Smartsheet Object Tracker, JIRA, and Zephyr Scale to enable end-to-end progress tracking. This serves as the reference model for all 8 towers.

---

## Overview

The IAO Architecture Portal organizes all delivery artifacts by **Capability ID** (from Signavio BPMN). Each capability belongs to an **L1 Process Group** (sub-tower), which belongs to a **Tower**. For accurate tracking, every RICEFW object (Smartsheet), defect (JIRA), and test case (Zephyr Scale) must be tagged to its corresponding sub-tower and capability.

**Hierarchy:**

```
Tower (FPR)
  └── L1 Process Group / Sub-Tower (3.5 FPR - Fixed Assets)
        └── Capability (DC-040 — Perform Fixed Asset Accounting)
              └── RICEFW Objects (FPRI0195_IF, FPRC0195_IP, ...)
              └── Defects (IAODTM-12345, ...)
              └── Test Cases (IAODTM-T-001, ...)
```

---

## FPR Capability → Sub-Tower → Data Cross-Reference

This table shows the complete mapping for all 19 FPR capabilities, along with the current state of RICEFW objects and JIRA defects linked through the sub-tower.

### DC — Manage Accounting and Control Data (9 capabilities)

| Capability ID | Capability Name | Sub-Tower (Smartsheet / JIRA) | RICEFW Objects | Status | R3 Defects | Open | Critical |
|:---:|---|---|:---:|---|:---:|:---:|:---:|
| DC-010 | Perform Transaction Processing | 3.1 FPR - GL Close & Consolidate | 81 | 95% complete | 24¹ | 1 | 0 |
| DC-020 | Manage the General Ledger | 3.1 FPR - GL Close & Consolidate | 81 | 95% complete | 24¹ | 1 | 0 |
| DC-030 | Perform Closing | 3.1 FPR - GL Close & Consolidate | 81 | 95% complete | 24¹ | 1 | 0 |
| DC-040 | Perform Fixed Asset Accounting | 3.5 FPR - Fixed Assets | 40 | 100% complete | 34 | 16 | 0 |
| DC-050 | Project Accounting | 3.11 FPR - Project Accounting | 86 | 95% complete | 46 | 9 | 0 |
| DC-060 | Manage Taxes | 3.2 FPR - Tax | 20 | 75% complete | 5 | 1 | 1 |
| DC-100 | Revenue Recognition | 3.3 FPR - Revenue Recognition & Reporting | 14 | 100% complete | 0 | 0 | 0 |
| DC-110 | Manage Intercompany | 3.4 FPR - Intercompany | 15 | 100% complete | 3 | 1 | 0 |
| DC-120 | Maintenance & Management Accounting | 3.8 FPR - Financial Planning & Analysis | 14 | 100% complete | 8 | 0 | 0 |

### DS — Provide Decision Support (3 capabilities)

| Capability ID | Capability Name | Sub-Tower (Smartsheet / JIRA) | RICEFW Objects | Status | R3 Defects | Open | Critical |
|:---:|---|---|:---:|---|:---:|:---:|:---:|
| DS-010 | Perform Overhead Accounting and Allocation | 3.8 FPR - Financial Planning & Analysis | 14 | 100% complete | 8 | 0 | 0 |
| DS-020 | Perform Product Costing and Inventory Valuation | 3.7 FPR - Product Costing and Inventory Valuation | 27 | 89% complete | 27 | 1 | 6 |
| DS-030 | Perform Customer & Product Profitability Analysis | 3.6 FPR - Cost and Profitability Analysis | 3 | 100% complete | 1 | 0 | 0 |

### MB — Plan and Manage Business (2 capabilities)

| Capability ID | Capability Name | Sub-Tower (Smartsheet / JIRA) | RICEFW Objects | Status | R3 Defects | Open | Critical |
|:---:|---|---|:---:|---|:---:|:---:|:---:|
| MB-060 | Plan the Business | 3.8 FPR - Financial Planning & Analysis | 14 | 100% complete | 8 | 0 | 0 |
| MB-070 | Prepare Budgets | 3.8 FPR - Financial Planning & Analysis | 14 | 100% complete | 8 | 0 | 0 |

### MR — Manage Capital and Risk (4 capabilities)

| Capability ID | Capability Name | Sub-Tower (Smartsheet / JIRA) | RICEFW Objects | Status | R3 Defects | Open | Critical |
|:---:|---|---|:---:|---|:---:|:---:|:---:|
| MR-010 | Manage Liquidity | 3.9 FPR - Treasury and Cash Management | 42 | 98% complete | 5 | 0 | 0 |
| MR-020 | Manage Capital Structure | 3.9 FPR - Treasury and Cash Management | 42 | 98% complete | 5 | 0 | 0 |
| MR-030 | Manage Financial Risk | 3.9 FPR - Treasury and Cash Management | 42 | 98% complete | 5 | 0 | 0 |
| MR-070 | In-House Banking | 3.9 FPR - Treasury and Cash Management | 42 | 98% complete | 5 | 0 | 0 |

### OR — Receivables Management (1 capability)

| Capability ID | Capability Name | Sub-Tower (Smartsheet / JIRA) | RICEFW Objects | Status | R3 Defects | Open | Critical |
|:---:|---|---|:---:|---|:---:|:---:|:---:|
| OR-140 | Process Receipts | 3.10 FPR - Accounts Receivable & Collections | 24 | 100% complete | 8 | 3 | 2 |

> ¹ DC-010, DC-020, DC-030 share sub-tower `3.1 FPR - GL Close & Consolidate`. Defects show **0** in the system because JIRA uses an em dash (`–`) in `3.1 FPR – GL Close & Consolidate` while Smartsheet uses a hyphen (`-`). The 24 defects exist but are not linked due to this character mismatch.

---

## FPR Defects Not Currently Mapped to Capabilities

These JIRA defects are tagged to FPR tower but their `Assigned Sub Team` values don't match any Smartsheet sub-tower, so they can't be attributed to a specific capability.

| JIRA Assigned Sub Team | Defects | Open | Issue | Recommended Action |
|---|:---:|:---:|---|---|
| **10.10 Analytics - DARC** | 97 | 29 | Cross-functional team, not a delivery sub-tower | Reassign to the FPR sub-tower where the defect was found (e.g., 3.7 for costing, 3.1 for GL) |
| **10.3A Analytics - FPR** | 42 | 21 | Cross-functional team | Same — assign to specific FPR sub-tower |
| **3.1 FPR – GL Close & Consolidate** | 24 | 1 | Em dash (–) instead of hyphen (-) | Fix to `3.1 FPR - GL Close & Consolidate` |
| **3.12 FPR - ALL** | 10 | 4 | "ALL" catch-all, not a specific sub-tower | Assign to the specific sub-tower where defect applies |
| **11.1 Technology - ALL** | 4 | 2 | Infrastructure team | Reassign to the FPR sub-tower impacted |
| **10.1 Analytics - ALL** | 3 | 2 | Cross-functional catch-all | Reassign to specific sub-tower |
| **15.1 Cutover – Cutover All** | 3 | 0 | Cutover team | Reassign to the FPR sub-tower impacted |
| **11.2 Technology - ABAP** | 1 | 1 | Infrastructure team | Reassign to the sub-tower where the ABAP object belongs |
| **10.9 Analytics - Master Data** | 1 | 1 | Cross-functional | Reassign to specific sub-tower |
| **10.6 Analytics – FTS IF** | 1 | 1 | Wrong tower entirely | Reassign to FTS-IF or correct FPR sub-tower |
| **13.2 Security - Cyber/ App Security** | 1 | 0 | Security team | Reassign to the sub-tower impacted |
| **9A.1 Master Data - ALL** | 1 | 0 | MDM team | Reassign to FPR sub-tower or move to MDM tower |
| | **188** | **62** | | |

**Impact:** 188 of 325 FPR defects (58%) cannot be tracked at the capability level.

---

## What Needs to Change — Field-by-Field Guide

### Smartsheet Object Tracker

The Smartsheet Object Tracker is **already well-structured** for FPR. All 366 RICEFW objects have a valid `Sub-Tower Name` that maps to capabilities. The only enhancement needed:

| Field | Current State | Desired State | Action |
|---|---|---|---|
| `Tower Name` | ✅ All populated (e.g., `03. FPR`) | No change | — |
| `Sub-Tower Name` | ✅ All populated (11 unique values) | No change | — |
| **`Capability ID`** (NEW) | ❌ Does not exist | Add column with values like `DC-040` | **Add new column**, populate using the mapping table above |
| `Object ID` | ✅ Unique (e.g., `FPRI0195_IF`) | No change | — |

**Adding a `Capability ID` column** to Smartsheet would allow direct object-to-capability linkage without needing the sub-tower mapping bridge. Example values:

| Object ID | Sub-Tower Name | Capability ID (NEW) |
|---|---|---|
| FPRI0195_IF | 3.5 FPR - Fixed Assets | DC-040 |
| FPRW0367_IP | 3.11 FPR - Project Accounting | DC-050 |
| FPRE0887 | 3.7 FPR - Product Costing and Inventory Valuation | DS-020 |
| FPRC0195_IP | 3.1 FPR - GL Close & Consolidate | DC-010, DC-020, DC-030 |

> **Note:** Some sub-towers map to multiple capabilities (e.g., 3.8 maps to DC-120, DS-010, MB-060, MB-070). In these cases, the specific capability should be determined by the functional scope of the object.

### JIRA Defects

| Field | Current State | Desired State | Action |
|---|---|---|---|
| `Assigned Sub Team` | ⚠️ Inconsistent — em dashes, cross-functional teams, "ALL" catch-alls | Values must exactly match the 11 Smartsheet FPR sub-tower names (see list below) | **Standardize values**, fix character encoding |
| **`External ID`** | ⚠️ 30% populated, uses ALM numbers | Populate with Smartsheet `Object ID` (e.g., `FPRI0195_IF`) | **Change convention** — use Object Tracker IDs |
| **`Capability ID`** (custom field or label) | ❌ Does not exist | Add field with values like `DC-040` | **Request field** from JIRA admin, or use Labels |
| `Assigned Team` | ✅ Populated | No change | — |

**Canonical FPR Sub-Tower values** (JIRA `Assigned Sub Team` must use exactly these):

| # | Sub-Tower Name (canonical) | Common JIRA Mismatches |
|---|---|---|
| 1 | `3.1 FPR - GL Close & Consolidate` | `3.1 FPR – GL Close & Consolidate` (em dash) |
| 2 | `3.2 FPR - Tax` | — |
| 3 | `3.3 FPR - Revenue Recognition & Reporting` | — |
| 4 | `3.4 FPR - Intercompany` | — |
| 5 | `3.5 FPR - Fixed Assets` | — |
| 6 | `3.6 FPR - Cost and Profitability Analysis` | — |
| 7 | `3.7 FPR - Product Costing and Inventory Valuation` | — |
| 8 | `3.8 FPR - Financial Planning & Analysis` | — |
| 9 | `3.9 FPR - Treasury and Cash Management` | — |
| 10 | `3.10 FPR - Accounts Receivable & Collections` | — |
| 11 | `3.11 FPR - Project Accounting` | — |

**Values to retire/reassign:**

| Current JIRA Value | Defects | Action |
|---|:---:|---|
| `3.12 FPR - ALL` | 10 | Reassign to specific sub-tower (3.1–3.11) |
| `10.3A Analytics - FPR` | 42 | Reassign to specific FPR sub-tower |
| `10.10 Analytics - DARC` | 97 | Reassign to specific FPR sub-tower |
| `10.1 Analytics - ALL` | 3 | Reassign to specific FPR sub-tower |
| `10.9 Analytics - Master Data` | 1 | Reassign to specific sub-tower or MDM |
| `10.6 Analytics – FTS IF` | 1 | Move to FTS-IF tower |
| `11.x Technology - *` | 5 | Reassign to the impacted sub-tower |
| `13.2 Security - *` | 1 | Reassign to the impacted sub-tower |
| `15.1 Cutover – *` | 3 | Reassign to the impacted sub-tower |

### Zephyr Scale Test Cases

| Field | Current State | Desired State | Action |
|---|---|---|---|
| `Release` | ❌ All existing tests tagged R1 | Set to `R3` for Release 3 test cases | **Create R3 test cases** |
| `Sub Team` | ⚠️ Unknown for R3 | Must match the 11 canonical FPR sub-tower names | **Populate consistently** |
| `L3 ID` | ⚠️ Unknown for R3 | Set to Capability ID (e.g., `DC-040`) | **Populate for every test case** |
| `Team` | ⚠️ Unknown for R3 | Set to `FPR` | **Populate** |

---

## Example: Fully Mapped Capability — DC-040 (Fixed Assets)

This is what complete mapping looks like when all systems are aligned:

```
BPMN Capability: DC-040 — Perform Fixed Asset Accounting
L1 Process:      DC Manage Accounting and Control Data
Sub-Tower:       3.5 FPR - Fixed Assets
Tower:           FPR

SMARTSHEET OBJECT TRACKER:
┌────────────────┬──────────────┬──────────────────────────────────┬──────────────────┬────────────┐
│ Object ID      │ Type         │ Sub-Tower Name                   │ Capability ID    │ Status     │
├────────────────┼──────────────┼──────────────────────────────────┼──────────────────┼────────────┤
│ FPRI0195_IF    │ Interface    │ 3.5 FPR - Fixed Assets           │ DC-040           │ Complete   │
│ FPRI0195_IP    │ Interface    │ 3.5 FPR - Fixed Assets           │ DC-040           │ Complete   │
│ FPRC0195_IF    │ Conversion   │ 3.5 FPR - Fixed Assets           │ DC-040           │ Complete   │
│ ...            │ (40 total)   │                                  │                  │ 100% done  │
└────────────────┴──────────────┴──────────────────────────────────┴──────────────────┴────────────┘

JIRA DEFECTS:
┌────────────────┬────────────────────────────────────┬──────────────────────┬──────────────────┬──────────┐
│ Defect Key     │ Summary                            │ Assigned Sub Team    │ External ID      │ Severity │
├────────────────┼────────────────────────────────────┼──────────────────────┼──────────────────┼──────────┤
│ IAODTM-XXXX    │ Fixed asset depreciation calc...   │ 3.5 FPR - Fixed ...  │ FPRI0195_IF      │ High     │
│ IAODTM-YYYY    │ Asset transfer posting error       │ 3.5 FPR - Fixed ...  │ FPRC0195_IF      │ Medium   │
│ ...            │ (34 total, 16 open)                │                      │                  │          │
└────────────────┴────────────────────────────────────┴──────────────────────┴──────────────────┴──────────┘

ZEPHYR TEST CASES:
┌────────────────┬────────────────────────────────────┬─────────┬──────────────────────┬──────────┐
│ Test Key       │ Test Name                          │ Release │ Sub Team             │ L3 ID    │
├────────────────┼────────────────────────────────────┼─────────┼──────────────────────┼──────────┤
│ IAODTM-T-XXX   │ Verify asset depreciation run      │ R3      │ 3.5 FPR - Fixed ...  │ DC-040   │
│ IAODTM-T-YYY   │ Validate asset transfer posting    │ R3      │ 3.5 FPR - Fixed ...  │ DC-040   │
│ ...            │ (to be created)                    │         │                      │          │
└────────────────┴────────────────────────────────────┴─────────┴──────────────────────┴──────────┘
```

**Result:** The IAO Architecture Portal can automatically show for DC-040:
- 40 RICEFW objects (100% complete)
- 34 defects (16 open, 0 critical)
- Test execution status (when R3 tests are created)
- Links to: Systems Architecture Document, RICEFW Tracker, Testing Report

---

## Summary of Required Changes

| System | Change | Effort | Owner | Impact |
|---|---|---|---|---|
| **Smartsheet** | Add `Capability ID` column to Object Tracker | Low | PM / Smartsheet admin | Direct object→capability linkage |
| **JIRA** | Standardize `Assigned Sub Team` to canonical sub-tower names | Low | JIRA admin + Tower leads | Maps 188 unmapped FPR defects |
| **JIRA** | Fix em dash → hyphen in `3.1 FPR – GL Close & Consolidate` | Trivial | JIRA admin | Maps 24 defects immediately |
| **JIRA** | Retire `X.Y FPR - ALL` and cross-functional team tags | Medium | Tower leads | Forces specific sub-tower assignment |
| **JIRA** | Change `External ID` convention to use Smartsheet Object IDs | Medium | Testing leads | Enables defect→object traceability |
| **JIRA** | Add `Capability ID` custom field or label | Low | JIRA admin | Direct defect→capability linkage |
| **Zephyr** | Create R3 test cases with Release, Sub Team, L3 ID | High | Testing leads | Enables test execution tracking |

**Once these changes are made for FPR, the same pattern should be replicated across all 8 towers.**

---

## Appendix: FPR Sub-Tower → Capability Mapping Reference

This is the authoritative mapping used by the Architecture Portal. Tower leads for other towers need to provide equivalent mappings.

| Sub-Tower Name | Capability IDs | Capability Names |
|---|---|---|
| 3.1 FPR - GL Close & Consolidate | DC-010, DC-020, DC-030 | Transaction Processing, General Ledger, Closing |
| 3.2 FPR - Tax | DC-060 | Manage Taxes |
| 3.3 FPR - Revenue Recognition & Reporting | DC-100 | Revenue Recognition |
| 3.4 FPR - Intercompany | DC-110 | Manage Intercompany |
| 3.5 FPR - Fixed Assets | DC-040 | Perform Fixed Asset Accounting |
| 3.6 FPR - Cost and Profitability Analysis | DS-030 | Customer & Product Profitability Analysis |
| 3.7 FPR - Product Costing and Inventory Valuation | DS-020 | Product Costing and Inventory Valuation |
| 3.8 FPR - Financial Planning & Analysis | DC-120, DS-010, MB-060, MB-070 | Mgmt Accounting, Overhead Accounting, Plan Business, Budgets |
| 3.9 FPR - Treasury and Cash Management | MR-010, MR-020, MR-030, MR-070 | Liquidity, Capital Structure, Financial Risk, In-House Banking |
| 3.10 FPR - Accounts Receivable & Collections | OR-140 | Process Receipts |
| 3.11 FPR - Project Accounting | DC-050 | Project Accounting |

---

*Generated by IAO Architecture Pipeline — March 31, 2026*
