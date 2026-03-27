<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-98 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-98 R3 Equipment Product Supporting Items (PSI) Procurement** within the IAO program. It includes 3 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-98 - R3 Equipment Product Supporting Items (PSI) Procurement |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-98 - R3 Equipment Product Supporting Items (PSI) Procurement |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-98 Process Migration | Migrate R3 Equipment Product Supporting Items (PSI) Procurement business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-98 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **3 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-98 R3 Equipment Product Supporting Items (PSI) Procurement.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-98A_R3_Equipment_Product_Supporting_Items_(PSI)_Procurement | E2E-98A_R3_Equipment_Product_Supporting_Items_(PSI)_Procurement | Boundary Apps, External Partners/Supplier
, SAP S/4HANA IF | 26 | 15 |
| 2 | E2E-98B_R3_CFIN | E2E-98B_R3_CFIN | Boundary Apps, CFIN, MBC, SAP S/4 (IP & IF) | 17 | 10 |
| 3 | E2E-98C_R3_SAP_Transportation_Management | E2E-98C_R3_SAP_Transportation_Management | Boundary Apps, External Partners/
Supplier
, SAP S/4 (IP & IF) | 12 | 6 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-98A_R3_Equipment_Product_Supporting_Items_(PSI)_Procurement — E2E-98A_R3_Equipment_Product_Supporting_Items_(PSI)_Procurement

**Swim Lanes**: Boundary Apps · External Partners/Supplier
 · SAP S/4HANA IF | **Tasks**: 26 | **Gateways**: 15

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
        n1["Perform Supply Planning ICS (Phoenix)"]
        n2["Receive Procurement Planning Information"]
        n3["Review and Approve Procurement Planning Proposal by Intel Product BUs"]
        n4["Receive Information in ECA"]
        n5["Organize Transport-Intel Routing Guide (IRG)"]
        n6["Receive Manual invoices through OCR"]
        n7["Receive Incoming invoice/ B2B/OpenText/Web suite"]
        n8["ReadSoft Validation/Exception Handling based on rules setup"]
        n27(["fa:fa-play Initiate Supply Planning Process"])
        n28(["fa:fa-stop Information Received"])
        n31{{"fa:fa-code-branch exclusiveGateway"}}
        n32{{"fa:fa-code-branch B2B or OCR?"}}
        n33{{"fa:fa-code-branch exclusiveGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph External Partners/Supplier 
        n22["Perform Purchase Order Collaboration via SIFRIS"]
        n23["Perform Carrier Selection via Intel Routing Guide hosted Collaboration Portal"]
        n24["Pick Goods (Carrier) Order shipment"]
        n25["Forecast Communication and Commit"]
        n26["Raise Invoice (Supplier End)"]
        n36{{"fa:fa-code-branch exclusiveGateway"}}
        n37{{"fa:fa-code-branch exclusiveGateway"}}
        n45{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4HANA IF
        n9["Create Purchase Requisition Change ( Pull-in/Push-out)"]
        n10["Receive Purchase Requisition Approval"]
        n11["Create Purchase Order"]
        n12["Purchase Order Change (Quantity/Schedule Dates)"]
        n13["Purchase Order Line-Item Deletion"]
        n14["Trigger GTS Check"]
        n15["Calculate Taxes"]
        n16["Publish Purchase Order"]
        n17["Acknowledge/Confirm Purchase Order"]
        n18["Create Inbound Delivery with House Airway bill number (HAWB)"]
        n19["TM Embedded"]
        n20["Post Goods Receipt"]
        n21["Post Supplier invoice"]
        n29["E2E-98C R3 SAP Transportation Management"]
        n30["E2E-98B R3 CFIN"]
        n34{{"fa:fa-code-branch Purchase Order Amendment Needed?"}}
        n35{{"fa:fa-code-branch Invoice Accepted?"}}
        n39{{"fa:fa-arrows-alt parallelGateway"}}
        n40{{"fa:fa-arrows-alt parallelGateway"}}
        n41{{"fa:fa-arrows-alt parallelGateway"}}
        n42{{"fa:fa-arrows-alt parallelGateway"}}
        n43{{"fa:fa-arrows-alt parallelGateway"}}
        n44{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n9 --> n43
    n10 --> n39
    n39 --> n34
    n34 -->|"Pull-In/Push-Out"| n12
    n34 -->|"Cancellation"| n13
    n31 --> n2
    n13 --> n36
    n11 --> n42
    n1 --> n31
    n2 --> n38
    n27 --> n1
    n38 --> n3
    n38 --> n4
    n4 --> n28
    n3 --> n9
    n40 --> n14
    n40 --> n15
    n15 --> n41
    n14 --> n41
    n41 --> n16
    n23 --> n5
    n17 -->|"For Intel Qwned 
Transport only"| n23
    n5 --> n24
    n42 --> n40
    n43 --> n10
    n24 -->|"3B2 / E2Open"| n18
    n18 --> n44
    n44 --> n19
    n44 --> n20
    n19 --> n29
    n25 -->|"Supplier Responses via SIRFIS"| n31
    n38 -->|"Forecast sharing via SIRFIS"| n25
    n33 --> n8
    n6 --> n33
    n32 -->|"OCR"| n6
    n21 --> n30
    n8 --> n35
    n37 --> n26
    n35 -->|"No"| n37
    n26 --> n32
    n7 --> n33
    n35 -->|"Yes"| n21
    n42 --> n31
    n43 --> n31
    n22 --> n45
    n45 --> n17
    n16 --> n36
    n36 --> n22
    n12 --> n36
    n32 -->|"B2B"| n7
    n39 --> n11
    class n27 startEvt
    class n28 endEvt
    class n29 startEvt
    class n30 startEvt
    class n31 gateway
    class n32 gateway
    class n33 gateway
    class n34 gateway
    class n35 gateway
    class n36 gateway
    class n37 gateway
    class n38 gateway
    class n39 gateway
    class n40 gateway
    class n41 gateway
    class n42 gateway
    class n43 gateway
    class n44 gateway
    class n45 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWG1v4joW_isWo1E7EgjyAqF8uCtIoYM0M-VC7x2ttvvBJA5YDXbWTgpsp_99jxM7gJteaXv7oVKenOe8n2OHl1bEY9IatT5_fqGM5iP0cpVvyY5cjdDVGkty1UYV8CcWFK9TIq-UTMJZvqL_LcUcPzsoMYXN8I6mR4WuyIYT9Me8jcZATNtIYiY7kgiaXLWvMkF3WBxDnnKhpD-RYdJLSmv61YSLmIiTQK8XOFEfqCll5AR7gR_4M8WTJOIsvlCa9JNhEl29KudSvo-2WOSl-4Uk3_HhJ43zLTwnOJUEZLb5Lv2G1yRVMeaiUFhUiGeTDCqVHQYJW2U4omwDuN8DSGD2dIL6vddX9Pr58yOrjaJvy0eG4C9KsZS3JEEyB3j6nKOEpunokx-OZ_1eW-aCP5HRJ3ca3HpuO1KRjCD0Xlslt7MndLPNR2uexlq0s1cxjNzs0BaHkdtriyP8t2wRFp8shQN36A5rS5PACZ3QWEqS5G9ZgryKByyftK2pN3Nnt7Utpz_oh723-kyYt34wduw8EfFMI3KmdDabedNTqqaDvtN7X-lk5g16oaV0g3Oyx8eTwpvQrxXO-sHMCd5VWNmzvSzWC8Ejo9Cb9mf9WmEwcWZj912F_tjxh9pD0LMRONuiCS_KXkbjLJPVO_XHnH89thZEJFzs0KrIsvSIFilmDDoPzcMVul5sOWH08OWx9e8zmgu0JYkIfSZIOVoImGiWn3GZUolzytkl0yuZz5TsEWaxckfw95QAmHGJU7Q-gsKcpAqJiyhHkz_kpVr_zKEz24gyNA3Hl7J9kL0XG8xg36AHmDWZcZF3KgtLXuTK9l1BY4Ku58s7K_TBmaXvmBXgHmXPHHpKonwreLHZovtweUkKLtyL-E6Z0LQumriT7n1G2AM55N2fZA1lozm51DAsNeB4xZMc_YlTGpcBdqeHiGRlqF8hn6nSq9ZsjAARBaxX6Pi8yKzyBdegLsGjBHeyFKvs0pxCE7_pAVUXIlWyv5zzhye-zHl2kXIdZ2xxPOflxXDUGdFZQ-ajLSKHKC0kEO6qIXpsvb6e09xmGuQMcaEy_Q-b4X3M0PBEw0LwvezgNEcZFjhNSfqGBEvQmrHpISeCQT8sYBUzImS3zCYlAp3nzj0buUUhYJ9Lgu7V4YTgpEnxmosqkc8Uo9V8tpyvrOp5ZxpC8FVZWJGURDWtqZe3XObQF5c2FtD5OLX0q2Fa0OgJ3XEeS3StbXzRXsotzdSgWiw1VjMuSIRlDlZ2u4LRqLKiJl0h1OaUw4SpVFNRDgO6rnM2ZbE1et7gY5UNPkTz-3-3IVbjBVp1_a_jH2M0n52pvoGwQ0HUwNUdsCT_KaikZb7CLWYbyAW8TdMOZd1FIbcdqKaVEKd3voebNFX71a6w4zQ4UBbXkit71epR7dvvBWY5zY_dVbQlMWwadAvqpO2h91bDN7hwdeY52aFbaNq3R4Sj-u9B0M0GhO8eVmCSRE-WjOq2EKdRkaogHvCBWCeCMygtr1Mqt38dpFrO4-iJ8X1K4g3phpwl9M1wWqThKYNztlanq4oG6gBn7J7mW_SVw-UFjalQF4M1nOOIFbs1RHT9dfxzYqdJdcTDdzQFiTgud-f5mKgyL2B89UCWFc_sWXKMUD1B-oCx5JSpqTvt3AxDtPTKJq0PwWpc4VjDG_J2xL1eTZ0oajib_7Ak_OZRszpgDLrj8qz_QQiE-2aF95vVmCUxjtSh18C7-f9Gtprz3kdIzkdI7kdI3kdI_gd3F7tBnc5vyqp-dnoV4N1owNMSnm8AXwG_1LDBsprrZXVfQPP8UivEFguhlATOoGrwlYix5TmVakNxPG1qYAAt4NcSWkDf8pmrn4fmOagA894bagHr2cTiawcMXztgYvd1MhzfBvrGob5WaCw6vgX42mfHBOVqI7WKQCcKDlN9kP--Z3ByP7J6TuF2lx7L5LkmFG3YrV3TufB7BtB2HAO4piLexEVdNHXVHbSqiInfMfmptepwnBsLMJ9u8EYDRsLtazP1XloSCIJJuJtWV5zlTF1xfp3VsarLr7MLhYTPXnWXsRiuyZqnozOeD3Sh60q7WmN5NwdmnX7TQyYA0yK1Zt1DrmF4JqAfvPI6MKqMUdOege2EYf5TnVbKfceqVp0BU61Ta5t6Gr98XXHHmHcG1rh4GnDrcXFtCZMVuE6XDgXWlDvn38_lPJkfGi7xof5R4BK9aZb2eu_gjvmSvoTdZthrhv1muN8MD5rhoBkeNsM3jTAsh0a4OUq_OUq_OUq_OUq_jrLVbu0IfJLRuDV6aZW_uLVGrZgkuEjz1mu7hYucr44sao3KX6ZaRQZflOSWYri77irw9X8fCRXH" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-98B_R3_CFIN — E2E-98B_R3_CFIN

**Swim Lanes**: Boundary Apps · CFIN · MBC · SAP S/4 (IP & IF) | **Tasks**: 17 | **Gateways**: 10

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
        n1["Receive File in Bank"]
        n2["Update Payment Remittance"]
        n19(["fa:fa-stop Payment Data Updated"])
    end
    subgraph CFIN
        n3["Execute Payment Run"]
        n4["Create APM Memo Record"]
        n5["Process BCM Payment Batching Based on Business Rules"]
        n6["Generate APM Payment File"]
        n7["Route to Approver"]
        n8["Correct APM Correction File"]
        n9["Reverse APP Doc Number and Memo Record Deletion"]
        n10["Fetch Payments Factory (APM, BCM, MBC Monitor)"]
        n11["Review Failed Payment Log"]
        n12["Generate Payment Proposal"]
        n13["Replicate Supplier Invoice Posting"]
        n14["Post Collateral Expense Chargeback – IF Profit Center (Allocations)"]
        n15["Posted Collateral Cost Charged – IP Profit Center"]
        n18(["fa:fa-play Initiate Charge Back Process"])
        n21(["fa:fa-stop Memo Record Created"])
        n22(["fa:fa-stop APP Doc Reversed"])
        n23(["fa:fa-stop Charge Back Process Completed"])
        n25{{"fa:fa-code-branch Manual Approval Necessary?"}}
        n26{{"fa:fa-code-branch Approved?"}}
        n27{{"fa:fa-code-branch exclusiveGateway"}}
        n28{{"fa:fa-code-branch Can Be Corrected?"}}
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n30{{"fa:fa-code-branch exclusiveGateway"}}
        n31{{"fa:fa-code-branch Reversal or Reprocessing?"}}
        n32{{"fa:fa-arrows-alt parallelGateway"}}
        n33{{"fa:fa-arrows-alt parallelGateway"}}
        n34{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph MBC
        n16["Multi-Bank Connectivity (host-to-host)"]
        n17["Multi-Bank Connectivity (host-to-host)"]
    end
    subgraph SAP S/4 (IP & IF)
        n20(["fa:fa-stop Payment Details provided back to Source System (IP/IF)"])
        n24["E2E-98A R3 Equipment Product Supporting Items (PSI) Procurement"]
    end
    n12 --> n3
    n3 --> n32
    n4 --> n21
    n5 --> n25
    n25 -->|"No"| n27
    n7 --> n26
    n27 --> n6
    n29 --> n5
    n28 -->|"No"| n30
    n9 --> n22
    n10 --> n33
    n30 --> n9
    n33 --> n11
    n32 --> n4
    n11 --> n31
    n31 -->|"Reversal"| n30
    n2 --> n19
    n6 --> n16
    n33 --> n2
    n8 --> n29
    n13 --> n12
    n33 --> n20
    n24 --> n13
    n25 -->|"Yes"| n7
    n1 -->|"PAIN.002 (Pay-load file)"| n17
    n16 -->|"PAIN.001 (Pay-load file)"| n1
    n32 -->|"Reprocessing"| n29
    n34 --> n8
    n26 -->|"Yes"| n27
    n26 -->|"No"| n28
    n17 --> n10
    n31 -->|"Reprocessing"| n34
    n28 -->|"Yes"| n34
    n15 --> n23
    n14 -->|"Overhead Expense
 + Service Charges"| n15
    n18 --> n14
    class n18 startEvt
    class n19 endEvt
    class n20 endEvt
    class n21 endEvt
    class n22 endEvt
    class n23 endEvt
    class n24 startEvt
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
    class n31 gateway
    class n32 gateway
    class n33 gateway
    class n34 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWFtzozYU_isadlInU7tFXHx7aMc3djyzTj1xt51O3QcZRKxZjKgAJ27W_71HIGGDyUO3eUjQ4TvfuR8gb4bPA2qMjbu7NxazbIzeOtmeHmhnjDo7ktJOF5WC34hgZBfRtCMxIY-zDfungGEneZUwKfPIgUUnKd3QZ07R52UXTUAx6qKUxGkvpYKFnW4nEexAxGnGIy4k-gMdhmZYWFO3plwEVFwApjnAvguqEYvpRWwPnIHjSb2U-jwOaqShGw5Dv3OWzkX8xd8TkRXu5yldkdffWZDt4RySKKWA2WeH6BPZ0UjGmIlcyvxcHHUyWCrtxJCwTUJ8Fj-D3DFBJEj85SJyzfMZne_utnFlFH162sYIfvyIpOmchijNQLw4ZihkUTT-4Mwmnmt200zwL3T8wVoM5rbV9WUkYwjd7Mrk9l4oe95n4x2PAgXtvcgYxlby2hWvY8vsihP8btiicXCxNOtbQ2tYWZoO8AzPtKUwDP-XJcir-JWkX5Sthe1Z3ryyhd2-OzNv-XSYc2cwwc08UXFkPr0i9TzPXlxStei72HyfdOrZfXPWIH0mGX0hpwvhaOZUhJ478PDgXcLSXtPLfLcW3NeE9sL13IpwMMXexHqX0JlgZ6g8BJ5nQZI9mvK86GU0SZK0vCd_Yvzn1niiPmVHijwWUcRiNIXu2xp_XaEsQH1OAogSrcnpQOMMPdEDyzIS-7QOxaN7AIdkHJJemvGkUpiTjKCSJACVh1IHWqnh6cxbPl7x2cC2eKV-fm07j-tGHQDNBJX-TdYrtKIHDg76MPF1nAs4mVeapmg6W1WEU5L5exg2uEhpgDjkIE9hLQDsKYcVVWfpA8tHGlOh7WkamcA6dCDTy6XvGZepF_xIRR0ylL5zIaifFWTqmoETt3yjolzAkUrLazSHHnnMDzsqEImD68DRnEZUsjTKYwKDRyFc7XWKPOJnHFrjHsx3ZV66aDWdoRWH_c3FQ4Og7Jgjoy-gCA4GVfif-HMDa11nSsOgAAlPSdTA2gVvEjFfgjd5ApcQ1jI-cphXtOZpBhVqKMnCyzuQtSgCPUEitHhNaAz5mcGifKY74n9B29wysY2WnjQeMoCDI0B-P4kiDvYgTWkzTldRQ4BX5LPCWMEcVLTrOm2DaHgZiCSCJbGEtDIZY0kDPQceqq68DEY5d7gxTNcFLhs-aKpYDRXdJqptbvB2A9_iFUR9SKCbbpXdtzetLJ_7vR08uaC1ViTOIVllw8PFI5U0sH5-3hrn8zVBv51AjUpwgx-04-mrH8HEHunHchM31YbtajMCk071yLWYG32TOdv8NjXcrlZWDtLIBVwnZU1gFpre2tZFnwjBX9IeiTKUEGjciEbvGLW_RclpVWLxe_HdrnnYMNdDInfqKo8y1pNPH6hIHMsleGQZ7KU9DF0v4z35tzmmg_-ueOvMZrJGmx8ddA-j_B2siVqPm-890GgG-y9FslNZAOugWDWw5zc8F7CxNidYHgfJ-aNkbEyO3FwLa9EbDSfoyUaLv3OW6PUY5PAskBuQC7nz0BJ4UnS_3iwfipHMBZXQ24Bg46Je7ycokDrb6mips1OeLfVWFLvq7KqzVQi-bo1HvjW-ynlTNwYK2NdAJajOo_JcEQ3rRLZ6w4kVztIeYVO5WLmsBCN9VjFg7bOtYnQ0A1YMFQAr23pw6h4odawN9NW53zCoPRyqo8Zj7ZDVVKgsqDRju5nWP-S7BDij06o9XU-Wjz-YpgVFJqdexEkgX_3oQwHGFbpfh-N2eC1PRRouO6OsapVb5ehQ-9lv-FnVv7qjG0OrYNUI2LzNfsOs7TSbQ5up7mDdkDpz2FHQX6CUewqBqsc73P8ebcqXefXMKrmwbkGsCoedq5frQqy_lerykfquqUkts1WKW6VWq9RulTrtXkCnqI-JurjfLh60i4ft4lGrGAauVYzbxVa72G4XO1psdI0DFQfCAmP8ZhT_ATDGRkBDAsvbOHcNkmd8c4p9Y1x8KRt58akwZwRW9KEUnv8F0GQFJw==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-98C_R3_SAP_Transportation_Management — E2E-98C_R3_SAP_Transportation_Management

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4 (IP & IF) | **Tasks**: 12 | **Gateways**: 6

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
        n1["Receive/Send Information in Carrier Invoice Reconciliation/Dispute..."]
        n2["Event updates are received in GTT"]
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n11["Feed Rates/Charges Integrators 3rd party service – Redwood"]
        n12["Carrier"]
        n13(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n14(["fa:fa-play Events Published"])
        n20{{"fa:fa-arrows-alt parallelGateway"}}
        n21{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n3["Generate Freight Unit (TM)"]
        n4["Create Freight Order (TM)"]
        n5["Perform Carrier Updates and Calculate Charges"]
        n6["Execute Freight Order (TM)"]
        n7["Post Freight Settlement Document (TM)"]
        n8["Create Service PO for FSD (TM)"]
        n9["Post SES with Auto Release (TM)"]
        n10["Create Cost Distribution/Agency Business Document (TM)"]
        n15(["fa:fa-stop TM process ended"])
        n16["E2E-98A R3 Equipment Product Supporting Items (PSI) Procurement"]
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n3 --> n4
    n5 --> n18
    n7 --> n8
    n19 --> n5
    n6 --> n22
    n4 --> n19
    n9 --> n10
    n10 --> n15
    n11 --> n20
    n13 --> n11
    n17 --> n1
    n14 --> n12
    n12 --> n21
    n21 --> n17
    n20 --> n17
    n21 --> n2
    n1 --> n22
    n20 --> n19
    n2 -->|"Event Update"| n18
    n18 --> n6
    n8 --> n9
    n22 --> n7
    n16 --> n3
    class n13 startEvt
    class n14 startEvt
    class n15 endEvt
    class n16 startEvt
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVtuO2zYQ_RVCwdYbwM6KsmTZfijgmwIDWcRYbdqHuA-0RNlEaEklKV-y8b93KFG-rbdtWj8sdo5mzswcDi8vVpTF1Opbd3cvLGWqj14aakXXtNFHjQWRtNFEFfAbEYwsOJUN7ZNkqQrZ99INu_lOu2ksIGvG9xoN6TKj6Mu0iQYQyJtIklS2JBUsaTQbuWBrIvajjGdCe7-j3cROymzm0zATMRUnB9v2ceRBKGcpPcFt3_XdQMdJGmVpfEGaeEk3iRoHXRzPttGKCFWWX0j6SHa_s1itwE4IlxR8VmrNP5EF5bpHJQqNRYXY1GIwqfOkIFiYk4ilS8BdGyBB0m8nyLMPB3S4u5unx6To09M8RfCLOJFyTBMkFcCTjUIJ47z_zh0NAs9uSiWyb7T_zpn447bTjHQnfWjdbmpxW1vKlivVX2Q8Nq6tre6h7-S7ptj1Hbsp9vD3KhdN41OmUcfpOt1jpqGPR3hUZ0qS5H9lAl3FM5HfTK5JO3CC8TEX9jreyH7NV7c5dv0BvtaJig2L6BlpEATtyUmqScfD9tukw6DdsUdXpEui6JbsT4S9kXskDDw_wP6bhFW-6yqLxUxkUU3YnniBdyT0hzgYOG8SugPsdk2FwLMUJF-hYVaUs4wGeS6rb_qX4q9z64lGlG3oQwjriqZpkok1USxLEUvRiAjBqAB4k4Fs6ElviohxVno8jJnMC0U_fPgwt_44o3WAdrKhqUJFHoM4EhFBkagSxZr44_PzZQj2X17mVkL6CWnpM6S1gF0QrRDdRbyQEPaxEnluHQ5VGJR71eVkp6hICUcz2AwpFfIBhUWec93BeSrddUChkCdd28MIttQSapymigKRyoREbRGjHFj29cSgeeHYuA0KxNssi6-K1w0bra6-tO-_1m3lHGZEryuVOhlToCIUMYRjMUagt67mWMxgQxjXByTwvT8ndK8IS50lmhULzuSKxlf-jn3SFQrMtrJFuNK9Ec4pf6VqFYR_Luj1UoSDGQofXHQ_naFf0DQ4L6kNDXyksD5AgwJRHg3oC-iB7p8f31_q52phBT33_KwP8huuHrjOqNDze5zbL_X4wWiPCI8KrpmMxpfhHT2zOxoV_yKVr1NlUh0dQ6oUh1sNJn6cRUX5z-uw7qmZ0EzV7DOCglEQjm_49-o04SREW6ZWaFCoDEaQU5iZGwHYPmUY6UDYoEqwRVHu1sGSptEeDWE7pXoE_6ZS7J2mTKosR8-PKDeTC4v9aspwqZ4zafW6A_TURpM_C5aX3DDvcRGpciNmQsGVhqaKriW6n4XT9-V2KESp3FUF3Z89D6qw3n8Kc5ybA8_Sfzx80jZqtX6FQTWmV5m4a2y_smsT9yrbM3anMh3H2K4J7xnbuGO7jrcNUBNgbBiOHqYgjGvAlHC06xx1TuwYitrDMZzYrwH7Gqiz1hRXbRwD6j7KFD_qW6HalnPrx5lQuFuFdIxtzCOBKbKuABvl2mdXZ9l8_RK6xN03cM-8Zi7Rzhvefn3VX8Ld23DvJgzS3ITxbdipYatprSlczSy2-i9W-YaGd3ZME1JwZR2aFoGzIdynkdUv35pWdfWOGYETeV2Bh78AAYWYEg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-98A_R3_Equipment_Product_Supporting_Items_(PSI)_Procurement, E2E-98B_R3_CFIN, E2E-98C_R3_SAP_Transportation_Management | |
| External Partners/Supplier
 | E2E-98A_R3_Equipment_Product_Supporting_Items_(PSI)_Procurement,  | |
| SAP S/4HANA IF | E2E-98A_R3_Equipment_Product_Supporting_Items_(PSI)_Procurement,  | |
| CFIN | E2E-98B_R3_CFIN,  | |
| MBC | E2E-98B_R3_CFIN,  | |
| SAP S/4 (IP & IF) | E2E-98B_R3_CFIN, E2E-98C_R3_SAP_Transportation_Management | |
| External Partners/
Supplier
 | E2E-98C_R3_SAP_Transportation_Management | |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
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

    subgraph E2E98CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E98CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E98CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E98CDAA_e_g_XEUS -.-> E2E98CDAD_e_g_Azure_SQL
    end
    style E2E98CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E98CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E98CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E98CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E98CDAA_e_g_MES_300 -.-> E2E98CDAD_e_g_SAP_HANA
    end
    style E2E98CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E98CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E98CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9vmkAUx_-VyzXGLdGOatFK0ian4GpCm67YbUlZyAkPvfQEAseqtf7vuwOlm9Wu6V1CvPfj-x6fR84V9uMAsIFrtRWLmDDQqi5mMIe6geoTmkG9geoZ-HnKxNKG38CVg8dx6SlCv9OU0QmHrK6ywzgSDnsqBE70ZKHClG1I54wvldWBaQzobtRARCby-lpF8PjRn9FUFBp5Bld08YMFYibPIeUZyJiZmHObToCrQiLNlS2S3TsJ9Vk0lca2Lk0pjR5eTKf6eo3WtZobVSXQuO9GSC6f0ywzIUQ0SfrxAoWMc-Oor5vD4bCRiTR-AONI07rdfmdzbD6qnoxWsmj4MY9T5W6b-q5eMBks-UaO6GaHdCu5ltU1262Dcid93WppO3IQ85f2hsO-3tcrvcFAk-ugXqej3G5UKmb5ZJrSZIasltU7G5hkYHvgTT3ylKfgOd_sexcjF_8qo9UKWAq-YHFUQVNrm06K7J_WnSMT4Xh6jNRvKWAYRsn0dY65U_GTi908OGsH8hn4p24egiZfWYkVQUgGufizkiywvtUFah43Lw5VKhMhCjYsxJLDQRBb2ETtCralqf0v7JNk8T-8DrnxLsk1-RDdK8vx2pq2BSyPSB7fw7gq-wZiGYNUzHsIbzrZB3lb6j2Mt7EfQry_LDo_v3jeADILpugLIjcj-RwyDi5-PvxR7IzOhqls__4vYn6gIZOMCSK3g8vR2BqM724tZFtfrWvzwDTt2xer7am5kyThzKfKu390tmcemJNJBVU38f4R2Z4l5a0oaMZh02YhlPLllbF3HOUbbunralf0e73eK_S4geeQzikLsLHCxY0v_y8CCGnOBV43MM1F7CwjHxvFpYzzJKACTEYl0XlpXP8BPPf1zQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E98FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E98FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E98FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E98FDAA_e_g_XEUS -.-> E2E98FDAD_e_g_Azure_SQL
    end
    style E2E98FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E98FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E98FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E98FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E98FDAA_e_g_MES_300 -.-> E2E98FDAD_e_g_SAP_HANA
    end
    style E2E98FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E98FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E98FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9vmkAUx_-VyzXGLdGOatFK0ianwGpCm67YbUlZyAkPvfQEAseqtf7vuwO1m9Wu6V1CvPfj-x6fR84lDpIQsIFrtSWLmTDQsi6mMIO6gepjmkO9geo5BEXGxMKB38CVgydJ5SlDv9OM0TGHvK6yoyQWLnsqBU70dK7ClM2mM8YXyurCJAF0N2wgIhN5faUiePIYTGkmSo0ihys6_8FCMZXniPIcZMxUzLhDx8BVIZEVyhbL7t2UBiyeSGNbl6aMxg8vplN9tUKrWs2LtyXQqO_FSK6A0zw3IUI0TfvJHEWMc-Oor5u2bTdykSUPYBxpWrfb76yPzUfVk9FK540g4Umm3G1T39ULx4MFX8sR3eyQ7lauZXXNduug3Elft1rajhwk_KU92-7rfX2rNxhoch3U63SU24srxbwYTzKaTpHVsnpntkkGjg_-xCdPRQa--8259zDy8K8qWq2QZRAIlsRbaGpt0kmZ_dO6c2UiHE-OkfotBQzDqJi-zjF3Kn7ysFeEZ-1QPsPg1Csi0OQrK7EyCMkgD39WkiXWt7pAzePmxaFKVSLE4ZqFWHA4CGIDm6i9hW1pav8L-ySd_w-vS278S3JNPkT3ynL9tqZtAMsjksf3MN6WfQOxjEEq5j2E153sg7wp9R7Gm9gPId5fFp2fXzyvAZklU_QFkZuhfNqMg4efD38UO6NzYCLbv_-LWBBqyCQjgsjt4HI4sgaju1sLOdZX69o8ME3n9sXq-GruJE05C6jy7h-d45sH5mRSQdVNvH9Ejm9JeSsOm0nUdFgElXx1ZewdR_WGG_q62lv6vV7vFXrcwDPIZpSF2Fji8saX_xchRLTgAq8amBYicRdxgI3yUsZFGlIBJqOS6Kwyrv4AuJz19w==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-98-R001 | Report | R3 Equipment Product Supporting Items (PSI) Procurement operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-98-C001 | Conversion | Legacy data migration for R3 Equipment Product Supporting Items (PSI) Procurement | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-98.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E98C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E98C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E98CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E98CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E98C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E98CMW_e_g_Azure_Service_Bus
    E2E98CMW_e_g_Azure_Service_Bus --> E2E98C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1vokAQ_isbGuMXbemLb6QxAcGLF2yb0pe7nBeysoNuugJhl7bW-t9vF6xYbNPemmCYeeaZ5ZmZ3ZUWxAQ0Q6vVVjSiwkCrupjDAuoGqk8xh3oD1TkEWUrF0oVHYMrB4rjw5NA7nFI8ZcDrKjqMI-HRl5zguJ08K5iyDfGCsqWyejCLAd2OGsiUgayBOI54k0NKw_paoVn8FMxxKnK-jMMYP99TIubyPcSMg8TMxYK5eApMJRVppmyR_BIvwQGNZtJ4pktTiqOH0tTS12u0rtUm0TYFurEmEZKrVkPNptxQMKdjLKBJI57QFAjiYskABQxzDlxiCnj-bkOIphmnEXCO8hVSxoyDoVxWq8FFGj-AcWB1u23d2rw2n9SXGCfJcyOIWZwaB7quVzhxkqByFZxWS7FuOXW907Ha_8FJsMD7nHb3C87jd5xvPoK5FC_FS6kpalUyLSghDJ5wCruK2G2zVMTptIcl2zd2DzHbU0RpvKPyYKDrX3EWrDybzlKczJHp_plok4x0T4l8ktMWMq-u3NHAvBldXiDX_O1cT7S_RZBaRDZEIGgcIfe6tDonTq878MGf-WPH8091fZc1gDaCw9khkj4kfZLQMAxZ4Q8Jfjm33ofRyvFp6Pg-DzZfshR8D9JHGoBvZfzd1x13CqYchTYoJFEFbVm1Krvt5OyDmAvfYXLeI9Hf3WJwVhArANoAzqfpUf-c9guHd4eO0MiOA_n307u8OD-i_SKr6soiH0TkrT77gsqx679OtJzNzosgmcyrkXwOKYOJ9vqFErvEn2FUkmot1JY2TZMfA5a7M-JD_asR3w01t6H6dyZ5r1ldmEmN3jUH0ZHr_HAu7G90qevL3q62lpkkjAZYgT9oLtcf31dbaFy2yadt4_q2U-0QWx0_TiTkLVKtfBHiXBbDeNImZxJImnHYdGm4SSPnf6dNSlELUd6EbanfVther7d3lmkNbQHpAlOiGSstv73k3UcgxBkT2rqh4UzE3jIKNCO_VLQskRsFm2JZhEVhXP8Dj2E9sQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-98.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E98F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E98F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E98FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E98FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E98F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E98FMW_e_g_Azure_Service_Bus
    E2E98FMW_e_g_Azure_Service_Bus --> E2E98F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1vokAQ_isbGuMXbemLb6QxgYIXL9g2pS93OS9kZQfddAXCLm2t9b_fLlix2MbemmCYeeaZ5ZmZ3aUWxAQ0Q6vVljSiwkDLupjBHOoGqk8wh3oD1TkEWUrFwoUnYMrB4rjw5NB7nFI8YcDrKjqMI-HR15zguJ28KJiyDfCcsoWyejCNAd0NG8iUgayBOI54k0NKw_pKoVn8HMxwKnK-jMMIvzxQImbyPcSMg8TMxJy5eAJMJRVppmyR_BIvwQGNptJ4pktTiqPH0tTSVyu0qtXG0SYFurXGEZKrVkPNptxQMKMjLKBJI57QFAjiYsEABQxzDlxiCnj-bkOIJhmnEXCO8hVSxoyDgVxWq8FFGj-CcWB1u23dWr82n9WXGCfJSyOIWZwaB7quVzhxkqByFZxWS7FuOHW907Ha_8FJsMC7nHZ3D-fxB853H8FcipfihdQUtSqZ5pQQBs84hW1F7LZZKuJ02oOS7Ru7h5jtKKI03lL54kLX93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3eGFeTu8ukSu-du5GWt_iyC1iGyIQNA4Qu5NaXVOnF534IM_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydkvYi58h8l5j0R_e4vBWUGsAGgNOJ-kR_1z2i8c3j06QkM7DuTfT-_q8vyI9ousqiuLfBCR9_rsCirHrv821nI2Oy-CZDKvh_I5oAzG2tseJbaJv8KoJNVaqC2tmyY_Bix3a8QH-r4R3w41N6H6dyZ5p1ldmEqNPjQH0ZHr_HAu7W90qevL3q62lpkkjAZYgT9pLtcfPVRbaFS2yZdt4_q2U-0QWx0_TiTkLVKtfBHiXBXDeNImZxJImnHYdGm4TiPnf6tNSlELUd6FbanfRther7dzlmkNbQ7pHFOiGUstv73k3UcgxBkT2qqh4UzE3iIKNCO_VLQskRsFm2JZhHlhXP0D1dI9yQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
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

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-98-I001 | Interface | R3 Equipment Product Supporting Items (PSI) Procurement inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-98-E001 | Enhancement | R3 Equipment Product Supporting Items (PSI) Procurement custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-98-F001 | Form/Report | R3 Equipment Product Supporting Items (PSI) Procurement operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
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

    subgraph E2E98CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E98CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E98CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E98CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E98CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E98CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E98CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E98CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRF6iQgoFVKp2is26QxIQeOxKqDEZg1acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuD38BUgnHeZ7rSb6SiZMGg1tTqnBcioo8dYDgqN6pMaSFZU7ZVagRLDujuRkeuXMi0VlUw_pCuSCU6RlPDLdl8p5lYyTgnrAZZsxJrNiMLYGojUTVKK6T7qCQpLZZSHBlSqkhxf5Rso21ROxjExWEL9NWLCyRHykhdTyFHpCw9vkE5Zcw58-xpGIZ6LSp-D86ZYVxeeuN9-OFBeXLMcqOnnPFKpa2p_ZpXMiKOQH8SjP2rA9CaTALLfwm0jsChZwem8QoInB15YejZnn3g-b4hx0mD47FKx0VPrJvFsiLlCgVmcDXx57N5AskycR-bCpI5IdHPGMeNOTaGcZODIXc-X56jLo1UOsa_epAaGa0gFZQXaPblqD6T3Y78I7hTzA6jviXAcZy-4f0aKLK9N7FlcNLYPzXzzcNHySj55H52E9Mwre782cTK5JwR--8uRBcjpOqQqnt3I26DKLEM47kXMkQyfGc7Xlj9Dx15i359_fFpb3banQ9dIHd-I-eQMojx08mrwjpeQ7UmNMPODndvhHxhMshJwwRudUwawaNtkWKn-41xU2ZEwJQSeT3rXmz_AOKzbqI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E98FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E98FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E98FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E98FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E98FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E98FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E98FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E98FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRF6iRIQKuUTtFYt0ljQg4ciVWDEZg1acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3Db2AqwTjvM13pN1JRsmRQa2p1xgsR0scOMByVG1WmtIDklG2VGsKKA7q70ZErFzKtVRWMPyRrUomO0dRwSzbfaSrWMs4Iq0HWrEXO5mQJTG0kqkZphXQfliShxUqKI0NKFSnuj5JttC1qB4OoOGyBvnpRgeRIGKnrGWSIlKXHNyijjDlnnj0LgkCvRcXvwTkzjMtLb7wPPzwoT45ZbvSEM16ptDWzX_NKRsQROJ344-nVAWhNJr41fQm0jsChZ_um8QoInB15QeDZnn3gTaeGHCcNjscqHRU9sW6Wq4qUa-Sb_tUkWMwXMcSr2H1sKogXhIQ_Ixw15tgYRk0Ghtz5fHWOujRS6Qj_6kFqpLSCRFBeoPmXo_pMdjvyD_9OMTuM-pYAx3H6hvdroEj33sSWwUlj_9TMNw8fxqP4k_vZjU3DtLrzpxMrlXNK7L-7EF6MkKpDqu7djbj1w9gyjOdeyBDJ8J3teGH1P3TkLfr19cenvdlZdz50gdzFjZwDyiDCTyevCus4hyonNMXODndvhHxhUshIwwRudUwawcNtkWCn-41xU6ZEwIwSeT15L7Z_AAWTbro=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
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

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-98 — R3 Equipment Product Supporting Items (PSI) Procurement</span></div>
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
*E2E-98 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

