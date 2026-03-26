# IAO Architecture — API Probe Findings

**Date:** 2026-03-23  
**Probe Scripts:** `api_probe.py`, `probe_iapm.py`, `probe_bic_detail.py`, `probe_bic_backend.py`, `probe_bic_real_api.py`, `probe_bic_auth.py`, `probe_data_analysis.py`

---

## Executive Summary

Local API probing confirms that all four target systems are **network-reachable** from this workstation, but each requires **authenticated access** before data extraction can proceed. The BIC API architecture was fully reverse-engineered from its SPA JavaScript bundles, revealing a Spring Boot backend with OpenAPI documentation available behind Basic auth. Existing local data (IAPM CSV, BPMN manifests, flow data) is rich and well-structured, confirming the build plan's data scoping is accurately sized.

---

## 1. IAPM API — `iapm.intel.com`

| Test | Result | Detail |
|------|--------|--------|
| **Network reachability** | ✓ PASS | HTTP 200 (with `verify=False` for Intel internal CA) |
| **SSL certificate** | ⚠ Self-signed chain | Python `requests` fails with `CERTIFICATE_VERIFY_FAILED`; need to add Intel CA to certifi or use `verify=False` |
| **Auth: NTLM** | ✗ FAIL | 401 — site does not support Windows Integrated Auth |
| **Auth: Bearer (MSAL)** | ⏳ NOT TESTED | Requires token from browser `localStorage` |
| **API endpoint** | Confirmed | `/internal/api/AllSolution` returns 401 with `WWW-Authenticate: Bearer` |
| **CORS** | Open | `Access-Control-Allow-Origin: *`, `Allow-Methods: GET, PUT, POST, DELETE, PATCH, OPTIONS` |

### Existing Local Data

| File | Size | Records | Columns |
|------|------|---------|---------|
| `IAPM_All_Solutions.csv` | 19.8 MB | 30,372 | 54 |
| `System_IAPM_Lookup.csv` | 16.7 KB | 61 | 16 |
| `Application_Catalog.csv` | 13.8 KB | — | 8 |

**IAPM CSV Key Columns (54):**
`applicationId`, `applicationNm`, `applicationAcronymNm`, `applicationClassificationNm`, `productOwnerNm`, `productTypeNm`, `superGroupLongNm`, `groupLongNm`, `divisionLongNm`, `applicationLifecycleStatusNm`, `applicationLifecycleStatusMonthCount`, `applicationLifecycleStatusEndDtm`, `applicationUserBaseNm`, `informationTechnologySupportTierNm`, `informationTechnologyServiceNm`, `informationTechnologySegmentNm`, `informationDataClassificationNm`, `businessOrganizationNm`, `tmModelNm`, `paceLayeringNm`, `informationTechnologyManagedApplicationInd`, `applicationOwningDepartmentNm`, `publishInd`, `tmModelEndDt`, `saasSolutionInd`, `applicationAccessibleOutsideIntelNetworkWithoutVpnInd`, `applicationHostingTypeNm`, `applicationOwningDepartmentLevel3Nm`, `applicationOwningDepartmentLevel4Nm`, `applicationOwningDepartmentLevel5Nm`, `capabilityNm`, `businessOwnerNm`, `supplierId`, `applicationDevelopedByIntelInd`, `applicationDeliveryTypeNm`, `applicationOwningDepartmentHierarchyTxt`, `logicalPlatformGroupNm`, `productOwnerWwid`, `productOwnerEmailTxt`, `submitDtm`, `applicationLastCertifiedDtm`, `assetAndServiceUsedInd`, `managedServiceProviderInd`, `electronicDesignAutomationInd`, `serviceOfferingNm`, `applicationUsageClassificationNm`, `idmAccelerationOfficeTowerClassificationNm`, `idmAccelerationOfficeTmModelNm`, `secondaryProductOwnerNm`, `secondaryProductOwnerWwid`, `secondaryProductOwnerEmailTxt`, `softwarePublisherNm`, `softwareEditionNm`, `softwareProductNm`

### Action Required
> **Get a Bearer token from the browser:**
> 1. Open https://iapm.intel.com in a browser (Edge/Chrome)
> 2. Press F12 → Console tab
> 3. Run: `Object.entries(localStorage).find(([k,v])=>k.includes('accesstoken'))`
> 4. Copy the `secret` value (starts with `eyJ...`)
> 5. Run: `python api_probe.py --iapm-token YOUR_TOKEN --skip-bic --skip-smartsheet --skip-odata`

### SSL Fix for Production
Add Intel's internal CA certificate to the Python certifi bundle:
```python
# Option 1: Point to Intel CA bundle
import os
os.environ["REQUESTS_CA_BUNDLE"] = r"C:\path\to\intel-ca-bundle.pem"

# Option 2: Add to certifi (permanent)
# certifi location: python -c "import certifi; print(certifi.where())"
```

---

## 2. SAP BIC — `processdesign.intel.bicplatform.com`

| Test | Result | Detail |
|------|--------|--------|
| **Network reachability** | ✓ PASS | HTTP 200, Angular SPA at `/portal` |
| **SSL certificate** | ✓ PASS | Valid certificate, no bypass needed |
| **Health endpoint** | ✓ PASS | `/health` → `{"status": "UP"}` (unauthenticated) |
| **Backend framework** | Confirmed | Spring Boot (Actuator endpoints detected) |
| **Auth: Frontend API** | 🔒 Token required | `Token error="token is null"` |
| **Auth: Backend API** | 🔒 Basic Auth required | `WWW-Authenticate: Basic realm="Realm"` |
| **Auth: NTLM** | ✗ NOT SUPPORTED | Returns 401 even with NTLM |
| **Auth: SSO Flow** | Detected | `/auth` redirects to `/auth/` (SSO gateway) |
| **API Base Path** | Discovered | `/process-design/frontend/api` (token auth) |
| **OpenAPI Spec** | Discovered | `/process-design/v3/api-docs` (Basic auth) |

### API Architecture (Reverse-Engineered from JS Bundles)

```
BIC Process Design (GBTEC Platform)
├── /portal                         ← Angular SPA (frontend)
│   ├── main-4D3KIZ3T.js           ← 212K chars, API config + routes
│   ├── scripts-Z2TOLL7U.js        ← 254K chars, Summernote editor
│   └── polyfills-EONH2QZO.js      ← 34K chars
├── /process-design/                ← Spring Boot backend
│   ├── /frontend/api               ← Frontend REST API (Token auth)
│   ├── /v3/api-docs                ← OpenAPI 3.0 specification (Basic auth)
│   ├── /health                     ← Health check (Basic auth)
│   └── /actuator/*                 ← Spring Boot actuator (Basic auth)
├── /auth                           ← SSO/Auth gateway
└── /health                         ← Platform health (public)
```

### Discovered Service Names (from JS bundle analysis)
- `biccloud-catalog-service` — Catalog items (CRUD + events)
- `biccloud-catalog-data-transfer-service` — Catalog import/export
- `biccloud-workflow-service` — Workflow & diagram management
- **Functional Domains:** processes, diagrams, catalogs, users, export
- **Export Operations:** `processesexport.export`, `domainDataTransfer.export`, `users.export`
- **Roles:** REVIEWER, AUTHOR, EDITOR, ADMINISTRATOR
- **API Format:** SIREN (Hypermedia) via `this.siren` in JS

### Existing BPMN Data

| File | Records | Detail |
|------|---------|--------|
| BPMN manifest (towers) | 3,337 | All "Business Process Diagram (BPMN 2.0)" |
| Successful exports | 3,078 | Status "OK" |
| Failed exports | 259 | Various Signavio export failures |
| Actual .bpmn files | 0 | Not yet exported to local filesystem |

### Action Required
> **Two auth paths, either will work:**
>
> **Path A — Basic Auth (for OpenAPI docs + backend):**
> Get BIC platform username/password (may be a service account or your Intel SSO credentials)
>
> **Path B — Token Auth (for frontend API):**
> 1. Open https://processdesign.intel.bicplatform.com/portal in a browser
> 2. Log in with your Intel SSO
> 3. Press F12 → Network tab → filter XHR
> 4. Find any request to `/process-design/frontend/api/*`
> 5. Copy the `Authorization` header value
>
> **Priority: Get the OpenAPI spec first** — it will reveal every available API endpoint,
> request/response schemas, and export capabilities. This alone will define Notebook 02.

---

## 3. Smartsheet API — `api.smartsheet.com`

| Test | Result | Detail |
|------|--------|--------|
| **Authentication** | ✓ PASS | Authenticated as sajiv.francis@intel.com |
| **Account** | ✓ PASS | Intel Enterprise Account |
| **Workspace discovery** | ✓ PASS | 5 workspaces accessible |
| **Target workspace** | ✓ PASS | "IDM 2.0 Implementation" — 12 folders, 1 root sheet |
| **IAO TMO workspace** | ✓ PASS | Full IAO TMO structure — TMO, E2E, SCP, B-Apps, Data |
| **Sheet read access** | ⚠ MFA POLICY | 1,227 sheets visible with EDITOR access; but 44+ return error 1362 (MFA Policy) |
| **MFA Policy** | ⚠ Error 1362 | `"This action is restricted by an MFA Policy"` — workspace enforces MFA for API reads |
| **Token re-confirmed** | ✓ 2026-03-24 | Token `RP22i...` valid; user can view MFA-blocked sheets in browser (MFA passes via authenticator) |

### Workspace Structure

**IDM 2.0 Implementation** (target workspace):
- 12 top-level folders: Archive, Core PMO, Integrated Plan, Team Insights, Change Control, Deliverables Tracker, LE Merge, Object Tracker (incl. RICEFW Console), RAID, Sprint Plan, Tower/Horizontal Folders, WIP
- Tower/Horizontal Folders: E2E, FPR, OTC IF, OTC IP, PTP, FTS IF, FTS IP, Master Data, Data Migration, PDM, Analytics, Technology, Infrastructure, Security, OCM, Testing, Cutover, Hypercare

**IAO TMO Workspace**:
- TMO, E2E, Supply Chain Planning, Boundary Apps (incl. **1.3.7 Enterprise Architecture**), Data, Legal Entity, COE, Integration Readiness, PMO Workspace

### Key Sheets — Schemas Discovered

#### IAO Master RAID Log (id=2062365868642180) — ✓ READABLE
- **3,243 rows** × 48 columns
- Key columns: `RAID ID`, `RAID Type` (Action/Issue/Key Decision/Risk), `Title`, `Description`, `Due Date`, `RAID Severity` (P0-P3), `Escalation Level` (L1-L4), `Status`, `Assigned To (Team)`, `Assigned To (Sub-Team)`, `Created By (Team)` (PMO/E2E/FPR/PTP), `Open/Closed`, `Days Past Due`, `Release` (R1-R4), `ERP/SCP`
- **Directly maps to Notebook 03 RAID extraction**

#### E2E RAID Log (id=2147893813137284) — ✓ READABLE
- **425 rows** × 32 columns
- Key columns: `Row ID`, `RAID Item` (Risk/AR/Issue/Decision), `Risk/Impact Level`, `RAID Description`, `POR Due Date`, `Status`, `RAID Resolution Owner`, `Meeting Origin` (Design Forums, Core Team), `Release`, `Integration Team Impacted`, `MisCo`
- Tower-tagged: can filter by COE/Tower Tag (BPM COE, CM COE, Data COE, etc.)

#### IAO TMO RAID Log (id=8532290086850436) — ✓ READABLE
- **50 rows** × 32 columns
- TMO-level risks, actions, issues, decisions — executive governance layer

#### E2E Workplan (id=1834853108502404) — ✓ READABLE
- **401 rows** × 16 columns — program task tracking with milestones
- Key columns: `Task`, `Status`, `Start (POR)`, `End (POR)`, `Assigned To`, `Tied to Milestone` (ITC2/ITC3/UAT1/UAT2), `Release`

#### IAO Operational Metrics (id=7589965303074692) — ✓ READABLE
- **101 rows** × 39 columns — KPI/metric definitions
- Key columns: `Operational Metric`, `Value Driver`, `Tier`, `Business` (IP/IF/Corp), `Tower`, `Metric Performance Target`, `Data Source`, `Data Required`, `Key L3 Related Process`
- **Note:** Sheet marked EOL as of Dec 2024 — redirected to Intel Metrics Central

#### SCP-PMO WRICEF (id=5352213586071428) — ✓ READABLE
- **188 rows** × 110 columns — SCP RICEFW tracker (fully loaded!)
- Key columns: `SCP Object ID`, `Object Description`, `Object Type`, `Tower Name`, `Sub-Tower`, `Complexity`, `Dev Completion Status`, `FUT Approval`, `Source System`, `Target System`, `Boundary App IAPM ID`, `Boundary Application Name`, `Sprint Number`, `Change Request ID`
- **This is the primary RICEFW data source for SCP towers**

#### Enterprise Architecture Folder (1.3.7)
- `IAO Enterprise Architecture Gantt` (id=5810176758075268)
- `EA Status Input_Sheet` (id=4382268676067204)
- `NEW_B-Apps Enterprise Architecture` folder

### Access Summary

| Category | Accessible | 403 Forbidden | Notes |
|----------|-----------|---------------|-------|
| RAID Logs (Master, E2E, TMO) | ✓ 3/3 | — | Full API read access (no MFA restriction) |
| E2E Workplan & Metrics | ✓ 2/2 | — | Full API read access |
| SCP WRICEF (RICEFW) | ✓ 1/1 | — | 188 objects, 110 columns — API works |
| Object Trackers (S4, ECA) | EDITOR | 🔒 2/2 | **MFA Policy (error 1362)** — browser works, API blocked |
| Transport Trackers | EDITOR | 🔒 7/7 | **MFA Policy** — all 7 towers |
| RICEFW Request Console | EDITOR | 🔒 1/1 | **MFA Policy** |
| Integrated Plan | EDITOR | 🔒 1/1 | **MFA Policy** |
| Deliverables Tracker | EDITOR | 🔒 3/3 | **MFA Policy** |
| Change Control | EDITOR | 🔒 22/22 | **MFA Policy** — CR Log, metrics, ITC exceptions |
| Config Trackers (per tower) | EDITOR | 🔒 7/7 | **MFA Policy** — all 7 towers |
| User Story Trackers (per tower) | EDITOR | 🔒 7/7 | **MFA Policy** — all 7 towers |
| L2/L3 Repository | EDITOR | 🔒 4/4 | **MFA Policy** — includes Signavio L3 mapping |
| Total sheets visible | 1,227 | — | EDITOR access across all |

> **Root Cause (Updated 2026-03-24)**: NOT a sharing/permission issue. All 44 blocked sheets show `accessLevel=EDITOR` in the sheet list. The IDM 2.0 Implementation workspace has an **MFA Policy** enabled that blocks API-only access (Smartsheet error code 1362). Browser access works because the authenticator app satisfies MFA. The API token alone does not carry MFA context.
>
> **Solution**: Use **Playwright browser extraction** (Mode A) for MFA-blocked sheets — the browser session carries the MFA-verified context. This aligns with the same Playwright approach needed for IAPM and BIC.

### Full Folder Inventory (Probed 2026-03-24)

**IDM 2.0 Implementation** workspace: 12 top-level folders. Four target folders scanned:

| Folder | Sheets | Sub-folders | Access |
|--------|--------|-------------|--------|
| Intel IDM Deliverables Tracker (id=3616638567245700) | 5 | 1 | All 403 |
| Intel IDM Change Control (id=8849950185416580) | 22 | 9 | All 403 |
| Intel IDM Object Tracker (id=968650837518212) | 57 | 21 | All 403 |
| Tower/Horizontal Folders (id=264963395741572) | 74 | 68 | All 403 |
| **Total** | **158** | **99** | **All 403** |

> **Root cause (CORRECTED)**: MFA Policy enforcement (error 1362), not sharing permissions. User has EDITOR access on all 158 sheets, but the workspace MFA policy blocks API-token-only reads. Browser access works (authenticator satisfies MFA). Solution: Playwright browser extraction for these sheets.

#### Intel IDM Deliverables Tracker
| Sheet | ID |
|-------|----|
| Anafi Deliverables Log & Sign off Tracker | 4321189485825924 |
| IDM 2.0 Deliverables Log & Sign off Tracker | 8568208059486084 |
| IDM 2.0 Deliverables Log & Sign off Tracker_Backup | 5235562236563332 |
| Implementation Sprint Deliverables Tracker | 2297542419107716 |
| Deliverables Summary - Calc Sheet | 2397290070232964 |

#### Intel IDM Change Control
| Sheet | ID |
|-------|----|
| IDM 2.0 Program Change Request Log | 8701667910307716 |
| CR Added Objects (Normalized) | 2635053717737348 |
| CR BApp IAPM ID Calc Sheet | 7325212707082116 |
| Build CR Completion Overview | 7248135647612804 |
| Build CR Completion Tracker | 2538087050596228 |
| Design/Other CR Completion Overview | 4229786059624324 |
| Design/Other CR Completion Tracker | 6818917168140164 |
| R3 ITC1 Exceptions & Testing Impact Inputs | 5402864919728004 |
| R3 ITC1* RICEFW | 1607564421713796 |
| R3 ITC3 CR's (+Testing Impact For Prior Cycles) | 3590151943966596 |
| R3 ITC2 Internal CR's | 8803584071126916 |
| Core Leadership CR Approvals | 8481401029480324 |
| CR Metric Summary / CR Metrics / CR Metrics (Program & Build) | various |
| ERP Transformation Change Control Summary | 5637591114141572 |

#### Intel IDM Object Tracker (Key Sheets)
| Sheet | ID |
|-------|----|
| S4 [R3] Intel IDM Object Tracker | 5077868279189380 |
| ECA [R3] IDM Object Tracker | 5042493213069188 |
| FUT Tracker | 4947944298991492 |
| [R1/R2] IDM Object Tracker | 6022866990485380 |
| Intel IDM 2.0 RICEFW Request Console | 216957114601348 |
| Consolidated Report - RICEFW Console/Tracker | 5009410606714756 |
| IAO ERP Scope Volatility | 8727490970210180 |
| Intel IDM Transport Tracker | 6369113634983812 |
| IDM Intel RICEFW Issues Tracker | 6388577386581892 |

#### Tower/Horizontal Folders — Per-Tower Structure
Each tower folder follows this pattern: Transport Tracker, Config Tracker (with Archive/WIP), User Story Tracker (with Dashboard/Burndown).

| Tower | Transport Tracker ID | Config Tracker ID | User Story Tracker ID |
|-------|---------------------|-------------------|----------------------|
| 03. FPR | 776566959198084 | 765066727083908 | 5599933126102916 |
| 04. OTC IF | 2292621695209348 | 3478874142756740 | 465097860272004 |
| 05. OTC IP | 6831818011529092 | 1126733021400964 | 5274780479475588 |
| 06. PTP | 1553681161867140 | 893351075204996 | 7440833418579844 |
| 07. FTS IF | 8238299541884804 | 2232006482022276 | 55641448075140 |
| 08. FTS IP | 4721301147045764 | 208033208553348 | 2423233580060548 |
| 09A. Master Data | 6268314007326596 | 4541806473596804 | — |

Additional Tower/Horizontal sub-folders: E2E Process Integration (with L2/L3 Repository), Data Migration, PDM, Analytics, Technology, Infrastructure, Security, OCM, Testing, Cutover, Hypercare, plus Build Sprint Readout Reports, Config Tracker Dashboards, User Story Dashboards.

**E2E Process Integration — L2/L3 Repository** (notable):
| Sheet | ID |
|-------|----|
| Consolidated Final - Intel IAO L2 L3 Repository | 6956209458335620 |
| L3 from Signavio | 8945793852460932 |
| SOW - Intel IAO L2 L3 Repository | 8761819615154052 |
| Separation Design - L3 Disposition | 7407506977410948 |

### What We Can Extract Now (POC)

| Data Category | Sheet ID | Rows | Maps to NB03 Section |
|---------------|----------|------|---------------------|
| RAID (Master) | 2062365868642180 | 3,243 | RAID logs — Risks, Actions, Issues, Decisions |
| RAID (E2E) | 2147893813137284 | 425 | E2E-level RAID |
| RAID (TMO) | 8532290086850436 | 50 | TMO governance RAID |
| RICEFW (SCP) | 5352213586071428 | 188 | RICEFW tracker, object status, dependencies |
| Workplan (E2E) | 1834853108502404 | 401 | Program timelines, milestones |
| Metrics | 7589965303074692 | 101 | KPI/operational metrics (EOL, backup only) |

### Sheets Needing Access (Request from Admin)

**MFA-Blocked Sheets — Accessible via Playwright (Mode A)**:

All 44 sheets below have `accessLevel=EDITOR` but are blocked by workspace MFA policy (error 1362). They are accessible in the browser with authenticator.

| Category | Sheets | Key IDs |
|----------|--------|---------|
| Object Trackers | S4 R3, ECA R3, R1/R2, FUT | 5077868279189380, 5042493213069188, 6022866990485380, 4947944298991492 |
| RICEFW Console & Reports | Console, Consolidated, Issues | 216957114601348, 5009410606714756, 6388577386581892 |
| Transport Trackers (7 towers) | FPR, OTC-IF, OTC-IP, PTP, FTS-IF, FTS-IP, MDM | 776566959198084, 2292621695209348, 6831818011529092, 1553681161867140, 8238299541884804, 4721301147045764, 6268314007326596 |
| Config Trackers (7 towers) | FPR, OTC-IF, OTC-IP, PTP, FTS-IF, FTS-IP, MDM | 765066727083908, 3478874142756740, 1126733021400964, 893351075204996, 2232006482022276, 208033208553348, 4541806473596804 |
| User Story Trackers (7 towers) | FPR, OTC-IF, OTC-IP, PTP, FTS-IF, FTS-IP | 5599933126102916, 465097860272004, 5274780479475588, 7440833418579844, 55641448075140, 2423233580060548 |
| Deliverables Tracker | 3 sheets | 8568208059486084, 4321189485825924, 2297542419107716 |
| Change Control | CR Log + 8 sheets | 8701667910307716 + various |
| L2/L3 Repository | 4 sheets | 6956209458335620, 8945793852460932, 8761819615154052, 7407506977410948 |
| Integrated Plan | 1 sheet | 3514737224535940 |
| Scope & Misc | Scope Volatility, Completion Tracker | 8727490970210180, 8028476577632132 |

**Two options to unlock**:
1. **Playwright extraction (Mode A)** — browser session carries MFA context, can read all sheets
2. **Request MFA policy exemption** — ask workspace admin to exempt API tokens from MFA enforcement

---

## 4. SAP S/4HANA OData — Sandbox PTF (client 210)

**Probed**: 2025-03-24 | **Gateway**: `https://sapptfci.intel.com:8300` | **Client**: 210

| Test | Result | Detail |
|------|--------|--------|
| **Network reachability** | ✓ PASS | `sapptfci.intel.com:8300` responds, TLS handshake OK |
| **Anonymous probe** | 401 Negotiate | `WWW-Authenticate: Negotiate` — SPNEGO/Kerberos required |
| **Windows SSO (SPNEGO)** | ✓ PASS | `requests-negotiate-sspi` auto-authenticates via Kerberos ticket |
| **Service catalog** | ✓ PASS | **92 OData services** discovered via `/sap/opu/odata/iwfnd/CATALOGSERVICE;v=2/ServiceCollection` |
| **CSRF token** | ✓ PASS | `x-csrf-token: azTk8xdf0fGpzbP3dxVGxQ==` — write operations possible |
| **ADT Repository Search** | ✓ PASS | Custom objects found at `/sap/bc/adt/repository/informationsystem/search` |
| **ADT Package Listing** | ✓ PASS | 16 packages visible |
| **Standard APIs (API_*)** | ✗ 403 | `IWFND/MED/170: No service found for namespace` — not activated on sandbox |
| **Z-custom OData services** | ✗ 403/500 | In catalog but namespace routing / backend alias issues |
| **ADT Transport Search** | ⚠ 406 | HTTP 406 Not Acceptable — content negotiation issue (needs different Accept header) |

### ADT Repository Objects Found (Sandbox)

| Type | Count | Examples |
|------|-------|---------|
| Z* objects (all types) | 9 | Various custom objects |
| Y* objects (all types) | 49 | Various custom objects |
| ZCL_* ABAP Classes | 11 | `ZCL_DF_CF_FIORI_OBJECTS`, `ZCL_DF_CF_SEL`, `ZCL_IM_BIFPR_ACCIDMOD`, `ZCL_IM_BIFPR_BP_BADI_IMPL` |
| ZCDS_* CDS Views | 3 | `ZCDS_E_GLACCOUNTLINEITEMS`, `ZCDS_E_OPACCTDOCITEM` |
| Packages | 16 | Various development packages |
| IDM-specific (Z_IDM*, Z_IAO*) | **0** | Expected — this is a sandbox, not IDM DEV |

### Service Catalog Highlights (92 services total)

| Category | Count | Examples |
|----------|-------|---------|
| BOM / Manufacturing | 4 | ZBILLOFMATERIALV2_SRV, ZBOM_COMPARISON |
| MRP / Production | 6 | ZPP_MRP_COCKPIT_SRV, ZPP_MRP_MATERIAL_COVERAGE_SRV |
| HR / Payroll | 16 | HRSFEC_*, PYC_*, PYD_* |
| CDS View Browsing | 2 | ZCDSALLVIEWS, ZVDM_CDSVIEW_BROWSER |
| Transport Mgmt | 1 | ZTRANSPORT |
| Fiori Infrastructure | 12 | /UI2/FDM_*, PAGE_BUILDER |
| Gateway / Platform | 8 | /IWFND/*, /IWBEP/* |
| ADT (REST, not OData) | — | Repository search, package listing (working!) |

### Probe Scripts

| Script | Purpose | Key Findings |
|--------|---------|-------------|
| `probe_sap_odata.py` | Anonymous network probe | Reachable, 401 Negotiate |
| `probe_sap_odata2.py` | Windows SSO probe | Auth works! 92 services discovered |
| `probe_sap_odata3.py` | Z-custom service queries | All 403 (namespace routing) |
| `probe_sap_odata4.py` | 403 root cause diagnosis | `IWFND/MED/170` namespace issue; ADT works |
| `probe_sap_odata5.py` | ADT deep probe | 11 classes, 3 CDS views, 16 packages, 0 IDM objects |

### Key Findings

1. **Windows SSO is the auth model** — SPNEGO/Kerberos via `requests-negotiate-sspi`. No password needed.
2. **ADT REST API is the richest data source** — repository search, packages, object metadata all work.
3. **Standard OData APIs (API_*) are not activated** on this sandbox — namespace routing returns 403.
4. **Z-custom OData services exist** in the catalog but have backend alias issues (system alias not configured).
5. **This is PTF (sandbox)** — no IDM-specific custom code. The actual IDM DEV system will have tower-specific
   RICEFW objects, transport requests, and deployment artifacts.
6. **The extraction pattern is proven** — Windows SSO + ADT + Service Catalog works. Just needs the right gateway.

### Remaining Need

> **From SAP BASIS / IDM 2.0 Technical Lead:**
> 1. **IDM DEV system gateway hostname and port** (e.g., `https://sapXXX.intel.com:XXXX`)
> 2. **SAP client number** for IDM DEV
> 3. Confirm OData services are activated (at minimum: service catalog + ADT endpoints)
> 4. Confirm Windows SSO (SPNEGO) is enabled on the IDM DEV gateway
>
> **No password or service user needed** — Windows SSO via Kerberos ticket handles authentication.

---

## 5. Existing Data Quality Assessment

### DS-020 CurrentFlows (Reference Capability)

| Column | Coverage | Notes |
|--------|----------|-------|
| Flow Chain | 36/36 (100%) | All flow chains named |
| Hop # | 36/36 (100%) | |
| Source System | 36/36 (100%) | |
| Target System | 36/36 (100%) | |
| Interface / Technology | 36/36 (100%) | e.g., "Direct" |
| Direction | 36/36 (100%) | e.g., "→" |
| Frequency | 36/36 (100%) | e.g., "Near Real-Time" |
| Data Description | 36/36 (100%) | |
| Flow Purpose | 36/36 (100%) | |
| Notes / Corrections | 2/36 (6%) | Sparse |
| Process/System Owner | 36/36 (100%) | |
| Data Owner | 20/36 (56%) | Partial |
| Applicable Scope | 36/36 (100%) | |
| Src Web Address | 5/36 (14%) | Very sparse |
| Src Business Owner | 34/36 (94%) | |
| Src Product Owner | 9/36 (25%) | Sparse |
| Src/Tgt IAPM URL | 36/36 (100%) | Populated by enrichment |

### System_IAPM_Lookup

- 61 flow system names → 44 unique IAPM applications
- 3 lifecycle statuses: Deployed, Planning, Retirement
- 4 app classifications: Application, Platform, etc.
- Match confidence: AUTO_DEPLOYED_PRIORITY (automated matching)

---

## 6. Recommendations & Next Steps

### Immediate Actions (Remaining)

| Priority | API | What to Get | How |
|----------|-----|-------------|-----|
| **1** | **IAPM** | Bearer token from browser | F12 → Console → localStorage access token |
| **2** | **BIC** | Session token from browser | F12 → Network → copy Authorization header |
| ~~3~~ | ~~Smartsheet~~ | ~~API access token~~ | ✅ **DONE — Token validated, 400+ sheets accessible** |
| **4** | **SAP OData** | IDM DEV gateway hostname | SAP BASIS team — sandbox pattern proven, need production/dev gateway |
| **5** | **Smartsheet Admin** | Share key sheets (Object Tracker, RICEFW Console, Transport Trackers) | Request from workspace admin |

### Smartsheet — Ready for Development

With the validated token, **Notebook 03 can begin development immediately** using these confirmed data sources:

| Sheet | ID | Rows | Status |
|-------|----|------|--------|
| IAO Master RAID Log | 2062365868642180 | 3,243 | ✓ Ready |
| E2E RAID Log | 2147893813137284 | 425 | ✓ Ready |
| IAO TMO RAID Log | 8532290086850436 | 50 | ✓ Ready |
| SCP-PMO WRICEF (RICEFW) | 5352213586071428 | 188 | ✓ Ready |
| E2E Workplan | 1834853108502404 | 401 | ✓ Ready |

### Once IAPM/BIC Tokens Are Available, We Can:

1. **IAPM** — Verify the 30K-record API response matches our 54-column schema, confirm field names, measure response time
2. **BIC** — Download the full OpenAPI spec from `/process-design/v3/api-docs` (this alone defines the entire Notebook 02 design), identify BPMN export endpoints, test diagram retrieval

### Build Plan Impact

| Finding | Impact on Build Plan |
|---------|---------------------|
| IAPM uses MSAL Bearer (not NTLM) | POC auth needs Playwright login or manual token, not NTLM |
| IAPM SSL uses Intel internal CA | Add `REQUESTS_CA_BUNDLE` env var or cert injection to all notebooks |
| BIC has OpenAPI docs at `/process-design/v3/api-docs` | Notebook 02 design can be fully data-driven from spec |
| BIC uses SIREN hypermedia format | `bic_client.py` needs SIREN link traversal, not flat REST |
| BIC has Basic Auth on backend | Alternative to SSO token for service-level access |
| BIC real API at `/process-design/frontend/api` | Token auth (not Basic) required for data endpoints |
| BPMN manifest has 259 failed models | Need error handling for failed BPMN exports in Notebook 02 |
| Timeline CSV has encoding issues | `pd.read_csv(encoding='latin-1')` or fix non-breaking spaces |
| 0 .bpmn files exported locally | Notebook 02 must export fresh from BIC, cannot rely on local files |
| **Smartsheet: RAID Logs fully accessible** | **3,718 RAID records across 3 sheets — ready for NB03** |
| **Smartsheet: SCP RICEFW accessible** | **188 objects × 110 columns — ready for NB03** |
| **Smartsheet: E2E Workplan accessible** | **401 tasks — program timeline ready for NB03** |
| **Smartsheet: ERP RICEFW Console 403** | Need admin to share — or pull ERP RICEFW from SCP-PMO WRICEF (partial) |
| **Smartsheet: Object Trackers 403** | Need admin to share S4/ECA Object Trackers |
| **Smartsheet: Transport Trackers 403** | Need admin to share per-tower transport trackers |
| **Smartsheet: Config Trackers 403** | 7 per-tower config trackers discovered — all 403 |
| **Smartsheet: User Story Trackers 403** | 7 per-tower user story trackers — all 403 |
| **Smartsheet: Deliverables Tracker 403** | 5 sheets — all 403 |
| **Smartsheet: Change Control 403** | 22 sheets (CR Log, metrics, ITC exceptions) — all 403 |
| **Smartsheet: L2/L3 Repository 403** | Consolidated L2/L3 Repository + Signavio mapping — all 403 |
| **Smartsheet: Total inventory** | 158 sheets in 4 target folders, 99 sub-folders — all 403 |
| **Smartsheet workspace structure** | `IDM 2.0 Implementation` + `IAO TMO` = two key workspaces |

---

## 7. Files Created During This Probe

| File | Purpose | Keep? |
|------|---------|-------|
| `api_probe.py` | Main probe script (all APIs) | ✓ Reuse with tokens |
| `probe_iapm.py` | IAPM-specific SSL bypass test | Can delete |
| `probe_bic_detail.py` | BIC SPA endpoint discovery | Can delete |
| `probe_bic_backend.py` | BIC backend path discovery | Can delete |
| `probe_bic_real_api.py` | BIC real API path discovery | Can delete |
| `probe_bic_auth.py` | BIC auth method testing | Can delete |
| `probe_bic_js.py` | BIC JS bundle analysis | Can delete |
| `probe_data_analysis.py` | Local data schema analysis | ✓ Reuse for data validation |
| `probe_smartsheet.py` | Initial Smartsheet workspace discovery | Can delete |
| `probe_smartsheet2.py` | Deep Smartsheet folder/sheet access testing | Can delete |
| `probe_smartsheet_keys.py` | Key sheet schema extraction | ✓ Reuse — has all sheet IDs |
| `probe_smartsheet3.py` | Full sheet-level probe with row counts | Can delete |
| `probe_smartsheet3b.py` | Fast folder tree scan — discovered 158 sheets in 4 folders | ✓ Reuse |
| `probe_smartsheet4.py` | Targeted S4 Object Tracker re-probe — discovered error 1362 MFA | Can delete |
| `probe_smartsheet5.py` | Comprehensive 50-sheet MFA audit — classified all key sheets | ✓ Reuse |
| `smartsheet_folder_scan.json` | Full folder tree JSON (all IDs) | ✓ Reference data |
| `smartsheet_access_audit.json` | 50-sheet access audit results (accessible vs MFA-blocked) | ✓ Reference data |
