<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-71 — E2E-71</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-71 · Forecast to Stock</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-71 E2E-71** within the IAO program. It includes 6 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Forecast to Stock |
| **Capability** | E2E-71 - E2E-71 |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Forecast to Stock |
| **L2 Capability** | E2E-71 - E2E-71 |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-71 Process Migration | Migrate E2E-71 business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-71 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **6 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-71 E2E-71.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End | E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End | Boundary Apps, SAP S/4 IF Sending Plant (EWM) , SAP S/4 IF​
Receiving Plant (EWM), SAP S/4 Intel Foundry

Sending Plant (IM) 
, SAP S/4 Intel Foundry
Receiving Plant (IM) | 27 | 7 |
| 2 | E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End | E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End | Boundary Apps, SAP S/4 IF Sending Plant (EWM) , SAP S/4 IF​
Receiving Plant (EWM), SAP S/4 Intel Foundry

Sending Plant (IM) 
, SAP S/4 Intel Foundry
Receiving Plant (IM) | 27 | 7 |
| 3 | E2E-_71C_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_(IM_to_EWM) | E2E-_71C_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_(IM_to_EWM) | EWM, SAP S/4 Intel Foundry
 (IM)
 | 10 | 1 |
| 4 | E2E-_71D_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_IM) | E2E-_71D_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_IM) | EWM, SAP S/4 Intel Foundry
 (IM)
 | 10 | 1 |
| 5 | E2E-_71E–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_EWM) | E2E-_71E–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_EWM) | Receiving Warehouse (EWM)
, SAP S/4 Intel Foundry
 (IM)
, Supplying Warehouse (EWM | 14 | 5 |
| 6 | E2E-_71F_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_–_TM_Steps | E2E-_71F_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_–_TM_Steps | EWM, External Partners/ B2B
, SAP S/4  | 19 | 5 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End — E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End

**Swim Lanes**: Boundary Apps · SAP S/4 IF Sending Plant (EWM)  · SAP S/4 IF​
Receiving Plant (EWM) · SAP S/4 Intel Foundry

Sending Plant (IM) 
 · SAP S/4 Intel Foundry
Receiving Plant (IM) | **Tasks**: 27 | **Gateways**: 7

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
        n8["Send Production Update"]
        n9["Receive Shipping Information"]
    end
    subgraph SAP S/4 IF Sending Plant (EWM) 
        n10["Inbound Delivery Distribution to EWM"]
        n11["Create and Confirm Put-away Warehouse task (EWM)​"]
        n12["Goods Receipt EWM​"]
        n13["Outbound Delivery Order (EWM)"]
        n14["Pick and Pack Updates (EWM Managed)"]
        n15["Goods Issue and Update Inventory"]
        n16["PGI"]
        n21["fa:fa-user Ad hoc Move from doc storage type to FG storage type"]
        n31(["fa:fa-stop endEvent"])
    end
    subgraph SAP S/4 IF​ Receiving Plant (EWM)
        n17["Inbound Delivery distribution to EWM"]
        n18["Goods Receipt EWM"]
        n19["Create and Confirm Put-away Warehouse task (EWM)"]
        n20["Create Ad-hoc task for movement from EWM location (SLOC2) to factory (SLOC1)"]
    end
    subgraph SAP S/4 Intel Foundry  Sending Plant (IM)  
        n2["311 / Inbound Delivery Creation SLOC 2​"]
        n3["Ship to Customer (Sales Order)"]
        n4["311 is posted in S4 from SLOC1 to SLOC2"]
        n5["Create STR"]
        n6["Convert STR to STO"]
        n7["CI and Billing document"]
        n23[["fa:fa-cog Complete Production"]]
        n24[["fa:fa-cog GR Production Order at SLoc 1"]]
        n25[["fa:fa-cog Ship to Next Factory (STO)"]]
        n26[["fa:fa-cog Perform Outbound Delivery"]]
        n27[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n29(["fa:fa-stop GR Posted"])
        n30(["fa:fa-stop endEvent"])
        n32["E2E- 71F – Intel Foundry - Shipment of goods through Stock transfer – TM Steps"]
        n33{{"fa:fa-code-branch If Customer requires later?"}}
        n34{{"fa:fa-code-branch Customer or Next Factory?"}}
        n35{{"fa:fa-code-branch exclusiveGateway"}}
        n36{{"fa:fa-code-branch exclusiveGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
        n39{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph SAP S/4 Intel Foundry Receiving Plant (IM)
        n1["Stock Posted in Manufacturing locations"]
        n22[["fa:fa-cog Perform Inbound Delivery (S/4)"]]
        n28(["fa:fa-stop Stock Posted"])
    end
    n23 --> n24
    n25 --> n35
    n24 --> n29
    n10 --> n12
    n12 --> n11
    n33 -->|"Yes"| n21
    n4 --> n37
    n11 --> n4
    n34 -->|"Factory"| n36
    n38 --> n27
    n26 --> n38
    n35 --> n26
    n3 --> n35
    n13 --> n14
    n14 --> n15
    n15 --> n16
    n16 --> n22
    n22 --> n17
    n17 --> n18
    n18 --> n19
    n19 --> n20
    n1 --> n28
    n5 --> n6
    n2 --> n10
    n6 --> n36
    n38 --> n13
    n37 --> n33
    n37 --> n34
    n20 --> n1
    n36 -->|"Next Factory
 location"| n25
    n38 --> n7
    n21 --> n31
    n7 --> n30
    n27 --> n32
    n34 -->|"Customer"| n39
    n33 -->|"No"| n39
    n39 --> n3
    class n21 userTask
    class n22 serviceTask
    class n23 serviceTask
    class n24 serviceTask
    class n25 serviceTask
    class n26 serviceTask
    class n27 serviceTask
    class n28 endEvt
    class n29 endEvt
    class n30 endEvt
    class n31 endEvt
    class n32 startEvt
    class n33 gateway
    class n34 gateway
    class n35 gateway
    class n36 gateway
    class n37 gateway
    class n38 gateway
    class n39 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWFtv4jgU_itWRhWtBJo4FwI87IpSUiG1U1Q6O1pN98EkToka4qzj9LId_vseJ3YgIWhWs32oyufznevnE9IPI2AhNSbG2dlHnMZigj56YkO3tDdBvTXJaa-PKuAPwmOyTmjekzYRS8Uq_qc0w072Js0k5pNtnLxLdEWfGEVfF300BWLSRzlJ80FOeRz1-r2Mx1vC32csYVxaf6KjyIzKaOrokvGQ8r2BaXo4cIGaxCndw7bneI4veTkNWBo2nEZuNIqC3k4ml7DXYEO4KNMvcnpL3r7FodjA54gkOQWbjdgmN2RNE1mj4IXEgoK_6GbEuYyTQsNWGQni9AlwxwSIk_R5D7nmbod2Z2ePaR0U3dw_pgh-goTk-RWNUC4Anr8IFMVJMvnkzKa-a_ZzwdkznXyy5t6VbfUDWckESjf7srmDVxo_bcRkzZJQmQ5eZQ0TK3vr87eJZfb5O_xuxaJpuI80G1oja1RHuvTwDM90pCiK_lck6Ct_IPmzijW3fcu_qmNhd-jOzGN_uswrx5vidp8of4kDeuDU9317vm_VfOhi87TTS98emrOW0yci6Ct53zscz5zaoe96PvZOOqzitbMs1kvOAu3Qnru-Wzv0LrE_tU46dKbYGakMwc8TJ9kGXbKi1DKaZllencmfdPT90VjBPBGEC4tAxCxFX7MQ6nk0_jqwG4PdPQ1o_ELRahNnGUgTLdKI8S2RpNoafLVCr6ZLtPrsoIWPZCRJXCYkFeh8_u32Ah0EwSZEWaRrmSu6ogkEg4yvYqg0XhdlboIhYDVzwxhoM04haUSAOWNpFPMtWhZiQORYvhFONwy0hIQcexn3sbBMc91yZIGja8bCHJW1ZqIM1mVpg-VdIVqp3skVo_w37R2wX8bBc5ngksAfVZfz0hrdkpQ80bDNcut8FnleVNVVPOj9C00F4-8tylAGul40UUt2KCKTiAzkjULTEG1AXbcMphlxtkUhfMrBGySBxHtGZZ_96wbU9Gjj89olWGXVToCMwOzi50qoelp1-aWliMNqvC5BhD8VxKhzjk2b8a-IptlVc-9iGg5kR0tTuBRoC63dQjuq9soRJywobwo6X93czawLmXlEAjnCCsIX_-USpYImyJcNAV77Qi3gPh1eKKlnG2P0GR01scxbpiNDI6tL5FLj8q7LTGcFTHkrxb0i8MyulN7qh6OixTnKWC5oiGJw71QtKCuUnsrqm0R338fVw33zTOoZZgM5C3lYeni4a9pIlcwW5RgvYWHKhoCgi20lx8N-2N9r1QbsCYa-zRIKYffbDwgNhtNkXN8fbsrqvhPI7AaGj9tct8nVvfxC3wTy69E_3F20icMmcUm5XLToaOG0eV6rvKqnPi8fvugrfB8rm6SBMv22j3HrYsuKy2nub3alDvOnG6CykyKcW_MB8rCPpM6w3ZLxoGxNeV0YPEzLiys2nBVPIHzBYFkK-EaUR9BrxX-4hQMKT7KmYO2Pj339IR2sgRZs0CLa65fTv4uYg4ITaA3__dHY7Q49ON0eajpc7cPxHfHdbj59C5Iih5ldV98U2rThr9G8PY1wzl7zAUkEyggnSUKTE6TRr5DGnaQ4PZXff91gR0-ARfMBIFdQqYBlvVHgWVnIxVlwSdNrtSUFy-q-Qkd78BxyOrp_o5a0D1PoeMDBXkGDwW9yW2jArQDb1YCjLMYKwGYFYEsDlgLUN1ZQswR-PBp_Uijuh3yKqxPly_Y0FVeAjm47iqlUWrLtoT4dqVQ03RoqfyNtobK3akqrGqwArCNilRKuLZQLrF1gFcTS9Vq63roKTwE6DawSxXXPxsqHqQH1WTNUUB1TR9Dmus52J7CtAZWCfQTUg9Vj0wZD1erDrQBnWpbV4NxWwLrzqgBbu9PhdMaWBqz2aPVGqmY7bmvmC2sdqNbZBy8aZXz9htXErcP3pOaRffrIOX3knj4anj7yTh-N1FtoEx13obbZieJO1KrfpJu4rV_ymrDTDbvd8LAb9rrhUTc81rDRN0AAWxKHxuTDKP-pYkyMkEakSISx6xukEGz1ngbGpPzng1GUrw5XMYGNvK3A3b-mL2I0" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End — E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End

**Swim Lanes**: Boundary Apps · SAP S/4 IF Sending Plant (EWM)  · SAP S/4 IF​
Receiving Plant (EWM) · SAP S/4 Intel Foundry

Sending Plant (IM) 
 · SAP S/4 Intel Foundry
Receiving Plant (IM) | **Tasks**: 27 | **Gateways**: 7

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
        n8["Send Production Update"]
        n9["Receive Shipping Information"]
    end
    subgraph SAP S/4 IF Sending Plant (EWM) 
        n10["Inbound Delivery Distribution to EWM"]
        n11["Create and Confirm Put-away Warehouse task (EWM)​"]
        n12["Goods Receipt EWM​"]
        n13["Outbound Delivery Order (EWM)"]
        n14["Pick and Pack Updates (EWM Managed)"]
        n15["Goods Issue and Update Inventory"]
        n16["PGI"]
        n21["fa:fa-user Ad hoc Move from Dock Storage type to FG storage type"]
        n31(["fa:fa-stop endEvent"])
    end
    subgraph SAP S/4 IF​ Receiving Plant (EWM)
        n17["Inbound Delivery distribution to EWM"]
        n18["Goods Receipt EWM"]
        n19["Create and Confirm Put-away Warehouse task (EWM)"]
        n20["Create Ad-hoc task for movement from EWM location (SLOC2) to factory (SLOC1)"]
    end
    subgraph SAP S/4 Intel Foundry  Sending Plant (IM)  
        n2["311 / Inbound Delivery Creation SLOC 2​"]
        n3["Ship to Customer (Sales Order)"]
        n4["311 is posted in S4 from SLOC1 to SLOC2"]
        n5["Create STR"]
        n6["Convert STR to STO"]
        n7["CI and BIlling Document"]
        n23[["fa:fa-cog Complete Production"]]
        n24[["fa:fa-cog GR Production Order at SLoc 1"]]
        n25[["fa:fa-cog Ship to Next Factory (STO)"]]
        n26[["fa:fa-cog Perform Outbound Delivery"]]
        n27[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n29(["fa:fa-stop GR Posted"])
        n30(["fa:fa-stop endEvent"])
        n32["E2E- 71F – Intel Foundry - Shipment of goods through Stock transfer – TM Steps"]
        n33{{"fa:fa-code-branch If Customer requires later?"}}
        n34{{"fa:fa-code-branch Customer or Next Factory?"}}
        n35{{"fa:fa-code-branch exclusiveGateway"}}
        n36{{"fa:fa-code-branch exclusiveGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
        n39{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph SAP S/4 Intel Foundry Receiving Plant (IM)
        n1["Stock Posted in Manufacturing locations"]
        n22[["fa:fa-cog Perform Inbound Delivery (S/4)"]]
        n28(["fa:fa-stop Stock Posted"])
    end
    n23 --> n24
    n25 --> n35
    n24 --> n29
    n10 --> n12
    n12 --> n11
    n4 --> n37
    n11 --> n4
    n34 -->|"Customer"| n39
    n34 -->|"Factory"| n36
    n38 --> n27
    n26 --> n38
    n35 --> n26
    n3 --> n35
    n13 --> n14
    n14 --> n15
    n15 --> n16
    n16 --> n22
    n22 --> n17
    n17 --> n18
    n18 --> n19
    n19 --> n20
    n1 --> n28
    n5 --> n6
    n2 --> n10
    n6 --> n36
    n38 --> n13
    n37 --> n33
    n37 --> n34
    n33 -->|"No"| n39
    n39 --> n3
    n20 --> n1
    n36 -->|"Next Factory
 location"| n25
    n33 -->|"Yes"| n21
    n21 --> n31
    n38 --> n7
    n7 --> n30
    n27 --> n32
    class n21 userTask
    class n22 serviceTask
    class n23 serviceTask
    class n24 serviceTask
    class n25 serviceTask
    class n26 serviceTask
    class n27 serviceTask
    class n28 endEvt
    class n29 endEvt
    class n30 endEvt
    class n31 endEvt
    class n32 startEvt
    class n33 gateway
    class n34 gateway
    class n35 gateway
    class n36 gateway
    class n37 gateway
    class n38 gateway
    class n39 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWFtv4jgU_itWRhWtBJo4FwI87IoCqZDaKSqdHa2m-2ASB6KGmHWSXrbDf99jxw4kBM1qtg9V-Xy-c_nO8QnphxGwkBoj4-LiI07jfIQ-OvmGbmlnhDorktFOF5XAH4THZJXQrCNsIpbmy_gfaYad3ZswE5hPtnHyLtAlXTOKvs67aAzEpIsykma9jPI46nQ7Ox5vCX-fsIRxYf2JDiIzktHU0TXjIeUHA9P0cOACNYlTeoBtz_EcX_AyGrA0rDmN3GgQBZ29SC5hr8GG8FymX2T0jrx9i8N8A58jkmQUbDb5NrklK5qIGnNeCCwo-IsWI85EnBQEW-5IEKdrwB0TIE7S5wPkmvs92l9cPKVVUHT78JQi-AkSkmVTGqEsB3j2kqMoTpLRJ2cy9l2zm-WcPdPRJ2vmTW2rG4hKRlC62RXi9l5pvN7koxVLQmXaexU1jKzdW5e_jSyzy9_hdyMWTcNDpEnfGliDKtK1hyd4oiNFUfS_IoGu_JFkzyrWzPYtf1rFwm7fnZin_nSZU8cb46ZOlL_EAT1y6vu-PTtINeu72Dzv9Nq3--ak4XRNcvpK3g8OhxOncui7no-9sw7LeM0si9WCs0A7tGeu71YOvWvsj62zDp0xdgYqQ_Cz5mS3QdeskLOMxrtdVp6Jn3Tw_clYQj8RhAuLII9Zir7uQqjnyfjryG4Idg80oPELRctNvNvBaKJ5GjG-JYJUWYOvRujleIGWnx0095GIJIiLhKQ5upx9u7tCR0GwCVHm6UrkiqY0gWCQ8TSGSuNVIXPLGQJWPTeMgTbhFJJGBJgTlkYx36JFkfeIaMs3wumGwSyhXLRdxn0qLNNcNRxZ4OiGsTBDstZdLoO1WdpgeV_kjVTvxYpR_uv2Dtgv4uBZJrgg8Eepciat0R1JyZqGTZZb5TPPsqKsruSB9i80zRl_b1D6ItDNvI5aQqGIjCLSEzcKjUO0gem6Y9DNiLMtmjLIaAnuIAuUv--oENq_ga1ygOoubXxZ-QSrXbkUICUwu_r5KJSiljK_NEbiuByvbSLCn07EoLWRdZvhr0xNXVbz4GIc9oSk0hRuBdqCtluQo9RX9Dhhgbwq6HJ5ez-xrkTmEQlED0sIX_2XW5TmNEG-EAR4zRs1hwt1fKPEQNsYo8_oRESZt0hHhEZW25SLIReXXWQ6KaDLWzHdSwIP7XLUG3o4KlqcoR3LchqiGNw7pQSyQuFJVl8nugcdl48P9TMx0NAbyDkXh9LD433dRkzJZC7beD1PEiEITHSxLcfxWA_7ezW1AVtD07e7hELYw_oDQo3h1Bk3D8ersrzwBDK7hebjJtetc7WWX-hbjvyq9Y_3V01iv05cUC42LTrZOE2e1yiv1NTn8umLvsIXMimSBmT6TR_DxsUWFctuHm52OR3mTzdAaSeGcGbNesjDPhJzhu3GGPekNPK6MHiayoubbzgr1huxlWA35fCVKItAa8V_vIMDCo-y-sDaHx-H-kPaWwEt2KB5dJhfTv8uYg4TnIA0_PcnY78_9uC0e6jocLWP23fCd9v59C1Iigx6dlN-VWjS-r9G8w40wjl7zXokydGOcJIkNDlDGvwKadhKitNz-f3XDXbyBJjXHwBiBckJWFQbBR6WhVicBRc0vVYbo2BZ7VfoZA9eQk4n92_QGO3jFFoecLBXUK_3m9gWGnBLwHY14CiLoQKwWQLY0oClAPWVNVUM29MGuAR0DFsa_IDVp4bzyfghOtU8VqNanvb16UDlo71bfRVuoC1UCVZFaZSEFYB1QlhljCsL5QJrF1gFsXTRli66KtJTgE4Dq0RxJdxQ-TA1oD5rhgqqY-oI2lzX2VQC2xpQKdgnQKW8raT9whqaq9w009JN1ud9TTzaIXCmh1h6s9xmmD9pVp5oP5aq2caNIrSMOmNdtKUB6-hNQ_rRr1h13Dp-Uaof2eePnPNH7vmj_vkj7_zRQL2G1tFhG2qbrShuRa3qVbqO2_otrw477bDbDvfbYa8dHrTDQw0bXQNu_ZbEoTH6MOR_VYyREdKIFElu7LsGKXK2fE8DYyT_-2AU8t1hGhPYyNsS3P8L7VFiHw==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-_71C_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_(IM_to_EWM) — E2E-_71C_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_(IM_to_EWM)

**Swim Lanes**: EWM · SAP S/4 Intel Foundry
 (IM)
 | **Tasks**: 10 | **Gateways**: 1

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
    subgraph EWM
        n8[["fa:fa-cog Perform Inbound Delivery distribution to EWM"]]
        n9[["fa:fa-cog Perform Goods Receipt EWM"]]
        n10[["fa:fa-cog Create and Confirm Put-away Warehouse task (EWM)"]]
        n12(["fa:fa-stop Shipment of Goods Comleted"])
    end
    subgraph SAP S/4 Intel Foundry  (IM) 
        n1[["fa:fa-cog Create Stock Transport Request"]]
        n2[["fa:fa-cog Create Outbound Delivery"]]
        n3[["fa:fa-cog Convert STR to STO"]]
        n4[["fa:fa-cog Perform Pick and Pack Updates (IM Managed)"]]
        n5[["fa:fa-cog Perform Goods Issue and Update Inventory"]]
        n6[["fa:fa-cog Perform Inbound Delivery"]]
        n7[["fa:fa-cog Freight Unit and Freight Order Creation"]]
        n11(["fa:fa-play Shipment of goods through Stock Initiated"])
        n13["E2E- 71F – Intel Foundry - Shipment of goods through Stock transfer – TM Steps"]
        n14{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n3
    n5 --> n6
    n3 --> n2
    n4 --> n5
    n14 --> n7
    n2 --> n14
    n10 --> n12
    n6 --> n8
    n8 --> n9
    n9 --> n10
    n14 --> n4
    n11 --> n1
    n7 --> n13
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 startEvt
    class n12 endEvt
    class n13 startEvt
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVttu6jgU_RUrVUUrBU2uhOZhJBrIUaVTFZV2-nB6HkzigFVjZ2ynLYP499km4ZbTzIw0eUDs21rbyzt2NlYmcmLF1uXlhnKqY7Tp6SVZkV6MenOsSM9GteMPLCmeM6J6JqcQXM_oX7s0Nyg_TZrxpXhF2dp4Z2QhCHq-s9EICpmNFOaqr4ikRc_ulZKusFwngglpsi_IsHCKHVsTuhUyJ_KY4DiRm4VQyignR7cfBVGQmjpFMsHzM9AiLIZF1tua5pj4yJZY6l37lSL3-POF5noJdoGZIpCz1Cv2Hc8JM2vUsjK-rJLvezGoMjwcBJuVOKN8Af7AAZfE_O3oCp3tFm0vL1_5gRR9f3zlCJ6MYaXGpEBKg3vyrlFBGYsvgmSUho6ttBRvJL7wJtHY9-zMrCSGpTu2Ebf_QehiqeO5YHmT2v8wa4i98tOWn7Hn2HINvy0uwvMjUzLwht7wwHQbuYmb7JmKovhfTKCrfMLqreGa-KmXjg9cbjgIE-dXvP0yx0E0cts6EflOM3ICmqapPzlKNRmErtMNepv6AydpgS6wJh94fQS8SYIDYBpGqRt1AtZ87S6r-VSKbA_oT8I0PABGt2468joBg5EbDJsOAWchcblEk5f72mMePvzx49UqcFzgfiYWaEpkIeQK3fG5qHiOxoTRdyLXKKdAQueVpoIjLXYo1s-fJ0g3XyN9EyJX6JFkhJb6izLXOa9LJAEJEQbyRPCCAsS00n1sRH3BkiwFTALSZtOuAO26DeddHeCUFiWaLWm5IlwjUTS9JGLFiCY5VF7XlTDFLZFmoyma_RaADpowlBotQAR0dXd_jU7Zvux9pkX2hp7g1VWlgDf0kfxZEaVbnXpf1j5U-lz5VpXfqhIckjSaPT2aXZk9PbTyg693ZUqhQ6PxFMOf5zIHbmWWh-4xxwuSt3UN_2l375Sq6i2rkUC2d5Bc_NL94L9NW6sqOq9K5e4EQc9wqexI944Hc6zXQsKUtgfDPQ5GyWCYTgdjsVuGXkpRLZbN_t0BPMVnc1ID-YAz8SZ9FLkpeq08x_Vbc9L_V3BthqOAbpv6p3sIkFIB1ylVsNnse8ZSig_Vx0yjEkvMGGHf6rPm1dpuW3PMXdTv_w7T0phhbQ4a069NrzGD2gz3tY0dNbZXm26wjzuNY18_qO1hYw5r86Yxb5pspwV_gGt6bY5nHjWmf3IQmgWdHNdnEa8z4ndGgs5I2BkZdEaizsiwM3LTGQF5O0Pu4XI_93vNRXzu9Tuyg_0tZdnWisgVprkVb6zdtxh8r-WkwBXT1ta2cKXFbM0zK959s1jV7vUeUwyn5Kp2bv8GgwMfKA==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E-_71D_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_IM) — E2E-_71D_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_IM)

**Swim Lanes**: EWM · SAP S/4 Intel Foundry
 (IM)
 | **Tasks**: 10 | **Gateways**: 1

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
    subgraph EWM
        n8[["fa:fa-cog Perform Outbound Delivery Order (EWM)"]]
        n9[["fa:fa-cog Create and Confirm Picking and Packing (EWM)"]]
        n10[["fa:fa-cog Issue Goods"]]
    end
    subgraph SAP S/4 Intel Foundry  (IM) 
        n1[["fa:fa-cog Create STR"]]
        n2[["fa:fa-cog Convert STR to STO"]]
        n3[["fa:fa-cog Create Outbound Delivery (IM)"]]
        n4[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n5[["fa:fa-cog Update Goods Issue in IM"]]
        n6[["fa:fa-cog Perform Inbound Delivery"]]
        n7[["fa:fa-cog Perform Goods Receipt at IM SLOC"]]
        n11(["fa:fa-play Shipment of goods through Stock transfer (EWM to IM Initiated"])
        n12(["fa:fa-stop Shipment of goods through Stock transfer (EWM to IM) Completed"])
        n13["E2E- 71F Shipment of goods through Stock transfer – TM Steps"]
        n14{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n2
    n5 --> n6
    n2 --> n3
    n14 --> n8
    n14 --> n4
    n11 --> n1
    n8 --> n9
    n9 --> n10
    n10 --> n5
    n6 --> n7
    n7 --> n12
    n4 --> n13
    n3 -->|"Supplying 
SLoc"| n14
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 startEvt
    class n12 endEvt
    class n13 startEvt
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqllltv4jgUgP-KlaqilYI2VwJ5WIkGMkJqVdS0Ow_DPJjEAQtjR45TyjL897Vz4ZIh0mqXB-DcvnN8bJ_koMUsQZqv3d8fMMXCB4eeWKMt6vmgt4Q56umgUvwFOYZLgvKe8kkZFRH-u3QznexLuSldCLeY7JU2QiuGwMdMB2MZSHSQQ5r3c8Rx2tN7GcdbyPcBI4wr7zs0TI20zFabnhhPED87GIZnxq4MJZiis9r2HM8JVVyOYkaTK2jqpsM07h1VcYTt4jXkoiy_yNEL_PqOE7GWcgpJjqTPWmzJM1wiotYoeKF0ccE_m2bgXOWhsmFRBmNMV1LvGFLFId2cVa5xPILj_f2CnpKC57cFBfITE5jnE5SCXEj19FOAFBPi3znBOHQNPRecbZB_Z029iW3psVqJL5du6Kq5_R3Cq7Xwl4wktWt_p9bgW9mXzr98y9D5Xn63ciGanDMFA2toDU-ZnjwzMIMmU5qm_yuT7Ct_h_mmzjW1QyucnHKZ7sANjN95zTInjjc2231C_BPH6AIahqE9PbdqOnBNoxv6FNoDI2hBV1CgHdyfgaPAOQFD1wtNrxNY5WtXWSznnMUN0J66oXsCek9mOLY6gc7YdIZ1hZKz4jBbg-n3l0qjPnT448dCS6Gfwn7MVmCOeMr4FrwWYskKmoAJIvgT8T14VXcGPMjox4X28-cFYnSNCDiSPQBQBgeMpljS5jjeyANc6uaw-n-LZBrXqFmeFwh8YyzJz57yyLVWFI3nIPrDATMqEAGhqlsWDB5mL4_gkn6zzuj9rVWF1fJjVDZAKEcgmPx5bfnbN7m_d1DV0wp1boaGvLwi4ENOzbJnjaLcgxbCvUZ8ZIlClD2r-4cpmL20oga3t31Gr2tuRXm3o6pkbyhGOJMFC5kORM-vQXt3zYdTeEbkHYnWONsiKgCT96ZkiDVnxUruqGDxRs5JOdfT-tSp3kvuTPYEyxUmEv54CbfO8Fyw7L_AH-VebzOCbtBtCZ9a0z7wzPDfoxeFZZg2eJftEChTZ_iS6RwOTcWQc7bL-5AIkEEOCUHkWzVIFtrx2Dr31AT9_p_ynNaiW4mDWrQq0W6cnUoetmSnkWtaPR3psBJHtTiqrUbjblQKt5YHlejVole7N7XVycymGlvJvxZaVGQZ2as5sKDRM4sX2i9V2sXsU8u8mNBXFqvTYndanE6L22kZdFq8Tsuw0zLqtMimdprM0_P8Wm_Vz95rrd3h7TQPJk3XtohvIU40_6CVr1_yFS1BKSyI0I66BgvBoj2NNb98TdGKcqBMMJSzdlspj_8Af4oXSQ==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 E2E-_71E–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_EWM) — E2E-_71E–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_EWM)

**Swim Lanes**: Receiving Warehouse (EWM)
 · SAP S/4 Intel Foundry
 (IM)
 · Supplying Warehouse (EWM | **Tasks**: 14 | **Gateways**: 5

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
    subgraph Receiving Warehouse (EWM) 
        n10[["fa:fa-cog Perform Inbound Delivery distribution to EWM"]]
        n11[["fa:fa-cog Perform Goods Receipt EWM"]]
        n12[["fa:fa-cog Create and Confirm Put-away Warehouse task (EWM)"]]
        n18(["fa:fa-stop Shipment of Goods Completed"])
    end
    subgraph SAP S/4 Intel Foundry  (IM) 
        n2[["fa:fa-cog Receive Information froM BY"]]
        n3[["fa:fa-cog Create STR"]]
        n4[["fa:fa-cog Create STO"]]
        n5[["fa:fa-cog Perform Outbound Delivery (IM)"]]
        n6[["fa:fa-cog Perform ATP Check"]]
        n7[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n8[["fa:fa-cog Perform Inbound Delivery"]]
        n9[["fa:fa-cog Receive In Transit Inventory"]]
        n15(["fa:fa-play Plant Transfer Process Initiated"])
        n16(["fa:fa-stop PO SO Model and Process to be followed"])
        n17(["fa:fa-stop ATP Check Completed"])
        n19["E2E- 71F Shipment of goods through Stock transfer – TM Steps"]
        n20{{"fa:fa-code-branch Type of Plant Transfer ?"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
        n23{{"fa:fa-arrows-alt parallelGateway"}}
        n24{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Supplying Warehouse (EWM
        n1["Create and Confirm Picking and Packing (EWM)"]
        n13[["fa:fa-cog Perform Outbound Delivery Order (EWM)"]]
        n14[["fa:fa-cog Issue Goods"]]
    end
    n15 --> n2
    n13 --> n1
    n1 --> n14
    n2 --> n20
    n20 -->|"Intra"| n3
    n3 --> n4
    n4 --> n22
    n22 --> n6
    n23 -->|"Supplying SLoc"| n13
    n14 --> n24
    n22 --> n21
    n24 --> n9
    n9 --> n8
    n10 --> n11
    n11 --> n12
    n20 -->|"Inter"| n16
    n8 -->|"Receiving SLoc"| n10
    n12 --> n18
    n21 --> n5
    n23 --> n7
    n5 --> n23
    n7 --> n19
    n6 --> n17
    n24 --> n21
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 startEvt
    class n16 endEvt
    class n17 endEvt
    class n18 endEvt
    class n19 startEvt
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV21v4jgQ_itWqoquBLq8EuDDnSglq0qtikr3qtOyH0zigFUTR47Tluvy32-cxATSRNq740NVz8zzjOfxeDAfRsgjYkyMy8sPmlA5QR89uSU70pug3hpnpNdHpeFPLCheM5L1VEzME7mkfxdhlpu-qzBlC_COsr2yLsmGE_Ttto-mAGR9lOEkG2RE0LjX76WC7rDYzzjjQkVfkFFsxkW2ynXNRUREHWCavhV6AGU0IbXZ8V3fDRQuIyFPojPS2ItHcdg7qM0x_hZusZDF9vOM3OP3ZxrJLaxjzDICMVu5Y3d4TZiqUYpc2cJcvGoxaKbyJCDYMsUhTTZgd00wCZy81CbPPBzQ4fJylRyTorvHVYLgEzKcZTckRpkE8_xVopgyNrlwZ9PAM_uZFPyFTC7suX_j2P1QVTKB0s2-EnfwRuhmKydrzqIqdPCmapjY6XtfvE9ssy_28LeRiyRRnWk2tEf26Jjp2rdm1kxniuP4f2UCXcUTzl6qXHMnsIObYy7LG3oz8zOfLvPG9adWUyciXmlITkiDIHDmtVTzoWeZ3aTXgTM0Zw3SDZbkDe9rwvHMPRIGnh9Yfidhma-5y3y9EDzUhM7cC7wjoX9tBVO7k9CdWu6o2iHwbAROt-iRhIS-Qj-hZyzIloOw6Gr-fP8FlYHqk1jm9-8rI8aTGA9CvkELImIudug2WfM8idANYfSViD2KKCSn61xSniDJERCtjB8_TqmsdqqvnEdZuZtUtuHsc9xMENAWYcg-40lMgWKRywFWateVSHWaRTlNutHVkS6TPEXLLU13JJGIx9VeZnyXMiJJBNAvJRT6uyHfcrpAy99cUEIShgKlBsiArm7PBWxsvhSdAErVjgu1YsHv0fVfjX06rVUvnx4bcW5H3EMjzmtX_yGXjZNUFTSww3bs9GmBZlsSvjTC_dYtBaK48OgbfAcUp6cND2oKNyhGv9Z2DdS4S2z0BPMzg7y3ySscNf-EtLy6K1IGnbRgGFqigMVEIHX1SJYBnkqKz1qjxA8bXbV4QMsHdA-DnBXFagK4GmuCYs5gbn9m8RssR4XberKEjAExt-cD5FvBWS9vil6WW8HzDbSr5MAidT2r3DYtBz3dg4OkGZCe9qz58VHrGJHBGmDhFj3tU6KYG9r8sTIOh1O41Q4n7yHLMziQr-VsbMLsGoaF4G_ZADOJUiwwY4R1gJz_AnL_Hajl8udpyvafZ-fpwcC5tI0qGr4oXNETuPxfj6lTtPOr17W4Pe2TrjEabrMsJ-WIqyOPtcEVQIPB76COXjvl2tLraulWa7sKN_XaVIafKwMmosAr4yfMsMpVMWmkWyF1JruiGuq1UzHVMi_veFhQWprT0ixug8XWG7ariHG1HpfLkSYwq4KOBeoK7ZaK1IRS6fUeR5Wr_hatt6gVsaodWTqlXWXwzgqFgVmt9QnoGv0KrysYVmu_UaF9-qRRJ3PypDnzOJ0et9PjdXqGnR6_0zPq9Iw7PXBSnS6r29Utg9Wtg9UtBFwQ_aQ-tw-r5--51W-1jlqt43ZmaMDqHXluttrNdrvZaTe72mz0jR2BxwiNjMmHUfwSg19rEYlxzqRx6Bs4l3y5T0JjUvxiMfI0AuQNxTAMd6Xx8A-Rz1OD" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 E2E-_71F_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_–_TM_Steps — E2E-_71F_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_–_TM_Steps

**Swim Lanes**: EWM · External Partners/ B2B
 · SAP S/4  | **Tasks**: 19 | **Gateways**: 5

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
    subgraph EWM
        n12[["fa:fa-cog Create Outbound delivery Order"]]
        n13[["fa:fa-cog Create Wave Release and Pick WH Task"]]
        n14[["fa:fa-cog Perform Picking WH Task Confirmation"]]
        n15[["fa:fa-cog Perform Packing (Shipping Label Printing) and Packing List"]]
        n16[["fa:fa-cog Create Outbound Delivery (OD) with HU details"]]
        n17[["fa:fa-cog Perform Loading"]]
        n18[["fa:fa-cog Perform Goods Issue (EWM)"]]
        n26{{"fa:fa-arrows-alt parallelGateway"}}
        n27{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph External Partners/ B2B 
        n19[["fa:fa-cog Perform Carrier Sevices"]]
    end
    subgraph SAP S/4 
        n1["Allocate Freight Costs to Delivery Items (CO/PA) or Material Valuation"]
        n2[["fa:fa-cog Ship (Goods Issue)"]]
        n3[["fa:fa-cog Perform Carrier Selection and Calculate Charges"]]
        n4[["fa:fa-cog Create Outbound delivery (S/4)"]]
        n5[["fa:fa-cog Create/ Update Freight Unit and Order"]]
        n6[["fa:fa-cog Send Loading Instructions to EWM"]]
        n7[["fa:fa-cog Perform Freight Order Execution and Status Updates post GI"]]
        n8[["fa:fa-cog Create/ Update Freight Settlement Document"]]
        n9[["fa:fa-cog Receive reconciled Carrier Invoice(s)"]]
        n10[["fa:fa-cog Post Accrual to Freight Expense Account(s)"]]
        n11[["fa:fa-cog Create Service PO/ Entry Sheet"]]
        n20(["fa:fa-play Shipment of goods through Stock transfer – TM Steps Initiated"])
        n21(["fa:fa-stop Accrual Freight Expense Completed"])
        n22(["fa:fa-stop Freight Freight Cost allocation completed"])
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-arrows-alt parallelGateway"}}
        n25{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n12 --> n13
    n14 --> n15
    n20 --> n4
    n17 --> n18
    n13 --> n14
    n15 --> n16
    n4 --> n24
    n24 --> n5
    n5 --> n3
    n16 --> n26
    n18 --> n2
    n2 --> n7
    n7 --> n8
    n9 --> n8
    n3 --> n25
    n25 --> n6
    n6 --> n27
    n26 --> n27
    n27 --> n17
    n11 --> n23
    n23 --> n10
    n23 --> n1
    n26 -->|"HU Details updated in S/4 
and trigger for
 shipment document generation"| n25
    n24 -->|"Replication of delivery from S/4 to EWM"| n12
    n8 --> n11
    n10 --> n21
    n1 --> n22
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 startEvt
    class n21 endEvt
    class n22 endEvt
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV21v4jgQ_itWVhVUAjUJCaF8OIkG2KvUqqhstx-W_eAmDlg1cWQ7fbku__3GweYlS-729vhQNY9nnpl5PB4nH07CU-IMnbOzD5pTNUQfLbUia9IaotYTlqTVQVvgKxYUPzEiW9om47ma078qMy8o3rSZxqZ4Tdm7RudkyQl6uO6gETiyDpI4l11JBM1anVYh6BqL95gzLrT1JzLI3KyKZpauuEiJ2Bu4buQlIbgympM93IuCKJhqP0kSnqdHpFmYDbKktdHJMf6arLBQVfqlJLf47ZGmagXPGWaSgM1KrdkNfiJM16hEqbGkFC9WDCp1nBwEmxc4ofkS8MAFSOD8eQ-F7maDNmdni3wXFN3cL3IEv4RhKcckQ1IBPHlRKKOMDT8F8Wgauh2pBH8mw0_-JBr3_E6iKxlC6W5Hi9t9JXS5UsMnzlJj2n3VNQz94q0j3oa-2xHv8LcWi-TpPlLc9wf-YBfpKvJiL7aRsiz7X5FAV_EFy2cTa9Kb-tPxLpYX9sPY_ZnPljkOopFX14mIF5qQA9LpdNqb7KWa9EPPbSa9mvb6blwjXWJFXvH7nvAyDnaE0zCaelEj4TZePcvyaSZ4Ygl7k3Aa7gijK2868hsJg5EXDEyGwLMUuFihyePtFtG_3PO_fVs4GR5muJvwJYoFgQrQXameeJmnKCWMvhDxju70mVk4378fOvdOOj_iF4LuCSNwyBEGkhlNntHjn0hLXacIjilmRGRcrCsX6HnrhWKeZ1SssaI8r1OEDRR4S9Ger2hR6P-qE4hmguYKHs-3uRmrGypVnbj_z9qMrTbtu_E5eqVqhf58AMUUpkzWuaLTSd5wnEL4uvXgtPVnzlOJrqUsCWrDRp7X_Pz-x4f1w0LwV9nFTKECC8wYYZ-3zblwNptDp-i_OcGZr7fUmyIixyAtTJ6cCHmBrvwrdFjQ5emCYghIiUBzoo_igWg_B5mPZmh-ERyxAueIMZ7obZmKarBAp0glkeL77blWZC1RO767mI3OERfoFuz1zYG-YlbaljpU5DhZ3T-ofaB9XfbevxXHSKKjVA0XY5aUTGccw_xeknqnBL94INsgRj2R8JTvBXoo0kOFHuA2rlI5daZrPT-HjbBNiq5zmDRlVUqlsB4lx94NXW4jVwGhXUhS7vSYK6xKaXKUqIDtQ5-va7yDXypsTpRi8EKRKzTmSan_qfHU2vCeJATUREJf8AllJN1t2nX-wqEl27KusefWatQJj5JElNBQIIpNZvJWkBwGICzBxqkTRN7JnZ5vryU0u7tAk1zBTs9XhNQL8d32zrlg-L1q0qpyDpdQ1apqJXi5hIOjOIxfBW8SMoPCFqXvej305RYWSAEdDd1AIXAKEc4PI3j7CFLxYldjvcCYrwtGThD4NQLreHhSEd6eX90NSRNRbz-g9Dtl9wlqSVaIvCWslLB_DXMt-J1hGP7mMISbFHW7f-hL0QKBAUID-O4WCKxBZAwGFugZYGcRGqBvAEPpWwPfADaEsd-l0Df21t8bGMD6bx8j82gSsvlcHj-a7PxdPSaaJbfBLJv_E2ALtoDnGQubsG8VcOvAEeePhQM37Xh706KymgIporm5IPRYUYIul9DuMH_AVdrTkZq5gJYELioz-38cFhWYAPekYNR0Jpyp3dzNBF9XcewA_KH33ngbeT2brme23N8B5tk_eM3T23DwMnq00mtcCRpXwsaVfuNK1LgyaFy5bFyBshuXvOalZhm8Zh28ZiG8ZiW8Zim8Zi28ZjG8ZjXg3NtvsmPcM99Px6h_Eu3ZT4tjODgNh6fh_mk4srDTcdYE3rJp6gw_nOrjHD7gU5Lhkiln03Fwqfj8PU-cYfUR62yP3phieEdbb8HN3ytNBXY=" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End, E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End,  | |
| SAP S/4 IF Sending Plant (EWM)  | E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End, E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End,  | |
| SAP S/4 IF​
Receiving Plant (EWM) | E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End, E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End,  | |
| SAP S/4 Intel Foundry

Sending Plant (IM) 
 | E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End, E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End,  | |
| SAP S/4 Intel Foundry
Receiving Plant (IM) | E2E-_71A_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Front_End, E2E-_71B_–_Intel_Foundry_–_Factory_Handover_(Prospal)_–_Back_End,  | |
| EWM | E2E-_71C_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_(IM_to_EWM), E2E-_71D_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_IM), E2E-_71F_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_–_TM_Steps | |
| SAP S/4 Intel Foundry
 (IM)
 | E2E-_71C_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_(IM_to_EWM), E2E-_71D_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_IM), E2E-_71E–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_EWM),  | |
| Receiving Warehouse (EWM)
 | E2E-_71E–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_EWM),  | |
| Supplying Warehouse (EWM | E2E-_71E–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_(EWM_to_EWM),  | |
| External Partners/ B2B
 | E2E-_71F_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_–_TM_Steps | |
| SAP S/4  | E2E-_71F_–_Intel_Foundry_-_Shipment_of_goods_through_Stock_transfer_–_TM_Steps | |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
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

    subgraph E2E71CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E71CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E71CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E71CDAA_e_g_XEUS -.-> E2E71CDAD_e_g_Azure_SQL
    end
    style E2E71CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E71CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E71CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E71CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E71CDAA_e_g_MES_300 -.-> E2E71CDAD_e_g_SAP_HANA
    end
    style E2E71CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E71CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E71CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9vmkAUx_-Vyy2GLdEOtehK0ianwNqENl2x25KykBMeeukJBI5Va_3fdwdqN6td07uEeO_H9z0-j5xLHKYRYBM3GkuWMGGipSamMAPNRNqYFqA1kVZAWOZMLFz4DVw5eJrWnir0O80ZHXMoNJUdp4nw2GMl0DayuQpTNofOGF8oqweTFNDtRRMRmci1lYrg6UM4pbmoNMoCLun8B4vEVJ5jyguQMVMx4y4dA1eFRF4qWyK79zIasmQijV1DmnKa3D-bjo3VCq0aDT_ZlkCjgZ8guUJOi8KCGNEsG6RzFDPOzQ8Dw3Icp1mIPL0H84Ou9_uD3vrYelA9mZ1s3gxTnubK3bWMXb1oPFzwtRwxrB7pb-U6dt_qdg7KtQeG3dF35CDlz-05zsAYGFu94VCX66Ber6fcflIrFuV4ktNsimzZRntokaEbQDAJyGOZQ-B9c-98jHz8q45WK2I5hIKlyRaaWpt0UmX_tG89mQhHkyOkfksB0zRrpi9zrJ2KH33sl9GXbiSfUXjslzHo8pWVWBWEZJCPPynJCutrXaDWUevsUKU6EZJozUIsOBwEsYFN1N7CtnW1_4Xdzub_w-uR6-CcXJF30b20vaCr6xvA8ojk8S2Mt2VfQSxjkIp5C-F1J_sgb0q9hfEm9l2I95dFp6dnT2tAVsUUfUbk-kI-HcbBx0-HP4qd0bkwke3f_UUsjHRkkRFB5GZ4fjGyh6PbGxu59lf7yjowTffm2eoGau4kyzgLqfLuH50bWAfmZFFB1U28f0RuYEt5O4laadxyWQy1fH1l7B1H_YYb-obaW_onJycv0OMmnkE-oyzC5hJXN778v4ggpiUXeNXEtBSpt0hCbFaXMi6ziAqwGJVEZ7Vx9QfJUPVP" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E71FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E71FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E71FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E71FDAA_e_g_XEUS -.-> E2E71FDAD_e_g_Azure_SQL
    end
    style E2E71FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E71FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E71FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E71FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E71FDAA_e_g_MES_300 -.-> E2E71FDAD_e_g_SAP_HANA
    end
    style E2E71FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E71FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E71FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9vmkAUx_-Vyy3GLdEOtehK0ianwNqENl2x25KykBMeeukJBI5Va_3fdwdKN6td07uEeO_H9z0-j5wrHCQhYAM3GisWM2GgVVPMYA5NAzUnNIdmCzVzCIqMiaUDv4ErB0-SylOGfqcZoxMOeVNlR0ksXPZYCnT0dKHClM2mc8aXyurCNAF0e9FCRCby5lpF8OQhmNFMlBpFDpd08YOFYibPEeU5yJiZmHOHToCrQiIrlC2W3bspDVg8lcaeLk0Zje-fTcf6eo3WjYYX1yXQeOjFSK6A0zw3IUI0TYfJAkWMc-PDUDdt227lIkvuwfigaYPBsL85th9UT0Y3XbSChCeZcvdMfVcvnIyWfCNHdLNPBrVc1xqYve5Buc5Qt7rajhwk_Lk92x7qQ73WG400uQ7q9fvK7cWVYl5MphlNZ8iSbXRsk4wcH_ypTx6LDHz3m3PnYeThX1W0WiHLIBAsiWtoam3TSZn907p1ZSIcTY-Q-i0FDMOomL7MMXcqfvSwV4RfeqF8hsGxV0SgyVdWYmUQkkEe_qQkS6yvdYHaR-2zQ5WqRIjDDQux5HAQxBY2UbuGbWlq_wu7ky7-h9cl1_45uSLvontpuX5P07aA5RHJ41sY12VfQSxjkIp5C-FNJ_sgb0u9hfE29l2I95dFp6dnTxtAZskUfUbk-kI-bcbBw0-HP4qd0Tkwle3f_UUsCDVkkjFB5GZ0fjG2RuPbGws51lfryjwwTefm2er4au4kTTkLqPLuH53jmwfmZFJB1U28f0SOb0l5Kw7bSdR2WASVfHVl7B1H9YZb-rraNf2Tk5MX6HELzyGbUxZiY4XLG1_-X4QQ0YILvG5hWojEXcYBNspLGRdpSAWYjEqi88q4_gNFBPV5" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-71-R001 | Report | E2E-71 operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-71-C001 | Conversion | Legacy data migration for E2E-71 | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-71.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E71C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E71C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E71CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E71CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E71C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E71CMW_e_g_Azure_Service_Bus
    E2E71CMW_e_g_Azure_Service_Bus --> E2E71C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTue474M_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPu6c9aQ==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-71.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E71F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E71F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E71FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E71FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E71F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E71FMW_e_g_Azure_Service_Bus
    E2E71FMW_e_g_Azure_Service_Bus --> E2E71F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1P4kAQ_iubGsIX0KLyYmNIWlsuXIoa68tdjkuzdKewcWmb7lZF5L_fbosUiwZvSUo688wz22dmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OCVid5UTBlG-A5ZQtl9WAaA7obNpApA1kDcRzxJoeUhvWVQrP4OZjhVOR8GYcRfnmgRMzke4gZB4mZiTlz8QSYSirSTNki-SVeggMaTaXxVJemFEePpamtr1ZoVauNo00KdGuNIyRXrYaaTbmhYEZHWECTRjyhKRDExYIBChjmHLjEFPD83YYQTTJOI-Ac5SukjBkHA7msdoOLNH4E48Dq9Tq6tX5tPqsvMY6Tl0YQszg1DnRdr3DiJEHlKjittmLdcOp6t2t1_oOTYIF3Oe3eHs7WB853H8FcipfihdQUtSuZ5pQQBs84hW1F7I5ZKuJ0O4OS7Ru7h5jtKKI03lL54kLX93EWrDybTFOczJDp_hlr44z0Toh8kpM2Mq-v3eGFeTu8ukSu-du5GWt_iyC1iGyIQNA4Qu5NaXWOnW5r4IM_9UeO55_o-jZrAB0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHr2t1C6YchdYoJFEFbVm1Krvt5OwXMRe-w-S8R6K_vcXgtCBWALQGnE_So_457RcO7x4doaEdB_Lvp3d1eX5E-0VW1ZVFPojIe312BZVj138bazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPO6QUwkkzThsujRcp5Hzv9UmpaiFKO_CttVvI-zZ2dnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPAic9gQ==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
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

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-71-I001 | Interface | E2E-71 inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-71-E001 | Enhancement | E2E-71 custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-71-F001 | Form/Report | E2E-71 operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
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

    subgraph E2E71CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E71CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E71CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E71CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E71CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E71CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E71CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E71CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhCRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1tslZKpWrzB4t77_z49Vl4j1OeAXbwYLCnBRUO2mtiDRvQHKQtSQ2ajrQa0qaiYjeHO2AqwTjvM13pd1JRsmRQa2p1zgsR0YcOMByVW1WmtJBsKNspNYIVB3RzpSNXLmRaqyoYv0_XpBIdo6nhmmx_0EysZZwTVoOsWYsNm5MlMLWRqBqlFdJ9VJKUFispjgwpVaS4PUq20baoHQzi4rAF-ubFBZIjZaSuZ5AjUpYe36KcMuacefYsDEO9FhW_BefMMCYTb_wUfrhXnhyz3OopZ7xSaWtmv-aVjIgj0J8GY__jAWhNp4HlvwRaR-DQswPTeAUEzo68MPRszz7wfN-Q46TB8Vil46In1s1yVZFyjQIzmAz9xXyRQLJK3IemgmRBSPQrxnFjjo1h3ORgyJ3PV-eoSyOVjvHvHqRGRitIBeUFmn89qs9ktyP_DG4Us8OobwlwHKdveL8GiuzJm9gxOGnsn5r55uGjZJR8dr-4iWmYVnf-bGplcs6I_XcXoosRUnVI1b27EddBlFiG8dwLGSIZvrMdL6z-h468Rb-8_PT4ZHbWnQ9dIHdxJeeQMojx48mrwjreQLUhNMPOHndvhHxhMshJwwRudUwawaNdkWKn-41xU2ZEwIwSeT2bXmz_AHnoblo=" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E71FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E71FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E71FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E71FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E71FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E71FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E71FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E71FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhCRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1tslZKpWrzB4t77_z49Vl4jxOeAnbwYLCnBRUO2mtiAzloDtJWpAZNR1oNSVNRsVvAHTCVYJz3ma70O6koWTGoNbU644UI6UMHGI7KrSpTWkByynZKDWHNAd1c6ciVC5nWqgrG75MNqUTHaGq4JtsfNBUbGWeE1SBrNiJnC7ICpjYSVaO0QroPS5LQYi3FkSGlihS3R8k22ha1g0FUHLZA37yoQHIkjNT1HDJEytLjW5RRxpwzz54HQaDXouK34JwZxmTijZ_CD_fKk2OWWz3hjFcqbc3t17ySEXEEzqb-ePbxALSmU9-avQRaR-DQs33TeAUEzo68IPBszz7wZjNDjpMGx2OVjoqeWDerdUXKDfJNfzIMlotlDPE6dh-aCuIlIeGvCEeNOTaGUZOBIXc-X5-jLo1UOsK_e5AaKa0gEZQXaPH1qD6T3Y78079RzA6jviXAcZy-4f0aKNInb2LH4KSxf2rmm4cP41H82f3ixqZhWt3506mVyjkl9t9dCC9GSNUhVffuRlz7YWwZxnMvZIhk-M52vLD6HzryFv3y8tPjk9l5dz50gdzllZwDyiDCjyevCus4hyonNMXOHndvhHxhUshIwwRudUwawcNdkWCn-41xU6ZEwJwSeT15L7Z_AJy5bnI=" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
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

<div class="page-footer"><span>Page 27</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-71 — E2E-71</span></div>
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
*E2E-71 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

