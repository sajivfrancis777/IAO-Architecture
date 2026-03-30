<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-45 — E2E-45</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-45 · Forecast to Stock</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-45 E2E-45** within the IAO program. It includes 5 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Forecast to Stock |
| **Capability** | E2E-45 - E2E-45 |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Forecast to Stock |
| **L2 Capability** | E2E-45 - E2E-45 |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-45 Process Migration | Migrate E2E-45 business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-45 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **5 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-45 E2E-45.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-_45A-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Raw_Materials_&am | E2E-_45A-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Raw_Materials_&am | SAP S/4 Intel Foundry
Receiving Plant  (IM)
, SAP S/4 Intel Foundry
Supplying Plant  (IM)
 | 10 | 1 |
| 2 | E2E-_45B-IF_-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_u | E2E-_45B-IF_-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_u | EWM, SAP S/4 Intel Foundry
 Supplying Plant (IM)
 | 10 | 1 |
| 3 | E2E-_45C-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us | E2E-_45C-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us | EWM, SAP S/4 Intel Foundry
 (IM)
 | 10 | 1 |
| 4 | E2E-_45D-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us | E2E-_45D-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us | Receiving Warehouse (EWM)
, SAP S/4 Intel Foundry
 Production Plant (IM)
, Supplying Warehouse (EWM | 14 | 5 |
| 5 | E2E-_45E-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_and | E2E-_45E-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_and | EWM, External Partners/ B2B
, SAP S/4  | 19 | 6 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-_45A-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Raw_Materials_&am — E2E-_45A-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Raw_Materials_&am

**Swim Lanes**: SAP S/4 Intel Foundry
Receiving Plant  (IM)
 · SAP S/4 Intel Foundry
Supplying Plant  (IM)
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
    subgraph SAP S/4 Intel Foundry Receiving Plant  (IM) 
        n7["Perform Inbound Delivery (S/4)"]
        n8["Perform Goods Receipt"]
        n9["fa:fa-user Create STR"]
        n10[["fa:fa-cog Convert STR To STO"]]
        n11(["fa:fa-play Shipment of goods through Stock transfer Initiated"])
        n12(["fa:fa-stop Goods Received"])
    end
    subgraph SAP S/4 Intel Foundry Supplying Plant  (IM) 
        n1["Perform Outbound Delivery"]
        n2["Perform Goods Issue and Update Inventory"]
        n3["Perform Pick and Pack Updates (IM Managed)"]
        n4["Perform Commercial Invoicing"]
        n5["Perform Post Good Issue"]
        n6["Create Freight Unit and Freight Order"]
        n13["TM Steps"]
        n14{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n2 --> n3
    n4 --> n5
    n7 --> n8
    n9 --> n10
    n11 --> n9
    n3 --> n4
    n10 --> n1
    n1 --> n14
    n14 --> n6
    n14 --> n2
    n5 --> n7
    n8 --> n12
    n6 --> n13
    class n9 userTask
    class n10 serviceTask
    class n11 startEvt
    class n12 endEvt
    class n13 startEvt
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl1v4jgU_StWqopWCtokJITmYSUayAhpqqLS7j5M98EkDlh14sh2oCziv-91PiBh1NFIywNwrs_9OrZvcjRinhAjMG5vjzSnKkDHgdqSjAwCNFhjSQYmqg1_YUHxmhE50JyU52pF_61otlt8apq2RTij7KCtK7LhBL0tTDQFR2YiiXM5lETQdGAOCkEzLA4hZ1xo9g2ZpFZaZWuWHrlIiLgQLMu3Yw9cGc3JxTzyXd-NtJ8kMc-TXtDUSydpPDjp4hjfx1ssVFV-KckT_vybJmoLOMVMEuBsVca-4zVhukclSm2LS7FrxaBS58lBsFWBY5pvwO5aYBI4_7iYPOt0Qqfb2_f8nBR9f3nPEXxihqWckRRJBeb5TqGUMhbcuOE08ixTKsE_SHDjzP3ZyDFj3UkArVumFne4J3SzVcGas6ShDve6h8ApPk3xGTiWKQ7wfZWL5MklUzh2Js7knOnRt0M7bDOlafq_MoGu4hXLjybXfBQ50eycy_bGXmj9HK9tc-b6U_taJyJ2NCadoFEUjeYXqeZjz7a-DvoYjcZWeBV0gxXZ48Ml4EPongNGnh_Z_pcB63zXVZbrpeBxG3A09yLvHNB_tKOp82VAd2q7k6ZCiLMRuNii1XSJVn-4aJErwlDEyzwRB_RCYkJ3cMrQkuFcIXS3eLpHtav-5P6Pd2NJRMpFBq5r7YZmhNEdAe87CHj_bvzT4U86_G-cJ7JOUag-7QFoKQ5SPNQbjEJBQEC0en3p02zrx5kY8w0KeQ6JlSaiVw4_z8DvOdh3Z4eCwYastrTICHTGYZOqetRW8HIDgigef8ClhCGSQgkLmFUUikgg4n03onOJKBUvul3tumy4E78l-aosCnb4heR2R8LnUvU17-vj_KT2QsqSIAweb0WiNV2AYrni156jjueSghDaZYnhT-0ndVnoCed4Q5KrPXY7viHPMiJimMc6E6d6YvXZXjcTl6oqtK6zTxwDsTkIkaimBXqDTakqaw3PeoRfnRHdyusT7Ccp5NWSezy2e4eF4Hs5xEyhAgvMGGHf6kv7bpxOV1uYO2g4_BNUaqBbQ6-Bfg0nDXyood3cYTiEteGhwaMauu2y1fBb3MDzepNtfIWdBns19Bs4adzb5XGDR52JomtsJ2nPDLV05mF_yT4_Uvp2pxn_fevoC7bbzkbDNOCkZJgmRnA0qjcAeEtISIpLpoyTaeBS8dUhj42gelIaZXUQZxTDbcpq4-k_UNqZBw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-_45B-IF_-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_u — E2E-_45B-IF_-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_u

**Swim Lanes**: EWM · SAP S/4 Intel Foundry
 Supplying Plant (IM)
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
    subgraph SAP S/4 Intel Foundry  Supplying Plant (IM) 
        n1[["fa:fa-cog Create Stock Transport Request"]]
        n2[["fa:fa-cog Convert STR to STO"]]
        n3[["fa:fa-cog Create Outbound Delivery"]]
        n4[["fa:fa-cog Perform Pick and Pack Updates (IM Managed)"]]
        n5[["fa:fa-cog Perform Inbound Delivery"]]
        n6[["fa:fa-cog Perform Goods Issue and Update Inventory"]]
        n7[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n11(["fa:fa-play Shipment of goods through Stock Initiated"])
        n13["E2E- 45E"]
        n14{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n2
    n6 --> n5
    n2 --> n3
    n4 --> n6
    n14 --> n7
    n3 --> n14
    n10 --> n12
    n5 --> n8
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVltv4jgU_itWqopWCtpcCeRhJRrIqNJURU27fZjOg0kcsGrsrO1AGcR_XzsJtwxZrbQ8VD237zvn84mTnZGyDBmhcXu7wxTLEOx6colWqBeC3hwK1DNB7fgLcgznBImezskZlQn-VaXZXvGl07QvhitMttqboAVD4O3RBGNVSEwgIBV9gTjOe2av4HgF-TZihHGdfYOGuZVXbE3ogfEM8VOCZQV26qtSgik6ud3AC7xY1wmUMppdgOZ-PszT3l43R9gmXUIuq_ZLgZ7g1zvO5FLZOSQCqZylXJHvcI6InlHyUvvSkq8PYmCheagSLClgiulC-T1LuTiknyeXb-33YH97-0GPpOD7ywcF6pcSKMQE5UBI5Z6uJcgxIeGNF41j3zKF5OwThTfONJi4jpnqSUI1umVqcfsbhBdLGc4ZyZrU_kbPEDrFl8m_Qscy-Vb9bXEhmp2YooEzdIZHpofAjuzowJTn-f9iUrryVyg-G66pGzvx5Mhl-wM_sn7HO4w58YKx3dYJ8TVO0RloHMfu9CTVdODbVjfoQ-wOrKgFuoASbeD2BDiKvCNg7AexHXQC1nztLsv5jLP0AOhO_dg_AgYPdjx2OgG9se0Nmw4VzoLDYgmm70-1R__o8MePDyOHYQ77KVuAGeI54yvwSOespBmYIILXiG9BhhUJnpcSMwokq1CMnz_PkEbXkb4xlgnwglKEC3mlzLYu6yKOlIQAKvKI0RwriFkp-1CL-g45WjK1CUDqQ7tTaPdtOOfuCCckK0CyxMUKUQlY3vQSsRVBEmWq8r6uVFvcEikZz0Dyh6d0kIiAWGuhRABJWRRkq55FMCNQYd49Pt2Dc_arsySSpZ_gVT3KomDqiX1Bf5dIyFbnTquWUSW8BMnri9Y7eX1u5btXuZ5LeXlyrSrv-inNsOpQaz6D6p-3IlNYQo8HniCFC5S1dfb_2960qgb_tiOPQpT1wdf8CmytDo79hhJcnTzm1cUC3tS7pkI5OJ71bd9eE_u0JgVRq3W-JouqHbnkrFwsm9N7VKgYXmxNDeQqnKkz7QPPn6rYecjb7Q4ckHO2EX1IJCggh4Qg8q2-KT6M_b61hdQG_f6faiMac1CbfmM6tek2plebg0NtYweN7dam7R3iVuM4oPu1PWzMYW2OGnPUZFst-CNc02tzudKgMd2za0wPdHbZXkSczojbGfE6I35nZNAZCTojw87IqDOi5O0M2cdX86XfaV6jl163I9s7vGMM01ghvoI4M8KdUX1Jqa-tDOWwJNLYmwYsJUu2NDXC6ovDKKvHaoKhuuNWtXP_D2jKCSA=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-_45C-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us — E2E-_45C-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us

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
        n8["Perform Outbound Delivery Order (EWM)"]
        n9["Create and Confirm Picking and Packing (EWM)"]
        n10["Issue Goods"]
    end
    subgraph SAP S/4 Intel Foundry  (IM) 
        n1["Create STR"]
        n2["Convert STR to STO"]
        n3["Create Outbound Delivery (IM)"]
        n4["Create Freight Unit and Freight Order"]
        n5["Update Goods Issue in IM"]
        n6["Perform Inbound Delivery"]
        n7["Perform Goods Receipt at IM SLOC"]
        n11(["fa:fa-play Shipment of goods through Stock transfer Semi Finished using STO (EWM to IM)"])
        n12(["fa:fa-stop Shipment of goods through Stock transfer Semi Finished using STO (EWM to IM)"])
        n13["TM Steps"]
        n14{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n2
    n5 --> n6
    n14 --> n8
    n14 --> n4
    n3 -->|"Supplying 
SLoc"| n14
    n8 --> n9
    n9 --> n10
    n10 --> n5
    n6 --> n7
    n7 --> n12
    n11 --> n1
    n2 --> n3
    n4 --> n13
    class n11 startEvt
    class n12 endEvt
    class n13 startEvt
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq1Vttu6jgU_RUrRxWtFDS5EpqHkWggR0itWjXtnIdhHkzigFVjR7bTluHw77OdC7czfRpNHoC9vdbaF2877KxcFMSKraurHeVUx2g30GuyIYMYDZZYkYGNWscfWFK8ZEQNDKYUXGf07wbmBtWngRlfijeUbY03IytB0OvcRhMgMhspzNVQEUnLgT2oJN1guU0EE9Kgv5Fx6ZRNtG7pTsiCyCPAcSI3D4HKKCdHtx8FUZAaniK54MWZaBmW4zIf7E1yTHzkayx1k36tyAP-_EELvQa7xEwRwKz1ht3jJWGmRi1r48tr-d43gyoTh0PDsgrnlK_AHzjgkpi_HV2hs9-j_dXVgh-CovvnBUfw5AwrNSUlUhrcs3eNSspY_C1IJmno2EpL8Ubib94smvqenZtKYijdsU1zhx-ErtY6XgpWdNDhh6kh9qpPW37GnmPLLXxexCK8OEZKRt7YGx8i3UVu4iZ9pLIs_1Mk6Kt8weqtizXzUy-dHmK54ShMnF_1-jKnQTRxL_tE5DvNyYlomqb-7Niq2Sh0na9F71J_5CQXoiusyQfeHgVvk-AgmIZR6kZfCrbxLrOsl09S5L2gPwvT8CAY3bnpxPtSMJi4wbjLEHRWEldrNPvx0HrMw8d_LqwnIkshN-ix1ktR8wJNCaPvRG7Rozko6BooNwvrrxPaLdASSaBYhIGQCF5SUHii-RtMauN7wu3vf2G7DtDnStUEfReiUIdVGKeLbLPJE8p-C9Cca8JQatKDvND1_OEGnSoe88lens-jeWZNcChIm0WkBXw9nmP8I__XLphg5_DgCE9lM8_oFa64pu7e0fTunBYC7bUqDK2pG7U9oBzNH86Ro5NtmfPzfM6R0QmyFX0mOaEVJKNBFmX3j8lF991r4JQ4LvGwYjCr2ZpWG8I1EjC_jYReS1GvoPta5G9wX8H9WsIgZGRDUQqXuVqTAk6k2V5oZbPFpq1tn25OY3nHWEqL6n-NZTbxBSrWpFIXJQe7XZ8GllJ8qCFmGlVYYsYI-94e2oW131_MIXfRcPg7zFBnhq056leD1h5f2EFn-8b8ubCyuqrY1pSw4Nm9yBfWTwPuUOOWdNuZt63pOr2o0zrCzh61ZtSZUQfvU3S7lLvrjnut6Xdml6Hrn9wzDal_bZz7ve6KP_f6X6CD_v6zbGtD5AbTwop3VvOWh38CBSlxzbS1ty1ca5FteW7FzdvQqptjMaUYjv2mde7_AXxIjXQ=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E-_45D-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us — E2E-_45D-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us

**Swim Lanes**: Receiving Warehouse (EWM)
 · SAP S/4 Intel Foundry
 Production Plant (IM)
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
        n9[["fa:fa-cog Perform Inbound Delivery distribution to EWM"]]
        n10[["fa:fa-cog Perform Goods Receipt EWM"]]
        n11[["fa:fa-cog Create and Confirm Put-away Warehouse task (EWM)"]]
        n18(["fa:fa-stop Shipment of Goods Completed"])
    end
    subgraph SAP S/4 Intel Foundry  Production Plant (IM) 
        n1[["fa:fa-cog Receive Information froM BY"]]
        n2[["fa:fa-cog Create STO"]]
        n3[["fa:fa-cog Receive ATP Check Updates"]]
        n4[["fa:fa-cog Perform Outbound Delivery (IM)"]]
        n5[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n6[["fa:fa-cog Create STR"]]
        n7[["fa:fa-cog Receive In Transit Inventory"]]
        n8[["fa:fa-cog Perform Inbound Delivery"]]
        n15(["fa:fa-play Plant Transfer Process Initiated"])
        n16(["fa:fa-stop PO SO Model and Process to be followed"])
        n17(["fa:fa-stop ATP check completed"])
        n19["TM steps"]
        n20{{"fa:fa-code-branch Type of Plant Transfer ?"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
        n23{{"fa:fa-arrows-alt parallelGateway"}}
        n24{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Supplying Warehouse (EWM
        n12[["fa:fa-cog Perform Outbound Delivery Order (EWM)"]]
        n13[["fa:fa-cog Create and Confirm Picking and Packing (EWM)"]]
        n14[["fa:fa-cog Issue Goods"]]
    end
    n15 --> n1
    n12 --> n13
    n13 --> n14
    n1 --> n20
    n20 -->|"Intra"| n6
    n6 --> n2
    n2 --> n22
    n22 --> n3
    n23 -->|"Supplying SLoc"| n12
    n14 --> n24
    n22 --> n21
    n24 --> n7
    n7 --> n8
    n9 --> n10
    n10 --> n11
    n20 -->|"Inter"| n16
    n11 --> n18
    n21 --> n4
    n23 --> n5
    n4 --> n23
    n8 -->|"Receiving SLoc"| n9
    n24 --> n21
    n5 --> n19
    n3 --> n17
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV21v4jgQ_itWqoquBLq8EuDDnSglq0qtigq96rTsB5M4YNXEkePQsiz__cZ5IZAmur07PrT48cwznmfGk3DQfB4QbaRdXx9oROUIHTpyQ7akM0KdFU5Ip4ty4E8sKF4xknSUTcgjOac_MjPDjj-UmcI8vKVsr9A5WXOCXu67aAyOrIsSHCW9hAgadrqdWNAtFvsJZ1wo6ysyCPUwi1Zs3XIREFEZ6Lpr-A64MhqRCrZc27U95ZcQn0fBBWnohIPQ7xzV4Rh_9zdYyOz4aUIe8ccrDeQG1iFmCQGbjdyyB7wiTOUoRaowPxW7UgyaqDgRCDaPsU-jNeC2DpDA0VsFOfrxiI7X18voFBQ9PC8jBB-f4SS5IyFKJMDTnUQhZWx0ZU_GnqN3Eyn4GxldmVP3zjK7vspkBKnrXSVu753Q9UaOVpwFhWnvXeUwMuOPrvgYmXpX7OFvLRaJgirSpG8OzMEp0q1rTIxJGSkMw_8VCXQVC5y8FbGmlmd6d6dYhtN3JvpnvjLNO9sdG3WdiNhRn5yRep5nTSuppn3H0NtJbz2rr09qpGssyTveV4TDiX0i9BzXM9xWwjxe_ZTpaia4XxJaU8dzToTureGNzVZCe2zYg-KEwLMWON6gZ-ITuoN-Qq9YkA0HYdHN9PXxC8oN1Scafvu21EI8CnHP52s0IyLkYovuoxVPowDdEUZ3ROxRQCE2XaWS8ghJjoBnqX3_fsZk6M1UXzkPkvwwsWzyMy79JoKAtAhD9AmPQgoUs1T2sBK7SkSqYmbZ1OkGNye6RPIYzTc03pJIIh4WZ5nwbcyIJAG4fsldob1r6s3HMzT_zQYlJGHIU2qADAhKFKR-psKMYWC9ub8UtJZNXgQCNEoMnDmGgj-i279qBzcbZZgvnmp2VnOA8WKGJhviv6GXOADPpOZmN1fnKZW1SquEar5O49E8kV1w9AIzPytXCTypqVuj6Ldk91yzc9vkQwuYkAlEuo92UE0u9jXPwa91cr1dnKpdYgYtllc1CxYSoertkyQBGiopvuiZ3L9fa7fZE5o_oUcY8CwTpSSAO7MiKOQM5vlnFrfGoqrpZ9X0Pzdr7jIEj8UjPARIrGp93kn64VBJEZDeCrLxN2ixj4m6BbUU_1hqx-O5u9HsTj58liYg4td89NXdzMoNC8Hfkx5mEsVYYMYIa3Gy_ouT_e-cGi53Gsds_3k0nutr_uqFydq9eRZZ_zzaqP-mzpG1Cs6_N1LV7u99kqQkn2eV5SlRaGvU6_0O_8u1WaytErAKwC6BfF0-juGLAn4uNRiAAi-1n3CHi61-YVpaFsvTugDKUKZVMFWqzx-4n1EapZNhFyx2jcUsUzALC7dYu_lyUCyHRT7l-Q29AIyGhNR4UtHLjIwie6NkMwvAvsgBJmGxLk9b5jgouKtn7inFYe38p4TKEpUGZUXcsxcDVZez15eLHbN1x2rdsVt3nNadfuuO27ozaN0Ztu5AxVq32lUw2mUw2nUw2oWAq1O-WF_i_eIl-BJ1G9FBIzpsZobOLN4mL2GjGTabYasZtktY62pbAq8gNNBGBy37PQa_2QIS4pRJ7djVcCr5fB_52ij73aKl2XvEHcUwM7c5ePwbNE1W_w==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 E2E-_45E-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_and — E2E-_45E-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_and

**Swim Lanes**: EWM · External Partners/ B2B
 · SAP S/4  | **Tasks**: 19 | **Gateways**: 6

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
        n25{{"fa:fa-code-branch exclusiveGateway"}}
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
        n20(["fa:fa-play Shipment of goods through Stock transfer Initiated"])
        n21(["fa:fa-stop Accrual Posting to Freight account completed"])
        n22(["fa:fa-stop Freight Cost Allocated"])
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n26{{"fa:fa-arrows-alt parallelGateway"}}
        n28{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n12 --> n13
    n14 --> n15
    n20 --> n28
    n17 --> n18
    n13 --> n14
    n15 --> n16
    n4 --> n26
    n26 --> n5
    n5 --> n3
    n16 --> n27
    n18 --> n2
    n2 --> n7
    n7 --> n8
    n9 --> n8
    n3 --> n23
    n23 --> n6
    n6 --> n25
    n27 --> n25
    n25 --> n17
    n11 --> n24
    n24 --> n10
    n24 --> n1
    n26 -->|"Replication of delivery from S/4 to EWM"| n12
    n28 --> n4
    n27 --> n28
    n27 -->|"HU Details updated in S/4 
and trigger for
 shipment document generation"| n23
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
    class n28 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV21vozgQ_isWqyqplKhAIKT5cFKal91KXTVqrtsP2_3ggEmsOhjZpi_XzX-_MWCSULjb28uHqjyeeWbm8XgM71bII2KNrbOzd5pQNUbvHbUlO9IZo84aS9LpoQL4hgXFa0ZkR9vEPFEr-ldu5njpqzbT2ALvKHvT6IpsOEH31z00AUfWQxInsi-JoHGn10kF3WHxNuWMC239iYxiO86jlUtXXEREHAxsO3BCH1wZTcgBHgRe4C20nyQhT6IT0tiPR3HY2evkGH8Jt1ioPP1Mkq_49YFGagvPMWaSgM1W7dgNXhOma1Qi01iYiWcjBpU6TgKCrVIc0mQDuGcDJHDydIB8e79H-7Ozx6QKim7uHhMEv5BhKWckRlIBPH9WKKaMjT9508nCt3tSCf5Exp_ceTAbuL1QVzKG0u2eFrf_Quhmq8ZrzqLStP-iaxi76WtPvI5duyfe4G8tFkmiQ6Tp0B25oyrSVeBMnamJFMfx_4oEuoo_sXwqY80HC3cxq2I5_tCf2h_5TJkzL5g4dZ2IeKYhOSJdLBaD-UGq-dB37HbSq8VgaE9rpBusyAt-OxBeTr2KcOEHCydoJSzi1bPM1kvBQ0M4mPsLvyIMrpzFxG0l9CaONyozBJ6NwOkWzR--Foj-JY77_fujFeNxjPsh36CpIFABus3UmmdJhCLC6DMRb-hWn5lH68ePY-dBo_MDfibojjAChxxhIFnS8Ak9fEFa6jqFd0qxJCLmYpe7QM8bLzTlSUzFDivKkzqF30KBC4ruakvTVP-Xn0C0FDRR8Hhe5FZa3VCp6sTDf9ZmZrTp3s7O0QtVW_TlHhRTmDJZ5wqak7zhOILwdetRs_VnziOJrqXMCOrCRp7X_Fz__f3gF5H-GuZHuEXkNWSZhGQ_F-35aO33x27BwQ0LwV9kHzOFUiwwY4R9cIJTX2-qV0VEgkFcmD0JEfICXblX6Liky-aSphCQEoFWRB_GI9k-BllNlmh14Z2wAueEMR7qjVmIfLRAr0glkeKHDbpWZCdRd3p7sZycIy7QV7DXdwf6hllmmupYkdNkdQeh7pH6deEH_1YcI6GOkrfcFLMwYzrjKUzwDan3iveLR7ILYtQT8Zt8L9B9Gh0rdA_3cZ5K06mudf0KNsK0KbpOYNZkeSm5wnqYnHq39LmJnAeEdiFhVumxUlhlssxRohS2D32-rvGOfqmwFVGKwStFotCMh5n-p8ZTa8M7EhJQEwl9xYeUkajatOvkmUNLdmVdY8eu1agTnoShyKChQBSTzPw1JQmMQFiCjVMNRE7jTq-Kiwktby_QPFGw06stIfVCXLtbOacMv-VNmlfO4RrKW1VtBc82cHAUhwGsYBbIOC-MKgqBImA8P2Z0DoxS8bSqSReod_-oNlzUhEK-Sxlp4HJrXMeHE5kj-8Fr8Hvzy_s9t-F_G3uF06jRiSZtoao5Bnct6vf_0NemAbwS8EvAtQvAHRmLoLSogEEJeAbwS2BYAiWna57dYQGYGKV9lUO57AYGGJWA8S8ezXKZkMnn8vSxzM417G4JmGRMsKrgoA6Ycqp0nNLCFOwa0ew6cFLwz0frjqSMhvl012eimpux4Lv8IjED7KfeG-Ndlu_VMxydAEAPd_2suOtRlk-hCLqgvKD0WFOCbjZw3GD-gas0pzMq5xLaELgoy7vn55FmZQKOqccxTVEB5bN79Kqo9-nohfZkZdC64rWu-K0rw9aVoHVl1Lpy2boCZbcuOe1L7TI47To47UI47Uo47VI47Vo47WI47WrAZDDfdae4U36DnaJuIzownyensNcM-83wsBkOmuGRga2etSPwAk8ja_xu5d_91tiKSIwzpqx9z8KZ4qu3JLTG-fexVZypGcXw8rcrwP3fYwUgcg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| SAP S/4 Intel Foundry
Receiving Plant  (IM)
 | E2E-_45A-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Raw_Materials_&am,  | |
| SAP S/4 Intel Foundry
Supplying Plant  (IM)
 | E2E-_45A-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Raw_Materials_&am,  | |
| EWM | E2E-_45B-IF_-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_u, E2E-_45C-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us, E2E-_45E-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_and | |
| SAP S/4 Intel Foundry
 Supplying Plant (IM)
 | E2E-_45B-IF_-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_u,  | |
| SAP S/4 Intel Foundry
 (IM)
 | E2E-_45C-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us,  | |
| Receiving Warehouse (EWM)
 | E2E-_45D-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us,  | |
| SAP S/4 Intel Foundry
 Production Plant (IM)
 | E2E-_45D-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us,  | |
| Supplying Warehouse (EWM | E2E-_45D-IF-_Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_us,  | |
| External Partners/ B2B
 | E2E-_45E-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_and | |
| SAP S/4  | E2E-_45E-IF-Shipment_of_goods_through_Stock_transfer_with_planning_integration_for_Semi_Finished_and | |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
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

    subgraph E2E45CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E45CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E45CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E45CDAA_e_g_XEUS -.-> E2E45CDAD_e_g_Azure_SQL
    end
    style E2E45CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E45CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E45CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E45CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E45CDAA_e_g_MES_300 -.-> E2E45CDAD_e_g_SAP_HANA
    end
    style E2E45CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E45CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E45CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYGE20eRKyzSpxlncltilOdpXuHi0TXtVEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHHoArB0-SylOG_qAZo2MOeVNlR0ksXPZUChzp6VyFKduQzhhfKKsLkwTQ7UULEZnImysVwZPHYEozUWoUOVzS-U8Wiqk8R5TnIGOmYsYdOgauComsULZYdu-mNGDxRBq7ujRlNL5_MR3rqxVaNRpeXJdAI9OLkVwBp3luQYRomprJHEWMc-PA1K3hcNjKRZbcg3Ggaf2-2Vsf24-qJ6OTzltBwpNMubuWvq0XjgcLvpYjutUj_VquY_etbmev3JGp2x1tSw4S_tLecGjqpl7rDQaaXHv1ej3l9uJKMS_Gk4ymU2R37GN9YJGB44M_8clTkYHvfnfuPIw8_LuKVitkGQSCJXENTa1NOimzf9m3rkyEw8khUr-lgGEYFdPXOdZWxU8e9orwazeUzzA49ooINPnKSqwMQjLIw5-VZIn1rS5Q-7B9tq9SlQhxuGYhFhz2gtjAJmrXsG1N7X9hH6Xz_-F1ybV_Tq7Ih-he2q7f1bQNYHlE8vgexnXZNxDLGKRi3kN43ckuyJtS72G8if0Q4t1l0enp2fMakFUyRV8Qub6QzyHj4OHn_R_F1ugcmMj27_4iFoQassiIIHIzOL8Y2YPR7Y2NHPubfWXtmaZz82J1fDV3kqacBVR5d4_O8a09c7KooOom3j0ix7elvB2H7SRqOyyCSr66MnaOo3rDDX1d7Zr-ycnJK_S4hWeQzSgLsbHE5Y0v_y9CiGjBBV61MC1E4i7iABvlpYyLNKQCLEYl0VllXP0B8mv1XQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E45FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E45FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E45FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E45FDAA_e_g_XEUS -.-> E2E45FDAD_e_g_Azure_SQL
    end
    style E2E45FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E45FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E45FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E45FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E45FDAA_e_g_MES_300 -.-> E2E45FDAD_e_g_SAP_HANA
    end
    style E2E45FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E45FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E45FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYGE20eSg7TSpxlncltilOdpXuHi0TXtVEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHHoArB0-SylOG_qAZo2MOeVNlR0ksXPZUChzp6VyFKZtNZ4wvlNWFSQLo9qKFiEzkzZWK4MljMKWZKDWKHC7p_CcLxVSeI8pzkDFTMeMOHQNXhURWKFssu3dTGrB4Io1dXZoyGt-_mI711QqtGg0vrkug0cCLkVwBp3luQoRomg6SOYoY58bBQDdt227lIkvuwTjQtH5_0Fsf24-qJ6OTzltBwpNMubumvq0XjocLvpYjutkj_VquY_XNbmev3NFAtzralhwk_KU92x7oA73WGw41ufbq9XrK7cWVYl6MJxlNp8jqWMe6bZKh44M_8clTkYHvfnfuPIw8_LuKVitkGQSCJXENTa1NOimzf1m3rkyEw8khUr-lgGEYFdPXOeZWxU8e9orwazeUzzA49ooINPnKSqwMQjLIw5-VZIn1rS5Q-7B9tq9SlQhxuGYhFhz2gtjAJmrXsC1N7X9hH6Xz_-F1ybV_Tq7Ih-heWq7f1bQNYHlE8vgexnXZNxDLGKRi3kN43ckuyJtS72G8if0Q4t1l0enp2fMakFkyRV8Qub6QT5tx8PDz_o9ia3QOTGT7d38RC0INmWREELkZnl-MrOHo9sZCjvXNujL3TNO5ebE6vpo7SVPOAqq8u0fn-OaeOZlUUHUT7x6R41tS3orDdhK1HRZBJV9dGTvHUb3hhr6udk3_5OTkFXrcwjPIZpSF2Fji8saX_xchRLTgAq9amBYicRdxgI3yUsZFGlIBJqOS6Kwyrv4Abh_1hw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-45-R001 | Report | E2E-45 operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-45-C001 | Conversion | Legacy data migration for E2E-45 | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-45.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E45C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E45C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E45CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E45CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E45C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E45CMW_e_g_Azure_Service_Bus
    E2E45CMW_e_g_Azure_Service_Bus --> E2E45C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonzlmr74M_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUP0xI9cQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-45.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E45F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E45F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E45FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E45FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E45F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E45FMW_e_g_Azure_Service_Bus
    E2E45FMW_e_g_Azure_Service_Bus --> E2E45F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonzllr4IM_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPGZI9iQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-45-I001 | Interface | E2E-45 inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-45-E001 | Enhancement | E2E-45 custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-45-F001 | Form/Report | E2E-45 operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
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

    subgraph E2E45CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E45CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E45CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E45CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E45CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E45CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E45CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E45CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuDe2AqwTjvM13pd1JRsmBQa2p1zgsR0ccOMByVG1WmtJCsKdsqNYIlB3R7rSNXLmRaqyoYf0hXpBIdo6nhhmx-0EysZJwTVoOsWYk1m5EFMLWRqBqlFdJ9VJKUFkspjgwpVaS4O0q20baoHQzi4rAF-ubFBZIjZaSup5AjUpYe36CcMuacefY0DEO9FhW_A-fMMC4vvfE-_PCgPDlmudFTznil0tbUfs0rGRFHoD8Jxv7HA9CaTALLfwm0jsChZwem8QoInB15YejZnn3g-b4hx0mD47FKx0VPrJvFsiLlCgVmMLL9-WyeQLJM3MemgmROSPQrxnFjjo1h3ORgyJ3Pl-eoSyOVjvHvHqRGRitIBeUFmn09qs9ktyP_DG4Vs8OobwlwHKdveL8GimzvTWwZnDT2T8188_BRMko-u1_cxDRMqzt_NrEyOWfE_rsL0cUIqTqk6t7diJsgSizDeO6FDJEM39mOF1b_Q0feol9dfXram51250MXyJ1fyzmkDGL8dPKqsI7XUK0JzbCzw90bIV-YDHLSMIFbHZNG8GhbpNjpfmPclBkRMKVEXs-6F9s_hXNuYg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E45FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E45FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E45FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E45FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E45FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E45FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E45FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E45FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DPTCVYJz3ma70O6koWTKoNbU644UI6WMHGI7KjSpTWkByyrZKDWHFAd1e68iVC5nWqgrGH5I1qUTHaGq4IZsfNBVrGWeE1SBr1iJnc7IEpjYSVaO0QroPS5LQYiXFkSGlihR3R8k22ha1g0FUHLZA37yoQHIkjNT1DDJEytLjG5RRxpwzz54FQaDXouJ34JwZxuWlN96HHx6UJ8csN3rCGa9U2prZr3klI-IInE788fTjAWhNJr41fQm0jsChZ_um8QoInB15QeDZnn3gTaeGHCcNjscqHRU9sW6Wq4qUa-Sb_sgOFvNFDPEqdh-bCuIFIeGvCEeNOTaGUZOBIXc-X52jLo1UOsK_e5AaKa0gEZQXaP71qD6T3Y78079VzA6jviXAcZy-4f0aKNK9N7FlcNLYPzXzzcOH8Sj-7H5xY9Mwre786cRK5ZwS--8uhBcjpOqQqnt3I278MLYM47kXMkQyfGc7Xlj9Dx15i3519elpb3bWnQ9dIHdxLeeAMojw08mrwjrOocoJTbGzw90bIV-YFDLSMIFbHZNG8HBbJNjpfmPclCkRMKNEXk_ei-0fqERueg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-45 — E2E-45</span></div>
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
*E2E-45 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

