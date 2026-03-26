<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">PM-080 — Purchase Materials and Services</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Procure To Pay (PTP) Tower<br/>
  Capability PM-080 · PM Procure Materials and Services (Direct and Indirect)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **PM-080 Purchase Materials and Services** within the IAO program. It includes 21 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Procure To Pay (PTP) |
| **Process Group** | PM Procure Materials and Services (Direct and Indirect) |
| **Capability** | PM-080 - Purchase Materials and Services |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 3 Reports, 171 Interfaces, 16 Conversions, 171 Enhancements, 7 Forms, 10 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Procure To Pay |
| **L1 Process** | PM Procure Materials and Services (Direct and Indirect) |
| **L2 Capability** | PM-080 - Purchase Materials and Services |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Procurement Process Standardization | Standardize procurement processes across direct, indirect, and services on S/4 HANA + Ariba | IDM 2.0 Procurement Excellence | High |
| 2 | Supplier Collaboration Enhancement | Enable digital supplier collaboration for consignment, subcontracting, and quality management | Supplier Ecosystem | High |
| 3 | Payment Automation | Automate invoice verification, three-way matching, and payment execution | Finance Efficiency | Medium |
| 4 | PM-080 Process Migration | Migrate Purchase Materials and Services business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Procurement | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| PO Cycle Time | < 24 hours | Requisition approval to PO dispatch to supplier | 48 hours (current) | Procurement Lead |
| Invoice Automation Rate | > 80% | Invoices processed without manual intervention (touchless) | 45% (current) | AP Manager |
| Supplier On-Time Delivery | > 95% | Supplier adherence to confirmed delivery date | 89% (current) | Supplier Management |
| PM-080 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **21 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for PM-080 Purchase Materials and Services.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | PM-080-010_Create_PO_Manually_With_’Text_Materials’ | PM-080-010_Create_PO_Manually_With_’Text_Materials’ | Procurement Agent | 3 | 4 |
| 2 | PM-080-020_Release_Scheduling_Line_from_Scheduling_Agreement | PM-080-020_Release_Scheduling_Line_from_Scheduling_Agreement | Procurement Agent | 1 | 4 |
| 3 | PM-080-030_Create_and_Release_Contract_Order | PM-080-030_Create_and_Release_Contract_Order | Procurement Agent | 3 | 4 |
| 4 | PM-080-040_Create_Plant-to-Plant_Transfer_Order | PM-080-040_Create_Plant-to-Plant_Transfer_Order | Procurement Agent | 6 | 2 |
| 5 | PM-080-050_Create_and_Process_Purchase_Order | PM-080-050_Create_and_Process_Purchase_Order | Procurement Agent | 4 | 7 |
| 6 | PM-080-060_Transmit_Order_to_Supplier | PM-080-060_Transmit_Order_to_Supplier | Procurement Agent | 7 | 9 |
| 7 | PM-080-070_Manage_Order_Acknowledgment_Process | PM-080-070_Manage_Order_Acknowledgment_Process | Buyer/Planner | 2 | 1 |
| 8 | PM-080-080_Monitor_Order_Status | PM-080-080_Monitor_Order_Status | Procurement Agent | 5 | 7 |
| 9 | PM-080-090_Resolve_Order_Issues_with_Supplier | PM-080-090_Resolve_Order_Issues_with_Supplier | Procurement Agent | 2 | 0 |
| 10 | PM-080-100_Modify_Purchase_Order | PM-080-100_Modify_Purchase_Order | Purchaser | 6 | 8 |
| 11 | PM-080-110_Cancel_Original_Purchase_Order | PM-080-110_Cancel_Original_Purchase_Order | Cost Accountant, Purchaser | 8 | 13 |
| 12 | PM-080-120_Determine_Alternate_Materials_and_Approaches | PM-080-120_Determine_Alternate_Materials_and_Approaches | Procurement Agent | 3 | 3 |
| 13 | PM-080-130_Select_New_Supplier_&amp;_Reissue_PO | PM-080-130_Select_New_Supplier_&amp;_Reissue_PO | Procurement Agent | 3 | 2 |
| 14 | PM-080-140_Verify_Requirements_and_Terms_with_New_Supplier | PM-080-140_Verify_Requirements_and_Terms_with_New_Supplier | Procurement Agent | 2 | 4 |
| 15 | PM-080-150_Transmit_Dunning_Letter | PM-080-150_Transmit_Dunning_Letter | Procurement Agent | 1 | 3 |
| 16 | PM-080-160_Manage_Advanced_Shipping_Notifications | PM-080-160_Manage_Advanced_Shipping_Notifications | Procurement Agent | 3 | 4 |
| 17 | PM-080-170_Manage_P-Card_Purchases | PM-080-170_Manage_P-Card_Purchases | Procurement Agent | 4 | 1 |
| 18 | PM-080-180_Create_and_Maintain_Internal_Catalogue | PM-080-180_Create_and_Maintain_Internal_Catalogue | Buyer/Planner, Catalog Administrator | 6 | 3 |
| 19 | PM-080-210_Vendor_Managed_Inventory_(Pay_Upon_Receipt_OEM) | PM-080-210_Vendor_Managed_Inventory_(Pay_Upon_Receipt_OEM) | AP Processor, Buyer, Warehouse Manager | 6 | 0 |
| 20 | PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI) | PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI) | AP Processor, Buyer, MRP Controller, Supplier, Warehouse Manager | 9 | 0 |
| 21 | PM-080_Purchase_Materials_and_Services | PM-080_Purchase_Materials_and_Services | Procurement Agent | 8 | 23 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 PM-080-010_Create_PO_Manually_With_’Text_Materials’ — PM-080-010_Create_PO_Manually_With_’Text_Materials’

**Swim Lanes**: Procurement Agent | **Tasks**: 3 | **Gateways**: 4

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
    subgraph Procurement Agent
        n1["fa:fa-user Create PO with 'Text Materials'"]
        n2["fa:fa-user Delete Purchase Requisition"]
        n3["fa:fa-user Modify Purchase Requisition"]
        n4(["fa:fa-play PR with Text Materials Created"])
        n5(["fa:fa-stop Purchase Requisition Deleted"])
        n6["Order Transmitted to Supplier System"]
        n7["Receive Materials and Services"]
        n8["Order Acknowledgment Received"]
        n9["Maintain Supplier Certification and Monitor Performance"]
        n10["Project Accounting"]
        n11["ASN Received"]
        n12{{"fa:fa-code-branch PR Approved?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n15{{"fa:fa-code-branch Delete or Modify Purchase Requisition?"}}
        n16[["fa:fa-folder-open Perform Purchase Requisitions Approval Process"]]
        n17[["fa:fa-folder-open Transmit Order to Supplier"]]
        n18[["fa:fa-folder-open Manage Order Acknowledgment Process"]]
        n19[["fa:fa-folder-open Manage Advanced Shipping Notifications"]]
    end
    n16 --> n12
    n12 -->|"No"| n15
    n15 -->|"Delete"| n2
    n2 --> n5
    n4 --> n13
    n1 --> n17
    n17 --> n6
    n6 --> n8
    n13 --> n16
    n14 --> n1
    n12 -->|"Yes"| n14
    n10 --> n14
    n9 -->|"Supplier Master Data"| n14
    n15 -->|"Modify"| n3
    n8 --> n18
    n18 --> n11
    n11 --> n19
    n19 --> n7
    n3 --> n13
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 endEvt
    class n6 startEvt
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 subProc
    class n17 subProc
    class n18 subProc
    class n19 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVmuP4jYU_StWViNaCaQ8CeRDKwZIVanMjoZpq2rpB5M44E6IU9sZYFn-e6-TOBA2rKo2EhE5vufch68fJyNiMTEC4-HhRDMqA3TqyS3ZkV6AemssSK-PKuA3zClep0T0lE3CMrmkn0szy80PykxhId7R9KjQJdkwgn79uY8mQEz7SOBMDAThNOn1ezmnO8yPU5Yyrqw_kFFiJqW3euiR8Zjwi4Fp-lbkATWlGbnAju_6bqh4gkQsi1uiiZeMkqh3VsGlbB9tMZdl-IUgC3z4ncZyC98JTgUBm63cpb_gNUlVjpIXCosK_q6LQYXyk0HBljmOaLYB3DUB4jh7u0CeeT6j88PDKmucotfZKkPwRCkWYkYSJCTA83eJEpqmwQd3Ogk9sy8kZ28k-GDP_Zlj9yOVSQCpm31V3MGe0M1WBmuWxrXpYK9yCOz80OeHwDb7_AjvG18kiy-epkN7ZI8aT4--NbWm2lOSJP_LE9SVv2LxVvuaO6Edzhpfljf0pubXejrNmetPrNs6Ef5OI3IlGoahM7-Uaj70LPO-6GPoDM3pjegGS7LHx4vgeOo2gqHnh5Z_V7DydxtlsX7mLNKCztwLvUbQf7TCiX1X0J1Y7qiOEHQ2HOdbpNQKDssuk2iygXc1rp7M-rQyEhwkeKDKjaacQDro-SPaU7lFvVdykGgBkFp2orcy_rzi2m3ujKREcQsObSoIeiF_F1RQSVnW5jlt3oLFNDn-C577XUPMU6j480sVZTvIOocYuN9fkb0LWUiWd7qrU7ilDoH5UW0g6BUWp9hRCTZIMrQs8jylgC-PQpJdO1ofWC8kIvSdXAWHsxgtqzYUbftR42USvWVsn5J4U05ZLRK3zcdgvsA0k_C7BDIlXNKERrhMRzlbMNiJGUfPhCeM73AWkbaQZYIStMhfJIL2iCJWZBL2nhsj1SeT5dOdYCz7dNLVVWfAYA2FirZqhiZ5zhkQflwZ5_M1xemmkEOUFgJc_FStq1ua-99oXjet7ln2zS78KvThp6aXEtjUCB-wnGS6xJ0aoi4ETsvlSISa_VYJ_W5R3XKo6o2rrrsVGHULLHCGNwR1ttadUMbfVJrE76qLoI-3NM-hVdATuzTdlRgcFdUfqBgaDH5QfaIBWwFfVsYTWxlf1PzoAa8eqGamHNQkuxLRpm6t6Whq_e3rb78ChvV3HcNIDzu1vR63tOBtjH-opaqCdPWIWVtqYFxbNutwgWFDgC0RS3xD1flV_VYO6gRGtWoToQaaiHSKYw2MK0Cn7LRLUh4pqjD6KG3BdjfsdMNuc8towV59IWiBw25bvxsedcPjbhhq341bd3Bbn9Bt2OmG3W7Y64aH-rBuw343POqGxxo2-saOwBZNYyM4GeVFGS7TMUlwkUrj3DdwIdnymEVGUF4ojSKPIaoZxXDO7yrw_A_rWKRh" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 PM-080-020_Release_Scheduling_Line_from_Scheduling_Agreement — PM-080-020_Release_Scheduling_Line_from_Scheduling_Agreement

**Swim Lanes**: Procurement Agent | **Tasks**: 1 | **Gateways**: 4

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
    subgraph Procurement Agent
        n1["fa:fa-user Release Delivery Schedule Line from Scheduling Agreement"]
        n2(["fa:fa-stop Delivery Schedule Line Transmitted to Supplier"])
        n3["Create and Process Purchase Order"]
        n4["Identify MRP Requirements"]
        n5["Identify Non-MRP Requirements"]
        n6{{"fa:fa-code-branch exclusiveGateway"}}
        n7{{"fa:fa-code-branch Scheduling Agreement Exists??"}}
        n8{{"fa:fa-code-branch Scheduling Agreement Required?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
        n10[["fa:fa-folder-open Create Scheduling Agreement"]]
    end
    n4 --> n6
    n5 --> n6
    n6 --> n7
    n7 -->|"Yes"| n9
    n7 -->|"No"| n8
    n8 -->|"No"| n3
    n8 -->|"Yes"| n10
    n9 --> n1
    n10 --> n9
    n1 --> n2
    class n1 userTask
    class n2 endEvt
    class n3 startEvt
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
    class n8 gateway
    class n9 gateway
    class n10 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVW2PozYQ_isWq1VaiUhAIGT50FM2CdVJd9fVZXun6tIPDowTax1DbbObNJf_3nGAvDWp1JYPiHmYeZ6ZwTNsnazIwUmc-_stl9wkZNsxS1hBJyGdOdXQcUkNfKGK07kA3bE-rJBmyv_cu_lhubZuFkvpiouNRaewKID8-t4lQwwULtFU6q4GxVnH7ZSKr6jajApRKOt9BwPmsb1a8-qxUDmoo4PnxX4WYajgEo5wLw7jMLVxGrJC5mekLGIDlnV2NjlRvGVLqsw-_UrDR7r-ynOzRJtRoQF9lmYlPtA5CFujUZXFskq9ts3g2upIbNi0pBmXC8RDDyFF5csRirzdjuzu72fyIEqexzNJ8MoE1XoMjGiD8OTVEMaFSO7C0TCNPFcbVbxAchdM4nEvcDNbSYKle65tbvcN-GJpknkh8sa1-2ZrSIJy7ap1Eniu2uD9QgtkflQa9YNBMDgoPcb-yB-1Soyx_6WEfVXPVL80WpNeGqTjg5Yf9aOR93e-tsxxGA_9yz6BeuUZnJCmadqbHFs16Ue-d5v0Me31vdEF6YIaeKObI-HDKDwQplGc-vFNwlrvMstq_qSKrCXsTaI0OhDGj346DG4ShkM_HDQZIs9C0XJJLFulcOykIcMF3uv39pL-t5nDaMJo17abfAYBOKhkDIK_gtqQabaEvBJAPuCkEKaKVQvh-UQ2BXvemfP7CWnww4FVm6K8xfaMR12vuDGQE1OQaVWWgoNCrh9PyHrINVKAXSZU5vtiQGvyVCmcBkz1Fzva5_ohhrzPMS3ONuTj5ycs64-K1x3Q567RqeunQnb_2b2_3baV2V3XnWMJ2ZLAOhOVxhp_rg_DzNntTqLi61HXGkkma66NfvfugmLwLyia9PNLjof_lLzvfTt8TYYjDKpblCBJ801unIamabgt6gcZkm73J2xgY0bnZr8248aMrfl95vwG2P_vmPkF_qnYw4MGHpzDvQu4ZfGbSZMPtVqzHhCv7VbFr83gZC4t2O6jMzhoFuIZ2Dts5DM4vA5H1-F-u1nO0PgqOriKPlxFsdpmwziuswK1ojx3kq2z_zHjzzsHRithnJ3r0MoU043MnGT_A3OqMkfCMae4V1Y1uPsLUYOMEA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 PM-080-030_Create_and_Release_Contract_Order — PM-080-030_Create_and_Release_Contract_Order

**Swim Lanes**: Procurement Agent | **Tasks**: 3 | **Gateways**: 4

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
    subgraph Procurement Agent
        n1["fa:fa-user Create Contract Order (PO w.r.t Contract)"]
        n2["fa:fa-user Create Manual Purchase Order w.r.t PR"]
        n3["fa:fa-user Release Contract Order (PO w.r.t Contract)"]
        n4(["fa:fa-stop Contract Release Order Transmitted to Supplier"])
        n5["Identify MRP Requirements"]
        n6["Identify Non-MRP Requirements"]
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8{{"fa:fa-code-branch Supplier Contract Exists?"}}
        n9{{"fa:fa-code-branch Purchase Info Record Exists?"}}
        n10{{"fa:fa-code-branch exclusiveGateway"}}
        n11[["fa:fa-folder-open Create and Process Purchase Order"]]
    end
    n5 --> n7
    n6 --> n7
    n7 --> n8
    n8 -->|"No"| n9
    n9 -->|"Yes"| n11
    n10 --> n4
    n11 --> n10
    n9 -->|"No"| n2
    n2 --> n10
    n8 -->|"Yes"| n1
    n1 --> n3
    n3 --> n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 endEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
    class n9 gateway
    class n10 gateway
    class n11 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqllluP4jYUx7-KldGIXSlZ5UoyediKCaQaaWcXDdNW1dIHk9hgTXBS2xlgWb772uQCSTOVtuUBcf4553cucU44akmeIi3Ubm-PhBIRguNIbNAWjUIwWkGORjqohN8hI3CVIT5SPjinYkG-nd0st9grN6XFcEuyg1IXaJ0j8NuDDiYyMNMBh5QbHDGCR_qoYGQL2SHKs5wp7xsUYBOfs9WX7nOWInZxME3fSjwZmhGKLrLju74bqziOkpymHSj2cICT0UkVl-W7ZAOZOJdfcvQI93-QVGykjWHGkfTZiG32Ca5QpnoUrFRaUrLXZhiEqzxUDmxRwITQtdRdU0oM0peL5JmnEzjd3i5pmxQ8T5cUyE-SQc6nCAMupDx7FQCTLAtv3GgSe6bOBctfUHhjz_ypY-uJ6iSUrZu6Gq6xQ2S9EeEqz9La1dipHkK72OtsH9qmzg7yu5cL0fSSKRrbgR20me59K7KiJhPG-H9lknNlz5C_1LlmTmzH0zaX5Y29yPwnr2lz6voTqz8nxF5Jgq6gcRw7s8uoZmPPMt-G3sfO2Ix60DUUaAcPF-Bd5LbA2PNjy38TWOXrV1mu5ixPGqAz82KvBfr3Vjyx3wS6E8sN6golZ81gsQGKVjL52FEBJmv5XV1XH2p9XWoYhhgaatwgYki2AyJ52xhMBPiinhvwbv4F7D6wD6K98H6p_XVFsQcpj5CWMAPzkslzy1ENq0Dzpy7B6RKeUIZUyM8W4r5rOVzkxSW-AVacZ_mQ8S0RAqVA5GBRFkVGEJOs91cwT7IeUjkvgg_g8WkuIX-XpBok7-YdX7t-zqnx7-7-8diUqVamsZL1JBuA9klWcvKKfq3O1FI7na6iguGopvpLs7M94YL_0gu_Gw5vb88DxbmsOZG78g2CZf6nui3ra3tXsFwCiBl5gWhzTCBNz0cUcd47K3Jo9dTk1ql-UA8Yxkc5wdocd02_MoPaDJT5fal9zpfadzmBWr6r5T8RP-tWvShkg1W829hWZVtmL7IG2rVs99yCfoKGV_k5tel0w84bQDk1m68j28OyMyy79aLuiF77pujI42HZb1ZbRw0G1btBVY5zULaaHafp2haxLSSpFh61818D-fchRRiWmdBOugZLkS8ONNHC8ytUK4tUAqcEys22rcTTD0Agr1M=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 PM-080-040_Create_Plant-to-Plant_Transfer_Order — PM-080-040_Create_Plant-to-Plant_Transfer_Order

**Swim Lanes**: Procurement Agent | **Tasks**: 6 | **Gateways**: 2

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
    subgraph Procurement Agent
        n1["fa:fa-user Identify Material, Supplying Plant, Receiving Plant"]
        n2["fa:fa-user Send ASN for STO to Suppliers"]
        n3["fa:fa-user Create Outbound Delivery in Supplying Plant"]
        n4["fa:fa-user Create Stock Transfer Order"]
        n5[["fa:fa-cog Create Stock Transfer Requisition"]]
        n6[["fa:fa-cog Convert STR to Stock Transfer PO"]]
        n7(["fa:fa-stop ASN Sent"])
        n8(["fa:fa-stop Outbound Delivery Created in Supplying Plant"])
        n9["Identify Non-MRP Requirements"]
        n10["Identify MRP Requirements"]
        n11{{"fa:fa-code-branch STO Created for OSAT and BOX/CPU Suppliers?"}}
        n12{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n9 --> n1
    n2 --> n7
    n11 -->|"Yes"| n2
    n11 -->|"No"| n8
    n3 --> n11
    n1 --> n4
    n4 --> n12
    n12 --> n3
    n10 --> n5
    n5 --> n6
    n6 --> n12
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 endEvt
    class n8 endEvt
    class n9 startEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVluP2jgU_itWRiN2paDNlTB56AoCWVXqDGhC96KyDyZxwJpgs7bDQCn_vXZukBS0D81DlPOd833nEtvJSYtpgjRfe3w8YYKFD049sUFb1PNBbwU56umgBP6EDMNVhnhPxaSUiAh_LcJMZ3dQYQoL4RZnR4VGaE0R-PxRByNJzHTAIeF9jhhOe3pvx_AWsmNAM8pU9AMapkZaZKtcY8oSxC4BhuGZsSupGSboAtue4zmh4nEUU5K0RFM3HaZx76yKy-h7vIFMFOXnHD3Dw184ERtppzDjSMZsxDb7BFcoUz0Klissztm-HgbmKg-RA4t2MMZkLXHHkBCD5O0Cucb5DM6Pj0vSJAWLyZIAecUZ5HyCUsCFhKd7AVKcZf6DE4xC19C5YPQN-Q_W1JvYlh6rTnzZuqGr4fbfEV5vhL-iWVKF9t9VD761O-js4FuGzo7y3smFSHLJFAysoTVsMo09MzCDOlOapj-VSc6VLSB_q3JN7dAKJ00u0x24gfGjXt3mxPFGZndOiO1xjK5EwzC0p5dRTQeuadwXHYf2wAg6omso0Ds8XgSfAqcRDF0vNL27gmW-bpX5as5oXAvaUzd0G0FvbIYj666gMzKdYVWh1FkzuNsApZYzue2IAKO1vJd-dRHzy1JLoZ_Cvho3-JhIN06P4Fl2VW61KN_tsqNcjWCeQSJ08IpihPcNsNT-vdKz2nqRXC5gFL2AlEpjMQOCloIYMd5m2m1mwJAsAcxysaK5FJmgDO8ROwJMuiW1dZybOpGg8RtYyM3FU4nO1HnQ5rlfGmJM13d4r-i_HHMsMCWSfU0fdOiUyGqF7Pm16LktM5912N4vDZsLuitGFqGitV-vwoadsB-nU5ad3J7StdSTVGre9gsl_efXedleuVI6b8c0ruP_J9Y8nS6zSFB_JfuON8X7r-tT62EWjRYAyurHs79_C-afLyvj96V2Pl8rWrcV0SHOci47_6PchBeaXHflA3kC_f4HKVGZVml6lWmayv621P5Bsotv0t91vNACH1a4XcnVemZpO5XpVO5Gpspn17ZR2m5lu6U5qMxBm16cCSpHfRa2YOs2bN-Gnduwe30qtjyDux6v-gq0wOEt8Kn5NrUbMu7gZn2ctmGrhjVd2yK2hTjR_JNW_EvI_40EpTDPhHbWNZgLGh1JrPnFN1fLd4lkTjCUR-G2BM_fAZZovWI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 PM-080-050_Create_and_Process_Purchase_Order — PM-080-050_Create_and_Process_Purchase_Order

**Swim Lanes**: Procurement Agent | **Tasks**: 4 | **Gateways**: 7

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
    subgraph Procurement Agent
        n1["fa:fa-user Create PO in S/4"]
        n2["fa:fa-user Trigger PO Approval"]
        n3["fa:fa-user Validate PO Details and Output"]
        n4["fa:fa-user Rectify PO"]
        n5(["fa:fa-play Initiate PO Creation"])
        n6(["fa:fa-stop PO Information Sent to External Planning Engine"])
        n7["Transmit Order to Supplier"]
        n8{{"fa:fa-code-branch Is the PO Created value $25k or10% (whichever is lower) as Compared to PR..."}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
        n10{{"fa:fa-code-branch PO Approval Status"}}
        n11{{"fa:fa-code-branch Is PO Applicable for Approval ?"}}
        n12{{"fa:fa-code-branch exclusiveGateway"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n5 --> n1
    n8 -->|"Yes"| n2
    n2 --> n9
    n8 -->|"No"| n9
    n9 --> n10
    n14 --> n6
    n14 -->|"Optional"| n3
    n3 --> n7
    n10 -->|"Approved"| n12
    n12 --> n14
    n11 -->|"Yes"| n13
    n10 -->|"Rejected"| n4
    n13 --> n8
    n4 --> n13
    n11 -->|"No"| n12
    n1 --> n11
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
    class n12 gateway
    class n13 gateway
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVluPozYY_SsWs6PsSmTKNWR4aJVJwmqktjOaTLeqmj44YBJ3HINsk0uz-e_7OUASWOZlywOJD-ec7wL-4GDEWUKM0Li9PVBOVYgOPbUia9ILUW-BJemZqAS-YEHxghHZ05w042pG_zvRbC_faZrGIrymbK_RGVlmBP3xaKIRCJmJJOayL4mgac_s5YKusdiPM5YJzb4hw9RKT9GqSw-ZSIi4ECwrsGMfpIxycoHdwAu8SOskiTOeNExTPx2mce-ok2PZNl5hoU7pF5L8hnd_0kStYJ1iJglwVmrNfsULwnSNShQaiwuxqZtBpY7DoWGzHMeULwH3LIAE5m8XyLeOR3S8vZ3zc1D0OplzBEfMsJQTkiKpAJ5uFEopY-GNNx5FvmVKJbI3Et4402DiOmasKwmhdMvUze1vCV2uVLjIWFJR-1tdQ-jkO1PsQscyxR7OrViEJ5dI44EzdIbnSA-BPbbHdaQ0Tf9XJOireMXyrYo1dSMnmpxj2f7AH1vf-9VlTrxgZLf7RMSGxuTKNIoid3pp1XTg29b7pg-RO7DGLdMlVmSL9xfD-7F3Noz8ILKDdw3LeO0si8WzyOLa0J36kX82DB7saOS8a-iNbG9YZQg-S4HzFdJuhYBtxxUaLeFcXtcHt_-eGykOU9zX7UZjQaAc9PyEKEezn7y58c8V2WmSXwVdLuEX2KM8F9kGsybfbfK_YEaTyn5CFKZMIswT9FSovFBNqdeUvpBY0XQPyibN_3jm5QxuwiOMHVqFONVCMw6KT1eSwUUiVZZr5iNPM7E-kdFMd0llaLpTRHDM0DPDnMNmRFO-hGnRcgvA7BW2rFxThZ70lNHiWZHnjBLRTHZ4ONSR9aDsL0AXr9CjRDAUzxmTBEEjC4I-OP4byoRt3aKP2xWNV2QD7lQiGAREfEJYonG2zrEABcR8frm7u5sbx-NVxPvuiGQXs0LSDflcPrstlW11y67uM5oprArZFtrvVlhqGY312EfQ7ovVL20X58eydn9M5l1kWIhsK_uYKQRtxYwR9p0I5l_5h_uo3_8ZDKrlUC-_zo2_CLTlK2yWCndK2n2L9nt2YtXwfWVWDQNIqwQGjTXonnL9mOqdBmq3uuqW5KAmWxW57DFJTmS7zsiuUrK9GrBbudtu2-mF_AtbsHI666q4w2pd5XxR281iLxlUxOsBrdF65Ddgpxt2u2GvG_bPL8kGPKjeZw0w6OYO61HfQO87UehbJ2x3w0437HbDXg0bprEmMLhoYoQH4_RlBV9fCUlxwZRxNA1cqGy257ERnr5AjCLX83dCMbwY1iV4_AYeDQ09" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 PM-080-060_Transmit_Order_to_Supplier — PM-080-060_Transmit_Order_to_Supplier

**Swim Lanes**: Procurement Agent | **Tasks**: 7 | **Gateways**: 9

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
    subgraph Procurement Agent
        n1[["fa:fa-cog Create Carbon Copy of PO Created in Ariba"]]
        n2[["fa:fa-cog Rectify Error"]]
        n3[["fa:fa-cog Route Logic for Ariba PO"]]
        n4[["fa:fa-cog Route Logic on Vendor Id, Plant and Storage Location"]]
        n5[["fa:fa-cog Route Logic on Plant and Storage Location"]]
        n6[["fa:fa-cog Send PO to Websuite"]]
        n7["Transmit Order to Supplier"]
        n8(["fa:fa-play PO created in Ariba"])
        n9(["fa:fa-stop Ariba PO Sent to Business Network"])
        n10["Manage Order Acknowledgment Process"]
        n11["PO Sent to Supplier"]
        n12["Release Scheduling Line from Scheduling Agreement"]
        n13["Create and Process Purchase Order"]
        n14["Create PO Manually With ’Text Materials’"]
        n15{{"fa:fa-code-branch exclusiveGateway"}}
        n16{{"fa:fa-code-branch Error?"}}
        n17{{"fa:fa-code-branch Ariba PO Type?"}}
        n18{{"fa:fa-code-branch Supplier is B2B Enabled?"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
        n23{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n8 --> n21
    n21 --> n1
    n12 --> n15
    n13 --> n15
    n14 --> n15
    n1 --> n15
    n15 --> n7
    n7 --> n16
    n16 -->|"Yes"| n2
    n17 -->|"Yes"| n3
    n17 -->|"No"| n18
    n3 --> n19
    n18 -->|"Yes"| n22
    n18 -->|"No"| n19
    n22 --> n4
    n22 --> n5
    n19 --> n6
    n5 --> n23
    n6 --> n20
    n20 --> n11
    n23 --> n20
    n4 --> n23
    n16 -->|"No"| n17
    n21 -->|"Integration Sent to Business
 Network for Onboarded Supplier"| n9
    n11 --> n10
    n2 --> n15
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n8 startEvt
    class n9 endEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 startEvt
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV1tv4kYU_isjRxGtZCRfsfFDKyC4ipTdREu6UbXsw2CPzSjGY43HAZblv_cMvgCOXbUpD4j5zvm-c5krByVgIVE85fb2QFMqPHQYiDXZkIGHBiuck4GKSuAr5hSvEpIPpE_EUrGgP05uupXtpJvEfLyhyV6iCxIzgv68V9EEiImKcpzmw5xwGg3UQcbpBvP9jCWMS-8b4kZadIpWmaaMh4SfHTTN0QMbqAlNyRk2HcuxfMnLScDS8Eo0siM3CgZHmVzCtsEac3FKv8jJJ7x7oaFYwzjCSU7AZy02yQNekUTWKHghsaDgb3UzaC7jpNCwRYYDmsaAWxpAHKevZ8jWjkd0vL1dpk1Q9Hy3TBF8ggTn-R2JUC4Anr8JFNEk8W6s2cS3NTUXnL0S78aYO3emoQayEg9K11TZ3OGW0HgtvBVLwsp1uJU1eEa2U_nOMzSV7-G7FYuk4TnSbGS4httEmjr6TJ_VkaIo-l-RoK_8GeevVay56Rv-XRNLt0f2THuvV5d5ZzkTvd0nwt9oQC5Efd835-dWzUe2rvWLTn1zpM1aojEWZIv3Z8HxzGoEfdvxdadXsIzXzrJYPXEW1ILm3PbtRtCZ6v7E6BW0JrrlVhmCTsxxtkZSreCw7VKBJjF8l3b5SfVv35ZKhL0IDwMWoxknUA6aYb5iKZqxbI9YhJ4eK0OIaCq34Aovle_fL2SMa5kvJBA02qM554y3XM2WKysg4AOLKVTMeKkOEVssq58FiX6FVQnc-1BFTwmGMnEaooVgHMfSK8CCsrSlaP-j4r-WGV3LLCAT2S_B0AtZ5QUVpEVwwP8ZNnm-oQI9ynNJOi-KLEsokc268HV_acSzBNYYCAfvJ-LXC8b4zMgFy5p2ysSEDDQtcjjz8hx9JmLL-GuLr2vA_4RTWXGZ3CR4Tdk2IWF8WkByMQH9Ok9dB9ZFkO5qdAO8vpCEwFWAFsGahAWcvzF6gIRQxNnmEpzEnJyWbEvDBI1qlcrZqdJBTwWHwzGvkm5xrDMHkoTqCpwke_RCxRotC0PTx89kJ8AgiLxe8hJridiHw3miQzJcwRwGa0R2QQItfSN_lOfAUjkeL2mjbtppZ_zedna6nZtJfN5n5B3J7SbVc4BojqbGFM1TeeOG7-jjD9VlaB-j6WcahhZs8yFOBMowhxkhSQ_J-AjJ_G8k2Lflj9RFw-FvMtVqbOglUI91oxrbNWC2AasNtMd2CTjV2Knso9o-ksDPpfIXgZ32E3KoDU7LYLYNn9kJ193KUOc2rh3dtrTRttQSNcWoCrZa46aacTmus6-KM-rcRtVYq_lalVPTYbPlYbUUmn7UqTlXcwOG-1QQuO3kAf3uqAPf6rA73TCP6YphOCXCi2MKNJsG1ZPVpHs9ead7Wk7pxWviymL0Wsxei9VrsXsto16L27wIr-Bx9Xi7rkPrdoY2dONGD2724FYPbtcvp2t41A073bDbDY87YVh3nbDeDRvdsFnDiqpsCN9gGireQTn9r4H_PiGJcJEI5agquBBssU8DxTu9_5UiC4F5RzEs1E0JHv8GHm4drg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 PM-080-070_Manage_Order_Acknowledgment_Process — PM-080-070_Manage_Order_Acknowledgment_Process

**Swim Lanes**: Buyer/Planner | **Tasks**: 2 | **Gateways**: 1

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
    subgraph Buyer/Planner
        n1[["fa:fa-cog Process Order Acknowledgement"]]
        n2["Receive Order Acknowledgement"]
        n3["PO Sent"]
        n4["Monitor Order Status"]
        n5["Manage Order Acknowledgment Process"]
        n6["Create and Process Purchase Order"]
        n7["Order Confirmation (OC) Received"]
        n8{{"fa:fa-code-branch Acknowledgement Required?"}}
        n9[["fa:fa-folder-open Transmit Order to Supplier"]]
    end
    n6 --> n9
    n9 --> n3
    n3 --> n8
    n8 -->|"Yes"| n7
    n7 --> n2
    n2 --> n1
    n8 -->|"No"| n4
    n1 --> n5
    class n1 serviceTask
    class n3 startEvt
    class n4 startEvt
    class n5 startEvt
    class n6 startEvt
    class n7 startEvt
    class n8 gateway
    class n9 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVVtv4jgU_itWqopZKWhzJWkedgSBSCvtTKuhs6vVMA8mOQarxs7aTinD8N_HJuHa9ml5QD2fv4vPSU_YOqWowMmc29st5VRnaNvTS1hBL0O9OVbQc1EL_I0lxXMGqmc5RHA9pT_2ND-qXyzNYgVeUbax6BQWAtDXP100NELmIoW56iuQlPTcXi3pCstNLpiQln0DKfHIPq07GglZgTwRPC_xy9hIGeVwgsMkSqLC6hSUglcXpiQmKSl7O3s5JtblEku9v36j4BN--YdWemlqgpkCw1nqFfsLz4HZHrVsLFY28vkwDKpsDjcDm9a4pHxh8MgzkMT86QTF3m6Hdre3M34MRY_jGUfmUzKs1BgIUtrAk2eNCGUsu4nyYRF7rtJSPEF2E0yScRi4pe0kM617rh1ufw10sdTZXLCqo_bXtocsqF9c-ZIFnis35vsqC3h1SsoHQRqkx6RR4ud-fkgihPyvJDNX-YjVU5c1CYugGB-z_HgQ595rv0Ob4ygZ-tdzAvlMSzgzLYoinJxGNRnEvve-6agIB15-ZbrAGtZ4czK8y6OjYREnhZ-8a9jmXd-ymT9IUR4Mw0lcxEfDZOQXw-Bdw2joR2l3Q-OzkLheolGzAfn7A8Ocg2zP7If7377NHIIzgvulWCAbCkqhe7sraFg-cbFmUC3MvnI9c75_P5MGRvkFSqDP8C7_jB4a-sM9mr46iMzBJ2HeFUJ2PlONdaMuWbFlYY4Xr8Ns1uHml6KBEeUSzNNBmFfH7h4aabZIdU6XksRI2oBccELlCmsqOPpwn_-Gum6rS0W63Z5GWEF_bra3XF4Pw4j_a6iE6uPM2e3O5HenJ0DMdoDsixo4ejQuakV1160WaNrUNaP7-3bxZg_bP_gA9ft_GK-uvGvLsCvDtky7MrXlz5nzL5hx_TQtd3jS0oKuDNrSv1J9FntR1MF-y4rP_oEteLZmFyfh8UV1AUdvw_Hb8OBtOHkbTg_reYHeHXbMcZ0VmMdMKyfbOvufJvPzVQHBDdPOznVwo8V0w0sn27_CnaaujN-YYrNZqxbc_QJYcTbm" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 PM-080-080_Monitor_Order_Status — PM-080-080_Monitor_Order_Status

**Swim Lanes**: Procurement Agent | **Tasks**: 5 | **Gateways**: 7

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
    subgraph Procurement Agent
        n1["fa:fa-user Monitor PO Status"]
        n2["fa:fa-user Review PO Item Details and Changes"]
        n3["fa:fa-user Monitor Supplier Ack and Confirmations"]
        n4["fa:fa-user Check Document Flow"]
        n5["fa:fa-user Modify PR with Change"]
        n6["Cancel Original Purchase Order"]
        n7["Receive Materials and Services"]
        n8["Create and Process Purchase Order"]
        n9{{"fa:fa-code-branch exclusiveGateway"}}
        n10{{"fa:fa-code-branch Issues/Variances Identified?"}}
        n11{{"fa:fa-code-branch Is Existing PO Required?"}}
        n12{{"fa:fa-code-branch Is Ariba PO Relevant?"}}
        n13{{"fa:fa-code-branch Approved?"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
        n16[["fa:fa-folder-open Modify Purchase Order"]]
    end
    n8 --> n9
    n9 --> n1
    n1 --> n2
    n2 --> n10
    n10 -->|"No"| n3
    n11 -->|"No"| n6
    n4 --> n7
    n3 --> n4
    n12 -->|"No"| n15
    n5 --> n13
    n10 -->|"Yes"| n11
    n11 -->|"Yes"| n12
    n12 -->|"Yes"| n14
    n14 --> n5
    n13 -->|"No"| n14
    n16 --> n9
    n15 --> n16
    n13 -->|"Yes"| n15
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 startEvt
    class n7 startEvt
    class n8 startEvt
    class n9 gateway
    class n10 gateway
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl2PozYU_SsWo1FeiMo3GR5aZUioRup0R5Ntq2rTBwcuwRpiqG3y0Wz-e-3wkYFl-rDNA4qP7znH99q-cNbiIgEt0O7vz4QSEaDzRGSwg0mAJhvMYaKjGvgdM4I3OfCJikkLKlbkn2uY6ZRHFaawCO9IflLoCrYFoN-edDSXxFxHHFM-5cBIOtEnJSM7zE5hkRdMRd_BLDXSq1sz9ViwBNgtwDB8M3YlNScUbrDtO74TKR6HuKBJTzR101kaTy5qcXlxiDPMxHX5FYdnfPyDJCKT4xTnHGRMJnb5L3gDucpRsEphccX2bTEIVz5UFmxV4pjQrcQdQ0IM07cb5BqXC7rc369pZ4o-L9YUyV-cY84XkCIuJLzcC5SSPA_unHAeuYbOBSveILizlv7CtvRYZRLI1A1dFXd6ALLNRLAp8qQJnR5UDoFVHnV2DCxDZyf5HHgBTW5OoWfNrFnn9OiboRm2Tmma_i8nWVf2GfO3xmtpR1a06LxM13ND41u9Ns2F48_NYZ2A7UkM70SjKLKXt1ItPdc0PhZ9jGzPCAeiWyzggE83wYfQ6QQj149M_0PB2m-4ymrzwoq4FbSXbuR2gv6jGc2tDwWduenMmhVKnS3DZYaUWsXktaMCzbfyWc-rHzW_rLUUBymeqnKj50Le24Khl09oJbCo-Fr761201Y9-hT2Bgwp-ErBDCxCY5BxhmqAww3QLA7o9braqyjInEpjHbzW5oClhOyxIQQcSTl8izEByFjK_a3aRvCP9eHdomZD0hF5e0YGIrFlln-FJRohpDDn6xMiWUJyjl4rJq8dBIrKP9ON9Gf8KMZA9oGd5FlSDqmuwqo_bIIOZ0mcgI69BanOA8_-0eDif2yxUh51uZI-IMwTHOK-49P25PoJr7XJ5v7XGOO2J8wr4D9ceLNPk6CmRtSMpgeSnoYT5kQRaHgkXskep3X-FvyvCRujWh3TZxze45uawx1R8w7XHufOyZMV-xMv5viK530fzvnQHK5V9Ddi0KIF252u4mc1uyuZZ_6EzNJ3-KHe2GT7Uw6ZhUbMeWs3QamaNdtpQwNe19mux1r7Ke9XiZh_3Gtyp-X4ztOuh07KsPst0mwm3sbWHtn-qM60izaFxN2MNxbuZzrZZVetm2oNldIFev1Zmuy5vyOw83HctVVWzfZX0YGsctsdhZxx2x2Gveyf3YH8cno3DD-27pZ-NMQ6b47A1DtvjsDMOu-Ow176rNF3bgWzYJNGCs3b9xJOfgQmkuMqFdtE1XIlidaKxFlw_hbSqTKTggmD5htrV4OVf2uI2_g==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.9 PM-080-090_Resolve_Order_Issues_with_Supplier — PM-080-090_Resolve_Order_Issues_with_Supplier

**Swim Lanes**: Procurement Agent | **Tasks**: 2 | **Gateways**: 0

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
    subgraph Procurement Agent
        n1["fa:fa-user Post Confirmation"]
        n2["fa:fa-user Resolve PO-related Issues"]
        n3(["fa:fa-play Notification Received"])
        n4(["fa:fa-play Confirmation Received"])
        n5(["fa:fa-stop Issues Resolved"])
        n6["Modify Purchase Order"]
    end
    n2 --> n5
    n1 --> n2
    n3 --> n6
    n4 --> n1
    class n1 userTask
    class n2 userTask
    class n3 startEvt
    class n4 startEvt
    class n5 endEvt
    class n6 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVMuO2jAU_RUrI5RWClKehGZRCQKRRup0UJm2i9KFSWywMHZkOzyK-PfaJIRHh1WziLgn53F9sX2wcl4gK7E6nQNhRCXgYKslWiM7AfYcSmQ7oAZ-QEHgnCJpGw7mTE3JnxPNC8udoRksg2tC9wadogVH4PuzAwZaSB0gIZNdiQTBtmOXgqyh2KeccmHYT6iPXXxKaz4NuSiQuBBcN_bySEspYegCB3EYh5nRSZRzVtyY4gj3cW4fTXOUb_MlFOrUfiXRC9z9JIVa6hpDKpHmLNWafoFzRM0alagMlldicx4GkSaH6YFNS5gTttB46GpIQLa6QJF7PIJjpzNjbSh4G80Y0E9OoZQjhIFUGh5vFMCE0uQpTAdZ5DpSCb5CyZM_jkeB7-RmJYleuuuY4Xa3iCyWKplzWjTU7tasIfHLnSN2ie86Yq_fd1mIFZektOf3_X6bNIy91EvPSRjj_0rScxVvUK6arHGQ-dmozfKiXpS6__qdlzkK44F3PyckNiRHV6ZZlgXjy6jGvchzH5sOs6DnpnemC6jQFu4vhp_SsDXMojjz4oeGdd59l9V8Inh-NgzGURa1hvHQywb-Q8Nw4IX9pkPtsxCwXALjVgl97JgCg4V-19_Nw7xfMwvDBMOuGTeYcKlAyhkmYg0V4Wxm_b5i-7fsb0hyukFg8toViOo5FOBZygrJW1XwoZWVVE_qK1cEk_zkrz1yRDao0JKPV5rwTnPd0yNNdNFIxcuml3OX9-yeJr_wguA9mFRCnyyJwKu5Jtrm9VavfzAfdLufdUBTenXpN2VQl72mDOvyevMZyXk738D--3DQHukbOHwfjppDeQP2Wq7lWGukR0cKKzlYp_tX39EFwrCiyjo6FqwUn-5ZbiWne8qqykL_lyMC9fZZ1-DxL5Wu3s4=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.10 PM-080-100_Modify_Purchase_Order — PM-080-100_Modify_Purchase_Order

**Swim Lanes**: Purchaser | **Tasks**: 6 | **Gateways**: 8

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
    subgraph Purchaser
        n1["fa:fa-user Process PO Approval"]
        n2["fa:fa-user Trigger PO Change Approval"]
        n3["fa:fa-user Manually Update PO Confirmation"]
        n4["fa:fa-user Rectify PO"]
        n5[["fa:fa-cog Update Confirmations In PO"]]
        n6[["fa:fa-cog Update Purchase Order Line Item"]]
        n7(["fa:fa-play PO Commit Received from Supplier"])
        n8(["fa:fa-stop No Action Needed"])
        n9["Transmit Order to Supplier"]
        n10{{"fa:fa-code-branch Is the PO Change Value Greater than $25k or10% (whichever is lower) as..."}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
        n12{{"fa:fa-code-branch Confirmation Received ?"}}
        n13{{"fa:fa-code-branch Modify Purchase Order?"}}
        n14{{"fa:fa-code-branch PO Approval Status"}}
        n15{{"fa:fa-code-branch Is the PO Applicable for Change Approval?"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n5 --> n13
    n7 --> n12
    n10 -->|"Yes"| n2
    n2 --> n11
    n11 --> n1
    n1 --> n14
    n12 -->|"No"| n3
    n12 -->|"Yes"| n5
    n3 --> n13
    n13 -->|"Yes"| n6
    n13 -->|"No"| n8
    n10 -->|"No"| n11
    n16 --> n9
    n14 -->|"Approved"| n16
    n14 -->|"Rejected"| n4
    n17 --> n10
    n4 --> n17
    n15 -->|"Yes"| n17
    n15 -->|"No"| n16
    n6 --> n15
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
    class n9 startEvt
    class n10 gateway
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVltvozgY_SsW3SgzEqm4k_KwqzQJo0rTiyadWa0m8-CASbwFjGyTNpvJf187mAQo0Wp381DV5zvnfBeDzV6LSIy0QBsM9jjHPAD7Id-gDA0DMFxBhoY6qIBvkGK4ShEbSk5Ccr7Afx1pplO8SZrEQpjhdCfRBVoTBL7e6WAihKkOGMzZiCGKk6E-LCjOIN1NSUqoZF-hcWIkx2wqdEtojOiZYBi-GblCmuIcnWHbd3wnlDqGIpLHLdPETcZJNDzI4lLyGm0g5cfyS4bu4dvvOOYbsU5gypDgbHiWfoYrlMoeOS0lFpV0Ww8DM5knFwNbFDDC-VrgjiEgCvOXM-QahwM4DAbL_JQUPM-WORC_KIWMzVACGBfwfMtBgtM0uHKmk9A1dMYpeUHBlTX3Z7alR7KTQLRu6HK4o1eE1xserEgaK-roVfYQWMWbTt8Cy9DpTvzt5EJ5fM409ayxNT5luvXNqTmtMyVJ8r8yibnSZ8heVK65HVrh7JTLdD13arz3q9ucOf7E7M4J0S2OUMM0DEN7fh7V3HNN47LpbWh7xrRjuoYcvcLd2fBm6pwMQ9cPTf-iYZWvW2W5eqIkqg3tuRu6J0P_1gwn1kVDZ2I6Y1Wh8FlTWGzAU0nFgyOar3D5y83vSy2BQQJHcsxAJkSMgadHMCkKSrYwXWo_GnyrzX-meL2Wukcw3cB8jS7I7LbsHuYlTNMd-FrEYmxHOckTTDPIMcnbWqet_YIijpOd0LRp7vcTLyLr2rlpy8BdXsmaOq9XV88KPMoTA3wW5wO44yjriP0PJ3GRwl3VSJZhLstEeItikFCSgUVZFCkWk9d-fGzIx2c546QADwRMIlkqeEAoRnGHfiPYz-JcYDJBVRgnTe_mxhr7_bmvGI1WQhhtwB0D4uhtbNg3mJYIfKJItC38BAh-sdwXQKhpDMCH1w2ONmgrQpgBcfQg-hFAdn19vdQOh2Y-sz8feovSkolJfKrej67M6pc19-08y9-6artffU_i4yPS2sR3Yqdf3Hj2wYJDXrKu0P2n0U7kjkTyZgMJod1X410h3n8bnf9vZeLMrv7JXTAa_Srnp9a-WltqbRoS-LnU_kCi-5_ivVcBSxHNmmgqoF6rpVOvLWX0QI4-dhevE7gqYHcqM-0O0esGlPO4W7rCz6V6lfVNvXYUsdoX-bZJutcNf0F_iiNHhU991RNTp3buqLVfE9xO3e8jdYF1RlWf6TYuAjnR-gJswVY_bPfDTj_sNq_CVsS7GPFPnxkteKy-CFrgTT9XbJG6Lduw2Q9b_bDdDzv9sNsPe_2wX8OarmVInEM41oK9dvxoFR-2MUpgmXLtoGuw5GSxyyMtOH7caeXx_phhKO7crAIPfwOXhHZU" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.11 PM-080-110_Cancel_Original_Purchase_Order — PM-080-110_Cancel_Original_Purchase_Order

**Swim Lanes**: Cost Accountant · Purchaser | **Tasks**: 8 | **Gateways**: 13

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
        n5["fa:fa-user Process Supplier Invoice for Received Quantity"]
        n6["fa:fa-user Process Supplier Payment"]
        n8[["fa:fa-cog Generate ERS Invoice"]]
        n12(["fa:fa-stop Purchase Order Canceled"])
        n17["Invoice Received"]
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n30{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Purchaser
        n1["fa:fa-user Reduce PO Quantity to Match GR/IR Quantity"]
        n2["fa:fa-user Process GRN For Cancellation Fee Line"]
        n3["fa:fa-user Delete Purchase Requisition"]
        n4["fa:fa-user Delete Purchase Order Without Cancellation Fees"]
        n7[["fa:fa-cog Delete PO Lines and Add Cancellation Fee Line"]]
        n9(["fa:fa-play Demand Change Identified"])
        n10(["fa:fa-play Supplier Driven Changes Received"])
        n11(["fa:fa-stop Purchase Order Is Kept"])
        n13["Information Of PO Cancelation Sent"]
        n14["Email Sent to Determine the Cancellation Fees"]
        n15["Confirmation on PO Received"]
        n16["Email Received on Cancellation Fees"]
        n18{{"fa:fa-code-branch Check If PR is Converted to PO?"}}
        n19{{"fa:fa-code-branch Check if PO Sent to Supplier?"}}
        n20{{"fa:fa-code-branch Check for Goods Receipt?"}}
        n21{{"fa:fa-code-branch Check for Invoice Receipt?"}}
        n22{{"fa:fa-code-branch Cancelation Fee Acceptable?"}}
        n23{{"fa:fa-code-branch Partial GR/IR Posted for PO ?"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n25{{"fa:fa-code-branch ERS Supplier ?"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch exclusiveGateway"}}
        n28{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n9 --> n18
    n18 -->|"Yes"| n19
    n22 -->|"No"| n11
    n22 -->|"Yes"| n23
    n23 -->|"No"| n24
    n1 --> n24
    n13 --> n25
    n23 -->|"Yes"| n1
    n2 --> n8
    n8 --> n29
    n29 --> n6
    n17 --> n29
    n6 --> n30
    n18 -->|"No"| n26
    n26 --> n3
    n4 --> n26
    n19 -->|"No"| n4
    n20 -->|"Yes"| n21
    n21 -->|"No"| n5
    n5 --> n27
    n25 -->|"Yes"| n2
    n25 -->|"No"| n17
    n10 --> n28
    n28 --> n15
    n15 --> n20
    n20 -->|"No"| n27
    n21 -->|"Yes"| n27
    n24 --> n7
    n7 --> n13
    n27 --> n14
    n14 --> n16
    n16 --> n22
    n30 --> n12
    n3 --> n30
    n19 -->|"Yes"| n28
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 startEvt
    class n10 startEvt
    class n11 endEvt
    class n12 endEvt
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 startEvt
    class n17 startEvt
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWO9v6jYU_VesPFVsEmhxfpDAh000kKrae68M3vY0ve6DmzhgNcQscWhZH__7rkkcSEharUNVpRz7nHvv8bVxeNECHlJtrF1dvbCEiTF66Yk13dDeGPUeSEZ7fVQAf5CUkYeYZj05J-KJWLJ_jtOwtX2W0yTmkw2L9xJd0hWn6PfbPpoAMe6jjCTZIKMpi3r93jZlG5LuPR7zVM7-QN1Ij47RyqFrnoY0PU3QdQcHNlBjltATbDqWY_mSl9GAJ2FNNLIjNwp6B5lczJ-CNUnFMf08o5_I81cWijU8RyTOKMxZi038kTzQWNYo0lxiQZ7ulBksk3ESMGy5JQFLVoBbOkApSR5PkK0fDuhwdXWfVEHRl-l9guATxCTLpjRCmQB4thMoYnE8_mB5E9_W-5lI-SMdfzBmztQ0-oGsZAyl631p7uCJstVajB94HJZTB0-yhrGxfe6nz2ND76d7-N-IRZPwFMkbGq7hVpGuHexhT0WKouh_RQJf0y8keyxjzUzf8KdVLGwPbU-_1FNlTi1ngps-0XTHAnom6vu-OTtZNRvaWO8WvfbNoe41RFdE0CeyPwmOPKsS9G3Hx06nYBGvmWX-ME95oATNme3blaBzjf2J0SloTbDllhmCziol2zXyeCbQJAh4ngiSiGJUfhL7270WkXFEBtJsJMPSLEPLfLuNGQC3yY6DYSjiKVrQgLIdDdFvOYgwsb_X_jqTGr4hNSf7DYXgNZL7rWIFfIVuaEJTsBPNFksVGwjnDGz8UFEywbdonqewKzKK7uQWRx5JAhrTEGg_ntMcYKlqVCX1XIzRy8spmZAOHmAnBmtEn4M4z2D-TbHQ99rhcEYz9f9Kgx3UWCBVQ3qecd3PBQ1zSH1-V9mPBEefiIBQN4ufbhcdy2K0L8vN4jPyubIrJoLxBPmUoo9wINYVzLrCFNyFFapsX9C_c5YxKVDnWa_ziuX6ysSa5-Iij6yu5dT7RGndHdPNEElCNAnDzmrOpUan_tnGsG2ndCPp3pokK4puQ-hRFrHLBtIbvKqxpyksclIKZOfNVePj1_v2NkO_0q1ossxj28L22xRF3UWy6qLOAllebCosnZ9tCIuPg7JPpmBXugEzEHz9vmU2lqeCx5OIqajwB1Hbtw0eVtGqEwLmvxXDbd813poGj-gWqlwglsHJlexoKkASipjf_dLYe3j0mgo7eqUsUOvV1DD01zTkwXfDeViu61Zc0PFb9Nqp0yJgdAicrbFsZTi_oT_kpelCwWxXmMOlAC5L5fEwhy8B8FFmBK5caFjvOvwMu50mz-9qg1zEGr4vlvM-mvvu8zkZocHgZ9ms5TN2JfD9XvtT9vN32YDliGGUI595MYCbA4pimGrErFMMS0Upop6ezRKwm8wqDTVQTFTpuiWvSrKsZ6iEncaEYfFs6s16VYqKaaiZ5bNVClXKozpRlWLoTTeq1HGdoWq1S2VHzbObCs0BtQKKgfVSQtlilL5gFQOrIHozTVW308yyil6NlBao59JaXK22AqpVLQm48qz01FAVmWXiuAKayzNqZuOeXSVlI6krdA022mGzHbbaYbsdHrbDzvnVuzbido6MqteaelF6B47LV5M6arSiZoeG1YHbHfiwA3c6cFe9LdThUSsMXdgK43bYaIfNdthqh-12eNgOO-1we5VGe5VmVaXW1zZwSyEs1MYv2vF3AvgtIaQRyWOhHfoayQVf7pNAGx_fp7V8GwJzygjcojcFePgXaaUgOg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.12 PM-080-120_Determine_Alternate_Materials_and_Approaches — PM-080-120_Determine_Alternate_Materials_and_Approaches

**Swim Lanes**: Procurement Agent | **Tasks**: 3 | **Gateways**: 3

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
    subgraph Procurement Agent
        n1["fa:fa-user Select New Supplier"]
        n2["fa:fa-user Create Purchase Requisition"]
        n3["fa:fa-user Identify Alternate Material Using Material Master Data"]
        n4(["fa:fa-stop Purchase Requisition Created"])
        n5["Receive Materials and Services"]
        n6["Monitor Order Status"]
        n7{{"fa:fa-code-branch Is Supplier Meeting Commitments?"}}
        n8{{"fa:fa-code-branch Others Suppliers?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n6 --> n7
    n2 --> n4
    n1 --> n9
    n9 --> n2
    n3 --> n9
    n7 -->|"No"| n8
    n7 -->|"Yes"| n5
    n8 -->|"Yes"| n1
    n8 -->|"No"| n3
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 endEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVd-P2jgQ_lesrFb0pCDlJ4E8tGIDOa10tFVp73Qq92CSCVjr2DnbWaCU__1sCIRQ9unyEGW-zHzfzMQz2VsZz8GKrcfHPWFExWjfU2sooRej3hJL6NnoBPyJBcFLCrJnfArO1Jz8OLq5QbU1bgZLcUnozqBzWHFA355tNNaB1EYSM9mXIEjRs3uVICUWu4RTLoz3AwwLpziqNa-euMhBtA6OE7lZqEMpYdDCfhREQWriJGSc5R3SIiyGRdY7mOQo32RrLNQx_VrCDG__Irlaa7vAVIL2WauS_oGXQE2NStQGy2rxem4GkUaH6YbNK5wRttJ44GhIYPbSQqFzOKDD4-OCXUTR18mCIX1lFEs5gQJJpeHpq0IFoTR-CJJxGjq2VIK_QPzgTaOJ79mZqSTWpTu2aW5_A2S1VvGS07xx7W9MDbFXbW2xjT3HFjt9v9EClrdKycAbesOL0lPkJm5yViqK4n8p6b6Kr1i-NFpTP_XSyUXLDQdh4vzKdy5zEkRj97ZPIF5JBlekaZr607ZV00HoOm-TPqX-wEluSFdYwQbvWsJRElwI0zBK3ehNwpPebZb18rPg2ZnQn4ZpeCGMntx07L1JGIzdYNhkqHlWAldrZNhqoceOKTRe6fvpvbmY-31hFTgucN-0G82BQqbQR9igeV1VlIBYWP9c-Xtd_0SALh99roU-mhLQF_i3JpIowlk3zu_GPec6DVLs0JgqEMxwzPTNDDf6JvXRb80ZlvoJTbDCXcrg3YVTKl7dTaJJMNeRv12FhjryC2RAXltdiTDLdQOOR0R2pQbaf8b1SuMCfTKrBM0VVvWNV7TfnxMyi7C_1KOcrdGzvPQSzQCUqS7hZUmU-SLyw8I6HK5YhvdZPunFKVqmX8JG98Ngm9Fa6jp_Px3TNkoP8umBDVC__16n35jeyQwa0z2Zo8YcnUyvMf3u28iYPxfWR76wfupabuC_TWM1Hjb48AZ3b_CGxr-aEJPQeTN0YO8-7N-Hg2aRdcDwskk78OA-HJ1Hv4MO76KjM2rZVgmixCS34r11_BnqH2YOBa6psg62hWvF5zuWWfHxp2HVVa4jJwTrWS5P4OE__IBeMg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.13 PM-080-130_Select_New_Supplier_&amp;_Reissue_PO — PM-080-130_Select_New_Supplier_&amp;_Reissue_PO

**Swim Lanes**: Procurement Agent | **Tasks**: 3 | **Gateways**: 2

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
    subgraph Procurement Agent
        n1["fa:fa-user Identify Alternate Suppliers"]
        n2["fa:fa-user Select Alternate Supplier"]
        n3["fa:fa-user Create Purchase Requisition"]
        n4["Perform Requisition Approval Process"]
        n5["Cancel Original Purchase Order"]
        n6{{"fa:fa-code-branch Original MM ID To Be Reordered?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8[["fa:fa-folder-open Determine Alternate Materials and Approaches"]]
    end
    n5 --> n6
    n1 --> n2
    n2 --> n7
    n7 --> n3
    n6 -->|"Yes"| n1
    n6 -->|"No"| n8
    n3 --> n4
    n8 --> n7
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
    class n8 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVVuPozYU_isWo1FeiMQ1UB5aJSSsRup0R820VbXZBweOE2scw9omk2w2_702kAtp5ml5sDifz_ediziHg5WXBViJ9fh4oJyqBB0Gag0bGCRosMQSBjZqgb-xoHjJQA6MDym5mtPvjZsbVDvjZrAMbyjbG3QOqxLQX082Gmsis5HEXA4lCEoG9qASdIPFPi1ZKYz3A8TEIU207mpSigLExcFxIjcPNZVRDhfYj4IoyAxPQl7yoidKQhKTfHA0ybHyPV9joZr0awnPePcPLdRa2wQzCdpnrTbsd7wEZmpUojZYXovtqRlUmjhcN2xe4ZzylcYDR0MC87cLFDrHIzo-Pi74OSh6nS440k_OsJRTIEgqDc-2ChHKWPIQpOMsdGypRPkGyYM3i6a-Z-emkkSX7timucN3oKu1SpYlKzrX4bupIfGqnS12iefYYq_Pm1jAi0ukdOTFXnyONInc1E1PkQghPxVJ91W8YvnWxZr5mZdNz7HccBSmzv_1TmVOg2js3vYJxJbmcCWaZZk_u7RqNgpd52PRSeaPnPRGdIUVvOP9RfCXNDgLZmGUudGHgm282yzr5Yso85OgPwuz8CwYTdxs7H0oGIzdIO4y1Dorgas1Mmq10GPHFRqv9Nnem4e7XxYWwQnBQ9Nu9FToa0r2aMwUCK5LQ_O6qhgFIRfW1yui1yfOgUGu7tD6LL_PSgUY35da6C9bAvoTvtVUUkVL3ucFmvcCgpRic-2ExlUlyi1mTY0gb3IMNSvFPAeGPgu6otw4nmJ9Niuh7z86HE7pmU02XOpZzNcX7vMzepqi1xJNTKrNToHit4V1PF6JRPdFYJezWtItfGq_lxtW_OXcGaLnBMSwrICjKeh-bvSSuurssz7MFpQI86LtAM7XYGrvitEz2r7wEA2Hv-rCOtNtTa8zvdaMOjNqTb8zR8b8sbD-NdI_NPkG_6Ns4LiD_ZYddGbc024-bhP_NNQ92LsP-_fh4LzvenB4Hx6dBrSHRnfR-DR7lm1tdN8xLazkYDW_LP1bK4DgminraFu4VuV8z3MraVa7VVeF1ptSrCdu04LH_wCxSkJ9" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.14 PM-080-140_Verify_Requirements_and_Terms_with_New_Supplier — PM-080-140_Verify_Requirements_and_Terms_with_New_Supplier

**Swim Lanes**: Procurement Agent | **Tasks**: 2 | **Gateways**: 4

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
    subgraph Procurement Agent
        n1["fa:fa-user Verify Terms and Conditions with New Supplier"]
        n2["Send PO to Supplier"]
        n3["Manage Order Acknowledgment Process"]
        n4["Cancel Original Purchase Order"]
        n5["Monitor Order Status"]
        n6{{"fa:fa-code-branch Is Supplier Meeting Commitments?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8{{"fa:fa-code-branch Can New Supplier Meet Requirement?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
        n10[["fa:fa-folder-open Select New Supplier and Reissue PO"]]
    end
    n5 --> n6
    n10 --> n2
    n1 --> n8
    n2 --> n1
    n7 --> n10
    n6 -->|"Yes"| n9
    n6 -->|"No"| n7
    n9 --> n3
    n7 --> n4
    n8 -->|"Yes"| n9
    n8 -->|"No"| n7
    class n1 userTask
    class n3 startEvt
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
    class n8 gateway
    class n9 gateway
    class n10 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVVGPokgQ_isdJhNfMAEEYXi4i4Ny2WRnd7LO7eWy7kMLhXam7Xa7m1HP9b9ftaCOnr7s8UCoj6rvq6qmiq1TyBKc1Lm_3zLBTEq2HTOHBXRS0plSDR2XNMBXqhidctAd61NJYcbsn72bHy7X1s1iOV0wvrHoGGYSyJ8fXDLAQO4STYXualCs6ridpWILqjaZ5FJZ7ztIKq_aq7WvHqUqQZ0cPC_2iwhDORNwgntxGIe5jdNQSFGekVZRlVRFZ2eT43JVzKky-_RrDU90_RcrzRztinIN6DM3C_6RToHbGo2qLVbU6u3QDKatjsCGjZe0YGKGeOghpKh4PUGRt9uR3f39RBxFyctwIgheBadaD6Ei2iA8ejOkYpynd2E2yCPP1UbJV0jvglE87AVuYStJsXTPtc3troDN5iadSl62rt2VrSENlmtXrdPAc9UG7xdaIMqTUtYPkiA5Kj3GfuZnB6Wqqv6XEvZVvVD92mqNenmQD49aftSPMu-_fIcyh2E88C_7BOqNFfCONM_z3ujUqlE_8r3bpI95r-9lF6QzamBFNyfChyw8EuZRnPvxTcJG7zLLevqsZHEg7I2iPDoSxo9-PghuEoYDP0zaDJFnpuhyTixbrXDshCGDGd6b9_YS_reJU9G0ol3bbvLVjtSGvIBaaEJFSTIcA2aYFJqsmJmTT7Ai43q55AzUxPn-jilApjF-HeT5MzHyhlMPnZ6ooDMgn-1IkkHxKuSKQznbp2dTBa3Pg0IMyqgogGMQmzFBOXmuFQ6DbmnO_SMrInEBSdWqjA019QVrf7s9lG7XVneKg1fMyQd9TJ08ARgcQ2zCYsGMTVD_PnF2u3cs8XUWWBe81uwN_mi-jouo5HoUFnnW4H0C5Av8qFlzfJfqD7-k7nvfjqde4VCC6solCDIGDoU5z8B-A1-AaV0DHix2sG0hHnTzICLS7f6G7WxN32vs4GA3ZtKaQWO2kyni1mxnQPSt_XPi_A14Wj-xwAv8k9zDcQs_NOG9c7awNZMbZMlVsv382XwPe-cM7h2X7BkcXoej63D_sCzO0PgqmlxFH66i2PN2aTius8DZpax00q2z_9fi_7iEitbcODvXobWR440onHT_T3LqZYmEQ0ZxVSwacPcvfJN51g==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.15 PM-080-150_Transmit_Dunning_Letter — PM-080-150_Transmit_Dunning_Letter

**Swim Lanes**: Procurement Agent | **Tasks**: 1 | **Gateways**: 3

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
    subgraph Procurement Agent
        n1["fa:fa-user Post Confirmation"]
        n2(["fa:fa-stop Dunning Letter Transmitted"])
        n3(["fa:fa-stop Good Receipt Posted in SAP S/4HANA"])
        n4["Create and Process Purchase Order"]
        n5{{"fa:fa-code-branch Acknowledgement/ASN Received?"}}
        n6{{"fa:fa-code-branch Shipment Received?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n1 --> n6
    n7 --> n2
    n6 -->|"No"| n7
    n6 -->|"Yes"| n3
    n5 -->|"Yes"| n1
    n4 --> n5
    n5 -->|"No"| n7
    class n1 userTask
    class n2 endEvt
    class n3 endEvt
    class n4 startEvt
    class n5 gateway
    class n6 gateway
    class n7 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVdtu4zYQ_RVCQeAWkLG6Wq4eWiiytS2QZoM63cVi3QdaGtpEZFIgKV_W8b-XlGQ71iZPqwdBPJxzzsyAQx2snBdgxdbt7YEyqmJ0GKgVrGEQo8ECSxjYqAU-Y0HxogQ5MDGEMzWj35swN6h2JsxgGV7Tcm_QGSw5oH__slGiiaWNJGZyKEFQMrAHlaBrLPYpL7kw0TcwJg5p3LqtOy4KEJcAx4ncPNTUkjK4wH4UREFmeBJyzoorURKSMckHR5Ncybf5CgvVpF9L-BvvvtBCrfSa4FKCjlmpdXmPF1CaGpWoDZbXYnNqBpXGh-mGzSqcU7bUeOBoSGD2fIFC53hEx9vbOTuboqfJnCH95CWWcgIESaXh6UYhQssyvgnSJAsdWyrBnyG-8abRxPfs3FQS69Id2zR3uAW6XKl4wcuiCx1uTQ2xV-1ssYs9xxZ7_e55ASsuTunIG3vjs9Nd5KZuenIihPyUk-6reMLyufOa-pmXTc5ebjgKU-dHvVOZkyBK3H6fQGxoDq9Esyzzp5dWTUeh67wvepf5IyftiS6xgi3eXwR_S4OzYBZGmRu9K9j69bOsF4-C5ydBfxpm4VkwunOzxHtXMEjcYNxlqHWWAlcrZNRqoceOKZQs9bvdNw9zv80tgmOCh6bd6JFLhVLOCBVrrChnc-u_V9HeL-dwqXiFJjVj-pyie1BKs5_02ZVrqr8Lzfv1FdHvET9yXqB_IAdaqcYUCkQZmiWPaPYh-DN5SHoCgeanAnSvEWZFUxJIiR5roWdCAvpkBvw62fBwOHmae2m40NnlK5Tkz4xvSyiWTUc-JLOHNpMNFH_MrePxlcTobYnZilZNN9_jRW_zYJeXtdSEj-2ZubD0VLUfzEXD4e_auVtG7dLrliOzfJlbD3xuvejdHvwVZIP7HR728G4gWNCqhr2wa9XmQJqEToN4BXvdTXAF-m-Bwfl-uoLD0-RcoaM30eiEWra1Bn00aWHFB6v5l-j_TQEE16WyjraFa8Vne5ZbcXPnWnVVaOaEYj0K6xY8_g9UdB7q" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.16 PM-080-160_Manage_Advanced_Shipping_Notifications — PM-080-160_Manage_Advanced_Shipping_Notifications

**Swim Lanes**: Procurement Agent | **Tasks**: 3 | **Gateways**: 4

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
    subgraph Procurement Agent
        n1[["fa:fa-cog Create Inbound Delivery"]]
        n2["Send Rejection to Supplier"]
        n3["Receive Supplier ASN"]
        n4["Receive Material Against Advanced Shipping Notification (ASN)"]
        n5["Manage Order Acknowledgement Process"]
        n6{{"fa:fa-code-branch Quality Check Required?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8{{"fa:fa-code-branch MQCS Certified Accepted?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n1
    n1 --> n4
    n6 -->|"Yes"| n9
    n9 --> n8
    n2 --> n9
    n8 -->|"Yes"| n7
    n6 -->|"No"| n7
    n8 -->|"No"| n2
    n7 --> n3
    n5 --> n6
    class n1 serviceTask
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVduOo0YQ_ZUWo5ETCUuAwTA8JPJgE62UmWTXuxtF631oN4XdcbshTeNLvP73VBt8Xc9DFB6Q6_Spc6oKyuwsVmRgxdbj445LrmOy6-g5LKETk86UVtCxSQN8porTqYCqYzh5IfWY_3OguX65MTSDpXTJxdagY5gVQD69s8kAE4VNKiqrbgWK5x27Uyq-pGqbFKJQhv0AUe7kB7f26LlQGagzwXFClwWYKriEM9wL_dBPTV4FrJDZlWge5FHOOntTnCjWbE6VPpRfV_BCN3_wTM8xzqmoADlzvRS_0ikI06NWtcFYrVbHYfDK-Egc2LikjMsZ4r6DkKJycYYCZ78n-8fHiTyZko_DiSR4MUGragg5qTTCo5UmORcifvCTQRo4dqVVsYD4wRuFw55nM9NJjK07thludw18NtfxtBBZS-2uTQ-xV25stYk9x1ZbvN94gczOTknfi7zo5PQcuombHJ3yPP9fTjhX9ZFWi9Zr1Eu9dHjycoN-kDjf6x3bHPrhwL2dE6gVZ3AhmqZpb3Qe1agfuM7bos9pr-8kN6IzqmFNt2fBp8Q_CaZBmLrhm4KN322V9fR3VbCjYG8UpMFJMHx204H3pqA_cP2orRB1ZoqWc2LUaoVrJzUZzPDenJtLul--TKycxjntsmJGEgXYDnknp0UtMzIEwVegthPr69eLJA9zxvgikA_wFzDNC0l0QcZ1WQoOCskX3B5yPwAD1DkxyGD8es3yL1gvWIHZcqyVcllhzdmKSgYZGc95WeJekNdC85wzerD-AdV-vJYLUO6FSjoD8pvZfDJgC1msBWSzZgxmJFBV11n93e48iwy6U1xFNifvayq43pJkDmyBLf9dcwXZzxNrv79IDu8nw4aJusK2fmlek5us6H7Wy_tkTBJQpkvse8AYlPp7z6f_6onPrPkhe6Tb_Qkffxu6Tei3Yd-E3ybWn4Aj-oZGLf7U0KI29JrweBrdZIU3aq_FFRxdw14Lh41orw2DJuxfLIkp92KVr07805_hFRzch_vH7b1Cw7todBd9OqKWbS1BLSnPrHhnHb5y-CXMIKe10Nbetmiti_FWMis-fA2suswwc8gpLumyAff_AqEITwg=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.17 PM-080-170_Manage_P-Card_Purchases — PM-080-170_Manage_P-Card_Purchases

**Swim Lanes**: Procurement Agent | **Tasks**: 4 | **Gateways**: 1

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
    subgraph Procurement Agent
        n1["fa:fa-user Identify Requirements Allowing Procurement Card Usage​"]
        n2["fa:fa-user Purchase Using Procurement Card"]
        n3["fa:fa-user Authorize CPC Card Holder"]
        n4[["fa:fa-cog Manage P-Card Purchases"]]
        n5(["fa:fa-play Item Needed to be Purchased"])
        n6["Purchase Materials and Services"]
        n7["Bank Statement Sent"]
        n8["Enable Payment"]
        n9["GL/Cost Center Spends Actualized"]
        n10{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n5 --> n1
    n1 --> n3
    n2 --> n10
    n10 --> n4
    n4 --> n7
    n7 --> n9
    n9 --> n8
    n10 --> n6
    n3 --> n2
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 startEvt
    class n6 startEvt
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVduO2jAQ_RUrqxWtFNRcCeShEgTSrtStUOnlofTBJA5Y6zip7SxLEf_eMQmBUPapPETMmTlnLhk7eyMpUmKExv39nnKqQrTvqQ3JSS9EvRWWpGeiGviOBcUrRmRPx2QFVwv65xhme-WLDtNYjHPKdhpdkHVB0LcHE42ByEwkMZd9SQTNemavFDTHYhcVrBA6-o4MMys7Zmtck0KkRJwDLCuwEx-ojHJyht3AC7xY8yRJCp52RDM_G2ZJ76CLY8U22WChjuVXkjzilx80VRuwM8wkgZiNytknvCJM96hEpbGkEs-nYVCp83AY2KLECeVrwD0LIIH50xnyrcMBHe7vl7xNir5OlxzBL2FYyinJkFQAz54Vyihj4Z0XjWPfMqUSxRMJ75xZMHUdM9GdhNC6Zerh9reErjcqXBUsbUL7W91D6JQvpngJHcsUO3he5SI8PWeKBs7QGbaZJoEd2dEpU5Zl_5UJ5iq-YvnU5Jq5sRNP21y2P_Aj61-9U5tTLxjb13Mi4pkm5EI0jmN3dh7VbODb1uuik9gdWNGV6BorssW7s-Ao8lrB2A9iO3hVsM53XWW1mosiOQm6Mz_2W8FgYsdj51VBb2x7w6ZC0FkLXG6QVqsEHDuu0HgNz9qvf9z-uTQyHGa4r8eNHlJw02yHvpDfFa05Eo0Z7B7sY0cpwiJF3yRek2XlWNZqafy60HW6uvNKwO5KOMPylk6X63a540ptCgH3A4rmUZ32I6wSEV2W97OlJcUaPWIOpaF5_0g45ZfAuST5b1pSyeAlPiiSo8-EpCRFqkAr0jJ1jW8vmAMgtl09wg7oi0kizFO0qNdMdusLgDCBs40WCqKPrS_0u-gEDSFoxvXViOZ4l__jH4H_w6d3USFhcOCF8SxKOJLwjhJVYQZTuhqmbe33pxaxEMVW9jFTqMQCM0bYh3p7l8bhUJNArP7DfdTvvweBxrRr021Mp_FaJ7dVA15je7UZNGZQm6PGHNXm8Io8aGy3Np2Lk6ELON0IHdi5Dbu3Ye_yEuh4_PYa7cCD23BwGx7ehke3YWi7uT0M08iJyDFNjXBvHL-R8B1NSYYrpoyDaeBKFYsdT4zw-C0xqjIF5pRiOOJ5DR7-AorgYDs=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.18 PM-080-180_Create_and_Maintain_Internal_Catalogue — PM-080-180_Create_and_Maintain_Internal_Catalogue

**Swim Lanes**: Buyer/Planner · Catalog Administrator | **Tasks**: 6 | **Gateways**: 3

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
    subgraph Buyer/Planner
        n1["fa:fa-user Upload Internal Item Catalog for Create/Update"]
        n2["fa:fa-user Publish Item Level Contract Workspace"]
        n3["fa:fa-user Create Requisition by Using Approved Catalogs"]
        n8(["fa:fa-play Internal Item Catalog Created"])
        n9(["fa:fa-stop Requisition Created"])
        n11["Catalog is Live"]
        n14{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Catalog Administrator
        n4[["fa:fa-cog Request Approval of Catalog from Intel Commodity Manager"]]
        n5["Notify Supplier about Catalog Rejection due to Validation Rules"]
        n6["Receive Catalog File in Buyer SAP Ariba Network"]
        n7(["fa:fa-play Creation and Maintenace of Internal Catalog Initiated on Supplier's End"])
        n10["CIF or Punchout Catalog Uploaded in Supplier Ariba Network"]
        n12{{"fa:fa-code-branch Catalog Approved by Commodity Manager?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n4 --> n12
    n3 --> n9
    n8 --> n1
    n12 -->|"Yes"| n14
    n11 --> n3
    n14 --> n11
    n1 --> n2
    n2 --> n14
    n6 --> n4
    n10 --> n6
    n7 --> n13
    n13 --> n10
    n5 --> n13
    n12 -->|"No"| n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n7 startEvt
    class n8 startEvt
    class n9 endEvt
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVltv4jgU_itWqopdCTS5EpqHXVFKVpU6VVW2M1qVeTCJA946dtZ2aFmG_77H5AKhdB5m8wA6n4-_79xiZ2slIiVWZF1ebimnOkLbnl6RnPQi1FtgRXp9VAFfsKR4wYjqGZ9McD2j_-7dHL94M24Gi3FO2cagM7IUBD3d9tEYNrI-UpirgSKSZr1-r5A0x3IzEUxI431BRpmd7dXqpWshUyIPDrYdOkkAWxnl5AB7oR_6sdmnSCJ42iHNgmyUJb2dCY6J12SFpd6HXyryGb99palegZ1hpgj4rHTO7vCCMJOjlqXBklKum2JQZXQ4FGxW4ITyJeC-DZDE_OUABfZuh3aXl3PeiqK7xzlH8CQMK3VDMqQ0wNO1RhllLLrwJ-M4sPtKS_FCogt3Gt54bj8xmUSQut03xR28Erpc6WghWFq7Dl5NDpFbvPXlW-TafbmB3xMtwtOD0mTojtxRq3QdOhNn0ihlWfa_lKCu8k-sXmqtqRe78U2r5QTDYGK_52vSvPHDsXNaJyLXNCFHpHEce9NDqabDwLE_Jr2OvaE9OSFdYk1e8eZAeDXxW8I4CGMn_JCw0juNslw8SJE0hN40iIOWMLx24rH7IaE_dvxRHSHwLCUuVui63BD56YFhzoms1szDnee5leEowwNTavRUMIFTdMs1kRwzdKtJjiZYYyaWKBMSTSSBXD89FSn8za1vR1Rul-qhXDCqVhXFHVkThiYwCRInGn0V8kXBfJ8weF2GSgs9kn9KqqimgqPFBj0peCvQuCikWJO0CU51mUa_tFQFg8acT6gSSGHrr0d7rw57lRZFR__8DsdUsSGlCt3R9Ulmjr_dNqTmgBws4BVPVoi8JaxU4P5HNUFza7ertsE7dtLCRmCc5nCyQvexFset9J-fDxLLfdhE6bpSkLrIDp2UIt_XxPQkz0VK9QZ9xhwvYTisb8eRB0B6LzTNNmhWFgWj0Bi8EKVuyR7J3yTZVyctCdICfcGMwngY5LGEA75biiEQPpKEQNItRUwZQZRXU4pm4wdzxi8wuif6FUalSxCe9HbfEyOGeQpJUEiLw2iZfNu2N0K3cCVR00EE_k0-PYWm_F1PbdPT2xgJM8rQq-OUq9cEWOiB5UchO-759rctbaYZ5vtdQ34_DEVF5v30LHEfDQa_mXhq26vsq9oc1cu16bjG_j63_jJN_G7GuFlxKk-vsRvidmtlNzpuvdzsH1Z2S2dX9rC2w9q9pa_jdOpzkgenDk2k92IfaHB0nppgmnukA7vnYe887B9fHZ2VsL18O_DoPHxVX5_dCO3zzlDn87jb3Dld2DsP-w1s9a2cyBzT1Iq21v47DL7VUpLhkmlr17dwqcVswxMr2n-vWOX-oL-hGM6gvAJ3_wETmyV1" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.19 PM-080-210_Vendor_Managed_Inventory_(Pay_Upon_Receipt_OEM) — PM-080-210_Vendor_Managed_Inventory_(Pay_Upon_Receipt_OEM)

**Swim Lanes**: AP Processor · Buyer · Warehouse Manager | **Tasks**: 6 | **Gateways**: 0

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
    subgraph AP Processor
        n2["fa:fa-user Validate Invoice"]
        n6[["fa:fa-cog Process ERS Invoice"]]
        n8(["fa:fa-stop Invoice Validated"])
        n13["Invoice Received"]
    end
    subgraph Buyer
        n3[["fa:fa-cog Send Inventory Report and Min/Max Data"]]
        n4[["fa:fa-cog Create Purchase Order"]]
        n5[["fa:fa-cog Create Inbound Delivery"]]
        n7(["fa:fa-play ROP and Min/Max Data Monitored by DSV"])
        n9["Report and Data Sent"]
        n10["PO Sent"]
        n12["Receive Shipment Details"]
    end
    subgraph Warehouse Manager
        n1["fa:fa-user Receive Materials and Services"]
        n11["GR Notification Sent"]
    end
    n3 --> n9
    n9 --> n12
    n4 --> n10
    n1 --> n11
    n5 --> n1
    n10 --> n5
    n12 --> n4
    n11 --> n6
    n7 --> n3
    n6 --> n13
    n13 --> n2
    n2 --> n8
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVltv4jgU_itWqopdKWhzJTQPK1Egq0rDFMFu52G6DyZxwGqwI9uhZSv--x7nBsnAvEwekM53vvOdC_ZJPo2YJ8QIjfv7T8qoCtHnQO3IngxCNNhgSQYmqoAXLCjeZEQONCflTK3pfyXN9vIPTdNYhPc0O2p0TbacoH-eTDSBwMxEEjM5lETQdGAOckH3WBynPONCs-_IOLXSMlvteuQiIeJMsKzAjn0IzSgjZ9gNvMCLdJwkMWdJRzT103EaD066uIy_xzssVFl-IckCf3yjidqBneJMEuDs1D77gjck0z0qUWgsLsShGQaVOg-Dga1zHFO2BdyzABKYvZ0h3zqd0On-_pW1SdGX1StD8MQZlnJGUiQVwPODQinNsvDOm04i3zKlEvyNhHfOPJi5jhnrTkJo3TL1cIfvhG53KtzwLKmpw3fdQ-jkH6b4CB3LFEf47eUiLDlnmo6csTNuMz0G9tSeNpnSNP2lTDBX8TeWb3WuuRs50azNZfsjf2r9qNe0OfOCid2fExEHGpML0SiK3Pl5VPORb1u3RR8jd2RNe6JbrMg7Pp4FH6ZeKxj5QWQHNwWrfP0qi81S8LgRdOd-5LeCwaMdTZybgt7E9sZ1haCzFTjfockSaUEiJReVSz_M-f5qpDhM8VBPGr3gjCbQC3piBw5TejX-vSCPvrfsmG8bPTRfrS_4lwHj39oAqXjesNo0CfB_v-DbLvAb0orEhB5KTkWBU9dr6rE4kstu3G6Ba4jQOQlTXBxBMOdwczCAC8r-gPuKZljhXs1eV2MqiJ7HshBw7yRBz3qJ9EL8qyFPbMMLyDUjGbQhjr2g4DybPIOjs3pe_lAaWnBYoVyQBG2OaLZ-6c3rASQuuipDoGnV_dtsC2jL52sepxQo54zWO5rvgQIFK0wz-ZO5f8OC7DicGLTADG87_4HdPVGN-gJGote2LCtdV5dQ9srRsX-t0FeuaEpjrChn3arbUpiLhsM_YQK1-VCZtlPbXm3X94rZtV1vA-bXduO2KttvbKeyvcau40e1HVSmW5ujWq2x7bq6pppabXxxyXVJzXLrwM512L1cXB2Pd9Pj3_SMbnqC9kXSgcf1zu-AD9e5MMzruH0Dd27gbosbprEnYo9pYoSfRvn5AJ8YCUlxkSnjZBq4UHx9ZLERlq9Zo8j1fplRDAd2X4Gn_wHt86_O" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.20 PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI) — PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI)

**Swim Lanes**: AP Processor · Buyer · MRP Controller · Supplier · Warehouse Manager | **Tasks**: 9 | **Gateways**: 0

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
    subgraph AP Processor
        n9[["fa:fa-cog Process ERS Invoice"]]
    end
    subgraph Buyer
        n1["fa:fa-user Validate Invoice"]
        n4[["fa:fa-cog Create Purchase Requisition"]]
        n5[["fa:fa-cog Create IB Delivery"]]
        n6[["fa:fa-cog Create Purchase Order"]]
        n7[["fa:fa-cog Modify PO Per OEM Supplier Confirmation"]]
        n11(["fa:fa-stop Invoice Validated"])
        n12["PO Sent"]
        n13["PO Info Shared for Monitoring"]
        n14["ASN Received"]
        n15["PO Confirmation Received"]
        n16["Invoice Received"]
    end
    subgraph MRP Controller
        n2["fa:fa-user Modify Material Master"]
        n10(["fa:fa-play ROP and Min/Max Data Monitored by DSV"])
    end
    subgraph Supplier
        n8[["fa:fa-cog Perform MRP Planning"]]
    end
    subgraph Warehouse Manager
        n3["fa:fa-user Create Goods Receipt"]
    end
    n14 --> n5
    n5 --> n3
    n12 --> n15
    n10 --> n2
    n4 --> n6
    n6 --> n12
    n13 --> n14
    n7 --> n13
    n15 --> n7
    n3 --> n9
    n9 --> n16
    n16 --> n1
    n1 --> n11
    n2 --> n8
    n8 --> n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 startEvt
    class n11 endEvt
    class n12 startEvt
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl1v6jgQ_StWqopdKWjzSWgeVuIrq0qXW1Tu7X24vQ8mccCqsbN2QstW_PcdEwcIbfZleUDMmZkzM8fOkHcrFRmxYuv29p1yWsbovVduyJb0YtRbYUV6NqqBJywpXjGiejomF7xc0n-OYW5QvOkwjSV4S9leo0uyFgR9v7fRCBKZjRTmqq-IpHnP7hWSbrHcTwQTUkffkGHu5MdqxjUWMiPyHOA4kZuGkMooJ2fYj4IoSHSeIqngWYs0D_NhnvYOujkmXtMNluWx_UqROX77QbNyA3aOmSIQsym37AteEaZnLGWlsbSSu0YMqnQdDoItC5xSvgY8cACSmL-codA5HNDh9vaZn4qiL4_PHMEnZVipKcmRKgGe7UqUU8bim2AySkLHVqUULyS-8WbR1PfsVE8Sw-iOrcXtvxK63pTxSrDMhPZf9QyxV7zZ8i32HFvu4fuqFuHZudJk4A294anSOHIn7qSplOf5_6oEuspvWL2YWjM_8ZLpqZYbDsKJ85GvGXMaRCP3WicidzQlF6RJkvizs1SzQeg63aTjxB84kyvSNS7JK96fCe8mwYkwCaPEjToJ63rXXVarhRRpQ-jPwiQ8EUZjNxl5nYTByA2GpkPgWUtcbNBogTQhUUrI2qU__O7nz2crx3GO-6lYNyFo9rhE93wnQKhn69evOgFO_Yp0XO3JJZt7ItPnhp4woxkoc0F1ERy0S08k0aGLSsIFVwQ9kr8rqmhJBT-3cEwMP028H6MpYXRH5P4qfvDfhR70WrhKidopc5HRfI8WD2gBYz3M5mhZFQWjYEwEz6nc4k_6dN3fTiyqFEUjw0mXDBJ-v0zwIB6KLAkv21q5fu2557lAS1gAJEO5kNAYrFghYU1cxQcQP1p-BRVTAppkV-6wprtsvit0AKFN4x9CPl6J-eNC08LVZKx1N7z23TCSzkEGvc3hhyqPx3BZ2zkLWDB4vB4fFgjzDM0p_wPWLZriEjcagCKrPZoun86ifuyuObaLIsOrJ4BIEHZ7nGPBMOe1tp3z_oCz2AgYCSbgeN2i9tsjm4v3lxCZqqUsyo9Kwtmhfv9PuObGDmvTb9xebbuN33VqwDO2SR8Yc2DCG7frGyAwQGTsUwFTMDK2ib8z5p0Jb_jdpkBjG7OxTbtDYw5rM7jYdzqn2fMt2Psc9j-Hg8vV3vKEnZ5Bpyfq9Aw7PXedHjij5v-5jbvmv7SNeh3RfgcedOBhBz444ZZtbQlsAJpZ8bt1fC-Dd7eM5LhipXWwLVyVYrnnqRUf31-sqtCba0oxXP9tDR7-BdiaGJ4=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.21 PM-080_Purchase_Materials_and_Services — PM-080_Purchase_Materials_and_Services

**Swim Lanes**: Procurement Agent | **Tasks**: 8 | **Gateways**: 23

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
    subgraph Procurement Agent
        n1["Transmit Remind Letter"]
        n2["Identify Requirements Allowing Procurement Card Usage"]
        n3["Create and Maintain Internal Catalogue"]
        n4["Purchase Using Procurement Card"]
        n5["fa:fa-user Receive Order Acknowledgment​"]
        n6["fa:fa-user Process Order Acknowledgement​"]
        n7["fa:fa-user Receive Order Confirmation/ASN"]
        n8["fa:fa-user Process Order Confirmation/ASN"]
        n9(["fa:fa-play Requirement Identification Initiated"])
        n10(["fa:fa-stop Alternate Materials and Approaches Determined"])
        n11["Receive Materials and Services"]
        n12["Manage Contracts"]
        n13["Manage Subcontractor Manufacturing"]
        n14["Enable Payment"]
        n15["Manage Quotation"]
        n16["Manage Contracts"]
        n17["Create and Maintain Purchase Requisitions"]
        n18["Create and Maintain Subcon Purchase Requisitions"]
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-code-branch Acknowledgement Required?"}}
        n22{{"fa:fa-code-branch Issue Identified?"}}
        n23{{"fa:fa-code-branch Is Supplier ​ Meeting Commitments?​"}}
        n24{{"fa:fa-code-branch Can Terms be Altered?"}}
        n25{{"fa:fa-code-branch Is Material Required Immediately?"}}
        n26{{"fa:fa-code-branch Other Suppliers?"}}
        n27{{"fa:fa-code-branch Can New supplier Meet Requirements?"}}
        n28{{"fa:fa-code-branch Is Supplier Meeting Commitments?"}}
        n29{{"fa:fa-code-branch Is Supplier Meeting Commitments?"}}
        n30{{"fa:fa-code-branch exclusiveGateway"}}
        n31{{"fa:fa-code-branch exclusiveGateway"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n33{{"fa:fa-code-branch exclusiveGateway"}}
        n34{{"fa:fa-code-branch exclusiveGateway"}}
        n35{{"fa:fa-code-branch exclusiveGateway"}}
        n36{{"fa:fa-code-branch exclusiveGateway"}}
        n37{{"fa:fa-code-branch Cluster?"}}
        n38{{"fa:fa-code-branch exclusiveGateway"}}
        n39{{"fa:fa-arrows-alt parallelGateway"}}
        n40{{"fa:fa-arrows-alt parallelGateway"}}
        n41{{"fa:fa-arrows-alt parallelGateway"}}
        n42[["fa:fa-folder-open - 010 Select New Supplier and Reissue PO"]]
        n43[["fa:fa-folder-open Create PO Manually With ’Text Materials'"]]
        n44[["fa:fa-folder-open Release Scheduling Line from Scheduling Agreement"]]
        n45[["fa:fa-folder-open Create and Release Contract Order"]]
        n46[["fa:fa-folder-open Create Plant-to-Plant Transfer Order"]]
        n47[["fa:fa-folder-open Transmit Order to Supplier"]]
        n48[["fa:fa-folder-open Monitor Order Status"]]
        n49[["fa:fa-folder-open Resolve Order Issues with Supplier"]]
        n50[["fa:fa-folder-open Modify Purchase Order"]]
        n51[["fa:fa-folder-open Transmit Dunning Letter"]]
        n52[["fa:fa-folder-open Verify Requirements and Terms with New Supplier"]]
        n53[["fa:fa-folder-open Determine Alternate Materials and Approaches"]]
        n54[["fa:fa-folder-open Cancel Original Purchase Order"]]
        n55[["fa:fa-folder-open Create Purchase Order"]]
    end
    n15 --> n19
    n16 --> n19
    n19 --> n39
    n39 --> n43
    n39 --> n46
    n18 --> n20
    n20 --> n55
    n40 --> n30
    n47 --> n21
    n48 --> n23
    n39 --> n45
    n46 --> n40
    n45 --> n40
    n7 --> n8
    n2 --> n3
    n3 --> n4
    n30 --> n47
    n22 -->|"No"| n32
    n32 --> n48
    n24 -->|"No"| n34
    n33 --> n7
    n23 -->|"Yes"| n33
    n28 -->|"Yes"| n33
    n29 -->|"Yes"| n33
    n29 -->|"No"| n34
    n25 -->|"Yes"| n35
    n41 --> n36
    n36 --> n14
    n9 --> n2
    n17 --> n19
    n44 --> n40
    n6 --> n31
    n21 -->|"No"| n31
    n21 -->|"Yes"| n5
    n31 --> n22
    n24 -->|"Yes"| n50
    n34 --> n25
    n25 -->|"No"| n1
    n26 -->|"No"| n53
    n43 --> n40
    n1 --> n28
    n28 -->|"No"| n51
    n22 -->|"Yes"| n49
    n49 --> n32
    n5 --> n6
    n35 --> n26
    n4 --> n36
    n23 -->|"No"| n24
    n54 --> n20
    n39 --> n44
    n27 --> n35
    n27 -->|"Yes"| n54
    n52 --> n27
    n26 -->|"Yes"| n37
    n38 --> n52
    n8 --> n41
    n41 --> n11
    n51 --> n29
    n41 --> n13
    n41 --> n12
    n37 -->|"Cluster 1, Cluster 3"| n42
    n50 --> n30
    n53 --> n10
    n37 -->|"Cluster 2"| n38
    n42 --> n38
    n55 --> n30
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 startEvt
    class n10 endEvt
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
    class n39 gateway
    class n40 gateway
    class n41 gateway
    class n42 subProc
    class n43 subProc
    class n44 subProc
    class n45 subProc
    class n46 subProc
    class n47 subProc
    class n48 subProc
    class n49 subProc
    class n50 subProc
    class n51 subProc
    class n52 subProc
    class n53 subProc
    class n54 subProc
    class n55 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtWf1v4jga_lcsRiPuJNAlcUwCP-yKoeVUaTrTG7q7Om33BxMciCYknJ1My3b7v9_rxDaNcTordiu1gof3ed5Pf5A-D5Jywwazwfv3z1mRVTP0PKx2bM-GMzRcU8GGI9QCP1Oe0XXOxFDapGVRrbLfGzM_PDxJM4kt6T7LjxJdsW3J0E83IzQHYj5CghZiLBjP0uFoeODZnvLjosxLLq3fsTj10sab-uhDyTeMnww8L_ITAtQ8K9gJxlEYhUvJEywpi01HNCVpnCbDFxlcXj4mO8qrJvxasFv69Eu2qXbwPqW5YGCzq_b5R7pmucyx4rXEkpp_08XIhPRTQMFWB5pkxRbw0AOI0-LrCSLeywt6ef_-oTBO0f3VQ4HgJ8mpEFcsRaIC-PpbhdIsz2fvwsV8SbyRqHj5lc3eBdfRFQ5GicxkBql7I1nc8SPLtrtqti7zjTIdP8ocZsHhacSfZoE34kf4a_lixebkaTEJ4iA2nj5E_sJfaE9pmv4lT1BXfk_FV-XrGi-D5ZXx5ZMJWXjnejrNqzCa-3adGP-WJeyV6HK5xNenUl1PiO_1i35Y4om3sES3tGKP9HgSnC5CI7gk0dKPegVbf3aU9fqOl4kWxNdkSYxg9MFfzoNewXDuh7GKEHS2nB52SKrVHJZdUaH5Fv62n8ufwv_1YXAPIyf2WYW-sH1WbNBHVlWMPwx-e2UXgN3NBrhZegS7_9VZKyjQPIfBhGHtuFlQvkE_CbplXRkMMgvOoGSIgqdbmhUV_KKbAjwWNAdiRfNyW1u8EHh3NYf5F7APCJe7LoEAIaWzlI7lGEHECcu-MfRZ7gNonnwtysecbbaS_VAHnrfu0idduvTFhDijsz5-9Jb7RVmkGd_TKiuLf81Xn7rU-C3Xb1On_zDcQ047fUKqeVnScKHgWZVBG2TZ_vl6HryThqjKA7S36Qw07Bb-yN1XNK2bHw68pMmOCXTF4AOYnHMxOV069y591S5F0U3Al2N2SwuYG5lqxWlS2Sb4ZLKq14myKjk4KOoUXtYcxsMiyfm5LuSRg-7osela14CcVP9Tl1VTJMtk8v3Yop7xNqPbdERkUt3mxj3cNsk_JTF9fta9kyfxeA0LO9kh9pTktYAe_Lvdqh4GLy-vl7Z3Gc1306zVoYdw86PND9z8GyFqZsbVwcN9PCjV4ZBnsEzaJYluGavkVrEo97C9NdvVj3q1djVDt-aCFugeZlugNWtXgiMe0huPHnlTA3Sz37ONXHf58Uxn4tb5DDcmblITZ7SoP_RP7BFOAVUTWYzOzn2mFH-_sM6KWjLTv0UGXzaV2L-MFlxGw5fRwsto5DLa5DJa32ABCcb6rF_xZV5eTQvlvHwUY5pX6EA5zXOWu0mhdwnJv4QU_GqOwxTur4yPywMr0Bh5vgeHWM6SqllmZrTl3v2FZc0mdvcZNujONQa75dS-f_e5OcQgniP6Jat2zT7mT-_ZU3U6Poe2ZujW_ALByfNiBWf0ps7lcvsIZzRKebl_Dc63nDF1InZ0yZuxtnm2LvRx2F5SbJ3J2znnFL4iVOW4eYGau2gKdXRKRW4pc4FtL0lVadphC8RugdsSrkOlcopWcPzXwqZO-8osytxc7ZrDS6BH2byeGIjXF8NG3q3NOe8qAPG_U4CruiiaTusrfIfdM8w_y-_R1q1etrc9-ZpcXo-4rdoz0-ZW-CeukLZkz0jDmZawHCqTbTP5ZeHtWr09v31c-H7bvoA7IRqPf5DXKg1MbGDaAlgDWAEhtoGJpsQtoL_twosWIEQBoQKwtggjRfE1oDXOvBgNFWloNIgFKM1YR6F8akFlrd-qkMJImzf2fzwMPpUPgz_k8aktlVBohEPL0mgqH0YSK8P_ynGQljqYIO79ZPrdT2y3AbEppma-qoFuFdbt1lxVZZ2rH1njEIZWkZUA1o0LfCuqsw90VDoorIIKAruexlI7w8p7QOxUlTfjbNLFiS5aiK34tfPY7oRm-vY86KhCUxO9RHQCahBNkdX7QAOh1QUzF8pnoLtBQmslmVVgeq0aZFrcAq-LZ8TU3AaRXSQzJ_oTrFYf0Rmp96FvDZKvAaLrOLUtsA2YdaQjVbct5I_0xQvhtsKmoPZ-QVQbfa9PLGgz0m0N9erXACFdyebRlGydfiTXgSduOHLDsRuemoeYHRguWe0Dxy7q91gHPTjuwcMenPTgkx486sHjHnyqnxp2YDgKnLDvhgM3jN1w6IaJG5644cgNx27YnSV2Z4ndWWJ3ltidJXZnid1ZYneW2J0ldmeJ3VmG7ixDd5awAtVT3y6M3XDohokbnrjhyA3HbnjqhGHvccK-G3ZnSdxZEneWxGQ5GA32cMOk2WYwex40_1eC_z1tWErrvBq8jAa0rsrVsUgGs-b_L4P6sIHaX2UUHovvW_Dl_1eMSwQ=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Procurement Agent | PM-080-010_Create_PO_Manually_With_’Text_Materials’, PM-080-020_Release_Scheduling_Line_from_Scheduling_Agreement, PM-080-030_Create_and_Release_Contract_Order, PM-080-040_Create_Plant-to-Plant_Transfer_Order, PM-080-050_Create_and_Process_Purchase_Order, PM-080-060_Transmit_Order_to_Supplier, PM-080-080_Monitor_Order_Status, PM-080-090_Resolve_Order_Issues_with_Supplier, PM-080-120_Determine_Alternate_Materials_and_Approaches, PM-080-130_Select_New_Supplier_&amp;_Reissue_PO, PM-080-140_Verify_Requirements_and_Terms_with_New_Supplier, PM-080-150_Transmit_Dunning_Letter, PM-080-160_Manage_Advanced_Shipping_Notifications, PM-080-170_Manage_P-Card_Purchases, PM-080_Purchase_Materials_and_Services | |
| Buyer/Planner | PM-080-070_Manage_Order_Acknowledgment_Process, PM-080-180_Create_and_Maintain_Internal_Catalogue,  | |
| Purchaser | PM-080-100_Modify_Purchase_Order, PM-080-110_Cancel_Original_Purchase_Order,  | |
| Cost Accountant | PM-080-110_Cancel_Original_Purchase_Order,  | |
| Catalog Administrator | PM-080-180_Create_and_Maintain_Internal_Catalogue,  | |
| AP Processor | PM-080-210_Vendor_Managed_Inventory_(Pay_Upon_Receipt_OEM), PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI),  | |
| Buyer | PM-080-210_Vendor_Managed_Inventory_(Pay_Upon_Receipt_OEM), PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI),  | |
| Warehouse Manager | PM-080-210_Vendor_Managed_Inventory_(Pay_Upon_Receipt_OEM), PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI),  | |
| MRP Controller | PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI),  | |
| Supplier | PM-080-220_Vendor_Managed_Inventory_(Pay_upon_Receipt_Third_Party_VMI),  | |

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for PM-080. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
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

<div class="page-footer"><span>Page 27</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for PM-080.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for PM-080.

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

<div class="page-footer"><span>Page 28</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
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

<div class="page-footer"><span>Page 29</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for PM-080:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 30</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for PM-080:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 31</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
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

<div class="page-footer"><span>Page 32</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-080 — Purchase Materials and Services</span></div>
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
*PM-080 — Architecture Document (TOGAF BDAT) · Procure To Pay · Generated: March 2026*

