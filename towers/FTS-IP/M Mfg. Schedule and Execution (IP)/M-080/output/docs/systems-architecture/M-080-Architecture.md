<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">M-080 — Perform Materials Requirement Planning (IP)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Forecast to Stock (IP) (FTS-IP) Tower<br/>
  Capability M-080 · M Mfg. Schedule and Execution (IP)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **M-080 Perform Materials Requirement Planning (IP)** within the IAO program. It includes 5 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Forecast to Stock (IP) (FTS-IP) |
| **Process Group** | M Mfg. Schedule and Execution (IP) |
| **Capability** | M-080 - Perform Materials Requirement Planning (IP) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 2 Reports, 34 Interfaces, 20 Conversions, 35 Enhancements, 7 Forms, 3 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Forecast to Stock (IP) |
| **L1 Process** | M Mfg. Schedule and Execution (IP) |
| **L2 Capability** | M-080 - Perform Materials Requirement Planning (IP) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Intel Products Supply Chain Unification | Consolidate Intel Products manufacturing and logistics onto S/4 HANA platform | IDM 2.0 Products Transformation | High |
| 2 | End-to-End Traceability | Enable lot/batch traceability from raw material to finished goods shipment | Quality & Compliance | High |
| 3 | Demand-Supply Matching | Implement responsive demand and supply matching (RDSM) for IP product lines | Supply Chain Agility | Medium |
| 4 | M-080 Process Migration | Migrate Perform Materials Requirement Planning (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Supply Chain (Intel Products) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Production Schedule Adherence | > 95% | Percentage of production orders completed on schedule | 88% (current) | Production Manager |
| Material Availability Rate | > 98% | Materials available at point of need for production | 94% (current) | Materials Planning |
| Shipping On-Time Delivery | > 97% | Orders shipped within committed delivery window | 93% (current) | Logistics Lead |
| M-080 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **5 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for M-080 Perform Materials Requirement Planning (IP).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | M-080-010_Run_MRP_for_All_Materials_(IP) | M-080-010_Run_MRP_for_All_Materials_(IP) | Boundary Apps, IT Department, Material Planner | 9 | 2 |
| 2 | M-080-020_Run_MRP_for_Single_Material_(IP) | M-080-020_Run_MRP_for_Single_Material_(IP) | Boundary Apps, IT Department, Material Planner | 10 | 4 |
| 3 | M-080-030_Run_MRP_for_All_Programs_(Mfg.)_(IP) | M-080-030_Run_MRP_for_All_Programs_(Mfg.)_(IP) | Boundary Apps, IT Department, Material Planner | 10 | 4 |
| 4 | M-080-060_Analyze_Alternatives_and_Determine_Changes_(MRP)_(IP) | M-080-060_Analyze_Alternatives_and_Determine_Changes_(MRP)_(IP) | IT Department, Master Data Steward, Material Planner | 3 | 0 |
| 5 | M-080-070_Edit_MRP_List_(IP) | M-080-070_Edit_MRP_List_(IP) | Material Planner | 1 | 0 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 M-080-010_Run_MRP_for_All_Materials_(IP) — M-080-010_Run_MRP_for_All_Materials_(IP)

**Swim Lanes**: Boundary Apps · IT Department · Material Planner | **Tasks**: 9 | **Gateways**: 2

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
        n8["Perform Planning in Boundary Apps"]
        n9["Send Planned Production order to S4"]
        n12(["fa:fa-play Initiate request for planning in Boundary Apps"])
    end
    subgraph IT Department
        n6["Receive Planned Production Order From Boundary Apps"]
        n7["Send Planned Production Order to S4HANA"]
    end
    subgraph Material Planner
        n1["fa:fa-user Monitor Material Requirement Planning (MRP)"]
        n2["fa:fa-user Create/Revise Demands/ Create Planned Independent Requirement for ALPS"]
        n3["Run MRP for All Materials"]
        n4["Create Purchase Requisition for ALPS Material"]
        n5["Create Production Order"]
        n10(["fa:fa-play Request Received to Run MRP for ALPS Material"])
        n11(["fa:fa-play Request Received to run MRP for Master Data changes"])
        n13["Analyze Alternatives and Determine Changes (MRP) (IP)"]
        n14{{"fa:fa-arrows-alt parallelGateway"}}
        n15{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n14 --> n2
    n11 --> n1
    n10 --> n14
    n8 --> n9
    n9 --> n6
    n12 --> n8
    n5 --> n15
    n4 --> n15
    n15 --> n13
    n2 --> n3
    n1 --> n14
    n3 --> n4
    n6 --> n7
    class n1 userTask
    class n2 userTask
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl1v4jgU_StWqopWCpokJITmYSW-slup7CCYmX3Y7oNJHLDq2Fk7gTKI_77X5APIDNWulodW93DvOfceX5wcjEjExAiM-_sD5TQP0KGTb0hKOgHqrLAiHROVwDcsKV4xojo6JxE8X9LvpzTbzd51msZCnFK21-iSrAVBX59NNIRCZiKFueoqImnSMTuZpCmW-7FgQursOzJIrOSkVn01EjIm8pxgWb4deVDKKCdnuOe7vhvqOkUiweMr0sRLBknUOermmNhFGyzzU_uFIjP8_geN8w3ECWaKQM4mT9kLXhGmZ8xlobGokNvaDKq0DgfDlhmOKF8D7loASczfzpBnHY_oeH__yhtR9LJ45Qg-EcNKTUiCVA7wdJujhDIW3LnjYehZpsqleCPBnTP1Jz3HjPQkAYxumdrc7o7Q9SYPVoLFVWp3p2cInOzdlO-BY5lyD39bWoTHZ6Vx3xk4g0Zp5Ntje1wrJUnyv5TAV_kFq7dKa9oLnXDSaNle3xtbP_LVY05cf2i3fSJySyNyQRqGYW96tmra92zrNuko7PWtcYt0jXOyw_sz4dPYbQhDzw9t_yZhqdfusljNpYhqwt7UC72G0B_Z4dC5SegObXdQdQg8a4mzDRqJ4rTLaJhlqvxOf_jgz1djTmQiZIrmDHMOK4cob-Ubf12UPEHJElagzCfwX4q4iHIqODr9xlAu0NK9LrKdByhLcJDgbsbAqme4HCjYhiT5uyAKtklIlH3QwWPJBsKt0Z6_oAnJYPtTwvMLyT4ILkhE6Jb8rNXPp1ZDKdKPhvU_GPbzedjfhr8Pm8IfW5zBoPrSqljkpTGNLXrX0UyAL-BEU7EAe6gkerbzAT3MFvPH60ada56xJMDwaUG2VBHwJ8U8Vp8quBnmmcckg3Y1-aWQPovhy3x5LdHThhYcgXiZwVjTZ8s2F1JrrULClQVNnAQUPVlXCzT11-XeRXnL79ZaWa21WlTbVB18rI_nqueW6OMlmf0vyOQF2QwrIEITnGMEM_I1UW1K7dmQY7b_TsAvyOY4ByqF4DzgWABI4fGDxmV1ebDo4bl9urZ7ONStYSnFTnUxyxFsPWaMsF_L--fVOB4vi7z_VtTsLcihbvcXWKo6tsvYrmOrit0KGJTxUxU-lWG_TnfKeFDFXlXtVbHbiu06oVcBVX0d2i31XhnXYb8M_Ys7VdfUz5Ir2Pk5DAPWD9Rr3L6BOzfw3g3crZ8Z17BXw4ZppLAbmMZGcDBOL0zwUhWTBBcsN46mgYtcLPc8MoLTi4VRZDFUTiiGGyctweM_rSYENg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 M-080-020_Run_MRP_for_Single_Material_(IP) — M-080-020_Run_MRP_for_Single_Material_(IP)

**Swim Lanes**: Boundary Apps · IT Department · Material Planner | **Tasks**: 10 | **Gateways**: 4

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
        n9["Perform Planning in Boundary Apps"]
        n10["Send Planned Production order to S4"]
        n13(["fa:fa-play Initiate request for planning in Boundary Apps"])
    end
    subgraph IT Department
        n7["Receive Planned Production Order From Boundary Apps"]
        n8["Send Planned Production Order to S4HANA"]
    end
    subgraph Material Planner
        n1["fa:fa-user Monitor Material Requirement Planning (MRP) (Master Data Changes Daily)"]
        n2["fa:fa-user Create/Revise Demands"]
        n3["Run MRP for Single Material"]
        n4["Create Purchase Requisition"]
        n5["Create Production order"]
        n6["Create Planned Order"]
        n11(["fa:fa-play Request Received to Run MRP for All Materials"])
        n12(["fa:fa-play Request Received to Monitor Master Data Changes Daily"])
        n14["Analyze Alternatives and Determine Changes (MRP) (IP)"]
        n15{{"fa:fa-arrows-alt parallelGateway"}}
        n16{{"fa:fa-arrows-alt parallelGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n17 --> n2
    n12 --> n1
    n11 --> n17
    n2 --> n3
    n3 --> n15
    n15 --> n6
    n15 --> n4
    n1 --> n17
    n5 --> n16
    n4 --> n16
    n16 --> n14
    n6 --> n18
    n18 --> n5
    n8 --> n18
    n9 --> n10
    n13 --> n9
    n10 --> n7
    n7 --> n8
    class n1 userTask
    class n2 userTask
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 startEvt
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVttu4zYQ_RVCQeANIKO6WooeCji21QbYbAx7u_vQ9IGRKJsIRaqklMRr-N87tC62lThot36QMYczZ2YORxS3RiJSYkTG5eWWclpGaDso1yQngwgNHrEiAxPVwDcsKX5kRA20TyZ4uaQ_9m62V7xqN43FOKdso9ElWQmC_rg10RgCmYkU5mqoiKTZwBwUkuZYbiaCCam9L0iYWdk-W7N0I2RK5MHBsgI78SGUUU4OsBt4gRfrOEUSwdMT0szPwiwZ7HRxTLwkayzLffmVInf49TtNyzXYGWaKgM-6zNln_EiY7rGUlcaSSj63YlCl83AQbFnghPIV4J4FkMT86QD51m6HdpeXD7xLij4vHjiCX8KwUlOSIVUCPHsuUUYZiy68yTj2LVOVUjyR6MKZBVPXMRPdSQStW6YWd_hC6GpdRo-CpY3r8EX3EDnFqylfI8cy5QaevVyEp4dMk5ETOmGX6SawJ_akzZRl2f_KBLrKr1g9NblmbuzE0y6X7Y_8ifWWr21z6gVju68Tkc80IUekcRy7s4NUs5FvW-dJb2J3ZE16pCtckhe8ORBeT7yOMPaD2A7OEtb5-lVWj3MpkpbQnfmx3xEGN3Y8ds4SemPbC5sKgWclcbFGN6LazzIaF4Wq1_SPX__5YMyJzITM0ZxhzmHkEOU9f-OvoxDbgpglzEAdQOBfirRKSio42r9kqBRo6fWi3E8QluEow8OCgVa3cDpQ0A1J8ndFFIyTkKj4oISrmg0S93q7_YqmpIDxzwkvj1IGkHBBEkKfyXul3u9LjaXIP-o2_KDZ-0Ozv4-_jLvAtyXeQaP61GpY5LEwnSx62NGdAF1AiS5iAfJQSXRvhx36dLeYX8ETK_BCU1xiNFljviIKDDgwr06bcE5zTCQB9l8W5JkqAtrlmKe9tl2tXcUR5NlvzBKyMtJVdersgXPNieaVhAMKWPdlK6p1OnX2j5x7c3PqODpybLS_f-tl2725WjTj1Ox8qvfnuJMxY10bR2NVkzn_guywQ2fE75NqecYcs80PAtkhhuMSyBQC2UF9AHL4BHUczd7eznubaPvbbVscllK8qCFmJYLBx4wR9lt9Bj0Yu91x0OhngoKfCQr_W1D3kkA6NBz-ClPa2k5t261tN3bQAM2625hus-y3_n4NjHq219o9umbZbv29nm2PGqAlaO2wdQhroC0g7K1fN7bV-jcVX7e2VdttQY0e4dFHQVfdfgxPYOd9GDRrbwSnuHMGd8_g3hncbz96p_DofTh4Hw5b2DCNHF4DTFMj2hr7-yHcIVOS4YqVxs40cFWK5YYnRrS_RxlVkULklGI4X_Ma3P0DFddJMA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 M-080-030_Run_MRP_for_All_Programs_(Mfg.)_(IP) — M-080-030_Run_MRP_for_All_Programs_(Mfg.)_(IP)

**Swim Lanes**: Boundary Apps · IT Department · Material Planner | **Tasks**: 10 | **Gateways**: 4

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
        n9["Perform Planning in Boundary Apps"]
        n10["Send Planned Production Order to S4"]
        n13(["fa:fa-play Initiate request for planning in Boundary Apps"])
    end
    subgraph IT Department
        n7["Receive Planned Production Order From Boundary Apps"]
        n8["Send Planned Production Order to S4HANA"]
    end
    subgraph Material Planner
        n1["fa:fa-user Monitor MRP (Master Data Changes Daily)"]
        n2["fa:fa-user Create/Revise Demand for All the Materials"]
        n3["Create Purchase Requisition"]
        n4["Run Full Planning MPS or MRP"]
        n5["Create Planned Orders"]
        n6["Create Production Order"]
        n11(["fa:fa-play Request Received to Run Material Requirement Planning (MRP) for All Programs"])
        n12(["fa:fa-play Request Received to Monitor Master Data Changes Daily"])
        n14(["fa:fa-stop MRP Run for All Programs Done"])
        n15{{"fa:fa-arrows-alt parallelGateway"}}
        n16{{"fa:fa-arrows-alt parallelGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n11 --> n17
    n3 --> n16
    n4 --> n15
    n15 --> n5
    n15 --> n3
    n12 --> n1
    n17 --> n2
    n1 --> n17
    n16 --> n14
    n2 --> n4
    n9 --> n10
    n13 --> n9
    n10 --> n7
    n7 --> n8
    n6 --> n16
    n8 --> n18
    n5 --> n18
    n18 --> n6
    class n1 userTask
    class n2 userTask
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 endEvt
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl1v6kYQ_SsrRxGJZFR_m_ihEgHcRrq0CG7bh6YPi72GVdZed9dOQhH_vbN4bcA3XN3e8pBojufMmTk7_tgbCU-JERm3t3ta0CpC-0G1JTkZRGiwxpIMTNQAv2NB8ZoROVA5GS-qFf3nmGZ75btKU1iMc8p2Cl2RDSfotycTjYHITCRxIYeSCJoNzEEpaI7FbsIZFyr7howyKzuq6UuPXKREnBIsK7QTH6iMFuQEu6EXerHiSZLwIr0omvnZKEsGB9Uc42_JFovq2H4tyRy__0HTagtxhpkkkLOtcvYJrwlTM1aiVlhSi9fWDCqVTgGGrUqc0GIDuGcBJHDxcoJ863BAh9vb56ITRZ-WzwWCX8KwlFOSIVkBPHutUEYZi268yTj2LVNWgr-Q6MaZhVPXMRM1SQSjW6Yyd_hG6GZbRWvOUp06fFMzRE75bor3yLFMsYO_PS1SpCelSeCMnFGn9BjaE3vSKmVZ9r-UwFfxGcsXrTVzYyeedlq2H_gT68t67ZhTLxzbfZ-IeKUJOSsax7E7O1k1C3zbul70MXYDa9IrusEVecO7U8GHidcVjP0wtsOrBRu9fpf1eiF40hZ0Z37sdwXDRzseO1cLemPbG-kOoc5G4HKLHnl93GU0LkvZXFO_4uHPZ2NBRMZFjhYMFwWsHKJFL9_464xiW8BZwQ40BAL_BU_rpKK8QL-qmwxVHK28Hsu9A1qGowwPSwZePcHTgYJvSJC_ayJhnbhA5VdauG-qgXBvtqfPaEpKWP-cFNWZZAiCS5IQ-kqutxoLnn9t2tG3Dfvz-JdxR_yyxTkMqp5auoo4N6azRS07mnPwBZyYLxfobo4l8NAUVxhNtrjYEAkBPBDvL5t0LmtMBAG9H5bklUoC3uQY-lf2jhlD8PDt2unN6kKZhosWtYAHDbCXcDpUUjXvZbKn3K0LFNeMnVZnvlihpvvLbP-stDby6F6vg-Asredzb53s3jot9RbpA0_Vsaj2OuePgwiiduTU7h00et9ZA5JwXPnZsjVazjdoded27cj6Rb1TUVnx8njgquF-M2jKC9In-_t9S8ZC8Dc5xKxCcA9gxgj7qXkcPRuHwzkp-B5S-D2k0X8jdfcLHCsaDn9UshpwdRzo2NOx3xL8BujHbhs7mtDGYRM7bdzTswMNeBrQ_DZ80JetNl83-NDGVhO39bTcSIdBb5yRjtvrfi-2dUJw9n5QTbfvxQvY-RgGT9uPg0vcuYK7V3BPv_gvUb99-13Cwcdw-DE8amHDNHIickxTI9obxw9F-JhMSYZrVhkH08B1xVe7IjGi4weVUZcpMKcUq5ulAQ__Aqi7SzA=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 M-080-060_Analyze_Alternatives_and_Determine_Changes_(MRP)_(IP) — M-080-060_Analyze_Alternatives_and_Determine_Changes_(MRP)_(IP)

**Swim Lanes**: IT Department · Master Data Steward · Material Planner | **Tasks**: 3 | **Gateways**: 0

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
        n3["fa:fa-user Analyze the Material Requirement Planning (MRP) Output"]
        n5["Run MRP for All Materials"]
    end
    subgraph Master Data Steward
        n2["fa:fa-user Make an Adjustment in the Master Data ( If Required)"]
    end
    subgraph Material Planner
        n1["fa:fa-user Check any Rescheduling in the Planning Required"]
        n4(["fa:fa-stop Alternatives Analyzed and MRP Changes Determined Successfully"])
    end
    n5 --> n3
    n2 --> n1
    n1 --> n4
    n3 --> n2
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 endEvt
    class n5 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVU1v4zYU_CuEgsAJIAP6jFwdCjiSBQSo0SBO20OzB1p6tLimKS9JJfEG_u_7aMvyRzd7qQ4COBzOvDciqQ-nbCpwUuf6-oNLblLyMTA1rGCQksGcahi4ZA_8TRWncwF6YDmskWbGv-9ofrR-tzSLFXTFxcaiM1g0QP56cMkYFwqXaCr1UIPibOAO1oqvqNpkjWiUZV_BiHls59ZN3TeqAnUkeF7ilzEuFVzCEQ6TKIkKu05D2cjqTJTFbMTKwdYWJ5q3sqbK7MpvNUzp-z-8MjWOGRUakFOblfiDzkHYHo1qLVa26vUQBtfWR2JgszUtuVwgHnkIKSqXRyj2tluyvb5-kb0pec5fJMGnFFTrHBjRBuHJqyGMC5FeRdm4iD1XG9UsIb0KJkkeBm5pO0mxdc-14Q7fgC9qk84bUXXU4ZvtIQ3W7656TwPPVRt8X3iBrI5O2V0wCka9033iZ352cGKM_S8nzFU9U73svCZhERR57-XHd3Hm_Vfv0GYeJWP_MidQr7yEE9GiKMLJMarJXex7n4veF-Gdl12ILqiBN7o5Cv6WRb1gESeFn3wquPe7rLKdP6qmPAiGk7iIe8Hk3i_GwaeC0diPRl2FqLNQdF2Th2eSwxq3yAqk2c_ZR4b_vjiMpowObdRkLKnYfAeCJ5RMsSl70sgTfGu5AruSPAoqJW5LcjN9erwlf7Zm3ZoX58uJZIyST60kSCCsQU0hei3dU3EPXZQ4pRpJJKeGkpnNU1UnqsF5oVO6BEIlGVdfW71rinDZlX2UuSEP7FB-dftL767XXX-gToz9c-OshnKJzhvU1WUNVStsHJ15H8_B9Dya6KYX06ZZYzRoK6nhr6AP2VcoXu3Cy2oqFziRA7JWeEtVZNaWJWjNWiE2KH170Y-MyXD4O37Vbhjsh90ZkP5-GHXDcD8MTvae5RzO3Bkc_BwOfw5H3RVxBsb9HeW4zgo7orxy0g9n9zfAP0YFjLbCOFvXoa1pZhtZOunu1nTadYUfKOcUv9ZqD25_AFhEEJo=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.5 M-080-070_Edit_MRP_List_(IP) — M-080-070_Edit_MRP_List_(IP)

**Swim Lanes**: Material Planner | **Tasks**: 1 | **Gateways**: 0

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
    subgraph Material Planner
        n1["fa:fa-user Edit Material Requirement Planning (MRP) List"]
        n2(["fa:fa-play Request Received to Edit MRP List"])
        n3(["fa:fa-stop MRP List Edit Completed"])
    end
    n2 --> n1
    n1 --> n3
    class n1 userTask
    class n2 startEvt
    class n3 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVE2P2jAU_CtWVii7UpDySWgOlSAQqVJXQsu2PZQeTPIM1jpOapuvIv57bQIJS7Wn5pDEkzcz743sHK28KsBKrF7vSDlVCTraag0l2Amyl1iC7aAG-I4FxUsG0jY1pOJqTv-cy7yw3psyg2W4pOxg0DmsKkDfvjhopInMQRJz2ZcgKLEduxa0xOKQVqwSpvoBhsQlZ7fLp3ElChBdgevGXh5pKqMcOjiIwzjMDE9CXvHinSiJyJDk9sk0x6pdvsZCndvfSHjG-x-0UGu9JphJ0DVrVbKveAnMzKjExmD5RmyvYVBpfLgObF7jnPKVxkNXQwLztw6K3NMJnXq9BW9N0etkwZG-coalnABBUml4ulWIUMaShzAdZZHrSCWqN0ge_Gk8CXwnN5MkenTXMeH2d0BXa5UsK1ZcSvs7M0Pi13tH7BPfdcRB3--8gBedUzrwh_6wdRrHXuqlVydCyH856VzFK5ZvF69pkPnZpPXyokGUuv_qXcechPHIu88JxJbmcCOaZVkw7aKaDiLP_Vh0nAUDN70TXWEFO3zoBD-lYSuYRXHmxR8KNn73XW6WM1HlV8FgGmVRKxiPvWzkfygYjrxweOlQ66wErtfoWXdojg2aMcw5iOazubj3c2ERnBDcN2mjaUFVV_4CvzdU6OPKVUPVWxI9Pr_MntBXKtXC-nWj5D-2UjXTcRgySKWfOdAtFEhVF_mX2ZX-dMMPOr5UVd2WNaS0KmsGCoqOpTdi88J91O9_1rNcll6zDG5iNeB1O72D_fbsvIODyza3HKsEUWJaWMnROv-69O-tAII3TFknx8IbVc0PPLeS8xG3NnWh05tQrJMvG_D0F3vloes=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | M-080-010_Run_MRP_for_All_Materials_(IP), M-080-020_Run_MRP_for_Single_Material_(IP), M-080-030_Run_MRP_for_All_Programs_(Mfg.)_(IP),  | |
| IT Department | M-080-010_Run_MRP_for_All_Materials_(IP), M-080-020_Run_MRP_for_Single_Material_(IP), M-080-030_Run_MRP_for_All_Programs_(Mfg.)_(IP), M-080-060_Analyze_Alternatives_and_Determine_Changes_(MRP)_(IP),  | |
| Material Planner | M-080-010_Run_MRP_for_All_Materials_(IP), M-080-020_Run_MRP_for_Single_Material_(IP), M-080-030_Run_MRP_for_All_Programs_(Mfg.)_(IP), M-080-060_Analyze_Alternatives_and_Determine_Changes_(MRP)_(IP), M-080-070_Edit_MRP_List_(IP) | |
| Master Data Steward | M-080-060_Analyze_Alternatives_and_Determine_Changes_(MRP)_(IP),  | |

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for M-080. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
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
| LOGM024_IP | Conversion | Create/Upload Vehicle resource | 10. Object Complete |  |  | N/A |
| LOGM023_IP | Conversion | Update Business Share | 10. Object Complete |  |  | N/A |
| LOGM022_IP | Conversion | Upload Transportation Allocation | 10. Object Complete |  |  | N/A |
| LOGM021_IP | Conversion | Upload Schedules | 10. Object Complete |  |  | N/A |
| LOGM019_IP | Conversion | Default Routes | 10. Object Complete |  | S4 | N/A |
| LOGM018_IP | Conversion | Upload Rate Table | 10. Object Complete |  |  | N/A |
| LOGM016_IP | Conversion | Create and review Charge Calculation Sheet | 10. Object Complete |  | S4 | N/A |
| LOGM015_IP | Conversion | Create and review Freight Agreement | 10. Object Complete |  | S4 | N/A |
| LOGM012_IP | Conversion | Creation of Location based on BP, Shipping points, plants | 10. Object Complete | ECC | S4 | N/A |
| LOGM008_IP | Conversion | Location creation-ocean ports, airports | 10. Object Complete |  |  | N/A |
| LOGM005_IP | Conversion | UPLOAD TRANSPORTATION ZONES (TM) | 10. Object Complete | TMS | S4 | N/A |
| LOGM004_IP | Conversion | UPLOAD TRANSPORTATION LANES | 10. Object Complete | TMS | S4 | N/A |
| LOGC1500 | Conversion | IM Stock conversion from Non SAP system to S4 system | 10. Object Complete |  |  | 02.High |
| LOGC0972_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  |  | 02.High |
| LOGC0946_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  |  | 02.High |
| FTSM002_IP | Conversion | Work Center | 10. Object Complete | NA | S4 | N/A |
| FTSC1682 | Conversion | Conversion of Intel Products Bailed Inventory & Lot Attributes | 10. Object Complete |  |  | 03.Medium |
| FTSC1559 | Conversion | Conversion of Open PO/Engineering/Rework Orders into Production orders from I... | 10. Object Complete |  |  | 03.Medium |
| FTSC0434 | Conversion | Conversion of Open Production Orders from ECC purchase order data into S4 | 10. Object Complete | ECC | S4 HANA | 03.Medium |
| FTSC0052_IP | Conversion | Conversion of Reference Operation Sets to S/4 | 10. Object Complete | ECC | S4 | 03.Medium |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for M-080.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for M-080.

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

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| LOGW1078_IP | Workflow | ISM Workflows - Capital/AMT | 10. Object Complete |  | NA | 03.Medium |
| LOGW1077_IP | Workflow | ISM Workflows - EIMS/Lab | 10. Object Complete |  | NA | 03.Medium |
| LOGW1076_IP | Workflow | ISM Workflows - Non-inventory | 10. Object Complete |  | NA | 02.High |
| LOGR1176_IP | Report | ISM - International Traffic Report | 10. Object Complete |  | NA | 02.High |
| LOGR0833_IP | Report | Email Notification for deletion of Shipping Memos | 10. Object Complete |  | NA | 03.Medium |
| LOGM024_IP | Conversion | Create/Upload Vehicle resource | 10. Object Complete |  | NA | N/A |
| LOGM023_IP | Conversion | Update Business Share | 10. Object Complete |  | NA | N/A |
| LOGM022_IP | Conversion | Upload Transportation Allocation | 10. Object Complete |  | NA | N/A |
| LOGM021_IP | Conversion | Upload Schedules | 10. Object Complete |  | NA | N/A |
| LOGM019_IP | Conversion | Default Routes | 10. Object Complete |  → S4 | NA | N/A |
| LOGM018_IP | Conversion | Upload Rate Table | 10. Object Complete |  | NA | N/A |
| LOGM016_IP | Conversion | Create and review Charge Calculation Sheet | 10. Object Complete |  → S4 | NA | N/A |
| LOGM015_IP | Conversion | Create and review Freight Agreement | 10. Object Complete |  → S4 | NA | N/A |
| LOGM012_IP | Conversion | Creation of Location based on BP, Shipping points, plants | 10. Object Complete | ECC → S4 | NA | N/A |
| LOGM008_IP | Conversion | Location creation-ocean ports, airports | 10. Object Complete |  | NA | N/A |
| LOGM005_IP | Conversion | UPLOAD TRANSPORTATION ZONES (TM) | 10. Object Complete | TMS → S4 | NA | N/A |
| LOGM004_IP | Conversion | UPLOAD TRANSPORTATION LANES | 10. Object Complete | TMS → S4 | NA | N/A |
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
| LOGF1614_IP | Form | TM-Bill of lading print output ( NSO/ Prospal STO's) | 10. Object Complete |  | NA | 03.Medium |
| LOGF1100_IP | Form | Printing of Standard Shipping Label | 10. Object Complete |  | NA | 02.High |
| LOGF0359_IP | Form | ISM - Generate Commercial Invoice - IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0358_IP | Form | ISM - Generate Traveler Document - IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0352_IP | Form | ISM - IPLA | 10. Object Complete |  | NA | 02.High |
| LOGF0351_IP | Form | ISM - Custom China Special label | 10. Object Complete |  | NA | 02.High |
| LOGF0350_IP | Form | ISM - India GST DC | 10. Object Complete |  | NA | 02.High |
| LOGE1686 | Enhancement | IP custom table for reconciliation data | 10. Object Complete |  | NA | 03.Medium |
| LOGE1572_IP | Enhancement | SAP GUI T-code to Move stock from Blocked to unblock Status | 10. Object Complete |  | NA | 02.High |
| LOGE1569_IP | Enhancement | Enhancement to change billing status based on ship reason in ISM | 10. Object Complete |  | NA | 03.Medium |
| LOGE1526_IP | Enhancement | Automatic HAWB assignment for Freight Forwarders( ISM/ Prospal STO's) | 10. Object Complete |  | NA | 02.High |
| LOGE1327 | Enhancement | ECD_Enhancement to retrieve plant details for material/batch and update custo... | 08. FUT In Progress |  | NA | 02.High |
| LOGE1276_IP | Enhancement | TM:Replace VTRC and integrate with parcel carrier to retrieve the package lev... | 10. Object Complete |  | NA | 03.Medium |
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
| LOGE0405_IP | Enhancement | Dangerous Goods indicator from the delivery header text to be transmitted to ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0403_IP | Enhancement | In SAP TM, update FU and FO Transportation Cockpit w/ custom fields Purchase ... | 10. Object Complete | NA → NA | NA | 02.High |
| LOGE0239_IP | Enhancement | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 - Table Creation | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0190_IP | Enhancement | Delivery Split for STO in S/4 | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGC1500 | Conversion | IM Stock conversion from Non SAP system to S4 system | 10. Object Complete |  | NA | 02.High |
| LOGC0972_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  | NA | 02.High |
| LOGC0946_IP | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  | NA | 02.High |
| FTSM002_IP | Conversion | Work Center | 10. Object Complete | NA → S4 | NA | N/A |
| FTSI1693 | Interface | Interface for Reporting Scrap of Semi Finished Goods at OSAT and IF manufactu... | 06. Dev In Progress |  | BODS | 03.Medium |
| FTSI1692 | Interface | Interface for Reporting Scrap of Semi Finished Goods at OSAT and IF manufactu... | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1681 | Interface | Enhancement to create Zero Lead Time Order to convert Sorted Wafers into Sort... | 10. Object Complete |  | MULESOFT | 03.Medium |
| FTSI1631 | Interface | Interface to update Remnants in production order | 10. Object Complete |  | APIGEE | 03.Medium |
| FTSI1619 | Interface | Interface to capture Sales Order 3B2 ASN and Virtual 3B2 ASN signals from Int... | 10. Object Complete |  | APIGEE | 02.High |
| LOGI1584 | Interface | Interface to post inventory in SAP S/4HANA from ECA via MuleSoft. | 06. Dev In Progress |  | MuleSoft | 03.Medium |
| FTSI1023 | Interface | Interface to Transfer stock from Unrestricted stock to Block stock and vice v... | 10. Object Complete | E2OPEN → S/4 | APIGEE | 03.Medium |
| FTSI1022 | Interface | Inbound Interface to update projected release quantity and date for lots on q... | 10. Object Complete | FLAT FILE → S/4 | NA | 03.Medium |
| FTSI0725 | Interface | Inbound interface to capture Yield Confirmation and Goods Receipt against Pro... | 10. Object Complete | E2OPEN → S/4 | APIGEE | 03.Medium |
| FTSI0724 | Interface | Inbound interface from e2open to IP SAP S4 HANA system to update Die Quantity... | 10. Object Complete | E2OPEN → S/4 | APIGEE | 02.High |
| FTSI0492 | Interface | Interface between E2Open and S4 for goods issue against production order | 10. Object Complete | E2Open → S/4 | APIGEE | 03.Medium |
| FTSI0491 | Interface | Interface between E2Open and S4 for capturing confirmation of scrap against p... | 10. Object Complete | E2Open → S/4 | APIGEE | 03.Medium |
| FTSI0268 | Interface | Interface to be developed from S/4 to E2Open to transmit Build Instruction​ d... | 10. Object Complete | S/4 → E2Open | MULESOFT | 03.Medium |
| FTSI0210 | Interface | Interface Function to Create Purchase Requisitions from ECA to S/4 | 10. Object Complete | ECA (PDH) → S/4 | BODS | 03.Medium |
| FTSI0209 | Interface | Interface to create Production Order from ECA to S/4 | 10. Object Complete | ECA (PDH) → S/4 | BODS | 03.Medium |
| FTSE1701 | Enhancement | Enhancement to automate updation of Routing_Prod versions with reference to S... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1694 | Enhancement | Enhancement to Introduction of additional restrictions by MRP Area for S4 IP ... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1653 | Enhancement | Enhancement to automate creation of Routing_Prod versions with reference to S... | 10. Object Complete |  | NA | 02.High |
| FTSE1642 | Enhancement | Enhancement to create a user exit (or) Business Add In to update Components a... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1597 | Enhancement | Develop a utility for mass creation of production orders via load file in SAP... | 10. Object Complete |  | NA | 02.High |
| FTSE1586 | Enhancement | Text Purchase Requisition while creating with reference to Production Order O... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1194 | Enhancement | Enhancement in IP SAP HANA system to re-assign the first operation plant to C... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1146 | Enhancement | Enhancement to link KB sales orders / STR to purchase requisition generated b... | 10. Object Complete |  | NA | 04.Low |
| FTSE1144 | Enhancement | Total Quantity’ update for Parent Production Order with reference to Actual G... | 10. Object Complete |  | NA | 03.Medium |
| FTSE1024 | Enhancement | Create a custom table and a custom Fiori app in S4 to manually update the rel... | 10. Object Complete |  | NA | 03.Medium |
| FTSE0593 | Enhancement | Enhancement of standard iDoc to capture and transfer Build Instructions from ... | 10. Object Complete |  | NA | 02.High |
| FTSE0424 | Enhancement | Conversion of Production Versions data into S4 | 10. Object Complete | S4 HANA → S4 HANA | NA | 03.Medium |
| FTSE0198 | Enhancement | Conversion Program for Routings | 10. Object Complete | NA → S4 HANA | NA | 03.Medium |
| FTSC1682 | Conversion | Conversion of Intel Products Bailed Inventory & Lot Attributes | 10. Object Complete |  | NA | 03.Medium |
| FTSC1559 | Conversion | Conversion of Open PO/Engineering/Rework Orders into Production orders from I... | 10. Object Complete |  | NA | 03.Medium |
| FTSC0434 | Conversion | Conversion of Open Production Orders from ECC purchase order data into S4 | 10. Object Complete | ECC → S4 HANA | NA | 03.Medium |
| FTSC0052_IP | Conversion | Conversion of Reference Operation Sets to S/4 | 10. Object Complete | ECC → S4 | NA | 03.Medium |
| FTSE1739 | Enhancement | Develop Utility for mass change of Production Orders in SAP S4 system | 01. Pending Approval |  | NA | 03.Medium |

**Summary**: 2 Reports, 34 Interfaces, 20 Conversions, 35 Enhancements, 7 Forms, 3 Workflows

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for M-080:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for M-080:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (101 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 91 | 90.1% |
| 08. FUT In Progress | 6 | 5.9% |
| 06. Dev In Progress | 2 | 2.0% |
| 09. FUT Overdue | 1 | 1.0% |
| 01. Pending Approval | 1 | 1.0% |
| **Total** | **101** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 2 |
| Interface (I) | 34 |
| Conversion (C) | 20 |
| Enhancement (E) | 35 |
| Form (F) | 7 |
| Workflow (W) | 3 |
| **Total** | **101** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 1 |
| 02.High | 25 |
| 03.Medium | 60 |
| 04.Low | 2 |
| N/A | 13 |

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
| FTSI1693 | 02.Interface | Interface for Reporting Scrap of Semi Finished Goods at OSAT and IF manufacturin... | 06. Dev In Progress | 03.Medium |
| LOGI1584 | 02.Interface | Interface to post inventory in SAP S/4HANA from ECA via MuleSoft. | 06. Dev In Progress | 03.Medium |
| FTSE1739 | 04.Enhancement | Develop Utility for mass change of Production Orders in SAP S4 system | 01. Pending Approval | 03.Medium |

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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>M-080 — Perform Materials Requirement Planning (IP)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*100 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| LOGW1078_IP | ISM Workflows - Capital/AMT | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGW1077_IP | ISM Workflows - EIMS/Lab | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| LOGW1076_IP | ISM Workflows - Non-inventory | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGR1176_IP | ISM - International Traffic Report | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGR0833_IP | Email Notification for deletion of Shipping Memos | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGM024_IP | Create/Upload Vehicle resource | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM023_IP | Update Business Share | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM022_IP | Upload Transportation Allocation | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM021_IP | Upload Schedules | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM019_IP | Default Routes | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM018_IP | Upload Rate Table | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM016_IP | Create and review Charge Calculation Sheet | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM015_IP | Create and review Freight Agreement | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM012_IP | Creation of Location based on BP, Shipping points, plants | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM008_IP | Location creation-ocean ports, airports | May-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM005_IP | UPLOAD TRANSPORTATION ZONES (TM) | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
| LOGM004_IP | UPLOAD TRANSPORTATION LANES | Jun-25 (100%) | — | — | Sep-25 (100%) |  |
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

*... and 70 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

**Mapped sub-tower(s):** 8.1 FTS IP - ALL, 8.4 FTS IP - Logistics & Inventory Management, 8.5 FTS IP - Manufacturing, 8.6 FTS IP - MRP & Planning Integration, 8.7 FTS IP - TM

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
*M-080 — Architecture Document (TOGAF BDAT) · Forecast to Stock (IP) · Generated: March 2026*

