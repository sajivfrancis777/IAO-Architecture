<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-118 — E2E-118</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-118 · Forecast to Stock</p>
  <p style="font-size:14px; color:#888;">IAO Program · Release 2<br/>
  Generated: March 2026<br/>
  Sajiv Francis</p>
  <p style="font-size:12px; color:#aaa;">IAO Architecture Pipeline — Intel Confidential</p>
</div>

<style>
@media print {
  @page { margin: 0.75in; }
  .mermaid { page-break-inside: avoid; overflow: hidden; }
  pre, table { page-break-inside: avoid; }
  h2, h3, h4 { page-break-after: avoid; }
}
.mermaid { overflow-x: auto; overflow-y: auto; }
.mermaid svg { height: auto !important; }
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-118 E2E-118** within the IAO program. It includes 5 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Forecast to Stock |
| **Capability** | E2E-118 - E2E-118 |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Forecast to Stock |
| **L2 Capability** | E2E-118 - E2E-118 |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-118 Process Migration | Migrate E2E-118 business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-118 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **5 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-118 E2E-118.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E_118F__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_CMMS | E2E_118F__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_CMMS | Boundary Apps
, SAP S/4 Intel Foundry 
(Receiving Company)
B
, SAP S/4 Intel Foundry 
(Sending Company)
A
 | 19 | 3 |
| 2 | E2E_118G__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_CMM | E2E_118G__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_CMM | Boundary Apps
, SAP S/4 Intel Foundry 
(Receiving Site)
B
, SAP S/4 Intel Foundry 
(Sending Site)
A
 | 19 | 3 |
| 3 | E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART | E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART | Boundary Apps
, SAP S/4 Intel Foundry 
(Receiving Company
B
, SAP S/4 Intel Foundry 
(Sending Company)
A
, UI | 20 | 4 |
| 4 | E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST | E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST | Boundary Apps
, SAP S/4 Intel Foundry 
(Receiving Site)
B
, SAP S/4 Intel Foundry 
(Sending Site)
A
, UI | 20 | 4 |
| 5 | Slide_13_-_Detail-out_on_TM_Embedded_Steps | Slide_13_-_Detail-out_on_TM_Embedded_Steps | Boundary Apps, External Partners/ B2B
, SAP S/4 (Intel Foundry)
 | 19 | 13 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E_118F__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_CMMS — E2E_118F__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_CMMS

**Swim Lanes**: Boundary Apps
 · SAP S/4 Intel Foundry 
(Receiving Company)
B
 · SAP S/4 Intel Foundry 
(Sending Company)
A
 | **Tasks**: 19 | **Gateways**: 3

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial, sans-serif','primaryColor': '#e8f0fe', 'primaryBorderColor': '#0071c5','lineColor': '#37474F', 'secondaryColor': '#f5f8fc'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'curve': 'basis', 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps 
        n1["Initiate iSTART Approval Process (Factory Team)​"]
        n2["Send CMMS (Asset Transfer)"]
        n3["Initiate Asset Transfer Process"]
        n17["fa:fa-user Return EQ on WO – Return Reason Code Transfer in UI Determine Final Asset or..."]
        n20(["fa:fa-play Initiate Asset Transfer Request"])
        n21(["fa:fa-play startEvent"])
        n22(["fa:fa-stop endEvent"])
    end
    subgraph SAP S/4 Intel Foundry  (Receiving Company) B 
        n15["Acquire Asset in Receiving Company"]
        n16["Update maintenance plant and location after transfer completed in Equipment..."]
        n23(["fa:fa-stop Asset Received at Receiving Company Code"])
    end
    subgraph SAP S/4 Intel Foundry  (Sending Company) A 
        n4["Initiate Inter-Company Asset Transfer"]
        n5["Update Transfer Details and Shipment Flag"]
        n6["Validate Transfer"]
        n7["Request Submitted for Approval"]
        n8["Update ISM Number in request line of AMT Table"]
        n9["TM Embedded"]
        n10["Generate Shipping/ Commercial Docs"]
        n11["Post Goods Issue Against ISM Delivery Doc"]
        n12["Approve Asset Transfer Request"]
        n13["Post Financial Entry (Via Batch Job)"]
        n14["Retire Asset in Sending Company"]
        n18["fa:fa-user Approve via My Inbox App"]
        n19["fa:fa-user Generate ISM Number (ZISM Delivery Doc)"]
        n24["Detail-out on TM Embedded Steps"]
        n25{{"fa:fa-code-branch Shipment Flag?"}}
        n26{{"fa:fa-arrows-alt parallelGateway"}}
        n27{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n4 --> n5
    n5 --> n6
    n6 --> n7
    n26 --> n8
    n26 --> n9
    n9 --> n24
    n8 --> n10
    n10 --> n11
    n11 --> n27
    n27 --> n12
    n26 --> n27
    n12 --> n13
    n13 --> n14
    n14 --> n15
    n3 --> n2
    n20 --> n1
    n15 --> n16
    n16 --> n23
    n1 --> n22
    n21 --> n3
    n25 -->|"No"| n27
    n7 --> n18
    n18 --> n25
    n25 -->|"Yes"| n19
    n19 --> n26
    n2 --> n17
    n17 --> n4
    class n17 userTask
    class n18 userTask
    class n19 userTask
    class n20 startEvt
    class n21 startEvt
    class n22 endEvt
    class n23 endEvt
    class n24 startEvt
    class n25 gateway
    class n26 gateway
    class n27 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11v2zYU_SuEisAJYLeSLFmOHzb4S0WGuutit8U274GWqZgoLaoklY-l_u-7lEjZUuI9bH4IwuN77rn38JKSn52Eb4kzci4unmlG1Qg9d9SO7ElnhDobLEmniyrgCxYUbxiRHR2T8kwt6d9lmBfkjzpMYzHeU_ak0SW54wR9vumiMRBZF0mcyZ4kgqadbicXdI_F05QzLnT0GzJM3bRUM19NuNgScQxw3chLQqAympEj3I-CKIg1T5KEZ9tG0jRMh2nSOejiGH9IdliosvxCkgV-_Eq3agfrFDNJIGan9uwD3hCme1Si0FhSiHtrBpVaJwPDljlOaHYHeOACJHD27QiF7uGADhcX66wWRR9u1xmCT8KwlDOSIqkAnt8rlFLGRm-C6TgO3a5Ugn8jozf-PJr1_W6iOxlB625Xm9t7IPRup0YbzrYmtPegexj5-WNXPI58tyue4G9Li2Tbo9J04A_9Ya00ibypN7VKaZr-LyXwVayw_Ga05v3Yj2e1lhcOwqn7Mp9tcxZEY6_tExH3NCEnSeM47s-PVs0HoeeeTzqJ-wN32kp6hxV5wE_HhNfToE4Yh1HsRWcTVnrtKovNJ8ETm7A_D-OwThhNvHjsn00YjL1gaCqEPHcC5zs04UU5y2ic5xJVX-pP5v25dm7goFJoAdHlany70jGC32OGdA1ESnQZ40RxYK8I3l-tC991N2vnr5M0PqRZwlyg6WKxRJdjKYlCK5hjmRJx1Yztn0o2I61ik-BFwEjxKMU9PRDolqhCZGj-G-IZ-vor0gV5fQvfEiwBn8KxOualGVwdaEYUEXs47yimGfRXiXPx9u3bVjvuZS2ZM9jZc_Xeku8FkQrYV6d0r0U3p5NkLyL9Y6RUPK_OViMOkNZmLsef0PJdAEUpwlCstxb2Bl3ekoTQe7g0oPl9jrOnKzRp7HUIWuPke0GFbYRqv1qslvkDIH3Ot7r5PaYgmeEsIQj6yhTCsOWMJ1hRsBynYC9cdMabBNIxcHyrVeagmu-hsZde91sWVJVVZQEZq5cllrv7XyzSM9owaHxqUHA6mZoqelawue_NDsKjQ_VgwKhhymRp0HJXtY5ihu-aVG3uF8xog9wM0cNvxgwti82eKm1pykV9Tpvxw2M1N8sF-ljsN9UBECaJfuAhnqLxYoVW-hHc5F8Df7VAc6Btt2TbmgYXvn1PMiJ0ft1YDna-037uiUjgwYxmPGmfX33JfOIg_Z7zrUQ3UhYwgHcwTYDpImeEwV7DDgG5xdU3S9Xovxy-U0LfiukznpUlzTMFuS-_UIwmWCU79AvftC4lLyhtVo2j0ZqWFmPYvJVskfegstA3xoY_arDFum6yai9P9uryj7YnrWJ9XWw1YT1eKH0NnuwYWiqSt7bAD5-fra5-Q-ttwEQwojGaP6-dw-GUNDiSsBD8QfYwUyjHAjNG2PvqqdcmRa-SaJawQkJDL1j14c0C1Ov9BMfJLMNqOTDLQbWMzNI362FrfW3W19XSD8x6WK0986iFfwzgWcAzjFohMhF-S6KO8HwT0bdA3wBW1TM9ebYpE1CntFXYeNO0Z7v2rGYtYdZ1BgPY7_0yw4-185GvnR8nxdpurGGeccQP28zfiSypnvXSs2baqmzftREmeXDyHlOi9gWuiQ_P4Nev42CSfb1t4t4Z3DevqE20_yoanMkR2re6Jjx4HY4s7HQduAjhQbl1Rs9O-UsHfg1tSYoLppxD18GF4sunLHFG5S8Cpyiv6hnF8ODaV-DhH_DwFNI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E_118G__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_CMM — E2E_118G__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_CMM

**Swim Lanes**: Boundary Apps
 · SAP S/4 Intel Foundry 
(Receiving Site)
B
 · SAP S/4 Intel Foundry 
(Sending Site)
A
 | **Tasks**: 19 | **Gateways**: 3

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial, sans-serif','primaryColor': '#e8f0fe', 'primaryBorderColor': '#0071c5','lineColor': '#37474F', 'secondaryColor': '#f5f8fc'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'curve': 'basis', 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps 
        n1["Initiate iSTART Approval Process (Factory Team)​"]
        n2["Send CMMS (Asset Transfer)"]
        n3["Initiate Asset Transfer Process"]
        n17["fa:fa-user Return EQ on WO – Return Reason Code Transfer in UI Determine Final Asset or..."]
        n20(["fa:fa-play Initiate Asset Transfer Request"])
        n21(["fa:fa-play startEvent"])
        n22(["fa:fa-stop endEvent"])
    end
    subgraph SAP S/4 Intel Foundry  (Receiving Site) B 
        n15["Asset Acquired in Receiving Site"]
        n16["Update maintenance plant and location after transfer completed in Equipment..."]
        n23(["fa:fa-stop Asset Received at Receiving Company Code"])
    end
    subgraph SAP S/4 Intel Foundry  (Sending Site) A 
        n4["Initiate Intra-Company Asset Transfer"]
        n5["Update Transfer Details and Shipment Flag"]
        n6["Validate Transfer"]
        n7["Request Submitted for Approval"]
        n8["Update ISM Number in request line of AMT Table"]
        n9["TM Embedded"]
        n10["Generate Shipping/ Commercial Docs"]
        n11["Post Goods Issue Against ISM Delivery Doc"]
        n12["Approve Asset Transfer Request"]
        n13["Post Financial Entry (Via Batch Job)"]
        n14["Asset Retired in Sending Site"]
        n18["fa:fa-user Approve via My Inbox App"]
        n19["fa:fa-user Generate ISM Number (ZISM Delivery Doc)"]
        n24["Detail-out on TM Embedded Steps"]
        n25{{"fa:fa-code-branch Shipment Flag?"}}
        n26{{"fa:fa-arrows-alt parallelGateway"}}
        n27{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n4 --> n5
    n5 --> n6
    n6 --> n7
    n26 --> n8
    n26 --> n9
    n8 --> n10
    n10 --> n11
    n11 --> n27
    n27 --> n12
    n26 --> n27
    n12 --> n13
    n13 --> n14
    n14 --> n15
    n3 --> n2
    n20 --> n1
    n15 --> n16
    n16 --> n23
    n1 --> n22
    n21 --> n3
    n25 -->|"No"| n27
    n9 --> n24
    n2 --> n17
    n17 --> n4
    n7 --> n18
    n18 --> n25
    n25 -->|"Yes"| n19
    n19 --> n26
    class n17 userTask
    class n18 userTask
    class n19 userTask
    class n20 startEvt
    class n21 startEvt
    class n22 endEvt
    class n23 endEvt
    class n24 startEvt
    class n25 gateway
    class n26 gateway
    class n27 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11zozYU_SsadjJOZuxdwGAcP7TjL3bSWW-3wbs7bd0HGYStWYxYSSRxs_7vvQKEgcR9aP2QiQ733HO_JMGzEbKIGBPj6uqZplRO0HNP7smB9Caot8WC9PqoBL5gTvE2IaKnbGKWyoD-XZhZTvakzBTm4wNNjgoNyI4R9Pmuj6ZATPpI4FQMBOE07vV7GacHzI9zljCurN-QcWzGhVr1aMZ4RPjZwDQ9K3SBmtCUnOGh53iOr3iChCyNWk5jNx7HYe-kgkvYY7jHXBbh54Ks8NNXGsk9rGOcCAI2e3lIPuAtSVSOkucKC3P-oItBhdJJoWBBhkOa7gB3TIA4Tr-dIdc8ndDp6mqT1qLow_0mRfALEyzEgsRISICXDxLFNEkmb5z51HfNvpCcfSOTN_bSWwztfqgymUDqZl8Vd_BI6G4vJ1uWRJXp4FHlMLGzpz5_mthmnx_hb0eLpNFZaT6yx_a4Vpp51tyaa6U4jv-XEtSVr7H4Vmkth77tL2otyx25c_OlP53mwvGmVrdOhD_QkDSc-r4_XJ5LtRy5lnnZ6cwfjsx5x-kOS_KIj2eHt3Ondui7nm95Fx2Wet0o8-0nzkLtcLh0fbd26M0sf2pfdOhMLWdcRQh-dhxnezRjeTHLaJplApUP1S-1_twYd7BRKaSAaLCe3q-VDWcPOEEqBiIEuvZxKBmw1wQfbja5bZrbjfFXw40NbgKYCzRfrQJ0PRWCSLSGORYx4Tdt22FTsm2pFdsEywNGjCcxHqiBQPdE5jxFy98QS9HXX5EKyBpq-J5gAfgcttXZL03h6EALIgk_wH5HPk0hv1Kc8bdv33bSMa9rySyBzl6K9558z4mQwL5p0q0OvdqdJH1haZ8thWRZubdadoB0mhlMP6HgnQNBSZIgX7UWeoOu70lI6AMcGiigktygWavRLgiV0U_D7znlJFJVaXM6dR8B5XMWqbwPmIJaitOQIEgplQhDtxMWYkmh2jiGysIZV5UlZIcsgWIXEktQyw6Q08syDzvZl_GVMQEZy0Z8c_CJ02PR2P9SHTWe59pMm7VxmhMJPI4HWq3d73b47rk89UDAiGGaiKI6wb7MG_kJ3rWpqrJfcEJb5LaJGvpqvFCQbw9UqnrGjNf7s20_PkdzF6zQx_ywLQefV07URYdYjKarNVqrq7fNvwX-eoWWQIsiEnVGwYSn70lKuPKvEsuglu9UUw6Eh3AhowULu_tWHS6fGEi_ZywS6E6IHHbQDkYJMBXkgiTQaGgPkDtcdaKUif7LpmsShlpM7e20CGkJrTyi6y8UoxmW4R79wradw8hy6m0B54feFc1Z6diP22eRDvEBNFbqnNiyJwV2WLdtVl3JRqeu_-hWpBOqrUIt52vAcqkOv0a_UCBJ1mmA7T4_a131XjbYQgmhDK3B_HljnE5N0uhMwpyzRzHAiUQZ5jhJSPK-vOu6JO9VEk3DJBeQ0AtWvW9TBw0GP8FmqpZuuRxVy1G59KqlXa3HnfVttR6XS6u6UOGfCrA0YJWAXXv0Kgu747K2sOzKYqiBYQU4GqhysHQSlUHtUkeh7askLZ2lpTVriWpde6gA_dwuPPzYGB_ZxvjRCPa2IurQdOx1MlW6-rnOXhfUqipou12l34kopCxda0trjRpvL4WCfm1r4-ML-O3rOBRNv9S2cesCblcvpm10-CrqXPDh6ne5Njx6HfY0bPQNOAbhjoyMybNRfN_AN1BEYpwn0jj1DZxLFhzT0JgU3wFGXhzUC4rhzjqU4OkfXmEQjg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART — E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART

**Swim Lanes**: Boundary Apps
 · SAP S/4 Intel Foundry 
(Receiving Company
B
 · SAP S/4 Intel Foundry 
(Sending Company)
A
 · UI | **Tasks**: 20 | **Gateways**: 4

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial, sans-serif','primaryColor': '#e8f0fe', 'primaryBorderColor': '#0071c5','lineColor': '#37474F', 'secondaryColor': '#f5f8fc'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'curve': 'basis', 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps 
        n1["iSTART sends an email notification to the requestor, instructing them to..."]
        n2["iSTART sends an email notification to the requestor, instructing them..."]
        n16["fa:fa-user Initiate iSTART Approval Process (Factory Team)​\"]
        n23{{"fa:fa-code-branch Approval"}}
    end
    subgraph SAP S/4 Intel Foundry  (Receiving Company B 
        n13["Asset Acquired in Receiving Company"]
        n14["Update maintenance plant and location after transfer completed in Equipment..."]
        n21(["fa:fa-stop Asset Received at Receiving Company Code"])
    end
    subgraph SAP S/4 Intel Foundry  (Sending Company) A 
        n3["Update Transfer Details and Shipment Flag"]
        n4["Validate Transfer"]
        n5["Request Submitted for Approval"]
        n6["Update ISM Number in request line of AMT Table"]
        n7["TM Embedded"]
        n8["Generate Shipping/ Commercial Docs"]
        n9["Post Goods Issue Against ISM Delivery Doc"]
        n10["Approve Asset Transfer Request"]
        n11["Post Financial Entry (Via Batch Job)"]
        n12["Asset Retired in Sending Company"]
        n17["fa:fa-user Approve via My Inbox App"]
        n18["fa:fa-user Generate ISM Number (ZISM Delivery Doc)"]
        n19["fa:fa-user Initiate Intra-Company Asset Transfer"]
        n22["Detail-out on TM Embedded Steps"]
        n24{{"fa:fa-code-branch Shipment Flag?"}}
        n25{{"fa:fa-arrows-alt parallelGateway"}}
        n26{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph UI
        n15["Trigger iSTART process"]
        n20["fa:fa-user Initiate Work Order"]
    end
    n3 --> n4
    n4 --> n5
    n25 --> n6
    n25 --> n7
    n6 --> n8
    n8 --> n9
    n9 --> n26
    n26 --> n10
    n25 --> n26
    n10 --> n11
    n11 --> n12
    n12 --> n13
    n13 --> n14
    n14 --> n21
    n24 -->|"No"| n26
    n7 --> n22
    n5 --> n17
    n17 --> n24
    n24 -->|"Yes"| n18
    n18 --> n25
    n15 --> n16
    n16 --> n23
    n23 --> n1
    n23 --> n2
    n20 --> n15
    n3 -->|"Manual Update"| n20
    n6 --> n20
    n20 -->|"Interface"| n19
    n19 --> n3
    class n16 userTask
    class n17 userTask
    class n18 userTask
    class n19 userTask
    class n20 userTask
    class n21 endEvt
    class n22 startEvt
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtV99z4jYQ_lc0vsmQzMDVMjYQHtrhl2_SuVxvAnc3bemDsGXQRFg-SU5Cc_zvXWHLYBMeOi0PCVrvfrvftyvJvDqRiKkzdK6uXlnK9BC9tvSGbmlriForomirjQrDVyIZWXGqWsYnEames78PbtjPXoybsYVky_jOWOd0LSj6ctdGIwjkbaRIqjqKSpa02q1Msi2Ru4ngQhrvd3SQuMkhW_loLGRM5dHBdfs4CiCUs5Qezd2-3_dDE6doJNK4BpoEySCJWntTHBfP0YZIfSg_V_SevHxjsd7AOiFcUfDZ6C3_SFaUG45a5sYW5fLJisGUyZOCYPOMRCxdg913wSRJ-ng0Be5-j_ZXV8u0Soo-PixTBJ-IE6WmNEFKg3n2pFHCOB--8yejMHDbSkvxSIfvvFl_2vXakWEyBOpu24jbeaZsvdHDleBx6dp5NhyGXvbSli9Dz23LHfxt5KJpfMw06XkDb1BlGvfxBE9spiRJ_lMm0FUuiHosc826oRdOq1w46AUT9xzP0pz6_RFu6kTlE4voCWgYht3ZUapZL8DuZdBx2O25kwbommj6THZHwNuJXwGGQT_E_YuARb5mlfnqsxSRBezOgjCoAPtjHI68i4D-CPuDskLAWUuSbdBY5IdZRqMsU6h4aD4p_nPpsPli9LAAadJYIZIiuiWMo1RolrCIaCZSpAWCXYsk_Z5TpYVsI5ZCAXmkYUbNoy24vH__fun8dQLu_V_gZ8i4B9AJGSakY2YE3cFZw6ALqEwHNKV4IhwZGalS6DokEUDv0IKS7c0y91x3tVw2yu2-vlpUc4x1VrARo00FtnT2-8IdyDQEno8-o_lPPhSiKUehkRuSoesHGlH2ZHhMxDYj6Q6Na_J3gcdIKarRKPqeM0ljII_OohrsfYj6ksWGMMgJKVMolKKMk1SDyDHiotSWJBrk0UBEJfAlAjhOdZFlBgmzLU31eePwdaUvdCRDRYlFWRBM9HmJ8D-mAHPzbyWag-sJzg0anSrUPVJdWBZTqmGI1IHpfFNwQCEn6zoLo9JXwlktuO4SgMtDMXdonq-2TBttEiFPmn7q3ztWcze_R5_y7QrqAS3L4UXmNkEiQaP7BVqY-60e34f4xT2aQVgc07j-cAAPP9CUSgNveGUgy09Gly2VEVx6aCoiVY-5hZjPAhJ_EAI22J1SOUWjNTE76FDilHJoGQgNsY0pcs3sHWjSssGVwqUmjQBsk4XMDJypaJZqwL7-yggaEw2b5VexummEedWMP1BtR7zR9UZIv769bZVPkOZ-BxO0Ei_G2Iga1KMqLU9adf1HU5RmtbcXThYYW0k6dtjrejV2jyFczGhH5BrBNjzpOZprmjW66Plvnzy14f7leP4UQcExiEgpnlWHcI0yIgnnlH8oLqVmUO_NIJZGPFegyVnU-T7-cncql9lBC8nWa7MPisM3K87cBkX3gq7fhHxEv5mXsyqgypl2UafzM-zkcukXy6BcekGx7jXW_XLdK5aDcjkolrfl8rZYelV06Y7dBlzlgd3SA1sDLg2eNXiloWsNJQNsKeCSg2cxvIPhx9L5JJbOj5Ns_dLRYpfVYMsOWwe_ifQ7VQcobJnjkrpnlcMWrKJWkvds4Z4tvLG21XhWi-C0VZD8nqQ5HAzFKVkwcuv9qNYFBsSYK0EmJCr8se0QLlvUPXk9OpRq3wvr9v4F--CC_fZtO1T1th2Xb751q1e9e9ftXftaWDf7b5uDt809a3baDlwCcNnHzvDVOfyCgl9ZMU1IzrWzbzsk12K-SyNnePil4eQH_aeMwKbdFsb9P12CNRc=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST — E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST

**Swim Lanes**: Boundary Apps
 · SAP S/4 Intel Foundry 
(Receiving Site)
B
 · SAP S/4 Intel Foundry 
(Sending Site)
A
 · UI | **Tasks**: 20 | **Gateways**: 4

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial, sans-serif','primaryColor': '#e8f0fe', 'primaryBorderColor': '#0071c5','lineColor': '#37474F', 'secondaryColor': '#f5f8fc'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'curve': 'basis', 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps 
        n1["iSTART sends an email notification to the requestor, instructing them to..."]
        n2["iSTART sends an email notification to the requestor, instructing them..."]
        n17["fa:fa-user Initiate iSTART Approval Process (Factory Team)​\"]
        n23{{"fa:fa-code-branch Approval"}}
    end
    subgraph SAP S/4 Intel Foundry  (Receiving Site) B 
        n14["Asset Acquired in Receiving Site"]
        n15["Update maintenance plant and location after transfer completed in Equipment..."]
        n21(["fa:fa-stop Asset Received at Receiving Company Code"])
    end
    subgraph SAP S/4 Intel Foundry  (Sending Site) A 
        n3["Update Transfer Details and Shipment Flag"]
        n4["Validate Transfer"]
        n5["Request Submitted for Approval"]
        n6["Update ISM Number in request line of AMT Table"]
        n7["TM Embedded"]
        n8["Generate Shipping/ Commercial Docs"]
        n9["Post Goods Issue Against ISM Delivery Doc"]
        n10["Approve Asset Transfer Request"]
        n11["Post Financial Entry (Via Batch Job)"]
        n12["Asset Retired in Sending Site"]
        n13["Initiate Intra-Company Asset Transfer"]
        n18["fa:fa-user Approve via My Inbox App"]
        n19["fa:fa-user Generate ISM Number (ZISM Delivery Doc)"]
        n22["Detail-out on TM Embedded Steps"]
        n24{{"fa:fa-code-branch Shipment Flag?"}}
        n25{{"fa:fa-arrows-alt parallelGateway"}}
        n26{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph UI
        n16["Trigger iSTART process"]
        n20["fa:fa-user Initiate UI Work Order"]
    end
    n3 --> n4
    n4 --> n5
    n25 --> n6
    n25 --> n7
    n6 --> n8
    n8 --> n9
    n9 --> n26
    n26 --> n10
    n25 --> n26
    n10 --> n11
    n11 --> n12
    n12 --> n14
    n14 --> n15
    n15 --> n21
    n24 -->|"No"| n26
    n7 --> n22
    n5 --> n18
    n18 --> n24
    n24 -->|"Yes"| n19
    n19 --> n25
    n16 --> n17
    n17 --> n23
    n23 --> n1
    n23 --> n2
    n20 --> n16
    n3 -->|"Manual Update"| n20
    n6 --> n20
    n20 -->|"Interface"| n13
    n13 --> n3
    class n17 userTask
    class n18 userTask
    class n19 userTask
    class n20 userTask
    class n21 endEvt
    class n22 startEvt
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtV99z4jYQ_lc0vsmQzEDOMjYQHtrhl29yc7neBJKbtvRB2DJoIiyfJCehOf73rrBlsJM8dFoeErTe_Xa_b1eSeXEiEVNn6JydvbCU6SF6aekN3dLWELVWRNFWGxWGeyIZWXGqWsYnEames78PbtjPno2bsYVky_jOWOd0LSi6u26jEQTyNlIkVR1FJUta7VYm2ZbI3URwIY33BzpI3OSQrXw0FjKm8ujgun0cBRDKWUqP5m7f7_uhiVM0EmlcA02CZJBErb0pjounaEOkPpSfK3pDnr-zWG9gnRCuKPhs9JZ_ISvKDUctc2OLcvloxWDK5ElBsHlGIpauwe67YJIkfTiaAne_R_uzs2VaJUVfbpcpgk_EiVJTmiClwTx71ChhnA8_-JNRGLhtpaV4oMMP3qw_7XrtyDAZAnW3bcTtPFG23ujhSvC4dO08GQ5DL3tuy-eh57blDv42ctE0Pmaa9LyBN6gyjft4gic2U5Ik_ykT6CoXRD2UuWbd0AunVS4c9IKJ-xrP0pz6_RFu6kTlI4voCWgYht3ZUapZL8Du-6DjsNtzJw3QNdH0ieyOgFcTvwIMg36I--8CFvmaVearb1JEFrA7C8KgAuyPcTjy3gX0R9gflBUCzlqSbIPGIj_MMhplmULFQ_NJ8Z9Lh80Xo9sFSJPGCpEU0S1hHKVCs4RFRDORIi0Q7Fok6Y-cKi1kG7EUCsgjDTNqHm3B5fLycun8dQLu_V_gr5BxH6ATMkxIx8wIuoazhkEXUJkOaErxSDgyMlKl0HlIIoDeoQUl24tl7rnuarlslNt9ebGo5hjrrGAjRpsKbOns94U7kGkIPB99Q_OPPhSiKUehkRuSofNbGlH2aHjMmaYXaFwT3wcWI6WoRqPoR84kjYE6qsc0iAcQcpfFhisoCdlSqJGijJNUg74x4qKUlSQalNHAQSXwJRLbjFNdpJhBtmxLU_26Z_i8khaakaGivqImCCb6pL4JYJJ0B_9jU-fFv1VnDq5HbUan2nSPPBeWwpRqGB51oDnfFARQyMm6TsGoek84qwXXXYyKt8W8oXm-2jJthEmEPGn2qX_vWM31_AZ9zbcrqAeELIcWmVsEiQSNbhZoYe61erwZ18UNmkFYHNO4_nAADz_RlEoDb3hloMlHI-6WygguOzQVkarHXEHMNwGJPwkBG-taqZyi0ZqYnXMocUo59AtUhtjGCLlm6g40adndSuFSk0YAtslCZqbNVDRLNWCf3zOCxkTDJvksVheNMK-a7luq7XCftrzhb1pebWQYFUk6dsDqZTbiBvWzwFJ7hNpudgC0Es_G2Ii6qkdVDTjp7_kfTSUbFD1DsZjKjsg1gl130mU01zRr9M3z3z5jauP86_GkKYKCYxCRUjypDuEaZUQSzin_VFw_zaDem0EsjXiugNCrqNfb9u76VDCzBxaSrddm8otjNitO1wZF952z-e4afRfyAf1m3sSqmCpt2kWdzi-wfculXyyDcukFxbrXWPfLda9YDsrloFhelcurYulV0aU7dhtwlQd2Sw9sDbg0eNbglQZbMS5LxrZmbEEthnfw-Ll0voql8_MkW790tNhlILZ0cMnH85tIv1N1gMKWKrZcqyosVysVttm6FqyUHjfWthrPatE7bRUkvyFpDqdBcTQWjNx6P6p1gfHTbHG4lxISFf7Y1oDLnN2Td6FDqfYlsG4fvGO_etsO2d-24_J1tm71qhfqur1r3_XqZv9tc_C2uWfNTtuBEx6u8dgZvjiHn0Xw0ymmCcm5dvZth-RazHdp5AwPPx-c_KDzlBHYn9vCuP8H_mYlWw==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 Slide_13_-_Detail-out_on_TM_Embedded_Steps — Slide_13_-_Detail-out_on_TM_Embedded_Steps

**Swim Lanes**: Boundary Apps · External Partners/ B2B
 · SAP S/4 (Intel Foundry)
 | **Tasks**: 19 | **Gateways**: 13

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial, sans-serif','primaryColor': '#e8f0fe', 'primaryBorderColor': '#0071c5','lineColor': '#37474F', 'secondaryColor': '#f5f8fc'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'curve': 'basis', 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps
        n15["CTSI Carrier Invoice Reconciliation/ Dispute Management"]
    end
    subgraph External Partners/ B2B 
        n16["Send to SAP B4NL"]
        n17["Notify carrier"]
        n18["Capture Execution events via BN4L-GTT"]
        n19["Receive Physical receipt at receiver company location"]
        n22(["fa:fa-play Data needs to be Sent to B4NL"])
        n36{{"fa:fa-arrows-alt parallelGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 (Intel Foundry) 
        n1["Create ZISM Outbound Delivery (S/4)"]
        n2["Create/Update Freight Unit and Freight Order"]
        n3["Perform Carrier Selection and Calculate Charges"]
        n4["Send Rates/Charges/Au to HAWB assignment: Freight forwarders (Within TM)"]
        n5["Ship (Goods Issue)"]
        n6["Execute Freight Order and Update Status Post GI"]
        n7["Create and Update Freight Settlement Document"]
        n8["Create Service PO/ Entry Sheet"]
        n9["Post Accrual to Freight Expense Account(s)"]
        n10["Allocate Freight Costs to Delivery Items (CO/PA) or Material Valuation"]
        n11["Pick and Pack Updates (IM)"]
        n12["Update Maintenance Plant and Location after Transfer Completed in Equipment..."]
        n13["Start tendering/Subcontracting Carrier Selection"]
        n14["Receive reconciled Carrier Invoice(s)"]
        n20(["fa:fa-play Rates/Charges need to be Sent"])
        n21(["fa:fa-play Initiate Tendering"])
        n23(["fa:fa-stop Accrual Posted and Freight Costs Allocated"])
        n24(["fa:fa-stop Asset Master Updated with Location"])
        n25["Intra-Company Asset Transfer using AMT and ISM Fiori Apps (Same Company Code)"]
        n26["Inter-Company Asset Transfer using AMT and ISM Fiori Apps"]
        n27{{"fa:fa-code-branch exclusiveGateway"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt parallelGateway"}}
        n31{{"fa:fa-arrows-alt parallelGateway"}}
        n32{{"fa:fa-arrows-alt parallelGateway"}}
        n33{{"fa:fa-arrows-alt parallelGateway"}}
        n34{{"fa:fa-arrows-alt parallelGateway"}}
        n35{{"fa:fa-arrows-alt parallelGateway"}}
        n39{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n2 --> n28
    n5 --> n34
    n22 --> n36
    n6 --> n31
    n31 --> n35
    n36 --> n16
    n28 --> n39
    n7 --> n8
    n8 --> n32
    n32 --> n9
    n32 --> n10
    n10 --> n33
    n9 --> n33
    n39 --> n3
    n17 --> n38
    n37 --> n18
    n34 --> n6
    n38 --> n19
    n33 --> n23
    n37 --> n39
    n35 --> n7
    n4 --> n29
    n20 --> n4
    n29 --> n39
    n1 --> n2
    n11 --> n5
    n16 --> n37
    n3 --> n11
    n31 --> n36
    n37 --> n17
    n38 --> n30
    n19 --> n12
    n12 --> n24
    n14 --> n35
    n13 --> n39
    n21 --> n13
    n28 --> n30
    n30 --> n15
    n26 --> n27
    n25 --> n27
    n27 --> n1
    n18 -->|"POD Receipt Events 
(via BN4L-GTT)"| n34
    n29 -->|"Freight forwarder Rates to CTSI"| n30
    n15 -->|"FO (Freight 
Order) & 
HAWB
(House 
Airway Bill) 
Mapping"| n14
    class n20 startEvt
    class n21 startEvt
    class n22 startEvt
    class n23 endEvt
    class n24 endEvt
    class n25 startEvt
    class n26 startEvt
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
    class n31 gateway
    class n32 gateway
    class n33 gateway
    class n34 gateway
    class n35 gateway
    class n36 gateway
    class n37 gateway
    class n38 gateway
    class n39 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWFtv4jgU_isWo9m2Egzkxu1hJQgwi9RO0aSzI-12H0xwwJrgZG2Hlu30v-9xYgdw6cOyfajik_N95-pjh5dGnK1IY9j4-PGFMiqH6OVKbsiWXA3R1RILctVEleB3zClepkRcKZ0kYzKi_5Rqjp8_KzUlm-EtTfdKGpF1RtC3eRONAJg2kcBMtAThNLlqXuWcbjHfh1macaX9gfSTTlJa06_GGV8RflDodHpOHAA0pYwcxF7P7_kzhRMkztjqhDQJkn4SX70q59LsKd5gLkv3C0Hu8PN3upIbWCc4FQR0NnKb3uIlSVWMkhdKFhd8Z5JBhbLDIGFRjmPK1iD3OyDimP04iILO6yt6_fjxkdVG0e3XR4bgL06xEBOSICFBPN1JlNA0HX7ww9Es6DSF5NkPMvzgTnsTz23GKpIhhN5pquS2nghdb-RwmaUrrdp6UjEM3fy5yZ-HbqfJ9_DfskXY6mAp7Lp9t19bGvec0AmNpSRJ_pclyCt_wOKHtjX1Zu5sUttygm4Qdt7ymTAnfm_k2HkifEdjckQ6m8286SFV027gdN4nHc-8bie0SNdYkie8PxAOQr8mnAW9mdN7l7CyZ3tZLBc8iw2hNw1mQU3YGzuzkfsuoT9y_L72EHjWHOcbNM6KspfRKM9F9U79MSf487ERPkRzFGLOKeFoznYZJAh9Ve0f05RiSTPWRhMq8kISdIcZXsP-ZfKx8VfFBP1gmZs-S8IZTtECupIRLtpo7I7RseEuGI4AiWSGotECjf0vtzVjpdIDlS-ZpMkexZV3lkJfOY9zWXACJklcKFcR2YFzAu0oRuMv_m3r88ODhRsADuIjdEfQYrMXNAZXuRLkEmFZPe4gGXG2zTHbozSLyzSc8rjuNRAleJjgVp5C_SdYYsQIWQkV1ZIgCFCqRx3czRHY6768GDAElz2JFk4lyjHHaUrSz1VLPTZeX49BvUtA_f8GeltOVZ-o7aPrOZMkRTPVTHx_c1JPVQpOgAv9MY_u0H0hl0oNTUiqUrlH18BwYyWwBrW_5SuFnfFyUKBvcHYgDHAjuFfT-xTtAXpBeJLxbd29EUlJXHaBAoc4jYtU8YYwNddEnBL4pgW_gopoa532qFAl-230fYxgO9I1U80-rD0Be09YeSPQ9XcqN5ShhzsrMLWrog3N0fXnLINumAtREEtHbYCqaclplKXrOh-RxLIQaJEJiT7PTwl6h5QfIQxVRKRMy32KJllcnGzYEt4_wKNqKKLFfRtNmYRiRRtCLH21aUo_RnHMC9gwkCRjbPqcEyaIegVFl9fCitXpAHiUltvo4GIIbOVOqXtkLskW0hretxejG5RxmDYwSOC4R7_jtDizBR3Vdwsa_yhTsMDwUOUBWOZ2VRzVbzpNd5hCLzPMVNgpZlW33ep9jnACdtEDHMQigYcQ5kBKJFkhqPb074LmKp-fPn2yDKiWjNRJjIAbSgkHeDsqljBJJcfQl2z9tlMtCv9oNnE9g8nKHs9vMux2rFl00tPlUDqaSdYsch0LPIftR1WaHkwYNsI7IITM8ropVIeAqeOtW5XZVH9lM_k2kxBEQn2EqkBVrRV6go1WV8dmULttrjLcCvW8rjjq8hVCZX5091D6pcbTjGaclochzCW8JcggQ7iN2antVvyEX8JvcR0NcHVTbi2BI94g8hynwLIj50e4279g7ruDSw6LziUg5xKQewnIuwTkXwIKLgGdTzll71W3PmuZi1qtX1Wl9Tqo1p5v3msFr6sFXb3WN1x40ILACLSGYxBuX2sMtKBXrY1J89o1BNrkwFo7-roKDxrhacHAWntGYADaomdMelrg1AK_EhifPe2UUzvh6UR5FkUdladT19Nrzeia9672us7swCLQiTRpcPTa5NUxmTcGtEfOm0p07Sh7VlRenUntg1MbNf1gvHR8q7yOZ7ntarOOZ9fbWPF05I7hcHUornHMDWyBcd1YLTl_wqF7P0Ff9ZV5Wt24H9n18aUbxujP4wYeaOSbi1R1VqnjSX2JVKg6MYFB3aNrg3xk5UXpBv0Cj-qiBpZ_y-BjEZYjytWn2Bi-nNQF9Q7neXl8_VQpPPrMKvvAfDWfyp135O47ck9_EZ9K_bPS4B2O7jvynvm4PBX3z4sHZ8VQ9rNi57zYPS_2zov98-LgvLh7Xnw-Su98lF4dZaPZ2BK-xXTVGL40yp-V4KenFUlwkcrGa7OBC5lFexY3huXPL42ivE5MKIbvmm0lfP0Xf9rFbQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps
 | E2E_118F__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_CMMS, E2E_118G__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_CMM, E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART, E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST,  | |
| SAP S/4 Intel Foundry 
(Receiving Company)
B
 | E2E_118F__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_CMMS,  | |
| SAP S/4 Intel Foundry 
(Sending Company)
A
 | E2E_118F__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_CMMS, E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART,  | |
| SAP S/4 Intel Foundry 
(Receiving Site)
B
 | E2E_118G__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_CMM, E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST,  | |
| SAP S/4 Intel Foundry 
(Sending Site)
A
 | E2E_118G__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_CMM, E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST,  | |
| SAP S/4 Intel Foundry 
(Receiving Company
B
 | E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART,  | |
| UI | E2E_118H__Inter-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_-_with_iSTART, E2E_118I__Intra-Company_Asset_Transfer_using_AMT_&amp;_ISM_Fiori_Apps_(Same_Company_Code)_-_with_iST,  | |
| Boundary Apps | Slide_13_-_Detail-out_on_TM_Embedded_Steps | |
| External Partners/ B2B
 | Slide_13_-_Detail-out_on_TM_Embedded_Steps | |
| SAP S/4 (Intel Foundry)
 | Slide_13_-_Detail-out_on_TM_Embedded_Steps | |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
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

    subgraph E2E118CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E118CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E118CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E118CDAA_e_g_XEUS -.-> E2E118CDAD_e_g_Azure_SQL
    end
    style E2E118CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E118CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E118CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E118CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E118CDAA_e_g_MES_300 -.-> E2E118CDAD_e_g_SAP_HANA
    end
    style E2E118CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E118CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E118CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlYFumzAQhl_F8hRlk5KOJCVpkVrJCWStRKuupNukMiEHjsSqAwjMmjTNu8-GhG5Z6KraEsLnu__O3yGzxn4cADZwo7FmERMGWjfFHBbQNFBzSjNotlAzAz9PmVjZ8Au42uBxXO4Urt9oyuiUQ9ZU0WEcCYc9FQIdPVkqN2Ub0wXjK2V1YBYDurtsISIDeXOjPHj86M9pKgqNPIMruvzOAjGX65DyDKTPXCy4TafAVSKR5soWyeqdhPosmkljT5emlEYPL6ZjfbNBm0bDjaoUaDJ0IySHz2mWmRAimiTDeIlCxrnxYaib4_G4lYk0fgDjg6YNBsP-dtl-VDUZ3WTZ8mMep2q7Z-r7esF0tOJbOaKbfTKo5LrWwOx1a-U6Q93qantyEPOX8sbjoT7UK73RSJOjVq_fV9tuVCpm-XSW0mSOrK7V6ZyMTDKyPfBmHnnKU_Ccr_a9i5GLf5buagQsBV-wOKqoqVHFkyL8h3XnyEg4mh0h9S4VDMMoqR4IMvdyfnSxmwcnvUA-A__YzUPQ5KmVWuGEpJOLPynNguyrdaD2Ufu8NlcZClGwBSJWHOpp7JATNSvklqbm38g7yfK_kB1y412Qa_I-xleW4_U0bYdZLpFcvol0lfgV0NIHKZ83cd7WchD1LtmbSO-c3wW6JjE6Ozt_3lIyC7LoMyI3l_I5Zhxc_PzK17HXQhtm8gT3f2DzAw2ZZEIQuR1dXE6s0eTu1kK29cW6Nmuaat--WG1PtZ8kCWc-VbuHG2h7Zk2zTCqoupcP98n2LClvRUE7Dts2C6GULy-Qgx0pT7jjr6tZ8T89Pf0HPm7hBaQLygJsrHFx_8u_RwAhzbnAmxamuYidVeRjo7iicZ4EVIDJqCS6KI2b39Pc-As=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E118FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E118FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E118FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E118FDAA_e_g_XEUS -.-> E2E118FDAD_e_g_Azure_SQL
    end
    style E2E118FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E118FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E118FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E118FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E118FDAA_e_g_MES_300 -.-> E2E118FDAD_e_g_SAP_HANA
    end
    style E2E118FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E118FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E118FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlYFumzAQhl_F8hRlk5KOJCVpkVrJCbBWolVX0m1SmZADR2LVAQRmTZrm3WdDQrcs6araEsLnu__O3yGzwkESAjZwo7FiMRMGWjXFDObQNFBzQnNotlAzh6DImFg68Au42uBJUu2Urt9oxuiEQ95U0VESC5c9lQIdPV0oN2Wz6ZzxpbK6ME0A3V22EJGBvLlWHjx5DGY0E6VGkcMVXXxnoZjJdUR5DtJnJubcoRPgKpHICmWLZfVuSgMWT6Wxp0tTRuOHF9Oxvl6jdaPhxXUKNB56MZIj4DTPTYgQTdNhskAR49z4MNRN27ZbuciSBzA-aNpgMOxvlu1HVZPRTRetIOFJprZ7pr6rF05GS76RI7rZJ4NarmsNzF73oFxnqFtdbUcOEv5Snm0P9aFe641GmhwH9fp9te3FlWJeTKYZTWfI6lqdzoltkpHjgz_1yVORge9-de49jDz8s3JXI2QZBIIlcU1NjTqelOE_rDtXRsLR9Aipd6lgGEZFdU-QuZPzo4e9IjzphfIZBsdeEYEmT63USicknTz8SWmWZF-tA7WP2ucHc1WhEIcbIGLJ4TCNLXKiZo3c0tT8G3knXfwXsktu_AtyTd7H-Mpy_Z6mbTHLJZLLN5GuE78CWvog5fMmzpta9qLeJnsT6a3zu0AfSIzOzs6fN5TMkiz6jMjNpXzajIOHn1_5OnZa6MBUnuD-D2xBqCGTjAkit6OLy7E1Gt_dWsixvljX5oGmOrcvVsdX7SdpyllA1e7-Bjq-eaBZJhVU3cv7--T4lpS34rCdRG2HRVDJVxfI3o5UJ9zy19Ws-Z-env4DH7fwHLI5ZSE2Vri8_-XfI4SIFlzgdQvTQiTuMg6wUV7RuEhDKsBkVBKdV8b1b1Ch-DU=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-118-R001 | Report | E2E-118 operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-118-C001 | Conversion | Legacy data migration for E2E-118 | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-118.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E118C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E118C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E118CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E118CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E118C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E118CMW_e_g_Azure_Service_Bus
    E2E118CMW_e_g_Azure_Service_Bus --> E2E118C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVWtv4jAQ_CtWKsQXaENbHo0qpISEE6fQVk0fdzpOkYk3YNUkUey0pZT_fnZCCa-qPSMFZT0768yO7YUWxAQ0Q6tUFjSiwkCLqpjCDKoGqo4xh2oNVTkEWUrF3IVnYGqCxXExk0MfcErxmAGvquwwjoRH33KCRit5VTAV6-MZZXMV9WASA7of1JApE1kNcRzxOoeUhtWlQrP4JZjiVOR8GYchfn2kREzle4gZB4mZihlz8RiYKirSTMUi-SVeggMaTWTwXJehFEdPZaipL5doWamMonUJdGeNIiRHpYLqdbmgYEqHWECdRjyhKRDExZwBChjmHLjEFPD83YYQjTNOI-Ac5SOkjBlHfTmsZo2LNH4C48jqdFq6tXqtv6gvMU6T11oQszg1jnRd3-HESYLKUXBaTcW65tT1dttq_QcnwQLvc9qdLzgbW5wfcwRzKV6K51JT1NypNKOEMHjBKWwqYrfMUhGn3eqXbN9YPcRsTxGl8YbKvZ6uf8VZsPJsPElxMkWm-2ekjTLSOSPySc6ayLy5cQc9825wfYVc87dzO9L-FklqEGmIQNA4Qu5tGXVOnUaj0_PBn_hDx_PPdH2TNoAWguPJMZJzSM5JRsMwZIsPM_xy7r2D6Wri89zhY55tvmUp-B6kzzQA38r41gc22gVVjkIrFJKogrds3B697eT0vZgL32Fyz0eiu7nI4LxgVgC0AlyO05PuJe0WE94DOkEDOw7k30_v-uryhHaLssqZRUGIyEePDogq9173faTldHbeCUll3gzks08ZjLT3r8TYov4MpMrsdUQta2We_Diw3I2t3te_2uqbqeY6Vf_Ojt4zrQsTqdOWRYiOXOeHc2V_w62uLz2-azAzSRgNsAIfsJjrDx93fTQsvfKpd1zfdnZdYqtjyImEvE12u1-kONfFpjxtkXMJJPU4rLs0XJWR58CGVUpRC1E-hG2q31rYi4uLvTNNq2kzSGeYEs1YaPktJu9AAiHOmNCWNQ1nIvbmUaAZ-eWiZYlcKNgUyybMiuDyH97qPvk=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-118.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E118F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E118F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E118FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E118FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E118F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E118FMW_e_g_Azure_Service_Bus
    E2E118FMW_e_g_Azure_Service_Bus --> E2E118F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVWtv4jAQ_CtWKsQXaENbHo0qpKQJJ06hrZo-7nScIhNvwKpJothpSyn__eyEEl4VPSMFZT0768yO7bkWxAQ0Q6tU5jSiwkDzqpjAFKoGqo4wh2oNVTkEWUrFzIUXYGqCxXExk0MfcUrxiAGvquwwjoRH33OCRit5UzAV6-EpZTMV9WAcA3ro15ApE1kNcRzxOoeUhtWFQrP4NZjgVOR8GYcBfnuiREzke4gZB4mZiClz8QiYKirSTMUi-SVeggMajWXwXJehFEfPZaipLxZoUakMo1UJdG8NIyRHpYLqdbmgYEIHWECdRjyhKRDExYwBChjmHLjEFPD83YYQjTJOI-Ac5SOkjBlHPTmsZo2LNH4G48jqdFq6tXytv6ovMU6Tt1oQszg1jnRd3-LESYLKUXBaTcW64tT1dttq_QcnwQLvctqdA5yNDc7POYK5FC_FM6kpam5VmlJCGLziFNYVsVtmqYjTbvVKtm-sHmK2o4jSeE3lqytdP8RZsPJsNE5xMkGm-2eoDTPSOSPySc6ayLy9dftX5n3_5hq55m_nbqj9LZLUINIQgaBxhNy7MuqcOo1Gp-eDP_YHjuef6fo6bQAtBMfjYyTnkJyTjIZhyBbvZ_jlPHh709XE17mDpzzbfM9S8D1IX2gAvpXxjQ9stAuqHIWWKCRRBW_ZuB1628npr2IufIfJPR-J7voig_OCWQHQEnA5Sk-6l7RbTHiP6AT17TiQfz-9m-vLE9otyipnFgUhIp892iOq3Hvdj6GW09l5JySVeduXzx5lMNQ-DomxQf0VSJXZ6Yha1tI8-XFguWtbvacf2urrqeYqVf_Ojt4xrQtjqdOGRYiOXOeHc21_w62uLz2-bTAzSRgNsALvsZjrD562fTQovfKld1zfdrZdYqtjyImEvE22u1-kODfFpjxtkXMJJPU4rLs0XJaR58CaVUpRC1E-hW2q30rYi4uLnTNNq2lTSKeYEs2Ya_ktJu9AAiHOmNAWNQ1nIvZmUaAZ-eWiZYlcKNgUyyZMi-DiHyW-PxE=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-118-I001 | Interface | E2E-118 inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-118-E001 | Enhancement | E2E-118 custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-118-F001 | Form/Report | E2E-118 operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
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

    subgraph E2E118CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E118CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E118CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E118CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E118CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E118CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E118CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E118CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iQgoFVKp2is26QxIQeOxKrBCMyaNOW_z4YuWSulUrX5g8W9d358fi28xynPADt4NNrTkgoH7TWxgQI0B2kr0oCmI62BtK2p2C3gFzCVYJwPmb70K6kpWTFoNLU656WI6EMPGE-qrSpTWkgKynZKjWDNAd1e68iVC5nWqQrG79MNqUXPaBu4IdtvNBMbGeeENSBrNqJgC7ICpjYSdau0UnYfVSSl5VqKE0NKNSnvjpJtdB3qRqO4PGyBvnhxieRIGWmaOeSIVJXHtyinjDlnnj0Pw1BvRM3vwDkzjMtLb_oUvrtXPTlmtdVTznit0tbcfsmrGBFHoD8Lpv77A9CazQLLfw60jsCxZwem8QIInB15YejZnn3g-b4hx8kGp1OVjsuB2LSrdU2qDQrMYDye-cvFMoFknbgPbQ3JkpDoR4zj1pwa47jNwZBbn6_PUZ9GKh3jnwNJjYzWkArKS7T4fFQPaLdHfw9uFbTnqG9JcBxnsHxYBGX21J3YMTjd2j_5-fr5o2SSfHQ_uYlpmFZvQTazMjlnxP7biOhiglQdUnVv9-ImiBLLMP7YIUMkw7c68qzZ_2DKq_irqw-PT-3O-yOiC-Qur-UcUgYxfjx9X1jHBdQFoRl29rh_K-RLk0FOWiZwp2PSCh7tyhQ7_e-M2yojAuaUyDsqBrH7DaZxb-o=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E118FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E118FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E118FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E118FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E118FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E118FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E118FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E118FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRDaiVIQKuUTtFYt0mjQg4ciVWDEZg1acp_nw1ZslZKpWrzB4t77_z4_Fp4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DL2AqwTjvM13pN1JRsmRQa2p1xgsR0qcOMByVG1WmtIDklG2VGsKKA7q70ZErFzKtVRWMPyZrUomO0dRwSzbfaSrWMs4Iq0HWrEXO5mQJTG0kqkZphew-LElCi5UUR4aUKlI8HCXbaFvUDgZRcdgCffWiAsmRMFLXM8gQKUuPb1BGGXPOPHsWBIFei4o_gHNmGJeX3ngffnhUPTlmudETznil0tbMfs0rGRFH4HTij6cfD0BrMvGt6UugdQQOPds3jVdA4OzICwLP9uwDbzo15DjZ4His0lHRE-tmuapIuUa-6Q-Hk2AxX8QQr2L3qakgXhAS_oxw1JhjYxg1GRhy6_PVOerSSKUjfN-T1EhpBYmgvEDzL0f1gHY79A__TkE7jvqWBMdxesv7RVCk--7ElsHp1v7Jz7fPH8aj-JP72Y1Nw7Q6C9KJlco5JfbfRoQXI6TqkKp7vxe3fhhbhvHHDhkiGb7XkRfN_gdT3sRfXV0_79uddUdEF8hd3Mg5oAwi_Hz6vrCOc6hyQlPs7HD3VsiXJoWMNEzgVsekETzcFgl2ut8ZN2VKBMwokXeU92L7G8mWcAI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**RICEFW Status Summary** — E2E Tower (0 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-118 — E2E-118</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*No timeline data available for this capability.*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

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
*E2E-118 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

