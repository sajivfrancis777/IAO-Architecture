<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-122 — E2E-122</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-122 · Forecast to Stock</p>
  <p style="font-size:14px; color:#888;">IAO Program · Release 2<br/>
  Generated: March 2026<br/>
  Sajiv Francis</p>
  <p style="font-size:12px; color:#aaa;">IAO Architecture Pipeline — Intel Confidential</p>
</div>

<style>
@media print {
  @page { margin: 0.75in; }
  .mermaid { page-break-inside: avoid; overflow: visible; }
  pre, table { page-break-inside: avoid; }
  h2, h3, h4 { page-break-after: avoid; }
}
.mermaid { overflow: visible; }
.mermaid svg { max-width: 100%; height: auto !important; }
.page-footer {
  padding-top: 8px;
  border-top: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: #888;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 6px 20px;
  background: #fff;
}
@media print {
  .page-footer { position: fixed; bottom: 0; left: 0.75in; right: 0.75in; }
}
.page-footer a { color: #00aeef; text-decoration: none; font-weight: 500; }
.page-footer a:hover { color: #0071c5; text-decoration: underline; }
</style>

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

<a id="toc"></a>

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Business Context & Objectives](#2-business-context--objectives)
   - 2.1 [Classification](#21-classification)
   - 2.2 [Business Drivers](#22-business-drivers)
   - 2.3 [Success Criteria](#23-success-criteria)
   - 2.4 [Companion Documents](#24-companion-documents)
3. [Business Architecture (TOGAF "B")](#3-business-architecture-togaf-b)
   - 3.1 [Business Process Overview](#31-business-process-overview)
   - 3.2 [Business Process Diagrams](#32-business-process-diagrams)
   - 3.3 [Business Roles & Responsibilities](#33-business-roles--responsibilities)
4. [Data Architecture (TOGAF "D")](#4-data-architecture-togaf-d)
   - 4.1 [Data Entities & Ownership](#41-data-entities--ownership)
   - 4.2 [Data Flow Diagrams](#42-data-flow-diagrams)
   - 4.3 [Data Lineage](#43-data-lineage)
   - 4.4 [RICEFW Data Objects](#44-ricefw-data-objects)
   - 4.5 [Data Governance & Quality](#45-data-governance--quality)
5. [Application Architecture (TOGAF "A")](#5-application-architecture-togaf-a)
   - 5.1 [Current-State Application Landscape](#51-current-state--current-state-application-landscape)
   - 5.2 [Future-State Application Landscape](#52-future-state--future-state-application-landscape)
   - 5.3 [Change Impact Summary](#53-change-impact-summary)
   - 5.4 [Component Overview](#54-component-overview)
   - 5.5 [RICEFW Inventory](#55-ricefw-inventory)
   - 5.6 [Integration Patterns](#56-integration-patterns)
6. [Technology Architecture (TOGAF "T")](#6-technology-architecture-togaf-t)
   - 6.1 [Platform & Infrastructure](#61-platform--infrastructure)
   - 6.2 [SAP Development Object Status](#62-sap-development-object-status)
   - 6.3 [NFRs & Design Principles](#63-nfrs--design-principles)
   - 6.4 [Security & Governance](#64-security--governance)
7. [Project Context](#7-project-context)
   - 7.1 [Project Roadmap & Go-Live Plan](#71-project-roadmap--go-live-plan)
   - 7.2 [RAID Log](#72-raid-log)
   - 7.3 [Recommendations & Next Steps](#73-recommendations--next-steps)

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-122 E2E-122** within the IAO program. It includes 1 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Forecast to Stock |
| **Capability** | E2E-122 - E2E-122 |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Forecast to Stock |
| **L2 Capability** | E2E-122 - E2E-122 |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-122 Process Migration | Migrate E2E-122 business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-122 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **1 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-122 E2E-122.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-122_C_IP_Sending_spares_for_repair_to_IMR_site_in_ECC | E2E-122_C_IP_Sending_spares_for_repair_to_IMR_site_in_ECC | IMR Site ECC, Intel Products Lab (Faulty part) | 17 | 3 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-122_C_IP_Sending_spares_for_repair_to_IMR_site_in_ECC — E2E-122_C_IP_Sending_spares_for_repair_to_IMR_site_in_ECC

**Swim Lanes**: IMR Site ECC · Intel Products Lab (Faulty part) | **Tasks**: 17 | **Gateways**: 3

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial, sans-serif','primaryColor': '#e8f0fe', 'primaryBorderColor': '#0071c5','lineColor': '#37474F', 'secondaryColor': '#f5f8fc'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'curve': 'basis', 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TD
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph IMR Site ECC
        n1["Create Inbound Delivery"]
        n2["Post Goods Recept"]
        n3["Create Purchase Order"]
        n4["Repair Completed"]
        n5["AR Posting From Finance"]
        n16["fa:fa-user Create FOC Purchase Order"]
        n17["fa:fa-user Ship-Out Repaired part through ISM"]
        n19(["fa:fa-stop AR Posted"])
        n25{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Intel Products Lab (Faulty part)
        n6["Sub Con Purchase Requisition"]
        n7["Sub- Con Purchase Order"]
        n8["Trigger GTS Check"]
        n9["Calculate Taxes"]
        n10["Outbound Delivery"]
        n11["Goods Issue (Defective Material)"]
        n12["Inbound Delivery against Sub-Con PO"]
        n13["Goods Receipt against SubCon PO (On Physical Receipt)"]
        n14["Trigger GTS Check"]
        n15["SubCon PO Invocie Posting"]
        n18(["fa:fa-play PO triggered from IRIS"])
        n20(["fa:fa-stop GTS Check Complete"])
        n21(["fa:fa-stop Taxes Calculated"])
        n22(["fa:fa-stop GTS Check Complete"])
        n23(["fa:fa-stop Invoice Posted"])
        n24(["fa:fa-stop Defective material issued against Sub Con PO"])
        n26{{"fa:fa-arrows-alt parallelGateway"}}
        n27{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n7
    n7 --> n26
    n26 --> n8
    n8 --> n20
    n26 --> n9
    n9 --> n21
    n26 --> n10
    n10 --> n11
    n26 --> n16
    n16 --> n1
    n1 --> n2
    n2 --> n3
    n3 -->|"Perform Repair
As-Is"| n4
    n4 --> n17
    n5 --> n19
    n17 --> n25
    n25 --> n12
    n25 --> n5
    n12 --> n27
    n14 --> n22
    n27 --> n13
    n27 --> n14
    n13 --> n15
    n15 --> n23
    n18 --> n6
    n11 --> n24
    class n16 userTask
    class n17 userTask
    class n18 startEvt
    class n19 endEvt
    class n20 endEvt
    class n21 endEvt
    class n22 endEvt
    class n23 endEvt
    class n24 endEvt
    class n25 gateway
    class n26 gateway
    class n27 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl1v4jgU_StWRhUdCaQ4HwTysBINpELaqhV0dx-WfTCJA1ZNkrWdtgzDf1-b2IGkdFazy0MrH5977ofvdXywkiLFVmjd3BxITkQIDj2xxTvcC0FvjTju9UEN_I4YQWuKeU9xsiIXS_LtRINe-a5oCovRjtC9Qpd4U2Dw27wPJtKQ9gFHOR9wzEjW6_dKRnaI7aOCFkyxv-BRZmcnb3rrrmApZmeCbQcw8aUpJTk-w27gBV6s7DhOijxtiWZ-NsqS3lEFR4u3ZIuYOIVfcfyA3v8gqdjKdYYox5KzFTv6K1pjqnIUrFJYUrFXUwzClZ9cFmxZooTkG4l7toQYyl_OkG8fj-B4c7PKG6fgebrKgfwlFHE-xRngQsKzVwEyQmn4xYsmsW_3uWDFCw6_OLNg6jr9RGUSytTtviru4A2TzVaE64Kmmjp4UzmETvneZ--hY_fZXv7t-MJ5evYUDZ2RM2o83QUwgpHxlGXZ__Ik68qeEX_RvmZu7MTTxhf0h35kf9QzaU69YAK7dcLslST4QjSOY3d2LtVs6EP7c9G72B3aUUd0gwR-Q_uz4DjyGsHYD2IYfCpY--tGWa2fWJEYQXfmx34jGNzBeOJ8KuhNoDfSEUqdDUPlFswfFmBJBAazSG-pXw7_XFkRwzJ8MM_XRZWnYIopecVsv7L-uiA6kvhUcAHuiyLlYIETXIo2xT1rPVVMtinH4FHNXJvmSdoCl4gwEBW7kmKB0zbDl4zJAih3cgBAzIodiEmO8gS3iXAomRkKMzRQjQK09_gx-mEEMGibLbekHDxWAtRh4RSUasTElhXVRpZu-dCxH982AlwUJdDBnvL4elk0_3AwRMRY8cYHiAqljijF9L7umpV1PNZGcq66x5YLTIFshbRKBAfyMgG3Maqo2J9ivHSmarGs1rKo-Tn7Bf67IpwIUuTtHIKaPWjTrxRrJInPjGw2slD3z0sQbXHy0qaM1cEjmlRUVf8ZvWPeKZgtGbLAP2owqFqxbq455xUGt3IOcCIkFTxIXXXnf-2YqKbsti1AG0Ry2agqu1Nyjx0rt3GkupiU4tKktgC3j_Lfds9Jgqihdb17_14Z6Ndl1qrz_LVICDad3eGOzl1VUnmZSANRy8uOzNQQzBfzZbfF7E4vNpE009W1gB2L04GB5gA_NLHz0x7cjoXKW965nwyJ12Gfz32nzx0Q1RHp5TmB5mhbWsOfG7jaKPiPU5oPwWDwi5wlvQzqpTPUa0fvj_R6pPftzv5Yr8d6H3b2oTGAtgY-MIxLaACz1pKGXy9dvXTV8ru82DHLCrbT998qn_DBXI7wd3lZa6anZU2qvl6b0KHJ3TeeDMPpAIYAdSyOkYTah9NYaE3odgETFXQ10IhqJ44xgbrmTX1MQbyLD-6pbOal0caDT_BR895q42P9Nmqhjn0VhVdR5yrqXkW9q6hvniNteHgdDgxs9a0dZjtEUis8WKcnunzGpzhTnxvr2LdQJYrlPk-s8PSUtaoylZZTguSnaleDx38AMw-j7g==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| IMR Site ECC | E2E-122_C_IP_Sending_spares_for_repair_to_IMR_site_in_ECC | |
| Intel Products Lab (Faulty part) | E2E-122_C_IP_Sending_spares_for_repair_to_IMR_site_in_ECC | |

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

#### 4.2.1 Current-State — Current-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E122CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E122CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E122CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E122CDAA_e_g_XEUS -.-> E2E122CDAD_e_g_Azure_SQL
    end
    style E2E122CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E122CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E122CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E122CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E122CDAA_e_g_MES_300 -.-> E2E122CDAD_e_g_SAP_HANA
    end
    style E2E122CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E122CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E122CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlYFumzAQhl_FchVlk5KOJCVZkVrJCWStRKuupNukMiEHjsSqAwjMmjTNu8-GhG5Z6KraEsLnu__O3yGzxn4cADZwo7FmERMGWjfFHBbQNFBzSjNotlAzAz9PmVjZ8Au42uBxXO4Urt9oyuiUQ9ZU0WEcCYc9FQIdPVkqN2Ub0wXjK2V1YBYDurtsISIDeXOjPHj86M9pKgqNPIMruvzOAjGX65DyDKTPXCy4TafAVSKR5soWyeqdhPosmkljT5emlEYPL6YTfbNBm0bDjaoUaDJ0IySHz2mWmRAimiTDeIlCxrlxNNTN8XjcykQaP4BxpGmDwbC_XbYfVU1GN1m2_JjHqdrumfq-XjAdrfhWjuhmnwwqua41MHvdWrnOULe62p4cxPylvPF4qA_1Sm800uSo1ev31bYblYpZPp2lNJkjq2t1ut2RSUa2B97MI095Cp7z1b53MXLxz9JdjYCl4AsWRxU1Nap4UoT_sO4cGQnHs2Ok3qWCYRgl1QNB5l7ODy528-BzL5DPwD9x8xA0eWqlVjgh6eTij0qzIPtqHah93D6vzVWGQhRsgYgVh3oaO-REzQq5pan5N_JOsvwvZIfceBfkmryP8ZXleD1N22GWSySXbyJdJX4FtPRByudNnLe1HES9S_Ym0jvnd4GuSYzOzs6ft5TMgiz6hMjNpXyOGQcXP7_ydey10IaZPMH9H9j8QEMmmRBEbkcXlxNrNLm7tZBtfbGuzZqm2rcvVttT7SdJwplP1e7hBtqeWdMskwqq7uXDfbI9S8pbUdCOw7bNQijlywvkYEfKE-7462pW_E9PT_-Bj1t4AemCsgAba1zc__LvEUBIcy7wpoVpLmJnFfnYKK5onCcBFWAyKokuSuPmNwPK98U=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E122FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E122FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E122FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E122FDAA_e_g_XEUS -.-> E2E122FDAD_e_g_Azure_SQL
    end
    style E2E122FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E122FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E122FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E122FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E122FDAA_e_g_MES_300 -.-> E2E122FDAD_e_g_SAP_HANA
    end
    style E2E122FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E122FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E122FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlYFumzAQhl_FchVlk5KOJCVZkVrJCbBWolVX0m1SmZADR2LVAQRmTZrm3WdDQrcs6araEsLnu__O3yGzwkESAjZwo7FiMRMGWjXFDObQNFBzQnNotlAzh6DImFg68Au42uBJUu2Urt9oxuiEQ95U0VESC5c9lQIdPV0oN2Wz6ZzxpbK6ME0A3V22EJGBvLlWHjx5DGY0E6VGkcMVXXxnoZjJdUR5DtJnJubcoRPgKpHICmWLZfVuSgMWT6Wxp0tTRuOHF9OJvl6jdaPhxXUKNB56MZIj4DTPTYgQTdNhskAR49w4GuqmbdutXGTJAxhHmjYYDPubZftR1WR000UrSHiSqe2eqe_qhZPRkm_kiG72yaCW61oDs9c9KNcZ6lZX25GDhL-UZ9tDfajXeqORJsdBvX5fbXtxpZgXk2lG0xmyulan27VNMnJ88Kc-eSoy8N2vzr2HkYd_Vu5qhCyDQLAkrqmpUceTMvyHdefKSDieHiP1LhUMw6io7gkyd3J-8LBXhJ97oXyGwYlXRKDJUyu10glJJw9_VJol2VfrQO3j9vnBXFUoxOEGiFhyOExji5yoWSO3NDX_Rt5JF_-F7JIb_4Jck_cxvrJcv6dpW8xyieTyTaTrxK-Alj5I-byJ86aWvai3yd5Eeuv8LtAHEqOzs_PnDSWzJIs-IXJzKZ824-Dh51e-jp0WOjCVJ7j_A1sQasgkY4LI7ejicmyNxne3FnKsL9a1eaCpzu2L1fFV-0machZQtbu_gY5vHmiWSQVV9_L-Pjm-JeWtOGwnUdthEVTy1QWytyPVCbf8dTVr_qenp__Axy08h2xOWYiNFS7vf_n3CCGiBRd43cK0EIm7jANslFc0LtKQCjAZlUTnlXH9G4CA9-8=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-122-R001 | Report | E2E-122 operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-122-C001 | Conversion | Legacy data migration for E2E-122 | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-122.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '16px', 'fontFamily': 'Segoe UI, Arial, sans-serif'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        E2E122C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E122C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E122CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E122CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E122C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E122CMW_e_g_Azure_Service_Bus
    E2E122CMW_e_g_Azure_Service_Bus --> E2E122C_e_g_XEUS

    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px

    subgraph Legend["📐 LEGEND"]
        direction LR
        L_APP["📦 Application"]:::app
        L_MW["🔗 Middleware"]:::middleware
        L_DE>"📄 Data Entity"]:::data
        L_EOL["⛔ End-of-Life"]:::eol
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVWtv4jAQ_CtWKsQXaAMtj0YVUkLCiVNoq6aPOx2nyMQLWDVJFDttKeW_n51QwquiZ6SgrGdnndmxvdCCiIBmaKXSgoZUGGhRFlOYQdlA5RHmUK6gMocgTaiYu_ACTE2wKMpnMugjTigeMeBllT2OQuHR94yg1ozfFEzFenhG2VxFPZhEgB76FWTKRFZBHIe8yiGh4_JSoVn0GkxxIjK-lMMAvz1RIqbyfYwZB4mZihlz8QiYKiqSVMVC-SVejAMaTmTwQpehBIfPRaihL5doWSoNw3UJdG8NQyRHqYSqVbmgYEoHWECVhjymCRDExZwBChjmHLjE5PDs3YYxGqWchsA5ysaYMmac9OSwGhUukugZjBOr3W7q1uq1-qq-xKjHb5UgYlFinOi6vsOJ4xgVI-e0Gop1zanrrZbV_A9OggXe57TbRzhrW5yfcwRzKV6C51JT1NipNKOEMHjFCWwqYjfNQhGn1ewVbN9YPURsTxGl8YbK3a6uH-PMWXk6miQ4niLT_TPUhilpnxP5JOcNZN7euv2ued-_uUau-du5G2p_8yQ1iDREIGgUIveuiDp1p1avd33wJ_7A8fxzXd-kDaCJ4HRyiuQcknOS0TAM2eLDDL-cB-9gupr4OnfwlGWb72kCvgfJCw3At1K-9YG1Vk6VodAKhSQq5y0at0dvOxl9N-LCd5jc86HobC4yuMiZFQCtAFej5KxzRTv5hPeIzlDfjgL599O7ub46o528rHJmXhBC8tmjA6LKvdf5GGoZnZ11QlKZt3357FEGQ-3jmBhb1F-BVJm9jqhlrcyTHQeWu7HVe_qxrb6Zaq5T9e_s6D3TujCROm1ZhOjIdX441_Y33Or60uO7BjPjmNEAK_ABi7n-4GnXR4PCK196x_VtZ9cltjqGnFDI22S3-3mKc5NvynqTXEggqUbjqkvHqzLyHNiwSiFqLsqnsA31Wwt7eXm5d6ZpFW0GyQxTohkLLbvF5B1IYIxTJrRlRcOpiLx5GGhGdrloaSwXCjbFsgmzPLj8B2jXPtE=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-122.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '16px', 'fontFamily': 'Segoe UI, Arial, sans-serif'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        E2E122F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E122F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E122FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E122FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E122F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E122FMW_e_g_Azure_Service_Bus
    E2E122FMW_e_g_Azure_Service_Bus --> E2E122F_e_g_XEUS

    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px

    subgraph Legend["📐 LEGEND"]
        direction LR
        L_APP["📦 Application"]:::app
        L_MW["🔗 Middleware"]:::middleware
        L_DE>"📄 Data Entity"]:::data
        L_EOL["⛔ End-of-Life"]:::eol
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVWtv4jAQ_CtWKsQXaAMtj0YVUkLCiVNoq6aPOx2nyMQLWDVJFDttKeW_n51QwquiZ6SgrGdnndmxvdCCiIBmaKXSgoZUGGhRFlOYQdlA5RHmUK6gMocgTaiYu_ACTE2wKMpnMugjTigeMeBllT2OQuHR94yg1ozfFEzFenhG2VxFPZhEgB76FWTKRFZBHIe8yiGh4_JSoVn0GkxxIjK-lMMAvz1RIqbyfYwZB4mZihlz8QiYKiqSVMVC-SVejAMaTmTwQpehBIfPRaihL5doWSoNw3UJdG8NQyRHqYSqVbmgYEoHWECVhjymCRDExZwBChjmHLjE5PDs3YYxGqWchsA5ysaYMmac9OSwGhUukugZjBOr3W7q1uq1-qq-xKjHb5UgYlFinOi6vsOJ4xgVI-e0Gop1zanrrZbV_A9OggXe57TbRzhrW5yfcwRzKV6C51JT1NipNKOEMHjFCWwqYjfNQhGn1ewVbN9YPURsTxGl8YbK3a6uH-PMWXk6miQ4niLT_TPUhilpnxP5JOcNZN7euv2ued-_uUau-du5G2p_8yQ1iDREIGgUIveuiDp1p1av93zwJ_7A8fxzXd-kDaCJ4HRyiuQcknOS0TAM2eLDDL-cB-9gupr4OnfwlGWb72kCvgfJCw3At1K-9YG1Vk6VodAKhSQq5y0at0dvOxl9N-LCd5jc86HobC4yuMiZFQCtAFej5KxzRTv5hPeIzlDfjgL599O7ub46o528rHJmXhBC8tmjA6LKvdf5GGoZnZ11QlKZt3357FEGQ-3jmBhb1F-BVJm9jqhlrcyTHQeWu7HVe_qxrb6Zaq5T9e_s6D3TujCROm1ZhOjIdX441_Y33Or60uO7BjPjmNEAK_ABi7n-4GnXR4PCK196x_VtZ9cltjqGnFDI22S3-3mKc5NvynqTXEggqUbjqkvHqzLyHNiwSiFqLsqnsA31Wwt7eXm5d6ZpFW0GyQxTohkLLbvF5B1IYIxTJrRlRcOpiLx5GGhGdrloaSwXCjbFsgmzPLj8B6-cPuk=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 5.3 Change Impact Summary

| Change Type | Flow Chain | Detail |
|-------------|-----------|--------|
| **UNCHANGED** | e.g. MES Route to ICOST | No change |

**Totals**: 0 new - 0 removed - 0 modified - 1 unchanged

### 5.4 Component Overview

#### System Inventory

| System | IAPM ID | Status |
|--------|---------|--------|
| e.g. MES 300 | - | N/A |
| e.g. XEUS | - | N/A |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-122-I001 | Interface | E2E-122 inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-122-E001 | Enhancement | E2E-122 custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-122-F001 | Form/Report | E2E-122 operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### 6.1.1 Current-State — Current-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E122CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E122CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E122CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E122CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E122CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E122CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E122CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E122CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iQgoFVKp2is26QxIQeOxKrBCMyaNOW_z4YuWSulUrX5g8W9d358fi28xynPADt4NNrTkgoH7TWxgQI0B2kr0oCmI62BtK2p2C3gFzCVYJwPmb70K6kpWTFoNLU656WI6EMPGE-qrSpTWkgKynZKjWDNAd1e68iVC5nWqQrG79MNqUXPaBu4IdtvNBMbGeeENSBrNqJgC7ICpjYSdau0UnYfVSSl5VqKE0NKNSnvjpJtdB3qRqO4PGyBvnhxieRIGWmaOeSIVJXHtyinjDlnnj0Pw1BvRM3vwDkzjMtLb_oUvrtXPTlmtdVTznit0tbcfsmrGBFHoD8Lpv77A9CazQLLfw60jsCxZwem8QIInB15YejZnn3g-b4hx8kGp1OVjsuB2LSrdU2qDQrMYGya_nKxTCBZJ-5DW0OyJCT6EeO4NafGOG5zMOTW5-tz1KeRSsf450BSI6M1pILyEi0-H9UD2u3R34NbBe056lsSHMcZLB8WQZk9dSd2DE639k9-vn7-KJkkH91PbmIaptVbkM2sTM4Zsf82IrqYIFWHVN3bvbgJosQyjD92yBDJ8K2OPGv2P5jyKv7q6sPjU7vz_ojoArnLazmHlEGMH0_fF9ZxAXVBaIadPe7fCvnSZJCTlgnc6Zi0gke7MsVO_zvjtsqIgDkl8o6KQex-A2u-b8I=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E122FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E122FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E122FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E122FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E122FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E122FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E122FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E122FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRDaiVIQKuUTtFYt0mjQg4ciVWDEZg1acp_nw1ZslZKpWrzB4t77_z4_Fp4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DL2AqwTjvM13pN1JRsmRQa2p1xgsR0qcOMByVG1WmtIDklG2VGsKKA7q70ZErFzKtVRWMPyZrUomO0dRwSzbfaSrWMs4Iq0HWrEXO5mQJTG0kqkZphew-LElCi5UUR4aUKlI8HCXbaFvUDgZRcdgCffWiAsmRMFLXM8gQKUuPb1BGGXPOPHsWBIFei4o_gHNmGJeX3ngffnhUPTlmudETznil0tbMfs0rGRFH4HTij6cfD0BrMvGt6UugdQQOPds3jVdA4OzICwLP9uwDbzo15DjZ4His0lHRE-tmuapIuUa-6Q9NM1jMFzHEq9h9aiqIF4SEPyMcNebYGEZNBobc-nx1jro0UukI3_ckNVJaQSIoL9D8y1E9oN0O_cO_U9COo74lwXGc3vJ-ERTpvjuxZXC6tX_y8-3zh_Eo_uR-dmPTMK3OgnRipXJOif23EeHFCKk6pOre78WtH8aWYfyxQ4ZIhu915EWz_8GUN_FXV9fP-3Zn3RHRBXIXN3IOKIMIP5--L6zjHKqc0BQ7O9y9FfKlSSEjDRO41TFpBA-3RYKd7nfGTZkSATNK5B3lvdj-Bo7jb9o=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**RICEFW Status Summary** — E2E Tower (0 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| **Total** | **0** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| **Total** | **0** |

### 6.3 NFRs & Design Principles

| Category | Requirement | Target / SLA | Priority |
|----------|-------------|-------------|----------|
| Performance | Order/transaction processing within interactive SLA | < 3 seconds for online transactions | High |
| Availability | Business-critical systems available during extended hours | 99.9% (06:00-22:00 all time zones) | High |
| Scalability | Support seasonal and promotional volume spikes | Handle 2x baseline transaction volume | Medium |
| Recoverability | Customer-facing systems recover within business impact window | RPO < 30 min, RTO < 2 hours | High |
| Data Volume | Support transactional data growth from business expansion | 10M+ documents/year | Medium |
| Latency | Near-real-time integration for order status updates | < 30 seconds for status propagation | Medium |
| Concurrency | Support global user base across business functions | 300+ concurrent users | Medium |

### 6.4 Security & Governance

| Concern | Approach | Standard / Policy | Owner |
|---------|----------|--------------------|-------|
| Authentication | Single Sign-On (SSO) via Intel corporate Azure AD identity | Intel IT Security Policy - Identity Management | IT Security |
| Authorization | Role-based access control (RBAC) with SAP authorization objects | Intel SAP Security Standards - Role Design | SAP Security Team |
| Data Classification | All financial/operational data classified per Intel Data Classification Standard | Intel Data Classification Policy | Data Governance |
| Data Encryption (at rest) | AES-256 encryption for SAP HANA database and file storage | Intel Encryption Standard | Infrastructure Security |
| Data Encryption (in transit) | TLS 1.3 for all system-to-system and user-to-system communication | Intel Network Security Policy | Network Engineering |
| Network Segmentation | SAP systems in dedicated network zones with firewall controls | Intel Network Architecture Standard | Network Security |
| API Security | OAuth 2.0 / certificate-based authentication for all API integrations | Intel API Security Guidelines | Integration Architecture |
| Audit Logging | Comprehensive audit trail for all data changes and user actions (SAP Security Audit Log) | SOX Compliance / Intel Audit Policy | Internal Audit |
| Certificate Management | Automated certificate lifecycle management for system-to-system trust | Intel PKI Standard | Certificate Authority Team |
| Compliance | SOX controls, export control (EAR/ITAR) screening, data privacy (GDPR) | Intel Corporate Compliance Framework | Compliance Office |

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-122 — E2E-122</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*No timeline data available for this capability.*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**RAID Summary:** 15 open items (0 capability-specific, 15 tower-level), 56 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 3 | 3 |
| P2 - Medium | 0 | 10 | 10 |
| P3 - Low | 0 | 2 | 2 |
| **Total** | **0** | **15** | **15** |

**Other E2E Tower RAID Items** (15 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03681 | Risk | P1 - High | ITC Execution: Planning run availability - Prerequisite for ... | In Progress | E2E | 2026-03-27 |
| 03762 | Risk | P1 - High | FTS-IF (esp SCP) related test cases/sequencing are not accur... | In Progress | FTS IF | 2026-04-03 |
| 01733 | Risk | P2 - Medium | Tariffs impacts Item/BOM design which is impacting ERP/SCP (... | In Progress | E2E | 2026-03-06 |
| 03592 | Risk | P2 - Medium | Lack of Defined IMO Owner for CBA Mask Billing and Materials... | In Progress | E2E | 2026-03-27 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03628 | Risk | P2 - Medium | R3 Returns Rework Process Causing Finance Double Counting in... | In Progress | E2E | 2026-03-27 |
| 03642 | Issue | P2 - Medium | E2E Process with Anafi on order/invoice point.  Need IFS SC ... | In Progress | E2E | 2026-03-24 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03753 | Risk | P2 - Medium | PDF-SMH IF test cases are not available in JIRA | To Be Reviewed | B-Apps | 2026-03-25 |
| 03756 | Risk | P2 - Medium | LE101-1001 Operation Support Ownership for SIMS/Tester Front... | In Progress | E2E | 2026-04-24 |
| 03769 | Action | P2 - Medium | Need a Labs SPOC owner to define IP Labs enterprise and mate... | In Progress | E2E | 2026-04-17 |
| 03216 | Action | P3 - Low | Mask Expense vs. Invoice | In Progress | E2E | 2026-03-06 |
| 03315 | Risk | P3 - Low | BPMG – SCP L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-03-27 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 1 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 1 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*E2E-122 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

