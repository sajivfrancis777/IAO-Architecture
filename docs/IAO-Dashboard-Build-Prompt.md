# IAO Architecture Dashboard — Engineering Prompt

> **Purpose:** Hand this prompt to a coding agent (Claude, Copilot, etc.) to extend the existing IAO Architecture Pipeline with a unified dashboard, additional auto-generated documents, and an AI chatbot. The prompt is grounded in the actual repository structure as of March 2026.

---

## REPOSITORY CONTEXT

**GitHub:** `https://github.com/sajivfrancis777/IAO-Architecture`
**Branch:** `main`
**Local:** `C:\Users\sajivfra\Documents\IAO-JPNotebookPython`

Review the following before proceeding:

| What to Review | Where |
|----------------|-------|
| GitHub Actions workflows (all paused — manual dispatch only) | `.github/workflows/` |
| Core pipeline orchestrator | `src/gen_systems_arch.py` |
| Smartsheet data injection into SADs | `scripts/update_sad_from_smartsheet.py` |
| Smartsheet data loader (RICEFW + RAID from CSV) | `src/smartsheet_loader.py` |
| MCP server implementations (5 servers, 20 tools) | `mcp_servers/` |
| Existing data files (Smartsheet CSVs, IAPM catalog) | `data/` |
| Generated architecture documents (HTML, PDF, MD, SVG) | `towers/**/output/` |
| GitHub Pages deployment (deploy-pages.yml builds `_site/`) | `.github/workflows/deploy-pages.yml` |
| Jinja2 templates for SAD generation | `templates/` |
| Pipeline configuration and credentials | `src/config.py`, `.env.example` |
| Existing documentation | `docs/` |

---

## EXISTING STACK (what is already built and working)

### Working Pipeline (end-to-end)
- **Input:** Architects fill `towers/<TOWER>/<ProcessGroup>/<CAP>/input/data/*.xlsx` (47-column extended schema across 8 tabs: Flows, BusinessDrivers, SuccessCriteria, NFRs, SecurityControls, SAPDevStatus, Recommendations, ProcessFlows)
- **Generation:** `src/gen_systems_arch.py` orchestrates: xlsx → `csv_parser.py` → `iapm_lookup.py` (30,372 apps) → `mermaid_builder.py` → `diff_engine.py` → `context_loader.py` → Jinja2 → Markdown
- **Smartsheet enrichment:** `scripts/update_sad_from_smartsheet.py` injects live RICEFW status (§6.2), project roadmap (§7.1), and RAID log (§7.2) from Smartsheet API
- **HTML/PDF export:** `scripts/gen_pdf.py` converts MD → styled HTML with Mermaid.js CDN diagrams
- **SharePoint sync:** `scripts/sync_sharepoint.py` uploads HTML/PDF/SVG via Microsoft Graph API (OAuth2 client credentials)
- **GitHub Pages:** `deploy-pages.yml` builds `_site/` with themed landing page (tower cards) and per-tower pages with capability tables

### Working Data Sources
| Source | Integration | Data Volume | Key Files |
|--------|-------------|-------------|-----------|
| **Smartsheet** | Live API (token auth) + CSV cache | 1,635 RICEFW objects × 212 cols; RAID logs | `data/smartsheet/object_trackers/s4_r3_object_tracker.csv`, `data/smartsheet/raid/master_raid_log.csv` |
| **IAPM** | CSV fallback (30K apps) | 30,372 apps × 54 cols | `data/iapm/IAPM_All_Solutions.csv` |
| **SharePoint** | Graph API (client credentials OAuth2) | xlsx input files + HTML/PDF outputs | `scripts/sync_sharepoint.py` |

### Placeholder (not yet implemented)
| Source | MCP Server | Status | Blocker |
|--------|-----------|--------|---------|
| **JIRA** | `mcp_servers/jira_server.py` — 4 tools defined, all return `not_implemented` | Needs credentials | `JIRA_BASE_URL`, `JIRA_USER_EMAIL`, `JIRA_API_TOKEN` not in .env |
| **SAP OData (BI0/DI0)** | `mcp_servers/sap_odata_server.py` — 4 tools defined | Network reachable, auth-gated | S_SERVICE SAP role not granted; Kerberos/NTLM negotiate auth |
| **SAP BIC (Signavio)** | `mcp_servers/bic_server.py` — 4 tools defined | API endpoints reverse-engineered | Token auth (ephemeral browser token); Spring Boot SIREN API at `/process-design/frontend/api` |

### Known Smartsheet Sheet IDs (already mapped)
| Sheet | ID | Current Usage |
|-------|-----|--------------|
| Object Tracker (RICEFW master) | `5077868279189380` | ✅ Consumed → §6.2, §7.1 |
| Master RAID Log | `2062365868642180` | ✅ Consumed → §7.2 |
| E2E RAID Log | `2147893813137284` | ✅ Consumed → §7.2 |
| Deliverables Tracker | `8568208059486084` | ❌ Discovered but not consumed |
| Change Request Log | `8701667910307716` | ❌ Discovered but not consumed |
| RICEFW Request Console | `216957114601348` | ❌ Discovered but not consumed |

### Architecture Scale
- **8 towers:** E2E, FPR, FTS-IF, FTS-IP, MDM, OTC-IF, OTC-IP, PTP
- **~188 capabilities** across all towers (scaffolded with input/output directories)
- **Currently generated:** Systems Architecture Documents (SAD) per capability — 11-section TOGAF BDAT format (Business, Data, Application, Technology) with Mermaid diagrams, IAPM-linked system nodes, RICEFW inventory, RAID logs, and project roadmaps
- **SAD filtering rule (IMPLEMENTED):** SAD §6.2 (RICEFW Status) and §7.1 (Roadmap) show **only active items** — completed (`10. Object Complete`) and rejected/cancelled (`99. Rejected/Cancelled/On Hold`) objects are excluded. The separate RICEFW Register (Phase 2) carries the complete inventory including all statuses.

---

## WHAT NEEDS TO BE BUILT / EXTENDED

### PHASE 1 — Fix Capability-Specific Smartsheet Extraction (PREREQUISITE)

**Problem:** The current Smartsheet extraction pulls tower-level data but does not correctly filter/categorize by individual capability (e.g., DS-020, DC-010). The pipeline needs to extract per-capability data so that each SAD reflects only the RICEFW objects, RAID items, and timeline milestones that belong to that specific capability.

**Files to fix:**
- `scripts/update_sad_from_smartsheet.py` — review the 3-tier matching logic (by object ID → by sub-team → tower-level fallback) and ensure it actually filters to the correct capability
- `src/smartsheet_loader.py` — verify column mapping for capability-level filtering (the Object Tracker CSV has `Sub-Tower` and `Object ID` fields that can be mapped to capabilities)
- `mcp_servers/smartsheet_server.py` — the `get_ricefw_objects` and `get_raid_items` tools should accept capability-level filters, not just tower

**Deliverables:**
- Fixed extraction logic that correctly maps Smartsheet rows to individual capabilities
- Validation by running a single capability (e.g., `FPR/DS-020`) and confirming only its RICEFW objects appear in §6.2, only its RAID items in §7.2, only its milestones in §7.1

---

### PHASE 2 — Additional Automated Documents

Extend the Python pipeline to produce two additional auto-generated documents alongside the existing SAD.

#### Document 2: RICEFW / Objects Register (by Capability)

Extract and generate a living register tracking **ALL** RICEFW objects across the program — including completed, rejected, and in-progress items. This is the comprehensive reference, complementing the SAD which only shows active items needing attention.

- **Source:** Smartsheet Object Tracker (sheet `5077868279189380`) — already loaded into `data/smartsheet/object_trackers/s4_r3_object_tracker.csv` (1,635 rows × 212 cols)
- **Available fields:** Object ID, Type (R/I/C/E/F/W), Description, Tower, Sub-Tower, Status, Source System, Target System, Middleware, Boundary App, FS/TDD/Build/FUT completion %, FS/TDD/Build/FUT end dates, Complexity, Release, Rev Trac ID
- **ALSO consume** the currently unused sheets: Deliverables Tracker (`8568208059486084`), Change Request Log (`8701667910307716`), RICEFW Request Console (`216957114601348`)
- **Output:** Structured JSON at `data/dashboard/ricefw.json` AND a rendered HTML register **grouped by capability**
- **Include all statuses:** Active, Completed, Rejected/Cancelled — with clear status indicators
- **Cross-reference:** Link RICEFW objects to SAD capabilities where system relationships exist (use Objects Tracker `Sub-Tower` field + IAPM app IDs to match)
- Update automatically every time the pipeline runs

**Relationship to SAD:** The SAD §6.2 shows only active RICEFW items (objects with status other than `10. Object Complete` or `99. Rejected/Cancelled/On Hold`). This register shows the full picture including all completed work.

**New file:** `scripts/extract_ricefw.py`

#### Document 3: Testing Register (JIRA Extract, by Capability)

Extract testing data from JIRA and generate a living test register **grouped by capability** — all test statuses included. This should:

- **Connect to JIRA** using existing placeholder `mcp_servers/jira_server.py` (needs real implementation)
  - Credentials: `JIRA_BASE_URL` (`https://jira.intel.com`), `JIRA_USER_EMAIL`, `JIRA_API_TOKEN` → stored as GitHub Secrets
  - Tool specs already defined: `get_test_cases(tower, capability_name, status_filter)`, `get_defects(tower, capability_name, severity)`, `get_sprint_status(tower)`, `search_issues(jql)`
- **Extract:** Test cases, defects, test execution status grouped by Tower and Capability
- **Track:** Total tests, passed, failed, blocked, not-run — per tower and per capability
- **Output:** `data/dashboard/testing.json` AND rendered HTML register
- Update automatically on each pipeline run
- **Graceful degradation:** If JIRA credentials are not configured, produce an empty/placeholder JSON with a "JIRA not configured" status flag

**New file:** `scripts/extract_testing_jira.py`
**Updated file:** `mcp_servers/jira_server.py` — implement the 4 existing tool stubs

---

### PHASE 3 — Unified Dashboard Frontend

Build a single self-contained dashboard deployed to GitHub Pages alongside the existing tower/capability architecture views.

#### Data Layer
- **New script:** `scripts/export_dashboard_json.py` — merges all sources into a unified `data/dashboard/dashboard.json`:
  - SAD metadata (from towers: system counts, flow chain counts, per-capability summary)
  - RICEFW status (from `ricefw.json`)
  - Testing health (from `testing.json`)
  - RAID summary (from Smartsheet RAID logs)
  - IAPM system catalog summary (from `data/iapm/IAPM_All_Solutions.csv`)
  - Timestamp of last pipeline run
- **Updated GitHub Actions workflow:** Run all extractors in sequence: gen_systems_arch → update_sad → extract_ricefw → extract_testing_jira → export_dashboard_json → gen_pdf → commit → deploy

#### Global Summary View (Landing Page)
- KPI cards: total systems, total processes, total RICEFW objects, overall test pass rate, last updated timestamp
- System architecture network graph (from SAD flow chain data)
- RICEFW completion status by tower (bar/donut chart)
- Testing health by tower (pass/fail/blocked stacked bar)
- RAID summary by tower (open risk/issue counts)

#### Tower & Capability Drill-Down Views
- Navigation by Tower → Capability (sidebar or tab structure)
- Each Tower view shows:
  - Systems assigned to that tower (from SAD system inventory)
  - RICEFW objects by status for that tower
  - Test execution summary for that tower
  - RAID items for that tower
- Each Capability view shows the same, scoped to that capability
- Link from each capability view to its full SAD document (already on Pages)
- All views dynamically rendered from JSON — no hardcoded data

#### Technical Requirements
- **Plotly.js** via CDN for all charts — no npm, no build step
- `fetch()` loads JSON files from `/data/dashboard/` on page load
- Intel enterprise dark theme (use existing color palette: `#00285a`, `#0071c5`, `#00aeef`)
- Must coexist with existing `deploy-pages.yml` tower/capability Pages structure
- Degrades gracefully if any data source JSON is missing or partial
- "Last updated: [timestamp]" badge on every view

---

### PHASE 4 — AI-Powered Architecture Assistant

Build a chat assistant embedded in the dashboard that can answer architecture questions using live pipeline data.

#### Functionality
- Answers questions about architecture, processes, RICEFW objects, and testing status using the live `dashboard.json` as context
- Supports queries like:
  - "Which systems integrate with S/4 HANA?"
  - "What RICEFW objects are at risk in the FPR tower?"
  - "Show me test failures for the DS-020 capability"
  - "Which processes are owned by the PTP tower?"
  - "What are the open RAID items for OTC-IF?"
- Maintains conversation history within the session
- States when data was last refreshed

#### Technical Setup
- **Powered by Claude** (claude-opus-4-6 model) via Anthropic API
- Corporate Anthropic API key stored as GitHub Secret (`ANTHROPIC_API_KEY`)
- **Proxy required** — GitHub Pages is static, so API key cannot be in client JS:
  1. **Preferred:** Cloudflare Worker (free tier, zero infrastructure)
  2. **Fallback:** GitHub Actions webhook endpoint
  3. **Dev-only:** Direct browser call acceptable during testing if repo is private
- System prompt dynamically built from latest `dashboard.json` on each conversation start
- Embedded as a collapsible chat panel in the dashboard page — not a separate page

#### Optional: MCP Integration for Live Queries
- If MCP servers are accessible, allow the chatbot to query live data beyond the JSON snapshot:
  - Smartsheet: live RICEFW status, RAID items
  - JIRA: live defect counts, test execution
- Fall back to `dashboard.json` context if MCP query fails
- Log MCP usage to console for debugging

---

### PHASE 5 — Secrets & Setup Documentation

Produce `docs/SETUP.md` documenting:

| Secret | Purpose | Where to Get It |
|--------|---------|-----------------|
| `SMARTSHEET_TOKEN` | Smartsheet API (RICEFW Tracker, RAID logs) | Smartsheet > Account > API Access |
| `IAPM_BEARER_TOKEN` | IAPM application portfolio lookup | Browser localStorage after IAPM login |
| `BIC_AUTH_TOKEN` | Signavio/BIC process model API | Browser F12 > Network > Authorization header |
| `SP_TENANT_ID`, `SP_CLIENT_ID`, `SP_CLIENT_SECRET` | SharePoint Graph API (OAuth2) | Azure AD App Registration |
| `SP_SITE_URL`, `SP_DOC_LIBRARY`, `SP_TARGET_FOLDER` | SharePoint target location | SharePoint site URL |
| `JIRA_BASE_URL`, `JIRA_USER_EMAIL`, `JIRA_API_TOKEN` | JIRA test/defect extraction | **NEW** — Jira Profile > Security > API Token |
| `ANTHROPIC_API_KEY` | Claude chatbot | **NEW** — Corporate Anthropic account |
| `CLOUDFLARE_WORKER_URL` | API key proxy for chatbot | **NEW** — Cloudflare dashboard |

Include:
- Cloudflare Worker setup (step-by-step) for API key proxy
- How to wire the Anthropic API key through the proxy
- How to test each connection before the first full pipeline run
- Pipeline troubleshooting guide

---

## CONSTRAINTS

- **No backend servers** — GitHub Pages must remain fully static
- **No npm or webpack** on the frontend — CDN-only for JS libraries
- **Python 3.12** on GitHub Actions runner (matches existing `.venv`)
- **All credentials via GitHub Secrets** only — nothing hardcoded, `.env` for local only
- **Graceful degradation** — every component must work if a data source is unavailable (JIRA not configured? Show "JIRA pending" placeholder. BIC not accessible? Skip process data.)
- **Dashboard must work read-only** for stakeholders with no repo access
- **Coexist with existing Pages** — the tower/capability HTML architecture docs must remain navigable alongside the new dashboard
- **Existing pipeline must not break** — all existing scripts and templates should continue working; new features extend, not replace

---

## DELIVERABLES (in order)

Produce one phase at a time. Wait for confirmation before proceeding to next.

1. **Phase 1:** Fix capability-specific Smartsheet extraction → validate with `FPR/DS-020`
2. **Phase 2a:** `scripts/extract_ricefw.py` + `data/dashboard/ricefw.json` schema
3. **Phase 2b:** `scripts/extract_testing_jira.py` + implement `mcp_servers/jira_server.py` stubs + `data/dashboard/testing.json` schema
4. **Phase 3a:** `scripts/export_dashboard_json.py` + unified `dashboard.json` schema with sample data
5. **Phase 3b:** Updated `generate-architecture.yml` workflow to run full pipeline
6. **Phase 3c:** Dashboard frontend (`_site/dashboard.html` or integrated into `_site/index.html`)
7. **Phase 4a:** Cloudflare Worker proxy script
8. **Phase 4b:** Chatbot panel embedded in dashboard
9. **Phase 5:** `docs/SETUP.md`

After reviewing the repo, flag any integration points, field name mismatches, or missing data that need manual wiring before the pipeline runs end-to-end.

---

## PIPELINE FLOW (target state)

```
GitHub Actions (cron / push / manual)
    │
    ├── gen_systems_arch.py          ← Generate SAD Markdown (all capabilities)
    ├── update_sad_from_smartsheet.py ← Inject live Smartsheet data into SADs
    ├── extract_ricefw.py             ← NEW: RICEFW register from Smartsheet
    ├── extract_testing_jira.py       ← NEW: Testing register from JIRA
    ├── export_dashboard_json.py      ← NEW: Merge all sources → dashboard.json
    ├── gen_pdf.py                    ← Convert MD → HTML + PDF
    │
    ├── git commit + push             ← Outputs committed to repo
    ├── sync_sharepoint.py            ← Forward sync → SharePoint
    │
    └── deploy-pages.yml (chained)    ← Deploy to GitHub Pages
         ├── _site/index.html          ← Tower cards (existing)
         ├── _site/tower-*.html        ← Per-tower capability lists (existing)
         ├── _site/dashboard.html      ← NEW: Unified dashboard
         ├── _site/data/dashboard/     ← NEW: JSON data files
         └── _site/towers/**/*.html    ← SAD documents (existing)
```

**Stakeholder experience:**
```
Stakeholders → Pages URL → Dashboard (KPIs + charts)
                         → Tower drill-down → Capability drill-down
                         → Full SAD document (BDAT architecture)
                         → AI assistant answers architecture questions
                         → All data refreshed automatically on schedule
```

<details>
<summary>View the Prompt Used</summary>

```markdown
This prompt was refined from the user's original engineering prompt, grounded
against the actual IAO Architecture Pipeline repository as of March 30, 2026.
Key refinements:
- Replaced generic "review my repo" with specific file paths and data volumes
- Added Phase 1 (Smartsheet capability-specific extraction fix) as prerequisite
- Documented all 6 known Smartsheet sheet IDs and their consumption status
- Specified exact RICEFW column names from the 212-column Object Tracker
- Documented that JIRA server has 4 tool stubs already defined
- Noted 3 undiscovered sheets (Deliverables, Change Requests, RICEFW Console)
- Added coexistence constraint with existing Pages tower/capability structure
- Removed references to /docs/ as output dir (pipeline uses _site/ via deploy-pages.yml)
- Added pipeline flow diagram showing full target-state execution sequence
- Removed "Mermaid" branding from diagram links per user preference
```

</details>
