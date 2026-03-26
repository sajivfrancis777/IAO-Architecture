# IAO Pipeline — Process Flow, Folder Cleanup & Document Architecture

**Date**: 2025-03-24 | **Author**: Enterprise Architecture (Copilot-assisted)

---

## 1. Folder Cleanup Plan

### Current State — 35 Files, Mostly Disposable Probes

The workspace accumulated 25+ probe/extraction scripts during API discovery. These have served their purpose — the findings are documented in `API-Probe-Findings.md`. Time to archive and restructure.

### What to Keep vs. Archive

| Action | Files | Rationale |
|--------|-------|-----------|
| **KEEP** | `IAO-Architecture-Notebook-Build-Plan.md` | Master plan document |
| **KEEP** | `API-Probe-Findings.md` | Probe results reference |
| **KEEP** | `.env.example` | Credential template |
| **KEEP** | `api_probe.py` | Reusable multi-API probe (has --token flags) |
| **KEEP** | `probe_smartsheet_keys.py` | Hardcoded sheet ID reference (useful for NB03) |
| **KEEP** | `probe_data_analysis.py` | Local data schema analysis (useful for NB05) |
| **KEEP** | `smartsheet_access_audit.json` | Sheet access classification reference |
| **KEEP** | `smartsheet_folder_scan.json` | Folder tree reference |
| **ARCHIVE** | `probe_bic_*.py` (5 files) | BIC discovery complete — findings in API-Probe-Findings.md |
| **ARCHIVE** | `probe_iapm*.py` (4 files) | IAPM discovery complete — Playwright path decided |
| **ARCHIVE** | `probe_sap_odata*.py` (5 files) | SAP discovery complete — ADT + SSO pattern proven |
| **ARCHIVE** | `probe_smartsheet[2-5]*.py` (6 files) | Smartsheet discovery complete — MFA findings documented |
| **ARCHIVE** | `probe_smartsheet_folders.py` | Folder scanning done |
| **ARCHIVE** | `probe_smartsheet_jsmodel.py` | JS model analysis done |
| **ARCHIVE** | `probe_smartsheet_network.py` | Network interception done |
| **ARCHIVE** | `extract_smartsheet_*.py` (4 files) | Playwright extraction attempts (all failed) |
| **ARCHIVE** | `playwright_profile/` | Browser profile for Playwright (no longer needed) |
| **ARCHIVE** | `data/smartsheet/_debug/` | Debug captures from Playwright |

### Target Folder Structure (Post-Cleanup)

```
IAO-JPNotebookPython/
├── .env.example
├── .gitignore
├── README.md                              # NEW — project overview + quickstart
├── requirements.txt                       # NEW — pip dependencies
│
├── IAO-Architecture-Notebook-Build-Plan.md
├── IAO-Pipeline-ProcessFlow-and-Cleanup.md  # THIS FILE
├── API-Probe-Findings.md
│
├── config/                                # NEW — configuration files
│   ├── towers.yaml                        # Tower/capability registry
│   ├── api_endpoints.yaml                 # All API endpoint configs
│   └── sheet_ids.yaml                     # Smartsheet IDs (from probe_smartsheet_keys.py)
│
├── notebooks/                             # NEW — Jupyter notebooks (9)
│   ├── 01_Extract_IAPM.ipynb
│   ├── 02_Extract_BIC.ipynb
│   ├── 03_Extract_Smartsheet.ipynb
│   ├── 04_Extract_SAP_OData.ipynb
│   ├── 05_Build_Lookup_Enrich.ipynb
│   ├── 06_Process_BPMN.ipynb
│   ├── 07_Gen_Architecture_Docs.ipynb     # CHANGED — single gen notebook (see §2)
│   ├── 08_Cross_Reference_Mapping.ipynb   # NEW — SAP ↔ Smartsheet object mapping
│   └── 09_Orchestrator.ipynb
│
├── src/                                   # NEW — reusable Python modules
│   ├── __init__.py
│   ├── iapm_client.py
│   ├── bic_client.py
│   ├── smartsheet_client.py
│   ├── sap_odata_client.py                # ADT + OData dual-path client
│   ├── bpmn_parser.py
│   ├── bpmn_to_mermaid.py
│   ├── doc_generator.py
│   ├── flow_enricher.py
│   ├── lookup_builder.py
│   └── utils.py
│
├── templates/                             # NEW — Jinja2 document templates
│   ├── capability_architecture.md.j2      # SINGLE TEMPLATE (see §2 rationale)
│   ├── tower_summary.md.j2               # Per-tower roll-up
│   └── assets/
│       ├── cover_image.png
│       └── footer.css
│
├── data/                                  # Extracted data (git-ignored)
│   ├── iapm/
│   ├── bic/
│   ├── smartsheet/
│   │   ├── timelines/
│   │   ├── ricefw/
│   │   ├── raid/
│   │   └── object_trackers/
│   └── sap_odata/
│       ├── service_catalog.csv
│       ├── adt_objects.csv
│       ├── transport_requests.csv
│       └── _extraction_metadata.json
│
├── output/                                # Generated documents
│   └── towers/
│       ├── FPR/
│       │   └── {L1 Process Group}/
│       │       └── {Capability ID}/
│       │           ├── {Cap}_Architecture.md
│       │           └── {Cap}_Architecture.pdf
│       ├── OTC-IF/
│       ├── OTC-IP/
│       ├── FTS-IF/
│       ├── FTS-IP/
│       ├── PTP/
│       ├── MDM/
│       └── E2E/
│
├── reference/                             # Probe data worth keeping
│   ├── smartsheet_access_audit.json
│   ├── smartsheet_folder_scan.json
│   └── api_probe.py                       # Multi-API probe tool
│
└── _archive/                              # Disposable probe scripts (git-ignored)
    ├── probe_bic_auth.py
    ├── probe_bic_backend.py
    ├── probe_bic_detail.py
    ├── probe_bic_js.py
    ├── probe_bic_real_api.py
    ├── probe_iapm.py
    ├── probe_iapm_token.py
    ├── probe_iapm_token2.py
    ├── probe_iapm_v3.py
    ├── probe_sap_odata.py
    ├── probe_sap_odata2.py
    ├── probe_sap_odata3.py
    ├── probe_sap_odata4.py
    ├── probe_sap_odata5.py
    ├── probe_smartsheet.py
    ├── probe_smartsheet2.py
    ├── probe_smartsheet3.py
    ├── probe_smartsheet3b.py
    ├── probe_smartsheet4.py
    ├── probe_smartsheet5.py
    ├── probe_smartsheet_folders.py
    ├── probe_smartsheet_jsmodel.py
    ├── probe_smartsheet_network.py
    ├── extract_smartsheet_playwright.py
    ├── extract_smartsheet_v2.py
    ├── extract_smartsheet_v3.py
    ├── extract_smartsheet_v4.py
    └── playwright_profile/
```

### Cleanup Commands

```powershell
# Run from IAO-JPNotebookPython/
# 1. Create new directory structure
New-Item -ItemType Directory -Force -Path config, notebooks, src, templates, templates/assets
New-Item -ItemType Directory -Force -Path reference, _archive
New-Item -ItemType Directory -Force -Path data/iapm, data/bic, data/sap_odata
New-Item -ItemType Directory -Force -Path data/smartsheet/timelines, data/smartsheet/ricefw
New-Item -ItemType Directory -Force -Path data/smartsheet/raid, data/smartsheet/object_trackers

# 2. Move reference data
Move-Item smartsheet_access_audit.json reference/
Move-Item smartsheet_folder_scan.json reference/
Copy-Item api_probe.py reference/            # Keep a copy in reference
Move-Item probe_smartsheet_keys.py reference/ # Sheet ID reference
Move-Item probe_data_analysis.py reference/   # Schema analysis reference

# 3. Archive all probe/extraction scripts
Move-Item probe_bic_*.py _archive/
Move-Item probe_iapm*.py _archive/
Move-Item probe_sap_odata*.py _archive/
Move-Item probe_smartsheet*.py _archive/      # probe_smartsheet[2-5]*.py etc.
Move-Item extract_smartsheet_*.py _archive/
Move-Item api_probe.py _archive/              # Original stays in _archive
Move-Item playwright_profile _archive/

# 4. Move debug data to archive
Move-Item data/smartsheet/_debug _archive/

# 5. Update .gitignore
Add-Content .gitignore "`n_archive/`nplaywright_profile/`ndata/smartsheet/_debug/"
```

---

## 2. Document Architecture — Single vs. Separate BDAT Documents

### Recommendation: **Single Document per Capability** (with Summary + Detailed sections)

A single document is the right choice. Here's the analysis:

### Why NOT Separate B, D, A, T Documents

| Problem | Impact |
|---------|--------|
| **Document explosion** | 4 docs × ~15 capabilities × 8 towers = **480 documents** + 120 summaries = 600 files |
| **Cross-references break** | Data Architecture references Application components, Application references Technology platforms — these dependencies are natural and constant. Splitting them forces the reader to jump between 4 files. |
| **Automated generation complexity** | 4 templates, 4 generation passes, 4 naming conventions, 4 review cycles per capability |
| **Integration points invisible** | The value of TOGAF BDAT is seeing how Business drives Data, Data enables Applications, Applications run on Technology. Splitting them hides this traceability chain. |
| **Architect overhead** | Manual review of 4 docs per capability vs. 1 comprehensive doc. At 120 capabilities, this is unsustainable. |

### Why Single Document Works

| Benefit | Detail |
|---------|--------|
| **One source of truth** | Each capability has exactly ONE document. Find it, read it, done. |
| **BDAT traceability** | Business → Data → Application → Technology flows naturally within one document, with cross-references that are section links (not file links). |
| **Automated generation** | One Jinja2 template, one pass, one output file per capability. Clean pipeline. |
| **Review efficiency** | Architect reviews one doc per capability. Tower lead reviews one doc per capability. |
| **Pipeline simplicity** | NB07 generates one document per capability instead of 4. |
| **Version control** | Git diff on one file shows all changes. Not scattered across 4 files. |

### Document Structure — Two-Tier Architecture

The sweet spot is **two tiers**: a **per-capability document** (detailed BDAT) and a **per-tower roll-up** (summary across all capabilities in a tower).

```
output/towers/
├── FPR/
│   ├── FPR_Tower_Summary.md                   # TIER 2: Roll-up of all FPR capabilities
│   ├── FPR_Tower_Summary.pdf
│   │
│   └── DS Provide Decision Support/           # L1 Process Group
│       └── DS-020/                            # Capability ID
│           ├── DS-020_Architecture.md         # TIER 1: Full BDAT for this capability
│           └── DS-020_Architecture.pdf
│
├── OTC-IF/
│   ├── OTC-IF_Tower_Summary.md
│   └── {L1}/{Capability}/
│       └── {Cap}_Architecture.md
│  ... (same pattern for all 8 towers)
```

### Tier 1: Capability Architecture Document (Single BDAT)

Each capability gets ONE document with this structure:

```markdown
# {Capability Name} — Architecture Document
## Tower: {Tower} | Capability: {ID} | Version: {date}

## 1. Executive Summary
   - 1-page overview: what this capability does, key systems, current state, key risks
   - Auto-generated from data across all 4 source systems

## 2. Business Context & Objectives
   - Business goals this capability supports
   - Success metrics / KPIs
   - Stakeholder mapping (from Smartsheet)

## 3. Business Architecture (B)
   3.1 Process Inventory (from BIC/Signavio BPMN)
   3.2 Process Flow Diagrams (Mermaid — from BPMN conversion)
   3.3 Process Classification (APQC PCF L1/L2/L3)
   3.4 Roles & Swim Lanes
   3.5 Task Details & Process Statistics

## 4. Data Architecture (D)
   4.1 Data Entities & Relationships
   4.2 Data Flow Diagrams (from enriched Flows CSV)
   4.3 Data Ownership & Governance
   4.4 RICEFW Data Objects — Reports (R), Conversions (C)
   4.5 CDS Views (from SAP OData — Z*/Y* custom CDS)

## 5. Application Architecture (A)
   5.1 System Landscape (Mermaid — from IAPM + enriched flows)
   5.2 Component Overview (from IAPM lifecycle, status, owners)
   5.3 RICEFW Inventory — Interfaces (I), Enhancements (E), Forms (F), Workflows (W)
   5.4 Integration Patterns (from flow hop data)
   5.5 API & Interface Specifications

## 6. Technology Architecture (T)
   6.1 Platform & Infrastructure (from IAPM infra_type, hosting)
   6.2 SAP Development Objects (from SAP OData/ADT — classes, packages)
   6.3 Transport Status (from SAP OData — DEV/QAS/PRD deployment state)
   6.4 Security Architecture
   6.5 Non-Functional Requirements

## 7. Project Status
   7.1 Roadmap & Timeline (from Smartsheet timelines)
   7.2 RAID Log (from Smartsheet RAID sheets)
   7.3 Open Items & Dependencies

## Appendices
   A. Data Source Inventory (extraction timestamps, row counts)
   B. Change Log (auto-generated from Git commits)
```

### Tier 2: Tower Summary Document (Roll-Up)

Each tower gets ONE summary that aggregates across all its capabilities:

```markdown
# {Tower} — Architecture Summary
## IDM 2.0 Implementation | Version: {date}

## 1. Tower Overview
   - Scope, objectives, tower lead, team
   - Capability inventory (count, status breakdown)

## 2. Business Architecture Summary
   - Process inventory (total count, % modeled, APQC classification)
   - Key process flows (Mermaid — top 3-5 critical processes)

## 3. Data Architecture Summary
   - Data entity inventory across capabilities
   - Cross-capability data flows (the interesting integration view)
   - Data quality & governance summary

## 4. Application Architecture Summary
   - System landscape (all systems touched by this tower)
   - RICEFW summary (count by type: R/I/C/E/F/W)
   - Integration pattern summary

## 5. Technology Architecture Summary
   - Platform inventory
   - SAP development object count (custom classes, CDS views, packages)
   - Transport status summary (% in DEV, QAS, PRD)

## 6. Cross-Cutting Concerns
   - Inter-tower dependencies
   - Shared systems / integration points
   - Aggregate RAID summary

## 7. Recommendations & Next Steps
```

### Why This Two-Tier Approach

| Audience | Reads | Purpose |
|----------|-------|---------|
| **Capability architect** | Tier 1 (their capability) | Detailed design & review |
| **Tower lead** | Tier 2 (tower summary) + Tier 1 as needed | Tower-level decisions |
| **Program leadership** | Tier 2 (all tower summaries) | Portfolio view, risk management |
| **TRC/TWG governance** | Tier 2 (relevant tower) + Tier 1 for deep dives | Architecture review |

---

## 3. End-to-End Process Flow — POC to Production

### Design Principle: Extraction Mode Abstraction

Every extraction notebook implements a **mode switch** controlled by `config/api_endpoints.yaml`. The mode determines how data arrives — but the output contract is identical regardless of mode.

```yaml
# config/api_endpoints.yaml
extraction_mode: poc       # Options: poc | direct_api | hybrid

iapm:
  poc:
    mode: playwright       # Browser SSO extraction
    url: https://iapm.intel.com
  direct_api:
    mode: bearer           # MSAL service principal
    url: https://iapm.intel.com/internal/api
    client_id: d6696e64-1ce1-4938-8c3b-8d93bf125ed5
    tenant_id: 46c98d88-e344-4ed4-8496-4ed7712e255d

smartsheet:
  poc:
    mode: token            # Personal API token (6 sheets direct, rest CSV import)
    token_env: SMARTSHEET_TOKEN
  direct_api:
    mode: token            # Same token, but with MFA exemption (all sheets direct)
    token_env: SMARTSHEET_TOKEN

sap_odata:
  poc:
    mode: windows_sso      # SPNEGO/Kerberos via requests-negotiate-sspi
    gateway: https://sapptfci.intel.com:8300
    client: "210"
    extraction_path: adt   # ADT REST API (proven on sandbox)
  direct_api:
    mode: windows_sso      # Same auth — no password needed
    gateway: https://{idm_dev_host}:{port}   # TBD from SAP BASIS
    client: "{idm_dev_client}"
    extraction_path: adt+odata               # ADT + activated OData services

bic:
  poc:
    mode: local_bpmn       # Pre-exported BPMN manifest (3,337 models)
  direct_api:
    mode: signavio_api     # Signavio REST API when available
    url: https://editor.signavio.com/p/
```

### Pipeline Stages

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                    IAO ARCHITECTURE PIPELINE — PROCESS FLOW                          │
├──────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  STAGE 1: EXTRACT (Notebooks 01-04)                                                  │
│  ┌────────────────────────────────────────────────────────────────────────────────┐  │
│  │ Mode-aware extraction — same output contract regardless of POC or Direct API  │  │
│  │                                                                                │  │
│  │  NB01: IAPM         NB02: BIC/Signavio  NB03: Smartsheet   NB04: SAP OData   │  │
│  │  ┌───────────┐      ┌───────────┐       ┌───────────┐      ┌───────────┐     │  │
│  │  │ POC:      │      │ POC:      │       │ POC:      │      │ POC:      │     │  │
│  │  │ Playwright│      │ Local BPMN│       │ Token+CSV │      │ ADT+SSO   │     │  │
│  │  │ + SSO     │      │ manifest  │       │ import    │      │ (sandbox) │     │  │
│  │  ├───────────┤      ├───────────┤       ├───────────┤      ├───────────┤     │  │
│  │  │ PROD:     │      │ PROD:     │       │ PROD:     │      │ PROD:     │     │  │
│  │  │ MSAL      │      │ Signavio  │       │ Token     │      │ ADT+OData │     │  │
│  │  │ Bearer    │      │ REST API  │       │ (MFA-     │      │ (IDM DEV) │     │  │
│  │  │ token     │      │           │       │  exempt)  │      │           │     │  │
│  │  └─────┬─────┘      └─────┬─────┘       └─────┬─────┘      └─────┬─────┘     │  │
│  │        v                  v                    v                  v            │  │
│  │  data/iapm/         data/bic/            data/smartsheet/   data/sap_odata/   │  │
│  │  *.csv              *.bpmn               *.csv              *.csv             │  │
│  └────────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                              │
│                                       v                                              │
│  STAGE 2: ENRICH & MAP (Notebooks 05-06, 08)                                        │
│  ┌────────────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                                │  │
│  │  NB05: Build Lookups         NB06: BPMN to Mermaid   NB08: Cross-Reference    │  │
│  │  ┌──────────────────┐        ┌──────────────────┐     ┌──────────────────┐    │  │
│  │  │ IAPM Lookup table│        │ Parse BPMN XML   │     │ SAP objects      │    │  │
│  │  │ Enrich flows     │        │ Extract lanes,   │     │   matched to     │    │  │
│  │  │ Merge timelines  │        │   tasks, gateways│     │   Smartsheet     │    │  │
│  │  │ Merge SAP status │        │ Generate Mermaid │     │   object tracker │    │  │
│  │  │ Capability map   │        │   flowcharts     │     │   entries        │    │  │
│  │  └──────────────────┘        └──────────────────┘     └──────────────────┘    │  │
│  │       │                            │                        │                  │  │
│  │       v                            v                        v                  │  │
│  │  data/enriched/             data/mermaid/             data/xref/               │  │
│  │  *_enriched.csv             *.mmd                     sap_smartsheet_map.csv   │  │
│  └────────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                              │
│                                       v                                              │
│  STAGE 3: GENERATE (Notebook 07)                                                     │
│  ┌────────────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                                │  │
│  │  NB07: Generate Architecture Documents                                         │  │
│  │  ┌──────────────────────────────────────────────────────────────────────────┐  │  │
│  │  │ For each tower:                                                          │  │  │
│  │  │   For each capability in tower:                                          │  │  │
│  │  │     1. Load enriched data (flows, IAPM, RICEFW, RAID, SAP objects)       │  │  │
│  │  │     2. Load Mermaid diagrams (BPMN-converted + architect-authored)        │  │  │
│  │  │     3. Load SAP cross-reference mapping                                  │  │  │
│  │  │     4. Render capability_architecture.md.j2 template                     │  │  │
│  │  │        → Single BDAT document (B + D + A + T + Project Status)           │  │  │
│  │  │     5. Generate PDF via Pandoc/weasyprint                                │  │  │
│  │  │                                                                          │  │  │
│  │  │   Generate tower_summary.md.j2 template                                 │  │  │
│  │  │     → Tower roll-up (BDAT summary across all capabilities)               │  │  │
│  │  └──────────────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                                │  │
│  │  Output:                                                                       │  │
│  │  output/towers/{Tower}/{L1}/{Cap}/{Cap}_Architecture.md + .pdf                 │  │
│  │  output/towers/{Tower}/{Tower}_Tower_Summary.md + .pdf                         │  │
│  └────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. SAP OData ↔ Smartsheet Cross-Reference Mapping (Notebook 08)

This is the key synergy pipeline between SAP development objects and Smartsheet project tracking.

### The Problem

SAP development objects (ABAP classes, CDS views, function modules, enhancements) live in the SAP system. Project tracking of these objects (status, tower assignment, capability mapping, go-live readiness) lives in Smartsheet Object Trackers and Transport Trackers. Today these are manually correlated. We automate the join.

### Data Sources for Cross-Reference

| Source | What It Contains | Key Fields |
|--------|-----------------|------------|
| **SAP ADT** (NB04) | Custom objects: ZCL_*, ZCDS_*, Z_*, Y_* | Object name, type, package, creation date |
| **SAP Transport** (NB04) | Transport requests, status per environment | Transport ID, description, status (open/released/imported), target system |
| **Smartsheet Object Tracker** (NB03) | Per-tower Object Tracker sheets | Object name, type, tower, capability, status, owner, transport ID |
| **Smartsheet Transport Tracker** (NB03) | Per-tower Transport Tracker sheets | Transport ID, description, status, tower, approval |
| **Smartsheet RICEFW/WRICEF** (NB03) | Program-level RICEFW tracking | RICEFW ID, type (R/I/C/E/F/W), capability, status |

### Cross-Reference Algorithm

```python
# Pseudocode for Notebook 08
def cross_reference():
    # 1. Load SAP ADT objects (from NB04 output)
    sap_objects = pd.read_csv('data/sap_odata/adt_objects.csv')
    sap_transports = pd.read_csv('data/sap_odata/transport_requests.csv')

    # 2. Load Smartsheet Object Trackers (from NB03 output)
    ss_objects = pd.read_csv('data/smartsheet/object_trackers/all_towers.csv')
    ss_transports = pd.read_csv('data/smartsheet/object_trackers/transport_trackers.csv')
    ss_ricefw = pd.read_csv('data/smartsheet/ricefw/wricef.csv')

    # 3. Join SAP objects → Smartsheet Object Tracker
    #    Match on: object_name (exact) or object_name LIKE ss_object_name
    xref = sap_objects.merge(
        ss_objects,
        left_on='object_name',
        right_on='sap_object_name',
        how='outer',
        indicator=True
    )

    # 4. Classify match results
    xref['match_status'] = xref['_merge'].map({
        'both': 'MATCHED',           # Object in SAP AND Smartsheet
        'left_only': 'SAP_ONLY',     # In SAP but not tracked in Smartsheet
        'right_only': 'SS_ONLY'      # Tracked in Smartsheet but not found in SAP
    })

    # 5. Enrich with transport status
    xref = xref.merge(sap_transports, on='transport_id', how='left')

    # 6. Derive deployment status
    xref['deployment_status'] = derive_env_status(xref)
    # DEV only → "In Development"
    # DEV + QAS → "In Testing"
    # DEV + QAS + PRD → "Deployed"

    # 7. Map to tower/capability (from Smartsheet columns)
    # This gives us: object → tower → capability → BDAT section

    # 8. Output
    xref.to_csv('data/xref/sap_smartsheet_map.csv')
    return xref
```

### What This Enables in the Architecture Documents

| Match Status | Impact on SAD | Section |
|--------------|---------------|---------|
| **MATCHED** | Full traceability: SAP object → Smartsheet tracking → Tower → Capability | §6 T-Architecture: Dev objects, Transport status |
| **SAP_ONLY** | Flag untracked objects — governance gap (developed but not tracked) | §6 T-Architecture: "Untracked Objects" alert |
| **SS_ONLY** | Objects planned in Smartsheet but not yet created in SAP | §7 Project Status: "Planned but not developed" |

### Per-Tower Sheet IDs for Object Tracking

| Tower | Object Tracker ID | Transport Tracker ID |
|-------|-------------------|---------------------|
| FPR | (in smartsheet_access_audit.json) | (in smartsheet_access_audit.json) |
| OTC-IF | " | " |
| OTC-IP | " | " |
| FTS-IF | " | " |
| FTS-IP | " | " |
| PTP | " | " |
| MDM | " | " |

> **Note**: All Object/Transport Tracker sheets are MFA-blocked (error 1362). For POC, use Mode C (manual CSV export). When MFA exemption is granted (Mode D), these flow directly via API.

---

## 5. Output Folder Hierarchy — L0, L1, L2, L3

### Mapping APQC PCF Levels to Folder Structure

The L0/L1/L2/L3 levels align to the APQC PCF hierarchy and the EA governance phases:

| Level | APQC PCF | EA Governance | Folder | Document |
|-------|----------|---------------|--------|----------|
| **L0** | PCF Category (e.g., 9.0 Manage Financial Resources) | L0 Strategic Review | `output/towers/{Tower}/` | Tower Summary |
| **L1** | PCF Process Group (e.g., 9.2 Perform Revenue Accounting) | L1 Incremental Review | `output/towers/{Tower}/{L1 Process Group}/` | (folder only) |
| **L2** | PCF Process (e.g., 9.2.1 Process Customer Credit) | L2 Optimization Review | `.../{ L1}/{Capability ID}/` | Capability Architecture |
| **L3** | PCF Activity (e.g., 9.2.1.1 Receive and verify credit application) | — (task level) | — | Detail within L2 document |

### Example: FPR Tower

```
output/towers/FPR/
├── FPR_Tower_Summary.md                           # L0 — Tower-level BDAT summary
├── FPR_Tower_Summary.pdf
│
├── DS Provide Decision Support/                    # L1 — Process Group
│   ├── DS-010/                                    # L2 — Capability
│   │   ├── DS-010_Architecture.md
│   │   └── DS-010_Architecture.pdf
│   └── DS-020/
│       ├── DS-020_Architecture.md
│       └── DS-020_Architecture.pdf
│
├── GL General Ledger/                              # L1 — Process Group
│   ├── GL-010/
│   │   ├── GL-010_Architecture.md
│   │   └── GL-010_Architecture.pdf
│   └── GL-020/
│       └── ...
│
└── AR Accounts Receivable/                         # L1 — Process Group
    └── ...
```

### How the Pipeline Populates L0 Through L3

```
towers.yaml (config)          Notebook 07 (generation)          output/
┌──────────────────────┐      ┌──────────────────────────┐      ┌──────────────────┐
│ FPR:                 │      │ For each tower:          │      │ FPR/             │
│   tower_name: FPR    │─────>│   Generate tower summary │─────>│   FPR_Tower      │
│   capabilities:      │      │                          │      │   _Summary.md    │
│     - id: DS-020     │      │   For each capability:   │      │                  │
│       name: Provide  │─────>│     Generate cap arch doc│─────>│   DS .../DS-020/ │
│         Decision Supp│      │                          │      │   DS-020_Arch.md │
│       l1_group: DS   │      │                          │      │                  │
│       pcf_l1: "9.0"  │      │   L3 detail is WITHIN    │      │ (L3 = sections   │
│       pcf_l2: "9.2"  │      │   each L2 capability doc │      │  inside the doc) │
│       pcf_l3: "9.2.1"│      │                          │      │                  │
└──────────────────────┘      └──────────────────────────┘      └──────────────────┘
```

---

## 6. Pivot Strategy — POC to Production

### Phase 1: POC (Current)

| Source | Extraction Mode | Data Available |
|--------|----------------|----------------|
| IAPM | Local CSV (30K records from prior export) | Full portfolio, lifecycle, owners |
| BIC/Signavio | Local BPMN manifest (3,337 models) | Process flows for all towers |
| Smartsheet | Direct API (6 sheets) + Manual CSV (44 MFA-blocked) | RAID, RICEFW, partial object trackers |
| SAP OData | ADT on sandbox (Windows SSO) | Custom objects (not IDM-specific) |

**POC deliverable**: End-to-end pipeline producing Tier 1 + Tier 2 documents for 1-2 reference capabilities (e.g., FPR DS-020) using available data.

### Phase 2: Expanded Access (When Granted)

| Pivot | Config Change | Impact |
|-------|---------------|--------|
| IAPM → MSAL Bearer | `api_endpoints.yaml`: change mode from `playwright` to `bearer`, add client_secret | Live 30K-record refresh |
| Smartsheet → MFA exempt | Admin grants exemption | All 44 sheets flow via direct API |
| SAP → IDM DEV gateway | `api_endpoints.yaml`: change gateway URL + client | Real IDM custom objects + transports |
| BIC → Signavio API | `api_endpoints.yaml`: add Signavio API credentials | Live BPMN refresh |

**The pipeline code doesn't change** — only `config/api_endpoints.yaml` values change.

### Phase 3: Production (Scheduled)

| Feature | Implementation |
|---------|---------------|
| Scheduled runs | `config/scheduling.yaml` → cron or Airflow DAG |
| SharePoint sync | `src/sharepoint_sync.py` → push PDFs to SharePoint |
| Notification | Email/Teams webhook on generation completion |
| Diff detection | Compare current vs. prior extraction → flag changes |

---

## 7. Updated Notebook Inventory (9 Notebooks)

| # | Notebook | Stage | Purpose |
|---|----------|-------|---------|
| 01 | `01_Extract_IAPM.ipynb` | Extract | IAPM application portfolio |
| 02 | `02_Extract_BIC.ipynb` | Extract | BIC/Signavio BPMN process models |
| 03 | `03_Extract_Smartsheet.ipynb` | Extract | Object trackers, transports, RAID, RICEFW, timelines |
| 04 | `04_Extract_SAP_OData.ipynb` | Extract | SAP dev objects (ADT), transports, service catalog |
| 05 | `05_Build_Lookup_Enrich.ipynb` | Enrich | Build IAPM lookup, enrich flow CSVs, merge timelines |
| 06 | `06_Process_BPMN.ipynb` | Enrich | BPMN XML → Mermaid conversion |
| 07 | `07_Gen_Architecture_Docs.ipynb` | Generate | Tier 1 (per-capability BDAT) + Tier 2 (tower summary) |
| 08 | `08_Cross_Reference_Mapping.ipynb` | Enrich | SAP ↔ Smartsheet object/transport cross-reference |
| 09 | `09_Orchestrator.ipynb` | Control | Run all notebooks in sequence, validate outputs |

**Change from build plan**: NB07 and NB08 swapped roles — NB07 is now the single generation notebook (was separate business + systems); NB08 is the cross-reference mapping (new).

---

## 8. Decision Summary

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Document structure | **Single BDAT doc per capability** + tower roll-up | Avoids 480-document explosion; maintains BDAT traceability; simpler pipeline |
| Document tiers | **Tier 1** (capability) + **Tier 2** (tower summary) | Serves both detailed architect needs and leadership summary needs |
| L3 detail | **Sections within L2 document** (not separate files) | Activities/tasks are too granular for separate documents |
| SAP ↔ Smartsheet | **Dedicated cross-reference notebook (NB08)** | Key synergy — maps development to project tracking; flags gaps |
| Folder cleanup | **Archive probes to `_archive/`** (git-ignored) | Preserves history without cluttering workspace |
| POC → Production | **Config-driven mode switch** (`api_endpoints.yaml`) | Zero code change to pivot; only config values change |

---

<details>
<summary>View the Prompt Used</summary>

```markdown
After these probes, we need to clean up the folder and have a process flow that takes what we currently have for POC but should be able to pivot to actual API keys for the right system for better execution. On the Odata API for S4Hana Source systems, the goal would be to extract development objects from the source system, somehow map them to objects being tracked in smartsheet, create synergy for the SAD documentation for each tower's capabilities under the folder structure for L0, L1, L2, L3. Additionally, I wanted to check with you to see if we need to have a separate document for business, data, application and technology architecture with a summarized document for all 4 or would a single document split between summary & detailed for BDAT Architecture work for each capability?
```

</details>
