<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">M-090 — Schedule Production (IF)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Forecast to Stock (IF) (FTS-IF) Tower<br/>
  Capability M-090 · M Mfg. Schedule and Execution (IF)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **M-090 Schedule Production (IF)** within the IAO program. It includes 12 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Forecast to Stock (IF) (FTS-IF) |
| **Process Group** | M Mfg. Schedule and Execution (IF) |
| **Capability** | M-090 - Schedule Production (IF) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 5 Reports, 92 Interfaces, 31 Conversions, 118 Enhancements, 15 Forms, 4 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Forecast to Stock (IF) |
| **L1 Process** | M Mfg. Schedule and Execution (IF) |
| **L2 Capability** | M-090 - Schedule Production (IF) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Intel Foundry Supply Chain Integration | Integrate Intel Foundry manufacturing and logistics into unified S/4 HANA supply chain | IDM 2.0 Foundry Enablement | High |
| 2 | Warehouse & Logistics Modernization | Modernize warehouse management and shipping processes with EWM integration | Supply Chain Digital Transformation | High |
| 3 | Production Planning Optimization | Enable MRP-driven production planning with real-time material availability | Manufacturing Excellence | Medium |
| 4 | M-090 Process Migration | Migrate Schedule Production (IF) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Supply Chain (Intel Foundry) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Fulfillment Lead Time | < 48 hours | Time from production completion to shipment dispatch | 72 hours (legacy) | Logistics Manager |
| Inventory Accuracy | > 99.5% | Physical vs system inventory match rate | 97.8% (current) | Warehouse Manager |
| MRP Planning Cycle | < 4 hours | End-to-end MRP run including exception processing | 8 hours (legacy) | Planning Lead |
| M-090 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **12 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for M-090 Schedule Production (IF).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | M-090-050_Identify_Consumable_Material_Requirements_(IF) | M-090-050_Identify_Consumable_Material_Requirements_(IF) | Batch User, Boundary Apps, Master Data Steward, Production Scheduler | 9 | 10 |
| 2 | M-090-060_Schedule_Consumable_Material_Requirements_(IF) | M-090-060_Schedule_Consumable_Material_Requirements_(IF) | FTS IF - Materials Planner, LOG IF Batch User, Material Handler, PTP System ID | 13 | 1 |
| 3 | M-090-080_Re-schedule_Planned_Order_(IF) | M-090-080_Re-schedule_Planned_Order_(IF) | Boundary Apps, FTS IF - Production Scheduler, IT Department | 6 | 4 |
| 4 | M-090-090_Check_for_Material_Availability_(IF) | M-090-090_Check_for_Material_Availability_(IF) | FTS IF - Production Planner | 11 | 7 |
| 5 | M-090-110_Initiate_Production_Order_Creation_(IF) | M-090-110_Initiate_Production_Order_Creation_(IF) | FTS IF - Materials Planner, Factory Supervisor, IT Department | 14 | 8 |
| 6 | M-090-180_Expedite_Missing_Material_(IF) | M-090-180_Expedite_Missing_Material_(IF) | FTS IF - Production Planner | 11 | 7 |
| 7 | M-090-210_Identify_Change_in_Production_Data_(IF) | M-090-210_Identify_Change_in_Production_Data_(IF) | FTS IF - Batch User, FTS IF - Production - Master Data Steward, FTS IF - System Batch ID (RFC User), IT Department, Production Supervisor | 10 | 2 |
| 8 | M-090-250_Execute_Change_(IF) | M-090-250_Execute_Change_(IF) | FTS IF - Batch User, FTS IF - System Batch ID (RFC User), IT Department, Master Data Steward - Production, Production Supervisor | 10 | 2 |
| 9 | M-090-280_Process_Work_Centers_(IF) | M-090-280_Process_Work_Centers_(IF) | FTS IF - Production - Cost Accountant, FTS IF - Production - Master Data Steward | 9 | 0 |
| 10 | M-090-290_Process_Routing_(IF) | M-090-290_Process_Routing_(IF) | FTS IF - Batch User, FTS IF - Production - Master Data Steward, IT Department, Production Supervisor | 13 | 5 |
| 11 | M-090-300_Process_Reference_Operation_Set_(IF) | M-090-300_Process_Reference_Operation_Set_(IF) | IT Department, Master Data Steward - Production, Production Supervisor | 35 | 8 |
| 12 | M-090-430_Process_Production_Version_(IF) | M-090-430_Process_Production_Version_(IF) | FTS IF - Production - Master Data Steward, FTS IF Batch System ID, IT Department, Production Supervisor | 13 | 5 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 M-090-050_Identify_Consumable_Material_Requirements_(IF) — M-090-050_Identify_Consumable_Material_Requirements_(IF)

**Swim Lanes**: Batch User · Boundary Apps · Master Data Steward · Production Scheduler | **Tasks**: 9 | **Gateways**: 10

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
    subgraph Batch User
        n4[["fa:fa-cog Perform Dependent Demand MRP"]]
        n7["Maintain Forecasting Data for Auto Reorder Point"]
        n8["Maintain Consumption Data"]
        n9["Perform Material Requirement Planning Run"]
        n11(["fa:fa-stop Purchase Requisition Created"])
        n17{{"fa:fa-code-branch exclusiveGateway"}}
        n18{{"fa:fa-arrows-alt UPI Demand?"}}
        n19{{"fa:fa-arrows-alt parallelGateway"}}
        n21{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph Boundary Apps
        n1[["fa:fa-cog Perform Planning for Materials"]]
        n2[["fa:fa-cog Perform Planning for Materials"]]
        n3[["fa:fa-cog Perform Planning for Materials"]]
        n10(["fa:fa-play Planning for Materials Initiated"])
        n12{{"fa:fa-code-branch Type of Demand?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch Types of Commodities?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-arrows-alt MRP Path?"}}
    end
    subgraph Master Data Steward
        n6["Maintain Fix Reorder Point-"]
        n16{{"fa:fa-code-branch MRP Type?"}}
    end
    subgraph Production Scheduler
        n5["Create Planned Orders"]
    end
    n6 --> n9
    n9 --> n17
    n2 --> n13
    n10 --> n20
    n7 --> n17
    n8 --> n17
    n15 --> n3
    n13 --> n14
    n14 -->|"SUBS, EMIB, MEM, IHS"| n15
    n19 --> n21
    n14 -->|"UPI, FG"| n5
    n18 --> n4
    n18 --> n15
    n16 --> n6
    n16 --> n7
    n16 --> n8
    n3 --> n19
    n17 --> n21
    n21 --> n11
    n20 -->|"Path 3,4 ,6"| n16
    n20 -->|"Path 1,2"| n12
    n4 --> n19
    n12 -->|"Engineering Demand"| n2
    n1 --> n13
    n12 -->|"Revenue Demand"| n1
    n5 --> n18
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n10 startEvt
    class n11 endEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV9uO4jgQ_RUroxa7UpDiXAidhx1xy2xLgxY107sPwzy4EwesTpysnXTDMvz7lnMDMmEeppFA-LjOqXKVy3GOWpCGVPO0u7sj4yz30HGQ72hCBx4aPBNJBzqqgL-JYOQ5pnKgbKKU52v2X2mG7WyvzBTmk4TFB4Wu6Tal6OlBRxMgxjqShMuhpIJFA32QCZYQcZilcSqU9Qc6joyo9FZPTVMRUnE2MAwXBw5QY8bpGbZc27V9xZM0SHl4JRo50TgKBicVXJy-BTsi8jL8QtIl2f_DwnwH44jEkoLNLk_iz-SZxmqNuSgUFhTitUkGk8oPh4StMxIwvgXcNgAShL-cIcc4ndDp7m7DW6fo8-OGI_gEMZFyTiMkc4AXrzmKWBx7H-zZxHcMXeYifaHeB3Phzi1TD9RKPFi6oavkDt8o2-5y7zmNw9p0-KbW4JnZXhd7zzR0cYDfji_Kw7On2cgcm-PW09TFMzxrPEVR9C5PkFfxhciX2tfC8k1_3vrCzsiZGT_qNcuc2-4Ed_NExSsL6IWo7_vW4pyqxcjBxm3RqW-NjFlHdEty-kYOZ8H7md0K-o7rY_emYOWvG2XxvBJp0AhaC8d3WkF3iv2JeVPQnmB7XEcIOltBsh2akjzYoSdYfTWhPtz--nWjRcSLyDBIt2hFRZSKBM1pBhWmPId_CeEhWj6uNtq3bxdMF4hLwngOX-SnggZE5rBb0ZzkBIEKmhR5ih5p2XRolYIpSFwojC8VZimXRZLlLOWlwrXpPZg2sS0h06r9Qfrfggk4RyDMVUw4V94fC35Nxfi3dokyTzO0KgQ0kKQVX7LS5UxQkA2B-vsl1z0ez-kJ6fAZ2hKSSPdBXEj2Sj9VVd9op9MlbXymESHSNzkkcY6eVg91Oj92Cfe9hIwIEsc07vdi4l4S47dig4p2t0RalMcbmmSZvIynf1e0SVbVbcogO_vCfAfXegcXG-c6ZzF0Yj8LPcAjifXV2uyv9ZdDRlEa3aqc9Ws7xL7tTCpvszRJ0hAipfIHl84vuTSN3u0CjY1WJN99_Nk-WUJrQw-Xnb1W4iK8UB5dnQRsf93zw047jvqjV3Go1f80DjgQwyIoG3Yd7GhYxFeHmQOBVI1cFZ-G6C8ViGxDaCX5CA2Hf8DBUg_vqyF267FZj616jI0KaB5P3O0Qxp0xdiqgFbBqA7sBbAV832jrp-laR4vlw1RHy8VSRw9_rjfadyXRmNbRmbjLhSNFR_6n0ry1rkOxO-OzXL32UWfsdsbjetxE3uQKu51wTFxbtIBRx6d2FrJ0G-mjakmjXgusm9W0WU_bXZdmbb7gW7irQSurB03ZkSWx4eFu2RreI32lvKCXnCbYulB4fPEAVkoX14SrGfPmjHVzxr45Axurubdd47i-Y12jZnPRuIatftjuh51-eNQPu_3wuB--74Wh3L0wbmBN1xIqEsJCzTtq5dsBvEGENCJFnGsnXSNwmVgfeKB55S1aK7IQmHNG4GRIKvD0P1P_4Rw=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 M-090-060_Schedule_Consumable_Material_Requirements_(IF) — M-090-060_Schedule_Consumable_Material_Requirements_(IF)

**Swim Lanes**: FTS IF - Materials Planner · LOG IF Batch User · Material Handler · PTP System ID | **Tasks**: 13 | **Gateways**: 1

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
    subgraph FTS IF - Materials Planner
        n1["fa:fa-user Perform Reservation Review by 3PL"]
        n4[["fa:fa-cog Create SAP Reservation with 201 Movement"]]
        n5[["fa:fa-cog Send Material by 3PL"]]
        n6[["fa:fa-cog Receive goods into the Warehouse"]]
        n15(["fa:fa-stop Schedule Consumable Material Requirements Completed"])
        n16(["fa:fa-stop Schedule Consumable Material Requirements Completed"])
    end
    subgraph LOG IF Batch User
        n7[["fa:fa-cog Create Outbound Delivery"]]
        n8[["fa:fa-cog Perform Batch Determination (Move material from consigned stock to Intel..."]]
        n9[["fa:fa-cog Pick/Pack"]]
        n10[["fa:fa-cog Perform Goods Issue"]]
        n11[["fa:fa-cog Perform GI against Reservation by 3PL"]]
        n17{{"fa:fa-code-branch w/ offsite 3PL?"}}
    end
    subgraph Material Handler
        n2[["fa:fa-cog Place Order on New UI(PM) for Factory Portal Replacement"]]
        n3[["fa:fa-cog Acknowledge Receipt"]]
        n14(["fa:fa-play Process initiated to schedule Consumable Material Requirements"])
    end
    subgraph PTP System ID
        n12[["fa:fa-cog Generate STO for Replenishment from Offsite based by ROP MRP"]]
        n13[["fa:fa-cog Receive STO"]]
    end
    n14 --> n2
    n2 --> n4
    n4 --> n1
    n1 --> n5
    n11 --> n17
    n12 --> n13
    n13 --> n7
    n7 --> n8
    n8 --> n9
    n9 --> n10
    n10 --> n6
    n6 --> n16
    n5 --> n3
    n3 -->|"Pass Through Hand-off  drop and go
 (triggered by New UI Portal with unloading sloc)

RICEFW"| n11
    n17 -->|"YES"| n15
    n17 -->|"NO"| n12
    class n1 userTask
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
    class n14 startEvt
    class n15 endEvt
    class n16 endEvt
    class n17 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtVm1v4jgQ_itWVhVdCboJJITy4U4UyB5Su42gvdVpuQ8mcYJFsFnbKeW6_Pcb5wVItjmddMeHqvP2zPiZ8cRvRsBDYgyNq6s3yqgaoreWWpMtaQ1Ra4UlabVRrvgdC4pXCZEt7RNxphb0r8zNsnev2k3rPLylyUFrFyTmBD3P2mgEgUkbScxkRxJBo1a7tRN0i8VhzBMutPcHMojMKMtWmO64CIk4O5imawUOhCaUkbO659qu7ek4SQLOwgpo5ESDKGgddXEJ3wdrLFRWfirJA379SkO1BjnCiSTgs1bb5B6vSKLPqESqdUEqXkoyqNR5GBC22OGAshj0tgkqgdnmrHLM4xEdr66W7JQU3c-XDMEvSLCUExIhqUA9fVEookky_GCPR55jtqUSfEOGH7pTd9LrtgN9kiEc3Wxrcjt7QuO1Gq54Ehaunb0-w7C7e22L12HXbIsD_K3lIiw8Zxr3u4Pu4JTpzrXG1rjMFEXRf8oEvIonLDdFrmnP63qTUy7L6Ttj82e88pgT2x1ZdZ6IeKEBuQD1PK83PVM17TuW2Qx65_X65rgGGmNF9vhwBrwd2ydAz3E9y20EzPPVq0xXvuBBCdibOp5zAnTvLG_UbQS0R5Y9KCoEnFjg3Rp5Tws081AHPUCp-v5I5CeYMSJyR_1j1relEeFhhDuad-QTEXGxRXOiScOKcgb_v1CyR6sD6vn3S-PPi2j72yk84DEaCwKp0GLkVwD2VK1R17TQA3-BLcAUgFyiOFWUBczaqeZz2suIfjViTgJCXwiKOQ8lokxxBPsGfcWCrDmcqxZtOdencKn4Di2CNQnThKAxZzLd6hV1LmBOvqdUZHVLcNjuEqJICJAfLyH7_yckEFDr5f3jZ93LO6yCNXqWlRa67zbhMVUrngKTE5IAN-JQI2FQjSobn2eYQD1iS1nev2vdN7Qtq48E3yLYk5LGjISwhXiwQUD5jCmS3Nzc1BLd1hLRYPPJx8Gm3hTz_YI-Zz2dSZn-1EarIWKGcIwpk6oyhe8OkuW-vZ0xQtJZwR4GAvafEI8iSYFICPp1aRyPTa05dfU3zMKk0plurcAEB9AY_U1CUNAXuFTPs2v_4SOCupGHA8XFAflcqGxGdtr9nevSq6KOgg3j-4SEMckvwq4eYNnn4QRQSAF7hkh9U6iiUH6o2yf_7cT-05z6Tz5aHKQiWzSbXJZQo-IzgTWU7Yqnx-z0-riEUbnWKfIReywaoJ8QoW7f_NFHD3O_frre-8sAkM-ep0qBDNTp_AK9KeRuLtqFWFit0jsXnVIsZMstFUW41SsVvVxROri5OCjEQS7eFuJtEW2W0Wau6Bdyv7CXspPLZbIs14-l4cMnBD2tBU_jdTaGHRhehEIBiwgk2IsQcK0EjWMici7z4SuHLdvQKUs4DuH9gWTCA2jxks1n46n3dWn80Ecva3SLrH9MF7nFqVu-POaG7sUnTnNZftor6u7l97li6TVa7EaL02jpN1rcRsug0XLbaIEeNpqsZlMzDVYzDzDM5SOwqneKB1tV239X65ZvGaNtbGHtYxoawzcje7HDqz4kEU4TZRzbBk4VXxxYYAyzl62R7kKInFAMl3-bK49_A3CE0Zs=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 M-090-080_Re-schedule_Planned_Order_(IF) — M-090-080_Re-schedule_Planned_Order_(IF)

**Swim Lanes**: Boundary Apps · FTS IF - Production Scheduler · IT Department | **Tasks**: 6 | **Gateways**: 4

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
        n5["Create Production Plan for Next Run"]
        n7(["fa:fa-play Initiated Process for Re-schedule Planned Order"])
    end
    subgraph FTS IF - Production Scheduler
        n1["fa:fa-user Compare Material, Plant, Date, Quantity"]
        n2["fa:fa-user Create New Planned Order"]
        n3["fa:fa-user Update Planned Order Quantity"]
        n4["fa:fa-user Update Planned Order Date"]
        n8(["fa:fa-stop New Planned Order Created"])
        n9(["fa:fa-stop No change Required"])
        n10(["fa:fa-stop Planned Order Date Updated"])
        n11{{"fa:fa-code-branch Planned Order Exists?"}}
        n12{{"fa:fa-code-branch Quantity matches ?"}}
        n13{{"fa:fa-code-branch Date Matches?"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph IT Department
        n6["Perform Staging of Updated Production Plan"]
    end
    n7 --> n5
    n5 --> n6
    n6 --> n1
    n1 --> n11
    n2 --> n8
    n11 -->|"Yes"| n12
    n11 -->|"No"| n2
    n13 -->|"No"| n4
    n13 -->|"Yes"| n9
    n12 -->|"No"| n3
    n14 --> n13
    n3 --> n14
    n12 -->|"Yes"| n14
    n4 --> n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n7 startEvt
    class n8 endEvt
    class n9 endEvt
    class n10 endEvt
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl2P6jYQ_StWVitaKUj5JGweWkEg1Up3926Xva2q0geTOGBtYqe2s0C5_Pfa-YKErFSpPCDNGZ8zZya2k5MW0RhpvnZ_f8IECx-cRmKHMjTywWgDORrpoAJ-gwzDTYr4SK1JKBEr_E-5zHTyg1qmsBBmOD0qdIW2FIFvjzqYSWKqAw4JH3PEcDLSRznDGWTHgKaUqdV3aJoYSVmtTs0pixG7LDAMz4xcSU0xQRfY9hzPCRWPo4iSuCOauMk0iUZnZS6l-2gHmSjtFxw9wcPvOBY7GScw5Uiu2Yks_QI3KFU9ClYoLCrYRzMMzFUdIge2ymGEyVbijiEhBsn7BXKN8xmc7-_XpC0KvryuCZC_KIWcL1ACuJDw8kOABKepf-cEs9A1dC4YfUf-nbX0FralR6oTX7Zu6Gq44z3C253wNzSN66XjverBt_KDzg6-ZejsKP97tRCJL5WCiTW1pm2luWcGZtBUSpLkf1WSc2VvkL_XtZZ2aIWLtpbpTtzAuNVr2lw43szszwmxDxyhK9EwDO3lZVTLiWsan4vOQ3tiBD3RLRRoD48XwYfAaQVD1wtN71PBql7fZbF5YTRqBO2lG7qtoDc3w5n1qaAzM51p7VDqbBnMd2BOi3Ivg1me8yqnfsT9c60FDEn_QBaMi0hgSsBLCglIKAPP6CDAa0HW2l9XJO8HyUqgn8Bxnsq2H-VBx1IiVhoR4rzkvqIxj3YoLlJUChKZ_6rOoBT7sVKTG6nnM3xbgccQjK_drGoVdmXBbB2oLQICmuWQIfAkXVS3g6oodLCQgA5-LWSAxbHbhtXTqMbwjPY3dq9Idpf0LY_L2V0TPinn_AemsttlTS-z5oLmt_Zq3_FlqiXvoc-jQN4cZIvkc_m7wOyGYBo9xq2z2vMN0zydGqa6_ccbeX9Fu57A8oC54D-vtfP5mmsNc5sRggwK-fg5uCHaw8TS51NFuuE4wxx0iNKC4w_0S3WOL7TbDfr4BhZI7jWRISKutCdyeC-IyY2fgZWAW3l1A5o0E-sfrvYZtwWIB8bjn-SBrEO3Cid1OKnC-jYjZh02sVXF0yZd5r-vtT8QX2vf1Zj7mWdaJlrc7uJOH2-UHpqE1SXYDe7U1hrArmOnT2y9NZmGeX0Zqlabl0AHtoZhexh2hmGvfW124Gn9huuAD0OgaQyiZvNG6MLWMGwPw04Da7qWIZZBHGv-SSs_nuQHVowSWKRCO-saLARdHUmk-eVHhlaUm26BodyyWQWe_wWoQgQj" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 M-090-090_Check_for_Material_Availability_(IF) — M-090-090_Check_for_Material_Availability_(IF)

**Swim Lanes**: FTS IF - Production Planner | **Tasks**: 11 | **Gateways**: 7

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
    subgraph FTS IF - Production Planner
        n1["fa:fa-user Sum Requirements for all Planned Orders in Run at Item Level"]
        n2["fa:fa-user Check Item Availability in Local Plant and 3PL"]
        n3["fa:fa-user Check Lot Availability in Local Plant and 3PL"]
        n4[["fa:fa-cog Check Planned Order-Current Date and X Weeks/Date"]]
        n5[["fa:fa-cog Check Sales Order (SO) Line Pegging for Planned Orders"]]
        n6[["fa:fa-cog Retrieve Component and Component Lot Info from Assembly Build Record (ABR) Table"]]
        n7[["fa:fa-cog Determine Intel Lots/Customer Lot SAP Batch and Plant where Current Stock Exists"]]
        n8[["fa:fa-cog Check Silicon Components in BOM"]]
        n9["Send Alert and Report to Required Owners"]
        n10["Check if Plant is Non DMRA/External App (Configurable at Plant Level)"]
        n11["Check Local Supplying Plant"]
        n12(["fa:fa-play Request Received to Check for Material Availability"])
        n13(["fa:fa-stop Alert Sent to Required Owners"])
        n14(["fa:fa-stop Material Availability Checked"])
        n15{{"fa:fa-code-branch Silicon Components Exists in Planned Order?"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-code-branch Lot Availability Exists?"}}
        n18{{"fa:fa-code-branch Item Availability Exists?"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch Lot Level Instructions Received?"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n4 --> n8
    n6 --> n7
    n7 --> n16
    n16 --> n20
    n15 -->|"Yes"| n5
    n8 --> n15
    n3 --> n17
    n2 --> n18
    n19 --> n9
    n17 -->|"No"| n19
    n1 --> n2
    n18 -->|"No"| n19
    n20 -->|"Yes"| n3
    n20 -->|"No"| n1
    n9 --> n13
    n18 --> n21
    n5 --> n6
    n21 --> n14
    n12 --> n4
    n17 -->|"Yes"| n21
    n15 -->|"No"| n10
    n10 --> n11
    n11 --> n16
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n12 startEvt
    class n13 endEvt
    class n14 endEvt
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV9tu4zYQ_RVCi8AJYGN1tRw_tPBNRYBkE8Rpt8WmD7RE2URoSqWoxN6s_71DiZItRX7Y1g-G55BzZuZwNKLfjTCJiDE2Li7eKadyjN57ckO2pDdGvRXOSK-PSuAPLCheMZL11J444XJJvxfbLDfdqW0KC_CWsr1Cl2SdEPT7TR9NwJH1UYZ5NsiIoHGv30sF3WKxnyUsEWr3JzKKzbiIppemiYiIOG4wTd8KPXBllJMj7Piu7wbKLyNhwqMGaezFozjsHVRyLHkLN1jIIv08I3d495VGcgN2jFlGYM9GbtktXhGmapQiV1iYi9dKDJqpOBwEW6Y4pHwNuGsCJDB_OUKeeTigw8XFM6-Doqf5M0fwCRnOsjmJUSYBXrxKFFPGxp_c2STwzH4mRfJCxp_shT937H6oKhlD6WZfiTt4I3S9keNVwiK9dfCmahjb6a4vdmPb7Is9fLdiER4dI82G9sge1ZGmvjWzZlWkOI7_VyTQVTzh7EXHWjiBHczrWJY39GbmR76qzLnrT6y2TkS80pCckAZB4CyOUi2GnmWeJ50GztCctUjXWJI3vD8SXs_cmjDw_MDyzxKW8dpZ5qsHkYQVobPwAq8m9KdWMLHPEroTyx3pDIFnLXC6QcHTEt0EaICANspDSROOHhjmnIhyp_pw69uzEeNxjAdKeLTMt-iR_JNTAc8rlxmKE4EwY9ozQvfqkcoQ5egx5whLdCPJFt2SV8Kejb9PiO0m8WxDwpdy8-QVU4ZXlFG5V0S3SYjLABJhHiHn4bZJ5XRR3Sby55ncbzVVmKw1U6O0wSwXAipHczjgguRP9JWQl-yzAoDtlM7roltimHAlGbpc3l-hW5g26IGs1_BsF3o2tWxxDpucj0QKCuqiWbJNE050ZUdL6XDD4wTFIgFts4xsV2yPpjllEXiHMAPR5WT6eIWe1OxtRfOb0eZEErFV-d5wSZgizz7P8kwmW6hGhVpOHtAUy3BTpFFK_bYhAhLUwi1lAiosdjST7dpGnXrB8cHYPZZUdNf0_q7lfA2-S5hDaMKIKFV4JGkCP2VS9Sxo-sZLTU973ATXMhiNdc40Q18g6PzucfJ5sYOqOXTOJE3R5SzhMV3nQqmlGrzcX3T4VYvXqnnLzlvmacr26pgLp9Zu-7KuPmUwOlTOJJPqkAh9hdyhjpJNNckdtJt66zWaHBivTimdIyWcUaqlWapj6BSl4ey2nDsjlhmRqO3svb8fjzIigxW8wKApOg6z7AR1po2-__XZOBxOGYfdjGQXsjwDfX4rJ27bze92-zAeyjQ-RB11u38cVGf8r_9T1rZ5Puui0-D5g2FfTu2s7pB2dNv62ejw_JQ_uIsGg1_gkdTmsDR9bfqlaQ21ben16nUNDaCAH8_GXwQa6wfMQr0w0p6V7Wi7Yra1XQW2rkvgurJ9TfwlKXitekFnUJmjM_tss5WZ016oPDSuE7CcBrNSVwNeaVda2DoTy60cdE1uu4Qqg5qpVq1KoZbT1Jz1Tqt5AsU9QYlQ3Y8asN0NO92we3olaqx4Z1eGZ1f8syujsyugWHV7beKOvmk2UbcT9apLWBMedsN-Nzzqhq87YeigTtiqYKNvwItyi2lkjN-N4k8P_DGKSIxzJo1D38C5TJZ7Hhrj4s-BkacReM4phjvbtgQP_wKBkTGF" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 M-090-110_Initiate_Production_Order_Creation_(IF) — M-090-110_Initiate_Production_Order_Creation_(IF)

**Swim Lanes**: FTS IF - Materials Planner · Factory Supervisor · IT Department | **Tasks**: 14 | **Gateways**: 8

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
    subgraph FTS IF - Materials Planner
        n1[["fa:fa-cog Create Production Order"]]
        n16["_Release Production Order"]
        n19{{"fa:fa-code-branch Production Order Exists?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Factory Supervisor
        n2["Determine Data Elements"]
        n3["Receive Operation Table for Manufacturing (MFG) Stage"]
        n15(["fa:fa-play Lot Creation Request Received"])
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph IT Department
        n4["Create Copy of Operation Table"]
        n5["Filter Lot Owner From Operation Table (TD)"]
        n6["Check if Operation is for Production Start in Moveout Operation"]
        n7["Check Production Order Exists for the Stage (ASSM)"]
        n8["Determine Start Date"]
        n9["Determine Production Version"]
        n10["Determine Enterprise Resource Planning (ERP) Routing"]
        n11["Determine Plant"]
        n12["Determine Unique Product ID"]
        n13["Determine Order Type"]
        n14["Determine Die Level Cherry Picking (DLCP) to UPI Mapping"]
        n17{{"fa:fa-code-branch DLCP Applicable?"}}
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n23{{"fa:fa-arrows-alt parallelGateway"}}
        n24{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n4 --> n5
    n5 --> n6
    n23 --> n7
    n24 --> n13
    n8 --> n23
    n19 -->|"Yes"| n20
    n24 --> n10
    n24 --> n9
    n9 --> n23
    n13 --> n17
    n10 --> n23
    n24 --> n11
    n24 --> n12
    n11 --> n23
    n12 --> n23
    n6 --> n24
    n24 --> n8
    n19 -->|"No"| n1
    n1 --> n20
    n20 --> n16
    n7 --> n19
    n15 --> n21
    n21 --> n2
    n21 --> n3
    n2 --> n22
    n22 --> n4
    n3 --> n22
    n14 --> n18
    n17 -->|"Yes"| n14
    n17 -->|"No"| n18
    n18 --> n23
    class n1 serviceTask
    class n15 startEvt
    class n16 startEvt
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV21v4jgQ_itWqopWAinOCwE-3IkCWVVqrxW0ezptVyc3OGDVxDnHact1-e83zhvE0A-7x4eq83jmmZknMyZ8WJFYUmtknZ9_sISpEfroqDXd0M4IdZ5JRjtdVAJfiWTkmdOso31ikagF-7dww176rt00FpIN41uNLuhKUPR43UVjCORdlJEk62VUsrjT7aSSbYjcTgQXUnuf0UFsx0W26uhKyCWVewfbDnDkQyhnCd3DbuAFXqjjMhqJZNkijf14EEednS6Oi7doTaQqys8zekve_2RLtQY7Jjyj4LNWG35DninXPSqZayzK5WstBst0ngQEW6QkYskKcM8GSJLkZQ_59m6HdufnT0mTFN3MnxIEn4iTLJvSGGUK4NmrQjHjfHTmTcahb3czJcULHZ05s2DqOt1IdzKC1u2uFrf3RtlqrUbPgi8r196b7mHkpO9d-T5y7K7cwl8jF02W-0yTvjNwBk2mqwBP8KTOFMfx_8oEusoHkr1UuWZu6ITTJhf2-_7EPuar25x6wRibOlH5yiJ6QBqGoTvbSzXr-9j-nPQqdPv2xCBdEUXfyHZPOJx4DWHoByEOPiUs85lV5s_3UkQ1oTvzQ78hDK5wOHY-JfTG2BtUFQLPSpJ0jcKHBboOUQ_dQql6fzJ0z0mSUFk66k-Cv317smIyikkvEis0kRScERSyzCPFRILu9Ao9Wd-_Hwb1IejvOeUUtvuU86Hv8ONjn2FJe88w6dH6KArN3lmmst-frN3uINyxT4fT94jnGXulX8rnsA-DSTWFIJEScosWeaonIROHAjjQypSCQBu4E9CUKIJmHO6qRGXtRlxwnNOIQk50B0SkqP1B32coFhJUTvIYMuUSVhhd3IZfLtFCkRU19PAvGsVTDgN0I1Qpu6ab039ymilUJVpC7OVhsXivBpFSvGU9whVKiSScU36kRRnk_FzQsYDXD2hKwV9pWQ6YPeikmpiJSLdIxKYy7d598A8ZB7GLru_eYBZRKMXmSNCLh-llO1aP3GRNoxfEDrOwrBD_YJoW-lZELEG34pWKXO2d24RBQ_jJKBbE8L1VPkV0MV4sbo2iBq3hKTPDCBltD1teB9m-Upkd1YXtlvssgf_g-wwWbU4zkcuIlmtcTNlsfn-J5tAlWAYNbmeFEGV4tEf_MWEwe3V56HpqeLst71Koh21qjrfX3idG0Q19pRyB1BJ28J5FL0Xl05sJlK4Eery_ht1J0-MOgtOrryPROE05i_SsmDcGHvzsjVFuifsrq-X94molHur1foONqEy_NPuV6bilHdR25Y7dChiUtlPbeKiBH0_WXxSurR_63jRDTWBY2UOTqsqN6-TYNjwaSmwCTh2CTVLHAPqV7RkUA7OhP0TRT52qJm66qYrDtXRBZdft4Upapym2pjDsprvquDmvgLpS1zjHdfNN6YHxLLBnntRNNSHG8yxeCnSzB68u7RO_eftr4_1P8KB-YWnDg9Pw8CQMWp-E8WnYOQ27p2Gvhq2utYHbg7ClNfqwit8N8NtiSWOSc2XtuhbJlVhsk8gaFe_XVp4uIXLKCHxZbUpw9x9VYt80" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 M-090-180_Expedite_Missing_Material_(IF) — M-090-180_Expedite_Missing_Material_(IF)

**Swim Lanes**: FTS IF - Production Planner | **Tasks**: 11 | **Gateways**: 7

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
    subgraph FTS IF - Production Planner
        n1["fa:fa-user Sum Requirements for all planned orders in run at Item level"]
        n2["fa:fa-user Check Item Availability in Local Plant and 3PL"]
        n3["fa:fa-user Check Lot Availability in Local Plant and 3PL"]
        n4[["fa:fa-cog Check Planned Order-Current Date and X Weeks/Date"]]
        n5[["fa:fa-cog Check Sales Order (SO) Line Pegging for Planned Orders"]]
        n6[["fa:fa-cog Retrieve Component and Component Lot Info from Assembly Build Record (ABR) Table"]]
        n7[["fa:fa-cog Determine Intel Lots/Customer Lot SAP Batch and Plant where Current Stock Exists"]]
        n8[["fa:fa-cog Check Silicon Components in BOM"]]
        n9["Send Alert and Report to Required Owners"]
        n10["Check if Plant is Non DMRA/External App (Configurable at Plant Level)"]
        n11["Check Local Supplying Plant"]
        n12(["fa:fa-play Request Received to Check for Material Availability"])
        n13(["fa:fa-stop Alert Sent to Required Owners"])
        n14(["fa:fa-stop Material Availability Checked"])
        n15{{"fa:fa-code-branch Silicon Components Exists in Planned Order?"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-code-branch Lot Availability Exists?"}}
        n18{{"fa:fa-code-branch Item Availability Exists?"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch Lot Level Instructions Received?"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n4 --> n8
    n6 --> n7
    n7 --> n16
    n16 --> n20
    n15 -->|"Yes"| n5
    n8 --> n15
    n3 --> n17
    n2 --> n18
    n19 --> n9
    n17 -->|"No"| n19
    n1 --> n2
    n20 -->|"Yes"| n3
    n20 -->|"No"| n1
    n9 --> n13
    n5 --> n6
    n21 --> n14
    n12 --> n4
    n17 -->|"Yes"| n21
    n15 -->|"No"| n10
    n10 --> n11
    n11 --> n16
    n18 -->|"No"| n19
    n18 -->|"Yes"| n21
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n12 startEvt
    class n13 endEvt
    class n14 endEvt
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11v4jgU_StWRhWtBJokJITysCu-sqrUTqvS3dnVdB9M4oBVY2dtp4Xp8N_3Oh9A0vAwuzwgfOx7zr3H1054tyIRE2tkXVy8U071CL139JpsSGeEOkusSKeLCuAPLCleMqI6Zk0iuF7Q7_kyx0u3ZpnBQryhbGfQBVkJgn6_6aIxBLIuUpirniKSJp1uJ5V0g-VuKpiQZvUnMkzsJFcrpyZCxkQeF9h24EQ-hDLKyRHuB17ghSZOkUjwuEaa-MkwiTp7kxwTb9EaS52nnylyh7dfaazXME4wUwTWrPWG3eIlYaZGLTODRZl8rcygyuhwMGyR4ojyFeCeDZDE_OUI-fZ-j_YXF8_8IIqeZs8cwSdiWKkZSZDSAM9fNUooY6NP3nQc-nZXaSleyOiTOw9mfbcbmUpGULrdNeb23ghdrfVoKVhcLu29mRpGbrrtyu3ItbtyB98NLcLjo9J04A7d4UFpEjhTZ1opJUnyv5TAV_mE1UupNe-Hbjg7aDn-wJ_aH_mqMmdeMHaaPhH5SiNyQhqGYX9-tGo-8B37POkk7A_saYN0hTV5w7sj4fXUOxCGfhA6wVnCQq-ZZbZ8kCKqCPtzP_QPhMHECcfuWUJv7HjDMkPgWUmcrlH4tEA3IeohoI2zSFPB0QPDnBNZrDQf7nx7thI8SnDPGI8W2QY9kn8yKuG8cq1QIiTCjKE0j4xRfqQUohzJjCOs0Y0mG8TIK2HP1t8nxG6deLom0UuxePyKKcNLyqjeGaJbEWGWp6YR5jHqP9zWqfptVLdC_zyT9-1AFYlVyfRQlnZvSutNMymhcjSDDc5J_kRfCXlRnw0AbKd0fhvdAsMNV5Chy8X9FbqF2wY9kNUKznbuZ01QNTgHdc5HoiUFd9FUbFLBSVnZcWR8uOGJQIkU4K1SZLNkOzTJKIshOoINQ5fjyeMVejJ3b0MtqKvNiCZyY_K94ZowQ64-TzOlxQaqMVKL8QOaYB2t8zQKq9_WREKCpXELLcCF-ZYq3axt2OoXbB9cu8eS8u6a3N81gq8hdgH3EBozIgsXHkkq4KcWVc-Cp2-88PS0x20ILcRoUuZMFfoCorO7x_Hn-Raq5tA54zRFl1PBE7rKpHHLNHix_tZ0-FWD1znwFp23yNKU7cw250GN1e7loXo4Tbs8Z6K02SRCXyF3qKNgM01yB-1mnnq1JgfGq1PK_pES9igtrVmYbWg1pRbsNYJbFYuMSNwM9t_fj1sZk94SHmDQFC2bWXSC2dNa3__6bO33p4yDdkayjVimwJ_fihu3GRa0h324Hoo0PqgO28M_XlRn4q__U9aufT7rvNPg_MFlX9za6tAhTXXX-Vl1OD_FD-6hXu8XOJLlcFAMg3IYFENnUI6dcr56XEMDGODHs_UXgcb6AXdhOTEsI6txvxxXzG45roSd6wK4rsZBSfxF5LzOYaLMoOKxGwn0mxMVQYmXOk61zi_GVYVuye94lV6ZqddMrBJ0naYXleLBJLvkPKx0mr4Oz1U7PKOWvzAYN6oXpRrstsP9dtg7fTeqzfhnZwZnZ4KzM8OzM2By9Rpbx_vlK2cd9VpRv3obq8ODdjhoh4ft8HUrDD3WCjsVbHUteGJuMI2t0buV__uBf0gxSXDGtLXvWjjTYrHjkTXK_yVYWRpD5IxieHnbFOD-Xy0JNSo=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 M-090-210_Identify_Change_in_Production_Data_(IF) — M-090-210_Identify_Change_in_Production_Data_(IF)

**Swim Lanes**: FTS IF - Batch User · FTS IF - Production - Master Data Steward · FTS IF - System Batch ID (RFC User) · IT Department · Production Supervisor | **Tasks**: 10 | **Gateways**: 2

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
    subgraph FTS IF - Batch User
        n5[["fa:fa-cog Update All Routings Which use Reference Operation Set​ Automatically"]]
        n12(["fa:fa-stop Change in Production Data Identified"])
        n14{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph FTS IF - Production - Master Data Steward
        n4["fa:fa-user Resolve Error with IT and Manufacturing"]
    end
    subgraph FTS IF - System Batch ID (RFC User)
        n10["Call BAPI to Update Reference Operation Set​"]
    end
    subgraph IT Department
        n3["fa:fa-user Identify Stage Specific Flow Plan/Routes Updates​"]
        n6["Send Alert Notification"]
        n7["Determine Reference Operation Set by Flow plan/Route Name and Stage and Plant​"]
        n8["Determine Changes at Operation, Area or Module Level​"]
        n9["Prepare Application Performance Interface (API) Structure for API Calls​"]
        n13{{"fa:fa-code-branch If Failure"}}
    end
    subgraph Production Supervisor
        n1["fa:fa-user Update Flow Plans and Routes"]
        n2["fa:fa-user Perform Changes in Flow/Plan"]
        n11(["fa:fa-play Request Sent to Initiate Flow/Plan"])
    end
    n11 --> n2
    n3 --> n7
    n7 --> n8
    n8 --> n9
    n10 --> n13
    n5 --> n12
    n2 --> n1
    n1 --> n3
    n6 --> n4
    n4 --> n14
    n14 --> n5
    n9 --> n10
    n13 -->|"Yes"| n6
    n13 -->|"No"| n14
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n11 startEvt
    class n12 endEvt
    class n13 gateway
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVttu4kgQ_ZWSo4iMBBrb2IHwsBIBvEJKMlFIdrQa5qGxy9BKY3u720nYDP--1b4AZkn2YXmIUuXqc05d-vJuhWmE1sA6P3_nCdcDeG_pFa6xNYDWgilstaF0_MEkZwuBqmVi4jTRM_53EeZ42ZsJM76ArbnYGO8MlynC07QNQ1oo2qBYojoKJY9b7VYm-ZrJzSgVqTTRZ9iP7bhgqz5dpzJCuQ-w7Z4T-rRU8AT37m7P63mBWacwTJOoARr7cT8OW1sjTqSv4YpJXcjPFd6yt-880iuyYyYUUsxKr8UNW6AwOWqZG1-Yy5e6GFwZnoQKNstYyJMl-T2bXJIlz3uXb2-3sD0_nyc7Urh5mCdAv1AwpcYYg9LknrxoiLkQgzNvNAx8u620TJ9xcOZOeuOu2w5NJgNK3W6b4nZekS9XerBIRVSFdl5NDgM3e2vLt4Frt-WG_h5xYRLtmUaXbt_t75iue87IGdVMcRz_Lyaqq3xk6rnimnQDNxjvuBz_0h_Z_8ar0xx7vaFzXCeULzzEA9AgCLqTfakml75jfwx6HXQv7dER6JJpfGWbPeDVyNsBBn4vcHofApZ8xyrzxb1MwxqwO_EDfwfYu3aCofshoDd0vH6lkHCWkmUrCB5nMA2gA9dMhyt4ojKUEeaX-D9-zK2YDWLWCdMlPGURJQRDIeAhzTVNoYLvK07rqB_wgDFKTEKEbxlKpnmawAz1PHdtewHDXKdrcoZMiM3c-vnzgMZxL3Y8SqcZjFYsWSLwBCjbKA8LrDHTDKYRJprHHCPC-HKI4b2_77VG2FnQZiFl-BaKXPEX_L3sxdzabstlNK0fFeOAtQO3TGmUJf3MYMjogNfbKTczSUVQqXhBmEiZSnjlegXTR2BJRDBJHrNQ55LqRuL_U8RsQ7zrqjHTMVw8BKOiQY20beIfUU3heng_BZ3WTfq0G5_Qk9oxZnRmrKnQB0TdZp5VHzZUEUadmmUYUldCCOgkgnvBkq9mQlBVctQRbwF5SZAzUkADhXR03aWmsWEhtRnYo8AxUhPWdCR_lBksNiV7tmOHO7bGovilSvOf0aZPqek3SMoJVMD0nsXcMMiA-npL4yEQbvAFxSmsK8K6l6aMtFuyTFRZwT3KOJVrZsRPE-KigUC4oM59IYkyN9OBQCFgmmnaerJwTvf0rE9jCBgXhPHZlB8M9yzPzLGn0sNN7zQ7Xc3TrrGqKGPZ3aYst7mwSnZXStrNBuSrATnKx9nvf-rehlr8V45KU1sTbWZ6Si8GXquoAb4cJUgw0On8Rjoqu1uavcrslWa_MvuleVUvtkvb6VYOv7JrNLey6_jSrKMvS9OrTK8Krm2ncviVfVV9t-vvhdZfc-tPU9RfhHf84S4t_DVicSMYFfVN2HC7p93d027vtNs_vBObrM7uWdH0u9UToOnt1vdg0-3VbqttrWnbMR5Zg3ereATSQzHCmOVCW9u2xejumG2S0BoUjyUrL0ZyzBkN9Lp0bv8BwtVHXg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 M-090-250_Execute_Change_(IF) — M-090-250_Execute_Change_(IF)

**Swim Lanes**: FTS IF - Batch User · FTS IF - System Batch ID (RFC User) · IT Department · Master Data Steward - Production · Production Supervisor | **Tasks**: 10 | **Gateways**: 2

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
    subgraph FTS IF - Batch User
        n5[["fa:fa-cog Update All Routings Which use Reference Operation Set​ Automatically"]]
        n12(["fa:fa-stop Change Executed in Production Order"])
    end
    subgraph FTS IF - System Batch ID (RFC User)
        n10["Call BAPI to Update Reference Op Set​"]
    end
    subgraph IT Department
        n3["fa:fa-user Identify Stage Specific Flow Plan/Routes Updates​"]
        n6["Send Alert Notification"]
        n7["Determine Reference Operation Set by Flow plan/Route Name and Stage and Plant​"]
        n8["Determine Changes at Operation, Area or Module Level​"]
        n9["Prepare Application Performance Interface (API) Structure for API Calls​"]
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch If Failure"}}
    end
    subgraph Master Data Steward - Production
        n4["fa:fa-user Resolve Error with IT and Manufacturing"]
    end
    subgraph Production Supervisor
        n1["fa:fa-user Update Flow Plans and Routes"]
        n2["fa:fa-user Perform Changes in Flow/Plan"]
        n11(["fa:fa-play Request Sent to Initiate Flow/Plan"])
    end
    n11 --> n2
    n3 --> n7
    n7 --> n8
    n8 --> n9
    n9 --> n10
    n5 --> n12
    n2 --> n1
    n1 --> n3
    n4 --> n13
    n14 -->|"Yes"| n6
    n6 --> n4
    n10 --> n14
    n13 --> n5
    n14 -->|"No"| n13
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n11 startEvt
    class n12 endEvt
    class n13 gateway
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVttu4kgQ_ZWWo4hEAo1tbCB-WImbV0hJJgrJjlbDPDR2GVppbG93m8Aw_PtW-wKYgX1ZPyCqXHVOXbu9M4IkBMMzbm93LGbKI7uGWsIKGh5pzKmERpMUir-oYHTOQTa0TZTEasp-5maWk260mdb5dMX4VmunsEiAvE-apI-OvEkkjWVLgmBRo9lIBVtRsR0mPBHa-gZ6kRnlbOWrQSJCEEcD0-xagYuunMVwVLe7TtfxtZ-EIInDGmjkRr0oaOx1cDz5DJZUqDz8TMIT3XxjoVqiHFEuAW2WasUf6Ry4zlGJTOuCTKyrYjCpeWIs2DSlAYsXqHdMVAkafxxVrrnfk_3t7Sw-kJLH11lM8Ak4lXIEEZEK1eO1IhHj3Ltxhn3fNZtSieQDvBt73B217WagM_EwdbOpi9v6BLZYKm-e8LA0bX3qHDw73TTFxrPNptji7xkXxOGRadixe3bvwDToWkNrWDFFUfS_mLCu4o3Kj5Jr3PZtf3TgstyOOzR_x6vSHDndvnVeJxBrFsAJqO_77fGxVOOOa5nXQQd-u2MOz0AXVMEn3R4BH4bOAdB3u77VvQpY8J1Hmc1fRBJUgO2x67sHwO7A8vv2VUCnbzm9MkLEWQiaLon_NiUTn7TIgKpgSd6xDIWFfmL3-_eZEVEvoq0gWZD3NMSESJ9z8ppkCqdQkm9Lhn7YD_IKEQiIAyBfUxBUsSQmU1CzzDbNOelnKlmhMqCcb2fGjx8nNJZ9d-CRKknJcEnjBZDxBoJMQUhYTDDtMAty0K96YRHivoDAqbuW1HQrFazK3CYjcvfqD_Mc70_ZTSQfYlhk0H-ZEJVUeZ4mdMwEia_xTt7ICFLctxXE6oShfchOzy2ZhPiaRVsyVRSznKYQsIgFxMctJi-cxl90dUGWccgz3hyyg5BTjACbAbj2z4nSEHnR64ZdNByBArHC4-xaj8h8W7CnB3byTFdAKDIUUep_OjZ1KZpejaToniRUHVn06QyUJII8YR85kEdYA7-E9YBYL0KXESctTXmZFXkBESViRXXwkxi5Ior_7rBl9xiiwNnI0ANNiO6i7ufFwlnt3e440yG05nio4nTAJuCZZGv4s9jZmbHfn7o5l90mEfEp40h9dPh9MJ4ozqEgI6ooxorwIsTpPI70CZFTn5VXkAlf4yoIgZl9MpVPmW7GE40zLAFmjXv4H0N5sjjTLNWnnExOd9yqE5azf5hFmZMVA1mvpF13LPtz6D7urAb5okHOWmAd1x0HbotJ_pOBVDiJsdL7N8EPBFZFUQGcbzvCkFbrD4yjlNuF2C3FbiH2SrFXiA-l-FCIVnnAxm4pV2B2KVdchdguRad8W8lWrvg1M_7WRfqF61m-6BSGTmVnlo4HRRm0ew70nOQ4FUN-AegwqouvprYvq9uX1c5ltXt6BdZZrcNXRF1vlzd-Xduurr262qnURtNY4UlBWWh4OyP_5sPvwhAimnFl7JsGxatiuo0Dw8u_jYwsH8kRozjQq0K5_xfdpUIn" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.9 M-090-280_Process_Work_Centers_(IF) — M-090-280_Process_Work_Centers_(IF)

**Swim Lanes**: FTS IF - Production - Cost Accountant · FTS IF - Production - Master Data Steward | **Tasks**: 9 | **Gateways**: 0

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
    subgraph FTS IF - Production - Cost Accountant
        n6["fa:fa-user Provide Standard Values"]
        n7["fa:fa-user Provide Cost Center and Activity Types values"]
        n8["fa:fa-user Provide Formula Definition"]
        n9[["fa:fa-cog Determine Required Relevant Work Centers"]]
        n10(["fa:fa-play Work Center Creation Required"])
    end
    subgraph FTS IF - Production - Master Data Steward
        n1["fa:fa-user Create or Maintain General Data for Work Center"]
        n2["fa:fa-user Maintain Formulas"]
        n3["fa:fa-user Maintain Standard Value Key for Routing"]
        n4["fa:fa-user Maintain Cost Center Data"]
        n5["fa:fa-user Maintain Activity Types"]
        n11(["fa:fa-stop Work Centers Created"])
    end
    n5 --> n2
    n10 --> n9
    n9 --> n6
    n2 --> n11
    n3 --> n4
    n1 --> n3
    n4 --> n5
    n6 --> n7
    n7 --> n8
    n8 --> n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 serviceTask
    class n10 startEvt
    class n11 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl2P2jgU_StWRiN2pSDlk4Q8rMQEUlXbSqthtn3o9MEkDlhjbGo7zLAj_vtekxASGqRK5WE053DPOb7XscO7lYuCWIl1f_9OOdUJeh_pDdmSUYJGK6zIyEY18QVLileMqJGpKQXXS_rfqcwNdm-mzHAZ3lJ2MOySrAVB_3600QyEzEYKczVWRNJyZI92km6xPKSCCWmq70hcOuUprfnqQciCyEuB40RuHoKUUU4utB8FUZAZnSK54EXPtAzLuMxHR7M4Jl7zDZb6tPxKkc_47Sst9AZwiZkiULPRW_YJrwgzPWpZGS6v5P48DKpMDoeBLXc4p3wNfOAAJTF_uVChczyi4_39M29D0afHZ47gkzOs1JyUSGmgF3uNSspYcheksyx0bKWleCHJnbeI5r5n56aTBFp3bDPc8Suh641OVoIVTen41fSQeLs3W74lnmPLA_y9yiK8uCSlEy_24jbpIXJTNz0nlWX5W0kwV_mE1UuTtfAzL5u3WW44CVPnZ79zm_MgmrnXcyJyT3PSMc2yzF9cRrWYhK5z2_Qh8ydOemW6xpq84sPFcJoGrWEWRpkb3TSs865XWa3-kSI_G_qLMAtbw-jBzWbeTcNg5gZxs0LwWUu826DsaYk-ZmiMwLaock0FB5AKpdEsz0XFNea61pgPn3x7tkqclHhstsCo9rQgaAllcCQK9AWziqhn63tHEw1rTiEp4Ro4UEOepnuqD-jpsCMK7Qec4mGnTMhtxTCCCZm7BXroy6bfWl0u1lAGkVs43eiR_KioJAX8w8geOkVfhXxpFmWyuy6u80drs2Owq51alEqCT8M7W4L4z1oMp-KXhv4ZK-M0xxrDPOG5kUU3vd_6KY8gIUFGYZMoRx8IJxKz2qCEbzrr68_D63u1Ds0cr4bu36ju7zn6mxxOqY-i0nA_9T2CGx7dZ8Csu68Kb6j6T0pf47qXXVJa7Ho72oxtaHN4iMbjv2A2DXSdGk8bPK3hpIFeDd3mGuF-jYOzuoZ-A4Mahg2c1DBqYFTDuIFxY905-sbwfOX1aG-Y9ofpYJgOh-nJMB0N0_EwPe1erP2OnPbd1Ofd5j1i2dYWzimmhZW8W6ffBvD7oSAlrpi2jraFKy2WB55byekdalW7AjZ3TjGcsm1NHv8HKvyv-Q==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.10 M-090-290_Process_Routing_(IF) — M-090-290_Process_Routing_(IF)

**Swim Lanes**: FTS IF - Batch User · FTS IF - Production - Master Data Steward · IT Department · Production Supervisor | **Tasks**: 13 | **Gateways**: 5

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
    subgraph FTS IF - Batch User
        n6["fa:fa-user Create UPID Specific Routing Group by Assigning Reference Operation Set"]
        n7["fa:fa-user Create Alternate Routing with Group Counter by Assigning Reference Operation Set"]
        n8["fa:fa-user Create Production Version"]
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch Routing Group Exists for UPI at the Plant?"}}
    end
    subgraph FTS IF - Production - Master Data Steward
        n5["fa:fa-user Resolve Error with IT and Manufacturing"]
    end
    subgraph IT Department
        n3["fa:fa-user Separate Operations By Stage And Assign Stage"]
        n4["fa:fa-user Publish MES Routing with SFPID and Stage"]
        n9["Send Alert Notification"]
        n10["Identify Unique Product Identifier (UPI) from SFPID, Stage and Plant"]
        n11["Identify Reference Operation Set by MES Route Name, Stage and Plant"]
        n12["Check Reference Operation Set Already Assigned to UPI at Plant"]
        n13["Check Routing Group Exists for UPI at Plant"]
        n15(["fa:fa-stop Process Routing Created"])
        n16{{"fa:fa-code-branch Reference Operation Set Already Assigned to UPI at Plant?"}}
        n17{{"fa:fa-code-branch If Failure Occurs?"}}
        n18{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Production Supervisor
        n1["fa:fa-user Assign New Shop Floor Production ID (SFPID) With MES Route"]
        n2["fa:fa-user Load MES Routing by SFPID"]
        n14(["fa:fa-play Routing Creation Required"])
    end
    n1 --> n2
    n14 --> n1
    n11 --> n12
    n6 --> n19
    n4 --> n10
    n2 --> n3
    n19 --> n8
    n8 --> n17
    n7 --> n19
    n3 --> n4
    n20 -->|"Yes"| n7
    n20 -->|"No"| n6
    n10 --> n11
    n12 --> n16
    n5 --> n18
    n18 --> n15
    n16 -->|"No"| n13
    n16 -->|"Yes"| n18
    n17 -->|"Yes"| n9
    n17 -->|"No"| n18
    n13 --> n20
    n9 --> n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n14 startEvt
    class n15 endEvt
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11v4jgU_StWRhUzEkhJSAjwsCMKZFRppls10xmtln0wiQNWg521nbZsh_--1xCHJA0a7SwPLT6-95z75cS8WjFPiDW1rq5eKaNqil57akt2pDdFvTWWpNdHJ-AbFhSvMyJ72iblTEX0n6OZ4-Uv2kxjId7RbK_RiGw4QQ83fTQDx6yPJGZyIImgaa_fywXdYbGf84wLbf2OjFM7PaqVW9dcJEScDWw7cGIfXDPKyBkeBl7ghdpPkpizpEGa-uk4jXsHHVzGn-MtFuoYfiHJF_zynSZqC-sUZ5KAzVbtss94TTKdoxKFxuJCPJliUKl1GBQsynFM2QZwzwZIYPZ4hnz7cECHq6sVq0TR5_sVQ_CJMyzlgqRIKoCXTwqlNMum77z5LPTtvlSCP5LpO3cZLIZuP9aZTCF1u6-LO3gmdLNV0zXPktJ08KxzmLr5S1-8TF27L_bwt6VFWHJWmo_csTuulK4DZ-7MjVKapv9LCeoqvmL5WGoth6EbLiotxx_5c_stn0lz4QUzp10nIp5oTGqkYRgOl-dSLUe-Y18mvQ6HI3veIt1gRZ7x_kw4mXsVYegHoRNcJDzptaMs1neCx4ZwuPRDvyIMrp1w5l4k9GaONy4jBJ6NwPkWhV8jdBOiAbrGKt6iByjDyUJ_2OjPlZXiaYoHuuBoLggkhB7ubhYoyklMUxqje14omEf0SfAiR-s9mklJN0xD9yQlgrCYoN9zIrCinKGIqJX1V00j6NSYZYoIpr8Z_meqtqXInBcMtn9BbNwpBiVNivjo8Y0ICf-bXs7k9dX46cfYYA0HEapFXuKskPSJfDr1eWUdDjU31-52a1Zs-UKlkijlQhcWYYXgMYjuMszUxzMhHK1LnatFP0BfsNSVWWCFUaSDEkktIr-Z_j2RPHsiaCkEqB8LfPMVYZYADStSHKtCQKBVMd4GAeYLksMTZkeYqgkNm0KRttGVrloj0fUeAsQbaDXondp4Apq195pMd8U6o3KLviyj5mREoZ5KHXsHyQRIIqJ1MgIPyVuu9OgeA2l12gbLmwSSoekePTD6d1GNBypxCmG8h1Z9QKngu5Nwv8xF6x9b16J16rQXJlWPs0mLoFu8Iz9jdYF1viXx40XKWQYTnphjQhKkuJmyLsLhmfAnM9rl7b-veiUVz3XdYiJlxXU6bQl4fai7jS6ckl9M6WPrFDpBN_9NikJMs0KAQAxvX_nGcfxfT_3b81E7m1GR61eM5PUHrNOc7vIY3JJnFG2hgmHGoeQ1Ehjx98eB-4C-66mv5qXZCrdJ-5njpHFiYNKOLK0GeucG5hm8thqN0_L35O-CinoLq5SZgwaD30DaLL3T2jHrct8xBqNyPSnXxr585TH3tB4a_8lpPS7X49I8KNdBi254WnuGzdbrHyvrDyJX1g-wb2_c8iM-Mnp2SVglUAbkGAu_XJuIHBOSb4BRk9oZtjdMMGeOoLUzaW8YrsqjTNRckVhZJ792c9DNMTemBux2w8Nu2OuG_W541A0H3fC4G4YpMhfYJu6Xl80mOjI3riYcdMPjbnjSCcOclLDVt3ZE7DBNrOmrdfzNAr9rEpLiIlPWoW_hQvFoz2JrerzbW0WegOeCYngm7E7g4V-8fRtt" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.11 M-090-300_Process_Reference_Operation_Set_(IF) — M-090-300_Process_Reference_Operation_Set_(IF)

**Swim Lanes**: IT Department · Master Data Steward - Production · Production Supervisor | **Tasks**: 35 | **Gateways**: 8

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
    subgraph IT Department
        n2["Send Alert Notification"]
        n3["Send Alert Notification"]
        n5["Create Operations 1 per Area"]
        n6["Assign Count of Operations as Number of Planned Moves in Each Operation"]
        n7["Determine and Assign Work Center by Area"]
        n8["Add Standard Values per Operation​"]
        n9["Create Operations 1 per Module"]
        n10["Determine and Assign Work Center by Module​"]
        n11["Determine Count of Operations by Area"]
        n12["Verify Operations by Module"]
        n13["Adjust Planned Number of Moves per Operation​"]
        n14["Add New Operations if New FAB Area found with Number of Planned Moves​"]
        n15["Determine and Assign Work Center for new FAB Area​"]
        n16["Add Standard Values per Operation​"]
        n17["Add or Remove Operation for Module"]
        n18["Verify Sequence of Operations"]
        n19["Add or Remove Operation for Module"]
        n20["Determine and Assign Work Center for new Fab Area"]
        n21["Add Standard Values for New Operations"]
        n22["Create Operations MES/WS operation"]
        n23["Add Standard Values per Operation"]
        n24["Add Activity Types"]
        n25["Determine and Assign Work Center"]
        n26["Add Standard Values per Operation"]
        n27["Check Reference Operation (ROS) Set Exists by Route Name Process Stage and Plant"]
        n28["Determine and Assign Work Center by Module"]
        n29["Add Standard Values per Operation​"]
        n30["Add Activity Types"]
        n31["Reference Operation Set Created"]
        n32["Reference Operation Set Changed"]
        n33["Separate Operations by Stage and Assign Stage"]
        n34["Publish MES Flow, Routing, Stage, Operations, Plant and Process"]
        n35["Determine SAP Plant"]
        n37(["fa:fa-stop Reference Operation Set Changed"])
        n38(["fa:fa-stop Reference Operation Set Created"])
        n40{{"fa:fa-code-branch Stage of Manufacturing?"}}
        n41{{"fa:fa-code-branch ROS Exists?"}}
        n42{{"fa:fa-code-branch exclusiveGateway"}}
        n43{{"fa:fa-code-branch Stage of Manufacturing?"}}
        n44{{"fa:fa-code-branch exclusiveGateway"}}
        n45{{"fa:fa-code-branch If Failure Occurs?"}}
        n46{{"fa:fa-code-branch If Failure Occurs?"}}
    end
    subgraph Master Data Steward - Production
        n1["fa:fa-user Resolve Error with IT and Manufacturing"]
        n39(["fa:fa-stop Error Resolved and Reference Operation Set Changed"])
        n47{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Production Supervisor
        n4["Check MES Flow Plan/Work Stream Route with Route Name"]
        n36(["fa:fa-play Reference Operation Set Creation Initiated"])
    end
    n34 --> n27
    n36 --> n4
    n5 --> n6
    n6 --> n7
    n7 --> n8
    n9 --> n10
    n11 --> n13
    n13 --> n14
    n14 --> n15
    n15 --> n16
    n16 --> n44
    n8 --> n30
    n4 --> n33
    n41 -->|"Yes/Change"| n43
    n18 --> n19
    n19 --> n20
    n20 --> n21
    n40 -->|"Others"| n22
    n23 --> n24
    n24 --> n42
    n22 --> n25
    n25 --> n26
    n27 --> n41
    n40 -->|"WLA"| n9
    n33 --> n35
    n35 --> n34
    n12 --> n17
    n28 --> n29
    n17 --> n28
    n21 --> n44
    n41 -->|"No/Create"| n40
    n30 --> n42
    n10 --> n23
    n26 --> n42
    n42 --> n31
    n44 --> n32
    n31 --> n45
    n29 --> n44
    n43 -->|"Wafer Level Assembly (WLA)"| n12
    n40 -->|"Fabrication+BUMP"| n5
    n32 --> n46
    n43 -->|"Fabrication (FAB)"| n11
    n3 --> n47
    n45 -->|"Yes"| n2
    n47 --> n1
    n1 --> n39
    n43 -->|"Others"| n18
    n45 -->|"No"| n38
    n46 -->|"Yes"| n3
    n46 -->|"No"| n37
    n2 --> n47
    class n1 userTask
    class n36 startEvt
    class n37 endEvt
    class n38 endEvt
    class n39 endEvt
    class n40 gateway
    class n41 gateway
    class n42 gateway
    class n43 gateway
    class n44 gateway
    class n45 gateway
    class n46 gateway
    class n47 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWG1vozgQ_isWqypdXaJiAyHJhzuleTlV2narTXer0_U-OGASrgRy2LTNdfPfbww2BEp3014-VGWYZ56ZZ8bG8Gx4ic-MkXFy8hzGoRih545Ysw3rjFBnSTnrdFFh-EbTkC4jxjvSJ0hisQj_zd2wvX2SbtI2p5sw2knrgq0Shr5edNEYgFEXcRrzHmdpGHS6nW0abmi6myRRkkrvD2wQmEHOpm6dJ6nP0srBNF3sOQCNwphVZsu1XXsucZx5SezXggZOMAi8zl4mFyWP3pqmIk8_4-ySPt2GvljDdUAjzsBnLTbRJ7pkkaxRpJm0eVn6oMUIueSJQbDFlnphvAK7bYIppfF9ZXLM_R7tT07u4pIU3UzvYgQ_L6KcT1mAuADz7EGgIIyi0Qd7Mp47ZpeLNLlnow9k5k4t0vVkJSMo3exKcXuPLFytxWiZRL5y7T3KGkZk-9RNn0bE7KY7-NvgYrFfMU36ZEAGJdO5iyd4opmCIPhfTKBrekP5veKaWXMyn5Zc2Ok7E_NlPF3m1HbHuKkTSx9Cjx0Enc_n1qySatZ3sPl60PO51TcnjaArKtgj3VUBhxO7DDh33Dl2Xw1Y8DWzzJbXaeLpgNbMmTtlQPccz8fk1YD2GNsDlSHEWaV0u0YXN2jKtjAiGxaL4p78xeTPO2MB_UTjiMFYXSUiDEKPijCJ74y_DhytYx0dcJykDBRBn7cszT04wgj-h5XLaN27D95jzsNVjCZJFguUBIcwytFVtlkCFOzXEY1j5qPL5IFxFMZoRr115V0P7ELgKRMs3cDyRlQmXtDcJuk9moAKEHS5a0lpIFPyfbQQVC5_H32jUQaEsoCKLCOmuawDhz-o_DLxs4jV_bF5ZI4K3EKJcS1Em4StNWLZ929y79w1fFsTtXJJ_s64KJtQtaVox0_VwbbS9Yo9HnKGQW6Zj8_zPFEANfjoMRTr11rfGt05RssgSVF8QNYaqf_e_mNXIYHlC9tAqpV_Tt2q7aDqxIL9k7HYY_UONvyH7yAh5pvUocuWkSH4FV0krN7TBpC0rovL2eLsdoGS9uVLrKO6UMfoCRt7InwIxQ7d7Lasmc0xg9KA9N-Ri5yFyZp599ClgKV5W6tGnX75vPgI_RZo9hRyka-8L0kGCl3RDUNy72ecS8JVkaNcAKJBMXjb9lEHD9875ZZ5hMqWHJa2wmXJxSz4DQT5EWJN49ULRPFIgodaY7Kg5Eo4JUluaODluFxnyyjkazmNaA6nq27eBjh3dQtI9yBwt-hC0Y-iQ42I9dlajK_b-ma5p-AW0FFAe1wkW_Tzqj8ewgfHwkuZD-G2-fys4fKo3lvCYRMeo4VicjuncRZQT2QpqPDbnbHfH6JxOxrGWU3yCwRpR7AnL8p4-MB-L85OTZj1v9K030fqtMMuAtgTwyhLQWIPDvAvi-y_HQhnqcYZ7ZJyuWKnVFCoE_KDVdmTk-ZnXr4aD54C5QjIEzKMAE8ieBLM0hQ24_zZCQc-Oac1mRpzOGwMUoFWsfwc_rbRtN23yv5ShKpctMi28rDOk_SQo9xX9ZLN19hZvuctBMz8Ru2kuQzVptoovl8Vv43g6P7DVSQvLuBtNqwvqDJ72EtQr_er3Pa1oV8YbHXtFJd9danuam-3uByoy2FxidVbAZzylMHSBksZdHis-LGjDYoQa0asE9KQQXFtaRIVwdIcdk76_c74g_Gzot93xne5MnVEFQEPtUHlrd_i4B9lwDqmqWJ-hk8AKc_jEaK9VVFEZ0hUSnbpQZSHrpKoKomukigl7ReMt5_GOZ1O1lJslo5lqVhWqaliw7pLRBVMyoIVG9GNI7ghciniVXJW7MeFhlohy2yUiLVkWmXSb3jYKi2rLFF3TntYOotSpmEzLUurQmHq0Sf2wCL5pGSbZbRDp6DVxzxPTJoywtkwVa99v5x_vbzO3UoJVWp2v8lzAEOncPpW4XUJqhe2Vtp2qtkrhkTfUIproKrUGjYJDwYMD5pRr5L8hlXe6DforOYNjShHoZ5w_t4us9HfK2pm2Av015m63VVfUurWQat12GaFtqhPD3UzbjeTdrPVbrbbzU67ud9udrXZ6BobOBfR0DdGz0b-BRC-EvosoFkkjH3XoJlIFrvYM0b5lzIj2_qAnIYUngubwrj_D8f1PQY=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.12 M-090-430_Process_Production_Version_(IF) — M-090-430_Process_Production_Version_(IF)

**Swim Lanes**: FTS IF - Production - Master Data Steward · FTS IF Batch System ID · IT Department · Production Supervisor | **Tasks**: 13 | **Gateways**: 5

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
    subgraph FTS IF - Production - Master Data Steward
        n5["fa:fa-user Resolve Error with IT and Manufacturing"]
    end
    subgraph FTS IF Batch System ID
        n6["fa:fa-user Create Production Version"]
        n7["fa:fa-user Create UPID Specific Routing Group by Assigning Reference Operation Set"]
        n8["fa:fa-user Create Alternate Routing with Group Counter by Assigning Reference Operation Set"]
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch Routing Group Exists for UPI at the Plant?"}}
    end
    subgraph IT Department
        n3["fa:fa-user Separate Operations By Stage And Assign Stage"]
        n4["fa:fa-user Publish MES Routing with SFPID and Stage"]
        n9["Send Alert Notification"]
        n10["Identify Unique Product Identifier (UPI) from SFPID, Stage and Plant"]
        n11["Identify Reference Operation Set by MES Route Name, Stage and Plant"]
        n12["Check Reference Operation Set Already Assigned to UPI at Plant"]
        n13["Check Routing Group Exists for UPI at Plant"]
        n15(["fa:fa-stop Process Routing Created"])
        n16{{"fa:fa-code-branch Reference Operation Set Already Assigned to UPI at Plant?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
        n18{{"fa:fa-code-branch If Failure Occurs?"}}
    end
    subgraph Production Supervisor
        n1["fa:fa-user Assign New Shop Floor Production ID (SFPID) With MES Route"]
        n2["fa:fa-user Load MES Routing by SFPID"]
        n14(["fa:fa-play Routing Creation Required"])
    end
    n1 --> n2
    n14 --> n1
    n11 --> n12
    n4 --> n10
    n2 --> n3
    n19 --> n6
    n17 --> n15
    n8 --> n19
    n3 --> n4
    n20 -->|"Yes"| n8
    n16 -->|"Yes"| n17
    n12 --> n16
    n20 -->|"No"| n7
    n10 --> n11
    n7 --> n19
    n16 -->|"No"| n13
    n13 --> n20
    n9 --> n5
    n6 --> n18
    n18 -->|"Yes"| n9
    n5 --> n17
    n18 -->|"No"| n17
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n14 startEvt
    class n15 endEvt
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11v4jgU_StWRhUzEkhJSAjlYUcUyAhp2q2adkarZR9M4oDVYDO205bt8N_3OokDyaQ72lkeWnxy7zn3y455tWKeEGtiXVy8UkbVBL321JbsSG-CemssSa-PSuALFhSvMyJ72iblTEX078LM8fYv2kxjId7R7KDRiGw4QQ_LPpqCY9ZHEjM5kETQtNfv7QXdYXGY8YwLbf2OjFM7LdSqR1dcJEScDGw7cGIfXDPKyAkeBl7ghdpPkpizpEGa-uk4jXtHHVzGn-MtFqoIP5fkGr98pYnawjrFmSRgs1W77DNek0znqESusTgXT6YYVGodBgWL9jimbAO4ZwMkMHs8Qb59PKLjxcWK1aLo892KIfjEGZZyTlIkFcCLJ4VSmmWTd95sGvp2XyrBH8nknbsI5kO3H-tMJpC63dfFHTwTutmqyZpnSWU6eNY5TNz9S1-8TFy7Lw7wt6VFWHJSmo3csTuula4CZ-bMjFKapv9LCeoq7rF8rLQWw9AN57WW44_8mf0jn0lz7gVTp10nIp5oTM5IwzAcLk6lWox8x36b9CocjuxZi3SDFXnGhxPh5cyrCUM_CJ3gTcJSrx1lvr4VPDaEw4Uf-jVhcOWEU_dNQm_qeOMqQuDZCLzfovA-QssQDRDQJnmsKGewuMZSEYHmWGEU6RREUvrpD_P_XFkpnqR4oNuA7ojk2RNBCyG4QM9UbdHyHmGWAA3LUxyrXMDArqy_Sg6Yku4grrCKtyg6gPYOLedniqOm4kwQKOx5yF-IkPC_1ii8gk6vh9vlHEV7EtOUxuiO5wqCQ58Ez_dofUBTKemGaeiOpEQQFhP0-54IXOhERDU1xp0a0wzKx_Q3w1-UpRSZ8Zzp6v53Mefy9dXI6eN0sIYDAUpGXuIsl_SJfCrnbWUdj2durt3t1sx98UKlkiiFHkKJEFYIjmN0m2GmPp4If2we9HpO9nDI7AhTZ6rDZmUibaMrUucn0dUBpgtvoF4wLGUtSqCZttdkus3XGZVbdL2ImuWNQt1aPXgdJJdAEhGtkxE4J2-40v0vAmkV2QbLZQLJ0PSAHhj9ltejhiqcQhjvoUofUCr4rhTuV7lo_aJqLVrnnPaNduuZMGkRdIN35GesLrDOtiR-fJNymsFMJmbWSIIUNw3uIhyeCH8yHl3e_vu6V1Lxva5bTKSsucr9kYDXh3O30RsD-ospfWxtACf4pX3jjLvdlikKMc1yAXHF8N6W_7o_zk6pKN_rt4zk4lylOd3VNrghzyjaQgXDjEPJz0hgxN8XA_cBfdVTX89LsxVuk_Yzx0ljx8CkFSytBnqnBu4zeHM1Gqfl78i3nIrzFtYpMwcNBr-BtFl65dox6-q5YwzM8-otx9xyPTT2l-V6ZNZBZe9XwLhaX1brYbn2DJ2t199X1h9ErqzvYG-IRq0HTmCeVCE4ozbHDS8sa0O7MjTJBa1Yao3K0amzqqI0dxpWZWmSGlVEdbDjVrBGwa8Mg7ahUQzOLg-6OebS1IDdbnjYDXvdsN8Nj7rhoBsed8MwReYO28T96r7ZREfm0tWEg2543A1fdsIwCxVs9a0dETtME2vyahU_W-CnTUJSnGfKOvYtnCseHVhsTYrrvZXvE_CcUwxnwq4Ej_8AR88csg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Batch User | M-090-050_Identify_Consumable_Material_Requirements_(IF),  | |
| Boundary Apps | M-090-050_Identify_Consumable_Material_Requirements_(IF), M-090-080_Re-schedule_Planned_Order_(IF),  | |
| Master Data Steward | M-090-050_Identify_Consumable_Material_Requirements_(IF),  | |
| Production Scheduler | M-090-050_Identify_Consumable_Material_Requirements_(IF),  | |
| FTS IF - Materials Planner | M-090-060_Schedule_Consumable_Material_Requirements_(IF), M-090-110_Initiate_Production_Order_Creation_(IF),  | |
| LOG IF Batch User | M-090-060_Schedule_Consumable_Material_Requirements_(IF),  | |
| Material Handler | M-090-060_Schedule_Consumable_Material_Requirements_(IF),  | |
| PTP System ID | M-090-060_Schedule_Consumable_Material_Requirements_(IF),  | |
| FTS IF - Production Scheduler | M-090-080_Re-schedule_Planned_Order_(IF),  | |
| IT Department | M-090-080_Re-schedule_Planned_Order_(IF), M-090-110_Initiate_Production_Order_Creation_(IF), M-090-210_Identify_Change_in_Production_Data_(IF), M-090-250_Execute_Change_(IF), M-090-290_Process_Routing_(IF), M-090-300_Process_Reference_Operation_Set_(IF), M-090-430_Process_Production_Version_(IF) | |
| FTS IF - Production Planner | M-090-090_Check_for_Material_Availability_(IF), M-090-180_Expedite_Missing_Material_(IF),  | |
| Factory Supervisor | M-090-110_Initiate_Production_Order_Creation_(IF),  | |
| FTS IF - Batch User | M-090-210_Identify_Change_in_Production_Data_(IF), M-090-250_Execute_Change_(IF), M-090-290_Process_Routing_(IF),  | |
| FTS IF - Production - Master Data Steward | M-090-210_Identify_Change_in_Production_Data_(IF), M-090-280_Process_Work_Centers_(IF), M-090-290_Process_Routing_(IF), M-090-430_Process_Production_Version_(IF) | |
| FTS IF - System Batch ID (RFC User) | M-090-210_Identify_Change_in_Production_Data_(IF), M-090-250_Execute_Change_(IF),  | |
| Production Supervisor | M-090-210_Identify_Change_in_Production_Data_(IF), M-090-250_Execute_Change_(IF), M-090-290_Process_Routing_(IF), M-090-300_Process_Reference_Operation_Set_(IF), M-090-430_Process_Production_Version_(IF) | |
| Master Data Steward - Production | M-090-250_Execute_Change_(IF), M-090-300_Process_Reference_Operation_Set_(IF),  | |
| FTS IF - Production - Cost Accountant | M-090-280_Process_Work_Centers_(IF),  | |
| FTS IF Batch System ID | M-090-430_Process_Production_Version_(IF) | |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for M-090. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
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
| FTSR1466 | Report | Custom ABAP report for SIMS PO Exceptions​ | 10. Object Complete |  |  | 03.Medium |
| FTSR1364 | Report | Factory Portal - Warranty Claim (Warranty Dashboard​​) | 10. Object Complete |  |  | 02.High |
| FTSR1011 | Report | Report- Custom Fiori report to show full parts tracking status dashboard (wor... | 10. Object Complete |  |  | 02.High |
| LOGM024_IF | Conversion | Create/Upload Vehicle resource | 10. Object Complete |  |  | N/A |
| LOGM023_IF | Conversion | Update Business Share | 10. Object Complete |  |  | N/A |
| LOGM022_IF | Conversion | Upload Transportation Allocation | 10. Object Complete |  |  | N/A |
| LOGM021_IF | Conversion | Upload Schedules | 10. Object Complete |  |  | N/A |
| LOGM019_IF | Conversion | Default Routes | 10. Object Complete |  |  | N/A |
| LOGM018_IF | Conversion | Upload Rate Table | 10. Object Complete |  |  | N/A |
| LOGM016_IF | Conversion | Create and review Charge Calculation Sheet | 10. Object Complete |  |  | N/A |
| LOGM015_IF | Conversion | Create and review Freight Agreement | 10. Object Complete |  |  | N/A |
| LOGM012_IF | Conversion | Creation of Location based on BP, Shipping points, plants | 10. Object Complete |  |  | N/A |
| LOGM008_IF | Conversion | Location creation-ocean ports, airports | 10. Object Complete |  |  | N/A |
| LOGM007_IF | Conversion | Storage Bin Upload | 10. Object Complete | WIINGS | EWM | N/A |
| LOGM006_IF | Conversion | Product Master conversion (additional EWM attribution) | 10. Object Complete | WIINGS, ECC WM | EWM | N/A |
| LOGM005_IF | Conversion | UPLOAD TRANSPORTATION ZONES (TM) | 10. Object Complete |  |  | N/A |
| LOGM004_IF | Conversion | UPLOAD TRANSPORTATION LANES | 10. Object Complete |  |  | N/A |
| LOGC0972_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  |  | 02.High |
| LOGC0971 | Conversion | Open Inventory Conversion for IP and IF (as applicable) , WIINGs to EWM | 10. Object Complete |  |  | 02.High |
| LOGC0970 | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC/WM to EWM | 10. Object Complete |  |  | 02.High |
| LOGC0946_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  |  | 02.High |
| FTSM0986 | Conversion | Convert Equipment Warranty information to SAP S/4 Equipment Master – reusable... | 10. Object Complete |  |  | 02.High |
| FTSM019 | Conversion | Conversion of Inflight Work Orders | 10. Object Complete |  |  | N/A |
| FTSM018 | Conversion | Conversion of General Task List | 10. Object Complete |  |  | N/A |
| FTSM017_IF | Conversion | Manual Conversion of Functional Locations (FLOC) | 10. Object Complete |  |  | 03.Medium |
| FTSM016 | Conversion | Equipment Master | 10. Object Complete | MES, SAP ME, EMS, EDFIT, Workstream, NIT, ECM | S4 | N/A |
| FTSM011 | Conversion | Catalogs | 10. Object Complete |  | S4 | N/A |
| FTSM010 | Conversion | Maintenance Plans | 10. Object Complete | ME | S4 | N/A |
| FTSM009 | Conversion | Maintenance Items | 10. Object Complete | NA | S4 | N/A |
| FTSM008 | Conversion | Equipment Class | 10. Object Complete | NA | S4 | N/A |
| FTSM007 | Conversion | Characteristics | 10. Object Complete | NA | S4 | N/A |
| FTSM002_IF | Conversion | Work Center | 10. Object Complete | Fuzion, ME, Manual | S4 | N/A |
| FTSC1550 | Conversion | Inventory Conversion | 02. FS Unplanned |  |  | 03.Medium |
| FTSC0052_IF | Conversion | Conversion of Reference Operation Sets to S/4 | 10. Object Complete | ECC | S4 | 02.High |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for M-090.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for M-090.

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

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| LOGW1078_IF | Workflow | ISM Workflows - Capital/AMT | 10. Object Complete |  | NA | 03.Medium |
| LOGW1077_IF | Workflow | ISM Workflows - EIMS/Lab | 10. Object Complete |  | NA | 03.Medium |
| LOGW1076_IF | Workflow | ISM Workflows - Non-inventory | 10. Object Complete |  | NA | 03.Medium |
| LOGR1176_IF | Report | ISM - International Traffic Report | 10. Object Complete |  | NA | 03.Medium |
| LOGR0833_IF | Report | Email Notification for deletion of Shipping Memos | 10. Object Complete |  | NA | 04.Low |
| LOGM024_IF | Conversion | Create/Upload Vehicle resource | 10. Object Complete |  | NA | N/A |
| LOGM023_IF | Conversion | Update Business Share | 10. Object Complete |  | NA | N/A |
| LOGM022_IF | Conversion | Upload Transportation Allocation | 10. Object Complete |  | NA | N/A |
| LOGM021_IF | Conversion | Upload Schedules | 10. Object Complete |  | NA | N/A |
| LOGM019_IF | Conversion | Default Routes | 10. Object Complete |  | NA | N/A |
| LOGM018_IF | Conversion | Upload Rate Table | 10. Object Complete |  | NA | N/A |
| LOGM016_IF | Conversion | Create and review Charge Calculation Sheet | 10. Object Complete |  | NA | N/A |
| LOGM015_IF | Conversion | Create and review Freight Agreement | 10. Object Complete |  | NA | N/A |
| LOGM012_IF | Conversion | Creation of Location based on BP, Shipping points, plants | 10. Object Complete |  | NA | N/A |
| LOGM008_IF | Conversion | Location creation-ocean ports, airports | 10. Object Complete |  | NA | N/A |
| LOGM007_IF | Conversion | Storage Bin Upload | 10. Object Complete | WIINGS → EWM | NA | N/A |
| LOGM006_IF | Conversion | Product Master conversion (additional EWM attribution) | 10. Object Complete | WIINGS, ECC WM → EWM | NA | N/A |
| LOGM005_IF | Conversion | UPLOAD TRANSPORTATION ZONES (TM) | 10. Object Complete |  | NA | N/A |
| LOGM004_IF | Conversion | UPLOAD TRANSPORTATION LANES | 10. Object Complete |  | NA | N/A |
| LOGI1718 | Interface | To align on batch attributes for straddle in S4 | 08. FUT In Progress |  | NA | 03.Medium |
| LOGI1708 | Interface | Wrapper program for Inbound interface from Kommand AS to SAP | 10. Object Complete |  | Apigee | 03.Medium |
| LOGI1677 | Interface | Send 4C1 Inventory Reconciliation Snapshot to IP | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1676 | Interface | Send 4C1 Inventory movement Stock type change and cycle count to IP | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1675 | Interface | Interface for SiGaC to extract inventory data from EWM to meet their existing... | 06. Dev In Progress |  | NA | 03.Medium |
| LOGI1626 | Interface | Inventory adjustment data in XML format from Kommand auto-store to SAP EWM | 06. Dev In Progress |  | APIGEE | 03.Medium |
| LOGI1595 | Interface | Summary Reconciliation and Inventory Snapshot data in XML format from SAP EWM... | 10. Object Complete |  | APIGEE | 02.High |
| LOGI1594 | Interface | Pickresult(Pick Warehouse task confirmation) data in XML format from SAP EWM ... | 06. Dev In Progress |  | APIGEE | 02.High |
| LOGI1593 | Interface | Replenresult(Putaway warehouse task confirmation) data in XML format from SAP... | 06. Dev In Progress |  | APIGEE | 02.High |
| LOGI1591 | Interface | MergePick (Pick Warehouse task)data in XML format from SAP EWM to Kommand aut... | 10. Object Complete |  | APIGEE | 03.Medium |
| LOGI1589 | Interface | MergeReplen(Putaway Warehouse task) data in XML format from SAP EWM to Komman... | 10. Object Complete |  | APIGEE | 03.Medium |
| LOGI1587 | Interface | MergeItem (Product master)data in XML format from SAP EWM to Kommand auto-store | 10. Object Complete |  | APIGEE | 03.Medium |
| LOGI1555 | Interface | Straddle Plant to be automatically complete the Goods Receipt and write of th... | 09. FUT Overdue |  | MuleSoft | 03.Medium |
| LOGI1091 | Interface | STO based Outbound Delivery Notification Confirmation for Delivery Note Deletion | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI1084 | Interface | Interface to SiGac for capturing the consumption of Chems and Gases against a... | 10. Object Complete | SIGAC → S/4 | APIGEE | 03.Medium |
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
| LOGF1614_IF | Form | TM-Bill of lading print output ( NSO/ Prospal STO's) | 10. Object Complete |  | NA | 04.Low |
| LOGF1525 | Form | Consolidated Commercial Invoice for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1524 | Form | Commercial Invoice for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1523 | Form | Packing list for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1100_IF | Form | Printing of Standard Shipping Label | 10. Object Complete |  | NA | 03.Medium |
| LOGF1089 | Form | Creation of Forms for Cycle count | 10. Object Complete |  | NA | 03.Medium |
| LOGF1057 | Form | Print Pick List | 10. Object Complete |  | NA | 02.High |
| LOGF1056 | Form | Print Return Label | 10. Object Complete |  | NA | 03.Medium |
| LOGF1055 | Form | Print Pick Label (PM-EWM) | 10. Object Complete |  | NA | 02.High |
| LOGF0359_IF | Form | ISM - Generate Commercial Invoice - IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0358_IF | Form | ISM - Generate Traveler Document - IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0352_IF | Form | ISM - IPLA | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0351_IF | Form | ISM - Custom China Special label | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0350_IF | Form | ISM - India GST DC | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE1691 | Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF a... | 08. FUT In Progress |  | NA | 03.Medium |
| LOGE1690 | Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF a... | 07. FUT Roadblock |  | NA | 03.Medium |
| LOGE1601 | Enhancement | Interface between ECD (Excursion Containment Disposition) and SAP S/4 EWM for... | 06. Dev In Progress |  | NA | 02.High |
| LOGE1596 | Enhancement | Summary Reconciliation and Inventory Snapshot data in XML format from SAP EWM... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1592 | Enhancement | MergePick (Pick Warehouse task)data in XML format from SAP EWM to Kommand aut... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1590 | Enhancement | MergeReplen(Putaway Warehouse task) data in XML format from SAP EWM to Komman... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1588 | Enhancement | MergeItem (Product master)data in XML format from SAP EWM to Kommand auto-store | 10. Object Complete |  | NA | 03.Medium |
| LOGE1572_IF | Enhancement | SAP GUI T-code to Move stock from Blocked to unblock Status | 10. Object Complete |  | NA | 03.Medium |
| LOGE1569_IF | Enhancement | Enhancement to change billing status based on ship reason in ISM | 10. Object Complete |  | NA | 04.Low |
| LOGE1554 | Enhancement | Straddle Plant to be automatically complete the Goods Receipt and write of th... | 09. FUT Overdue |  | NA | 03.Medium |
| LOGE1526_IF | Enhancement | Automatic HAWB assignment for Freight Forwarders( ISM/ Prospal STO's) | 10. Object Complete |  | NA | 03.Medium |
| LOGE1522 | Enhancement | WIP HU overpacking validation for unique TU | 10. Object Complete |  | NA | 03.Medium |
| LOGE1521 | Enhancement | WIP Overpack Label Printing | 10. Object Complete |  | NA | 03.Medium |
| LOGE1520 | Enhancement | Enhancement to enable WIP movement for receiving between Factory to EWM Wareh... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1453 | Enhancement | Trigger the request for cancellation 3B14R and cancel the demand on STO based... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1450 | Enhancement | Inbound idoc processing logic during 3B2 and 3B13 | 10. Object Complete |  | NA | 03.Medium |
| LOGE1415 | Enhancement | Suppress Batch and serial number validation in MIGO/MB26 for movement type 261 | 08. FUT In Progress |  | NA | 03.Medium |
| LOGE1414 | Enhancement | Creation of outbound Delivery for WIP inventory from STO | 10. Object Complete |  | NA | 03.Medium |
| LOGE1276_IF | Enhancement | TM:Replace VTRC and integrate with parcel carrier to retrieve the package lev... | 10. Object Complete |  | NA | 04.Low |
| LOGE1255 | Enhancement | Visibility of New & Old Part Number during RF picking/ issue process | 10. Object Complete |  | NA | 03.Medium |
| LOGE1254 | Enhancement | Print Product Label in SAP EWM after physical inventory document posting | 10. Object Complete |  | NA | 03.Medium |
| LOGE1177_IF | Enhancement | India GST E-invoicing | 10. Object Complete |  | NA | 04.Low |
| LOGE1118_IF | Enhancement | ISM – MY Security Check Fiori app - IF | 10. Object Complete |  | NA | 03.Medium |
| LOGE1117_IF | Enhancement | ISM – Employee acknowledgement - IF | 10. Object Complete |  | NA | 03.Medium |
| LOGE1090_IF | Enhancement | PGI confirmation for non-inventory Intel freight shipments via email | 10. Object Complete |  | NA | 04.Low |
| LOGE1080_IF | Enhancement | Email notifications to be triggered as part of ISM Workflows | 10. Object Complete |  | NA | 03.Medium |
| LOGE1061 | Enhancement | Enhancement for Pop-Up message during Decontamination Process (Copper to Non-... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1059 | Enhancement | RF Capability for Rejection of the Returns to Factory and send notification | 10. Object Complete |  | NA | 03.Medium |
| LOGE1058 | Enhancement | Determine Warehouse Process type for PM Returns | 10. Object Complete |  | NA | 04.Low |
| LOGE1054 | Enhancement | Email/Text Trigger to Factory Technician and Post Goods Issue upon all WO con... | 10. Object Complete |  | NA | 02.High |
| LOGE1052_IF | Enhancement | Custom fields required on delivery screen | 10. Object Complete |  | NA | 04.Low |
| LOGE0935_IF | Enhancement | Fiori App - Shipping Memo | 08. FUT In Progress |  | NA | 02.High |
| LOGE0835_IP | Enhancement | Interface to get the AMT (Asset Management Tool) data on the ISM | 10. Object Complete |  | NA | 03.Medium |
| LOGE0405_IF | Enhancement | Dangerous Goods indicator from the delivery header text to be transmitted to ... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0403_IF | Enhancement | In SAP TM, update FU and FO Transportation Cockpit w/ custom fields Purchase ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0239_IF | Enhancement | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 - Table Creation | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0190_IF | Enhancement | Delivery Split for STO in S/4 | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGC0972_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  | NA | 02.High |
| LOGC0971 | Conversion | Open Inventory Conversion for IP and IF (as applicable) , WIINGs to EWM | 10. Object Complete |  | NA | 02.High |
| LOGC0970 | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC/WM to EWM | 10. Object Complete |  | NA | 02.High |
| LOGC0946_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  | NA | 02.High |
| FTSW1372 | Workflow | Factory Portal - Equipment to Parts Management (Custom Fields – Part Check ou... | 03. FS Not Started |  | NA | 03.Medium |
| FTSR1466 | Report | Custom ABAP report for SIMS PO Exceptions​ | 10. Object Complete |  | NA | 03.Medium |
| FTSR1364 | Report | Factory Portal - Warranty Claim (Warranty Dashboard​​) | 10. Object Complete |  | NA | 02.High |
| FTSR1011 | Report | Report- Custom Fiori report to show full parts tracking status dashboard (wor... | 10. Object Complete |  | NA | 02.High |
| FTSM0986 | Conversion | Convert Equipment Warranty information to SAP S/4 Equipment Master – reusable... | 10. Object Complete |  | NA | 02.High |
| FTSM019 | Conversion | Conversion of Inflight Work Orders | 10. Object Complete |  | NA | N/A |
| FTSM018 | Conversion | Conversion of General Task List | 10. Object Complete |  | NA | N/A |
| FTSM017_IF | Conversion | Manual Conversion of Functional Locations (FLOC) | 10. Object Complete |  | NA | 03.Medium |
| FTSM016 | Conversion | Equipment Master | 10. Object Complete | MES, SAP ME, EMS, EDFIT, Workstream, NIT, ECM → S4 | NA | N/A |
| FTSM011 | Conversion | Catalogs | 10. Object Complete |  → S4 | NA | N/A |
| FTSM010 | Conversion | Maintenance Plans | 10. Object Complete | ME → S4 | NA | N/A |
| FTSM009 | Conversion | Maintenance Items | 10. Object Complete | NA → S4 | NA | N/A |
| FTSM008 | Conversion | Equipment Class | 10. Object Complete | NA → S4 | NA | N/A |
| FTSM007 | Conversion | Characteristics | 10. Object Complete | NA → S4 | NA | N/A |
| FTSM002_IF | Conversion | Work Center | 10. Object Complete | Fuzion, ME, Manual → S4 | NA | N/A |
| FTSI1702 | Interface | Interface to transfer Vendor details from S4 to DMRA on a daily basis | 02. FS Unplanned | S/4 → DMRA | MULESOFT | 03.Medium |
| FTSI1680 | Interface | An interface from Prospal to create lot level STO in S4 for the straddle solu... | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1667 | Interface | Interface to transfer BOM details from S4 to DMRA on a daily basis | 02. FS Unplanned | S/4 → DMRA | MULESOFT | 03.Medium |
| FTSI1654 | Interface | Interface to transfer Material Master details from S4 to DMRA on a daily basis | 02. FS Unplanned | S/4 → DMRA | MULESOFT | 04.Low |
| FTSI1652 | Interface | Interface to transfer STO Change & Delete from S4 to DMRA on a daily basis | 02. FS Unplanned | S/4 → DMRA | MULESOFT | 04.Low |
| FTSI1651 | Interface | Interface to transfer STO details from S4 to DMRA on a daily basis - STO create | 02. FS Unplanned | S/4 → DMRA | MULESOFT | 04.Low |
| FTSI1647 | Interface | New Interface required from APPS/XEUS for each different site with S/4 using ... | 10. Object Complete |  | BODS | 03.Medium |
| FTSI1646 | Interface | New Interface required from FFS/MARS for each different site with S/4 using B... | 10. Object Complete |  | BODS | 03.Medium |
| FTSI1610 | Interface | Interface from SMH to S/4 to Transfer DP and Stack Orders from Interim Locati... | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1602 | Interface | Interface from SGP to S4 to get Inventory status | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1580 | Interface | Interface between SMH to S/4 to Trigger UNDO START event, which will Reverse ... | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1578 | Interface | Interface to send Lot attribute signal to Workstream from SAP S4 - Mulesoft R... | 06. Dev In Progress |  | MuleSoft | 02.High |
| FTSI1574 | Interface | A new interface for the Believe Handheld application will allow users to fetc... | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1573 | Interface | interface between S4 and ECA via BODS to post consumption of DTC and EMIB Die... | 10. Object Complete |  | MULESOFT | 03.Medium |
| FTSI1538 | Interface | CMMS – get location info from CMMS | 02. FS Unplanned |  | NA | 03.Medium |
| FTSI1537 | Interface | CMMS – Get Collateral Details | 02. FS Unplanned |  | NA | 03.Medium |
| FTSI1536 | Interface | CMMS – Collateral Conversion | 02. FS Unplanned |  | NA | 03.Medium |
| FTSI1527 | Interface | Interface to get Cu flag from XEUS | 10. Object Complete |  | MULESOFT | 03.Medium |
| FTSI1473 | Interface | MDG to S4 for SFP, Stage, UPI | 10. Object Complete |  | BODS | 03.Medium |
| FTSI1471 | Interface | MDG to S4 for MES Site Code to Plant | 10. Object Complete |  | MULESOFT | 03.Medium |
| FTSI1469 | Interface | Inventory Conversion for R3 | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1455 | Interface | Interface from FSCO for lot level material staging by shift​ | 10. Object Complete |  | BODS | 03.Medium |
| FTSI1454 | Interface | Interface from PDH to S4 for lot level STR assignment​ | 10. Object Complete |  | MULESOFT | 03.Medium |
| FTSI1431 | Interface | Interface to transfer batch SLED details from S4 to DMRA on a daily basis | 06. Dev In Progress | S/4 → DMRA | MULESOFT | 03.Medium |
| FTSI1371 | Interface | CMMS – Equipment create and update (status and collateral name) | 04. FS In Progress |  → S/4 | MULESOFT | 03.Medium |
| FTSI1370 | Interface | Factory Portal - Equipment to Parts Management (Custom Fields – Part Check ou... | 04. FS In Progress |  → S/4 | MULESOFT | 03.Medium |
| FTSI1355 | Interface | CMMS – Equipment with MMS flag (S4 to CMMS) | 06. Dev Not Started |  → S/4 | MULESOFT | 03.Medium |
| FTSI1326 | Interface | Interface to send Lot create & Lot attribute signal to Workstream from SAP S4 | 06. Dev In Progress |  | MULESOFT | 02.High |
| FTSI1323 | Interface | M-100-170_API 9 is to provide Shipping details Ship Server | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| FTSI1321 | Interface | M-100-170_API 6 is to get Shippable lots from Work Stream | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| FTSI1320 | Interface | M-100-170_API 7 is for Precheck Request and Response to Ship Server | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| FTSI1319 | Interface | M-100-170_API4 is to provide Shipping details to ULT from S4 | 10. Object Complete |  | MULESOFT | 03.Medium |
| FTSI1318 | Interface | M-100-170_API3 is to provide Shipping details to WorkStream from S4 | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| FTSI1317 | Interface | M-100-170_API 11 is to get Shippable lots from Ship server | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| FTSI1159 | Interface | Interface from ECA to S4 to maintain POLP table | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FTSI1158 | Interface | Interface from SMH to S4 to handle movement of lots from Revenue to TD | 10. Object Complete | PDF → S/4 | MULESOFT | 03.Medium |
| FTSI1157 | Interface | Custom program for STO generation for Raw Silicon | 10. Object Complete | 3PL → S/4 | APIGEE | 03.Medium |
| FTSI1021 | Interface | Interface to be developed from ECA to SAP which helps to upload PIR via BAPI | 06. Dev In Progress | ECA → S/4 | APIGEE | 03.Medium |
| FTSI1020 | Interface | IMO - Interface from NBS to S4 to induct stock from IMO plant to S4 | 10. Object Complete | NBS → S/4 | APIGEE | 03.Medium |
| FTSI1016 | Interface | IMR - Interface between SAP S/4 and SAP ME to replicate production orders. Th... | 10. Object Complete | S/4 → SAP ME | NA | 03.Medium |
| FTSI1008 | Interface | Interface S/4 with EMS | 10. Object Complete | EMS → S/4 | MULESOFT | 03.Medium |
| FTSI1007 | Interface | Interface S/4 with XEUS | 10. Object Complete | XEUS/Mars → S/4 | APIGEE | 02.High |
| FTSI0985 | Interface | Claim Status Update from e2open to SAP S4 (Inbound Interface) | 10. Object Complete | E2Open → S/4 | MULESOFT | 03.Medium |
| FTSI0983 | Interface | SAP Warranty Claim Document to e2open (Outbound Interface) | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| FTSI0924 | Interface | Interface: SAP ME to S/4 to Create & Maintain Notifications | 10. Object Complete | SAP ME → S/4 | NA | 03.Medium |
| FTSI0860 | Interface | Interface to create Kanban trigger from DMRA and get Reservation created and ... | 06. Dev In Progress | DMRA → S/4 | MULESOFT | 01.Very High |
| FTSI0830 | Interface | Shipserver Interface to S4 to get handling units for the logical ship | 06. Dev In Progress | MPL → S/4 | MULESOFT | 03.Medium |
| FTSI0689 | Interface | Interface between PDF and S4 to handle DLCP update in S4 based on the DLCP UP... | 10. Object Complete | MES → S/4 | MULESOFT | 03.Medium |
| FTSI0686 | Interface | Interface between PDF and S4 to handle production order merge events in S4 ba... | 10. Object Complete | MES → S/4 | APIGEE | 02.High |
| FTSI0677 | Interface | API from SHIP server to validate shipment readiness” | 06. Dev In Progress | PDF → S/4 | MULESOFT | 01.Very High |
| FTSI0676 | Interface | Interface between PDF and S4 to handle undo complete in S4 based on the UNDO ... | 10. Object Complete | PDF → S/4 | APIGEE | 03.Medium |
| FTSI0675 | Interface | Interface between PDF and S4 to handle mid stage transfers in S4 based on the... | 10. Object Complete | MES → S/4 | APIGEE | 03.Medium |
| FTSI0674 | Interface | Interface between PDF and S4 to handle undo move and scrap in S4 based on the... | 10. Object Complete | MES → S/4 | APIGEE | 03.Medium |
| FTSI0484 | Interface | Interface between PDF and S4 to handle quantity or batch attribute updates ba... | 10. Object Complete | MES → S/4 | APIGEE | 03.Medium |
| FTSI0483 | Interface | Interface between PDF and S4 to handle production order split events in S4 ba... | 10. Object Complete | MES → S/4 | APIGEE | 02.High |
| FTSI0481 | Interface | Interface between PDF and S4 to handle production order complete events in S4... | 10. Object Complete | MES → S/4 | APIGEE | 03.Medium |
| FTSI0422 | Interface | Interface between PDF and S4 for production order process in S4 based on the ... | 10. Object Complete | PDF → S/4 | APIGEE | 02.High |
| FTSI0421 | Interface | Custom RFC triggered in S4 by PDF to determine activity values and post confi... | 10. Object Complete | PDF → S/4 | APIGEE | 03.Medium |
| FTSI0420 | Interface | Custom RFC triggered in S4 by PDF to post goods movement in S4 based on the R... | 10. Object Complete | PDF → S/4 | APIGEE | 03.Medium |
| FTSI0338 | Interface | Interface from MES staging database to S/4 to create/update reference operati... | 10. Object Complete | MES → S/4 | APIGEE | 02.High |
| FTSI0311 | Interface | Production plan from ECA planning data hub (PDH) to S/4 to create planned Orders | 10. Object Complete | PDH (ECA) → S/4 | BODS | 03.Medium |
| FTSI0310 | Interface | Network Plan from ECA Planning Data Hub to S/4 for STO Creation | 10. Object Complete | PDH (ECA) → S/4 | BODS | 03.Medium |
| FTSI0308 | Interface | Interface from PDF to S/4 to update Lot level out date on Production orders | 10. Object Complete | MES → S/4 | APIGEE | 02.High |
| FTSI0050 | Interface | Interface to transfer Purchase Requisitions created in IBP/MAPPS/other system... | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FTSF1361 | Form | Factory Portal - Returns Order Flow (Form-Based (CRD) Return Order​) | 10. Object Complete |  | NA | 03.Medium |
| FTSE1645 | Enhancement | Wafer Stock management for Reclaim Purposes | 10. Object Complete |  | NA | 03.Medium |
| FTSE1641 | Enhancement | Enhancement to create a program which can query on Master Data, Batch & STO d... | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1582 | Enhancement | A Custom table to map and capture the relationship between RSQ Batch ID/STO# ... | 10. Object Complete |  | NA | 04.Low |
| FTSE1581 | Enhancement | Automated Batch Status Update Based on MRB Release Date using custom program. | 10. Object Complete |  | NA | 03.Medium |
| FTSE1579 | Enhancement | Custom tables to store Board Failure Form details | 10. Object Complete |  | NA | 03.Medium |
| FTSE1577 | Enhancement | Perform Auto batch determination at the time of STO creation – DMRA | 09. FUT Overdue |  | NA | 02.High |
| FTSE1549 | Enhancement | Custom Attributes for AMT/ISM | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1548 | Enhancement | Automation for Product Conversions – Equipment Structure update | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1547 | Enhancement | Automation for Product Conversions – Work Order Closure | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1546 | Enhancement | Automation for Product Conversions – Parts Request and Return | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1545 | Enhancement | Automation for Product Conversions – Explode BOM | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1544 | Enhancement | Automation for Product Conversions – create Work Order | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1543 | Enhancement | PM inbound from AMT | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1542 | Enhancement | PM outbound to AMT | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1541 | Enhancement | Send SAP notification on Work Order update | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1540 | Enhancement | Send SAP notification on Equipment update | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1539 | Enhancement | Custom Fiori UI – Move Equipment SRoom to SRoom (screen) | 02. FS Unplanned |  | NA | 03.Medium |
| FTSE1528 | Enhancement | Warranty claim for non E2O supplier | 10. Object Complete |  | NA | 03.Medium |
| FTSE1480 | Enhancement | B2B SLOC Mapping Table | 10. Object Complete |  | NA | 04.Low |
| FTSE1479 | Enhancement | Table for SFP/Operation for KM2/KM5 | 10. Object Complete |  | NA | 04.Low |
| FTSE1478 | Enhancement | Table for All Shippable Mid Stage and End Stage Operations | 10. Object Complete |  | NA | 04.Low |
| FTSE1477 | Enhancement | Enhancement - Lot Level Exception UI | 09. FUT Overdue |  | NA | 01.Very High |
| FTSE1476 | Enhancement | Lot to STR Mapping table | 10. Object Complete |  | NA | 04.Low |
| FTSE1475 | Enhancement | Non Revenue Shipping Demand Screen (Custom Table) | 10. Object Complete |  | NA | 04.Low |
| FTSE1474 | Enhancement | Non Revenue Shipping Demand Screen | 10. Object Complete |  | NA | 02.High |
| FTSE1472 | Enhancement | Custom Table for SFP, Stage, UPI Mapping | 10. Object Complete |  | NA | 04.Low |
| FTSE1470 | Enhancement | Custom Table for MES Facility, MES Site Code to Plant | 10. Object Complete |  | NA | 04.Low |
| FTSE1468 | Enhancement | Custom table to store PO Lot Pegging (POLP) | 10. Object Complete |  | NA | 04.Low |
| FTSE1467 | Enhancement | Custom Report for Operating Supplies Reservations​ | 06. Dev In Progress |  | NA | 02.High |
| FTSE1456 | Enhancement | Custom Table to store FSCO lot level material staging​ | 10. Object Complete |  | NA | 04.Low |
| FTSE1451 | Enhancement | Enhancement required for triggering Interface between S4 and SAP ME from the ... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1435 | Enhancement | Custom Table - Cross Site Ref Op sets will be maintained at a higher level in... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1433 | Enhancement | Custom Program to assign Routings to Items based on Item Characteristics​​ | 10. Object Complete |  | NA | 03.Medium |
| FTSE1432 | Enhancement | Custom Enhancement to Issue out stock in S4 | 10. Object Complete |  | NA | 03.Medium |
| FTSE1413 | Enhancement | Reusable Mass Upload Program for Equipment Master Warranty | 10. Object Complete |  | NA | 03.Medium |
| FTSE1385 | Enhancement | Factory Portal - Preventative Maintenance (AT) (Schedule Maintenance Plan) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1383 | Enhancement | Factory Portal - Preventative Maintenance (AT) (Set Maintenance Counte) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1382 | Enhancement | Factory Portal - Preventative Maintenance (AT) (Set Maintenance Cycle​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1381 | Enhancement | Factory Portal - Preventative Maintenance (AT) (Create Maintenance Plan) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1379 | Enhancement | Factory Portal - Part list (Part list creation / modify (IA05​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1378 | Enhancement | Factory Portal - Functional Location​ (FLOC creation / Update (IL01 and IL02)​​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1376 | Enhancement | Factory Portal - Admin (Notifications​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1374 | Enhancement | Factory Portal - Admin (Admin Screen - My Profile) - Contacts custom Table En... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1373 | Enhancement | Factory Portal - Admin (Admin Screen - My Profile) - Fiori Enhancement | 10. Object Complete |  | NA | 01.Very High |
| FTSE1369 | Enhancement | Factory Portal - Equipment to Parts Management (Custom Fields – Part Check ou... | 04. FS In Progress |  | NA | 01.Very High |
| FTSE1368 | Enhancement | Factory Portal - Equipment to Parts Management (Equipment Management (details... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1367 | Enhancement | Factory Portal - Equipment to Parts Management (Equipment/ Entity/ Sub-Entity... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1366 | Enhancement | Factory Portal - Operating Supply (Reserve Ops Suppl​​​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1365 | Enhancement | Factory Portal - Operating Supply (Search for Ops Supply​​​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1363 | Enhancement | Factory Portal - Warranty Claim (Create Warranty Claim – Detailed Vie​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1360 | Enhancement | Custom Fiori UI – HAZMAT Enhancement to pull data | 10. Object Complete |  | NA | 03.Medium |
| FTSE1359 | Enhancement | Factory Portal - Returns Order Flow (Prevent TECO until after parts have been... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1358 | Enhancement | Factory Portal - Returns Order Flow (Form-Based (CRD) Return Order​) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1354 | Enhancement | Factory Portal - Work Order Flow ( Confirm and Submit Parts (Table Extension ... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1353 | Enhancement | Factory Portal - Work Order Flow ( Confirm and Submit Parts (Fiori Enhancemen... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1351 | Enhancement | Factory Portal - Work Order Flow ( Add component to work order ) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1350 | Enhancement | Factory Portal - Work Order Flow ( Search Parts ) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1349 | Enhancement | Factory Portal - Work Order Flow ( Change Color of WO, Equipment, and CRD & e... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1348 | Enhancement | Factory Portal - Work Order Flow ( Show Work Order – Single Work Order View +... | 10. Object Complete |  | NA | 01.Very High |
| FTSE1347 | Enhancement | Factory Portal - Work Order Flow ( Search work orders - ​List View ) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1344 | Enhancement | Factory Portal - Work Order Flow ( Home Page - View S/4 work orders ) | 10. Object Complete |  | NA | 01.Very High |
| FTSE1325 | Enhancement | M-100-170_Create Manual ship FIORI UI in S4 | 06. Dev In Progress |  | NA | 01.Very High |
| FTSE1160 | Enhancement | Custom Utility for Engineering Planners to create Rev Eng Planned Orders in S4 | 10. Object Complete |  | NA | 03.Medium |
| FTSE1125 | Enhancement | Custom table in S4 to store merging orders and surviving order association fr... | 10. Object Complete |  | NA | 04.Low |
| FTSE1119 | Enhancement | Custom Table required to support enhancement to store lot attributes when Lot... | 07. FUT Roadblock |  | NA | 03.Medium |
| FTSE1019 | Enhancement | WIINGS factory portal UI to send signal for raw material consumption in S4 | 10. Object Complete |  | NA | 02.High |
| FTSE1010 | Enhancement | Update the Copper/Heavy Metal flag (User Status) for the tools on placement a... | 10. Object Complete |  | NA | 03.Medium |
| FTSE0996 | Enhancement | Create Purchase Requisition with multiple purchase req document types from Wo... | 10. Object Complete |  | NA | 03.Medium |
| FTSE0995 | Enhancement | Enhancement to update rejection reason and text in maintenance work order fro... | 10. Object Complete |  | NA | 03.Medium |
| FTSE0993 | Enhancement | Auto Roll Function to add Item/Part through Batch job in Master Warranty | 10. Object Complete |  | NA | 03.Medium |
| FTSE0992 | Enhancement | Custom Fields Enhancement in WTY Claim | 10. Object Complete |  | NA | 03.Medium |
| FTSE0991 | Enhancement | Claim Generation from Maintenance Work Order per Item | 10. Object Complete |  | NA | 03.Medium |
| FTSE0990 | Enhancement | Create PR with Free of Charge from approved claim status – MMID & Non-MMID | 10. Object Complete |  | NA | 03.Medium |
| FTSE0989 | Enhancement | Warranty validation at Equipment level & Item/Part level in Work Order | 10. Object Complete |  | NA | 03.Medium |
| FTSE0988 | Enhancement | Convert Item/Part Warranty information upload to SAP S/4 Master Warranty | 10. Object Complete |  | NA | 02.High |
| FTSE0984 | Enhancement | SAP Warranty Claim Document to e2open (Outbound Interface) | 10. Object Complete |  | NA | 03.Medium |
| FTSE0982 | Enhancement | SAP PM enhancement to capture reason codes for returns (dropdown) | 10. Object Complete |  | NA | 02.High |
| FTSE0925 | Enhancement | Enhancement: Batch process to create Equipment from Material BOM after GR | 10. Object Complete |  | NA | 03.Medium |
| FTSE0507 | Enhancement | Custom Program to read planned orders and build instruction data and generate... | 10. Object Complete |  | NA | 03.Medium |
| FTSE0506 | Enhancement | Custom table to store planned orders and pegged sales orders in S4 | 10. Object Complete |  | NA | 03.Medium |
| FTSE0423 | Enhancement | Create custom table in SAP to store the build instruction data | 10. Object Complete |  | NA | 04.Low |
| FTSC1550 | Conversion | Inventory Conversion | 02. FS Unplanned |  | NA | 03.Medium |
| FTSC0052_IF | Conversion | Conversion of Reference Operation Sets to S/4 | 10. Object Complete | ECC → S4 | NA | 02.High |
| LOGI1738 | Interface | Interface to send data to Factory Comm to activate the Mobile text receiving ... | 02. FS Unplanned |  | NA | 02.High |

**Summary**: 5 Reports, 92 Interfaces, 31 Conversions, 118 Enhancements, 15 Forms, 4 Workflows

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for M-090:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for M-090:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (265 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 209 | 78.9% |
| 02. FS Unplanned | 22 | 8.3% |
| 06. Dev In Progress | 19 | 7.2% |
| 08. FUT In Progress | 4 | 1.5% |
| 09. FUT Overdue | 4 | 1.5% |
| 04. FS In Progress | 3 | 1.1% |
| 07. FUT Roadblock | 2 | 0.8% |
| 03. FS Not Started | 1 | 0.4% |
| 06. Dev Not Started | 1 | 0.4% |
| **Total** | **265** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 5 |
| Interface (I) | 92 |
| Conversion (C) | 31 |
| Enhancement (E) | 118 |
| Form (F) | 15 |
| Workflow (W) | 4 |
| **Total** | **265** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 29 |
| 02.High | 31 |
| 03.Medium | 149 |
| 04.Low | 33 |
| N/A | 23 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| LOGI1718 | 02.Interface | To align on batch attributes for straddle in S4 | 08. FUT In Progress | 03.Medium |
| LOGI1675 | 02.Interface | Interface for SiGaC to extract inventory data from EWM to meet their existing bu... | 06. Dev In Progress | 03.Medium |
| LOGI1626 | 02.Interface | Inventory adjustment  data in XML format from Kommand auto-store to SAP EWM | 06. Dev In Progress | 03.Medium |
| LOGI1594 | 02.Interface | Pickresult(Pick Warehouse task confirmation) data in XML format from SAP EWM to ... | 06. Dev In Progress | 02.High |
| LOGI1593 | 02.Interface | Replenresult(Putaway warehouse task confirmation) data in XML format from SAP EW... | 06. Dev In Progress | 02.High |
| LOGI1555 | 02.Interface | Straddle Plant to be automatically complete the Goods Receipt and write of the i... | 09. FUT Overdue | 03.Medium |
| LOGE1691 | 04.Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF and ... | 08. FUT In Progress | 03.Medium |
| LOGE1690 | 04.Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF and ... | 07. FUT Roadblock | 03.Medium |
| LOGE1601 | 04.Enhancement | Interface between ECD (Excursion Containment Disposition) and SAP S/4 EWM for In... | 06. Dev In Progress | 02.High |
| LOGE1554 | 04.Enhancement | Straddle Plant to be automatically complete the Goods Receipt and write of the i... | 09. FUT Overdue | 03.Medium |
| LOGE1415 | 04.Enhancement | Suppress Batch and serial number validation in MIGO/MB26 for movement type 261 | 08. FUT In Progress | 03.Medium |
| LOGE0935_IF | 04.Enhancement | Fiori App - Shipping Memo | 08. FUT In Progress | 02.High |
| FTSW1372 | 06.Workflow | Factory Portal - Equipment to Parts Management (Custom Fields – Part Check out &... | 03. FS Not Started | 03.Medium |
| FTSI1702 | 02.Interface | Interface to transfer Vendor details from S4 to DMRA on a daily basis | 02. FS Unplanned | 03.Medium |
| FTSI1667 | 02.Interface | Interface to transfer BOM details from S4 to DMRA on a daily basis | 02. FS Unplanned | 03.Medium |
| FTSI1654 | 02.Interface | Interface to transfer Material Master details from S4 to DMRA on a daily basis | 02. FS Unplanned | 04.Low |
| FTSI1652 | 02.Interface | Interface to transfer STO Change  & Delete from S4 to DMRA on a daily basis | 02. FS Unplanned | 04.Low |
| FTSI1651 | 02.Interface | Interface to transfer STO details from S4 to DMRA on a daily basis - STO create | 02. FS Unplanned | 04.Low |
| FTSI1578 | 02.Interface | Interface to send Lot attribute signal to Workstream from SAP S4 - Mulesoft Requ... | 06. Dev In Progress | 02.High |
| FTSI1538 | 02.Interface | CMMS – get location info from CMMS | 02. FS Unplanned | 03.Medium |
| FTSI1537 | 02.Interface | CMMS – Get Collateral Details | 02. FS Unplanned | 03.Medium |
| FTSI1536 | 02.Interface | CMMS – Collateral Conversion | 02. FS Unplanned | 03.Medium |
| FTSI1431 | 02.Interface | Interface to transfer batch SLED details from S4 to DMRA on a daily basis | 06. Dev In Progress | 03.Medium |
| FTSI1371 | 02.Interface | CMMS – Equipment create and update (status and collateral name) | 04. FS In Progress | 03.Medium |
| FTSI1370 | 02.Interface | Factory Portal - Equipment to Parts Management (Custom Fields – Part Check out &... | 04. FS In Progress | 03.Medium |
| FTSI1355 | 02.Interface | CMMS – Equipment with MMS flag (S4 to CMMS) | 06. Dev Not Started | 03.Medium |
| FTSI1326 | 02.Interface | Interface to send Lot create & Lot attribute signal to Workstream from SAP S4 | 06. Dev In Progress | 02.High |
| FTSI1323 | 02.Interface | M-100-170_API 9 is to provide Shipping details Ship Server | 06. Dev In Progress | 03.Medium |
| FTSI1321 | 02.Interface | M-100-170_API 6 is to get Shippable lots from Work Stream | 06. Dev In Progress | 03.Medium |
| FTSI1320 | 02.Interface | M-100-170_API 7 is for Precheck Request and Response to Ship Server | 06. Dev In Progress | 03.Medium |
| FTSI1318 | 02.Interface | M-100-170_API3 is to provide Shipping details to WorkStream from S4 | 06. Dev In Progress | 03.Medium |
| FTSI1317 | 02.Interface | M-100-170_API 11 is to get Shippable lots from Ship server | 06. Dev In Progress | 03.Medium |
| FTSI1021 | 02.Interface | Interface to be developed from ECA to SAP which helps to upload PIR via BAPI | 06. Dev In Progress | 03.Medium |
| FTSI0860 | 02.Interface | Interface to create Kanban trigger from DMRA and get Reservation created and sha... | 06. Dev In Progress | 01.Very High |
| FTSI0830 | 02.Interface | Shipserver Interface to S4 to get handling units for the logical ship | 06. Dev In Progress | 03.Medium |
| FTSI0677 | 02.Interface | API from SHIP server to validate shipment readiness” | 06. Dev In Progress | 01.Very High |
| FTSE1641 | 04.Enhancement | Enhancement to create a program which can query on  Master Data, Batch & STO det... | 02. FS Unplanned | 03.Medium |
| FTSE1577 | 04.Enhancement | Perform Auto batch determination at the time of STO creation – DMRA | 09. FUT Overdue | 02.High |
| FTSE1549 | 04.Enhancement | Custom Attributes for AMT/ISM | 02. FS Unplanned | 03.Medium |
| FTSE1548 | 04.Enhancement | Automation for Product Conversions – Equipment Structure update | 02. FS Unplanned | 03.Medium |
| FTSE1547 | 04.Enhancement | Automation for Product Conversions – Work Order Closure | 02. FS Unplanned | 03.Medium |
| FTSE1546 | 04.Enhancement | Automation for Product Conversions – Parts Request and Return | 02. FS Unplanned | 03.Medium |
| FTSE1545 | 04.Enhancement | Automation for Product Conversions – Explode BOM | 02. FS Unplanned | 03.Medium |
| FTSE1544 | 04.Enhancement | Automation for Product Conversions – create Work Order | 02. FS Unplanned | 03.Medium |
| FTSE1543 | 04.Enhancement | PM inbound from AMT | 02. FS Unplanned | 03.Medium |
| FTSE1542 | 04.Enhancement | PM outbound to AMT | 02. FS Unplanned | 03.Medium |
| FTSE1541 | 04.Enhancement | Send SAP notification on Work Order update | 02. FS Unplanned | 03.Medium |
| FTSE1540 | 04.Enhancement | Send SAP notification on Equipment update | 02. FS Unplanned | 03.Medium |
| FTSE1539 | 04.Enhancement | Custom Fiori UI – Move Equipment SRoom to SRoom (screen) | 02. FS Unplanned | 03.Medium |
| FTSE1477 | 04.Enhancement | Enhancement - Lot Level Exception UI | 09. FUT Overdue | 01.Very High |

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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-090 — Schedule Production (IF)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*239 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| LOGW1078_IF | ISM Workflows - Capital/AMT | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGW1077_IF | ISM Workflows - EIMS/Lab | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| LOGW1076_IF | ISM Workflows - Non-inventory | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGR1176_IF | ISM - International Traffic Report | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGR0833_IF | Email Notification for deletion of Shipping Memos | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGM024_IF | Create/Upload Vehicle resource | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM023_IF | Update Business Share | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM022_IF | Upload Transportation Allocation | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM021_IF | Upload Schedules | Aug-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM019_IF | Default Routes | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM018_IF | Upload Rate Table | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM016_IF | Create and review Charge Calculation Sheet | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM015_IF | Create and review Freight Agreement | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM012_IF | Creation of Location based on BP, Shipping points, plants | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM008_IF | Location creation-ocean ports, airports | May-25 (100%) | — | — | Sep-25 (100%) | 1. On Track |
| LOGM007_IF | Storage Bin Upload | Jul-25 (100%) | — | — | Oct-25 (100%) |  |
| LOGM006_IF | Product Master conversion (additional EWM attribution) | Jul-25 (100%) | — | — | Oct-25 (100%) |  |
| LOGM005_IF | UPLOAD TRANSPORTATION ZONES (TM) | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM004_IF | UPLOAD TRANSPORTATION LANES | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGI1718 | To align on batch attributes for straddle in S4 | Feb-26 (100%) | Mar-26 (100%) | Mar-26 (100%) | Mar-26 (5%) | 3. Off Track |
| LOGI1708 | Wrapper program for Inbound interface from Kommand AS to SAP | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | 1. On Track |
| LOGI1677 | Send 4C1 Inventory Reconciliation Snapshot to IP | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1676 | Send 4C1 Inventory movement Stock type change and cycle count to IP | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1675 | Interface for SiGaC to extract inventory data from EWM to meet their existing business needs​ | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 4. Completed |
| LOGI1626 | Inventory adjustment data in XML format from Kommand auto-store to SAP EWM | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | Mar-26 (77%) | 1. On Track |
| LOGI1595 | Summary Reconciliation and Inventory Snapshot data in XML format from SAP EWM to Kommand auto-store | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Jan-26 (100%) | 4. Completed |
| LOGI1594 | Pickresult(Pick Warehouse task confirmation) data in XML format from SAP EWM to Kommand auto-store | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Mar-26 (80%) | 1. On Track |
| LOGI1593 | Replenresult(Putaway warehouse task confirmation) data in XML format from SAP EWM to Kommand auto-store | Aug-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Mar-26 (80%) | 1. On Track |
| LOGI1591 | MergePick (Pick Warehouse task)data in XML format from SAP EWM to Kommand auto-store | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Jan-26 (100%) | 4. Completed |
| LOGI1589 | MergeReplen(Putaway Warehouse task) data in XML format from SAP EWM to Kommand auto-store | Aug-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Jan-26 (100%) | 1. On Track |

*... and 209 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

**Mapped sub-tower(s):** 7.1 FTS IF - ALL, 7.4 FTS IF - EWM, 7.5 FTS IF - TM, 7.6 FTS IF - Logistics & Inventory Management, 7.7 FTS IF - Manufacturing & MES Integration, 7.8 FTS IF - MRP & Planning Integration, 7.9 FTS IF - Plant Maintenance

**RAID Summary:** 102 open items (23 capability-specific, 79 tower-level), 439 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 6 | 6 |
| P2 - Medium | 21 | 60 | 81 |
| P3 - Low | 2 | 13 | 15 |
| **Total** | **23** | **79** | **102** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03294 |  | P2 - Medium | Factory portal application is not ready from FTS and this is... | In Progress | FTS IF | 2026-02-27 |
| 02987 |  | P2 - Medium | LOGF1525 - Consolidated Commercial Invoice for WIP Awaiting ... | In Progress | FTS IF | 2025-11-06 |
| 03716 | Risk | P2 - Medium | Raising RAID to track the progress of FUT for LOGE1690 as it... | In Progress | FTS IF | 2026-03-13 |
| 03518 | Action | P2 - Medium | Batch Attributes for WIP Straddle-LOGI1718 | Not Started |  | 2026-02-06 |
| 02315 | Action | P2 - Medium | Need Approval on Preload file | Not Started | FTS IF |  |
| 02419 | Key Decision | P2 - Medium | Batch classification details clarification required LOGC0972... | Not Started | FTS IF | 2025-10-15 |
| 03752 | Risk | P2 - Medium | IF-LOGE1691-Enhancement to restrict access based on Storage ... | In Progress | Security & Controls | 2026-03-24 |
| 01857 | Action | P2 - Medium | TF Signavio Flows Update Request | In Progress | FTS IF | 2026-01-30 |
| 03157 |  | P2 - Medium | Split Logic to Segregate IF & IP data from EWM tables | Not Started |  | 2025-12-04 |
| 03231 | Risk | P2 - Medium | Need LE Sample Data (Shipping Point & Delivery Route) for va... | Not Started | FTS IF | 2026-02-10 |
| 03331 | Risk | P2 - Medium | Clarity on finalized SAP S/4 Plant and storage location mapp... | In Progress | Master Data | 2026-02-20 |
| 03703 | Risk | P2 - Medium | For FUT: Factory Automation Apps waiting on Heartbeat Loader... | In Progress | FTS IF | 2026-03-24 |
| 03704 | Risk | P2 - Medium | ASN Data from CIBR via e2Open needs to incorporate new attri... | In Progress | Data Foundation Program ( | 2026-03-10 |
| 02088 | Risk | P2 - Medium | Equipment Master Conversion help needed | In Progress | FTS IF | 2026-03-31 |
| 03539 | Risk | P2 - Medium | TPTD coming back into scope for SAP PM poses risk for R3 | Roadblock / At Risk | FTS IF | 2026-03-27 |
| 03517 | Issue | P2 - Medium | Need help to determine correct timezone for EWM datetime fie... | Not Started | FTS IF | 2026-02-11 |
| 02133 | Action | P2 - Medium | clarification on storage location xref for one to many scena... | Not Started | FTS IF |  |
| 03671 | Risk | P2 - Medium | R4 GFM US EWM Warehouses Structure | Roadblock / At Risk | FTS IF | 2026-04-30 |
| 03685 |  | P2 - Medium | Rinchem ITC1 Test Scenario/Case Readiness | In Progress | FTS IF |  |
| 03515 | Risk | P2 - Medium | Need E2E test data for STO of IM to IM (Interfactory shipmen... | In Progress | FTS IF | 2026-03-06 |
| 03779 | Risk | P2 - Medium | Chem 3PL PIP Enhancement to support FTZ | In Progress | FTS IF | 2026-04-17 |
| 03061 | Risk | P3 - Low | Athena Operational Team needed to handle data updates during... | In Progress | FTS IF | 2026-03-06 |
| 03404 | Risk | P3 - Low | [WIINGS] EWM labels updates | Not Started | FTS IF | 2026-04-03 |

**Other FTS-IF Tower RAID Items** (79 open):

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
| 03079 | Action | P2 - Medium | Request for PDH Design WTF | In Progress | FTS IP | 2026-03-04 |
| 03128 | Risk | P2 - Medium | Application Health Monitoring | In Progress | FTS IF | 2026-05-13 |
| 03205 | Action | P2 - Medium | Provide an update WW50 on the production rollout plan for th... | In Progress | FTS IF | 2026-03-06 |
| 03241 | Risk | P2 - Medium | Materials Planning Policy for Constrained Materials | In Progress | FTS IP | 2026-07-31 |
| 03292 | Risk | P2 - Medium | SCP IF BY ESP Solves during ITC1 | In Progress | FTS IF | 2026-01-09 |
| 03308 | Action | P2 - Medium | Missing information for Anafi material master | Not Started | FTS IF |  |
| 03314 | Risk | P2 - Medium | Executive lock cause performance issues in IF Dev | In Progress | FTS IF | 2026-04-17 |
| 03334 | Issue | P2 - Medium | Application Monitoring - Connectors Health Monitoring | In Progress | FTS IF | 2026-05-15 |
| 03368 | Issue | P2 - Medium | Infrastructure resources support PDF SMH ability to provide ... | In Progress | FTS IF | 2026-03-27 |
| 03398 | Action | P2 - Medium | Kafka Admin Password for both IF and IP | In Progress | FTS IF | 2026-04-03 |
| 03713 | Risk | P2 - Medium | Lack of TRDI data impacting delivery of ECA report by ITC2 | In Progress | FTS IF | 2026-03-27 |
| 03718 | Risk | P2 - Medium | Storage Location Logic for Non-MMID Parts. | In Progress | PTP | 2026-03-27 |
| 03732 | Risk | P2 - Medium | Production scheduling systems will likely only provide mock ... | Not Started |  | 2026-03-27 |
| 03526 | Action | P2 - Medium | Review process for post-validation of system changes | In Progress | FTS IP | 2026-04-03 |
| 02856 | Risk | P2 - Medium | SMH IF and (IP) Entra ID issue | In Progress | FTS IF | 2026-04-03 |
| 03543 | Risk | P2 - Medium | SME's lack level of knowledge for BE SCP | In Progress | CM & Comms | 2026-04-03 |
| 03560 | Issue | P2 - Medium | Apigee Endpoints for different ITC's | In Progress | Technology | 2026-02-28 |
| 03579 | Risk | P2 - Medium | FTS-IF ECA reports as risk due to open TD & data source ques... | In Progress | FTS IF | 2026-03-27 |
| 03610 | Action | P2 - Medium | Schedule follow-up with Mike Lange (re: CR1690 fix to missin... | In Progress | FTS IF | 2026-02-27 |
| | | | *... and 49 more tower-level items* | | | |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*M-090 — Architecture Document (TOGAF BDAT) · Forecast to Stock (IF) · Generated: March 2026*

