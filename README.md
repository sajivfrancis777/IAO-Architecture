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
|--------|---------||
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

## GitHub Actions

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `generate-architecture.yml` | Weekly (Mon 06:00 UTC), push to main, manual | Regenerate architecture docs |
| `sharepoint-reverse-sync.yml` | Manual | Reverse-sync from SharePoint |

## License

Internal use only.
