<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">PLB-020 — Supply Planning & Management (IP)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Forecast to Stock (IP) (FTS-IP) Tower<br/>
  Capability PLB-020 · PLB Supply Chain Planning (IP)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **PLB-020 Supply Planning & Management (IP)** within the IAO program. It includes 4 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Forecast to Stock (IP) (FTS-IP) |
| **Process Group** | PLB Supply Chain Planning (IP) |
| **Capability** | PLB-020 - Supply Planning & Management (IP) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 2 Reports, 20 Interfaces, 3 Conversions, 17 Enhancements, 6 Forms, 3 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Forecast to Stock (IP) |
| **L1 Process** | PLB Supply Chain Planning (IP) |
| **L2 Capability** | PLB-020 - Supply Planning & Management (IP) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Intel Products Supply Chain Unification | Consolidate Intel Products manufacturing and logistics onto S/4 HANA platform | IDM 2.0 Products Transformation | High |
| 2 | End-to-End Traceability | Enable lot/batch traceability from raw material to finished goods shipment | Quality & Compliance | High |
| 3 | Demand-Supply Matching | Implement responsive demand and supply matching (RDSM) for IP product lines | Supply Chain Agility | Medium |
| 4 | PLB-020 Process Migration | Migrate Supply Planning & Management (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Supply Chain (Intel Products) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Production Schedule Adherence | > 95% | Percentage of production orders completed on schedule | 88% (current) | Production Manager |
| Material Availability Rate | > 98% | Materials available at point of need for production | 94% (current) | Materials Planning |
| Shipping On-Time Delivery | > 97% | Orders shipped within committed delivery window | 93% (current) | Logistics Lead |
| PLB-020 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **4 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for PLB-020 Supply Planning & Management (IP).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | PLB-020-010_Supply_Parameter_&amp;_Data_Management_(010)_(IP) | PLB-020-010_Supply_Parameter_&amp;_Data_Management_(010)_(IP) | Analytics Specialist, Boundary Apps, FTS IP - Production Planner | 4 | 3 |
| 2 | PLB-020-050_Distribution_Requirements_Planning_(IP) | PLB-020-050_Distribution_Requirements_Planning_(IP) | Batch User, Boundary Apps, FTS IF Logistic Business Role, FTS IP - Production Planner, Master Data Team, Material Planner, RFC User | 7 | 1 |
| 3 | PLB-020-090_Product_Data_Management_(IP) | PLB-020-090_Product_Data_Management_(IP) | Batch User - FTS, Boundary Apps, MDG Business Admin | 11 | 2 |
| 4 | PLB-020-120_Master_Production_Scheduling_(IP) | PLB-020-120_Master_Production_Scheduling_(IP) | Analytics Specialist, Boundary Apps, FTS IP - Production Planner | 13 | 4 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 PLB-020-010_Supply_Parameter_&amp;_Data_Management_(010)_(IP) — PLB-020-010_Supply_Parameter_&amp;_Data_Management_(010)_(IP)

**Swim Lanes**: Analytics Specialist · Boundary Apps · FTS IP - Production Planner | **Tasks**: 4 | **Gateways**: 3

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
    subgraph Analytics Specialist
        n1["fa:fa-user Create Parameters"]
        n2["fa:fa-user Manage / Change Parameters"]
        n5(["fa:fa-play Manage Parameters"])
        n6{{"fa:fa-arrows-alt parallelGateway"}}
        n7{{"fa:fa-arrows-alt Create or Manage / Change"}}
        n8{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Boundary Apps
        n3[["fa:fa-cog Selected paraments will be received (for e.g., Scrap %)"]]
    end
    subgraph FTS IP - Production Planner
        n4[["fa:fa-cog Selected paraments will be received (for e.g., Scrap% in BOM)"]]
    end
    n5 --> n7
    n2 --> n8
    n8 --> n6
    n6 --> n3
    n6 --> n4
    n7 -->|"Create"| n1
    n1 --> n8
    n7 -->|"Manage / Change"| n2
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 startEvt
    class n6 gateway
    class n7 gateway
    class n8 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2PozYU_SsWoyi7EtnyGSgPlRISqpU66kiZtg-bfXDMhVhjDLLNZNJs_ntNgCRkJg_V8oB0j889595rsA8GKVMwImM0OlBOVYQOY7WFAsYRGm-whLGJWuBvLCjeMJDjhpOVXK3ovyea7VVvDa3BElxQtm_QFeQloL--mmimE5mJJOZyIkHQbGyOK0ELLPZxyUrRsB8gzKzs5NYtzUuRgrgQLCuwia9TGeVwgd3AC7ykyZNASp4ORDM_CzMyPjbFsXJHtlioU_m1hEf89g9N1VbHGWYSNGerCvYH3gBrelSibjBSi9d-GFQ2PlwPbFVhQnmucc_SkMD85QL51vGIjqPRmp9N0fNizZF-CMNSLiBDUml4-apQRhmLHrx4lviWKZUoXyB6cJbBwnVM0nQS6dYtsxnuZAc036poU7K0o052TQ-RU72Z4i1yLFPs9fvGC3h6cYqnTuiEZ6d5YMd23DtlWfZTTnqu4hnLl85r6SZOsjh72f7Uj633en2bCy-Y2bdzAvFKCVyJJkniLi-jWk5927ovOk_cqRXfiOZYwQ7vL4K_xt5ZMPGDxA7uCrZ-t1XWmydRkl7QXfqJfxYM5nYyc-4KejPbC7sKtU4ucLVFM47ZXlEi0aoCov8fKlVLaR5uf1sbGY4yPGkmjmIBuiP0hAUuQIGQa-P7FdsZsh8xxzmgX1C8xTy_n-Z_OudVTE-ryxvQP1_xp4dDz8dClDs5wUyhStMZA_Z7O_O1cTxe5QQf5nT9lO9qvckO_5-j_g9uxjwv69ORgWZVJa-E3W_n1kmZoxUwIArSk3QBXEm00zuNNoAEEKCveulTpsuFL_kXE62IFkejz3o-3-85J88r9PUJTZD-btKaKFpy9MQw5yCu6vB-vo4RohzN_3z8qBruo8nkN70LXei0YdiFYRtOu3Dahu4w9LowaMIfa6Pdu7XxQ3-l3ZI9lO2Z7_ZWpzhXP1aT2B8oA9j5GHavD4vBind3xT8fxAN42h8RAzT4EA171DCNAkSBaWpEB-N0aeqLNYUM10wZR9PAtSpXe06M6HS5GHWV6swFxfqTKFrw-B9zimk9" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 PLB-020-050_Distribution_Requirements_Planning_(IP) — PLB-020-050_Distribution_Requirements_Planning_(IP)

**Swim Lanes**: Batch User · Boundary Apps · FTS IF Logistic Business Role · FTS IP - Production Planner · Master Data Team · Material Planner · RFC User | **Tasks**: 7 | **Gateways**: 1

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
        n1[["fa:fa-cog Convert STR's to Stock Transfer Order (STO)"]]
    end
    subgraph Boundary Apps
        n2[["fa:fa-cog Send Stock Transfer Requisition (STR)"]]
        n8(["fa:fa-play Distribution Requirement Planning (DRP) for Group A and B Sent"])
    end
    subgraph FTS IF Logistic Business Role
        n3[["fa:fa-cog Perform Goods Issue Against STO"]]
    end
    subgraph FTS IP - Production Planner
        n4[["fa:fa-cog Perform Goods Receipt against STO"]]
        n10(["fa:fa-stop Distribution Requirement Planning Created"])
    end
    subgraph Master Data Team
        n5[["fa:fa-cog Maintain Reorder Point"]]
        n9(["fa:fa-play Distribution Requirement Planning (DRP) for Group B, C and Manual Sent"])
    end
    subgraph Material Planner
        n6[["fa:fa-cog Perform Material Requirement Planning (MRP)"]]
        n11{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph RFC User
        n7[["fa:fa-cog Create STR"]]
    end
    n1 --> n3
    n3 --> n4
    n6 --> n11
    n4 --> n10
    n8 -->|"Type A and B Group"| n2
    n5 --> n6
    n11 --> n7
    n2 --> n11
    n9 -->|"Type B and C Group"| n5
    n7 --> n1
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 startEvt
    class n9 startEvt
    class n10 endEvt
    class n11 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVltv4jgU_itWqopWClISEkLzsBIEUlUqKgJm92GYB5M4YDXYWdtpYRj--x6HcF3SXWkigeRz-b5zdbI1Yp4QIzDu77eUURWgbUMtyYo0AtSYY0kaJtoL_sSC4nlGZEPbpJypCf1ZmtluvtZmWhbhFc02WjohC07QtxcTdcExM5HETDYlETRtmI1c0BUWm5BnXGjrO9JJrbRkq1Q9LhIiTgaW5duxB64ZZeQkbvmu70baT5KYs-QCNPXSTho3djq4jH_GSyxUGX4hyRCv_6KJWsI5xZkkYLNUq-wVz0mmc1Si0LK4EB-HYlCpeRgUbJLjmLIFyF0LRAKz95PIs3Y7tLu_n7EjKXodzxiCJ86wlH2SIqlAPPhQKKVZFty5YTfyLFMqwd9JcOcM_H7LMWOdSQCpW6YubvOT0MVSBXOeJZVp81PnEDj52hTrwLFMsYH_Ky7CkhNT2HY6TufI1PPt0A4PTGma_hYT1FVMsXyvuAatyIn6Ry7ba3uh9W-8Q5p91-_a13Ui4oPG5Aw0iqLW4FSqQduzrXrQXtRqW-EV6AIr8ok3J8Cn0D0CRp4f2X4t4J7vOspiPhI8PgC2Bl7kHQH9nh11nVpAt2u7nSpCwFkInC9RD6t4ib5B9nuFfpj9_fvMSHGQ4mbMFyjk7IPAbE2m44ZEiqOJ4vE7msI0ypQI9KYXCD1Mpm-PM-PHjz0QzMI1FS_KtUHdPJdnbM4l2wQ8rxnG5O-CSqooZ5pnfMZTQnQejhB5BvXuUygCnRelQ-ks4GZhCo0yzBhsD3roj0ePKOUCPQte5KiLMND2NLsC8Me6JKLpBL1E6JUvgILGqFdIuCakRGOekbOIWpdJjYgArhV65jyR6EXKgqDuAlMmdVnfvipbyThCTQSNT4q4TKlM46Jl7ld8YxITmiuEbzHuO26dKigVz_9HBUNBYLqTr4o1xFJB9_pYYTQleHVG6F3GO4TAFPyAqryO0YjTshHnQT79dpd7JgrLRg8xK3D2n90eQob6pXKj4O3bBT963I5nCPFcl97ebk9ICWnOYephJ8k6zmC4Psjz_hKZGbtdXZzjKLzeYf9qh8tu6RW-MWvMRs3mHzC01bG1P7rVsb0_2tWVydzqXF1OrKPPv2bGdJOT4yKVBZ8Zv2C_KzNv79Y-cFakfnV2rliezlF7JWp4hupVZn7ldnZR6nzOrvMLjVOradVq3FqNV6tp12r8Wk3n-LK-ED_dFttW9b69lNqHl45hGisiVpgmRrA1yk8r-PxKSIqLTBk708CF4pMNi42g_AQxijwBzz7FMFOrvXD3DyPrF1E=" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 PLB-020-090_Product_Data_Management_(IP) — PLB-020-090_Product_Data_Management_(IP)

**Swim Lanes**: Batch User - FTS · Boundary Apps · MDG Business Admin | **Tasks**: 11 | **Gateways**: 2

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
    subgraph Batch User - FTS
        n2[["fa:fa-cog Create/Update BOM Data"]]
        n3[["fa:fa-cog Create /Update Material Data"]]
        n14{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Boundary Apps
        n1["fa:fa-user Send the Item and Bill of Material (BOM) Data to Translator"]
        n5[["fa:fa-cog Modify Data into Standard PLM Data"]]
        n6[["fa:fa-cog Send Modified PLM Data to Middleware"]]
        n7[["fa:fa-cog Convert Item and BOM Data from one Format to Another"]]
        n8[["fa:fa-cog Send Item and BOM Data to S4 Platform"]]
        n9[["fa:fa-cog Convert Planning Item and BOM Data"]]
        n10[["fa:fa-cog Send Planning Item and BOM Data to ECA"]]
        n11[["fa:fa-cog Store Planning designated Item and BOM Data"]]
        n12(["fa:fa-play Request Received to Trigger Product Data"])
        n13(["fa:fa-stop Material and BOM Data Stored"])
    end
    subgraph MDG Business Admin
        n4[["fa:fa-cog Sync Material Data"]]
        n15{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n12 --> n1
    n1 --> n5
    n5 --> n6
    n6 --> n7
    n7 --> n8
    n8 --> n15
    n15 --> n4
    n15 --> n2
    n4 --> n3
    n2 --> n14
    n9 --> n10
    n10 --> n11
    n3 --> n14
    n14 --> n9
    n11 --> n13
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
    class n12 startEvt
    class n13 endEvt
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVttu4zYQ_RVCQeBdQEZ1tRw9FPBNiwViNFgn3YfNPjASZROhRZWknLiG_71DXSxbsbZAqwcJM8Nz5syIt4MR84QYoXF7e6AZVSE6DNSGbMkgRIMXLMnARJXjTywofmFEDvSYlGdqRf8uh9le_q6HaV-Et5TttXdF1pygp68mmgCQmUjiTA4lETQdmINc0C0W-xlnXOjRN2ScWmmZrQ5NuUiIaAdYVmDHPkAZzUjrdgMv8CKNkyTmWXJBmvrpOI0HRy2O8bd4g4Uq5ReSLPH7d5qoDdgpZpLAmI3asnv8QpiuUYlC--JC7JpmUKnzZNCwVY5jmq3B71ngEjh7bV2-dTyi4-3tc3ZKiu6_PWcInphhKeckRVKBe7FTKKWMhTfebBL5limV4K8kvHEWwdx1zFhXEkLplqmbO3wjdL1R4QtnST10-KZrCJ383RTvoWOZYg_vTi6SJW2m2cgZO-NTpmlgz-xZkylN0_-VCfoqHrF8rXMt3MiJ5qdctj_yZ9ZHvqbMuRdM7G6fiNjRmJyRRlHkLtpWLUa-bfWTTiN3ZM06pGusyBvet4R3M-9EGPlBZAe9hFW-rsri5UHwuCF0F37knwiDqR1NnF5Cb2J741oh8KwFzjdoilW8QU9QPRqi6HFVhfWTOT9-PBspDlM8jPkazQSBan57yhP4oOkfSzTHCj8bP3-eYdxrGNSAlvDSa_Qa0vYOhwaKheBvcoiZQjkWmDHCvlSdfDaOxwoEc61bCi_KZYkmeS7PmU-S9KxBK0Ai2GnQV0W2CIMxhWYinrbyPkF1n0uRSHH0CKtOMqy4AMlnvP5lrUue0HRfoWgGuJXCWk-CHu6v9mp0iS91lSSUtBgtYEmThEH1gnQYgk63ebYjsAe0hdU_CaWCbxHPCIq42GKlSScZhyaIDuP4iqaPdLo4Dz1AT1Lg61DcXRcFo7MM9q2PdN2JYF3R0I_WYhazSZfE7pDA3yMtS0IkXWfwu5N_l-N8OjHlDNbyN_JXQaSCb0zoDhjKKULXa5hbsDaTIlYNz-dzHrflkYrn7Wy7qKYUmrTYj9N8Of-CpoWEw0lKNEm2NDvL4nXK3mfxr1ed_x9XHfQFDYe_w7exK9OvTb8yR7U5qsygNoPKHNfmuKZqwHaN9jq2U9teZbq12Shpht_VttXArdrRaHU7ALsmvGvsuhjbPdt-dYnNsXPhds7PjouI2xvxeiN-b2TUGwl6I-PeyF1vBNrVG7L7Q87pqnHpd-trwaXXa87GS7ffuA3T2BLYq2hihAejvBjC5TEhKS6YMo6mgQvF9fQ2wvICZRTlETOnGFbJtnIe_wHkM0Vb" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 PLB-020-120_Master_Production_Scheduling_(IP) — PLB-020-120_Master_Production_Scheduling_(IP)

**Swim Lanes**: Analytics Specialist · Boundary Apps · FTS IP - Production Planner | **Tasks**: 13 | **Gateways**: 4

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
    subgraph Analytics Specialist
        n6[["fa:fa-cog Transfer the Data to S4 HANA"]]
        n7[["fa:fa-cog Stage Firm Order Details and Send Back to BY"]]
        n8[["fa:fa-cog Send Order Details to Blue Yonder"]]
    end
    subgraph Boundary Apps
        n1[["fa:fa-cog Send Planned Orders"]]
        n2[["fa:fa-cog Send Planned Purchase / Purchase Requisition"]]
        n3[["fa:fa-cog Send Planned Arrivals / Stock Transfer Requests"]]
        n4[["fa:fa-cog Receive Order Details from S4 HANA"]]
        n5[["fa:fa-cog Run MPS"]]
        n14(["fa:fa-play Request Initiated for Master Production Schedule (MPS) Process"])
        n15(["fa:fa-stop Master Production Scheduling (MPS) Completed"])
        n16{{"fa:fa-arrows-alt parallelGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph FTS IP - Production Planner
        n9[["fa:fa-cog Create Production Orders"]]
        n10[["fa:fa-cog Create Purchase Requisition (Type A)"]]
        n11[["fa:fa-cog Create Stock Transfer Requisition"]]
        n12[["fa:fa-cog Convert Purchase Requisition into Purchase Order"]]
        n13[["fa:fa-cog Convert Stock Transfer Requisition into Stock Transfer Order"]]
        n18{{"fa:fa-arrows-alt parallelGateway"}}
        n19{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n14 --> n5
    n11 --> n13
    n10 --> n12
    n4 --> n15
    n5 --> n16
    n16 --> n1
    n16 --> n2
    n16 --> n3
    n2 --> n17
    n6 --> n18
    n18 --> n9
    n18 --> n10
    n18 --> n11
    n12 --> n19
    n13 --> n19
    n19 --> n8
    n9 --> n19
    n8 --> n7
    n7 --> n4
    n1 --> n17
    n3 --> n17
    n17 --> n6
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
    class n14 startEvt
    class n15 endEvt
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV9tu4zYQ_RVCQeAEsFFdLVsPBXyJ2gCbNojSFovNPjDSyCZCiypJOXEN_3tJW_KFKy3QrR8Mz5k5Z4ajGUneWinLwIqs6-stKYiM0LYnl7CCXoR6r1hAr48OwJ-YE_xKQfR0TM4KmZB_9mGOX37oMI3FeEXoRqMJLBigP-77aKKItI8ELsRAACd5r98rOVlhvpkxyriOvoJRbuf7bLVryngG_BRg26GTBopKSQEn2Av90I81T0DKiuxCNA_yUZ72dro4yt7TJeZyX34l4AF__EUyuVR2jqkAFbOUK_oJvwLVZ5S80lha8XXTDCJ0nkI1LClxSoqFwn1bQRwXbycosHc7tLu-fimOSdGnp5cCqU9KsRBzyJGQCr5bS5QTSqMrfzaJA7svJGdvEF25d-Hcc_upPkmkjm73dXMH70AWSxm9MprVoYN3fYbILT_6_CNy7T7fqG8jFxTZKdNs6I7c0THTNHRmzqzJlOf5_8qk-sqfsXirc915sRvPj7mcYBjM7G_1mmPO_XDimH0CviYpnInGcezdnVp1Nwwcu1t0GntDe2aILrCEd7w5CY5n_lEwDsLYCTsFD_nMKqvXR87SRtC7C-LgKBhOnXjidgr6E8cf1RUqnQXH5RJNCkw3kqQCJSWkan-IkIcQ_SmGX768WDmOcjxI2QI9qwEUOXCkNhXNscRIMpT46NfJb5MX6-vXM2Z4yUwkXgCKCV-h3_W-oTlITKhAuMhQogYHTXH6puWmnw2lkaGkgy81NItWgD6rvQR-oqtI47hTVu1XF03KUpzlcFpyPFJcFFDnEkZR7ncIjxVXyygA_XT6-QR_V0QQSVhhKHnfUZpwTtbqpqGUEslUf44XQOuBkGZZ_qXYE6RA1mC0K-ds1XHVAoNfFejhMTGCHP_mGFVSNd51Mehe3diJGvkM5YyjByykyqrmNatSfXCUpEvIKgroRoneak8KQh_h9lw9OKkLycpuHXUXrJVmbFVSUIlNreF222hhztm7GGAqUYk5phToL4f1fLF2u3NS-N9I305Z_Jyg-0c0OK_5cEn5WZ7xZa9nHJTyOaV18By7ndYyaOjmeVMCmtyaEk6rRMuEtU-sYwz_jBVrUM-e1hpIobbz6NkfyZTz2uW66zmIGv5W6dGPXP_xD15_tRhoMPhZbVFjOwfb8RrArgG3BmqC0zCC2h42hGENGLZr2E0Ctw4Pa7uhj5r40QEYG7Zjm8AxYyN5pHgmMD4ATY6x4a8Vm5LCg-k3bKNiz7CdOn549iTUrLPn9YXH7fR4nR6_0xN0eoadnrDTM-r0jDs9amQ6Xd1dcLrb4HT3Qc1v87p4iQf1q90lOmzeby7hsB0etcPjBrb61gr4CpPMirbW_q-A-ruQQY4rKq1d38KVZMmmSK1o_8psVWWmmHOC1U13dQB3_wKrBeWV" title="View in Mermaid Live">&#128065; View in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Analytics Specialist | PLB-020-010_Supply_Parameter_&amp;_Data_Management_(010)_(IP), PLB-020-120_Master_Production_Scheduling_(IP) | |
| Boundary Apps | PLB-020-010_Supply_Parameter_&amp;_Data_Management_(010)_(IP), PLB-020-050_Distribution_Requirements_Planning_(IP), PLB-020-090_Product_Data_Management_(IP), PLB-020-120_Master_Production_Scheduling_(IP) | |
| FTS IP - Production Planner | PLB-020-010_Supply_Parameter_&amp;_Data_Management_(010)_(IP), PLB-020-050_Distribution_Requirements_Planning_(IP), PLB-020-120_Master_Production_Scheduling_(IP) | |
| Batch User | PLB-020-050_Distribution_Requirements_Planning_(IP),  | |
| FTS IF Logistic Business Role | PLB-020-050_Distribution_Requirements_Planning_(IP),  | |
| Master Data Team | PLB-020-050_Distribution_Requirements_Planning_(IP),  | |
| Material Planner | PLB-020-050_Distribution_Requirements_Planning_(IP),  | |
| RFC User | PLB-020-050_Distribution_Requirements_Planning_(IP),  | |
| Batch User - FTS | PLB-020-090_Product_Data_Management_(IP),  | |
| MDG Business Admin | PLB-020-090_Product_Data_Management_(IP),  | |

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for PLB-020. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
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

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for PLB-020.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for PLB-020.

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

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
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

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for PLB-020:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for PLB-020:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (51 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>PLB-020 — Supply Planning & Management (IP)</span></div>
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

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

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
*PLB-020 — Architecture Document (TOGAF BDAT) · Forecast to Stock (IP) · Generated: March 2026*

