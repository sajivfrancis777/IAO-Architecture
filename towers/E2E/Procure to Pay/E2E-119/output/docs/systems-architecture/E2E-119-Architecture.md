<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-119 — R3 Shipping Rejects Inventory Movement</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-119 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-119 R3 Shipping Rejects Inventory Movement** within the IAO program. It includes 2 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-119 - R3 Shipping Rejects Inventory Movement |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: "loose"` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-119 - R3 Shipping Rejects Inventory Movement |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-119 Process Migration | Migrate R3 Shipping Rejects Inventory Movement business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-119 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **2 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-119 R3 Shipping Rejects Inventory Movement.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-119C_R3_IF_Factory_to_IF_Factory | E2E-119C_R3_IF_Factory_to_IF_Factory | Boundary Apps, Decentralized EWM, Intel Foundry (Supp. Entity), SAP S/4 Intel Foundry (Receiving Entity) | 25 | 4 |
| 2 | E2E-119E_R3__Rejected_Inventory_Receipt_at_Intel_Product_Lab | E2E-119E_R3__Rejected_Inventory_Receipt_at_Intel_Product_Lab | SAP S/4 Intel Foundry | 5 | 0 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-119C_R3_IF_Factory_to_IF_Factory — E2E-119C_R3_IF_Factory_to_IF_Factory

**Swim Lanes**: Boundary Apps · Decentralized EWM · Intel Foundry (Supp. Entity) · SAP S/4 Intel Foundry (Receiving Entity) | **Tasks**: 25 | **Gateways**: 4

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps
        n1["Procure to Pay"]
        n2["Order to Cash"]
        n3["Finance Plan to Report"]
        n4["Forecast to Stock"]
    end
    subgraph Decentralized EWM
        n5["Posting Change"]
        n6["Pick and Pack"]
        n7["Post Goods Issue"]
        n8["Outbound Del. Order"]
        n9["Distribute Inbound Delivery"]
        n10["Perform Unloading EWM"]
        n11["Post Goods Receipt EWM"]
        n12["Create/Confirm Put-Away Task​ EWM​"]
        n28(["fa:fa-stop Stock type changed at EWM"])
        n29(["fa:fa-stop Putaway Task Confirmed"])
        n34{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Intel Foundry (Supp. Entity)
        n19["Outbound Del. Creation"]
        n20["GTS Trade Compliance"]
        n21["Post Goods Issue"]
        n22["Create IC Invoice"]
        n23["AR Posting and Auto Clearing"]
        n25["fa:fa-user Move stock from Blocked stock to Unrestricted Stock via MIGO"]
        n27(["fa:fa-play Initiate stock movement from Blocked stock to Unrestricted stock"])
        n33(["fa:fa-stop Outbound Del. screening via GTS"])
        n36{{"fa:fa-arrows-alt parallelGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 Intel Foundry (Receiving Entity)
        n13["Create Inbound Delivery"]
        n14["Goods Receipt Unrestricted Stock"]
        n15["Auto Stock Transport Order"]
        n16["Trigger GTS Check"]
        n17["AP Posting and Auto Clearing"]
        n18["GTS Compliance SPL and EMB"]
        n24["fa:fa-user Create Stock Transport Request (Manual)"]
        n26(["fa:fa-play Initiate Inventory movement from IF Factory to IF Factory"])
        n30(["fa:fa-stop Good Receipt Posted"])
        n31(["fa:fa-stop I/C Invoice settlement"])
        n32(["fa:fa-stop STO Screened through GTS"])
        n35{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n10 --> n11
    n11 --> n34
    n34 --> n14
    n14 --> n30
    n12 --> n29
    n5 --> n28
    n15 --> n35
    n8 --> n6
    n6 --> n7
    n19 --> n36
    n36 --> n20
    n36 --> n8
    n20 --> n33
    n7 --> n21
    n21 --> n37
    n22 --> n23
    n17 --> n31
    n37 --> n22
    n37 --> n13
    n23 --> n17
    n13 --> n18
    n9 --> n10
    n18 --> n9
    n34 --> n12
    n35 --> n16
    n35 --> n19
    n16 --> n32
    n26 --> n24
    n24 --> n15
    n27 --> n25
    n25 --> n5
    class n24 userTask
    class n25 userTask
    class n26 startEvt
    class n27 startEvt
    class n28 endEvt
    class n29 endEvt
    class n30 endEvt
    class n31 endEvt
    class n32 endEvt
    class n33 endEvt
    class n34 gateway
    class n35 gateway
    class n36 gateway
    class n37 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1uP4jYU_itWViO2EuzmSoCHSpAhI6Qd7WiY7T50-mASB6wJduo4zNAR_712YgdioN1284Dw53M_33GcdyuhKbIm1s3NOyaYT8B7j2_QFvUmoLeCJer1QQP8BhmGqxyVPSmTUcKX-K9azPGLNykmsRhucb6X6BKtKQLfFn0wFYp5H5SQlIMSMZz1-r2C4S1k-4jmlEnpD2iU2VntTW3NKEsROwrYdugkgVDNMUFH2Av90I-lXokSStKO0SzIRlnSO8jgcvqabCDjdfhVie7h23ec8o1YZzAvkZDZ8G3-Ba5QLnPkrJJYUrGdLgYupR8iCrYsYILJWuC-LSAGycsRCuzDARxubp5J6xR8eXwmQDxJDsvyFmWg5AKe7zjIcJ5PPvjRNA7sfskZfUGTD-48vPXcfiIzmYjU7b4s7uAV4fWGT1Y0T5Xo4FXmMHGLtz57m7h2n-3Fr-ELkfToKRq6I3fUepqFTuRE2lOWZT_lSdSVPcHyRfmae7Eb37a-nGAYRPa5PZ3mrR9OHbNOiO1wgk6MxnHszY-lmg8Dx75udBZ7QzsyjK4hR69wfzQ4jvzWYByEsRNeNdj4M6OsVg-MJtqgNw_ioDUYzpx46l416E8df6QiFHbWDBYbMKNVzWUwLYqy2ZMPcX5_tqSniiHAKXiA-2frj5N9V-x_lYMjdyNYbrrbntiOMYEkQeAhh0RKPaKCMt6V86UcZSiBJZcyS06Tl1ZE8MkI9xYliHAGc3EkpGD-_f7EViBDpiUXwwGiDSRr1PU1lPs4eQGQpCKhEz_1dqjUwR2laQkWZVkZBkYy54qvZMlEJPknUFegKzQWQrdY9ACvKo7AgrTieIeYUUXHlk4Ryyjbgm8kpzCV0cu8unJON7hHUQZc8AuCsi8RQ4J3nyNKMizsPlR8MJUslNx-rlzbXtWK9T-jq6OPQj-DkwwOSk6Lph-A7wsEkrqkKYDa7S-nimNDUTiF2idQkaDU0PL893etBRmjr-UA5hwUUDQ4R_ldMz3P1uFwjQ8LwlEOYlliweGPy6ooPoE54ZjvTx0547PW1UXClBgFkA25e1qCJwZTJALfFjmWLDbEnH8li3vsBFhEItAdxWdm5JhMH4FmrSTmtJIDlSPxFiRrQzxoayzPP3BPd0ic77JDGaNbMMvFX9GhBhJmvhGGJBMTLtCmlTsMwf3i7qthOTy2r8hF2xbiFY1l6I2trfC0FYP3I35KNcKdRnsGPbq9KBOGEJEVkOGJ8pvqw__Gk0Yp_FlyLacPYPnZN0lWD9-untNzonknXf_n0ZdHX3eaz9tlqMj-1_xoeik4Skp5pl46hxx53D0xvF4LpkhGRxt0ZlCeeSLJH-SfM1LDcRwLsHz4UqvN72cGpfwuWVVRzMgf0Z-VSBp8vIekgvkvhpHhNV6KeRJ8pKIfXW4uYhDDpN4QeRxXJqNsg5CyE20jZD3ODyvHUFl8bsda3B44z-swTC3XPFGfvoJlzXfRZL5htFpvLlE--J_sFe8UMBj8Kt8ZGnAawPMV4PlKQgOOAjxbA24DuGMFBGo90gIK8AIFjJr1UC2HzTLU4mMlrvc9JaAvdi2gHbgqC89TQKgUdFauzkr7cHXMWsNRKp5W8bQN1wAcreJ6CmgD14COSyXitJVSiY_N2rY-VKWcoQloFUel7mkVVxdH98fVRnW1XZ1JCyijwcl9sdbTF-UuHlzBh-3nQhcPr-AjdeXvouNLqGdfRJ2LqHsR9S6ivr5ld-HgMjy8DIcatvrWFrEtxKk1ebfqD1Lx0ZqiDFY5tw59C4rzcbkniTWpP9ysqkiF5i2G4p2xbcDD39Zxic4=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-119E_R3__Rejected_Inventory_Receipt_at_Intel_Product_Lab — E2E-119E_R3__Rejected_Inventory_Receipt_at_Intel_Product_Lab

**Swim Lanes**: SAP S/4 Intel Foundry | **Tasks**: 5 | **Gateways**: 0

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TD
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph SAP S/4 Intel Foundry
        n1["Standard Pur. Order"]
        n2["Goods Receipt at IP Lab S.Loc."]
        n3["Post Goods Receipt EWM"]
        n4["Put-Away Confirmation with Exception Codes"]
        n5["fa:fa-user Goods Issue against Cost Center via MIGO"]
        n6(["fa:fa-play Initiate Pur, Order from IP Labs"])
        n7(["fa:fa-play Initiate Text PO from IP Labs"])
        n8(["fa:fa-stop Reject Inventory issued to IP Lab"])
        n9(["fa:fa-stop endEvent"])
    end
    n1 --> n2
    n3 --> n4
    n6 --> n1
    n4 --> n9
    n7 --> n3
    n2 --> n5
    n5 --> n8
    class n5 userTask
    class n6 startEvt
    class n7 startEvt
    class n8 endEvt
    class n9 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVVtv2jAY_SufUlVsUuhyJTQPk2ggFVKrotGtD-seTGKD12BHtsNlFf99NgnQsHUvy0PEdzjnfBdf8mplPMdWbF1evlJGVQyvHbXAS9yJoTNDEndsqIFvSFA0K7DsGA7hTE3prz3NDcqNoRksRUtabA06xXOO4evYhoEWFjZIxGRXYkFJx-6Ugi6R2Ca84MKwL3CfOGSfrfnrhoscixPBcSI3C7W0oAyfYD8KoiA1OokzzvKWKQlJn2SdnSmu4OtsgYTal19JfI82TzRXCx0TVEisOQu1LO7QDBemRyUqg2WVWB2GQaXJw_TApiXKKJtrPHA0JBB7OUGhs9vB7vLymR2TwuPwmYF-sgJJOcQEpNLwaKWA0KKIL4JkkIaOLZXgLzi-8EbR0PfszHQS69Yd2wy3u8Z0vlDxjBd5Q-2uTQ-xV25ssYk9xxZb_T7LhVl-ypT0vL7XP2a6idzETQ6ZCCH_lUnPVTwi-dLkGvmplw6PudywFybOn36HNodBNHDP54TFimb4jWmapv7oNKpRL3Sd901vUr_nJGemc6TwGm1PhtdJcDRMwyh1o3cN63znVVazieDZwdAfhWl4NIxu3HTgvWsYDNyg31SofeYClQuYDiYw_RTAmClcQMorlottzTEPc78_W1OFzH7PYVKJK3gwx-XZ-vGG5GnSLee5hC84w7RUgBSMJ6D3OEyv7nh21eb7mj_hUkFbNHq6b_MCw6tUd2BmmHBGqFgiRTmDNVULGG0yXO7DRB8V2daGWktQTFDX7JUm01jKCgOaI8p09sSUkGDduYAVRXA_vn1om_Q-HF3KQtcw1jcX1WtqJmHXkwAi-LJp1pTw8Y08ek_-iDcKJg__0vZPWql4qYf0E2d6qmylC-ZiC9T0koPijcGZ_vpMvz-bWnqiaaT-wVzodj_rZWxCvw6DJuzVYXNgWFCH100Y1aHfhF4dhk0Y1mH_zTY24OH4tuDe8a5qwdHf4X5z27TA6wa0bGuJ9V6huRW_WvvPiv705JigqlDWzrZQpfh0yzIr3l-_VlXmel2GFOlTsazB3W82Xxmd" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-119C_R3_IF_Factory_to_IF_Factory,  | |
| Decentralized EWM | E2E-119C_R3_IF_Factory_to_IF_Factory,  | |
| Intel Foundry (Supp. Entity) | E2E-119C_R3_IF_Factory_to_IF_Factory,  | |
| SAP S/4 Intel Foundry (Receiving Entity) | E2E-119C_R3_IF_Factory_to_IF_Factory,  | |
| SAP S/4 Intel Foundry | E2E-119E_R3__Rejected_Inventory_Receipt_at_Intel_Product_Lab | |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

#### 4.2.1 Current-State — Current-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E119CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E119CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E119CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E119CDAA_e_g_XEUS -.-> E2E119CDAD_e_g_Azure_SQL
    end
    style E2E119CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E119CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E119CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E119CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E119CDAA_e_g_MES_300 -.-> E2E119CDAD_e_g_SAP_HANA
    end
    style E2E119CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E119CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E119CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYFu2jAQhl_FcoXYJOgCNDAitZIhYUVKq66h26RmikxyAasmiRJnhVLefXYC6cagq2pLUXy---_8XeSssR8HgA1cq61ZxISB1nUxhwXUDVSf0gzqDVTPwM9TJlY2_AKuNngclzuF6zeaMjrlkNVVdBhHwmFPhUBLT5bKTdlGdMH4SlkdmMWA7sYNRGQgr2-UB48f_TlNRaGRZ3BFl99ZIOZyHVKegfSZiwW36RS4SiTSXNkiWb2TUJ9FM2ns6NKU0ujhxXSmbzZoU6u5UZUCTQZuhOTwOc0yE0JEk2QQL1HIODdOBro5Go0amUjjBzBONK3XG3S3y-ajqsloJ8uGH_M4VdsdU9_XC6bDFd_KEd3skl4l17Z6Zqd9VK410K22ticHMX8pbzQa6AO90hsONTmO6nW7atuNSsUsn85SmsyR1bZarf7QJEPbA2_mkac8Bc_5at-7GLn4Z-muRsBS8AWLo4qaGlU8KcJ_WHeOjITT2SlS71LBMIyS6oEgcy_nBxe7efC5E8hn4J-5eQiaPLVSK5yQdHLxR6VZkH21DtQ8bV4czVWGQhRsgYgVh-M0dsiJmhVyS1Pzb-StZPlfyA658S7JNXkf4yvL8TqatsMsl0gu30S6SvwKaOmDlM-bOG9rOYh6l-xNpHfO7wJ9JDE6P7943lIyC7LoEyI3Y_kcMQ4ufn7l69hroQ0zeYL7P7D5gYZMMiGI3A4vxxNrOLm7tZBtfbGuzSNNtW9frLan2k-ShDOfqt3DDbQ980izTCqoupcP98n2LClvRUEzDps2C6GULy-Qgx0pT7jjr6tZ8e_3-__Axw28gHRBWYCNNS7uf_n3CCCkORd408A0F7GzinxsFFc0zpOACjAZlUQXpXHzG_18-Bk=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E119FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E119FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E119FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E119FDAA_e_g_XEUS -.-> E2E119FDAD_e_g_Azure_SQL
    end
    style E2E119FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E119FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E119FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E119FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E119FDAA_e_g_MES_300 -.-> E2E119FDAD_e_g_SAP_HANA
    end
    style E2E119FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E119FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E119FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYFumzAQhl_FchVlk5KOJCVZkVrJCbBWolVX0m1SmZADR2LVAQRmTZrm3WdDQrcs6araEsLnu__O3yGzwkESAjZwo7FiMRMGWjXFDObQNFBzQnNotlAzh6DImFg68Au42uBJUu2Urt9oxuiEQ95U0VESC5c9lQIdPV0oN2Wz6ZzxpbK6ME0A3V22EJGBvLlWHjx5DGY0E6VGkcMVXXxnoZjJdUR5DtJnJubcoRPgKpHICmWLZfVuSgMWT6Wxp0tTRuOHF9OJvl6jdaPhxXUKNB56MZIj4DTPTYgQTdNhskAR49w4GuqmbdutXGTJAxhHmjYYDPubZftR1WR000UrSHiSqe2eqe_qhZPRkm_kiG72yaCW61oDs9c9KNcZ6lZX25GDhL-UZ9tDfajXeqORJsdBvX5fbXtxpZgXk2lG0xmyulanc2qbZOT44E998lRk4LtfnXsPIw__rNzVCFkGgWBJXFNTo44nZfgP686VkXA8PUbqXSoYhlFR3RNk7uT84GGvCD_3QvkMgxOviECTp1ZqpROSTh7-qDRLsq_WgdrH7fODuapQiMMNELHkcJjGFjlRs0ZuaWr-jbyTLv4L2SU3_gW5Ju9jfGW5fk_TtpjlEsnlm0jXiV8BLX2Q8nkT500te1Fvk72J9Nb5XaAPJEZnZ-fPG0pmSRZ9QuTmUj5txsHDz698HTstdGAqT3D_B7Yg1JBJxgSR29HF5dgaje9uLeRYX6xr80BTndsXq-Or9pM05Sygand_Ax3fPNAskwqq7uX9fXJ8S8pbcdhOorbDIqjkqwtkb0eqE27562rW_E9PT_-Bj1t4DtmcshAbK1ze__LvEUJECy7wuoVpIRJ3GQfYKK9oXKQhFWAyKonOK-P6N3pB-EM=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-119-R001 | Report | R3 Shipping Rejects Inventory Movement operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-119-C001 | Conversion | Legacy data migration for R3 Shipping Rejects Inventory Movement | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-119.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "16px", "fontFamily": "Segoe UI, Arial, sans-serif"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        E2E119C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E119C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E119CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E119CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E119C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E119CMW_e_g_Azure_Service_Bus
    E2E119CMW_e_g_Azure_Service_Bus --> E2E119C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVWtv4jAQ_CtWKsQXaENbXlGFlJBw4hTaqunjTscpMvECVk0SxU5bSvnvZyeU8KroGSko69lZZ3ZsL7QgIqAZWqm0oCEVBlqUxRRmUDZQeYQ5lCuozCFIEyrmLrwAUxMsivKZDPqIE4pHDHhZZY-jUHj0PSOoNeI3BVOxHp5RNldRDyYRoId-BZkykVUQxyGvckjouLxUaBa9BlOciIwv5TDAb0-UiKl8H2PGQWKmYsZcPAKmiookVbFQfokX44CGExm81GUoweFzEarryyValkrDcF0C3VvDEMlRKqFqVS4omNIBFlClIY9pAgRxMWeAAoY5By4xOTx7t2GMRimnIXCOsjGmjBknPTmseoWLJHoG48RqtRq6tXqtvqovMc7jt0oQsSgxTnRd3-HEcYyKkXNadcW65tT1ZtNq_AcnwQLvc9qtI5y1Lc7POYK5FC_Bc6kpqu9UmlFCGLziBDYVsRtmoYjTbPQKtm-sHiK2p4jSeEPlblfXj3HmrDwdTRIcT5Hp_hlqw5S0Loh8kos6Mm9v3X7XvO_fXCPX_O3cDbW_eZIaRBoiEDQKkXtXRJ1zp1Zrd33wJ_7A8fwLXd-kDaCB4HRyiuQcknOS0TAM2eLDDL-cB-9gupr4OnfwlGWb72kCvgfJCw3At1K-9YG1Zk6VodAKhSQq5y0at0dvOxl9N-LCd5jc86HobC4yuMyZFQCtAFej5KxzRTv5hPeIzlDfjgL599O7ub46o528rHJmXhBC8tmjA6LKvdf5GGoZnZ11QlKZt3357FEGQ-3jmBhb1F-BVJm9jqhlrcyTHQeWu7HVe_qxrb6Zaq5T9e_s6D3TujCROm1ZhOjIdX441_Y33Or60uO7BjPjmNEAK_ABi7n-4GnXR4PCK196x_VtZ9cltjqGnFDI22S3-3mKc5NvyvMGuZRAUo3GVZeOV2XkObBhlULUXJRPYevqtxa23W7vnWlaRZtBMsOUaMZCy24xeQcSGOOUCW1Z0XAqIm8eBpqRXS5aGsuFgk2xbMIsDy7_AfaJPwE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-119.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "16px", "fontFamily": "Segoe UI, Arial, sans-serif"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        E2E119F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E119F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E119FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E119FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E119F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E119FMW_e_g_Azure_Service_Bus
    E2E119FMW_e_g_Azure_Service_Bus --> E2E119F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVWtv4jAQ_CtWKsQXaENbXlGFlJBw4hTaqunjTscpMvECVk0SxU5bSvnvZyeU8KroGSko69lZZ3ZsL7QgIqAZWqm0oCEVBlqUxRRmUDZQeYQ5lCuozCFIEyrmLrwAUxMsivKZDPqIE4pHDHhZZY-jUHj0PSOoNeI3BVOxHp5RNldRDyYRoId-BZkykVUQxyGvckjouLxUaBa9BlOciIwv5TDAb0-UiKl8H2PGQWKmYsZcPAKmiookVbFQfokX44CGExm81GUoweFzEarryyValkrDcF0C3VvDEMlRKqFqVS4omNIBFlClIY9pAgRxMWeAAoY5By4xOTx7t2GMRimnIXCOsjGmjBknPTmseoWLJHoG48RqtRq6tXqtvqovMc7jt0oQsSgxTnRd3-HEcYyKkXNadcW65tT1ZtNq_AcnwQLvc9qtI5y1Lc7POYK5FC_Bc6kpqu9UmlFCGLziBDYVsRtmoYjTbPQKtm-sHiK2p4jSeEPlblfXj3HmrDwdTRIcT5Hp_hlqw5S0Loh8kos6Mm9v3X7XvO_fXCPX_O3cDbW_eZIaRBoiEDQKkXtXRJ1zp1Zr93zwJ_7A8fwLXd-kDaCB4HRyiuQcknOS0TAM2eLDDL-cB-9gupr4OnfwlGWb72kCvgfJCw3At1K-9YG1Zk6VodAKhSQq5y0at0dvOxl9N-LCd5jc86HobC4yuMyZFQCtAFej5KxzRTv5hPeIzlDfjgL599O7ub46o528rHJmXhBC8tmjA6LKvdf5GGoZnZ11QlKZt3357FEGQ-3jmBhb1F-BVJm9jqhlrcyTHQeWu7HVe_qxrb6Zaq5T9e_s6D3TujCROm1ZhOjIdX441_Y33Or60uO7BjPjmNEAK_ABi7n-4GnXR4PCK196x_VtZ9cltjqGnFDI22S3-3mKc5NvyvMGuZRAUo3GVZeOV2XkObBhlULUXJRPYevqtxa23W7vnWlaRZtBMsOUaMZCy24xeQcSGOOUCW1Z0XAqIm8eBpqRXS5aGsuFgk2xbMIsDy7_AT1dPxk=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-119-I001 | Interface | R3 Shipping Rejects Inventory Movement inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-119-E001 | Enhancement | R3 Shipping Rejects Inventory Movement custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-119-F001 | Form/Report | R3 Shipping Rejects Inventory Movement operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### 6.1.1 Current-State — Current-State Platform Architecture

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E119CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E119CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E119CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E119CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E119CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E119CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E119CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E119CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRF6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1ZslZKpWrzB4t77_z4_Fp4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuDB2AqwTjvM13pN1JRsmBQa2p1zgsR0acOMByVG1WmtJCsKdsqNYIlB3R3oyNXLmRaqyoYf0xXpBIdo6nhlmy-00ysZJwTVoOsWYk1m5EFMLWRqBqlFbL7qCQpLZZSHBlSqkhxf5Rso21ROxjExWEL9NWLCyRHykhdTyFHpCw9vkE5Zcw58-xpGIZ6LSp-D86ZYVxeeuN9-OFR9eSY5UZPOeOVSltT-zWvZEQcgf4kGPtXB6A1mQSW_xJoHYFDzw5M4xUQODvywtCzPfvA831DjpMNjscqHRc9sW4Wy4qUKxSYwXB45c9n8wSSZeI-NRUkc0KinzGOG3NsDOMmB0Nufb48R10aqXSMf_UkNTJaQSooL9Dsy1E9oN0O_SO4U9COo74lwXGc3vJ-ERTZvjuxZXC6tX_y8-3zR8ko-eR-dhPTMK3OgmxiZXLOiP23EdHFCKk6pOre78VtECWWYfyxQ4ZIhu915EWz_8GUN_HX1x-f9-1OuyOiC-TOb-QcUgYxfj59X1jHa6jWhGbY2eHurZAvTQY5aZjArY5JI3i0LVLsdL8zbsqMCJhSIu9o3Yvtb7Iwb_I=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E119FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E119FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E119FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E119FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E119FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E119FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E119FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E119FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRF6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1ZslZKpWrzB4t77_z4_Fp4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DAzCVYJz3ma70G6koWTKoNbU644UI6VMHGI7KjSpTWkByyrZKDWHFAd3d6MiVC5nWqgrGH5M1qUTHaGq4JZvvNBVrGWeE1SBr1iJnc7IEpjYSVaO0QnYfliShxUqKI0NKFSnuj5JttC1qB4OoOGyBvnpRgeRIGKnrGWSIlKXHNyijjDlnnj0LgkCvRcXvwTkzjMtLb7wPPzyqnhyz3OgJZ7xSaWtmv-aVjIgjcDrxx9OrA9CaTHxr-hJoHYFDz_ZN4xUQODvygsCzPfvAm04NOU42OB6rdFT0xLpZripSrpFv-sPhVbCYL2KIV7H71FQQLwgJf0Y4asyxMYyaDAy59fnqHHVppNIR_tWT1EhpBYmgvEDzL0f1gHY79A__TkE7jvqWBMdxesv7RVCk--7ElsHp1v7Jz7fPH8aj-JP72Y1Nw7Q6C9KJlco5JfbfRoQXI6TqkKp7vxe3fhhbhvHHDhkiGb7XkRfN_gdT3sRfX3983rc7646ILpC7uJFzQBlE-Pn0fWEd51DlhKbY2eHurZAvTQoZaZjArY5JI3i4LRLsdL8zbsqUCJhRIu8o78X2N9VVcAo=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
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

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-119 — R3 Shipping Rejects Inventory Movement</span></div>
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
*E2E-119 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

