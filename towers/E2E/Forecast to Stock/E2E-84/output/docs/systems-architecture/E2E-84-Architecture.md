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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWWtv2zgW_SuEiyIOam9FUi_7wy4cxy4CtNNMnHZ2MOkHWqJjIbLk1SOJN5P_vpcyKTs0GXSd-kMQHfHcx-HlJSU9daI85p1h5_37pyRLqiF6OqmWfMVPhuhkzkp-0kNb4DsrEjZPeXkixizyrJol_22GYXf9KIYJbMpWSboR6Izf5hx9u-ihERDTHipZVvZLXiSLk97JukhWrNiM8zQvxOh3PFw4i8abvHWWFzEvdgMcJ8CRB9Q0yfgOpoEbuFPBK3mUZ_ELowtvES6ik2cRXJo_REtWVE34dcm_sMc_krhawvWCpSWHMctqlX5mc56KHKuiFlhUF_dKjKQUfjIQbLZmUZLdAu46ABUsu9tBnvP8jJ7fv7_JWqfo-vwmQ_CLUlaW53yBygrgyX2FFkmaDt-549HUc3plVeR3fPiOTIJzSnqRyGQIqTs9IW7_gSe3y2o4z9NYDu0_iByGZP3YKx6HxOkVG_ir-eJZvPM09klIwtbTWYDHeKw8LRaLN3kCXYtrVt5JXxM6JdPz1hf2fG_sHNpTaZ67wQjrOvHiPon4ntHpdEonO6kmvocdu9GzKfWdsWb0llX8gW12BgdjtzU49YIpDqwGt_70KOv5ZZFHyiCdeFOvNRic4emIWA26I-yGMkKwc1uw9RJ9nqAPHz6gm5o4mKLLlGUVArf_hjHbkeKXYf-vv246CzZcsH6U36JxwSEzdJFVvIjy1ZplGzS7vkLd2fRT38GnN50fP_bpgZ0-bulfrfTwJf2SF4u8WKFP1zN0XbCYI2EkTVgWcZ06sHie53UWo3OeJve82IDnj-4pekiqZV5XSMSzLnjEY1hoKM6jf2hmiWOJKM_jEl0BM1lXqPudpTW4ixvDaFYx0TZiiLaERVLkK5SIf_V0CdZiXvLoDv1ew9Qk1QZVOZpzFTmPdTIxR_a1rrSU5ZRP6zRFv1cb3Q41Cmc1cwldBrqvsIS6n3MoooO03Dda_O3AomfOdXR9KUXr1lnBYT0kkZiFssqju1NlH2Zct-cfXWckMFMvE4gCph2ygX--rWNIuUTdiy8fJ398QX1IOuJZVbAUtriDqQxNdQBmQbq8LPvzZuNCSXafQ-P6l842V_7kcZ3DNnGxJWkc6hg5kPUK1rmYDMlDXehCIkGmzwnFdg270jkknbKCVUmeoW8z9DVL9eqjxBiIEFGsyDSBBfTiYhTHsPnUK92OuYpnDI4Xu1yEpF_-7KHvCa8ytuqB0knGdFNa-c6WyRp1twv-oizrAy214rwYtw7PoHmj63wIzTcIQp1nKcLRFbqEZiEyFvU0qqEPjFMOh6XsVjPhBt3WBNT8Wss3akQQ1Xa6Two1klb13EAZaJTdwhvn2SIpVgcUz3ndS7O2rA49_FNsGYHFBn162ukb8_4cDlXRctdf286KYEk9P-9TXTN1uxy358gDjmfm8McorUtw9Gl7RNBp_nG04DhaeBxtcBTN35ORFUX-UPZZWqE1tIQ05amF5B1D8v8_ErQQ7Xg0G4l9Al1Mt2sVdZvWcPrycGResFd8zaGgQAbY-fm6RJVY9tueHW2XR9MC9b79Ssf6Ksh6v_iZo5X1ZOYeveN5bzrSHb_TBm9uj5bTpOFMuA0dPcCeBbloZgY_dQS0nGido_One819ncKzxQU8TSeN9mfnWq-jBw36Cq2lStamftChdwndH47WO3JTotb275K3N3CX_gIb7i_YSMhx3c85ppHhtzeyy10nww6Gg9d-PWLjav6WRWoi0cfdpO53o1KvbMvJrS6iJSs51NF_6qRMmrNf17w26OsWthVm4R7fz7B3_JIMtSWpKaUXn_cLCth_uw2fHFOJ9BjSXtNe5CnMXz9f8wxNyKQfupMhuoLHveWmTCJ4xIAni7iOqla6H1pJQ4mhfv-folAk4CvAVSPoFvCJBOQA31EMRzLktbe99NR47EsgUMBgC6gXUfCQLkeoILzG5983HfFAfdP5WzyKq7HSvTdQQCDjUQGTUI5oAemPKn9URkzbkF3p77e88UaVNyq90VYeV8YeagB1dVt_CsVF6CpSKoVQOlBJ9T0JyEzoQFPW1eZGRScT9VUavtQROxrQaiUNEsWQyriK4MkQiasDB1MjXyk0KXq-SkkWi9vOtbxWDokc4KmciasBnqdNsCeD9JUTX8Xk6UCgA4pCJOCqaSPSi6u8YFU1rXZyBG0DU4WvXeMWkPOHgxcAaHX4XobdsiQr5VFov749GQdWkWJlZMZWXBw_P4qjYJxH9YpnFZydH8RReM7RPWwF85SjJEPzvBJvI5uXM4NtFXqh5kBNKFZKqDyxnDO_rXk5Z5joQEuRk-gqKdR1y5DXrVNV2arOqGoBqlCokr-ddaVuO0KVf6BL1y44SQn3XvyKktx7Pf3iDrHeodY7rvWOZ73jW-8E1juh9c7AegdUtt6yq4DtMmC7DtguBLYrge1SYLsW2C4GtqtB7GqQV2rCrgaxq0HsahC7GsSuBrGrQexqELsa1K4GtatBX1kidjWoXQ1qV4Pa1YCFrT7FvcRDCz6Qn9NeLl3HiGIjSowoNaKuEfWMqG9EAyMaGlFjbp4xN8-YG2xk8tvaS5iaYdcMe2bYN8OBGQ7N8MAIw_HICGMzbM7SN2fpm7P0zVn65ixhy5LfGDu9zooXK5bEneFTp_k03xl2Yr5gdVp1nnsdVlf5bJNFnWHzCbtTN183zhMGT5yrLfj8PxQayaM=" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWVtv27gS_iuEiiIOYJ-IpGTJfjgLx5dugHSbrdMuFpt9oCU6JiJLhi5JfNL89zOUSTmmxS7WbR6S6CPn9s1whrJfnCiLuTN03r9_Eakoh-jlrFzxNT8borMFK_hZF-2ArywXbJHw4kzuWWZpORf_q7dhb_Mst0lsxtYi2Up0zu8zjr5cddEIBJMuKlha9Aqei-VZ92yTizXLt-MsyXK5-x0Pl-6ytqaWLrM85vl-g-sGOPJBNBEp38M08AJvJuUKHmVpfKB06S_DZXT2Kp1LsqdoxfKydr8q-Ef2_IeIyxU8L1lScNizKtfJNVvwRMZY5pXEoip_1GSIQtpJgbD5hkUivQfccwHKWfqwh3z39RW9vn9_lzZG0e3kLkXwEyWsKCZ8iYoS4OljiZYiSYbvvPFo5rvdosyzBz58R6bBhJJuJCMZQuhuV5Lbe-LiflUOF1kSq629JxnDkGyeu_nzkLjdfAu_DVs8jfeWxn0SkrCxdBngMR5rS8vl8ocsAa_5LSselK0pnZHZpLGF_b4_do_16TAnXjDCJk88fxQRf6N0NpvR6Z6qad_Hrl3p5Yz23bGh9J6V_Ilt9woHY69ROPODGQ6sCnf2TC-rxU2eRVohnfozv1EYXOLZiFgVeiPshcpD0HOfs80KoespdhUX8ifFf_115yzZcMl6UXaPxjmHGNCcwYFEn-RJKe6cv_9-I0AOBW54vszy9W4v-soSEbNSZCnqiDRKqhhKVyqNRYlYGqMPt3MUrXj0UJwbeumh3s884uKRo_HtDfqyAZ3cdMT7niPjLF2KfF27Ysj57XLSs9ucxWAyW28SwdKIG5L9dsnRZ3STFaWMVIY4qsoMjRMOfS29NzQE7UF2voq8rFhichIebp-vxAZ1PmRZXKCroqi4uX_QmsxxVZTZGki5Sh8zcRQVdk8mBJvVw5KoSqTNW_Z8lDBslM5Y1gH6vWJpKcotAtYWHE14AoxAwZjC1JLuywm6q4iLKZpVSYJ-L7empK1QqnKRVZCweGdyq_XcQAeFySJVoc51ViJs8oz9f3TmSMlvRwXvdxolmwS6xhXMSSHJK-rTV88pkDl_KxPsZSCpG1l7G1V7dZZ4WTN3IBMaMm2JVcmw6hj8uA7Pf3nZkxbz3gLGW7TaF0CTevTLnfP6-la03y7Kn6HFFCD0Ydd4TbHgNLHwJDGf7MVYnmdPRY8lJdqwnCUJTyxC9N8Jwcg1Ovr1NAhC1JmvOFT_TQJcnqO3pdpv7QlX6a72J7r2O_ML7xw9iXKVVbJVb9Emh-5U9-84i_5jnoDA0jTq5lT3tU0JfY0lFZiLa8VoXjJ5kYqhRAq4NuTZGgn579HxCn-kUQxObRTE_emNguCf0CiIZeSOYDTuqOlUac7hHiAiyTUc0OjhXOuHvJr66MkNn1h66Y0AL-Twu2Hwj5rXqHP18WL6x0fUg2RFPC2hpuFqbyaM-G3ZBrVQq1lR9BZ1I0RiN7x-MaXb63v6vMngetw-8UjQPiezNUzJSCZDyaEO3L5kgOwoJ2GrChm-PDGJgAI_eBjFMZzdam3qGXzn_tV4Icn4-GcXfRW8TNm6CxyJlJnzxP2H24K531KbyurFJdw5pfvyL7rNhrurY61WPulbxcWn-ejWVE1--KZETy9S6tlFO6owoCAT6LH1TfXLHH1KE7Mb0L5tPF9dTszR5v77sexhQ0aXy7Usl7oOpHNa3JQmP2Eg05-gwwMVUzLthd6vvc_QzVbbQkRwguDgxFVUqrtMh15QeYTeSg5Ovg74brvorl_sXvCPZPBpQ907Zaj7pwj1TxEKThEKT7xzpAT1ev-Fo6EecX_37PsaCHeAN1CAN5DAtztHjtw755scz3rvQAljrRybgDJHtD1f7SBE7_CUiKcBXwGuBpSLJNA6lAjVO9QGGphGtE4c7AAcKoCqILWAsokDA6CN365i4U_5TvRNemWu_JbtFhobmoxmp_ZTx04VO55rREZ0NohynDTZ0JFoEZUCjM10qUtJ7ZOv4yI6u3q7r1xo0q8eibGun5V5T8fkGc9E-UM1tdRVGkODhYYVHSI2AR2ipySwdsLzj0qSmksH4TdZVHnHTWHoDPjmjoYQVQmephB7JkANQNdOUwi6uvSzjkdTQLWG5lBooHFc5Y1iA2icUDRTXSg60doJTwHN2cXmBkV747WO03vzgZYskDcfux2sEOsKta541hXfutK3rgTWldC6MrCuAKXWJTsL2E4DtvOA7URgOxPYTgW2c4HtZGA7G8TOBvlOTdjZIHY2iJ0NYmeD2NkgdjaInQ1iZ4Pa2aB2Nuh3joidDWpnAzqL_rLgEO9b8EB94H-Ihq3ooA313FYUt6KkFaWtqNfuMfRz9Yn8Idxvh4N2OGyHB60wDPRWGLfDpB2m7bDXDrdH6bdH6bdH6TdROl0H3urWTMTO8MWpv6Jzhk7Ml6xKSue16zB4a5tv08gZ1l9lOVX9tj8R7D5n6x34-n_sOpdN" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWFtv4jgU_itWRt1SCUSuBHhYCQLMVOpMq9JOH6b74AanWA1x5DgUttP_vseJHcClD8v0YTT5cr5zP8cOb1bMFsQaWmdnbzSjYojezsWSrMj5EJ0_4YKct1EN_MSc4qeUFOdSJmGZmNN_KzHHzzdSTGIzvKLpVqJz8swIur9soxEQ0zYqcFZ0CsJpct4-zzldYb6NWMq4lP5C-omdVNbUqzHjC8J3ArYdOnEA1JRmZAd7oR_6M8krSMyyxYHSJEj6SXz-Lp1L2Wu8xFxU7pcF-Y43D3QhlvCc4LQgILMUq_QKP5FUxih4KbG45GudDFpIOxkkbJ7jmGbPgPs2QBxnLzsosN_f0fvZ2WPWGEVXt48Zgr84xUUxIQkqBMDTtUAJTdPhFz8azQK7XQjOXsjwizsNJ57bjmUkQwjdbsvkdl4JfV6K4RNLF0q08ypjGLr5ps03Q9du8y38a9gi2WJnKeq5fbffWBqHTuRE2lKSJH9kCfLK73DxomxNvZk7mzS2nKAXRPZHfTrMiR-OHDNPhK9pTPaUzmYzb7pL1bQXOPbnSsczr2dHhtJnLMgr3u4UDiK_UTgLwpkTfqqwtmd6WT7dcBZrhd40mAWNwnDszEbupwr9keP3lYeg55njfInGrKx6GY3yvKjfyb_MGfx6tG5lp8c0JSi6m1MUYc4p4egyWzNIFcLZAk1okZeCoO84w88wvZl4tP7Z0-PatR5C1wRxrW9h6moVFw0PushwcvrwHaHWhHQi0M9xCvtgcbHvrFsZSQnsEfSA17VrNzR-QQ_fUFXSiBMsKMsOvXM8IB7KsSyhfFXJotbdbffu-sLg-JKDgdOaL2mewyyiapjRDaeZgMeL2jyIVO9oYeTECaQGwhPGV-iK4QWIGRI9KcEKgb4ytijQZVGUBLUgD6YzIQhel-JJlhFNSApphmK2ricX6JWKJfp2D6jANC0MYn-vLh8VXMudiGgmU39I9N23t0crwcMEd6CG7LXo4FSgHENdUpJ-rTv-0Xp__7SaG0F4hiFfsJkywovu2B3vt4wDrs2BhwRD89ENGvs_royukgX_wQRNtiiuO8kQkIWNcC5KTsxeK1BrTTGaTi4Ry9KtkVHX32NONyQuq1Yga2i9Akni-Id_1fl6d2fwgj3ezXJb0BhC5DLDuUAMdkFVSQwrehqGfYPcb_3SSc1TWBgTLDDKCAEGJOGJIMiHkP9Vudjvfs_ekQvB8p31W2VdubUwid6ulPJ07jzB-RIvEdnEaVlAI3woZt0B3v_rgJrk_2nbyE6Yd32oooBZm8l-hUbtQDoD20aXnKRy6vZbXBZEjv2xBm-BKrPyjXz3Pl9I2oxXpxO6hwtLNdMaqMbjkO3tzbRuuDmspLhqH0mOcBqXqdQbwVH9TIyJ9HXXq40AgcImLyt-1QUfRjHQjFtQWnSV1mHjJfjyiqWn0PEPsAxgnO_MBSIXjVxjqLW3aQwZuWPqSSCHGajCUrmaCyzKAtVL6_JQQX9XiT2GVjUnQqTV0YEmLC4_niGDHX1en9Lo5rqLpnAWbNF8SYi5X229PUdxzEsYBMietjbd5CSDYwJeQUeI_YOnJsu2GaUpi_d9jEBbVYSmgS4FWUFeo-vuzegCMQ4nIKw1uICinzgtj5w1bs-Y8Y9NCQWrzrp65OuQzaF1Q0PNQfGrnbG3MkzywFgVOkEyW0Dc7_E6ZJ2JD7vDOWl3eO5pNP-EleMFp5B6p5DCU0j9U0iDU3avfQrJOXFhw6UKdTp_y4uSBlwFeBoIa8B3FeBriUBL1M-eVqHee_q959eAVqBMNuJ9Ja8tKoNeX8srAd_RgNLgNkCgKBpQjIF6HKjX-tlTgGObgFbgqKB8LeHYBuDpsHUYmtEAKg--DtTXedASvo5DS3iKEpoMnUpXB6q98JVbrg7N7alItN8qFY7OvqNUOD3DiyZ5jkqG2xhRoemCaCe0BldVrCl4z9BYA7_hEiv3n1x58I0C585vOY4HboAM3PW68IUCm64ScBvHVTKchmE0pu4zR_vpKD-0n9qthqD8dgYHnQY-jBl76d7BmMC5Cd4-ZvqWoO-Ute9NqX3Fu7meNBe5aXULrQW1RVfnWsfg2mZvB0rV7Bq1Dg7wC4T-Qt9GD3D9bn1jpTwWKZcfrGP4vryAI636vDlIavUpWvWE_mXhEA8_wfuf4AP1q8EB6tlHUUd_UB_C7nHYOw77x-HgONw7DofH4f5xeHAUhjk7Ch-P0j8epX88Sr-J0mpbKwIftHRhDd-s6hc2a2gtSILLVFjvbQuXgs23WWwNq1-irLK6nU0ohmv3qgbf_wNXSwZc" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWW1v4rgW_itWRqNSCe7EjkOAD_eKUlhVmpfu0JnVajsfTOKUqCaJ8tKW7fa_3-NgBzDOapfhQ1Uen-e8PLaPnfDqhFnEnYnz_v1rkibVBL1eVGu-4RcTdLFiJb_oox3wnRUJWwleXkibOEurZfJnY4Zp_iLNJLZgm0RsJbrkDxlH3276aApE0UclS8tByYskvuhf5EWyYcV2lomskNbv-Ch24yaaGrrKiogXewPXDXDoA1UkKd_DXkADupC8kodZGh05jf14FIcXbzI5kT2Ha1ZUTfp1yT-xl9-SqFrD95iJkoPNutqIj2zFhayxKmqJhXXxpMVIShknBcGWOQuT9AFw6gJUsPRxD_nu2xt6e__-Pm2Dorvr-xTBJxSsLK95jMoK4PlTheJEiMk7OpsufLdfVkX2yCfvyDy49kg_lJVMoHS3L8UdPPPkYV1NVpmIlOngWdYwIflLv3iZELdfbOGvEYun0T7SbEhGZNRGugrwDM90pDiOfyoS6FrcsfJRxZp7C7K4bmNhf-jP3FN_usxrGkyxqRMvnpKQHzhdLBbefC_VfOhjt9vp1cIbujPD6QOr-DPb7h2OZ7R1uPCDBQ46He7imVnWq9siC7VDb-4v_NZhcIUXU9LpkE4xHakMwc9DwfI1QkuWo-UHim4W6OM8CEaot1xzIdCtYGl1iXbm8pNi-scf907MJjEbhNkDuuVFnBUb9MvdEt0VLOJolm1ykbA05PfOjx-HVP-YOis4KINu0lVWpxG65iJ54sUWYn-gl-g5qdZZXSGWblFe8JBHsN5RlIX_Md0OOzLKsqhEX4GZ5BXqfWeihnBR4xgtKyZ3bwTZlrBWi2yDEvnvpek8MHJe8_AR_VqDLEm1RVWGVlxnziOTPLJn9qWujJLva-JiDy1q0PzXamv6GVuF63RzC5sdmqD0hHofswphsyzi_qTHzycesb3W6d2tEq1XpwWHZZmEchbKKgsfL7V_mHHTHzl7nRHPTr1NIAuYdqgG_vmWR1ByiXo3nz7Mf_uEBlB0yNOqYAJOGnMqCbWtA3AL0mVlOVg15wdK0qcM-sf_TLZ95c9f8gy69c2OZHKGVg5UveFFKCdD8VAPmoEskJ3MSdCtYU8Fh6IFK1iVZCn6tkRfUmGuPjKyJiJFlDtSJLCBjr5MowjOgHpj-rGv4iWDU35fi5T00-999D3hVco2fVA6SZnhyjOW73Kd5Ki32_A3ZVmbWnrG4ryZtQGvoIeiu2yy63smr2MRTr-iW2gWsmK5nqY19IGZ4HBnSR9MF6Ne6wLWfG7UGzYiyNV2eUgaGyRj1fNTCnX_ntJslG42Ntj7bTvL0jgpNqcU8o8CKh8dYT0z7FeUg7CnhvT1dT8RER-s4BIUrveNuG3BCPbe29sh1bdTd_t2d-874QztHP4SirqEQL_sjnSTFpxHG51F8709jRVF9lwOmKhQDrtZCC46SPQckn8OaXgOKfh3JOgzxlVmtrj5fOAwgPW1362wqg7GRjAmW2dSsVUi5Cqapkxs4eJ9bDcGuxkr12iaw7IOm155bIFd6YptN3B-6BvHsQUd_9s5Pi1tOb3dX9Kwi6FfH-YAKTShnzg0z6KqmThOgYDB6QHfw_IS0xznhw0IbJumetxTDwsCi46z-HA-pXQ1bG04sw7OuQOLYSOuqMNayNPgjr1wQ36MrefGtzTUnQl92Hcp1V-_yG1dmveo8-8U2Pv5k-Cg2eUCngeMnM0zgP58f_V8i48DdtjFGxo8mBa0myXYjqfmgb2NS1W6UvPdc9oDPodEziEdXHpieCzlxSDLeYrmZD4Y0fkEfYVL8Rp6RQgXMWgiUR1W7TT-MHYwPPmgweC_sidqINgBlCqAUgn8de_IR4B75y_58KBtR8pWA8RT3jwNUGXha0DFIzoeGSog0PF8Fe9z1kQjrXMVjYwV4KtohBqA55q-fpfVS2c6D89VmWou1lydB1aJ4TYxpQxxDQCPTanUQ0kTkmo-GasIrXwKoK0WrgHQoSEwVRr4ug5f64lNwDMBoqMQlYdOm2AVpfWhZs3TANbTqEvH2kcrn_Lhawtf1YLbsHphacBTimNsUHxdra-qbdNQlWiPyrzlq3Fdua6inXNlr83VV-1Oae1p8X29AE4AXbSni9ZT7KsaPWIAWOfkqaSpZyTdrmFloIMqB1oSvWTGhnkLUGXRLmMl6vjgTU0zXQcvlI6HSPeQ1z1Eu4f87qFh91DQPTTqHhp3DsHm6hzqVoN0q0G61SDdapBuNUi3GqRbDdKtBulWw-tWw-tWw-tWA3azfpV7jFP12vUY9a3o0IoGVnRkRcc2lLpWFFtRYkU9K0r1G9Rj2LfDQzsc2OGRHR5bYWidVhjbYWKHPTtsr9K3V-nbq_TtVUKHV6-Mnb4DN_ENSyJn8uo0v7Q4EyfiMatF5bz1HQYX2OU2DZ1J84uEUzdvya4TBo8gmx349n8ngdwU" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWm1v2zYQ_iuEiyIuYKMiqRfbHzY4jh0EaBovTlYMyz7QMhULkSVPL0m8LP99R5mUbYYMOrf9UFQP-RzvHt4dKbkvrTBb8Nag9fHjS5zG5QC9nJRLvuInA3QyZwU_6aAt8DvLYzZPeHEi5kRZWs7if-pp2F0_i2kCm7BVnGwEOuP3GUe3Fx00BGLSQQVLi27B8zg66Zys83jF8s0oS7JczP7Ae5ET1avJodMsX_B8N8FxAhx6QE3ilO9gGriBOxG8godZujgwGnlRLwpPXoVzSfYULlle1u5XBb9kz9_iRbmE54glBYc5y3KVfGFznogYy7wSWFjlj0qMuBDrpCDYbM3COL0H3HUAyln6sIM85_UVvX78eJc2i6Kbs7sUwZ8wYUVxxiNUlACPH0sUxUky-OCOhhPP6RRlnj3wwQcyDs4o6YQikgGE7nSEuN0nHt8vy8E8SxZyavdJxDAg6-dO_jwgTiffwN_aWjxd7FYa-aRHes1KpwEe4ZFaKYqiH1oJdM1vWPEg1xrTCZmcNWthz_dGzlt7KswzNxhiXSeeP8Yh3zM6mUzoeCfV2PewYzd6OqG-M9KM3rOSP7HNzmB_5DYGJ14wwYHV4HY93ctqPs2zUBmkY2_iNQaDUzwZEqtBd4jdnvQQ7NznbL1EaMbWaPbZRRcT9GXsOQ66yHnC0gXaThR_Uhz8-eddK2KDiHXD7B6Ncg6BoYu05HmYrdYs3aDZzTVqzybnXQd_umv99dc-vWeno1HDv7Ly-4f8Kc-jLF-h85sZusnZgtdGkpilIdeoxDEuPYUIU75AV6L0bcsSbF52VvJ1gUrYAQR7oYyMn3lYlXGW6laI0YPza8TuWZwW5Z4RnUoPqZfZI0dlhm7TnMMmx2EJIczKLHzQia625pKHD-i3iqVlXG6EiTlHZzyJH3nOFzrZM4d9VZXzrILEkMQNuquIgymaVKDEb-VGt-P_TztTaFTQwIUp1P6Slejrmx0JzCaz7zb5dpN7ZpPDm6mUrV3ty10IuT8p-1A4ur3jc5U6Zuo0Bi9ERU4Z_ON2vYD8KVD74vLz-Nsl6kLQIU_LnCVwTOqbSbEpE8As5GFWFN15ffihOH3MoPn9qrPNuTt-Xmdw1FxsSTqHGjkQ9QqahdgMyUNtSHwRINP3hLp2DdtycQg6YTkTBYduZ-gqTfT8o57RkRmDq8XOByHF5R8d9HvMy5StOqBQnDLdlG_uIrAfcBKjJBZVvP8wXCzgLKxWuh0tf2fLeI3a51m2AI-KonqjpZacF6PG8VPRfm6yATTtIOjpPEsSDq_RNCtK4abIp2EFnWCUcLhwpfeaCZe0GxPrBI4w1TIz2ag-7U32nN1kKJD1XvWMsjSK81WdmAcUrFG0AuHlWwp5n1LXVLOsxQb9CTbcl5edugvencO1LFzu-mvTWREU1OvrPtUzU7fFuL2JvuH4Zg5_DpOqgIXOt5cMnRYcR-sdRfP3NGF5nj0VXZaUaA0lmiQ8sZC8Y0j-MaTgGFLv_5Gg4rXL1Wy4u1pBlaJ23Vw-oe5sycXtAUqqPLhnmcv2mq85JBaIv3_32HbucFtfzHTzeKf_ma4b9HtuaeL4EwWTFhHA1_zvCs5G2w3KPfos9L7Dl_oohtcn6YvFB_9oH4IfbqKWu8VFqt1WlOvoCU42uAhrZmxXivrcuIbTP15btwBrl4pveVzy7lUUiZMErg1Zrp-bGB-tmOtoh8YFvOnH9c6dnmld1NU7Mei6lrraOq_rapwmhjquOizF1anejzd-1_8JNoKfcAD1j-lmzjEkfAzJ7F6c2k4QU-Oc7jondjBc8fYz1NzZbtNQXTbQ593FY7_jFXqum3vetMrDJSt43d_iIq5vmW1zfbnvW5BvmGaud3Sl4ePbmou1It0pVdRKZUqpg7zt_YTc7_-4DZ8ck5H0CFKw1zmjLAFNutmap2hMxt2eOx6ga3i_XG6KOGTbDwFVWG5zbSd4k9mQaajb_UXkiwR8IgFPzXC3gE8kICd4ffns9SVDEeR8NS5XUPY8OdxMDyTQU_adLUDUDCItksYD6QKhCpBrEBUFkU57CvBq4N-7lvgqcNf6V3xPUHOlR55ygEoHfEWm0gFPUahcjzZBedL816w2Tn0lp3SEYh0IlK2eBPq6rT_ElgljKm4qlVZUX3pOG8-Vlsov-exSba_03VYreNIZX_mvnh1FkNpgFY_afDUBywluo7z0gQQ64Ot7Iz-L1EF7jT4qyGY3pM-02X1p0FMGia8Bnq9tsS8B6mgA0WcQtS1ERuo1aSm18RobKvO1Z9zsl3QUK5u-tEm1CU3tYOmF2wAyeL-hqAJWgMwvV6WAsqC8wioOteeuygEVB1XFo0xiGYjbBCJDx70DALbw7Vc09Tmxvj_u1x1WnBlbcfGd9rP41rrIwmrF6_ePJ_E6MefoEY66ecLhpEbzrFzC0Vt_5upvq8NXTgUqNYkuTRO6TCVXue3KwAI9vZXcrnzu7X3vFh1u76v8wQixjlDriGsd8awjvnUksI70rCN96whUs3XIrgK2y4DtOmC7ENiuBLZLge1aYLsY2K4GsatB3skJuxrErgaxq0HsahC7GsSuBrGrQexqULsa1K4GfadE7GpQuxrUrga1q0HtalC7GtSuBnQK9ZPmIY4tOLHgVP5ceYi6RtQzor4RDYxoz4j2TajnGFFsRIkRNcYGx7_8PfIQ9sywb4YDM9wzw30jDN3fCGMzTMwwNcPmKH1zlL45St8cpW-O0jdHCeek_Lm21WmteL5i8aI1eGnV_8uhNWgteMSqpGy9dlqsKrPZJg1bg_p_A7Sq-kees5jB6_BqC77-B33GMkU=" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYEGbaHLQMk2qcRa3JXZpjvYVLh5t014niPzvu2uhbkid8S5puPfj-14_rzlW2I8DwAZuNFYsYsJAq6aYwRyaBmpOaAbNFmpm4OcpE0sbfgNXDh7HpacI_U5TRiccsqbKDuNIOOypEDjSk4UKU7YRnTO-VFYHpjGgu8sWIjKRN9cqgseP_oymotDIM7iiix8sEDN5DinPQMbMxJzbdAJcFRJprmyR7N5JqM-iqTR2dWlKafTwYjrW12u0bjTcqCqBxgM3QnL5nGaZCSGiSTKIFyhknBsHA90cjUatTKTxAxgHmtbvD3qbY_tR9WR0kkXLj3mcKnfX1Hf1gslwyTdyRDd7pF_Jday-2e3Uyh0NdKuj7chBzF_aG40G-kCv9IZDTa5avV5Pud2oVMzyyTSlyQxZHevkeGiSoe2BN_XIU56C53yz712MXPyrjFYrYCn4gsVRBU2tbTopsn9ad45MhMPpIVK_pYBhGCXT1znmTsVPLnbz4KQbyGfgH7t5CJp8ZSVWBCEZ5OLPSrLA-lYXqH3YPq-rVCZCFGxYiCWHWhBb2ETtCralqf0v7KNk8T-8DrnxLsg1-RDdK8vxupq2BSyPSB7fw7gq-wZiGYNUzHsIbzrZB3lb6j2Mt7EfQry_LDo7O3_eADILpugLIjeX8jliHFz8XP9R7IzOhqls__4vYn6gIZOMCSK3w4vLsTUc391ayLa-WtdmzTTt2xer7am5kyThzKfKu390tmfWzMmkgqqbeP-IbM-S8lYUtOOwbbMQSvnyytg7jvINt_R1tSv6p6enr9DjFp5DOqcswMYKFze-_L8IIKQ5F3jdwjQXsbOMfGwUlzLOk4AKMBmVROelcf0HboH1hw==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYEGbaHLQdppU4yxuS-zSHO0rXDzapr1OEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHfgNXDp4klacM_U4zRscc8qbKjpJYuOypFDjS07kKUzabzhhfKKsLkwTQ3WULEZnImysVwZPHYEozUWoUOVzR-Q8Wiqk8R5TnIGOmYsYdOgauComsULZYdu-mNGDxRBq7ujRlNH54MR3rqxVaNRpeXJdAo4EXI7kCTvPchAjRNB0kcxQxzo2DgW7att3KRZY8gHGgaf3-oLc-th9VT0YnnbeChCeZcndNfVsvHA8XfC1HdLNH-rVcx-qb3c5euaOBbnW0LTlI-Et7tj3QB3qtNxxqcu3V6_WU24srxbwYTzKaTpHVsU6ObZMMHR_8iU-eigx895tz72Hk4V9VtFohyyAQLIlraGpt0kmZ_dO6c2UiHE4OkfotBQzDqJi-zjG3Kn7ysFeEJ91QPsPg2Csi0OQrK7EyCMkgD39WkiXWt7pA7cP2-b5KVSLE4ZqFWHDYC2IDm6hdw7Y0tf-FfZTO_4fXJTf-BbkmH6J7Zbl-V9M2gOURyeN7GNdl30AsY5CKeQ_hdSe7IG9KvYfxJvZDiHeXRWdn589rQGbJFH1B5OZSPm3GwcPP-z-KrdE5MJHt3_9FLAg1ZJIRQeR2eHE5soaju1sLOdZX69rcM03n9sXq-GruJE05C6jy7h6d45t75mRSQdVNvHtEjm9JeSsO20nUdlgElXx1ZewcR_WGG_q62jX909PTV-hxC88gm1EWYmOJyxtf_l-EENGCC7xqYVqIxF3EATbKSxkXaUgFmIxKorPKuPoD6ib1sQ==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTves74M_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPGco9iQ==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTvds4IM_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPYDs9oQ==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuDe2AqwTjvM13pd1JRsmBQa2p1zgsR0ccOMByVG1WmtJCsKdsqNYIlB3R7rSNXLmRaqyoYf0hXpBIdo6nhhmx-0EysZJwTVoOsWYk1m5EFMLWRqBqlFdJ9VJKUFkspjgwpVaS4O0q20baoHQzi4rAF-ubFBZIjZaSup5AjUpYe36CcMuacefY0DEO9FhW_A-fMMC4vvfE-_PCgPDlmudFTznil0tbUfs0rGRFHoD8Jxv7HA9CaTALLfwm0jsChZwem8QoInB15YejZnn3g-b4hx0mD47FKx0VPrJvFsiLlCgVmMBn589k8gWSZuI9NBcmckOhXjOPGHBvDuMnBkDufL89Rl0YqHePfPUiNjFaQCsoLNPt6VJ_Jbkf-GdwqZodR3xLgOE7f8H4NFNnem9gyOGnsn5r55uGjZJR8dr-4iWmYVnf-bGJlcs6I_XcXoosRUnVI1b27ETdBlFiG8dwLGSIZvrMdL6z-h468Rb-6-vS0NzvtzocukDu_lnNIGcT46eRVYR2voVoTmmFnh7s3Qr4wGeSkYQK3OiaN4NG2SLHT_ca4KTMiYEqJvJ51L7Z_AKh8bno=" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DPTCVYJz3ma70O6koWTKoNbU644UI6WMHGI7KjSpTWkByyrZKDWHFAd1e68iVC5nWqgrGH5I1qUTHaGq4IZsfNBVrGWeE1SBr1iJnc7IEpjYSVaO0QroPS5LQYiXFkSGlihR3R8k22ha1g0FUHLZA37yoQHIkjNT1DDJEytLjG5RRxpwzz54FQaDXouJ34JwZxuWlN96HHx6UJ8csN3rCGa9U2prZr3klI-IInE788fTjAWhNJr41fQm0jsChZ_um8QoInB15QeDZnn3gTaeGHCcNjscqHRU9sW6Wq4qUa-Sb_mQULOaLGOJV7D42FcQLQsJfEY4ac2wMoyYDQ-58vjpHXRqpdIR_9yA1UlpBIigv0PzrUX0mux35p3-rmB1GfUuA4zh9w_s1UKR7b2LL4KSxf2rmm4cP41H82f3ixqZhWt3504mVyjkl9t9dCC9GSNUhVffuRtz4YWwZxnMvZIhk-M52vLD6HzryFv3q6tPT3uysOx-6QO7iWs4BZRDhp5NXhXWcQ5UTmmJnh7s3Qr4wKWSkYQK3OiaN4OG2SLDT_ca4KVMiYEaJvJ68F9s_y01ukg==" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-84 — Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State)</span></div>
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
*E2E-84 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

