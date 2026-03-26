<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">L-040 — Receive and Put-away Product - PTP</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Procure To Pay (PTP) Tower<br/>
  Capability L-040 · L Logistics and Inventory Management - PTP</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **L-040 Receive and Put-away Product - PTP** within the IAO program. It includes 10 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Procure To Pay (PTP) |
| **Process Group** | L Logistics and Inventory Management - PTP |
| **Capability** | L-040 - Receive and Put-away Product - PTP |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 3 Reports, 171 Interfaces, 16 Conversions, 171 Enhancements, 7 Forms, 10 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Procure To Pay |
| **L1 Process** | L Logistics and Inventory Management - PTP |
| **L2 Capability** | L-040 - Receive and Put-away Product - PTP |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Procurement Process Standardization | Standardize procurement processes across direct, indirect, and services on S/4 HANA + Ariba | IDM 2.0 Procurement Excellence | High |
| 2 | Supplier Collaboration Enhancement | Enable digital supplier collaboration for consignment, subcontracting, and quality management | Supplier Ecosystem | High |
| 3 | Payment Automation | Automate invoice verification, three-way matching, and payment execution | Finance Efficiency | Medium |
| 4 | L-040 Process Migration | Migrate Receive and Put-away Product - PTP business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Procurement | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| PO Cycle Time | < 24 hours | Requisition approval to PO dispatch to supplier | 48 hours (current) | Procurement Lead |
| Invoice Automation Rate | > 80% | Invoices processed without manual intervention (touchless) | 45% (current) | AP Manager |
| Supplier On-Time Delivery | > 95% | Supplier adherence to confirmed delivery date | 89% (current) | Supplier Management |
| L-040 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **10 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for L-040 Receive and Put-away Product - PTP.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | L-040-030_Manage_Receiving_Manifest_-_PTP | L-040-030_Manage_Receiving_Manifest_-_PTP | Warehouse Operator | 1 | 0 |
| 2 | L-040-040_Prioritize_Receipts_-_PTP | L-040-040_Prioritize_Receipts_-_PTP | Procurement Agent, Warehouse Operator | 13 | 5 |
| 3 | L-040-050_Assign_Trucks_to_Docks_-_PTP | L-040-050_Assign_Trucks_to_Docks_-_PTP | Warehouse Operator | 11 | 7 |
| 4 | L-040-080_Record_Receipt_and_Create_Tracking_Label_-_PTP | L-040-080_Record_Receipt_and_Create_Tracking_Label_-_PTP | Warehouse Operator | 22 | 15 |
| 5 | L-040-090_Assign_Batch_Tracking_Number_-_PTP | L-040-090_Assign_Batch_Tracking_Number_-_PTP | Warehouse Operator | 11 | 5 |
| 6 | L-040-110_Build_Pallet_-_PTP | L-040-110_Build_Pallet_-_PTP | Warehouse Operator | 8 | 4 |
| 7 | L-040-120_Determine_Put-away_Location_-_PTP | L-040-120_Determine_Put-away_Location_-_PTP | Warehouse Operator | 10 | 6 |
| 8 | L-040-130_Stage_Product_for_Appropriate_Zone_Moves_-_PTP | L-040-130_Stage_Product_for_Appropriate_Zone_Moves_-_PTP | Warehouse Operator | 2 | 0 |
| 9 | L-040-150_Transport_Product_to_Storage_-_PTP | L-040-150_Transport_Product_to_Storage_-_PTP | Warehouse Operator | 3 | 0 |
| 10 | L-040-170_Record_Stock_Location_-_PTP | L-040-170_Record_Stock_Location_-_PTP | Warehouse Operator | 4 | 0 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 L-040-030_Manage_Receiving_Manifest_-_PTP — L-040-030_Manage_Receiving_Manifest_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 1 | **Gateways**: 0

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
        n1["Receive Manifest from External Vendor"]
        n2(["fa:fa-play Stock Physically Received"])
        n3(["fa:fa-stop Manifest Received"])
    end
    n1 --> n3
    n2 --> n1
    class n2 startEvt
    class n3 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVFtv2jAU_itWKpRNClKuhOVhEgQiTVq1anTtw7oHkxwTC8eObENhiP8-m1soVZ_mhyj-8l18jmPvnFJU4GROr7ejnOoM7VxdQwNuhtw5VuB66Ag8YUnxnIFyLYcIrmf074EWxO3G0ixW4IayrUVnsBCAfn3z0MgImYcU5qqvQFLiem4raYPlNhdMSMu-gyHxySHt9GksZAWyI_h-GpSJkTLKoYOjNE7jwuoUlIJXb0xJQoakdPd2cUy8ljWW-rD8lYJ7vHmmla7NnGCmwHBq3bDveA7M1qjlymLlSq7PzaDK5nDTsFmLS8oXBo99A0nMlx2U-Ps92vd6L_wSih4nLxyZUTKs1AQIUtrA07VGhDKW3cX5qEh8T2kplpDdhdN0EoVeaSvJTOm-Z5vbfwW6qHU2F6w6UfuvtoYsbDee3GSh78mted5kAa-6pHwQDsPhJWmcBnmQn5MIIf-VZPoqH7FanrKmUREWk0tWkAyS3H_vdy5zEqej4LZPINe0hCvToiiiadeq6SAJ_I9Nx0U08PMb0wXW8Iq3neGXPL4YFklaBOmHhse821Wu5g9SlGfDaJoUycUwHQfFKPzQMB4F8fC0QuOzkLit0TOWUAvTTvSjBYm1kEeCHTz4_eL8hBLoGtA95pSAMrsrRYOmGw2SY4aezJ4bjfPnShZ-MjqCM4L7LTPVz7Qol-ih3ipaYsa26ORZGdnnK13U6ZQWbRf5nm9Sjy88QP3-V6M9TcPj9Hp3LXg-BW_g6PTDOp7TgGwwrZxs5xwuIXNRVUDwimln7zl4pcVsy0snOxxWZ9VWZmMnFJseNkdw_w9Q5pHF" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 L-040-040_Prioritize_Receipts_-_PTP — L-040-040_Prioritize_Receipts_-_PTP

**Swim Lanes**: Procurement Agent · Warehouse Operator | **Tasks**: 13 | **Gateways**: 5

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
    subgraph Procurement Agent
        n1["fa:fa-user Create Purchase Order (PO) in S/4"]
        n2["fa:fa-user Assign Priority in Purchase Order in S/4"]
        n14(["fa:fa-play Inbound Delivery Prioritization Initiated"])
        n16["Send PO Information"]
    end
    subgraph Warehouse Operator
        n3["fa:fa-user Create Inbound Delivery Manually with Delivery Priority Indicator in S4"]
        n4["fa:fa-user Run Report to Check Priority Inbound Deliveries"]
        n5["fa:fa-user Perform Unloading Using SAP GUI or RF Scanner"]
        n6["fa:fa-user Perform Goods Receipt Using SAP GUI or RF Scanner"]
        n7[["fa:fa-cog Create Inbound Delivery with Delivery Priority in S4 (Automatically)"]]
        n8[["fa:fa-cog Distribute Inbound Delivery with Delivery Priority Indicator to EWM"]]
        n9[["fa:fa-cog Create Inbound Delivery with Delivery Priority Indicator in S4"]]
        n10[["fa:fa-cog Create Task to Move Inventory from GR Staging Area to Pass Through Area"]]
        n11["Unload Inventory Physically into Warehouse"]
        n12["Count and Verify"]
        n13["Move Inventory from Receiving Area to Staging Area"]
        n15(["fa:fa-stop Process Prioritization Completed"])
        n17["Receive ASN Information"]
        n18{{"fa:fa-code-branch Receiving ?"}}
        n19{{"fa:fa-code-branch Creation of Inbound Delivery ?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
        n23[["fa:fa-folder-open Flow-thru Crossdock Product - FTS (IF)"]]
    end
    n14 --> n1
    n1 --> n2
    n7 --> n20
    n20 --> n8
    n3 --> n20
    n9 --> n20
    n8 --> n21
    n21 --> n4
    n21 --> n11
    n11 --> n5
    n12 --> n6
    n4 --> n22
    n5 --> n22
    n22 --> n12
    n6 --> n23
    n23 --> n10
    n10 --> n13
    n13 --> n15
    n19 -->|"Batch Job"| n9
    n2 --> n16
    n16 --> n18
    n17 --> n7
    n18 -->|"ASN Scenario"| n17
    n18 -->|"Non ASN Scenario"| n19
    n19 -->|"Manual"| n3
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n14 startEvt
    class n15 endEvt
    class n16 startEvt
    class n17 startEvt
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV22P2jgQ_itWqhVbCXR5JcCHO7FAqq26LVq67YdyH0ziEGuDHTkOu3TLf79xSEISgnR33Q8s83jmmRd7xuZN83lAtIl2c_NGGZUT9NaTEdmR3gT1NjglvT46Ad-woHgTk7SndELO5Ir-zNUMO3lVagrz8I7GB4WuyJYT9HTfR1MwjPsoxSwdpETQsNfvJYLusDjMeMyF0n5HRqEe5t6KpTsuAiLOCrruGr4DpjFl5Axbru3anrJLic9Z0CANnXAU-r2jCi7mL36EhczDz1LygF-_00BGIIc4TgnoRHIXf8IbEqscpcgU5mdiXxaDpsoPg4KtEuxTtgXc1gESmD2fIUc_HtHx5mbNKqfo0-OaIfjzY5ymcxKiVAK82EsU0jievLNnU8_R-6kU_JlM3pkLd26ZfV9lMoHU9b4q7uCF0G0kJxseB4Xq4EXlMDGT1754nZh6Xxzgs-WLsODsaTY0R-ao8nTnGjNjVnoKw_C3PEFdxVecPhe-FpZnevPKl-EMnZl-yVemObfdqdGuExF76pMaqed51uJcqsXQMfTrpHeeNdRnLdItluQFH86E45ldEXqO6xnuVcKTv3aU2WYpuF8SWgvHcypC987wpuZVQntq2KMiQuDZCpxESLFlAtqOSTTdwudpXf0x48daC_EkxANVbjQTBNJBy0zAUUsJ-qL6Bt0uv7xHlKHVH_Za-7tmbTatp2lKtwz8US6oPCiTFlMXiWHfVjRJDJW8ZxuesQDNSUz3RBxKQvoTS8oZrMN3CDMAnvd1oiHwrOCAouUXUAq52OUGlTtYapXmOxYk4pmKLyECSy5qfFZnbS6ie8Asw3F8QC9URhdBq3QC6ivqPPtW8nbTx2PG0CNJOHS55GgWEf-5TtTwTEna5HKaXEsiVAnQE4s5DmCcoKdUfa6mS_Th6R5BQI8eWvmYMSKaTMNupg-cBynE5xOayH_P5v6o6Hy-vVrHK-XLi4Zup5nkajt9Ver34KDuYdT0MKfQH3ST_Qcv502Cui--P7QcjH8rhcsT0Dj_eid5PqUgmAe-V5720LccSEPBYSMe0Urirar_FLSV2hKmB_oaCZ5toxxse1GdfjoKNbZldEhPJYXQgKXqh1aLqkafQa4SYcj3m7p4Dy0V1S1dsebHZV8PtR56i8Q5j4JU8iQfXQQSa02AGd8lMemYAC6YnxwSNF197pwCJ83R29u56AEZbODe9aNatH-tteOxbjHutsi3SwXFw8sD0SYx9W4S8urHWQo2H063SdvMOJthIfhLOsCxRAkWsHUkvmJk_h8j63wYQ7iwiRjwhDDkwetjICORQb48TQOeDyYeZL5EA-R9XaHbe6_WltWohfGOBoM_4X8pn0SzEN1CLG5B-HICRoVstdbHLXlUyCW9WfDbLdmo_BeAU8rmSR4WchGuWQbotGSz0DdKYFgoWKVCEbJRhmgUKRmlhlFqVDHkWf1aa3dYwmn4yDdr7RfkWjIW6mWIRuHSKItkFFV0S3lU8KkeWPmEwXub55TGhcpnOLqXauN2ZKdbLl-0ag8WtZ_lQ60Bm92w1Q3b3bDTDQ-7Ybf-wGusjK6ujK-uwK5dXbKrJ3cTd4rncRMdXtF2r-Cj8k3ZhMedMPRLJ2x0w2Y3bJWvTq2v7QhMTBpokzct_7EGP-gCEuIsltqxr2G4h1cH5muT_EeNliUBEM4phgfV7gQe_wHxImwb" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 L-040-050_Assign_Trucks_to_Docks_-_PTP — L-040-050_Assign_Trucks_to_Docks_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 11 | **Gateways**: 7

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
        n1["fa:fa-user Perform Unloading of Physical Boxes via RF Scanner or SAP GUI"]
        n2["fa:fa-user Perform Manual Entry of PO in Standard Monitor Report to Identify the..."]
        n3["fa:fa-user Scan 'Vendor Label' Details to Identify Correct Inbound Delivery"]
        n4["fa:fa-user Perform Manual Update of House Airway Bill (HAWB) Details in Inbound Delivery"]
        n5["fa:fa-user Create Inbound Delivery for EWM Location"]
        n6["fa:fa-user Save the Inbound Delivery Document"]
        n7["fa:fa-user Raise Exception or Perform GR and Print GR Label/Exception Label"]
        n8[["fa:fa-cog Distribute Inbound Delivery to EWM"]]
        n9[["fa:fa-cog Create Inbound Delivery for EWM Location with HAWB Details (Automatic)"]]
        n10["Update S4 Inbound Delivery Number with HAWB Details"]
        n11["Count and Verify Physical Boxes"]
        n12(["fa:fa-play Truck Assignment to Dock Initiated"])
        n13(["fa:fa-stop Inbound Delivery Number Updated"])
        n14["Determine Put-away Location - PTP"]
        n15{{"fa:fa-code-branch Vendor Label Available?"}}
        n16{{"fa:fa-code-branch Manual Update of HAWB Details in EWM?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
        n18{{"fa:fa-code-branch Receiving Scenario ?"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-arrows-alt Update Number / Raise Exception?"}}
        n22[["fa:fa-folder-open Record Receipt and Create Tracking Label - PTP"]]
    end
    n12 --> n18
    n8 --> n1
    n2 --> n19
    n1 --> n15
    n11 --> n16
    n22 --> n14
    n4 --> n6
    n18 -->|"Non ASN"| n5
    n7 --> n22
    n6 --> n21
    n9 --> n17
    n15 -->|"Yes"| n3
    n18 -->|"ASN"| n9
    n5 --> n17
    n17 --> n8
    n15 -->|"No"| n2
    n19 --> n11
    n3 --> n19
    n20 --> n7
    n10 --> n13
    n21 -->|"Raise Exception"| n20
    n21 -->|"Update INB Number in S4"| n10
    n16 -->|"No Manual update (ASN scenario)"| n20
    n16 -->|"Yes (Non ASN Scenario)"| n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 serviceTask
    class n9 serviceTask
    class n12 startEvt
    class n13 endEvt
    class n14 startEvt
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11vozgU_SsWoyqtlMwAgZDkYVf5YqbStBM17VSryT44YBKrBCNj0mQ7-e97DZgEQker2TxU9eHec-6XsXnTPOYTbahdXb3RiIohemuJDdmS1hC1VjghrTbKge-YU7wKSdKSNgGLxIL-k5kZVryXZhJz8ZaGB4kuyJoR9HTbRiNwDNsowVHSSQinQavdijndYn6YsJBxaf2B9AM9yNSKR2PGfcJPBrruGJ4NriGNyAnuOpZjudIvIR6L_AppYAf9wGsdZXAhe_U2mIss_DQhd3j_TH2xgXWAw4SAzUZsw694RUKZo-CpxLyU71QxaCJ1IijYIsYejdaAWzpAHEcvJ8jWj0d0vLpaRqUoepwuIwQ_L8RJMiUBSgTAs51AAQ3D4QdrMnJtvZ0Izl7I8IM5c6Zds-3JTIaQut6Wxe28ErreiOGKhX5h2nmVOQzNeN_m-6Gpt_kB_ta0SOSflCY9s2_2S6WxY0yMiVIKguB_KUFd-SNOXgqtWdc13WmpZdg9e6Jf8qk0p5YzMup1InxHPXJG6rpud3Yq1axnG_r7pGO329MnNdI1FuQVH06Eg4lVErq24xrOu4S5Xj3KdDXnzFOE3Znt2iWhMzbckfkuoTUyrH4RIfCsOY436BlzsmFQTvQtJhwLxnMD-YuMH0stwMMAd2S90ZzwgPEteopChn2YQcQCNN8cEurhEI3ZniRoRzF6cNHCw1EELoyjxWiOPj_dLrW_z5jNZuY7HKVANYsEP2Tk3xCN0EJgud98dMfgzQGUDyRmMOuCoVufRIIGBwSvjo8fP1ZFulURGRNqfYchBYps-7XQlAhMw6RCNWGcE0-g22jF0sgHm5DuCD9Uya1fZvAU-9B6mcKXrLgjyuUcjKFt6PrL6Hl8U0pDgr9WsqtKE04kdd0HgTyaPd-hr8zDgrKoStKr1QLviKzZJc2UeekWKlF1d6ruD5hCUrO9R2IpJdusCvD5AUG30JzTSMhFVuhPJ9NsXSXv_yjZPbZGUwoTTFdpU5LQJ8gR3M_9B1X__1og9ErFBslmlL24HqWCbeGpd1PTMHTQKLq6sC7J79PtCgpzQVnN1JA7agKeIivSd3lIHWpbqOZhXpfJxSGM0CNPvRc0ShK6jmSfZEmgZy8QEhUUwvOB4OacoXtiSASL3409z-7CXQ46JEP4Fs5DNE9FB8tRLqvYQfPHeS1o--3t1BGfdFZwcHkbdL730GgH9ZEH_Z9L7Xg89-41e19urfPWwTaC5l5wOc1cZO-FaQLpf87f0HW3frPbA_EI3ck338IjEVxUGLpQHPyWoqn_nptxcsOcs9ekg0OhalQ09lN9v9ZjNs3TDgrgJCa8w2ISyXThcpRnHecjW2yuR469F1mHvJdqBoohgDbn_8D4ok7nD1nQAugX62KpHg-UfbG21VoBPeWgPKwCsPK1em5kAj-X2j2M5mhxv9R-whu0eOjktqZZrHvFWkUzKLgdRWYXZH_JbQlE3bqKUlDx23WGQrJfZ7xnmZ-KxFDSKpRurTCmngMlcbE2VEimUTDXep3L6HWrYkJu78dqSuRBa2XWhrI2emW0avelud81JI6SYg_cVDVKL6gaui76UG6Y3Ng6u9fIrqv7XAU2m-FuM2w1w3Yz3GuGnWa4f349rDwZvPsERl_dvat4t7gnV1HrHWtbXSKrcK8ZdprhfjM8aIRh1Bphoxk21aVUa2tbOCUw9bXhm5Z9y8H3nk8CnIZCO7Y1DIfr4hB52jD75tHyWZpSDFfRbQ4e_wUmR3TW" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 L-040-080_Record_Receipt_and_Create_Tracking_Label_-_PTP — L-040-080_Record_Receipt_and_Create_Tracking_Label_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 22 | **Gateways**: 15

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
        n1["fa:fa-user Perform Good Receipt via RF Scanners Using Inbound Delivery"]
        n2["fa:fa-user Perform Unloading of Physical Boxes via RF Scanner or SAP GUI"]
        n3["fa:fa-user Move to Pick and Drop Location"]
        n4["fa:fa-user Create Inbound Delivery for EWM Location"]
        n5["fa:fa-user Create Inbound Delivery for EWM Location"]
        n6["fa:fa-user Change Staging Area from GR Zone to Hold Area"]
        n7["fa:fa-user Post GR"]
        n8["fa:fa-user Create an Exception Notification (Log in to the Quality Notification App)"]
        n9["fa:fa-user Select Predefined Disposition and Create a Task (Buyer/Planner)"]
        n10["fa:fa-user Select Relevant Disposition from the Catalogue and Enter the Comments in the..."]
        n11["fa:fa-user Utilize Exception Report to Find out the Disposition Provided from the Buyer..."]
        n12["fa:fa-user Perform Action as per Disposition and Update Action in Exception Notification"]
        n13["fa:fa-user Create Task for the Buyer/Procurement Agent with Details of the Exceptions"]
        n14[["fa:fa-cog Auto Create Inbound Delivery for EWM Location"]]
        n15[["fa:fa-cog Auto Print Good Receipt (GR) Tracking Labels"]]
        n16[["fa:fa-cog Update Goods Receipt Status in Inbound Delivery"]]
        n17[["fa:fa-cog Distribute Inbound Delivery to EWM"]]
        n18[["fa:fa-cog Receive Buyer/Planner Email with the Link to the Exception (in the App)"]]
        n19[["fa:fa-cog Create Task for Buyer with Reject Comments"]]
        n20["Count and Verify Physical Boxes"]
        n21["Deconsolidate Physical Boxes"]
        n22["Collaborate Buyer/Planner With Supplier and Provide Disposition"]
        n23(["fa:fa-play Goods Receipt Process Initiated"])
        n24(["fa:fa-stop Stock Moved to Drop Point"])
        n25["Determine Putaway Location"]
        n26["Delivery Created for QM Relevant Material in Quality Inspection (QI) Stock Type"]
        n27["Delivery Created for MQCS Relevant Material Based on the MQCS Status table..."]
        n28["Delivery Created in Unrestricted for Putaway (F2) Stock Type"]
        n29["Delivery Created for QM Relevant Material in Quality Inspection (QI) Stock Type"]
        n30["Delivery Created for MQCS Relevant Material in Blocked(B6) Stock Type"]
        n31["Delivery Created in Unrestricted for Putaway (F2) Stock Type"]
        n32["Exception Label Print Triggered"]
        n33{{"fa:fa-code-branch Priority Shipment ?"}}
        n34{{"fa:fa-code-branch Exception ?"}}
        n35{{"fa:fa-code-branch Receiving Scenario ?"}}
        n36{{"fa:fa-code-branch QM or MQCS active?"}}
        n37{{"fa:fa-code-branch Creation of Inbound Delivery?"}}
        n38{{"fa:fa-code-branch exclusiveGateway"}}
        n39{{"fa:fa-code-branch QM or MQCS active?"}}
        n40{{"fa:fa-code-branch exclusiveGateway"}}
        n41{{"fa:fa-code-branch exclusiveGateway"}}
        n42{{"fa:fa-code-branch exclusiveGateway"}}
        n43{{"fa:fa-code-branch Delivery Available?"}}
        n44{{"fa:fa-code-branch Operator Checks the disposition ?"}}
        n45{{"fa:fa-code-branch exclusiveGateway"}}
        n46{{"fa:fa-code-branch exclusiveGateway"}}
        n47{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n33 -->|"No"| n25
    n3 --> n24
    n21 --> n20
    n20 --> n34
    n1 --> n15
    n15 --> n16
    n17 --> n2
    n2 --> n21
    n23 --> n35
    n14 --> n36
    n33 -->|"Yes"| n3
    n34 -->|"No"| n1
    n35 -->|"ASN"| n14
    n35 -->|"Non ASN"| n37
    n4 --> n38
    n5 --> n38
    n38 --> n39
    n40 --> n41
    n41 --> n17
    n42 --> n41
    n6 --> n7
    n7 --> n46
    n8 --> n13
    n18 --> n22
    n22 --> n9
    n10 --> n11
    n11 --> n44
    n16 --> n45
    n12 --> n45
    n45 --> n33
    n19 --> n47
    n44 -->|"Accepted"| n12
    n9 --> n10
    n37 -->|"Batch Job"| n5
    n37 -->|"Manual"| n4
    n26 --> n40
    n36 -->|"QM is active"| n26
    n27 --> n40
    n36 -->|"MQCS is active"| n27
    n36 -->|"Both not active"| n28
    n28 --> n40
    n29 --> n42
    n39 -->|"MQCS is active"| n30
    n30 --> n42
    n31 --> n42
    n39 -->|"QM is active"| n29
    n39 -->|"Both not active"| n31
    n46 --> n8
    n43 -->|"Yes"| n6
    n43 -->|"No"| n46
    n13 --> n32
    n32 --> n47
    n47 --> n18
    n44 -->|"Rejected"| n19
    n34 -->|"Yes"| n43
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
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n23 startEvt
    class n24 endEvt
    class n25 startEvt
    class n26 startEvt
    class n27 startEvt
    class n28 startEvt
    class n29 startEvt
    class n30 startEvt
    class n31 startEvt
    class n32 startEvt
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
    class n45 gateway
    class n46 gateway
    class n47 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNq1WW1z4jgS_isqpqaSqSKz-B34cFdAYDZXkzkmTHbqbnMfhJFBF2O5ZEHCZfPfr2VLBgt5qia3lw9J_Kj76Rd1t4R56cRsRTrDzvv3LzSjYoheLsSGbMnFEF0scUEuuqgCfsOc4mVKigspk7BMLOh_SjHHz5-lmMRmeEvTg0QXZM0Iur_pohEopl1U4Ky4KginyUX3Iud0i_lhwlLGpfQ70k96SWlNLY0ZXxF-FOj1IicOQDWlGTnCXuRH_kzqFSRm2apBmgRJP4kvXqVzKXuKN5iL0v1dQW7x83e6Eht4TnBaEJDZiG36GS9JKmMUfCexeMf3Ohm0kHYySNgixzHN1oD7PYA4zh6PUNB7fUWv798_ZLVR9O36IUPwE6e4KK5JggoB8HQvUELTdPjOn4xmQa9bCM4eyfCdO42uPbcby0iGEHqvK5N79UToeiOGS5aulOjVk4xh6ObPXf48dHtdfoDfhi2SrY6WJqHbd_u1pXHkTJyJtpQkyf9kCfLKv-HiUdmaejN3dl3bcoIwmPTO-XSY1340csw8Eb6nMTkhnc1m3vSYqmkYOL120vHMC3sTg3SNBXnChyPhYOLXhLMgmjlRK2Flz_Ryt5xzFmtCbxrMgpowGjuzkdtK6I8cv688BJ41x_kGfcecbBikE_09JxwLxisB-ZM5vz90EjxM8JXMN5oTnjC-RZ8YW6E7EhOaC7SnGN3N0CLGWUZ4ge4LKE50ky3ZLluha5LSPeGHh86_TnhdO-99ljK8kuosQfPNoaAxTtGYPZPCMIMYR4vRHH26v2kye03mW7YnSDA0p_EjwtIfznL0mcVYUJY1Vf2m6oQT2LyzQBB4iqbfb1tIgj-DJDRINjhbE7QQeC1zMwJOlHAG-3CH_smyMsBfoX_KlSZTZCSaFQK0mjJ9q8s4Q9PnmOTSO_SFCZrQylV0-ZmtEc2kVZjX6OsOp1QcmjKjPP_QtDJoWlmQlMQCzTlZkQTmLOSGFjkraKkud0r7gcqOvBzvDoT_Mk_L7Te4nZ6V_A7-7HEmGtRl4qTfEyxwytY7UlqbZgIUS5xttyQTRRnihnz8-NEwZjTFvaApnE8n2bojOYNJDPmZUaBmO1ESn3oBPbynK4i6dqeM79xYS6eM4ipPBYKmPUvdfb6SqVNCtG0nDVOetQ6qecj40clf5ADacSKzhEZr-fuJig0Ut8A0LWTvStnaZmHY8X-vDcVQSaMdJOon-qTBFVi45pyCS40Zdfnp7gP6xnH8KBuoOnlNqrBJpXIoaYqaB1pQ7MrKsMy3BlvUZIMdEpwud7YYwWUI0SToNwlKD_b1DlRtgKZbyHiVfZnyzzR71G153PLLqpB1TzasDJpWzD0vrVX8d-Tfsqd0dxhEruzACcQlygL8TV6-DsYIN44A2UbX8iZVsJSWuf6huFsaSFO8ZFwKNxPxXbq42OV5SuFJuqA67LQ3DEbvso49T-GMbm61LHJSFLBdoAsGV6D94VTdP6oXAg6VhWBwxsgDZyX3oDxo5gxK0VQMysBh3Gxh7qH5TmB5Q7CfBG5YCqtKqbZnVW7N19vjfLsFVF59ZWHqcXyTFTmpBsDl15sPyr1vh5wYFqI2C7dfJwuLjTHc1WGoVTVVyqiuEPLSfjbB3L6NHxy9zziRTRFrezoTlzP3B-4O_t8J8Xo_mRCwMU6Bi6wux-EPeJ0_NRGebIhjk5czTY2-b5yu14SXJXuq4b28HJt9Ra6W8Gki3kglxmWGFhual0P9rw-d19dTTd-ueTR_phHYNaoxJofwIiYZfNBj56qhXRX2V-8Bhm3ckzPFyK5Yplo6CQeTOXzPOPp2DvIcp7sCVD5VF3pTbfBGn_3em-z5ztvU3LeptRROXcyjPRxDsvvPwmspHP1RA662JH4sylGyOrnEnPEEb3M8fJta9LNq8Lm3-geaDF1d_eWPh84X9tD5Q057vSBxeWyoZ9dRQE8DvQrwtIQScDSDEygg1ECkKDSDenT0s7Lp1Qy-AkLT23_I8xbc9fSC3wxDU3qBwkeLL9WCb658kdd_tepFalUb7qvnwHj2-goYaAWVDV9b9nU6akrXkAirZ72ukuPrWJUFR4foKMCt06cItQuOcsHRBhzlgl_vkDLp1wl2DcDXgdZWB0qiDkNnehTLYSqHtkyrdkqJO7pKvEiJj7GAkvwbW5bygbl8izM498q1uuK0tzVXqIRhTNFCTaiqanXS3KhNpxxqhlZkCo0ZXMsyJhpSes_dvsHt6tzo4L1BuzGv9qhnajltNOdxDkwRm8deXYMqgzoC32yf0FxQ7VMXoaNbsvbNNetBZdzpmwVS3cB1gQzMTtU--N7JKyM5RfSrsgbs2mHPDvt2OLDDoR2O7HDfDg_sMDSlHW-J02kJ1GmJFEbkyYvA5lLQvhS2L0XtS_32pUHrEkx1_Uq3ifvq9WsTDVqkwxY8asH7LfjAjkNX2nGnBXdbcE-_Q23Cvh0O7HBohyM73LfDAysMB5UVduywa4ftUfr2KH17lL49Sr-OstPtbOFTJ6arzvClU37XAt_HwPs3vEtF57XbwfD6ZHHI4s6w_E6isyvfgVxTDK-KtxX4-l9X1xJ6" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 L-040-090_Assign_Batch_Tracking_Number_-_PTP — L-040-090_Assign_Batch_Tracking_Number_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 11 | **Gateways**: 5

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
        n1["fa:fa-user Create Inbound Delivery"]
        n2["fa:fa-user Create SAP Batch While Performing Good Receipt via RF Scanner Based on..."]
        n3[["fa:fa-cog Create Batch Number From ASN"]]
        n4[["fa:fa-cog Distribute Inbound Delivery With Batch Information"]]
        n5[["fa:fa-cog Create Inbound Delivery Without Batch number"]]
        n6[["fa:fa-cog Create Inbound Delivery With Batch Information"]]
        n7[["fa:fa-cog Distribute Inbound Delivery Without Batch Number"]]
        n8[["fa:fa-cog Distribute Inbound Delivery"]]
        n9[["fa:fa-cog Update SAP Batch in Inbound Delivery"]]
        n10[["fa:fa-cog Create Inbound Delivery"]]
        n11["Check For The Receiving Scenario"]
        n12(["fa:fa-play Batch Number Capture Initiated"])
        n13(["fa:fa-stop Batch Number is Captured"])
        n14["Record Receipt and Create Tracking Label - PTP"]
        n15["ASN received"]
        n16{{"fa:fa-code-branch Receiving Scenario?"}}
        n17{{"fa:fa-code-branch Is Material Batch Managed ?"}}
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch Creation of Inbound Delivery ?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21[["fa:fa-folder-open Record Receipt and Create Tracking Label"]]
    end
    n12 --> n17
    n3 --> n6
    n6 --> n4
    n1 --> n20
    n2 --> n9
    n5 --> n7
    n17 -->|"No"| n5
    n11 --> n16
    n17 -->|"Yes"| n11
    n8 --> n2
    n7 --> n14
    n4 --> n21
    n21 --> n18
    n9 --> n18
    n18 --> n13
    n20 --> n8
    n10 --> n20
    n15 --> n3
    n16 -->|"ASN"| n15
    n19 -->|"Batch Job"| n10
    n16 -->|"Non ASN Scenario"| n19
    n19 -->|"Manual"| n1
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n12 startEvt
    class n13 endEvt
    class n14 startEvt
    class n15 startEvt
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV9tu4zYQ_RVCQeAWsAPdZeuhhS_RIosmDdbZBsW6D7RE2URkUqAkJ67X_96hLpalSNi09UMQnplz5uKRhj4qPg-I4irX10fKaOqi4yDdkh0ZuGiwxgkZDFEB_IEFxeuIJAPpE3KWLunfuZtmxm_STWIe3tHoINEl2XCCvt4N0RSI0RAlmCWjhAgaDoaDWNAdFoc5j7iQ3ldkHKphHq00zbgIiKgdVNXRfAuoEWWkhg3HdExP8hLicxY0REMrHIf-4CSTi_irv8UizdPPEnKP355pkG7hHOIoIeCzTXfRb3hNIlljKjKJ-ZnYV82giYzDoGHLGPuUbQA3VYAEZi81ZKmnEzpdX6_YOSh6WqwYgo8f4SRZkBAlKcC3-xSFNIrcK3M-9Sx1mKSCvxD3Sr91FoY-9GUlLpSuDmVzR6-Ebrapu-ZRULqOXmUNrh6_DcWbq6tDcYC_rViEBXWkua2P9fE50szR5tq8ihSG4f-KBH0VTzh5KWPdGp7uLc6xNMu25up7varMhelMtXafiNhTn1yIep5n3NaturUtTe0XnXmGrc5bohuckld8qAUnc_Ms6FmOpzm9gkW8dpbZ-lFwvxI0bi3POgs6M82b6r2C5lQzx2WGoLMRON6iZyzIlkM70e8xETjlonCQH6Z9WykhdkM8kv1Gc0GgHnTH1jxjAVqQiO6JOKyUvy44eidnOX1EM5z6EHBLI4IeiQi52MEco0-cB-gL8QmNU7SnGH3x0NLHjAF7Bi-GAHF2c3PTjGJ8O4fx-aaKUkR4yHZr4HqC79B0-QDES6bZZC4otIuus4660DNNt6XmHZPp4pRy1tKzOjPp1OJZWsqxPMWWkv1xpR9m5fy7KuvMHroyG39YrUWcNIlf46A5DJT9SEFTP9SVNktO7nxL_BfkcYGetqSYsL0cuKVPGOwY3pwoTf_pHCiO4JltDNMcx2kmZFyaUkggAPLPl2yjZicpj5tsmlQC73gm0CA12EHnZwBDXWWZTwL7LzLnfFugEXp8emylbYEATDkSeX15gEuzfTzW7QvIaA0rBBJ7341fV8rpdMl0upl3CbqH1OSqLYu8xwxv4DF9pzDuViBvfpQlkOun4u3Ypk26aXlLYNIRD98PcTu2rv6n2LpWT1sIK4mIEY8JQx_9huoxhFVY_AODhUajX2RDS8AoznZ5tIujWbkXx2rjsZI9KY9Wcay0NEeev6-UBxjn72Cu8FJGs9uOf5Ik99TKBcjGZcDy6JTEKh-zNFfueqU8LoFJ66yVgppRMdQCODuorRK1sqiKoNllrvnbW-Z6LmtSWorJ-8zXhV1tMx9gTuRTUT_r0m3SloHRzXBUGC82rfwWqhtGA9a7YePy9tCwmL0Wq9di91qcXsu41zLptcD30GvSz_fGJm6Ud7wmavZ4Wz24XV2MmrDTDY-74UknDMPWCWvV1UkZKjsCS5MGintU8l8c8KskICHOolQ5DRWcpXx5YL7i5jdzJcuX1oJiuDDtCvD0D2zkBTk=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 L-040-110_Build_Pallet_-_PTP — L-040-110_Build_Pallet_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 8 | **Gateways**: 4

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
        n1["fa:fa-user Create Inbound Delivery"]
        n2["fa:fa-user Perform Unloading Via RF Scanner Using ‘Unloading by Delivery’ Option"]
        n3[["fa:fa-cog Distribute Inbound Delivery Without Any HU Number"]]
        n4[["fa:fa-cog Distribute Inbound Delivery to EWM"]]
        n5[["fa:fa-cog Create Handling Unit via Packaging Specification or Based on Vendor Label"]]
        n6["Deconsolidate Received Physical Box"]
        n7["Initiate Put-away for Stock With HU Number"]
        n8["Initiate Put-away for Stock Without HU Number"]
        n9(["fa:fa-play Material Shipping Initiated by Vendor Based on the Purchase Order (via ASN..."])
        n10["Determine Put-away Location PTP"]
        n11{{"fa:fa-code-branch exclusiveGateway"}}
        n12{{"fa:fa-code-branch Spares ?"}}
        n13{{"fa:fa-code-branch HU Number Required for Final Put-away?"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n15[["fa:fa-folder-open Record Receipt and Create Tracking Label - PTP"]]
    end
    n3 --> n6
    n7 --> n11
    n11 --> n10
    n8 --> n11
    n9 --> n1
    n1 --> n12
    n4 --> n2
    n2 --> n5
    n15 --> n13
    n12 -->|"No"| n4
    n12 -->|"Yes"| n3
    n13 -->|"No"| n8
    n13 -->|"Yes"| n7
    n5 --> n14
    n6 --> n14
    n14 --> n15
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n9 startEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVm2P4jYQ_itWViuuUljllbD50Iq39Fa63aJjX1Qd_WASB6wNduo4LJTjv3cckkByIJ1aPqD48cwzM48n4-y1kEdE87Xb2z1lVPpo35ErsiYdH3UWOCMdHR2BVywoXiQk6yibmDM5o_8UZqaTbpWZwgK8pslOoTOy5AS9POhoAI6JjjLMsm5GBI07eicVdI3FbsQTLpT1DenHRlxEK7eGXEREnAwMwzNDF1wTysgJtj3HcwLll5GQs6hBGrtxPw47B5Vcwj_CFRaySD_PyCPevtFIrmAd4yQjYLOS6-QLXpBE1ShFrrAwF5tKDJqpOAwEm6U4pGwJuGMAJDB7P0GucTigw-3tnNVB0fN4zhD8wgRn2ZjEKJMATzYSxTRJ_BtnNAhcQ8-k4O_Ev7Em3ti29FBV4kPphq7E7X4QulxJf8GTqDTtfqgafCvd6mLrW4YudvDfikVYdIo06ll9q19HGnrmyBxVkeI4_l-RQFfxjLP3MtbEDqxgXMcy3Z47Mn7kq8ocO97AbOtExIaG5Iw0CAJ7cpJq0nNN4zrpMLB7xqhFusSSfODdifB-5NSEgesFpneV8BivnWW-mAoeVoT2xA3cmtAbmsHAukroDEynX2YIPEuB0xV6w4KsOMiJ_kiJwJKLo4H6MfPbXIuxH-Ou0huNBIF60ANb8JxFaEwSuiFiN9f-OvOxmj5TImIu1uiFJRxH0LfolWL0NUCzEDMGBi-ZAue5ZZj9k9Fid6JXW_eQnqScNWPZ3-pgIV-iMYXS6SK_kCN6oxLKlGjAdujzC3rK1wsigO2czvl5OsnR5O2x5e82_Uu5PmMWJaqmFxh7aAPVT3H4jpcKmqUkpDENsaoNcYGGMAkjBM-v8C7BupgSrTA9iDJWMyjjCY1UiK8kJJBXhKarXQZsCRrybVMqD5weIAGq7Ke57OKiLyHETPLwvdCnIcyZb_8nfJW2V9zvP9WypAk4PgKNmtRotqJpqmSoyCN17mXltRJwKUBQAeNNNama1eiTUnEwe7q7u4NQv5x3rFGIAwHWML1PyX7hpcbT52kzO9Pc70-nFpHuAoZsuEJkGyZ5Bqr-fnyH59rhcO5mXXaD6SxIhn5rm9uXzWvJ4Az_zqmAkpWuAWWgT5X9D2TOf0v5rD9jmLdEdHlKmOoeuAKPTZRKBO1ate6zgE5VB1S0IeqW6pXywTkdH5iNut1foTHLpXdcmuWIhYcSKKcZ67cM7st1ZV8urXLtHNfV0jou3craLc3tCigMvs-1Jz7XvoN7G_-TZMVG7WA3HfptvHLwyo0qYsXca63NMmPTPRvfqq7q2mrA1mXYPr-SGjvO1R336s59_SHQTMm4gpvV3dWErcuwfRl2LsNudY1puraGNxXTSPP3WvH1B1-IEYlxnkjtoGs4l3y2Y6HmF19JWp6qeTemGC6v9RE8_AvFSkXy" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 L-040-120_Determine_Put-away_Location_-_PTP — L-040-120_Determine_Put-away_Location_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 10 | **Gateways**: 6

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
        n1["fa:fa-user Enter Final Putaway Storage Bin to during Warehouse Task Creation"]
        n2["fa:fa-user Create and Save Putaway Warehouse Task"]
        n3["fa:fa-user Check for Available Storage Bins via SAP monitor"]
        n4[["fa:fa-cog Create Putaway Warehouse Task with details of Final HU and Destination..."]]
        n5[["fa:fa-cog Create Putaway Product Warehouse Task with only Destination Storage Bin for..."]]
        n6[["fa:fa-cog Update Goods Receipt Completion in Inbound Delivery"]]
        n7[["fa:fa-cog Determine Appropriate Storage Bin as per Putaway Strategies, Storage Bin..."]]
        n8[["fa:fa-cog Determine Appropriate Storage Type"]]
        n9[["fa:fa-cog Determine Appropriate Storage Section"]]
        n10["Move to Pick and Drop Location"]
        n11(["fa:fa-stop Stock Moved to Drop Point"])
        n12["Confirm/Adjust Location - PTP"]
        n13["The Stock Type of the QM Relevant Material in this Delivery Document still..."]
        n14["The Stock Type of MQCS Relevant Material in this Delivery Document is Based..."]
        n15["The Stock Type for No Quality Inspection and MQCS relevant material in this..."]
        n16["Record Receipt and Create Tracking Label - PTP"]
        n17{{"fa:fa-code-branch Creation of Putaway Task ?"}}
        n18{{"fa:fa-code-branch Parts stored in HU ?"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch High priority Order?"}}
        n21{{"fa:fa-code-branch QM or MQCS Active?"}}
        n22{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n1 --> n2
    n3 --> n1
    n7 --> n18
    n8 --> n9
    n9 --> n7
    n6 --> n20
    n10 --> n11
    n19 --> n12
    n16 --> n6
    n2 --> n19
    n18 -->|"Yes"| n4
    n18 -->|"No"| n5
    n5 --> n19
    n4 --> n19
    n17 -->|"System Driven"| n8
    n20 -->|"Yes"| n10
    n17 -->|"Manual Creation"| n3
    n20 -->|"No"| n21
    n22 --> n17
    n13 --> n22
    n14 --> n22
    n15 --> n22
    n21 -->|"MQCS is Active"| n14
    n21 -->|"QM is Active"| n13
    n21 -->|"Both not active"| n15
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n11 endEvt
    class n12 startEvt
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 startEvt
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV22P4jYQ_itWTitaCa5JSAjwoRVvuTvp9o4rez1VRz-YxAF3ExvZDrt0j__ecUhCEkKlVfmA8OOZ55kZj194MQIeEmNs3N29UEbVGL101I4kpDNGnQ2WpNNFZ-APLCjexER2tE3EmVrRfzIzy9k_azON-Tih8VGjK7LlBH390EUTcIy7SGIme5IIGnW6nb2gCRbHGY-50NZvyDAyo0wtn5pyERJxMTBNzwpccI0pIxe47zme42s_SQLOwhpp5EbDKOicdHAxfwp2WKgs_FSSe_z8jYZqB-MIx5KAzU4l8Ue8IbHOUYlUY0EqDkUxqNQ6DAq22uOAsi3gjgmQwOzxArnm6YROd3drVoqih_maIfgEMZZyTiIkFcCLg0IRjePxG2c28V2zK5Xgj2T8xl54877dDXQmY0jd7Ori9p4I3e7UeMPjMDftPekcxvb-uSuex7bZFUf4bmgRFl6UZgN7aA9LpalnzaxZoRRF0f9SgrqKBywfc61F37f9ealluQN3Zl7zFWnOHW9iNetExIEGpELq-35_cSnVYuBa5m3Sqd8fmLMG6RYr8oSPF8LRzCkJfdfzLe8m4VmvGWW6WQoeFIT9heu7JaE3tfyJfZPQmVjOMI8QeLYC73foGxZkx6Gc6POeCKy4OBvoD7O-r40IjyPc0_VGC6bg26cMx2iZKqwzW4EH3hI0pQwpjsJUQG9WWLN6zgTBinK2Nv6qsNt19syIIMxCtMIHUirUueoU_QbFjgSwelygyQHTWJ8i1QAlOlCMVpMlSjgcQZBqjcz5XrIFfFvE0x4GeqJqh0KiQEYiHuVVef81i39OpIKxTvnt27egUpVx_1MGVjdMA9Uqx1l8rHLXig9ZX2sN6lpf96HWesd5KNHvJCB0r9CMJ_uYZHxA84FteJqlENMDEccGoVcnnBPoiATOSTTZ7wWHE1XzV8PCEkFfVdoFeoxsKZHdqtl15MPXCD0c96ThP3qN_4oEeXtWKSwTKO45tCI09pJCZ2VrC97oIw9aGtqyfipFpQIz4AcvTRFqjsx1ySlT4Pdz1VFvhRlnERXJL5Pw71SqUgL10PJh2RDSff-wI7mATl_3IFyf6Ms9LGxMDpgpdA856itRr6vaUVkuKprzIE0ImEAvxfG5-lV-p5X__sts9Sp2AKdwtYfXAu61gN62nzj6kuKYqiM0otyflyUre6YtCu2koX0tMAAB6HC428tG1zT5bnsQOHjUB1V2C7eW2Ht5uTRQSHobuHuDXXmU6XoUTZ3t0N_WxulUJRi2EyzhOpZQdy6gKSB8ODKuXEftruQ5iFMJNX53vlYabrbZ7vYeblgEHc-Frutn_dppKtpWuyt0E6xKVvsJrMWBXDnarw0V3gjnH8xCvd6vQJEP--dhfi8zLx8O8_HwPB7lw9F56OXDQc5lFtxm7l7QWbmDVchZucsgH9v5fCFgZYI_1safRK6NH3A9NCc-8Qx3c9xtEDhNQi_3Wx2lIgmcBlAellEUOdpmQ9Mym873mMEGqdyoYNVvuueR2UXydpFcUS4rL7ZdVsNpAm4DsK0iAt0NsLPPDXEO02kaQeM0TPpNkymHK41x2JcVK7fy3tEdUrzzarDdDvfbYaf6tKvNuDdnBjdnvJszw5szo5szlpW_meuoXb7a63j_Bu7cwN0b-OAG7hUP1jo8bIdHrTA0YStstcN2ARtdI4ErGtPQGL8Y2T9B-LcYkginsTJOXQOniq-OLDDG2T8mI80eM3OK4SGbnMHTvw2djA8=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 L-040-130_Stage_Product_for_Appropriate_Zone_Moves_-_PTP — L-040-130_Stage_Product_for_Appropriate_Zone_Moves_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 2 | **Gateways**: 0

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
        n1["Move Product from Goods Receipt Area"]
        n2["Stage the Products in Appropriate Zone- Label or Putaway Area"]
        n3(["fa:fa-play Movement for Putaway is Initated"])
        n4(["fa:fa-stop Product Movement is Completed"])
    end
    n3 --> n1
    n1 --> n2
    n2 --> n4
    class n3 startEvt
    class n4 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVNuK2zAQ_RXhJbgFB3yNUz8UEicuC126NNsutOmDYo8TsbZkJDmXhvx7R7lvln2qH4LnZM45MyOPtlYuCrASq9PZMs50Qra2XkANdkLsGVVgO-QA_KSS0VkFyjY5peB6wv7u07ywWZs0g2W0ZtXGoBOYCyA_7h0yQGLlEEW56iqQrLQdu5GspnKTikpIk30H_dIt927Hv4ZCFiAvCa4be3mE1IpxuMBBHMZhZngKcsGLV6JlVPbL3N6Z4iqxyhdU6n35rYIHun5mhV5gXNJKAeYsdF19pTOoTI9atgbLW7k8DYMp48NxYJOG5ozPEQ9dhCTlLxcocnc7sut0pvxsSp5GU07wySuq1AhKojTC46UmJauq5C5MB1nkOkpL8QLJnT-OR4Hv5KaTBFt3HTPc7grYfKGTmaiKY2p3ZXpI_GbtyHXiu47c4O-NF_Di4pT2_L7fPzsNYy_10pNTWZb_5YRzlU9UvRy9xkHmZ6Ozlxf1otR9q3dqcxTGA-92TiCXLIcr0SzLgvFlVONe5Lnviw6zoOemN6JzqmFFNxfBT2l4FsyiOPPidwUPfrdVtrNHKfKTYDCOsugsGA-9bOC_KxgOvLB_rBB15pI2C_JMJSwEjpN8a0BSLeQhwTzc-z21HsQSCHoWbY4nK0VNvghRKPIdcmCNxqUDOrX-XLF8ZE00nQPBfT5RFWGcDJpGClw7nAr5JTh0yX4LiJDksdXUTOqtXPAB9UqalLTbVJhhCqqBYzFXNKbIPd4qKFwg--MVPbzQlRbNuZWzDFJTUTcVvOLip3x44QHpdj_jLI6hdwj9Y-gfwvDqnAzltHWv4PC4IJZj1SBrygor2Vr7Sw8vxgJK2lba2jkWbbWYbHhuJfvLwWqbAjsbMYpnVh_A3T-UabVz" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.9 L-040-150_Transport_Product_to_Storage_-_PTP — L-040-150_Transport_Product_to_Storage_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 3 | **Gateways**: 0

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
        n1["fa:fa-user Assign Resource to Move Physical Boxes to Putaway Storage Bins"]
        n2["fa:fa-user Track Resource via SAP Monitor"]
        n3["Transport Physical Boxes to Putaway Storage Bins"]
        n4(["fa:fa-play Transportation of Stock is Initiated"])
        n5(["fa:fa-stop Transportation of Stock is Completed"])
    end
    n4 --> n1
    n1 --> n3
    n3 --> n2
    n2 --> n5
    class n1 userTask
    class n2 userTask
    class n4 startEvt
    class n5 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqllE2P2jAQhv-KlRVKKwUpn4TmUAkCkVbqqqhsu4fSg0lsYmHsyHZYKOK_1yaBAO320OaAmJeZ550ZYh-snBfISqxe70AYUQk42KpEG2QnwF5CiWwHNMI3KAhcUiRtk4M5U3Py85TmhdXOpBktgxtC90adoxVH4OujA0a6kDpAQib7EgmCbceuBNlAsU855cJkP6AhdvHJrf1pzEWBRJfgurGXR7qUEoY6OYjDOMxMnUQ5Z8UNFEd4iHP7aJqj_DUvoVCn9muJnuDuhRSq1DGGVCKdU6oN_QSXiJoZlaiNltdie14GkcaH6YXNK5gTttJ66GpJQLbupMg9HsGx11uwiyl4niwY0E9OoZQThIFUWp5uFcCE0uQhTEdZ5DpSCb5GyYM_jSeB7-RmkkSP7jpmuf1XRFalSpacFm1q_9XMkPjVzhG7xHcdsdefd16IFZ1TOvCH_vDiNI691EvPThjj_3LSexXPUK5br2mQ-dnk4uVFgyh1f-edx5yE8ci73xMSW5KjK2iWZcG0W9V0EHnu29BxFgzc9A66ggq9wn0H_JCGF2AWxZkXvwls_O67rJczwfMzMJhGWXQBxmMvG_lvAsORFw7bDjVnJWBVghcoUMn1OsHnCgmouGgSzMO87wsLwwTDvtk3GElJVgx8QZLXIkdAcfDEtwjMyr0kOaRgzHdIGnlWK2jmnmseXCEwJkwurB9XaP8W_Sxgvu7IWwLBfDTTeH1V6JZuSgNdqvOZrLh-4f_FPHx3ca-ozrzQoCKcAY5Nre6HSPCoGyD6Xyw04f0VIuoQUvHqb4iUbyqKbhD6oDRfWAj6_Y96023oNWHQhkET-m3oN2F09VKYkvNhuJH9P8vh5UK4kaP27FqOtUFiA0lhJQfrdB_rO7tAGNZUWUfHgrXi8z3LreR0b1l1VejtTAjUr9OmEY-_AN6S6J4=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.10 L-040-170_Record_Stock_Location_-_PTP — L-040-170_Record_Stock_Location_-_PTP

**Swim Lanes**: Warehouse Operator | **Tasks**: 4 | **Gateways**: 0

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
        n1["fa:fa-user Verify Stock in Storage bin via SAP Monitor"]
        n2["fa:fa-user Record Storage Bin Location of Material via Label"]
        n3["fa:fa-user Update Inventory and Check Stock Storage Location in S/4 System"]
        n4[["fa:fa-cog Update Putaway Task Confirmation in Inbound Delivery"]]
        n5(["fa:fa-stop Inbound Delivery is Completed"])
        n6["Confirm/ Adjust Location"]
    end
    n6 --> n4
    n4 --> n2
    n2 --> n1
    n1 --> n3
    n3 --> n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 endEvt
    class n6 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlld9vmzAQx_8Vi6rKJhGVnyHjYVJCglRp1aql3R7WPThwTryCjWyTllX532cDIUnXPo2HiDvuPt-7iw9erIznYMXW5eULZVTF6GWktlDCKEajNZYwslHn-I4FxesC5MjEEM7Uiv5pw9ygejZhxpfikhaN8a5gwwHdX9tophMLG0nM5FiCoGRkjypBSyyahBdcmOgLmBKHtGr9ozkXOYhjgONEbhbq1IIyOLr9KIiC1ORJyDjLz6AkJFOSjfamuII_ZVssVFt-LeEGP_-gudpqm-BCgo7ZqrL4gtdQmB6VqI0vq8XuMAwqjQ7TA1tVOKNso_2Bo10Cs8ejK3T2e7S_vHxggyi6WzwwpK-swFIugCCptHu5U4jQoogvgmSWho4tleCPEF94y2jhe3ZmOol1645thjt-ArrZqnjNi7wPHT-ZHmKverbFc-w5tmj07ystYPlRKZl4U286KM0jN3GTgxIh5L-U9FzFHZaPvdbST710MWi54SRMnH95hzYXQTRzX88JxI5mcAJN09RfHke1nISu8z50nvoTJ3kF3WAFT7g5Aj8lwQBMwyh1o3eBnd7rKuv1reDZAegvwzQcgNHcTWfeu8Bg5gbTvkLN2QhcbdEPLGDL9TjR1woEVlx0AeZi7s8Hi-CY4LGZN_pudqpBK8WzR0SZuRF4A2it73cUo9XsFt1wvdwaYv064XjnnG96gUQ-pM91-heeYUU5Q5ygGz00s8kts12Tc5p_Truvcp2ArtkOmCY2CLMcJVvQNXaVHnQGDVP6VYBWjVRQnrODnwM845sD-7ZW2PyN7eFIOCNUlAPqmq15rSUXUNAdiEYDT4nhh4EoFa_-CUdUamRZFaAg17kfT3InOrWXu0Kz_Hct1dDFULdeuu6GTdB4_Fn30JtBZ3q96XVmf-6Z25l-b_qdGZ6cNxNz2LMzt_e223_bHZyu1tmTsH9hnDknwxvLsq0S9KBpbsUvVvtt0N-PHAiuC2XtbQvXiq8alllx-w616vbfWlCsj3bZOfd_AciYFAI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Warehouse Operator | L-040-030_Manage_Receiving_Manifest_-_PTP, L-040-040_Prioritize_Receipts_-_PTP, L-040-050_Assign_Trucks_to_Docks_-_PTP, L-040-080_Record_Receipt_and_Create_Tracking_Label_-_PTP, L-040-090_Assign_Batch_Tracking_Number_-_PTP, L-040-110_Build_Pallet_-_PTP, L-040-120_Determine_Put-away_Location_-_PTP, L-040-130_Stage_Product_for_Appropriate_Zone_Moves_-_PTP, L-040-150_Transport_Product_to_Storage_-_PTP, L-040-170_Record_Stock_Location_-_PTP | |
| Procurement Agent | L-040-040_Prioritize_Receipts_-_PTP,  | |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for L-040. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
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
| PTPR1530_IP | Report | Develop a custom report in SAP S/4 HANA for auto PR to PO conversion failures... | 10. Object Complete |  |  | 03.Medium |
| PTPR1530_IF | Report | Develop a custom report in SAP S/4 HANA for auto PR to PO conversion failures... | 10. Object Complete |  |  | 04.Low |
| LOGR0856 | Report | Capital Call Ahead GAP Report​ | 10. Object Complete |  |  | 03.Medium |
| PTPM0008 | Conversion | Quality Info record upload [T-Code - QI01] | 10. Object Complete |  |  | N/A |
| PTPM0007 | Conversion | Inspection Plan upload [T-Code - QP01] | 10. Object Complete |  |  | N/A |
| PTPM0006 | Conversion | Master Inspection Characteristics upload [T-Code - QS21] | 10. Object Complete |  |  | N/A |
| PTPC0808_IP | Conversion | 2379_Master Data Migration from ECC to S/4 to bring Approved Manufacturer Par... | 10. Object Complete |  |  | 03.Medium |
| PTPC0808_IF | Conversion | 2379_Master Data Migration from ECC to S/4 to bring Approved Manufacturer Par... | 10. Object Complete |  |  | 04.Low |
| PTPC0633 | Conversion | Purchase Requisition Conversion from ECC to S/4 - IF | 10. Object Complete |  |  | 02.High |
| PTPC0537_IP | Conversion | Purchasing Info Records Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA | NA | 03.Medium |
| PTPC0537_IF | Conversion | Purchasing Info Records Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA | NA | 03.Medium |
| PTPC0536_IP | Conversion | Source List Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA | NA | 03.Medium |
| PTPC0536_IF | Conversion | Source List Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA | NA | 03.Medium |
| PTPC0509_IP | Conversion | Open Contracts Migration from ECC to S/4 - IF and IP | 10. Object Complete |  |  | 01.Very High |
| PTPC0509_IF | Conversion | Open Contracts Migration from ECC to S/4 - IF and IP | 10. Object Complete |  |  | 01.Very High |
| PTPC0504_IP | Conversion | Quota Arrangement Migration from ECC to S/4 - IF and IP | 10. Object Complete |  |  | 03.Medium |
| PTPC0504_IF | Conversion | Quota Arrangement Migration from ECC to S/4 - IF and IP | 10. Object Complete |  |  | 03.Medium |
| PTPC0176_IP | Conversion | Open PO conversion from Legacy to SAP S/4 | 10. Object Complete | ECC | S4 | 02.High |
| PTPC0176_IF | Conversion | Open PO conversion from Legacy to SAP S/4 | 10. Object Complete | ECC | S4 | 03.Medium |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for L-040.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for L-040.

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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| PTPW0367_IP | Workflow | Workflow for Email Functionality and Notification to PO approver(IP) | 10. Object Complete | NA → NA | NA | 02.High |
| PTPW0367_IF | Workflow | Workflow for Email Functionality and Notification to PO approver(IF) | 10. Object Complete | NA → NA | NA | 02.High |
| PTPW0366_IP | Workflow | Workflow to trigger PO approvals in S4_IF | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPW0366_IF | Workflow | Workflow to trigger PO approvals in S4_IF | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPW0363_IP | Workflow | Workflow for Email Functionality and Notification to PR approver - IF | 10. Object Complete | NA → NA | NA | 02.High |
| PTPW0363_IF | Workflow | Workflow for Email Functionality and Notification to PR approver - IF | 10. Object Complete | NA → NA | NA | 02.High |
| PTPW0362_IP | Workflow | Workflow to Trigger PR approvals in S/4 – IF | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPW0362_IF | Workflow | Workflow to Trigger PR approvals in S/4 – IF | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPR1530_IP | Report | Develop a custom report in SAP S/4 HANA for auto PR to PO conversion failures... | 10. Object Complete |  | NA | 03.Medium |
| PTPR1530_IF | Report | Develop a custom report in SAP S/4 HANA for auto PR to PO conversion failures... | 10. Object Complete |  | NA | 04.Low |
| PTPM0008 | Conversion | Quality Info record upload [T-Code - QI01] | 10. Object Complete |  | NA | N/A |
| PTPM0007 | Conversion | Inspection Plan upload [T-Code - QP01] | 10. Object Complete |  | NA | N/A |
| PTPM0006 | Conversion | Master Inspection Characteristics upload [T-Code - QS21] | 10. Object Complete |  | NA | N/A |
| PTPI1689 | Interface | New custom API needed to process GET and DELETE function for Document Info Re... | 10. Object Complete |  | Apigee | 03.Medium |
| PTPI1657 | Interface | Interface to send Invoice PAID Status from CFIN to IP | 10. Object Complete |  | NA | 03.Medium |
| PTPI1533 | Interface | Pay@accept – Inbound Interface to fetch the values from FCE ODS to SAP S/4 HA... | 10. Object Complete |  | APIGEE | 03.Medium |
| PTPI1529_IP | Interface | An interface to retrieve the list of approvers from a custom MDG table(MDG sy... | 10. Object Complete |  | NA | 04.Low |
| PTPI1529_IF | Interface | An interface to retrieve the list of approvers from a custom MDG table(MDG sy... | 10. Object Complete |  | NA | 04.Low |
| PTPI1458 | Interface | Develop an interface between PEGA and S/4 HANA system to transmit MSL informa... | 10. Object Complete |  | MULESOFT | 03.Medium |
| PTPI1428_IP | Interface | Setting Up Inbound Interface from SPT tool/GTT(Global Trade and Tax) system t... | 10. Object Complete |  → S/4 | APIGEE | 04.Low |
| PTPI1428_IF | Interface | Setting Up Inbound Interface from SPT tool/GTT(Global Trade and Tax) system t... | 10. Object Complete |  → S/4 | APIGEE | 03.Medium |
| PTPI1331_IP | Interface | Ariba POs Goods Receipts to be sent from WIINGS to S/4 for R4 sites | 10. Object Complete | WIINGS → S/4 | MULESOFT | 03.Medium |
| PTPI1331_IF | Interface | Ariba POs Goods Receipts to be sent from WIINGS to S/4 for R4 sites | 10. Object Complete | WIINGS → S/4 | MULESOFT | 04.Low |
| PTPI1329_IP | Interface | FSD to change Purchase Order information from B2B Staging DB ePO from S4 IP | 10. Object Complete | S/4 → Stagging DB | MULESOFT | 03.Medium |
| PTPI1329_IF | Interface | FSD to change Purchase Order information from B2B Staging DB ePO from S4 IF | 10. Object Complete | S/4 → Stagging DB | MULESOFT | 04.Low |
| PTPI1308_IP | Interface | FSD to publish SAP Contracts pricing condition details to Web Contract - IP | 10. Object Complete | S/4 → WebContract | MULESOFT | 03.Medium |
| PTPI1308_IF | Interface | FSD to publish SAP Contracts pricing condition details to Web Contract - IF | 10. Object Complete | S/4 → WebContract | MULESOFT | 04.Low |
| PTPI1307_IP | Interface | FSD to publish SAP Contracts changes details to Web Contract - IP | 10. Object Complete | S/4 → WebContract | MULESOFT | 03.Medium |
| PTPI1307_IF | Interface | FSD to publish SAP Contracts changes details to Web Contract - IF | 10. Object Complete | S/4 → WebContract | MULESOFT | 04.Low |
| PTPI1171 | Interface | Get Material details from IF to METs/SOM | 10. Object Complete | S/4 → METs/SOM | APIGEE | 03.Medium |
| PTPI1170 | Interface | Get Source List details from IF to METs/SOM | 10. Object Complete | METs/SOM → S/4 | APIGEE | 02.High |
| PTPI1169 | Interface | Read Outline Agreement (OA) from IF in METs/SOM app. | 10. Object Complete | S/4 → METs/SOM | APIGEE | 02.High |
| PTPI1168 | Interface | Get PO details from IF to METs/SOM | 10. Object Complete | S/4 → METs/SOM | APIGEE | 03.Medium |
| PTPI1167 | Interface | Maintain PR in IF from METs/SOM | 10. Object Complete | METs/SOM → S/4 | APIGEE | 03.Medium |
| PTPI1154 | Interface | ILM to SAP S4 Interface – Assigning Material to Inspection Plan | 10. Object Complete | ILM → S/4 | NA | 03.Medium |
| PTPI1153 | Interface | Interface from ILM to SAP S/4 - Create/Modify Quality Info records | 10. Object Complete | ILM → S/4 | NA | 03.Medium |
| PTPI1152 | Interface | Develop an interface to create PO/STO from IRIS Non-Standard Request to S/4 Hana | 10. Object Complete | IRIS → S/4 | APIGEE | 04.Low |
| PTPI1138 | Interface | This interface is required to trigger split account assigned Purchase Requisi... | 10. Object Complete | MySamples → S/4 | APIGEE | 03.Medium |
| PTPI1137_IP | Interface | Interface between S4 to Boundary Apps (Customs Tracker and PEGA-ISMQ) for rea... | 10. Object Complete | ILM → S/4 | MULESOFT | 02.High |
| PTPI1137_IF | Interface | Interface between S4 to Boundary Apps (Customs Tracker and PEGA-ISMQ) for rea... | 10. Object Complete | S/4 → Boundary Apps (Customs Tracker and PEGA-ISMQ | MULESOFT | 03.Medium |
| PTPI1134 | Interface | Inbound Interface from E2Open to IF – Intel Foundry in S/4 to bring shipping ... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| PTPI1128_IP | Interface | Interface to send Ariba PO closure status information from S4 to Ariba | 10. Object Complete | S/4 → SAP Ariba Network | NA | 03.Medium |
| PTPI1128_IF | Interface | Interface to send Ariba PO closure status information from S4 to Ariba | 10. Object Complete | S/4 → SAP Ariba Network | NA | 04.Low |
| PTPI1032 | Interface | MQCS data pull Interface | 10. Object Complete | MQCS → S/4 | MULESOFT | 03.Medium |
| PTPI0825 | Interface | Get Purchase Group details from IF to CWB | 10. Object Complete | S/4 → CWB | MULESOFT | 04.Low |
| PTPI0823 | Interface | Get Purchase Req Details from IF to CWB | 10. Object Complete | S/4 → CWB | APIGEE | 03.Medium |
| PTPI0822_IP | Interface | Ariba Invoice Integration through (CIG - Cloud Integration Gateway (Currently... | 10. Object Complete | SAP Ariba Network → S/4 | NA | 03.Medium |
| PTPI0822_IF | Interface | Ariba Invoice Integration through (CIG - Cloud Integration Gateway (Currently... | 10. Object Complete | SAP Ariba Network → S/4 | NA | 04.Low |
| PTPI0821_IP | Interface | Invoice Status Update from SAP S/4 to Ariba Network through CIG - Cloud Integ... | 10. Object Complete | S/4 → SAP Ariba Network | NA | 03.Medium |
| PTPI0821_IF | Interface | Invoice Status Update from SAP S/4 to Ariba Network through CIG - Cloud Integ... | 10. Object Complete | S/4 → SAP Ariba Network | NA | 04.Low |
| PTPI0820_IP | Interface | Carbon Copy Invoice Integration from SAP S/4 to Ariba Network | 10. Object Complete | S/4 → SAP Ariba Network | NA | 03.Medium |
| PTPI0820_IF | Interface | Carbon Copy Invoice Integration from SAP S/4 to Ariba Network | 10. Object Complete | S/4 → SAP Ariba Network | NA | 04.Low |
| PTPI0819_IP | Interface | Intel B2B – XML (3C7) Notify of Self Billing Invoice – Interface to send noti... | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| PTPI0819_IF | Interface | Intel B2B – XML (3C7) Notify of Self Billing Invoice – Interface to send noti... | 10. Object Complete | S/4 → OpenText | MULESOFT | 04.Low |
| PTPI0817_IP | Interface | Purchasing Services Fiori Catalog | 10. Object Complete | S/4 → Shopping@Intel | NA | 03.Medium |
| PTPI0817_IF | Interface | Purchasing Services Fiori Catalog | 10. Object Complete | S/4 → Shopping@Intel | NA | 04.Low |
| PTPI0816_IP | Interface | Intel WebSuite - Web PO – Interface to display Purchase Order information fro... | 10. Object Complete | Stagging DB → S/4 | MULESOFT | 03.Medium |
| PTPI0816_IF | Interface | Intel WebSuite - Web PO – Interface to display Purchase Order information fro... | 10. Object Complete | Stagging DB → S/4 | MULESOFT | 04.Low |
| PTPI0812_IP | Interface | Intel WebSuite - Web Forecast – Interface to display Purchase Order informati... | 10. Object Complete | Intel WebSuite Web Contract → S/4 | MULESOFT | 03.Medium |
| PTPI0812_IF | Interface | Intel WebSuite - Web Forecast – Interface to display Purchase Order informati... | 10. Object Complete | Intel WebSuite Web Contract → S/4 | MULESOFT | 04.Low |
| PTPI0735_IP | Interface | Ariba/Capital PO details to be retrieved from SAP S/4 at the time of receivin... | 10. Object Complete | WIINGS → S/4 | MULESOFT | 03.Medium |
| PTPI0735_IF | Interface | Ariba/Capital PO details to be retrieved from SAP S/4 at the time of receivin... | 10. Object Complete | WIINGS → S/4 | MULESOFT | 04.Low |
| PTPI0710_IP | Interface | S4 Manual Invoice Release Blocking functionality requires connection with GTT... | 10. Object Complete | S/4 → GTT (Custom Tracker) | NA | 03.Medium |
| PTPI0710_IF | Interface | S4 Manual Invoice Release Blocking functionality requires connection with GTT... | 10. Object Complete | S/4 → GTT (Custom Tracker) | NA | 04.Low |
| PTPI0709_IP | Interface | Ariba Asset Settlement Interface | 10. Object Complete | Shopping@Intel → S/4 | NA | 03.Medium |
| PTPI0709_IF | Interface | Ariba Asset Settlement Interface | 10. Object Complete | Shopping@Intel → S/4 | NA | 04.Low |
| PTPI0692_IP | Interface | Custom program to send configurations from S4 system to Illumis | 10. Object Complete | S/4 → Accounts Payable Recovery Tool | SFT | 03.Medium |
| PTPI0692_IF | Interface | Custom program to send configurations from S4 system to Illumis | 10. Object Complete | S/4 → Accounts Payable Recovery Tool | SFT | 04.Low |
| PTPI0691_IP | Interface | Custom program to send the supplier master data from S4 system to Illumis. | 10. Object Complete | S/4 → Accounts Payable Recovery Tool | SFT | 03.Medium |
| PTPI0691_IF | Interface | Custom program to send the supplier master data from S4 system to Illumis. | 10. Object Complete | S/4 → Accounts Payable Recovery Tool | SFT | 04.Low |
| PTPI0685 | Interface | Custom program to send the Transactions (Invoices) from IF system to Illumis | 10. Object Complete | S/4 → Accounts Payable Recovery Tool | SFT | 03.Medium |
| PTPI0671 | Interface | Interface to automatically create VMI PO & IB delivery in S/4 (IF and IP) via... | 10. Object Complete | S/4 → E2Open | MULESOFT | 02.High |
| PTPI0568 | Interface | Maintain Purchasing Info Record in IF from Pega PSI | 10. Object Complete | PEGA PSI → S/4 | APIGEE | 03.Medium |
| PTPI0567 | Interface | Get Material Master details from IF to Pega PSI | 10. Object Complete | S/4 → PEGA PSI | APIGEE | 02.High |
| PTPI0566 | Interface | Maintain Outline Agreement in IF from Pega PSI | 10. Object Complete | PEGA PSI → S/4 | APIGEE | 03.Medium |
| PTPI0559_IP | Interface | All Validation of Chemical purchases on non MRP PR by using integration betwe... | 10. Object Complete | ICHEM → S/4 | NA | 03.Medium |
| PTPI0559_IF | Interface | All Validation of Chemical purchases on non MRP PR by using integration betwe... | 10. Object Complete | ICHEM → S/4 | NA | 04.Low |
| PTPI0494 | Interface | Maintain PO in IF from CWB | 10. Object Complete | CWB → S/4 | APIGEE | 01.Very High |
| PTPI0473 | Interface | Demand Change - Automatic update of PR/PO/STR/STO/Scheduling agreement and Pr... | 06. Dev In Progress | NA → NA | Mulesoft | 02.High |
| PTPI0470 | Interface | Payment Proposal after invoice posted from SAP S/4 HANA CFIN to Ariba | 10. Object Complete | S/4 → SAP Ariba Network | NA | 03.Medium |
| PTPI0469 | Interface | Payment Remittance after payment posted from CFIN to IP/IF and from IP/IF to ... | 10. Object Complete | S/4 → SAP Ariba Network | NA | 03.Medium |
| PTPI0468 | Interface | Payment Status after payment is cancelled / Void from CFIN to IP / IF and Fro... | 10. Object Complete | S/4 → SAP Ariba Network | NA | 02.High |
| PTPI0467 | Interface | Maintain Outline Agreement in IF from EMS | 10. Object Complete | EMS → S/4 | APIGEE | 02.High |
| PTPI0466_IP | Interface | Payment Remittance after payment posted from CFIN to IP/IF for Readsoft | 10. Object Complete | S/4 → Readsoft | NA | 03.Medium |
| PTPI0466_IF | Interface | Payment Remittance after payment posted from CFIN to IP/IF for Readsoft | 10. Object Complete | S/4 → Readsoft | NA | 04.Low |
| PTPI0463_IP | Interface | GR Carbon Copy (Posted in S4) | 10. Object Complete | S/4 → SAP Ariba Network | NA | 02.High |
| PTPI0463_IF | Interface | GR Carbon Copy (Posted in S4) | 10. Object Complete | S/4 → SAP Ariba Network | NA | 03.Medium |
| PTPI0452 | Interface | Get Material Master alternate UOM details from IF to CWB | 10. Object Complete | S/4 → CWB | APIGEE | 02.High |
| PTPI0449 | Interface | Maintain Outline Agreement in IF from CWB | 10. Object Complete | CWB → S/4 | APIGEE | 01.Very High |
| PTPI0448 | Interface | Maintain Purchasing Info Record in IF from CWB | 10. Object Complete | CWB → S/4 | APIGEE | 02.High |
| PTPI0388_IP | Interface | Custom program to send the Purchase order from SAP S4 system to Illumis | 10. Object Complete | S/4 → Accounts Payable Recovery Tool | SFT | 02.High |
| PTPI0388_IF | Interface | Custom program to send the Purchase order from SAP S4 system to Illumis | 10. Object Complete | S/4 → Accounts Payable Recovery Tool | SFT | 03.Medium |
| PTPI0386 | Interface | Maintain Document Info Record in IF from CWB | 10. Object Complete | CWB → S/4 | APIGEE | 02.High |
| PTPI0384 | Interface | Create Document Info Record in IF from EMS | 10. Object Complete | Equipment Management System → S/4 | APIGEE | 02.High |
| PTPI0382 | Interface | Get OA determination by material from IF to CWB | 10. Object Complete | Commercial Workbench → S/4 | APIGEE | 02.High |
| PTPI0370 | Interface | Get OA determination by material from IF to EMS | 10. Object Complete | S/4 → Equipment Management System | APIGEE | 03.Medium |
| PTPI0369 | Interface | Develop an interface to send inventory reports and MRP parameters from S4(IF)... | 10. Object Complete | S/4 → E2Open | MULESOFT | 02.High |
| PTPI0368 | Interface | Automatic creation of Discrete PO & IB delivery when supplier initiates shipm... | 10. Object Complete | E2open → S/4 | MULESOFT | 02.High |
| PTPI0272 | Interface | Get Material Master details from IF to EMS | 10. Object Complete | S/4 → EMS | APIGEE | 02.High |
| PTPI0271 | Interface | Get Material Master details from IF to SIRFIS | 10. Object Complete | S/4 → SIRFIS | APIGEE | 02.High |
| PTPI0269_IP | Interface | Supplier Onboarding Data - IF | 10. Object Complete | Shopping@Intel → S/4 | NA | 03.Medium |
| PTPI0269_IF | Interface | Supplier Onboarding Data - IP | 10. Object Complete | Shopping@Intel → S/4 | NA | 04.Low |
| PTPI0269_CFIN | Interface | Supplier Onboarding Data - CFIN | 10. Object Complete | Shopping@Intel → S/4 | NA | 03.Medium |
| PTPI0266 | Interface | Get PO details from IF to EMS | 10. Object Complete | S/4 → EMS | APIGEE | 02.High |
| PTPI0263 | Interface | Maintain PR in IF from EMS | 10. Object Complete | EMS → S/4 | APIGEE | 02.High |
| PTPI0262 | Interface | Get PR details from IF to EMS | 10. Object Complete | S/4 → EMS | APIGEE | 03.Medium |
| PTPI0261 | Interface | Get PR details from IF to SIRFIS | 10. Object Complete | S/4 → SIRFIS | APIGEE | 03.Medium |
| PTPI0211_IP | Interface | Outbound interface to publish SAP Contracts details to Web Contract - IP | 10. Object Complete | S/4 → WebContract | MULESOFT | 03.Medium |
| PTPI0211_IF | Interface | Outbound interface to publish SAP Contracts details to Web Contract - IF | 10. Object Complete | S/4 → WebContract | MULESOFT | 04.Low |
| PTPI0144_IP | Interface | Interface from E2Open to S4 to publish supplier commits against Purchase Order | 10. Object Complete | E2Open → S/4 | MULESOFT | 02.High |
| PTPI0144_IF | Interface | Interface from E2Open to S4 to publish supplier commits against Purchase Order | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| PTPI0140_IP | Interface | Interface from S4 to E2Open to send SA delivery schedule lines | 10. Object Complete | S/4 → E2Open | MULESOFT | 02.High |
| PTPI0140_IF | Interface | Interface from S4 to E2Open to send SA delivery schedule lines | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| PTPI0138 | Interface | Interface from S4 to OpenText to send new purchase orders & purchase order ch... | 10. Object Complete | S/4 → GXS (Open text) | MULESOFT | 02.High |
| PTPI0136_IP | Interface | Interface from S4 to E2open to send new purchase orders, purchase order chang... | 10. Object Complete | S/4 → E2Open | MULESOFT | 02.High |
| PTPI0136_IF | Interface | Interface from S4 to E2open to send new purchase orders, purchase order chang... | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| PTPI0134_IP | Interface | Interface from S4 to E2Open for SIMS Master Data & supply demand elements | 10. Object Complete | S/4 → E2Open | MULESOFT | 02.High |
| PTPI0134_IF | Interface | Interface from S4 to E2Open for SIMS Master Data & supply demand elements | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| PTPI0133 | Interface | Get OA determination by material from IF to SIRFIS | 10. Object Complete | SIRFIS → S/4 | APIGEE | 03.Medium |
| PTPI0131 | Interface | Get Outline Agreement data from IF to SIRFIS | 10. Object Complete | SIRFIS → S/4 | APIGEE | 02.High |
| PTPI0111_IP | Interface | PO change (Custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 03.Medium |
| PTPI0111_IF | Interface | PO change (Custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 04.Low |
| PTPI0110 | Interface | Get PO details from IF to SIRFIS | 10. Object Complete | SIRFIS → S/4 | APIGEE | 02.High |
| PTPI0107_IP | Interface | PO Cancel | 10. Object Complete | SAP Ariba Network → S/4 | NA | 03.Medium |
| PTPI0107_IF | Interface | PO Cancel | 10. Object Complete | SAP Ariba Network → S/4 | NA | 04.Low |
| PTPI0103_IP | Interface | PO create (Custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 03.Medium |
| PTPI0103_IF | Interface | PO create (Custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 04.Low |
| PTPI0100_IP | Interface | PR Cancel | 10. Object Complete | SAP Ariba Network → S/4 | NA | 03.Medium |
| PTPI0100_IF | Interface | PR Cancel | 10. Object Complete | SAP Ariba Network → S/4 | NA | 04.Low |
| PTPI0098_IP | Interface | PR change (Custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 03.Medium |
| PTPI0098_IF | Interface | PR change (Custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 04.Low |
| PTPI0096_IP | Interface | PR creation (budget check, custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 03.Medium |
| PTPI0096_IF | Interface | PR creation (budget check, custom logic) | 10. Object Complete | SAP Ariba Network → S/4 | NA | 04.Low |
| PTPI0094_IP | Interface | validate and enrich (PR - master data and custom code) | 10. Object Complete | S/4 → SAP Ariba Network | MULESOFT | 03.Medium |
| PTPI0094_IF | Interface | validate and enrich (PR - master data and custom code) | 10. Object Complete | S/4 → SAP Ariba Network | MULESOFT | 04.Low |
| PTPI0092_IP | Interface | Transfer of Ownership (change Ariba PR/PO) | 10. Object Complete | S/4 → SAP Ariba Network | APIGEE | 03.Medium |
| PTPI0092_IF | Interface | Transfer of Ownership (change Ariba PR/PO) | 10. Object Complete | S/4 → SAP Ariba Network | APIGEE | 04.Low |
| PTPI0018 | Interface | SAP S4 IF Boundary App Interface for updating Requested Dock Date (RDD) for C... | 10. Object Complete | S/4 → SIRFIS | APIGEE | 03.Medium |
| PTPI0017 | Interface | SAP S4 IF Boundary App Interface for updating POChange/PODeliveryDates - PO S... | 10. Object Complete | S/4 → SIRFIS | APIGEE | 02.High |
| PTPF1384 | Form | Exception Notification – Label printing functionality – IF only | 10. Object Complete |  | NA | 03.Medium |
| PTPF0014_IP | Form | PO Output Form Customization - IP | 10. Object Complete | NA → NA | NA | 02.High |
| PTPF0014_IF | Form | PO Output Form Customization - IF | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE1700 | Enhancement | Enhancement required in the purchase order (change only) to validate if the u... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1699 | Enhancement | Enhancement required in the purchase requisition (change only) to validate if... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1687 | Enhancement | Automate Warranty Credit Memo Posting | 10. Object Complete |  | NA | 03.Medium |
| PTPE1656 | Enhancement | Enhancement to Update Invoice PAID Status from CFIN to IF & IP ARIBA Standard... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1644 | Enhancement | New Enhancement required for to make PO price updates for HVM OSAT and SIFO o... | 06. Dev In Progress |  | NA | 02.High |
| PTPE1628_IP | Enhancement | INT-CR0941-Develop a custom enhancement in SAP S/4 for Subcon PO BOM comparis... | 08. FUT In Progress |  | NA | 04.Low |
| PTPE1628_IF | Enhancement | INT-CR0941-Develop a custom enhancement in SAP S/4 for Subcon PO BOM comparis... | 08. FUT In Progress |  | NA | 03.Medium |
| PTPE1622 | Enhancement | Enhancement to update Purchase document amount into USD when BAPP pull data f... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1621 | Enhancement | Enhancement to deleting all entries from ESH_SR_LTXT and ESH_SR_TXT_OBJ, runn... | 10. Object Complete |  | NA | 04.Low |
| PTPE1606_IP | Enhancement | Custom enhancement to edit the posted accounting document for Payment Term, B... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1606_IF | Enhancement | Custom enhancement to edit the posted accounting document for Payment Term, B... | 10. Object Complete |  | NA | 04.Low |
| PTPE1606_CFIN | Enhancement | Custom enhancement to edit the posted accounting document for Payment Term, B... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1603 | Enhancement | Enhancement to Auto block the Expired Batches in IM Locations | 10. Object Complete |  | NA | 03.Medium |
| PTPE1532 | Enhancement | Enhancement required in the purchase order (change only) to validate if the u... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1531 | Enhancement | Enhancement required in the purchase requisition (change only) to validate if... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1495_IP | Enhancement | Enhancement required for ORDERS05 IDOC applicable for PO outbound from S4 to ... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1495_IF | Enhancement | Enhancement required for ORDERS05 IDOC applicable for PO outbound from S4 to ... | 10. Object Complete |  | NA | 04.Low |
| PTPE1494_IP | Enhancement | Enhancement to trigger Output type which will generate IDOC once GR or GR rev... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1494_IF | Enhancement | Enhancement to trigger Output type which will generate IDOC once GR or GR rev... | 10. Object Complete |  | NA | 04.Low |
| PTPE1465_IP | Enhancement | Enhancement to Get Purchase order details like Payee, Supnam, Purchase group ... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1465_IF | Enhancement | Enhancement to Get Purchase order details like Payee, Supnam, Purchase group ... | 10. Object Complete |  | NA | 04.Low |
| PTPE1452_IP | Enhancement | Enhancement to create AMPL (Approved manufacturer part list ) in S/4 using ex... | 10. Object Complete |  | NA | 02.High |
| PTPE1452_IF | Enhancement | Enhancement to create AMPL (Approved manufacturer part list ) in S/4 using ex... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1440_IP | Enhancement | Custom program to generate a PDF printout of SAP self-billing invoices (ERS/C... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1440_IF | Enhancement | Custom program to generate a PDF printout of SAP self-billing invoices (ERS/C... | 10. Object Complete |  | NA | 04.Low |
| PTPE1437_IP | Enhancement | Enhancement required to populate custom logic for BLAORD (PTPI0211_IP_IF). | 10. Object Complete |  | NA | 03.Medium |
| PTPE1437_IF | Enhancement | Enhancement required to populate custom logic for BLAORD (PTPI0211_IP_IF). | 10. Object Complete |  | NA | 04.Low |
| PTPE1436_IP | Enhancement | Enhancement required to populate custom logic for BLAOCH (PTPI0211_IP_IF). | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| PTPE1436_IF | Enhancement | Enhancement required to populate custom logic for BLAOCH (PTPI0211_IP_IF). | 99. Rejected/Cancelled/On Hold |  | NA | 04.Low |
| PTPE1424_IP | Enhancement | Enhancement for I-chem PR creation from Ariba until R5 go-live | 10. Object Complete |  | NA | 03.Medium |
| PTPE1424_IF | Enhancement | Enhancement for I-chem PR creation from Ariba until R5 go-live | 10. Object Complete |  | NA | 04.Low |
| PTPE1422_IP | Enhancement | Enhancement to Update Invoice PAID Status from CFIN to IF & IP ARIBA Standard... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1422_IF | Enhancement | Enhancement to Update Invoice PAID Status from CFIN to IF & IP ARIBA Standard... | 10. Object Complete |  | NA | 04.Low |
| PTPE1343 | Enhancement | Enhancement required to maintain the list of approved suppliers for copper ma... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1195_IP | Enhancement | Enhancement to auto close Purchase Orders based on policy criteria , executed... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1195_IF | Enhancement | Enhancement to auto close Purchase Orders based on policy criteria , executed... | 10. Object Complete |  | NA | 04.Low |
| PTPE1139_IP | Enhancement | Custom Enhancements for Payment Proposal, payment remittance, payment status,... | 10. Object Complete |  | NA | 04.Low |
| PTPE1139_IF | Enhancement | Custom Enhancements for Payment Proposal, payment remittance, payment status,... | 10. Object Complete |  | NA | 04.Low |
| PTPE1139_CFIN | Enhancement | Custom Enhancements for Payment Proposal, payment remittance, payment status,... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1135_IP | Enhancement | Enhancement required while triggering the COND_A idoc for contracts (PTPI0211... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1135_IF | Enhancement | Enhancement required while triggering the COND_A idoc for contracts (PTPI0211... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1133 | Enhancement | Enhancement to Get Purchase group email address details from IF system to CWB. | 10. Object Complete |  | NA | 04.Low |
| PTPE1120 | Enhancement | Enhancement required to automatically create and change subcon purchase requi... | 10. Object Complete |  | NA | 04.Low |
| PTPE1107 | Enhancement | Enhancement required to automatically create and change subcon purchase order... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1099 | Enhancement | Exception Notification – Label printing functionality – IF only | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE1050_IP | Enhancement | BADI Enhancement for PR PO Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| PTPE1050_IF | Enhancement | BADI Enhancement for PR PO Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| PTPE1049_IP | Enhancement | Enhancement to create custom field on Purchase Order Header Table to store Ap... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1049_IF | Enhancement | Enhancement to create custom field on Purchase Order Header Table to store Ap... | 10. Object Complete |  | NA | 03.Medium |
| PTPE1036 | Enhancement | Batch update Program | 10. Object Complete |  | NA | 03.Medium |
| PTPE1033 | Enhancement | UD Enhancement | 10. Object Complete |  | NA | 03.Medium |
| PTPE1031 | Enhancement | Send email notification with details of task for Quality notification – IF only | 10. Object Complete |  | NA | 03.Medium |
| PTPE1030 | Enhancement | Creation of Return PO from Action box within Notification – IF only | 10. Object Complete |  | NA | 03.Medium |
| PTPE1029 | Enhancement | Creation of Notification as a follow up action with rejection codes – IF only | 10. Object Complete |  | NA | 02.High |
| PTPE1009 | Enhancement | Returns to 3PL | 99. Rejected/Cancelled/On Hold |  | NA | 04.Low |
| PTPE0977 | Enhancement | Develop app/transaction to Automate the stock from ‘Unrestricted/Blocked to Q... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0962 | Enhancement | Enhancement required to automatically create return purchase orders based on ... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0961 | Enhancement | Enhancement required to automatically create rework or repair and replacement... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0958_IP | Enhancement | Activating the Final Invoice Indicator at PO Level SAP S/4 HANA - IP | 10. Object Complete |  | NA | 03.Medium |
| PTPE0958_IF | Enhancement | Activating the Final Invoice Indicator at PO Level - SAP S/4 HANA - IF | 10. Object Complete |  | NA | 04.Low |
| PTPE0941_IP | Enhancement | Enhancement to capture material price from receiving plant in Intercompany STO. | 10. Object Complete |  | NA | 03.Medium |
| PTPE0941_IF | Enhancement | Enhancement to capture material price from receiving plant in Intercompany STO. | 10. Object Complete |  | NA | 04.Low |
| PTPE0919_IP | Enhancement | Enhancement to trigger Output type which will generate IDOC once GR or GR rev... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0919_IF | Enhancement | Enhancement to trigger Output type which will generate IDOC once GR or GR rev... | 10. Object Complete |  | NA | 04.Low |
| PTPE0826 | Enhancement | Enhancement required for FS-PTPI0017_IF, PTPI0018 to update the EKPO-VSART Field | 10. Object Complete |  | NA | 03.Medium |
| PTPE0790_IP | Enhancement | Enhancement to enrich or remove transactions from Intrastat arrival declarati... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0790_IF | Enhancement | Enhancement to enrich or remove transactions from Intrastat arrival declarati... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0745_IP | Enhancement | Quota Arrangement Mass Upload Tool Functionality IP | 10. Object Complete |  | NA | 02.High |
| PTPE0745_IF | Enhancement | Quota Arrangement Mass Upload Tool Functionality IF | 10. Object Complete |  | NA | 03.Medium |
| PTPE0744_IP | Enhancement | PIR Mass Upload Tool Functionality IP | 10. Object Complete |  | NA | 02.High |
| PTPE0744_IF | Enhancement | PIR Mass Upload Tool Functionality IF | 10. Object Complete |  | NA | 03.Medium |
| PTPE0743_IP | Enhancement | OA Mass Upload Tool Functionality IP | 10. Object Complete |  | NA | 02.High |
| PTPE0743_IF | Enhancement | OA Mass Upload Tool Functionality IF | 10. Object Complete |  | NA | 03.Medium |
| PTPE0733_IP | Enhancement | Enhancement to validate the user that creates/edits the PO cannot make themse... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0733_IF | Enhancement | Enhancement to validate the user that creates/edits the PO cannot make themse... | 10. Object Complete |  | NA | 04.Low |
| PTPE0732 | Enhancement | Pay@Accept Custom Program to release the invoice - SAP S/4 HANA IP and IF | 10. Object Complete |  | NA | 03.Medium |
| PTPE0731_IP | Enhancement | Enhancement on Goods Receipts created from S4 (IF-IP) to Ariba Network | 10. Object Complete |  | NA | 03.Medium |
| PTPE0731_IF | Enhancement | Enhancement on Goods Receipts created from S4 (IF-IP) to Ariba Network | 10. Object Complete |  | NA | 04.Low |
| PTPE0730_IP | Enhancement | PR and PO interface enhancements to support Ariba Asset Interface | 10. Object Complete |  | NA | 03.Medium |
| PTPE0730_IF | Enhancement | PR and PO interface enhancements to support Ariba Asset Interface | 10. Object Complete |  | NA | 04.Low |
| PTPE0729_IP | Enhancement | Enhancement - Transfer of ownership Interface | 10. Object Complete |  | NA | 03.Medium |
| PTPE0729_IF | Enhancement | Enhancement - Transfer of ownership Interface | 10. Object Complete |  | NA | 04.Low |
| PTPE0727_IP | Enhancement | Source List Data Mass Upload Tool Functionality IP | 10. Object Complete |  | NA | 02.High |
| PTPE0727_IF | Enhancement | Source List Data Mass Upload Tool Functionality IF | 10. Object Complete |  | NA | 03.Medium |
| PTPE0726_IP | Enhancement | Enhancement to validate enabled supplier details to trigger Ariba relevant in... | 10. Object Complete |  | NA | 04.Low |
| PTPE0726_IF | Enhancement | Enhancement to validate enabled supplier details to trigger Ariba relevant in... | 10. Object Complete |  | NA | 04.Low |
| PTPE0726_CFIN | Enhancement | Enhancement to validate enabled supplier details to trigger Ariba relevant in... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0707 | Enhancement | PR workflow Custom Table enhancement | 10. Object Complete |  | NA | 03.Medium |
| PTPE0706_IP | Enhancement | Enhancement to Post Goods Receipt for the converted Ariba Purchase Orders in ... | 10. Object Complete |  | NA | 02.High |
| PTPE0706_IF | Enhancement | Enhancement to Post Goods Receipt for the converted Ariba Purchase Orders in ... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0656_IP | Enhancement | Enhancement on Purchase Orders Created or Changed from Ariba to S4 (IF-IP) | 10. Object Complete |  | NA | 03.Medium |
| PTPE0656_IF | Enhancement | Enhancement on Purchase Orders Created or Changed from Ariba to S4 (IF-IP) | 10. Object Complete |  | NA | 04.Low |
| PTPE0606_IP | Enhancement | Enhancement to create idoc extension for payload header info to send data to ... | 10. Object Complete |  | NA | 02.High |
| PTPE0606_IF | Enhancement | Enhancement to create idoc extension for payload header info to send data to ... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0558_IP | Enhancement | Enhancements for chemical purchases on non MRP PR’s. | 10. Object Complete |  | NA | 03.Medium |
| PTPE0558_IF | Enhancement | Enhancements for chemical purchases on non MRP PR’s. | 10. Object Complete |  | NA | 04.Low |
| PTPE0543_IP | Enhancement | Enhancement required for ORDERS05 IDOC applicable for PO outbound from S4 to ... | 10. Object Complete |  | NA | 03.Medium |
| PTPE0543_IF | Enhancement | Enhancement required for ORDERS05 IDOC applicable for PO outbound from S4 to ... | 10. Object Complete |  | NA | 04.Low |
| PTPE0472_IP | Enhancement | Enhancement to map correct plant and user ID’s for Ariba PR replication in S4 | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0472_IF | Enhancement | Enhancement to map correct plant and user ID’s for Ariba PR replication in S4 | 10. Object Complete | NA → NA | NA | 04.Low |
| PTPE0471 | Enhancement | Review the auto reversal of payment documents, Reset clearing of invoice and ... | 99. Rejected/Cancelled/On Hold | NA → NA | NA | 02.High |
| PTPE0371_IP | Enhancement | Standard BTE for Manage Supplier Line items to add the PO and Supplier name -... | 10. Object Complete | NA → NA | NA | 04.Low |
| PTPE0371_IF | Enhancement | Standard BTE for Manage Supplier Line items to add the PO and Supplier name -... | 10. Object Complete | NA → NA | NA | 04.Low |
| PTPE0371_CFIN | Enhancement | Standard BTE for Manage Supplier Line items to add the PO and Supplier name -... | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0365 | Enhancement | Enhancement for populating DPAS data on Purchase Requisition (IF and IP) | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0318_IP | Enhancement | Custom program to block the vendor invoice based on the different business sc... | 10. Object Complete | NA → NA | NA | 04.Low |
| PTPE0318_IF | Enhancement | Custom program to block the vendor invoice based on the different business sc... | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0259_IP | Enhancement | Develop a routing logic to send Purchase Order to the Boundary apps from S/4 ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0259_IF | Enhancement | Develop a routing logic to send Purchase Order to the Boundary apps from S/4 ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0241_IP | Enhancement | Payment Term Mass change functionality in FBL1N Vendor Line item report | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0241_IF | Enhancement | Payment Term Mass change functionality in FBL1N Vendor Line item report | 10. Object Complete | NA → NA | NA | 04.Low |
| PTPE0202_IP | Enhancement | Develop a change utility for mass PR creation and change of purchase requisit... | 10. Object Complete | NA → NA | NA | 02.High |
| PTPE0202_IF | Enhancement | Develop a change utility for mass PR creation and change of purchase requisit... | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0200_IP | Enhancement | PO Mass Change - Upload Tool Functionality (IP) | 10. Object Complete | NA → NA | NA | 02.High |
| PTPE0200_IF | Enhancement | PO Mass Change - Upload Tool Functionality (IF) | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0090_IP | Enhancement | Attachment need to copy from PR to PO automatically | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPE0090_IF | Enhancement | Attachment need to copy from PR to PO automatically | 10. Object Complete | NA → NA | NA | 04.Low |
| PTPC0808_IP | Conversion | 2379_Master Data Migration from ECC to S/4 to bring Approved Manufacturer Par... | 10. Object Complete |  | NA | 03.Medium |
| PTPC0808_IF | Conversion | 2379_Master Data Migration from ECC to S/4 to bring Approved Manufacturer Par... | 10. Object Complete |  | NA | 04.Low |
| PTPC0633 | Conversion | Purchase Requisition Conversion from ECC to S/4 - IF | 10. Object Complete |  | NA | 02.High |
| PTPC0537_IP | Conversion | Purchasing Info Records Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPC0537_IF | Conversion | Purchasing Info Records Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPC0536_IP | Conversion | Source List Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPC0536_IF | Conversion | Source List Migration from ECC to S/4 – IF and IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| PTPC0509_IP | Conversion | Open Contracts Migration from ECC to S/4 - IF and IP | 10. Object Complete |  | NA | 01.Very High |
| PTPC0509_IF | Conversion | Open Contracts Migration from ECC to S/4 - IF and IP | 10. Object Complete |  | NA | 01.Very High |
| PTPC0504_IP | Conversion | Quota Arrangement Migration from ECC to S/4 - IF and IP | 10. Object Complete |  | NA | 03.Medium |
| PTPC0504_IF | Conversion | Quota Arrangement Migration from ECC to S/4 - IF and IP | 10. Object Complete |  | NA | 03.Medium |
| PTPC0176_IP | Conversion | Open PO conversion from Legacy to SAP S/4 | 10. Object Complete | ECC → S4 | NA | 02.High |
| PTPC0176_IF | Conversion | Open PO conversion from Legacy to SAP S/4 | 10. Object Complete | ECC → S4 | NA | 03.Medium |
| LOGW0978_IP | Workflow | Workflow for processing Goods Receipt and tracking and tracing of non-invento... | 10. Object Complete |  | NA | 03.Medium |
| LOGW0978_IF | Workflow | Workflow for processing Goods Receipt and tracking and tracing of non-invento... | 10. Object Complete |  | NA | 03.Medium |
| LOGR0856 | Report | Capital Call Ahead GAP Report​ | 10. Object Complete |  | NA | 03.Medium |
| LOGI1726 | Interface | GR replication for raw materials for Straddle Sites from ECC to S4 IP via ECA​ | 04. FS In Progress |  | MULESOFT | 03.Medium |
| LOGI1427_IP | Interface | Interface between S4 to Boundary Apps (PEGA-ISMQ) for real time data on Deliv... | 10. Object Complete | S/4 → PEGA | APIGEE | 03.Medium |
| LOGI1427_IF | Interface | Interface between S4 to Boundary Apps (PEGA-ISMQ) for real time data on Deliv... | 10. Object Complete | S/4 → PEGA | APIGEE | 04.Low |
| LOGI1309 | Interface | Inbound interface to receive Finished Goods Advanced Shipping notifications f... | 10. Object Complete | E2Open → S/4 | MULESOFT | 01.Very High |
| LOGI1206_IP | Interface | S4 sending 3B2 ASN information to supplier as outbound signal for return deli... | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| LOGI1206_IF | Interface | S4 sending 3B2 ASN information to supplier as outbound signal for return deli... | 10. Object Complete | S/4 → E2Open | MULESOFT | 04.Low |
| LOGI1136_IP | Interface | Interface between S4 to Boundary Apps (Customs Tracker) for real time data on... | 10. Object Complete | S/4 → Boundary Apps (Customs Tracker) | APIGEE | 04.Low |
| LOGI1136_IF | Interface | Interface between S4 to Boundary Apps (Customs Tracker) for real time data on... | 10. Object Complete | S/4 → Boundary Apps (Customs Tracker and PEGA-ISMQ | APIGEE | 03.Medium |
| LOGI1129 | Interface | TM: RICEFW 1:Carrier selection and Charges calculation for IRG/ISCG( Intel ro... | 10. Object Complete | IRG/IRSG → S/4 | MULESOFT | 03.Medium |
| LOGI0956 | Interface | Inbound interface to receive OSAT Finished Goods and Return rework FG “Goods ... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0955 | Interface | Inbound interface to receive Box CPU Finished Goods and Return Rework FG “Goo... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0954 | Interface | Bailment Process: Inbound 4B2 from 3PL to IF via OpenText for Receipt of Bail... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0953 | Interface | Bailment Process: Generated Outbound 4B2 from IF to OpenText for Bailed Material | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0852_IP | Interface | Outbound Interface to send freight forwarder rates from TM to CTSI. | 10. Object Complete | S/4 → CTSI | NA | 03.Medium |
| LOGI0852_IF | Interface | Outbound Interface to send freight forwarder rates from TM to CTSI | 10. Object Complete | S/4 → CTSI | NA | 04.Low |
| LOGI0834 | Interface | Inbound interface for WLA Hold scenario to trigger Outbound ASN with Non-Valu... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0755 | Interface | PTP-LE: ASN (Inbound 3B2) from SIFO Suppliers - E2Open to S/4 IP | 10. Object Complete | E2OPEN → S/4 | MULESOFT | 03.Medium |
| LOGI0753_IP | Interface | The process involves sending a Real time consumption signal from a supplier o... | 10. Object Complete | E2OPEN → S/4 | MULESOFT | 03.Medium |
| LOGI0749_IP | Interface | TM –CTSI integration – Freight details to CTSI for Liability validation | 10. Object Complete | S/4 → CTSI | SFT | 03.Medium |
| LOGI0749_IF | Interface | TM –CTSI integration – Freight details to CTSI for Liability validation | 10. Object Complete | S/4 → CTSI | SFT | 04.Low |
| LOGI0516_IP | Interface | PTP IF​Fetch Integrators rate in TM via an API call to Redwood and leverage i... | 10. Object Complete | ECD → S/4 | APIGEE | 03.Medium |
| LOGE0515_IF | Enhancement | TM : Fetch Integrators rate in TM via an API call to Redwood and leverage it ... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGI0516_IF | Interface | PTP IP​Fetch Integrators rate in TM via an API call to Redwood and leverage i... | 10. Object Complete | ECD → S/4 | APIGEE | 04.Low |
| LOGI0503_IP | Interface | Outboundinterface GR data send to NIT as WIINGS gets replaced by S4 | 10. Object Complete | S/4 → NIT | MULESOFT | 03.Medium |
| LOGI0503_IF | Interface | Outboundinterface GR data send to NIT as WIINGS gets replaced by S4 | 10. Object Complete | S/4 → NIT | MULESOFT | 04.Low |
| LOGI0502 | Interface | Inbound Interface to receive and process 4B2 Goods receipt signal from 3PL to... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0501 | Interface | Inbound interface to receive ASN (3B2) from fab material suppliers via E2Open... | 10. Object Complete | E2Open → S/4 | MULESOFT | 02.High |
| LOGI0267 | Interface | Inbound Interface to receive Advanced Shipment Notice (ASN) data in txt file ... | 10. Object Complete | GXS → S/4 | MULESOFT | 02.High |
| LOGI0253 | Interface | Inbound interface to receive Finished Goods Advanced Shipping notifications f... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0252 | Interface | Inbound interface to receive “Goods Receipt” (4B2) signal for Raw Materials/F... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0249 | Interface | Inbound interface to receive Realtime consumption (4B3) of raw materials/FG C... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0245 | Interface | Inbound interface to receive Finished Goods ASN (3B2) from BOX CPU subcontrac... | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| LOGI0244 | Interface | Inbound interface to receive ODM Finished Goods “Goods Receipt” (4B2) signal ... | 10. Object Complete | GSX → S/4 | MULESOFT | 03.Medium |
| LOGI0197_IP | Interface | Create Inbound Delivery Note from ASN in IP | 10. Object Complete | WebASN → S/4 | MULESOFT | 03.Medium |
| LOGI0197_IF | Interface | Create Inbound Delivery Note from ASN in IF | 10. Object Complete | WebASN → S/4 | MULESOFT | 04.Low |
| LOGI0163_IP | Interface | Inbound interface to receive consignment inventory adjustments (manual postin... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0163_IF | Interface | Inbound interface to receive consignment inventory adjustments (manual postin... | 10. Object Complete | E2Open → S/4 | MULESOFT | 04.Low |
| LOGI0161 | Interface | Inbound interface to receive ODM Finished Goods “Goods Receipt” (4B2) signal ... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0158 | Interface | Inbound interface to receive “Goods Receipt” (4B2) signal from OSATs for semi... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0157_IP | Interface | Inbound interface to receive raw materials “Goods Receipt” (4B2) signal for c... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0157_IF | Interface | Inbound interface to receive raw materials “Goods Receipt” (4B2) signal for c... | 10. Object Complete | E2Open → S/4 | MULESOFT | 04.Low |
| LOGI0156 | Interface | Outbound interface to send “Advanced Shipment Notification” signal (3B2) for ... | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| LOGI0155 | Interface | Inbound interface to receive Semi-Finished Goods Advanced Shipping notificati... | 10. Object Complete | E2Open → S/4 | MULESOFT | 02.High |
| LOGI0154 | Interface | Inbound interface to receive Finished Goods Advanced Shipping notifications f... | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| LOGI0150_IP | Interface | Outbound interface to send “Goods Receipt” signal (4B2) for Raw materials & O... | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| LOGI0150_IF | Interface | Outbound Interface to send 4B2 Goods receipt acknowledgement from S/4 to E2Op... | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| LOGF1085 | Form | Enhancement to print the Bin Location label in SAP EWM. | 10. Object Complete |  | NA | 03.Medium |
| LOGF1045 | Form | Goods Receipt Label Print triggered at the point of completion of the GR | 10. Object Complete |  | NA | 03.Medium |
| LOGF0920_IP | Form | Form for printing Goods receipt label in IM - IP | 10. Object Complete |  | NA | 02.High |
| LOGF0920_IF | Form | Form for printing Goods receipt label in IM - IF | 10. Object Complete |  | NA | 03.Medium |
| LOGE1728 | Enhancement | Automate Outbound delivery note creation for 250K annual Subcon POs for repai... | 04. FS In Progress |  | NA | 03.Medium |
| LOGE1570 | Enhancement | CR0856 - Enhancement required (a report) to post the goods receipt for the ad... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1506 | Enhancement | Enhancement to bring attachments of images from Material master (MM03) to the... | 10. Object Complete |  | NA | 02.High |
| LOGE1337 | Enhancement | Enhancement to generate outbound IDOC for 3B2 ASN information to RMA supplier... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1193_IP | Enhancement | S4 – Enhancement to stop GR for Purchase Order for which Delivery Completed i... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1193_IF | Enhancement | S4 – Enhancement to stop GR for Purchase Order for which Delivery Completed i... | 10. Object Complete |  | NA | 04.Low |
| LOGE1087 | Enhancement | Enhancement on the RF screen to auto populate the HU number for receiving. | 10. Object Complete |  | NA | 03.Medium |
| LOGE1086 | Enhancement | Enhancement on the RF screen for identifying the correct inbound delivery bas... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1048 | Enhancement | To Identify Priority Inbound Deliveries in EWM and display the details of the... | 10. Object Complete |  | NA | 02.High |
| LOGE1047 | Enhancement | RF Scanner -Inbound Process Screen to enhanced to show the Delivery Priority ... | 10. Object Complete |  | NA | 02.High |
| LOGE1046 | Enhancement | Enhancement to capture Priority Indicator field in EWM Inbound Delivery from ... | 10. Object Complete |  | NA | 02.High |
| LOGE1035 | Enhancement | Inventory update program for Stock type updates | 10. Object Complete |  | NA | 03.Medium |
| LOGE1034 | Enhancement | Delivery creation enhancement to update Stock type | 10. Object Complete |  | NA | 03.Medium |
| LOGE0976_IP | Enhancement | Enhancement to enable delivery priority Indicator in Inbound delivery Documen... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0976_IF | Enhancement | Enhancement to enable delivery priority Indicator in Inbound delivery Documen... | 10. Object Complete |  | NA | 04.Low |
| LOGE0952 | Enhancement | Generate Outbound 3B2 Message from S4 to OSAT supplier E2Open onboarded Suppl... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0858_IP | Enhancement | Determine mode in freight order and charge calculation​ | 10. Object Complete |  | NA | 03.Medium |
| LOGE0858_IF | Enhancement | Determine mode in freight order and charge calculation​ | 10. Object Complete |  | NA | 04.Low |
| LOGE0855 | Enhancement | Capital Call Ahead Report​ | 10. Object Complete |  | NA | 03.Medium |
| LOGE0854 | Enhancement | Custom Fiori Application development to generate Call Ahead Reports for Capit... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0853_IP | Enhancement | Inbound Carrier selection over-ride and exclusion rules to be considered duri... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0853_IF | Enhancement | Inbound Carrier selection over-ride and exclusion rules to be considered duri... | 10. Object Complete |  | NA | 04.Low |
| LOGE0851_IP | Enhancement | Enhancement to store + transform + trigger freight forwarder rates to CTSI. | 10. Object Complete |  | NA | 02.High |
| LOGE0851_IF | Enhancement | Enhancement to store + transform + trigger freight forwarder rates to CTSI. | 10. Object Complete |  | NA | 03.Medium |
| LOGE0850_IP | Enhancement | Order management for inbound ASN and Non ASN scenarios using automatic optimi... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0850_IF | Enhancement | Order management for inbound ASN and Non ASN scenarios using automatic optimi... | 10. Object Complete |  | NA | 04.Low |
| LOGE0849_IP | Enhancement | Introduce HAWB in Transportation Cockpit, FRO worklist and selection criteria... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0849_IF | Enhancement | introduce HAWB in Transportation Cockpit, FRO worklist and selection criteria... | 10. Object Complete |  | NA | 04.Low |
| LOGE0848_IP | Enhancement | Planning for inbound ASN, Non ASN. ODM/OSAT scenarios using automatic optimiz... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0848_IF | Enhancement | Planning for inbound ASN, Non ASN. ODM/OSAT scenarios using automatic optimiz... | 10. Object Complete |  | NA | 04.Low |
| LOGE0847 | Enhancement | TM: RICEFW 1:Carrier selection and Charges calculation for IRG/ISCG( Intel ro... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0769_IP | Enhancement | TM: Distribute the freight cost to R&D/OCOS/PCOS/Capital cost objects based o... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0769_IF | Enhancement | TM: Distribute the freight cost to R&D/OCOS/PCOS/Capital cost objects based o... | 10. Object Complete |  | NA | 04.Low |
| LOGE0768_IP | Enhancement | TM: Identify correct Company code, Purchase org, Purchase group, Virtual GLO ... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0768_IF | Enhancement | TM: Identify correct Company code, Purchase org, Purchase group, Virtual GLO ... | 10. Object Complete |  | NA | 04.Low |
| LOGE0767_IP | Enhancement | TM - GTT: GTT to S4 for IF and IP data split | 10. Object Complete |  | NA | 03.Medium |
| LOGE0767_IF | Enhancement | TM - GTT: GTT to S4 for IF and IP data split | 10. Object Complete |  | NA | 04.Low |
| LOGE0754_IP | Enhancement | Enhancement to enable Outbound Interface to send 4B2 Goods receipt acknowledg... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0754_IF | Enhancement | Enhancement to enable Outbound Interface to send 4B2 Goods receipt acknowledg... | 10. Object Complete |  | NA | 04.Low |
| LOGE0752_IP | Enhancement | TM: Auto-approve dispute doc for CTSI based invoices to update pass invoice c... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0752_IF | Enhancement | TM: Auto-approve dispute doc for CTSI based invoices to update pass invoice c... | 10. Object Complete |  | NA | 04.Low |
| LOGE0751_IP | Enhancement | TM: Shortcut planning and optimizer-based planning for Capital PO to perform ... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0751_IF | Enhancement | TM: Shortcut planning and optimizer-based planning for Capital PO to perform ... | 10. Object Complete |  | NA | 04.Low |
| LOGE0750_IP | Enhancement | TM: Update Pass invoice amount including prompt payment discount from CTSI to... | 10. Object Complete |  | NA | 01.Very High |
| LOGE0750_IF | Enhancement | TM: Update Pass invoice amount including prompt payment discount from CTSI to... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0665_IP | Enhancement | Calculation base and Associated charge calculation logic for field creation a... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0665_IF | Enhancement | Calculation base and Associated charge calculation logic for field creation a... | 10. Object Complete |  | NA | 04.Low |
| LOGE0655_IP | Enhancement | TM :PTP IP/IF​ - Weekly Milk run Charge calculation (Local Trucking)​ | 10. Object Complete |  | NA | 02.High |
| LOGE0655_IF | Enhancement | TM :PTP IP/IF​ - Weekly Milk run Charge calculation (Local Trucking)​ | 10. Object Complete |  | NA | 03.Medium |
| LOGE0515_IP | Enhancement | TM : Fetch Integrators rate in TM via an API call to Redwood and leverage it ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0450_IP | Enhancement | In SAP TM, Custom BRF+ and enhancement to populate the commodity code in the ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0450_IF | Enhancement | In SAP TM, Custom BRF+ and enhancement to populate the commodity code in the ... | 10. Object Complete | NA → NA | NA | 04.Low |
| PTPE1740 | Enhancement | Fair Market value Determination using custom code/logic during the replicatio... | 01. Pending Approval |  | NA | 02.High |

**Summary**: 3 Reports, 171 Interfaces, 16 Conversions, 171 Enhancements, 7 Forms, 10 Workflows

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for L-040:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for L-040:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (378 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 367 | 97.1% |
| 99. Rejected/Cancelled/On Hold | 4 | 1.1% |
| 06. Dev In Progress | 2 | 0.5% |
| 08. FUT In Progress | 2 | 0.5% |
| 04. FS In Progress | 2 | 0.5% |
| 01. Pending Approval | 1 | 0.3% |
| **Total** | **378** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 3 |
| Interface (I) | 171 |
| Conversion (C) | 16 |
| Enhancement (E) | 171 |
| Form (F) | 7 |
| Workflow (W) | 10 |
| **Total** | **378** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 6 |
| 02.High | 59 |
| 03.Medium | 213 |
| 04.Low | 97 |
| N/A | 3 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| PTPI0473 | 02.Interface | Demand Change - Automatic update of PR/PO/STR/STO/Scheduling agreement and Produ... | 06. Dev In Progress | 02.High |
| PTPE1644 | 04.Enhancement | New Enhancement required for to make PO price updates for HVM OSAT and SIFO orde... | 06. Dev In Progress | 02.High |
| PTPE1628_IP | 04.Enhancement | INT-CR0941-Develop a custom enhancement in SAP S/4 for Subcon PO BOM comparison ... | 08. FUT In Progress | 04.Low |
| PTPE1628_IF | 04.Enhancement | INT-CR0941-Develop a custom enhancement in SAP S/4 for Subcon PO BOM comparison ... | 08. FUT In Progress | 03.Medium |
| LOGI1726 | 02.Interface | GR replication for raw materials for Straddle Sites from ECC to S4 IP via ECA​ | 04. FS In Progress | 03.Medium |
| LOGE1728 | 04.Enhancement | Automate Outbound delivery note creation for 250K annual Subcon POs for repair/r... | 04. FS In Progress | 03.Medium |
| PTPE1740 | 04.Enhancement | Fair Market value Determination using custom code/logic during the replication o... | 01. Pending Approval | 02.High |

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

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>L-040 — Receive and Put-away Product - PTP</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*375 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| PTPW0367_IP | Workflow for Email Functionality and Notification to PO approver(IP) | Dec-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 1. On Track |
| PTPW0367_IF | Workflow for Email Functionality and Notification to PO approver(IF) | Dec-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 1. On Track |
| PTPW0366_IP | Workflow to trigger PO approvals in S4_IF | Dec-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 1. On Track |
| PTPW0366_IF | Workflow to trigger PO approvals in S4_IF | Dec-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 1. On Track |
| PTPW0363_IP | Workflow for Email Functionality and Notification to PR approver - IF | Sep-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| PTPW0363_IF | Workflow for Email Functionality and Notification to PR approver - IF | Sep-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| PTPW0362_IP | Workflow to Trigger PR approvals in S/4 – IF | Sep-24 (100%) | Aug-25 (100%) | Aug-25 (100%) | Dec-25 (100%) | 1. On Track |
| PTPW0362_IF | Workflow to Trigger PR approvals in S/4 – IF | Sep-24 (100%) | Aug-25 (100%) | Aug-25 (100%) | Dec-25 (100%) | 1. On Track |
| PTPR1530_IP | Develop a custom report in SAP S/4 HANA for auto PR to PO conversion failures instead in ECA – IP/IF | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| PTPR1530_IF | Develop a custom report in SAP S/4 HANA for auto PR to PO conversion failures instead in ECA – IP/IF | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| PTPM0008 | Quality Info record upload [T-Code - QI01] | May-25 (100%) | — | — | Jun-25 (100%) |  |
| PTPM0007 | Inspection Plan upload [T-Code - QP01] | May-25 (100%) | — | — | Jun-25 (100%) |  |
| PTPM0006 | Master Inspection Characteristics upload [T-Code - QS21] | May-25 (100%) | — | — | Jun-25 (100%) |  |
| PTPI1689 | New custom API needed to process GET and DELETE function for Document Info Record Object Link where boundary app CWB can perform GET and DELETE in S4. | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Jan-26 (100%) | 1. On Track |
| PTPI1657 | Interface to send Invoice PAID Status from CFIN to IP | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| PTPI1533 | Pay@accept – Inbound Interface to fetch the values from FCE ODS to SAP S/4 HANA IF | Sep-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| PTPI1529_IP | An interface to retrieve the list of approvers from a custom MDG table(MDG system) when a PR/PO creation or change workflow is triggered in S/4HANA.​ | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Dec-25 (100%) | 4. Completed |
| PTPI1529_IF | An interface to retrieve the list of approvers from a custom MDG table(MDG system) when a PR/PO creation or change workflow is triggered in S/4HANA.​ | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Dec-25 (100%) | 4. Completed |
| PTPI1458 | Develop an interface between PEGA and S/4 HANA system to transmit MSL information – IF | Jul-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 1. On Track |
| PTPI1428_IP | Setting Up Inbound Interface from SPT tool/GTT(Global Trade and Tax) system to S/4 IF and IP Systems | Jun-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 1. On Track |
| PTPI1428_IF | Setting Up Inbound Interface from SPT tool/GTT(Global Trade and Tax) system to S/4 IF and IP Systems | Jun-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 1. On Track |
| PTPI1331_IP | Ariba POs Goods Receipts to be sent from WIINGS to S/4 for R4 sites | May-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) | 1. On Track |
| PTPI1331_IF | Ariba POs Goods Receipts to be sent from WIINGS to S/4 for R4 sites | May-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) | 1. On Track |
| PTPI1329_IP | FSD to change Purchase Order information from B2B Staging DB ePO from S4 IP | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Dec-25 (100%) | 4. Completed |
| PTPI1329_IF | FSD to change Purchase Order information from B2B Staging DB ePO from S4 IF | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Dec-25 (100%) | 4. Completed |
| PTPI1308_IP | FSD to publish SAP Contracts pricing condition details to Web Contract - IP | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Nov-25 (100%) | 4. Completed |
| PTPI1308_IF | FSD to publish SAP Contracts pricing condition details to Web Contract - IF | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Nov-25 (100%) | 4. Completed |
| PTPI1307_IP | FSD to publish SAP Contracts changes details to Web Contract - IP | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Nov-25 (100%) | 4. Completed |
| PTPI1307_IF | FSD to publish SAP Contracts changes details to Web Contract - IF | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Nov-25 (100%) | 4. Completed |
| PTPI1171 | Get Material details from IF to METs/SOM | May-25 (100%) | Jul-25 (100%) | Jul-25 (100%) | Nov-25 (100%) | 4. Completed |

*... and 345 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

**Mapped sub-tower(s):** 6.2 PTP - Procurement, 6.3 PTP - EWM, 6.4 PTP - Logistics Management Inbound, 6.5 PTP - TM, 6.6 PTP - GTS, 6.7 PTP - Enable Payments, 6.8 PTP - QM

**RAID Summary:** 32 open items (4 capability-specific, 28 tower-level), 324 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 3 | 3 |
| P2 - Medium | 3 | 21 | 24 |
| P3 - Low | 1 | 3 | 4 |
| **Total** | **4** | **28** | **32** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03501 | Risk | P2 - Medium | PTPI0473 - DCR Interface from PDH to S/4 - Track development... | In Progress | B-Apps | 2026-03-27 |
| 03236 | Action | P2 - Medium | Assessment of IQC Solution mapping within Current QM Design ... | In Progress | PTP | 2026-03-27 |
| 03461 | Risk | P2 - Medium | PTP ECA DCM Process Changes and impacts to delivered self se... | In Progress | PTP | 2026-03-27 |
| 03373 | Risk | P3 - Low | incoterm location id value to be used for import requisition... | In Progress | PTP | 2026-05-01 |

**Other PTP Tower RAID Items** (28 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03681 | Risk | P1 - High | ITC Execution: Planning run availability - Prerequisite for ... | In Progress | E2E | 2026-03-27 |
| 03757 | Risk | P1 - High | IF Planning data not available in ITC1 until W4, leaving too... | In Progress | FTS IF | 2026-04-03 |
| 03234 | Action | P2 - Medium | Process code information missing from PTP | Not Started | PTP | 2025-12-12 |
| 03355 | Risk | P2 - Medium | PTP ECA OSAT Predictive Tool Test Self-Service Query View cr... | In Progress | FTS IP | 2026-04-03 |
| 03718 | Risk | P2 - Medium | Storage Location Logic for Non-MMID Parts. | In Progress | PTP | 2026-03-27 |
| 03729 | Action | P2 - Medium | AN and CC invoices are fetching wrong tax codes and posting ... | In Progress | FPR | 2026-03-23 |
| 03540 | Issue | P2 - Medium | FPR Tower help required for GR/IR Clearing document and Data... | To Be Reviewed | PTP | 2026-02-11 |
| 03542 | Action | P2 - Medium | T042A table data in IF & IP | In Progress |  | 2026-02-13 |
| 03548 | Risk | P2 - Medium | IAPMID 1532 SIC-Supplier Hub MRP data needs not aligned | In Progress | B-Apps | 2026-04-03 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03628 | Risk | P2 - Medium | R3 Returns Rework Process Causing Finance Double Counting in... | In Progress | E2E | 2026-03-27 |
| 03641 | Risk | P2 - Medium | Inventory Item Detailed Report | In Progress | Analytics (Reporting) | 2026-03-27 |
| 03462 | Risk | P2 - Medium | PTP ECA Demand Analytics dependency on MP PRF & RTF | In Progress | FTS IP | 2026-04-03 |
| 02173 | Risk | P2 - Medium | LE Restructuring : Jan 1 ‘26 EE+Asset changes reduced to Mal... | In Progress | Legal Entity | 2025-09-30 |
| 03733 | Risk | P2 - Medium | FTS IP string cases upload to JIRA | Not Started | PTP | 2026-03-13 |
| 03735 | Issue | P2 - Medium | Box CPU Supplier Moduslink Queries | In Progress | FTS IP | 2026-03-21 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03749 | Action | P2 - Medium | Logistics Data Intake and Creation Process Definition | In Progress | Test Management | 2026-03-27 |
| 03756 | Risk | P2 - Medium | LE101-1001 Operation Support Ownership for SIMS/Tester Front... | In Progress | E2E | 2026-04-24 |
| 03758 | Action | P2 - Medium | IMR Repair Order Creation Ownership | In Progress | PTP |  |
| 03765 | Risk | P2 - Medium | Net Price issue for ZIC STO creation | Not Started | PTP | 2026-03-27 |
| 03768 | Risk | P2 - Medium | E2Open interface smoke testing | In Progress | Cutover | 2026-04-03 |
| 03317 | Risk | P3 - Low | BPMG – E2E L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-05-29 |
| 03525 | Issue | P3 - Low | Vendor determination in PDH for 2DN PR's & STR's. | Not Started | FTS IP | 2026-03-06 |
| 03473 | Action | P3 - Low | Manual Service PIR creation for IP-IF Service Procurement. | In Progress | FPR | 2026-05-29 |
| 02358 |  |  | METs/SOM Bapp is not ready for E2E Testing | Not Started |  |  |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*L-040 — Architecture Document (TOGAF BDAT) · Procure To Pay · Generated: March 2026*

