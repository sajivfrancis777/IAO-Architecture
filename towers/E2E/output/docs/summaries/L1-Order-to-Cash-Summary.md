<div style="text-align:center; padding-top:60px;">
  <h1 style="font-size:36px; margin-top:24px;">Order to Cash</h1>
  <h2 style="font-size:24px;">TOGAF BDAT — Systems Integration Summary</h2>
  <p style="font-size:18px; color:#555;">Tower: End-to-End Integrated Processes (E2E) · Process: Order to Cash · R1 – R5</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

## 1 Executive Summary

This document provides a **L1** summary view of the systems architecture for **Tower: End-to-End Integrated Processes (E2E) · Process: Order to Cash · R1 – R5**.

| Metric | Current-State | Future-State | Delta |
|--------|:---:|:---:|:---:|
| **Unique Systems** | 2 | 2 | +0 |
| **System Connections** | 1 | 1 | +0 |
| **Total Flow Hops** | 3 | 3 | +0 |
| **Capabilities Covered** | 3 | 3 | — |

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

## 2 Capability Inventory

The following **3** capabilities are aggregated in this summary.
Click a capability ID to view its full TOGAF BDAT architecture document.

| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |
|:---:|:---:|---|---|:---:|:---:|
| 1 | [IF_Simplified_PO-SO_Model](towers/E2E/Order to Cash/IF_Simplified_PO-SO_Model/output/docs/systems-architecture/IF_Simplified_PO-SO_Model-Architecture.html) | IF Simplified PO-SO Model | Order to Cash | 1 | 1 |
| 2 | [Order_to_Cash_IF](towers/E2E/Order to Cash/Order_to_Cash_IF/output/docs/systems-architecture/Order_to_Cash_IF-Architecture.html) | Order to Cash (IF) | Order to Cash | 1 | 1 |
| 3 | [Order_to_Cash_IP](towers/E2E/Order to Cash/Order_to_Cash_IP/output/docs/systems-architecture/Order_to_Cash_IP-Architecture.html) | Order to Cash (IP) | Order to Cash | 1 | 1 |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

## 3 Current-State Architecture

Aggregated current-state view of **2** systems with **1** unique connections across **3** flow hops.

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 3.1 System Integration Map

```mermaid
graph LR
    SC_e_g__MES_300["📦 e.g. MES 300"]
    SC_e_g__XEUS["📦 e.g. XEUS"]

    SC_e_g__MES_300 -->|"e.g. Direct / API / File | 3 flows"| SC_e_g__XEUS
```

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
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

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Data Entities

**1** data entities in current-state flows.

| # | Data Entity | Source | Target | Owner | Classification | Volume | Master/Txn |
|:---:|---|---|---|---|---|---|---|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 3.4 Integration Patterns

**1** integration patterns in current-state.

| # | Pattern | Middleware | Protocol | Auth Method | Flow Chain |
|:---:|---|---|---|---|---|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert | e.g. MES Route to ICOST |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 3.5 Technology Stack

**2** technology platforms in current-state.

| # | Platform | Type | Systems | Environment |
|:---:|---|---|---|---|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

## 4 Future-State Architecture

Aggregated future-state view of **2** systems with **1** unique connections across **3** flow hops.

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 4.1 System Integration Map

```mermaid
graph LR
    SF_e_g__MES_300["📦 e.g. MES 300"]
    SF_e_g__XEUS["📦 e.g. XEUS"]

    SF_e_g__MES_300 -->|"e.g. Direct / API / File | 3 flows"| SF_e_g__XEUS
```

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
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

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Entities

**1** data entities in future-state flows.

| # | Data Entity | Source | Target | Owner | Classification | Volume | Master/Txn |
|:---:|---|---|---|---|---|---|---|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 4.4 Integration Patterns

**1** integration patterns in future-state.

| # | Pattern | Middleware | Protocol | Auth Method | Flow Chain |
|:---:|---|---|---|---|---|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert | e.g. MES Route to ICOST |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 4.5 Technology Stack

**2** technology platforms in future-state.

| # | Platform | Type | Systems | Environment |
|:---:|---|---|---|---|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

## 5 Transformation Analysis

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 5.1 System Landscape Changes

**Continuing Systems:** 2

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Integration Complexity

| System | Current Connections | Future Connections | Delta |
|---|:---:|:---:|:---:|
| e.g. MES 300 | 1 | 1 | — |
| e.g. XEUS | 1 | 1 | — |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>Order to Cash</span></div>
<div style="page-break-before: always;"></div>

## 6 System Inventory

| # | System | IAPM ID | Status |
|:---:|---|---|---|
| 1 | e.g. MES 300 | - | N/A |
| 2 | e.g. XEUS | - | N/A |

