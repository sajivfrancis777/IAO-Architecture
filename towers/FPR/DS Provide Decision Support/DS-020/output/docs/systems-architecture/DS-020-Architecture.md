<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">DS-020 — Perform Product Costing and Inventory Valuation</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Finance Plan To Report (FPR) Tower<br/>
  Capability DS-020 · DS Provide Decision Support</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
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
   - 5.1 [Current-State Application Landscape](#51-icost--current-state-application-landscape)
   - 5.2 [Future-State Application Landscape](#52-s/4-hana--future-state-application-landscape)
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **DS-020 Perform Product Costing and Inventory Valuation** within the IAO program. It includes 15 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Finance Plan To Report (FPR) |
| **Process Group** | DS Provide Decision Support |
| **Capability** | DS-020 - Perform Product Costing and Inventory Valuation |
| **Release** | Release 3 |
| **Total Systems** | 60 |
| **System Status** | 46 Deployed, 8 Developing, 4 EOL, 2 Pending IAPM |
| **RICEFW Objects** | 10 Interfaces, 2 Conversions, 15 Enhancements |
**Change Summary**: 22 new flow chains, 27 removed, 0 modified, 0 unchanged between ICOST and S/4 HANA states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Finance Plan To Report |
| **L1 Process** | DS Provide Decision Support |
| **L2 Capability** | DS-020 - Perform Product Costing and Inventory Valuation |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | S/4 HANA Finance Consolidation | Migrate legacy costing and reporting platforms to unified S/4 HANA finance backbone | IDM 2.0 Core Finance Transformation | High |
| 2 | Real-Time Financial Visibility | Enable real-time cost reporting and variance analysis replacing batch-driven legacy processes | CFO Digital Finance Initiative | High |
| 3 | Regulatory Compliance Readiness | Ensure SOX compliance and audit trail continuity through the ERP transition period | Intel Corporate Compliance | Medium |
| 4 | DS-020 Process Migration | Migrate Perform Product Costing and Inventory Valuation business processes and 42 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Finance | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Month-End Close Cycle Time | < 3 business days | Calendar days from period close trigger to final posting | 5 business days (legacy) | Finance Controller |
| Cost Variance Accuracy | < 0.5% deviation | Variance between standard and actual cost post-migration | 1.2% (ICOST baseline) | Cost Accounting Lead |
| System Availability (Finance) | 99.9% uptime | S/4 HANA finance module availability during business hours | 99.5% (legacy) | IT Operations |
| DS-020 Migration Completeness | 100% flow chains validated | All 22 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **15 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for DS-020 Perform Product Costing and Inventory Valuation.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | DS-020-020 | Perform Cumulative Costing Run | Cost Analyst | 10 | 3 |
| 2 | DS-020-030 | Analyze and Review Cost Estimates for Accuracy | Cost Accountant | 7 | 7 |
| 3 | DS-020-040 | Release Cost Estimates | Cost Accountant | 8 | 2 |
| 4 | DS-020-050 | Perform Off-Cycle, Unplanned Costing Run | Cost Accountant | 9 | 4 |
| 5 | DS-020-060 | Analyze Material Ledger | Cost Accountant | 4 | 4 |
| 6 | DS-020-080 | Verify Standard Cost | Cost Accountant | 10 | 10 |
| 7 | DS-020-090 | Review Production Orders | Cost Accountant | 7 | 9 |
| 8 | DS-020-100 | Actual Costing | Cost Accountant | 8 | 0 |
| 9 | DS-020-110 | Material Ledger Reports | Cost Accountant | 3 | 4 |
| 10 | DS-020-120 | Calculate and apply overhead for all MFG orders | Cost Accountant | 6 | 2 |
| 11 | DS-020-130 | Calculate WIP | Cost Accountant | 4 | 4 |
| 12 | DS-020-140 | Calculate Variances | Cost Accountant | 10 | 11 |
| 13 | DS-020-150 | Generate Variances Report | Cost Accountant | 12 | 11 |
| 14 | DS-020-160 | Execute Order Settlement | Cost Accountant | 4 | 3 |
| 15 | DS-020-170 | Product Costing Reports | TBD | 7 | 0 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 DS-020-020 — Perform Cumulative Costing Run

**Swim Lanes**: Cost Analyst | **Tasks**: 10 | **Gateways**: 3

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
    subgraph Cost Analyst
        n1["fa:fa-user Check Material Master Data"]
        n2["fa:fa-user Check Production Version Then Explore Bill of Materials (BOM) and Routing"]
        n3["fa:fa-user Calculate the Standard Price Based on BOM and Routing"]
        n4["fa:fa-user Calculate Standard Price Based on PIR or Planned Price of Material Master"]
        n5["fa:fa-user Update Standard Price Based on PIR or Planned Price of Material Master"]
        n6["fa:fa-user Update the Standard Price Based on BOM and Routing"]
        n7["fa:fa-user Check for Existing Cost Estimate for the Period"]
        n8["fa:fa-user Reset the Existing Cost Estimates for the Period"]
        n9[["fa:fa-cog Calculate Moving Average Price for the Material"]]
        n10[["fa:fa-cog Update Moving Average Price for the Material"]]
        n11(["fa:fa-play Perform Cumulative Costing Run Initiated"])
        n12(["fa:fa-stop Perform Cumulative Costing Run Completed"])
        n13{{"fa:fa-code-branch Is Price Control = S ?"}}
        n14{{"fa:fa-code-branch Is Procurement Type = E?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n11 --> n1
    n1 --> n13
    n13 -->|"Yes"| n7
    n13 -->|"No"| n9
    n14 -->|"No"| n4
    n14 -->|"Yes"| n2
    n2 --> n3
    n4 --> n5
    n3 --> n6
    n15 --> n12
    n5 --> n15
    n6 --> n15
    n9 --> n10
    n8 --> n14
    n7 --> n8
    n10 --> n15
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 startEvt
    class n12 endEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtVm2P4jYQ_itWTivupCDllbCR2goCqVa6bVfL3lXV0Q8mcSBax0a2w0I5_nvHJAHChat0bT5A5vHM88xMEo_3RsJTYoTG3d0-Z7kK0b6nVqQgvRD1FliSnokq4DMWOV5QInvaJ-NMzfK_j262t95qN43FuMjpTqMzsuQEfXow0QgCqYkkZrIvicizntlbi7zAYhdxyoX2fkeGmZUd1eqlMRcpEWcHywrsxIdQmjNyht3AC7xYx0mScJa2SDM_G2ZJ76CTo_wtWWGhjumXkjzi7R95qlZgZ5hKAj4rVdCPeEGorlGJUmNJKTZNM3KpdRg0bLbGSc6WgHsWQAKz1zPkW4cDOtzdzdlJFL1M5gzBlVAs5YRkSCqApxuFspzS8J0XjWLfMqUS_JWE75xpMHEdM9GVhFC6Zerm9t9IvlypcMFpWrv233QNobPemmIbOpYpdvB7pUVYelaKBs7QGZ6UxoEd2VGjlGXZf1KCvooXLF9rrakbO_HkpGX7Az-yvuVrypx4wci-7hMRmzwhF6RxHLvTc6umA9-2bpOOY3dgRVekS6zIG96dCe8j70QY-0FsBzcJK73rLMvFk-BJQ-hO_dg_EQZjOx45Nwm9ke0N6wyBZynweoUiLhUaMUx3UlVL-mL2l7mR4TDDfd1pFK1I8ooeoRr9icGNhDs0wQrPjb8uwpyuMEg4LROVc4Y-EyH1_8uKMDTdriEvgsZQC-LZiV6i9-PfHz8gzFL0zEsFL3tbxb1SwTQpKQQj2D_QTGH9caYgC48TjWFrSRFIAuVtRu8W4y22p4dnxAV6opgx0qxe1FC3qK3it1U-rdP_XWLQKfHDfQm6nmcGWU23udTu1fszhftCC-klLfYEGfK0zTVscz0TSdTRuZtLfpfs_suJLeHLiwf2yDeaarQhAi9JXWzD1LQOuC7JbKvNVnfth6js9yeqNYUvH5KHkAJFZaETzDfkWKYmfi4ZeoBRmAOVLu_DJY9z5pGKr_-NJ-LFmpIOHne_P5eWkv4CRkiyQg-yrieCTVhwin5CM_TL3DgcLoO97wRzGFgwrRmMnN2aQPz0m3C_O5xsE1pKqODXanc8h8H8qG6gj6jf_xn-G7s23cZ2NfB1bvxJ5Nz4Cm_q9cJv_IjfN7jXxr1rvCFy6gWnUmwEvcr0a9OtzEHD4tf5NdGN3fgPruz72q73dzas7SatoLKHDb_Vjj_OA92VZg62YKcbdrthrxv2u-FBNxx0w8Nu-P5y2rYrsm4v2aezTBt36nNHG3Wb4duGvW7Yb2DDNAoiCpynRrg3jgdSOLSmJMMlVcbBNHCp-GzHEiM8HtyM8rhZTHIM87SowMM_2fl10w==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 DS-020-030 — Analyze and Review Cost Estimates for Accuracy

**Swim Lanes**: Cost Accountant | **Tasks**: 7 | **Gateways**: 7

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
        n1["fa:fa-user Check the Procurement Type Material Master"]
        n2["fa:fa-user Check the BOM"]
        n3["fa:fa-user Check the Activity Prices for Routing Activities"]
        n4["fa:fa-user Check the PIR in Material Master"]
        n5["fa:fa-user Check the Standard Price of the Sending Plant"]
        n6["fa:fa-user Check the Price Calculation as per the Valuation Variant"]
        n7["fa:fa-user Validate the Standard Price of the Material"]
        n8(["fa:fa-play Analyze and Review Cost Estimates for Accuracy Initiated"])
        n9(["fa:fa-stop Activity Prices for Routing Components Completed"])
        n10["Perform Off-Cycle, Unplanned Costing Run"]
        n11{{"fa:fa-code-branch Is Procurement Type Inhouse Production?"}}
        n12{{"fa:fa-code-branch Check the Special Procurement Key Status?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n15{{"fa:fa-code-branch Discrepancies Found?"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n11
    n8 --> n13
    n11 -->|"Yes"| n17
    n11 -->|"No"| n12
    n13 --> n1
    n17 --> n3
    n12 -->|"STO"| n5
    n3 --> n14
    n4 --> n13
    n14 --> n7
    n5 --> n16
    n6 --> n16
    n7 --> n15
    n15 -->|"No"| n9
    n16 --> n14
    n15 -->|"Yes"| n10
    n17 --> n2
    n2 --> n13
    n12 -->|"Sub Contracting"| n4
    n12 -->|"No Special Procurement Key"| n6
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 startEvt
    class n9 endEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVltv4jgU_itWRhW7Eki5EpqHXdFAVtVOp1XpzGq17INJnGLV2JHtQBmG_77HkHAJoQ-zPKD4O-d85-JzbG-sVGTEiqybmw3lVEdo09FzsiCdCHVmWJFOF-2Bb1hSPGNEdYxOLrie0O87Nccv3o2awRK8oGxt0Al5FQR9ve-iIRiyLlKYq54ikuadbqeQdIHlOhZMSKP9iQxyO995q0R3QmZEHhVsO3TSAEwZ5eQIe6Ef-omxUyQVPDsjzYN8kKedrQmOiVU6x1Lvwi8VecDvf9FMz2GdY6YI6Mz1gn3GM8JMjlqWBktLuayLQZXxw6FgkwKnlL8C7tsASczfjlBgb7doe3Mz5Qen6GU05Qh-KcNKjUiOlAZ4vNQop4xFn_x4mAR2V2kp3kj0yR2HI8_tpiaTCFK3u6a4vRWhr3MdzQTLKtXeyuQQucV7V75Hrt2Va_hv-CI8O3qK--7AHRw83YVO7MS1pzzP_5cnqKt8weqt8jX2EjcZHXw5QT-I7Uu-Os2RHw6dZp2IXNKUnJAmSeKNj6Ua9wPHvk56l3h9O26QvmJNVnh9JLyN_QNhEoSJE14l3PtrRlnOnqRIa0JvHCTBgTC8c5Khe5XQHzr-oIoQeF4lLuYoFkqjYZqKkmvM9V5qftz5Z2rlOMpxzxQbxXOSviGYUGQCKCVMKod2WxcEPUCWZvTgQ8HX1Pr3hMa9RnP3-HCu6V3THKaaLqleg2fYIYVyIdGzKDVMQS2jRJ2T-Vejv39GlH8cc3DNeAI1gsnP9pEgke9R6HsTyxMzFTxj6l8voiGIMUtLhjUVHGGFClAxwm-YlXtwdxg2ScNzUtCmGaTzQYR1tuc8g18ORAWDLh1yzNbfCQIG9EyWlKz27TFWGk5KXVUemqWUOF2jezjGKcAZsP56Qnt7pFVaFB9uXywWheDQSWr3ycglnWMD3RORYLZAj3nei9cpgxPzK4egOSfZLkhD9lzy8wQdZ7OpQzHXT28GB2g6R_fqsonv-VxAOY0gK1NT_N-n1nZ7yua2s520R0FS01On5H-StdkUXaoLPq-dj7ynrFR0Sf7Ynx5NM__nzIJ2sxFVqSQFfMMMoQTOgewi0P7PeQyPZlhKsVI9zDQqsMSMEXZhBFO0_-AO6vV-M9tXrQfV2qvlO4UfU-tvM_Y_jKum5IvYC9xa4FUc9Trcrw-UbmU4eXncWQaVoLbzq7XfjKUC6giCSt6v1v3GuvLr1PxOcB7xbY33G44Pioek7UYuda5uM8RDbuUMhoVrGF8zMDsWv6n0RVzr451-_-RGMjtV38RnsNsOe-2w3w4H7XC_HQ7b4cHhAXQG31ZvlfNk7HZlaKrqIj-H3XbYa4f9djhoh_vtcFjDVtdaELnANLOijbV7OMPjOiM5Lpm2tl0Ll1pM1jy1ot0D0yoLc0eMKIZ7f7EHt_8BioqrBQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 DS-020-040 — Release Cost Estimates

**Swim Lanes**: Cost Accountant | **Tasks**: 8 | **Gateways**: 2

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
        n1["fa:fa-user Create a Costing Run"]
        n2["fa:fa-user Select Materials for Costing"]
        n3["fa:fa-user Execute Costing"]
        n4["fa:fa-user Analyze the Costs Calculated"]
        n5["fa:fa-user Mark the Cost Estimate"]
        n6["fa:fa-user Release the Cost Estimate"]
        n7["fa:fa-user Check the Price in Material Master"]
        n8["fa:fa-user Make Required Corrections"]
        n9(["fa:fa-play Release Cost Estimates Initiated"])
        n10(["fa:fa-stop Cost Estimates Released"])
        n11{{"fa:fa-code-branch exclusiveGateway"}}
        n12{{"fa:fa-code-branch Discrepancies Found?"}}
    end
    n9 --> n1
    n3 --> n4
    n6 --> n7
    n1 --> n2
    n5 --> n6
    n2 --> n11
    n11 --> n3
    n4 --> n12
    n12 -->|"No"| n5
    n8 --> n11
    n7 --> n10
    n12 -->|"Yes"| n8
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 startEvt
    class n10 endEvt
    class n11 gateway
    class n12 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2P4jYU_StWRiNaKUj5JJk8tGICqVbqrFbLtlVV-mAcByyMQ21nBpblv_fmE5LNqA_NA_I9ueec64tzk4tB8pQakfH4eGGC6QhdJnpHD3QSockGKzoxUQ38jiXDG07VpMzJcqFX7GuVZnvHU5lWYgk-MH4u0RXd5hT99sFEcyByEyks1FRRybKJOTlKdsDyHOc8l2X2Aw0zK6vcmlvPuUypvCVYVmATH6icCXqD3cALvKTkKUpykfZEMz8LMzK5lsXx_I3ssNRV-YWiL_j0B0v1DuIMc0UhZ6cP_Fe8obzco5ZFiZFCvrbNYKr0EdCw1RETJraAexZAEov9DfKt6xVdHx_XojNFXxZrgeAiHCu1oBlSGuDlq0YZ4zx68OJ54lum0jLf0-jBWQYL1zFJuZMItm6ZZXOnb5Rtdzra5DxtUqdv5R4i53gy5SlyLFOe4XfgRUV6c4pnTuiEndNzYMd23DplWfa_nKCv8gtW-8Zr6SZOsui8bH_mx9b3eu02F14wt4d9ovKVEXonmiSJu7y1ajnzbet90efEnVnxQHSLNX3D55vgU-x1gokfJHbwrmDtN6yy2HySOWkF3aWf-J1g8Gwnc-ddQW9ue2FTIehsJT7uUJwrjeaE5IXQWOj6bnkJ-6-1keEow9Oy2SiWFDaDcMWA84c-F2Jt_H1HcPqEFeWUaPQCrPK5VCjLZUvuE90-cXmipACr0VyvnzsXmJ-_UgSTo8pXKMacFBxM0z7R7xNfsNx3LLQEpwNw-pRZn_IZNgSD6r9YwaBvO0pqp08SzhdiomsJLBSs-vRwWOeegvM_BZM0BVspoaksF6rPevqhox05HLi21l6dCn2Aycua3vx4_19bN77S-XHIa-S-o9mXS0srx_t0AwOK7BA9EV4o9kp_qc__2rhe72nOOG3BFJH0CGsGngkcyfTnGxWGS70QT2g6_QlkmtCtQ68JZ3UYNKFdh04T-nU4a0KnkWq17CbdbWKvud_S7YrwbW18zNfGN5Br8HCgEzSxNeT9SVVFDO8e7LLIdqD1YGccdsdhbxz2x-HZOByMw-E4_NS9XvrbsZpXQR-123nYh50WNkzjQOUBs9SILkb1MQAfDCnNcMG1cTUNXOh8dRbEiKqXplEcU2AuGIZZdqjB67-mKKZ0" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 DS-020-050 — Perform Off-Cycle, Unplanned Costing Run

**Swim Lanes**: Cost Accountant | **Tasks**: 9 | **Gateways**: 4

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
        n1["fa:fa-user Validate the Costing Related Master Data"]
        n2["fa:fa-user Create Cost Estimate"]
        n3["fa:fa-user Make Required Corrections"]
        n4["fa:fa-user Mark the Cost Estimate"]
        n5["fa:fa-user Release the Cost Estimate"]
        n6["fa:fa-user Check the Price in Material Master"]
        n7["fa:fa-user Make Required Corrections"]
        n8["fa:fa-user Execute Costing Run"]
        n9["fa:fa-user Validate Cost"]
        n10(["fa:fa-play Off-Cycle, Unplanned Costing Run Initiated"])
        n11(["fa:fa-stop Off-Cycle, Unplanned Costing Run Completed"])
        n12{{"fa:fa-code-branch Discrepancies Found?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch Discrepancies Found?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n1 --> n12
    n10 --> n13
    n13 --> n1
    n3 --> n13
    n4 --> n5
    n5 --> n6
    n12 -->|"No"| n2
    n8 --> n9
    n2 --> n15
    n15 --> n8
    n7 --> n15
    n9 --> n14
    n14 -->|"No"| n4
    n6 --> n11
    n12 -->|"Yes"| n3
    n14 -->|"Yes"| n7
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2P4jYU_StWRiNaKUj5JJCHVkwg1Uqd7aqzu1VV-mAcByyMQ21nBsry33tNEiBp0KrbPCDu8T3n-N4k1zlapMioFVuPj0cmmI7RcaDXdEsHMRossaIDG1XAZywZXnKqBiYnL4R-YX-f09xgtzdpBkvxlvGDQV_oqqDo0zsbTYHIbaSwUENFJcsH9mAn2RbLQ1LwQprsBzrOnfzsVi89FTKj8prgOJFLQqByJugV9qMgClLDU5QUImuJ5mE-zsngZDbHizeyxlKft18q-oz3v7FMryHOMVcUctZ6y3_GS8pNjVqWBiOlfG2awZTxEdCwlx0mTKwADxyAJBabKxQ6pxM6PT4uxMUUfZwtBIKLcKzUjOZIaYDnrxrljPP4IUimaejYSstiQ-MHbx7NfM8mppIYSnds09zhG2WrtY6XBc_q1OGbqSH2dntb7mPPseUBfjteVGRXp2Tkjb3xxekpchM3aZzyPP9fTtBX-RGrTe0191MvnV283HAUJs6_9ZoyZ0E0dbt9ovKVEXojmqapP7-2aj4KXee-6FPqj5ykI7rCmr7hw1VwkgQXwTSMUje6K1j5dXdZLj_IgjSC_jxMw4tg9OSmU--uYDB1g3G9Q9BZSbxbo6RQGk0JKUqhsdDVqrmE-8fCynGc46FpNvqMOcugHAQv6ZkFzyD6lXKAMvSMlYacGdZ4Yf15I-K1RRJJjcTZdA4SW4jaBL9NeMYbCi5_lUyCTVJISYlmhVBtVtBlyc1ln3eMwjYFKqEwhb7GGnXqWVNSOX2Q8PAgJsAbOgFzqO5Jmx59U3XjNmu-p6TUNzehFO38yZ07ZwjtTNf57pK74_Cg_pLnw-RAOEykTwIQIc4buxihdzC7mbnnIPT9rZJ7VVK62H1dKSm2O057lLzjsVEyZ8ZwCVOPrNGMKSLpDv4zqlAKD2z248I6nW6pfj-V7gkvFXulP1XvY5cWfLtj-F8dYUZWf4SLhsMfTL1N7NSA3wB-DdSx31kPqjisw7AKRw3bM_GXhfW-WFhf4FWs8XGVNqlDrxZtVNxaZlzHUWd9UsdBkx-0bRp8VOe53e38TtU50e8KNAvRzcwzXWpmfQv2-mG_Hw764bAfHvXDUT887ocn_TDc5OZEbuNufXq2Ua85Qtqw3w8H_XDYwJZtbancYpZZ8dE6f23BF1lGc1xybZ1sC5e6eDkIYsXnrxKr3JnBMWMYDottBZ7-AVDaE0I=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 DS-020-060 — Analyze Material Ledger

**Swim Lanes**: Cost Accountant | **Tasks**: 4 | **Gateways**: 4

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
        n1["fa:fa-user Review Standard Price of the Material for the Period"]
        n2["fa:fa-user Review Material Movements"]
        n3["fa:fa-user Review Variances"]
        n4["fa:fa-user Review Actual Cost of the Material"]
        n5(["fa:fa-play Material Ledger Analysis Initiated"])
        n6(["fa:fa-stop Material Ledger Analysis Completed"])
        n7["Analyze and Review Cost Estimates for Accuracy"]
        n8["Review Production Orders"]
        n9["Calculate Variances"]
        n10["Actual Costing"]
        n11{{"fa:fa-code-branch Review Successful?"}}
        n12{{"fa:fa-code-branch Review Successful?"}}
        n13{{"fa:fa-code-branch Review Successful?"}}
        n14{{"fa:fa-code-branch Review Successful?"}}
    end
    n5 --> n1
    n1 --> n11
    n11 -->|"Yes"| n2
    n12 -->|"Yes"| n3
    n2 --> n12
    n13 -->|"Yes"| n4
    n3 --> n13
    n4 --> n14
    n14 -->|"Yes"| n6
    n11 -->|"No"| n7
    n12 -->|"No"| n8
    n13 -->|"No"| n9
    n14 -->|"No"| n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 startEvt
    class n6 endEvt
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2P4jYU_StWRiNaKUj5JEweWjGBSCvttKOyu1VV-mAcB6IxNrIdGJblv_c6JAGy4aHbPCB8fM65H4lvcrSIyKgVW4-Px4IXOkbHgV7TDR3EaLDEig5sdAa-YFngJaNqYDi54HpefK1obrB9NzSDpXhTsINB53QlKPr8wUYTEDIbKczVUFFZ5AN7sJXFBstDIpiQhv1Ax7mTV9HqrWchMyovBMeJXBKClBWcXmA_CqIgNTpFieDZjWke5uOcDE4mOSb2ZI2lrtIvFX3B738WmV7DOsdMUeCs9YZ9xEvKTI1algYjpdw1zSiUicOhYfMtJgVfAR44AEnM3y5Q6JxO6PT4uOBtUPRpuuAILsKwUlOaI6UBnu00ygvG4ocgmaShYystxRuNH7xZNPU9m5hKYijdsU1zh3tarNY6XgqW1dTh3tQQe9t3W77HnmPLA_x2YlGeXSIlI2_sjdtIz5GbuEkTKc_z_xUJ-io_YfVWx5r5qZdO21huOAoT53u_psxpEE3cbp-o3BWEXpmmaerPLq2ajULXuW_6nPojJ-mYrrCme3y4GD4lQWuYhlHqRncNz_G6WZbLVylIY-jPwjRsDaNnN514dw2DiRuM6wzBZyXxdo0SoTSaECJKrjHX511zcffvhZXjOMdD02z0B90VdI_mwIJnP0OvErqFRI7g0KIXqNMcPpQLWQGvsBTZwvrnytDrNWylL2IHp59rdavye1XVkOCEdshBL3lCdAkBqlI7Cd_Kw59a_ZbBbWtz-0izFfhNOGYHOJ3oA0ywAjZNhT9fGYwuBkqL7X2DRGy2jH5vEIG-In2lCBrdVFClPlMaBpamquoy3LNSYnK4rWAM-loDz0lWEl0Ijn43E67TqidgJpiRkoHlvX66jsnn0j6YOx2Cezw2FZsBP1zCiCLr9mkpCXiqvGS_LqzT6Vro_ajQ_1Fh8N-FMNDOf3iIhsNfwKReuvWyXVfAt4X1l2nhN3jYmw2vs-HXG17t0BL9DjGoN_ya2AiDet3su0FHOOrm9Juo8KibUo2PuxnU-FM3QI2710PJtKIZxjew1w_7_XDQD4ft6-sGHtVvmhsw6ueO--Gnfth17uBuM8tvYa8f9vvhoIEt29pQucFFZsVHq_rsgU-jjOa4ZNo62RYutZgfOLHi6vPAKrcZKKcFhqm9OYOnfwHJ0fMF" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 DS-020-080 — Verify Standard Cost

**Swim Lanes**: Cost Accountant | **Tasks**: 10 | **Gateways**: 10

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
        n1["fa:fa-user Check the Material Price"]
        n2["fa:fa-user Verify the Cost Planning"]
        n3["fa:fa-user Make Required Corrections to Cost Planning"]
        n4["fa:fa-user Verify the Activity Planning"]
        n5["fa:fa-user Verify the SKF Planning"]
        n6["fa:fa-user Validate Cost Split"]
        n7["fa:fa-user Validate the Plan Rates"]
        n8["fa:fa-user Verify Standard Cost"]
        n9["fa:fa-user Make Required Corrections to Activity Planning"]
        n10["fa:fa-user Make Required Corrections to SKF Planning"]
        n11(["fa:fa-play Cost Run Creation Initiated"])
        n12(["fa:fa-stop Standard Prices Updated in Material Master"])
        n13{{"fa:fa-code-branch Discrepancies Found?"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n15{{"fa:fa-code-branch Discrepancies Found?"}}
        n16{{"fa:fa-code-branch Discrepancies Found?"}}
        n17{{"fa:fa-code-branch Discrepancies Found?"}}
        n18{{"fa:fa-code-branch Discrepancies Found?"}}
        n19{{"fa:fa-code-branch Discrepancies Found?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n1 --> n14
    n2 --> n13
    n14 --> n2
    n11 --> n22
    n3 --> n14
    n4 --> n15
    n13 -->|"No"| n20
    n13 -->|"Yes"| n3
    n5 --> n16
    n15 -->|"No"| n21
    n6 --> n17
    n7 --> n18
    n8 --> n19
    n19 -->|"No"| n12
    n20 --> n4
    n9 --> n20
    n21 --> n5
    n10 --> n21
    n16 -->|"Yes"| n10
    n15 -->|"Yes"| n9
    n17 -->|"Yes"| n14
    n18 -->|"Yes"| n14
    n22 --> n1
    n17 -->|"No"| n7
    n18 -->|"No"| n8
    n16 -->|"No"| n6
    n19 -->|"Yes"| n22
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
    class n11 startEvt
    class n12 endEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV12P4jYU_StWViNaKUix80keWjGBVKvuVKNhd6uq9MEkzmBNcKjtzAxl-e-1QwyTNLQaygPCx_ecc--NHZu9lVU5sWLr5mZPGZUx2I_kmmzIKAajFRZkZIMj8BVzilclESMdU1RMLuhfTRj0tq86TGMp3tByp9EFeawI-PLRBlNFLG0gMBNjQTgtRvZoy-kG811SlRXX0R9IVDhF49ZO3VY8J_wc4DghzHxFLSkjZ9gNvdBLNU-QrGJ5R7Twi6jIRgedXFm9ZGvMZZN-Lcgdfv2V5nKtxgUuBVExa7kpP-EVKXWNktcay2r-bJpBhfZhqmGLLc4oe1S45yiIY_Z0hnzncACHm5slO5mCz7MlA-qTlViIGSmAkAqeP0tQ0LKMP3jJNPUdW0hePZH4A5qHMxfZma4kVqU7tm7u-IXQx7WMV1WZt6HjF11DjLavNn-NkWPznfrueRGWn52SAEUoOjndhjCBiXEqiuJ_Oam-8s9YPLVeczdF6ezkBf3AT5x_6pkyZ144hf0-Ef5MM_JGNE1Td35u1TzwoXNZ9DZ1AyfpiT5iSV7w7iw4SbyTYOqHKQwvCh79-lnWq3teZUbQnfupfxIMb2E6RRcFvSn0ojZDpfPI8XYNkkpIMM2yqmYSM3mc1R8Gf19aBY4LPNbNBsmaZE9A7VBwp4rSOw3cc9WwpfXHGxLqkr7qXbhrWI3RfYkZU4u3S3K7pDv8RMAD-bOmnOSKxznJJK2YALL6NxnvovdU8Z-p3F0g-heJi5_TC5ygx8ElzVVfjvkttiWV3fjwQrx20Q7gQY1ElxMN5rVQz0m9ffLGqkuYvKOR_9ET6LxD63KbIPzupLMt1U5o-vNQM5BwgrUA-KhOA6qKzxXz-7dUdKYKWW3PhTfrToAvW93BHFB2XpJ3WKhffSV3vzdK-hQar9R7NFuDGRUZJ1v1myq5VG2B_MeldTi8pXrDVPKalbWgz-Sn4w7v0_zrHYPrqeH11Oh66uRqKnKu6i6C19HQe2nqPDv-YBCMxz_o5dCOUTt2zbx3BJAZtwRkALcn0MZD3xCagG9L65dqaX3TrelP_KZfD2rGWPqtQmAC_Z5Ce8KxoA0M23HYjqN2HLXjiRGadIWgqQE5x0hTw6St0aSK2qJPNbXxp0xg0KsFOv3kzcwpmbBPMe4wujSDzNPpa7QFhX2FFo_6abZ40G-McTRPtzme9SIx15IOjIZhdxj2hmF_GA6G4XAYjobhyTCsHt8wDk-Xyi6O2gtgF3XNLagLe8OwPwwHw3A4DEfD8GQQVqt6EIbDMDKwZVsbwjeY5la8t5q_LurvTU4KXJfSOtgWrmW12LHMipsrvlU359WMYnXz2hzBw98_VBcQ" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 DS-020-090 — Review Production Orders

**Swim Lanes**: Cost Accountant | **Tasks**: 7 | **Gateways**: 9

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
        n1["fa:fa-user Display Cost Analysis of Production Order"]
        n2["fa:fa-user Display Production Order"]
        n3["fa:fa-user Review Planned Cost and Planned Quantity"]
        n4["fa:fa-user Review Actual Qty and Cost for Actual Quantity"]
        n5["fa:fa-user Review Activity Costs for the Order"]
        n6["fa:fa-user Review the Documented Goods Movements"]
        n7["fa:fa-user Review the Production Order Status"]
        n8(["fa:fa-play Production Orders Review is Initiated"])
        n9(["fa:fa-stop Production Orders Review Completed"])
        n10["Execute Production Operations (IF)"]
        n11["Execute Production Operations (IP)"]
        n12["Execute Production Operations (IF)"]
        n13["Execute Production Operations (IP)"]
        n14["Calculate and apply overhead for all MFG orders"]
        n15["Process Goods Receipt from Production (IF)"]
        n16["Process Goods Receipt from Production (IP)"]
        n17["Confirm Completion of Production Operation Order (IF)"]
        n18["Confirm Completion of Production Operation Order (IP)"]
        n19{{"fa:fa-code-branch Review Successful?"}}
        n20{{"fa:fa-code-branch Review Successful?"}}
        n21{{"fa:fa-code-branch Review Successful?"}}
        n22{{"fa:fa-code-branch Review Successful?"}}
        n23{{"fa:fa-code-branch Review Successful?"}}
        n24{{"fa:fa-arrows-alt parallelGateway"}}
        n25{{"fa:fa-arrows-alt parallelGateway"}}
        n26{{"fa:fa-arrows-alt parallelGateway"}}
        n27{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n2 --> n1
    n8 --> n2
    n5 --> n21
    n3 --> n19
    n1 --> n3
    n4 --> n20
    n19 -->|"Yes"| n4
    n20 -->|"Yes"| n5
    n6 --> n22
    n21 -->|"Yes"| n6
    n22 -->|"Yes"| n7
    n7 --> n23
    n23 -->|"Yes"| n9
    n19 --> n24
    n24 --> n10
    n24 --> n11
    n25 --> n12
    n25 --> n13
    n20 -->|"No"| n25
    n26 --> n15
    n26 --> n16
    n27 --> n17
    n27 --> n18
    n23 -->|"No"| n27
    n22 -->|"No"| n26
    n21 -->|"No"| n14
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 startEvt
    class n9 endEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 startEvt
    class n17 startEvt
    class n18 startEvt
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1uP4jYU_itWViN2JZDiXCEPrRggo5E67eyybVWVPpjEGawxcWQ7MJTlv9cODpdMUnVpHhD-zvm-c_FJ4uythKXYiqy7uz3JiYzAvidXeI17EegtkcC9PjgCvyFO0JJi0dM-GcvlnPxduUGveNNuGovRmtCdRuf4hWHw62MfjBWR9oFAuRgIzEnW6_cKTtaI7yaMMq69P-BhZmdVNGO6ZzzF_Oxg2yFMfEWlJMdn2A290Is1T-CE5emVaOZnwyzpHXRylG2TFeKySr8U-Am9_U5SuVLrDFGBlc9KrulPaImprlHyUmNJyTd1M4jQcXLVsHmBEpK_KNyzFcRR_nqGfPtwAIe7u0V-Cgq-Thc5UFdCkRBTnAEhFTzbSJARSqMP3mQc-3ZfSM5ecfTBmYVT1-knupJIlW73dXMHW0xeVjJaMpoa18FW1xA5xVufv0WO3ec79duIhfP0HGkSOENneIp0H8IJnNSRsiz7X5FUX_lXJF5NrJkbO_H0FAv6gT-x3-vVZU69cAybfcJ8QxJ8IRrHsTs7t2oW-NDuFr2P3cCeNERfkMRbtDsLjibeSTD2wxiGnYLHeM0sy-UzZ0kt6M782D8JhvcwHjudgt4YekOTodJ54ahYgQkTEoyThJW5RLk8WvWVwz8XVoaiDA10s8GUiIKqUo6EHNGdGlPAMqDySctEEpaDX_SdtLD-ulBx2lX-neRek77gDcFb8ExRnuP0mAHK0xPwuVSZE7m7FvFaRcaJLBEFn-Wukqi0MsZPeKuU3yVFNsq3EhGVinqAtdUTtPK185Ql5RrnUlXxwFgqwBPbYA2Ia4WwU6HZSTCXSJYN-vDjid_aflErqi19VE9nouY2VRKfLjRGZw0hWdGtMWHrguL3AtBWArM3nJTyOu0Cc6T_CfDxMf50nTmE_4H03CQ5t0Ryb4mkp2yCaFJS1bJqpFBR0B1Q28hXGKXVWCBKwVP8AKo3TWNroB4ufU9jIcwMfMEJJoWaS87Wl5m05Bx8B_ld7nqoJizPCF_Xm6Y9G_d0Xb4Zr5YkhrfpvMtntN_XE6YPC4Olet0lq3qs5mWiy8xK-uPCOhwunzH2rUR4K9G5lejeSvTORMQ524oBohIUiKvhwvTh-KJpkvxbSMEtpPD7SOqkcPyTO2Aw-EFtvlkOj0vHLH2zrM2u8R6ZNTyuXbP0jLtdm0ca-Law_sDqtvumHOqodsPgG0NgFOoEHNhwDGqD0zCExhAahTonx204jq6S01tbe5r0od0E6vId0w_oNAG3WdjPrArm1IU5pjL4DjhVZDKHYRMYNkupxcNmM2pD0GyfMUDv4kCjt68-yF3BTjvstsNeO-y3w0E7HLbDw9P5-QoemaPudTF2uzOEHbjTgbsduNeB-x140IGHHXhHsWpOzTn2epPsdhi2w0477LbDXjvst8NBOxzWsNW31pivEUmtaG9VX5nqSzTFGSqptA59C5WSzXd5YkXV15hVFqliTglSh-T1ETz8A7qQpQk=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 DS-020-100 — Actual Costing

**Swim Lanes**: Cost Accountant | **Tasks**: 8 | **Gateways**: 0

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
        n1["fa:fa-user Execute Actual Activity Price / Rate Calculation"]
        n2["fa:fa-user Calculate Work in Progress"]
        n3["fa:fa-user Perform Actual Costing Run"]
        n4["fa:fa-user Run Distribution Cycle"]
        n5["fa:fa-user Execute Variance Calculation"]
        n6["fa:fa-user Run Template Allocation"]
        n7["fa:fa-user Perform Actual Cost Splitting"]
        n8["fa:fa-user Execute Production Order Settlement"]
        n9(["fa:fa-play Actual Costing initiated"])
        n10(["fa:fa-stop Actual Costing Checked"])
    end
    n1 --> n2
    n8 --> n3
    n6 --> n4
    n4 --> n7
    n9 --> n6
    n2 --> n5
    n7 --> n1
    n5 --> n8
    n3 --> n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 startEvt
    class n10 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVduO2joU_RUroxGtFNRcSSYPlZhApEqtOipzTh_O9ME4Nlg4dmQ7M9AR_16bhEtopuehPABrea-1L0l2Xh0kSuxkzu3tK-VUZ-B1pNe4wqMMjJZQ4ZELWuJfKClcMqxGNoYIrhf05yHMj-qtDbNcASvKdpZd4JXA4J9PLpgaIXOBglyNFZaUjNxRLWkF5S4XTEgbfYNT4pFDtu7oXsgSy3OA5yU-io2UUY7PdJhESVRYncJI8LJnSmKSEjTa2-KYeEFrKPWh_EbhL3D7nZZ6bTCBTGETs9YV-wyXmNketWwshxr5fBwGVTYPNwNb1BBRvjJ85BlKQr45U7G334P97e0TPyUFj7MnDswHMajUDBOgtKHnzxoQylh2E-XTIvZcpaXY4OwmmCezMHCR7SQzrXuuHe74BdPVWmdLwcoudPxie8iCeuvKbRZ4rtyZ76tcmJfnTPkkSIP0lOk-8XM_P2YihPxVJjNX-QjVpss1D4ugmJ1y-fEkzr3f_Y5tzqJk6l_PCctnivCFaVEU4fw8qvkk9r23Te-LcOLlV6YrqPEL3J0N7_LoZFjESeEnbxq2-a6rbJYPUqCjYTiPi_hkmNz7xTR40zCa-lHaVWh8VhLWa5ALpcEUIdFwDbluT-2H-_89OQRmBI7tsMF8i1GjsYnVDWT2hz5TvQMP0kwNfADfTKsghww1DGoq-JPz48Is6Jsd4zD4LuQGUG5sxEpipfqysC97wJIIWR1rsLWbJwF8a66yRX2ZOQczasZCl40tDeQ7xHBfEg93e1hGHP2hs8nvuR5xVR-amzIm0IAm-d-2wKJmVNvu-sp0uEwzvbJBh96-2m0GFlhrZpapuaI9_d27k4EpcXc9SbuZqam8NKr3l_eCd9YpLeprXb7GaHOpMpug_cN9MB5_NDdAB9MWhh2ctDDqYNTCpIN3LZx0MGhh3MGkhd2DzOMWph0Mu9PLJ8hWc9wcPToYpsNhOhqm42F6Mkwnw3Q6TN-d9ni_Ha_buY7rVFhWkJZO9uoc3qPmXVtiAhumnb3rwEaLxY4jJzu8b5ymLs11nlFo1kDVkvtfyultXQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.9 DS-020-110 — Material Ledger Reports

**Swim Lanes**: Cost Accountant | **Tasks**: 3 | **Gateways**: 4

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
        n1["fa:fa-user Review Variances"]
        n2["fa:fa-user Review Standard Price vs Actual Prices Report"]
        n3["fa:fa-user Review Unabsorbed Variances"]
        n4(["fa:fa-play Running of Material Ledger Report Initiated"])
        n5(["fa:fa-stop Running of Material Ledger Report Completed"])
        n6["Analyze Material Ledger"]
        n7{{"fa:fa-code-branch Review Successful?"}}
        n8{{"fa:fa-code-branch Review Successful?"}}
        n9{{"fa:fa-code-branch Review Successful?"}}
        n10{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n4 --> n2
    n3 --> n9
    n2 --> n7
    n1 --> n8
    n9 -->|"Yes"| n5
    n8 -->|"Yes"| n3
    n7 -->|"Yes"| n1
    n10 --> n6
    n7 -->|"No"| n10
    n8 -->|"No"| n10
    n9 -->|"No"| n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 endEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P2jgU_StWRiO6UpDySUIetmICWVVqV1Vpd7Va-mAcG6wxdmQ7fJTy39cmAYY0I63aPCDu8bnnXN_E10cHiRI7mfP4eKSc6gwcB3qNN3iQgcESKjxwQQP8BSWFS4bVwHKI4HpOv51pflTtLc1iBdxQdrDoHK8EBl_euWBiEpkLFORqqLCkZOAOKkk3UB5ywYS07AecEo-c3dqlJyFLLG8Ez0t8FJtURjm-wWESJVFh8xRGgpd3oiQmKUGDky2OiR1aQ6nP5dcKf4D7v2mp1yYmkClsOGu9Ye_hEjO7Ry1ri6Fabi_NoMr6cNOweQUR5SuDR56BJOTPNyj2Tidwenxc8Ksp-DxdcGAexKBSU0yA0gaebTUglLHsIconRey5SkvxjLOHYJZMw8BFdieZ2brn2uYOd5iu1jpbCla21OHO7iELqr0r91ngufJgfjtemJc3p3wUpEF6dXpK_NzPL06EkF9yMn2Vn6F6br1mYREU06uXH4_i3PtR77LNaZRM_G6fsNxShF-IFkURzm6tmo1i33td9KkIR17eEV1BjXfwcBMc59FVsIiTwk9eFWz8ulXWy49SoItgOIuL-CqYPPnFJHhVMJr4UdpWaHRWElZrkAulwQQhUXMNuW5W7cP9fxcOgRmBQ9ts8AlvKd6B8-nkCKuF8_UFOeglz42kOSgl-ChNa8FWGSddQ9bEytAqIfW9Utir9IXDpRJyicvXKojeXBMrZlr-qebcHBMgCPhg3oIdDeA9LldnTWsL3pkxRM1SaYR-e6EU35SUFtX_UMrFpmL4R6WREZpwyA7fcDf1vvjkeLxY2jE5XJqDjtbXNtbIbFeRmr1dOKfTi7z0J_PGP5nne_2JeI9YregW_9F88Lc0MxKaPzwCw-Hv5ktpw7AJx20YNGHShn4Tpm04tuH3hfOPfevfzStq8bSDhy2edHD_Ius1uqMO70_R0LyObhcf9-Pn42mLvoylOzjoh8N-OLpO7Ds4bofrHTjq5yaXuXOHpr3ouBc1fWphx3U2WG4gLZ3s6JwvaHOJl5jAmmnn5Dqw1mJ-4MjJzheZU1elyZxSaObLpgFP_wGOeIp7" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.10 DS-020-120 — Calculate and apply overhead for all MFG orders

**Swim Lanes**: Cost Accountant | **Tasks**: 6 | **Gateways**: 2

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
        n1["fa:fa-user Perform Template Allocation for COH"]
        n2["fa:fa-user Perform Actual Activity Rate Calculation"]
        n3["fa:fa-user Perform Actual Costing"]
        n4[["fa:fa-cog Perform Production Order Activity Confirmation"]]
        n5[["fa:fa-cog Update Activity Quantity based on Template Allocation to Production Orders COH"]]
        n6[["fa:fa-cog Apply Standard Overhead Rates on Production Activity Quantity"]]
        n7(["fa:fa-play Overhead Calculation Initiated"])
        n8(["fa:fa-stop Overhead Calculation Completed"])
        n9{{"fa:fa-arrows-alt parallelGateway"}}
        n10{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n7 --> n9
    n1 --> n5
    n6 --> n2
    n9 --> n4
    n9 --> n1
    n4 --> n10
    n5 --> n10
    n10 --> n6
    n2 --> n3
    n3 --> n8
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P4jYU_StWRiNaKUj5JEweKjGBtCt1Ndsyu_uw9ME4Dlhj7Mh2YCjiv9fOB0kYqFQ1D5B77HPOvRd8fbIQz7AVW4-PJ8KIisFppLZ4h0cxGK2hxCMb1MA3KAhcUyxHZk_OmVqSv6ttblC8m20GS-GO0KNBl3jDMfj6yQYzTaQ2kJDJscSC5CN7VAiyg-KYcMqF2f2Ap7mTV27N0jMXGRbdBseJXBRqKiUMd7AfBVGQGp7EiLNsIJqH-TRHo7NJjvID2kKhqvRLiT_D9-8kU1sd55BKrPds1Y7-DteYmhqVKA2GSrFvm0Gk8WG6YcsCIsI2Gg8cDQnI3joodM5ncH58XLGLKXidrxjQD6JQyjnOgVQaXuwVyAml8UOQzNLQsaUS_A3HD94imvuejUwlsS7dsU1zxwdMNlsVrznNmq3jg6kh9op3W7zHnmOLo_688sIs65ySiTf1phen58hN3KR1yvP8fznpvopXKN8ar4Wfeun84uWGkzBxPuq1Zc6DaOZe9wmLPUG4J5qmqb_oWrWYhK5zX_Q59SdOciW6gQof4LETfEqCi2AaRqkb3RWs_a6zLNdfBEetoL8I0_AiGD276cy7KxjM3GDaZKh1NgIWW5BwqcAMIV4yBZmqV83D3B8rK4dxDsem2eALFjkXO_CKdwXVZYEZpRxBRTgDegEkL7-trL96fO82f4ZUCan5InuijuBPo5VAikpaiQ1F_H8VMcnrozCkBD8uHMQ3F4puW1aiKt0Xc-C7DBLOciJ2rXtfKxxqfS2yqvKW-UepW2ZezADLgJa-1R3FP5jLpl19r8nQa1YU9AiW-kfRoyYDL3ssthhmVb-kseppfkjoSjr66SKtszt2Yr2-g096KhMtnmnyzz3ytCNLxYvb5ITruvFH8tPp1JKhEPwgx5AqUEABKcX01_p4rKzzuf_Hc_4bSU-d-oVFYDz-RZs2oVuHYRNO6tBrwqc6DIZhMxZY0ITNAWThVew6NTBpYq8O_Sb063DaO74mn3ZsDWDvNuzfhoP-pBqshHdXJndXosv9MICnzSgfgE_tOBsW5bSwZVs7rM8Ryaz4ZFV3ub7vM5zDkirrbFuwVHx5ZMiKqzvPKqvjNCdQj6JdDZ7_AS-ing4=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.11 DS-020-130 — Calculate WIP

**Swim Lanes**: Cost Accountant | **Tasks**: 4 | **Gateways**: 4

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
        n1["fa:fa-user Execute Calculation of WIP"]
        n2["fa:fa-user Validate the WIP Amount for the Current Period"]
        n3["fa:fa-user Validate the WIP Reversal Amount of the Previous Period"]
        n4["fa:fa-user Review Production Order Level WIP"]
        n5(["fa:fa-play Calculation of WIP Started"])
        n6(["fa:fa-stop Calculation of WIP Completed"])
        n7["Review Production Orders"]
        n8{{"fa:fa-code-branch Validation Successful?"}}
        n9{{"fa:fa-code-branch Validation Successful?"}}
        n10{{"fa:fa-code-branch Review Successful?"}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n5 --> n1
    n1 --> n2
    n2 --> n8
    n3 --> n9
    n8 -->|"Yes"| n3
    n9 -->|"Yes"| n4
    n4 --> n10
    n10 -->|"Yes"| n6
    n11 --> n7
    n10 -->|"No"| n11
    n9 -->|"No"| n11
    n8 -->|"No"| n11
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 startEvt
    class n6 endEvt
    class n7 startEvt
    class n8 gateway
    class n9 gateway
    class n10 gateway
    class n11 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2P4jYU_StWRiNaKUhJSEjIQysmkGql3XZUtruqSh-Mcw3WmBjZDh9l-e-1QwIDk2kflgfEPb7nnHsv8k2ODhEFOKnz-HhkJdMpOvb0CtbQS1FvgRX0XHQGvmDJ8IKD6tkcKko9Y__UaX642ds0i-V4zfjBojNYCkB_fHDR2BC5ixQuVV-BZLTn9jaSrbE8ZIILabMfIKEerd2aoychC5DXBM-LfRIZKmclXOFBHMZhbnkKiCiLG1Ea0YSS3skWx8WOrLDUdfmVgk94_5UVemViirkCk7PSa_4RL4DbHrWsLEYquW2HwZT1Kc3AZhtMWLk0eOgZSOLy5QpF3umETo-P8_Jiij5P5iUyH8KxUhOgSGkDT7caUcZ5-hBm4zzyXKWleIH0IZjGk0HgEttJalr3XDvc_g7YcqXTheBFk9rf2R7SYLN35T4NPFcezPedF5TF1SkbBkmQXJyeYj_zs9aJUvpdTmau8jNWL43XdJAH-eTi5UfDKPPe6rVtTsJ47N_PCeSWEXglmuf5YHod1XQY-d77ok_5YOhld6JLrGGHD1fBURZeBPMozv34XcGz332V1eJZCtIKDqZRHl0E4yc_HwfvCoZjP0yaCo3OUuLNCmVCaTQmRFSlxqU-n9pP6f81dyhOKe7bYaPpHkilAWWYk4pjzUSJBEVfPzzPnb9f0YJb2hfMWWGmgMzdtslovLZWiApZQ1klJZj42dxXUdxKDf5H6nfYglSYt5qmHHv0LGHLRKU6NcNbTSPBYGcooqhI3dNvdhugj0aav20u-uFC33Dzv74dBprZ-wbW9cdXxOGVqLTYdBEzsd5weEuNDfOdMtVtdcnx2JrYZdtfmHVBVu3cLGtWEQJK0Yr_PHdOp1fc0Xdwfa-b3FT9H0S_mwh7wivFtvDL-f5caWbDnH-UEer3fzISTeifw6AJg3OYNOHgHI6aMLHht7nzJ5gJfjPHDT66w8MGDxsvrzXz7hKH7UFTRnyf-Kuo83z_zukeT7rx-v7bJtu9dwMH3fCgGw674ejypLiBh81SvwHj7tyk3Xc36KgTNZPphP0WdlxnDXKNWeGkR6d-MzBvDwVQXHHtnFwHV1rMDiVx0voJ6lQbuxwmDJvFtj6Dp38BkEKuuA==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.12 DS-020-140 — Calculate Variances

**Swim Lanes**: Cost Accountant | **Tasks**: 10 | **Gateways**: 11

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
        n1["fa:fa-user Display Cost Analysis of Production Order"]
        n2["fa:fa-user Display Production Order"]
        n3["fa:fa-user Review Planned Cost and Planned Quantity"]
        n4["fa:fa-user Review Actual Qty and Cost for Actual Quantity"]
        n5["fa:fa-user Review Activity Costs for the Order"]
        n6["fa:fa-user Review the Documented Goods Movements"]
        n7["fa:fa-user Review the Production Order Status"]
        n8["fa:fa-user Execute Variance Calculation Test mode"]
        n9["fa:fa-user Review Variance Amounts Calculated"]
        n10["fa:fa-user Calculate Variances Without Test"]
        n11(["fa:fa-play Variances Calculation is Initiated"])
        n12(["fa:fa-play Production Orders Review is Initiated"])
        n13(["fa:fa-stop Production Orders Review Completed"])
        n14(["fa:fa-stop Variances Calculation is Completed"])
        n15["Execute Production Operations (IF)"]
        n16["Execute Production Operations (IP)"]
        n17["Execute Production Operations (IF)"]
        n18["Execute Production Operations (IP)"]
        n19["Calculate and apply overhead for all MFG orders"]
        n20["Process Goods Receipt from Production (IF)"]
        n21["Process Goods Receipt from Production (IP)"]
        n22["Confirm Completion of Production Operation Order (IF)"]
        n23["Confirm Completion of Production Operation Order (IP)"]
        n24{{"fa:fa-code-branch Review Successful?"}}
        n25{{"fa:fa-code-branch Review Successful?"}}
        n26{{"fa:fa-code-branch Review Successful?"}}
        n27{{"fa:fa-code-branch Review Successful?"}}
        n28{{"fa:fa-code-branch Review Successful?"}}
        n29{{"fa:fa-code-branch Amounts are Correct?"}}
        n30{{"fa:fa-code-branch exclusiveGateway"}}
        n31{{"fa:fa-arrows-alt parallelGateway"}}
        n32{{"fa:fa-arrows-alt parallelGateway"}}
        n33{{"fa:fa-arrows-alt parallelGateway"}}
        n34{{"fa:fa-arrows-alt parallelGateway"}}
        n35[["fa:fa-folder-open Review Production Orders"]]
    end
    n2 --> n1
    n12 --> n2
    n5 --> n26
    n3 --> n24
    n1 --> n3
    n4 --> n25
    n24 -->|"Yes"| n4
    n25 -->|"Yes"| n5
    n6 --> n27
    n26 -->|"Yes"| n6
    n27 -->|"Yes"| n7
    n7 --> n28
    n28 -->|"Yes"| n13
    n24 --> n31
    n31 --> n15
    n31 --> n16
    n32 --> n17
    n32 --> n18
    n25 -->|"No"| n32
    n33 --> n20
    n33 --> n21
    n34 --> n22
    n34 --> n23
    n28 -->|"No"| n34
    n27 -->|"No"| n33
    n26 -->|"No"| n19
    n11 --> n30
    n35 --> n8
    n8 --> n9
    n9 --> n29
    n29 -->|"Yes"| n10
    n30 --> n35
    n29 -->|"No"| n30
    n10 --> n14
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
    class n11 startEvt
    class n12 startEvt
    class n13 endEvt
    class n14 endEvt
    class n15 startEvt
    class n16 startEvt
    class n17 startEvt
    class n18 startEvt
    class n19 startEvt
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
    class n31 gateway
    class n32 gateway
    class n33 gateway
    class n34 gateway
    class n35 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWF1v2zYU_SuEisAtYAP6lqyHDY5tFQWWrW26FUOzB0aiYiG0KJCUEy_1fx8pi7LFUMXm-cEwD-8590OXFOkXKyM5shLr6uqlrEqegJcJ36AtmiRgcg8ZmkzBEfgD0hLeY8Qm0qYgFb8t_27NHL9-lmYSS-G2xHuJ3qIHgsDvH6ZgIYh4Chis2IwhWhaT6aSm5RbS_ZJgQqX1GxQXdtF666auCc0RPRnYduRkgaDiskIn2Iv8yE8lj6GMVPlAtAiKuMgmBxkcJk_ZBlLeht8wdAOfv5Y534hxATFDwmbDt_gXeI-wzJHTRmJZQ3eqGCWTfipRsNsaZmX1IHDfFhCF1eMJCuzDARyuru6q3in4srqrgPhkGDK2QgVgXMDrHQdFiXHyxl8u0sCeMk7JI0reuOto5bnTTGaSiNTtqSzu7AmVDxue3BOcd6azJ5lD4tbPU_qcuPaU7sW35gtV-cnTMnRjN-49XUfO0lkqT0VR_C9Poq70C2SPna-1l7rpqvflBGGwtF_rqTRXfrRw9DohuiszdCaapqm3PpVqHQaOPS56nXqhvdREHyBHT3B_Epwv_V4wDaLUiUYFj_70KJv7j5RkStBbB2nQC0bXTrpwRwX9hePHXYRC54HCegOWhHGwyDLSVBxW_DgrP5Xz7c4qYFLAmSw2WJWsxiKVI6GCeC_aFJACiHjyJuMlqcBvciXdWX-dqbhmlR-TvCHpM9qV6Al8xLCqUH6MAFZ5D3xqROQl3w9FfKPIIuMNxOAT37cSrVZBaI8bpYIxqXInbFsR1qqIDcyUT2jkS-MVyZotqrjI4j0hOQM3ZIckwIYK0aiCXklwyyFvNHo8pK-fUdZwBNqttsoQWEKcNRi2Kl-QKMlW7D1Dibkxgl5hsZUdxHollA_pjj3k93a9BANfS74hDW8j0NjO257e9s-JdB66aMgP4t1Sdu7fnSu4moJeN6ZS-pGIdxJhnNTjIkuyrTEyKPiawmgiowqyGdUDPPdfI9qSGXj7IX2n1S_8F6SPOim6xFN8iSfZXKeOkAsT1jXeA7EY6AbBvF1cEGNwk74H7ftaa3BXtpfcGRFj3Ur6jDJU1mJ1U7I9j-R1zK7zH8h67K7c4ZakKkq6VQ9NWmo7o0q_W6SGILzLdF7F47-8qA6TR67ZvTg0ZBvVmLdNJtMsGvzznXU4nBODS4nhpcToUmJ8KXFuJqrdC1KxFxJKUcZ1qmebqeg5ww0rd-j98V2v05wTDVJKntgMYg5qSEU7IzxCci8heZeQ_EtIwbd-EyvEwQ3RGalR1b-n9U1RNGjXoeKAePxRuWA2-0ms_G7odGO3GwfdMOzGXjf2lf1x7HVDv5sOlHoLfL-z_kTC-3dhoCYCbUIxwk4hUoahZqgicSNtQjGiTiFWhrFm6HiD6GRvqOy6dJxAB_r8Vb0iHYj1zH4lrTdPldJTtbN1oHevyufqgKfnosR9vRpqwtPr1004c_Xk1KPrw-metUokPg6V_bwLRY3duV7WXsjulAPdVAWnLJ3O0vHPjteyqdS1YgC7Ztgzw74ZDsxwaIYjMxyb4bkZFlmacae_FA5xdwT3uovdEPWNaDCiEY7g0Qgej-BzM-7aI_hIru5Irq43gvvqLjeEAzMcmuHIDMdmeG6ERZcbYccMu2bYM8PmLMUK7e6d1tTaIrqFZW4lL1b7d42VWDkqYIO5dZhasOHkdl9lVtL-rWE1dS4EVyUUt83tETz8A_Viqe0=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.13 DS-020-150 — Generate Variances Report

**Swim Lanes**: Cost Accountant | **Tasks**: 12 | **Gateways**: 11

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
        n1["Execute Reports for Variances"]
        n2["Analyze the Variances"]
        n3["fa:fa-user Display Cost Analysis of Production Order"]
        n4["fa:fa-user Display Production Order"]
        n5["fa:fa-user Review Planned Cost and Planned Quantity"]
        n6["fa:fa-user Review Actual Qty and Cost for Actual Quantity"]
        n7["fa:fa-user Review Activity Costs for the Order"]
        n8["fa:fa-user Review the Documented Goods Movements"]
        n9["fa:fa-user Review the Production Order Status"]
        n10["fa:fa-user Execute Variance Calculation Test mode"]
        n11["fa:fa-user Review Variance Amounts Calculated"]
        n12["fa:fa-user Calculate Variances Without Test"]
        n13(["fa:fa-play Variance Report Generation is Initiated"])
        n14(["fa:fa-play Variances Calculation is Initiated"])
        n15(["fa:fa-play Production Orders Review is Initiated"])
        n16(["fa:fa-stop Variance Report Generation is Completed"])
        n17(["fa:fa-stop Production Orders Review Completed"])
        n18(["fa:fa-stop Variances Calculation is Completed"])
        n19["Execute Production Operations (IF)"]
        n20["Execute Production Operations (IP)"]
        n21["Execute Production Operations (IF)"]
        n22["Execute Production Operations (IP)"]
        n23["Calculate and apply overhead for all MFG orders"]
        n24["Process Goods Receipt from Production (IF)"]
        n25["Process Goods Receipt from Production (IP)"]
        n26["Confirm Completion of Production Operation Order (IF)"]
        n27["Confirm Completion of Production Operation Order (IP)"]
        n28{{"fa:fa-code-branch Review Successful?"}}
        n29{{"fa:fa-code-branch Review Successful?"}}
        n30{{"fa:fa-code-branch Review Successful?"}}
        n31{{"fa:fa-code-branch Review Successful?"}}
        n32{{"fa:fa-code-branch Review Successful?"}}
        n33{{"fa:fa-code-branch Amounts are Correct?"}}
        n34{{"fa:fa-code-branch exclusiveGateway"}}
        n35{{"fa:fa-arrows-alt parallelGateway"}}
        n36{{"fa:fa-arrows-alt parallelGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
        n39[["fa:fa-folder-open Calculate Variances"]]
        n40[["fa:fa-folder-open Review Production Orders"]]
    end
    n4 --> n3
    n15 --> n4
    n7 --> n30
    n5 --> n28
    n3 --> n5
    n6 --> n29
    n28 -->|"Yes"| n6
    n29 -->|"Yes"| n7
    n8 --> n31
    n30 -->|"Yes"| n8
    n31 -->|"Yes"| n9
    n9 --> n32
    n32 -->|"Yes"| n17
    n28 --> n35
    n35 --> n19
    n35 --> n20
    n36 --> n21
    n36 --> n22
    n29 -->|"No"| n36
    n37 --> n24
    n37 --> n25
    n38 --> n26
    n38 --> n27
    n32 -->|"No"| n38
    n31 -->|"No"| n37
    n30 -->|"No"| n23
    n14 --> n34
    n40 --> n10
    n10 --> n11
    n11 --> n33
    n33 -->|"Yes"| n12
    n34 --> n40
    n33 -->|"No"| n34
    n12 --> n18
    n13 --> n39
    n39 --> n1
    n1 --> n2
    n2 --> n16
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
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 endEvt
    class n17 endEvt
    class n18 endEvt
    class n19 startEvt
    class n20 startEvt
    class n21 startEvt
    class n22 startEvt
    class n23 startEvt
    class n24 startEvt
    class n25 startEvt
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
    class n38 gateway
    class n39 subProc
    class n40 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWF1v2zYU_SuEisAtYAMiJVmyHzY4thUUWLe26VYMzR4YiYqFyqJAUU7c1P99pEzKFkN1m-eHIDq859wPXl5TfnYSmhJn7lxdPedlzufgecQ3ZEtGczC6xzUZjcER-AOzHN8XpB5Jm4yW_Db_1ppBv3qSZhKL8TYv9hK9JQ-UgN_fjsFCEIsxqHFZT2rC8mw0HlUs32K2X9KCMmn9ikSZm7Xe1NI1ZSlhJwPXDWESCGqRl-QEe6Ef-rHk1SShZdoTzYIsypLRQQZX0Mdkgxlvw29q8g4_fc5TvhHPGS5qImw2fFv8gu9JIXPkrJFY0rCdLkZeSz-lKNhthZO8fBC47wqI4fLrCQrcwwEcrq7uys4p-LS6K4H4JAWu6xXJQM0FvN5xkOVFMX_lLxdx4I5rzuhXMn-F1uHKQ-NEZjIXqbtjWdzJI8kfNnx-T4tUmU4eZQ5zVD2N2dMcuWO2F38NX6RMT56WUxShqPN0HcIlXGpPWZb9L0-iruwTrr8qX2svRvGq8wWDabB0X-rpNFd-uIBmnQjb5Qk5E43j2FufSrWeBtAdFr2Ovam7NEQfMCePeH8SnC39TjAOwhiGg4JHf2aUzf17RhMt6K2DOOgEw2sYL9CgoL-AfqQiFDoPDFcbsKQ1B4skoU3JccmPq_JTwi93zvqJJA0n4COpKOM1yCgD7fksE1LfOX-dmSNhvihxsf9GgDjHQ2aeMMvwPMMTuYVglddVIQp0DEPSRfMDmgGRZdokPKcl-E2ez76Kb1f5MSnokz6SXU4ewfsClyVJjxHgMu2AD42oR873fZGpVWSR8AYX4APftxKtlqyVxq1S4ZBUvhO2rcix4rKclnwiK18ar2jSbEnJRRY3lKY1eEd3RALGZswGFcxKgluOeWPQodvn627RWw-WuEiaArcyn4ioyVaMNEMDWmPoJBZb2Zl1J0VSg4_6_M7u1IDgc843tOFtCAbbe93R2w7q_B47HtyQkrBjAqIv34ovrlzF8OZcxh-QqXsl-JFCYCiYG1DryvxIZHoSqTmt_iGbJd1WBbHIhIbMYCyDCtFAIC_qMagwO5s-5_4rlUANXr-N3xgjyP0XpPcmCV7iCV3iSc6-U3_KQYGrqtgDcTjZhuC0Pey4KMC7-Aa0txJzxsq5J-c_qWt1sj-ShOSVmDaMbs8jscQc_Afyi9jl3FvSMsvZVm-atDQmtU5fDQ1LEOFlOi_iiZ6fdYfJi-XkXlyNko1uzNsmkWlmTfHznXM4nBNnFxI991IivJSILiV6dqKepZiJ0UwZIwl_QfXtVPKUFE2d78jN8UZj0oITDTNGH-sJLjioMBPtTIoB0vQSUngJKbqENPvSDbFMXE8Jm9CKlLZvGNGbvduJa2fqG4c5Tk90cYE-_lP6YDL5SQShHmFwfPbVc6iW1f2wVMsoUs_e8TlQj1O1PFPPKJLA9zvnTxn8d2GgF2bGQqgWIuUQageuYdh5hsaC9jlTCkgbIsMQhr3oZFdpU5UenBmAfi8QvaQAaALIzOxX2nrzdMqeqiXyTaBzr-JBUxMIzVy0-Itq6IXQrJ9aQN1O653X4fiuSl7nCjWgc4VQUbSG55ml7Yqu1H3XNNUBarcQKS86Fah6yus2Qe1oF4Yqii64Wp2evcLIxtSvbj3Yt8OBHZ7a4dAOR3Z4ZodFde04HMDRAO51r9593B_AgwF8ql6r-2hoRSMrOrMrI3cAhwM4GsAHMkUDmaKBTNF0AA8H8Ei_X_fhmRUWB84KQzuM7LBnh307HNjhqR0O7bA9S3H41G8B_XPkatgZO1vCtjhPnfmz0_6y5sydlGS4KbhzGDu44fR2XybOvP0FymmqVPhZ5fiB4e0RPPwNXpgsYQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.14 DS-020-160 — Execute Order Settlement

**Swim Lanes**: Cost Accountant | **Tasks**: 4 | **Gateways**: 3

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
        n1["fa:fa-user Execute Order Settlement in Update Run"]
        n2["fa:fa-user Validate Accounting Document"]
        n3["fa:fa-user Validate the Settlement Values"]
        n4["fa:fa-user Execute Order Settlement in Test Run"]
        n5(["fa:fa-play Order Settlement Execution Initiated"])
        n6(["fa:fa-stop Order Settlement Execution Completed"])
        n7["Review Production Orders"]
        n8{{"fa:fa-code-branch Validation Successful?"}}
        n9{{"fa:fa-code-branch Validation Successful?"}}
        n10{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n1 --> n2
    n3 --> n8
    n2 --> n9
    n4 --> n3
    n5 --> n4
    n9 -->|"Yes"| n6
    n8 -->|"Yes"| n1
    n10 --> n7
    n9 -->|"No"| n10
    n8 -->|"No"| n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 startEvt
    class n6 endEvt
    class n7 startEvt
    class n8 gateway
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVWuP2jgU_StWRiN2pSDlSUI-bMUEsqq0j6pMu1ot_WAcB6wxdmQ7PJby32vnwSPDVJWaD4h7cs85vjf29dFCPMdWYj0-HgkjKgHHgVrjDR4kYLCEEg9s0ACfoSBwSbEcmJyCMzUn_9dpblDuTZrBMrgh9GDQOV5xDD69t8FEE6kNJGRyKLEgxcAelIJsoDiknHJhsh9wXDhF7da-euIix-KS4DiRi0JNpYThC-xHQRRkhicx4iy_ES3CIi7Q4GQWR_kOraFQ9fIrif-E-39IrtY6LiCVWOes1Yb-AZeYmhqVqAyGKrHtmkGk8WG6YfMSIsJWGg8cDQnIXi5Q6JxO4PT4uGBnU_A8XTCgH0ShlFNcAKk0PNsqUBBKk4cgnWShY0sl-AtOHrxZNPU9G5lKEl26Y5vmDneYrNYqWXKat6nDnakh8cq9LfaJ59jioH97XpjlF6d05MVefHZ6itzUTTunoih-ykn3VTxD-dJ6zfzMy6ZnLzcchanzWq8rcxpEE7ffJyy2BOEr0SzL_NmlVbNR6Dpviz5l_shJe6IrqPAOHi6C4zQ4C2ZhlLnRm4KNX3-V1fKD4KgT9GdhFp4Foyc3m3hvCgYTN4jbFWqdlYDlGqRcKjBBiFdMQaaat-Zh7n8Lq4BJAYem2WC2x6hSGPxtTguYY6WoPqxMAcLApzLXhYKPFVtYX64kvFuJz5CSOrH107sYTDmqjMwt0X-DqAfEtbXGKyxvqcGPL_sZ69pfLTr85axQUv3tXjEbScIZeK8HGdHryrXCr1cSo4uEVLz8nkTKNyXFryUirfARbwneAf3B8wrV2bVQr-D4eOzMzIgdLvWQQOuuZ4Y1rxDCUhYVfbewTqcr7vgnuK5zn4z3iFaSbPHvzea_0PR4aP4wFwyHv-n90YZ-E8Zt6DXhuA2DJvTbMGzCoA3HJvy6sP41G-Gr7n2Lxz3c7aydhh_1-H_xJs3p8Xt4fRJNAd0EuoG9-7B_Hw7uw-F5Zt_Ao3a83oDR_dy4mzw36PguqhvSwpZtbbDYQJJbydGqL2N9Yee4gBVV1sm2YKX4_MCQldSXllXV535KoJ4lmwY8fQOY6obN" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.15 DS-020-170 — Product Costing Reports

**Swim Lanes**: TBD | **Tasks**: 7 | **Gateways**: 0

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
    subgraph TBD
        n1["fa:fa-user Execute Product Costing Reports"]
        n2["fa:fa-user Execute Cost Center Reports"]
        n3["fa:fa-user Execute Production Order Reports"]
        n4["fa:fa-user Execute Scrap Reports"]
        n5["fa:fa-user Execute Variance Reports"]
        n6["fa:fa-user Execute Material Ledger Reports"]
        n7["fa:fa-user Execute Inventory Reports"]
        n8(["fa:fa-play Product Costing Reports Execution Started"])
        n9(["fa:fa-stop Product Costing Reports Execution Completed"])
    end
    n8 --> n2
    n2 --> n1
    n1 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
    n6 --> n7
    n7 --> n9
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 startEvt
    class n9 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVduK2zAU_BXhJbgFB3y344dC4sSwsKWl2bYPTR8UW07EKpKR5Fwa8u-VYudapxTqB5OZnJmRjnXZGzkrkJEYvd4eUywTsDflEq2QmQBzDgUyLdAQ3yDHcE6QMHVNyaic4l_HMsevtrpMcxlcYbLT7BQtGAJfny0wVEJiAQGp6AvEcWlaZsXxCvJdygjjuvoJxaVdHtPav0aMF4hfCmw7cvJASQmm6EJ7kR_5mdYJlDNa3JiWQRmXuXnQgyNsky8hl8fh1wJ9hNvvuJBLhUtIBFI1S7kiL3COiJ6j5LXm8pqvT83AQudQ1bBpBXNMF4r3bUVxSN8uVGAfDuDQ683oORS8jmcUqCcnUIgxKoGQip6sJSgxIcmTnw6zwLaE5OwNJU_uJBp7rpXrmSRq6ralm9vfILxYymTOSNGW9jd6DolbbS2-TVzb4jv1vstCtLgkpaEbu_E5aRQ5qZOeksqy_K8k1Vf-CsVbmzXxMjcbn7OcIAxS-0-_0zTHfjR07vuE-Brn6Mo0yzJvcmnVJAwc-7HpKPNCO70zXUCJNnB3MRyk_tkwC6LMiR4aNnn3o6znnznLT4beJMiCs2E0crKh-9DQHzp-3I5Q-Sw4rJbgddQuGP1Q58fMKGFSwr5uMJhsUV5LBFRkUecSpExItfTAF1QxLsXM-Hmldbu1WgNSRKXiOnXeXzMxo-CT3qDdYr9bPM3V5LoVQbfieOrQHHWLwm7RR_V59ZkDXlCxeDTEqFv7TNeqKYzvulXxu7OsImoFPfgErZ3u0lRvdFQom_dXPoOLj5Cs-geflK0qgm6c1L5uftAY9Psf1LduodvAdi9Rp4FeC70G-i30Gxi0MGhg2MKwgVELowYOrta_9j_t-xva7aa9btrvpoNuOuymo246Ph-3N_SgPRkNy1ghvoK4MJK9cbzt1I1YoBLWRBoHy4C1ZNMdzY3keCsYdVWoJTbGUG3WVUMefgOVTlPN" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Cost Analyst | DS-020-020,  | |
| Cost Accountant | DS-020-030, DS-020-040, DS-020-050, DS-020-060, DS-020-080, DS-020-090, DS-020-100, DS-020-110, DS-020-120, DS-020-130, DS-020-140, DS-020-150, DS-020-160,  | |
| TBD | DS-020-170 | |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for DS-020. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | APIGEE Business Data | APIGEE | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |
| 2 | ATCR Business Data | ATCR | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |
| 3 | BOBJ Business Data | BOBJ | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |
| 4 | CFIN S/4 HANA Business Data | CFIN S/4 HANA | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |
| 5 | CIBR Business Data | CIBR | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |
| 6 | COMPASS Business Data | COMPASS | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |
| 7 | Capacity Forecast Data Store Business Data | Capacity Forecast Data Store | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |
| 8 | Corp / IP S/4 Business Data | Corp / IP S/4 | SAP S/4HANA | FPR Data Steward | Intel Confidential | Per transaction | Transaction |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

#### 4.2.1 ICOST — Current-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph DS020CDACL_Azure_Data_Lake[" "]
        direction TB
        DS020CDAA_ECA_ADLS["ECA-ADLS"]:::appBox
        DS020CDAD_Azure_Data_Lake[("🗄️ Azure Data Lake")]:::dbCyl
        DS020CDAA_ECA_ADLS -.-> DS020CDAD_Azure_Data_Lake
    end
    style DS020CDACL_Azure_Data_Lake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020CDACL_Delta_Lake[" "]
        direction TB
        DS020CDAA_ECA_DataBricks["ECA-DataBricks"]:::appBox
        DS020CDAD_Delta_Lake[("🗄️ Delta Lake")]:::dbCyl
        DS020CDAA_ECA_DataBricks -.-> DS020CDAD_Delta_Lake
    end
    style DS020CDACL_Delta_Lake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020CDACL_MSSQL[" "]
        direction TB
        DS020CDAA_MARS["MARS"]:::appBox
        DS020CDAA_WorkStream["WorkStream"]:::appBox
        DS020CDAD_MSSQL[("🗄️ MSSQL")]:::dbCyl
        DS020CDAA_MARS -.-> DS020CDAD_MSSQL
        DS020CDAA_WorkStream -.-> DS020CDAD_MSSQL
    end
    style DS020CDACL_MSSQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020CDACL_Oracle_DB[" "]
        direction TB
        DS020CDAA_CIBR["CIBR"]:::appBox
        DS020CDAA_COMPASS["COMPASS"]:::appBox
        DS020CDAA_DCS["DCS"]:::appBox
        DS020CDAA_EATS["EATS"]:::eolBox
        DS020CDAA_FCA["FCA"]:::appBox
        DS020CDAA_ICOST["ICOST"]:::appBox
        DS020CDAA_SAP_ECC["SAP ECC"]:::appBox
        DS020CDAA_SAP_ICX["SAP ICX"]:::appBox
        DS020CDAA_SPEED["SPEED"]:::appBox
        DS020CDAD_Oracle_DB[("🗄️ Oracle DB")]:::dbCyl
        DS020CDAA_CIBR -.-> DS020CDAD_Oracle_DB
        DS020CDAA_COMPASS -.-> DS020CDAD_Oracle_DB
        DS020CDAA_DCS -.-> DS020CDAD_Oracle_DB
        DS020CDAA_EATS -.-> DS020CDAD_Oracle_DB
        DS020CDAA_FCA -.-> DS020CDAD_Oracle_DB
        DS020CDAA_ICOST -.-> DS020CDAD_Oracle_DB
        DS020CDAA_SAP_ECC -.-> DS020CDAD_Oracle_DB
        DS020CDAA_SAP_ICX -.-> DS020CDAD_Oracle_DB
        DS020CDAA_SPEED -.-> DS020CDAD_Oracle_DB
    end
    style DS020CDACL_Oracle_DB fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020CDACL_PostgreSQL[" "]
        direction TB
        DS020CDAA_MES_300["MES 300"]:::appBox
        DS020CDAA_PEGA["PEGA"]:::appBox
        DS020CDAA_XEUS["XEUS"]:::appBox
        DS020CDAD_PostgreSQL[("🗄️ PostgreSQL")]:::dbCyl
        DS020CDAA_MES_300 -.-> DS020CDAD_PostgreSQL
        DS020CDAA_PEGA -.-> DS020CDAD_PostgreSQL
        DS020CDAA_XEUS -.-> DS020CDAD_PostgreSQL
    end
    style DS020CDACL_PostgreSQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020CDACL_SAP_HANA[" "]
        direction TB
        DS020CDAA_BOBJ["BOBJ"]:::appBox
        DS020CDAA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
        DS020CDAA_Corp_IP_S_4["Corp / IP S/4"]:::appBox
        DS020CDAA_Finance_HANA["Finance HANA"]:::appBox
        DS020CDAA_SAP_IBP["SAP IBP"]:::appBox
        DS020CDAA_SideCar["SideCar"]:::appBox
        DS020CDAD_SAP_HANA[("🗄️ SAP HANA")]:::dbCyl
        DS020CDAA_BOBJ -.-> DS020CDAD_SAP_HANA
        DS020CDAA_CFIN_S_4_HANA -.-> DS020CDAD_SAP_HANA
        DS020CDAA_Corp_IP_S_4 -.-> DS020CDAD_SAP_HANA
        DS020CDAA_Finance_HANA -.-> DS020CDAD_SAP_HANA
        DS020CDAA_SAP_IBP -.-> DS020CDAD_SAP_HANA
        DS020CDAA_SideCar -.-> DS020CDAD_SAP_HANA
    end
    style DS020CDACL_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020CDACL_Snowflake[" "]
        direction TB
        DS020CDAA_ECA["ECA"]:::appBox
        DS020CDAA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
        DS020CDAD_Snowflake[("🗄️ Snowflake")]:::dbCyl
        DS020CDAA_ECA -.-> DS020CDAD_Snowflake
        DS020CDAA_ECA_SnowFlake -.-> DS020CDAD_Snowflake
    end
    style DS020CDACL_Snowflake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020CDACL_Teradata[" "]
        direction TB
        DS020CDAA_EDW["EDW"]:::appBox
        DS020CDAD_Teradata[("🗄️ Teradata")]:::dbCyl
        DS020CDAA_EDW -.-> DS020CDAD_Teradata
    end
    style DS020CDACL_Teradata fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    DS020CDAA_Legacy_MDG["Legacy MDG"]:::appBox
    DS020CDAA_APIGEE["APIGEE"]:::appBox
    DS020CDAA_SAP_PO["SAP PO"]:::appBox
    DS020CDAA_SPAN["SPAN"]:::appBox

    DS020CDAD_PostgreSQL ==>|"Direct"| DS020CDAD_Oracle_DB
    DS020CDAD_MSSQL ==>|"Direct"| DS020CDAD_Oracle_DB
    DS020CDAD_Oracle_DB ==>|"Direct"| DS020CDAD_Teradata
    DS020CDAD_Oracle_DB ==>|"SLT"| DS020CDAD_SAP_HANA
    DS020CDAD_SAP_HANA ==>|"ADF Rest API / SFTP(Blob)"| DS020CDAD_Azure_Data_Lake
    DS020CDAD_Azure_Data_Lake ==>|"Unity Catalog"| DS020CDAD_Delta_Lake
    DS020CDAD_Delta_Lake ==>|"Snowflake Connector / Snowpipe"| DS020CDAD_Snowflake
    DS020CDAD_Snowflake ==>|"Direct"| DS020CDAD_Oracle_DB
    DS020CDAD_Snowflake ==>|"Internal"| DS020CDAD_Oracle_DB
    DS020CDAD_Oracle_DB ==>|"JE Posting"| DS020CDAD_SAP_HANA
    DS020CDAD_Oracle_DB ==>|"ETL"| DS020CDAD_Teradata
    DS020CDAD_Teradata ==>|"ETL"| DS020CDAD_Oracle_DB
    DS020CDAD_SAP_HANA ==>|"Direct"| DS020CDAD_Snowflake

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWItu2kgU_ZWRq4hWgi15kGyQWmn8IKVygheTTaWysgZ7IFaMbRmzCU35953rJxibwSxGYl7n3Jk59871410wPYsKXeHs7N127bCL3hvhM53TRhc1JmRBG03UWFBzGdjhSqX_UgcGHM-LRyLo3ySwycShiwawp54b6vavyMB5x38DGPT1yNx2VtCr05lH0WO_iTAjOo01IBzv1XwmQRjZWC7oPXl7sq3wmbWnxFlQhnkO545KJtSBicJgCX0uW73uE9N2Z6zzssO6AuK-5F1XnfUarc_Oxm42BRqJYxexy3TIYiHTKSK-L3pvaGo7TveD2JF7vV5zEQbeC-1-aLdvbsTrpNl6hTV1L_y3puk5XgDDl3KnaM-aSCsnMYc78jW-ycxdKDfy5UWluXOxo1y0C-ao5-TL6_XEjtjJ7ElSm12V9q6vYXjsxhYXy8ksIP4zkvX2RVuSsaQa-NcyoIZMQmKo5IX-HAtoLPwT4-Gy7ICaoe25mWxwpQawoUjYwLKqMyKrtqDK-N1uNxZ1lyLvTPlxLIyX1p-XFvu3zKvxckrbUxShEKAQoMbCJ7AaSbtvHaj1R-tr9WQxlbpWoki4cugeOVLRMfwy0ZU2_LZFP_ff9sksU-f_KAwLEgPbfFkkOucdPLU3Zi4XOgIcrHE-cVHpfCKeyDnyZPre6_pfam1p7_EQAheK_TJi48kLXvQwoGTOCHmDp368rnLhozGe5rC2otIxce8i91Cq_RKBTuaSQUBMh50lsbZbpL44ZCQoeG6RBvca1sGJSY1HkCUAs38eUMGjKKmxIobGabgM2pMwQ7J_ns2-NNBHDBqVPLCONXbiJAZnNcRqhxD60o-EwGpcgqYoMsCh5EVy7s7yaI7HkSzyIhrcWgzPzPgeH9fiMAfXwoObaxGYt2vhI5fXYiT-r81hjq_HAe9zGNU5IwOeLG9o3iKcBfSofK7oxmW7DSld0RGr8U6AptzB0YWCB_2hPEI-gIJ3VDZ2UH5WcgA3_cc7Krpnw0DFruoxYFc8RnUM5MiTBQEE8jf8gGuHgDgQvzMSFNx7R6__YOjGVToRtJH--QpBm0v2At_oa8AHKmuhz6ivAZ9H7dkucU2aTps0D5o1Ot-ilqZ4UeMSbItKJABCXOPFbiZ8eeTCtPFC98ct6F8MqNQ01xe1iLkf6tA2fVCHlzigFiUWfj-l-nCluNMdLdd7nTpHvonErx_cZyf2ogDT9JJp4I0la3MjMFtfRQim4we8ruyInnF5q-Yw9_grBZ7MYSMaEIu9dtX3l_wE4stPPMmzGcoVT4e5gstPRdkyKke1FHeUaPkKVDoj5sq4l-_YxuMGYo3d_ecUrPXvFIXB48o-KBxFbZAkX22wF6rhh-jJGj9sw7aBm3dZ9OXL19_s1SRy6lj4Xf00VnitO4aYP7ZVk7d9V83V1dE2cTu17fYnPCz30JAuQsSUZzdPvTfSPoqON_m0ba30C07lcGL70bXDFZJYr-PNtu0Vv1OUjaQ7y86y5LkuE8gLYKGs17d9Wtj0doIoGTjGT0Vy3w1p4BLnSDd_V6JnT9udHeaxIl8ZqYfFSHaeK3jVG96OkTKxNpQuJE124lmK-bmRxEyrjWQ8wggPpW_9kSKNHocKUpU75UGuyKXqMO9VDbjjYd93bJPAaHkmVQ256uMa0wC-o5enTtWAxKO4VsubtlR7Sne_NBRSZrzDNEt24Jdlydvb250UKTSFOQ3mxLaE7rsQfa8XuoJFp2TphMK6KZBl6Okr1xS60Sd1Yekzt1HZJkzRedy5_g9TDwE8" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 S/4 HANA — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph DS020FDACL_Azure_Data_Lake[" "]
        direction TB
        DS020FDAA_ECA_ADLS["ECA-ADLS"]:::appBox
        DS020FDAD_Azure_Data_Lake[("🗄️ Azure Data Lake")]:::dbCyl
        DS020FDAA_ECA_ADLS -.-> DS020FDAD_Azure_Data_Lake
    end
    style DS020FDACL_Azure_Data_Lake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020FDACL_Delta_Lake[" "]
        direction TB
        DS020FDAA_ECA_DataBricks["ECA-DataBricks"]:::appBox
        DS020FDAD_Delta_Lake[("🗄️ Delta Lake")]:::dbCyl
        DS020FDAA_ECA_DataBricks -.-> DS020FDAD_Delta_Lake
    end
    style DS020FDACL_Delta_Lake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020FDACL_MSSQL[" "]
        direction TB
        DS020FDAA_GraphiteConnect["GraphiteConnect"]:::appBox
        DS020FDAA_MARS["MARS"]:::appBox
        DS020FDAA_PDF_SMH["PDF-SMH"]:::appBox
        DS020FDAA_WSPW["WSPW"]:::appBox
        DS020FDAA_WorkStream["WorkStream"]:::appBox
        DS020FDAD_MSSQL[("🗄️ MSSQL")]:::dbCyl
        DS020FDAA_GraphiteConnect -.-> DS020FDAD_MSSQL
        DS020FDAA_MARS -.-> DS020FDAD_MSSQL
        DS020FDAA_PDF_SMH -.-> DS020FDAD_MSSQL
        DS020FDAA_WSPW -.-> DS020FDAD_MSSQL
        DS020FDAA_WorkStream -.-> DS020FDAD_MSSQL
    end
    style DS020FDACL_MSSQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020FDACL_Oracle_DB[" "]
        direction TB
        DS020FDAA_SPEED["SPEED"]:::appBox
        DS020FDAD_Oracle_DB[("🗄️ Oracle DB")]:::dbCyl
        DS020FDAA_SPEED -.-> DS020FDAD_Oracle_DB
    end
    style DS020FDACL_Oracle_DB fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020FDACL_PostgreSQL[" "]
        direction TB
        DS020FDAA_MES_300["MES 300"]:::appBox
        DS020FDAA_XEUS["XEUS"]:::appBox
        DS020FDAD_PostgreSQL[("🗄️ PostgreSQL")]:::dbCyl
        DS020FDAA_MES_300 -.-> DS020FDAD_PostgreSQL
        DS020FDAA_XEUS -.-> DS020FDAD_PostgreSQL
    end
    style DS020FDACL_PostgreSQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020FDACL_SAP_HANA[" "]
        direction TB
        DS020FDAA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
        DS020FDAA_Corp_IP_S_4_HANA["Corp / IP S/4 HANA"]:::appBox
        DS020FDAA_IF_S_4_HANA["IF S/4 HANA"]:::appBox
        DS020FDAA_SAP_BOBJ["SAP BOBJ"]:::eolBox
        DS020FDAA_SAP_IBP["SAP IBP"]:::appBox
        DS020FDAA_SAP_PAPM["SAP PAPM"]:::appBox
        DS020FDAA_SAP_S_4_MDG["SAP S/4 MDG"]:::appBox
        DS020FDAA_SideCar["SideCar"]:::appBox
        DS020FDAD_SAP_HANA[("🗄️ SAP HANA")]:::dbCyl
        DS020FDAA_CFIN_S_4_HANA -.-> DS020FDAD_SAP_HANA
        DS020FDAA_Corp_IP_S_4_HANA -.-> DS020FDAD_SAP_HANA
        DS020FDAA_IF_S_4_HANA -.-> DS020FDAD_SAP_HANA
        DS020FDAA_SAP_BOBJ -.-> DS020FDAD_SAP_HANA
        DS020FDAA_SAP_IBP -.-> DS020FDAD_SAP_HANA
        DS020FDAA_SAP_PAPM -.-> DS020FDAD_SAP_HANA
        DS020FDAA_SAP_S_4_MDG -.-> DS020FDAD_SAP_HANA
        DS020FDAA_SideCar -.-> DS020FDAD_SAP_HANA
    end
    style DS020FDACL_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020FDACL_SAP_HANA_Cloud[" "]
        direction TB
        DS020FDAA_SAP_Ariba["SAP Ariba"]:::appBox
        DS020FDAA_SAP_SAC["SAP SAC"]:::appBox
        DS020FDAD_SAP_HANA_Cloud[("🗄️ SAP HANA Cloud")]:::dbCyl
        DS020FDAA_SAP_Ariba -.-> DS020FDAD_SAP_HANA_Cloud
        DS020FDAA_SAP_SAC -.-> DS020FDAD_SAP_HANA_Cloud
    end
    style DS020FDACL_SAP_HANA_Cloud fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph DS020FDACL_Snowflake[" "]
        direction TB
        DS020FDAA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
        DS020FDAA_Power_BI_DARC["Power BI (DARC)"]:::appBox
        DS020FDAD_Snowflake[("🗄️ Snowflake")]:::dbCyl
        DS020FDAA_ECA_SnowFlake -.-> DS020FDAD_Snowflake
        DS020FDAA_Power_BI_DARC -.-> DS020FDAD_Snowflake
    end
    style DS020FDACL_Snowflake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    DS020FDAA_ECM_Windchill["ECM (Windchill)"]:::appBox
    DS020FDAA_PDM_Translator["PDM Translator"]:::appBox
    DS020FDAA_FCS["FCS"]:::eolBox
    DS020FDAA_Capacity_Forecast_Data_Store["Capacity Forecast Data Store"]:::appBox
    DS020FDAA_ICS_Phoenix["ICS (Phoenix)"]:::appBox
    DS020FDAA_ATCR["ATCR"]:::appBox
    DS020FDAA_SCS["SCS"]:::eolBox
    DS020FDAA_DXCR["DXCR"]:::appBox
    DS020FDAA_DMOCR["DMOCR"]:::appBox
    DS020FDAA_IF_Blue_Yonder["IF Blue Yonder"]:::appBox
    DS020FDAA_IF_PDH_Raw["IF PDH Raw"]:::appBox
    DS020FDAA_IF_PDH_Foundational["IF PDH Foundational"]:::appBox
    DS020FDAA_IF_PDH_Consumptional["IF PDH Consumptional"]:::appBox
    DS020FDAA_IP_Blue_Yonder["IP Blue Yonder"]:::appBox
    DS020FDAA_IP_PDH_Raw["IP PDH Raw"]:::appBox
    DS020FDAA_IP_PDH_Foundational["IP PDH Foundational"]:::appBox
    DS020FDAA_IP_PDH_Consumptional["IP PDH Consumptional"]:::appBox
    DS020FDAA_PDH_Raw["PDH Raw"]:::appBox
    DS020FDAA_PDH_Foundational["PDH Foundational"]:::appBox
    DS020FDAA_PDH_Consumptional["PDH Consumptional"]:::appBox

    DS020FDAD_PostgreSQL ==>|"Direct"| DS020FDAD_MSSQL
    DS020FDAD_MSSQL ==>|"EAI Connector"| DS020FDAD_SAP_HANA
    DS020FDAD_Oracle_DB ==>|"ADF Rest API / SFTP(Blob)"| DS020FDAD_Azure_Data_Lake
    DS020FDAD_Azure_Data_Lake ==>|"Unity Catalog"| DS020FDAD_Delta_Lake
    DS020FDAD_Delta_Lake ==>|"Snowflake Connector / Snowpipe"| DS020FDAD_Snowflake
    DS020FDAD_MSSQL ==>|"MuleSoft & Reltio"| DS020FDAD_SAP_HANA
    DS020FDAD_SAP_HANA ==>|"ADF Rest API / SFTP(Blob)"| DS020FDAD_Azure_Data_Lake
    DS020FDAD_Snowflake ==>|"MuleSoft/BODS"| DS020FDAD_SAP_HANA
    DS020FDAD_MSSQL ==>|"Direct"| DS020FDAD_Snowflake
    DS020FDAD_Snowflake ==>|"Remote Function Adapter / M..."| DS020FDAD_SAP_HANA
    DS020FDAD_SAP_HANA_Cloud ==>|"SAC Data Export Service (AP..."| DS020FDAD_Snowflake
    DS020FDAD_SAP_HANA_Cloud ==>|"SAP Odata services with con..."| DS020FDAD_SAP_HANA
    DS020FDAD_SAP_HANA_Cloud ==>|"Apigee / MuleSoft"| DS020FDAD_SAP_HANA

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWQtP20gQ_isrVxxUApoCgWukVlq_Sk5J8cXh6Kk5WYu9IRYbr-VHgVL---3Yjp04fqUlkeLd2flmZ77ZtWedZ8nmDpUG0t7es-u50QA970cLuqT7A7R_S0K6f4j2Q2rHgRs9jeh3ymCAcZ6OJKr_kMAlt4yG-4Cecy8y3R-Jgfd9_xHUQKaTpcueQGrSO07R9fAQYQFk-y-gwfiDvSBBlNiIQzomjzeuEy1Ef05YSIXOIlqyEbmlDCaKghhknvDe9IntendCeNoXooB494XorP_ygl729mZePgWayjMPiY_NSBiqdI6I78v8Ec1dxgZv5L6q6_phGAX8ng7e9HoXF_J51j16AJ8GJ_7joc0ZD2D4VO2X7Tm3yhPLzOG-eo4vcnMn2oV6elJr7r3c1056JXOUs8I9XZf7cj-3pyg98am1d34OwzMvtRjGt3cB8RdINXsnPV3FysjCP-KAWiqJiDUi9_TbTEIz6b9UHz6OG1A7crmX0waflQFsaQq2sDoyBVA0j6Ap8IPBICV1G6JuTXkwk2ax8-epI34d-2wWz2lvjhItBFoItGbSW7CaUNvkBzo6PvpUP1kKpZ6TMRI9MdpAx4p0DN-cdK0H303S3_uPTTSrlP0Ow-CQHLj2fZjxXAja2F6buZroRKEzx8XEZaaLidpILjRfjd-xaf492pnaz2DGjajCPU8oCnxJ0kwutsZ4AisfLm2qhqpb5vhSaIvWkWi1AW5M40Zow6VVlQf3ZhRQsgRA3mlbGilp1asiGWtbECW2yisitVFDW2fljLjO-kBYd-WcrAZI_UpOlF5tEV8FxGbi7iPvvJBNQ9NUgUqubWkvpqlOfTqOVLkt_clsZd5y623c5Yqvxp_Bw-guoL9yJxhrpnXa68Fe1kwkWm1b7qt2DTsfLm18r7lVTXih0MZ45maZ8zUDNa62IerTVGi-Wp5MbFiX-AveOUuKPvximdbZCg19ZL47Q9Bvy5jCA98aGht4IULv0NDobGSor-OHemcgxCxfyX_BJsUGgmYKSau7OshQNjKEaHWZw8DGOENAswsEAhqrnzMUBCR6rUDXoQoJAJS22nZBnvTqPQBTpzw274CNJVBe1as5uqR_F-xa1neBrXK-K0akelcI5HpXTJb3nWBprpsh9feSld6r30kshfHY2f2xKeDiEHpLsrWftDttGaystgtWuq78zMnm9Y8SpdYn78rxukykczW43wXYnshU-_XS6fGHOfvVQxKg9QwNZ6S831qa8wcaWPLQUvEE8pr0kTxEByB425rf3Oua1K7Gu5yvcqe3EpRbaYugBdmQ1ZXiLyV0PY6xdeN6jr0QZpJkjNFBLqjgc73YH1vTgHghIxEPksPSGBWCJqiuQEEmfrefq2tPAQKvhqInS-diQZEwSs_6prANy2Y1jFbD6QuIZLhp7qFiWsaCU899hLJAMdFB1m2MFk-VidCHS5OamURmNkemfk1swaXJljq-SvXg2hiSbskspta_3HNokBY7IECpoAVqqJfWhDykMNFBotMBovPYcwjsc8IK7Lq0gxFxGg3jpV-2siFuNGOUIzc6R26sR250ityojNzYLXKjOnJjt8gL3zs4XuH1Li5X-dvi7KaJ9UMM-vjx00-xqJOnxEz6WX2OLwkzkIaHKHuBATeYn7V1TcUZNzOBVR1NqLhbYGMozhOmPjUOZMZv326aq3wXWTuc2b724H6kCCnjd5v2ym_cqkYyK8WtPQ8VHBVS3_VpKerN50U1a-OYUZPPI_SHiJyJbHVjLq8AX5O4IrhN397JV6rZza_10KpWUS0n5bkndMkjivTYS8sV7BA_okD2-Pj4eDeSsuoqy6Co2ZKHkfbo8yBCJg2-uzZFB9jYNlzrbbVlA105YDpMbYbowY0WyObe77mMffeOUgg9S0idrVJFOKJ3okj5tlZM2U4PqXiKkShvLodTTZleTzQ00j5rX9SaOnE0KaQjC07r2PeZaye3puqSbmSpde_IBTvwd1h1BTeyNKhyPOeIz49G7pxuP6dLRVca4arM6sM3L7M-fPiwVWNJh9KSBkviOtLgWUr-dpMGkkPnJGaR9HIokTji5pNnS4PknzEp9kVCqeoSwegyFb78D6ZUQQE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

Data lineage traces the origin and transformation path of key data objects across integrated systems.

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | MES 300 | MES 300 master tables | XEUS | XEUS staging tables | ETL / API replication |
| 2 | XEUS | XEUS master tables | ICOST | ICOST staging tables | ETL / API replication |
| 3 | WorkStream | WorkStream master tables | MARS | MARS staging tables | ETL / API replication |
| 4 | MARS | MARS master tables | ICOST | ICOST staging tables | ETL / API replication |
| 5 | EATS | EATS master tables | ICOST | ICOST staging tables | ETL / API replication |
| 6 | SPEED | SPEED master tables | SAP ECC | SAP ECC staging tables | ETL / API replication |

> *Lineage detail will be refined when tower architects validate source/target schema object mappings.*

### 4.4 RICEFW Data Objects

Data-centric RICEFW objects (Reports and Conversions) from the Object Tracker:

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| FPRC1493 | Conversion | Conversion of WIP values as per Component structure in S/4 - IP | 10. Object Complete |  |  | 02.High |
| FPRC1491 | Conversion | Conversion of WIP values as per Component structure in S/4 - Back End IF | 10. Object Complete |  |  | 02.High |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 ICOST — Current-State Application Landscape

#### Overview

The ICOST architecture represents the **current / legacy** landscape for DS-020. Legacy and transitional product costing landscape. ICOST remains the primary costing engine during Release 3, with ECC as the book-of-record ERP.This view is generated from `R3_CurrentFlows.xlsx` (42 flow hops across 27 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '16px', 'fontFamily': 'Segoe UI, Arial, sans-serif'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        DS020C_APIGEE["📦 APIGEE"]:::app
        DS020C_BOBJ["📦 BOBJ"]:::app
        DS020C_CFIN_S_4_HANA["📦 CFIN S/4 HANA"]:::app
        DS020C_CIBR["📦 CIBR"]:::app
        DS020C_COMPASS["📦 COMPASS"]:::app
        DS020C_Corp_IP_S_4["📦 Corp / IP S/4<br/><i>DEV</i>"]:::app
        DS020C_DCS["📦 DCS"]:::app
        DS020C_EATS["📦 EATS<br/><i>EOL</i>"]:::eol
        DS020C_ECA["📦 ECA"]:::app
        DS020C_ECA_ADLS["📦 ECA-ADLS"]:::app
        DS020C_ECA_DataBricks["📦 ECA-DataBricks"]:::app
        DS020C_ECA_SnowFlake["📦 ECA-SnowFlake"]:::app
        DS020C_EDW["📦 EDW"]:::app
        DS020C_FCA["📦 FCA"]:::app
        DS020C_Finance_HANA["📦 Finance HANA"]:::app
        DS020C_ICOST["📦 ICOST"]:::app
        DS020C_Legacy_MDG["📦 Legacy MDG"]:::app
        DS020C_MARS["📦 MARS"]:::app
        DS020C_MES_300["📦 MES 300"]:::app
        DS020C_PEGA["📦 PEGA"]:::app
        DS020C_SAP_ECC["📦 SAP ECC"]:::app
        DS020C_SAP_IBP["📦 SAP IBP"]:::app
        DS020C_SAP_ICX["📦 SAP ICX"]:::app
        DS020C_SAP_PO["📦 SAP PO"]:::app
        DS020C_SPAN["📦 SPAN"]:::app
        DS020C_SPEED["📦 SPEED"]:::app
        DS020C_SideCar["📦 SideCar"]:::app
        DS020C_WorkStream["📦 WorkStream"]:::app
        DS020C_XEUS["📦 XEUS"]:::app
    end

    DS020C_MES_300 -->|"Direct"| DS020C_XEUS
    DS020C_XEUS -->|"Direct"| DS020C_ICOST
    DS020C_WorkStream -->|"Direct"| DS020C_MARS
    DS020C_MARS -->|"Direct"| DS020C_ICOST
    DS020C_EATS -->|"Direct"| DS020C_ICOST
    DS020C_SPEED -->|"SAP PO"| DS020C_SAP_ECC
    DS020C_SPEED -->|"Direct"| DS020C_EDW
    DS020C_Legacy_MDG -->|"DRF (Data Replication Frame..."| DS020C_SAP_ECC
    DS020C_CIBR -->|"SAP PO"| DS020C_SAP_ICX
    DS020C_SAP_ICX -->|"Direct"| DS020C_SAP_ECC
    DS020C_CIBR -->|"Direct"| DS020C_ICOST
    DS020C_SAP_ECC -->|"SLT"| DS020C_CFIN_S_4_HANA
    DS020C_CFIN_S_4_HANA -->|"SLT"| DS020C_SideCar
    DS020C_SideCar -->|"ADF Rest API / SFTP(Blob)"| DS020C_ECA_ADLS
    DS020C_ECA_ADLS -->|"Unity Catalog"| DS020C_ECA_DataBricks
    DS020C_ECA_DataBricks -->|"Snowflake Connector / Snowpipe"| DS020C_ECA_SnowFlake
    DS020C_Corp_IP_S_4 -->|"SLT"| DS020C_CFIN_S_4_HANA
    DS020C_ECA_SnowFlake -->|"Direct"| DS020C_CIBR
    DS020C_CIBR -->|"Internal"| DS020C_ICOST
    DS020C_ECA -->|"Internal"| DS020C_ICOST
    DS020C_ICOST -->|"File based"| DS020C_SAP_ECC
    DS020C_ICOST -->|"JE Posting"| DS020C_CFIN_S_4_HANA
    DS020C_SAP_ECC -->|"ETL"| DS020C_EDW
    DS020C_EDW -->|"ETL"| DS020C_ICOST
    DS020C_EDW -->|"ETL"| DS020C_CIBR
    DS020C_FCA -->|"Direct"| DS020C_ICOST
    DS020C_SAP_ECC -->|"SLT"| DS020C_Finance_HANA
    DS020C_Finance_HANA -->|"APIGEE"| DS020C_APIGEE
    DS020C_APIGEE -->|"APIGEE"| DS020C_PEGA
    DS020C_Finance_HANA -->|"Direct"| DS020C_BOBJ
    DS020C_Finance_HANA -->|"SAP PO"| DS020C_SAP_PO
    DS020C_SAP_PO -->|"SAP PO"| DS020C_SAP_ECC
    DS020C_SAP_IBP -->|"Direct"| DS020C_ECA
    DS020C_COMPASS -->|"Direct"| DS020C_ICOST
    DS020C_DCS -->|"Direct"| DS020C_ICOST
    DS020C_SPAN -->|"Denodo (Data Virtualization)"| DS020C_ICOST

    click DS020C_APIGEE href "https://iapm.intel.com/#/app/22790" "APIGEE -- IAPM #22790" _blank
    click DS020C_BOBJ href "https://iapm.intel.com/#/app/17651" "BOBJ -- IAPM #17651" _blank
    click DS020C_CFIN_S_4_HANA href "https://iapm.intel.com/#/app/42993" "CFIN S/4 HANA -- IAPM #42993" _blank
    click DS020C_CIBR href "https://iapm.intel.com/#/app/237" "CIBR -- IAPM #237" _blank
    click DS020C_COMPASS href "https://iapm.intel.com/#/app/16439" "COMPASS -- IAPM #16439" _blank
    click DS020C_Corp_IP_S_4 href "https://iapm.intel.com/#/app/41363" "Corp / IP S/4 -- IAPM #41363" _blank
    click DS020C_DCS href "https://iapm.intel.com/#/app/14464" "DCS -- IAPM #14464" _blank
    click DS020C_EATS href "https://iapm.intel.com/#/app/119" "EATS -- IAPM #119" _blank
    click DS020C_ECA href "https://iapm.intel.com/#/app/43119" "ECA -- IAPM #43119" _blank
    click DS020C_ECA_ADLS href "https://iapm.intel.com/#/app/25794" "ECA-ADLS -- IAPM #25794" _blank
    click DS020C_ECA_DataBricks href "https://iapm.intel.com/#/app/41458" "ECA-DataBricks -- IAPM #41458" _blank
    click DS020C_ECA_SnowFlake href "https://iapm.intel.com/#/app/35811" "ECA-SnowFlake -- IAPM #35811" _blank
    click DS020C_EDW href "https://iapm.intel.com/#/app/4010" "EDW -- IAPM #4010" _blank
    click DS020C_FCA href "https://iapm.intel.com/#/app/44990" "FCA -- IAPM #44990" _blank
    click DS020C_Finance_HANA href "https://iapm.intel.com/#/app/42993" "Finance HANA -- IAPM #42993" _blank
    click DS020C_ICOST href "https://iapm.intel.com/#/app/9008" "ICOST -- IAPM #9008" _blank
    click DS020C_Legacy_MDG href "https://iapm.intel.com/#/app/40068" "Legacy MDG -- IAPM #40068" _blank
    click DS020C_MARS href "https://iapm.intel.com/#/app/33537" "MARS -- IAPM #33537" _blank
    click DS020C_MES_300 href "https://iapm.intel.com/#/app/41275" "MES 300 -- IAPM #41275" _blank
    click DS020C_PEGA href "https://iapm.intel.com/#/app/43163" "PEGA -- IAPM #43163" _blank
    click DS020C_SAP_ECC href "https://iapm.intel.com/#/app/21195" "SAP ECC -- IAPM #21195" _blank
    click DS020C_SAP_IBP href "https://iapm.intel.com/#/app/40709" "SAP IBP -- IAPM #40709" _blank
    click DS020C_SAP_ICX href "https://iapm.intel.com/#/app/21195" "SAP ICX -- IAPM #21195" _blank
    click DS020C_SAP_PO href "https://iapm.intel.com/#/app/21195" "SAP PO -- IAPM #21195" _blank
    click DS020C_SPAN href "https://iapm.intel.com/#/app/21159" "SPAN -- IAPM #21159" _blank
    click DS020C_SPEED href "https://iapm.intel.com/#/app/31517" "SPEED -- IAPM #31517" _blank
    click DS020C_SideCar href "https://iapm.intel.com/#/app/42993" "SideCar -- IAPM #42993" _blank
    click DS020C_WorkStream href "https://iapm.intel.com/#/app/37871" "WorkStream -- IAPM #37871" _blank
    click DS020C_XEUS href "https://iapm.intel.com/#/app/35612" "XEUS -- IAPM #35612" _blank

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWQtv4jgQ_itWqqp7UinhXdCqUsijxwoKarrbPR0nZIgpUUOCknBdtu1_Pzt2Ql4ORsdKK3Vmvvni8Xg8tt-llWchaSBdXr7brh0OwPtVuEFbdDUAV0sYoKtrcBWg1d63w8MY_YsconA8j2oi0x_Qt-HSQcEVQa89NzTt35GDRnf3i5gRmQG3tnMgUhO9eAh8H10DBQOdaxBAN6gFyLfXV5_E2vHeVhvoh5G_fYAm8NezbYUb_PcaOgHCNptw64zhEjmENPT3RObikZg7uLLdFyxsy1jkQ_f1KOrIn5_g8_Jy7iYU4Gk4dwH-XV6CWg1_0GpjT2CIarYb7GwfWSAIDw4CKwcGAQqwDTWP_tbQGiz3ge2iIADRb207zuDCwL9h5zoIfe8VDS6Gt7ddecj-rL2RkQyau1_XK8_x_MGFLMs5n3C3A8cf9TnsEK-JT1nu9YbdM3xaMIRFn9rtCZ-NjM9YZ8EAB8-HBxxT0MkxbW3LctAb9FE6IlpXOUZE73WNozeBr0eeU4gIiXEqyqoqy6d8Uq_Bfvniw90GKOO_59J8b922LPy_1eoAZTYbj1TlaTR9AGPlL_1xLv1DQeRn4YRYhbbngvHjUaqZclNWF8psdK_raYcr1AVUir0MBgM8rQXUcDr8lscQGR-hGqOHhbloL_5UHpQ8lCiBWW8DoqzwMRo-FqBYVoGYTmaKaRZAVFyB8_zdYjQjH1zAYhWog9GMfPDXpV-_-2rfafqPr3X7ju9QUwsfgUV8e115KgCILCbUp-MjIU6zogO1EGUsqiBUlYWijc0SUI3Iq5EaXqZD3169BmX4o7bai-l6b4YDX1GZk0RZ4UN7LiC1Z769UYyRURUjw3ahu0KlKcx0JzJ4pE7Npzw0EvIxY_QCV4fFRLvPA6kGYA0fPVEeC3NKZBUI3Vy0ZLkA0k2AxXzcTL8vRIXI-AhTmeF5V_MgLMYzrlbjRsNZGQ6LT-DUn6U49Wc1bjYtg82mFaiZ8lDAYFkVQte1IgQLKzC2hVToF1BUzMc9e_6rGfoIbvPQo4aP_ql_L2QVkeUQyLXi3SubXLghufuYS1q0M82lj7TfjD0R8IzpunFLB8XDRKnv5taHOAEpweLW0dQx8zhbPnLJzwUU_JNS5pbWhRjxaIAvpNaCR7Rz7BWM9nzDh1t0c3Nzgprso1WfShaIW1xLvI89QSESPOoh_qbxU8o600xkOdKaUmy8MtziImL2imbgCAYh6YLwTm8aT7MvQ8db_pGeDLZdZrODCZmf7_hgcgAqnhDHe8lhU1uiy91L4-_HO9-a7Hy493BdHDfPJ5-FpTt7h3KOj9ukW97PnBnQjE_e7EVNGGeqR26IfBc61etKVc4xjyQMYNj4nEOOfNaJ9EuDvulg5gUhPl8JBSGbi_rTuGJZ4r9L7UoGzbEsRNNIovM_1026gckypBTxKmBHgI_sSSEDoyIeINr8T7AUBhSdIk6ASgsUFriFPfus4ku7Cm75VXOVhp4hxCcG9_vnbB3KQ2yNXM_yWGX_YfvhHjr276i4_1H0EZ9Acf3IzdLGxyfSubQJw10wqNdtuNve2Hi1OTcrb1u_qONdu95s9vq4xQPxbJLLhZEym4CLWLNYOtB9LWEhEyfE0eh1O42II4IkDLGcy5Ct7SJU7Wa_34qoMifMI2dswOckhUwocq0eJaKVL45aJOV7ZzkkFLZuu9WnFEnmxZFjKj5PqvwLxa3R6rK4pU-7qbgxAy4jSXahUbXb3XbERJdHPCIm5vqPGjEhggYNGuvcYv-NyniR7UgoTq3EvZrOqtZp_7RREMqsTq_fjklqrL-I84vpKplSDYXY5Lc7twlfphtJZp9aVLIemwYR0lbnttFISNMNB-OMDficeDcVGp7coBWObr_xkKiU690QzYh2nxVQI5MRTMz3n97lzitt6ZuHMyobbYdEqPqyTPMh7qAYBZNzGVIHFLGJkbuU53ivkZ4gquWyRQc5oVRrdVitZme_OMOYnM_Azq5ii6jZ61ASem-SXj1UxeUhfZNo-WFlOoKk6091dY57RKHyg2sZHQm7l0lVH6aq5CEtldj09-R-wkMbsWTuqaqaBx9Gzx8PPcKeMx7cVJ5PE3Wiwiyk9xPk6LCQ0XbxyNCpjld0zyC0WBqdRo9R0LuJeLUwBZ-DnanPK2bHk7hoHUvd-QgNqHfboxtN5rIoHhXTctmi-yixDa3baEY87Aor2ceoPGZgbzvRa91wnHqJM-RTL3FpqJJAZZEHt8KbEi65yLUyV3qWDMb6vf6gCTwmjfEho3Afq-ySW6iSm8TxYpK5rbcaPTBJ3uAo4Pgml8Zp-l2aadUG0dFId0M7PFAgeTZMQ_QpfTNrdq02NrRq3ro2ttco934S3Vceg0qDEge2Q_4lge33-4UnR-la2iJ_C21LGrxL0SOzNJAstIZ7J5Q-ryW4Dz3z4K6kQfT2K-13-EORZkM8CVsq_PwPTZ368A==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### ICOST Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | ATM Cycle Times to ICOST | EATS → ICOST | Direct | Near Real-Time |
| 2 | CIBR Inv to ICOST | CIBR → ICOST | Direct | Event-Driven |
| 3 | CIBR RM Inv to ECC | CIBR → SAP ICX → SAP ECC | SAP PO → Direct | Near Real-Time |
| 4 | COMPASS LRP to ICOST | COMPASS → ICOST | Direct | Batch |
| 5 | DCS MyDeals to ICOST | DCS → ICOST | Direct | Batch |
| 6 | ECA Costing Chain | CIBR → ICOST | Internal (×2) | Near Real-Time |
| 7 | ECC BOH to EDW | SAP ECC → EDW | ETL | Batch |
| 8 | ECC GL to EDW | SAP ECC → EDW | ETL | Batch |
| 9 | ECC Replication to ECA | SAP ECC → CFIN S/4 HANA → SideCar → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake | SLT (×2) → ADF Rest API / SFTP(Blob) → Unity Catalog → Snowflake Connector / Snowpipe | Batch / Near Real-Time / Real-Time/NRT |
| 10 | ECC to EDW Reporting | SAP ECC → EDW | ETL | Batch |
| 11 | ECC to Finance HANA | SAP ECC → Finance HANA | SLT | Real-Time/NRT |
| 12 | EDW Feedback to CIBR | EDW → CIBR | ETL | Batch |
| 13 | EDW Feedback to ICOST | EDW → ICOST | ETL | Batch |
| 14 | FCA to ICOST | FCA → ICOST | Direct | Batch |
| 15 | Finance HANA to BOBJ | Finance HANA → BOBJ | Direct | Batch |
| 16 | GL Posting to CFIN | ICOST → CFIN S/4 HANA | JE Posting | Batch |
| 17 | GL Posting to ECC | ICOST → SAP ECC | File based | Batch |
| 18 | IBP Demand Planning (Legacy) | SAP IBP → ECA | Direct | Event-Driven |
| 19 | MES Route to ICOST | MES 300 → XEUS → ICOST | Direct (×2) | Near Real-Time |
| 20 | Master Data to ECC | Legacy MDG → SAP ECC | DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC) | Event-Driven |
| 21 | RM Std Cost Update to ECC | Finance HANA → SAP PO → SAP ECC | SAP PO (×2) | Event-Driven |
| 22 | RM Std Fluctuations Alert | Finance HANA → APIGEE → PEGA | APIGEE (×2) | Event-Driven |
| 23 | S/4 Inv. Mvt to CIBR | Corp / IP S/4 → CFIN S/4 HANA → SideCar → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake → CIBR | SLT (×2) → ADF Rest API / SFTP(Blob) → Unity Catalog → Snowflake Connector / Snowpipe → Direct | Near Real-Time |
| 24 | SPAN Planning to ICOST | SPAN → ICOST | Denodo (Data Virtualization) | Batch |
| 25 | SPEED BOM to ECC | SPEED → SAP ECC | SAP PO | Event-Driven |
| 26 | SPEED BOM to EDW | SPEED → EDW | Direct | Batch |
| 27 | WorkStream Routes to ICOST | WorkStream → MARS → ICOST | Direct (×2) | Near Real-Time |

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 5.2 S/4 HANA — Future-State Application Landscape

#### Overview

The S/4 HANA architecture represents the **target** landscape for DS-020. Target S/4 HANA-based landscape with SAP PAPM for allocation, ECA lakehouse for analytics, and Power BI for self-service reporting.This view is generated from `R3_FutureFlows.xlsx` (114 flow hops across 22 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '16px', 'fontFamily': 'Segoe UI, Arial, sans-serif'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        DS020F_ATCR["📦 ATCR"]:::app
        DS020F_CFIN_S_4_HANA["📦 CFIN S/4 HANA"]:::app
        DS020F_Capacity_Forecast_Data_Store["📦 Capacity Forecast Data Store"]:::app
        DS020F_Corp_IP_S_4_HANA["📦 Corp / IP S/4 HANA<br/><i>DEV</i>"]:::app
        DS020F_DMOCR["📦 DMOCR"]:::app
        DS020F_DXCR["📦 DXCR"]:::app
        DS020F_ECA_ADLS["📦 ECA-ADLS"]:::app
        DS020F_ECA_DataBricks["📦 ECA-DataBricks"]:::app
        DS020F_ECA_SnowFlake["📦 ECA-SnowFlake"]:::app
        DS020F_ECM_Windchill["📦 ECM (Windchill)"]:::app
        DS020F_FCS["📦 FCS<br/><i>EOL</i>"]:::eol
        DS020F_GraphiteConnect["📦 GraphiteConnect"]:::app
        DS020F_ICS_Phoenix["📦 ICS (Phoenix)"]:::app
        DS020F_IF_Blue_Yonder["📦 IF Blue Yonder"]:::app
        DS020F_IF_PDH_Consumptional["📦 IF PDH Consumptional"]:::app
        DS020F_IF_PDH_Foundational["📦 IF PDH Foundational"]:::app
        DS020F_IF_PDH_Raw["📦 IF PDH Raw"]:::app
        DS020F_IF_S_4_HANA["📦 IF S/4 HANA<br/><i>DEV</i>"]:::app
        DS020F_IP_Blue_Yonder["📦 IP Blue Yonder"]:::app
        DS020F_IP_PDH_Consumptional["📦 IP PDH Consumptional<br/><i>DEV</i>"]:::app
        DS020F_IP_PDH_Foundational["📦 IP PDH Foundational<br/><i>DEV</i>"]:::app
        DS020F_IP_PDH_Raw["📦 IP PDH Raw<br/><i>DEV</i>"]:::app
        DS020F_MARS["📦 MARS"]:::app
        DS020F_MES_300["📦 MES 300"]:::app
        DS020F_PDF_SMH["📦 PDF-SMH<br/><i>DEV</i>"]:::app
        DS020F_PDH_Consumptional["📦 PDH Consumptional"]:::app
        DS020F_PDH_Foundational["📦 PDH Foundational"]:::app
        DS020F_PDH_Raw["📦 PDH Raw"]:::app
        DS020F_PDM_Translator["📦 PDM Translator"]:::app
        DS020F_Power_BI_DARC["📦 Power BI (DARC)"]:::app
        DS020F_SAP_Ariba["📦 SAP Ariba"]:::app
        DS020F_SAP_BOBJ["📦 SAP BOBJ<br/><i>EOL</i>"]:::eol
        DS020F_SAP_IBP["📦 SAP IBP"]:::app
        DS020F_SAP_PAPM["📦 SAP PAPM<br/><i>DEV</i>"]:::app
        DS020F_SAP_S_4_MDG["📦 SAP S/4 MDG"]:::app
        DS020F_SAP_SAC["📦 SAP SAC"]:::app
        DS020F_SCS["📦 SCS<br/><i>EOL</i>"]:::eol
        DS020F_SPEED["📦 SPEED"]:::app
        DS020F_SideCar["📦 SideCar"]:::app
        DS020F_WSPW["📦 WSPW"]:::app
        DS020F_WorkStream["📦 WorkStream"]:::app
        DS020F_XEUS["📦 XEUS"]:::app
    end

    DS020F_MES_300 -->|"Direct"| DS020F_XEUS
    DS020F_XEUS -->|"Direct"| DS020F_PDF_SMH
    DS020F_PDF_SMH -->|"EAI Connector"| DS020F_IF_S_4_HANA
    DS020F_IF_S_4_HANA -->|"SLT"| DS020F_CFIN_S_4_HANA
    DS020F_WorkStream -->|"Direct"| DS020F_MARS
    DS020F_MARS -->|"Direct"| DS020F_PDF_SMH
    DS020F_ECM_Windchill -->|"PDM Translator"| DS020F_PDM_Translator
    DS020F_PDM_Translator -->|"PDM Translator"| DS020F_SAP_S_4_MDG
    DS020F_SAP_S_4_MDG -->|"DRF (Data Replication Frame..."| DS020F_IF_S_4_HANA
    DS020F_SAP_S_4_MDG -->|"DRF (Data Replication Frame..."| DS020F_Corp_IP_S_4_HANA
    DS020F_SPEED -->|"PDM Translator"| DS020F_PDM_Translator
    DS020F_SPEED -->|"ADF Rest API / SFTP(Blob)"| DS020F_ECA_ADLS
    DS020F_ECA_ADLS -->|"Unity Catalog"| DS020F_ECA_DataBricks
    DS020F_ECA_DataBricks -->|"Snowflake Connector / Snowpipe"| DS020F_ECA_SnowFlake
    DS020F_GraphiteConnect -->|"MuleSoft & Reltio"| DS020F_SAP_S_4_MDG
    DS020F_IF_S_4_HANA -->|"SLT"| DS020F_SideCar
    DS020F_Corp_IP_S_4_HANA -->|"SLT"| DS020F_SideCar
    DS020F_CFIN_S_4_HANA -->|"SLT"| DS020F_SideCar
    DS020F_SideCar -->|"ADF Rest API / SFTP(Blob)"| DS020F_ECA_ADLS
    DS020F_FCS -->|"Direct"| DS020F_Capacity_Forecast_Data_Store
    DS020F_Capacity_Forecast_Data_Store -->|"ADF / DB Unity Catalog / Th..."| DS020F_ECA_ADLS
    DS020F_ECA_SnowFlake -->|"MuleSoft/BODS"| DS020F_IF_S_4_HANA
    DS020F_ICS_Phoenix -->|"Direct"| DS020F_Capacity_Forecast_Data_Store
    DS020F_ATCR -->|"Direct"| DS020F_Capacity_Forecast_Data_Store
    DS020F_SCS -->|"Direct"| DS020F_Capacity_Forecast_Data_Store
    DS020F_DXCR -->|"Direct"| DS020F_Capacity_Forecast_Data_Store
    DS020F_DMOCR -->|"Direct"| DS020F_Capacity_Forecast_Data_Store
    DS020F_WSPW -->|"Direct"| DS020F_ECA_SnowFlake
    DS020F_IF_Blue_Yonder -->|"ADF / DB Unity Catalog / Co..."| DS020F_IF_PDH_Raw
    DS020F_IF_PDH_Raw -->|"ADF / DB Unity Catalog / Th..."| DS020F_IF_PDH_Foundational
    DS020F_IF_PDH_Foundational -->|"Unity Catalog"| DS020F_IF_PDH_Consumptional
    DS020F_IF_PDH_Consumptional -->|"Snowflake Connector / Snowpipe"| DS020F_ECA_SnowFlake
    DS020F_ECA_SnowFlake -->|"Remote Function Adapter / M..."| DS020F_SAP_PAPM
    DS020F_IP_Blue_Yonder -->|"ADF / DB Unity Catalog / Co..."| DS020F_IP_PDH_Raw
    DS020F_IP_PDH_Raw -->|"ADF / DB Unity Catalog / Th..."| DS020F_IP_PDH_Foundational
    DS020F_IP_PDH_Foundational -->|"Unity Catalog"| DS020F_IP_PDH_Consumptional
    DS020F_IP_PDH_Consumptional -->|"Snowflake Connector / Snowpipe"| DS020F_ECA_SnowFlake
    DS020F_PDH_Raw -->|"ADF / DB Unity Catalog / Th..."| DS020F_IP_PDH_Foundational
    DS020F_PDH_Foundational -->|"Unity Catalog"| DS020F_IP_PDH_Consumptional
    DS020F_PDH_Consumptional -->|"Snowflake Connector / Snowpipe"| DS020F_ECA_SnowFlake
    DS020F_ECA_SnowFlake -->|"MuleSoft/BODS"| DS020F_Corp_IP_S_4_HANA
    DS020F_SAP_SAC -->|"SAC Data Export Service (AP..."| DS020F_ECA_SnowFlake
    DS020F_SAP_SAC -->|"SAP Odata services with con..."| DS020F_IF_S_4_HANA
    DS020F_SAP_SAC -->|"SAP Odata services with con..."| DS020F_Corp_IP_S_4_HANA
    DS020F_ECA_SnowFlake -->|"MuleSoft/BODS"| DS020F_CFIN_S_4_HANA
    DS020F_SAP_SAC -->|"SAP Odata services with con..."| DS020F_CFIN_S_4_HANA
    DS020F_SAP_PAPM -->|"SAP Integration Suite / Sma..."| DS020F_IF_S_4_HANA
    DS020F_SAP_PAPM -->|"SAP Integration Suite / Sma..."| DS020F_Corp_IP_S_4_HANA
    DS020F_SAP_IBP -->|"ADF / DB Unity Catalog / Co..."| DS020F_IF_PDH_Raw
    DS020F_SAP_Ariba -->|"Apigee / MuleSoft"| DS020F_IF_S_4_HANA
    DS020F_SAP_Ariba -->|"Apigee / MuleSoft"| DS020F_Corp_IP_S_4_HANA
    DS020F_ECA_SnowFlake -->|"Snowflake Connector / Snowpipe"| DS020F_Power_BI_DARC
    DS020F_SideCar --> DS020F_SAP_BOBJ

    click DS020F_CFIN_S_4_HANA href "https://iapm.intel.com/#/app/41052" "CFIN S/4 HANA -- IAPM #41052" _blank
    click DS020F_Capacity_Forecast_Data_Store href "https://iapm.intel.com/#/app/37284" "Capacity Forecast Data Store -- IAPM #37284" _blank
    click DS020F_Corp_IP_S_4_HANA href "https://iapm.intel.com/#/app/41363" "Corp / IP S/4 HANA -- IAPM #41363" _blank
    click DS020F_DMOCR href "https://iapm.intel.com/#/app/13284" "DMOCR -- IAPM #13284" _blank
    click DS020F_DXCR href "https://iapm.intel.com/#/app/13284" "DXCR -- IAPM #13284" _blank
    click DS020F_ECA_ADLS href "https://iapm.intel.com/#/app/43119" "ECA-ADLS -- IAPM #43119" _blank
    click DS020F_ECA_DataBricks href "https://iapm.intel.com/#/app/43119" "ECA-DataBricks -- IAPM #43119" _blank
    click DS020F_ECA_SnowFlake href "https://iapm.intel.com/#/app/43119" "ECA-SnowFlake -- IAPM #43119" _blank
    click DS020F_ECM_Windchill href "https://iapm.intel.com/#/app/38775" "ECM (Windchill) -- IAPM #38775" _blank
    click DS020F_FCS href "https://iapm.intel.com/#/app/9297" "FCS -- IAPM #9297" _blank
    click DS020F_GraphiteConnect href "https://iapm.intel.com/#/app/36398" "GraphiteConnect -- IAPM #36398" _blank
    click DS020F_ICS_Phoenix href "https://iapm.intel.com/#/app/19477" "ICS (Phoenix) -- IAPM #19477" _blank
    click DS020F_IF_Blue_Yonder href "https://iapm.intel.com/#/app/41040" "IF Blue Yonder -- IAPM #41040" _blank
    click DS020F_IF_PDH_Consumptional href "https://iapm.intel.com/#/app/40747" "IF PDH Consumptional -- IAPM #40747" _blank
    click DS020F_IF_PDH_Foundational href "https://iapm.intel.com/#/app/40747" "IF PDH Foundational -- IAPM #40747" _blank
    click DS020F_IF_PDH_Raw href "https://iapm.intel.com/#/app/40747" "IF PDH Raw -- IAPM #40747" _blank
    click DS020F_IF_S_4_HANA href "https://iapm.intel.com/#/app/41363" "IF S/4 HANA -- IAPM #41363" _blank
    click DS020F_IP_Blue_Yonder href "https://iapm.intel.com/#/app/41039" "IP Blue Yonder -- IAPM #41039" _blank
    click DS020F_IP_PDH_Consumptional href "https://iapm.intel.com/#/app/40750" "IP PDH Consumptional -- IAPM #40750" _blank
    click DS020F_IP_PDH_Foundational href "https://iapm.intel.com/#/app/40750" "IP PDH Foundational -- IAPM #40750" _blank
    click DS020F_IP_PDH_Raw href "https://iapm.intel.com/#/app/40750" "IP PDH Raw -- IAPM #40750" _blank
    click DS020F_MARS href "https://iapm.intel.com/#/app/33537" "MARS -- IAPM #33537" _blank
    click DS020F_MES_300 href "https://iapm.intel.com/#/app/41275" "MES 300 -- IAPM #41275" _blank
    click DS020F_PDF_SMH href "https://iapm.intel.com/#/app/59283" "PDF-SMH -- IAPM #59283" _blank
    click DS020F_PDH_Consumptional href "https://iapm.intel.com/#/app/40747" "PDH Consumptional -- IAPM #40747" _blank
    click DS020F_PDH_Foundational href "https://iapm.intel.com/#/app/40747" "PDH Foundational -- IAPM #40747" _blank
    click DS020F_PDH_Raw href "https://iapm.intel.com/#/app/40747" "PDH Raw -- IAPM #40747" _blank
    click DS020F_Power_BI_DARC href "https://iapm.intel.com/#/app/63659" "Power BI (DARC) -- IAPM #63659" _blank
    click DS020F_SAP_Ariba href "https://iapm.intel.com/#/app/19569" "SAP Ariba -- IAPM #19569" _blank
    click DS020F_SAP_BOBJ href "https://iapm.intel.com/#/app/11377" "SAP BOBJ -- IAPM #11377" _blank
    click DS020F_SAP_IBP href "https://iapm.intel.com/#/app/40709" "SAP IBP -- IAPM #40709" _blank
    click DS020F_SAP_PAPM href "https://iapm.intel.com/#/app/41401" "SAP PAPM -- IAPM #41401" _blank
    click DS020F_SAP_SAC href "https://iapm.intel.com/#/app/37401" "SAP SAC -- IAPM #37401" _blank
    click DS020F_SAP_S_4_MDG href "https://iapm.intel.com/#/app/40068" "SAP S/4 MDG -- IAPM #40068" _blank
    click DS020F_SCS href "https://iapm.intel.com/#/app/21327" "SCS -- IAPM #21327" _blank
    click DS020F_SPEED href "https://iapm.intel.com/#/app/31517" "SPEED -- IAPM #31517" _blank
    click DS020F_SideCar href "https://iapm.intel.com/#/app/42993" "SideCar -- IAPM #42993" _blank
    click DS020F_WSPW href "https://iapm.intel.com/#/app/4119" "WSPW -- IAPM #4119" _blank
    click DS020F_WorkStream href "https://iapm.intel.com/#/app/37871" "WorkStream -- IAPM #37871" _blank
    click DS020F_XEUS href "https://iapm.intel.com/#/app/35612" "XEUS -- IAPM #35612" _blank

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq9W4tu27gS_RVCQTZZIInl9wNFANmyWy_sRojSbRabC0Gx6FiILAmSvElum3-_pEhJ1JuKuzcFimaGcw45HI44JPtD2DgGFCbC6ekP0zaDCfhxFuzgHp5NwNmj7sOzC3Dmw83BM4O3FfwHWlhhOQ7RhE3_1D1Tf7Sgf4att44dqOZ_Q4D2wH3FzbBsoe9N6w1LVfjkQPBteQEkZGhdAF-3_Usfeub27B23tpyXzU73ghDv4MO1_vrdNIId-n2rWz5EbXbB3lrpj9DCpIF3wDIbjUR19Y1pPyFhT0QiT7efE1FffH8H76enD3ZMAe6mDzZAP6en4PISdWizM9d6AC9N23dNDxrAD94sCDaW7vvQR21I8_B3GW7B48E3bej7IPzZmpY1OVmgn2n_wg885xlOTqaj0UCc0l8vX_BIJh339WLjWI43ORFFMYOpuy5IfgjmtI9RY0xRHA6ngwaYhh7oeUx5VIPZTmFGOkP3kfM8_Q35FPQzTHvTMCz4onuQ9Yg8kBKPzIeDRYLG0XvoWDmPYB8zXp7NRLEOk6D6h8cnT3d3QFr9_SA8HIxR10B_G90-kBRltZxJd8ubr2Al_TW_fRD-Q4zwj4ECYhOYjg1Wt4lUVsWOuNCku9ktC7eBA4BlCGEymaApzVnMFsuvmqr1tC_SVylripVAbfUAVlZg6Di6gzdt4aC-6X6gyWiiNTVAv-YgaVsQtQW4LQjbVjA4nqstlfKOIj1ogaUS9_bTo9e6_mRey_M_P7XM63JoeX2T91korLC5LzC5r7KYzyRNkldq1grJL7G82hK7aOqZm2e_yD7RVqOotvOysPRnWAQSK6sw1tp30zZQdrKsPMYanMfa38tRFrOcE5Aomq75zSqZLrTgcuaf8aIxAzhzbButgyxURl3ejeVM1ZSdA23zNYuBVOCc6ioGslxoU-sAtb8c24BeDmQBsBYQbSWKIn9BAW77h72L17VuFWChNiDVphZx4RxslG-rANkmtXi3-ksJDNJUWpctWmTeeLWiHFDldIXT6QqH05W805t0s3YOlNwcNIUvmhIlmhJusLV0m1uRWFZhMVe1rijmjOYqQOJyO0VGwbD-krVD4ksk5u5w7dQ1WCx1s8S_TEompHaBKPJau0NbRN_S0Tcwb74GibYCxXmBnjZdarJ0O8uBYCWYLsE51lakNFVSNLQdftSzCEgBQkW17fRm-keRKZZzZ3gMtJwqRThIXN0BRVLWRYZYzh1fGAjnrLX8uQgL5yykqrGXZoW20qzCLv9lVBt8GVVlPpdzAFhYQWkacKbnoo6Ky-2-q8r3rBGWVVg43rMaeFDf5-xiTbn1_fxbzjdYlrGAthHtr9OpCpVM1z8fBDncOz8IP1ncVHssKGtM01eqPZVRk7m0BHTngRfrz4KPYMqakVMEdXXH2KU25ynLxGllvQ1TuJ3J802GltruUcNsOvpZnMUyLmJVdUDM4kuhMPJoELcLlNBw8XALXcvchBkaLDx9D6-urji8fwRkth5J4-I1d4TDWHtJXqC-oCpJUpaowFEXd8r51HIef2egotoiM3tESHG-2bjmmqGhWc5TxpapH-zSwiOKT1QmbHGZkMQ57haSuqYLM8BJTWGX7-Ap8PpgQdXZBuA3NF4L-Z0jJuqWT5TG7IpKkt-QXYvcVlR27GyiCqls6VYV3-kBVDRk-tcC8hSkwgWJ7nbp-C8NuXjKM9Pamt7IKk9GTMqyoweMDz6OBlF_gefx0cDxIPhI4mgU_JEuAylfsulSty5YZk4u_9LNcRaUiptGX0GFW4TM6mvSYFEVXgSZavDrUmLRyrmFeyeAYHGwyWmfZOhuADH0Ou2NaN-b7q9y1IwpxTOmfHjGlJoZUxrPmFI3Y8q_OWP_kh9-tRP-zzFblu2rt0ukXIp6hv4V7sDmr67jBUCF3j_mBoJzScl_gop7lgVUwE148eATKB-8mMEObBy7wTaxOVzlmBs5r7QI-GjPKgFxKmEQl3YAnzyyEVYPaNuG42Sv87vuI3i18bKcKr_oKxQfeUR4rvkEcaei6eAcJi9G47DgXqqpI6CyTWj2tCYqlzeo2nku3uruPLgFD8IuCFx_0mqZuru_MtEsWlcbZ986aaHqu9Vri_3Og4Capa6M8G3mEs__SdRAe7R0-7mIs2p3ytOF7rAz6pEuVFwxJT2K2pf3KFsp8DmiO-iSXuSupFhvkFal3GSzx0PY7kbDjjaIlCNSlHPcN6e4b8QQ16Bcnuu22-OQJboTY_xFdZVMTK3anC9V6DZhTZZrc1J2qfNzsqcyXAtjNBz2KWfqjo5ZC7RJKSuuP3m4xp3xMKQiBSuFp9JS9OyJANeoBt3xKKTKnydEo6JNSnnZYpNrIYx7QzK81BUhsyJog3LGdCHFmVp7IiFNXSmmcmvYooo1vxHk4haHvWHEnbtVYXpA29X1ILW1_VAHMpvjhvx4x_4hWrLVb8D2wY8GcyXa4GuRKfY4o6pLElH6zjQVVd1xDeuHo6ovRtzVUdUXOXrwkahKd6A0qrj4G0RVmjYbVdVs4fk9V2rs9rskeumRf5QPqbycgV6W8AVQh35V6LUvGzmd6q9JdGnCw9Mfd0ZkbdBr4oQnUlXwHJf0jsl4R6a7I3LdxxJd8yyXqje42AbdQZ8kncyNdMIaNSllTWotvi92f0AY4xts9mtNlJVcuEjio2p36eYguvFmmKiukgnXtJxzJiZjIpVwMmdi7YjCgpxviffEdkxE6_h4jRNdJRM-m-Ar3VgicqIRV2k8PPQSj8974mCUcJG7fNaDRF3Ox7kT7qDqiIYDuxWOxOX44eUfl9fa_TZloBeGkc-oopyDngdw-aszHpP8m5wiRL6iqlKe8LKBL9JoVUSvJ-Igq66FmEtwvjAbDUmYpW7P40gj2lK28GkAF09_0CaHIfQ1QcRA5REDfQgcPu2erphn2wux7tk2ayrFpiLP6-zcA-QVfIK2kXpdYYhgNf88_ypzvDxeaZKSe6wjufH1ecGjjpW2Tr0eMdpDsI4fbBOD5AE3ayfPr1mmTY-eFduBGbwRQ3wCyprMb8gD687A6KGGxqWzvVyZW5h5SBM-HUmcSpwSObaP_8SOHY_HuffpwoWwh95eNw1h8kMI_0eCMBEMuNUPViC8Xwj6IXDUN3sjTML_KCAcXNRRKJs6moQ9Eb7_D-zpwGw=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 27</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### S/4 HANA Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | Ariba Procurement to S/4 | SAP Ariba → IF S/4 HANA → Corp / IP S/4 HANA | Apigee / MuleSoft (×2) | Event-Driven |
| 2 | Blue Yonder Demand to ECA | IF Blue Yonder → IF PDH Raw / IP PDH Raw → IF PDH Foundational / IP PDH Foundational → IF PDH Consumptional / IP PDH Consumptional → ECA-SnowFlake → SAP PAPM → IF S/4 HANA → Corp / IP S/4 HANA | ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule) (×6) → ADF / DB Unity Catalog / Third Party (e.g., Denodo) (×6) → Unity Catalog (×6) → Snowflake Connector / Snowpipe (×6) → Remote Function Adapter / MuleSoft / SAP Integration Suite (×4) → MuleSoft/BODS (×2) | NRT / Batch / On demand |
| 3 | Data Products to Power BI | ECA-SnowFlake → Power BI (DARC) | Snowflake Connector / Snowpipe | Batch / On-demand |
| 4 | ECM to S/4 via MDG | ECM (Windchill) → PDM Translator → SAP S/4 MDG → IF S/4 HANA → Corp / IP S/4 HANA | PDM Translator (×2) → DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC) (×2) | Batch / On-demand |
| 5 | ERP to SideCar | IF S/4 HANA → SideCar | SLT (×3) | Trigger based (SLT) |
| 6 | Factory Rpt to ECA (ATCR) | ATCR → Capacity Forecast Data Store → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake → IF S/4 HANA | Direct → ADF / DB Unity Catalog / Third Party (e.g., Denodo) → Unity Catalog → Snowflake Connector / Snowpipe → MuleSoft/BODS | Batch / On-demand |
| 7 | Factory Rpt to ECA (DMOCR) | DMOCR → Capacity Forecast Data Store → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake → IF S/4 HANA | Direct → ADF / DB Unity Catalog / Third Party (e.g., Denodo) → Unity Catalog → Snowflake Connector / Snowpipe → MuleSoft/BODS | Batch / On-demand |
| 8 | Factory Rpt to ECA (DXCR) | DXCR → Capacity Forecast Data Store → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake → IF S/4 HANA | Direct → ADF / DB Unity Catalog / Third Party (e.g., Denodo) → Unity Catalog → Snowflake Connector / Snowpipe → MuleSoft/BODS | Batch / On-demand |
| 9 | Factory Rpt to ECA (FCS) | FCS → Capacity Forecast Data Store → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake → IF S/4 HANA | Direct → ADF / DB Unity Catalog / Third Party (e.g., Denodo) → Unity Catalog → Snowflake Connector / Snowpipe → MuleSoft/BODS | Batch / On-demand |
| 10 | Factory Rpt to ECA (ICS) | ICS (Phoenix) → Capacity Forecast Data Store → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake → IF S/4 HANA | Direct → ADF / DB Unity Catalog / Third Party (e.g., Denodo) → Unity Catalog → Snowflake Connector / Snowpipe → MuleSoft/BODS | Batch / On-demand |
| 11 | Factory Rpt to ECA (SCS) | SCS → Capacity Forecast Data Store → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake → IF S/4 HANA | Direct → ADF / DB Unity Catalog / Third Party (e.g., Denodo) → Unity Catalog → Snowflake Connector / Snowpipe → MuleSoft/BODS | Batch / On-demand |
| 12 | GraphiteConnect Vendor MD | GraphiteConnect → SAP S/4 MDG → IF S/4 HANA → Corp / IP S/4 HANA | MuleSoft & Reltio → DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC) (×2) | Batch / On-demand |
| 13 | IBP to ECA (Legacy Overlap) | SAP IBP → IF PDH Raw → IF PDH Foundational → IF PDH Consumptional → ECA-SnowFlake → SAP PAPM | ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule) (×2) → ADF / DB Unity Catalog / Third Party (e.g., Denodo) (×2) → Unity Catalog (×2) → Snowflake Connector / Snowpipe (×2) → Remote Function Adapter / MuleSoft / SAP Integration Suite | NRT / Batch / On demand |
| 14 | MES Routes to S/4 | MES 300 → XEUS → PDF-SMH → IF S/4 HANA → CFIN S/4 HANA | Direct (×2) → EAI Connector → SLT | Batch / On-demand |
| 15 | SAC Planning to S/4 | SAP SAC → ECA-SnowFlake → IF S/4 HANA → Corp / IP S/4 HANA → CFIN S/4 HANA → IF S/4 HANA → Corp / IP S/4 HANA → CFIN S/4 HANA | SAC Data Export Service (API) - Direct Write (Speed Layer in Snowflake / Use ADF / MuleSoft for DataBricks (×3) → MuleSoft/BODS (×3) → SAP Odata services with connector (×3) | Batch / On-demand |
| 16 | SAP PAPM to S/4 | SAP PAPM → IF S/4 HANA → Corp / IP S/4 HANA | SAP Integration Suite / Smart Data Integration/BTP Destinations (HTTP) (×2) | Batch / On-demand |
| 17 | SPEED BOMs to ECA | SPEED → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake | ADF Rest API / SFTP(Blob) → Unity Catalog → Snowflake Connector / Snowpipe | Batch / On-demand |
| 18 | SPEED to S/4 via MDG | SPEED → PDM Translator → SAP S/4 MDG → IF S/4 HANA → Corp / IP S/4 HANA | PDM Translator (×2) → DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC) (×2) | Batch / On-demand |
| 19 | SideCar to ECA | SideCar → ECA-ADLS → ECA-DataBricks → ECA-SnowFlake | ADF Rest API / SFTP(Blob) → Unity Catalog → Snowflake Connector / Snowpipe | NRT / Batch / On-demand |
| 20 | SideCar to SAP BOBJ | SideCar → SAP BOBJ | - | - |
| 21 | WSPW Direct to ECA | WSPW → ECA-SnowFlake → IF S/4 HANA | Direct → MuleSoft/BODS | Batch / On-demand |
| 22 | WorkStream Routes to S/4 | WorkStream → MARS → PDF-SMH → IF S/4 HANA → CFIN S/4 HANA | Direct (×2) → EAI Connector → SLT | Batch / On-demand |

<div class="page-footer"><span>Page 28</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 5.3 Change Impact Summary

| Change Type | Flow Chain | Detail |
|-------------|-----------|--------|
| **NEW** | Ariba Procurement to S/4 | Added in future state |
| **NEW** | Blue Yonder Demand to ECA | Added in future state |
| **NEW** | Data Products to Power BI | Added in future state |
| **NEW** | ECM to S/4 via MDG | Added in future state |
| **NEW** | ERP to SideCar | Added in future state |
| **NEW** | Factory Rpt to ECA (ATCR) | Added in future state |
| **NEW** | Factory Rpt to ECA (DMOCR) | Added in future state |
| **NEW** | Factory Rpt to ECA (DXCR) | Added in future state |
| **NEW** | Factory Rpt to ECA (FCS) | Added in future state |
| **NEW** | Factory Rpt to ECA (ICS) | Added in future state |
| **NEW** | Factory Rpt to ECA (SCS) | Added in future state |
| **NEW** | GraphiteConnect Vendor MD | Added in future state |
| **NEW** | IBP to ECA (Legacy Overlap) | Added in future state |
| **NEW** | MES Routes to S/4 | Added in future state |
| **NEW** | SAC Planning to S/4 | Added in future state |
| **NEW** | SAP PAPM to S/4 | Added in future state |
| **NEW** | SPEED BOMs to ECA | Added in future state |
| **NEW** | SPEED to S/4 via MDG | Added in future state |
| **NEW** | SideCar to ECA | Added in future state |
| **NEW** | SideCar to SAP BOBJ | Added in future state |
| **NEW** | WSPW Direct to ECA | Added in future state |
| **NEW** | WorkStream Routes to S/4 | Added in future state |
| **REMOVED** | ATM Cycle Times to ICOST | Not present in future state |
| **REMOVED** | CIBR Inv to ICOST | Not present in future state |
| **REMOVED** | CIBR RM Inv to ECC | Not present in future state |
| **REMOVED** | COMPASS LRP to ICOST | Not present in future state |
| **REMOVED** | DCS MyDeals to ICOST | Not present in future state |
| **REMOVED** | ECA Costing Chain | Not present in future state |
| **REMOVED** | ECC BOH to EDW | Not present in future state |
| **REMOVED** | ECC GL to EDW | Not present in future state |
| **REMOVED** | ECC Replication to ECA | Not present in future state |
| **REMOVED** | ECC to EDW Reporting | Not present in future state |
| **REMOVED** | ECC to Finance HANA | Not present in future state |
| **REMOVED** | EDW Feedback to CIBR | Not present in future state |
| **REMOVED** | EDW Feedback to ICOST | Not present in future state |
| **REMOVED** | FCA to ICOST | Not present in future state |
| **REMOVED** | Finance HANA to BOBJ | Not present in future state |
| **REMOVED** | GL Posting to CFIN | Not present in future state |
| **REMOVED** | GL Posting to ECC | Not present in future state |
| **REMOVED** | IBP Demand Planning (Legacy) | Not present in future state |
| **REMOVED** | MES Route to ICOST | Not present in future state |
| **REMOVED** | Master Data to ECC | Not present in future state |
| **REMOVED** | RM Std Cost Update to ECC | Not present in future state |
| **REMOVED** | RM Std Fluctuations Alert | Not present in future state |
| **REMOVED** | S/4 Inv. Mvt to CIBR | Not present in future state |
| **REMOVED** | SPAN Planning to ICOST | Not present in future state |
| **REMOVED** | SPEED BOM to ECC | Not present in future state |
| **REMOVED** | SPEED BOM to EDW | Not present in future state |
| **REMOVED** | WorkStream Routes to ICOST | Not present in future state |

**Totals**: 22 new - 27 removed - 0 modified - 0 unchanged

### 5.4 Component Overview

#### System Inventory

| System | IAPM ID | Status |
|--------|---------|--------|
| APIGEE | 22790 | Deployed |
| ATCR | - | N/A |
| BOBJ | 17651 | Deployed |
| CFIN S/4 HANA | 42993 | Deployed |
| CIBR | 237 | Deployed |
| COMPASS | 16439 | Deployed |
| Capacity Forecast Data Store | 37284 | Deployed |
| Corp / IP S/4 | 41363 | Developing |
| Corp / IP S/4 HANA | 41363 | Developing |
| DCS | 14464 | Deployed |
| DMOCR | 13284 | Deployed |
| DXCR | 13284 | Deployed |
| EATS | 119 | End of Life |
| ECA | 43119 | Deployed |
| ECA-ADLS | 25794 | Deployed |
| ECA-DataBricks | 41458 | Deployed |
| ECA-SnowFlake | 35811 | Deployed |
| ECM (Windchill) | 38775 | Deployed |
| EDW | 4010 | Deployed |
| FCA | 44990 | Deployed |
| FCS | 9297 | End of Life |
| Finance HANA | 42993 | Deployed |
| GraphiteConnect | 36398 | Deployed |
| ICOST | 9008 | Deployed |
| ICS (Phoenix) | 19477 | Deployed |
| IF Blue Yonder | 41040 | Deployed |
| IF PDH Consumptional | 40747 | Deployed |
| IF PDH Foundational | 40747 | Deployed |
| IF PDH Raw | 40747 | Deployed |
| IF S/4 HANA | 41363 | Developing |
| IP Blue Yonder | 41039 | Deployed |
| IP PDH Consumptional | 40750 | Developing |
| IP PDH Foundational | 40750 | Developing |
| IP PDH Raw | 40750 | Developing |
| Legacy MDG | 40068 | Deployed |
| MARS | 33537 | Deployed |
| MES 300 | 41275 | Deployed |
| PDF-SMH | 59283 | Developing |
| PDH Consumptional | 40747 | Deployed |
| PDH Foundational | 40747 | Deployed |
| PDH Raw | 40747 | Deployed |
| PDM Translator | - | N/A |
| PEGA | 43163 | Deployed |
| Power BI (DARC) | 63659 | Deployed |
| SAP Ariba | 19569 | Deployed |
| SAP BOBJ | 11377 | End of Life |
| SAP ECC | 21195 | Deployed |
| SAP IBP | 40709 | Deployed |
| SAP ICX | 21195 | Deployed |
| SAP PAPM | 41401 | Developing |
| SAP PO | 21195 | Deployed |
| SAP S/4 MDG | 40068 | Deployed |
| SAP SAC | 37401 | Deployed |
| SCS | 21327 | End of Life |
| SPAN | 21159 | Deployed |
| SPEED | 31517 | Deployed |
| SideCar | 42993 | Deployed |
| WSPW | 4119 | Deployed |
| WorkStream | 37871 | Deployed |
| XEUS | 35612 | Deployed |

<div class="page-footer"><span>Page 29</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| FPRI1704 | Interface | Automated Tool MUP Excess Capacity calculation and associated PCOS/OCOS Split... | 10. Object Complete |  | BODS | 03.Medium |
| FPRI1439 | Interface | Receive planned production quantities per production version from ECA to S/4 ... | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1288 | Interface | Activity Inbound interface from ECA to S4 IP | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1287 | Interface | Production quantity update in WAC custom table from ECA to S4 IF | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1273 | Interface | Activity Quantity Inbound interface from ECA to S4 IF | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI0704 | Interface | IF-IP Integration Actual Cost - Inbound Interface | 10. Object Complete | OpenText → S/4 | SFT | 02.High |
| FPRI0703 | Interface | IF-IP Integration Actual Cost - Outbound Interface | 10. Object Complete | S/4 → OpenText | SFT | 02.High |
| FPRI0554 | Interface | SKF Interface to get file from ECA and send to S4 via BODS - IF | 10. Object Complete | ECA → S/4 | MuleSoft | 02.High |
| FPRI0545 | Interface | IF-IP Integration - Interface to send Cost Idoc from S4 If to S4 IP | 10. Object Complete | S/4 → S/4 | SFT | 03.Medium |
| FPRI0544 | Interface | IF-IP Integration - Interface to receive Cost Idoc from S4 If to S4 IP | 10. Object Complete | S/4 → S/4 | SFT | 03.Medium |
| FPRE1620_IP | Enhancement | Implement OSS Note 2358961 to allow COGS split based on Aux CCS at time of de... | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE1620_IF | Enhancement | Implement OSS Note 2358961 to allow COGS split based on Aux CCS at time of de... | 99. Rejected/Cancelled/On Hold |  | NA | 04.Low |
| FPRE1438 | Enhancement | Update mixing ratio for Procurement alternative for Cross site transfer based... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1419 | Enhancement | Update Procurement alternatives based on production version & PIR for cross s... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1328 | Enhancement | Legal Valuation standard cost calculation enhancement | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE0702 | Enhancement | Calculation of variance to be loaded for Group Actual Costing | 10. Object Complete |  | NA | 03.Medium |
| FPRE0701_IP | Enhancement | Mixed Costing ratio auto update | 10. Object Complete |  | NA | 03.Medium |
| FPRE0701_IF | Enhancement | Mixed Costing ratio auto update | 10. Object Complete |  | NA | 04.Low |
| FPRE0700_IP | Enhancement | Representative material ID – Q2-Q8 Forecast | 10. Object Complete |  | NA | 03.Medium |
| FPRE0700_IF | Enhancement | Representative material ID – Q2-Q8 Forecast | 10. Object Complete |  | NA | 04.Low |
| FPRE0699 | Enhancement | Enhancement for Excess Capacity – Fixed Spending Adjustment | 10. Object Complete |  | NA | 02.High |
| FPRE0698 | Enhancement | Legal Valuation standard cost calculation enhancement | 10. Object Complete |  | NA | 04.Low |
| FPRE0551 | Enhancement | SKF Actual Driver volume update from actual activity confirmation Automation | 10. Object Complete |  | NA | 03.Medium |
| FPRE0550 | Enhancement | Enhancement to update additive cost in IP based on Idoc of IF cost | 10. Object Complete |  | NA | 03.Medium |
| FPRE0549 | Enhancement | Enhancement to a) update Cost and Production volume in custom table, b) calcu... | 10. Object Complete |  | NA | 03.Medium |
| FPRC1493 | Conversion | Conversion of WIP values as per Component structure in S/4 - IP | 10. Object Complete |  | NA | 02.High |
| FPRC1491 | Conversion | Conversion of WIP values as per Component structure in S/4 - Back End IF | 10. Object Complete |  | NA | 02.High |

**Summary**: 10 Interfaces, 2 Conversions, 15 Enhancements

<div class="page-footer"><span>Page 30</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for DS-020:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | Point-to-Point | MES Route to ICOST | Direct | REST / IDoc | SSO / Certificate |
| 2 | Point-to-Point | MES Route to ICOST | Direct | REST / IDoc | SSO / Certificate |
| 3 | Point-to-Point | WorkStream Routes to ICOST | Direct | REST / IDoc | SSO / Certificate |
| 4 | Point-to-Point | WorkStream Routes to ICOST | Direct | REST / IDoc | SSO / Certificate |
| 5 | Point-to-Point | ATM Cycle Times to ICOST | Direct | REST / IDoc | SSO / Certificate |
| 6 | API-Led | SPEED BOM to ECC | SAP PO | REST / IDoc | SSO / Certificate |
| 7 | Point-to-Point | SPEED BOM to EDW | Direct | REST / IDoc | SSO / Certificate |
| 8 | API-Led | Master Data to ECC | DRF (Data Replicatio | REST / IDoc | SSO / Certificate |

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 31</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### 6.1.1 ICOST — Current-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph DS020CPLP_Azure_Cloud["☁️ Azure Cloud"]
        direction LR
        DS020CPLA_ECA["ECA"]:::appBox
        DS020CPLA_ECA_ADLS["ECA-ADLS"]:::appBox
        DS020CPLA_ECA_DataBricks["ECA-DataBricks"]:::appBox
        DS020CPLA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
    end
    style DS020CPLP_Azure_Cloud fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020CPLP_Google_Cloud_SaaS["☁️ Google Cloud (SaaS)"]
        direction LR
        DS020CPLA_APIGEE["APIGEE"]:::appBox
    end
    style DS020CPLP_Google_Cloud_SaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020CPLP_On_Prem_Linux["🖥️ On-Prem (Linux)"]
        direction LR
        DS020CPLA_CIBR["CIBR"]:::appBox
        DS020CPLA_COMPASS["COMPASS"]:::appBox
        DS020CPLA_EATS["EATS"]:::eolBox
        DS020CPLA_EDW["EDW"]:::appBox
        DS020CPLA_FCA["FCA"]:::appBox
        DS020CPLA_ICOST["ICOST"]:::appBox
        DS020CPLA_MES_300["MES 300"]:::appBox
        DS020CPLA_PEGA["PEGA"]:::appBox
        DS020CPLA_SPEED["SPEED"]:::appBox
        DS020CPLA_XEUS["XEUS"]:::appBox
    end
    style DS020CPLP_On_Prem_Linux fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020CPLP_On_Prem_Windows["🖥️ On-Prem (Windows)"]
        direction LR
        DS020CPLA_DCS["DCS"]:::appBox
        DS020CPLA_MARS["MARS"]:::appBox
        DS020CPLA_WorkStream["WorkStream"]:::appBox
    end
    style DS020CPLP_On_Prem_Windows fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020CPLP_SAP_BTP["☁️ SAP BTP"]
        direction LR
        DS020CPLA_SAP_IBP["SAP IBP"]:::appBox
    end
    style DS020CPLP_SAP_BTP fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020CPLP_SAP_HEC_On_Prem["🖥️ SAP HEC (On-Prem)"]
        direction LR
        DS020CPLA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
        DS020CPLA_Corp_IP_S_4["Corp / IP S/4"]:::appBox
        DS020CPLA_Finance_HANA["Finance HANA"]:::appBox
        DS020CPLA_SideCar["SideCar"]:::appBox
    end
    style DS020CPLP_SAP_HEC_On_Prem fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020CPLP_SAP_On_Prem_Linux["🖥️ SAP On-Prem (Linux)"]
        direction LR
        DS020CPLA_BOBJ["BOBJ"]:::appBox
        DS020CPLA_SAP_ECC["SAP ECC"]:::appBox
        DS020CPLA_SAP_ICX["SAP ICX"]:::appBox
    end
    style DS020CPLP_SAP_On_Prem_Linux fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020CPLP_Unassigned["📋 Other / Unassigned Platform"]
        direction LR
        DS020CPLA_Legacy_MDG["Legacy MDG"]:::appBox
        DS020CPLA_SAP_PO["SAP PO"]:::appBox
        DS020CPLA_SPAN["SPAN"]:::appBox
    end
    style DS020CPLP_Unassigned fill:#FFF9C4,stroke:#F9A825,stroke-width:2px,color:#5D4037

    DS020CPLP_On_Prem_Windows ==>|"Direct"| DS020CPLP_On_Prem_Linux
    DS020CPLP_On_Prem_Linux ==>|"SAP PO"| DS020CPLP_SAP_On_Prem_Linux
    DS020CPLP_SAP_On_Prem_Linux ==>|"SLT"| DS020CPLP_SAP_HEC_On_Prem
    DS020CPLP_SAP_HEC_On_Prem ==>|"ADF Rest API / SFTP(Blob)"| DS020CPLP_Azure_Cloud
    DS020CPLP_Azure_Cloud ==>|"Direct"| DS020CPLP_On_Prem_Linux
    DS020CPLP_Azure_Cloud ==>|"Internal"| DS020CPLP_On_Prem_Linux
    DS020CPLP_On_Prem_Linux ==>|"File based"| DS020CPLP_SAP_On_Prem_Linux
    DS020CPLP_On_Prem_Linux ==>|"JE Posting"| DS020CPLP_SAP_HEC_On_Prem
    DS020CPLP_SAP_On_Prem_Linux ==>|"ETL"| DS020CPLP_On_Prem_Linux
    DS020CPLP_SAP_HEC_On_Prem ==>|"APIGEE"| DS020CPLP_Google_Cloud_SaaS
    DS020CPLP_Google_Cloud_SaaS ==>|"APIGEE"| DS020CPLP_On_Prem_Linux
    DS020CPLP_SAP_HEC_On_Prem ==>|"Direct"| DS020CPLP_SAP_On_Prem_Linux
    DS020CPLP_SAP_BTP ==>|"Direct"| DS020CPLP_Azure_Cloud

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq9WGlv4joU_StWRhUdiWpSlpZGmidl7TCiJWroo9LjKTKJoVGNjbJMy7T893edhKUsE9KKx4d4O_fYPvd641XyuE8kRTo5eQ1YECvotRI_kgmpKKgyxBGpVFElIl4SBvGsQ34RKhoo51lLCv0bhwEeUhJVhPWIs9gJfqcE543pi4CJOgtPAjoTtQ4Zc4Lu21WkgiGtzAWC8mfvEYdxypFE5Aa_9AM_foTyCNOIAOYxntAOHhIqOorDRNQxGL0zxV7AxlDZkKEqxOxpVdWU53M0PzkZsGUXqKcNGIKfR3EUGWSE8HSq8Rc0CihVvmhNw7KsahSH_IkoX2T58lK7yItnz2JMSm36UvU45aForhvNTb4pxfGKUG-ZF_rVkrDeapl1_T1hfUV4rjXNmrxBSDhd8VmW1tSaSz5dl-G3d4AXF6J5wDLGKBmOQzx9RIYj12Td7tiu-jsJiatTnvj_DKRBUruQzwfJiMgjlDahtGkg_ZsxiJ8fhMSLA85Q525Vu6BUXVNXgQq-YKUoSibvHqCrGh0nQ5-J7CEmBo6xFgbeU5QbrioOMXcYf7YofiK59bK8bUyYnwsXzyjZrdqn3LzXLdecj2neg-tg7Gw6JwNk3kGnAvG1lJNUu31tmsCaZUrMfWtox1Ggy1w7JBO3E7DkJZ2936r78PVxM9egy84EBJ2mmHLz19vaHbCKpCho9O6NrTrCA3muMMrUXhrTkGTQbAHvhBp9gTT6RZxWuqis4kXV1rtOD6BpWgS-MR23LssAhxyCXJGBbV6LcYikCOrYpmkANk2LwA_mvZBMJCVC8V2MHDcM-wHz-XNUEIg5qlwoGrqYOnwLvaXeCaRIiqB9Hj45cUjwBAxWhQ9om0_pOOo6qu1qPXtzc4NqBNWlVBRUbU1QCWvIlZhrPozjzfGHqS8E3R1BYswAQqd5KJXczKz2reu4DfeHeiuWpygj51sDiXLh9sbDqdu2hb0whRL6htq2sC_clAKGmUcW3ebFg3p1Ap_oOBTuynIl3bWm6PHcdsAZJBz3mXNI62o_gVkkhZLBiExdzyMccocYtPWHxZLQH0pq_D9sr_cM7rjBmBF_XV7PG6IuvC5CiMQVAtlwsR7xcFJK4A4ZY2_m3hjX0ENWQFA4RDu7m0tnd4sPO_U2PevU2xIir81tcbm3rvTGUl3rSm3Vmnsv902jIdcvF-ru37q_f__rDQ6YVKiB9LbvAN1Hk7k_I1mo8fanUNkk2o6lnKzT22ZaW9i7eNbXfcaiGha6I1GM4CYL8eJYPftUo3z49T332pV9k3f9Nv9BrbYp2iwmIcP0k4JbAUSMeIr7JUXfRfbTRDaPYngbl9Z9F53Z65SY3R7v5c-Ptz-9MDaptp8g-8k-MKZd3j8oyMUdYj_FWoxIVWlCwgkOfEl5ldL_USRF8skIJzSW5lUJJzF3ZsyTlPSvDimZ-jgmRoBhA51klfP_AC5CZb8=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 32</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 S/4 HANA — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph DS020FPLP_Azure_Cloud["☁️ Azure Cloud"]
        direction LR
        DS020FPLA_ECA_ADLS["ECA-ADLS"]:::appBox
        DS020FPLA_ECA_DataBricks["ECA-DataBricks"]:::appBox
        DS020FPLA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
        DS020FPLA_GraphiteConnect["GraphiteConnect"]:::appBox
        DS020FPLA_IF_Blue_Yonder["IF Blue Yonder"]:::appBox
        DS020FPLA_IP_Blue_Yonder["IP Blue Yonder"]:::appBox
        DS020FPLA_Power_BI_DARC["Power BI (DARC)"]:::appBox
    end
    style DS020FPLP_Azure_Cloud fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020FPLP_On_Prem_Linux["🖥️ On-Prem (Linux)"]
        direction LR
        DS020FPLA_MES_300["MES 300"]:::appBox
        DS020FPLA_SPEED["SPEED"]:::appBox
        DS020FPLA_XEUS["XEUS"]:::appBox
    end
    style DS020FPLP_On_Prem_Linux fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020FPLP_On_Prem_Windows["🖥️ On-Prem (Windows)"]
        direction LR
        DS020FPLA_MARS["MARS"]:::appBox
        DS020FPLA_PDF_SMH["PDF-SMH"]:::appBox
        DS020FPLA_WSPW["WSPW"]:::appBox
        DS020FPLA_WorkStream["WorkStream"]:::appBox
    end
    style DS020FPLP_On_Prem_Windows fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020FPLP_SAP_BTP["☁️ SAP BTP"]
        direction LR
        DS020FPLA_SAP_IBP["SAP IBP"]:::appBox
        DS020FPLA_SAP_PAPM["SAP PAPM"]:::appBox
        DS020FPLA_SAP_SAC["SAP SAC"]:::appBox
    end
    style DS020FPLP_SAP_BTP fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020FPLP_SAP_Cloud_SaaS["☁️ SAP Cloud (SaaS)"]
        direction LR
        DS020FPLA_SAP_Ariba["SAP Ariba"]:::appBox
    end
    style DS020FPLP_SAP_Cloud_SaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020FPLP_SAP_HEC_On_Prem["🖥️ SAP HEC (On-Prem)"]
        direction LR
        DS020FPLA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
        DS020FPLA_Corp_IP_S_4_HANA["Corp / IP S/4 HANA"]:::appBox
        DS020FPLA_IF_S_4_HANA["IF S/4 HANA"]:::appBox
        DS020FPLA_SAP_S_4_MDG["SAP S/4 MDG"]:::appBox
        DS020FPLA_SideCar["SideCar"]:::appBox
    end
    style DS020FPLP_SAP_HEC_On_Prem fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020FPLP_SAP_On_Prem_Linux["🖥️ SAP On-Prem (Linux)"]
        direction LR
        DS020FPLA_SAP_BOBJ["SAP BOBJ"]:::eolBox
    end
    style DS020FPLP_SAP_On_Prem_Linux fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph DS020FPLP_Unassigned["📋 Other / Unassigned Platform"]
        direction LR
        DS020FPLA_ECM_Windchill["ECM (Windchill)"]:::appBox
        DS020FPLA_PDM_Translator["PDM Translator"]:::appBox
        DS020FPLA_FCS["FCS"]:::eolBox
        DS020FPLA_Capacity_Forecast_Data_Store["Capacity Forecast Data Store"]:::appBox
        DS020FPLA_ICS_Phoenix["ICS (Phoenix)"]:::appBox
        DS020FPLA_ATCR["ATCR"]:::appBox
        DS020FPLA_SCS["SCS"]:::eolBox
        DS020FPLA_DXCR["DXCR"]:::appBox
        DS020FPLA_DMOCR["DMOCR"]:::appBox
        DS020FPLA_IF_PDH_Raw["IF PDH Raw"]:::appBox
        DS020FPLA_IF_PDH_Foundational["IF PDH Foundational"]:::appBox
        DS020FPLA_IF_PDH_Consumptional["IF PDH Consumptional"]:::appBox
        DS020FPLA_IP_PDH_Raw["IP PDH Raw"]:::appBox
        DS020FPLA_IP_PDH_Foundational["IP PDH Foundational"]:::appBox
        DS020FPLA_IP_PDH_Consumptional["IP PDH Consumptional"]:::appBox
        DS020FPLA_PDH_Raw["PDH Raw"]:::appBox
        DS020FPLA_PDH_Foundational["PDH Foundational"]:::appBox
        DS020FPLA_PDH_Consumptional["PDH Consumptional"]:::appBox
    end
    style DS020FPLP_Unassigned fill:#FFF9C4,stroke:#F9A825,stroke-width:2px,color:#5D4037

    DS020FPLP_On_Prem_Linux ==>|"Direct"| DS020FPLP_On_Prem_Windows
    DS020FPLP_On_Prem_Windows ==>|"EAI Connector"| DS020FPLP_SAP_HEC_On_Prem
    DS020FPLP_On_Prem_Linux ==>|"ADF Rest API / SFTP(Blob)"| DS020FPLP_Azure_Cloud
    DS020FPLP_Azure_Cloud ==>|"MuleSoft & Reltio"| DS020FPLP_SAP_HEC_On_Prem
    DS020FPLP_SAP_HEC_On_Prem ==>|"ADF Rest API / SFTP(Blob)"| DS020FPLP_Azure_Cloud
    DS020FPLP_Azure_Cloud ==>|"MuleSoft/BODS"| DS020FPLP_SAP_HEC_On_Prem
    DS020FPLP_On_Prem_Windows ==>|"Direct"| DS020FPLP_Azure_Cloud
    DS020FPLP_Azure_Cloud ==>|"Remote Function Adapter / M..."| DS020FPLP_SAP_BTP
    DS020FPLP_SAP_BTP ==>|"SAC Data Export Service (AP..."| DS020FPLP_Azure_Cloud
    DS020FPLP_SAP_BTP ==>|"SAP Odata services with con..."| DS020FPLP_SAP_HEC_On_Prem
    DS020FPLP_SAP_BTP ==>|"SAP Integration Suite / Sma..."| DS020FPLP_SAP_HEC_On_Prem
    DS020FPLP_SAP_Cloud_SaaS ==>|"Apigee / MuleSoft"| DS020FPLP_SAP_HEC_On_Prem
    DS020FPLP_SAP_HEC_On_Prem ==> DS020FPLP_SAP_On_Prem_Linux

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq9WG1v2zgM_iuCh15SoN28pum6ADvAL_GaoVmNqLvucDkYiq00Rh3J8MvSrut_P1J2mjRNZntDzx9iidLzmKQokcq95suAaz1tb-8-FGHWI_etbMbnvNUjrQlLeeuAtFLu50mY3Z3zbzzCgUjKYkRN_YslIZtEPG0heipFRsPviuDtcXyL01DmsHkY3aGU8mvJyZfBATEAGLUecEYkF_6MJZniyFM-ZLdXYZDNoD9lUcphziybR-dswiP8UJbkKBOgPY2ZH4prEB7rIEqYuFmJuvrDA3nY2xuLx0-QS3MsCDx-xNLU5lPC4tiUt2QaRlHvldm1Hcc5SLNE3vDeK11_9848KbuHC9SpdxTfHvgykgkOd-zuJl8csWxFaJ32T6z3j4Sd09N-x3pK2FkRvjW7_SN9g5DLaMXnOGbX7D7yWZYOz04FT05weCwKxjSfXCcsnhGb6ke64567nvE9T7hnRTIP_hlr4_zoRH87zqdcnxI1RNTQWPu3YMAnCBPuZ6EU5Hy0ki4pDa9vGZ5hn1Pgg-YhNgHf6_UKR--C2CxjZhL6N2kJXAnqwKmQCydiN7xEP_arwB_RI2HGLSkE2AXwDUkVwcDxzCjn3t9SBDwB_MAhKCCFoBLubsLdJnBXLnjimQPPNkYWoFWfmAPSRsH-czgXQRkN2V3Et4fCb8Xuzli7EJ6b8Ll3Hor8VkVbcNoJ4Ddg3TLmLsQhTiFtNWe_UdwN-9Tr6DoQQ4tAq8p11O33bZiu3lWTv_a_YETjq4FPn5j8sl69CkUgF2mFX8tZDT1rjNB2fFWGo-14dHiGgWg7h9CqAlxR9wpm46tyqkxuaJZwNkfAY-cXlqP0wsssCDVgR1-6m8cpiAmIGzkeqQYmUiEaWpUhDQDXcIclApt1INSwSgS0GvizNPXl_KhOI48yRre5szir2ji839ivUH5MWGm1aje0e6Xay5l_1reWMbt9X6PyMIm0yw3ezA2WM_jsUe_YOzM-G_AB7BP65phgvypuLJnEmLzW8SAibwgksLokkDvX8JA46wJV1AJyaH9cRi4goVcJDANuMcyzZavhsq8tycute41MiSb_TrZUW_fC_FR6D5uFJ4pqs4Yn_ofc9kVACRxeCx6sO8H3J-QCLh8JxNpqBnGh7p7KZN6wWB2qbODPQH9VOg6LJKkE-9Xpbuhdwp0jhW_LRGW9IVkJquCOheca_D53_cZmY3inye48R4I9LM1UuexR-AYWvMthshwmOEzUcOUWtKjnziQXIUYa9Ei77FZab1xaI8Dgq3LbKUtptaX2V8WJrypOe3hRzMV3jZPGtc-8EVsUBw10CHRqwhyZi4BhHLFohV-X1iSCO0Waz-NNpifiGjeGNVPc2qa4W01xm5vibjfFbW7Kyo6aRmyxoKn623SvofjOs3DtCFpe0Z331vHjIei8N06Pujuv6F37WO-8Wx6Cu64OHz78-QMiXZ1mY-3H7pp2F82y5C2I-saAlNdbPKV-7E5yddQybIeMOJw6hjuAM5k6l27bjORk_ynz2gVzk3X97llwDvOIUznNyB9AHcGiNNJyM1O_vJ5vzAub_pInn67MtiVupNCIz2XGiZOLIu8ZAYszlSuHr1-_fq4h3km2eA_L-oIQrgRFOunfxjLJCOXJt9DnpG24zwh_oukmKZQvAbKmBV1KFmE2I74UW7WsWOunxAORcSgllPk0D8EbsNhz9ivEa1V-GUNxeM2RcLnwvxuXP6uqtANtzpM5CwOtd6-p_1u1nhbwKcujTHs40FieSXonfK2n_hLV8hh8yu2QgfnzQvjwH-XJruc=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

Platform landscape inferred from integrated systems for DS-020:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |
| 4 | APIGEE Platform | On-Premise | APIGEE | DEV, QAS, PRD |
| 5 | ATCR Platform | On-Premise | ATCR | DEV, QAS, PRD |
| 6 | BOBJ Platform | On-Premise | BOBJ | DEV, QAS, PRD |
| 8 | CIBR Platform | On-Premise | CIBR | DEV, QAS, PRD |
| 9 | COMPASS Platform | On-Premise | COMPASS | DEV, QAS, PRD |
| 10 | Capacity Forecast Data Store Platform | On-Premise | Capacity Forecast Data Store | DEV, QAS, PRD |
| 13 | DCS Platform | On-Premise | DCS | DEV, QAS, PRD |
| 14 | DMOCR Platform | On-Premise | DMOCR | DEV, QAS, PRD |
| 15 | DXCR Platform | On-Premise | DXCR | DEV, QAS, PRD |
| 16 | EATS Platform | On-Premise | EATS | DEV, QAS, PRD |
| 17 | ECA Platform | On-Premise | ECA | DEV, QAS, PRD |
| 18 | ECA-ADLS Platform | On-Premise | ECA-ADLS | DEV, QAS, PRD |
| 19 | ECA-DataBricks Platform | On-Premise | ECA-DataBricks | DEV, QAS, PRD |
| 20 | ECA-SnowFlake Platform | On-Premise | ECA-SnowFlake | DEV, QAS, PRD |
| 21 | ECM (Windchill) Platform | On-Premise | ECM (Windchill) | DEV, QAS, PRD |
| 22 | EDW Platform | On-Premise | EDW | DEV, QAS, PRD |
| 23 | FCA Platform | On-Premise | FCA | DEV, QAS, PRD |
| 24 | FCS Platform | On-Premise | FCS | DEV, QAS, PRD |
| 25 | Finance HANA Platform | On-Premise | Finance HANA | DEV, QAS, PRD |
| 26 | GraphiteConnect Platform | On-Premise | GraphiteConnect | DEV, QAS, PRD |
| 27 | ICOST Platform | On-Premise | ICOST | DEV, QAS, PRD |
| 28 | ICS (Phoenix) Platform | On-Premise | ICS (Phoenix) | DEV, QAS, PRD |
| 29 | IF Blue Yonder Platform | On-Premise | IF Blue Yonder | DEV, QAS, PRD |
| 30 | IF PDH Consumptional Platform | On-Premise | IF PDH Consumptional | DEV, QAS, PRD |
| 31 | IF PDH Foundational Platform | On-Premise | IF PDH Foundational | DEV, QAS, PRD |
| 32 | IF PDH Raw Platform | On-Premise | IF PDH Raw | DEV, QAS, PRD |
| 34 | IP Blue Yonder Platform | On-Premise | IP Blue Yonder | DEV, QAS, PRD |
| 35 | IP PDH Consumptional Platform | On-Premise | IP PDH Consumptional | DEV, QAS, PRD |
| 36 | IP PDH Foundational Platform | On-Premise | IP PDH Foundational | DEV, QAS, PRD |
| 37 | IP PDH Raw Platform | On-Premise | IP PDH Raw | DEV, QAS, PRD |
| 38 | Legacy MDG Platform | On-Premise | Legacy MDG | DEV, QAS, PRD |
| 39 | MARS Platform | On-Premise | MARS | DEV, QAS, PRD |
| 40 | MES 300 Platform | On-Premise | MES 300 | DEV, QAS, PRD |
| 41 | PDF-SMH Platform | On-Premise | PDF-SMH | DEV, QAS, PRD |
| 42 | PDH Consumptional Platform | On-Premise | PDH Consumptional | DEV, QAS, PRD |
| 43 | PDH Foundational Platform | On-Premise | PDH Foundational | DEV, QAS, PRD |
| 44 | PDH Raw Platform | On-Premise | PDH Raw | DEV, QAS, PRD |
| 45 | PDM Translator Platform | On-Premise | PDM Translator | DEV, QAS, PRD |
| 46 | PEGA Platform | On-Premise | PEGA | DEV, QAS, PRD |
| 47 | Power BI (DARC) Platform | On-Premise | Power BI (DARC) | DEV, QAS, PRD |
| 57 | SCS Platform | On-Premise | SCS | DEV, QAS, PRD |
| 58 | SPAN Platform | On-Premise | SPAN | DEV, QAS, PRD |
| 59 | SPEED Platform | On-Premise | SPEED | DEV, QAS, PRD |
| 60 | SideCar Platform | On-Premise | SideCar | DEV, QAS, PRD |
| 61 | WSPW Platform | On-Premise | WSPW | DEV, QAS, PRD |
| 62 | WorkStream Platform | On-Premise | WorkStream | DEV, QAS, PRD |
| 63 | XEUS Platform | On-Premise | XEUS | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 33</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (27 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 24 | 88.9% |
| 99. Rejected/Cancelled/On Hold | 3 | 11.1% |
| **Total** | **27** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Interface (I) | 10 |
| Conversion (C) | 2 |
| Enhancement (E) | 15 |
| **Total** | **27** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 02.High | 6 |
| 03.Medium | 17 |
| 04.Low | 4 |

**Tower Context:** FPR has 366 total RICEFW objects (349 complete, 17 active/other)

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

<div class="page-footer"><span>Page 34</span><span><a href="#toc">↑ Back to TOC</a></span><span>DS-020 — Perform Product Costing and Inventory Valuation</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*25 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| FPRI1704 | Automated Tool MUP Excess Capacity calculation and associated PCOS/OCOS Split for the forecast. | Feb-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| FPRI1439 | Receive planned production quantities per production version from ECA to S/4 for mixed costing | Jul-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 4. Completed |
| FPRI1288 | Activity Inbound interface from ECA to S4 IP | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Feb-26 (100%) | 4. Completed |
| FPRI1287 | Production quantity update in WAC custom table from ECA to S4 IF | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Feb-26 (100%) | 4. Completed |
| FPRI1273 | Activity Quantity Inbound interface from ECA to S4 IF | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Feb-26 (100%) | 4. Completed |
| FPRI0704 | IF-IP Integration Actual Cost - Inbound Interface | Feb-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Jun-25 (100%) | 3. Off Track |
| FPRI0703 | IF-IP Integration Actual Cost - Outbound Interface | Feb-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Sep-25 (100%) | 3. Off Track |
| FPRI0554 | SKF Interface to get file from ECA and send to S4 via BODS - IF | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Feb-26 (100%) | 4. Completed |
| FPRI0545 | IF-IP Integration - Interface to send Cost Idoc from S4 If to S4 IP | Sep-24 (100%) | Mar-25 (100%) | Mar-25 (100%) | Apr-25 (100%) |  |
| FPRI0544 | IF-IP Integration - Interface to receive Cost Idoc from S4 If to S4 IP | Sep-24 (100%) | Mar-25 (100%) | Mar-25 (100%) | Apr-25 (100%) | 1. On Track |
| FPRE1438 | Update mixing ratio for Procurement alternative for Cross site transfer based on production volume from BY | Jul-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 1. On Track |
| FPRE1419 | Update Procurement alternatives based on production version & PIR for cross site transfer scenario | Jun-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Dec-25 (100%) | 4. Completed |
| FPRE1328 | Legal Valuation standard cost calculation enhancement | Feb-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | — | 1. On Track |
| FPRE0702 | Calculation of variance to be loaded for Group Actual Costing | Feb-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Aug-25 (100%) | 1. On Track |
| FPRE0701_IP | Mixed Costing ratio auto update | Jan-25 (100%) | May-25 (100%) | May-25 (100%) | Jul-25 (100%) |  |
| FPRE0701_IF | Mixed Costing ratio auto update | Jan-25 (100%) | May-25 (100%) | May-25 (100%) | Jul-25 (100%) |  |
| FPRE0700_IP | Representative material ID – Q2-Q8 Forecast | Jan-25 (100%) | May-25 (100%) | May-25 (100%) | Jul-25 (100%) | 2. At Risk |
| FPRE0700_IF | Representative material ID – Q2-Q8 Forecast | Jan-25 (100%) | May-25 (100%) | May-25 (100%) | Jun-25 (100%) |  |
| FPRE0699 | Enhancement for Excess Capacity – Fixed Spending Adjustment | Feb-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Dec-25 (100%) | 4. Completed |
| FPRE0698 | Legal Valuation standard cost calculation enhancement | Feb-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | May-25 (100%) | 1. On Track |
| FPRE0551 | SKF Actual Driver volume update from actual activity confirmation Automation | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Mar-25 (100%) |  |
| FPRE0550 | Enhancement to update additive cost in IP based on Idoc of IF cost | Sep-24 (100%) | May-25 (100%) | May-25 (100%) | Aug-25 (100%) |  |
| FPRE0549 | Enhancement to a) update Cost and Production volume in custom table, b) calculate WAC in Custom table and send Idoc to IP system | Sep-24 (100%) | Mar-25 (100%) | Mar-25 (100%) | Apr-25 (100%) |  |
| FPRC1493 | Conversion of WIP values as per Component structure in S/4 - IP | Jul-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| FPRC1491 | Conversion of WIP values as per Component structure in S/4 - Back End IF | Jul-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**Mapped sub-tower(s):** 3.7 FPR - Product Costing and Inventory Valuation

**RAID Summary:** 18 open items (0 capability-specific, 18 tower-level), 234 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 1 | 1 |
| P2 - Medium | 0 | 14 | 14 |
| P3 - Low | 0 | 3 | 3 |
| **Total** | **0** | **18** | **18** |

**Other FPR Tower RAID Items** (18 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03197 | Issue | P2 - Medium | Company Code address disappearing in DI0 250 | Not Started |  |  |
| 03729 | Action | P2 - Medium | AN and CC invoices are fetching wrong tax codes and posting ... | In Progress | FPR | 2026-03-23 |
| 03564 | Risk | P2 - Medium | Development of the AMT impacting FPR Capital Tool report | In Progress | FTS IP | 2026-03-27 |
| 03624 | Issue | P2 - Medium | Test Data not provided for CR "INT-Build-CR0918" | In Progress | FPR | 2026-03-20 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03628 | Risk | P2 - Medium | R3 Returns Rework Process Causing Finance Double Counting in... | In Progress | E2E | 2026-03-27 |
| 03629 | Risk | P2 - Medium | Consensus Demand Data for ICOST | In Progress | FTS IP | 2026-03-27 |
| 03633 | Action | P2 - Medium | Conversion RICEFW (FPRC1724_IF/IP) has dependency on the enh... | In Progress | FPR | 2026-03-13 |
| 02680 | Action | P2 - Medium | T042A table config in IP and IF | In Progress | FPR | 2026-04-03 |
| 02799 | Risk | P2 - Medium | Deloite FPR objects FPRXV490, FPRXV038 and FPRXV048 are dela... | In Progress | FPR | 2026-03-25 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03740 | Action | P2 - Medium | Provide count of report with list of names due in ITC1 and I... | In Progress | FPR | 2026-03-20 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03782 | Risk | P2 - Medium | Auto processing of JPMC lockbox BAI2 for AR Cashapp not work... | Not Started | FPR | 2026-04-10 |
| 03333 |  | P3 - Low | FPR NRT : IF and IP  Power BI Workspace Provisioning | In Progress | Analytics (Reporting) | 2026-01-12 |
| 03473 | Action | P3 - Low | Manual Service PIR creation for IP-IF Service Procurement. | In Progress | FPR | 2026-05-29 |
| 02226 | Action | P3 - Low | DMEE related FPR objects not ready for development | In Progress | FPR | 2026-03-31 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Integration | Validate integration patterns and middleware for high-complexity flows across 42 systems (ATCR, CFIN S/4 HANA, Capacity Forecast Data Store, Corp / IP S/4 HANA, DMOCR...) | High | Integration Architect | 2026-Q2 | Open |
| 3 | Data | Define data ownership and classification for all 22 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 4 | Testing | Develop integration test scenarios covering all 22 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 5 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 6 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*DS-020 — Architecture Document (TOGAF BDAT) · Finance Plan To Report · Generated: March 2026*

