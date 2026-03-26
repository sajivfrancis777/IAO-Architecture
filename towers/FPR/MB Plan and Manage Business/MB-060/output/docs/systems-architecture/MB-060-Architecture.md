<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">MB-060 — MB-060</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Finance Plan To Report (FPR) Tower<br/>
  Capability MB-060 · </p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **MB-060 MB-060** within the IAO program. It includes 13 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Finance Plan To Report (FPR) |
| **Process Group** |  |
| **Capability** | MB-060 - MB-060 |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 17 Reports, 86 Interfaces, 25 Conversions, 219 Enhancements, 1 Forms, 18 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Finance Plan To Report |
| **L1 Process** |  |
| **L2 Capability** | MB-060 - MB-060 |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | S/4 HANA Finance Consolidation | Migrate legacy costing and reporting platforms to unified S/4 HANA finance backbone | IDM 2.0 Core Finance Transformation | High |
| 2 | Real-Time Financial Visibility | Enable real-time cost reporting and variance analysis replacing batch-driven legacy processes | CFO Digital Finance Initiative | High |
| 3 | Regulatory Compliance Readiness | Ensure SOX compliance and audit trail continuity through the ERP transition period | Intel Corporate Compliance | Medium |
| 4 | MB-060 Process Migration | Migrate MB-060 business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Finance | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Month-End Close Cycle Time | < 3 business days | Calendar days from period close trigger to final posting | 5 business days (legacy) | Finance Controller |
| Cost Variance Accuracy | < 0.5% deviation | Variance between standard and actual cost post-migration | 1.2% (ICOST baseline) | Cost Accounting Lead |
| System Availability (Finance) | 99.9% uptime | S/4 HANA finance module availability during business hours | 99.5% (legacy) | IT Operations |
| MB-060 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **13 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for MB-060 MB-060.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | MB-060-010_Load_Sales_Plan_into_Profitability_Analysis | MB-060-010_Load_Sales_Plan_into_Profitability_Analysis | Corporate Planner, IT Admin | 5 | 2 |
| 2 | MB-060-020_Transfer_Sales_Plan_from_Profitability_Analysis_to_Sales_and_Operating_Plan | MB-060-020_Transfer_Sales_Plan_from_Profitability_Analysis_to_Sales_and_Operating_Plan | Corp. FP&A Analyst | 5 | 0 |
| 3 | MB-060-060_Analyze_Alternatives_and_Determine_Changes | MB-060-060_Analyze_Alternatives_and_Determine_Changes | Cost Accountant | 5 | 0 |
| 4 | MB-060-090_Transfer_Planned_Activity_Requirements_for_Production | MB-060-090_Transfer_Planned_Activity_Requirements_for_Production | Cost Accountant | 5 | 2 |
| 5 | MB-060-100_Prepare_Planning_Structure | MB-060-100_Prepare_Planning_Structure | Corp. FP&A Analyst, IT Admin | 9 | 2 |
| 6 | MB-060-110_Process_Material_Changes | MB-060-110_Process_Material_Changes | IT Administrator | 7 | 4 |
| 7 | MB-060-120_Process_Organizational_and_Financial_Elements | MB-060-120_Process_Organizational_and_Financial_Elements | Corp. Planner, Receiver, Sender | 12 | 7 |
| 8 | MB-060-130_Plan_Types_of_Work_and_Develop_Rates | MB-060-130_Plan_Types_of_Work_and_Develop_Rates | Cost Accountant | 4 | 0 |
| 9 | MB-060-140_Process_Distributions_and_Assessments | MB-060-140_Process_Distributions_and_Assessments | Cost Accountant | 5 | 2 |
| 10 | MB-060-170_Reconciliation_and_Alignment_of_Functional_and_Product_Plans | MB-060-170_Reconciliation_and_Alignment_of_Functional_and_Product_Plans | Corp. FP&A Analyst | 9 | 4 |
| 11 | MB-060-180_Transfer_Detailed_Financial_Plans_to_Profitability_Analysis | MB-060-180_Transfer_Detailed_Financial_Plans_to_Profitability_Analysis | Corp. Allocations Lead, Corp. FP&A Analyst | 7 | 7 |
| 12 | MB-060-190_Review_Final_Profitability_Analysis_Reports | MB-060-190_Review_Final_Profitability_Analysis_Reports | Corp. FP&A Analyst | 11 | 5 |
| 13 | MB-060-200_Perform_CAPEX_Planning | MB-060-200_Perform_CAPEX_Planning | Corp. FP&A Analyst | 13 | 6 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 MB-060-010_Load_Sales_Plan_into_Profitability_Analysis — MB-060-010_Load_Sales_Plan_into_Profitability_Analysis

**Swim Lanes**: Corporate Planner · IT Admin | **Tasks**: 5 | **Gateways**: 2

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
    subgraph Corporate Planner
        n4["fa:fa-user Enter the adjustments"]
    end
    subgraph IT Admin
        n1["fa:fa-user Load Blue Yonder (Demand, Plan and Response) Data"]
        n2["fa:fa-user Import the Revenue Volume Forecast Data"]
        n3["fa:fa-user Load Customer and Product Master Data from IF ECA"]
        n5[["fa:fa-cog Load the Revenue Volume Forecast Data"]]
        n6(["fa:fa-play Sales Plan Loading Initiated"])
        n7(["fa:fa-stop Sales Plan Loaded into Profitability Analysis"])
        n8{{"fa:fa-arrows-alt parallelGateway"}}
        n9{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n8
    n1 --> n4
    n2 --> n5
    n4 --> n9
    n5 --> n7
    n9 --> n2
    n3 --> n9
    n8 --> n3
    n8 --> n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n6 startEvt
    class n7 endEvt
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVe-P2jgQ_VesrFa0UpDyk0A-nASBnFZqparstarKfTCJA7517Mh2lqWI__3GJATCsdKdjg8R72XmvZmJMzlYmciJFVuPjwfKqY7RYaC3pCSDGA3WWJGBjRriG5YUrxlRAxNTCK6X9NcpzA2qNxNmuBSXlO0NuyQbQdAfTzaaQiKzkcJcDRWRtBjYg0rSEst9IpiQJvqBjAunOLm1t2ZC5kReAhwncrMQUhnl5EL7URAFqclTJBM874kWYTEussHRFMfELttiqU_l14p8xm_faa63gAvMFIGYrS7ZJ7wmzPSoZW24rJav52FQZXw4DGxZ4YzyDfCBA5TE_OVChc7xiI6PjyvemaLn-Yoj-GUMKzUnBVIa6MWrRgVlLH4IkmkaOrbSUryQ-MFbRHPfszPTSQytO7YZ7nBH6Gar47VgeRs63JkeYq96s-Vb7Dm23MP1xovw_OKUjLyxN-6cZpGbuMnZqSiK_-UEc5XPWL20Xgs_9dJ55-WGozBx_ql3bnMeRFP3dk5EvtKMXImmaeovLqNajELXeV90lvojJ7kR3WBNdnh_EZwkQSeYhlHqRu8KNn63VdbrL1JkZ0F_EaZhJxjN3HTqvSsYTN1g3FYIOhuJqy1KhKyEhDLRF4Y5J7K5b348-LmyChwXeGjGjRZcwxXeUYTzv2qlS8K1Wll_Nhnw7G-kn57RNC8pv1J0-4qfBM7RjNUE_YA3CogPc1JintunYhD8Q1-JqgRX5COaY407t5Oa11d7KqETfSrwK3klHGS_CVaXZFU7DnZSIUmGlb4j5N8pK4EORQnIVAEzz-tMo8-QD5RRQIUUJXpK0SKZ9tXCn51cJjaN2r8t6lpn9KHTqRgcoiWGpdhMxmjCDkBPsEkpPLwcUj9epUaXVOiiuk0lOaJcC9NWQTVeU0b1Hk05ZnvYPTda48PhrIWlFDs1xEyjCkvMGGG_Nyd8ZR2PVzmT_5bTnR0-QsPhb-DZQreBQQu9BoYtDBo4aWHYwKiFkwZ6LfT7weMG-n14vRSM-3nN9GjvPu3fp4P7dHi9cHp3Rt3K7tFRu1175Pi8YXrs5MxatgUnuMQ0t-KDdfq6whc4JwWumbaOtoVrLZZ7nlnx6Stk1VUOmXOK4Q0uG_L4Nxj9dZ0=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.2 MB-060-020_Transfer_Sales_Plan_from_Profitability_Analysis_to_Sales_and_Operating_Plan — MB-060-020_Transfer_Sales_Plan_from_Profitability_Analysis_to_Sales_and_Operating_Plan

**Swim Lanes**: Corp. FP&A Analyst | **Tasks**: 5 | **Gateways**: 0

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
    subgraph Corp. FP&A Analyst
        n1["fa:fa-user Perform Manual Input at Product Hierarchy Level"]
        n2["fa:fa-user Facilitate Ability to View the Inventory Impacts POR Data in the..."]
        n3["fa:fa-user Facilitate Ability to View Data at Super Group, Group, Division, Profit..."]
        n4["fa:fa-user Execute Forecasting Cycle"]
        n5[["fa:fa-cog Feed from Inventory Reserve into Cost and Profitability Model"]]
        n6(["fa:fa-play Transfer Sales Plan from Profitability Analysis to Sales and Operating Plan..."])
        n7(["fa:fa-stop Transfer Sales Plan from Profitability Analysis to Sales and Operating Plan..."])
    end
    n3 --> n1
    n2 --> n3
    n1 --> n4
    n5 --> n2
    n6 --> n5
    n4 --> n7
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n6 startEvt
    class n7 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNq1Vdtu4zYQ_RVCQeoWkANdLVcPBRzZagNssMY63T5s-kBLpE2EIgWSsq0N_O8dWvItmwAFiupB1hzNnDMzHo5enUKWxEmd29tXJphJ0evArElFBikaLLEmAxd1wFesGF5yogfWh0phFuz7wc2P6p11s1iOK8Zbiy7IShL054OLJhDIXaSx0ENNFKMDd1ArVmHVZpJLZb1vyJh69KDWv7qXqiTq7OB5iV_EEMqZIGc4TKIkym2cJoUU5RUpjemYFoO9TY7LbbHGyhzSbzR5xLu_WGnWYFPMNQGftan4J7wk3NZoVGOxolGbYzOYtjoCGraoccHECvDIA0hh8XKGYm-_R_vb22dxEkVP02eB4Co41npKKNIG4NnGIMo4T2-ibJLHnquNki8kvQlmyTQM3MJWkkLpnmubO9wStlqbdCl52bsOt7aGNKh3rtqlgeeqFu5vtIgoz0rZKBgH45PSfeJnfnZUopT-JyXoq3rC-qXXmoV5kE9PWn48ijPvR75jmdMomfhv-0TUhhXkgjTP83B2btVsFPvex6T3eTjysjekK2zIFrdnwl-z6ESYx0nuJx8Sdnpvs2yWcyWLI2E4i_P4RJjc-_kk-JAwmvjRuM8QeFYK12uUSVXfoXz-0wRNBOatNp2DvYT_7dmhOKV4aPuN5kRRqSr0iEWDOXoQdWMQNggyKpvCoD8YUVgV6xZ9IhvCn52_L7iCa64chpgzA_1Bk6V9apGR6CsjWwRbALg3RBipWvRQwbwbjeafv6ApNhgxYT3u7u6u-cN_zX9ggbQXTQ2OvyvZ1O7xZ8o2TDMpXFsUZeYHmehaZrYjRQMauVSkwNrAwURZW3ByHRV_O4UVcoVyQkpElawu6vxC7AQSKA_yzKSGzoqyzwL3FTzCRrBtvaQe_XyirjmM2hPsCE0htQWGHYrmHItO6pqq-7OZtl3pPK3cZ-gIPhRh47rif7kQS85i2sj6fxODRdI9iBANh7_BJPZm0Jlhb_qdGfVm3JlBb446M-7NqDOTiyNlGY6r5AoO3ofD9-HofTi-XCpXb0antXwFJ_0GdVynIqrCrHTSV-fwVYQvZ0kobrhx9q6DGyMXrSic9PD1cJq6hEmfMgyHuurA_T8vQGY8" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 MB-060-060_Analyze_Alternatives_and_Determine_Changes — MB-060-060_Analyze_Alternatives_and_Determine_Changes

**Swim Lanes**: Cost Accountant | **Tasks**: 5 | **Gateways**: 0

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
    subgraph Cost Accountant
        n1["fa:fa-user Calculate Activity Rates for WIF Scenario"]
        n2["fa:fa-user Calculate Cost for WIF Scenario"]
        n3[["fa:fa-cog Update KP26 with Planned Quantity for WIF Version from ECA"]]
        n4[["fa:fa-cog Update SKFs from Boundary apps"]]
        n5[["fa:fa-cog Update Plan Cost for WIF Version from SAC"]]
        n6(["fa:fa-play Alternatives and Determine Changes Analysis Initiated"])
        n7(["fa:fa-stop Alternatives and Determine Changes Analysis Completed"])
    end
    n5 --> n4
    n1 --> n2
    n4 --> n1
    n3 --> n5
    n6 --> n3
    n2 --> n7
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 startEvt
    class n7 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlldtu2zgQhl-FUBC4C8iAjpariwKybAFBu0C2bpuLZC9oibSJUKRAUnHcwO--Q0s-Ni6wqC4Mz8-Zbw7QUG9OKSvipM7t7RsTzKTobWBWpCaDFA0WWJOBizrhB1YMLzjRA-tDpTBz9nPn5kfNq3WzWoFrxjdWnZOlJOj7nYsyCOQu0ljooSaK0YE7aBSrsdrkkktlvW_ImHp0l60_mkhVEXV08LzEL2MI5UyQoxwmURIVNk6TUorqDEpjOqblYGuL43JdrrAyu_JbTf7Grw-sMiuwKeaagM_K1PwLXhBuezSqtVrZqpf9MJi2eQQMbN7gkokl6JEHksLi-SjF3naLtre3T-KQFH2bPgkET8mx1lNCkTYgz14Moozz9CbKsyL2XG2UfCbpTTBLpmHglraTFFr3XDvc4Zqw5cqkC8mr3nW4tj2kQfPqqtc08Fy1gd-LXERUx0z5KBgH40OmSeLnfr7PRCn9o0wwV_UN6-c-1ywsgmJ6yOXHozj3fuXt25xGSeZfzomoF1aSE2hRFOHsOKrZKPa969BJEY68_AK6xIas8eYI_JhHB2ARJ4WfXAV2-S6rbBf3SpZ7YDiLi_gATCZ-kQVXgVHmR-O-QuAsFW5WKJfaoKwsZSsMFqY7tY_wH58cilOKh3bYKMe8bDn0A96GvTCzQV_B0ohKhR7uCjQviYDVlU_OvyeU4Bpll_j3seHjIbiUS_S9qWzg5_tghNbMrNA9x0KQCv3TQuW2oD3uB1GaSYGokjWa5RlgT7nRu9z550J3ERMYht1vhJtGX8TG78baSs47OithnuUXmNGHA6bh8IJk3BAlMAwWJopFhaYEhBpuIJSvsFiCmgnMN3A1oDu4PhlkrYD51wkzOTK1kc3_Yuaybjg5Y8Iyd39EjIbDTzC23vQ7M-jNqDP7fRJhZ8a9OerMsDeDzkxOXmsL3K_zmRy8L4enq3p2El09ia-ejA4X5Jmc9HeZ4zo1zAyzyknfnN33Cb5hFaG45cbZug5ujZxvROmku3vcaXcvxJRhWK-6E7f_AdHdPKQ=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.4 MB-060-090_Transfer_Planned_Activity_Requirements_for_Production — MB-060-090_Transfer_Planned_Activity_Requirements_for_Production

**Swim Lanes**: Cost Accountant | **Tasks**: 5 | **Gateways**: 2

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
    subgraph Cost Accountant
        n1[["fa:fa-cog Receive Planned Production Data from BY"]]
        n2[["fa:fa-cog Receive Routing Information from S4"]]
        n3[["fa:fa-cog Receive Open Production Order Data from S4"]]
        n4[["fa:fa-cog Calculate Monthly Plan of Activity Quantity"]]
        n5[["fa:fa-cog Update KP26 with Activity Quantity Calculated"]]
        n6(["fa:fa-play Planned Activity Requirements for Production Transfer Initiated"])
        n7(["fa:fa-stop Planned Activity Requirements for Production Transfer Completed"])
        n8{{"fa:fa-arrows-alt parallelGateway"}}
        n9{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n8
    n8 --> n1
    n8 --> n2
    n8 --> n3
    n1 --> n9
    n2 --> n9
    n3 --> n9
    n9 --> n4
    n4 --> n5
    n5 --> n7
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 startEvt
    class n7 endEvt
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqllVuP4jYUx7-KldGIVgpSrgTyUAkCqUbtaqfDbKtq2Qfj2GCNsVPbgaGI717nQkiY5aFtHlD-59i_c8E-OVlIZNiKrcfHE-VUx-A00Fu8w4MYDNZQ4YENasPvUFK4ZlgNyjVEcL2kf1fL3CB_L5eVthTuKDuW1iXeCAy-PNlgajYyGyjI1VBhScnAHuSS7qA8JoIJWa5-wGPikCpa45oJmWF5XeA4kYtCs5VRjq9mPwqiIC33KYwEz3pQEpIxQYNzmRwTB7SFUlfpFwp_gu9_0ExvjSaQKWzWbPWO_QrXmJU1almUNlTI_aUZVJVxuGnYMoeI8o2xB44xScjfrqbQOZ_B-fFxxdug4HW-4sA8iEGl5pgApY15sdeAUMbihyCZpqFjKy3FG44fvEU09z0blZXEpnTHLps7PGC62ep4LVjWLB0eyhpiL3-35XvsObY8mt-bWJhn10jJyBt74zbSLHITN7lEIoT8r0imr_IVqrcm1sJPvXTexnLDUZg4H3mXMudBNHVv-4TlniLcgaZp6i-urVqMQte5D52l_shJbqAbqPEBHq_ASRK0wDSMUje6C6zj3WZZrJ-lQBegvwjTsAVGMzedeneBwdQNxk2GhrORMN-CRCgNpgiJgmvIde0tH-5-_bqyCIwJHCKxAS8YYbrH4JlBznEGTBpZgTQVHMyhhoBIsQOzP1fWt28diPd9yIsotDnD4IkTIXewolSAZXAD8L8P-Jxj3k3hc3mHO4l84AR9TgIZKpj5d8Ancwq37FjVBQQxvdB0T_UR_FaYfpiXG1DYB33Js5Lyy7M3Ageqtx_3X2NlN6jRDy0qZ_DYtrZFvOC_CirNTORaAdOpbsWvZhYoYop-MtOUNvQfO_ToSlda5P-RnohdzvBH-vh0utChlOKghpBpkEMJGcPs5_rcr6zzubNn8u_2mGlSv_ARGA5_MjEbOa6l25deX_qNdGs5aaTXl35fTmoZNDKoZdjIsJZR506W_M7k6Hm8ux7_rie46wnvekbtjO-Zo2Yc94zjy0jqWScXq2VbO2wuJM2s-GRVn2Pzyc4wgQXT1tm2YKHF8siRFVefLauojv-cQjNNdrXx_A_Bx4rS" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 MB-060-100_Prepare_Planning_Structure — MB-060-100_Prepare_Planning_Structure

**Swim Lanes**: Corp. FP&A Analyst · IT Admin | **Tasks**: 9 | **Gateways**: 2

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
    subgraph Corp. FP&A Analyst
        n8["fa:fa-user Enter Latest FX Rates"]
        n9["fa:fa-user Update FX Conversions Based on Latest Currency Rates Available"]
        n11["Determine Operational and Non-core Operational Requirements"]
        n13{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph IT Admin
        n1["fa:fa-user Set up SAC Model With Agreed Upon Dimensions"]
        n2["fa:fa-user Populate Dimensions with Correct Dimension Members and Associated Hierarchy"]
        n3["fa:fa-user Designate Dimensions as Public or Private"]
        n4["fa:fa-user Determine Dimensions that Would Need to be Secured"]
        n5["fa:fa-user Load Latest Master Data Dimensions from MDG"]
        n6["fa:fa-user Load Actuals and Transaction Data"]
        n7["fa:fa-user Create and Embed any Required Data Actions"]
        n10(["fa:fa-play Request to Prepare Planning Structure Initiated"])
        n12{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n10 --> n12
    n12 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
    n6 --> n7
    n12 --> n8
    n8 --> n9
    n7 --> n13
    n9 --> n13
    n13 --> n11
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 userTask
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVu1v-jYQ_lesVB2bBFNeCeXDpDSQ3yq1GyrtOmndB5M4YNXYme1AGeJ_3zkvQBj9svEh4h7fPXf32Dlnb6UiI9bYur3dU071GO17ekXWpDdGvQVWpNdHNfAblhQvGFE945MLruf078rN8YtP42awBK8p2xl0TpaCoNeHPoogkPWRwlwNFJE07_V7haRrLHexYEIa7xsyyu28ytYs3QuZEXlysO3QSQMIZZSTE-yFfugnJk6RVPCsQ5oH-ShPewdTHBPbdIWlrsovFXnCn2800yuwc8wUAZ-VXrNHvCDM9KhlabC0lJtWDKpMHg6CzQucUr4E3LcBkph_nKDAPhzQ4fb2nR-Tosfnd47glzKs1ITkSGmApxuNcsrY-MaPoySw-0pL8UHGN-40nHhuPzWdjKF1u2_EHWwJXa70eCFY1rgOtqaHsVt89uXn2LX7cgfPi1yEZ6dM8dAduaNjpvvQiZ24zZTn-f_KBLrKF6w-mlxTL3GTyTGXEwyD2P43X9vmxA8j51InIjc0JWekSZJ405NU02Hg2F-T3ife0I4vSJdYky3enQjvYv9ImARh4oRfEtb5LqssFzMp0pbQmwZJcCQM750kcr8k9CPHHzUVAs9S4mKFYiGLH1Ey-y5CEcdsp3TtYH589Me7leNxjgdGbzTlGp6P0JPSKPkdPZt_79afZxF33YjXIgMf4xsLviFSUcEVuofXPUOCt1RxKSXh6a4mRNEGU2YmQJfacYB7QqCENbyY6NeCSKyBDzOEeYZ-EXyQCtldeCZ_lVTCUOH6olDH2-_bUrGUYqsGmGlUYIkZI-xbvXHv1uFQB8HRvlDu4QVFGZRyTtrtfk40Kgs0j2L0BO8yQ29Ur1C0lATafy1AgAmF0ipRutW5XaKZKEpmhDz5o63hgt2TJNUnHD2R9QJ0riSJlBIphbgM_UxBFJmudt08XjfPhCi65BeJsEKzcsFoigRUIukG1rss_iVLu0dnLHqFNXoTJYOdMu1rgRYEFIKxR7IuXdClexQ4a0_KE1bmCE6wxufkuRRr9DT51uUZXuGJUl3CEK7keYFpqnBqjkrF2I0Ou9GxJEYXEzcFhTP4t2uPV1YXFFVUl-fM_v5IVDBcx5hWQICZJHDeCJoxzDmMdDSHuwAKBOgBrshq54Dth3M69z8eWygEDQY_GYYWcBugtWuzXW5Wvcb0atNvTL82g8YManPYmMPaDC8yjRp7VJt3jRk2dbSp7i5sp8ntnI9sU297CXRg9zrsXYf963BwHR5eh8Pr8Og6fHcdhv1pr-ou7nyBu-3t0oW9Frb61hreQ0wza7y3qk8r-PzKSI5Lpq1D38KlFvMdT61x9QlildWwnlAM821dg4d_AHckGLc=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 MB-060-110_Process_Material_Changes — MB-060-110_Process_Material_Changes

**Swim Lanes**: IT Administrator | **Tasks**: 7 | **Gateways**: 4

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
    subgraph IT Administrator
        n1["fa:fa-user Capture Source Master Data from MDG"]
        n2["fa:fa-user Capture Source Master Data from CFIN"]
        n3["fa:fa-user Capture Source Master Data from SAP and Non-SAP"]
        n4["fa:fa-user Capture Source Transactional Data from S/4HANA"]
        n5["fa:fa-user Set up SAC Model Dimensionality and Attributes from S/4 Master Data"]
        n6[["fa:fa-cog Seed SAC P and L Model with Transactional Data"]]
        n7[["fa:fa-cog Seed SAC base Models with Transactional Data"]]
        n8(["fa:fa-play Process Material Changes Initiated"])
        n9(["fa:fa-stop Process Material Changes Completed"])
        n10{{"fa:fa-arrows-alt parallelGateway"}}
        n11{{"fa:fa-arrows-alt parallelGateway"}}
        n12{{"fa:fa-arrows-alt parallelGateway"}}
        n13{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n8 --> n10
    n1 --> n2
    n10 --> n1
    n10 --> n3
    n10 --> n4
    n2 --> n11
    n11 --> n5
    n3 --> n11
    n12 --> n6
    n12 --> n7
    n5 --> n13
    n6 --> n13
    n7 --> n13
    n4 --> n12
    n13 --> n9
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 startEvt
    class n9 endEvt
    class n10 gateway
    class n11 gateway
    class n12 gateway
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlll1vozgUhv-KRVVlViJaPkPKxUiUhNlK02qkdHcuJnPhgEmsGhvZpmk2yn9fO3wkMMloOstFlPP6nOf1seDA3khZhozQuL3dY4plCPYjuUEFGoVgtIICjUxQC_9AjuGKIDHSOTmjcoH_PabZXvmm07SWwAKTnVYXaM0Q-PvBBJEqJCYQkIqxQBznI3NUclxAvosZYVxn36BpbuVHt2bpnvEM8VOCZQV26qtSgik6yW7gBV6i6wRKGc160NzPp3k6OujNEbZNN5DL4_YrgR7h21ecyY2Kc0gEUjkbWZDPcIWI7lHySmtpxV_bw8BC-1B1YIsSppiule5ZSuKQvpwk3zocwOH2dkk7U_A8W1KgrpRAIWYoB0Iqef4qQY4JCW-8OEp8yxSSsxcU3jjzYOY6Zqo7CVXrlqkPd7xFeL2R4YqRrEkdb3UPoVO-mfwtdCyT79TvwAvR7OQUT5ypM-2c7gM7tuPWKc_z_-WkzpU_Q_HSeM3dxElmnZftT_zY-pHXtjnzgsgenhPirzhFZ9AkSdz56ajmE9-2rkPvE3dixQPoGkq0hbsT8C72OmDiB4kdXAXWfsNdVqsvnKUt0J37id8Bg3s7iZyrQC-yvWmzQ8VZc1huwMMziLJCPZGqCkrG62V9Ufvb0shhmMOxPm0Qw1JWHIEFq3iKwCMUUqkzKCHIOSvA4-zT0vh-Vu-8rz5OHp76APd9gEX0BUCagSdGx-p_n-X9lPWsHiwBU4kZheQc-af3V_QU9VF-H7VAElSlco_Bo3piVTkuEBVHFJa745YiKTleVRKJjnu-_z5_8q0zSNla8VF2pNfdfW5ctlhuLuxboc5ZwRWWnrg1SPwiafqhI5VE3dL6NkRCqDZUF2rugngD6Vo1-KCmO1ZipgB_nAHuTgAhWXkdELOiJOhHgG3t9y0Bcs62YgyJBCXkkBBEPtXP2tI4HM6L7N8pcn6nyH1fkRqW9R86BePxR91fE9t17LSh1awPYncQe03sNOldfsPzm9gdrjcFk0EcNLHf5Ld-k0EcDGKvibv9N4Z3Z7NMN9nO8J7sXJbdy7J3WfYvy5PzId9bCa6uTLsXaE--a951_ZasduD3Zfuy7FyW3VY2TKNAvIA4M8K9cfw2Ut9PGcphRaRxMA1YSbbY0dQIj98QRlVmqnKGoRrtRS0e_gPb3fti" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 MB-060-120_Process_Organizational_and_Financial_Elements — MB-060-120_Process_Organizational_and_Financial_Elements

**Swim Lanes**: Corp. Planner · Receiver · Sender | **Tasks**: 12 | **Gateways**: 7

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
    subgraph Corp. Planner
        n1["fa:fa-user Transfer Kickoff"]
        n2["fa:fa-user Assign Re-Organization ID"]
        n3["fa:fa-user Review and Process Transfer"]
        n11["Discuss Scope, Timing and Owner of Re-Organization"]
        n12["Announce Re-Organization"]
        n13(["fa:fa-play Process Organizational and Financial Elements Initiated"])
        n14(["fa:fa-stop Reorganized Data Package Sent to P and L model"])
        n16{{"fa:fa-code-branch Discrepancies Found?"}}
    end
    subgraph Receiver
        n9["fa:fa-user Review Side by Side Comparison of Pre and Post reorganization PnL Approve..."]
        n10["fa:fa-user Communicate with Sender"]
        n20{{"fa:fa-code-branch Edits Required to the Transfer?"}}
        n21{{"fa:fa-code-branch Discrepancies Found?"}}
        n22{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Sender
        n4["fa:fa-user Assign Contributor"]
        n5["fa:fa-user Begin Transfer Preparation"]
        n6["fa:fa-user Calculate GM, OM, etc. and Target Transfer Amount"]
        n7["fa:fa-user Review Side by Side Comparison of Pre and Post reorganization PnL Approve..."]
        n8["fa:fa-user Communicate with Receiver"]
        n15["Relevant Transfer Data Entered by Contributor via Input Form"]
        n17{{"fa:fa-code-branch Discrepancies Found?"}}
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n13 --> n11
    n11 --> n12
    n12 --> n1
    n1 --> n2
    n2 --> n4
    n4 --> n5
    n5 --> n18
    n15 --> n6
    n6 --> n7
    n7 --> n17
    n17 -->|"No"| n19
    n8 --> n9
    n9 --> n21
    n18 --> n15
    n10 --> n20
    n21 -->|"No"| n22
    n3 --> n16
    n16 -->|"No"| n14
    n20 -->|"Yes"| n18
    n20 -->|"No"| n3
    n17 -->|"Yes"| n18
    n19 --> n8
    n22 --> n10
    n16 -->|"Yes"| n22
    n21 -->|"Yes"| n19
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
    class n13 startEvt
    class n14 endEvt
    class n15 startEvt
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNq9V22P4jYQ_itWVitaCVZJSAjwoRUL5HTqXhct21ZV6QeTOGBt4qS2A8tx_PeOSRxILttTt1KR9sWPZ56ZeTwekqMRpCExxsbt7ZEyKsfo2JFbkpDOGHXWWJBOFxXAr5hTvI6J6CibKGVyST-fzSwne1VmCvNxQuODQpdkkxL0y8cumoBj3EUCM9EThNOo0-1knCaYH6ZpnHJlfUOGkRmdo5Vb9ykPCb8YmKZnBS64xpSRC9z3HM_xlZ8gQcrCGmnkRsMo6JxUcnG6D7aYy3P6uSCf8OtvNJRbWEc4FgRstjKJH_CaxKpGyXOFBTnfaTGoUHEYCLbMcEDZBnDHBIhj9nKBXPN0Qqfb2xWrgqKHpxVD8AliLMSMREhIgOc7iSIax-MbZzrxXbMrJE9fyPjGnnuzvt0NVCVjKN3sKnF7e0I3Wzlep3FYmvb2qoaxnb12-evYNrv8AL8bsQgLL5GmA3toD6tI9541taY6UhRF_ykS6MqfsXgpY837vu3PqliWO3Cn5td8usyZ402spk6E72hArkh93-_PL1LNB65lvk167_cH5rRBusGS7PHhQjiaOhWh73q-5b1JWMRrZpmvFzwNNGF_7vpuRejdW_7EfpPQmVjOsMwQeDYcZ1s0TXl2hxYxZozwYk99mPXHyojwOMI9JTV6hs4TEfzzEw1e0ihaGX9eGdt144kQdMPQE-k98g1m9DOWNGXo46zu1a97PZEdJXuEWYhUiUSIKmrdz1K5zagIcjBZBmkG1-eZJnAnzs6Pe6gEpVEzfoNE5TxhLM1ZQL5h2v-uyjSL4TR1etcuOD4H9ynDLIAxhOYxzDImBfoI045CH4TA-v01rXOhFTLNIIm0ICQhmmGJ0QIHL3hD0BJ4kEzR4hziASUwGOIm2-B41Gxq0vbWoF2wRUonTjKVFBHIh3LDH1fG6VS4woVt9MMTCQjd1Vph1HpOSxoStD4Uf6dpksHYFnDKIPyCk-IYUyER11UVTbBgD2iSZTzdkbu7u4bQZj0SsCY5owGIh_ZUbpUQYbMbbLO98HlIQfwn8ldOOQgK8sG3S9VRVxoULNZ75Ctc7XZX8hrEuQAtPxRD4J9ULwu7kDqtN2oKE5PTdS7Thghu3fyebCi73NmFqoC3dPagoTeOgzxWan_41EWP8ENkcHc-ymfMN0ReKCcJSCHrbN7_1SfDb7RJ1cP17lIiPZGY7DC7quR80-ZMEtUlkOeVxmhHMVzfLJdw8jxp0Hnv7hhr-G87pnAbvbvRYIahXu8HNTs1YJWArQG7BPS6WOrtctcpl06xdMulW_oOtXMJDMr1oFh65dIrzfXaOgNfVsbP6cr4oiotN4aFoV6OypyqHMt9S-dhmaWFqdO26sy2rkfroTO0Bo0UdKW2WW78TkSxM2zulC79ZjVfeVhlARWD1txsZqFdq3yrQirS0dWjgTou_UhUg-12uN8OO-2w2w4P2mGvHR62w6N2GA6yHe9XD7R13CkfPuuo-4b1QD-Z1WGvHR62w6NWGLqiFbbaYVvDRtdICE8wDY3x0Ti_CcHbUkginMfSOHUNDCNpeWCBMT6_MRh5FoLnjGL4CkkK8PQ3aTY1Sg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 MB-060-130_Plan_Types_of_Work_and_Develop_Rates — MB-060-130_Plan_Types_of_Work_and_Develop_Rates

**Swim Lanes**: Cost Accountant | **Tasks**: 4 | **Gateways**: 0

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
    subgraph Cost Accountant
        n1["fa:fa-user Allocate Costs from Spending Cost Centers to Tech Level Cost centers"]
        n2["fa:fa-user Calculate Activity Rates"]
        n3[["fa:fa-cog Update KP26 with Activity Quantity Calculated"]]
        n4[["fa:fa-cog Update SKFs from Boundary Apps"]]
        n5(["fa:fa-play Rates Planning to be Developed"])
        n6(["fa:fa-stop Types of Work and Develop Rates Planning Completed"])
    end
    n5 --> n3
    n3 --> n4
    n4 --> n1
    n1 --> n2
    n2 --> n6
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 startEvt
    class n6 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVV1vmzAU_SsWVZVNIhKfIeNhEiFBmtpJ3dKuD-0eHGMnVo2NbJM0q_LfZwdCPtY-jQfEPb7nHN_rD94cJErspM719RvlVKfgbaBXuMKDFAwWUOGBC1rgF5QULhhWA5tDBNdz-mef5kf1q02zWAEryrYWneOlwODhmwsyQ2QuUJCrocKSkoE7qCWtoNzmgglps6_wmHhk79YNTYQssTwmeF7io9hQGeX4CIdJlESF5SmMBC_PRElMxgQNdnZyTGzQCkq9n36j8Hf4-khLvTIxgUxhk7PSFbuFC8xsjVo2FkONXB-aQZX14aZh8xoiypcGjzwDSchfjlDs7XZgd339zHtTcD995sA8iEGlppgApQ08W2tAKGPpVZRnRey5SkvxgtOrYJZMw8BFtpLUlO65trnDDabLlU4XgpVd6nBja0iD-tWVr2nguXJr3hdemJdHp3wUjINx7zRJ_NzPD06EkP9yMn2V91C9dF6zsAiKae_lx6M49_7VO5Q5jZLMv-wTlmuK8IloURTh7Niq2Sj2vY9FJ0U48vIL0SXUeAO3R8EvedQLFnFS-MmHgq3f5SybxZ0U6CAYzuIi7gWTiV9kwYeCUeZH426GRmcpYb0CuVAaZAiJhmvIdTtqH-4_PTsEpgQObbNBxphAppw9QwEiRQXmtVlxsxdblRxzjaUCWoB7jFbgFq8xa4dQO_Ts_D4xCM4NcshQw6xDhjRdU70FP010QQqfehYSS_BQl5ZxcxeMwIbq1ZH7ozHl2I9etzRKp1LRu1Lzm6KrbmJ6Yo85yOpaXXDjTz23ZrCbKbhjkHPbD9OCBQZT2wBR740_n5BHR7LSogb329qQBQGPQr4AyMsD81I2F1XNsD4VNAvQfvAYDIdfTYO6MGzDqAujNux2PffbMOjCoA1HJ7vN5hxO2RkcvA-HpyfobCT6cCTub6czeNRdJI7rVFhWkJZO-ubsfw7mB1JiAhumnZ3rwEaL-ZYjJ91fok6zX8IphWZvVy24-wtngRPB" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.9 MB-060-140_Process_Distributions_and_Assessments — MB-060-140_Process_Distributions_and_Assessments

**Swim Lanes**: Cost Accountant | **Tasks**: 5 | **Gateways**: 2

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
    subgraph Cost Accountant
        n1["fa:fa-user Perform Actual Posting in Primary Cost Center"]
        n2["fa:fa-user Allocate Costs from Spending Cost Centers to Tech Level Cost Centers"]
        n3["fa:fa-user Allocate Costs from Spending Cost Centers to Tech Level Cost Centers"]
        n4[["fa:fa-cog Update SKFs from Boundary apps"]]
        n5[["fa:fa-cog Receive Spending Forecast from SAC at Primary CC Level"]]
        n6(["fa:fa-play Distributions and Assessments Processing Initiated"])
        n7(["fa:fa-stop Distributions and Assessments Processing Completed"])
        n8{{"fa:fa-arrows-alt parallelGateway"}}
        n9{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n4
    n4 --> n8
    n8 --> n5
    n8 --> n1
    n5 --> n2
    n1 --> n3
    n2 --> n9
    n3 --> n9
    n9 --> n7
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 startEvt
    class n7 endEvt
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNq1VV2P4jYU_StWRiNaKUj5JJCHShBItepWGpXZ9mHpg3FuwBrHjmwHhiL-e20SPsLuSK2q5gFxju895_rGvjk6RBTgpM7z85FyqlN0HOgtVDBI0WCNFQxc1BK_Y0nxmoEa2JhScL2kf53D_Kh-t2GWy3FF2cGyS9gIQF8-uWhqEpmLFOZqqEDScuAOakkrLA-ZYELa6CcYl155duuWZkIWIG8Bnpf4JDapjHK40WESJVFu8xQQwYueaBmX45IMTrY4JvZki6U-l98o-BW__0ELvTW4xEyBidnqin3Ga2B2j1o2liON3F2aQZX14aZhyxoTyjeGjzxDSczfblTsnU7o9Py84ldT9DpfcWQewrBScyiR0oZe7DQqKWPpU5RN89hzlZbiDdKnYJHMw8Aldiep2brn2uYO90A3W52uBSu60OHe7iEN6ndXvqeB58qD-X3wAl7cnLJRMA7GV6dZ4md-dnEqy_I_OZm-yles3jqvRZgH-fzq5cejOPO-1btscx4lU_-xTyB3lMCdaJ7n4eLWqsUo9r2PRWd5OPKyB9EN1rDHh5vgJIuugnmc5H7yoWDr91hls36RglwEw0Wcx1fBZObn0-BDwWjqR-OuQqOzkbjeokwojaaEiIZrzHW7ah_uf105JU5LPLTNRi8gSyErE6sbzNCLyTOnEFGOXtp71EplwDXIlfPnnVLQV5oyJohpzDlBoVKKCi1rc3as3p2IQlqgVyBb9Bl2wHpLfYPw_zaIvl4diNigL3Vh5Ze_5J36zLTPTgSE69qm3ufG_dzfgADdwa2gXEgg2Di3dU4zhPWtp1lb24Pm6IerZs3M-ZpT89LputFUcIUwL9BUKVCqMptRyJ4YA6zZJzN6qam9MII_3gkmN0GlRf3PBTNR1Qy-FRwfjxdBLKXYqyFmGtVYYsaA_dzei5VzOt3lTP5djulf-4eP0HD4k3lLHYxaOO7guIVxH3b3n8ctDDrotzDsYNDCSQfDPpy0MLm7pFbhMpx6dPB9Ovw-Hd3Po95K_OHK6Drre3TSjeUeOb6Mph47ubCO61QgK0wLJz0658-y-XQXUOKGaefkOrjRYnngxEnPny-nOd-IOcVmqlQtefobDF2PBA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.10 MB-060-170_Reconciliation_and_Alignment_of_Functional_and_Product_Plans — MB-060-170_Reconciliation_and_Alignment_of_Functional_and_Product_Plans

**Swim Lanes**: Corp. FP&A Analyst | **Tasks**: 9 | **Gateways**: 4

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
    subgraph Corp. FP&A Analyst
        n1["fa:fa-user Compare Current Forecasting Cycle with Previous Forecasting Cycle"]
        n2["fa:fa-user Compare Current Quarter Forecast Cycle with Quarter Actuals"]
        n3["fa:fa-user Compare Full Year Forecasting Cycle with Full Year Actuals"]
        n4["fa:fa-user Access Variance Explanation Form Directly in the system"]
        n5["fa:fa-user Submit Variance Explanations for Revenue"]
        n6["fa:fa-user Submit Variance Explanations for COS and OPEX Spending"]
        n7["fa:fa-user Submit Variance Explanations for Margin"]
        n8["fa:fa-user Report Variance Explanations to Corp. Planning"]
        n9["fa:fa-user Report P and L Variance Explanations to External Reporting Stakeholders"]
        n10(["fa:fa-play Reconciliation and Alignment of Functional and Product Plans Initiated"])
        n11(["fa:fa-stop Reconciliation and Alignment of Functional and Product Plans Completed"])
        n12{{"fa:fa-code-branch What Cycles need to be Compared?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch What is Variance Explanation for ?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n10 --> n12
    n12 -->|"Current Quarter Forecast and Actuals"| n2
    n1 --> n13
    n3 --> n13
    n2 --> n13
    n13 --> n4
    n4 --> n14
    n6 --> n15
    n5 --> n15
    n7 --> n15
    n15 --> n8
    n8 --> n9
    n9 --> n11
    n12 -->|"Full Year Forecast and Actuals"| n3
    n12 -->|"Current and Previous Forecast Cycles"| n1
    n14 -->|"Spend"| n6
    n14 -->|"Revenue"| n5
    n14 -->|"Margin"| n7
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 userTask
    class n10 startEvt
    class n11 endEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVm2P4jYQ_itWVltaKVR5JWw-tGIDqU6609Hj2mtV-sE4DljrOJHtsFCO_147JEBCOGl1fFjtPDPzPPZkPPbBQHmCjdB4fDwQRmQIDgO5wRkehGCwggIPTHAC_oScwBXFYqBj0pzJBfmvCrO9YqfDNBbDjNC9Rhd4nWPwxzsTTFQiNYGATAwF5iQdmIOCkwzyfZTTnOvoBzxOrbRSq13POU8wvwRYVmAjX6VSwvAFdgMv8GKdJzDKWdIiTf10nKLBUS-O5q9oA7msll8K_AHuvpBEbpSdQiqwitnIjL6HK0z1HiUvNYZKvm2KQYTWYapgiwIiwtYK9ywFccheLpBvHY_g-Pi4ZGdR8Hm6ZED9EIVCTHEKhFTwbCtBSigNH7xoEvuWKSTPX3D44MyCqeuYSO8kVFu3TF3c4Ssm640MVzlN6tDhq95D6BQ7k-9CxzL5Xv3taGGWXJSikTN2xmel58CO7KhRStP0u5RUXflnKF5qrZkbO_H0rGX7Iz-ybvmabU69YGJ364T5liB8RRrHsTu7lGo28m3rPulz7I6sqEO6hhK_wv2F8CnyzoSxH8R2cJfwpNddZbma8xw1hO7Mj_0zYfBsxxPnLqE3sb1xvULFs-aw2IAo58XPIJ7_MAETBuleyFOA_jH7n6WRwjCFQ11vFZsVkGMQlZxjJkGcc4ygkKobQbRHFINXIjdgzvGW5KW49S-Nf6_YnW-z_16qxlV4w3It0fgmSJbqTLV53X7euKQU_I0hv7fuS0AvrdemnSCEhQDVtGIIg9muoJBBSXKmBTIwJUpF0j0gDKjBBoSqLc7anH6bc1GuMiJ7OQVIcw4-4S1mZaeOozeSRB8XALIEfJzP_gKLQh1aVYg2ZfBGyg-Qrwlrc4zbHJ9wkfN7HDKvG3GuMHaznKdeqnm1i_f3KWc71SOqqesE_bkXEr7gjRo2mHc-r239eFZRNHuVpMY8IpScvqnWmlCyZpluzjxV7cKQ9ih-7VPHMimRrHYgwDt1xalEnCiRn65V7IuKkHnxfSq6tSnuUXEOh0ZFX7vDlbo40AZ82cD6GAnAME50kVa4OSHJr0vjeLymcftp8A7RUpAt_u003rpp3jfUyZ0jo7voRt9_q77q5dM_6nOC4fAXXYoGcDTwdWncnS9V7ZuT_1XNpyazZnJr2-3YTse26wCvtr3a39ij2vZr2-_YQce264BxbY9P5lNtPtXhdnejtwPvZovuveKceq0zx-vWqTLPal6dWQ2SyjXqus5TSzn9rrMZHcoXXF12uuzNJd-CnX7Y7Ye9ftjvh0f9cNAPj_vhp35YNWTzFGvjdv1saqNO83Zow24_7PXDfgMbppFhnkGSGOHBqJ7Z6ime4BSWVBpH04ClzBd7hoyweo4aZZGozCmB6pWQncDj_wpUyEY=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.11 MB-060-180_Transfer_Detailed_Financial_Plans_to_Profitability_Analysis — MB-060-180_Transfer_Detailed_Financial_Plans_to_Profitability_Analysis

**Swim Lanes**: Corp. Allocations Lead · Corp. FP&A Analyst | **Tasks**: 7 | **Gateways**: 7

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
    subgraph Corp. Allocations Lead
        n1["fa:fa-user Capture Spending (OCOS) at Partner Cost Center and Project"]
        n2["fa:fa-user Receive and Validate SSA Allocation Output from PaPM"]
        n3["fa:fa-user Run PBA Allocations in SAC Cost Center Model"]
        n8(["fa:fa-play Detailed Financial Plans to Profitability Analysis Transfer Initiated"])
        n11{{"fa:fa-code-branch Validation Successful?"}}
        n12{{"fa:fa-code-branch exclusiveGateway"}}
        n15{{"fa:fa-arrows-alt parallelGateway"}}
        n16{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Corp. FP&A Analyst
        n4["fa:fa-user Load Allocated Spending (OCOS) Data at Profit Center into Margin Model"]
        n5["fa:fa-user Pre-Populate Previous Quarter /Historical Actuals into the Margins Model"]
        n6["fa:fa-user Review Post-Allocated Forecasted Spending at Super Group Level"]
        n7["fa:fa-user Perform Cost of Sales and Profitability Reporting and Analysis and Scenario..."]
        n9(["fa:fa-play Previous Quarter /Historical Actuals need to be Populated"])
        n10(["fa:fa-stop Detailed Financial Plans to Profitability Analysis Transfer Completed"])
        n13{{"fa:fa-code-branch Review Successful?"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n8 --> n15
    n15 --> n1
    n15 --> n12
    n2 --> n11
    n1 --> n3
    n11 -->|"Yes"| n16
    n3 --> n16
    n9 --> n5
    n5 --> n17
    n17 --> n14
    n16 --> n17
    n4 --> n6
    n6 --> n13
    n13 -->|"Yes"| n7
    n7 --> n10
    n12 --> n2
    n11 -->|"No"| n12
    n14 --> n4
    n13 -->|"No"| n14
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 startEvt
    class n9 startEvt
    class n10 endEvt
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVm1v2zYQ_iuEiswtYGd6tRx_2ODIUVcgWbyo6zDM-0BLVMyFJgWSsuOl_u872pJtqcqwtf4Q5B7ePQ_veCfyxUpFRqyxdXHxQjnVY_TS00uyIr0x6i2wIr0-OgCfsKR4wYjqGZ9ccJ3Qv_dujl88GzeDxXhF2dagCXkUBP36oY8mEMj6SGGuBopImvf6vULSFZbbSDAhjfcbMsrtfK9WLV0LmRF5crDt0EkDCGWUkxPshX7oxyZOkVTwrEGaB_koT3s7szkmNukSS73ffqnIHX7-jWZ6CXaOmSLgs9QrdosXhJkctSwNlpZyXReDKqPDoWBJgVPKHwH3bYAk5k8nKLB3O7S7uJjzoyi6fZhzBL-UYaWmJEdKA3yz1iinjI3f-NEkDuy-0lI8kfEb9yacem4_NZmMIXW7b4o72BD6uNTjhWBZ5TrYmBzGbvHcl89j1-7LLfxtaRGenZSioTtyR0el69CJnKhWyvP8m5SgrvIjVk-V1o0Xu_H0qOUEwyCyv-Sr05z64cRp14nINU3JGWkcx97NqVQ3w8CxXye9jr2hHbVIH7EmG7w9EV5F_pEwDsLYCV8lPOi1d1kuZlKkNaF3E8TBkTC8duKJ-yqhP3H8UbVD4HmUuFiiSMjiEk0YEynWVHCFbgnODk7mx50_5laOxzkemJqjCBe6lAQlBRw2tCF6ex_dJ-8Q1mgGjcaNi1AaRYRr-B_zDMGG_yKpnlt_ntG6TdoHkhK6Jnv_T5jRDAqHkmRytjN0X-qihO6SYgVas7smodciLDmaXU8amVGOkknU2N8dzBhrEo3eHpkKBmc3JRpTRjIUU455Cp8YNGPwiUFamNRyqvGCMqq3aMIx28Lwoo8wpyoH-g_wpaOQSgYS786L6ry81CLmuzhYQES6rFM32SZlmhKl8pL9OLd2u_NgtzuYPKesVFDF94eua4cFpzAspdioAWYaFVhixgh7JWj4_4KgKTobLJ59N6nqo8_o_eah3Qqc1ScGBW_32BRrvG-0fdXrI6QcDuIOy0c43o7jDJoSM0kGM1GUzDQYGGsqSoV-KaF3YfX7n6jSQtIUDnmS6hK-1wd-uJkqDdUlMmx385qSDZpBow1O6cRCkhSrRmaQTVIWEPJeirKA2Vu3qcPW_onMhVwdmljkKMFwU9ZjdtaLD6QQUu8lYO3YmcZIUsLhjhWXl5dNqatW5_-n8nAC-UCFFlDOqq5fdLt9Iob44ptGKhKrgpEOEa97Kqqz-Jdx8r9unMKvnAw-QoPBD2YeK9sJKqBtuxXgVvbR4WB7tbm3P8-t34maW5_N0FYrXhVY21cHuxaudcKaKKwAvwaGLQ__YNd89fJxJ15rJ3VcTWzXjlVKbjuFn8Uhg-NCpei3FWpH_-yCNJWpHwYN2O2GvW7Y74aDbnjYDYfd8Oj4HmvAV92wY1dPqibq1O-KJux2w1437HfDQTc87IbDGrb61orIFaaZNX6x9u94eOtnJMcl09aub-FSi2TLU2u8f-9aZWGu-CnFcEusDuDuHyPU3mc=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.12 MB-060-190_Review_Final_Profitability_Analysis_Reports — MB-060-190_Review_Final_Profitability_Analysis_Reports

**Swim Lanes**: Corp. FP&A Analyst | **Tasks**: 11 | **Gateways**: 5

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
    subgraph Corp. FP&A Analyst
        n1["fa:fa-user Apply Judgement to COS at Profit Center Level using Data-source dimension"]
        n2["fa:fa-user Update Margins Model in SAC for Gross Margin and Product Margin"]
        n3["fa:fa-user Capture Reports in SAC for QoQ, YoY, GM/PM Variance Analysis"]
        n4["fa:fa-user Capture Reports in ECA for QoQ, YoY, GM/PM/OM Variance Analysis and Walks"]
        n5[["fa:fa-cog Initiate Data loads based on POR / CQU Planning Calendar"]]
        n6[["fa:fa-cog Get the Forecasted Inventory Impact from ICOST into SAC at Profit Center,..."]]
        n7[["fa:fa-cog Get the Forecasted OCOS from Cost Center Model within SAC at Profit Center..."]]
        n8[["fa:fa-cog Get the Forecasted Revenue from IBP into SAC at Profit Center, Product Level"]]
        n9[["fa:fa-cog Get the Actuals from S4 CFIN into SAC at Profit Center, Product Level"]]
        n10[["fa:fa-cog Load Outbound Data to ECA"]]
        n11[["fa:fa-cog Get the Forecasted COGS from ICOST into CFIN into SAC at Profit Center..."]]
        n12(["fa:fa-play Final Profitability Analysis Reports Review Initialized"])
        n13(["fa:fa-stop Final Profitability Analysis Reports Review Completed"])
        n14{{"fa:fa-arrows-alt parallelGateway"}}
        n15{{"fa:fa-arrows-alt parallelGateway"}}
        n16{{"fa:fa-arrows-alt parallelGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n12 --> n5
    n5 --> n14
    n14 --> n11
    n14 --> n6
    n14 --> n7
    n14 --> n8
    n14 --> n9
    n11 --> n15
    n6 --> n15
    n15 --> n1
    n7 --> n16
    n1 --> n16
    n8 --> n16
    n9 --> n16
    n16 --> n2
    n2 --> n17
    n17 --> n3
    n17 --> n10
    n10 --> n4
    n3 --> n18
    n4 --> n18
    n18 --> n13
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
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
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV1tv4jgU_itWRl12pdDmSigPK9FAKkbtlpZ2R6NhH0zigFVjR7ZTylb89z2BhEsKU02XB8T5js_3nYvjmDcjFgkxOsbZ2RvlVHfQW0PPyJw0OqgxwYo0TLQB_saS4gkjqlGsSQXXI_rvepntZa_FsgKL8JyyZYGOyFQQ9DQwURcCmYkU5qqpiKRpw2xkks6xXIaCCVms_kLaqZWu1UrXlZAJkbsFlhXYsQ-hjHKyg93AC7yoiFMkFjw5IE39tJ3GjVWRHBOLeIalXqefK3KLX7_RRM_ATjFTBNbM9Jzd4AlhRY1a5gUW5_KlagZVhQ6Hho0yHFM-BdyzAJKYP-8g31qt0OrsbMy3ouixN-YIPjHDSvVIipQGuP-iUUoZ63zxwm7kW6bSUjyTzhenH_Rcx4yLSjpQumUWzW0uCJ3OdGciWFIubS6KGjpO9mrK145jmXIJ3zUtwpOdUthy2k57q3QV2KEdVkppmv4vJeirfMTqudTqu5ET9bZatt_yQ-s9X1Vmzwu6dr1PRL7QmOyRRlHk9net6rd82zpNehW5LSuskU6xJgu83BFeht6WMPKDyA5OEm706lnmk6EUcUXo9v3I3xIGV3bUdU4Sel3ba5cZAs9U4myGQiGzcxQNf-uiLsdsqfRmQfHh9o-xkeJOiptFv1E3y9gSfc2TKTymXCMtUHg3QlgjyCmlGoWAwrob8kIYjAh26Ti3LGz1sMZNJXIZE5RQiFVU8LHxz56Ucyj1lCXQOnSL5ZRyhW7hUWCIcjTqhigVEl1LoVTpRpgnRQZJHusSOuR2D7lDnOlcEvRAMiG12qe9F_cm-i6-m-j69mJ4i9ZnEYesN72h6pDY-5C4H3aPEV_cHeFe1_ENs-eaiv9jKxOLKRrA6UmL5hRdRUzgRKHiAE2Q4Gh494AuUHj_hIYMcw4TgKwYKY4rIN1nbR2yXhOY54ygSEgSY6WBbsBfYJ5CLtFgDmcOPNdSzNEARv4IpcHwi67Vh2-en5_XlIIPle6KbbRmD4XabqPN0BdUz8oJ1bXeS7U_lHqAvclzUtZyNfxJJds9td7PNaXL40rdWOdwyG_oRx4Ko8Ffn5WwrUONGxg1usv1ROSwUdbTB17YYfU4-8MuhHfXo3fj_Hmu75ttO79vdTIGp1xEYSeXUXhCGdXL3eauHgoYACWLchczeLMnQPvHPq27o1VaZL9EG4p5xoh-T-q9vVWkWEqxUE3MNMqwxIwRdr05p8fGarUf5H8mqPWZoOAzQe1fC4JTYPMDJoeazT_hZCltf2PaXuX3SsCuAa2aHdTsds2-rGy7JKwUWzXbrlIo7aA0t4I1u12zL-vrSwGntMuC7W3CpYBbs22rAqwNULXELf1VhV7NtquM3L03dpF3dVM5gJ3jsHsc9o7D_v6d5cDTOukJTnraJz2XJz3QpJMu-7TL2V5KD3G3vEAeol51izqE_eNw6zgcHIfbFWyYxpzIOaaJ0Xkz1v9D4L9KQlKcM22sTAPnWoyWPDY66_u6ka8vKD2K4Ro134Cr_wAXhQ2g" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.13 MB-060-200_Perform_CAPEX_Planning — MB-060-200_Perform_CAPEX_Planning

**Swim Lanes**: Corp. FP&A Analyst | **Tasks**: 13 | **Gateways**: 6

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
    subgraph Corp. FP&A Analyst
        n1["fa:fa-user Add Judgement for Volume and ASP"]
        n2["fa:fa-user Perform Volume and ASP Modeling"]
        n3["fa:fa-user Ratify POR Submit to Arrive at Total Revenue (Net Sales Volume and ASP)"]
        n4["fa:fa-user Review POR with SMG Leadership"]
        n5["fa:fa-user Review POR with BU CFO"]
        n6["fa:fa-user Revise Revenue POR Based on Management Review"]
        n7[["fa:fa-cog Input Volume and ASP to Arrive at Net Rev at Product and Customer Level"]]
        n8[["fa:fa-cog Disaggregate Rev down to MMID level Using Drivers"]]
        n9[["fa:fa-cog Add Judgement for Volume and ASP by RPP"]]
        n10[["fa:fa-cog Calculate Rev POR"]]
        n11[["fa:fa-cog Calculate Full P and L POR"]]
        n12[["fa:fa-cog Final Lock Full P and L POR"]]
        n13[["fa:fa-cog Update EPMA, Margin Analytics Excel"]]
        n14(["fa:fa-play Perform CAPEX Planning Initiated"])
        n15(["fa:fa-stop Perform CAPEX Planning Completed"])
        n16["Rev POR Submit Fed from IBP to SAC"]
        n17{{"fa:fa-code-branch Approved?"}}
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch Approved?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n8 --> n9
    n2 --> n1
    n3 --> n18
    n4 --> n19
    n7 --> n8
    n5 --> n17
    n1 --> n3
    n14 --> n2
    n17 -->|"Yes"| n4
    n18 --> n5
    n6 --> n18
    n17 -->|"No"| n20
    n19 -->|"Yes"| n7
    n20 --> n6
    n19 -->|"No"| n20
    n9 --> n10
    n10 --> n16
    n16 --> n21
    n11 --> n12
    n21 --> n11
    n12 --> n22
    n22 --> n15
    n13 --> n22
    n21 --> n13
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
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV12P4jYU_StWVlN2JajySRgeWoVAVlMNu2jY2bba6YNJHLDG2JGTwNBZ_nuvQxJIlnS1LQ-Ie3zPOdc3dmxetVBERBtrNzevlNNsjF572YZsSW-Meiuckl4fnYDPWFK8YiTtqZxY8GxJ_y7SDDt5UWkKC_CWsoNCl2QtCHq86yMPiKyPUszTQUokjXv9XiLpFsuDL5iQKvsNGcV6XLiVQxMhIyLPCbruGqEDVEY5OcOWa7t2oHgpCQWPGqKxE4_isHdUxTGxDzdYZkX5eUrm-OV3GmUbiGPMUgI5m2zL7vGKMDXHTOYKC3O5q5pBU-XDoWHLBIeUrwG3dYAk5s9nyNGPR3S8uXnitSn6NH3iCD4hw2k6JTFKM4BnuwzFlLHxG9v3Akfvp5kUz2T8xpy5U8vsh2omY5i63lfNHewJXW-y8UqwqEwd7NUcxmby0pcvY1PvywN8t7wIj85O_tAcmaPaaeIavuFXTnEc_y8n6Kv8hNPn0mtmBWYwrb0MZ-j4-rd61TSntusZ7T4RuaMhuRANgsCanVs1GzqG3i06Cayh7rdE1zgje3w4C976di0YOG5guJ2CJ792lflqIUVYCVozJ3BqQXdiBJ7ZKWh7hj0qKwSdtcTJBvlCJj-jYPGThzyO2SHNTgnqw40vT1qMxzEeqH4jL4rQb3m0hk3K4SkLiT4Llm8JwjxC3nLxpP11QTab5AWRwNi2KGgOixw22rrJtZrcB5zR-IAWHx_QMl9taYYyAbtd0h0IwZoXGWbogewIzwl6-4FkaInhBdLyetf0sFseZEfJvvDY02yDlvP36J5geDWkG5o0qc6_UyePyA8-NinDbykpqWtW1Am8BCMkOJpjjssen5SbSu6XWioUa3THkzxrd7XRHtUPEFI_Ye1EeZgVeX6eZmILtdxDEQw8Lk1GTZMpTfF6LYlaz4VWJPZcucznd1PElAB6TOExoqlylWlL7rYp972FhFYH9LBYtEQMvaniYxbmrKoIWtjON7ryg5wxtCjc7q8RzSYxoLAz0L0In7_LtJrMxyRSfrPF3OvDc5Vryk_bLKNhimYv4TeNN-y3tULC4NVR7RvfW8z-QAuGOVd9voMzlIJ2BPx3l3znzIfnm3TxfbFNGLnCVwu17Ge12QJYl7EUW3Q3KZbW0vObS9JwX1_P047IYAUHVbhBXpJIsSPRr0_a8XiZP7qeT15ClqewgN6f3ptt2u2P2Zj6f7IxjTMNSyn26QCzDCVYYsYI6yCZP0aCo_L0g4_QYPALbJEyNE9heTxxqwxHZWyXcZXunuJq2CmH3TI2TrFVhSXdrOKC_vVJ-5PAlv0K8tVAWZVTxsNWGTXxgyh41QENhbUUq0pM_SQxbCe2FW5Lq1qxJBo1syzGrHpklLM0qmmZFVBnlF0164yqzdUEDaudUWlYF0ewamh19WjA5nXYug7b12HnOjy8DruXV5bGyKhz5LZzBLrcOWR0D5ndQ1b3kF3fSpu4U94gm-iwI9utrldNeHQdvr0Kw6q8ChvXYbOCtb4GR-cW00gbv2rF_xb4bxORGOcs0459DeeZWB54qI2L-72WFyfBlGK4dm1P4PEfR5ENgQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Corporate Planner | MB-060-010_Load_Sales_Plan_into_Profitability_Analysis,  | |
| IT Admin | MB-060-010_Load_Sales_Plan_into_Profitability_Analysis, MB-060-100_Prepare_Planning_Structure,  | |
| Corp. FP&A Analyst | MB-060-020_Transfer_Sales_Plan_from_Profitability_Analysis_to_Sales_and_Operating_Plan, MB-060-100_Prepare_Planning_Structure, MB-060-170_Reconciliation_and_Alignment_of_Functional_and_Product_Plans, MB-060-180_Transfer_Detailed_Financial_Plans_to_Profitability_Analysis, MB-060-190_Review_Final_Profitability_Analysis_Reports, MB-060-200_Perform_CAPEX_Planning | |
| Cost Accountant | MB-060-060_Analyze_Alternatives_and_Determine_Changes, MB-060-090_Transfer_Planned_Activity_Requirements_for_Production, MB-060-130_Plan_Types_of_Work_and_Develop_Rates, MB-060-140_Process_Distributions_and_Assessments,  | |
| IT Administrator | MB-060-110_Process_Material_Changes,  | |
| Corp. Planner | MB-060-120_Process_Organizational_and_Financial_Elements,  | |
| Receiver | MB-060-120_Process_Organizational_and_Financial_Elements,  | |
| Sender | MB-060-120_Process_Organizational_and_Financial_Elements,  | |
| Corp. Allocations Lead | MB-060-180_Transfer_Detailed_Financial_Plans_to_Profitability_Analysis,  | |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for MB-060. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
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
| FPRR1514_IP | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  |  | 03.Medium |
| FPRR1514_IF | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  |  | 04.Low |
| FPRR1240 | Report | Custom report for Revenue Recognition by Stage for Product/Services Sale​ act... | 10. Object Complete |  |  | 03.Medium |
| FPRR1211 | Report | Report for searching on and viewing government contract timesheets for Intel ... | 10. Object Complete |  |  | 03.Medium |
| FPRR1210 | Report | Report for searching on and viewing government contract timesheet changes for... | 10. Object Complete |  |  | 03.Medium |
| FPRR0907_IP | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  |  | 03.Medium |
| FPRR0907_IF | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  |  | 04.Low |
| FPRR0497 | Report | CFR - Report to support multiple Treasury Funding requests from Multiple Inte... | 10. Object Complete |  |  | 03.Medium |
| FPRR0496 | Report | TPR-Report to support multiple Treasury Payment Requests from Multiple Intel ... | 10. Object Complete |  |  | 03.Medium |
| FPRR0461 | Report | Inter-company Outage Pre-consolidate Report (ACDOCA) | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0380 | Report | GL Interface – Reconciliation Report/Dashboard | 10. Object Complete | NA | NA | 02.High |
| FPRR0327_IP | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA | NA | 02.High |
| FPRR0327_IF | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0288_IP | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0288_IF | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0288_CFIN | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA | NA | 02.High |
| FPRR0027 | Report | In House Cash – Loan Account balance Detailed report | 10. Object Complete | NA | NA | 01.Very High |
| FPRM003 | Conversion | Revenue Recognition Rules | 10. Object Complete |  |  | N/A |
| FPRM002 | Conversion | Revenue Contracts | 10. Object Complete |  |  | N/A |
| FPRM001 | Conversion | Bank Master | 10. Object Complete | ECC | CFIN | N/A |
| FPRC1724_IP | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  |  | 02.High |
| FPRC1724_IF | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  |  | 03.Medium |
| FPRC1565 | Conversion | Convert active delegate relationships for Timesheet approval | 10. Object Complete |  |  | 02.High |
| FPRC1493 | Conversion | Conversion of WIP values as per Component structure in S/4 - IP | 10. Object Complete |  |  | 02.High |
| FPRC1491 | Conversion | Conversion of WIP values as per Component structure in S/4 - Back End IF | 10. Object Complete |  |  | 02.High |
| FPRC1464_IP | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  |  | 02.High |
| FPRC1464_IF | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  |  | 02.High |
| FPRC1442 | Conversion | Conversion of Actual Labor hours for Intel Federal Projects | 10. Object Complete |  |  | 02.High |
| FPRC1441 | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete |  |  | 02.High |
| FPRC1212 | Conversion | Project Actuals Conversion including Intel Federal | 10. Object Complete |  |  | 03.Medium |
| FPRC0908_IP | Conversion | Project Budget Conversion | 10. Object Complete |  |  | 03.Medium |
| FPRC0908_IF | Conversion | Project Budget Conversion | 10. Object Complete |  |  | 03.Medium |
| FPRC0196_IP | Conversion | Asset Transaction data conversion | 10. Object Complete | NA | NA | 02.High |
| FPRC0196_IF | Conversion | Asset Transaction data conversion | 10. Object Complete | NA | NA | 02.High |
| FPRC0195_IP | Conversion | Asset Master data conversion | 10. Object Complete | NA | NA | 03.Medium |
| FPRC0195_IF | Conversion | Asset Master data conversion | 10. Object Complete | NA | NA | 03.Medium |
| FPRC0174_IP | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC | S4 | 02.High |
| FPRC0174_IF | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC | S4 | 03.Medium |
| FPRC0117 | Conversion | Conversion – In House Cash: Current Account creation and Current Account Bala... | 10. Object Complete | ECC | CFIN | 02.High |
| FPRC0116 | Conversion | Conversion – Migration of Existing Bank Guarantees and Intercompany Loans to ... | 10. Object Complete | Quantum | CFIN | 03.Medium |
| FPRC0035_IP | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  | MDG | 03.Medium |
| FPRC0035_IF | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  | MDG | 04.Low |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for MB-060.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for MB-060.

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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| FPRW1449 | Workflow | TPR : Workflow to handle Memo creation and cancellation process | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRW1444 | Workflow | TFR: Workflow to handle Memo creation and cancellation process | 10. Object Complete |  | NA | 03.Medium |
| FPRW1064_IP | Workflow | Custom Workflow will also be created with some predefined process/rules for a... | 10. Object Complete |  | NA | 01.Very High |
| FPRW1064_IF | Workflow | Custom Workflow will also be created with some predefined process/rules for a... | 10. Object Complete |  | NA | 02.High |
| FPRW0930 | Workflow | Workflow for Counterparty Approval | 10. Object Complete |  | NA | 03.Medium |
| FPRW0906_IP | Workflow | Custom workflow: Change Order Create and Change Approval | 10. Object Complete |  | NA | 03.Medium |
| FPRW0906_IF | Workflow | Custom workflow: Change Order Create and Change Approval | 10. Object Complete |  | NA | 03.Medium |
| FPRW0904_IP | Workflow | Custom Workflow - WBS Element Request approval with WBS Element creation | 10. Object Complete |  | NA | 03.Medium |
| FPRW0904_IF | Workflow | Custom Workflow - WBS Element Request approval with WBS Element creation | 10. Object Complete |  | NA | 03.Medium |
| FPRW0900_IP | Workflow | Custom Workflow: Approval for Project creation and create a Project def and l... | 10. Object Complete |  | NA | 03.Medium |
| FPRW0900_IF | Workflow | Custom Workflow: Approval for Project creation and create a Project def and l... | 10. Object Complete |  | NA | 03.Medium |
| FPRW0445_IP | Workflow | Project budget approval workflow (Capex)​ | 10. Object Complete |  | NA | 03.Medium |
| FPRW0445_IF | Workflow | Project budget approval workflow (Capex)​ | 10. Object Complete |  | NA | 03.Medium |
| FPRW0325_IP | Workflow | Custom workflow to manage the approval process in bulk/individual requests | 10. Object Complete | NA → NA | NA | 02.High |
| FPRW0325_IF | Workflow | Custom workflow to manage the approval process in bulk/individual requests | 10. Object Complete | NA → NA | NA | 02.High |
| FPRW0165_IP | Workflow | Workflow is required to trigger the approvers based on the business requireme... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRW0165_IF | Workflow | Workflow is required to trigger the approvers based on the business requireme... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRW0165_CFIN | Workflow | Workflow is required to trigger the approvers based on the business requireme... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR1514_IP | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  | NA | 03.Medium |
| FPRR1514_IF | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  | NA | 04.Low |
| FPRR1240 | Report | Custom report for Revenue Recognition by Stage for Product/Services Sale​ act... | 10. Object Complete |  | NA | 03.Medium |
| FPRR1211 | Report | Report for searching on and viewing government contract timesheets for Intel ... | 10. Object Complete |  | NA | 03.Medium |
| FPRR1210 | Report | Report for searching on and viewing government contract timesheet changes for... | 10. Object Complete |  | NA | 03.Medium |
| FPRR0907_IP | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  | NA | 03.Medium |
| FPRR0907_IF | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  | NA | 04.Low |
| FPRR0497 | Report | CFR - Report to support multiple Treasury Funding requests from Multiple Inte... | 10. Object Complete |  | NA | 03.Medium |
| FPRR0496 | Report | TPR-Report to support multiple Treasury Payment Requests from Multiple Intel ... | 10. Object Complete |  | NA | 03.Medium |
| FPRR0461 | Report | Inter-company Outage Pre-consolidate Report (ACDOCA) | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0380 | Report | GL Interface – Reconciliation Report/Dashboard | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR0327_IP | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR0327_IF | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0288_IP | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0288_IF | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0288_CFIN | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR0027 | Report | In House Cash – Loan Account balance Detailed report | 10. Object Complete | NA → NA | NA | 01.Very High |
| FPRM003 | Conversion | Revenue Recognition Rules | 10. Object Complete |  | NA | N/A |
| FPRM002 | Conversion | Revenue Contracts | 10. Object Complete |  | NA | N/A |
| FPRM001 | Conversion | Bank Master | 10. Object Complete | ECC → CFIN | NA | N/A |
| FPRI1725_IP | Interface | Interface to be developed to transfer the files from Denodo to FS share path ... | 10. Object Complete |  | Intel MW | 03.Medium |
| FPRI1725_IF | Interface | Interface to be developed to transfer the files from Denodo to FS share path ... | 10. Object Complete |  | Intel MW | 04.Low |
| FPRI1704 | Interface | Automated Tool MUP Excess Capacity calculation and associated PCOS/OCOS Split... | 10. Object Complete |  | BODS | 03.Medium |
| FPRI1670 | Interface | Import Dot process/stage details from MDG into S4. ​ | 10. Object Complete |  | NA | 03.Medium |
| FPRI1669 | Interface | Import Xeus/Mars volumes from ECA into S4.​ | 07. FUT Roadblock |  | BODS | 03.Medium |
| FPRI1504 | Interface | Asset Delete from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1503 | Interface | Asset Display from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1502 | Interface | Asset Change from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1463 | Interface | Interface to upload payroll data from Workday to S/4 IP for legal entity 199 ... | 10. Object Complete |  | MULESOFT | 03.Medium |
| FPRI1447 | Interface | GL Interface –Create Inbound IDOCs to CFIN from IF system | 10. Object Complete | IF → CFIN | NA | 03.Medium |
| FPRI1446 | Interface | GL Interface –Create Inbound IDOCs to CFIN from IP system | 10. Object Complete | IP → CFIN | NA | 03.Medium |
| FPRI1439 | Interface | Receive planned production quantities per production version from ECA to S/4 ... | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1338 | Interface | Outbound Interface to view the Cleared Customer Invoices from CFIN System to ... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI1315 | Interface | Asset Create from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1306 | Interface | Interface for importing GL transactional data from SAP CFIN system into SAP IF | 10. Object Complete | CFIN → S/4 | NA | 03.Medium |
| FPRI1305 | Interface | Interface for importing GL transactional data from SAP CFIN system into SAP IP | 10. Object Complete | CFIN → S/4 | NA | 03.Medium |
| FPRI1288 | Interface | Activity Inbound interface from ECA to S4 IP | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1287 | Interface | Production quantity update in WAC custom table from ECA to S4 IF | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1286_IP | Interface | Interface between SAP IP and IF boxes for Outbound IDOC flow_IP | 10. Object Complete | MULESOFT → S/4 | SFT | 03.Medium |
| FPRI1286_IF | Interface | Interface between SAP IP and IF boxes for Outbound IDOC flow_IF | 10. Object Complete | MULESOFT → S/4 | SFT | 04.Low |
| FPRI1273 | Interface | Activity Quantity Inbound interface from ECA to S4 IF | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1241 | Interface | Disti Rebate percentage of gross for Unissued Returns and Intransit Deferral | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FPRI1238 | Interface | Pull Foundry WBS from HAT and create in LE 199 in IP S/4 for Foundry Employee... | 10. Object Complete | Head Count Assignment Tool → S/4 | BODS | 03.Medium |
| FPRI1105 | Interface | Interface for automatic creation of B2B customer related payment advice | 10. Object Complete |  | MULESOFT | 03.Medium |
| FPRI0981_IP | Interface | Interface of SAP PPM module to SPEED | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FPRI0981_IF | Interface | Interface of SAP PPM module to SPEED | 10. Object Complete | ECA → S/4 | BODS | 04.Low |
| FPRI0913_IP | Interface | Export the Planning data from the SAC table to PPM standard tables using the ... | 10. Object Complete | SAC → S/4 | NA | 02.High |
| FPRI0913_IF | Interface | Export the Planning data from the SAC table to PPM standard tables using the ... | 10. Object Complete | SAC → S/4 | NA | 03.Medium |
| FPRI0909_IP | Interface | Interface for importing the Headcount details by Person# and WBS element comb... | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FPRI0909_IF | Interface | Interface for importing the Headcount details by Person# and WBS element comb... | 10. Object Complete | ECA → S/4 | BODS | 04.Low |
| FPRI0895 | Interface | Import Tool Sharing Forecasted Data from FCS to S4 & derive FTQ data by Capex... | 10. Object Complete | FCS → S/4 | BODS | 02.High |
| FPRI0894 | Interface | Planned Volume from IP-BY will be utilized as a KP26 quantity to split 'Overh... | 10. Object Complete | ICS → S/4 | BODS | 02.High |
| FPRI0869 | Interface | Interface for automatic creation of WOM related payment advice | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0867 | Interface | Outbound Interface to view the open & Cleared Customer Invoices from CFIN Sys... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0866 | Interface | Interface to Obtains the payer associated to the sold to from CFIN System to ... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0865 | Interface | Interface to transfer the Uploaded WCP Grant Amount from CFIN to WOM and Defe... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0864_IP | Interface | Interface between SAP IP and IF boxes for Inbound IDOC flow_IP | 10. Object Complete | MULESOFT → S/4 | SFT | 03.Medium |
| FPRI0864_IF | Interface | Interface between SAP IP and IF boxes for Inbound IDOC flow_IF | 10. Object Complete | MULESOFT → S/4 | SFT | 04.Low |
| FPRI0863_IP | Interface | Interface between SAP & ECA to provide information for auto certification in ... | 10. Object Complete | ECA → BLACKLINE | APIGEE;DENODO | 03.Medium |
| FPRI0863_IF | Interface | Interface between SAP & ECA to provide information for auto certification in ... | 10. Object Complete | ECA → BLACKLINE | APIGEE;DENODO | 04.Low |
| FPRI0863_CFIN | Interface | Interface between SAP & ECA to provide information for auto certification in ... | 10. Object Complete | ECA → BLACKLINE | APIGEE;DENODO | 03.Medium |
| FPRI0862 | Interface | Interface to transfer the details of selected invoice from WOM to CFIN ( Inbo... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| FPRI0778_IP | Interface | Continue to auto-certify a BL task when the related JE is approved | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 03.Medium |
| FPRI0778_IF | Interface | Continue to auto-certify a BL task when the related JE is approved | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 03.Medium |
| FPRI0778_CFIN | Interface | Continue to auto-certify a BL task when the related JE is approved | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 02.High |
| FPRI0770_IP | Interface | To enable auto-certify a BL [Blackline] task when the related JE is approved | 10. Object Complete | BLACKLINE → ECA | NA | 03.Medium |
| FPRI0770_IF | Interface | To enable auto-certify a BL [Blackline] task when the related JE is approved | 10. Object Complete | BLACKLINE → ECA | NA | 03.Medium |
| FPRI0770_CFIN | Interface | To enable auto-certify a BL [Blackline] task when the related JE is approved | 10. Object Complete | BLACKLINE → ECA | NA | 02.High |
| FPRI0704 | Interface | IF-IP Integration Actual Cost - Inbound Interface | 10. Object Complete | OpenText → S/4 | SFT | 02.High |
| FPRI0703 | Interface | IF-IP Integration Actual Cost - Outbound Interface | 10. Object Complete | S/4 → OpenText | SFT | 02.High |
| FPRI0696_IP | Interface | Interface between ONESOURCE and Readsoft Process Director built on the back o... | 10. Object Complete | ONESOURCE → READSOFT | NA | 02.High |
| FPRI0696_IF | Interface | Interface between ONESOURCE and Readsoft Process Director built on the back o... | 10. Object Complete | ONESOURCE → READSOFT | NA | 03.Medium |
| FPRI0695 | Interface | Reference Interest Rates - S4 converted data from MDG to CFIN | 10. Object Complete | S/4 MDG → CFIN | NA | 03.Medium |
| FPRI0694 | Interface | Exchange Rates N - S4 converted data from MuleSoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0693 | Interface | Exchange Rates L - S4 converted data from MuleSoft to Treasury Suite | 10. Object Complete | Treasury Suite → MULESOFT | MULESOFT | 03.Medium |
| FPRI0600_IP | Interface | Continuation to use Blackline Account Reconciliations Tool (ART), Blackline M... | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 04.Low |
| FPRI0600_IF | Interface | Continuation to use Blackline Account Reconciliations Tool (ART), Blackline M... | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 04.Low |
| FPRI0600_CFIN | Interface | Continuation to use Blackline Account Reconciliations Tool (ART), Blackline M... | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 03.Medium |
| FPRI0599_IP | Interface | ServiceNow Asset change | 10. Object Complete | SERVICENOW → S/4 | MULESOFT | 03.Medium |
| FPRI0599_IF | Interface | ServiceNow Asset change | 10. Object Complete | SERVICENOW → S/4 | MULESOFT | 04.Low |
| FPRI0598 | Interface | N rate from Mulesoft to MDG | 10. Object Complete | MULESOFT → S/4 MDG | MULESOFT | 04.Low |
| FPRI0597 | Interface | N rate from Mulesoft to Bloomberg | 10. Object Complete | MULESOFT → BLOOMBERG | MULESOFT | 03.Medium |
| FPRI0596 | Interface | N rate from Mulesoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0554 | Interface | SKF Interface to get file from ECA and send to S4 via BODS - IF | 10. Object Complete | ECA → S/4 | MuleSoft | 02.High |
| FPRI0545 | Interface | IF-IP Integration - Interface to send Cost Idoc from S4 If to S4 IP | 10. Object Complete | S/4 → S/4 | SFT | 03.Medium |
| FPRI0544 | Interface | IF-IP Integration - Interface to receive Cost Idoc from S4 If to S4 IP | 10. Object Complete | S/4 → S/4 | SFT | 03.Medium |
| FPRI0533 | Interface | Reference Interest Rates from MuleSoft to S4 MDG | 10. Object Complete | Bloomberg → S/4 MDG | MULESOFT | 03.Medium |
| FPRI0532 | Interface | Request for Reference Interest Rates from MuleSoft to Bloomberg | 10. Object Complete | MULESOFT → BLOOMBERG | MULESOFT | 03.Medium |
| FPRI0531 | Interface | L Rates from MuleSoft to S4 MDG | 10. Object Complete | Bloomberg → S/4 MDG | MULESOFT | 03.Medium |
| FPRI0530 | Interface | Request for L Rates from MuleSoft to Bloomberg | 10. Object Complete | MULESOFT → BLOOMBERG | MULESOFT | 03.Medium |
| FPRI0529 | Interface | L Rates from MuleSoft to Quantum | 10. Object Complete | MULESOFT → QUANTUM | MULESOFT | 03.Medium |
| FPRI0528 | Interface | L Rates from MuleSoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0527 | Interface | Reference Interest Rates from MuleSoft to Quantum | 10. Object Complete | MULESOFT → QUANTUM | MULESOFT | 03.Medium |
| FPRI0526 | Interface | Reference Interest Rates from MuleSoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0505 | Interface | Interface – Copp Clark Holiday Calendar Integration with SAP | 10. Object Complete | Copp Clark → S/4 | SFT | 03.Medium |
| FPRI0379 | Interface | GL Interface – File processing in MuleSoft-Payroll | 10. Object Complete | PAYROLL → S/4 | MULESOFT | 02.High |
| FPRI0378_IP | Interface | GL Interface - SAP API IP | 10. Object Complete | API → S/4 | MULESOFT | 02.High |
| FPRI0378_IF | Interface | GL Interface - SAP API IF | 10. Object Complete | API → S/4 | MULESOFT | 03.Medium |
| FPRI0377 | Interface | GL Interface - File Processing in Mulesoft | 10. Object Complete | CONCUR → S/4 | MULESOFT | 02.High |
| FPRI0376 | Interface | GL Interface - File Processing in Mulesoft | 10. Object Complete | ICOST → S/4 | MULESOFT | 02.High |
| FPRI0323_IP | Interface | Create a common API for Asset updates, transfer, retire and Mass upload | 10. Object Complete |  | NA | 02.High |
| FPRI0323_IF | Interface | Create a common API for Asset updates, transfer, retire and Mass upload | 10. Object Complete |  | NA | 03.Medium |
| FPRI0227 | Interface | Outbound Interface from CFIN to QTM in relation to not only QTM payment ackno... | 10. Object Complete | S/4 → Quantum | SFT | 03.Medium |
| FPRI0226 | Interface | Inbound Interface from QTM to CFIN in relation to QTM payment files and MT me... | 10. Object Complete | Quantum → S/4 | SFT | 03.Medium |
| FPRI0224 | Interface | Outbound Interface - SAP to Quantum for Transmitting Cash Management Relevant... | 10. Object Complete | S/4 → Quantum | SFT | 02.High |
| FPRI0188 | Interface | Inbound Interface from EMS to S/4 to create WBS element and Update WBS elemen... | 10. Object Complete | XEUS → S/4 | APIGEE | 02.High |
| FPRF0230 | Form | Invoice output Layout - America | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE1723_IP | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1723_IF | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1722_IP | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1722_IF | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1711 | Enhancement | BADI Enhancement to change Order Type from Product cost Collector from IP & I... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1706 | Enhancement | Enhancement to create Cash Management relevant data from F110 Payment Run for... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1705 | Enhancement | Enhancement to do Cash App post EBS load with the corresponding payment advice. | 10. Object Complete |  | NA | 03.Medium |
| FPRE1695 | Enhancement | Custom Fiori app - Change WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1671_IP | Enhancement | S4, Perform required calculations, summarizations, mappings and post the allo... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1671_IF | Enhancement | S4, Perform required calculations, summarizations, mappings and post the allo... | 10. Object Complete |  | NA | 04.Low |
| FPRE1661_IP | Enhancement | WBS transfer tool | 07. FUT Roadblock |  | NA | 02.High |
| FPRE1661_IF | Enhancement | WBS transfer tool | 07. FUT Roadblock |  | NA | 03.Medium |
| FPRE1660 | Enhancement | Enhancement for Revenue Recognition by Stage postings for Product/Services Sa... | 10. Object Complete |  | NA | 02.High |
| FPRE1659 | Enhancement | Enhancement for Revenue Recognition by Stage postings for Product/Services Sa... | 10. Object Complete |  | NA | 02.High |
| FPRE1650_IP | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Forecast.​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1650_IF | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Forecast.​ | 10. Object Complete |  | NA | 04.Low |
| FPRE1620_IP | Enhancement | Implement OSS Note 2358961 to allow COGS split based on Aux CCS at time of de... | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE1620_IF | Enhancement | Implement OSS Note 2358961 to allow COGS split based on Aux CCS at time of de... | 99. Rejected/Cancelled/On Hold |  | NA | 04.Low |
| FPRE1600 | Enhancement | Custom Fiori app - Create WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1599_IP | Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO li... | 07. FUT Roadblock |  | NA | 03.Medium |
| FPRE1599_IF | Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO li... | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1564 | Enhancement | Employee Notification for timesheet entry | 10. Object Complete |  | NA | 03.Medium |
| FPRE1563 | Enhancement | Manager notification for timesheet approval | 10. Object Complete |  | NA | 03.Medium |
| FPRE1562 | Enhancement | Manage Delegates for approval | 10. Object Complete |  | NA | 03.Medium |
| FPRE1561 | Enhancement | Timesheet approval | 10. Object Complete |  | NA | 02.High |
| FPRE1560 | Enhancement | Timesheet entry for Intel Federal employees | 10. Object Complete |  | NA | 01.Very High |
| FPRE1553 | Enhancement | Custom Fiori app - Change WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1519_IP | Enhancement | Project Change Order - Edit and Submit of draft request with change functiona... | 10. Object Complete |  | NA | 02.High |
| FPRE1519_IF | Enhancement | Project Change Order - Edit and Submit of draft request with change functiona... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1518_IP | Enhancement | Project Change Order - Change existing Purchase Orders during creation of Pro... | 10. Object Complete |  | NA | 02.High |
| FPRE1518_IF | Enhancement | Project Change Order - Change existing Purchase Orders during creation of Pro... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1517_IP | Enhancement | Project Change Order - Create Purchase Orders during creation of Project Chan... | 10. Object Complete |  | NA | 02.High |
| FPRE1517_IF | Enhancement | Project Change Order - Create Purchase Orders during creation of Project Chan... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1516_IP | Enhancement | Enhancement to enable user decision action to be taken from email directly fo... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1516_IF | Enhancement | Enhancement to enable user decision action to be taken from email directly fo... | 10. Object Complete |  | NA | 04.Low |
| FPRE1515_IP | Enhancement | Enhancement to display popup screen to trigger project creation workflow | 10. Object Complete |  | NA | 03.Medium |
| FPRE1515_IF | Enhancement | Enhancement to display popup screen to trigger project creation workflow | 10. Object Complete |  | NA | 04.Low |
| FPRE1513_IP | Enhancement | Generate and download JV file for JE posting | 10. Object Complete |  | NA | 03.Medium |
| FPRE1513_IF | Enhancement | Generate and download JV file for JE posting | 10. Object Complete |  | NA | 04.Low |
| FPRE1513_CFIN | Enhancement | Generate and download JV file for JE posting | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE1512_IP | Enhancement | Query confirm ITT document to determine the Capital/Expense and tax code manu... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1512_IF | Enhancement | Query confirm ITT document to determine the Capital/Expense and tax code manu... | 10. Object Complete |  | NA | 04.Low |
| FPRE1511_IP | Enhancement | Query existing draft ITT document and make changes | 10. Object Complete |  | NA | 03.Medium |
| FPRE1511_IF | Enhancement | Query existing draft ITT document and make changes | 10. Object Complete |  | NA | 04.Low |
| FPRE1510_IP | Enhancement | ITT document creation | 10. Object Complete |  | NA | 03.Medium |
| FPRE1510_IF | Enhancement | ITT document creation | 10. Object Complete |  | NA | 04.Low |
| FPRE1448 | Enhancement | FIORI screen to take care of TPR Display/ Change/ cancellation options | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE1443 | Enhancement | FIORI screen to take care of TFR Display/ Change/ cancellation options | 10. Object Complete |  | NA | 03.Medium |
| FPRE1438 | Enhancement | Update mixing ratio for Procurement alternative for Cross site transfer based... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1419 | Enhancement | Update Procurement alternatives based on production version & PIR for cross s... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1328 | Enhancement | Legal Valuation standard cost calculation enhancement | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE1239 | Enhancement | Enhancement for Revenue Recognition by Stage postings for Product/Services Sa... | 10. Object Complete |  | NA | 02.High |
| FPRE1235_IP | Enhancement | Add custom fields to CJI3 and CJI5 reports (SAP S/4HANA Project Systems modul... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1235_IF | Enhancement | Add custom fields to CJI3 and CJI5 reports (SAP S/4HANA Project Systems modul... | 10. Object Complete |  | NA | 04.Low |
| FPRE1209 | Enhancement | Upload adjustments to time sheet entries in bulk for Intel Federal. | 10. Object Complete |  | NA | 02.High |
| FPRE1104_IP | Enhancement | WBS with custom attributes will be created in the PS module. The master data ... | 10. Object Complete |  | NA | 02.High |
| FPRE1104_IF | Enhancement | WBS with custom attributes will be created in the PS module. The master data ... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1025_IP | Enhancement | Custom Fiori app will be created using Free style model to display WBS/AUC re... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1025_IF | Enhancement | Custom Fiori app will be created using Free style model to display WBS/AUC re... | 10. Object Complete |  | NA | 04.Low |
| FPRE0942_IP | Enhancement | Interface of SAP PPM module to ATLAS | 10. Object Complete | S4 → ATLAS | NA | 03.Medium |
| FPRE0942_IF | Enhancement | Interface of SAP PPM module to ATLAS | 10. Object Complete | S4 → ATLAS | NA | 04.Low |
| FPRE0931_IP | Enhancement | Rebuild Boundary Application ITT in S/4 | 10. Object Complete |  | NA | 03.Medium |
| FPRE0931_IF | Enhancement | Rebuild Boundary Application ITT in S/4 | 10. Object Complete |  | NA | 03.Medium |
| FPRE0931_CFIN | Enhancement | Rebuild Boundary Application ITT in S/4 | 10. Object Complete |  | NA | 02.High |
| FPRE0929 | Enhancement | Fiori UI for Counterparty Maintenance and User Exit to trigger replication to... | 10. Object Complete |  | NA | 02.High |
| FPRE0928 | Enhancement | Enhancement for automatic derivation and population of Purpose Of Payment (PO... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0899_IP | Enhancement | Custom Enhancement to disaggregate: Owner CC-DPN $ to WBS elements using Cape... | 10. Object Complete |  | NA | 02.High |
| FPRE0899_IF | Enhancement | Custom Enhancement to disaggregate:Owner CC-DPN $ to WBS elements using Capex... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0892 | Enhancement | Derive ICS FTQ data by Capex WBS L2 & Mfr. Process Node CC​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0891 | Enhancement | Split from primary Cost centers to PCOS & R&D/OCOS | 99. Rejected/Cancelled/On Hold |  | NA | 04.Low |
| FPRE0890_IP | Enhancement | Investment type creation and automatic settlement rule generation for Opex Pr... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0890_IF | Enhancement | Investment type creation and automatic settlement rule generation for Opex Pr... | 10. Object Complete |  | NA | 04.Low |
| FPRE0889_IP | Enhancement | Custom table needs to be created to hold allocation %s based on LOB Profit ce... | 10. Object Complete |  | NA | 04.Low |
| FPRE0889_IF | Enhancement | Custom table needs to be created to hold allocation %s based on LOB Profit ce... | 10. Object Complete |  | NA | 04.Low |
| FPRE0888_IP | Enhancement | Mass Update Fields in WBS Elements | 10. Object Complete |  | NA | 02.High |
| FPRE0888_IF | Enhancement | Mass Update Fields in WBS Elements | 10. Object Complete |  | NA | 03.Medium |
| FPRE0887_IP | Enhancement | WBS Element field synchronization to AUC and Fixed assets - Construction ID -... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0887_IF | Enhancement | WBS Element field synchronization to AUC and Fixed assets - Construction ID -... | 10. Object Complete |  | NA | 04.Low |
| FPRE0886_IP | Enhancement | Project Change Order - Create Project Change Order via custom Fiori Screens w... | 10. Object Complete |  | NA | 02.High |
| FPRE0886_IF | Enhancement | Project Change Order - Create Project Change Order via custom Fiori Screens w... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0885 | Enhancement | Custom Fiori app - Create WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0884_IP | Enhancement | Custom Fiori app - CPA (Project Budget) approval request using PPM Item decis... | 10. Object Complete |  | NA | 02.High |
| FPRE0884_IF | Enhancement | Custom Fiori app - CPA (Project Budget) approval request using PPM Item decis... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0883_IP | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Actuals.​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0883_IF | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Actuals.​ | 10. Object Complete |  | NA | 04.Low |
| FPRE0882 | Enhancement | Derive FCS FTQ data by Capex WBS L2 & Mfr. Process Node CC​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0881 | Enhancement | DMEE User Exits Required in the payment files- APAC​ | 10. Object Complete |  | NA | 04.Low |
| FPRE0880 | Enhancement | Cash concentration functionality for cross-currency current accounts | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE0879 | Enhancement | File Formatting and processing to support MBC and APM integration | 10. Object Complete |  | NA | 04.Low |
| FPRE0877_IP | Enhancement | Automation to set TECO and CLSD status on Project/ WBS | 10. Object Complete |  | NA | 02.High |
| FPRE0877_IF | Enhancement | Automation to set TECO and CLSD status on Project/ WBS | 10. Object Complete |  | NA | 03.Medium |
| FPRE0870 | Enhancement | Smart Exporter Interface to CFIN | 10. Object Complete | EY Smart Exporter Tool → S4 | NA | 04.Low |
| FPRE0827 | Enhancement | MT3xx and MT5xx Files - Adjust SWIFT Parameters for MBC | 10. Object Complete |  | NA | 04.Low |
| FPRE0786 | Enhancement | Enhancement to Mass upload of WOM payment advice. | 10. Object Complete |  | NA | 03.Medium |
| FPRE0785 | Enhancement | Enhancement to upload WCP Grant Amount in CFIN sys | 10. Object Complete |  | NA | 03.Medium |
| FPRE0784_IP | Enhancement | Reclass program for XIU/ SIU to reclass expense to inventory accounts (cost c... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0784_IF | Enhancement | Reclass program for XIU/ SIU to reclass expense to inventory accounts (cost c... | 10. Object Complete |  | NA | 04.Low |
| FPRE0783_IP | Enhancement | Asset creation from PO (S4 / Ariba / EMS, etc.) | 10. Object Complete | Ariba → S4 | NA | 03.Medium |
| FPRE0783_IF | Enhancement | Asset creation from PO (S4 / Ariba / EMS, etc.) | 10. Object Complete | Ariba → S4 | NA | 04.Low |
| FPRE0781_IP | Enhancement | Import Standard Cost from S4 tables into SAC using Custom CDS view. | 10. Object Complete |  | NA | 03.Medium |
| FPRE0781_IF | Enhancement | Import Standard Cost from S4 tables into SAC using Custom CDS view. | 10. Object Complete |  | NA | 04.Low |
| FPRE0780_IP | Enhancement | Read the workday file from AL11 in IP, IF | 10. Object Complete |  | NA | 03.Medium |
| FPRE0780_IF | Enhancement | Read the workday file from AL11 in IP, IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0779_IP | Enhancement | Enhance the details in workday file to meet AE format in IP, IF | 10. Object Complete |  | NA | 03.Medium |
| FPRE0779_IF | Enhancement | Enhance the details in workday file to meet AE format in IP, IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0777_IP | Enhancement | Add a field in ACDOCA to store Cert ID to continue auto-certify a BL task whe... | 10. Object Complete |  | NA | 04.Low |
| FPRE0777_IF | Enhancement | Add a field in ACDOCA to store Cert ID to continue auto-certify a BL task whe... | 10. Object Complete |  | NA | 04.Low |
| FPRE0777_CFIN | Enhancement | Add a field in ACDOCA to store Cert ID to continue auto-certify a BL task whe... | 10. Object Complete |  | NA | 04.Low |
| FPRE0764_IP | Enhancement | Import Headcount details by cost center and update in S4 for HR benefits spen... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0764_IF | Enhancement | Import Headcount details by cost center and update in S4 for HR benefits spen... | 10. Object Complete |  | NA | 04.Low |
| FPRE0763 | Enhancement | Placeholder - BADI for Memo Records with different Planning Levels/Types gene... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0761 | Enhancement | Branch Name and Address for Payments instead of entity Name and Address | 10. Object Complete |  | NA | 03.Medium |
| FPRE0760_IP | Enhancement | SAP RAR and TM Integration to trigger POD Event | 10. Object Complete |  | NA | 03.Medium |
| FPRE0760_IF | Enhancement | SAP RAR and TM Integration to trigger POD Event | 10. Object Complete |  | NA | 04.Low |
| FPRE0702 | Enhancement | Calculation of variance to be loaded for Group Actual Costing | 10. Object Complete |  | NA | 03.Medium |
| FPRE0701_IP | Enhancement | Mixed Costing ratio auto update | 10. Object Complete |  | NA | 03.Medium |
| FPRE0701_IF | Enhancement | Mixed Costing ratio auto update | 10. Object Complete |  | NA | 04.Low |
| FPRE0700_IP | Enhancement | Representative material ID – Q2-Q8 Forecast | 10. Object Complete |  | NA | 03.Medium |
| FPRE0700_IF | Enhancement | Representative material ID – Q2-Q8 Forecast | 10. Object Complete |  | NA | 04.Low |
| FPRE0699 | Enhancement | Enhancement for Excess Capacity – Fixed Spending Adjustment | 10. Object Complete |  | NA | 02.High |
| FPRE0698 | Enhancement | Legal Valuation standard cost calculation enhancement | 10. Object Complete |  | NA | 04.Low |
| FPRE0697 | Enhancement | RAR Balance sheet posting with MM & Sold To ID | 10. Object Complete |  | NA | 03.Medium |
| FPRE0648_IP | Enhancement | RD04 - Intercompany invoice billing posting to different GL accounts | 10. Object Complete |  | NA | 03.Medium |
| FPRE0648_IF | Enhancement | RD04 - Intercompany invoice billing posting to different GL accounts | 10. Object Complete |  | NA | 04.Low |
| FPRE0647_IP | Enhancement | Intercompany - Subledger Posting template & Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| FPRE0647_IF | Enhancement | Intercompany - Subledger Posting template & Approval Workflow | 10. Object Complete |  | NA | 04.Low |
| FPRE0647_CFIN | Enhancement | Intercompany - Subledger Posting template & Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| FPRE0646_IP | Enhancement | An automated solution to record the depreciation amount in a monthly basis fo... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0646_IF | Enhancement | An automated solution to record the depreciation amount in a monthly basis fo... | 10. Object Complete |  | NA | 04.Low |
| FPRE0645_IP | Enhancement | Need to identify a Mass settlement upload tool. Today, the capital life cycle... | 10. Object Complete |  | NA | 01.Very High |
| FPRE0645_IF | Enhancement | Need to identify a Mass settlement upload tool. Today, the capital life cycle... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0624 | Enhancement | Portal Remittance Automation- Retrofitting | 10. Object Complete |  | NA | 04.Low |
| FPRE0623 | Enhancement | Payment Advice Bot Success & Exception Report | 10. Object Complete |  | NA | 04.Low |
| FPRE0622 | Enhancement | Exception Handling & Trigger Set up | 10. Object Complete |  | NA | 04.Low |
| FPRE0621 | Enhancement | Payment Advice CSV Creation & Upload | 10. Object Complete |  | NA | 04.Low |
| FPRE0620 | Enhancement | Model Integration & Export | 10. Object Complete |  | NA | 04.Low |
| FPRE0619 | Enhancement | UiPath OCR - Model Validation | 10. Object Complete |  | NA | 04.Low |
| FPRE0618 | Enhancement | UiPath OCR - Iterative Model Training | 10. Object Complete |  | NA | 04.Low |
| FPRE0617 | Enhancement | UiPath OCR - Classification & Extraction | 10. Object Complete |  | NA | 04.Low |
| FPRE0616 | Enhancement | UiPath OCR - Taxonomy & Digitize | 10. Object Complete |  | NA | 04.Low |
| FPRE0605_IP | Enhancement | H2RA - 13th month bonus & Quarterly Performance Bonus (QPB) bonus accrual pos... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0605_IF | Enhancement | H2RA - 13th month bonus & Quarterly Performance Bonus (QPB) bonus accrual pos... | 10. Object Complete |  | NA | 04.Low |
| FPRE0604_IP | Enhancement | H2RA - Annual Performance Bonus (APB) ER taxes accrual & Quarterly Performanc... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0604_IF | Enhancement | H2RA - Annual Performance Bonus (APB) ER taxes accrual & Quarterly Performanc... | 10. Object Complete |  | NA | 04.Low |
| FPRE0602 | Enhancement | Reclassification of Vendor transactions from Default to Actual within CFIN | 10. Object Complete |  | NA | 03.Medium |
| FPRE0601 | Enhancement | Reclassification of Customer transactions from Default to Actual within CFIN | 10. Object Complete |  | NA | 03.Medium |
| FPRE0574_IP | Enhancement | Margin analysis Dimensions creation | 10. Object Complete |  | NA | 04.Low |
| FPRE0573_IP | Enhancement | Mass Asset Documents Reversal | 10. Object Complete |  | NA | 02.High |
| FPRE0573_IF | Enhancement | Mass Asset Documents Reversal | 10. Object Complete |  | NA | 03.Medium |
| FPRE0572_IP | Enhancement | Mass Asset Capitalization | 10. Object Complete |  | NA | 02.High |
| FPRE0572_IF | Enhancement | Mass Asset Capitalization | 10. Object Complete |  | NA | 03.Medium |
| FPRE0571_IP | Enhancement | DSD Matrix Rules to Update Depreciation Start Date in the Direct Cap Asset Ma... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0571_IF | Enhancement | DSD Matrix Rules to Update Depreciation Start Date in the Direct Cap Asset Ma... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0551 | Enhancement | SKF Actual Driver volume update from actual activity confirmation Automation | 10. Object Complete |  | NA | 03.Medium |
| FPRE0550 | Enhancement | Enhancement to update additive cost in IP based on Idoc of IF cost | 10. Object Complete |  | NA | 03.Medium |
| FPRE0549 | Enhancement | Enhancement to a) update Cost and Production volume in custom table, b) calcu... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0500_IP | Enhancement | Rule for Transaction Price Allocation in BRIM vs SD | 10. Object Complete |  | NA | 03.Medium |
| FPRE0500_IF | Enhancement | Rule for Transaction Price Allocation in BRIM vs SD | 10. Object Complete |  | NA | 03.Medium |
| FPRE0499_IP | Enhancement | Substitution and Validation rule user exit | 10. Object Complete |  | NA | 03.Medium |
| FPRE0499_IF | Enhancement | Substitution and Validation rule user exit | 10. Object Complete |  | NA | 04.Low |
| FPRE0495_IP | Enhancement | Custom Fields in WBS element Master Data | 10. Object Complete |  | NA | 03.Medium |
| FPRE0495_IF | Enhancement | Custom Fields in WBS element Master Data | 10. Object Complete |  | NA | 04.Low |
| FPRE0477 | Enhancement | Rebate for Direct Customer to Rebate of Intransit deferrals for Direct & Dist... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0476 | Enhancement | Accounting for Stock Rotation | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0475 | Enhancement | Accounting for reserves for unissued returns credit note & Rebate Return Accr... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0474 | Enhancement | Accounting for technical return reserve | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0462 | Enhancement | Enhancement to develop automatic creation of payment advice number in the AR ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0430 | Enhancement | Enhancement for automatic creation of MT210 (pre-advice) message for IC settl... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0429_IP | Enhancement | Utility program to look up inactive cost center and derive replacement cost c... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0429_IF | Enhancement | Utility program to look up inactive cost center and derive replacement cost c... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0429_CFIN | Enhancement | Utility program to look up inactive cost center and derive replacement cost c... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0428_IP | Enhancement | Program to replace inactive cost centers in Assets | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0428_IF | Enhancement | Program to replace inactive cost centers in Assets | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0425 | Enhancement | Treasury Funding - Enhancement to support multiple Treasury Funding scenarios... | 10. Object Complete |  | NA | 02.High |
| FPRE0407_IP | Enhancement | Period Close in CFin, IP & IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0407_IF | Enhancement | Period Close in CFin, IP & IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0407_CFIN | Enhancement | Period Close in CFin, IP & IF | 10. Object Complete |  | NA | 03.Medium |
| FPRE0375_IP | Enhancement | GL Interface – IDOC status from IF & IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0375_IF | Enhancement | GL Interface – IDOC status from IF & IP | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0375_CFIN | Enhancement | GL Interface – IDOC status from IF & IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0374_IP | Enhancement | GL Interface- Managing 999+ GL line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0374_IF | Enhancement | GL Interface- Managing 999+ GL line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0374_CFIN | Enhancement | GL Interface- Managing 999+ GL line items | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0373 | Enhancement | GL Interface – Splitting of enriched files and populating staging table | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0372 | Enhancement | GL Interface - Incoming file processing and Simulation | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0360_IP | Enhancement | Reclassify GL Accounts for Balance Carryforwards - IP | 10. Object Complete |  | NA | 04.Low |
| FPRE0360_IF | Enhancement | Reclassify GL Accounts for Balance Carryforwards - IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0328_IP | Enhancement | Validations on Asset updates, transfer and retirement | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0328_IF | Enhancement | Validations on Asset updates, transfer and retirement | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0326_IP | Enhancement | Mass upload tool to asset update, transfer and retire (S4 Fiori functionality... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0326_IF | Enhancement | Mass upload tool to asset update, transfer and retire (S4 Fiori functionality... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0324_IP | Enhancement | Custom Fiori App for Asset update, transfer, scrap, and retire based on Repor... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0324_IF | Enhancement | Custom Fiori App for Asset update, transfer, scrap, and retire based on Repor... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0322_IP | Enhancement | Fiori Dashboard to display/edit pre-paid amortization for PO​ | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0322_IF | Enhancement | Fiori Dashboard to display/edit pre-paid amortization for PO​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0321_IP | Enhancement | Fiori Dashboard to display/edit accruals for PO​ | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0321_IF | Enhancement | Fiori Dashboard to display/edit accruals for PO​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0320_IP | Enhancement | Enhancement to read PO data and create manual accrual object​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0320_IF | Enhancement | Enhancement to read PO data and create manual accrual object​ | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0319_IP | Enhancement | Enhancement for accrual posting notification​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0319_IF | Enhancement | Enhancement for accrual posting notification​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0315_IP | Enhancement | Activation of custom enhancement tab on portfolio bucket for custom fields. | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0315_IF | Enhancement | Activation of custom enhancement tab on portfolio bucket for custom fields. | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0314_IP | Enhancement | Smart numbering for portfolio items. | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0314_IF | Enhancement | Smart numbering for portfolio items. | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0289_IP | Enhancement | Update XREF1, XREF2 and XREF3 fields in subledger line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0289_IF | Enhancement | Update XREF1, XREF2 and XREF3 fields in subledger line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0289_CFIN | Enhancement | Update XREF1, XREF2 and XREF3 fields in subledger line items | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0287_IP | Enhancement | Need to enhance Fiori screen to capture business process and the approver whi... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0287_IF | Enhancement | Need to enhance Fiori screen to capture business process and the approver whi... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0287_CFIN | Enhancement | Need to enhance Fiori screen to capture business process and the approver whi... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0286_IP | Enhancement | Mass upload of the same supporting document as an attachment to multiple JEs | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0286_IF | Enhancement | Mass upload of the same supporting document as an attachment to multiple JEs | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0286_CFIN | Enhancement | Mass upload of the same supporting document as an attachment to multiple JEs | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0285 | Enhancement | Cash App rules engine for matching incoming payments with payment advice | 10. Object Complete |  | NA | 01.Very High |
| FPRE0284 | Enhancement | Mass upload of payment advice | 10. Object Complete |  | NA | 03.Medium |
| FPRE0282 | Enhancement | RPA BOT for collecting and transforming customer payment advice into standard... | 10. Object Complete |  | NA | 04.Low |
| FPRE0240 | Enhancement | Treasury Payment/funding Request - Enhancement to support multiple Treasury P... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0049 | Enhancement | Enhancement - Custom Fields in Manage bank Accounts | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRC1724_IP | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  | NA | 02.High |
| FPRC1724_IF | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  | NA | 03.Medium |
| FPRC1565 | Conversion | Convert active delegate relationships for Timesheet approval | 10. Object Complete |  | NA | 02.High |
| FPRC1493 | Conversion | Conversion of WIP values as per Component structure in S/4 - IP | 10. Object Complete |  | NA | 02.High |
| FPRC1491 | Conversion | Conversion of WIP values as per Component structure in S/4 - Back End IF | 10. Object Complete |  | NA | 02.High |
| FPRC1464_IP | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  | NA | 02.High |
| FPRC1464_IF | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  | NA | 02.High |
| FPRC1442 | Conversion | Conversion of Actual Labor hours for Intel Federal Projects | 10. Object Complete |  | NA | 02.High |
| FPRC1441 | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete |  | NA | 02.High |
| FPRC1212 | Conversion | Project Actuals Conversion including Intel Federal | 10. Object Complete |  | NA | 03.Medium |
| FPRC0908_IP | Conversion | Project Budget Conversion | 10. Object Complete |  | NA | 03.Medium |
| FPRC0908_IF | Conversion | Project Budget Conversion | 10. Object Complete |  | NA | 03.Medium |
| FPRC0196_IP | Conversion | Asset Transaction data conversion | 10. Object Complete | NA → NA | NA | 02.High |
| FPRC0196_IF | Conversion | Asset Transaction data conversion | 10. Object Complete | NA → NA | NA | 02.High |
| FPRC0195_IP | Conversion | Asset Master data conversion | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRC0195_IF | Conversion | Asset Master data conversion | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRC0174_IP | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC → S4 | NA | 02.High |
| FPRC0174_IF | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC → S4 | NA | 03.Medium |
| FPRC0117 | Conversion | Conversion – In House Cash: Current Account creation and Current Account Bala... | 10. Object Complete | ECC → CFIN | NA | 02.High |
| FPRC0116 | Conversion | Conversion – Migration of Existing Bank Guarantees and Intercompany Loans to ... | 10. Object Complete | Quantum → CFIN | NA | 03.Medium |
| FPRC0035_IP | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  → MDG | NA | 03.Medium |
| FPRC0035_IF | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  → MDG | NA | 04.Low |

**Summary**: 17 Reports, 86 Interfaces, 25 Conversions, 219 Enhancements, 1 Forms, 18 Workflows

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for MB-060:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for MB-060:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (366 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 349 | 95.4% |
| 07. FUT Roadblock | 10 | 2.7% |
| 99. Rejected/Cancelled/On Hold | 5 | 1.4% |
| 06. Dev In Progress | 2 | 0.5% |
| **Total** | **366** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 17 |
| Interface (I) | 86 |
| Conversion (C) | 25 |
| Enhancement (E) | 219 |
| Form (F) | 1 |
| Workflow (W) | 18 |
| **Total** | **366** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 5 |
| 02.High | 64 |
| 03.Medium | 201 |
| 04.Low | 93 |
| N/A | 3 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| FPRI1669 | 02.Interface | Import Xeus/Mars volumes from ECA into S4.​ | 07. FUT Roadblock | 03.Medium |
| FPRE1723_IP | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock | 04.Low |
| FPRE1723_IF | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock | 04.Low |
| FPRE1722_IP | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock | 04.Low |
| FPRE1722_IF | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock | 04.Low |
| FPRE1661_IP | 04.Enhancement | WBS transfer tool | 07. FUT Roadblock | 02.High |
| FPRE1661_IF | 04.Enhancement | WBS transfer tool | 07. FUT Roadblock | 03.Medium |
| FPRE1599_IP | 04.Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO line ... | 07. FUT Roadblock | 03.Medium |
| FPRE1599_IF | 04.Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO line ... | 07. FUT Roadblock | 04.Low |
| FPRE0880 | 04.Enhancement | Cash concentration functionality for cross-currency current accounts | 07. FUT Roadblock | 04.Low |
| FPRC1724_IP | 03.Conversion | Creation of output template with consumption data | 06. Dev In Progress | 02.High |
| FPRC1724_IF | 03.Conversion | Creation of output template with consumption data | 06. Dev In Progress | 03.Medium |

### 6.3 NFRs & Design Principles

| Category | Requirement | Target / SLA | Priority |
|----------|-------------|-------------|----------|
| Performance | Month-end batch costing/closing completes within SLA window | < 4 hours end-to-end batch window | High |
| Availability | S/4 HANA finance modules available during business hours | 99.9% (Mon-Fri 06:00-22:00 PST) | High |
| Scalability | Support 2x transaction volume growth over 3-year horizon | Handle 500K+ journal entries/day | Medium |
| Recoverability | RPO/RTO for financial systems meets audit requirements | RPO < 1 hour, RTO < 4 hours | High |
| Data Volume | Support growing data volumes from legacy migration + BAU | 50M+ records in material ledger | Medium |
| Latency | Near-real-time posting for financial transactions | < 5 seconds for online postings | Medium |
| Concurrency | Support concurrent month-end users across time zones | 200+ concurrent finance users | Medium |

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

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>MB-060 — MB-060</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*364 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| FPRW1449 | TPR : Workflow to handle Memo creation and cancellation process | Jul-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW1444 | TFR: Workflow to handle Memo creation and cancellation process | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Oct-25 (100%) | 1. On Track |
| FPRW1064_IP | Custom Workflow will also be created with some predefined process/rules for approval/rejection. | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 1. On Track |
| FPRW1064_IF | Custom Workflow will also be created with some predefined process/rules for approval/rejection. | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 1. On Track |
| FPRW0930 | Workflow for Counterparty Approval | Apr-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | 5. Not Dispositioned |
| FPRW0906_IP | Custom workflow: Change Order Create and Change Approval | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 1. On Track |
| FPRW0906_IF | Custom workflow: Change Order Create and Change Approval | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 1. On Track |
| FPRW0904_IP | Custom Workflow - WBS Element Request approval with WBS Element creation | Mar-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW0904_IF | Custom Workflow - WBS Element Request approval with WBS Element creation | Mar-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW0900_IP | Custom Workflow: Approval for Project creation and create a Project def and level n1 after approval using template | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 3. Off Track |
| FPRW0900_IF | Custom Workflow: Approval for Project creation and create a Project def and level n1 after approval using template | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW0445_IP | Project budget approval workflow (Capex)​ | Aug-24 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) | 1. On Track |
| FPRW0445_IF | Project budget approval workflow (Capex)​ | Aug-24 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) | 1. On Track |
| FPRW0325_IP | Custom workflow to manage the approval process in bulk/individual requests | Jul-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Mar-25 (100%) |  |
| FPRW0325_IF | Custom workflow to manage the approval process in bulk/individual requests | Jul-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Mar-25 (100%) |  |
| FPRW0165_IP | Workflow is required to trigger the approvers based on the business requirement for Journal entry | May-24 (100%) | Aug-24 (100%) | Aug-24 (100%) | Sep-24 (100%) |  |
| FPRW0165_IF | Workflow is required to trigger the approvers based on the business requirement for Journal entry | May-24 (100%) | Aug-24 (100%) | Aug-24 (100%) | Sep-24 (100%) |  |
| FPRW0165_CFIN | Workflow is required to trigger the approvers based on the business requirement for Journal entry | May-24 (100%) | Aug-24 (100%) | Aug-24 (100%) | Sep-24 (100%) |  |
| FPRR1514_IP | To generate reports out of the ITT documents that was created | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| FPRR1514_IF | To generate reports out of the ITT documents that was created | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| FPRR1240 | Custom report for Revenue Recognition by Stage for Product/Services Sale​ actual revenue vs planned revenue | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 4. Completed |
| FPRR1211 | Report for searching on and viewing government contract timesheets for Intel Federal. | Apr-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 1. On Track |
| FPRR1210 | Report for searching on and viewing government contract timesheet changes for Intel Federal.​ | Apr-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 4. Completed |
| FPRR0907_IP | Workflow Status Report ( Order Request / Approval Request / Others ) | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) | 2. At Risk |
| FPRR0907_IF | Workflow Status Report ( Order Request / Approval Request / Others ) | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) | 1. On Track |
| FPRR0497 | CFR - Report to support multiple Treasury Funding requests from Multiple Intel teams | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) | 1. On Track |
| FPRR0496 | TPR-Report to support multiple Treasury Payment Requests from Multiple Intel teams | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRR0461 | Inter-company Outage Pre-consolidate Report (ACDOCA) | Aug-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Mar-25 (100%) |  |
| FPRR0380 | GL Interface – Reconciliation Report/Dashboard | Aug-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Sep-25 (100%) |  |
| FPRR0327_IP | Report to display the requests/change IDs and status of the workflow approval and Error handling | Jul-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Mar-25 (100%) | 1. On Track |

*... and 334 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

**Mapped sub-tower(s):** 3.1 FPR - GL Close & Consolidate, 3.10 FPR - Accounts Receivable & Collections, 3.11 FPR - Project Accounting, 3.2 FPR - Tax, 3.3 FPR - Revenue Recognition & Reporting, 3.4 FPR - Intercompany, 3.5 FPR - Fixed Assets, 3.6 FPR - Cost and Profitability Analysis, 3.7 FPR - Product Costing and Inventory Valuation, 3.8 FPR - Financial Planning & Analysis, 3.9 FPR - Treasury and Cash Management

**RAID Summary:** 18 open items (6 capability-specific, 12 tower-level), 234 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 1 | 1 |
| P2 - Medium | 4 | 10 | 14 |
| P3 - Low | 2 | 1 | 3 |
| **Total** | **6** | **12** | **18** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03633 | Action | P2 - Medium | Conversion RICEFW (FPRC1724_IF/IP) has dependency on the enh... | In Progress | FPR | 2026-03-13 |
| 02226 | Action | P3 - Low | DMEE related FPR objects not ready for development | In Progress | FPR | 2026-03-31 |
| 03729 | Action | P2 - Medium | AN and CC invoices are fetching wrong tax codes and posting ... | In Progress | FPR | 2026-03-23 |
| 02680 | Action | P2 - Medium | T042A table config in IP and IF | In Progress | FPR | 2026-04-03 |
| 03782 | Risk | P2 - Medium | Auto processing of JPMC lockbox BAI2 for AR Cashapp not work... | Not Started | FPR | 2026-04-10 |
| 03473 | Action | P3 - Low | Manual Service PIR creation for IP-IF Service Procurement. | In Progress | FPR | 2026-05-29 |

**Other FPR Tower RAID Items** (12 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03197 | Issue | P2 - Medium | Company Code address disappearing in DI0 250 | Not Started |  |  |
| 03564 | Risk | P2 - Medium | Development of the AMT impacting FPR Capital Tool report | In Progress | FTS IP | 2026-03-27 |
| 03624 | Issue | P2 - Medium | Test Data not provided for CR "INT-Build-CR0918" | In Progress | FPR | 2026-03-20 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03628 | Risk | P2 - Medium | R3 Returns Rework Process Causing Finance Double Counting in... | In Progress | E2E | 2026-03-27 |
| 03629 | Risk | P2 - Medium | Consensus Demand Data for ICOST | In Progress | FTS IP | 2026-03-27 |
| 02799 | Risk | P2 - Medium | Deloite FPR objects FPRXV490, FPRXV038 and FPRXV048 are dela... | In Progress | FPR | 2026-03-25 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03740 | Action | P2 - Medium | Provide count of report with list of names due in ITC1 and I... | In Progress | FPR | 2026-03-20 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03333 |  | P3 - Low | FPR NRT : IF and IP  Power BI Workspace Provisioning | In Progress | Analytics (Reporting) | 2026-01-12 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*MB-060 — Architecture Document (TOGAF BDAT) · Finance Plan To Report · Generated: March 2026*

