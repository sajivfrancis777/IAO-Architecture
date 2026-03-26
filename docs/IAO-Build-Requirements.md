# IAO Architecture Pipeline — Build Requirements for Production Automation

## Purpose

This document specifies every access requirement, role, credential, and configuration needed to move the IAO Architecture Pipeline from POC (manual/local) to **production-ready fully automated** document generation synced between GitHub and SharePoint.

---

## 1. SAP S/4HANA OData & ADT API Access

### Systems

| System | Host | Client | Purpose |
|--------|------|--------|---------|
| **BI0** (Intel Foundry) | `sapbi0ci.intel.com:8220` | 200 | Dev objects, transports, OData catalog for IF towers |
| **DI0** (Intel Products) | `sapdi0ci.intel.com:8220` | 200 | Dev objects, transports, OData catalog for IP towers |

### Required SAP Roles & Authorizations

A **service account** (type: Dialog or System) is required with the following authorization objects:

| Authorization Object | Field | Value | Purpose |
|---------------------|-------|-------|---------|
| **`S_SERVICE`** | `SRV_NAME` | `*` | Access to OData/ICF services |
| | `SRV_TYPE` | `HT` | HTTP service type |
| **`S_RFC`** | `RFC_TYPE` | `FUGR`, `FUNC` | Function module access for ADT |
| | `RFC_NAME` | `SADT*`, `RS_*` | ADT repository search, transport APIs |
| | `ACTVT` | `16` (Execute) | Execute permission |
| **`S_TCODE`** | `TCD` | `SE80`, `/IWFND/MAINT_SERVICE` | Dev object browser, OData catalog (optional) |
| **`S_DEVELOP`** | `DEVCLASS` | `*` | Read access to development packages |
| | `OBJTYPE` | `*` | All object types (PROG, TABL, DDLS, etc.) |
| | `ACTVT` | `03` (Display) | Display only — no modify access needed |
| **`S_ADT_RES`** | `URI` | `/sap/bc/adt/*` | ADT REST API access |
| | `ACTVT` | `03` (Display) | Read-only |
| **`S_ICF`** | `ICF_VALUE` | `/sap/opu/odata/*`, `/sap/bc/adt/*` | ICF node access for OData and ADT |

### Specific API Endpoints Required

| Endpoint | Auth | Purpose | Data Extracted |
|----------|------|---------|----------------|
| `/sap/opu/odata/IWFND/CATALOGSERVICE/ServiceCollection` | Negotiate/Basic | OData service catalog | Service names, versions, status |
| `/sap/bc/adt/repository/informationsystem/search` | Negotiate/Basic | ADT repository search | Custom dev objects (DDLS, DTEL, PROG, etc.) |
| `/sap/bc/adt/cts/transportrequests` | Negotiate/Basic | Transport requests | Transport counts per environment |
| `/sap/opu/odata/sap/APC_FLP_VARIANT_PERS_SRV` | Negotiate/Basic | Fiori app catalog | Fiori tile/app counts |

### Authentication Methods

| Method | Use Case | Requirements |
|--------|----------|-------------|
| **Negotiate (SPNEGO/Kerberos)** | Local Windows workstation | Windows domain account with SAP access |
| **Basic Auth** | CI/CD (GitHub Actions) | SAP service account username + password |
| **SAP Logon Ticket** | Browser-based extraction | Manual session (POC only) |

### Access Request Process

1. **Submit AGS request** via Intel's Identity & Access Management portal
2. Request role: **`Z_IAO_EA_READ`** (or equivalent composite role containing above auth objects)
3. Request for **both BI0 and DI0** systems (separate requests per system)
4. Specify: **Display-only access** — no transport, no modify, no debug
5. Justification: *"Enterprise Architecture automation — read-only extraction of OData service catalog and development object metadata for architecture documentation"*

### POC Status

| System | Status | Objects Found | Gap |
|--------|--------|---------------|-----|
| BI0 | Working via Negotiate | 761 OData services, 911 ADT objects | Need service account for CI |
| DI0 | Partial (session issue) | 1,060 services, 996 objects (first run) | Need explicit credentials |

---

## 2. Smartsheet API Access

### Current State

| Item | Status | Detail |
|------|--------|--------|
| API Token | Active | Token `RP22i...` valid for `sajiv.francis@intel.com` |
| Account | Enterprise | Intel Enterprise Smartsheet account |
| Accessible Sheets | 1,227 | EDITOR-level access across IDM 2.0 workspaces |
| MFA-Blocked Sheets | 44+ | Error 1362 — workspace MFA policy blocks API-only reads |

### Required for Production

| Requirement | Detail | Action Owner |
|-------------|--------|--------------|
| **Service Account API Token** | A dedicated Smartsheet service account (not personal) for CI/CD; needs EDITOR+ access to IDM 2.0 workspace | Smartsheet Admin / IAO PMO |
| **MFA Policy Exemption** | Request API exemption from MFA policy for the service account on `IDM 2.0 Implementation` workspace | Smartsheet Admin |
| **Sheet Access (Critical)** | The following sheets must be readable via API without MFA: | |
| | S4 [R3] Object Tracker (id: `5077868279189380`) | — RICEFW inventory |
| | ECA [R3] Object Tracker (id: `5042493213069188`) | — ECA RICEFW |
| | Transport Trackers (7 towers) | — Transport status |
| | Config Trackers (7 towers) | — Configuration items |
| **Sheet Access (Already Working)** | These sheets are accessible now: | |
| | IAO Master RAID Log (id: `2062365868642180`) — 3,243 rows | |
| | E2E RAID Log (id: `2147893813137284`) — 425 rows | |
| | SCP WRICEF (id: `5352213586071428`) — 188 rows | |
| | E2E Workplan (id: `1834853108502404`) — 401 rows | |

### Sheet-to-Document Section Mapping

| Smartsheet Source | Document Section | Current Status |
|-------------------|-----------------|----------------|
| S4 [R3] Object Tracker | §5.5 RICEFW Inventory, §7.1 Timeline | MFA blocked — need exemption |
| IAO Master RAID Log | §7.2 RAID Log | Working — 3,243 rows accessible |
| E2E RAID Log | §7.2 RAID Log (E2E tower) | Working — 425 rows accessible |
| Transport Trackers | §6.2 SAP Dev Status | MFA blocked — need exemption |
| SCP WRICEF | §5.5 RICEFW (SCP towers) | Working — 188 rows accessible |

### Access Request Process

1. **Contact IDM 2.0 Program PMO** — request Smartsheet service account creation
2. **Request MFA exemption** for the service account on the IDM 2.0 Implementation workspace
3. **Provide justification**: *"Automated architecture documentation pipeline — read-only API access to Object Tracker, RAID logs, and Transport Trackers for scheduled document generation"*
4. **Alternative (interim)**: Use Playwright browser automation (Mode A) to extract MFA-blocked sheets using an authenticated browser session

---

## 3. IAPM API Access

### Current State

| Item | Status |
|------|--------|
| Endpoint | `https://iapm.intel.com/internal/api/AllSolution` |
| Auth | Azure AD Bearer token (OAuth2) |
| Local cache | 30,371 applications in `IAPM_All_Solutions.csv` (19.8 MB, 54 columns) |

### Required for Production

| Requirement | Detail |
|-------------|--------|
| **Azure AD App Registration** | Register an app in Azure AD with `IAPM.Read` permission (or equivalent) |
| **Client Credentials Grant** | Enable service-to-service auth (no user interaction) for CI/CD |
| **API Scope** | `api://iapm.intel.com/.default` (confirm with IAPM team) |
| **SSL** | Add Intel internal CA to Python certifi bundle, or use `REQUESTS_CA_BUNDLE` env var |

### Access Request Process

1. Register app in **Azure Portal → App Registrations**
2. Request API permission from the IAPM platform team
3. **Alternative (interim)**: Refresh local CSV cache periodically — the 30K-row CSV covers all applications

---

## 4. BIC Process Design API Access

### Current State

| Item | Status |
|------|--------|
| Platform | GBTEC BIC Cloud at `processdesign.intel.bicplatform.com` |
| Backend | Spring Boot with OpenAPI spec at `/process-design/v3/api-docs` |
| Auth | Token auth (frontend) or Basic Auth (backend) |
| Local BPMN cache | 2,603 BPMN XML files already extracted across 108 capabilities |

### Required for Production

| Requirement | Detail |
|-------------|--------|
| **Service Account** | BIC platform service account with REVIEWER role |
| **Basic Auth Credentials** | For OpenAPI/backend access in CI/CD |
| **Export Permissions** | `processesexport.export` capability for bulk BPMN extraction |

### Access Request Process

1. Contact **BIC platform admin** (GBTEC managed) for service account
2. Request REVIEWER role + export permissions
3. **Alternative (interim)**: BPMN files already cached locally from Signavio exports; BIC API only needed for net-new process diagrams

---

## 5. SharePoint Online API Access

### Required for Production

| Requirement | Detail |
|-------------|--------|
| **Azure AD App Registration** | App name: `IAO-Architecture-Pipeline` |
| **Supported Account Type** | Single tenant (Intel only) |
| **API Permissions** | Microsoft Graph → Application permissions → `Sites.ReadWrite.All` |
| **Admin Consent** | Required — Azure AD admin must grant tenant-wide consent |
| **Client Secret** | Generate under Certificates & secrets (max 2 year expiry) |

### Configuration Values

| Parameter | Value | Stored As |
|-----------|-------|-----------|
| `SP_TENANT_ID` | Intel Azure AD tenant ID | GitHub Secret |
| `SP_CLIENT_ID` | App registration client ID | GitHub Secret |
| `SP_CLIENT_SECRET` | App client secret | GitHub Secret |
| `SP_SITE_URL` | `https://intel.sharepoint.com/sites/IAO-Architecture` | GitHub Secret |
| `SP_DOC_LIBRARY` | `Shared Documents` | GitHub Secret |
| `SP_TARGET_FOLDER` | `Architecture/SAD` | GitHub Secret |

### Access Request Process

1. Go to **Azure Portal → App registrations → New registration**
2. Add `Sites.ReadWrite.All` application permission
3. Have an **Azure AD admin grant consent** (Settings → Enterprise Applications → Consent)
4. Create the target SharePoint site if it doesn't exist yet

---

## 6. GitHub Repository & Actions

### Required for Production

| Requirement | Detail |
|-------------|--------|
| **Repository** | Create on `github.com/intel-innersource` (Intel internal GitHub) |
| **GitHub Actions** | Must be enabled for the repository |
| **Secrets** | All 10 credentials from Sections 1-5 stored as Actions secrets |
| **Self-Hosted Runner** (optional) | Windows runner for SAP Negotiate auth — only needed if SAP basic auth unavailable |
| **GitHub PAT** (for reverse sync) | Personal Access Token with `repo` scope for Power Automate to trigger `repository_dispatch` |

### Secrets to Configure

| Secret Name | Source Section |
|-------------|---------------|
| `SMARTSHEET_TOKEN` | §2 Smartsheet |
| `IAPM_BEARER_TOKEN` | §3 IAPM (or use client_credentials) |
| `BIC_AUTH_TOKEN` | §4 BIC |
| `SAP_BI0_USER` | §1 SAP BI0 service account |
| `SAP_BI0_PASS` | §1 SAP BI0 service account |
| `SAP_DI0_USER` | §1 SAP DI0 service account |
| `SAP_DI0_PASS` | §1 SAP DI0 service account |
| `SP_TENANT_ID` | §5 SharePoint |
| `SP_CLIENT_ID` | §5 SharePoint |
| `SP_CLIENT_SECRET` | §5 SharePoint |
| `SP_SITE_URL` | §5 SharePoint |

---

## 7. RICEFW Data Quality Notes

The Smartsheet Object Tracker data is **real, live data from the IDM 2.0 program** — not generated or assumed. Analysis of the 1,635-row tracker reveals:

### Middleware Distribution

| Middleware | Count | % |
|-----------|-------|---|
| NA (no middleware) | 1,238 | 75.7% |
| MULESOFT | 235 | 14.4% |
| APIGEE | 104 | 6.4% |
| BODS | 27 | 1.7% |
| SFT | 26 | 1.6% |
| Other | 5 | 0.3% |

### Known Data Quality Issues

| Issue | Count | Detail |
|-------|-------|--------|
| **Description/Middleware mismatch** | 4 | Description mentions one middleware but column says another (e.g., FTSI1573: desc says "via BODS" but MW column says "MULESOFT") |
| **Status=Complete but Build=1%** | ~724 | Likely a formatting issue (1% may mean 100%) |
| **Missing Target Systems** | 42 | Objects in development status with blank Target System column |
| **Case inconsistency** | ~16 | "MULESOFT" vs "MuleSoft" vs "Mulesoft" |

> **These are source data quality issues in the Smartsheet tracker, not pipeline assumptions.** The pipeline faithfully renders whatever data the tracker contains. Tower architects should validate and correct entries in Smartsheet, which will flow through to the documents automatically.

---

## 8. Production Readiness Checklist

### Phase A: Access Provisioning (Parallel Requests)

| # | Request | System | Owner | Status |
|---|---------|--------|-------|--------|
| A1 | SAP service account with `S_SERVICE`, `S_DEVELOP`, `S_ADT_RES` (display only) on BI0 + DI0 | SAP Basis / AGS | EA Team | Not Started |
| A2 | Smartsheet service account + MFA exemption for IDM 2.0 workspace | Smartsheet Admin / PMO | EA Team | Not Started |
| A3 | Azure AD App Registration for SharePoint (`Sites.ReadWrite.All`) | Azure AD | EA Team | Not Started |
| A4 | Azure AD admin consent for SharePoint app | Azure AD Admin | IT Admin | Not Started |
| A5 | BIC service account with REVIEWER + export permissions | BIC/GBTEC Admin | EA Team | Not Started |
| A6 | IAPM API app registration (or confirm CSV cache is sufficient) | IAPM Team | EA Team | Not Started |
| A7 | GitHub repo creation on intel-innersource | GitHub Admin | EA Team | Not Started |
| A8 | GitHub PAT for Power Automate reverse sync | GitHub | EA Team | Not Started |

### Phase B: Configuration (After Access Granted)

| # | Task | Depends On |
|---|------|------------|
| B1 | Configure 11 GitHub Secrets | A1, A2, A3, A7 |
| B2 | Create SharePoint site + document library | A3, A4 |
| B3 | Create Power Automate flow (SharePoint → GitHub dispatch) | A7, A8, B2 |
| B4 | Push codebase to GitHub | A7 |
| B5 | Test forward workflow (generate + sync) | B1, B2, B4 |
| B6 | Test reverse workflow (SharePoint edit → regenerate) | B3, B5 |

### Phase C: Validation

| # | Test | Expected Result |
|---|------|----------------|
| C1 | Manual dispatch: generate single tower | 19+ MDs + HTMLs for FPR |
| C2 | Manual dispatch: generate all towers | 184 MDs + 184 HTMLs |
| C3 | Verify SharePoint upload | All HTML files in correct folder structure |
| C4 | Edit xlsx on SharePoint → verify regeneration | Updated document within 10 minutes |
| C5 | Cron trigger (Monday 06:00 UTC) | Full regeneration + sync |
| C6 | SAP OData extraction in CI | Dev object counts populated in §6.2 |
| C7 | Smartsheet live data in CI | RICEFW, RAID, Timeline populated |

---

<details>
<summary>View the Prompt Used</summary>

```markdown
Ensure there are no empty sections with placeholder text. Document the exact SAP roles needed,
Smartsheet API requirements, and all access needed for production automation. The RICEFW tracker
data shows BODS in descriptions but MuleSoft in the middleware column — clarify whether these are
real data or assumptions. Create build requirements to ensure a production-ready fully automated
document generation pipeline synced between GitHub and SharePoint.
```

</details>
