# IAO Architecture Pipeline

Automated generation of **TOGAF BDAT Architecture Documents** for the Intel IDM 2.0 (SAP S/4HANA transformation) program.

This pipeline produces per-capability **Systems Architecture Documents (SAD)**, **RICEFW Trackers**, **Testing Reports**, and **Interactive Dashboards** across 8 towers and ~184 capabilities — published to **GitHub Pages** and **SharePoint**.

**Live Portal**: [sajivfrancis777.github.io/IAO-Architecture](https://sajivfrancis777.github.io/IAO-Architecture/)

---

## Repositories

| Repository | Purpose | URL |
|---|---|---|
| **IAO-Architecture** | Pipeline code, templates, tower inputs, generated documents, CI/CD workflows | [github.com/sajivfrancis777/IAO-Architecture](https://github.com/sajivfrancis777/IAO-Architecture) |
| **IAO-Architecture-Input-Portal** | React + AG Grid data editor for tower architects — edits CurrentFlows/FutureFlows XLSX | [github.com/sajivfrancis777/IAO-Architecture-Input-Portal](https://github.com/sajivfrancis777/IAO-Architecture-Input-Portal) |
| **IAO-Architecture (Pages)** | Published portal — interactive architecture docs with sidebar, dashboards, release filtering | [sajivfrancis777.github.io/IAO-Architecture](https://sajivfrancis777.github.io/IAO-Architecture/) |

---

## What the Pipeline Produces

| Document Type | Count | Description |
|---|---|---|
| **Systems Architecture Documents (SAD)** | 184 | TOGAF BDAT architecture per L2 capability — business process flows, application landscape, integration diagrams, data architecture, technology stack, RICEFW summary, RAID items |
| **RICEFW Trackers** | 143 | Per-capability development object status — FS, TDD, Build, FUT dates with completion percentages, sourced from Smartsheet Object Tracker |
| **Testing & Quality Reports** | 196 | Per-capability test readiness — JIRA defect counts, test case coverage, FUT status, quality gates |
| **Interactive Dashboards** | 9 | Per-tower + program-level Plotly.js dashboards — 3 pillars (Architecture, Development, Testing) with tower chip filters, release dropdown, unique systems by release, defect severity/aging charts |
| **Summary Documents** | 9 | L0 (tower), L1 (process group), and program-level architecture rollups |
| **Tower Landing Pages** | 8 | Portal entry points with capability navigation and doc links |
| **Capability Pages** | 189 | Per-capability portal pages with links to SAD, RICEFW, Testing docs |

All documents are generated in Markdown, converted to HTML with live Mermaid.js diagrams, and published to GitHub Pages with a unified portal experience (sidebar navigation, release filtering, search).

---

## Towers

| Tower | Shortcode | Capabilities | Description |
|---|---|---|---|
| Forecast, Planning & Replenishment | FPR | 19 | Financial planning, costing, capital management |
| Order to Cash — Intel Foundry | OTC-IF | 26 | Sales, billing, receivables (Foundry) |
| Order to Cash — Intel Products | OTC-IP | 35 | Sales, billing, receivables (Products) |
| Forecast to Stock — Intel Foundry | FTS-IF | 23 | Demand planning, inventory, logistics (Foundry) |
| Forecast to Stock — Intel Products | FTS-IP | 14 | Demand planning, inventory, logistics (Products) |
| Procure to Pay | PTP | 15 | Procurement, AP, vendor management |
| Master Data Management | MDM | 4 | Material, customer, vendor master data |
| End-to-End | E2E | 53 | Cross-tower integration scenarios |

---

## Data Sources

The pipeline integrates data from multiple enterprise systems. Each source enriches a specific section of the architecture documents.

### Live API (Automated via CI)

| Source | Data Provided | Document Section |
|---|---|---|
| **Smartsheet** — RAID Logs (Master + E2E) | 3,600+ risks, actions, issues, decisions | §6.3 RAID Summary |
| **Smartsheet** — SCP-PMO WRICEF | 188 SCP RICEFW objects with status | §6.2 RICEFW Status |
| **Smartsheet** — E2E Workplan | 401 program tasks and milestones | §7.1 Roadmap |
| **Smartsheet** — EA Gantt | 437 timeline entries | §7.1 Roadmap |
| **JIRA** | Test cases, defects, execution results (project IAODTM) | Testing Reports |
| **IAPM** | 30,000+ application portfolio entries (hosting, lifecycle, ownership) | §4 Application Architecture |

### Manual Export (MFA-Blocked Sheets)

These Smartsheet sheets require MFA and cannot be accessed via API. Export as Excel from the Smartsheet browser app and place in the corresponding folder.

| Smartsheet Folder | Sheet Name | Local Folder | Status |
|---|---|---|---|
| Intel IDM Object Tracker | S4 [R3] Intel IDM Object Tracker | `data/smartsheet/manual/object_trackers/` | 1,643 rows × 213 cols |
| Intel IDM Deliverables Tracker | IDM 2.0 Deliverables Log & Sign off Tracker | `data/smartsheet/manual/boundary_apps/` | 841 rows × 25 cols |
| Intel IDM Change Control | IDM 2.0 Program Change Request Log | `data/smartsheet/manual/change_requests/` | 1,714 rows × 116 cols |
| Intel IDM Object Tracker | Intel IDM 2.0 RICEFW Request Console | `data/smartsheet/manual/request_console/` | 2,090 rows × 31 cols |
| Intel IDM 2.0 Ph 1 Integrated Plan | Master Program Timeline | `data/smartsheet/manual/timelines/` | Pending location |

After placing xlsx files, run the converter script to prepare them for the pipeline.

### Architect-Provided Inputs

| Input | Location | Who Maintains |
|---|---|---|
| Current-state process flows | `towers/<TOWER>/<L1>/<CAP>/input/data/CurrentFlows.xlsx` | Tower Architects |
| Future-state process flows | `towers/<TOWER>/<L1>/<CAP>/input/data/FutureFlows.xlsx` | Tower Architects |
| Per-release flow variants | `towers/<TOWER>/<L1>/<CAP>/input/data/R1_CurrentFlows.xlsx` etc. | Tower Architects |
| BPMN process models | `towers/<TOWER>/<L1>/<CAP>/input/bpmn/*.bpmn` | Exported from Signavio/BIC |
| Tower configuration | `towers/<TOWER>/tower.yaml` | Pipeline team |

---

## CI/CD Automation

Three GitHub Actions workflows automate the full lifecycle. Documents regenerate automatically on input changes or on schedule.

| Workflow | Trigger | Purpose |
|---|---|---|
| **Generate Architecture Docs** | Push to main (src/templates/inputs), daily schedule, manual | Fetch API data → generate all documents → convert to HTML → commit outputs |
| **Deploy to GitHub Pages** | After generation completes, manual | Build portal with sidebar, toolbar, release filtering → deploy to GitHub Pages |
| **Data Refresh** | Daily weekday schedule (06:00 UTC), manual | Fetch latest Smartsheet + JIRA data → commit updated cache → trigger site rebuild |

The pipeline also supports **SharePoint two-way sync** — architects edit Excel workbooks on SharePoint, and a Power Automate flow triggers regeneration via GitHub Actions.

---

## AI Chatbot Integration

Five MCP (Model Context Protocol) servers expose enterprise data as tools for GitHub Copilot Chat, enabling architects to query live data conversationally.

| MCP Server | Status | Example Query |
|---|---|---|
| **iao-smartsheet** | Working | "What RICEFW objects are in FPR DS-020?" |
| **iao-iapm** | Working (CSV) | "What's the IAPM status of MuleSoft?" |
| **iao-jira** | Working | "How many open defects in OTC-IF?" |
| **iao-sap-odata** | Placeholder | "Show transports for FPRI1234" |
| **iao-bic** | Placeholder | "Find BIC process models for DS-020" |

A web-based chatbot (accessible from the GitHub Pages portal without VS Code) is planned as a future phase using Azure Functions as the backend.

---

## Phases & Roadmap

### Phase 1 — Foundation ✅
- Pipeline framework with Jinja2 templates, tower/capability folder structure, and tower.yaml configuration
- Core generators for SAD, RICEFW Tracker, Testing Report, Dashboard, and Summary documents
- Excel workbook input format (CurrentFlows / FutureFlows with 8 tabs per workbook)
- BPMN parser for Signavio/BIC process model integration
- Mermaid diagram generation (6 diagram types including ArchiMate-style)
- IAPM application portfolio integration (30K+ apps with API and CSV fallback)
- GitHub Actions CI/CD (generate → deploy to GitHub Pages)
- Portal with sidebar navigation, tower landing pages, and capability pages

### Phase 2 — Live Data Integration ✅
- Smartsheet API integration for RAID logs, WRICEF, E2E Workplan, and EA Gantt
- Manual export workflow for MFA-blocked sheets (Object Tracker, Deliverables, Change Requests, RICEFW Console)
- XLSX-to-CSV converter for manual Smartsheet exports
- Smartsheet data injection into SADs (§6.2 RICEFW Status, §6.3 RAID Summary, §6.4 Timeline)
- JIRA integration for defects, test cases, and test execution results
- Data folder reorganization: live API data (CI-fetched) vs manual exports (git-tracked)
- Per-release document generation (R1–R5 filtered views) with release filtering on the portal

### Phase 3 — SAP Development Object Analysis 🔄 In Progress
- SSL certificate installation in STRUST on BI0 and DI0 (pending approval from Basis & Platforms)
- abapGit connectivity from SAP to GitHub for ABAP object extraction
- New Smartsheet columns: SAP Package Name, SAP Object ID, L2 Capability ID
- KDD ID and Link mapping to RICEFW trackers (OTC architecture team request)
- RICEFW → SAP Package → ABAP Object traceability in architecture documents
- Clean core compliance analysis (complementary to existing clean core assessment initiatives)
- Code quality scanning: dead code, deprecated APIs, hard-coded values, programming guideline adherence
- Impact analysis: dependency chain tracing for change management and effort estimation
- Functional and technical specification validation against actual implemented code
- Security and authorization review: direct DB access, hard-coded credentials, RFC patterns
- Knowledge continuity: auto-generated code-level summaries for Deloitte-to-Intel handover

### Phase 4 — Web Chatbot & Extended Integrations 📋 Planned
- Azure Functions backend for web-based chatbot on the GitHub Pages portal
- Same MCP tool logic adapted from stdio to HTTP transport
- Azure AD authentication restricting access to Intel employees
- SAP OData integration for dev object inventory, transport status, and CDS views
- SAP BIC/Signavio API integration for live process model queries
- ServiceNow integration for incident → tower → capability mapping
- SharePoint reverse sync via Power Automate (architect edits → auto-regenerate)

### Phase 5 — Operational Maturity 📋 Future
- Full API coverage for all Smartsheet sheets (pending MFA policy resolution with workspace admin)
- Automated knowledge handover documentation for production support transition
- Transport and deployment governance with Git-based audit trail (SOX compliance)
- Architecture review board dashboards and compliance reporting
- Steady-state operational metrics and KPI tracking
- Corporate GitHub migration (Intel GHE or Azure Static Web Apps) — see [Automation & Migration Plan](docs/IAO-Pipeline-Automation-and-Migration-Plan.md)

---

## Value Across the Project Lifecycle

| Phase | What the Pipeline Provides | Key Consumers |
|---|---|---|
| **Design** | TOGAF BDAT documents, Mermaid diagrams, capability hierarchy | Solution architects, enterprise architects |
| **Build** | Live RICEFW status, dev object inventory, RAID log | Tower leads, program managers |
| **Integration Test** | System dependency maps, interface inventory, current vs future state | Test leads, integration testers |
| **UAT** | Testing reports, defect tracking (JIRA), readiness dashboards | QA leads, business testers |
| **Go-Live** | Final architecture baseline, all RICEFW in Deployed status | Go-live command center, operations |
| **Post-Go-Live** | Incident → Tower → Capability lookup, AI chatbot queries | L2/L3 support, ServiceNow teams |
| **Steady State** | Versioned architecture (Git), change tracking, compliance audits | Governance, audit, architecture review boards |

---

## Credential Summary

All API integrations follow the same pattern: **API-first with graceful CSV fallback**. No credential is ever committed to the repository — they are stored as environment variables locally or as encrypted GitHub Actions Secrets in CI.

| Credential | System | Status |
|---|---|---|
| SMARTSHEET_TOKEN | Smartsheet API | Working |
| JIRA_PAT / JIRA_BASE_URL | JIRA REST API | Working |
| IAPM data | IAPM Application Portfolio | Working (CSV cache, 30K apps) |
| SP_TENANT_ID / SP_CLIENT_ID / SP_CLIENT_SECRET | SharePoint Sync | Working |
| SAP BI0/DI0 credentials | SAP S/4HANA OData | Pending (access request + STRUST SSL) |
| BIC_AUTH_TOKEN | SAP BIC / Signavio | Pending (auth token) |
| ANTHROPIC_API_KEY | AI Chatbot (web) | Planned (Phase 4) |

---

## Quick Start

1. **Clone** the repository and install Python dependencies (Python 3.12+, requirements.txt)
2. **Configure** credentials in .env (copy from .env.example)
3. **Place inputs** — Excel workbooks in the tower/capability input folders
4. **Generate** — run the main generator for all towers
5. **Enrich** — run the Smartsheet update script to inject live data
6. **Publish** — convert to HTML and push to trigger GitHub Pages deployment
7. **View** — browse the portal at the GitHub Pages URL

For targeting specific towers or capabilities, add tower and capability flags to any generator command.

---

## Key Design Principles

- **You maintain the inputs, the pipeline does everything else** — schedule it daily or trigger on every change
- **Graceful degradation** — every API is optional; without a token, the pipeline falls back to cached data or generates placeholders
- **Single source of truth** — centralized tower registry for metadata, tower.yaml for capability definitions
- **No manual document assembly** — all architecture documents are generated from structured data, never hand-edited
- **Version-controlled architecture** — every document change is tracked in Git with full diff history
