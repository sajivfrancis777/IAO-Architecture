<div style="text-align:center; padding-top:60px;">
  <h1 style="font-size:36px; margin-top:24px;">End-to-End Integrated Processes (E2E)</h1>
  <h2 style="font-size:24px;">TOGAF BDAT — Systems Integration Summary</h2>
  <p style="font-size:18px; color:#555;">Tower: End-to-End Integrated Processes (E2E) · R1 – R5</p>
  <p style="font-size:14px; color:#888;">IAO Program · R1 – R5<br/>
  Generated: April 2026<br/>
  Sajiv Francis</p>
  <p style="font-size:12px; color:#aaa;">IAO Architecture Pipeline — Intel Confidential</p>
</div>

<style>
@media print {
  @page { size: A4; margin: 0; }
  .mermaid { page-break-inside: avoid; break-inside: avoid; overflow: visible; }
  pre, table, blockquote { page-break-inside: avoid; break-inside: avoid; }
  h2, h3, h4 { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
  a[title="View full diagram"],
  a[title="Open full-size SVG"] {
    color: #0071c5 !important;
    text-decoration: underline !important;
    font-size: 10pt !important;
  }
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
  margin-top: auto;
  padding: 6px 0;
  background: #fff;
}
@media print {
  .page-footer {
    display: none !important;
  }
}
.page-footer a { color: #00aeef; text-decoration: none; font-weight: 500; }
.page-footer a:hover { color: #0071c5; text-decoration: underline; }
nav.toc { margin: 16px 0 24px 0; }
nav.toc ol, nav.toc ul { list-style: none; padding-left: 0; margin: 0; }
nav.toc > ol > li { margin-bottom: 6px; font-weight: 600; font-size: 14px; }
nav.toc > ol > li > ul { padding-left: 28px; margin-top: 4px; }
nav.toc > ol > li > ul > li { font-weight: 400; font-size: 13px; margin-bottom: 2px; }
nav.toc a { color: #0071c5; text-decoration: none; }
nav.toc a:hover { text-decoration: underline; }
</style>

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

<a id="toc"></a>

## Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. Capability Inventory](#2-capability-inventory)
- [3. Current-State Architecture](#3-current-state-architecture)
   - [3.1 System Integration Map](#31-system-integration-map)
   - [3.2 ArchiMate Application View](#32-archimate-application-view)
   - [3.3 Data Entities](#33-data-entities)
   - [3.4 Integration Patterns](#34-integration-patterns)
   - [3.5 Technology Stack](#35-technology-stack)
- [4. Future-State Architecture](#4-future-state-architecture)
   - [4.1 System Integration Map](#41-system-integration-map)
   - [4.2 ArchiMate Application View](#42-archimate-application-view)
   - [4.3 Data Entities](#43-data-entities)
   - [4.4 Integration Patterns](#44-integration-patterns)
   - [4.5 Technology Stack](#45-technology-stack)
- [5. Transformation Analysis](#5-transformation-analysis)
   - [5.1 System Landscape Changes](#51-system-landscape-changes)
   - [5.2 Integration Complexity](#52-integration-complexity)
- [6. System Inventory](#6-system-inventory)

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

## 1 Executive Summary

This document provides a **L0** summary view of the systems architecture for **Tower: End-to-End Integrated Processes (E2E) · R1 – R5**.

| Metric | Current-State | Future-State | Delta |
|--------|:---:|:---:|:---:|
| **Unique Systems** | 2 | 2 | +0 |
| **System Connections** | 1 | 1 | +0 |
| **Total Flow Hops** | 53 | 53 | +0 |
| **Capabilities Covered** | 53 | 53 | — |

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

## 2 Capability Inventory

The following **53** capabilities are aggregated in this summary.
Click a capability ID to view its full TOGAF BDAT architecture document.

| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |
|:---:|:---:|---|---|:---:|:---:|
| 1 | [E2E-80](towers/E2E/E2E-80 R2 Customer Requests Expedite/E2E-80/output/docs/systems-architecture/E2E-80-Architecture.html) | R2A Option 1  Customer Requests Expedite - Service Fee with Existing SO | E2E-80 R2 Customer Requests Expedite | 1 | 1 |
| 2 | [E2E-08](towers/E2E/Forecast to Stock/E2E-08/output/docs/systems-architecture/E2E-08-Architecture.html) | E2E-08 | Forecast to Stock | 1 | 1 |
| 3 | [E2E-110](towers/E2E/Forecast to Stock/E2E-110/output/docs/systems-architecture/E2E-110-Architecture.html) | IMR Flow | Forecast to Stock | 1 | 1 |
| 4 | [E2E-113](towers/E2E/Forecast to Stock/E2E-113/output/docs/systems-architecture/E2E-113-Architecture.html) | R3 IMR Labs Process | Forecast to Stock | 1 | 1 |
| 5 | [E2E-117](towers/E2E/Forecast to Stock/E2E-117/output/docs/systems-architecture/E2E-117-Architecture.html) | E2E-117 | Forecast to Stock | 1 | 1 |
| 6 | [E2E-118](towers/E2E/Forecast to Stock/E2E-118/output/docs/systems-architecture/E2E-118-Architecture.html) | E2E-118 | Forecast to Stock | 1 | 1 |
| 7 | [E2E-122](towers/E2E/Forecast to Stock/E2E-122/output/docs/systems-architecture/E2E-122-Architecture.html) | E2E-122 | Forecast to Stock | 1 | 1 |
| 8 | [E2E-45](towers/E2E/Forecast to Stock/E2E-45/output/docs/systems-architecture/E2E-45-Architecture.html) | E2E-45 | Forecast to Stock | 1 | 1 |
| 9 | [E2E-67](towers/E2E/Forecast to Stock/E2E-67/output/docs/systems-architecture/E2E-67-Architecture.html) | E2E-67 | Forecast to Stock | 1 | 1 |
| 10 | [E2E-68](towers/E2E/Forecast to Stock/E2E-68/output/docs/systems-architecture/E2E-68-Architecture.html) | -Intel Foundry   NPI planning and execution processes | Forecast to Stock | 1 | 1 |
| 11 | [E2E-71](towers/E2E/Forecast to Stock/E2E-71/output/docs/systems-architecture/E2E-71-Architecture.html) | E2E-71 | Forecast to Stock | 1 | 1 |
| 12 | [E2E-72](towers/E2E/Forecast to Stock/E2E-72/output/docs/systems-architecture/E2E-72-Architecture.html) | IP | Forecast to Stock | 1 | 1 |
| 13 | [E2E-73](towers/E2E/Forecast to Stock/E2E-73/output/docs/systems-architecture/E2E-73-Architecture.html) | R3 Hybrid Manufacturing process with external Wafer Procurement & Internal processing of | Forecast to Stock | 1 | 1 |
| 14 | [E2E-74](towers/E2E/Forecast to Stock/E2E-74/output/docs/systems-architecture/E2E-74-Architecture.html) | R3 Internal manufacturing process for Finished Goods in Intel Foundry with Planning integrati | Forecast to Stock | 1 | 1 |
| 15 | [E2E-76](towers/E2E/Forecast to Stock/E2E-76/output/docs/systems-architecture/E2E-76-Architecture.html) | Internal manufacturing process for Finished Goods in Intel Foundry with sales to External cus | Forecast to Stock | 1 | 1 |
| 16 | [E2E-84](towers/E2E/Forecast to Stock/E2E-84/output/docs/systems-architecture/E2E-84-Architecture.html) | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) | Forecast to Stock | 1 | 1 |
| 17 | [E2E-94](towers/E2E/Forecast to Stock/E2E-94/output/docs/systems-architecture/E2E-94-Architecture.html) | R3 Intel Foundry Maintenance process through spare parts (SWAP) | Forecast to Stock | 1 | 1 |
| 18 | [E2E-89](towers/E2E/Master Data/E2E-89/output/docs/systems-architecture/E2E-89-Architecture.html) | R3 Customer Master Data | Master Data | 1 | 1 |
| 19 | [E2E-90](towers/E2E/Master Data/E2E-90/output/docs/systems-architecture/E2E-90-Architecture.html) | R3 Material Master Data | Master Data | 1 | 1 |
| 20 | [E2E-91](towers/E2E/Master Data/E2E-91/output/docs/systems-architecture/E2E-91-Architecture.html) | R3 Bill of Material BOM Data | Master Data | 1 | 1 |
| 21 | [E2E-92](towers/E2E/Master Data/E2E-92/output/docs/systems-architecture/E2E-92-Architecture.html) | R3 Vendor Master Data | Master Data | 1 | 1 |
| 22 | [IF_Simplified_PO-SO_Model](towers/E2E/Order to Cash/IF_Simplified_PO-SO_Model/output/docs/systems-architecture/IF_Simplified_PO-SO_Model-Architecture.html) | IF Simplified PO-SO Model | Order to Cash | 1 | 1 |
| 23 | [Order_to_Cash_IF](towers/E2E/Order to Cash/Order_to_Cash_IF/output/docs/systems-architecture/Order_to_Cash_IF-Architecture.html) | Order to Cash (IF) | Order to Cash | 1 | 1 |
| 24 | [Order_to_Cash_IP](towers/E2E/Order to Cash/Order_to_Cash_IP/output/docs/systems-architecture/Order_to_Cash_IP-Architecture.html) | Order to Cash (IP) | Order to Cash | 1 | 1 |
| 25 | [E2E-100](towers/E2E/Procure to Pay/E2E-100/output/docs/systems-architecture/E2E-100-Architecture.html) | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box | Procure to Pay | 1 | 1 |
| 26 | [E2E-103](towers/E2E/Procure to Pay/E2E-103/output/docs/systems-architecture/E2E-103-Architecture.html) | R3 Procurement of WIINGS Replacement Related Commodities | Procure to Pay | 1 | 1 |
| 27 | [E2E-107](towers/E2E/Procure to Pay/E2E-107/output/docs/systems-architecture/E2E-107-Architecture.html) | R3 - Partner Owned Equipment Order | Procure to Pay | 1 | 1 |
| 28 | [E2E-112](towers/E2E/Procure to Pay/E2E-112/output/docs/systems-architecture/E2E-112-Architecture.html) | R3 Raw Silicon Procurement | Procure to Pay | 1 | 1 |
| 29 | [E2E-114](towers/E2E/Procure to Pay/E2E-114/output/docs/systems-architecture/E2E-114-Architecture.html) | R4 SIMS Harvest Process | Procure to Pay | 1 | 1 |
| 30 | [E2E-115](towers/E2E/Procure to Pay/E2E-115/output/docs/systems-architecture/E2E-115-Architecture.html) | R3 Inter-company Asset Transfer Process | Procure to Pay | 1 | 1 |
| 31 | [E2E-116](towers/E2E/Procure to Pay/E2E-116/output/docs/systems-architecture/E2E-116-Architecture.html) | R3 Wafer Reclaim Process | Procure to Pay | 1 | 1 |
| 32 | [E2E-119](towers/E2E/Procure to Pay/E2E-119/output/docs/systems-architecture/E2E-119-Architecture.html) | R3 Shipping Rejects Inventory Movement | Procure to Pay | 1 | 1 |
| 33 | [E2E-121](towers/E2E/Procure to Pay/E2E-121/output/docs/systems-architecture/E2E-121-Architecture.html) | R3 RM Bailed Inventory Movement (Straddle) | Procure to Pay | 1 | 1 |
| 34 | [E2E-123](towers/E2E/Procure to Pay/E2E-123/output/docs/systems-architecture/E2E-123-Architecture.html) | TD Substrates Manufacturing Process | Procure to Pay | 1 | 1 |
| 35 | [E2E-40](towers/E2E/Procure to Pay/E2E-40/output/docs/systems-architecture/E2E-40-Architecture.html) | R3 Sourcing Request-Project to Contracts for Direct-Capital on Ariba with Pricing Updates | Procure to Pay | 1 | 1 |
| 36 | [E2E-41](towers/E2E/Procure to Pay/E2E-41/output/docs/systems-architecture/E2E-41-Architecture.html) | R3 Sourcing Request | Procure to Pay | 1 | 1 |
| 37 | [E2E-43](towers/E2E/Procure to Pay/E2E-43/output/docs/systems-architecture/E2E-43-Architecture.html) | Process Procurement Card Invoice | Procure to Pay | 1 | 1 |
| 38 | [E2E-44](towers/E2E/Procure to Pay/E2E-44/output/docs/systems-architecture/E2E-44-Architecture.html) | R3 - Intel Owned Consignment with Planning Integration | Procure to Pay | 1 | 1 |
| 39 | [E2E-46](towers/E2E/Procure to Pay/E2E-46/output/docs/systems-architecture/E2E-46-Architecture.html) | R3 Direct procurement with Planning Integration-AT | Procure to Pay | 1 | 1 |
| 40 | [E2E-47](towers/E2E/Procure to Pay/E2E-47/output/docs/systems-architecture/E2E-47-Architecture.html) | Purchase Requisition to Payments for Direct procurement with planning integration - Fab Mater | Procure to Pay | 1 | 1 |
| 41 | [E2E-49](towers/E2E/Procure to Pay/E2E-49/output/docs/systems-architecture/E2E-49-Architecture.html) | R3 Purchase Requisition to Payments for procurement with financial planning and asset managem | Procure to Pay | 1 | 1 |
| 42 | [E2E-50](towers/E2E/Procure to Pay/E2E-50/output/docs/systems-architecture/E2E-50-Architecture.html) | Purchase Requisition to Payments for Indirect - Construction (Small Construction IPCS, Mainte | Procure to Pay | 1 | 1 |
| 43 | [E2E-51](towers/E2E/Procure to Pay/E2E-51/output/docs/systems-architecture/E2E-51-Architecture.html) | Purchase Requisition to Payments for Indirect Materials (Non-IPN and Non-Inventoried) ​ | Procure to Pay | 1 | 1 |
| 44 | [E2E-52](towers/E2E/Procure to Pay/E2E-52/output/docs/systems-architecture/E2E-52-Architecture.html) | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement | Procure to Pay | 1 | 1 |
| 45 | [E2E-53](towers/E2E/Procure to Pay/E2E-53/output/docs/systems-architecture/E2E-53-Architecture.html) | Purchase Requisition to Payments for Indirect procurement (simple material or services like H | Procure to Pay | 1 | 1 |
| 46 | [E2E-57](towers/E2E/Procure to Pay/E2E-57/output/docs/systems-architecture/E2E-57-Architecture.html) | R3 Subcontracting with Planning integration- Foundry,OSAT,ODM | Procure to Pay | 1 | 1 |
| 47 | [E2E-59](towers/E2E/Procure to Pay/E2E-59/output/docs/systems-architecture/E2E-59-Architecture.html) | R3 Rework Re-localization in Factory​ | Procure to Pay | 1 | 1 |
| 48 | [E2E-61](towers/E2E/Procure to Pay/E2E-61/output/docs/systems-architecture/E2E-61-Architecture.html) | R3 Consignment Material - Vendor | Procure to Pay | 1 | 1 |
| 49 | [E2E-62](towers/E2E/Procure to Pay/E2E-62/output/docs/systems-architecture/E2E-62-Architecture.html) | R3 Vendor Return for Direct Material | Procure to Pay | 1 | 1 |
| 50 | [E2E-70](towers/E2E/Procure to Pay/E2E-70/output/docs/systems-architecture/E2E-70-Architecture.html) | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte | Procure to Pay | 1 | 1 |
| 51 | [E2E-88](towers/E2E/Procure to Pay/E2E-88/output/docs/systems-architecture/E2E-88-Architecture.html) | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme | Procure to Pay | 1 | 1 |
| 52 | [E2E-96](towers/E2E/Procure to Pay/E2E-96/output/docs/systems-architecture/E2E-96-Architecture.html) | R3 Straddle & R4 SIMS Design with Returns | Procure to Pay | 1 | 1 |
| 53 | [E2E-98](towers/E2E/Procure to Pay/E2E-98/output/docs/systems-architecture/E2E-98-Architecture.html) | R3 Equipment Product Supporting Items (PSI) Procurement | Procure to Pay | 1 | 1 |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

## 3 Current-State Architecture

Aggregated current-state view of **2** systems with **1** unique connections across **53** flow hops.

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 3.1 System Integration Map

```mermaid
graph LR
    SC_e_g__MES_300["📦 e.g. MES 300"]
    SC_e_g__XEUS["📦 e.g. XEUS"]

    SC_e_g__MES_300 -->|"e.g. Direct / API / File | 53 flows"| SC_e_g__XEUS
```

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 3.2 ArchiMate Application View

```mermaid
graph TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["📦 Application Layer — Systems Integration"]
        direction LR
        SCA_e_g__MES_300["📦 e.g. MES 300"]
        SCA_e_g__XEUS["📦 e.g. XEUS"]
    end

    SCA_e_g__MES_300 -->|"e.g. Direct / API / File"| SCA_e_g__XEUS

    class SCA_e_g__MES_300 app
    class SCA_e_g__XEUS app
    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px
```

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Data Entities

**1** data entities in current-state flows.

| # | Data Entity | Source | Target | Owner | Classification | Volume | Master/Txn |
|:---:|---|---|---|---|---|---|---|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 3.4 Integration Patterns

**1** integration patterns in current-state.

| # | Pattern | Middleware | Protocol | Auth Method | Flow Chain |
|:---:|---|---|---|---|---|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert | e.g. MES Route to ICOST |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 3.5 Technology Stack

**2** technology platforms in current-state.

| # | Platform | Type | Systems | Environment |
|:---:|---|---|---|---|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

## 4 Future-State Architecture

Aggregated future-state view of **2** systems with **1** unique connections across **53** flow hops.

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 4.1 System Integration Map

```mermaid
graph LR
    SF_e_g__MES_300["📦 e.g. MES 300"]
    SF_e_g__XEUS["📦 e.g. XEUS"]

    SF_e_g__MES_300 -->|"e.g. Direct / API / File | 53 flows"| SF_e_g__XEUS
```

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 4.2 ArchiMate Application View

```mermaid
graph TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["📦 Application Layer — Systems Integration"]
        direction LR
        SFA_e_g__MES_300["📦 e.g. MES 300"]
        SFA_e_g__XEUS["📦 e.g. XEUS"]
    end

    SFA_e_g__MES_300 -->|"e.g. Direct / API / File"| SFA_e_g__XEUS

    class SFA_e_g__MES_300 app
    class SFA_e_g__XEUS app
    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px
```

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Entities

**1** data entities in future-state flows.

| # | Data Entity | Source | Target | Owner | Classification | Volume | Master/Txn |
|:---:|---|---|---|---|---|---|---|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 4.4 Integration Patterns

**1** integration patterns in future-state.

| # | Pattern | Middleware | Protocol | Auth Method | Flow Chain |
|:---:|---|---|---|---|---|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert | e.g. MES Route to ICOST |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 4.5 Technology Stack

**2** technology platforms in future-state.

| # | Platform | Type | Systems | Environment |
|:---:|---|---|---|---|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

## 5 Transformation Analysis

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 5.1 System Landscape Changes

**Continuing Systems:** 2

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Integration Complexity

| System | Current Connections | Future Connections | Delta |
|---|:---:|:---:|:---:|
| e.g. MES 300 | 1 | 1 | — |
| e.g. XEUS | 1 | 1 | — |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>End-to-End Integrated Processes (E2E)</span></div>
<div style="page-break-before: always;"></div>

## 6 System Inventory

| # | System | IAPM ID | Status |
|:---:|---|---|---|
| 1 | e.g. MES 300 | - | N/A |
| 2 | e.g. XEUS | - | N/A |

