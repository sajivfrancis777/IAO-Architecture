# IAO Architecture Pipeline

Python-based automation pipeline for generating **TOGAF BDAT-aligned** Solution Architecture Documents (SADs) across the IDM 2.0 (SAP S/4HANA transformation) program.

Pulls live data from enterprise APIs (Smartsheet, IAPM, SAP BIC, SAP S/4HANA OData), enriches it, and produces per-capability architecture documents — Business, Data, Application, and Technology architecture — for each tower.

## Towers

| Tower | Description |
|-------|-------------|
| FPR | Forecast, Planning & Replenishment |
| OTC-IF | Order to Cash — Intel Foundry |
| OTC-IP | Order to Cash — Intel Products |
| FTS-IF | Forecast to Stock — Intel Foundry |
| FTS-IP | Forecast to Stock — Intel Products |
| PTP | Procure to Pay |
| MDM | Master Data Management |
| E2E | End-to-End (cross-tower) |

## Project Structure

```
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── .env.example                # Credential template (copy to .env)
├── .gitignore
│
├── scripts/                    # Pipeline CLI entry points
│   ├── update_sad_from_smartsheet.py
│   ├── gen_pdf.py
│   ├── gen_xlsx_templates.py
│   ├── scaffold_inputs.py
│   ├── backfill_bpmn_to_xlsx.py
│   ├── backfill_sample_data.py
│   ├── cleanup_csvs.py
│   └── sync_sharepoint.py
│
├── src/                        # Reusable Python library modules
│   ├── smartsheet_loader.py    #   Smartsheet data loader
│   ├── bpmn_parser.py          #   BPMN XML parser
│   ├── csv_parser.py           #   CSV parsing utilities
│   ├── xlsx_loader.py          #   Excel workbook loader
│   ├── mermaid_builder.py      #   Mermaid diagram generator
│   ├── gen_systems_arch.py     #   Systems architecture doc generator
│   ├── diff_engine.py          #   Document diff engine
│   ├── context_loader.py       #   Tower/capability context loader
│   ├── iapm_lookup.py          #   IAPM application lookup
│   └── config.py               #   Configuration management
│
├── mcp_servers/                # MCP tool servers for Copilot integration
│   ├── smartsheet_server.py    #   Smartsheet API tools (live + CSV fallback)
│   ├── iapm_server.py          #   IAPM application portfolio tools
│   ├── jira_server.py          #   JIRA integration tools (placeholder)
│   ├── sap_odata_server.py     #   SAP OData tools (placeholder)
│   └── bic_server.py           #   SAP BIC process design tools (placeholder)
│
├── templates/                  # Jinja2 templates for doc generation
│   ├── capability_architecture.md.j2
│   ├── systems_architecture.md.j2
│   ├── CurrentFlows_TEMPLATE.xlsx
│   └── FutureFlows_TEMPLATE.xlsx
│
├── towers/                     # Tower data (one subfolder per tower)
│   ├── FPR/
│   ├── OTC-IF/
│   ├── OTC-IP/
│   ├── FTS-IF/
│   ├── FTS-IP/
│   ├── PTP/
│   ├── MDM/
│   └── E2E/
│
├── data/                       # Cached/extracted data
│   ├── smartsheet/             #   Smartsheet CSV exports
│   ├── iapm/                   #   IAPM application data
│   ├── bic/                    #   BIC process model data
│   ├── sap_odata/              #   SAP OData extractions
│   ├── enriched/               #   Enriched flow data
│   ├── mermaid/                #   Generated Mermaid diagrams
│   └── xref/                   #   Cross-reference mappings
│
├── docs/                       # Planning & architecture documentation
├── notebooks/                  # Jupyter notebooks (future)
├── config/                     # Configuration files
├── .github/workflows/          # GitHub Actions (scheduled generation)
├── reference/                  # Reference scripts & audit data
└── _archive/                   # Archived exploration/probe scripts
```

## Pipeline Scripts

All scripts live in `scripts/` and are run from the project root:

| Script | Purpose |
|--------|---------|
| `scripts/update_sad_from_smartsheet.py` | Update all SADs with live Smartsheet data (roadmap, RICEFW status, RAID log) |
| `scripts/gen_pdf.py` | Convert architecture Markdown to styled HTML and PDF |
| `scripts/gen_xlsx_templates.py` | Generate multi-tab Excel input templates for tower architects |
| `scripts/scaffold_inputs.py` | Deploy input templates and upgrade flow CSVs across all capabilities |
| `scripts/backfill_bpmn_to_xlsx.py` | Populate Business Architecture tabs from BPMN XML exports |
| `scripts/backfill_sample_data.py` | Pre-fill supplementary tabs with contextually grounded sample data |
| `scripts/cleanup_csvs.py` | Remove legacy CSV inputs superseded by xlsx workbooks |
| `scripts/sync_sharepoint.py` | Upload generated architecture docs to SharePoint Online |

## Setup

### Prerequisites

- Python 3.12+
- Access to Smartsheet API (token)
- Optional: IAPM, SAP BIC, SAP S/4HANA credentials for full pipeline

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd IAO-JPNotebookPython

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\Activate.ps1

# Activate (Linux/macOS)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
# Copy the environment template
cp .env.example .env

# Edit .env and add your credentials
# At minimum, set SMARTSHEET_TOKEN for the core pipeline
```

See [.env.example](.env.example) for all available configuration variables.

## Usage

### Generate / Update Architecture Documents

```bash
# Update all tower SADs with live Smartsheet data
python scripts/update_sad_from_smartsheet.py

# Update a specific tower
python scripts/update_sad_from_smartsheet.py --tower FPR

# Preview changes without writing
python scripts/update_sad_from_smartsheet.py --dry-run
```

### Generate Output Formats

```bash
# Generate HTML + PDF for all towers
python scripts/gen_pdf.py

# Generate HTML only for a specific tower
python scripts/gen_pdf.py --tower FPR --html-only
```

### Scaffold New Capabilities

```bash
# Deploy input templates to all capabilities
python scripts/gen_xlsx_templates.py --deploy

# Backfill BPMN data into workbooks
python scripts/backfill_bpmn_to_xlsx.py --tower FPR
```

## MCP Servers

The `mcp_servers/` directory contains [Model Context Protocol](https://modelcontextprotocol.io/) servers that expose enterprise data as tools for GitHub Copilot:

- **Smartsheet** — Live sheet queries + CSV cache fallback (RICEFW, RAID, timelines)
- **IAPM** — Application portfolio search across 30K+ applications
- **JIRA** — Test cases, defects, sprint status (placeholder)
- **SAP OData** — Development objects, transports (placeholder)
- **BIC** — BPMN process models (placeholder)

## CI/CD Workflows

Three GitHub Actions workflows automate the full document lifecycle:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `generate-architecture.yml` | Weekly (Mon 06:00 UTC), push to main, manual | Regenerate MDs, update from Smartsheet, generate HTML, sync to SharePoint |
| `sharepoint-reverse-sync.yml` | Power Automate webhook, manual | Pull updated Excel inputs from SharePoint → commit → triggers forward generation |
| `deploy-pages.yml` | After `Generate Architecture Docs` completes, manual | Deploy HTML outputs to GitHub Pages for browser viewing |

### Pipeline Flow

```
 SharePoint (architect edits xlsx)
        │
        ▼
 Power Automate → repository_dispatch
        │
        ▼
 sharepoint-reverse-sync.yml
   ├── Download updated file from SharePoint via Graph API
   ├── Commit to towers/<TOWER>/<CAP>/input/data/
   └── Push to main  ───────────────────────┐
                                             ▼
                                generate-architecture.yml
                                  ├── Generate architecture MDs
                                  ├── Update SADs from Smartsheet
                                  ├── Generate HTML outputs
                                  ├── Commit outputs to repo
                                  ├── Sync HTML/MD/SVG to SharePoint
                                  └── Trigger deploy-pages.yml
                                             │
                                             ▼
                                      deploy-pages.yml
                                        └── Deploy HTML to GitHub Pages
```

---

## SharePoint Two-Way Sync

The pipeline supports two-way sync between GitHub and SharePoint so that tower architects can update Excel input files directly on SharePoint without needing Git access.

### How It Works

1. **Forward sync** (GitHub → SharePoint): After docs are generated, `sync_sharepoint.py` uploads HTML, Markdown, and SVG files to the SharePoint document library.
2. **Reverse sync** (SharePoint → GitHub): When an architect updates an Excel file on SharePoint, a Power Automate flow triggers `sharepoint-reverse-sync.yml` to pull the file into the repo and regenerate docs.

### Folder Structure on SharePoint

The sync maps the GitHub `towers/` structure to SharePoint:

```
SharePoint: <SP_DOC_LIBRARY>/<SP_TARGET_FOLDER>/
  ├── FPR/
  │   ├── DS-001/
  │   │   ├── DS-001-Architecture.html
  │   │   ├── DS-001-Architecture.md
  │   │   └── svg/
  │   └── DS-002/
  ├── OTC-IF/
  ├── PTP/
  └── ...
```

**Default mapping** (from `.env`):
- `SP_DOC_LIBRARY` = `Shared Documents`
- `SP_TARGET_FOLDER` = `Architecture/SAD`

### Syncing Specific Towers

To sync only certain towers instead of all:

```bash
# Sync a single tower to SharePoint
python scripts/sync_sharepoint.py --tower FPR

# Sync all towers
python scripts/sync_sharepoint.py --all
```

In the GitHub Actions manual dispatch, enter a tower shortcode to limit the scope:

> **Actions → Generate Architecture Docs → Run workflow → Tower shortcode**: `FPR`

### Setting Up Reverse Sync (SharePoint → GitHub)

#### Prerequisites

1. **Azure AD App Registration** with `Sites.ReadWrite.All` Graph API permission
2. **GitHub Personal Access Token** (PAT) with `repo` scope for Power Automate to call the dispatch API
3. **Power Automate** (or Logic App) flow on the SharePoint site

#### Step 1: Configure GitHub Secrets

Go to **Settings → Secrets and variables → Actions** and add:

| Secret | Description |
|--------|-------------|
| `SMARTSHEET_TOKEN` | Smartsheet API token |
| `SP_TENANT_ID` | Azure AD tenant ID |
| `SP_CLIENT_ID` | Azure AD app client ID |
| `SP_CLIENT_SECRET` | Azure AD app client secret |
| `SP_SITE_URL` | SharePoint site URL (e.g., `https://intel.sharepoint.com/sites/IAO-Architecture`) |
| `SP_DOC_LIBRARY` | Document library name (default: `Shared Documents`) |
| `SP_TARGET_FOLDER` | Target folder path (default: `Architecture/SAD`) |

Optional (for full pipeline): `IAPM_BEARER_TOKEN`, `BIC_AUTH_TOKEN`

#### Step 2: Create Power Automate Flow

Create a flow that fires when an `.xlsx` file changes in the SharePoint document library:

1. **Trigger**: _When a file is modified (properties only)_ in the `Architecture/SAD` folder
2. **Filter**: File extension = `.xlsx`
3. **Parse path**: Extract tower and capability from the file path
   - Example: `Architecture/SAD/FPR/DS-001/input/data/CurrentFlows.xlsx`
   - Tower = `FPR`, Capability = `DS-001`, File = `CurrentFlows.xlsx`
4. **HTTP action**: Send `repository_dispatch` to GitHub:

```json
POST https://api.github.com/repos/<OWNER>/<REPO>/dispatches
Headers:
  Authorization: Bearer <GITHUB_PAT>
  Accept: application/vnd.github+json
Body:
{
  "event_type": "sharepoint-file-updated",
  "client_payload": {
    "tower": "FPR",
    "capability": "DS-001",
    "file_name": "CurrentFlows.xlsx",
    "sp_path": "Architecture/SAD/FPR/DS-001/input/data/CurrentFlows.xlsx"
  }
}
```

#### Step 3: Manual Reverse Sync (Alternative)

If Power Automate is not configured, you can trigger the reverse sync manually:

> **Actions → SharePoint Reverse Sync → Run workflow**
>
> - Tower shortcode: `FPR`
> - Capability ID: `DS-001`
> - File name: `CurrentFlows.xlsx`

This downloads the specified file from SharePoint and commits it to the repo. The push then triggers the forward generation workflow automatically.

### Sync Sequence Summary

| Step | What Happens | Triggered By |
|------|-------------|--------------|
| 1 | Architect edits Excel on SharePoint | Manual |
| 2 | Power Automate sends `repository_dispatch` | SharePoint file change trigger |
| 3 | `sharepoint-reverse-sync.yml` downloads file, commits | `repository_dispatch` event |
| 4 | `generate-architecture.yml` regenerates docs | Push to `main` (paths: `towers/**/input/**`) |
| 5 | Updated HTML/MD/SVG uploaded to SharePoint | End of generation workflow |
| 6 | `deploy-pages.yml` deploys HTML to GitHub Pages | After generation workflow completes |

---

## Viewing HTML Outputs

GitHub does not render HTML files inline — it shows the source code instead. Three options for viewing the generated architecture HTML files:

### Option 1: GitHub Pages (Recommended)

After enabling GitHub Pages, all HTML outputs are served at:

```
https://<username>.github.io/IAO-Architecture/towers/<TOWER>/<CAP>/output/<CAP>-Architecture.html
```

**Setup:**
1. Go to **Settings → Pages**
2. Source: **GitHub Actions**
3. The `deploy-pages.yml` workflow automatically deploys after each doc generation
4. An index page at the root lists all towers and capabilities

### Option 2: htmlpreview.github.io

For quick viewing without Pages setup, prepend the raw GitHub URL:

```
https://htmlpreview.github.io/?https://github.com/<OWNER>/<REPO>/blob/main/towers/FPR/DS-001/output/DS-001-Architecture.html
```

### Option 3: Local

```bash
# Open a specific HTML file locally
start towers/FPR/DS-001/output/DS-001-Architecture.html
```

---

## Scheduling Options

The `generate-architecture.yml` workflow runs weekly by default. To change the schedule:

| Frequency | Cron Expression | Description |
|-----------|----------------|-------------|
| Daily | `0 6 * * *` | Every day at 06:00 UTC |
| Weekly (default) | `0 6 * * 1` | Every Monday at 06:00 UTC |
| Bi-weekly | `0 6 1,15 * *` | 1st and 15th of each month |
| Monthly | `0 6 1 * *` | First day of each month |

Edit the `cron` line in `.github/workflows/generate-architecture.yml`:

```yaml
on:
  schedule:
    - cron: "0 6 * * *"   # Change to desired frequency
```

Or trigger an ad-hoc run from **Actions → Generate Architecture Docs → Run workflow**.

---

## License

Internal use only.
