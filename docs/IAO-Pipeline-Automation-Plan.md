# IAO Architecture Pipeline — Automation Plan

## Executive Summary

This plan transforms the IAO Architecture documentation pipeline from a **local, manual-run workflow** into an **automated, scheduled, GitHub-backed pipeline** that regenerates TOGAF BDAT Systems Architecture Documents and syncs them to SharePoint on a recurring schedule.

**Current state:** 184 SAD documents generated locally across 8 towers (53 E2E, 19 FPR, 22 FTS-IF, 14 FTS-IP, 4 MDM, 26 OTC-IF, 35 OTC-IP, 15 PTP).

**Target state:** Fully automated weekly generation with credential management, version control, and SharePoint delivery.

---

## Pipeline Architecture

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        IAO ARCHITECTURE AUTOMATION PIPELINE                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ TRIGGERS                                                                         │  │
│  │  ┌────────────────┐  ┌────────────────┐  ┌──────────────────────────────────┐    │  │
│  │  │ Cron: Mon 6AM  │  │ Push to main   │  │ Manual dispatch (tower filter)  │    │  │
│  │  └────────────────┘  └────────────────┘  └──────────────────────────────────┘    │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│                                          v                                             │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ GITHUB ACTIONS WORKFLOW                                                          │  │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────────┐    │  │
│  │  │ 1. Checkout      │  │ 2. Install deps  │  │ 3. Load secrets to .env     │    │  │
│  │  └──────────────────┘  └──────────────────┘  └──────────────────────────────┘    │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│                                          v                                             │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ GENERATE                                                                         │  │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────────┐    │  │
│  │  │ gen_systems_arch │  │ gen_pdf (HTML)   │  │ Commit outputs to repo      │    │  │
│  │  │ --all (184 MDs)  │  │ --html-only      │  │ towers/*/output/            │    │  │
│  │  └──────────────────┘  └──────────────────┘  └──────────────────────────────┘    │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│                                          v                                             │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ DELIVER                                                                          │  │
│  │  ┌──────────────────────────────────┐  ┌──────────────────────────────────────┐  │  │
│  │  │ sync_sharepoint.py --all         │  │ Upload artifact to GitHub Actions   │  │  │
│  │  │ Graph API > Document Library     │  │ Retention: 30 days                  │  │  │
│  │  └──────────────────────────────────┘  └──────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Inventory

| File | Purpose | Status |
|------|---------|--------|
| `src/gen_systems_arch.py` | Generate TOGAF BDAT SAD markdown per capability | Done |
| `src/bpmn_parser.py` | Parse BPMN 2.0 XML → Mermaid flowcharts with professional styling | Done |
| `src/mermaid_builder.py` | Application Architecture diagrams with status-colored nodes | Done |
| `gen_pdf.py` | Convert MD to branded HTML with Mermaid.js + Font Awesome | Done |
| `sync_sharepoint.py` | Upload outputs to SharePoint via MS Graph API | Done |
| `src/config.py` | Centralized credential loader from .env | Done |
| `.env.example` | Credential template (SAP BI0/DI0, SharePoint, etc.) | Done |
| `.gitignore` | Excludes .env, __pycache__, generated outputs | Done |
| `requirements.txt` | Python dependencies for CI | Done |
| `.github/workflows/generate-architecture.yml` | Forward: generate + upload to SharePoint | Done |
| `.github/workflows/sharepoint-reverse-sync.yml` | Reverse: SharePoint edits → GitHub → regenerate | Done |

---

## Data Priority Chain (API-First)

The pipeline uses a strict priority chain for each data source. **API data always takes precedence** — input files are fallback for architect review/override, not the primary source.

### Priority Order per Section

| SAD Section | Priority 1 (API) | Priority 2 (File) | Priority 3 (Default) |
|-------------|-------------------|--------------------|----------------------|
| **Section 3 — Business Processes** | BPMN XML files (`input/bpmn/*.bpmn`) | xlsx "Business Architecture" tab | Placeholder text |
| **Section 5.1/5.2 — App Architecture** | Smartsheet RICEFW (live API) | xlsx CurrentFlows/FutureFlows tabs | Placeholder text |
| **Section 5.5 — RICEFW Inventory** | Smartsheet Object Tracker (live API) | xlsx tabs | Empty table |
| **Section 6.2 — SAP Dev Status** | SAP OData / ADT APIs (live probe) | xlsx "SAP Dev Status" tab | Placeholder table |
| **Section 7.1 — Roadmap** | Smartsheet timeline (live API) | Manual CSV | Placeholder text |
| **Section 7.2 — RAID Log** | Smartsheet RAID log (live API) | Manual CSV | Placeholder text |
| **Section 2.2/2.3 — Drivers/Criteria** | *(Architect-authored — no API)* | xlsx tabs | Sample data |
| **Section 6.3/6.4 — NFRs/Security** | *(Architect-authored — no API)* | xlsx tabs | Sample data |

### How It Works in Code

```
generate_capability():
  1. Load xlsx workbooks (CurrentFlows.xlsx, FutureFlows.xlsx)
     → Contains flows, context tabs, business processes
  2. Load BPMN XML files (input/bpmn/*.bpmn)
     → Overrides xlsx "Business Architecture" tab if present
  3. Load Smartsheet data (live API via SmartsheetLoader)
     → RICEFW objects, RAID log, timeline for Sections 5.5, 7.1, 7.2
  4. Load supplementary context
     → xlsx tabs > individual CSVs > template defaults
  5. Merge all sources with priority chain above
  6. Render via Jinja2 template
```

### Architect Override Workflow

When an architect updates an xlsx input file on SharePoint:
1. Power Automate detects the file change
2. Sends `repository_dispatch` event to GitHub
3. `sharepoint-reverse-sync.yml` downloads the updated file
4. Commits it to `main` branch
5. Push triggers `generate-architecture.yml` (via `paths: towers/**/input/**`)
6. Documents regenerate with the architect's edits taking effect
7. Outputs sync back to SharePoint

---

## Phase 1: Local Setup (Complete)

### 1.1 Credential Management

All API credentials live in a single `.env` file (never committed). The `src/config.py` module loads them via `python-dotenv` and exposes a typed `Config` dataclass.

**Credential sources:**

| Credential | Source | Refresh Cadence |
|------------|--------|-----------------|
| `SMARTSHEET_TOKEN` | Smartsheet > Account > API Access | Long-lived |
| `IAPM_BEARER_TOKEN` | Browser localStorage extraction | ~1 hour (session) |
| `BIC_AUTH_TOKEN` | Browser Network tab | ~1 hour (session) |
| `SAP_BI0_*` / `SAP_DI0_*` | Windows Negotiate (SSO) or SAP user/pass | Long-lived |
| `SP_*` (SharePoint) | Azure AD App Registration | Long-lived (client credential) |

**Local workflow:**
1. Copy `.env.example` to `.env`
2. Fill in your credentials
3. Run any script — credentials auto-loaded via `from src.config import cfg`

### 1.2 Generation Pipeline

```bash
# Generate all 184 SAD markdown files (8 towers)
python -m src.gen_systems_arch --all

# Generate branded HTML with Mermaid.js
python gen_pdf.py --html-only

# Sync to SharePoint (requires SP_* credentials)
python sync_sharepoint.py --all
```

---

## Phase 2: GitHub Repository Setup

### 2.1 Initial Push

```bash
git init
git add .
git commit -m "feat: IAO Architecture Pipeline — initial commit"
git remote add origin https://github.com/intel-innersource/iao-architecture-pipeline.git
git push -u origin main
```

### 2.2 Repository Structure

```
iao-architecture-pipeline/
├── .github/workflows/
│   └── generate-architecture.yml     # CI/CD workflow
├── src/
│   ├── config.py                     # Credential loader
│   ├── gen_systems_arch.py           # SAD generator
│   ├── xlsx_loader.py                # Input parser
│   ├── bpmn_parser.py                # BPMN XML parser
│   ├── context_loader.py             # Context builder
│   ├── mermaid_builder.py            # Diagram generator
│   └── ...
├── templates/
│   └── systems_architecture.md.j2    # Jinja2 template
├── towers/
│   ├── E2E/                          # 53 capabilities
│   ├── FPR/                          # 19 capabilities
│   ├── FTS-IF/                       # 22 capabilities
│   ├── FTS-IP/                       # 14 capabilities
│   ├── MDM/                          # 4 capabilities
│   ├── OTC-IF/                       # 26 capabilities
│   ├── OTC-IP/                       # 35 capabilities
│   └── PTP/                          # 15 capabilities
├── gen_pdf.py
├── sync_sharepoint.py
├── requirements.txt
├── .env.example                      # Template (committed)
├── .env                              # Secrets (NOT committed)
└── .gitignore
```

### 2.3 GitHub Secrets Configuration

Navigate to **Settings > Secrets and variables > Actions** and add:

| Secret Name | Value |
|-------------|-------|
| `SMARTSHEET_TOKEN` | Your Smartsheet API token |
| `IAPM_BEARER_TOKEN` | IAPM Bearer token (manual refresh) |
| `BIC_AUTH_TOKEN` | BIC session token (manual refresh) |
| `SP_TENANT_ID` | Azure AD tenant ID |
| `SP_CLIENT_ID` | Azure AD app client ID |
| `SP_CLIENT_SECRET` | Azure AD app client secret |
| `SP_SITE_URL` | `https://intel.sharepoint.com/sites/IAO-Architecture` |
| `SP_DOC_LIBRARY` | `Shared Documents` |
| `SP_TARGET_FOLDER` | `Architecture/SAD` |

> **Note:** SAP BI0/DI0 use Windows Negotiate (SSO), which requires a Windows runner or service account. For CI, either use a GitHub self-hosted runner on Windows or switch to SAP basic auth credentials stored as secrets.

---

## Phase 3: GitHub Actions Automation

### 3.1 Workflow: `generate-architecture.yml`

**Triggers:**
- **Scheduled:** Every Monday at 06:00 UTC (cron)
- **Push to main:** Only when `src/`, `templates/`, or `towers/**/input/**` change
- **Manual dispatch:** With optional tower filter input

**Steps:**
1. Checkout repository
2. Setup Python 3.12 with pip cache
3. Install dependencies from `requirements.txt`
4. Write `.env` from GitHub Secrets
5. Run `gen_systems_arch --all` (or `--tower X` for manual)
6. Run `gen_pdf.py --html-only`
7. Commit updated `towers/*/output/` back to repo
8. Run `sync_sharepoint.py --all`
9. Upload artifacts (30-day retention)

### 3.2 SAP Authentication in CI

SAP APIs use Windows Negotiate (SPNEGO/Kerberos), which won't work on GitHub's Ubuntu runners. Options:

| Option | Complexity | Recommendation |
|--------|-----------|----------------|
| **Self-hosted Windows runner** | Medium | Best for full SSO compatibility |
| **SAP service account (basic auth)** | Low | Add `SAP_BI0_USER`/`SAP_BI0_PASS` as secrets |
| **Cached SAP data** | None | Probe locally, commit JSON results to repo |

**Recommended approach:** Run SAP probes locally (they're infrequent), commit the resulting JSON to the repo. CI uses cached data. SAP probe refresh is manual or self-hosted.

---

## Phase 4: SharePoint Integration

### 4.1 Azure AD App Registration

1. Go to **Azure Portal > App registrations > New registration**
2. Name: `IAO-Architecture-Pipeline`
3. Supported account type: **Single tenant**
4. After creation, note the **Application (client) ID** and **Directory (tenant) ID**
5. Under **Certificates & secrets > Client secrets**, create a new secret
6. Under **API permissions**, add:
   - `Microsoft Graph > Application permissions > Sites.ReadWrite.All`
7. **Grant admin consent** (requires Azure AD admin)

### 4.2 SharePoint Sync Behavior

`sync_sharepoint.py` uploads to:

```
SharePoint Site
└── Shared Documents
    └── Architecture/SAD
        ├── E2E/
        │   ├── html/
        │   │   ├── E2E-08-Architecture.html
        │   │   ├── E2E-80-Architecture.html
        │   │   └── ...
        │   └── md/
        │       ├── E2E-08-Architecture.md
        │       └── ...
        ├── FPR/
        │   ├── html/
        │   └── md/
        └── ... (all 8 towers)
```

### 4.3 Features

- Authenticates via OAuth2 client_credentials grant
- Resolves SharePoint site URL to MS Graph site/drive IDs
- Uploads files up to 4 MB via simple PUT (sufficient for HTML/MD)
- Rate-limited (200ms between uploads) for compliance
- Supports `--tower X` for single-tower sync or `--all`

### 4.4 Bidirectional Sync Architecture

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          BIDIRECTIONAL SYNC ARCHITECTURE                               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ FORWARD FLOW (Generate > SharePoint)                                             │  │
│  │  ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────────┐    │  │
│  │  │ GitHub Actions   │----->│ gen_systems_arch  │----->│ sync_sharepoint.py   │    │  │
│  │  │ (cron / push)    │      │ gen_pdf.py        │      │ (MS Graph upload)    │    │  │
│  │  └──────────────────┘      └──────────────────┘      └──────────────────────┘    │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                        │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ REVERSE FLOW (SharePoint > GitHub > Regenerate)                                  │  │
│  │  ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────────┐    │  │
│  │  │ Architect edits  │----->│ Power Automate   │----->│ repository_dispatch  │    │  │
│  │  │ xlsx on SP       │      │ detects change    │      │ to GitHub Actions    │    │  │
│  │  └──────────────────┘      └──────────────────┘      └──────────────────────┘    │  │
│  │                                                               v                  │  │
│  │  ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────────┐    │  │
│  │  │ Forward flow     │<-----│ Push to main     │<-----│ reverse-sync.yml     │    │  │
│  │  │ triggers         │      │ triggers gen      │      │ downloads + commits  │    │  │
│  │  └──────────────────┘      └──────────────────┘      └──────────────────────┘    │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

**Power Automate Setup (SharePoint → GitHub):**

1. **Trigger**: "When a file is created or modified" in the SharePoint document library
2. **Filter**: File path contains `/input/` (only input files, not generated outputs)
3. **Parse path**: Extract tower and capability from the file path
4. **HTTP action**: POST to `https://api.github.com/repos/{owner}/{repo}/dispatches`
   - Header: `Authorization: Bearer {GITHUB_PAT}`
   - Body:
     ```json
     {
       "event_type": "sharepoint-file-updated",
       "client_payload": {
         "tower": "<extracted tower>",
         "capability": "<extracted capability>",
         "file_name": "<changed file name>",
         "sp_path": "<full SharePoint path>"
       }
     }
     ```

**Conflict Prevention:**
- Forward sync commits with `[skip ci]` to prevent infinite loops
- Reverse sync commits trigger forward generation (no `[skip ci]`)
- SharePoint uploads only go to `output/` folders; reverse sync only downloads from `input/` folders

---

## Phase 5: Operational Runbook

### Daily / As-Needed (Local)

| Task | Command |
|------|---------|
| Regenerate one capability | `python -m src.gen_systems_arch --tower FPR --cap DS-020` |
| Regenerate one tower | `python -m src.gen_systems_arch --tower FPR` |
| Regenerate all towers | `python -m src.gen_systems_arch --all` |
| Generate HTML for one tower | `python gen_pdf.py --html-only --tower FPR` |
| Sync one tower to SharePoint | `python sync_sharepoint.py --tower FPR` |
| Refresh SAP probe data | `python probe_sap_devobjects.py --negotiate --compare` |

### Weekly (Automated via GitHub Actions)

The Monday 06:00 UTC cron job automatically:
1. Regenerates all 184 SAD markdowns
2. Generates all HTML outputs
3. Commits changes to the repository
4. Syncs to SharePoint

### Manual Trigger

Go to **GitHub > Actions > Generate Architecture Docs > Run workflow** and optionally specify a tower shortcode.

---

## Credential Refresh Guide

| Credential | How to Refresh | Frequency |
|------------|---------------|-----------|
| Smartsheet token | Smartsheet > Account > Personal Settings > API Access > Generate | Yearly (or when revoked) |
| IAPM Bearer | Browser F12 > Console > extract from localStorage | As needed (session-based) |
| BIC Auth | Browser F12 > Network > copy Authorization header | As needed (session-based) |
| SAP (Negotiate) | Automatic via Windows SSO (local only) | N/A |
| SAP (basic auth) | Update `.env` or GitHub Secrets | When password changes |
| SharePoint | Azure AD app > Certificates & secrets > New client secret | Before expiry (max 2 years) |

---

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| IAPM/BIC tokens expire during CI | Medium | Cache data locally; tokens only needed for live probe runs |
| SAP Negotiate won't work on Ubuntu runner | High | Use cached JSON or self-hosted Windows runner |
| SharePoint admin consent not granted | High | Engage Azure AD admin early in setup |
| Smartsheet MFA blocks sheet access | Low | 44 sheets blocked; live data for accessible sheets, manual for blocked |
| Large file uploads (>4 MB) | Low | HTML files are ~150KB average; not a concern |
| GitHub Actions minutes quota | Low | Pipeline runs ~5 min; free tier has 2,000 min/month |

---

## Implementation Checklist

- [x] Credential management (`.env.example`, `src/config.py`, `.gitignore`)
- [x] SAD generation for all 8 towers (184 capabilities)
- [x] HTML output generation (184 files)
- [x] E2E tower discovery fix (53 capabilities now generating)
- [x] Professional BPMN diagrams (Mermaid + Font Awesome icons, color-coded start/end events)
- [x] Professional Application Architecture diagrams (status-colored nodes, deployed style)
- [x] HTML legends for all diagram types (BPMN + Architecture)
- [x] GitHub Actions forward workflow (`.github/workflows/generate-architecture.yml`)
- [x] GitHub Actions reverse workflow (`.github/workflows/sharepoint-reverse-sync.yml`)
- [x] SharePoint sync script (`sync_sharepoint.py`)
- [x] Python dependency file (`requirements.txt`)
- [x] API-first data priority chain documented
- [ ] Push to GitHub (requires repo creation on GitHub)
- [ ] Configure GitHub Secrets (10 secrets)
- [ ] Azure AD App Registration for SharePoint
- [ ] Grant admin consent for `Sites.ReadWrite.All`
- [ ] Create Power Automate flow for reverse sync
- [ ] Test GitHub Actions end-to-end (forward + reverse)
- [ ] Validate SharePoint folder structure and uploads
- [ ] Set up self-hosted Windows runner (optional, for SAP probes)

---

<details>
<summary>View the Prompt Used</summary>

```markdown
run the script to update all of the MD files, I am hoping the MD files can be generated into PDF with a markdown preview enhanced and stored as a PDF.

We need to ensure that there is a central file where I can update the API credentials so that automated runs can be achieved. Keep things private where necessary, possible within .env files since this stack will get backed up to GitHub.

Once in GitHub, we need to be able to execute scripts on schedule to update the stack and have it sync to SharePoint, will need to include the API to authenticate us to SharePoint as well.

Can you come up with a plan?
```

</details>
