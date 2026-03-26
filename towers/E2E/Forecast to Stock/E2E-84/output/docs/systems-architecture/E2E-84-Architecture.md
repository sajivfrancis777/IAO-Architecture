<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-84 · Forecast to Stock</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-84 Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)** within the IAO program. It includes 5 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Forecast to Stock |
| **Capability** | E2E-84 - Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Forecast to Stock |
| **L2 Capability** | E2E-84 - Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-84 Process Migration | Migrate Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-84 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **5 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-84 Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-84C-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | E2E-84C-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | LE +++ – Plant 100X 

, SA S/4 IF
LE778 (China)

, SAP S/4 IF
LE101 US | 36 | 15 |
| 2 | E2E-84D-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | E2E-84D-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | 
LE101, LE778 (Shell Plant)
 | 34 | 14 |
| 3 | E2E-84F__R3_SAP_TM_-_Embedded | E2E-84F__R3_SAP_TM_-_Embedded | Boundary Apps, EWM 
(De-Centralized), External Partners/B2B, SAP S/4 Intel Foundry - LE500 Ireland
 | 25 | 14 |
| 4 | E2E-84I-R3_-_Inventory_Transfer_Interim_State_Variation_-_3 | E2E-84I-R3_-_Inventory_Transfer_Interim_State_Variation_-_3 | 
Sap S/4 IF
LE778 (Shell Plant)
, CFIN, SAP S/4 IF
LE101 US | 32 | 14 |
| 5 | E2E-_84A-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | E2E-_84A-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | 
Sap S/4 IF
LE500 Ireland
, SA S/4 IF
LE778 (China)
-Shell Plant
, SAP S/4 IF
LE101 US | 39 | 16 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-84C-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) — E2E-84C-Final_Delivery_Plant_is_Non-S4_Plant_(Shell)

**Swim Lanes**: LE +++ – Plant 100X 

 · SA S/4 IF
LE778 (China)

 · SAP S/4 IF
LE101 US | **Tasks**: 36 | **Gateways**: 15

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
    subgraph LE +++ – Plant 100X   
        n16[["fa:fa-cog Create Intercompany STR (SFG-01)"]]
        n17[["fa:fa-cog Create InterCompany STO (SFG-01)"]]
        n18[["fa:fa-cog Perform GTS Trade Compliance"]]
        n19[["fa:fa-cog Create Inbound Delivery (S/4) without any preceding doc."]]
        n20[["fa:fa-cog Perform Goods Receipt (Valuated with Standard Cost from iCost)"]]
        n21[["fa:fa-cog Check Quantity to be Delivered"]]
        n22[["fa:fa-cog Perform Outbound Delivery – Full Qty"]]
        n23[["fa:fa-cog Create Outbound Delivery – Partial Qty (Lot 1)"]]
        n24[["fa:fa-cog Create Outbound Delivery – Partial Qty (Lot N)"]]
        n25[["fa:fa-cog Perform ATP Check (unrestricted stock) – S/4"]]
        n26[["fa:fa-cog Perform GTS Trade Compliance"]]
        n27[["fa:fa-cog Perform Pick and Pack Updates (IM/EWM - Decentralized"]]
        n28[["fa:fa-cog Check for Cross-border invoice?"]]
        n29[["fa:fa-cog Create Export Invoice"]]
        n30[["fa:fa-cog Create Commercial Invoice (Proforma)"]]
        n31[["fa:fa-cog Perform GTS (Export Declaration US Only"]]
        n32[["fa:fa-cog Create Packing list Packing list Addendum"]]
        n33[["fa:fa-cog Create Sales Invoice (for MY, Vietnam, China"]]
        n34[["fa:fa-cog Ship (Goods Issue"]]
        n35[["fa:fa-cog IC Invoice Bill To: LE778"]]
        n36[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n47(["fa:fa-stop Sales Invoice created"])
        n48(["fa:fa-stop GTS Trade Completed"])
        n49(["fa:fa-stop ATP Check Confirmed"])
        n50(["fa:fa-stop GTS Trade Compliance Completed"])
        n51(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n53{{"fa:fa-code-branch Quantity Delivered ?"}}
        n54{{"fa:fa-code-branch Cross-Border?"}}
        n55{{"fa:fa-code-branch exclusiveGateway"}}
        n56{{"fa:fa-code-branch exclusiveGateway"}}
        n57{{"fa:fa-code-branch exclusiveGateway"}}
        n58{{"fa:fa-code-branch exclusiveGateway"}}
        n59{{"fa:fa-code-branch exclusiveGateway"}}
        n64{{"fa:fa-arrows-alt parallelGateway"}}
        n65{{"fa:fa-arrows-alt parallelGateway"}}
        n66{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SA S/4 IF LE778 (China)  
        n1[["fa:fa-cog Perform Repetitive Steps till order confirmation"]]
        n2[["fa:fa-cog Create Sales Order"]]
        n3[["fa:fa-cog Create InterCompany STR (SFG-01)"]]
        n4[["fa:fa-cog Perform GTS Trade Compliance"]]
        n5[["fa:fa-cog Create InterCompany STO (SFG-01)"]]
        n6[["fa:fa-cog Perform GTS Trade Compliance"]]
        n7[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n8[["fa:fa-cog Perform Inbound Delivery (SFG-01) wrt STO"]]
        n9[["fa:fa-cog Perform Goods Receipt (SFG-01)"]]
        n10[["fa:fa-cog Perform GTS Trade Compliance"]]
        n37(["fa:fa-play Initiate IBD"])
        n39(["fa:fa-stop AR posting Completed"])
        n40(["fa:fa-stop Goods Received"])
        n41(["fa:fa-stop Order Confirmed"])
        n42(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n43(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n44(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n52{{"fa:fa-code-branch exclusiveGateway"}}
        n60{{"fa:fa-arrows-alt parallelGateway"}}
        n61{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 IF LE101 US
        n11[["fa:fa-cog Create Unconfirmed / Confirmed Sales Orders"]]
        n12[["fa:fa-cog Create Purchase Requisition (FG-01)"]]
        n13[["fa:fa-cog Create Purchase Order (FG-01)"]]
        n14[["fa:fa-cog Perform GTS Trade Compliance"]]
        n15[["fa:fa-cog Perform GTS Trade Compliance"]]
        n38(["fa:fa-play Confirmed Sales"])
        n45(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n46(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n62{{"fa:fa-arrows-alt parallelGateway"}}
        n63{{"fa:fa-arrows-alt parallelGateway"}}
        n67[["fa:fa-folder-open E2E-84E: R3 Physical Product Sales"]]
    end
    n12 --> n13
    n62 --> n14
    n13 --> n62
    n2 --> n60
    n60 --> n1
    n5 --> n52
    n16 --> n57
    n19 --> n20
    n21 --> n53
    n53 -->|"Full"| n22
    n22 --> n59
    n27 --> n64
    n28 --> n54
    n29 --> n30
    n30 --> n31
    n54 -->|"No"| n32
    n32 --> n33
    n64 --> n28
    n64 --> n34
    n54 -->|"Yes"| n29
    n36 --> n7
    n34 --> n65
    n7 --> n39
    n60 --> n4
    n62 --> n2
    n8 --> n61
    n61 --> n10
    n61 --> n9
    n20 --> n21
    n9 --> n40
    n56 --> n24
    n56 --> n23
    n53 -->|"Partial"| n56
    n33 --> n47
    n1 --> n41
    n23 --> n55
    n24 --> n55
    n55 --> n59
    n59 --> n66
    n66 --> n25
    n66 --> n27
    n66 --> n26
    n26 --> n48
    n25 --> n49
    n18 --> n50
    n65 --> n35
    n52 --> n6
    n52 --> n16
    n57 --> n17
    n57 -->|"Outbound Delivery against STO"| n22
    n58 --> n18
    n17 -->|"Same STR/STO document 
will be visible in both LE’s"| n58
    n58 --> n3
    n15 --> n45
    n11 --> n63
    n63 --> n12
    n63 --> n15
    n14 --> n46
    n4 --> n42
    n6 --> n43
    n10 --> n44
    n31 --> n51
    n35 --> n36
    n67 --> n11
    n38 --> n67
    n58 --> n19
    n37 --> n8
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
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 serviceTask
    class n21 serviceTask
    class n22 serviceTask
    class n23 serviceTask
    class n24 serviceTask
    class n25 serviceTask
    class n26 serviceTask
    class n27 serviceTask
    class n28 serviceTask
    class n29 serviceTask
    class n30 serviceTask
    class n31 serviceTask
    class n32 serviceTask
    class n33 serviceTask
    class n34 serviceTask
    class n35 serviceTask
    class n36 serviceTask
    class n37 startEvt
    class n38 startEvt
    class n39 endEvt
    class n40 endEvt
    class n41 endEvt
    class n42 endEvt
    class n43 endEvt
    class n44 endEvt
    class n45 endEvt
    class n46 endEvt
    class n47 endEvt
    class n48 endEvt
    class n49 endEvt
    class n50 endEvt
    class n51 endEvt
    class n52 gateway
    class n53 gateway
    class n54 gateway
    class n55 gateway
    class n56 gateway
    class n57 gateway
    class n58 gateway
    class n59 gateway
    class n60 gateway
    class n61 gateway
    class n62 gateway
    class n63 gateway
    class n64 gateway
    class n65 gateway
    class n66 gateway
    class n67 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtWWtv2zgW_SuEiyIOam9FUi_7wy4cxy4CtNNMnHZ2MOkHWqJjIbLk1SOJN5P_vpcyKTs0GXSd-kMQHfHcx-HlFUU9daI85p1h5_37pyRLqiF6OqmWfMVPhuhkzkp-0kNb4DsrEjZPeXkixizyrJol_22GYXf9KIYJbMpWSboR6Izf5hx9u-ihERDTHipZVvZLXiSLk97JukhWrNiM8zQvxOh3PFw4i8abvHWWFzEvdgMcJ8CRB9Q0yfgOpoEbuFPBK3mUZ_ELowtvES6ik2cRXJo_REtWVE34dcm_sMc_krhawvWCpSWHMctqlX5mc56KHKuiFlhUF_dKjKQUfjIQbLZmUZLdAu46ABUsu9tBnvP8jJ7fv7_JWqfo-vwmQ_CLUlaW53yBygrgyX2FFkmaDt-549HUc3plVeR3fPiOTIJzSnqRyGQIqTs9IW7_gSe3y2o4z9NYDu0_iByGZP3YKx6HxOkVG_ir-eJZvPM09klIwtbTWYDHeKw8LRaLN3kCXYtrVt5JXxM6JdPz1hf2fG_sHNpTaZ67wQjrOvHiPon4ntHpdEonO6kmvocdu9GzKfWdsWb0llX8gW12BgdjtzU49YIpDqwGt_70KOv5ZZFHyiCdeFOvNRic4emIWA26I-yGMkKwc1uw9RJ9nqAPHz6gm5o4mKLLlGUVArf_hjHbkeKXYf-vv246CzZcsH6U36JxwSEzdJFVvIjy1ZplGzS7vkLd2fRT38GnN50fP_bpgZ0-bulfrfTwJf2SF4u8WKFP1zN0XbCYI2EkTVgWcZ06sHie53UWo3OeJve82IDnj-4pekiqZV5XSMSzLnjEY1hoKM6jf2hmiWOJKM_jEl0BM1lXqPudpTW4ixvDaFYx0TZiiLaERVLkK5SIf_V0CdZiXvLoDv1ew9Qk1QZVOZpzFTmPdTIxR_a1rrSU5ZRP6zRFv1cb3Q41Cmc1cwldBrqvsIS6n3MoooO03Dda_O3AomfOdXR9KUXr1lnBYT0kkZiFssqju1NlH2Zct-cfXWckMFMvE4gCph2ygX--rWNIuUTdiy8fJ398QX1IOuJZVbAUHnEHUxma6gDMgnR5WfbnzYMLJdl9Do3rXzrbXPmTx3UOj4mLLUnjUMfIgaxXsM7FZEge6kIXEgkyfU4otmvYlc4h6ZQVrEryDH2boa9ZqlcfJcZAhIhiRaYJLKAXF6M4hodPvdLtmKt4xmB7sctFSPrlzx76nvAqY6seKJ1kTDelle9smaxRd7vgL8qyPtBSK86LcevwDJo3us6H0HyDINR5liIcXaFLaBYiY1FPoxr6wDjlsFnKbjUTbtBtTUDNr7V8o0YEUW2n-6RQI2lVzw2UgUbZLbxxni2SYnVA8ZzXvTRry-rQwz_FlhFYbNCnp52-Me_PYVMVLXf9te2sCJbU8_M-1TVTt8txu4884HhmDn-M0roER5-2WwSd5h9HC46jhcfRBkfR_D0ZWVHkD2WfpRVaQ0tIU55aSN4xJP__I0EL0bZHs5F4TqCL6Xatom7TGk5fbo7MC_aKrzkUFMgAT36-LlEllv22Z0fb5dG0QL1vv9Kxvgqy3i9-Zmtl3Zm5Rz_xvDdt6Y5_0gZvbo-W3aRhT7gNHT3AMwty0cwMfmoLaNnROkfnT_ea-zqFd4sLeJtOGu3PzrVeRw8a9BVaS5WsTf2gQ-8Suj8crXfkpkSt7d8lb2_gLv0FNtxf8CAhx3U_55hGht_eyC53nQw7GDZe-_WIjav5WxapiUQfd5O6341KvbItO7e6gPOJkkMd_adOyqTZ-3XNa4O-bmFbYRbu8f0Me8cvyVBbkppSevF5v6CA_bfb8MkxlUiPIe017QWc9PCin695hiZk0g_dyRBdweveclMmEbxiwJtFXEdVK90PraShxFC__09RKBLwFeCqEXQL-EQCcoDvKIYjGfLa2156ajz2JRAoYLAF1EEUvKTLESoIr_H5901HvFDfdP4Wr-JqrHTvDRQQyHhUwCSUI1pA-qPKH5UR0zZkV_r7LW-8UeWNSm-0lceVsYcaQF3d1p9CcRG6ipRKIZQOVFJ9TwIyEzrQlHW1uVHRyUR9lYYvdcSOBrRaSYNEMaQyriJ4MkTi6sDB1MgjhSZFz1cpyWJx27mW18ohkQM8lTNxNcDztAn2ZJC-cuKrmDwdCHRAUYgEXDVtRHpxlResqqbVTo6gbWCq8LVr3AJy_nDwAgCtDs9l2C1LslJuhfbr25NxYBUpVkZmbMXF9vOj2ArCOVq9gtMO2Ds_iK0wnGLdw6MAjvrhDAPN80qcRjaHM4NtFXqh5kBNKFZKqDyxnDO_rXk5Z5joQEuRk-gqKdR1y5DXrVNV2arOqGoBqlCokr-ddaVuO0KVf6BL1y44SQn3Dn5FSe4dT7-4Q6x3qPWOa73jWe_41juB9U5ovTOw3gGVrbfsKmC7DNiuA7YLge1KYLsU2K4FtouB7WoQuxrklZqwq0HsahC7GsSuBrGrQexqELsaxK4GtatB7WrQV5aIXQ1qV4Pa1aB2NWBhq09xL_HQgg_k57SXS9cxotiIEiNKjahrRD0j6hvRwIiGRtSYm2fMzTPmBg8y-W3tJUzNsGuGPTPsm-HADIdmeGCEYXtkhLEZNmfpm7P0zVn65ix9c5bwyJLfGDu9Dpz6r1gSd4ZPnebTPHy-j_mC1WnVee51GJyxzDZZ1Bk2n7A7dfN14zxh8Ma52oLP_wMUGsmj" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-84D-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) — E2E-84D-Final_Delivery_Plant_is_Non-S4_Plant_(Shell)

**Swim Lanes**: 
LE101 · LE778 (Shell Plant)
 | **Tasks**: 34 | **Gateways**: 14

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
    subgraph  LE101
        n1[["fa:fa-cog Create Sales Orders"]]
        n2[["fa:fa-cog Perform Order Validation (including Credit and GTS checks)"]]
        n3[["fa:fa-cog Receive CTP Updates"]]
        n4[["fa:fa-cog Perform Order Confirmation"]]
        n5[["fa:fa-cog Perform GTS Trade Compliance"]]
        n6[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n7[["fa:fa-cog Receive (Virtual)"]]
        n8[["fa:fa-cog Ship (Goods Issue)"]]
        n9[["fa:fa-cog Create Customer Invoice"]]
        n10[["fa:fa-cog Perform GTS Trade Compliance"]]
        n11[["fa:fa-cog Calculate Taxes"]]
        n12[["fa:fa-cog Check Quantity to be Delivered"]]
        n13[["fa:fa-cog Perform OBD – Full Qty"]]
        n14[["fa:fa-cog Perform Outbound delivery – Partial Qty (Lot 1)"]]
        n15[["fa:fa-cog Perform OBD – Partial Qty (Lot N)"]]
        n35(["fa:fa-play Initiate sales order"])
        n37(["fa:fa-stop AR posting Completed"])
        n38(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n39(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n45{{"fa:fa-code-branch Quantity Delivered ?"}}
        n46{{"fa:fa-code-branch exclusiveGateway"}}
        n47{{"fa:fa-code-branch exclusiveGateway"}}
        n48{{"fa:fa-code-branch exclusiveGateway"}}
        n52{{"fa:fa-arrows-alt parallelGateway"}}
        n53{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph LE778 (Shell Plant) 
        n16[["fa:fa-cog Create Inbound Delivery (S/4) without any preceding doc."]]
        n17[["fa:fa-cog Perform Goods Receipt (Valuated with Standard Cost from iCost)"]]
        n18[["fa:fa-cog Check Quantity to be Delivered"]]
        n19[["fa:fa-cog Perform OBD – Full Qty"]]
        n20[["fa:fa-cog Perform Outbound delivery – Partial Qty (Lot 1)"]]
        n21[["fa:fa-cog Perform OBD – Partial Qty (Lot N)"]]
        n22[["fa:fa-cog Perform ATP Check (unrestricted stock) – S/4"]]
        n23[["fa:fa-cog Perform GTS Trade Compliance"]]
        n24[["fa:fa-cog Perform Pick and Pack Updates (IM/EWM - Decentralized"]]
        n25[["fa:fa-cog Check for Cross-border invoice?"]]
        n26[["fa:fa-cog Create Export Invoice"]]
        n27[["fa:fa-cog Create Commercial Invoice (Proforma)"]]
        n28[["fa:fa-cog Create Packing list Packing list Addendum"]]
        n29[["fa:fa-cog Create Sales Invoice (for MY, Vietnam, China"]]
        n30[["fa:fa-cog Ship (Goods Issue"]]
        n31[["fa:fa-cog Perform Invoice/Billing Bill To: LE101 ShipTo: Customer/OSAT"]]
        n32[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n33[["fa:fa-cog Perform GTS Trade Compliance"]]
        n34[["fa:fa-cog Perform GTS (Export Declaration US Only"]]
        n36(["fa:fa-play Initiate IBD"])
        n40(["fa:fa-stop AR posting Completed"])
        n41(["fa:fa-stop Packing List Creation Complete"])
        n42(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n43(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n44["E2E-84H-R3 Physical Product sales (3/3)"]
        n49{{"fa:fa-code-branch Quantity Delivered ?"}}
        n50{{"fa:fa-code-branch Cross-Border?"}}
        n51{{"fa:fa-code-branch exclusiveGateway"}}
        n54{{"fa:fa-arrows-alt parallelGateway"}}
        n55{{"fa:fa-arrows-alt parallelGateway"}}
        n56{{"fa:fa-arrows-alt parallelGateway"}}
        n57{{"fa:fa-arrows-alt parallelGateway"}}
        n58{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n2 --> n3
    n16 --> n55
    n18 --> n49
    n49 -->|"Full"| n19
    n19 --> n51
    n21 --> n51
    n22 --> n23
    n51 --> n22
    n24 --> n54
    n25 --> n50
    n26 --> n27
    n54 --> n30
    n6 --> n37
    n51 --> n24
    n17 --> n18
    n3 --> n4
    n55 --> n17
    n55 --> n33
    n50 -->|"Yes"| n26
    n50 -->|"No"| n28
    n31 --> n56
    n56 --> n32
    n32 --> n40
    n54 --> n25
    n27 --> n29
    n47 --> n10
    n9 --> n11
    n49 -->|"Partial"| n57
    n28 --> n41
    n52 --> n5
    n1 --> n52
    n52 --> n2
    n7 --> n46
    n4 --> n46
    n29 --> n34
    n30 --> n58
    n56 --> n6
    n57 --> n21
    n57 --> n20
    n46 --> n12
    n45 -->|"Full"| n13
    n45 -->|"Partial"| n53
    n53 --> n14
    n12 --> n45
    n53 --> n15
    n15 --> n47
    n14 --> n47
    n13 --> n47
    n5 --> n38
    n35 --> n1
    n36 --> n16
    n33 --> n42
    n23 --> n43
    n58 --> n31
    n58 --> n7
    n10 --> n39
    n8 --> n48
    n48 --> n9
    n11 --> n48
    n47 --> n8
    n34 --> n44
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
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 serviceTask
    class n21 serviceTask
    class n22 serviceTask
    class n23 serviceTask
    class n24 serviceTask
    class n25 serviceTask
    class n26 serviceTask
    class n27 serviceTask
    class n28 serviceTask
    class n29 serviceTask
    class n30 serviceTask
    class n31 serviceTask
    class n32 serviceTask
    class n33 serviceTask
    class n34 serviceTask
    class n35 startEvt
    class n36 startEvt
    class n37 endEvt
    class n38 endEvt
    class n39 endEvt
    class n40 endEvt
    class n41 endEvt
    class n42 endEvt
    class n43 endEvt
    class n44 startEvt
    class n45 gateway
    class n46 gateway
    class n47 gateway
    class n48 gateway
    class n49 gateway
    class n50 gateway
    class n51 gateway
    class n52 gateway
    class n53 gateway
    class n54 gateway
    class n55 gateway
    class n56 gateway
    class n57 gateway
    class n58 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtWVtv27gS_iuEiyIOYJ-IpGTJfjgLx5dugHSbrdMuFpt9oCUqJiJLhi5JfNL89zOUSTmmxS7WbR6S6CPn9s1whrJfOmEW8c6o8_79i0hFOUIvZ-WKr_nZCJ0tWcHPemgHfGW5YMuEF2dyT5yl5UL8r96G3c2z3CaxOVuLZCvRBb_POPpy1UNjEEx6qGBp0S94LuKz3tkmF2uWbydZkuVy9zsexE5cW1NLl1ke8Xy_wXF8HHogmoiU72Hqu747l3IFD7M0OlAae3EQh2ev0rkkewpXLC9r96uCf2TPf4ioXMFzzJKCw55VuU6u2ZInMsYyryQWVvmjJkMU0k4KhC02LBTpPeCuA1DO0oc95Dmvr-j1_fu7tDGKbqd3KYKfMGFFMeUxKkqAZ48likWSjN65k_Hcc3pFmWcPfPSOzPwpJb1QRjKC0J2eJLf_xMX9qhwtsyRSW_tPMoYR2Tz38ucRcXr5Fn4btnga7S1NBiQgQWPp0scTPNGW4jj-IUvAa37Ligdla0bnZD5tbGFv4E2cY306zKnrj7HJE88fRcjfKJ3P53S2p2o28LBjV3o5pwNnYii9ZyV_Ytu9wuHEbRTOPX-OfavCnT3Ty2p5k2ehVkhn3txrFPqXeD4mVoXuGLuB8hD03Odss0LoeoYdxYX8SfFff911YjaKWT_M7tEk5xADWjA4kOiTPCnFXefvv98IkEOBG57HWb7e7UVfWSIiVoosRV2RhkkVQelKpZEoEUsj9OF2gcIVDx-Kc0MvPdT7mYdcPHI0ub1BXzagk5uOuN9zZJKlscjXtSuGnNcuJz27zVkEJrP1JhEsDbkhOWiXHH9GN1lRykhliOOqzNAk4dDX0ntDg98eZPeryMuKJSYnweH2xUpsUPdDlkUFuiqKipv7h63JnFRFma2BlKv0MRNHUWHnZEKwWT0sCatE2rxlz0cJw0bpTGQdoN8rlpai3CJgbcnRlCfACBSMKUwt6b6coruKOJiieZUk6Pdya0raCqUql1kFCYt2Jrdazw10UJgsUhXqXmclwibP2PtHZ46U_HZU8F63UbJJoGtcwZwUkryiPn31nAKZ87cy_l4GkrqRtbdRtVdniZc1cwcygSHTlliVDKuO4Y_rcL2Xlz1pEe8vYbyFq30BNKlHv9x1Xl_fig7aRfkztJgChD7sGq8p5p8mFpwk5pG9GMvz7Knos6REG5azJOGJRYj-OyEYuUZHv575foC6ixWH6r9JgMtz9LZUB6094Srd1f5U1353ceGeoydRrrJKtuot2uTQner-HWXhf8wT4FuaRt2c6r62KaGvsaQCc1GtGC1KJi9SEZRIAdeGPFsjIf89Ol7BjzSK4amNgjg_vVEQ_BMaBbGM3DGMxh013SrNOdwDRCi5hgMaPpxr_ZBXUx89ueETSy-9EeCFHH43DP5R8xp1rz5ezP74iPqQrJCnJdQ0XO3NhBGvLdugFmo1K4r-sm6ESOyG1y-mdHt9z543GVyP2yce8dvnZLaGKRnKZCg51IXblwyQHeUkaFUhw5cnJhFQ4AcP4yiCs1utTT3D79y_Gi8kGR__7KGvgpcpW_eAI5Eyc544_3BbMPdbalNZvbiEO6d0X_5Ft9lod3Ws1confau4-LQY35qqyQ_flOjpRUpdu2hXFQYUZAI9tr6pflmgT2lidgM6sI3nq8upOdqcfz-WXWzI6HK5luVS14F0Toub0uQnDGT6E3S4oGJGZv3A_bX_GbrZaluIEE4QHJyoCkt1l-nSCyqP0FvJ4cnXAc9pF931i90L_pEMPm2ou6cMde8UocEpQv4pQsGJd46UoH7_v3A01CMe7J49TwPBDnCHCnCHEvh215Ej967zTY5nvXeohLFWjk1AmSPanqd2EKJ3uErE1YCnAEcDykXiax1KhOodagP1TSNaJ_Z3AA4UQFWQWkDZxL4B0MZvR7Hwp3wn-ia9Mld-y3YLjQ1NRrNT-6ljp4od1zEiIzobRDlOmmzoSLSISgHGZrrUpaT2ydNxEZ1dvd1TLjTpV4_EWNfPyryrY3KNZ6L8oZpa6iiNgcFCw4oOEZuADtFVElg74XpHJUnNpYPwmyyqvOOmMHQGPHNHQ4iqBFdTiF0ToAaga6cpBF1d-lnHoymgWkNzKDTQOK7yRrEBNE4omqkuFJ1o7YSrgObsYnODor3xWsfpvvlASxbIm4_dDlaIdYVaV1zrimddGVhXfOtKYF0ZWleAUuuSnQVspwHbecB2IrCdCWynAtu5wHYysJ0NYmeDfKcm7GwQOxvEzgaxs0HsbBA7G8TOBrGzQe1sUDsb9DtHxM4GtbMBnUV_WXCIDyy4rz7wP0SDVnTYhrpOK4pbUdKK0lbUbfcY-rn6RP4QHrTDfjsctMPDVhgGeiuM22HSDtN22G2H26P02qP02qP0mig7vQ681a2ZiDqjl079FR18jRfxmFVJ2XntdRi8tS22adgZ1V9ldar6bX8qGHwetd6Br_8H7DqXTQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-84F__R3_SAP_TM_-_Embedded — E2E-84F__R3_SAP_TM_-_Embedded

**Swim Lanes**: Boundary Apps · EWM 
(De-Centralized) · External Partners/B2B · SAP S/4 Intel Foundry - LE500 Ireland
 | **Tasks**: 25 | **Gateways**: 14

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
        n19["Reconcile CTSi Carrier Invoice and Dispute Management"]
        n20["Receive reconciled Carrier Invoice(s)"]
    end
    subgraph EWM  (De-Centralized)
        n12["Release Wave and Pick WH Task Creation"]
        n13["Pick WH Task Confirmation (TR/TO)"]
        n14["Pack (Shipping Label Printing) and Packing List"]
        n15["Perform Loading"]
        n16["Post Goods Issue (EWM)"]
        n17["Outbound Delivery (OD) with HU Details"]
        n18["Receive Outbound Delivery Order in EWM"]
        n42{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph External Partners/B2B
        n21["Send to SAP B4NL"]
        n22["Notify carrier"]
        n23["Capture Carrier Invoices (via EDI only)"]
        n24["Capture Execution events via BN4L-GTT"]
        n25["Capture Physical receipt of goods at LE778"]
        n28(["fa:fa-play Data needs to be Sent to B4NL"])
        n30(["fa:fa-stop Physical Receipt Captured"])
        n33{{"fa:fa-code-branch exclusiveGateway"}}
        n43{{"fa:fa-arrows-alt parallelGateway"}}
        n44{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 Intel Foundry - LE500 Ireland 
        n1["Create Outbound Delivery (S/4)"]
        n2["Create/Update Freight Unit and Freight Order"]
        n3["Perform Carrier Selection and Calculate Charges"]
        n4["Send Loading Instructions to EWM"]
        n5["Send Rates/Charges: Freight forwarders (Within TM)"]
        n6["Ship (Goods Issue)"]
        n7["Execute Freight Order and Update Status Post GI"]
        n8["Create and Update Freight Settlement Document"]
        n9["Create Service PO/ Entry Sheet"]
        n10["Post Accrual to Freight Expense Account(s)"]
        n11["Allocate Freight Costs to Delivery Items (CO/PA) or Material Valuation"]
        n26(["fa:fa-play Outbound Delivery for EWM to be Created"])
        n27(["fa:fa-play Rates/Charges need to be Sent"])
        n29(["fa:fa-stop Accrual Posted and Freight Costs Allocated"])
        n31{{"fa:fa-code-branch exclusiveGateway"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n34{{"fa:fa-arrows-alt parallelGateway"}}
        n35{{"fa:fa-arrows-alt parallelGateway"}}
        n36{{"fa:fa-arrows-alt parallelGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
        n39{{"fa:fa-arrows-alt parallelGateway"}}
        n40{{"fa:fa-arrows-alt parallelGateway"}}
        n41{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n13 --> n14
    n12 --> n13
    n17 --> n42
    n42 --> n15
    n1 --> n34
    n2 --> n35
    n34 --> n2
    n3 --> n4
    n28 --> n33
    n7 --> n38
    n38 --> n41
    n33 --> n21
    n35 --> n31
    n8 --> n9
    n9 --> n39
    n39 --> n10
    n39 --> n11
    n11 --> n40
    n10 --> n40
    n31 --> n3
    n21 --> n43
    n22 --> n44
    n44 --> n23
    n43 --> n24
    n32 --> n7
    n44 --> n25
    n25 --> n30
    n40 --> n29
    n26 --> n1
    n18 --> n12
    n15 --> n16
    n43 --> n31
    n19 --> n20
    n41 --> n8
    n5 --> n36
    n27 --> n5
    n36 --> n31
    n36 -->|"Rates to CTSI"| n37
    n43 -->|"EDI/Manual"| n22
    n14 --> n17
    n4 --> n42
    n34 --> n18
    n16 --> n6
    n6 --> n32
    n37 --> n19
    n38 -->|"Book/Tender to 
Carrier via BN4L"| n33
    n24 -->|"POD Receipt Events"| n32
    n23 --> n37
    n20 --> n41
    n35 -->|"FO (Freight Order)  & HAWB
(House Airway Bill) Mapping"| n37
    class n26 startEvt
    class n27 startEvt
    class n28 startEvt
    class n29 endEvt
    class n30 endEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWFtv4jgU_isWo26pBCJXAjysBAFmKnWmqNDpw3QfTHCK1RBHjtOW7fDf9zixA7j0YZk-jCZfznfu59jhvRGxFWkMGhcX7zSlYoDeL8WabMjlAF0ucU4uW6gCfmJO8TIh-aWUiVkq5vTfUsz2sjcpJrEp3tBkK9E5eWIE3V-30BCISQvlOM3bOeE0vmxdZpxuMN-GLGFcSn8hvdiKS2vq1YjxFeF7AcsK7MgHakJTsofdwAu8qeTlJGLp6khp7Me9OLrcSecS9hqtMRel-0VOvuO3B7oSa3iOcZITkFmLTXKDlySRMQpeSCwq-ItOBs2lnRQSNs9wRNMnwD0LII7T5z3kW7sd2l1cPKa1UXRz95gi-IsSnOdjEqNcADx5ESimSTL44oXDqW-1csHZMxl8cSbB2HVakYxkAKFbLZnc9iuhT2sxWLJkpUTbrzKGgZO9tfjbwLFafAv_GrZIutpbCrtOz-nVlkaBHdqhthTH8R9ZgrzyBc6fla2JO3Wm49qW7Xf90PqoT4c59oKhbeaJ8BcakQOl0-nUnexTNen6tvW50tHU7VqhofQJC_KKt3uF_dCrFU79YGoHnyqs7JleFssZZ5FW6E78qV8rDEb2dOh8qtAb2l5PeQh6njjO1mjEirKX0TDL8uqd_Evt_q_Hxp3s9IgmBIWLOUUh5pwSjq7TFwapQjhdoTHNs0IQ9B2n-AmmNxWPjX8O9DhWpYfQF4K41rcydTXzq5oHXWQ4OXn4jlBzTNoh6Oc4gX2wujp01imNJAT2CHrAL5VrMxo9o4dvqCxpyAkWlKXH3tkuEI_lWBpTvillUXNx11ncXhkcT3IwcJrzNc0ymEVUDjOacZoKeLyqzINI-Y7mRk5sX2ogPGZ8g24YXoGYIdGVEiwX6Ctjqxxd53lBUBPyYDoTgOBtIZayjGhMEkgzFLN5O75Cr1Ss0bd7QAWmSW4Qewd1-ajgVu5ERFOZ-mOi57y_PzZiPIhxG2rIXvM2TgTKMNQlIcnXquMfG7vdp9V8E4SnGPIFmyklPO-MnNFhy9jg2hx4SDA0H87QyPtxY3SVLPgPJmi8RVHVSYaALGyIM1FwYvZajpovFKPJ-BqxNNkaGXW8A-bkjURF2QrkBVovR5I4-uHdtL8uFgbPP-DN1tucRhAilxnOBGKwC8pKYljRkyDoGeRe85dOapbAwhhjgVFKCDAgCUuCIB9C_lfl4rD7XWtPzgXL9tbvlHXl1sokuvtSytO5vYTzJVoj8hYlRQ6N8KGYVQe4_68DKpL3p20jO2He8aCKAmZtKvsVGrUN6fQtC11zksipO2xxWRA59qcavAmqzMrX8p37bCVpU16eTugeLizlTGugHI9jtnsw07rh5rCSorJ9JDnESVQkUm8IR_UTMSbS012vNgIECpu8KPllF3wYRV8z7kBp3lFaB7WX4Msrlp5Cxz_AMoBxXpgLRC4aucZQ82DTGDJyx1STQI4zUIalcjUXWBQ5qpbW9bGC3r4SBwytak6ESMqjA41ZVHw8Q_p7-rw6pdHstoMmcBZs0XxNiLlfLb09h1HECxgEyJ62NnnLSArHBLyCjhCHB09Flm0zTBIWHfoYgrayCHUDXQuygbyGt53Z8AoxDicgrDW4gKKfOClOnDVO15jxj00JBSvPumrkq5DNoXUCQ81R8cudcbAyTHLfWBU6QTJbQDzs8SpknYkPu8M-a3e4znk074yV4_rnkLrnkIJzSL1zSP1zdq91Dsk-c2HDpQq123_Li5IGHAW4GggqwHMU4GkJX0tUz65Wod67-r3rVYBWoEzW4j0lry0qg25PyysBz9aA0uDUgK8oGlCMvnrsq9f62VWAbZmAVmCroDwtYVsG4OqwdRiaUQMqD54O1NN50BKejkNLuIoSmAydSkcHqr3wlFuODs3pqki03yoVts6-rVTYXcOLOnm2SoZTG1Gh6YJoJ7QGR1WsLnjX0FgBv-ESK_efXHnwjQLnzm85jkdugAzc9TrwhQKbrhRwasdVMuyaYTSm7jNb-2krP7Sf2q2aoPy2-0edBj6MGHvuLGBM4NwEbx9TfUvQd8rK97rUnuLNbsf1RW5S3kIrQW3R0bnWMTiW2du-UjW9Rc2jA_wKob_Qt-EDXL-b31ghj0XK5QfrCL4vr-BIKz9vjpJafoqWPaF_WTjGg0_w3id4X_1qcIS61knU1h_Ux7BzGnZPw95p2D8Nd0_DwWm4dxrun4Rhzk7Cp6P0TkfpnY7Sq6NstBobAh-0dNUYvDfKX9jgV7gViXGRiMau1cCFYPNtGjUG5S9RjaK8nY0phmv3pgJ3_wFXSwZc" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E-84I-R3_-_Inventory_Transfer_Interim_State_Variation_-_3 — E2E-84I-R3_-_Inventory_Transfer_Interim_State_Variation_-_3

**Swim Lanes**: 
Sap S/4 IF
LE778 (Shell Plant)
 · CFIN · SAP S/4 IF
LE101 US | **Tasks**: 32 | **Gateways**: 14

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
    subgraph  Sap S/4 IF LE778 (Shell Plant) 
        n14[["fa:fa-cog Perform GTS Trade Compliance"]]
        n15[["fa:fa-cog Create Inbound Delivery (S/4) without any preceding doc."]]
        n16[["fa:fa-cog Perform Goods Receipt (Valuated with Standard Cost from iCost)"]]
        n17[["fa:fa-cog Check Quantity to be Delivered"]]
        n18[["fa:fa-cog Perform Outbound Delivery – Full Qty"]]
        n19[["fa:fa-cog Create Outbound Delivery – Partial Qty (Lot 1)"]]
        n20[["fa:fa-cog Create Outbound Delivery – Partial Qty (Lot N)"]]
        n21[["fa:fa-cog Perform ATP Check (unrestricted stock) – S/4"]]
        n22[["fa:fa-cog Perform GTS Trade Compliance"]]
        n23[["fa:fa-cog Perform Pick and Pack Updates (IM/EWM - Decentralized"]]
        n24[["fa:fa-cog Check for Cross-border invoice?"]]
        n25[["fa:fa-cog Create Export Invoice"]]
        n26[["fa:fa-cog Create Commercial Invoice (Proforma)"]]
        n27[["fa:fa-cog Perform GTS (Export Declaration US Only"]]
        n28[["fa:fa-cog Create Packing list Packing list Addendum"]]
        n29[["fa:fa-cog Create Sales Invoice (for MY, Vietnam, China"]]
        n30[["fa:fa-cog Ship (Goods Issue"]]
        n31[["fa:fa-cog IC Invoice Bill To: LE778"]]
        n32[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n38(["fa:fa-stop Sales Invoice created"])
        n39(["fa:fa-stop GTS Trade Completed"])
        n40(["fa:fa-stop GTS Trade Compliance Completed"])
        n41(["fa:fa-stop ATP Check Confirmed"])
        n42(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n43(["fa:fa-stop AR posted"])
        n44{{"fa:fa-code-branch Quantity Delivered ?"}}
        n45{{"fa:fa-code-branch Cross-Border?"}}
        n46{{"fa:fa-code-branch exclusiveGateway"}}
        n47{{"fa:fa-code-branch exclusiveGateway"}}
        n48{{"fa:fa-code-branch exclusiveGateway"}}
        n53{{"fa:fa-arrows-alt parallelGateway"}}
        n54{{"fa:fa-arrows-alt parallelGateway"}}
        n55{{"fa:fa-arrows-alt parallelGateway"}}
        n56{{"fa:fa-arrows-alt parallelGateway"}}
        n57{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph CFIN
        n7["AR Posting"]
        n8["Profitability Analysis"]
        n9["Cash Application"]
        n10["Payment Receipt"]
        n49{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4 IF LE101 US
        n1["Receive Virtual"]
        n2["Outbound Delivery (1 to N)"]
        n3["Ship Goods Issue"]
        n4["GTS Trade Compliance"]
        n5["Customer Invoice"]
        n6["Caluculate Taxes"]
        n11[["fa:fa-cog Create Unconfirmed / Confirmed Sales Orders"]]
        n12[["fa:fa-cog Perform GTS Trade Compliance"]]
        n13[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n33(["fa:fa-play Confirmed Sales"])
        n34(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n35(["fa:fa-stop GTS Compliance completed"])
        n36(["fa:fa-stop Tax Calucualted"])
        n37(["fa:fa-stop AR posting Completed"])
        n50{{"fa:fa-arrows-alt parallelGateway"}}
        n51{{"fa:fa-arrows-alt parallelGateway"}}
        n52{{"fa:fa-arrows-alt parallelGateway"}}
        n58[["fa:fa-folder-open E2E-84E: R3 Physical Product Sales"]]
    end
    n15 --> n56
    n17 --> n44
    n44 -->|"Full"| n18
    n18 --> n48
    n23 --> n53
    n24 --> n45
    n25 --> n26
    n26 --> n27
    n45 -->|"No"| n28
    n28 --> n29
    n53 --> n24
    n53 --> n30
    n45 -->|"Yes"| n25
    n30 --> n54
    n13 --> n37
    n16 --> n17
    n47 --> n20
    n47 --> n19
    n44 -->|"Partial"| n47
    n29 --> n38
    n19 --> n46
    n20 --> n46
    n46 --> n48
    n48 --> n55
    n55 --> n21
    n55 --> n23
    n55 --> n22
    n22 --> n39
    n21 --> n41
    n54 --> n31
    n14 --> n40
    n12 --> n34
    n11 --> n50
    n50 --> n12
    n27 --> n42
    n33 --> n11
    n50 --> n58
    n58 --> n1
    n1 --> n2
    n2 --> n51
    n51 --> n3
    n4 --> n35
    n3 --> n5
    n5 --> n52
    n6 --> n36
    n56 --> n16
    n56 --> n14
    n31 --> n57
    n57 --> n32
    n57 --> n13
    n32 --> n43
    n51 --> n4
    n52 --> n6
    n7 --> n8
    n9 --> n49
    n52 --> n49
    n49 --> n7
    n10 --> n9
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 serviceTask
    class n21 serviceTask
    class n22 serviceTask
    class n23 serviceTask
    class n24 serviceTask
    class n25 serviceTask
    class n26 serviceTask
    class n27 serviceTask
    class n28 serviceTask
    class n29 serviceTask
    class n30 serviceTask
    class n31 serviceTask
    class n32 serviceTask
    class n33 startEvt
    class n34 endEvt
    class n35 endEvt
    class n36 endEvt
    class n37 endEvt
    class n38 endEvt
    class n39 endEvt
    class n40 endEvt
    class n41 endEvt
    class n42 endEvt
    class n43 endEvt
    class n44 gateway
    class n45 gateway
    class n46 gateway
    class n47 gateway
    class n48 gateway
    class n49 gateway
    class n50 gateway
    class n51 gateway
    class n52 gateway
    class n53 gateway
    class n54 gateway
    class n55 gateway
    class n56 gateway
    class n57 gateway
    class n58 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWW1v4rgW_isWo1GpBHdixyHAh3tFKawqzUt36MxqtZ0PJnFKVJNEeWnLdvvf73GwQzDOapfhQ1Uen-e8PLaPnfDaC9KQ96a99-9f4yQup-j1otzwLb-Yoos1K_jFAO2B7yyP2Vrw4kLaRGlSruI_azNMsxdpJrEl28ZiJ9EVf0g5-nYzQDMgigEqWFIMC57H0cXgIsvjLct381SkubR-x8eRE9XR1NBVmoc8Pxg4jo8DD6giTvgBdn3q06XkFTxIk_DIaeRF4yi4eJPJifQ52LC8rNOvCv6JvfwWh-UGvkdMFBxsNuVWfGRrLmSNZV5JLKjyJy1GXMg4CQi2ylgQJw-AUwegnCWPB8hz3t7Q2_v390kTFN1d3ycIPoFgRXHNI1SUAC-eShTFQkzf0fls6TmDoszTRz59Rxb-tUsGgaxkCqU7Aynu8JnHD5tyuk5FqEyHz7KGKcleBvnLlDiDfAd_jVg8CQ-R5iMyJuMm0pWP53iuI0VR9FORQNf8jhWPKtbCXZLldRMLeyNv7pz602VeU3-GTZ14_hQHvOV0uVy6i4NUi5GHnW6nV0t35MwNpw-s5M9sd3A4mdPG4dLzl9jvdLiPZ2ZZrW_zNNAO3YW39BqH_hVezkinQzrDdKwyBD8POcs2CK1YhlYfKLpZoo8L3x-j_mrDhUC3giXlJdqby0-C6R9_3PciNo3YMEgf0C3PozTfol_uVuguZyFH83SbiZglAb_v_fjRpnrH1HnOQRl0k6zTKgnRNRfxE893EPsDvUTPcblJqxKxZIeynAc8hPWOwjT4j-l21JFRmoYF-grMOCtR_zsTFYQLa8doVTK5e0PItoC1mqdbFMt_L03nvpHzhgeP6NcKZInLHSpTtOY6cx6a5LE9sy9VaZR8XxEHu2hZgea_ljvTz8QqXKebW9js0ASlJ9T_mJYIm2UR5yc9fj7xiO21zu5ulWj9Ksk5LMs4kLNQlGnweKn9w4yb_sjZ64y4duptDFnAtEM18M-3LISSC9S_-fRh8dsnNISiA56UORNw0phTSahtHYBbkC4tiuG6Pj9QnDyl0D_-Z7LtK3_xkqXQrW_2JJMzsnKg6i3PAzkZiof60AxkgexkTvxuDfsqOBQtWM7KOE3QtxX6kghz9ZGxNREpotyRIoYNdPRlFoZwBlRb0499Fa8YnPKHWqSkn34foO8xLxO2HYDSccIMV66xfFebOEP9_Ya_KYrK1NI1FufNvAl4BT0U3aXTfd8zeR2LcPYV3UKzkBXL9TSroA_MBYc7S_Jguhj3Gxew5jOj3qAWQa62yzZpYpCMVc9PKdT5e0q9UbrZ2GAftu08TaI4355SyD8KqHx0hHXNsF9RBsKeGtLX18NEhHy4hktQsDk04qYFI9h7b29tqmen7vft_t53whnZOfwlEFUBgX7ZH-kmzT-PNj6L5rkHGsvz9LkYMlGiDHazEFx0kOg5JO8c0ugckv_vSNBnjKvMfHnzueXQh_V12K2wqlpjYxiTrTMu2ToWchXNEiZ2cPE-tpuA3ZwVGzTLYFkHda88tsCOdMV2Wzg_9I3j2IJO_u0cn5a2mt0eLmnYwdCv2zlACnXoJw7NMy8rJo5TIGBwesD3sbzE1Md5uwGBbd1Uj3tquyCw6DiL2_Mppatga8OZ1TrnWhajWlxRBZWQp8Ede-GG_Bhbz41vSaA7E_pw6FKqv36R27ow71Hn3ymw-_MnQavZZQKeB4yczTOA_nx_dT2LjxY76OKNDB5MC9rPEmzHU3Pf3salKl2pec457QGfQyLnkFqXnggeS3k-TDOeoAVZDMd0MUVf4VK8gV4RwEUMmkhYBWUzjT-MHQxPPmg4_K_siRrw9wClCqBUAn_d9-QjwH3vL_nwoG3HylYDxFXeXA1QZeFpQMUjOh4ZKcDX8TwV73NaRyONcxWNTBTgqWiEGoDrmL5-l9VLZzoP11GZai7WXJ0HVonhJjGlDHEMAE9MqdRDSR2Saj6ZqAiNfAqgjRaOAdCRITBVGni6Dk_riU3ANQGioxCVh06bYBWl8aFmzdUA1tOoS8faRyOf8uFpC0_VgpuwemFpwFWKY2xQPF2tp6pt0lCVaI_KvOGrcV25rqKZc2WvzdVX7U5p7WrxPb0ATgBdtKuL1lPsqRpdYgBY5-SqpKlrJN2sYWWggyoHWhK9ZCaGeQNQZdEsYyXqpPWmpp6u1gul4yHSPeR2D9HuIa97aNQ95HcPjbuHJp1DsLk6h7rVIN1qkG41SLcapFsN0q0G6VaDdKtButVwu9Vwu9Vwu9WA3axf5R7jVL12PUY9Kzqyor4VHVvRiQ2ljhXFVpRYUdeKUv0G9Rj27PDIDvt2eGyHJ1YYWqcVxnaY2GHXDtur9OxVevYqPXuV0OHVK-PeoAc38S2Lw970tVf_0gK_xoQ8YpUoe2-DHoML7GqXBL1p_YtEr6rfkl3HDB5Btnvw7f8ngdwU" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 E2E-_84A-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) — E2E-_84A-Final_Delivery_Plant_is_Non-S4_Plant_(Shell)

**Swim Lanes**: 
Sap S/4 IF
LE500 Ireland
 · SA S/4 IF
LE778 (China)
-Shell Plant
 · SAP S/4 IF
LE101 US | **Tasks**: 39 | **Gateways**: 16

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
    subgraph  Sap S/4 IF LE500 Ireland 
        n17[["fa:fa-cog Create Intercompany STR (SFG-01)"]]
        n18[["fa:fa-cog Create Inter Company STO (SFG-01)"]]
        n19[["fa:fa-cog Perform GTS Trade Compliance"]]
        n20[["fa:fa-cog Create Planned Order (SFG-01)"]]
        n21[["fa:fa-cog Perform Steps till Prod Order Execution"]]
        n22[["fa:fa-cog Create GR against Prod Order"]]
        n23[["fa:fa-cog Move to Unrestricted Stock"]]
        n24[["fa:fa-cog Check Quantity to be Delivered"]]
        n25[["fa:fa-cog Perform Outbound Delivery – Full Qty"]]
        n26[["fa:fa-cog Perform Outbound Delivery – Partial Qty (Lot N)"]]
        n27[["fa:fa-cog Perform outbound Delivery – Partial Qty (Lot 1)"]]
        n28[["fa:fa-cog Perform ATP Check (unrestricted stock) – S/4"]]
        n29[["fa:fa-cog Perform GTS Trade Compliance"]]
        n30[["fa:fa-cog Perform Pick and Pack Updates (IM/EWM - Decentralized"]]
        n31[["fa:fa-cog Check for Cross-border invoice?"]]
        n32[["fa:fa-cog Create Export Invoice"]]
        n33[["fa:fa-cog Create Commercial Invoice (Proforma)"]]
        n34[["fa:fa-cog Perform GTS (Export Declaration US Only"]]
        n35[["fa:fa-cog Create Sales Invoice (for MY, Vietnam, China"]]
        n36[["fa:fa-cog Create Packing list Packing list Addendum"]]
        n37[["fa:fa-cog Ship (Goods Issue"]]
        n38[["fa:fa-cog IC Invoice Bill To: LE778"]]
        n39[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n42(["fa:fa-play Planned order"])
        n50(["fa:fa-stop ATP Check Confirmed"])
        n51(["fa:fa-stop GTS Trade Completed"])
        n52(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n53(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n54{{"fa:fa-code-branch Quantity Delivered ?"}}
        n55{{"fa:fa-code-branch Cross-Border?"}}
        n56{{"fa:fa-code-branch exclusiveGateway"}}
        n57{{"fa:fa-code-branch exclusiveGateway"}}
        n58{{"fa:fa-code-branch exclusiveGateway"}}
        n64{{"fa:fa-arrows-alt parallelGateway"}}
        n65{{"fa:fa-arrows-alt parallelGateway"}}
        n66{{"fa:fa-arrows-alt parallelGateway"}}
        n67{{"fa:fa-arrows-alt parallelGateway"}}
        n68{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SA S/4 IF LE778 (China) -Shell Plant 
        n1[["fa:fa-cog Perform Repetitive Steps till order confirmation"]]
        n2[["fa:fa-cog Create Sales Order"]]
        n3[["fa:fa-cog Create Inter Company Stock Transfer Request (SFG-01)"]]
        n4[["fa:fa-cog Perform GTS Trade Compliance"]]
        n5[["fa:fa-cog Create Inter Company stock transfer (SFG-01)"]]
        n6[["fa:fa-cog Perform GTS Trade Compliance"]]
        n7[["fa:fa-cog Perform AR Posting and Auto Clearing"]]
        n8[["fa:fa-cog Perform Inbound Delivery (SFG-01) wrt STO"]]
        n9[["fa:fa-cog Perform Goods Receipt (SFG-01)"]]
        n10[["fa:fa-cog Write-Off Inventory"]]
        n11[["fa:fa-cog Perform GTS Trade Compliance"]]
        n40(["fa:fa-play Initiate IBD"])
        n43(["fa:fa-stop AR posting Completed"])
        n44(["fa:fa-stop Inventory Writ-Off Complete"])
        n45(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n46(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n47(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n59{{"fa:fa-arrows-alt parallelGateway"}}
        n60{{"fa:fa-arrows-alt parallelGateway"}}
        n61{{"fa:fa-arrows-alt parallelGateway"}}
        n69{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph SAP S/4 IF LE101 US
        n12[["fa:fa-cog Create Unconfirmed / Confirmed Sales Orders"]]
        n13[["fa:fa-cog Create Purchase Requisition (FG-01)"]]
        n14[["fa:fa-cog Create Purchase Order (FG-01)"]]
        n15[["fa:fa-cog Perform GTS Trade Compliance"]]
        n16[["fa:fa-cog Perform GTS Trade Compliance"]]
        n41(["fa:fa-play Confirmed sales orders"])
        n48(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n49(["fa:fa-stop GTS Trade Compliance Check Completed"])
        n62{{"fa:fa-arrows-alt parallelGateway"}}
        n63{{"fa:fa-arrows-alt parallelGateway"}}
        n70[["fa:fa-folder-open E2E-84E: R3 Physical Product Sales"]]
    end
    n13 --> n14
    n62 --> n15
    n14 --> n62
    n2 --> n59
    n59 --> n1
    n1 --> n69
    n3 --> n5
    n5 --> n61
    n17 --> n68
    n20 --> n21
    n21 --> n22
    n22 --> n23
    n23 --> n24
    n24 --> n54
    n54 -->|"Full"| n25
    n25 --> n58
    n30 --> n64
    n31 --> n55
    n33 --> n35
    n55 -->|"No"| n36
    n64 --> n31
    n64 --> n37
    n38 --> n39
    n55 -->|"Yes"| n32
    n39 --> n7
    n65 --> n38
    n37 --> n65
    n7 --> n43
    n59 --> n4
    n62 --> n2
    n58 --> n66
    n8 --> n60
    n60 --> n11
    n9 --> n10
    n10 --> n44
    n57 --> n27
    n57 --> n26
    n54 -->|"Partial"| n57
    n35 --> n34
    n32 --> n33
    n27 --> n56
    n26 --> n56
    n56 --> n58
    n66 --> n30
    n66 --> n28
    n66 --> n29
    n29 --> n51
    n28 --> n50
    n61 --> n6
    n61 --> n17
    n67 --> n19
    n69 --> n3
    n67 --> n69
    n16 --> n49
    n12 --> n63
    n63 --> n13
    n4 --> n45
    n6 --> n46
    n19 --> n52
    n42 --> n20
    n34 --> n53
    n11 --> n47
    n68 --> n18
    n68 -->|"Outbound Delivery against STO"| n25
    n18 -->|"Same STR/STO document 
will be visible in both LE’s"| n67
    n70 --> n12
    n63 --> n16
    n15 --> n48
    n41 --> n70
    n60 --> n9
    n40 --> n8
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
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 serviceTask
    class n21 serviceTask
    class n22 serviceTask
    class n23 serviceTask
    class n24 serviceTask
    class n25 serviceTask
    class n26 serviceTask
    class n27 serviceTask
    class n28 serviceTask
    class n29 serviceTask
    class n30 serviceTask
    class n31 serviceTask
    class n32 serviceTask
    class n33 serviceTask
    class n34 serviceTask
    class n35 serviceTask
    class n36 serviceTask
    class n37 serviceTask
    class n38 serviceTask
    class n39 serviceTask
    class n40 startEvt
    class n41 startEvt
    class n42 startEvt
    class n43 endEvt
    class n44 endEvt
    class n45 endEvt
    class n46 endEvt
    class n47 endEvt
    class n48 endEvt
    class n49 endEvt
    class n50 endEvt
    class n51 endEvt
    class n52 endEvt
    class n53 endEvt
    class n54 gateway
    class n55 gateway
    class n56 gateway
    class n57 gateway
    class n58 gateway
    class n59 gateway
    class n60 gateway
    class n61 gateway
    class n62 gateway
    class n63 gateway
    class n64 gateway
    class n65 gateway
    class n66 gateway
    class n67 gateway
    class n68 gateway
    class n69 gateway
    class n70 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtWm1v4jgQ_isWq1VZCbSxnRfgw50oharSdsuV9lan630wwSlRQ8LlpS3X63-_cbADuHa1x24_rDZjP-OZxzPjicNLK8wWvDVoffz4EqdxOUAvJ-WSr_jJAJ3MWcFPOmgr-J3lMZsnvDgRc6IsLWfxP_U07K6fxTQhm7BVnGyEdMbvM45uLzpoCMCkgwqWFt2C53F00jlZ5_GK5ZtRlmS5mP2B9yInqleTQ6dZvuD5boLjBDj0AJrEKd-JaeAG7kTgCh5m6eJAaeRFvSg8eRXGJdlTuGR5WZtfFfySPX-LF-USniOWFBzmLMtV8oXNeSJ8LPNKyMIqf1RkxIVYJwXCZmsWxuk9yF0HRDlLH3Yiz3l9Ra8fP96lzaLo5uwuRfAXJqwozniEihLE48cSRXGSDD64o-HEczpFmWcPfPCBjIMzSjqh8GQArjsdQW73icf3y3Iwz5KFnNp9Ej4MyPq5kz8PiNPJN_CvthZPF7uVRj7pkV6z0mmAR3ikVoqi6IdWAl7zG1Y8yLXGdEImZ81a2PO9kfNWn3LzzA2GWOeJ549xyPeUTiYTOt5RNfY97NiVnk6o74w0pfes5E9ss1PYH7mNwokXTHBgVbhdT7eymk_zLFQK6dibeI3C4BRPhsSq0B1ityctBD33OVsvEZqxNZp9dtHFBH0Ze46DLnKesHSBthPFX4qDP_-8a0VsELFumN2jUc7BMXSRljwPs9WapRs0u7lG7dnkvOvgT3etv_7ah_fscDRq8FdWfP8QP-V5lOUrdH4zQzc5W_BaSRKzNOQalDjGpafgYcoX6Eqkvm1Zgs3Lzkq-LlAJO4BgL5SS8TMPqzLOUl0LMVpwfo3YPYvTotxTokPpIfQye-SozNBtmnPY5DgswYVZmYUPOtDV1lzy8AH9VrG0jMuNUDHn6Iwn8SPP-UIHe2a3r6pynlUQGBK4QXcVcTBFkwqY-K3c6Hr8_6lnCoUKCrhQhdpfshJ9fbMjgVll9t0q325yz6xyeDOVtLWrfboLQfcnpR8SR9d3fKxSxwydxmCFyMgpg__crhcQPwVqX1x-Hn-7RF1wOuRpmbMEjkl9Myk2RQKohTjMiqI7rw8_FKePGRS_X3W0OXbHz-sMjpqLLUjHUCMGvF5BsRCbIXGoDYEvHGT6nlDXzmFbLg5OJyxnIuHQ7QxdpYkef9QzGjJj0FrsbBBUXP7RQb_HvEzZqgMMxSnTVfnmKgL7AScxSmKRxfsPw8UCzsJqpevR4ne2jNeofZ5lC7CoKKo3XGrBeTFqDD8V5ecmG0DRDoKejrME4fAaTbOiFGaKeBpWUAlGCYeGK73XVLik3ahYJ3CEqZKZyUL1aW-y5-wmQ4Ks97JnlKVRnK_qwDyAYA2iJQgv30LI-5A6p5plLTroT9Dhvrzs2F3w7hzasnC5q69NZUWQUK-v-1DPDN0m47YTfYPxzRj-HCZVAQudb5sMHRYcB-sdBfP3OGF5nj0VXZaUaA0pmiQ8sYC8Y0D-MaDgGFDv_4Eg47XmajbctVaQpahdF5dPqDtbctE9QEqVB32WOW2v-ZpDYAH5-73HtnKH2_xips7jnfpnajfo93Rp4vgTCZMWEYiv-d8VnI22Dso9-iz0vsOW-iiG1ydpi8UG_2gbgh8uopbe4iLVuhVlOnqCkw0aYU2NraWoz41rOP3jtXULsNZUfMvjknevokicJNA2ZLl-bmJ8NGOuox0aF_CmH9c7d3qmVVFXr8TA61ryaqu8rqthGh9qv2q3FFaHej9e-F3_J-gIfsIB1D-mmjnHgPAxILN5cWo7QUyFc7qrnNjB0OLtR6i5st2moWo20Odd47Ff8Qo91s01b1rlcJtS8Lq-xUVcd5ltc36572uQb5hmrHd0puHjy5qLtSTdMVXUTGWKqYO47f2E2O__uA6fHBOR9AhQsFc5I7ie4nk3W_MUjcm423PHA3QN75fLTRGHbHsRUIXlNtZ2hDeRDZGGut1fRLxIgU-kwFMz3K3AJ1IgJ3h9-ez1JUIB5Hw1LldQ-jw53EwPpKCn9DtbAVEziNRIGgukCYQqgVyDKC-INNpTAq8W_HvXErcCd61_xX2Cmist8pQBVBrgKzCVBngKQuV6tHHKk-q_ZrVy6is6pSEU64JA6epJQV_X9YfYMqFM-U0l0wrqS8tpY7niUtkln12q7ZW-22oFTxrjK_vVs6MAkhus_FGbryZgOcFtmJc2kEAX-PreyGuR2mmv4Uc52eyGtJk2uy8Vekoh8TWB52tb7EsBdTQB0WcQtS1Eeuo1YSm58RodKvK1Z9zslzQUK52-1Em1CU3uYGmF2wik834DUQmsBDK-XBUCSoOyCis_1J67KgaUH1Qlj1KJpSNu44h0HfcOBLCFb2_R1HVi3T_u5x1WmBlbcXFP-1nctS6ysFrx-v3jSbxOwI3gIxx18OEFTmo0z8olHL31NVd_mx2-MipQoUl0ahrXZSi5ymxXOhbo4a3oduVzb---W1S4vVv5gxFiHaHWEdc64llHfOtIYB3pWUf61hHIZuuQnQVspwHbecB2IrCdCWynAtu5wHYysJ0NYmeDvBMTdjaInQ1iZ4PY2SB2NoidDWJng9jZoHY2qJ0N-k6K2NmgdjaonQ1qZ4Pa2aB2NqidDagU6pPmoRxb5MQip_Jz5aHUNUo9o9Q3SgOjtGeU9k1SzzFKsVFKjFKjb3D8y--Rh2LPLPbN4sAs7pnFfaMYqr9RjM1iYhZTs9jspW_20jd76Zu99M1e-mYv4ZyUn2tbnRZ8_FixeNEavLTqXznALyEWPGJVUrZeOy0Gl0izTRq2BvWvAVpV_ZHnLGbwOrzaCl__A33GMkU=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| LE +++ – Plant 100X 

 | E2E-84C-Final_Delivery_Plant_is_Non-S4_Plant_(Shell),  | |
| SA S/4 IF
LE778 (China)

 | E2E-84C-Final_Delivery_Plant_is_Non-S4_Plant_(Shell),  | |
| SAP S/4 IF
LE101 US | E2E-84C-Final_Delivery_Plant_is_Non-S4_Plant_(Shell), E2E-84I-R3_-_Inventory_Transfer_Interim_State_Variation_-_3, E2E-_84A-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | |
| 
LE101 | E2E-84D-Final_Delivery_Plant_is_Non-S4_Plant_(Shell),  | |
| LE778 (Shell Plant)
 | E2E-84D-Final_Delivery_Plant_is_Non-S4_Plant_(Shell),  | |
| Boundary Apps | E2E-84F__R3_SAP_TM_-_Embedded,  | |
| EWM 
(De-Centralized) | E2E-84F__R3_SAP_TM_-_Embedded,  | |
| External Partners/B2B | E2E-84F__R3_SAP_TM_-_Embedded,  | |
| SAP S/4 Intel Foundry - LE500 Ireland
 | E2E-84F__R3_SAP_TM_-_Embedded,  | |
| 
Sap S/4 IF
LE778 (Shell Plant)
 | E2E-84I-R3_-_Inventory_Transfer_Interim_State_Variation_-_3,  | |
| CFIN | E2E-84I-R3_-_Inventory_Transfer_Interim_State_Variation_-_3,  | |
| 
Sap S/4 IF
LE500 Ireland
 | E2E-_84A-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | |
| SA S/4 IF
LE778 (China)
-Shell Plant
 | E2E-_84A-Final_Delivery_Plant_is_Non-S4_Plant_(Shell) | |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
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

    subgraph E2E84CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E84CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E84CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E84CDAA_e_g_XEUS -.-> E2E84CDAD_e_g_Azure_SQL
    end
    style E2E84CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E84CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E84CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E84CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E84CDAA_e_g_MES_300 -.-> E2E84CDAD_e_g_SAP_HANA
    end
    style E2E84CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E84CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E84CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9P2kAUx_-VyxnCloCrYEGbaHLQMk2qcRa3JXZpjvYVLh5t014niPzvu2uhbkid8S5puPfj-14_rzlW2I8DwAZuNFYsYsJAq6aYwRyaBmpOaAbNFmpm4OcpE0sbfgNXDh7HpacI_U5TRiccsqbKDuNIOOypEDjSk4UKU7YRnTO-VFYHpjGgu8sWIjKRN9cqgseP_oymotDIM7iiix8sEDN5DinPQMbMxJzbdAJcFRJprmyR7N5JqM-iqTR2dWlKafTwYjrW12u0bjTcqCqBxgM3QnL5nGaZCSGiSTKIFyhknBsHA90cjUatTKTxAxgHmtbvD3qbY_tR9WR0kkXLj3mcKnfX1Hf1gslwyTdyRDd7pF_Jday-2e3Uyh0NdKuj7chBzF_aG40G-kCv9IZDTa5avV5Pud2oVMzyyTSlyQxZHevkeGiSoe2BN_XIU56C53yz712MXPyrjFYrYCn4gsVRBU2tbTopsn9ad45MhMPpIVK_pYBhGCXT1znmTsVPLnbz4KQbyGfgH7t5CJp8ZSVWBCEZ5OLPSrLA-lYXqH3YPq-rVCZCFGxYiCWHWhBb2ETtCralqf0v7KNk8T-8DrnxLsg1-RDdK8vxupq2BSyPSB7fw7gq-wZiGYNUzHsIbzrZB3lb6j2Mt7EfQry_LDo7O3_eADILpugLIjeX8jliHFz8XP9R7IzOhqls__4vYn6gIZOMCSK3w4vLsTUc391ayLa-WtdmzTTt2xer7am5kyThzKfKu390tmfWzMmkgqqbeP-IbM-S8lYUtOOwbbMQSvnyytg7jvINt_R1tSv6p6enr9DjFp5DOqcswMYKFze-_L8IIKQ5F3jdwjQXsbOMfGwUlzLOk4AKMBmVROelcf0HboH1hw==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E84FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E84FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E84FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E84FDAA_e_g_XEUS -.-> E2E84FDAD_e_g_Azure_SQL
    end
    style E2E84FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E84FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E84FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E84FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E84FDAA_e_g_MES_300 -.-> E2E84FDAD_e_g_SAP_HANA
    end
    style E2E84FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E84FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E84FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9P2kAUx_-VyxnCloCrYEGbaHLQdppU4yxuS-zSHO0rXDzapr1OEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHfgNXDp4klacM_U4zRscc8qbKjpJYuOypFDjS07kKUzabzhhfKKsLkwTQ3WULEZnImysVwZPHYEozUWoUOVzR-Q8Wiqk8R5TnIGOmYsYdOgauComsULZYdu-mNGDxRBq7ujRlNH54MR3rqxVaNRpeXJdAo4EXI7kCTvPchAjRNB0kcxQxzo2DgW7att3KRZY8gHGgaf3-oLc-th9VT0YnnbeChCeZcndNfVsvHA8XfC1HdLNH-rVcx-qb3c5euaOBbnW0LTlI-Et7tj3QB3qtNxxqcu3V6_WU24srxbwYTzKaTpHVsU6ObZMMHR_8iU-eigx895tz72Hk4V9VtFohyyAQLIlraGpt0kmZ_dO6c2UiHE4OkfotBQzDqJi-zjG3Kn7ysFeEJ91QPsPg2Csi0OQrK7EyCMkgD39WkiXWt7pA7cP2-b5KVSLE4ZqFWHDYC2IDm6hdw7Y0tf-FfZTO_4fXJTf-BbkmH6J7Zbl-V9M2gOURyeN7GNdl30AsY5CKeQ_hdSe7IG9KvYfxJvZDiHeXRWdn589rQGbJFH1B5OZSPm3GwcPP-z-KrdE5MJHt3_9FLAg1ZJIRQeR2eHE5soaju1sLOdZX69rcM03n9sXq-GruJE05C6jy7h6d45t75mRSQdVNvHtEjm9JeSsO20nUdlgElXx1ZewcR_WGG_q62jX909PTV-hxC88gm1EWYmOJyxtf_l-EENGCC7xqYVqIxF3EATbKSxkXaUgFmIxKorPKuPoD6ib1sQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-84-R001 | Report | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-84-C001 | Conversion | Legacy data migration for Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-84.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E84C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E84C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E84CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E84CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E84C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E84CMW_e_g_Azure_Service_Bus
    E2E84CMW_e_g_Azure_Service_Bus --> E2E84C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTves74M_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPGco9iQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-84.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E84F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E84F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E84FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E84FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E84F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E84FMW_e_g_Azure_Service_Bus
    E2E84FMW_e_g_Azure_Service_Bus --> E2E84F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTvds4IM_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPYDs9oQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-84-I001 | Interface | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-84-E001 | Enhancement | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-84-F001 | Form/Report | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
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

    subgraph E2E84CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E84CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E84CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E84CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E84CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E84CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E84CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E84CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuDe2AqwTjvM13pd1JRsmBQa2p1zgsR0ccOMByVG1WmtJCsKdsqNYIlB3R7rSNXLmRaqyoYf0hXpBIdo6nhhmx-0EysZJwTVoOsWYk1m5EFMLWRqBqlFdJ9VJKUFkspjgwpVaS4O0q20baoHQzi4rAF-ubFBZIjZaSup5AjUpYe36CcMuacefY0DEO9FhW_A-fMMC4vvfE-_PCgPDlmudFTznil0tbUfs0rGRFHoD8Jxv7HA9CaTALLfwm0jsChZwem8QoInB15YejZnn3g-b4hx0mD47FKx0VPrJvFsiLlCgVmMBn589k8gWSZuI9NBcmckOhXjOPGHBvDuMnBkDufL89Rl0YqHePfPUiNjFaQCsoLNPt6VJ_Jbkf-GdwqZodR3xLgOE7f8H4NFNnem9gyOGnsn5r55uGjZJR8dr-4iWmYVnf-bGJlcs6I_XcXoosRUnVI1b27ETdBlFiG8dwLGSIZvrMdL6z-h468Rb-6-vS0NzvtzocukDu_lnNIGcT46eRVYR2voVoTmmFnh7s3Qr4wGeSkYQK3OiaN4NG2SLHT_ca4KTMiYEqJvJ51L7Z_AKh8bno=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E84FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E84FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E84FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E84FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E84FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E84FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E84FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E84FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DPTCVYJz3ma70O6koWTKoNbU644UI6WMHGI7KjSpTWkByyrZKDWHFAd1e68iVC5nWqgrGH5I1qUTHaGq4IZsfNBVrGWeE1SBr1iJnc7IEpjYSVaO0QroPS5LQYiXFkSGlihR3R8k22ha1g0FUHLZA37yoQHIkjNT1DDJEytLjG5RRxpwzz54FQaDXouJ34JwZxuWlN96HHx6UJ8csN3rCGa9U2prZr3klI-IInE788fTjAWhNJr41fQm0jsChZ_um8QoInB15QeDZnn3gTaeGHCcNjscqHRU9sW6Wq4qUa-Sb_mQULOaLGOJV7D42FcQLQsJfEY4ac2wMoyYDQ-58vjpHXRqpdIR_9yA1UlpBIigv0PzrUX0mux35p3-rmB1GfUuA4zh9w_s1UKR7b2LL4KSxf2rmm4cP41H82f3ixqZhWt3504mVyjkl9t9dCC9GSNUhVffuRtz4YWwZxnMvZIhk-M52vLD6HzryFv3q6tPT3uysOx-6QO7iWs4BZRDhp5NXhXWcQ5UTmmJnh7s3Qr4wKWSkYQK3OiaN4OG2SLDT_ca4KVMiYEaJvJ68F9s_y01ukg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
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
*E2E-84 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

