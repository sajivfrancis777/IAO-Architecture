<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-70 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-70 R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte** within the IAO program. It includes 4 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-70 - R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: "loose"` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-70 - R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-70 Process Migration | Migrate R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-70 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **4 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-70 R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products) | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products) | Boundary Apps, External Partners/
Supplier, OSAT, SAP S/4 (IP & IF) | 23 | 10 |
| 2 | E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry | E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry | Boundary Apps, External Partners/
Supplier, SAP S/4 (IP & IF) | 27 | 10 |
| 3 | E2E-70_R3_CFIN | E2E-70_R3_CFIN | Boundary Apps, CFIN, MBC, SAP S/4 (IP & IF) | 15 | 10 |
| 4 | E2E-70_R3_SAP_Transportation_Management | E2E-70_R3_SAP_Transportation_Management | Boundary Apps, External Partners/
Supplier
, SAP S/4 (IP & IF) | 12 | 6 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products) — E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products)

**Swim Lanes**: Boundary Apps · External Partners/
Supplier · OSAT · SAP S/4 (IP & IF) | **Tasks**: 23 | **Gateways**: 10

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
        n1["Organize Transport-Intel Routing Guide (IRG)"]
        n2["ReadSoft Validation/Exception Handling based on rules setup"]
        n3["Incoming invoice/ B2B/OpenText/Web suite"]
        n4["Manual invoices through OCR"]
        n28{{"fa:fa-code-branch exclusiveGateway"}}
        n29{{"fa:fa-code-branch B2B/Manual?"}}
        n36{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier
        n15["Receive Manufacturing Order"]
        n16["Update Purchase order Information (Weekly)"]
        n17["Complete Manufacturing against Manufacturing Order"]
        n18["Receive PO at Supplier End"]
        n19["Select Carrier via Intel Routing Guide Hosted Collaboration Portal"]
        n20["Ready to Ship Manufacturing Inventory (Substrates)"]
        n21["Receive Order Shipment from Supplier"]
        n22["Supplier Invoicing"]
        n24(["fa:fa-stop Purchase Order Updated"])
        n37{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph OSAT
        n23["Receive Physical Receipt at OSAT Location"]
        n25(["fa:fa-stop Continued Manufacturing Process at OSAT (Refer E2E-57 OSAT Manu. Process)"])
        n35{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n5["Create Purchase Requisition (Feed from MAAPS)"]
        n6["Create Purchase Order"]
        n7["Trigger GTS Check"]
        n8["Calculate Taxes"]
        n9["Create Inbound Delivery"]
        n10["Trigger TM Embedded"]
        n11["Receive Goods Receipt(Virtual)"]
        n12["Evaluate Receipt Settlement (ERS) Self-Billing"]
        n13["Post Supplier Invoice"]
        n14["Publish Purchase Order"]
        n26["E2E-70 R3 SAP Transportation Management"]
        n27["E2E-70 R3 CFIN"]
        n30{{"fa:fa-code-branch Invoice Accepted?"}}
        n31{{"fa:fa-arrows-alt parallelGateway"}}
        n32{{"fa:fa-arrows-alt parallelGateway"}}
        n33{{"fa:fa-arrows-alt parallelGateway"}}
        n34{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n16 --> n24
    n6 --> n31
    n31 --> n8
    n17 --> n20
    n9 --> n32
    n32 --> n10
    n23 --> n35
    n11 --> n12
    n30 -->|"No"| n22
    n28 --> n2
    n35 --> n25
    n3 --> n36
    n32 --> n23
    n12 --> n28
    n5 --> n6
    n15 --> n17
    n21 -->|"3B2 - WebSuite /(Web ASN)"| n9
    n10 --> n26
    n29 --> n4
    n29 --> n3
    n2 --> n30
    n30 -->|"Yes"| n13
    n13 --> n27
    n14 --> n34
    n34 -->|"3A4 or 3A19WebSuite
 during IAO
E2Open(post IAO)"| n18
    n18 --> n19
    n19 --> n1
    n33 --> n14
    n8 --> n33
    n31 --> n7
    n7 --> n33
    n1 --> n37
    n20 --> n37
    n37 --> n21
    n35 --> n11
    n22 --> n29
    n36 --> n28
    n4 --> n36
    class n24 endEvt
    class n25 endEvt
    class n26 startEvt
    class n27 startEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1tv2kgU_isjV1mIBBtfMfCwKyCQIjUNwrTVquzDYI9hlMHjHY8JbMp_3zPGw8Ulq26Xhyj-fL5zP2fGr0bII2J0jZubV5pQ2UWvNbkia1LrotoCZ6TWQAfgMxYULxjJakom5okM6N-FmOWmWyWmsBFeU7ZTaECWnKBP4wbqAZE1UIaTrJkRQeNao5YKusZiN-CMCyX9jrRjMy6sla_6XEREnARM07dCD6iMJuQEO77ruyPFy0jIk-hCaezF7Tis7ZVzjL-EKyxk4X6ekUe8_UIjuYLnGLOMgMxKrtkHvCBMxShFrrAwFxudDJopOwkkLEhxSJMl4K4JkMDJ8wnyzP0e7W9u5snRKPownScIfiHDWXZPYpRJgIcbiWLKWPedO-iNPLORScGfSfedPfTvHbsRqki6ELrZUMltvhC6XMnugrOoFG2-qBi6drptiG3XNhtiB38rtkgSnSwNWnbbbh8t9X1rYA20pTiO_5clyKuY4ey5tDV0Rvbo_mjL8lrewPxenw7z3vV7VjVPRGxoSM6UjkYjZ3hK1bDlWebbSvsjp2UOKkqXWJIXvDsp7Azco8KR548s_02FB3tVL_PFRPBQK3SG3sg7KvT71qhnv6nQ7Vluu_QQ9CwFTleoz_Oil1EvTbPDO_VLrK9z40kscQKzh2bQd1nKhWyOE0kYmvJcQguih5xGBNXH04fbufHnGdsG9pTgKOCxRJ8xoxGWlCd3w21IUvUfeo-TiCkdavYjBIjIYeahDDJPL5U5oGychHytxGmy4VCmO9S3-3dPKUlmZCvvvpAFhEQluWS6wHzESY6Z5mVIrgTPlyv0NJhWfG6_vs6NGHdj3FS7qrmAqMMVItuQ5RndkIdDMefGfn9O61ynKf8Otn-vMJzWiYGF4C9ZEzMJHr5lB8aqUrXhVhKRQFgTGO6EiOwOBXmaMkrEeQ29ogwhAaVI-RLjUOZCpfFJ7bzL-K0WSH9KoVIETXIB6yQjqNiNaJzEXKyLEqL6F0Ke2a5ScMsH8oCvU0Zk1RZeYppk8gc8aJ_5O3lCWB6jQkPIwaVwB4QDwkgo0QDSqIQ2FKNrHfqeZxKaDPY1wwsuDoFMoJ8xq_SAWTbuDkmOghVNK16Pkw1JJId5qQf5AiYNspVVm986C6MIs9C0BiKKBV-fSnVJU0NzjHdc9CuYrAi59a-6dzLJ01OlDoYO9VOpuj3vOP9_d9xT0Jud--Gcl2q1y2gI3VgAqVSFU_LoAw-LXFdi8CoxDOAgoEkOFbpMttp0JMuO6upTEqtWsIdNzz9AivCrFrythu1dDTvFAjNG2A9EHfQmKLhzYcVN0C9oPDrXroZrIMjFuEzJXznN6GFQRgQiKgr-2OtNgkqXtK7Qr8yEmquZoMslBP4wC9BgRcLnSxE1NQPMwpwpZTO8JdmlQOdkapws1MJH94RB5cSuMlPmmbXZIxquFySKSHXyzvv7gfMo04Wvf6ZCwsarLgfV2cMNZrlyQTdJQKRkpJiK-nAa3ALA4mYfDrbvut5S3TaBIUaV-ajse0st_Em-YDRb_WtWbZV91Ue-iaZOUebjGXfYDtBYeFl4V2H6F8zBaPyxclqZ18-D0mHUC9URSKLvTgXrvzXrgWT_DMn5GZL7k7ME5wpqNn9Tq6sEymenvIHBPwegrQl-SSgvP0mnJNiaYB8ASwvYTinhaRWlSutIMRXwbW585HPjm1q2mtoujWlBr3zWqrTqVsW47WhbGtD-lxo0wSqfLV-btEpfnD5QEdxdAnV1QXd1dY3pBR9vCxc7mm-W-rVCu8yHW3nWDpX-OGY19j_UYvimxkmrLoOztWuWW3K1bsfVvvZcuAwgp2d1tMMgEpWnYu9pngxtdR2rp2pMATgEYR2LWubZOoZVen3sgtIXS5suCY5TaRPtq195X752jmk2K4Cj-8qq1NrSgK1LqZ10WpXaupfdUNzLVWuXnz6XqHcVbR0_yS5x_w28rb8iLuHOVRhqfRW2rsP2ddi5DrvXYe863LoO-xo2GsaawK2SRkb31Sg-_Y2uEZEY50wa-4aBc8mDXRIa3eIT2ciLu809xXA2rw_g_h_p1AEs" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry — E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry

**Swim Lanes**: Boundary Apps · External Partners/
Supplier · SAP S/4 (IP & IF) | **Tasks**: 27 | **Gateways**: 10

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
        n1["Organize Transport-Intel Routing Guide (IRG)"]
        n2["ReadSoft Validation/Exception Handling based on rules setup"]
        n3["Incoming invoice/ B2B/OpenText/Web suite"]
        n4["Manual invoices through OCR"]
        n35{{"fa:fa-code-branch exclusiveGateway"}}
        n36{{"fa:fa-code-branch B2B/Manual?"}}
        n44{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier
        n17["Receive Manufacturing Order"]
        n18["Update Purchase order Information (Weekly)"]
        n19["Complete Manufacturing against Manufacturing Order"]
        n20["Receive PO at Supplier End"]
        n21["Select Carrier via Intel Routing Guide Hosted Collaboration Portal"]
        n22["Ready to Ship Manufacturing Inventory (Substrates)"]
        n23["Receive Order Shipment from Supplier"]
        n24["Supplier Invoicing"]
        n25["PO communication to 3PL"]
        n26["Send ASN Copy to 3PL"]
        n27["Physical Receipt at 3PL"]
        n30(["fa:fa-stop Purchase Order Updated"])
        n31(["fa:fa-stop PO Received"])
        n32(["fa:fa-stop PO Communication Received"])
        n39{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n5["Create Purchase Requisition"]
        n6["Create Purchase Order"]
        n7["Trigger GTS Check"]
        n8["Calculate Taxes"]
        n9["Create Inbound Delivery"]
        n10["Trigger TM Embedded"]
        n11["Receive Goods Receipt Stock Unrestricted"]
        n12["Post Supplier Invoice"]
        n13["Evaluate Receipt Settlement (ERS) Self-Billing"]
        n14["Remain to Unrestricted stock"]
        n15["Move Inventory to Blocked Stock"]
        n16["Publish PO"]
        n28(["fa:fa-stop endEvent"])
        n29(["fa:fa-stop Inventory Moved to Blocked Stock"])
        n33["E2E-70 R3 SAP Transportation Management"]
        n34["E2E-70 R3 CFIN"]
        n37{{"fa:fa-code-branch Invoice Accepted?"}}
        n38{{"fa:fa-code-branch eCoC Approved in MQCS"}}
        n40{{"fa:fa-arrows-alt parallelGateway"}}
        n41{{"fa:fa-arrows-alt parallelGateway"}}
        n42{{"fa:fa-arrows-alt parallelGateway"}}
        n43{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n18 --> n30
    n6 --> n40
    n40 --> n8
    n22 --> n39
    n9 --> n41
    n41 --> n10
    n37 -->|"No"| n24
    n35 --> n2
    n5 --> n6
    n21 --> n1
    n17 --> n19
    n39 --> n23
    n23 -->|"3B2 - WebSuite /(Web ASN)"| n9
    n1 --> n39
    n10 --> n33
    n2 --> n37
    n37 -->|"Yes"| n12
    n12 --> n34
    n20 --> n31
    n19 --> n22
    n38 -->|"Yes"| n14
    n11 --> n38
    n13 --> n35
    n25 --> n32
    n38 --> n13
    n38 -->|"No"| n15
    n8 --> n42
    n42 --> n16
    n16 --> n43
    n43 -->|"3A4 or 3A19WebSuite
 during IAO
E2Open(post IAO)"| n20
    n43 -->|"E2 Open / OpenText"| n25
    n43 --> n21
    n26 --> n27
    n41 -->|"OpenText"| n26
    n14 --> n28
    n15 --> n29
    n36 -->|"B2B"| n3
    n36 --> n4
    n24 --> n36
    n40 --> n7
    n7 --> n42
    n44 --> n35
    n3 --> n44
    n4 --> n44
    n27 --> n11
    class n28 endEvt
    class n29 endEvt
    class n30 endEvt
    class n31 endEvt
    class n32 endEvt
    class n33 startEvt
    class n34 startEvt
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWF1z4jgW_Ssqd_UmXQUVf4GBh90CBzJUdTpMnJ6urWEfhC2DK8LyyDKBTee_75VtGaw4NTWzPKTiwz3nfuheSebVCFlEjInx-fNrkiZigl6vxI7sydUEXW1wTq56qAJ-wzzBG0ryK2kTs1QEyX9LM8vNjtJMYgu8T-hJogHZMoK-L3toCkTaQzlO835OeBJf9a4ynuwxP_mMMi6tP5FRbMalt_qrGeMR4WcD0_SscABUmqTkDDue67kLyctJyNKoJRoP4lEcXr3J4Ch7CXeYizL8Iif3-PgjicQOnmNMcwI2O7GnX_GGUJmj4IXEwoIfVDGSXPpJoWBBhsMk3QLumgBxnD6foYH59obePn9ep41T9PVxnSL4hBTn-S2JUS4Anh8EihNKJ59cf7oYmL1ccPZMJp_suXfr2L1QZjKB1M2eLG7_hSTbnZhsGI1q0_6LzGFiZ8ceP05ss8dP8FfzRdLo7Mkf2iN71HiaeZZv-cpTHMf_lyeoK3_C-XPta-4s7MVt48saDAe--V5PpXnrelNLrxPhhyQkF6KLxcKZn0s1Hw4s82PR2cIZmr4musWCvODTWXDsu43gYuAtLO9DwcqfHmWxWXEWKkFnPlgMGkFvZi2m9oeC7tRyR3WEoLPlONuhGSvKXkbTLMur7-QntX5fGw98i1OYPfQEfZdnjIv-MhWEokdWCGhBdFckEUHXy8e7L2vjPxdsG9iPBEcBiwX6DdMkwiJh6c38GJJM_od-wWlEpYac_QgBwguYeVgGUWRtMQfElmnI9tI8SQ8MlukGzezZzUNG0idyFDc_yAZSSgRpM11g3uO0wFTxciR2nBXbHXrwHzU3g9fXtRHjSYz7cq_qbyDrcIfIMaRFnhzIXbWYa-Pt7ZI27KbJ-Crf_9IYrntmYM7ZS97HVECEH_mBsdJWbX4UhKeQ1gqGOyU8v0FBkWU0IfxyDb1yGUICokjGEuNQFFyW8UHuee38rRFYf89gpQhaFRy2k5ygcm9EyzRmfF8uIbr-QcgzPWkLbo2B7LN9RonQfeEtTtJc_HkEtnkR7-oBYdFkheZQg7ax7NCAUBIK5EMZpdEhwairQ39huYAmg_2a4g3jVSIr6GdMNVHVuCckGAp2SaZFvUwPJBUM5uU6KDYwaVCtXG9-5yKNMs1SaQ9EFHO2Py9Vmya7tcl3WfYruNSMBmAEpYFp2BdpElapQKzO6qtmOSzrk0ZoGnyD1LNTt5nskdXulIMWlE1GnQlZ-XeWjnn9u2rbXLDs3CRVjlXryFX6csmydNYDqmvzztR-b-q38vyIOP6rk_t-ooLpCgU3LmxmK_QPtFxc6sua-5y0BuOR_FEkeSLDapdp2GHc0euy7E882W6hcndPAfJ3JHxum8h59DENCyrFnvCR5G2D8dnVMt3IjRzdEgr58pM2neaFt6d7NN9vSBQRbaIs66Jv7xiL8qYfAsHCZ_Q95QRaPgnFO6qcmxVMGdIaWNuQLTka8wOmhQy6USdCUFLOx_X8MfgCAI37Mzji3vW_5ZYx7mFHke18GRHcdJheQksu3T07kIvBBdqMgiUwgg6GXL9VsaFJvoMG1IZlpHVoeeEBXa0h7bFmd_Yug4m6Ymg1dFkme973TPTolL3ZHMHVJMCuhLdlybQhdVtMf7H8phl43bNSLxeahvKEJpF-aDmjD2bMZ768O_AyL1iV-1_9QD_wzM4DL8McU0po97nqWn-HZP8dkvPXSM3mAUcm6vf_KbfGGhhWz656ds0KGNXPtl0TxjUwrgmWIlgVYCkFx5PAz7Xxja2Nn_KUUF8MKku7fq4fh8qTElKhevWz8uzUrm1HMZzakzODKBFcqQJ5o0I31_J2BYfIlzIAxbe0TKw6VafRq589PZN_y33sp9w0FFWZqtxspdVEr4JVFGekiymupQJTNbecGhgo9bpUTltMWurqddEtRa0NXcV068gtVXZLdYCScpuqTl24TSFnao1VacEkqq8V04d1OrflffY6k9soAFW5bVMXmttI2qEbpK6_leGgZSg7QOVbx2R7rSYDqbZAk4Nb2zcVVK3W9M6wFoBLbsl1Wl-AB-W6lnKG2kCoUDy9oK62WHUyrlJ0tWdb9fXl-5yMvX4ZbaPjLtQxO1GrE7U7Uad5zW7j7gf4QL0ZtuFhN-x1w6NueNwJQ-E7Yasbtrthpxt2FWz0jD2BN4UkMiavRvlzjjExIhLjggrjrWfgQrDglIbGpPzZwyjKS-NtguEWtq_At_8BNTSFTQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-70_R3_CFIN — E2E-70_R3_CFIN

**Swim Lanes**: Boundary Apps · CFIN · MBC · SAP S/4 (IP & IF) | **Tasks**: 15 | **Gateways**: 10

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
        n1["Receive File in Bank"]
        n2["Update Payment Remittance"]
        n16(["fa:fa-stop Payment Data Updated"])
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
        n18(["fa:fa-stop Memo Record Created"])
        n19(["fa:fa-stop APP Doc Reversed"])
        n21{{"fa:fa-code-branch Manual Approval Necessary?"}}
        n22{{"fa:fa-code-branch Approved?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch Can Be Corrected?"}}
        n25{{"fa:fa-code-branch exclusiveGateway"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch Reversal or Reprocessing?"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph MBC
        n14["Multi-Bank Connectivity (host-to-host)"]
        n15["Multi-Bank Connectivity (host-to-host)"]
    end
    subgraph SAP S/4 (IP & IF)
        n17(["fa:fa-stop Payment Details provided back to Source System (IP/IF)"])
        n20["E2E-46A R3 Direct procurement with Planning Integration - AT"]
    end
    n12 --> n3
    n3 --> n28
    n4 --> n18
    n5 --> n21
    n21 -->|"No"| n23
    n7 --> n22
    n23 --> n6
    n25 --> n5
    n24 -->|"No"| n26
    n9 --> n19
    n10 --> n29
    n26 --> n9
    n29 --> n11
    n28 --> n4
    n11 --> n27
    n27 -->|"Reversal"| n26
    n2 --> n16
    n6 --> n14
    n29 --> n2
    n8 --> n25
    n13 --> n12
    n29 --> n17
    n20 --> n13
    n21 -->|"Yes"| n7
    n1 -->|"PAIN.002 (Pay-load file)"| n15
    n14 -->|"PAIN.001 (Pay-load file)"| n1
    n28 -->|"Reprocessing"| n25
    n30 --> n8
    n22 -->|"Yes"| n23
    n22 -->|"No"| n24
    n15 --> n10
    n27 -->|"Reprocessing"| n30
    n24 -->|"Yes"| n30
    class n16 endEvt
    class n17 endEvt
    class n18 endEvt
    class n19 endEvt
    class n20 startEvt
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1uP4jYU_itWVlNmJejmSoCHVtyyQlpGaNhtVXX6YBJnsCbEyHFg2Fn-e48TO5CQeeiWB4hPvvOd-yF5M0IWEWNk3N290ZSKEXrriC3Zkc4IdTY4I50uKgV_YE7xJiFZR2Jiloo1_V7ALHf_KmFSFuAdTU5SuibPjKBviy4ag2LSRRlOs15GOI073c6e0x3mpylLGJfoD2QQm3FhTd2aMB4RfgGYpm-FHqgmNCUXseO7vhtIvYyELI1qpLEXD-Kwc5bOJewYbjEXhft5Rpb49U8aiS2cY5xkBDBbsUu-4A1JZIyC51IW5vygk0EzaSeFhK33OKTpM8hdE0Qcpy8XkWeez-h8d_eUVkbRl8enFMEnTHCWzUiMMgHi-UGgmCbJ6IM7HQee2c0EZy9k9MGe-zPH7oYykhGEbnZlcntHQp-3YrRhSaSgvaOMYWTvX7v8dWSbXX6C74YtkkYXS9O-PbAHlaWJb02tqbYUx_H_sgR55V9x9qJszZ3ADmaVLcvre1Pzlk-HOXP9sdXME-EHGpIr0iAInPklVfO-Z5nvk04Cp29OG6TPWJAjPl0Ih1O3Igw8P7D8dwlLe00v882Ks1ATOnMv8CpCf2IFY_tdQndsuQPlIfA8c7zfognLi15G4_0-K-_JT2r9_WQ8kpDQA0EBTQiiKZpA9z0Z_1yhbEB920cQJVrh046kAj2SHRUCpyGpQ63-PYBjPIpxLxNsXynMsMCoJIlA5WOpA63U8HQaLB6u-Bxgm7-SML-2nad1oy6AppxI_8arJVqSHQMHQ5j4Os4DnMwryTI0mS4rwgkW4RaGDS4yEiEGOcgzWAsAe8xhRdVZ-sDymaSEa3uaRiawDvVlepn0XTCZes4OhNchA-k745yEoiBT1xScuOUbFuUCjkxaXqEZ9MhDvtsQjnAaXQeOZiQhkqVRHhMYAgLhaq8zFOBQMGiNezDflXnpouVkipYM9jfjHxsEZcccKDmCIjgYVeF_Yc8NrH2dKQ2DAuxZhpMG1il49wkNJXid7-ESwlqkBwbzilYsE1ChhtKg0WzXCSgb4qrXSpVhQ0WnUaW1ibettzeNl39tvQ0sZ8jeEqc5TlRN4eKByK6CCfv9yTifrwnsdgLVDdEN3mnHk9cwgaY8kM_lsmmque1qUwzNTHRXtZjzfs5c_-fU_Ha1MvmQRsbhel-OKJT7xtvBRR9zzo5ZDycC7THHSUKSd4wOf0LJMVuVaPpefLebDIbouvHkklrmiaA9uWChImkq5_xABYzeFtq7J1hP_jYnzvvvirfOrMcrtP7kovvFCv2CFkFtJvz3djYRMOIZkp1KIxj1DQ5f5Cpbs5zDUK5PmSA7yflJMjYmR66auT3vuf0xenTQjBY7ThY356TgP1IBeyjBaSqX7yIVBJwtVl8Pjb_eRgMbBfV6v0F11Nkpj_ZAnd3ybOmzp-6rpwC4kIIfT8YDezJ-yGFTN3wFtDVQMff1WTF5-uw2iDRwqDwYao9NxawFdr8UVGetUfk4KAWuZrAUg68BvrKtp6bugUqRpc_KnuU2DOpQlTlbh2ap0C276WHlgIrJcppp_Uv-V4IzGqnlq_Hi4VfTtNE9tFYvYTiSjzbkYwG2KstuHW61w2t5KtJwWRhlKjShoxzV7WDbDT-r-ld3dD2r7KvCW-Zt9htmHbPZHNqMc_18J0ujHqHrUr9VOmiVDtukUBf9GlCXW_oJtS6228VOu9htF3vt4n672G8XD9rFw1YxVFWJja6xI3yHaWSM3ozitRJePSMSY1iXxrlr4Fyw9SkNjVHx-mXkxfPnjGLYM7tSeP4Xr56AuA==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E-70_R3_SAP_Transportation_Management — E2E-70_R3_SAP_Transportation_Management

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4 (IP & IF) | **Tasks**: 12 | **Gateways**: 6

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
        n1["Receive/Send Information in Carrier Invoice Reconciliation/Dispute..."]
        n2["Event updates are received in GTT"]
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n11["Feed Rates/Charges Integrators 3rd party service – Redwood"]
        n12["Carrier"]
        n13(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n14(["fa:fa-play Events Published"])
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
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
        n16["E2E-46A R3 Direct procurement with Planning Integration - AT"]
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n4
    n5 --> n18
    n7 --> n8
    n19 --> n5
    n6 --> n20
    n4 --> n19
    n9 --> n10
    n10 --> n15
    n11 --> n21
    n13 --> n11
    n17 --> n1
    n14 --> n12
    n12 --> n22
    n22 --> n17
    n21 --> n17
    n22 --> n2
    n1 --> n20
    n21 --> n19
    n2 -->|"Event Update"| n18
    n16 --> n3
    n18 --> n6
    n8 --> n9
    n20 --> n7
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVttu2zgQ_RVCRdYtYCeiLpbjhwV8UxGgQY0o2X2o94GWKJsoTQkk5cum_vcd6uJbnMW264cgczRzZuZohtSrFWcJtfrWzc0rE0z30WtLL-mKtvqoNSeKttqoAv4gkpE5p6plfNJM6Ij9XbphL98aN4OFZMX4zqARXWQUvTy00QACeRspIlRHUcnSVruVS7YicjfKeCaN9wfaS-20zFY_GmYyofLoYNsBjn0I5UzQI-wGXuCFJk7ROBPJGWnqp700bu1NcTzbxEsidVl-oegj2f7JEr0EOyVcUfBZ6hX_QuaUmx61LAwWF3LdiMGUySNAsCgnMRMLwD0bIEnE9yPk2_s92t_czMQhKfryNBMIfjEnSo1pipQGeLLWKGWc9z94o0Ho222lZfad9j84k2DsOu3YdNKH1u22EbezoWyx1P15xpPatbMxPfSdfNuW275jt-UO_l7koiI5Zhp1nZ7TO2QaBniER02mNE3_VybQVT4T9b3ONXFDJxwfcmG_64_st3xNm2MvGOBLnahcs5iekIZh6E6OUk26PrbfJx2GbtceXZAuiKYbsjsS3o-8A2HoByEO3iWs8l1WWcynMosbQnfih_6BMBjicOC8S-gNsNerKwSehST5Eg2zopxlNMhzVT0zP4G_zawnGlO2pncRvFf0INJMrohmmUBMoBGRklEJ8DoD2dCTWYqYcVZ63I2ZygtNb29vZ9ZfJ7QO0E7WVGhU5AmIoxCRFMkqUWKIPz8_n4fg4PV1ZqWkn5KOOUM6c9iCeInoNuaFgrDPlcgza7-vwqDciy4nW02lIBxNYRkEleoORUWec9PBaSrTdUihkCdT290IVmoBNT4ITYFIZ1IhVyYoB5ZdMzFoVjg2dkGBZJNlyUXxpuFaq4sn7sdvTVs5hxkx75Uqk4xpUBGKGMKxmCDQ21RzKGawJoybAxL4Pp0SeheEpc4KTYs5Z2pJkwt_Bx91hQKzjeoQrk1vhHPK36haBTk_F_T2VUSDKYruPPTxYYp-Qw_haUkuNPCZwvsBGhTK8mhAL6AH-vj8-OlcP88IK-mp51dzkF9x9cF1SqWZ38PcvjTjB6M9IjwuuGGqNT4P75qZ3dK4-A-pApMqU_rgGFGtOdxqMPHjLC7Kf96G9Y7NRPVUTb8iKBiF0fiK_32TJppEaMP0Eg0KncEIcgozcyUA28cMIxMIC6olmxfltg4WVMQ7NIR1EmYE_6VS7B-nTOksR8-PKK8nF172mynDpXrOpON1B-jJhbyw7LoMKWSlS1n_lBMh4Fo77Jo5ZzpocHkY9H72MKjC7n8pzLF_-egRLup0focxrU2_MnGvtoPKbkx8X9l-bXcrs7n3hFeH39d27Y6b59iugYYA45oBN0BdED4AdQkHu8nhNIBTUzSAUwM4aAB8CTQhDcVFG4eApo_S_0dzJ1RLObN-nAiFayncxu5Vdre2a_NAWAsRnFycZfPNd9A57r2D-_W3zDnafcc7aC76c7h3Hb6_CkPhV2F8HXYa2GpbKwoXM0us_qtVfkHDV3ZCU1Jwbe3bFoGTIdqJ2OqXX5pWdfGOGYEtW1Xg_h8uS5b8" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products), E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry, E2E-70_R3_CFIN, E2E-70_R3_SAP_Transportation_Management | |
| External Partners/
Supplier | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products), E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry,  | |
| OSAT | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products),  | |
| SAP S/4 (IP & IF) | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products), E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry, E2E-70_R3_CFIN, E2E-70_R3_SAP_Transportation_Management | |
| CFIN | E2E-70_R3_CFIN,  | |
| MBC | E2E-70_R3_CFIN,  | |
| External Partners/
Supplier
 | E2E-70_R3_SAP_Transportation_Management | |

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

    subgraph E2E70CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E70CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E70CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E70CDAA_e_g_XEUS -.-> E2E70CDAD_e_g_Azure_SQL
    end
    style E2E70CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E70CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E70CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E70CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E70CDAA_e_g_MES_300 -.-> E2E70CDAD_e_g_SAP_HANA
    end
    style E2E70CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E70CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E70CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYGE20eRKyzSpxlncltilOdpXuHi0TXtVEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHHoArB0-SylOG_qAZo2MOeVNlR0ksXPZUChzp6VyFKduQzhhfKKsLkwTQ7UULEZnImysVwZPHYEozUWoUOVzS-U8Wiqk8R5TnIGOmYsYdOgauComsULZYdu-mNGDxRBq7ujRlNL5_MR3rqxVaNRpeXJdAI9OLkVwBp3luQYRomprJHEWMc-PA1K3hcNjKRZbcg3Ggaf2-2Vsf24-qJ6OTzltBwpNMubuWvq0XjgcLvpYjutUj_VquY_etbmev3JGp2x1tSw4S_tLecGjqpl7rDQaaXHv1ej3l9uJKMS_Gk4ymU2TLNrSBRQaOD_7EJ09FBr773bnzMPLw7yparZBlEAiWxDU0tTbppMz-Zd-6MhEOJ4dI_ZYChmFUTF_nWFsVP3nYK8Kv3VA-w-DYKyLQ5CsrsTIIySAPf1aSJda3ukDtw_bZvkpVIsThmoVYcNgLYgObqF3DtjW1_4V9lM7_h9cl1_45uSIfontpu35X0zaA5RHJ43sY12XfQCxjkIp5D-F1J7sgb0q9h_Em9kOId5dFp6dnz2tAVskUfUHk-kI-h4yDh5_3fxRbo3NgItu_-4tYEGrIIiOCyM3g_GJkD0a3NzZy7G_2lbVnms7Ni9Xx1dxJmnIWUOXdPTrHt_bMyaKCqpt494gc35bydhy2k6jtsAgq-erK2DmO6g039HW1a_onJyev0OMWnkE2oyzExhKXN778vwghogUXeNXCtBCJu4gDbJSXMi7SkAqwGJVEZ5Vx9QegC_VB" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E70FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E70FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E70FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E70FDAA_e_g_XEUS -.-> E2E70FDAD_e_g_Azure_SQL
    end
    style E2E70FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E70FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E70FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E70FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E70FDAA_e_g_MES_300 -.-> E2E70FDAD_e_g_SAP_HANA
    end
    style E2E70FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E70FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E70FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYGE20eSg7TSpxlncltilOdpXuHi0TXtVEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHHoArB0-SylOG_qAZo2MOeVNlR0ksXPZUChzp6VyFKZtNZ4wvlNWFSQLo9qKFiEzkzZWK4MljMKWZKDWKHC7p_CcLxVSeI8pzkDFTMeMOHQNXhURWKFssu3dTGrB4Io1dXZoyGt-_mI711QqtGg0vrkug0cCLkVwBp3luQoRomg6SOYoY58bBQDdt227lIkvuwTjQtH5_0Fsf24-qJ6OTzltBwpNMubumvq0XjocLvpYjutkj_VquY_XNbmev3NFAtzralhwk_KU92x7oA73WGw41ufbq9XrK7cWVYl6MJxlNp8iSbWi2SYaOD_7EJ09FBr773bnzMPLw7yparZBlEAiWxDU0tTbppMz-Zd26MhEOJ4dI_ZYChmFUTF_nmFsVP3nYK8Kv3VA-w-DYKyLQ5CsrsTIIySAPf1aSJda3ukDtw_bZvkpVIsThmoVYcNgLYgObqF3DtjS1_4V9lM7_h9cl1_45uSIfontpuX5X0zaA5RHJ43sY12XfQCxjkIp5D-F1J7sgb0q9h_Em9kOId5dFp6dnz2tAZskUfUHk-kI-bcbBw8_7P4qt0Tkwke3f_UUsCDVkkhFB5GZ4fjGyhqPbGws51jfrytwzTefmxer4au4kTTkLqPLuHp3jm3vmZFJB1U28e0SOb0l5Kw7bSdR2WASVfHVl7BxH9YYb-rraNf2Tk5NX6HELzyCbURZiY4nLG1_-X4QQ0YILvGphWojEXcQBNspLGRdpSAWYjEqis8q4-gMbv_Vr" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-70-R001 | Report | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-70-C001 | Conversion | Legacy data migration for R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-70.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E70C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E70C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E70CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E70CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E70C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E70CMW_e_g_Azure_Service_Bus
    E2E70CMW_e_g_Azure_Service_Bus --> E2E70C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTkfv--BP_ZHj-ae6vs0aQBvB4fQQSR-SPkloGIas8KcEv5w779No5fgydPSQB5uvWQq-B-kTDcC3Mv7h6447BVOOQmsUkqiCtqxald12cvZ-zIXvMDnvkehtbzE4K4gVAK0BF5P0qHdBe4XDu0dHaGjHgfz76V1dXhzRXpFVdWWRDyLyXp9dQeXY9d7GWs5m50WQTOb1UD4HlMFYe9ujxDbxVxiVpFoLtaV10-THgOVujfhA3zfi26HmJlT_ziTvNKsLU6nRh-YgOnKdH86l_Y0udX3Z29XWMpOE0QAr8CfN5fqjh2oLjco2-bJtXN92qh1iq-PHiYS8RaqVL0Kcq2IYT9rkTAJJMw6bLg3XaeT8b7VJKWohyruwLfXbCHt-fr5zlmkNbQ7pHFOiGUstv73k3UcgxBkT2qqh4UzE3iIKNCO_VLQskRsFm2JZhHlhXP0DpCQ9YQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-70.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E70F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E70F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E70FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E70FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E70F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E70FMW_e_g_Azure_Service_Bus
    E2E70FMW_e_g_Azure_Service_Bus --> E2E70F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTkcf-OBP_ZHj-ae6vs0aQBvB4fQQSR-SPkloGIas8KcEv5w779No5fgydPSQB5uvWQq-B-kTDcC3Mv7h6447BVOOQmsUkqiCtqxald12cvZ-zIXvMDnvkehtbzE4K4gVAK0BF5P0qHdBe4XDu0dHaGjHgfz76V1dXhzRXpFVdWWRDyLyXp9dQeXY9d7GWs5m50WQTOb1UD4HlMFYe9ujxDbxVxiVpFoLtaV10-THgOVujfhA3zfi26HmJlT_ziTvNKsLU6nRh-YgOnKdH86l_Y0udX3Z29XWMpOE0QAr8CfN5fqjh2oLjco2-bJtXN92qh1iq-PHiYS8RaqVL0Kcq2IYT9rkTAJJMw6bLg3XaeT8b7VJKWohyruwLfXbCHt-fr5zlmkNbQ7pHFOiGUstv73k3UcgxBkT2qqh4UzE3iIKNCO_VLQskRsFm2JZhHlhXP0D6pU9eQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-70-I001 | Interface | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-70-E001 | Enhancement | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-70-F001 | Form/Report | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

    subgraph E2E70CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E70CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E70CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E70CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E70CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E70CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E70CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E70CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhCRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1tslZKpWrzB4t77_z49Vl4j1OeAXbwYLCnBRUO2mtiDRvQHKQtSQ2ajrQa0qaiYjeHO2AqwTjvM13pd1JRsmRQa2p1zgsR0YcOMByVW1WmtJBsKNspNYIVB3RzpSNXLmRaqyoYv0_XpBIdo6nhmmx_0EysZZwTVoOsWYsNm5MlMLWRqBqlFdJ9VJKUFispjgwpVaS4PUq20baoHQzi4rAF-ubFBZIjZaSuZ5AjUpYe36KcMuacefYsDEO9FhW_BefMMCYTb_wUfrhXnhyz3OopZ7xSaWtmv-aVjIgj0J8GY__jAWhNp4HlvwRaR-DQswPTeAUEzo68MPRszz7wfN-Q46TB8Vil46In1s1yVZFyjQIzmBj-Yr5IIFkl7kNTQbIgJPoV47gxx8YwbnIw5M7nq3PUpZFKx_h3D1IjoxWkgvICzb8e1Wey25F_BjeK2WHUtwQ4jtM3vF8DRfbkTewYnDT2T8188_BRMko-u1_cxDRMqzt_NrUyOWfE_rsL0cUIqTqk6t7diOsgSizDeO6FDJEM39mOF1b_Q0feol9efnp8MjvrzocukLu4knNIGcT48eRVYR1voNoQmmFnj7s3Qr4wGeSkYQK3OiaN4NGuSLHT_ca4KTMiYEaJvJ5NL7Z_AG5FblI=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E70FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E70FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E70FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E70FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E70FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E70FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E70FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E70FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhCRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1tslZKpWrzB4t77_z49Vl4jxOeAnbwYLCnBRUO2mtiAzloDtJWpAZNR1oNSVNRsVvAHTCVYJz3ma70O6koWTGoNbU644UI6UMHGI7KrSpTWkByynZKDWHNAd1c6ciVC5nWqgrG75MNqUTHaGq4JtsfNBUbGWeE1SBrNiJnC7ICpjYSVaO0QroPS5LQYi3FkSGlihS3R8k22ha1g0FUHLZA37yoQHIkjNT1HDJEytLjW5RRxpwzz54HQaDXouK34JwZxmTijZ_CD_fKk2OWWz3hjFcqbc3t17ySEXEEzqb-ePbxALSmU9-avQRaR-DQs33TeAUEzo68IPBszz7wZjNDjpMGx2OVjoqeWDerdUXKDfJNf2IEy8Uyhngduw9NBfGSkPBXhKPGHBvDqMnAkDufr89Rl0YqHeHfPUiNlFaQCMoLtPh6VJ_Jbkf-6d8oZodR3xLgOE7f8H4NFOmTN7FjcNLYPzXzzcOH8Sj-7H5xY9Mwre786dRK5ZwS--8uhBcjpOqQqnt3I679MLYM47kXMkQyfGc7Xlj9Dx15i355-enxyey8Ox-6QO7ySs4BZRDhx5NXhXWcQ5UTmmJnj7s3Qr4wKWSkYQK3OiaN4OGuSLDT_ca4KVMiYE6JvJ68F9s_kRZuag==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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
*E2E-70 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

