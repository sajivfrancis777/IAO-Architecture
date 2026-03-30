<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">L-120 — Manage Line Replenishment - FTS (IF)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Forecast to Stock (IF) (FTS-IF) Tower<br/>
  Capability L-120 · L Logistics and Inventory Management - FTS (IF)</p>
  <p style="font-size:14px; color:#888;">IAO Program · Release 3<br/>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **L-120 Manage Line Replenishment - FTS (IF)** within the IAO program. It includes 5 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Forecast to Stock (IF) (FTS-IF) |
| **Process Group** | L Logistics and Inventory Management - FTS (IF) |
| **Capability** | L-120 - Manage Line Replenishment - FTS (IF) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 2 Reports, 18 Interfaces, 3 Conversions, 19 Enhancements, 9 Forms, 3 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Forecast to Stock (IF) |
| **L1 Process** | L Logistics and Inventory Management - FTS (IF) |
| **L2 Capability** | L-120 - Manage Line Replenishment - FTS (IF) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Intel Foundry Supply Chain Integration | Integrate Intel Foundry manufacturing and logistics into unified S/4 HANA supply chain | IDM 2.0 Foundry Enablement | High |
| 2 | Warehouse & Logistics Modernization | Modernize warehouse management and shipping processes with EWM integration | Supply Chain Digital Transformation | High |
| 3 | Production Planning Optimization | Enable MRP-driven production planning with real-time material availability | Manufacturing Excellence | Medium |
| 4 | L-120 Process Migration | Migrate Manage Line Replenishment - FTS (IF) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Supply Chain (Intel Foundry) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Fulfillment Lead Time | < 48 hours | Time from production completion to shipment dispatch | 72 hours (legacy) | Logistics Manager |
| Inventory Accuracy | > 99.5% | Physical vs system inventory match rate | 97.8% (current) | Warehouse Manager |
| MRP Planning Cycle | < 4 hours | End-to-end MRP run including exception processing | 8 hours (legacy) | Planning Lead |
| L-120 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **5 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for L-120 Manage Line Replenishment - FTS (IF).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | L-120-010_Receive_Empty_Kanban_Signal_-_FTS_(IF) | L-120-010_Receive_Empty_Kanban_Signal_-_FTS_(IF) | FTS IF - Manufacturing System Engineer (MSE), LOG IF - Inventory Controller | 4 | 0 |
| 2 | L-120-020_Generate_Kanban_Replenishment_Order_-_FTS_(IF) | L-120-020_Generate_Kanban_Replenishment_Order_-_FTS_(IF) | Boundary Apps, FTS IF - Batch System User, FTS IF - Manufacturing System Engineer (MSE) | 8 | 1 |
| 3 | L-120-120_Receive_Kanban_Materials_-_External_Procurement_-_FTS_(IF) | L-120-120_Receive_Kanban_Materials_-_External_Procurement_-_FTS_(IF) | FTS IF - Batch System User, FTS IF - Manufacturing System Engineer (MSE), Warehouse Operative (Extended Warehouse Management) | 7 | 0 |
| 4 | L-120-140_Issue_Material_to_Production_Order_-_FTS_(IF) | L-120-140_Issue_Material_to_Production_Order_-_FTS_(IF) | FTS IF - Materials Planner, LOG IF - Warehouse Manager, Material Handler | 6 | 0 |
| 5 | L-120-150_Deliver_Materials_to_Production_-_FTS_(IF) | L-120-150_Deliver_Materials_to_Production_-_FTS_(IF) | FTS IF - Batch System User, Material Handler - DMRA, Warehouse Manager - 3PL | 16 | 1 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 L-120-010_Receive_Empty_Kanban_Signal_-_FTS_(IF) — L-120-010_Receive_Empty_Kanban_Signal_-_FTS_(IF)

**Swim Lanes**: FTS IF - Manufacturing System Engineer (MSE) · LOG IF - Inventory Controller | **Tasks**: 4 | **Gateways**: 0

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
    subgraph FTS IF - Manufacturing System Engineer (MSE)
        n1[["fa:fa-cog Trigger Kanban Empty Scan"]]
        n2[["fa:fa-cog Receive Production Demand"]]
        n3["Send Kanban Signal"]
        n5(["fa:fa-play Request Initiate to Deliver Materials to Production"])
    end
    subgraph LOG IF - Inventory Controller
        n4["Receive Empty Kanban Signal"]
        n6(["fa:fa-stop Kanban Empty Signal Received"])
    end
    n4 --> n6
    n1 --> n3
    n2 --> n1
    n5 --> n2
    n3 --> n4
    class n1 serviceTask
    class n2 serviceTask
    class n5 startEvt
    class n6 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVU1v2zgQ_SuEgsBdQAb0aXl1KODIUhFsgy6q7PbQ9EBLQ5kIRaok5cQb-L8vackfcZteqoOBeZx5b-aJGr84lajBSZ3r6xfKqU7Ry0SvoYVJiiYrrGDiogH4F0uKVwzUxOYQwXVJ_9un-VH3bNMsVuCWsq1FS2gEoH9uXbQwhcxFCnM1VSApmbiTTtIWy20mmJA2-wrmxCN7tfHoRsga5CnB8xK_ik0poxxOcJhESVTYOgWV4PUrUhKTOakmO9scE0_VGku9b79XcIefv9Bar01MMFNgcta6ZR_xCpidUcveYlUvNwczqLI63BhWdriivDF45BlIYv54gmJvt0O76-sHfhRF98sHjsxTMazUEghS2sD5RiNCGUuvomxRxJ6rtBSPkF4FebIMA7eyk6RmdM-15k6fgDZrna4Eq8fU6ZOdIQ26Z1c-p4Hnyq35vdACXp-UslkwD-ZHpZvEz_zsoEQI-S0l46u8x-px1MrDIiiWRy0_nsWZ9yPfYcxllCz8S59AbmgFZ6RFUYT5yap8Fvve26Q3RTjzsgvSBmt4wtsT4Z9ZdCQs4qTwkzcJB73LLvvV31JUB8Iwj4v4SJjc-MUieJMwWvjRfOzQ8DQSd2tU3JfotkBTdId5T3Cle2kuFyq3SkOLct6YjwAkendX5n8Mpfbh_tevDw7BKcHTSjToXtKmMWl_Yb7CHOVtp7eorDB_cL59OysLXpd9hgroBpAZqe4rTQVHS2gxry_KQlNVmst14C9pwzEzSWc58bsjdceM5Z_hew9Ko1uzbKh5DUgLQ86MnDSzarC7QlnwJG4IxxmN1oVPHz99GHy65RvgWsgtysz9lYIxkGdtRKaLw1iDDb_oeXbqWWnRXdi3Lzh4VP-kOR6h6fS9oRlDfwjDMQyGcLzoPB7CYAzDIYzOLphlOPsMXp0Eb57ExxXzCp6N28BxnRZki2ntpC_OfsObf4EaCO6Zdnaug3styi2vnHS_CZ2-q83rWVJsjG8HcPc_fsX9Mw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 L-120-020_Generate_Kanban_Replenishment_Order_-_FTS_(IF) — L-120-020_Generate_Kanban_Replenishment_Order_-_FTS_(IF)

**Swim Lanes**: Boundary Apps · FTS IF - Batch System User · FTS IF - Manufacturing System Engineer (MSE) | **Tasks**: 8 | **Gateways**: 1

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
        n8["Receive STO"]
        n11(["fa:fa-stop Kanban Replenishment Order Created"])
        n12["Reservation Creation Signal Sent"]
    end
    subgraph FTS IF - Batch System User
        n1["fa:fa-user Create STO"]
        n2["fa:fa-user Receive Empty Kanban Signal"]
        n13{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph FTS IF - Manufacturing System Engineer (MSE)
        n3[["fa:fa-cog Trigger Kanban Empty Scan"]]
        n4[["fa:fa-cog Receive Production Demand"]]
        n5["Capture STO"]
        n6["Send kanban Signal"]
        n7["Capture STO Signal Sent"]
        n9(["fa:fa-play Request Initiate to Deliver Materials to Production"])
        n10(["fa:fa-stop Reservation Information Captured"])
    end
    n3 --> n6
    n5 --> n10
    n7 --> n5
    n9 --> n4
    n4 --> n3
    n13 --> n7
    n2 --> n1
    n6 --> n2
    n1 --> n13
    n8 --> n11
    n13 --> n12
    n12 --> n8
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n9 startEvt
    class n10 endEvt
    class n11 endEvt
    class n12 startEvt
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVk2PozgQ_SsWrVZmJSLxGdIcVkpIWLV2WrNqemYOkz04YIjVxrC26XQmyn9fOxhCmI72sByi1HPVq1flsuFopFWGjNC4vz9iikUIjhOxQyWahGCyhRxNTNAC3yDDcEsQnyifvKIiwT_PbrZXvys3hcWwxOSg0AQVFQJfH02wkIHEBBxSPuWI4XxiTmqGS8gOUUUqprzv0Dy38nM2vbSsWIbYxcGyAjv1ZSjBFF1gN_ACL1ZxHKUVza5Icz-f5-nkpMSRap_uIBNn-Q1HT_D9O87ETto5JBxJn50oyWe4RUTVKFijsLRhb10zMFd5qGxYUsMU00LiniUhBunrBfKt0wmc7u83tE8KPj9vKJBPSiDnK5QDLiS8fhMgx4SEd160iH3L5IJVryi8c9bBynXMVFUSytItUzV3uke42IlwW5FMu073qobQqd9N9h46lskO8neUC9HskimaOXNn3mdaBnZkR12mPM__VybZV_YC-avOtXZjJ171uWx_5kfWr3xdmSsvWNjjPiH2hlM0II3j2F1fWrWe-bZ1m3QZuzMrGpEWUKA9PFwIHyKvJ4z9ILaDm4RtvrHKZvsXq9KO0F37sd8TBks7Xjg3Cb2F7c21QslTMFjvwLJqzrMMFnXN2zX10PmPjfGMUoTfEEhevmyMvweLtv1JLucwzOGUi6oGf0K6hRQ8o5ogivmuRFSAL-pcgYgh2YRMEvw2ZHDO_KrpUOCKtm7qT4ILCglIJEOfVM7VSHb8koDHGEzBEop0B5IDF6gEXyXfMEkvUo2LVvJrNc61W1f1uqzFoausVTXqgns8dpGQsWrPp5AIUEMGCUHkj3bvN8bp9J9VPEHa5DAVDZMnu6tmTQt5A0lFn56S9bB57o9ecVoV4IXhopBuWmqrO0khlXKHer3rsK5OOU9Zk557v0IlpNkozJdREayltg96N5OLcqsy8Hq7T8E1wYc7fHZ8uExVTeSpeUb_NIgL8CjfF1htnaikRCJFM9kxgdR1zxV4KWE8ZtZoUIcj90jzipV6_Fp9gzHtd4u6YDr9XZaqTb81bX00adDavjYfWtPTptearjZtTRZo29Fk2py1ptN569Uueq5te8Rm9wGabz64NhRNd11ewc7HsDu8Cq9WvJsrD_1r5jqxpV8J16j9Ierc4HC7W9QwjRLJDcOZER6N87eC_J7IUA4bIoyTacBGVMmBpkZ4fqcaTZ3JyBWG8rSVLXj6F6X-q9s=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 L-120-120_Receive_Kanban_Materials_-_External_Procurement_-_FTS_(IF) — L-120-120_Receive_Kanban_Materials_-_External_Procurement_-_FTS_(IF)

**Swim Lanes**: FTS IF - Batch System User · FTS IF - Manufacturing System Engineer (MSE) · Warehouse Operative (Extended Warehouse Management) | **Tasks**: 7 | **Gateways**: 0

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
    subgraph FTS IF - Batch System User
        n2["fa:fa-user Receive Goods Against STO"]
        n3["fa:fa-user Receive Kanban Full Signal"]
        n9(["fa:fa-stop Deliver Materials to Production"])
    end
    subgraph FTS IF - Manufacturing System Engineer (MSE)
        n4[["fa:fa-cog Close STO"]]
        n5["120-120-030 Goods received against Reservation signal sent"]
        n6["Trigger Kanban Full scan"]
        n7["Send Kanban Full Signal"]
    end
    subgraph Warehouse Operative (Extended Warehouse Management)
        n1["fa:fa-user Issue Goods to STO /B2B order"]
        n8(["fa:fa-play Pick/Pack Process completes"])
    end
    n2 --> n5
    n5 --> n4
    n4 --> n6
    n6 --> n7
    n7 --> n3
    n3 --> n9
    n1 --> n2
    n8 --> n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n8 startEvt
    class n9 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVdtu2zgQ_RVCQeAUkFFdLUcPBXzTItgNGlRu-9D0gaYomTBNCiSV2Bv43zu05Fua9KUCbOCMZs7MnBGHLw6RBXVS5_r6hQlmUvTSM0u6pr0U9RZY056LWsM3rBhecKp71qeUwuTs_72bH9Ub62ZtGV4zvrXWnFaSoq93LhpBIHeRxkL3NVWs7Lm9WrE1VtuJ5FJZ7ys6LL1yn617NZaqoOrk4HmJT2II5UzQkzlMoiTKbJymRIrigrSMy2FJejtbHJfPZImV2ZffaHqPN99ZYZaAS8w1BZ-lWfP_8IJy26NRjbWRRj0dxGDa5hEgWF5jwkQF9sgDk8JidTLF3m6HdtfXj-KYFM2njwLBQzjWekpLpA2YZ08GlYzz9CqajLLYc7VRckXTq2CWTMPAJbaTFFr3XCtu_5myamnSheRF59p_tj2kQb1x1SYNPFdt4f9VLiqKU6bJIBgGw2OmceJP_MkhU1mWf5UJdFVzrFddrlmYBdn0mMuPB_HE-53v0OY0Skb-a52oemKEnpFmWRbOTlLNBrHvvU86zsKBN3lFWmFDn_H2RHg7iY6EWZxkfvIuYZvvdZXN4kFJciAMZ3EWHwmTsZ-NgncJo5EfDbsKgadSuF6ibJ6juwz10RgbskT5Vhu6Rl9BjdbRPiL48eiUOC1x3-qOvlBC2RNF_0hZaDSqMBPaoHz--dH5eRYVvh31LxYLLFDWcI5yVgnML8Nub45x2sgaTSmHMIXuQUt7wDUyEoEIRUMMkwKCP7TR8PW919w9Fk2JiWkUnJxDkzNRwQkH5pv7fPbhrILox7ECIis04VLTrr3zQmPw8gOvb39e6HVyqLbNAuFOly_UflrY1or0vl_41oS5bHoAXHPFqgrKORdIEywuPRPwzKHVP-n4uxLfsaJLCXNAn2uqoBgYxM1sY8ATSj29BaFwBUtYmHNB_MtJ3mndHKYPswBl0MdxMEb7RXpZ7fA0zJrDQXhgZPXxAZOVnSChWiMi1zWnhuo3BikC1O9_AqU7GLcw6mDUwkEHBy1MOpi0MOxg2MLbDvotDDo4bOH5UrA-hzVzYQ7eNodvm6PzzXLxZnjczRfm226NOq6zpmqNWeGkL87-aoTrs6Albrhxdq6DGyPzrSBOur9CnKYu4IhMGYaRr1vj7hfGhFsR" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 L-120-140_Issue_Material_to_Production_Order_-_FTS_(IF) — L-120-140_Issue_Material_to_Production_Order_-_FTS_(IF)

**Swim Lanes**: FTS IF - Materials Planner · LOG IF - Warehouse Manager · Material Handler | **Tasks**: 6 | **Gateways**: 0

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
    subgraph FTS IF - Materials Planner
        n1["fa:fa-user Perform Reservation Review by Warehouse"]
        n4[["fa:fa-cog Create SAP Reservation with 201 Movement"]]
        n5[["fa:fa-cog Send Material by Warehouse"]]
    end
    subgraph LOG IF - Warehouse Manager
        n6[["fa:fa-cog Performs GI Against Reservation"]]
        n8(["fa:fa-stop Issue Material to Production Order Process Completed"])
    end
    subgraph Material Handler
        n2[["fa:fa-cog Place Order for Components through New Portal UI (IMR Factory)"]]
        n3[["fa:fa-cog Acknowledge Receipt by Factory"]]
        n7(["fa:fa-play Process Initiated to Issue Material to Production Order"])
    end
    n7 --> n2
    n2 --> n4
    n4 --> n1
    n1 --> n5
    n5 --> n3
    n3 --> n6
    n6 --> n8
    class n1 userTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P2jgU_StWRiNaKUj5JGweVmICaZE6W1Sm7UOnD8ZxEmuMHdkODDviv69NQiBpUR82D4h7fe8595zE9puFeIat2Lq_fyOMqBi8jVSJt3gUg9EGSjyyQZP4BgWBG4rlyNTknKk1-fdU5gbVqykzuRRuCT2Y7BoXHIOvSxvMdCO1gYRMjiUWJB_Zo0qQLRSHhFMuTPUdnuZOfmJrlx64yLC4FDhO5KJQt1LC8CXtR0EUpKZPYsRZ1gPNw3yao9HRDEf5HpVQqNP4tcSP8PU7yVSp4xxSiXVNqbb0E9xgajQqUZscqsXubAaRhodpw9YVRIQVOh84OiUge7mkQud4BMf7-2fWkYKn-TMD-kEUSjnHOZBKpxc7BXJCaXwXJLM0dGypBH_B8Z23iOa-ZyOjJNbSHduYO95jUpQq3nCataXjvdEQe9WrLV5jz7HFQf8OuDDLLkzJxJt6047pIXITNzkz5Xn-v5i0r-IJypeWa-GnXjrvuNxwEibOr3hnmfMgmrlDn7DYEYSvQNM09RcXqxaT0HVugz6k_sRJBqAFVHgPDxfAv5KgA0zDKHWjm4AN33DKerMSHJ0B_UWYhh1g9OCmM-8mYDBzg2k7ocYpBKxKkD6twTIFY_CoRzX7R4IVhYxh0RSah7k_nq0cxjkcG9_BCouciy34go1pUBHO9P8dwXuwOYDvUOCS68Jn6-cVRvCjA0G8AInAmhCsZ6sezJ6oEniOCx75Tp8FTGmQa5Swj7LWX1w3-ZC87dMlA82fPn9oNHfVGoPBoqd50mdqNUvwYQlmBSRMquvBB2NO33XNUvEKLKWs8WVQxYF-i1mNTpo_m_PHJBCWEiR8W1GscKYh399S0CF9hCyjvbm9wdwUItxSaAEneM60sRKoUvC6KME_-r2tuFAa7usSvFs-fgEpRIqLw_uBLL-PPUMvjO8pzgqsvUCYVMq8g7Z50BtdLKmo3hJnvUt9GRAtJzOu_Nmn37jCIjAe_62Vt6HXhEEbBk3Y7nfmNmHYhmET-m3oN-GkDSdNOL3ahQbhfPr00t71EdJb8W-uBDdXwpsrk5srUXfY99LT9ly2bGuLxRaSzIrfrNNdq-_jDOewpso62hasFV8fGLLi051k1VWm38ScQP3RbZvk8T9Hqn7L" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 L-120-150_Deliver_Materials_to_Production_-_FTS_(IF) — L-120-150_Deliver_Materials_to_Production_-_FTS_(IF)

**Swim Lanes**: FTS IF - Batch System User · Material Handler - DMRA · Warehouse Manager - 3PL | **Tasks**: 16 | **Gateways**: 1

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
    subgraph FTS IF - Batch System User
        n1["fa:fa-user Create STO"]
        n2["fa:fa-user Receive Goods Against STO"]
        n3["fa:fa-user Receive Empty Kanban Signal"]
        n4["fa:fa-user Receive Kanban Full Signal"]
        n18(["fa:fa-stop Deliver Materials to Production"])
        n20["STO Creation Signal Sent"]
        n21{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Material Handler - DMRA
        n7[["fa:fa-cog Trigger Kanban Empty Scan"]]
        n8[["fa:fa-cog Close STO"]]
        n9[["fa:fa-cog Receive Production Demand"]]
        n11["Capture STO"]
        n12["120-150-120 Goods received against STO signal sent"]
        n13["Send kanban Signal"]
        n14["Capture STO Signal Sent"]
        n15["Trigger Kanban Full scan"]
        n16["Send Kanban Full Signal"]
        n17(["fa:fa-play Request Initiate to Deliver Materials to Production"])
        n19(["fa:fa-stop STO Information Captured"])
    end
    subgraph Warehouse Manager - 3PL
        n5["fa:fa-user Pick Physical Inventory"]
        n6["fa:fa-user Issue Goods to STO via B2B"]
        n10["Receive STO"]
    end
    n7 --> n13
    n5 --> n6
    n11 --> n19
    n6 --> n2
    n2 --> n12
    n12 --> n8
    n8 --> n15
    n15 --> n16
    n14 --> n11
    n10 --> n5
    n17 --> n9
    n9 --> n7
    n13 --> n3
    n3 --> n1
    n16 --> n4
    n4 --> n18
    n1 --> n20
    n20 --> n21
    n21 --> n10
    n21 --> n14
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n17 startEvt
    class n18 endEvt
    class n19 endEvt
    class n20 startEvt
    class n21 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVm1v6jYU_itWrio2CaQ4JATyYRJvuavWalXp3f1wuw8mccCqcZjt0DLEf98xsYFQ0DQNqRXnOec5L0-OcXZeVubUS7y7ux0TTCdo19JLuqKtBLXmRNFWG9XAH0QyMudUtUxMUQo9Y38fwnC4_jBhBkvJivGtQWd0UVL07b6NhkDkbaSIUB1FJSta7dZashWR23HJS2miv9B-4ReHatY1KmVO5SnA92OcRUDlTNAT3I3DOEwNT9GsFHkjaREV_SJr7U1zvHzPlkTqQ_uVoo_k4zvL9RLsgnBFIWapV_yBzCk3M2pZGSyr5MaJwZSpI0Cw2ZpkTCwAD32AJBFvJyjy93u0v7t7Fcei6OH5VSD4ZJwoNaEFUhrg6UajgnGefAnHwzTy20rL8o0mX4JpPOkG7cxMksDoftuI23mnbLHUybzkuQ3tvJsZkmD90ZYfSeC35Rb-X9SiIj9VGveCftA_VhrFeIzHrlJRFP-rEugqX4h6s7Wm3TRIJ8daOOpFY_9zPjfmJIyH-FInKjcso2dJ0zTtTk9STXsR9m8nHaXdnj--SLogmr6T7SnhYBweE6ZRnOL4ZsK63mWX1fxJlplL2J1GaXRMGI9wOgxuJgyHOOzbDiHPQpL1EqUvM3Sfog4aEZ0t0WyrNF2hb6BGHWg-Av949QqSFKRjdEdjSWEuNHv5_dX78ywsaIY904yyDUVfyzJXaLggTCj9mdW9zpqu1nqLfiNiTgSasYUgvMkLr_MsI604v0rD_Z-ORKXLNZpQDjyJHmEm8wOikC4RiJxXmWalAPbP5zP6wIYZahHAb4ugGRX6Qg6827lKRMryXXUI12hNJOGc8q_1brx6-31NgtNz8XBcS-hXInIOPXbQ5PF5eFYj_nEcJisX6EWyxQLirAi1hrOMmCnOW-s3aWNeKvc8z8MGzTAn8UkcEG8FrV3QsNmXMVnrSl7ZEmzWBAd-B0fwF_h2P2SdPEfktChI1dqqT9piszUgeY7ebm8IDpt93H5UOILIC_EOG6Rq7c5De67yv25afNq0NYdfgWf6V0Vhsnu4_5g5QbBo_2378OBiec1U96Io5apeRjttfuJ93qrvRNJlCYcGigqyOKxV9-nhrEzUPFpPLHtDT8utYhmody82oF8pt81pe03OvVKVO_owkelzwwgaBaMLkcx5cot1vivHvkWMOp1fzCO3dlTbPWtibP0DC_RqO7BmYN3OxhboW7tv_ZHz2_z4WCC0AHaAXwNHhu3QNTCozdi5u7Xt-rfmMZvtN7S2q-b6s-O5KxC-WMAlCJwA_iUQnt0eJpG7NRtwcB3uXofD63B0He5dh-Pz27bh6d_0DG56QH73ktPE-_aFpIkOrqEg6tUcIKW9w722t6JwzFjuJTvv8KYKb7M5LUjFtbdve6TS5WwrMi85vNF51ToH5oQROHWrGtz_Ax11Yo0=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| FTS IF - Manufacturing System Engineer (MSE) | L-120-010_Receive_Empty_Kanban_Signal_-_FTS_(IF), L-120-020_Generate_Kanban_Replenishment_Order_-_FTS_(IF), L-120-120_Receive_Kanban_Materials_-_External_Procurement_-_FTS_(IF),  | |
| LOG IF - Inventory Controller | L-120-010_Receive_Empty_Kanban_Signal_-_FTS_(IF),  | |
| Boundary Apps | L-120-020_Generate_Kanban_Replenishment_Order_-_FTS_(IF),  | |
| FTS IF - Batch System User | L-120-020_Generate_Kanban_Replenishment_Order_-_FTS_(IF), L-120-120_Receive_Kanban_Materials_-_External_Procurement_-_FTS_(IF), L-120-150_Deliver_Materials_to_Production_-_FTS_(IF) | |
| Warehouse Operative (Extended Warehouse Management) | L-120-120_Receive_Kanban_Materials_-_External_Procurement_-_FTS_(IF),  | |
| FTS IF - Materials Planner | L-120-140_Issue_Material_to_Production_Order_-_FTS_(IF),  | |
| LOG IF - Warehouse Manager | L-120-140_Issue_Material_to_Production_Order_-_FTS_(IF),  | |
| Material Handler | L-120-140_Issue_Material_to_Production_Order_-_FTS_(IF),  | |
| Material Handler - DMRA | L-120-150_Deliver_Materials_to_Production_-_FTS_(IF) | |
| Warehouse Manager - 3PL | L-120-150_Deliver_Materials_to_Production_-_FTS_(IF) | |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for L-120. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

### 4.3 Data Lineage

Data lineage traces the origin and transformation path of key data objects across integrated systems.

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|

> *Lineage detail will be refined when tower architects validate source/target schema object mappings.*

### 4.4 RICEFW Data Objects

Data-centric RICEFW objects (Reports and Conversions) from the Object Tracker:

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| LOGR1176_IF | Report | ISM - International Traffic Report | 10. Object Complete |  |  | 03.Medium |
| LOGR0833_IF | Report | Email Notification for deletion of Shipping Memos | 10. Object Complete |  |  | 04.Low |
| LOGC0972_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  |  | 02.High |
| LOGC0946_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  |  | 02.High |
| FTSC1550 | Conversion | Inventory Conversion | 02. FS Unplanned |  |  | 03.Medium |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for L-120.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for L-120.

#### Future-State Flow Narrative

*(No future-state flows defined.)*

### 5.3 Change Impact Summary

| Change Type | Flow Chain | Detail |
|-------------|-----------|--------|

**Totals**: 0 new - 0 removed - 0 modified - 0 unchanged

### 5.4 Component Overview

#### System Inventory

| System | IAPM ID | Status |
|--------|---------|--------|

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| LOGW1078_IF | Workflow | ISM Workflows - Capital/AMT | 10. Object Complete |  | NA | 03.Medium |
| LOGW1077_IF | Workflow | ISM Workflows - EIMS/Lab | 10. Object Complete |  | NA | 03.Medium |
| LOGW1076_IF | Workflow | ISM Workflows - Non-inventory | 10. Object Complete |  | NA | 03.Medium |
| LOGR1176_IF | Report | ISM - International Traffic Report | 10. Object Complete |  | NA | 03.Medium |
| LOGR0833_IF | Report | Email Notification for deletion of Shipping Memos | 10. Object Complete |  | NA | 04.Low |
| LOGI1718 | Interface | To align on batch attributes for straddle in S4 | 08. FUT In Progress |  | NA | 03.Medium |
| LOGI1677 | Interface | Send 4C1 Inventory Reconciliation Snapshot to IP | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1676 | Interface | Send 4C1 Inventory movement Stock type change and cycle count to IP | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1555 | Interface | Straddle Plant to be automatically complete the Goods Receipt and write of th... | 09. FUT Overdue |  | MuleSoft | 03.Medium |
| LOGI1091 | Interface | STO based Outbound Delivery Notification Confirmation for Delivery Note Deletion | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI1081_IF | Interface | Interface + Enhancement - Reprinting of Carrier Label | 10. Object Complete | S/4 → Redwood | APIGEE | 04.Low |
| LOGI1079_IF | Interface | Interface from S4 ISM to Service Now | 10. Object Complete | S/4 ISM → Service Now | NA | 04.Low |
| LOGI1074_IF | Interface | Send data via API to retrieve the tracking ID - interface + Enhancement | 10. Object Complete | S/4 → Redwood | APIGEE | 04.Low |
| LOGI1062 | Interface | STO based outbound delivery notification request for delivery note cancellation | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI1053 | Interface | STO based Outbound Delivery Notification from 3PL to S/4 for confirming Pick/... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI1043 | Interface | Inventory Movement from 3PL to S/4 - 4C1 Cycle Count | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI1041 | Interface | STO based Outbound Delivery PGI confirmation from 3PL to S/4 - 3B2 | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI1040 | Interface | STO based Outbound Delivery PGI confirmation for returns from S/4 to 3PL - 3B2 | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI1038 | Interface | STO based Outbound Delivery Notification from S/4 to 3PL - 3B12 | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI1037 | Interface | Inventory Movement from S/4 to 3PL – 4C1 (Outbound) | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0836_IF | Interface | Interface from S4 to NDA (IPLA –Intel Pre Release License Agreements) | 10. Object Complete | S/4 → NDA | NA | 04.Low |
| LOGI0237_IF | Interface | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 | 10. Object Complete | 3PL → S/4 | MULESOFT | 03.Medium |
| LOGF1525 | Form | Consolidated Commercial Invoice for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1524 | Form | Commercial Invoice for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1523 | Form | Packing list for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1100_IF | Form | Printing of Standard Shipping Label | 10. Object Complete |  | NA | 03.Medium |
| LOGF0359_IF | Form | ISM - Generate Commercial Invoice - IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0358_IF | Form | ISM - Generate Traveler Document - IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0352_IF | Form | ISM - IPLA | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0351_IF | Form | ISM - Custom China Special label | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0350_IF | Form | ISM - India GST DC | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE1690 | Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF a... | 07. FUT Roadblock |  | NA | 03.Medium |
| LOGE1572_IF | Enhancement | SAP GUI T-code to Move stock from Blocked to unblock Status | 10. Object Complete |  | NA | 03.Medium |
| LOGE1569_IF | Enhancement | Enhancement to change billing status based on ship reason in ISM | 10. Object Complete |  | NA | 04.Low |
| LOGE1554 | Enhancement | Straddle Plant to be automatically complete the Goods Receipt and write of th... | 09. FUT Overdue |  | NA | 03.Medium |
| LOGE1453 | Enhancement | Trigger the request for cancellation 3B14R and cancel the demand on STO based... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1450 | Enhancement | Inbound idoc processing logic during 3B2 and 3B13 | 10. Object Complete |  | NA | 03.Medium |
| LOGE1415 | Enhancement | Suppress Batch and serial number validation in MIGO/MB26 for movement type 261 | 08. FUT In Progress |  | NA | 03.Medium |
| LOGE1414 | Enhancement | Creation of outbound Delivery for WIP inventory from STO | 10. Object Complete |  | NA | 03.Medium |
| LOGE1177_IF | Enhancement | India GST E-invoicing | 10. Object Complete |  | NA | 04.Low |
| LOGE1118_IF | Enhancement | ISM – MY Security Check Fiori app - IF | 10. Object Complete |  | NA | 03.Medium |
| LOGE1117_IF | Enhancement | ISM – Employee acknowledgement - IF | 10. Object Complete |  | NA | 03.Medium |
| LOGE1090_IF | Enhancement | PGI confirmation for non-inventory Intel freight shipments via email | 10. Object Complete |  | NA | 04.Low |
| LOGE1080_IF | Enhancement | Email notifications to be triggered as part of ISM Workflows | 10. Object Complete |  | NA | 03.Medium |
| LOGE1054 | Enhancement | Email/Text Trigger to Factory Technician and Post Goods Issue upon all WO con... | 10. Object Complete |  | NA | 02.High |
| LOGE1052_IF | Enhancement | Custom fields required on delivery screen | 10. Object Complete |  | NA | 04.Low |
| LOGE0935_IF | Enhancement | Fiori App - Shipping Memo | 08. FUT In Progress |  | NA | 02.High |
| LOGE0835_IP | Enhancement | Interface to get the AMT (Asset Management Tool) data on the ISM | 10. Object Complete |  | NA | 03.Medium |
| LOGE0239_IF | Enhancement | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 - Table Creation | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0190_IF | Enhancement | Delivery Split for STO in S/4 | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGC0972_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  | NA | 02.High |
| LOGC0946_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  | NA | 02.High |
| FTSC1550 | Conversion | Inventory Conversion | 02. FS Unplanned |  | NA | 03.Medium |
| LOGI1738 | Interface | Interface to send data to Factory Comm to activate the Mobile text receiving ... | 02. FS Unplanned |  | NA | 02.High |

**Summary**: 2 Reports, 18 Interfaces, 3 Conversions, 19 Enhancements, 9 Forms, 3 Workflows

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for L-120:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for L-120:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (54 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 46 | 85.2% |
| 08. FUT In Progress | 3 | 5.6% |
| 09. FUT Overdue | 2 | 3.7% |
| 02. FS Unplanned | 2 | 3.7% |
| 07. FUT Roadblock | 1 | 1.9% |
| **Total** | **54** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 2 |
| Interface (I) | 18 |
| Conversion (C) | 3 |
| Enhancement (E) | 19 |
| Form (F) | 9 |
| Workflow (W) | 3 |
| **Total** | **54** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 02.High | 5 |
| 03.Medium | 35 |
| 04.Low | 14 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| LOGI1718 | 02.Interface | To align on batch attributes for straddle in S4 | 08. FUT In Progress | 03.Medium |
| LOGI1555 | 02.Interface | Straddle Plant to be automatically complete the Goods Receipt and write of the i... | 09. FUT Overdue | 03.Medium |
| LOGE1690 | 04.Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF and ... | 07. FUT Roadblock | 03.Medium |
| LOGE1554 | 04.Enhancement | Straddle Plant to be automatically complete the Goods Receipt and write of the i... | 09. FUT Overdue | 03.Medium |
| LOGE1415 | 04.Enhancement | Suppress Batch and serial number validation in MIGO/MB26 for movement type 261 | 08. FUT In Progress | 03.Medium |
| LOGE0935_IF | 04.Enhancement | Fiori App - Shipping Memo | 08. FUT In Progress | 02.High |
| FTSC1550 | 03.Conversion | Inventory Conversion | 02. FS Unplanned | 03.Medium |
| LOGI1738 | 02.Interface | Interface to send data to Factory Comm to activate the Mobile text receiving cap... | 02. FS Unplanned | 02.High |

**Tower Context:** FTS-IF has 265 total RICEFW objects (209 complete, 56 active/other)

### 6.3 NFRs & Design Principles

| Category | Requirement | Target / SLA | Priority |
|----------|-------------|-------------|----------|
| Performance | MRP/production planning run completes within defined window | < 4 hours full MRP run | High |
| Availability | Manufacturing execution systems available 24/7 | 99.95% (24x7 operations) | High |
| Scalability | Support production volume increases from new product lines | Handle 10K+ production orders/day | High |
| Recoverability | Production systems recover within shift change window | RPO < 15 min, RTO < 2 hours | High |
| Data Volume | Support high-frequency material movement transactions | 100K+ material documents/day | Medium |
| Latency | Real-time inventory visibility for warehouse operations | < 2 seconds for RF/scanner transactions | High |
| Concurrency | Support factory floor workers across multiple shifts/sites | 500+ concurrent warehouse users | Medium |

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

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-120 — Manage Line Replenishment - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*52 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| LOGW1078_IF | ISM Workflows - Capital/AMT | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGW1077_IF | ISM Workflows - EIMS/Lab | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| LOGW1076_IF | ISM Workflows - Non-inventory | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGR1176_IF | ISM - International Traffic Report | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGR0833_IF | Email Notification for deletion of Shipping Memos | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGI1718 | To align on batch attributes for straddle in S4 | Feb-26 (100%) | Mar-26 (100%) | Mar-26 (100%) | Mar-26 (5%) | 3. Off Track |
| LOGI1677 | Send 4C1 Inventory Reconciliation Snapshot to IP | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1676 | Send 4C1 Inventory movement Stock type change and cycle count to IP | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1555 | Straddle Plant to be automatically complete the Goods Receipt and write of the inventory | Sep-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (45%) | 3. Off Track |
| LOGI1091 | STO based Outbound Delivery Notification Confirmation for Delivery Note Deletion | Mar-25 (100%) | Jul-25 (100%) | Jul-25 (100%) | Sep-25 (100%) |  |
| LOGI1081_IF | Interface + Enhancement - Reprinting of Carrier Label | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) |  |
| LOGI1079_IF | Interface from S4 ISM to Service Now | May-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) |  |
| LOGI1074_IF | Send data via API to retrieve the tracking ID - interface + Enhancement | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) | 3. Off Track |
| LOGI1062 | STO based outbound delivery notification request for delivery note cancellation | Mar-25 (100%) | Jul-25 (100%) | Jul-25 (100%) | Sep-25 (100%) |  |
| LOGI1053 | STO based Outbound Delivery Notification from 3PL to S/4 for confirming Pick/Pack - 3B13 | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Aug-25 (100%) | 3. Off Track |
| LOGI1043 | Inventory Movement from 3PL to S/4 - 4C1 Cycle Count | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) | 1. On Track |
| LOGI1041 | STO based Outbound Delivery PGI confirmation from 3PL to S/4 - 3B2 | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) |  |
| LOGI1040 | STO based Outbound Delivery PGI confirmation for returns from S/4 to 3PL - 3B2 | Apr-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| LOGI1038 | STO based Outbound Delivery Notification from S/4 to 3PL - 3B12 | Mar-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Jul-25 (100%) | 2. At Risk |
| LOGI1037 | Inventory Movement from S/4 to 3PL – 4C1 (Outbound) | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Aug-25 (100%) |  |
| LOGI0836_IF | Interface from S4 to NDA (IPLA –Intel Pre Release License Agreements) | Apr-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Jan-26 (100%) | 4. Completed |
| LOGI0237_IF | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 | Jun-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Sep-25 (100%) |  |
| LOGF1525 | Consolidated Commercial Invoice for WIP | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 3. Off Track |
| LOGF1524 | Commercial Invoice for WIP | Aug-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | Feb-26 (100%) | 1. On Track |
| LOGF1523 | Packing list for WIP | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 3. Off Track |
| LOGF1100_IF | Printing of Standard Shipping Label | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) |  |
| LOGF0359_IF | ISM - Generate Commercial Invoice - IF/IP | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |
| LOGF0358_IF | ISM - Generate Traveler Document - IF/IP | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) | 1. On Track |
| LOGF0352_IF | ISM - IPLA | Sep-24 (100%) | May-25 (100%) | May-25 (100%) | Jul-25 (100%) |  |
| LOGF0351_IF | ISM - Custom China Special label | Sep-24 (100%) | May-25 (100%) | May-25 (100%) | Jul-25 (100%) |  |

*... and 22 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**Mapped sub-tower(s):** 7.6 FTS IF - Logistics & Inventory Management

**RAID Summary:** 102 open items (12 capability-specific, 90 tower-level), 439 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 6 | 6 |
| P2 - Medium | 12 | 69 | 81 |
| P3 - Low | 0 | 15 | 15 |
| **Total** | **12** | **90** | **102** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03294 |  | P2 - Medium | Factory portal application is not ready from FTS and this is... | In Progress | FTS IF | 2026-02-27 |
| 02987 |  | P2 - Medium | LOGF1525 - Consolidated Commercial Invoice for WIP Awaiting ... | In Progress | FTS IF | 2025-11-06 |
| 03716 | Risk | P2 - Medium | Raising RAID to track the progress of FUT for LOGE1690 as it... | In Progress | FTS IF | 2026-03-13 |
| 03518 | Action | P2 - Medium | Batch Attributes for WIP Straddle-LOGI1718 | Not Started |  | 2026-02-06 |
| 02419 | Key Decision | P2 - Medium | Batch classification details clarification required LOGC0972... | Not Started | FTS IF | 2025-10-15 |
| 03231 | Risk | P2 - Medium | Need LE Sample Data (Shipping Point & Delivery Route) for va... | Not Started | FTS IF | 2026-02-10 |
| 03704 | Risk | P2 - Medium | ASN Data from CIBR via e2Open needs to incorporate new attri... | In Progress | Data Foundation Program ( | 2026-03-10 |
| 02133 | Action | P2 - Medium | clarification on storage location xref for one to many scena... | Not Started | FTS IF |  |
| 02315 | Action | P2 - Medium | Need Approval on Preload file | Not Started | FTS IF |  |
| 03685 |  | P2 - Medium | Rinchem ITC1 Test Scenario/Case Readiness | In Progress | FTS IF |  |
| 03515 | Risk | P2 - Medium | Need E2E test data for STO of IM to IM (Interfactory shipmen... | In Progress | FTS IF | 2026-03-06 |
| 03779 | Risk | P2 - Medium | Chem 3PL PIP Enhancement to support FTZ | In Progress | FTS IF | 2026-04-17 |

**Other FTS-IF Tower RAID Items** (90 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03578 | Risk | P1 - High | HBI Process Flow Change impact Assessment | In Progress | FTS IF | 2026-03-27 |
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03600 | Risk | P1 - High | Error lifecycle functionality within PDF application is miss... | In Progress | FTS IF | 2026-05-01 |
| 03601 | Risk | P1 - High | Traceability functionality within PDF application is missing... | In Progress | FTS IF | 2026-05-15 |
| 03757 | Risk | P1 - High | IF Planning data not available in ITC1 until W4, leaving too... | In Progress | FTS IF | 2026-04-03 |
| 03762 | Risk | P1 - High | FTS-IF (esp SCP) related test cases/sequencing are not accur... | In Progress | FTS IF | 2026-04-03 |
| 01355 | Action | P2 - Medium | PDF SMHe product development approach does not appear to hav... | To Be Reviewed | FTS IF | 2026-04-03 |
| 01658 | Risk | P2 - Medium | Under Intel Review | In Progress |  | 2025-07-18 |
| 01709 | Action | P2 - Medium | No PAY1 or ENG1 storage locations defined or configured for ... | Not Started |  | 2025-08-08 |
| 01733 | Risk | P2 - Medium | Tariffs impacts Item/BOM design which is impacting ERP/SCP (... | In Progress | E2E | 2026-03-06 |
| 01769 | Action | P2 - Medium | Approach and duration for PDF SMH application refreshes to s... | In Progress | FTS IF | 2026-04-01 |
| 01857 | Action | P2 - Medium | TF Signavio Flows Update Request | In Progress | FTS IF | 2026-01-30 |
| 03079 | Action | P2 - Medium | Request for PDH Design WTF | In Progress | FTS IP | 2026-03-04 |
| 03128 | Risk | P2 - Medium | Application Health Monitoring | In Progress | FTS IF | 2026-05-13 |
| 03157 |  | P2 - Medium | Split Logic to Segregate IF & IP data from EWM tables | Not Started |  | 2025-12-04 |
| 03205 | Action | P2 - Medium | Provide an update WW50 on the production rollout plan for th... | In Progress | FTS IF | 2026-03-06 |
| 03241 | Risk | P2 - Medium | Materials Planning Policy for Constrained Materials | In Progress | FTS IP | 2026-07-31 |
| 03292 | Risk | P2 - Medium | SCP IF BY ESP Solves during ITC1 | In Progress | FTS IF | 2026-01-09 |
| 03308 | Action | P2 - Medium | Missing information for Anafi material master | Not Started | FTS IF |  |
| 03314 | Risk | P2 - Medium | Executive lock cause performance issues in IF Dev | In Progress | FTS IF | 2026-04-17 |
| 03331 | Risk | P2 - Medium | Clarity on finalized SAP S/4 Plant and storage location mapp... | In Progress | Master Data | 2026-02-20 |
| 03334 | Issue | P2 - Medium | Application Monitoring - Connectors Health Monitoring | In Progress | FTS IF | 2026-05-15 |
| 03368 | Issue | P2 - Medium | Infrastructure resources support PDF SMH ability to provide ... | In Progress | FTS IF | 2026-03-27 |
| 03398 | Action | P2 - Medium | Kafka Admin Password for both IF and IP | In Progress | FTS IF | 2026-04-03 |
| 03703 | Risk | P2 - Medium | For FUT: Factory Automation Apps waiting on Heartbeat Loader... | In Progress | FTS IF | 2026-03-24 |
| 03713 | Risk | P2 - Medium | Lack of TRDI data impacting delivery of ECA report by ITC2 | In Progress | FTS IF | 2026-03-27 |
| 03718 | Risk | P2 - Medium | Storage Location Logic for Non-MMID Parts. | In Progress | PTP | 2026-03-27 |
| 03732 | Risk | P2 - Medium | Production scheduling systems will likely only provide mock ... | Not Started |  | 2026-03-27 |
| 03526 | Action | P2 - Medium | Review process for post-validation of system changes | In Progress | FTS IP | 2026-04-03 |
| 02088 | Risk | P2 - Medium | Equipment Master Conversion help needed | In Progress | FTS IF | 2026-03-31 |
| | | | *... and 60 more tower-level items* | | | |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*L-120 — Architecture Document (TOGAF BDAT) · Forecast to Stock (IF) · Generated: March 2026*

