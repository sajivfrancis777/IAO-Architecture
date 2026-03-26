# IAO Notebook Pipeline — Build Readiness Assessment

**Date**: 2026-03-25  
**Status**: **GO** — All critical inputs exist for 135+ capabilities across 7 towers  
**Scope**: Systems Architecture Documents (Tier 1) + Process Documentation  

---

## 1. Inventory Summary

### 1.1 Towers & Capabilities

| Tower | Capabilities | Flow CSVs | BPMNs | tower.yaml | SAD Output Ready |
|-------|-------------|-----------|-------|------------|------------------|
| **FPR** | 19 | 41 | 719 | Yes | **YES** |
| **FTS-IF** | 22 | 44 | 213 | Yes | **YES** |
| **FTS-IP** | 14 | 28 | 90 | Yes | **YES** |
| **MDM** | 4 | 8 | 221 | Yes | **YES** |
| **OTC-IF** | 26 | 52 | 268 | Yes | **YES** |
| **OTC-IP** | 35 | 70 | 328 | Yes | **YES** |
| **PTP** | 15 | 30 | 226 | Yes | **YES** |
| **E2E** | 51 | 0 | 538 | Yes | Process Docs Only |
| **TOTALS** | **186** | **273** | **2,603** | **8/8** | **135 caps + 51 E2E** |

> **Note**: Each capability has a `CurrentFlows.csv` + `FutureFlows.csv` pair (and often release-scoped variants like `R3_CurrentFlows.csv` / `R3_FutureFlows.csv`). E2E capabilities contain only BPMN files — they document cross-tower end-to-end processes, not system architectures.

### 1.2 File Totals

| Type | Count | Purpose |
|------|-------|---------|
| `.bpmn` | 2,603 | Source process models (Signavio export) |
| `.csv` | 273 | Current/Future flow definitions (25-col schema) |
| `.yaml` | 8 | Tower config (capability registry) |
| `.md` | 608 | Previously generated outputs (validation baseline) |
| `.pdf` | 3 | PDF renders of architecture docs |
| **Total files** | **4,759** | Full towers dataset |

### 1.3 Supplemental Data Sources

| Source | Location | Status |
|--------|----------|--------|
| **S4 R3 Object Tracker** | `data/smartsheet/object_trackers/s4_r3_object_tracker.csv` | 1,635 × 212 cols — **Ready** |
| **Boundary App Tracker** | `data/smartsheet/boundary_apps/boundary_app_tracker.csv` | 821 × 18 cols — **Ready** |
| **WRICEF Column Definitions** | `data/smartsheet/wricef_columns.json` | 110 cols — **Ready** |
| **IAPM All Solutions** | `C:\Users\sajivfra\Documents\IAO-Architecture\IAPM_All_Solutions.csv` | 19 MB — **Needs copy to `data/iapm/`** |
| **IAPM Console Export Script** | `C:\Users\sajivfra\Documents\IAO-Architecture\iapm-console-export.js` | Reference — for future API mode |

---

## 2. Template Reverse-Engineering (DS-020 Reference)

The existing `DS-020-Architecture.md` (41 KB) in `towers/FPR/DS Provide Decision Support/DS-020/output/docs/systems-architecture/` provides the ground-truth template. Structure:

| Section | Content | Data-Driven? | Source |
|---------|---------|:------------:|--------|
| **Cover Page** | Tower, Capability ID/Name, Version | Yes | `tower.yaml` |
| **TOC** | 11 numbered sections with anchors | Yes | Auto-generated |
| **§1 Executive Summary** | System count, change summary stats | **Auto** | Computed from CSVs |
| **§2 Business Context** | PCF classification, drivers, criteria | Semi | PCF lookup + manual stubs |
| **§3 Current Architecture** | Mermaid flowchart + narrative table | **Auto** | `CurrentFlows.csv` + IAPM lookup |
| **§4 Future Architecture** | Mermaid flowchart + narrative table | **Auto** | `FutureFlows.csv` + IAPM lookup |
| **§5 Change Impact** | NEW/REMOVED/MODIFIED diff table | **Auto** | Diff of §3 vs §4 flow chains |
| **§6 Component Overview** | System inventory with IAPM IDs & status | **Auto** | Union of systems + IAPM lookup |
| **§7 Key Data Flows** | Sequence diagrams for critical flows | Manual | Stub (architect fills) |
| **§8 NFRs** | Performance, availability, security | Manual | Stub |
| **§9 Roadmap** | Gantt chart, milestones | Manual | Stub |
| **§10 RAID** | Risks, assumptions, dependencies | Manual | Stub |
| **§11 Recommendations** | Next steps | Manual | Stub |

**Key observations from DS-020 output:**

1. **IAPM URLs are already in the flow CSVs** (columns 20 `Src IAPM URL` and 25 `Tgt IAPM URL`) — no separate IAPM API call needed for click links
2. **Mermaid `click` events** use `href` with `_blank` target and require `securityLevel: 'loose'`
3. **System status annotations** (Deployed/Developing/EOL/N/A) appear in node labels — sourced from IAPM lookup
4. **Subgraph grouping** uses the `Source Lane` / `Target Lane` CSV columns (system category)
5. **CSS classDefs** color nodes by status: green=deployed, blue=developing, red=EOL, gray=no match
6. **`[^ Back to TOC](#table-of-contents)`** appears after every section — exactly as you requested
7. **`<div style="page-break-before: always;"></div>`** between sections for PDF pagination
8. **View labels** ("ICOST" / "S/4 HANA") come from `tower.yaml` `views.current.label` / `views.future.label`

---

## 3. Document Section → Input Mapping (Readiness Matrix)

### 3.1 Systems Architecture Document (Tier 1 — per capability)

| Section | Required Input | Available? | Gap / Action |
|---------|---------------|:----------:|-------------|
| Cover page | tower name, cap ID, cap name | **GREEN** | From `tower.yaml` |
| §1 Exec Summary | system counts, change stats | **GREEN** | Computed from CSVs |
| §2.1 Classification | tower, L1 process, L2 capability | **GREEN** | From `tower.yaml` |
| §2.2 Business Drivers | Business context per capability | **YELLOW** | Stub — architect fills |
| §2.3 Success Criteria | KPIs | **YELLOW** | Stub — architect fills |
| §3 Current Architecture diagram | `CurrentFlows.csv` | **GREEN** | 135 caps have these |
| §3 IAPM click links | `Src IAPM URL`, `Tgt IAPM URL` cols | **GREEN** | Already in CSV cols 20 & 25 |
| §3 System status labels | IAPM status per system | **YELLOW** | Need `IAPM_All_Solutions.csv` lookup |
| §3 Flow narrative table | All CSV columns | **GREEN** | Direct CSV parse |
| §4 Future Architecture | `FutureFlows.csv` | **GREEN** | Same 135 caps |
| §5 Change Impact | Current vs Future diff | **GREEN** | Computed |
| §6 System Inventory | Union of all systems + IAPM ID | **GREEN** | CSV columns + IAPM lookup |
| §7 Key Data Flows | Sequence diagrams | **YELLOW** | Stub — architect fills |
| §8-11 NFRs/Roadmap/RAID/Recs | Domain knowledge | **YELLOW** | Stubs — architect fills |

### 3.2 Process Documentation (per capability)

| Section | Required Input | Available? | Gap / Action |
|---------|---------------|:----------:|-------------|
| BPMN source files | `.bpmn` files per capability | **GREEN** | 2,603 files across all towers |
| PCF classification | APQC PCF L1/L2/L3 per process | **YELLOW** | Needs NB06 BPMN analysis |
| Mermaid process diagrams | BPMN → Mermaid conversion | **YELLOW** | Logic to build (NB06) |

### 3.3 Tower Summary (Tier 2 — per tower)

| Section | Required Input | Available? | Gap |
|---------|---------------|:----------:|-----|
| Capability roll-up | All Tier 1 docs for the tower | **GREEN** | Aggregation from Tier 1 outputs |
| Cross-capability flows | Shared system identification | **GREEN** | Computed from Tier 1 system inventories |
| Tower-level metrics | Aggregate system/flow counts | **GREEN** | Computed |

---

## 4. Critical Path & Blockers

### 4.1 Blockers (Must Fix Before Build)

| # | Blocker | Impact | Resolution | Effort |
|---|---------|--------|-----------|--------|
| 1 | **IAPM_All_Solutions.csv not in workspace** | System status lookup fails → all nodes show as "N/A" | Copy from `IAO-Architecture/` to `data/iapm/` | 1 min |

### 4.2 Non-Blockers (Can Proceed Without)

| # | Item | Impact | Workaround | When to Fix |
|---|------|--------|-----------|-------------|
| 1 | E2E has no flow CSVs | No systems architecture for 51 E2E capabilities | Generate process docs only (BPMN-derived) | Phase 2 — if E2E ever gets flow CSVs |
| 2 | §2.2/§2.3 business stubs empty | Drivers/criteria sections show placeholders | Already matches current DS-020 behavior | Architect fills post-generation |
| 3 | §7-§11 manual sections | Shows "To be completed" stubs | Already matches current DS-020 behavior | Architect fills post-generation |
| 4 | BPMN → Mermaid conversion | Process docs won't have diagrams initially | Build NB06 after NB07/NB08 | Iteration 2 |
| 5 | Enriched columns 26-47 | Extended schema not populated in POC | Use base 25-col CSVs (sufficient for SAD) | NB05 inference rules |

---

## 5. Go / No-Go Decision

### Decision: **GO**

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Flow CSV data exists | **PASS** | 273 CSVs across 135 capabilities (7 towers) |
| IAPM URLs embedded | **PASS** | Columns 20 & 25 of every flow CSV |
| Tower config exists | **PASS** | 8/8 `tower.yaml` files with capability registry |
| Reference template exists | **PASS** | DS-020-Architecture.md (41 KB) reverse-engineered |
| Existing outputs for validation | **PASS** | 608 generated .md files as ground truth |
| BPMN files exist | **PASS** | 2,603 `.bpmn` files |
| Smartsheet data converted | **PASS** | Object Tracker (1,635×212), Boundary Apps (821×18) |
| Extraction mode pivot designed | **PASS** | Mode C (manual) → Mode B (API) via config switch |

### What We Can Build NOW (Phase 1 — POC)

1. **NB07 → Systems Architecture doc generation** for 135 capabilities across 7 towers
   - Mermaid flowcharts with IAPM click links
   - Flow narrative tables
   - Change impact summaries
   - System inventories
   - TOC back-links + page breaks
2. **NB08 → SAP ↔ Smartsheet cross-reference mapping**
3. **Tier 2 tower summaries** (aggregation of Tier 1)

### What Requires Follow-Up (Phase 2)

1. **NB06 → BPMN → Mermaid process diagrams** (2,603 BPMNs)
2. **NB05 → Enrichment of columns 26-47** (extended schema)
3. **E2E tower architecture** (requires flow CSVs to be created)
4. **API mode pivot** (IAPM, Smartsheet, SAP OData → automated extraction)

---

## 6. Recommended Build Order

### Phase 1: Core Pipeline (Immediate Build)

| Step | Notebook/Module | What It Does | Inputs | Outputs |
|------|----------------|-------------|--------|---------|
| 0 | **Pre-req** | Copy `IAPM_All_Solutions.csv` to `data/iapm/` | IAO-Architecture ref | IAPM lookup table |
| 1 | **`config/towers.yaml`** | Master config: tower registry, paths, mode switch | `towers/*/tower.yaml` | Unified config |
| 2 | **`src/csv_parser.py`** | Parse CurrentFlows.csv / FutureFlows.csv | 25-col flow CSVs | Structured flow data |
| 3 | **`src/iapm_lookup.py`** | Build IAPM ID → status/URL lookup | `IAPM_All_Solutions.csv` | System status dict |
| 4 | **`src/mermaid_builder.py`** | Generate Mermaid flowcharts from flow data | Parsed flows + IAPM lookup | `.mmd` strings |
| 5 | **`src/diff_engine.py`** | Diff current vs future flow chains | Two parsed flow sets | Change impact table |
| 6 | **`templates/capability_architecture.md.j2`** | Jinja2 template (Tier 1) | All computed data | `.md` per capability |
| 7 | **`08_Gen_Systems_Architecture.ipynb`** | Orchestrate per-capability generation | All src modules + config | 135 architecture docs |
| 8 | **Validation** | Diff generated output vs existing DS-020 output | New vs reference `.md` | Confidence score |

### Phase 2: Enrichment & Process Docs

| Step | Module | What It Does |
|------|--------|-------------|
| 9 | `src/bpmn_parser.py` | Parse BPMN XML → activity/gateway/lane data |
| 10 | `src/bpmn_to_mermaid.py` | Convert parsed BPMN → Mermaid process diagrams |
| 11 | `06_Process_BPMN.ipynb` | Generate process documentation per capability |
| 12 | `05_Build_Lookup_Enrich.ipynb` | Populate columns 26-47 from Object Tracker + IAPM |

### Phase 3: Automation & Scaling

| Step | Module | What It Does |
|------|--------|-------------|
| 13 | `01_Extract_IAPM.ipynb` | IAPM API extraction (Playwright → Bearer → direct) |
| 14 | `03_Extract_Smartsheet.ipynb` | Smartsheet API extraction (Mode B) |
| 15 | `04_Extract_SAP_OData.ipynb` | SAP OData extraction (ADT + Gateway) |
| 16 | `09_Orchestrator.ipynb` | Full pipeline orchestration |

---

## 7. Flow CSV Schema (Reference)

The **existing 25-column** schema (from `towers/*/input/data/*.csv`):

| Col # | Column Name | Example (DS-020) |
|-------|-------------|-----------------|
| 1 | Flow Chain | MES Routes to S/4 |
| 2 | Hop # | 1 |
| 3 | Source System | MES 300 |
| 4 | Source Lane | Manufacturing Execution Systems |
| 5 | Target System | XEUS |
| 6 | Target Lane | Boundary Applications |
| 7 | Interface / Technology | Direct |
| 8 | Direction | -> |
| 9 | Frequency | Batch / On-demand |
| 10 | Data Description | MES Routes |
| 11 | Flow Purpose | Sends manufacturing route data |
| 12 | Notes / Corrections | |
| 13 | Process/System Owner | FTS - IF Forecast to Stock |
| 14 | Data Owner | Srivastava, Devendra |
| 15 | Applicable Scope | Intel Foundry |
| 16 | Src Web Address | |
| 17 | Src Business Owner | |
| 18 | Src Product Owner | |
| 19 | Src Product Owner Email | vivek.matkar@intel.com |
| 20 | Src IAPM URL | https://iapm.intel.com/#/app/41275 |
| 21 | Tgt Web Address | |
| 22 | Tgt Business Owner | Ashish Gupta |
| 23 | Tgt Product Owner | |
| 24 | Tgt Product Owner Email | robert.derber@intel.com |
| 25 | Tgt IAPM URL | https://iapm.intel.com/#/app/35612 |

**Key for Mermaid generation**: Cols 3-7 build the diagram nodes and edges; cols 4 & 6 define subgraph groupings; cols 20 & 25 provide IAPM click hrefs.

---

## 8. tower.yaml Schema (Reference)

```yaml
tower:
  shortcode: "FPR"
  name: "Finance Plan To Report"
  owner: ""
  contact: ""

capabilities:
  - id: DS-020
    name: "Perform Product Costing and Inventory Valuation"
    l1: "DS Provide Decision Support"
    status: active
    views:
      current:
        label: "ICOST"
        description: "Legacy and transitional product costing landscape..."
      future:
        label: "S/4 HANA"
        description: "Target S/4 HANA-based landscape..."

releases:
  - id: R3
    name: "Release 3"
    go_live: "2027-04-05"
```

> **Note**: Not all tower.yaml files may have views configured per capability. The default fallback is `current.label = "Current-State"`, `future.label = "Future-State"`.

---

## 9. Pre-Build Action Items

- [ ] Copy `IAPM_All_Solutions.csv` from `C:\Users\sajivfra\Documents\IAO-Architecture\` to `data/iapm/`
- [ ] Copy `iapm-console-export.js` to `reference/` for future API mode reference
- [ ] Create `config/towers.yaml` (master config consolidating all 8 tower.yaml files)
- [ ] Create `templates/capability_architecture.md.j2` (Jinja2 template based on DS-020)
- [ ] Create `src/csv_parser.py` (flow CSV parser)
- [ ] Create `src/iapm_lookup.py` (IAPM system status lookup)
- [ ] Create `src/mermaid_builder.py` (Mermaid flowchart generator)
- [ ] Create `src/diff_engine.py` (current vs future diff)
- [ ] Build `08_Gen_Systems_Architecture.ipynb` (orchestrator notebook)
- [ ] Validate against DS-020 reference output
