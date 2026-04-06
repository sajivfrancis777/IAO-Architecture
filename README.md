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

## Solution Architecture

This section presents the IAO Architecture Pipeline as an **enterprise solution** — its integration landscape, credential requirements, AI chatbot capabilities, and value across the IDM 2.0 project lifecycle.

### Architecture Overview

```
  ┌─────────────────────────────────────────────────────────────────────────────────┐
  │                          IAO ARCHITECTURE PIPELINE                              │
  │                          Solution Architecture Diagram                          │
  │                                                                                 │
  │  ┌─ SOURCE SYSTEMS ─────────────────────────────────────────────────────────┐   │
  │  │                                                                          │   │
  │  │  ┌──────────────┐ ┌────────────┐ ┌──────────────┐ ┌─────────────────┐   │   │
  │  │  │  Smartsheet   │ │ Signavio/  │ │    IAPM      │ │   SharePoint    │   │   │
  │  │  │  (RICEFW,     │ │ BIC        │ │ (App         │ │   (Excel        │   │   │
  │  │  │   RAID,       │ │ (BPMN      │ │  Portfolio   │ │    Workbooks)   │   │   │
  │  │  │   Timeline)   │ │  Models)   │ │  30K+ apps)  │ │                 │   │   │
  │  │  └──────┬───────┘ └─────┬──────┘ └──────┬───────┘ └───────┬─────────┘   │   │
  │  │         │ API           │ API/CSV        │ API/CSV         │ Graph API   │   │
  │  │         │               │                │                 │             │   │
  │  │  ┌──────┴───────┐ ┌────┴───────┐ ┌──────┴──────┐ ┌───────┴─────────┐   │   │
  │  │  │   SAP S/4    │ │   JIRA     │ │  ServiceNow │ │  Future         │   │   │
  │  │  │  OData       │ │  (Test     │ │  (Incident  │ │  Integrations   │   │   │
  │  │  │  (Dev Objs,  │ │   Cases,   │ │   data,     │ │                 │   │   │
  │  │  │   Transports)│ │   Defects) │ │   by tower) │ │                 │   │   │
  │  │  └──────┬───────┘ └─────┬──────┘ └──────┬──────┘ └───────┬─────────┘   │   │
  │  │         │ OData/ADT     │ REST           │ REST           │             │   │
  │  └─────────┼───────────────┼────────────────┼────────────────┼─────────────┘   │
  │            │               │                │                │                  │
  │            ▼               ▼                ▼                ▼                  │
  │  ┌─ PROCESSING ENGINE ─────────────────────────────────────────────────────┐   │
  │  │                                                                          │   │
  │  │  src/config.py ─── .env (credentials) ─── os.environ (runtime)          │   │
  │  │       │                                                                  │   │
  │  │       ├── smartsheet_loader.py ──── Live API → CSV fallback             │   │
  │  │       ├── iapm_lookup.py ────────── Live API → CSV fallback             │   │
  │  │       ├── bpmn_parser.py ────────── XML parse + Mermaid render          │   │
  │  │       ├── xlsx_loader.py ────────── Multi-tab workbook parse            │   │
  │  │       ├── csv_parser.py ─────────── Flow CSV parse + chain build        │   │
  │  │       └── mermaid_builder.py ────── 6 diagram types (ArchiMate, etc.)   │   │
  │  │                    │                                                     │   │
  │  │                    ▼                                                     │   │
  │  │  gen_systems_arch.py (orchestrator) ──> Jinja2 templates                │   │
  │  │       │                                                                  │   │
  │  │       ├── gen_pdf.py ────────── MD → HTML (Mermaid.js live rendering)   │   │
  │  │       ├── gen_dashboard.py ──── Plotly.js interactive dashboards        │   │
  │  │       ├── gen_ricefw_tracker.py  Per-tower RICEFW tracker docs          │   │
  │  │       └── gen_testing_report.py  Per-tower testing readiness docs       │   │
  │  │                                                                          │   │
  │  └──────────────────────────────────┬───────────────────────────────────────┘   │
  │                                     │                                           │
  │            ┌────────────────────────┼─────────────────────┐                    │
  │            ▼                        ▼                     ▼                    │
  │  ┌─ OUTPUT CHANNELS ───────────────────────────────────────────────────────┐   │
  │  │                                                                          │   │
  │  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │   │
  │  │  │ GitHub Pages │  │  SharePoint  │  │  Git Repo    │                  │   │
  │  │  │ (interactive │  │  (HTML+PDF   │  │  (versioned  │                  │   │
  │  │  │  dashboards, │  │   for arch   │  │   MD+HTML,   │                  │   │
  │  │  │  full docs)  │  │   workspace) │  │   diff-able) │                  │   │
  │  │  └──────────────┘  └──────────────┘  └──────────────┘                  │   │
  │  │                                                                          │   │
  │  └──────────────────────────────────────────────────────────────────────────┘   │
  │                                                                                 │
  │  ┌─ AI CHATBOT LAYER (MCP Servers) ────────────────────────────────────────┐   │
  │  │                                                                          │   │
  │  │  VS Code / GitHub Copilot Chat                                          │   │
  │  │       │                                                                  │   │
  │  │       ├── iao-smartsheet ─── "What RICEFW objects are in FPR DS-020?"   │   │
  │  │       ├── iao-iapm ──────── "What's the IAPM status of MuleSoft?"       │   │
  │  │       ├── iao-jira ──────── "How many open defects in OTC-IF?"          │   │
  │  │       ├── iao-sap-odata ─── "Show transports for FPRI1234"             │   │
  │  │       └── iao-bic ──────── "Find BIC process models for DS-020"        │   │
  │  │                                                                          │   │
  │  │  Each MCP server: API live → CSV fallback → structured JSON response    │   │
  │  │  Same tower_registry.py normalization used across pipeline + chatbot    │   │
  │  │                                                                          │   │
  │  └──────────────────────────────────────────────────────────────────────────┘   │
  │                                                                                 │
  └─────────────────────────────────────────────────────────────────────────────────┘
```

### Credential & Integration Inventory

Every API integration follows the same pattern: **API-first with graceful fallback**. The table below is the complete credential inventory for the solution.

#### Source System Credentials

| # | Variable | System | Auth Method | Status | Provisioning |
|---|----------|--------|-------------|--------|-------------|
| 1 | `SMARTSHEET_TOKEN` | Smartsheet API v2.0 | Bearer token | **Working** | Smartsheet admin generates API token |
| 2 | `IAPM_BEARER_TOKEN` | IAPM (Azure AD) | OAuth2 Bearer | **CSV fallback** | Browser: `localStorage` → access token; or Azure AD app |
| 3 | `BIC_AUTH_TOKEN` | SAP BIC / Signavio | Bearer token | **Placeholder** | Browser F12 → Network → Authorization header |
| 4 | `SAP_BI0_HOST` | SAP S/4HANA BI0 (Foundry) | — | **Placeholder** | `https://sapbi0ci.intel.com:8220` |
| 5 | `SAP_BI0_USER` | SAP BI0 | NTLM / Negotiate | **Pending** | SAP access request + `S_SERVICE` role |
| 6 | `SAP_BI0_PASS` | SAP BI0 | NTLM / Negotiate | **Pending** | Same as above |
| 7 | `SAP_BI0_CLIENT` | SAP BI0 | Client number | **Placeholder** | Default `200` |
| 8 | `SAP_DI0_HOST` | SAP S/4HANA DI0 (Products) | — | **Placeholder** | `https://sapdi0ci.intel.com:8220` |
| 9 | `SAP_DI0_USER` | SAP DI0 | NTLM / Negotiate | **Pending** | SAP access request + `S_SERVICE` role |
| 10 | `SAP_DI0_PASS` | SAP DI0 | NTLM / Negotiate | **Pending** | Same as above |
| 11 | `SAP_DI0_CLIENT` | SAP DI0 | Client number | **Placeholder** | Default `200` |
| 12 | `JIRA_BASE_URL` | JIRA REST API | — | **Placeholder** | `https://jira.intel.com` |
| 13 | `JIRA_USER_EMAIL` | JIRA | Basic / PAT | **Pending** | JIRA profile → Personal Access Token |
| 14 | `JIRA_API_TOKEN` | JIRA | PAT | **Pending** | Needs IDM 2.0 project read access |

#### LLM Provider Credentials (AI Chatbot)

| # | Variable | System | Auth Method | Status | Provisioning |
|---|----------|--------|-------------|--------|-------------|
| 15 | `ANTHROPIC_API_KEY` | Anthropic Claude API | API key | **Required for web chatbot** | [console.anthropic.com](https://console.anthropic.com) → API Keys; or Intel-approved Azure OpenAI endpoint |
| 16 | `LLM_MODEL` | LLM model selector | — | **Config** | Default: `claude-sonnet-4-20250514`; alternatives: `claude-opus-4-20250514`, Azure OpenAI deployment name |

> **VS Code + Copilot Chat**: No separate LLM key needed — GitHub Copilot Pro/Enterprise subscription provides the LLM. MCP servers connect via stdio transport.
>
> **GitHub Pages web chatbot**: Requires a server-side LLM API key (Anthropic or Azure OpenAI) because the browser cannot safely hold API keys. The key is stored in the backend service, never exposed to the client.

#### SharePoint & Delivery Credentials

| # | Variable | System | Auth Method | Status | Provisioning |
|---|----------|--------|-------------|--------|-------------|
| 17 | `SP_TENANT_ID` | Azure AD | OAuth2 client creds | **Working** | Azure portal → App Registration |
| 18 | `SP_CLIENT_ID` | Azure AD | OAuth2 client creds | **Working** | Same app registration |
| 19 | `SP_CLIENT_SECRET` | Azure AD | OAuth2 client creds | **Working** | App Registration → Certificates & Secrets |
| 20 | `SP_SITE_URL` | SharePoint Online | — | **Working** | `https://intel.sharepoint.com/sites/IAO-Architecture` |
| 21 | `SP_DOC_LIBRARY` | SharePoint | — | **Working** | Default: `Shared Documents` |
| 22 | `SP_TARGET_FOLDER` | SharePoint | — | **Working** | Default: `Architecture/SAD` |

#### GitHub Actions Runtime

All credentials above are stored as **GitHub Actions Secrets** (AES-256 encrypted at rest) and injected at workflow runtime via `${{ secrets.XXX }}`. No credential is ever committed to the repository.

| Status | Count | Credentials |
|--------|-------|-------------|
| **Working** | 7 | Smartsheet, SharePoint (6 vars) |
| **CSV fallback** | 1 | IAPM (30K apps from CSV cache) |
| **Placeholder** | 6 | BIC, SAP hosts, SAP clients, JIRA URL |
| **Pending enterprise access** | 6 | SAP BI0/DI0 user/pass, JIRA user/token |
| **LLM provider** | 2 | Anthropic API key + model config (for web chatbot) |
| **Total** | **22** | |

### AI Chatbot Integration

The chatbot layer is what transforms this pipeline from a static document site into an **interactive AI-powered architecture knowledge base**. Without it, the site is a Wikipedia — searchable but passive. With it, architects and support teams can query live build data conversationally.

#### Two Deployment Modes

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                    CHATBOT DEPLOYMENT ARCHITECTURE                      │
  │                                                                         │
  │  MODE 1: VS CODE + COPILOT (Current — Working)                         │
  │  ─────────────────────────────────────────────                          │
  │                                                                         │
  │  Developer / Architect                                                  │
  │       │                                                                 │
  │       ▼                                                                 │
  │  VS Code + GitHub Copilot Chat (Pro/Enterprise subscription)           │
  │       │                                                                 │
  │       │  LLM: Copilot handles (no separate API key needed)             │
  │       │  Transport: stdio (local subprocess)                            │
  │       ▼                                                                 │
  │  .vscode/settings.json → MCP servers (5 servers, 21 tools)            │
  │       │                                                                 │
  │       └──> Smartsheet API / IAPM CSV / JIRA / SAP / BIC               │
  │                                                                         │
  │  ✅ Works today. Limited to VS Code users with Copilot license.        │
  │                                                                         │
  ├─────────────────────────────────────────────────────────────────────────┤
  │                                                                         │
  │  MODE 2: GITHUB PAGES WEB CHATBOT (Target — Planned)                   │
  │  ───────────────────────────────────────────────────                     │
  │                                                                         │
  │  Any team member (browser)                                              │
  │       │                                                                 │
  │       ▼                                                                 │
  │  GitHub Pages site (chat widget embedded in HTML)                      │
  │       │                                                                 │
  │       │  User types: "What interfaces does FPR DC-020 use?"           │
  │       │                                                                 │
  │       ▼                                                                 │
  │  API Gateway (Azure Functions / GitHub Actions API)                    │
  │       │                                                                 │
  │       │  Holds: ANTHROPIC_API_KEY + source system credentials          │
  │       │  (API keys NEVER sent to browser)                               │
  │       │                                                                 │
  │       ├──(1) Send user query + tool definitions to Claude API          │
  │       │       (Anthropic claude-sonnet-4-20250514 or Azure OpenAI)               │
  │       │                                                                 │
  │       ├──(2) Claude decides which tools to call                        │
  │       │       (same MCP tool logic, refactored to HTTP)                │
  │       │                                                                 │
  │       ├──(3) Execute tool calls against source APIs                    │
  │       │       Smartsheet → RICEFW data                                 │
  │       │       IAPM → App metadata                                       │
  │       │       JIRA → Defects, test cases                               │
  │       │                                                                 │
  │       ├──(4) Return tool results to Claude                             │
  │       │                                                                 │
  │       └──(5) Claude formats final answer → browser                     │
  │                                                                         │
  │  🎯 Target: Any team member queries live architecture from browser.    │
  │     No VS Code, no Copilot license needed.                              │
  │     Works for support teams, test leads, program managers.             │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
```

#### Web Chatbot — Detailed Implementation Guide

**Why Azure Functions?** GitHub Pages serves static HTML only — no server-side code. You need a backend to (a) hold API keys securely and (b) proxy calls between the browser, the LLM, and source systems. Azure Functions is the simplest option because Intel already uses Azure, it's serverless (no VMs to manage), and it scales to zero when idle (no cost when nobody's chatting).

##### Prerequisites

| Requirement | What You Need | How to Get It |
|------------|---------------|---------------|
| Azure subscription | Intel Azure tenant access | IT self-service portal or Azure request form |
| Anthropic API key | `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) → API Keys (or Intel-approved LLM endpoint) |
| Azure Functions Core Tools | Local development/testing | `npm install -g azure-functions-core-tools@4` |
| Python 3.11+ | Azure Functions runtime | Already in this workspace |
| Source system credentials | Same `.env` vars from the pipeline | Copy from local `.env` to Azure Function App Settings |

##### Step 1: Create the Azure Function App

```bash
# Login to Azure (Intel tenant)
az login --tenant <INTEL_TENANT_ID>

# Create resource group (one-time)
az group create --name rg-iao-architecture --location westus2

# Create Function App (Python, consumption plan = pay-per-execution)
az functionapp create \
  --resource-group rg-iao-architecture \
  --consumption-plan-location westus2 \
  --runtime python \
  --runtime-version 3.11 \
  --functions-version 4 \
  --name iao-architecture-chat \
  --storage-account iaoarchstorage \
  --os-type Linux
```

##### Step 2: Add Credentials to Azure Function App Settings

```bash
# LLM provider
az functionapp config appsettings set --name iao-architecture-chat \
  --resource-group rg-iao-architecture \
  --settings \
    ANTHROPIC_API_KEY="sk-ant-..." \
    LLM_MODEL="claude-sonnet-4-20250514"

# Source system credentials (same as local .env)
az functionapp config appsettings set --name iao-architecture-chat \
  --resource-group rg-iao-architecture \
  --settings \
    SMARTSHEET_TOKEN="..." \
    IAPM_BEARER_TOKEN="..." \
    JIRA_BASE_URL="https://jira.intel.com" \
    JIRA_USER_EMAIL="..." \
    JIRA_API_TOKEN="..."
```

These are stored encrypted in Azure (equivalent to GitHub Secrets). They are **never** sent to the browser.

##### Step 3: Build the Chat Backend (`/api/chat` endpoint)

The backend is a single Python Azure Function that:
1. Receives the user's question from the browser
2. Sends it to Claude with tool definitions (reused from MCP servers)
3. Executes any tool calls Claude requests (Smartsheet, IAPM, etc.)
4. Returns Claude's final answer to the browser

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  AZURE FUNCTION: /api/chat                                      │
  │                                                                 │
  │  Request (from browser):                                        │
  │  {                                                              │
  │    "message": "What RICEFW objects are in FPR DC-020?",        │
  │    "tower": "FPR",                                              │
  │    "capability": "DC-020",                                      │
  │    "history": [ ... previous messages ... ]                    │
  │  }                                                              │
  │                                                                 │
  │  Processing:                                                    │
  │                                                                 │
  │  (1) Build messages array with system prompt + tools            │
  │      System prompt: "You are an IAO architecture assistant.     │
  │      The user is viewing {tower} {capability}. Use the          │
  │      provided tools to answer from live data."                  │
  │                                                                 │
  │  (2) Call Anthropic Messages API                                │
  │      POST https://api.anthropic.com/v1/messages                │
  │      Headers: x-api-key: $ANTHROPIC_API_KEY                    │
  │      Body: { model, messages, tools, max_tokens }              │
  │                                                                 │
  │  (3) If Claude response contains tool_use blocks:              │
  │      → Execute tool calls locally:                             │
  │        get_ricefw_objects(tower="FPR", capability="DC-020")    │
  │        → Calls Smartsheet API (or CSV fallback)                │
  │      → Send tool results back to Claude                         │
  │      → Claude formats final answer                              │
  │                                                                 │
  │  (4) Return final text to browser                               │
  │                                                                 │
  │  Response (to browser):                                         │
  │  {                                                              │
  │    "response": "FPR DC-020 has 14 RICEFW objects: ..."         │
  │  }                                                              │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘
```

The key insight: **the tool logic is identical to the MCP servers**. You import the same `smartsheet_server.py`, `iapm_server.py`, etc. functions — the only difference is transport (HTTP instead of stdio).

##### Step 4: Add the Chat Widget to GitHub Pages

Add to `deploy-pages.yml` output HTML (or to a shared template):

```html
<!-- Chat widget — floating button + panel -->
<div id="iao-chat-widget" style="position:fixed; bottom:20px; right:20px; z-index:9999;">
  <button id="chat-toggle"
    style="width:56px; height:56px; border-radius:50%; background:#00285a;
           color:#fff; border:none; font-size:24px; cursor:pointer;
           box-shadow:0 4px 12px rgba(0,0,0,0.3);">
    💬
  </button>
  <div id="chat-panel" style="display:none; width:400px; height:500px;
       background:#fff; border-radius:12px; box-shadow:0 8px 32px rgba(0,0,0,0.2);
       flex-direction:column; overflow:hidden; margin-bottom:8px;">
    <div style="background:#00285a; color:#fff; padding:12px 16px; font-weight:600;">
      IAO Architecture Assistant
    </div>
    <div id="chat-messages" style="flex:1; overflow-y:auto; padding:12px;"></div>
    <div style="padding:8px; border-top:1px solid #eee; display:flex; gap:8px;">
      <input id="chat-input" type="text" placeholder="Ask about this architecture..."
        style="flex:1; padding:8px 12px; border:1px solid #ddd; border-radius:6px;" />
      <button id="chat-send"
        style="background:#0071c5; color:#fff; border:none; border-radius:6px;
               padding:8px 16px; cursor:pointer;">Send</button>
    </div>
  </div>
</div>

<script>
  const CHAT_API = 'https://iao-architecture-chat.azurewebsites.net/api/chat';

  // Extract tower + capability from the current page URL or h1 tag
  const pageTitle = document.querySelector('h1')?.textContent || '';
  const capMatch = pageTitle.match(/^([A-Z]{1,4}-\d{2,4})/);
  const pageContext = {
    capability: capMatch ? capMatch[1] : '',
    tower: document.title.split('—')[0]?.trim() || ''
  };

  document.getElementById('chat-toggle').onclick = () => {
    const panel = document.getElementById('chat-panel');
    panel.style.display = panel.style.display === 'none' ? 'flex' : 'none';
  };

  document.getElementById('chat-send').onclick = async () => {
    const input = document.getElementById('chat-input');
    const msg = input.value.trim();
    if (!msg) return;

    // Show user message
    appendMessage('You', msg);
    input.value = '';

    // Call backend
    try {
      const res = await fetch(CHAT_API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: msg,
          tower: pageContext.tower,
          capability: pageContext.capability
        })
      });
      const data = await res.json();
      appendMessage('Assistant', data.response);
    } catch (e) {
      appendMessage('Assistant', 'Error connecting to chat service.');
    }
  };

  // Enter key sends
  document.getElementById('chat-input').onkeydown = (e) => {
    if (e.key === 'Enter') document.getElementById('chat-send').click();
  };

  function appendMessage(role, text) {
    const div = document.createElement('div');
    div.style.cssText = 'margin-bottom:8px; padding:8px; border-radius:8px; ' +
      (role === 'You' ? 'background:#e8f0fe; text-align:right;' : 'background:#f5f5f5;');
    div.innerHTML = '<strong>' + role + '</strong><br>' + text;
    document.getElementById('chat-messages').appendChild(div);
    div.scrollIntoView({ behavior: 'smooth' });
  }
</script>
```

##### Step 5: CORS — Allow GitHub Pages to Call Azure Function

```bash
az functionapp cors add --name iao-architecture-chat \
  --resource-group rg-iao-architecture \
  --allowed-origins "https://sajivfrancis777.github.io"
```

##### Step 6 (Optional): Azure AD Authentication

To restrict chatbot access to Intel employees only:

```bash
# Enable AAD auth on the Function App
az webapp auth update --name iao-architecture-chat \
  --resource-group rg-iao-architecture \
  --enabled true \
  --action LoginWithAzureActiveDirectory \
  --aad-client-id <APP_CLIENT_ID> \
  --aad-allowed-token-audiences "https://iao-architecture-chat.azurewebsites.net"
```

The browser chat widget would then acquire an AAD token via MSAL.js and include it in the `Authorization` header. Unauthenticated users get a 401.

##### Step 7: Deploy the Function

```bash
# From the azure-function/ directory (to be created)
func azure functionapp publish iao-architecture-chat
```

##### Complete Request Flow

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │                                                                      │
  │   Browser (GitHub Pages)                                             │
  │   ──────────────────────                                             │
  │   User clicks 💬, types: "What RICEFW objects are in FPR DC-020?"  │
  │                                                                      │
  │   chat-widget.js:                                                    │
  │     POST https://iao-architecture-chat.azurewebsites.net/api/chat  │
  │     Body: { message, tower: "FPR", capability: "DC-020" }          │
  │     Header: Authorization: Bearer <AAD_TOKEN> (optional)            │
  │                                                                      │
  ├──────────────────────────────────────────────────────────────────────┤
  │                                                                      │
  │   Azure Function (/api/chat)                                        │
  │   ──────────────────────────                                         │
  │                                                                      │
  │   1. Validate request (AAD token if auth enabled)                   │
  │                                                                      │
  │   2. Build Claude messages:                                          │
  │      system: "You are an IAO architecture assistant..."             │
  │      user: "What RICEFW objects are in FPR DC-020?"                │
  │      tools: [get_ricefw_objects, get_raid_items,                    │
  │              search_applications, lookup_application, ...]          │
  │                                                                      │
  │   3. POST https://api.anthropic.com/v1/messages                     │
  │      x-api-key: $ANTHROPIC_API_KEY (from App Settings)             │
  │      model: claude-sonnet-4-20250514                                         │
  │                                                                      │
  │   4. Claude responds with tool_use:                                  │
  │      { "type": "tool_use",                                          │
  │        "name": "get_ricefw_objects",                                │
  │        "input": { "tower": "FPR", "capability": "DC-020" } }      │
  │                                                                      │
  │   5. Execute tool (same code as mcp_servers/smartsheet_server.py): │
  │      → Calls Smartsheet API with $SMARTSHEET_TOKEN                  │
  │      → Returns: 14 objects (8 Interfaces, 3 Enhancements, ...)     │
  │                                                                      │
  │   6. Send tool result back to Claude                                │
  │                                                                      │
  │   7. Claude formats final answer:                                    │
  │      "FPR DC-020 (Manage the General Ledger) has 14 RICEFW         │
  │       objects: 8 Interfaces, 3 Enhancements, 2 Reports,            │
  │       1 Conversion. 11 are Deployed, 3 are Developing..."          │
  │                                                                      │
  │   8. Return to browser: { "response": "FPR DC-020 has..." }       │
  │                                                                      │
  ├──────────────────────────────────────────────────────────────────────┤
  │                                                                      │
  │   Browser renders response in chat panel                            │
  │   User can ask follow-up questions (conversation history sent)     │
  │                                                                      │
  └──────────────────────────────────────────────────────────────────────┘
```

##### Cost Estimate

| Component | Cost | Notes |
|-----------|------|-------|
| Azure Functions (Consumption) | ~$0 for low usage | Free grant: 1M executions/month + 400K GB-seconds |
| Anthropic Claude API | ~$3 per 1M input tokens, ~$15 per 1M output tokens | A typical query = ~2K tokens ≈ $0.01 per question |
| Azure Storage (Function state) | ~$0.05/month | Minimal storage for function app |
| **Estimated monthly** | **< $5 for team of 20** | Assuming ~100 queries/day |

##### Alternative: No Azure (Simpler but Less Secure)

If Azure setup is blocked, a lighter alternative:

| Option | Pros | Cons |
|--------|------|------|
| **GitHub Actions as API** | No Azure needed; trigger via `repository_dispatch`, poll for result | Slow (30-60s cold start); not real-time; awkward UX |
| **Cloudflare Workers** | Free tier, edge-deployed, fast | Not Intel-approved vendor; credential governance concern |
| **Self-hosted FastAPI** | Full control, same Python code | Need a VM/container; ops overhead |

> **Recommendation**: Azure Functions is the cleanest path given Intel's existing Azure tenant. Total setup time is approximately 2-3 hours for a working prototype.

#### LLM Provider Options

| Provider | Model | Pros | Cons |
|----------|-------|------|------|
| **Anthropic Claude** | claude-sonnet-4-20250514 / claude-opus-4-20250514 | Best tool_use support, large context window, strong reasoning | Requires external API key |
| **Azure OpenAI** | GPT-4o / GPT-4o-mini | Intel-approved Azure tenant, no external vendor | Tool calling slightly less reliable for complex queries |
| **GitHub Copilot** | (managed by GitHub) | Already licensed for VS Code users, zero config | Only works inside VS Code, not embeddable in web pages |

> **Recommendation**: Use **Anthropic Claude** (claude-sonnet-4-20250514) for the web chatbot via Azure Functions backend. For VS Code users, continue using **GitHub Copilot + MCP** (no additional cost). Both modes share the same tool definitions and source system credentials.

#### MCP Server Inventory

| Server | Tool Count | Status | Credential Required | Sample Queries |
|--------|-----------|--------|-------------------|---------------|
| `iao-smartsheet` | 6 tools | **Working** | `SMARTSHEET_TOKEN` | "Get RICEFW objects for FPR DS-020" / "Show RAID items for OTC-IF" |
| `iao-iapm` | 3 tools | **Working** | (CSV cache) | "Search IAPM for SAP S/4HANA" / "What's the status of MuleSoft?" |
| `iao-jira` | 4 tools | **Placeholder** | `JIRA_*` (3 vars) | "Get defects for PTP tower" / "Sprint status for FTS-IF" |
| `iao-sap-odata` | 4 tools | **Placeholder** | `SAP_BI0_*` or `SAP_DI0_*` | "Get dev objects for transport K9xxxxx" / "CDS view catalog" |
| `iao-bic` | 4 tools | **Placeholder** | `BIC_AUTH_TOKEN` | "Search BIC for DS-020 process models" / "Get process hierarchy" |

#### Chatbot Capabilities by BDAT Domain

| TOGAF Domain | MCP Server | What the Chatbot Provides |
|-------------|-----------|--------------------------|
| **Business** | `iao-bic` | Process model names, L1/L2/L3 hierarchy, BPMN metadata |
| **Data** | `iao-sap-odata` | CDS views, data object inventory, schema references |
| **Application** | `iao-iapm` + `iao-smartsheet` | Application lifecycle status, RICEFW object inventory, integration patterns |
| **Technology** | `iao-sap-odata` | Transport status, dev object inventory, system configuration |
| **Project** | `iao-jira` + `iao-smartsheet` | Test readiness, defect counts, RAID items, sprint burn-down, delivery timelines |

### Value Proposition — Project Lifecycle

This architecture delivers value across **every phase of the IDM 2.0 program**, not just design:

#### Pre-Go-Live: Integration Testing & Mock Cutovers

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  INTEGRATION TESTING & MOCK CUTOVER VALUE                       │
  │                                                                 │
  │  Integration Testers ask:                                       │
  │    "What interfaces does FPR DC-020 depend on?"                │
  │    "Which systems feed data into S/4HANA for this process?"    │
  │    "What RICEFW objects are in Developing vs Deployed status?"  │
  │                                                                 │
  │  ┌────────────────────┐    ┌──────────────────────────────┐    │
  │  │  GitHub Pages        │    │  Copilot Chat (MCP)          │    │
  │  │  ──────────────      │    │  ──────────────────────      │    │
  │  │  Full architecture  │    │  "Show RICEFW objects for     │    │
  │  │  docs per tower +   │    │   FPR DC-020 where status     │    │
  │  │  capability with    │    │   = Developing"               │    │
  │  │  Mermaid diagrams   │    │                               │    │
  │  │  showing integration│    │  → Returns live Smartsheet    │    │
  │  │  flows & system     │    │    data filtered by tower,    │    │
  │  │  dependencies       │    │    capability, and status     │    │
  │  └────────────────────┘    └──────────────────────────────┘    │
  │                                                                 │
  │  WITHOUT THIS PIPELINE:                                         │
  │  • Architects email Excel files to test leads                  │
  │  • Test leads manually search Smartsheet for RICEFW status     │
  │  • Integration diagrams are stale PowerPoint slides            │
  │  • No single view of current vs future architecture            │
  │                                                                 │
  │  WITH THIS PIPELINE:                                            │
  │  • Live RICEFW status auto-injected from Smartsheet API        │
  │  • Architectural diagrams regenerated on every input change    │
  │  • Chatbot answers "what depends on what" queries in seconds   │
  │  • Mock cutover teams see real build status, not stale docs    │
  └─────────────────────────────────────────────────────────────────┘
```

#### Post-Go-Live: Production Support & ServiceNow

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  PRODUCTION SUPPORT VALUE                                       │
  │                                                                 │
  │  Support team receives ServiceNow incident:                     │
  │    "Invoice posting fails in S/4HANA for customer X"           │
  │                                                                 │
  │  Step 1: Identify Tower & Capability                            │
  │    Incident → OTC-IF tower → BR-130 (Billing Revenue)          │
  │                                                                 │
  │  Step 2: Look up Architecture (GitHub Pages)                    │
  │    BR-130-Architecture.html shows:                              │
  │    • All systems in the billing flow (current + future)        │
  │    • Integration diagrams (which middleware, which protocol)    │
  │    • RICEFW objects (custom interfaces, enhancements)          │
  │    • Platform dependencies (SAP, MuleSoft, Ariba, etc.)        │
  │                                                                 │
  │  Step 3: Ask Chatbot for Live Data                              │
  │    "What interfaces does OTC-IF BR-130 use?"                   │
  │    → Returns: 12 interfaces, 3 enhancements, 2 reports         │
  │    "What's the IAPM status of MuleSoft?"                       │
  │    → Returns: Deployed, hosted on Azure, owner: Integration    │
  │                                                                 │
  │  Step 4: Resolve Faster                                         │
  │    Support team knows exactly which systems to check,          │
  │    which interfaces carry the invoice data, and who owns       │
  │    each integration point — without opening SAP or Smartsheet  │
  │                                                                 │
  │  SUPPORT TEAM BENEFITS:                                         │
  │  • Incident → Tower → Capability mapping (ServiceNow-ready)   │
  │  • Architecture docs organized by tower + capability ID        │
  │  • AI answers "what systems are involved" without SAP access   │
  │  • Understanding of current vs future state for transitions    │
  │  • Historical architecture versioned in Git (what changed?)    │
  └─────────────────────────────────────────────────────────────────┘
```

#### Lifecycle Coverage Summary

| Phase | What the Pipeline Provides | Key Consumers |
|-------|---------------------------|---------------|
| **Design** | TOGAF BDAT docs, Mermaid diagrams, capability hierarchy | Solution architects, enterprise architects |
| **Build** | Live RICEFW status, dev object inventory, RAID log | Tower leads, program managers |
| **Integration Test** | System dependency maps, interface inventory, current vs future state | Test leads, integration testers |
| **Mock Cutover** | Complete architecture per capability, platform dependencies | Cutover coordinators, release managers |
| **UAT** | Testing reports, defect tracking (via JIRA), readiness dashboards | QA leads, business testers |
| **Go-Live** | Final architecture baseline, all RICEFW objects in Deployed status | Go-live command center, operations |
| **Post-Go-Live Support** | Incident → Tower → Capability lookup, AI chatbot queries | L2/L3 support, ServiceNow teams |
| **Steady State** | Versioned architecture (Git), change tracking, compliance audits | Governance, audit, architecture review boards |

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
| `python scripts/fetch_smartsheet_data.py` | Pull RAID logs + Object Tracker from Smartsheet API → CSV cache |
| `python scripts/fetch_jira_data.py` | Pull defects + test cases from JIRA → JSON cache |
| `python scripts/gen_dashboard.py` | Generate interactive Plotly.js program + tower dashboards |
| `python scripts/gen_ricefw_tracker.py --all` | Generate per-tower RICEFW tracker documents |
| `python scripts/gen_testing_report.py --all` | Generate per-tower testing readiness reports |
| `python scripts/gen_tower_pages.py` | Generate tower + capability landing pages for portal |
| `python scripts/sync_sharepoint.py --all` | Upload outputs to SharePoint |
| `python scripts/gen_xlsx_templates.py --deploy` | Deploy blank Excel templates to all capabilities |
| `python scripts/scaffold_inputs.py` | Deploy input templates + upgrade legacy CSVs to 47-column xlsx |
| `python scripts/backfill_bpmn_to_xlsx.py` | Populate Business Architecture tab from BPMN XML |
| `python scripts/backfill_sample_data.py` | Pre-fill supplementary tabs with contextual sample data |
| `python scripts/cleanup_csvs.py` | Remove legacy CSVs superseded by xlsx workbooks |
| `python build_capability_master.py --apply` | Extract L1/L2/L3 hierarchy from Signavio manifest → update tower.yaml files |

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
| `deploy-pages.yml` | After generation completes, manual | Deploy HTML outputs to GitHub Pages with toolbar, sidebar, chatbot injection |
| `data-refresh.yml` | Daily weekday cron (06:00 UTC), manual | Pull latest Smartsheet RAID logs + JIRA data → commit updated CSV/JSON cache → trigger site rebuild |
| `chat-api.yml` | `repository_dispatch` (browser chatbot) | Receive chat question → call Anthropic Claude → write response JSON for browser polling |
| `sharepoint-reverse-sync.yml` | Power Automate webhook, manual | Pull updated xlsx from SharePoint → commit → triggers generation |

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
| `SMARTSHEET_TOKEN` | Smartsheet live data injection + data-refresh |
| `JIRA_PAT` | JIRA data fetch (defects, test cases) |
| `JIRA_BASE_URL` | JIRA REST API base (e.g. `https://jira.devtools.intel.com`) |
| `ANTHROPIC_API_KEY` | AI chatbot backend (Claude API) |
| `SP_TENANT_ID` | SharePoint sync |
| `SP_CLIENT_ID` | SharePoint sync |
| `SP_CLIENT_SECRET` | SharePoint sync |
| `SP_SITE_URL` | SharePoint sync |
| `SP_DOC_LIBRARY` | SharePoint sync (default: `Shared Documents`) |
| `SP_TARGET_FOLDER` | SharePoint sync (default: `Architecture/SAD`) |

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
│   ├── tower_registry.py         #   Centralized tower metadata (single source of truth)
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
├── config/                        # Centralized configuration
│   ├── tower_registry.json       #   Single source of truth for tower metadata
│   └── capability_master.yaml    #   L1/L2/L3 hierarchy (auto-generated)
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

## Operations Architecture

This section describes the end-to-end pipeline from an **operations** perspective: how credentials are managed, how inputs are validated, how data flows from source APIs through generation to published outputs, and how MCP servers integrate with Copilot for chatbot-driven architecture queries.

### Credential & Secret Management

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │                     SECRET MANAGEMENT FLOW                         │
  │                                                                    │
  │   Developer Machine                  GitHub Actions Runner         │
  │   ─────────────────                  ──────────────────────        │
  │                                                                    │
  │   .env.example ──(copy)──> .env      Settings > Secrets > Actions  │
  │                             │         ┌──────────────────────┐     │
  │     Never committed         │         │ SMARTSHEET_TOKEN     │     │
  │     (.gitignore)            │         │ IAPM_BEARER_TOKEN    │     │
  │                             │         │ BIC_AUTH_TOKEN       │     │
  │                             ▼         │ SP_TENANT_ID         │     │
  │                    src/config.py      │ SP_CLIENT_ID         │     │
  │                    (dotenv loader)    │ SP_CLIENT_SECRET     │     │
  │                             │         │ SAP_BI0_USER/PASS    │     │
  │                             │         │ SAP_DI0_USER/PASS    │     │
  │                             ▼         │ JIRA_API_TOKEN       │     │
  │                    All Python         └─────────┬────────────┘     │
  │                    scripts + MCP                │                  │
  │                    servers read                  ▼                  │
  │                    from os.environ     Workflow writes temp .env    │
  │                                        at runtime (never persisted)│
  │                                                 │                  │
  │                                                 ▼                  │
  │                                        src/config.py loads it      │
  │                                        (same code path as local)   │
  └─────────────────────────────────────────────────────────────────────┘
```

**Why `.env` is never in the repo**: The `.env` file contains plaintext API tokens and is excluded by `.gitignore`. In GitHub Actions, the workflow dynamically writes a temporary `.env` from encrypted GitHub Secrets (`${{ secrets.XXX }}`), which exists only during the workflow run and is destroyed when the runner terminates. This means:

- **Local development**: Developer copies `.env.example` → `.env` and fills in their own tokens
- **CI/CD execution**: GitHub Secrets are injected at runtime — no `.env` file is ever committed
- **Same code path**: `src/config.py` calls `load_dotenv()` in both cases — scripts don't care where the env vars came from

**Token rotation**: Smartsheet and IAPM tokens expire periodically. Update the GitHub Secret value in Settings when tokens are refreshed — no code changes needed.

### End-to-End Pipeline Flow

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  PHASE 1: CREDENTIAL SETUP                                         │
  │  ──────────────────────────                                         │
  │                                                                     │
  │  GitHub Secrets ──> Workflow writes .env ──> src/config.py loads    │
  │  (.env.example)     (runtime only)          (os.environ fallback)  │
  │                                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  PHASE 2: INPUT SOURCES & DATA EXTRACTION                          │
  │  ────────────────────────────────────────                           │
  │                                                                     │
  │  ┌─ MANUAL INPUT (Architect-authored) ──────────────────────────┐  │
  │  │                                                               │  │
  │  │  SharePoint Excel Workbooks (synced to towers/*/input/data/) │  │
  │  │  ├── CurrentFlows.xlsx  (current-state integration flows)    │  │
  │  │  ├── FutureFlows.xlsx   (future-state integration flows)     │  │
  │  │  └── Tabs: Flows · Context · Business Architecture           │  │
  │  │                                                               │  │
  │  │  This is the ONLY manual input from tower architects.        │  │
  │  │  sync_sharepoint.py keeps local copies in sync.              │  │
  │  │                                                               │  │
  │  └───────────────────────────────────┬───────────────────────────┘  │
  │                                      │                              │
  │  ┌─ API-AUTOMATED EXTRACTION ────────┼──────────────────────────┐  │
  │  │                                   │                           │  │
  │  │  ┌─────────────────┐  ┌──────────┴────────┐  ┌───────────┐  │  │
  │  │  │ Smartsheet API  │  │ Signavio/BIC API  │  │ IAPM API  │  │  │
  │  │  │ ───────────────│  │ ─────────────────│  │ ─────────│  │  │
  │  │  │ Object Tracker  │  │ BPMN Manifest    │  │ App meta  │  │  │
  │  │  │ RAID Log        │  │ Process models   │  │ 30K+ apps │  │  │
  │  │  │ Timeline        │  │ L1/L2/L3 hier.   │  │ statuses  │  │  │
  │  │  └───────┬─────────┘  └────────┬─────────┘  └─────┬─────┘  │  │
  │  │          │                      │                  │         │  │
  │  │          ▼                      ▼                  ▼         │  │
  │  │  smartsheet_loader    build_capability_m.   iapm_lookup.py   │  │
  │  │  .py (live API)       py (Signavio CSV)     (API or CSV)    │  │
  │  │                                                              │  │
  │  └─────────────────────────────────────────────────────────────┘  │
  │                                                                     │
  │  ┌─ POC FALLBACKS (ranked, used when API unavailable) ──────────┐  │
  │  │                                                               │  │
  │  │  Priority  Source              Trigger                        │  │
  │  │  ────────  ──────              ───────                        │  │
  │  │  1st       API live query      Token present in .env          │  │
  │  │  2nd       CSV cache           data/smartsheet/*.csv cached   │  │
  │  │  3rd       Manual download     Browser export → data/ folder  │  │
  │  │                                                               │  │
  │  │  Goal: 100% API. POC fallback is temporary.                  │  │
  │  │                                                               │  │
  │  └──────────────────────────────────────────────────────────────┘  │
  │                                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  PHASE 3: DOCUMENT GENERATION (fully automated)                    │
  │  ──────────────────────────────────────────────                     │
  │                                                                     │
  │  tower.yaml ──> gen_systems_arch.py ──> Jinja2 templates           │
  │  xlsx data        (orchestrator)         systems_architecture.md.j2│
  │  BPMN files           │                  ricefw_tracker.md.j2      │
  │  IAPM metadata        │                  testing_report.md.j2      │
  │  Smartsheet data      │                  dashboard.html.j2         │
  │                       ▼                                             │
  │            ┌──────────────────────────────┐                        │
  │            │  Per-Capability Outputs       │                        │
  │            │  ─────────────────────────    │                        │
  │            │  <CAP>-Architecture.md        │                        │
  │            │  <CAP>-RICEFW-Tracker.md      │                        │
  │            │  <CAP>-Testing-Report.md      │                        │
  │            └──────────────┬───────────────┘                        │
  │                           │                                         │
  │                           ▼                                         │
  │                    gen_pdf.py                                       │
  │                    (MD → HTML with Mermaid.js)                     │
  │                           │                                         │
  │                           ▼                                         │
  │            ┌──────────────────────────────┐                        │
  │            │  <CAP>-Architecture.html      │                        │
  │            │  <CAP>-RICEFW-Tracker.html    │                        │
  │            │  <CAP>-Testing-Report.html    │                        │
  │            │  <TOWER>-Dashboard.html       │                        │
  │            └──────────────┬───────────────┘                        │
  │                           │                                         │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  PHASE 4: PUBLISH & DISTRIBUTE (fully automated)                   │
  │  ───────────────────────────────────────────────                    │
  │                           │                                         │
  │              ┌────────────┼────────────┐                           │
  │              ▼            ▼            ▼                            │
  │      deploy-pages.yml  sync_share   Git commit                     │
  │      (GitHub Pages)    point.py     (versioned                     │
  │           │            (SharePoint)  in repo)                      │
  │           ▼                │                                        │
  │   ┌──────────────┐  ┌────┴──────┐  ┌────────────┐                │
  │   │ GitHub Pages  │  │SharePoint │  │ GitHub Repo │                │
  │   │ (HTML + nav)  │  │(HTML+PDF) │  │ (MD + HTML) │                │
  │   │ Interactive   │  │Architect  │  │ Version     │                │
  │   │ dashboards    │  │workspace  │  │ history     │                │
  │   └──────────────┘  └───────────┘  └────────────┘                │
  │                                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  PHASE 5: MCP SERVERS (Copilot Chatbot Integration)                │
  │  ──────────────────────────────────────────────────                 │
  │                                                                     │
  │  VS Code / Copilot Chat                                            │
  │        │                                                            │
  │        ▼                                                            │
  │  .vscode/settings.json (MCP server registration)                   │
  │        │                                                            │
  │        ├──> iao-smartsheet ──> Smartsheet API (or CSV fallback)    │
  │        ├──> iao-iapm ──────> IAPM CSV (30K+ apps)                 │
  │        ├──> iao-jira ──────> JIRA REST API (placeholder)          │
  │        ├──> iao-sap-odata ─> SAP Gateway OData (placeholder)      │
  │        └──> iao-bic ───────> BIC/Signavio API (placeholder)       │
  │                                                                     │
  │  User asks: "What RICEFW objects are in FPR DS-020?"               │
  │  Copilot invokes: iao-smartsheet > get_ricefw_objects(tower, cap)  │
  │  Response: Live data from Smartsheet (or cached CSV)               │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘
```

### Data Source Priority

Every data source in the pipeline follows **API-first extraction**. Manual inputs are limited to architect-authored XLSX workbooks synced via SharePoint:

| Data Source | Production (Target) | POC Fallback | Manual? |
|-------------|-------------------|--------------|---------|
| **Integration Flows** (CurrentFlows/FutureFlows) | SharePoint sync → `towers/*/input/data/*.xlsx` | Same (architect-authored) | **Yes** — only manual input |
| **RICEFW Objects** | Smartsheet API → `smartsheet_loader.py` | CSV cache in `data/smartsheet/` | No |
| **RAID Log** | Smartsheet API → `smartsheet_loader.py` | CSV cache | No |
| **BPMN Process Models** | BIC/Signavio API → `bpmn_parser.py` | CSV manifest export | No |
| **Capability L1/L2/L3 Hierarchy** | BIC API → `build_capability_master.py` | Signavio manifest CSV | No |
| **Application Metadata** (IAPM) | IAPM API → `iapm_lookup.py` | CSV cache (`IAPM_All_Solutions.csv`) | No |
| **Test Cases / Defects** | JIRA API → `jira_server.py` | Placeholder (API pending) | No |
| **SAP Dev Object Status** | SAP OData → `sap_odata_server.py` | Placeholder (API pending) | No |

### Single Source of Truth — Configuration Files

The pipeline eliminates manual mapping by centralizing metadata in two files:

| File | Purpose | Updated By |
|------|---------|-----------|
| `config/tower_registry.json` | Tower shortcodes, display names, icons, Signavio folder mappings, aliases | Manual (add new tower) or future API auto-discovery |
| `config/capability_master.yaml` | L1/L2/L3 hierarchy — 131 capabilities, 309 process steps | `build_capability_master.py --apply` (auto-extracted from Signavio manifest) |

Adding a new tower requires **one** edit to `tower_registry.json`. The capability master auto-regenerates from the Signavio BPMN manifest. All downstream consumers (`gen_dashboard.py`, `gen_ricefw_tracker.py`, `gen_testing_report.py`, `smartsheet_loader.py`, `deploy-pages.yml`) read from the centralized registry — no code changes needed.

### Input Validation Checkpoints

| Stage | What's Checked | Action on Failure |
|-------|---------------|-------------------|
| **Credential load** | `src/config.py` reads `.env` or `os.environ` | Missing token → graceful fallback to CSV cache |
| **Manifest parse** | `build_capability_master.py` parses Signavio CSV | Unknown tower folder → `[WARN]` printed, tower skipped |
| **Tower discovery** | `gen_systems_arch.py --all` scans `towers/*/` directories | Missing `tower.yaml` → capabilities discovered from directory structure |
| **Capability resolution** | `cap_name_resolver.py` multi-source fallback | tower.yaml → BIC API → Smartsheet → BPMN XML → L1 directory name |
| **Excel workbook parse** | `xlsx_loader.py` reads multi-tab `.xlsx` | Missing/empty tabs → placeholder text generated |
| **BPMN parse** | `bpmn_parser.py` reads `.bpmn` XML | Missing BPMN → Section 3 shows "No BPMN files" |
| **Smartsheet injection** | `smartsheet_loader.py` queries API | No token → falls back to `data/smartsheet/` CSV cache |
| **IAPM lookup** | `iapm_lookup.py` resolves application metadata | No token → loads from `data/iapm/IAPM_All_Solutions.csv` |
| **HTML generation** | `gen_pdf.py` converts MD → HTML with Mermaid.js | Template not found → error (non-recoverable) |
| **Deploy workflow** | `deploy-pages.yml` reads `tower_registry.json` | Unknown tower → generic name/icon fallback |

### MCP Server — Chatbot Readiness

Each MCP server follows the same pattern to ensure Copilot chatbot queries always return useful responses:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │                      MCP SERVER PATTERN                         │
  │                                                                 │
  │  User query via Copilot Chat                                   │
  │         │                                                       │
  │         ▼                                                       │
  │  .vscode/settings.json (stdio transport registration)          │
  │         │                                                       │
  │         ▼                                                       │
  │  mcp_servers/<name>_server.py                                  │
  │         │                                                       │
  │         ├──(1) Check: API token in os.environ?                 │
  │         │       YES ──> Call live API endpoint                  │
  │         │       NO  ──> Load CSV fallback from data/           │
  │         │                                                       │
  │         ├──(2) Normalize tower name (tower_registry.py)        │
  │         │                                                       │
  │         ├──(3) Filter data by tower / capability / status      │
  │         │                                                       │
  │         └──(4) Return structured JSON to Copilot               │
  │                                                                 │
  │  Copilot formats response for user                             │
  └─────────────────────────────────────────────────────────────────┘
```

**Ensuring accuracy**: MCP servers use the same `tower_registry.py` normalization as the generation pipeline, so tower names from Smartsheet (e.g., "03. FPR") resolve identically whether queried via chatbot or processed during document generation.

### Output Document Uniformity

All generated documents follow a consistent structure enforced by Jinja2 templates:

| Document Type | Template | Sections | Styling |
|--------------|----------|----------|---------|
| Systems Architecture | `systems_architecture.md.j2` | Title page, TOC, Business Architecture, Data Architecture, Application Architecture, Technology Architecture, RICEFW, RAID, Roadmap | Canonical page footers, Mermaid diagrams, PDF download button |
| RICEFW Tracker | `ricefw_tracker.md.j2` | Title page, TOC, per-type object tables, status summary | Same page footers, capability names resolved from tower.yaml |
| Testing Report | `testing_report.md.j2` | Title page, TOC, test phases, defect summary, readiness | Same page footers, capability names resolved from tower.yaml |
| Dashboard | `dashboard.html.j2` | KPI cards, 7 Plotly charts, filter chips, detailed tables | Plotly.js 2.32.0, responsive layout, print-friendly chart snapshots |

**Consistency enforcement**: All templates share canonical CSS for page footers, title pages, and table formatting. The `gen_pdf.py` script wraps all MD outputs in an identical HTML shell with Mermaid.js rendering and a PDF download button.

---

## Security

### Credential Security Model

```
  ┌─────────────────────────────────────────────────────────────────┐
  │                    SECURITY BOUNDARIES                          │
  │                                                                 │
  │  ┌─────────────────────────────────────────────────────────┐   │
  │  │  TRUSTED ZONE: Developer Machine                        │   │
  │  │                                                         │   │
  │  │  .env (gitignored, never committed)                     │   │
  │  │  Contains: API tokens, passwords                        │   │
  │  │  Access: Single developer only                          │   │
  │  └─────────────────────────────────────────────────────────┘   │
  │                                                                 │
  │  ┌─────────────────────────────────────────────────────────┐   │
  │  │  TRUSTED ZONE: GitHub Actions                           │   │
  │  │                                                         │   │
  │  │  GitHub Secrets (AES-256 encrypted at rest)             │   │
  │  │  Injected at runtime: ${{ secrets.XXX }}                │   │
  │  │  Written to temp .env (destroyed with runner)           │   │
  │  │  Access: Repo admins only                               │   │
  │  └─────────────────────────────────────────────────────────┘   │
  │                                                                 │
  │  ┌─────────────────────────────────────────────────────────┐   │
  │  │  PUBLIC ZONE: Repository & GitHub Pages                 │   │
  │  │                                                         │   │
  │  │  NO credentials stored in code or committed files       │   │
  │  │  .env in .gitignore (line 1)                            │   │
  │  │  .env.example has placeholders only (no real values)    │   │
  │  │  Generated HTML contains no API tokens or secrets       │   │
  │  │  Repo is Private (GitHub Enterprise Cloud)              │   │
  │  │  GitHub Pages is Private (collaborators only)           │   │
  │  └─────────────────────────────────────────────────────────┘   │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘
```

### Security Controls

| Control | Implementation | Status |
|---------|---------------|--------|
| **No secrets in code** | `.env` excluded by `.gitignore`; `.env.example` has placeholders only | Active |
| **GitHub Secrets encryption** | AES-256 at rest; injected as masked env vars at runtime | Active |
| **Temp .env in CI/CD** | Written by workflow step, destroyed when runner terminates | Active |
| **OAuth2 for SharePoint** | Client credentials flow (`SP_CLIENT_ID` + `SP_CLIENT_SECRET`) — no user passwords | Active |
| **Graceful degradation** | Missing tokens → fallback to CSV cache (no hard failures) | Active |
| **Private repository** | GitHub Enterprise Cloud — only authorized collaborators | Active |
| **Private GitHub Pages** | Access restricted to repository collaborators | Active |
| **No secrets in outputs** | Generated HTML/PDF contain zero credentials or tokens | Active |
| **Token isolation** | Each API system has its own credential — compromise of one doesn't affect others | Active |

### How GitHub Actions Gets Credentials Without `.env` in the Repo

The workflow dynamically creates a temporary `.env` file from GitHub Secrets:

```yaml
# In generate-architecture.yml (runtime only — never persisted)
- name: Write .env from secrets
  run: |
    cat > .env <<EOF
    SMARTSHEET_TOKEN=${{ secrets.SMARTSHEET_TOKEN }}
    IAPM_BEARER_TOKEN=${{ secrets.IAPM_BEARER_TOKEN }}
    BIC_AUTH_TOKEN=${{ secrets.BIC_AUTH_TOKEN }}
    JIRA_BASE_URL=${{ secrets.JIRA_BASE_URL }}
    JIRA_USER_EMAIL=${{ secrets.JIRA_USER_EMAIL }}
    JIRA_API_TOKEN=${{ secrets.JIRA_API_TOKEN }}
    ANTHROPIC_API_KEY=${{ secrets.ANTHROPIC_API_KEY }}
    LLM_MODEL=${{ secrets.LLM_MODEL }}
    SP_TENANT_ID=${{ secrets.SP_TENANT_ID }}
    SP_CLIENT_ID=${{ secrets.SP_CLIENT_ID }}
    SP_CLIENT_SECRET=${{ secrets.SP_CLIENT_SECRET }}
    SP_SITE_URL=${{ secrets.SP_SITE_URL }}
    SP_DOC_LIBRARY=${{ secrets.SP_DOC_LIBRARY }}
    SP_TARGET_FOLDER=${{ secrets.SP_TARGET_FOLDER }}
    EOF
```

This file exists **only during the workflow run**. GitHub Actions runners are ephemeral — the entire VM (and its filesystem) is destroyed after the job completes. The `.env` file is never committed, never cached, and never visible in logs (GitHub automatically masks secret values in output).

### Managing Secrets

| Action | Where | Who |
|--------|-------|-----|
| **Add/update a secret** | GitHub → Settings → Secrets and variables → Actions | Repo admin |
| **Rotate a token** | Replace the secret value in GitHub Settings; update local `.env` | Repo admin |
| **Revoke access** | Delete the secret from GitHub Settings; regenerate token at source | Repo admin |
| **Audit access** | GitHub → Settings → Audit log → filter by `secret` events | Repo admin |
| **Local development** | Edit `.env` directly — changes stay on developer machine only | Developer |

---

## License

Internal use only — Intel confidential. Do not make this repository or its contents publicly accessible.
