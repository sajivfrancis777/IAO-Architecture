<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">LO-180 — Manage Outbound Transportation - FTS (IP)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Forecast to Stock (IP) (FTS-IP) Tower<br/>
  Capability LO-180 · L Logistics and Inventory Management - FTS (IP)</p>
  <p style="font-size:14px; color:#888;">IAO Program · Release 3<br/>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **LO-180 Manage Outbound Transportation - FTS (IP)** within the IAO program. It includes 6 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Forecast to Stock (IP) (FTS-IP) |
| **Process Group** | L Logistics and Inventory Management - FTS (IP) |
| **Capability** | LO-180 - Manage Outbound Transportation - FTS (IP) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 2 Reports, 20 Interfaces, 3 Conversions, 17 Enhancements, 6 Forms, 3 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Forecast to Stock (IP) |
| **L1 Process** | L Logistics and Inventory Management - FTS (IP) |
| **L2 Capability** | LO-180 - Manage Outbound Transportation - FTS (IP) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Intel Products Supply Chain Unification | Consolidate Intel Products manufacturing and logistics onto S/4 HANA platform | IDM 2.0 Products Transformation | High |
| 2 | End-to-End Traceability | Enable lot/batch traceability from raw material to finished goods shipment | Quality & Compliance | High |
| 3 | Demand-Supply Matching | Implement responsive demand and supply matching (RDSM) for IP product lines | Supply Chain Agility | Medium |
| 4 | LO-180 Process Migration | Migrate Manage Outbound Transportation - FTS (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Supply Chain (Intel Products) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Production Schedule Adherence | > 95% | Percentage of production orders completed on schedule | 88% (current) | Production Manager |
| Material Availability Rate | > 98% | Materials available at point of need for production | 94% (current) | Materials Planning |
| Shipping On-Time Delivery | > 97% | Orders shipped within committed delivery window | 93% (current) | Logistics Lead |
| LO-180 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **6 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for LO-180 Manage Outbound Transportation - FTS (IP).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | LO-180-010_Process_Delivery_of_Line_Items_-_FTS_(IP) | LO-180-010_Process_Delivery_of_Line_Items_-_FTS_(IP) | Warehouse Operator | 8 | 2 |
| 2 | LO-180-050_Prepare_Delivery_Schedule_for_Non-orders_-_FTS_(IP) | LO-180-050_Prepare_Delivery_Schedule_for_Non-orders_-_FTS_(IP) | Inventory Manager, Trade Execution Analyst | 19 | 4 |
| 3 | LO-180-070_Plan_Transportation_-_FTS_(IP) | LO-180-070_Plan_Transportation_-_FTS_(IP) | Customer Business Analyst | 4 | 2 |
| 4 | LO-180-130_Coordinate_Transportation_-_FTS_(IP) | LO-180-130_Coordinate_Transportation_-_FTS_(IP) | Functional Analyst, Load Planner | 19 | 7 |
| 5 | LO-180-140_Record_Transportation_Information_-_FTS_(IP) | LO-180-140_Record_Transportation_Information_-_FTS_(IP) | Load Planner | 3 | 0 |
| 6 | LO-180-150_Generate_Shipping_Documentation_-_FTS_(IP) | LO-180-150_Generate_Shipping_Documentation_-_FTS_(IP) | Load Planner | 3 | 2 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 LO-180-010_Process_Delivery_of_Line_Items_-_FTS_(IP) — LO-180-010_Process_Delivery_of_Line_Items_-_FTS_(IP)

**Swim Lanes**: Warehouse Operator | **Tasks**: 8 | **Gateways**: 2

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
    subgraph Warehouse Operator
        n1[["fa:fa-cog Transfer Delivery to TM (Control Key)"]]
        n2[["fa:fa-cog Fetch Organization Structure Details"]]
        n3[["fa:fa-cog Determine Freight Unit Building Rule"]]
        n4[["fa:fa-cog Determine FU Type for ISM (IMF/VMF)"]]
        n5[["fa:fa-cog Check for Back Dated Orders and Update Freight Unit"]]
        n6[["fa:fa-cog Check Delivery Block and Shipment Planning Block Reasons"]]
        n7[["fa:fa-cog Update Freight Unit Based on Controller Strategy"]]
        n8[["fa:fa-cog Check for DG material and Update DG Indicator in Freight Unit"]]
        n9["Plan Transportation - FTS (IP)"]
        n10["Create Delivery Note"]
        n11{{"fa:fa-arrows-alt parallelGateway"}}
        n12{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n2
    n2 --> n3
    n11 --> n6
    n11 --> n7
    n11 --> n5
    n5 --> n12
    n6 --> n12
    n7 --> n12
    n10 --> n1
    n3 --> n4
    n4 --> n11
    n11 --> n8
    n8 --> n12
    n12 -->|"Freight Unit
Created"| n9
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 startEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVluP4jYU_itWRiNaKai5EiYPlSCQ1aid7mhhdh-WfTCJA9YYO7LNMCzLf-8xSbikm0pV84ByvnPOd272IQcrEzmxYuv-_kA51TE69PSabEgvRr0lVqRnowr4jCXFS0ZUz9gUgusZ_X4yc4Py3ZgZLMUbyvYGnZGVIOjl0UYjcGQ2UpirviKSFj27V0q6wXKfCCaksb4jw8IpTtFq1VjInMiLgeNEbhaCK6OcXGA_CqIgNX6KZILnN6RFWAyLrHc0yTGxy9ZY6lP6W0We8PsXmus1yAVmioDNWm_Yn3hJmKlRy63Bsq18a5pBlYnDoWGzEmeUrwAPHIAk5q8XKHSOR3S8v1_wc1A0nyw4gidjWKkJKZDSAE_fNCooY_FdkIzS0LGVluKVxHfeNJr4np2ZSmIo3bFNc_s7QldrHS8Fy2vT_s7UEHvluy3fY8-x5R5-W7EIzy-RkoE39IbnSOPITdykiVQUxf-KBH2Vc6xe61hTP_XSyTmWGw7CxPknX1PmJIhGbrtPRL7RjFyRpmnqTy-tmg5C1-kmHaf-wElapCusyQ7vL4QPSXAmTMModaNOwipeO8vt8lmKrCH0p2EangmjsZuOvE7CYOQGwzpD4FlJXK7RFyzJWkA70ceSSKyFrAzMw92vXxdWgeMC9zOxQnM4fqogEk0Io29E7pEWaP6EfklgklIw9AfZ_7qwvn27ovBuKVKiszX6KFeY0-9YU8HRDC5ApreSAK3GlKkWg3_LAEZEbuBqolSezg56gXWCxlvKcrgW6NOWkRZD0Mnwgub7kqBCSPQ4g0Ien9LfPj-l7SLCW4JkTbLXk9MYw8sEhpxDTbBFFMI8Ry9lDtBNfi3Cwc8Iz10dMwGiYZqtabkhXKNnhjk35VW6TwQrwdudim5Zf5IGJKwgV-h6PTIG04QBgN1q32IbdhU9-YA24GCW7XW5AD_ynGbmDCHK_638B2A2FVUnqhRSV0ehj9L5DKbwbAZwfQ4dcEgkOYVpuvSX0KRl5h4OTcpYSrFTfcw0KrHEUCj7UF3GhXU8Xjt5_80Jdlz1wl3U7_8OJ7wWvUr0G22tHrTkqCWHtRxWotvQDVpy1JJdpwZq2a_EoBaDWuu2wg1redimO6X_Y2HdjI1XTc8X1g-Y2tUuMtVfbcwbjdep8Ts1Qacm7NQMOjVRp2bYqXk4_1Pelul04G6z3G9hr4Et29rAmsE0t-KDdfqyga-fnBR4y7R1tC281WK255kVn74ArO3pGk0ohsW8qcDj31Ln6UA=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 LO-180-050_Prepare_Delivery_Schedule_for_Non-orders_-_FTS_(IP) — LO-180-050_Prepare_Delivery_Schedule_for_Non-orders_-_FTS_(IP)

**Swim Lanes**: Inventory Manager · Trade Execution Analyst | **Tasks**: 19 | **Gateways**: 4

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
    subgraph Inventory Manager
        n5["fa:fa-user Request to Move Non-Inventorised Material"]
        n6["fa:fa-user Submit Shipping Memo (Searching Shipping Memo)"]
        n7["fa:fa-user Print Commercial Invoice Packing List (CIPL) and Intel Pre-release Loan..."]
        n8["fa:fa-user Update Docking Process"]
        n9["fa:fa-user Print Box Label and Carrier Label"]
        n10["fa:fa-user Perform Manager Approval"]
        n11["fa:fa-user Perform EIMS/Capital approval wherever applicable"]
        n12["fa:fa-user Perform Packing Process"]
        n13["fa:fa-user Manual Update Carrier and WayBill"]
        n14["fa:fa-user Manual Update Waybill for Forwarder"]
        n16[["fa:fa-cog Create Shipping Memo in Fiori App"]]
        n17[["fa:fa-cog Create Delivery (Security Check and Recipient Acknowledgement)"]]
        n18[["fa:fa-cog Perform Post Goods Issue"]]
        n19[["fa:fa-cog Trigger Email to the Originator and Recipient of Shipping Memo"]]
        n20(["fa:fa-play Business Scenario Identified"])
        n23(["fa:fa-stop Shipping Memo Updated with PGI Complete Status (Document archiving)"])
        n24{{"fa:fa-code-branch Delivery Blocked ?"}}
        n25{{"fa:fa-code-branch Manual Transport Coordination?"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch Delivery Check?"}}
        n28[["fa:fa-folder-open Coordinate Transportation - FTS (IP)"]]
        n29[["fa:fa-folder-open Create Billing Document"]]
    end
    subgraph Trade Execution Analyst
        n1["fa:fa-user Perform GTS Check on Delivery"]
        n2["fa:fa-user Add Delivery in GTS Monitor"]
        n3["fa:fa-user Perform GTS Check on Delivery"]
        n4["fa:fa-user Add Delivery in GTS Monitor"]
        n15[["fa:fa-cog Perform GTS Approval"]]
        n21(["fa:fa-stop Delivery Queue Monitored"])
        n22(["fa:fa-stop Delivery Queue Monitored"])
    end
    n20 --> n5
    n5 --> n16
    n6 --> n17
    n24 -->|"No"| n18
    n25 -->|"No"| n28
    n2 --> n21
    n1 --> n24
    n7 --> n1
    n24 -->|"Yes"| n2
    n17 --> n10
    n16 --> n6
    n15 --> n12
    n12 --> n25
    n25 -->|"Yes"| n8
    n26 --> n9
    n27 -->|"Yes"| n7
    n28 --> n14
    n14 --> n26
    n8 --> n13
    n13 --> n26
    n9 --> n3
    n3 --> n27
    n4 --> n22
    n18 --> n19
    n19 --> n29
    n29 --> n23
    n10 --> n11
    n11 --> n15
    n27 -->|"No"| n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 userTask
    class n10 userTask
    class n11 userTask
    class n12 userTask
    class n13 userTask
    class n14 userTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 startEvt
    class n21 endEvt
    class n22 endEvt
    class n23 endEvt
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 subProc
    class n29 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWNtu4zYQ_RVCi8AJYG8tWbJsP7TwTYGBZJuus10Umz7Q0sgmIosqRfnSrP-9Q1uULUVu0dYPAXjIc-bCGZLKm-HzAIyBcXPzxmImB-StIVewhsaANBY0hUaTnIBfqWB0EUHaUGtCHss5-_O4zLSTnVqmMI-uWbRX6ByWHMiXWZMMkRg1SUrjtJWCYGGj2UgEW1OxH_OIC7X6A_TCdni0lk-NuAhAnBe0267pO0iNWAxnuOParu0pXgo-j4OSaOiEvdBvHJRzEd_6Kyrk0f0shUe6-8oCucJxSKMUcM1KrqMHuoBIxShFpjA_ExudDJYqOzEmbJ5Qn8VLxO02QoLGr2fIaR8O5HBz8xIXRsnz5CUm-PMjmqYTCEkqEZ5uJAlZFA0-2OOh57SbqRT8FQYfrKk76VhNX0UywNDbTZXc1hbYciUHCx4F-dLWVsUwsJJdU-wGVrsp9vi3Ygvi4Gxp3LV6Vq-wNHLNsTnWlsIw_F-WMK_imaavua1px7O8SWHLdLrOuP1eT4c5sd2hWc0TiA3z4ULU87zO9Jyqadcx29dFR16n2x5XRJdUwpbuz4L9sV0Ieo7rme5VwZO9qpfZ4klwXwt2po7nFILuyPSG1lVBe2javdxD1FkKmqzILN5ALLnYk0ca0yWI07z6xc63FyOkg5C2VLrJZ_gjg1QSyckj3wD5xOOWprMUAlSQoFrwxfj9QqVbVplnizWTZL5iSYJlTB5hzcntHKjwV2pcmrgrS7llqSfBYknGfL0G4aNdFQzHPSRP1H9VEg8M3b0dz54e7giNA5yXECENWgIiwEOHPHAaf_z4sWymVzbzJQkwMDLhJ1GVf0jTMqVf59mI78ixzY_Gx1QIhnNHpMw22xU6iJCLtd4SMkwSwTfVxJpmPWs6e5z_MKYJk5gSmlPJdgUCNrgMkYj56oStyFn1cjqZtXGbnTIJPc7QWJ4yHbIK_yvdj7BoK3T77-hIWSCFoBvE42JL1UFdEeh-KxR8viRjAYpZri4WE49hjao8Ir3Ed2v5E4gY5mqvChMPZib3ZLwC__UYyWfwWcKw7MnQf435NoJgifdWLO-q4r2yeJFRjmV5z3mQklmaZlCl9cu0Z8GWqgqma8oi1X14TZKfEWQxxdar-MTDcvQVcat9W4gnER5NoyzFey5NydyHGK9eTmYB6rCQQYDcu0tu58xNJU8qaT7tWkC2TK7I0_1MdWYSgdoOSWWWkltsoUwlihybfYPMu6oJ--3tHHsArQVeef7qvCGjCNsQjfz0YhwOl0SnnphX1DOO0oQLdVzgfa8yx3j8TqRbLwI7P8I0beD-dJ5Xae4_OH2snXfGLqojxOsPRIsnEJ8dhLPXR29Ji3jPc3I7e6oWmtW_InWqZtV3apd0-s9svLAr9wGaDIBMd1j2R5vDmEb7VF6WZ_0xcY-unXoEWTrycrNWDphhEJxThD2qFB45vg15pck7_9mi_R8tmk595yrCxWFcCs6sNEdh6JcMMtB23jeV9a95xa5hN5NW60e8qfOxcxqa3XzczceuXm8r4PuL8QnPhe_qhNITTnnCKiZOClb-XIrNfGznYze3UDXwG6QnIc3TC9sayH3Trpra94KhTTtVH7V24WMu1ddjt7KwCL-X29Dem3ZuQ3uhF3T0gk5lQf801vN6WlvQekUQWlD7ZuYCVuGsBgqT-Z6aRcrznJtONb58s-yLR6LaIf04LsFWPdyph-162KmHu_WwWw_36uF-PYzpqMevxGleCdS8Eql5JVSsx4tPgvJU9_qUe32qd32qf3UKO1x_wZVxM__aKqNWLdqpRW39eVKGnXq4Ww-79XBPf6mU4b6GjaaBj3Z80ATG4M04fvfj_wYCCGkWSePQNGgm-Xwf-8bg-H1sZMfHxYRRvKbWJ_DwFwWwHG8=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 LO-180-070_Plan_Transportation_-_FTS_(IP) — LO-180-070_Plan_Transportation_-_FTS_(IP)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 4 | **Gateways**: 2

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Create Site Specific Selection Profile"]
        n2["fa:fa-user Maintain Geo Attributes"]
        n3["fa:fa-user Maintain Time Related Attributes"]
        n4["fa:fa-user Maintain Additional Attributes"]
        n5(["fa:fa-play Selection Profile Creation Initiated"])
        n6["Coordinate Transportation - FTS (IP)"]
        n7{{"fa:fa-arrows-alt parallelGateway"}}
        n8{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n5 --> n1
    n1 --> n7
    n7 --> n3
    n7 --> n2
    n7 --> n4
    n2 --> n8
    n4 --> n8
    n3 --> n8
    n8 --> n6
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVduO2jAQ_RUrqxWtFKRcSZqHShBItVIrrQptH0ofTDIGa40d2c6yFPHvtQm3bJeHqpGIMoc558xMbGfnlKICJ3Pu73eUU52hXU-vYA29DPUWWEHPRS3wHUuKFwxUz-YQwfWU_j6k-VH9YtMsVuA1ZVuLTmEpAH17cNHQEJmLFOaqr0BS0nN7taRrLLe5YELa7DtIiUcObse_RkJWIC8Jnpf4ZWyojHK4wGESJVFheQpKwauOKIlJSsre3hbHxKZcYakP5TcKvuCXH7TSKxMTzBSYnJVes894Acz2qGVjsbKRz6dhUGV9uBnYtMYl5UuDR56BJOZPFyj29nu0v7-f87Mpmo3nHJmrZFipMRCktIEnzxoRylh2F-XDIvZcpaV4guwumCTjMHBL20lmWvdcO9z-BuhypbOFYNUxtb-xPWRB_eLKlyzwXLk191dewKuLUz4I0iA9O40SP_fzkxMh5L-czFzlDKuno9ckLIJifPby40Gce3_rndocR8nQfz0nkM-0hCvRoijCyWVUk0Hse7dFR0U48PJXokusYYO3F8EPeXQWLOKk8JObgq3f6yqbxaMU5UkwnMRFfBZMRn4xDG4KRkM_So8VGp2lxPUK5Y3SYg0SjRpl1rtSaMgx2yrd5tmL-z_nDsEZwX07dpRLMG2hKbW3GkpKaImmwKDUVHBk6jPVwdz5dSURdCW-YMq1-aFPINBQa0kXjQbV5YQ3ODO6BvQVmCmiukmObpCHVUVtmZjdpMbvztyamZf3V2vtBCzwYE4yauswCu-vJAZGIRfmYKHcjmpm9q2qhdQtq4-K2RS9e3h83zVOdruTMZZSbFQfM41qLDFjwD61a2nu7PdXnPTfOGaHtg88Rv3-R_Nuj6HfhskxTNow7IZBN4yOYdCG6TGMumHYDdM2HFwtbOt-2tAdOHgbDt-Go7fh-HwEduDB23By2rMdND2hjuuYzbLGtHKynXP4XplvWgUEN0w7e9fBjRbTLS-d7HCuO01dGeaYYrPd1i24_wMg0D9M" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 LO-180-130_Coordinate_Transportation_-_FTS_(IP) — LO-180-130_Coordinate_Transportation_-_FTS_(IP)

**Swim Lanes**: Functional Analyst · Load Planner | **Tasks**: 19 | **Gateways**: 7

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
    subgraph Functional Analyst
        n1["fa:fa-user Create Planning Profile"]
        n2["fa:fa-user Maintain Planning Profile Parameters"]
        n3["fa:fa-user Maintain Capacity Selection Profile"]
        n4["fa:fa-user Maintain Planning Cost settings"]
        n5["fa:fa-user Update Purchase Organization"]
        n6["fa:fa-user Maintain Optimizer Settings"]
        n7["fa:fa-user Maintain Incompatibilities"]
        n8["fa:fa-user Maintain Load Planning Settings"]
        n9["fa:fa-user Maintain Carrier Selection Settings"]
        n10["fa:fa-user Update Partner Roles in Freight Order"]
        n11["fa:fa-user Update Freight Order Based on Change Controller Strategy"]
        n20["Determine Mode of Transportation/ Carrier - FTS (IP)"]
        n23["Plan Transportation - FTS (IP)"]
        n27{{"fa:fa-arrows-alt parallelGateway"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Load Planner
        n12["fa:fa-user Manage Transportation Cockpit"]
        n13["fa:fa-user Check for Back Dated order in Freight Units for Automatic Planning"]
        n14["fa:fa-user Perform Manual Planning For International and Automatic Planning for Domestic"]
        n15["fa:fa-user Determine Freight Order Type for ISM (IMF/VMF)"]
        n16[["fa:fa-cog Perform Planning"]]
        n17[["fa:fa-cog If FU Has Planning and Execution Block Because Of Delivery Block"]]
        n18[["fa:fa-cog If FU Has Planning and Execution Block Because Of Delivery Block"]]
        n19[["fa:fa-cog System Determine FG Freight Order Type For STO"]]
        n21["LE Team Need To Release The Delivery Block"]
        n22["LE Team Need To Release The Delivery Block"]
        n24{{"fa:fa-code-branch No"}}
        n25{{"fa:fa-code-branch Yes"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n27 --> n2
    n27 --> n3
    n27 --> n4
    n2 --> n28
    n3 --> n28
    n4 --> n28
    n8 --> n28
    n1 --> n27
    n12 --> n13
    n5 --> n29
    n30 --> n10
    n30 --> n11
    n10 --> n29
    n11 --> n29
    n27 --> n6
    n6 --> n28
    n23 --> n1
    n29 --> n20
    n27 --> n9
    n27 --> n7
    n9 --> n28
    n7 --> n28
    n27 --> n8
    n24 -->|"Yes"| n21
    n25 --> n22
    n18 --> n25
    n25 -->|"No"| n16
    n24 --> n14
    n17 --> n24
    n13 --> n26
    n26 -->|"STO"| n18
    n16 --> n19
    n28 --> n12
    n26 -->|"ISM"| n17
    n15 --> n30
    n30 --> n5
    n19 --> n30
    n14 --> n15
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 userTask
    class n10 userTask
    class n11 userTask
    class n12 userTask
    class n13 userTask
    class n14 userTask
    class n15 userTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 startEvt
    class n21 startEvt
    class n22 startEvt
    class n23 startEvt
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNq1WP9v2jgU_1esTBV3EmhxSEjgh5MgkF2ldqsG3em03g8mOBA1sZHjtGUd__ueQxKIm-h0mw6pUH_83ud99cPh1Qj5hhoT4-rqNWaxnKDXntzRlPYmqLcmGe310Qn4QkRM1gnNekom4kwu42-FGLb3L0pMYQFJ4-Sg0CXdcorur_toCopJH2WEZYOMijjq9Xt7EadEHHyecKGk31EvMqPCWrk142JDxVnANF0cOqCaxIye4aFru3ag9DIacrZpkEZO5EVh76icS_hzuCNCFu7nGb0lL3_FG7mDdUSSjILMTqbJDVnTRMUoRa6wMBdPVTLiTNlhkLDlnoQx2wJumwAJwh7PkGMej-h4dfXAaqNoNX9gCF5hQrJsTiOUSYAXTxJFcZJM3tn-NHDMfiYFf6STd9bCnQ-tfqgimUDoZl8ld_BM4-1OTtY82ZSig2cVw8Tav_TFy8Qy--IA75otyjZnS_7I8iyvtjRzsY_9ylIURb9kCfIqViR7LG0thoEVzGtb2Bk5vvmWrwpzbrtTrOeJiqc4pBekQRAMF-dULUYONrtJZ8FwZPoa6ZZI-kwOZ8Kxb9eEgeMG2O0kPNnTvczXd4KHFeFw4QROTejOcDC1OgntKba90kPg2Qqy36EgZ6GMOSMJmsLbIZMnAfVi-OuDEZFJRAYq38gXFOJBdwlhDDoQgSfgB30w_rnQsZo6tyRmEv7eaKE7IkhKJRVZk2DYQeAT1fjygJY0oYXP7Q7Y_-aAzzMJ5ZYSFpptp6l7v98UAecCDldG0SexJSz-RpTxpuKow-invYxTGF8CvG4z6HboXbOQp3swtI6TWMZUU_M61G442ZwDbTc57syvEHHhaJXedn1sticJxgyD5WcOoxsBXyCKow1Jg_GqUeBWioYGmkHGNwjc8HeEbSmUjUFjJ4lyUQqQ3x60zlOOzVVHpTC50S2MT8QjtIKhme25kEXZ3tdxDlCwWqLfru9-12hUA6ocaprdCu7raxUOcPPnbEASifbQ3-Bt8uE0Ax6M4_FSyfsZpfFPKA3N_6YEQ1ybEeeugkJeVPHNUWcE6qRlzefh4z6WWgNoh9zf0RDGLldVh3_m4BOUvmiDi066h3tDVkhNc8lT4A_rZtf4tSFwRwWopcrFHCZdfUIC4Lpm0DGMlEOQsE0Le2F0zlOaAaqZ0mbGuQGb7bw67GlBc728hSa6Dd5_uQ20TsKjrzVZyLe12xdBNsTdpvh1hIJ79CfJzn6rcBYvNMyLWswSKAaa0ZDkappF4GwSP1FxOO3o9N7_Sz9u0i_hu4eml_n70JZCVbLl6pNGZqmJcrNAK0pS9JFC96w4-gyTTI3t1Y6-deVS2foVZft8vNQVd7CG_g936CPXD6_TLvi3Gu5NyVG7JH0JkzwDT7rPLAwjNBj8AZ_aeqit7WpdinvleqitbW3taWtcrt1qXRLiyqBTCowrA2YpYOoArihMTQVjDaiCGJXrkeaUVUZRMVrjUsDUCHTCKoqxRujqBkqgXhdp-v5gFMX8rvqx2qnirwqCqww6DQnQVR3zXQ2BBqkaZpVq5UYNVNWqVUYlV3FCFFldpzJHuA659ANbui4MqJNuXdMyhqFesioEPNYEcOW6c3F_Vc1S3dsbsNUOD9thux122uFRO-y2w147PG6HoVHb8Y44cUeguCNS3BEq7ogVanzxFNPccru3vO6tceeWZdZPlk0cd-BWBz7swO3q4akJO-3wqB1222GvHR63wtDsJWz0jRS-m0i8MSavRvFjBfygsaERyRNpHPsGgYvD8sBCY1I81Bt5ca-dxwTuUekJPP4AX1BKWg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 LO-180-140_Record_Transportation_Information_-_FTS_(IP) — LO-180-140_Record_Transportation_Information_-_FTS_(IP)

**Swim Lanes**: Load Planner | **Tasks**: 3 | **Gateways**: 0

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
    subgraph Load Planner
        n1[["fa:fa-cog Carrier Assigned to FO"]]
        n2[["fa:fa-cog Update Custom fields on Freight Order Subcontracting Tab"]]
        n3[["fa:fa-cog Check Custom BRF+ Table(Enhancement)"]]
        n4["Ship Order (IP)"]
        n5["Determine Mode of Transportation/Carrier FTS (IP)"]
    end
    n5 --> n1
    n1 --> n3
    n3 --> n2
    n2 --> n4
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 startEvt
    class n5 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVE2P2jAQ_StWVihbNaj5JDSHShCwtNKudlXY9rDswSQ2sdaxke0sUMR_r803VJyaA2LezLw3M_Z47RSixE7mtFpryqnOwNrVFa6xmwF3ihR2PbADfiFJ0ZRh5doYIrge0T_bsCCeL22YxSCqKVtZdIRnAoPXBw_0TCLzgEJctRWWlLieO5e0RnKVCyakjb7DXeKTrdre1ReyxPIU4PtpUCQmlVGOT3CUxmkMbZ7CheDlBSlJSJcU7sYWx8SiqJDU2_IbhZ_Q8jctdWVsgpjCJqbSNXtEU8xsj1o2Fisa-XkYBlVWh5uBjeaooHxm8Ng3kET84wQl_mYDNq3WhB9FwXgw4cB8BUNKDTABSht4-KkBoYxld3Heg4nvKS3FB87uwmE6iEKvsJ1kpnXfs8NtLzCdVTqbClbuQ9sL20MWzpeeXGah78mV-b3Swrw8KeWdsBt2j0r9NMiD_KBECPkvJTNXOUbqY681jGAIB0etIOkkuf8v36HNQZz2gus5YflJC3xGCiGMhqdRDTtJ4N8m7cOo4-dXpDOk8QKtToTf8_hICJMUBulNwp3edZXN9EWK4kAYDROYHAnTfgB74U3CuBfE3X2Fhmcm0bwCjwKV4IUhzrHcuezHg7e3iUNQRlC7EDOQIykplqCnFJ1xXAItAHyeOO_vZznhZc7rvDTdg7xRWtSmYMxKBQQHUG6PHDzbtQOjZmq2SUtUaHOpwRhNr1ijq0oqXHwcSPs_4VebwvD9kFeIF-b54PrLFUNsCEYVne8V7x9ebMRZQGICBlhjWZuNB09m7YAgYGyWTc2F1EhTwb8dRgDHo0sKc-l3f3gC2u0fZnZ7M9iZ0d6Mdma4N8OdGZ8dsE05u4YXnvCmJ7rpiY_LfwEnR9jxnNp0jWjpZGtn-_qaF7rEBDVMOxvPQY0WoxUvnGz7SjnN9kwHFJnLU-_AzV8nEd4u" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.6 LO-180-150_Generate_Shipping_Documentation_-_FTS_(IP) — LO-180-150_Generate_Shipping_Documentation_-_FTS_(IP)

**Swim Lanes**: Load Planner | **Tasks**: 3 | **Gateways**: 2

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
    subgraph Load Planner
        n1[["fa:fa-cog Create Freight Order"]]
        n2[["fa:fa-cog Generate Carrier Custom Invoice Form(ZCUS)"]]
        n3[["fa:fa-cog Generate Sales Invoice Summary Form(ZSIS)"]]
        n4(["fa:fa-stop Output Message Status Updated (Success or Failure)"])
        n5["Coordinate Transportation (Planning profiles, Optimizer settings Etc.)"]
        n6{{"fa:fa-code-branch Commodity Type?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n5 --> n1
    n1 --> n6
    n2 --> n7
    n3 --> n7
    n7 --> n4
    n6 -->|"ZCUS"| n2
    n6 -->|"ZSIS"| n3
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 endEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVdtu2zgQ_RVCQeAUkBe6Wl497MKRrSJAixRQsgVa94GmKJuIRAok5dh1_e87lORr10-rB0FzZuYczpBD7SwicmrF1v39jnGmY7Qb6BWt6CBGgwVWdGCjDvgHS4YXJVUDE1MIrjP2sw1zg3pjwgyW4oqVW4NmdCkoen2y0QQSSxspzNVQUcmKgT2oJauw3CaiFNJE39Fx4RStWu96FDKn8hTgOJFLQkgtGacn2I-CKEhNnqJE8PyCtAiLcUEGe7O4UryTFZa6XX6j6Ge8-cpyvQK7wKWiELPSVfkJL2hpatSyMRhp5PrQDKaMDoeGZTUmjC8BDxyAJOZvJyh09nu0v7-f86MoepnOOYKHlFipKS2Q0gDP1hoVrCzjuyCZpKFjKy3FG43vvFk09T2bmEpiKN2xTXOH75QtVzpeiDLvQ4fvpobYqze23MSeY8stvK-0KM9PSsnIG3vjo9Jj5CZuclAqiuJ_KUFf5QtWb73WzE-9dHrUcsNRmDi_8x3KnAbRxL3uE5VrRugZaZqm_uzUqtkodJ3bpI-pP3KSK9Il1vQdb0-EfybBkTANo9SNbhJ2eterbBZfpCAHQn8WpuGRMHp004l3kzCYuMG4XyHwLCWuV-iTwDn6UmLOqexc5uHu9-9zq8BxgYdELFEiKVSCUtnuFno2EzO3fvw4y_AuMz5SIDQ5CZaSUYmSRmlRoSe-FtBmlApZPXxLXrMPVzz-DZ4Mw5VwTM-aysxuT5M9_UYTPBxpQLdGz42uG40-U6XwEvI11o1Cr3UO3Dl6yBpCwIWERClmZSOpIfxwRhgCXyLgrmDcLOcFRlHVQgIPExw9tC2EsUS1FLA5VNnoudasgqtLwtnSGnwKzTT5wxCf8Y52u1O9OR0ugJisUCKqSuRMb9HLtqZ_z639_iwp-u8kuiFlo9iafuzO3SkLJrP74CEaDv-CDe5NtzNHvel1ZtSb_qUZdWbQmyNj_ppbZhvn1i_IvnbAxrQO_-wYG82zYbvweDc9_k1P0F87F2B4vPcu4NFhIi_Q6IBatlVRWWGWW_HOav9G8MfKaYGbUlt728KNFtmWEytub22rac_PlGEYpqoD9_8CPnI2nw==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Warehouse Operator | LO-180-010_Process_Delivery_of_Line_Items_-_FTS_(IP),  | |
| Inventory Manager | LO-180-050_Prepare_Delivery_Schedule_for_Non-orders_-_FTS_(IP),  | |
| Trade Execution Analyst | LO-180-050_Prepare_Delivery_Schedule_for_Non-orders_-_FTS_(IP),  | |
| Customer Business Analyst | LO-180-070_Plan_Transportation_-_FTS_(IP),  | |
| Functional Analyst | LO-180-130_Coordinate_Transportation_-_FTS_(IP),  | |
| Load Planner | LO-180-130_Coordinate_Transportation_-_FTS_(IP), LO-180-140_Record_Transportation_Information_-_FTS_(IP), LO-180-150_Generate_Shipping_Documentation_-_FTS_(IP) | |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for LO-180. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
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
| LOGR1176_IP | Report | ISM - International Traffic Report | 10. Object Complete |  |  | 02.High |
| LOGR0833_IP | Report | Email Notification for deletion of Shipping Memos | 10. Object Complete |  |  | 03.Medium |
| LOGC1500 | Conversion | IM Stock conversion from Non SAP system to S4 system | 10. Object Complete |  |  | 02.High |
| LOGC0972_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  |  | 02.High |
| LOGC0946_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  |  | 02.High |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for LO-180.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for LO-180.

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

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| LOGW1078_IP | Workflow | ISM Workflows - Capital/AMT | 10. Object Complete |  | NA | 03.Medium |
| LOGW1077_IP | Workflow | ISM Workflows - EIMS/Lab | 10. Object Complete |  | NA | 03.Medium |
| LOGW1076_IP | Workflow | ISM Workflows - Non-inventory | 10. Object Complete |  | NA | 02.High |
| LOGR1176_IP | Report | ISM - International Traffic Report | 10. Object Complete |  | NA | 02.High |
| LOGR0833_IP | Report | Email Notification for deletion of Shipping Memos | 10. Object Complete |  | NA | 03.Medium |
| LOGI1679 | Interface | Receive 4C1 Inventory movement Stock type change and cycle count from IF | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1678 | Interface | Receive 4C1 Inventory Reconciliation Snapshot from IF | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1576 | Interface | ECD_Interface between S4 to ECD for inventory status response | 08. FUT In Progress |  | MuleSoft | 03.Medium |
| LOGI1575 | Interface | ECD_Interface between S4 to 3PL for inventory status webservice​ | 08. FUT In Progress |  | MuleSoft | 03.Medium |
| LOGI1571 | Interface | ECD_Interface from ECD to S4 for Inventory status call​ | 10. Object Complete |  | MuleSoft | 03.Medium |
| LOGI1295 | Interface | ECD_Interface between S/4 and ECD for completion status | 08. FUT In Progress |  | MULESOFT | 03.Medium |
| LOGI1291 | Interface | ECD_Interface between S/4 and 3PL to send plant/batch level hold/unhold infor... | 08. FUT In Progress |  | MULESOFT | 03.Medium |
| LOGI1290 | Interface | ECD_Interface from ECD to S4 for Inventory Hold/unhold request | 08. FUT In Progress |  | MULESOFT | 03.Medium |
| LOGI1272 | Interface | Response to goods receipt posting from SAP to 3PL - EDI 4C1B | 10. Object Complete | S/4 → WMS (3PL) | MULESOFT | 03.Medium |
| LOGI1267 | Interface | Inventory Reconciliation with Consignment hub – EDI 4C1 with version control | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI1081_IP | Interface | Interface + Enhancement - Reprinting of Carrier Label | 10. Object Complete | S/4 → Redwood | APIGEE | 03.Medium |
| LOGI1079_IP | Interface | Interface from S4 ISM to Service Now | 10. Object Complete | S/4 ISM → Service Now | NA | 03.Medium |
| LOGI1074_IP | Interface | Send data via API to retrieve the tracking ID - interface + Enhancement | 10. Object Complete | S/4 → Redwood | APIGEE | 03.Medium |
| LOGI0951 | Interface | Inbound interface to receive Finished Goods “Goods Receipt” (4B2) signal from... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0950 | Interface | Interface to receive 4B2 signal from Factory and return shipments from ODM/OS... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0933 | Interface | W-lot inventory error handling | 10. Object Complete |  | MULESOFT | 03.Medium |
| LOGI0836_IP | Interface | Interface from S4 to NDA (IPLA –Intel Pre Release License Agreements) | 10. Object Complete | S/4 → NDA | NA | 03.Medium |
| LOGI0335 | Interface | Outbound PIP signal to 3PL for material document transfer – EDI 4C1 | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| LOGI0237_IP | Interface | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 | 10. Object Complete | 3PL → S/4 | MULESOFT | 02.High |
| LOGF1100_IP | Form | Printing of Standard Shipping Label | 10. Object Complete |  | NA | 02.High |
| LOGF0359_IP | Form | ISM - Generate Commercial Invoice - IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0358_IP | Form | ISM - Generate Traveler Document - IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0352_IP | Form | ISM - IPLA | 10. Object Complete |  | NA | 02.High |
| LOGF0351_IP | Form | ISM - Custom China Special label | 10. Object Complete |  | NA | 02.High |
| LOGF0350_IP | Form | ISM - India GST DC | 10. Object Complete |  | NA | 02.High |
| LOGE1686 | Enhancement | IP custom table for reconciliation data | 10. Object Complete |  | NA | 03.Medium |
| LOGE1572_IP | Enhancement | SAP GUI T-code to Move stock from Blocked to unblock Status | 10. Object Complete |  | NA | 02.High |
| LOGE1569_IP | Enhancement | Enhancement to change billing status based on ship reason in ISM | 10. Object Complete |  | NA | 03.Medium |
| LOGE1327 | Enhancement | ECD_Enhancement to retrieve plant details for material/batch and update custo... | 08. FUT In Progress |  | NA | 02.High |
| LOGE1253 | Enhancement | Inventory Reconciliation with Consignment hub – EDI 4C1 with version control | 10. Object Complete |  | NA | 03.Medium |
| LOGE1177_IP | Enhancement | India GST E-invoicing | 10. Object Complete |  | NA | 03.Medium |
| LOGE1118_IP | Enhancement | ISM – MY Security Check Fiori app - IF | 10. Object Complete |  | NA | 02.High |
| LOGE1117_IP | Enhancement | ISM – Employee acknowledgement - IP | 10. Object Complete |  | NA | 02.High |
| LOGE1090_IP | Enhancement | PGI confirmation for non-inventory Intel freight shipments via email | 10. Object Complete |  | NA | 03.Medium |
| LOGE1080_IP | Enhancement | Email notifications to be triggered as part of ISM Workflows | 10. Object Complete |  | NA | 02.High |
| LOGE1052_IP | Enhancement | Custom fields required on delivery screen | 10. Object Complete |  | NA | 03.Medium |
| LOGE0945 | Enhancement | Update COF, COA and FVR in 3PL WMS - EDI 4C1B | 10. Object Complete |  | NA | 03.Medium |
| LOGE0936 | Enhancement | Validate receiving consigned materials into consignment hub – EDI 4B2 CSGN | 10. Object Complete |  | NA | 03.Medium |
| LOGE0935_IP | Enhancement | Fiori App - Shipping Memo | 09. FUT Overdue |  | NA | 01.Very High |
| LOGE0835_IF | Enhancement | Interface to get the AMT (Asset Management Tool) data on the ISM | 10. Object Complete |  | NA | 04.Low |
| LOGE0239_IP | Enhancement | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 - Table Creation | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0190_IP | Enhancement | Delivery Split for STO in S/4 | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGC1500 | Conversion | IM Stock conversion from Non SAP system to S4 system | 10. Object Complete |  | NA | 02.High |
| LOGC0972_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  | NA | 02.High |
| LOGC0946_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  | NA | 02.High |
| LOGI1584 | Interface | Interface to post inventory in SAP S/4HANA from ECA via MuleSoft. | 06. Dev In Progress |  | MuleSoft | 03.Medium |

**Summary**: 2 Reports, 20 Interfaces, 3 Conversions, 17 Enhancements, 6 Forms, 3 Workflows

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for LO-180:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for LO-180:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (51 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 43 | 84.3% |
| 08. FUT In Progress | 6 | 11.8% |
| 09. FUT Overdue | 1 | 2.0% |
| 06. Dev In Progress | 1 | 2.0% |
| **Total** | **51** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 2 |
| Interface (I) | 20 |
| Conversion (C) | 3 |
| Enhancement (E) | 17 |
| Form (F) | 6 |
| Workflow (W) | 3 |
| **Total** | **51** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 1 |
| 02.High | 18 |
| 03.Medium | 31 |
| 04.Low | 1 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| LOGI1576 | 02.Interface | ECD_Interface between S4 to ECD for inventory status response | 08. FUT In Progress | 03.Medium |
| LOGI1575 | 02.Interface | ECD_Interface between S4 to 3PL for inventory status webservice​ | 08. FUT In Progress | 03.Medium |
| LOGI1295 | 02.Interface | ECD_Interface between S/4 and ECD for completion status | 08. FUT In Progress | 03.Medium |
| LOGI1291 | 02.Interface | ECD_Interface between S/4 and 3PL to send plant/batch level hold/unhold informat... | 08. FUT In Progress | 03.Medium |
| LOGI1290 | 02.Interface | ECD_Interface from ECD to S4 for Inventory Hold/unhold request | 08. FUT In Progress | 03.Medium |
| LOGE1327 | 04.Enhancement | ECD_Enhancement to retrieve plant details for material/batch and update custom t... | 08. FUT In Progress | 02.High |
| LOGE0935_IP | 04.Enhancement | Fiori App - Shipping Memo | 09. FUT Overdue | 01.Very High |
| LOGI1584 | 02.Interface | Interface to post inventory in SAP S/4HANA from ECA via MuleSoft. | 06. Dev In Progress | 03.Medium |

**Tower Context:** FTS-IP has 101 total RICEFW objects (91 complete, 10 active/other)

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

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>LO-180 — Manage Outbound Transportation - FTS (IP)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*51 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| LOGW1078_IP | ISM Workflows - Capital/AMT | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGW1077_IP | ISM Workflows - EIMS/Lab | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| LOGW1076_IP | ISM Workflows - Non-inventory | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGR1176_IP | ISM - International Traffic Report | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGR0833_IP | Email Notification for deletion of Shipping Memos | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGI1679 | Receive 4C1 Inventory movement Stock type change and cycle count from IF | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1678 | Receive 4C1 Inventory Reconciliation Snapshot from IF | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1576 | ECD_Interface between S4 to ECD for inventory status response | Sep-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (95%) | 4. Completed |
| LOGI1575 | ECD_Interface between S4 to 3PL for inventory status webservice​ | Sep-25 (100%) | Jan-26 (100%) | Jan-26 (100%) | Mar-26 (95%) | 4. Completed |
| LOGI1571 | ECD_Interface from ECD to S4 for Inventory status call​ | Sep-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Jan-26 (100%) | 1. On Track |
| LOGI1295 | ECD_Interface between S/4 and ECD for completion status | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Mar-26 (5%) | 3. Off Track |
| LOGI1291 | ECD_Interface between S/4 and 3PL to send plant/batch level hold/unhold information for webservice plants to hold/unhold inventory in 3PL | May-25 (100%) | Jan-26 (100%) | Jan-26 (100%) | Mar-26 (30%) | 3. Off Track |
| LOGI1290 | ECD_Interface from ECD to S4 for Inventory Hold/unhold request | May-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Mar-26 (75%) | 4. Completed |
| LOGI1272 | Response to goods receipt posting from SAP to 3PL - EDI 4C1B | Feb-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Aug-25 (100%) |  |
| LOGI1267 | Inventory Reconciliation with Consignment hub – EDI 4C1 with version control | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) | 1. On Track |
| LOGI1081_IP | Interface + Enhancement - Reprinting of Carrier Label | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) |  |
| LOGI1079_IP | Interface from S4 ISM to Service Now | May-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) | 4. Completed |
| LOGI1074_IP | Send data via API to retrieve the tracking ID - interface + Enhancement | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) | 3. Off Track |
| LOGI0951 | Inbound interface to receive Finished Goods “Goods Receipt” (4B2) signal from 3PL for interplant shipments to post the Goods Receipt in S/4. | Feb-25 (100%) | May-25 (100%) | May-25 (100%) | Aug-25 (100%) |  |
| LOGI0950 | Interface to receive 4B2 signal from Factory and return shipments from ODM/OSAT/Boxing in S4 | Feb-25 (100%) | May-25 (100%) | May-25 (100%) | Aug-25 (100%) |  |
| LOGI0933 | W-lot inventory error handling | Mar-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Oct-25 (100%) | 1. On Track |
| LOGI0836_IP | Interface from S4 to NDA (IPLA –Intel Pre Release License Agreements) | Apr-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Jan-26 (100%) | 4. Completed |
| LOGI0335 | Outbound PIP signal to 3PL for material document transfer – EDI 4C1 | Jul-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Aug-25 (100%) |  |
| LOGI0237_IP | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 | Jun-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Aug-25 (100%) |  |
| LOGF1100_IP | Printing of Standard Shipping Label | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) |  |
| LOGF0359_IP | ISM - Generate Commercial Invoice - IF/IP | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |
| LOGF0358_IP | ISM - Generate Traveler Document - IF/IP | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |
| LOGF0352_IP | ISM - IPLA | Oct-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |
| LOGF0351_IP | ISM - Custom China Special label | Oct-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) | 1. On Track |
| LOGF0350_IP | ISM - India GST DC | Oct-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |

*... and 21 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

**Mapped sub-tower(s):** 8.4 FTS IP - Logistics & Inventory Management

**RAID Summary:** 140 open items (3 capability-specific, 137 tower-level), 444 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 7 | 7 |
| P2 - Medium | 3 | 87 | 90 |
| P3 - Low | 0 | 12 | 12 |
| **Total** | **3** | **137** | **140** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03152 | Action | P2 - Medium | LOGC0972_IP & IF- Test Data to be provided in load files for... | Not Started | FTS IP |  |
| 03503 | Action | P2 - Medium | LOGI1678 and LOGI1679 Queue details | Not Started | FTS IP | 2026-02-03 |
| 03564 | Risk | P2 - Medium | Development of the AMT impacting FPR Capital Tool report | In Progress | FTS IP | 2026-03-27 |

**Other FTS-IP Tower RAID Items** (137 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03578 | Risk | P1 - High | HBI Process Flow Change impact Assessment | In Progress | FTS IF | 2026-03-27 |
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03600 | Risk | P1 - High | Error lifecycle functionality within PDF application is miss... | In Progress | FTS IF | 2026-05-01 |
| 03601 | Risk | P1 - High | Traceability functionality within PDF application is missing... | In Progress | FTS IF | 2026-05-15 |
| 03757 | Risk | P1 - High | IF Planning data not available in ITC1 until W4, leaving too... | In Progress | FTS IF | 2026-04-03 |
| 03764 | Risk | P1 - High | Unable to post IPLA call from postman | Not Started | B-Apps | 2026-03-24 |
| 03767 | Risk | P1 - High | Day 1 OTC Execution - APOP production cutover for allocation... | In Progress | OTC IP | 2026-04-24 |
| 01355 | Action | P2 - Medium | PDF SMHe product development approach does not appear to hav... | To Be Reviewed | FTS IF | 2026-04-03 |
| 01733 | Risk | P2 - Medium | Tariffs impacts Item/BOM design which is impacting ERP/SCP (... | In Progress | E2E | 2026-03-06 |
| 01769 | Action | P2 - Medium | Approach and duration for PDF SMH application refreshes to s... | In Progress | FTS IF | 2026-04-01 |
| 03059 | Risk | P2 - Medium | Operations SME Availability for Change Impact Assessment dev... | In Progress | CM & Comms | 2026-03-17 |
| 03079 | Action | P2 - Medium | Request for PDH Design WTF | In Progress | FTS IP | 2026-03-04 |
| 03128 | Risk | P2 - Medium | Application Health Monitoring | In Progress | FTS IF | 2026-05-13 |
| 03196 | Risk | P2 - Medium | MC1 R3 Data/SCP Readiness | In Progress | Data Readiness | 2026-05-01 |
| 03241 | Risk | P2 - Medium | Materials Planning Policy for Constrained Materials | In Progress | FTS IP | 2026-07-31 |
| 03245 | Action | P2 - Medium | ODM Expedite | Not Started | FTS IP | 2025-12-19 |
| 03246 | Action | P2 - Medium | Expedite Fees | Not Started | FTS IP | 2025-12-19 |
| 03250 | Action | P2 - Medium | Update Commit Date for Holds | In Progress | FTS IP | 2026-03-27 |
| 03251 | Action | P2 - Medium | Out of Cycle Replenishment | In Progress | FTS IP | 2026-03-27 |
| 03267 | Action | P2 - Medium | R3 metrics | In Progress | FTS IP | 2026-03-27 |
| 03276 | Action | P2 - Medium | Biz Documentation | In Progress | FTS IP | 2026-02-27 |
| 03278 | Action | P2 - Medium | Persona validation | In Progress | FTS IP | 2026-02-20 |
| 03334 | Issue | P2 - Medium | Application Monitoring - Connectors Health Monitoring | In Progress | FTS IF | 2026-05-15 |
| 03355 | Risk | P2 - Medium | PTP ECA OSAT Predictive Tool Test Self-Service Query View cr... | In Progress | FTS IP | 2026-04-03 |
| 03368 | Issue | P2 - Medium | Infrastructure resources support PDF SMH ability to provide ... | In Progress | FTS IF | 2026-03-27 |
| 03375 | Action | P2 - Medium | CIBR System Clarification | In Progress | FTS IP | 2026-03-27 |
| 03377 |  | P2 - Medium | KDD Telescoping vs exact network search | In Progress | FTS IP | 2026-03-20 |
| 03406 | Risk | P2 - Medium | Mass Change of Engineering Orders | In Progress | FTS IP | 2026-04-27 |
| 03701 | Risk | P2 - Medium | IP DP (CDP) string test cases has risk of completely beyond ... | In Progress | Test Management | 2026-04-04 |
| 03526 | Action | P2 - Medium | Review process for post-validation of system changes | In Progress | FTS IP | 2026-04-03 |
| | | | *... and 107 more tower-level items* | | | |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*LO-180 — Architecture Document (TOGAF BDAT) · Forecast to Stock (IP) · Generated: March 2026*

