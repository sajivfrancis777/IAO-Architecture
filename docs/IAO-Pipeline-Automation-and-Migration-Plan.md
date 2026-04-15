# IAO Architecture Pipeline — Automation Checklist & Corporate Migration Plan

**Date:** April 14, 2026
**Author:** Sajiv Francis — Enterprise Architect, IAO Program
**Status:** Assessment / Planning (No action without approval)

---

## 1. Current State Summary

### What's Built & Working Today

| Component | Status | Automation Level |
|-----------|--------|-----------------|
| **GitHub Pages Portal** | ✅ Live | Fully automated (deploy-pages.yml) |
| **SAD Document Generation** | ✅ 49 docs, 8 towers | Fully automated (generate-architecture.yml, 07:00 UTC Mon-Fri) |
| **RICEFW Tracker Generation** | ✅ Per tower/capability | Fully automated (same workflow) |
| **Testing Report Generation** | ✅ Per tower/capability | Fully automated (same workflow) |
| **L0/L1/Program Summaries** | ✅ All towers + program rollup | Fully automated (same workflow) |
| **Interactive Dashboards** | ✅ 9 dashboards (program + 8 towers) | Fully automated (same workflow) |
| **Per-Release Document Variants** | ✅ R1–R5 scoped outputs | Fully automated (deploy-pages.yml loops R1-R5) |
| **Smartsheet Data Fetch** | ✅ RAID, WRICEF, Timeline | Automated daily (data-refresh.yml, 06:00 UTC Mon-Fri) |
| **JIRA/Zephyr Data Fetch** | ✅ Defects + Test Cases + Zephyr Scale | Automated daily (same workflow) |
| **MD → HTML Conversion** | ✅ All doc types | Fully automated (gen_pdf.py --html-only) |
| **Chat API (Phase 1)** | ✅ Anthropic Claude via Actions | Triggered by repository_dispatch |
| **MCP Servers (3 of 5)** | ✅ Smartsheet, JIRA, IAPM | Local dev only (stdio transport) |
| **Input Portal (React)** | ✅ Functional, separate repo | Manual — AG Grid editor, XLSX export |
| **Unique Systems Extraction** | ✅ Per release, current vs future | Part of dashboard generation |

### CI/CD Workflow Schedule

```
06:00 UTC Mon-Fri → data-refresh.yml
  ├── fetch_smartsheet_data.py  (Smartsheet API → CSV cache)
  └── fetch_jira_data.py        (JIRA REST + Zephyr Scale → JSON cache)

07:00 UTC Mon-Fri → generate-architecture.yml (triggered by data-refresh)
  ├── enrich_flows.py            (IAPM enrichment)
  ├── gen_systems_arch --all     (49 SAD markdowns)
  ├── gen_summary --all          (L0/L1/Program rollups)
  ├── gen_ricefw_tracker --all   (RICEFW tracker docs)
  ├── gen_testing_report --all   (Testing reports)
  ├── gen_pdf --html-only        (MD → HTML conversion)
  └── gen_dashboard              (9 Plotly dashboards)

On push to main → deploy-pages.yml
  ├── Regenerate ALL docs (all releases + per-release R1-R5)
  ├── Build _site/ structure
  └── Deploy to GitHub Pages
```

---

## 2. Automation Gaps — What's Still Manual

### Priority 1: Data Sources Not Yet Automated

| Gap | Current Workaround | Effort to Automate | Blocker |
|-----|-------------------|-------------------|---------|
| **IAPM Live API** | 30K-app CSV cache (static) | Low — bearer token fetch script | Need IAPM bearer token (Azure AD OAuth) |
| **Smartsheet MFA-blocked sheets** (4 of 9) | Manual CSV export + commit | Medium — Smartsheet SDK or admin API key | 4 sheets require account-level access (MFA) |
| **Input Portal → Pipeline** | Manual XLSX upload + commit | Medium — Azure Function `/api/save-data` or GitHub API | Deploy Azure Function or use GitHub Actions API |

### Priority 2: API Integrations (Placeholder)

| Gap | Current State | Effort | Blocker |
|-----|--------------|--------|---------|
| **SAP OData (BI0/DI0)** | Placeholder MCP server, no fetch script | Medium — fetch_sap_data.py + gateway access | Need SAP service account (BI0/DI0 credentials) |
| **SAP BIC/Signavio** | Placeholder MCP server, BPMN files from manual export | Medium — BIC API fetch script | Need BIC auth token + API endpoint access |
| **SharePoint Reverse-Sync** | Workflow exists, awaiting trigger | Low — Power Automate flow to fire repository_dispatch | Need SharePoint app registration (tenant/client/secret) |

### Priority 3: Operational Enhancements

| Gap | Description | Effort |
|-----|-------------|--------|
| **IAPM Refresh Automation** | Periodic re-export of IAPM All Solutions CSV | Low — Add to data-refresh workflow with bearer token |
| **Notification on Failure** | No alerting when workflows fail | Low — Add Slack/Teams webhook or email on workflow failure |
| **Data Validation Gate** | No automated check for data quality before doc generation | Medium — Add validation script to generate-architecture workflow |
| **Input Portal Deployment** | React app not hosted (local dev only) | Medium — Deploy to GitHub Pages (separate repo) or Azure Static Web App |
| **Chat API Phase 2** | 30-60s latency via GitHub Actions | Medium — Azure Function with <5s response time |

---

## 3. What's Required for Full Automation

### Minimal Viable Automation (no new infra)

Only needs **credentials/tokens** — all code and workflows already exist:

1. ✅ Smartsheet API token (have it)
2. ✅ JIRA PAT (have it)
3. ❌ IAPM Bearer Token → enables live app portfolio refresh
4. ❌ SharePoint App Registration → enables reverse-sync from SharePoint
5. ❌ SAP BI0/DI0 service account → enables dev object tracking
6. ❌ BIC Auth Token → enables live BPMN process sync

**With just items 1-4, the pipeline is ~90% automated.** Items 5-6 are enrichment.

### Full Automation Target

```
       ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
       │  Smartsheet   │     │  JIRA/Zephyr  │     │    IAPM      │
       │  (API daily)  │     │  (API daily)  │     │ (API daily)  │
       └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
              │                     │                     │
              └─────────────┬───────┴─────────────────────┘
                            ▼
                ┌───────────────────────┐
                │   data-refresh.yml    │  06:00 UTC Mon-Fri
                │   (GitHub Actions)    │
                └───────────┬───────────┘
                            │  triggers
                            ▼
                ┌───────────────────────┐
                │  generate-architecture│  07:00 UTC Mon-Fri
                │  SADs, RICEFW, Tests, │
                │  Summaries, Dashboard │
                └───────────┬───────────┘
                            │  triggers
                            ▼
                ┌───────────────────────┐
                │    deploy-pages.yml   │
                │  GitHub Pages / Azure │
                └───────────┬───────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
        ┌──────────┐ ┌──────────┐ ┌──────────────┐
        │  Portal  │ │Dashboard │ │  SAD / RICEFW │
        │  (HTML)  │ │ (Plotly) │ │  (HTML docs)  │
        └──────────┘ └──────────┘ └──────────────┘

  Optional additions:
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  SAP OData   │     │  BIC/Signavio│     │  SharePoint   │
  │  (enrichment)│     │  (BPMN sync) │     │  (rev-sync)   │
  └──────────────┘     └──────────────┘     └──────────────┘
```

---

## 4. Corporate GitHub Migration Plan

### Current State
- **Repository:** `sajivfrancis777/IAO-Architecture` (personal GitHub)
- **Hosting:** GitHub Pages at `sajivfrancis777.github.io/IAO-Architecture`
- **Secrets:** Stored in GitHub repo settings + local `.env`

### Migration Options

#### Option A: Intel GitHub Enterprise (github.intel.com)

| Aspect | Impact | Changes Required |
|--------|--------|-----------------|
| **Repository** | Move to `github.intel.com/IAO/IAO-Architecture` | `git remote set-url origin` |
| **GitHub Actions** | ✅ Works if GHE has Actions runners | Verify runner availability; may need self-hosted runners |
| **GitHub Pages** | ⚠️ GHE Pages may or may not be enabled | Check with IT; if disabled, need Option B/C |
| **Secrets** | Re-create in GHE repo settings | One-time migration of 9 secrets |
| **Code Changes** | None | All scripts use relative paths |
| **Access Control** | ✅ Better — Intel SSO + team-based permissions | Configure team access |

**Risk:** GitHub Enterprise may not have Pages enabled or may restrict Actions minutes.

#### Option B: Azure Static Web Apps (Recommended for Corporate)

| Aspect | Impact | Changes Required |
|--------|--------|-----------------|
| **Repository** | Move to Intel GitHub or Azure DevOps | Standard git migration |
| **CI/CD** | Azure DevOps Pipelines or GitHub Actions | Convert 5 YAML workflows to Azure Pipelines (if ADO) |
| **Hosting** | Azure Static Web App (free tier available) | Replace GitHub Pages deploy with `az staticwebapp` CLI |
| **Secrets** | Azure Key Vault or Pipeline variables | Migrate 9 secrets to Key Vault |
| **Code Changes** | Minimal — only deployment step changes | Replace `deploy-pages.yml` with Azure SWA deploy action |
| **Custom Domain** | ✅ `iao-architecture.intel.com` via Azure | DNS CNAME record |
| **Auth** | ✅ Azure AD SSO built-in | No code changes — SWA handles auth at edge |

**Effort Estimate:** 2-3 days for pipeline conversion + 1 day for DNS/auth setup.

**Code Changes Required:**
```yaml
# Replace deploy-pages.yml upload step with:
- name: Deploy to Azure Static Web App
  uses: Azure/static-web-apps-deploy@v1
  with:
    azure_static_web_apps_api_token: ${{ secrets.AZURE_SWA_TOKEN }}
    app_location: "_site"
    skip_app_build: true
```

#### Option C: Full-Stack Azure Web App + Functions

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Azure Static Web App | Portal, dashboards, SAD docs |
| **Input Portal** | Same SWA (route: `/input`) | React AG Grid editor |
| **API Layer** | Azure Functions (Python 3.11) | `/api/save-data`, `/api/chat`, `/api/refresh` |
| **Data Pipeline** | Azure Functions Timer Trigger | Replace GitHub Actions cron (data-refresh) |
| **Storage** | Azure Blob Storage | Generated HTML, XLSX templates, cached data |
| **Auth** | Azure AD / Entra ID | SSO for all Intel users |
| **Secrets** | Azure Key Vault | All API tokens and credentials |

**Effort Estimate:** 1-2 weeks for initial migration, 1 week for testing.

**Code Changes Required:**

| File/Area | Change | Effort |
|-----------|--------|--------|
| `scripts/fetch_*.py` | Add Azure Blob output option | Low — add `--output-blob` flag |
| `src/gen_systems_arch.py` | No changes (reads files, outputs files) | None |
| `scripts/gen_dashboard.py` | No changes | None |
| `templates/*.j2` | Update asset paths for SWA routing | Low |
| **New: `azure-functions/`** | 3 Python functions (save-data, chat, timer-refresh) | Medium |
| **New: `staticwebapp.config.json`** | SWA routing rules + auth config | Low |
| **New: Azure Pipelines YAML** | CI/CD for SWA + Functions deployment | Medium |

### Migration Decision Matrix

| Criteria | Option A (GHE Pages) | Option B (Azure SWA) | Option C (Full-Stack) |
|----------|----------------------|---------------------|----------------------|
| **Effort** | 1 day | 2-3 days | 1-2 weeks |
| **Code Changes** | None | Minimal (deploy step) | Moderate (add Functions) |
| **Auth/SSO** | GHE built-in | Azure AD built-in | Azure AD built-in |
| **Custom Domain** | If GHE allows | ✅ Yes | ✅ Yes |
| **Input Portal** | Separate deploy | Integrated (SWA route) | Integrated (SWA route) |
| **Chat API** | GitHub Actions (slow) | Azure Function (fast) | Azure Function (fast) |
| **Scalability** | Limited by GHE | Good (serverless) | Best (full control) |
| **Cost** | $0 (if GHE available) | $0-9/mo (free tier) | $50-100/mo (Functions + Storage) |
| **Intel IT Approval** | Need GHE access | Need Azure subscription | Need Azure subscription |
| **Recommendation** | If GHE has Pages | **Best balance** | If Input Portal + Chat critical |

### Recommended Path

**Phase 1 — Immediate (Option A test):**
Check if Intel GitHub Enterprise has Pages enabled. If yes, migrate repo + secrets and done.

**Phase 2 — If GHE Pages unavailable (Option B):**
Deploy to Azure Static Web App. Minimal code changes. Gets SSO + custom domain.

**Phase 3 — When approved (Option C additions):**
Add Azure Functions for Input Portal save + Chat API. Replaces GitHub Actions cron with Timer Triggers.

---

## 5. Checklist Summary

### Already Done ✅

- [x] 5 CI/CD workflows (data-refresh, generate-architecture, deploy-pages, chat-api, sharepoint-sync)
- [x] Daily automated data fetch (Smartsheet + JIRA)
- [x] Daily automated doc generation (49 SADs + RICEFW + Testing + Summaries + Dashboards)
- [x] GitHub Pages deployment with per-release variants (R1-R5)
- [x] 3 working MCP servers (Smartsheet, JIRA, IAPM)
- [x] Unique system extraction from XLSX flows (per release, current/future)
- [x] Release dropdown filtering on all 3 dashboard pillars
- [x] Fabricated data removed from templates
- [x] Input Portal (React) — functional for data editing

### Needs Credentials Only 🔑

- [ ] IAPM Bearer Token → live app portfolio refresh
- [ ] SharePoint App Registration → reverse-sync from architects
- [ ] SAP BI0/DI0 Service Account → dev object tracking
- [ ] BIC Auth Token → live BPMN process sync

### Needs Development Work 🔧

- [ ] Input Portal deployment (GitHub Pages or Azure SWA)
- [ ] Input Portal → Pipeline integration (save XLSX → trigger rebuild)
- [ ] Chat API Phase 2 (Azure Function, <5s latency)
- [ ] Workflow failure notifications (Slack/Teams webhook)
- [ ] Data validation gate (pre-generation quality check)
- [ ] 2 remaining MCP servers (SAP OData, BIC — blocked on credentials)

### Needs Corporate Decision 🏢

- [ ] Determine target: Intel GitHub Enterprise vs Azure
- [ ] Obtain Azure subscription (if Option B/C)
- [ ] DNS record for custom domain (iao-architecture.intel.com)
- [ ] Intel IT security review for Azure AD SSO integration

---

<details>
<summary>View the Prompt Used</summary>

```markdown
ok the deploy is completed, lets push the latest changes to github and commit: 9924f721

[Follow-up] ok, can we outline a checklist of how to make this pipeline completely automated,
i am not looking to do more work unless there is interest or approval, however, wanted to
take account of what was completed and what else is required to make this fully automated.
Additionally, we need a plan to move the code from my personal github to a corporate one,
will the github pages still work, if not, we need alternate deployment plans and what type
of changes will be required to the code, this include azure web apps & functions or even a
full stack if there is not too much of a lift?
```

</details>
