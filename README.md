# IAO Architecture Pipeline

Automated generation of **TOGAF BDAT Architecture Documents** for the IDM 2.0 (SAP S/4HANA transformation) program.

This pipeline produces three document types per capability — **SAD** (Systems Architecture Document), **BPD** (Business Process Document), and **PM** (Project Management) — by consuming structured inputs (Excel workbooks + live API data) and rendering them through Jinja2 templates into HTML, PDF, and Markdown outputs.

---

## How It Works

```
  ┌─────────────────────────────────┐
  │         INPUTS (You Maintain)   │
  │                                 │
  │  Excel Workbooks (.xlsx)        │  ← Architect-editable, synced via SharePoint
  │  BPMN Process Models (.bpmn)    │  ← Exported from Signavio/BIC
  │  Tower Config (tower.yaml)      │  ← Capability registry per tower
  │  API Credentials (.env)         │  ← Smartsheet, IAPM, SAP, JIRA tokens
  └──────────────┬──────────────────┘
                 │
                 ▼
  ┌─────────────────────────────────┐
  │     PIPELINE (Automated)        │
  │                                 │
  │  1. Parse xlsx + BPMN inputs    │
  │  2. Query live APIs             │
  │  3. Resolve system metadata     │
  │  4. Generate Mermaid diagrams   │
  │  5. Render BDAT templates       │
  │  6. Inject Smartsheet data      │
  │  7. Produce HTML + PDF          │
  │  8. Sync to SharePoint + Pages  │
  └──────────────┬──────────────────┘
                 │
                 ▼
  ┌─────────────────────────────────┐
  │       OUTPUTS (Generated)       │
  │                                 │
  │  <CAP>-Architecture.html        │  → GitHub Pages + SharePoint
  │  <CAP>-Architecture.pdf         │  → SharePoint
  │  <CAP>-Architecture.md          │  → GitHub repo
  │  svg/ diagrams                  │  → Embedded in HTML
  └─────────────────────────────────┘
```

**Key principle**: You maintain the inputs. The pipeline does everything else. Schedule it to run daily, hourly, or on every input change — the outputs always reflect the latest data.

---

## Quick Start

### Step 1 — Clone & Install

```bash
git clone <repo-url>
cd IAO-JPNotebookPython
python -m venv .venv
.venv\Scripts\Activate.ps1          # Windows
pip install -r requirements.txt
```

### Step 2 — Configure Credentials

```bash
cp .env.example .env
# Edit .env with your API tokens (see "API Access" section below)
```

### Step 3 — Populate Inputs

Place your Excel workbooks in the correct tower/capability folders:

```
towers/<TOWER>/<Process Group>/<CAP-ID>/input/data/
  ├── CurrentFlows.xlsx     ← Current-state process flows
  └── FutureFlows.xlsx      ← Future-state process flows
```

Or deploy blank templates to all capabilities:

```bash
python scripts/gen_xlsx_templates.py --deploy
```

### Step 4 — Generate Documents

```bash
# Generate all architecture documents (all towers, all capabilities)
python -m src.gen_systems_arch --all

# Update with live Smartsheet data (RICEFW, RAID, roadmap)
python scripts/update_sad_from_smartsheet.py

# Produce HTML + PDF outputs
python scripts/gen_pdf.py
```

### Step 5 — View Results

- **GitHub Pages**: `https://<org>.github.io/IAO-Architecture/`
- **SharePoint**: Synced to `Shared Documents / Architecture/SAD/`
- **Local**: Open any `output/docs/systems-architecture/*.html` in browser

---

## Inputs — What You Maintain

Everything the pipeline needs comes from two sources: **files you edit** and **APIs it queries**.

### Excel Workbooks (Primary Input)

Each capability has two multi-tab workbooks in `towers/<TOWER>/<L1>/<CAP>/input/data/`:

| File | Tabs | Purpose |
|------|------|---------|
| `CurrentFlows.xlsx` | Flows, Business Drivers, Success Criteria, Business Architecture, NFRs, Security Controls, SAP Dev Status, Recommendations | Current-state architecture across all BDAT domains |
| `FutureFlows.xlsx` | Same 8 tabs | Future-state architecture (S/4HANA target) |

**The Flows tab is the core input** — each row defines a flow chain (source → interface → target) with lane assignments, system names, and status. The pipeline parses these into Mermaid diagrams, IAPM-linked nodes, and change impact analysis.

The remaining 7 tabs provide supplementary context for each BDAT section. If blank, the pipeline generates placeholder text.

> **Tip**: Use `python scripts/backfill_sample_data.py` to pre-fill supplementary tabs with contextually grounded sample data based on the systems and flows already defined.

### BPMN Process Models (Optional)

Place Signavio/BIC-exported `.bpmn` XML files in `towers/<TOWER>/<L1>/<CAP>/input/bpmn/`. The pipeline parses swim lanes, tasks, gateways, and sequence flows into Section 3 (Business Process Diagrams).

Naming convention: `<CAP-ID>-<step>_<Step_Name>.bpmn` (e.g., `DS-020-020_Perform Cumulative Costing Run.bpmn`)

### Tower Configuration

Each tower has a `tower.yaml` defining its capabilities:

```yaml
tower:
  name: Finance Plan To Report
  shortcode: FPR
capabilities:
  DS-020:
    name: "Perform Product Costing and Inventory Valuation"
    l1: "DS Provide Decision Support"
```

If a capability name is missing from `tower.yaml`, the pipeline auto-resolves it from BPMN XML definitions, Smartsheet sub-tower names, or the L1 directory name.

### API Credentials (.env)

Copy `.env.example` to `.env` and populate the tokens you have access to:

| Variable | Source | Impact |
|----------|--------|--------|
| `SMARTSHEET_TOKEN` | Smartsheet API admin | Live RICEFW status, RAID items, delivery timelines |
| `IAPM_BEARER_TOKEN` | Azure AD | Application portfolio metadata (hosting, lifecycle, ownership) |
| `BIC_AUTH_TOKEN` | Browser DevTools | BPMN process model names from Signavio/BIC |
| `SAP_BI0_HOST/USER/PASS` | SAP access request | Dev object inventory, transport status, CDS views |
| `SAP_DI0_HOST/USER/PASS` | SAP access request | Same for Products system |
| `JIRA_BASE_URL/USER_EMAIL/API_TOKEN` | JIRA PAT | Test case readiness, defect counts, sprint status |
| `SP_TENANT_ID/CLIENT_ID/CLIENT_SECRET` | Azure AD app | SharePoint two-way sync |
| `SP_SITE_URL/DOC_LIBRARY/TARGET_FOLDER` | SharePoint admin | SharePoint upload path |

**Graceful degradation**: Every API is optional. Without a token, the pipeline falls back to cached CSV/Excel data or generates placeholder sections. Add tokens as access is provisioned — no code changes needed.

---

## Pipeline Scripts

All scripts run from the project root. The three bolded scripts form the core generation pipeline.

| Script | What It Does |
|--------|-------------|
| **`python -m src.gen_systems_arch --all`** | **Generate** all architecture Markdown documents from inputs |
| **`python scripts/update_sad_from_smartsheet.py`** | **Enrich** with live Smartsheet data (RICEFW, RAID, roadmap) |
| **`python scripts/gen_pdf.py`** | **Produce** HTML + PDF outputs from Markdown |
| `python scripts/sync_sharepoint.py --all` | Upload outputs to SharePoint |
| `python scripts/gen_xlsx_templates.py --deploy` | Deploy blank Excel templates to all capabilities |
| `python scripts/scaffold_inputs.py` | Deploy input templates + upgrade legacy CSVs to 47-column xlsx |
| `python scripts/backfill_bpmn_to_xlsx.py` | Populate Business Architecture tab from BPMN XML |
| `python scripts/backfill_sample_data.py` | Pre-fill supplementary tabs with contextual sample data |
| `python scripts/cleanup_csvs.py` | Remove legacy CSVs superseded by xlsx workbooks |

### Targeting Specific Towers / Capabilities

Most scripts accept `--tower` and `--cap` flags:

```bash
python -m src.gen_systems_arch --tower FPR              # One tower
python -m src.gen_systems_arch --tower FPR --cap DS-020 # One capability
python scripts/gen_pdf.py --tower FPR --html-only       # HTML only, one tower
python scripts/update_sad_from_smartsheet.py --dry-run   # Preview without writing
```

---

## CI/CD — Automated Execution

Three GitHub Actions workflows automate the full lifecycle. Once inputs and credentials are set, documents regenerate automatically.

### Workflows

| Workflow | Trigger | What It Does |
|----------|---------|-------------|
| `generate-architecture.yml` | Schedule (cron), push to `main`, manual | Full pipeline: generate MDs → enrich from Smartsheet → produce HTML/PDF → sync to SharePoint |
| `sharepoint-reverse-sync.yml` | Power Automate webhook, manual | Pull updated xlsx from SharePoint → commit → triggers generation |
| `deploy-pages.yml` | After generation completes, manual | Deploy HTML outputs to GitHub Pages |

### Scheduling

Edit the cron in `.github/workflows/generate-architecture.yml`:

```yaml
on:
  schedule:
    - cron: "0 6 * * *"     # Daily at 06:00 UTC
    # - cron: "0 * * * *"   # Hourly
    # - cron: "0 6 * * 1"   # Weekly (Monday)
```

Or trigger manually: **Actions → Generate Architecture Docs → Run workflow**

### End-to-End Pipeline Flow

```
 SharePoint (architect edits xlsx)
        │
        ▼
 Power Automate → repository_dispatch
        │
        ▼
 sharepoint-reverse-sync.yml
   ├── Download updated xlsx from SharePoint via Graph API
   ├── Commit to towers/<TOWER>/<CAP>/input/data/
   └── Push to main  ───────────────────────┐
                                             ▼
                                generate-architecture.yml
                                  ├── Generate architecture MDs
                                  ├── Update SADs from Smartsheet
                                  ├── Generate HTML/PDF outputs
                                  ├── Commit outputs to repo
                                  ├── Sync to SharePoint
                                  └── Trigger deploy-pages.yml
                                             │
                                             ▼
                                      deploy-pages.yml
                                        └── Deploy HTML to GitHub Pages
```

### GitHub Secrets Required

Configure in **Settings → Secrets and variables → Actions**:

| Secret | Required For |
|--------|-------------|
| `SMARTSHEET_TOKEN` | Smartsheet live data injection |
| `SP_TENANT_ID` | SharePoint sync |
| `SP_CLIENT_ID` | SharePoint sync |
| `SP_CLIENT_SECRET` | SharePoint sync |
| `SP_SITE_URL` | SharePoint sync |
| `SP_DOC_LIBRARY` | SharePoint sync (default: `Shared Documents`) |
| `SP_TARGET_FOLDER` | SharePoint sync (default: `Architecture/SAD`) |

Optional: `IAPM_BEARER_TOKEN`, `BIC_AUTH_TOKEN`, `JIRA_*`, `SAP_*`

---

## Towers

| Tower | Shortcode | Description |
|-------|-----------|-------------|
| Forecast, Planning & Replenishment | FPR | Financial planning, costing, capital management |
| Order to Cash — Intel Foundry | OTC-IF | Sales, billing, receivables (Foundry) |
| Order to Cash — Intel Products | OTC-IP | Sales, billing, receivables (Products) |
| Forecast to Stock — Intel Foundry | FTS-IF | Demand planning, inventory, logistics (Foundry) |
| Forecast to Stock — Intel Products | FTS-IP | Demand planning, inventory, logistics (Products) |
| Procure to Pay | PTP | Procurement, AP, vendor management |
| Master Data Management | MDM | Material, customer, vendor master data |
| End-to-End | E2E | Cross-tower integration scenarios |

---

## Project Structure

```
IAO-JPNotebookPython/
│
├── src/                          # Core library modules
│   ├── gen_systems_arch.py       #   Main orchestrator (tower.yaml → template rendering)
│   ├── cap_name_resolver.py      #   Multi-source capability name resolution
│   ├── bpmn_parser.py            #   BPMN 2.0 XML parser
│   ├── csv_parser.py             #   Flow CSV parser (25/47 column schemas)
│   ├── xlsx_loader.py            #   Multi-tab Excel workbook parser
│   ├── mermaid_builder.py        #   Mermaid diagram generator
│   ├── iapm_lookup.py            #   IAPM application metadata resolver
│   ├── diff_engine.py            #   Current vs. future flow change analysis
│   ├── smartsheet_loader.py      #   Smartsheet data loader (API + CSV fallback)
│   ├── context_loader.py         #   Supplementary context CSV loader
│   ├── doc_format.py             #   Document formatting utilities
│   └── config.py                 #   Centralized configuration (.env loader)
│
├── scripts/                      # Pipeline CLI entry points
│   ├── update_sad_from_smartsheet.py
│   ├── gen_pdf.py
│   ├── gen_xlsx_templates.py
│   ├── scaffold_inputs.py
│   ├── backfill_bpmn_to_xlsx.py
│   ├── backfill_sample_data.py
│   ├── cleanup_csvs.py
│   └── sync_sharepoint.py
│
├── templates/                    # Jinja2 document templates
│   ├── systems_architecture.md.j2    # BDAT architecture template
│   ├── capability_architecture.md.j2 # SAP-level architecture template
│   ├── CurrentFlows_TEMPLATE.xlsx    # Blank input workbook (current-state)
│   ├── FutureFlows_TEMPLATE.xlsx     # Blank input workbook (future-state)
│   └── assets/                       # Cover banner, CSS assets
│
├── mcp_servers/                  # MCP tool servers (Copilot integration)
│   ├── smartsheet_server.py      #   ✅ Working — RICEFW, RAID, timelines
│   ├── iapm_server.py            #   ✅ Working — 30K+ app portfolio lookups
│   ├── jira_server.py            #   🟡 Placeholder — needs JIRA credentials
│   ├── sap_odata_server.py       #   🟡 Placeholder — needs SAP gateway access
│   └── bic_server.py             #   🟡 Placeholder — needs BIC auth token
│
├── towers/                       # Tower data (8 towers)
│   ├── FPR/                      #   tower.yaml + L1 process groups + L2 capabilities
│   ├── OTC-IF/                   #   Each capability: input/data/*.xlsx → output/docs/*.html
│   ├── OTC-IP/
│   ├── FTS-IF/
│   ├── FTS-IP/
│   ├── PTP/
│   ├── MDM/
│   └── E2E/
│
├── data/                         # Cached API data (CSV fallbacks)
│   ├── smartsheet/               #   Object trackers, RAID logs
│   ├── iapm/                     #   IAPM_All_Solutions.csv (30K+ apps)
│   ├── bic/                      #   BIC process data (when provisioned)
│   └── sap_odata/                #   SAP OData extractions (when provisioned)
│
├── .github/workflows/            # CI/CD automation
│   ├── generate-architecture.yml #   Full generation + SharePoint sync
│   ├── sharepoint-reverse-sync.yml # SharePoint → GitHub reverse sync
│   └── deploy-pages.yml          #   Deploy to GitHub Pages
│
├── docs/                         # Planning documentation (reference only)
├── reference/                    # API probe utilities (reference only)
├── _archive/                     # Archived exploration scripts (inactive)
│
├── requirements.txt              # Python dependencies
├── .env.example                  # Credential template
└── .gitignore
```

### Capability Folder Structure

Each capability under a tower follows this layout:

```
towers/<TOWER>/<Process Group>/<CAP-ID>/
├── input/
│   ├── bpmn/                              # BPMN XML exports (optional)
│   │   └── <CAP>-<step>_<name>.bpmn
│   └── data/                              # ◀ ARCHITECT-EDITABLE INPUTS
│       ├── CurrentFlows.xlsx              #   Current-state flows + context
│       └── FutureFlows.xlsx               #   Future-state flows + context
└── output/
    └── docs/
        └── systems-architecture/
            ├── <CAP>-Architecture.html    # ◀ Generated → SharePoint + Pages
            ├── <CAP>-Architecture.pdf     # ◀ Generated → SharePoint
            └── <CAP>-Architecture.md      #   Generated → GitHub only
```

---

## API Access

Each API enriches a specific BDAT domain. All are optional — the pipeline degrades gracefully.

| API | BDAT Domain | What It Provides | Without It |
|-----|-------------|-----------------|-----------|
| **Smartsheet** | All | Live RICEFW object status, RAID items, delivery timelines | Cached CSV — goes stale within days |
| **IAPM** | Application | App portfolio (30K+ apps) — hosting, lifecycle, ownership | Offline CSV — works but may miss changes |
| **SAP BIC** | Business | BPMN process model names, capability titles from Signavio | Manual BPMN XML export from BIC UI |
| **SAP OData** | Technology | Dev object inventory, transport status, CDS views | Manual collection from SAP GUI |
| **JIRA** | Project Mgmt | Test readiness, defect counts, sprint burn-down | No automated QA visibility |
| **SharePoint** | Delivery | Two-way sync of inputs/outputs with architect workspace | Manual file copy |

### Requesting Access (Intel Internal)

| System | How to Request |
|--------|---------------|
| Smartsheet | API token from Smartsheet admin — Bearer token with read access to IAO workspace |
| IAPM | Auto-granted via Azure AD for most Intel employees |
| JIRA | Create Personal Access Token at JIRA profile → needs IDM 2.0 project read access |
| SAP S/4HANA | Request `S_SERVICE` authorization role for BI0/DI0 OData catalog via SAP access form |
| SAP BIC | Access to BIC portal; extract token from browser DevTools (F12 → Network → Authorization header) |
| SharePoint | Azure AD App Registration with `Sites.ReadWrite.All` + GitHub PAT for Power Automate |

---

## MCP Servers (Copilot Integration)

Five [Model Context Protocol](https://modelcontextprotocol.io/) servers in `mcp_servers/` expose enterprise data as tools for GitHub Copilot. Registered in `.vscode/settings.json`, they run as stdio subprocesses.

| Server | Status | Sample Query |
|--------|--------|-------------|
| `iao-smartsheet` | ✅ Working | _"Get RICEFW objects for FPR DS-020"_ |
| `iao-iapm` | ✅ Working | _"Search IAPM for SAP S/4HANA"_ |
| `iao-jira` | 🟡 Placeholder | _"Get defects for PTP tower"_ |
| `iao-sap-odata` | 🟡 Placeholder | _"Get dev objects for transport K9xxxxx"_ |
| `iao-bic` | 🟡 Placeholder | _"Search BIC for DS-020 process models"_ |

Placeholder servers return stub data with instructions for provisioning credentials. Once tokens are added to `.env`, they activate automatically.

---

## SharePoint Two-Way Sync

### Forward Sync (GitHub → SharePoint)

After documents are generated, `sync_sharepoint.py` uploads HTML/PDF/SVG to SharePoint:

```bash
python scripts/sync_sharepoint.py --all                    # All towers
python scripts/sync_sharepoint.py --tower FPR              # One tower
python scripts/sync_sharepoint.py --all --include-inputs   # Include xlsx inputs (first-time bootstrap)
```

### Reverse Sync (SharePoint → GitHub)

When an architect edits an xlsx on SharePoint, a Power Automate flow triggers `sharepoint-reverse-sync.yml`:

1. Architect saves `CurrentFlows.xlsx` on SharePoint
2. Power Automate sends `repository_dispatch` to GitHub
3. Workflow downloads the file, commits to `towers/<TOWER>/<CAP>/input/data/`
4. Push triggers `generate-architecture.yml` → regenerates docs → syncs back

Manual alternative: **Actions → SharePoint Reverse Sync → Run workflow** with tower, capability, and file name.

### Power Automate Setup

Create a flow triggered on `.xlsx` file change in the SharePoint document library:

```json
POST https://api.github.com/repos/<OWNER>/<REPO>/dispatches
Headers:
  Authorization: Bearer <GITHUB_PAT>
Body:
{
  "event_type": "sharepoint-file-updated",
  "client_payload": {
    "tower": "FPR",
    "capability": "DS-020",
    "file_name": "CurrentFlows.xlsx",
    "sp_path": "Architecture/SAD/FPR/DS-020/input/data/CurrentFlows.xlsx"
  }
}
```

---

## Viewing Documents

| Method | URL / Path | Best For |
|--------|-----------|----------|
| **GitHub Pages** | `https://<org>.github.io/IAO-Architecture/` | Interactive browsing with Mermaid diagrams, sidebar navigation |
| **SharePoint** | `Shared Documents > Architecture/SAD > ...` | Architect access, PDF download |
| **Local** | `towers/<TOWER>/<L1>/<CAP>/output/docs/systems-architecture/*.html` | Development / preview |

---

## Security

- Repository is **Private** (GitHub Enterprise Cloud)
- GitHub Pages is **Private** (only repo collaborators)
- `.env` is in `.gitignore` — never committed
- All API tokens stored in GitHub Secrets for CI/CD
- SharePoint sync uses OAuth2 client credentials (no user passwords)
- Generated docs contain Intel confidential architecture data — do not make public

---

## License

Internal use only — Intel confidential. Do not make this repository or its contents publicly accessible.
