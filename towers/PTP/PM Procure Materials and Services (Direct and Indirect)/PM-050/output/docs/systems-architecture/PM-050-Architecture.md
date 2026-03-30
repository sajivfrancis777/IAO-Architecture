<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">PM-050 — Manage Quotation</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Procure To Pay (PTP) Tower<br/>
  Capability PM-050 · PM Procure Materials and Services (Direct and Indirect)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **PM-050 Manage Quotation** within the IAO program. It includes 19 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Procure To Pay (PTP) |
| **Process Group** | PM Procure Materials and Services (Direct and Indirect) |
| **Capability** | PM-050 - Manage Quotation |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 3 Reports, 171 Interfaces, 16 Conversions, 171 Enhancements, 7 Forms, 10 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Procure To Pay |
| **L1 Process** | PM Procure Materials and Services (Direct and Indirect) |
| **L2 Capability** | PM-050 - Manage Quotation |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Procurement Process Standardization | Standardize procurement processes across direct, indirect, and services on S/4 HANA + Ariba | IDM 2.0 Procurement Excellence | High |
| 2 | Supplier Collaboration Enhancement | Enable digital supplier collaboration for consignment, subcontracting, and quality management | Supplier Ecosystem | High |
| 3 | Payment Automation | Automate invoice verification, three-way matching, and payment execution | Finance Efficiency | Medium |
| 4 | PM-050 Process Migration | Migrate Manage Quotation business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Procurement | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| PO Cycle Time | < 24 hours | Requisition approval to PO dispatch to supplier | 48 hours (current) | Procurement Lead |
| Invoice Automation Rate | > 80% | Invoices processed without manual intervention (touchless) | 45% (current) | AP Manager |
| Supplier On-Time Delivery | > 95% | Supplier adherence to confirmed delivery date | 89% (current) | Supplier Management |
| PM-050 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **19 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for PM-050 Manage Quotation.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | PM-050-010_Identify_Need_for_RFQ | PM-050-010_Identify_Need_for_RFQ | Commodity Manager | 6 | 0 |
| 2 | PM-050-020_Determine_Material_Specifications | PM-050-020_Determine_Material_Specifications | Commodity Manager | 5 | 3 |
| 3 | PM-050-030_Establish_Material_Profile | PM-050-030_Establish_Material_Profile | Commodity Manager | 3 | 1 |
| 4 | PM-050-030_Establish_Material_Profile_(Copy) | PM-050-030_Establish_Material_Profile_(Copy) | Commodity Manager | 3 | 1 |
| 5 | PM-050-040_Identify_Potential_Suppliers | PM-050-040_Identify_Potential_Suppliers | Commodity Manager | 2 | 0 |
| 6 | PM-050-050_Identify_Supplier_Rationalization_Opportunities | PM-050-050_Identify_Supplier_Rationalization_Opportunities | Commodity Manager | 6 | 2 |
| 7 | PM-050-060_Manage_Tendering_Process | PM-050-060_Manage_Tendering_Process | Procurement Agent | 4 | 4 |
| 8 | PM-050-070_Create_Supplier_RFQ | PM-050-070_Create_Supplier_RFQ | Commodity Manager | 8 | 0 |
| 9 | PM-050-080_Issue_RFQ | PM-050-080_Issue_RFQ | Commodity Manager | 6 | 2 |
| 10 | PM-050-090_Conduct_Pre-bid_Quotation_Meeting | PM-050-090_Conduct_Pre-bid_Quotation_Meeting | Commodity Manager, Sourcing Manager | 6 | 0 |
| 11 | PM-050-100_Receive_Supplier_Quotations | PM-050-100_Receive_Supplier_Quotations | Commodity Manager | 4 | 0 |
| 12 | PM-050-110_Process_Supplier_Quotations | PM-050-110_Process_Supplier_Quotations | Commodity Manager | 5 | 0 |
| 13 | PM-050-120_Perform_Price_Simulation | PM-050-120_Perform_Price_Simulation | Commodity Manager | 8 | 0 |
| 14 | PM-050-130_Perform_Total_Cost_Model_Analysis | PM-050-130_Perform_Total_Cost_Model_Analysis | Procurement Agent | 4 | 0 |
| 15 | PM-050-140_Supplier_Onboarding | PM-050-140_Supplier_Onboarding | Supplier Administrator | 4 | 0 |
| 16 | PM-050-150_Supplier_Selection | PM-050-150_Supplier_Selection | Commodity Manager | 2 | 0 |
| 17 | PM-050-160_Maintain_Supplier_Profile | PM-050-160_Maintain_Supplier_Profile | Commodity Manager | 2 | 2 |
| 18 | PM-050-170_Identify_Approved_Suppliers | PM-050-170_Identify_Approved_Suppliers | Commodity Manager | 5 | 3 |
| 19 | PM-050_Manage_Quotation | PM-050_Manage_Quotation |  | 3 | 8 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 PM-050-010_Identify_Need_for_RFQ — PM-050-010_Identify_Need_for_RFQ

**Swim Lanes**: Commodity Manager | **Tasks**: 6 | **Gateways**: 0

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
    subgraph Commodity Manager
        n1["fa:fa-user Capture General RFx Information in System"]
        n2["Identify Need for RFQ"]
        n3["Perform Market Evaluation"]
        n4["Determine Procurement Strategy"]
        n5["Take Business Decision Based on Market Evaluation"]
        n6["Take Business Decision to Process RFQ"]
        n7["Determine Material Specifications"]
        n8["Manage Quotation"]
    end
    n8 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
    n1 --> n7
    n6 --> n1
    class n1 userTask
    class n7 startEvt
    class n8 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVU1v4kgQ_SstRxEXI_kTsz6sBAavIk1GkyE7c9jsobGroYXdjbrbCZ6I_z7V2ECcKNrD-oD8nl-9V1Xg5tUpZAlO6tzevnLBTUpeR2YLNYxSMlpTDSOXdMQPqjhdV6BHVsOkMCv-6yTzo_3ByiyX05pXrWVXsJFA_r5zyQwLK5doKvRYg-Js5I72itdUtZmspLLqG5gyj53S-kdzqUpQV4HnJX4RY2nFBVzpMImSKLd1GgopyoEpi9mUFaOjba6SL8WWKnNqv9FwTw8_eWm2iBmtNKBma-rqC11DZWc0qrFc0ajn8zK4tjkCF7ba04KLDfKRh5SiYnelYu94JMfb2ydxCSWPiydB8CoqqvUCGNEG6eWzIYxXVXoTZbM89lxtlNxBehMsk0UYuIWdJMXRPdcud_wCfLM16VpWZS8dv9gZ0mB_cNUhDTxXtfj5LgtEeU3KJsE0mF6S5omf-dk5iTH2v5Jwr-qR6l2ftQzzIF9csvx4EmfeR7_zmIsomfnv9wTqmRfwxjTP83B5XdVyEvve56bzPJx42TvTDTXwQtur4R9ZdDHM4yT3k08Nu7z3XTbrb0oWZ8NwGefxxTCZ-_ks-NQwmvnRtO8QfTaK7rckk3UtS25ack8F3YDqnttL-P88OYymjI7tuklG96ZRQP4CAYpW5Ht-IHeCSVVTw6UgXJBVqw3UT86_b1wCdLkrQRjOWvIVoCRYgsUPQ1mIsm-grB22onZgyPKZVs3JeyiNULoAA6rGN5TYfWBbNSaQlVG48U071Meof6Q7IPNGY4XWZAEF17bnOZ48JcGb_4icfG5h5KkFy30YKhl0eo-92SOKrPZYzHhxCtLDkimWdF8FeWikGfaCL1h3I6ZkPP4Tl9vDoINhD8MORj2MOhj3MO7gpId-B5MeTjr49v2wmvMbN6CTy_EyoKcX2nGdGqenvHTSV-d0vuN_QAmMNpVxjq5DGyNXrSic9HQOOs2-xC0tOMWfZ92Rx98TEfsR" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.2 PM-050-020_Determine_Material_Specifications — PM-050-020_Determine_Material_Specifications

**Swim Lanes**: Commodity Manager | **Tasks**: 5 | **Gateways**: 3

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
    subgraph Commodity Manager
        n1["fa:fa-user Create Material Master"]
        n2[["fa:fa-cog Determine Material Specifications"]]
        n3[["fa:fa-cog Capture Material Specifications"]]
        n4[["fa:fa-cog Establish Material Profile"]]
        n5[["fa:fa-cog Execute Master Data Replication"]]
        n6(["fa:fa-play Material Master Creation Initiated"])
        n7["Manage Quotation"]
        n8{{"fa:fa-code-branch exclusiveGateway"}}
        n9{{"fa:fa-arrows-alt Material Master Existing?"}}
        n10{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n8
    n8 --> n1
    n1 --> n9
    n2 --> n3
    n3 --> n4
    n4 --> n10
    n5 --> n7
    n9 -->|"Yes"| n2
    n10 --> n5
    n9 -->|"No"| n8
    n9 --> n10
    class n1 userTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 startEvt
    class n7 startEvt
    class n8 gateway
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVe-P2jgQ_VesrFbcSUHKTxLy4So2kFOla3VX2judSj8YxwFrTRzZzgJH-d9vTAKB7CJVKh9Q5nneezOjeHKwiMiplViPjwdWMp2gw0Cv6YYOEjRYYkUHNmqAv7FkeMmpGpicQpR6zv47pblBtTNpBsvwhvG9Qed0JSj68t5GEyByGylcqqGikhUDe1BJtsFynwoupMl-oHHhFCe39uhJyJzKLsFxIpeEQOWspB3sR0EUZIanKBFlfiNahEVckMHRFMfFlqyx1Kfya0U_4N0_LNdriAvMFYWctd7wP_CSctOjlrXBSC1fzsNgyviUMLB5hQkrV4AHDkASl88dFDrHIzo-Pi7Kiyn6PF2UCH6EY6WmtEBKAzx70ahgnCcPQTrJQsdWWopnmjx4s2jqezYxnSTQumOb4Q63lK3WOlkKnrepw63pIfGqnS13iefYcg__PS9a5p1TOvJiL744PUVu6qZnp6IofsoJ5io_Y_Xces38zMumFy83HIWp81rv3OY0iCZuf05UvjBCr0SzLPNn3ahmo9B17os-Zf7ISXuiK6zpFu87wXEaXASzMMrc6K5g49evsl7-KQU5C_qzMAsvgtGTm028u4LBxA3itkLQWUlcrVEqNhuRM71HH3CJV1Q25-ZXul8XVoGTAg_NuFEqKbQDeZqaiwYPCp4W1rcrivf1wiFihaYUMjZwjzrWvKKEFYxgzUSpgH1N92_pKa50LX-UHNySZ_DmLzlT644Oo4PB0R4v7PF2lNSnPk17aIo1Rp9oxVvXHnn0y4VccbzvT6cZGtDQe1h6DA5zEPj1SiACfjN69Fct9NnjKiM-HLr6cjpcwhYga0R3hNeKvdDfm5dsYR2PV6xxx8JSiq0aYq5flTfbMaVhm7zrsV3nTXqFJeac8leWcPObh3KEhsPfoOg2jJuwvW2l24TjNvSa0G9DvwmDNgxabnsJyrCJozYcm_D7wvqXwpvwHcTOHk6TF_byPopTWnwNd-qnK2YKPK-WG9i73g83J_7dk-DuSXj3ZHTZ1zdw9DYcnxfMDTp-E4WptLBlWxu4lZjlVnKwTt9c-C7ntMA119bRtnCtxXxfEis5fZususqBOWUYVsamAY__A78UfHk=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 PM-050-030_Establish_Material_Profile — PM-050-030_Establish_Material_Profile

**Swim Lanes**: Commodity Manager | **Tasks**: 3 | **Gateways**: 1

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
    subgraph Commodity Manager
        n1[["fa:fa-cog Establish Material Profile"]]
        n2[["fa:fa-cog Execute Master Data Replication in MDG"]]
        n3[["fa:fa-cog Replicate Master Data in Ariba"]]
        n4(["fa:fa-stop Setting up Material Profile Data Completed"])
        n5["Manage Quotation"]
        n6["Determine Material Specifications"]
        n7{{"fa:fa-arrows-alt parallelGateway"}}
        n8[["fa:fa-folder-open Identify Potential Suppliers"]]
    end
    n6 --> n1
    n1 --> n7
    n7 --> n2
    n2 --> n3
    n7 --> n4
    n3 --> n8
    n8 --> n5
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 endEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVduO2zYQ_RVCi4UTQAZ0tVQ9BPDKVhAgC6R12j7EeaCloU0sTQoktbZr-N87suRr6qfqQdCcmXPmIg21d0pVgZM5z897LrnNyH5gV7CGQUYGC2pg4JIO-ItqThcCzKCNYUraGf_nGOZH9bYNa7GCrrnYtegMlgrIn19cMkaicImh0gwNaM4G7qDWfE31LldC6Tb6CVLmsWO23vWidAX6EuB5iV_GSBVcwgUOkyiJipZnoFSyuhFlMUtZOTi0xQm1KVdU22P5jYFXuv2bV3aFNqPCAMas7Fp8pQsQbY9WNy1WNvr9NAxu2jwSBzaracnlEvHIQ0hT-XaBYu9wIIfn57k8JyXfJ3NJ8CoFNWYCjBiL8PTdEsaFyJ6ifFzEnmusVm-QPQXTZBIGbtl2kmHrntsOd7gBvlzZbKFE1YcON20PWVBvXb3NAs_VO7zf5QJZXTLloyAN0nOml8TP_fyUiTH2vzLhXPV3at76XNOwCIrJOZcfj-Lc-1Xv1OYkSsb-_ZxAv_MSrkSLoginl1FNR7HvPRZ9KcKRl9-JLqmFDd1dBH_Lo7NgESeFnzwU7PLdV9ksvmlVngTDaVzEZ8HkxS_GwUPBaOxHaV8h6iw1rVckV-u1qrjdkVcq6RJ0528v6f_4MXcYzRgdlmpJpvgpLQQ3Kwy10O4awVqwEpg7P39e8YI73hbKxgKyDNLIhFpK_oBa8JJariThkrxOPt9phLcap_hbFWTizi_oHTf6cOYaq2oyA2txY0hT_1J5p4NDqAVYqFDo45VQjDrdWMjvjbLHcjHkKmKEERNk6jUeFhf1WQ0lZ32D5paS7Pen6qjWamOGVFhSU02FAPG5-2LmzuFwxUkv02C4KaCHqgZJvlQgLWc78k3Z9qnN3NQ4KdDmMhPcyu5Bjshw-Anfa2_6nZn0ZtKZQW8GnRneeqPeDDsz7c20M-Orz7XVv1qqG0_w0BM-9ET98XIDxufz7QYe_TecnBbyBk1PW-W4zhrfJOWVk-2d488If1gVMNoI6xxchzZWzXaydLLjoe00dYV6E05xl9YdePgXh8A1Zg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.4 PM-050-030_Establish_Material_Profile_(Copy) — PM-050-030_Establish_Material_Profile_(Copy)

**Swim Lanes**: Commodity Manager | **Tasks**: 3 | **Gateways**: 1

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
    subgraph Commodity Manager
        n1[["fa:fa-cog Establish Material Profile"]]
        n2[["fa:fa-cog Execute Master Data Replication in MDG"]]
        n3[["fa:fa-cog Replicate Master Data in Ariba"]]
        n4(["fa:fa-stop Setting up Material Profile Data Completed"])
        n5["Manage Quotation"]
        n6["Determine Material Specifications"]
        n7{{"fa:fa-arrows-alt parallelGateway"}}
        n8[["fa:fa-folder-open Identify Potential Suppliers"]]
    end
    n6 --> n1
    n1 --> n7
    n7 --> n2
    n2 --> n3
    n7 --> n4
    n3 --> n8
    n8 --> n5
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 endEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVduO2zYQ_RVCi4UTQAZ0tVQ9BPDKVhAgC6R12j7EeaCloU0sTQoktbZr-N87suRr6qfqQdCcmXPmIg21d0pVgZM5z897LrnNyH5gV7CGQUYGC2pg4JIO-ItqThcCzKCNYUraGf_nGOZH9bYNa7GCrrnYtegMlgrIn19cMkaicImh0gwNaM4G7qDWfE31LldC6Tb6CVLmsWO23vWidAX6EuB5iV_GSBVcwgUOkyiJipZnoFSyuhFlMUtZOTi0xQm1KVdU22P5jYFXuv2bV3aFNqPCAMas7Fp8pQsQbY9WNy1WNvr9NAxu2jwSBzaracnlEvHIQ0hT-XaBYu9wIIfn57k8JyXfJ3NJ8CoFNWYCjBiL8PTdEsaFyJ6ifFzEnmusVm-QPQXTZBIGbtl2kmHrntsOd7gBvlzZbKFE1YcON20PWVBvXb3NAs_VO7zf5QJZXTLloyAN0nOml8TP_fyUiTH2vzLhXPV3at76XNOwCIrJOZcfj-Lc-1Xv1OYkSsb-_ZxAv_MSrkSLoginl1FNR7HvPRZ9KcKRl9-JLqmFDd1dBH_Lo7NgESeFnzwU7PLdV9ksvmlVngTDaVzEZ8HkxS_GwUPBaOxHaV8h6iw1rVckV-u1qrjdkVcq6RJ0528v6f_4MXcYzRgdlmpJpvgpLQQ3Kwy10O4awVqwEpg7P39e8YI73hbKxgKyDNLIhFpK_oBa8JJariThkrxOPt9phLcap_hbFWTizi_oHTf6cOYaq2oyA2txY0hT_1J5p4NDqAVYqFDo45VQjDrdWMjvjbLHcjHkKmKEERNk6jUeFhf1WQ0lZ32D5paS7Pen6qjWamOGVFhSU02FAPG5-2LmzuFwxUkv02C4KaCHqgZJvlQgLWc78k3Z9qnN3NQ4KdDmMhPcyu5Bjshw-Anfa2_6nZn0ZtKZQW8GnRneeqPeDDsz7c20M-Orz7XVv1qqG0_w0BM-9ET98XIDxufz7QYe_TecnBbyBk1PW-W4zhrfJOWVk-2d488If1gVMNoI6xxchzZWzXaydLLjoe00dYV6E05xl9YdePgXh8A1Zg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.5 PM-050-040_Identify_Potential_Suppliers — PM-050-040_Identify_Potential_Suppliers

**Swim Lanes**: Commodity Manager | **Tasks**: 2 | **Gateways**: 0

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
    subgraph Commodity Manager
        n1["fa:fa-user Identify Potential Suppliers"]
        n2["fa:fa-user Generate Supplier list"]
        n3["Conduct Pre-bid Quotation Meeting"]
        n4["Manage Quotation"]
    end
    n4 --> n1
    n1 --> n2
    n2 --> n3
    class n1 userTask
    class n2 userTask
    class n3 startEvt
    class n4 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVE2P2jAU_CtWViiXIOWT0BwqQSBVpa60Fdv2UHowyTNY69iR7SxQxH-vTSAstHtqDlHeZN6M38TxwSlFBU7mDAYHyqnO0MHVG6jBzZC7wgpcD3XAdywpXjFQruUQwfWC_j7RgrjZWZrFClxTtrfoAtYC0LfPHpqYRuYhhbkaKpCUuJ7bSFpjuc8FE9KyH2BMfHJyO7-aClmBvBJ8Pw3KxLQyyuEKR2mcxoXtU1AKXt2IkoSMSeke7eKY2JYbLPVp-a2CR7z7QSu9MTXBTIHhbHTNvuAVMDujlq3Fyla-XsKgyvpwE9iiwSXla4PHvoEk5i9XKPGPR3QcDJa8N0XPsyVH5ioZVmoGBClt4PmrRoQylj3E-aRIfE9pKV4gewjn6SwKvdJOkpnRfc-GO9wCXW90thKsOlOHWztDFjY7T-6y0Pfk3tzvvIBXV6d8FI7Dce80TYM8yC9OhJD_cjK5ymesXs5e86gIi1nvFSSjJPf_1ruMOYvTSXCfE8hXWsIb0aIoovk1qvkoCfz3RadFNPLzO9E11rDF-6vghzzuBYskLYL0XcHO736V7epJivIiGM2TIukF02lQTMJ3BeNJEI_PKzQ6a4mbDcpFXYuK6j16xByvQXbv7cWDn0uH4IzgoY0bfa6Aa0r26Elo-4QZWrRNwyhItXR-vWkMbxs_AQdpkujpiFGlb1si05Kb36otNXqSMFzRCn1thcaaCo4eAbTZ87ctsWnpFn1l9gyzFbsHHqPh8KMZ5lwGXRmey7Arozc5W85lf93A4b_hqP_HbuC4hx3PqUHWmFZOdnBOh5w5CCsguGXaOXoObrVY7HnpZKfDwGmbysQ1o9h8o7oDj38ABD6wJw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 PM-050-050_Identify_Supplier_Rationalization_Opportunities — PM-050-050_Identify_Supplier_Rationalization_Opportunities

**Swim Lanes**: Commodity Manager | **Tasks**: 6 | **Gateways**: 2

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
    subgraph Commodity Manager
        n1["Identify Supplier Rationalization Opportunities"]
        n2["Analyze Spend Report"]
        n3["Identify Tail Spend"]
        n4["Review Product/Service for Consolidation/Substitution"]
        n5["Check any Contract Terms"]
        n6["Identify Preferred Suppliers from Top Supplier List"]
        n7(["fa:fa-stop Controls / Other Strategies to manage Tail Spend"])
        n8["Create Supplier RFQ"]
        n9["Manage Quotation"]
        n10["Negotiate Terms and Conditions With Supplier"]
        n11{{"fa:fa-code-branch exclusiveGateway"}}
        n12{{"fa:fa-code-branch Consolidate/Substitute?"}}
        n13[["fa:fa-folder-open Maintain Supplier Profile"]]
    end
    n9 --> n13
    n13 --> n1
    n1 --> n11
    n10 --> n11
    n11 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
    n6 --> n12
    n12 -->|"Yes"| n8
    n12 -->|"No"| n7
    class n7 endEvt
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
    class n13 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVduO4jgQ_RUrrRa7UlAnISF0HmZFA1mNNNemd0erYR5MUgarkziyHS7N8O9TTsJ1up8WCUSdHJ-qOrYrOysRKViRdXu74wXXEdl19BJy6ESkM6cKOjZpgH-p5HSegeoYDhOFnvKXmub65cbQDBbTnGdbg05hIYD8894mQ1yY2UTRQnUVSM46dqeUPKdyOxKZkIZ9AwPmsDpb--hByBTkieA4oZsEuDTjBZzgXuiHfmzWKUhEkV6IsoANWNLZm-IysU6WVOq6_ErBR7r5xlO9xJjRTAFyljrPPtA5ZKZHLSuDJZVcHczgyuQp0LBpSRNeLBD3HYQkLZ5PUODs92R_ezsrjknJ03hWEPwkGVVqDIwojfBkpQnjWRbd-KNhHDi20lI8Q3TjTcJxz7MT00mErTu2Mbe7Br5Y6mgusrSldtemh8grN7bcRJ5jyy3-XuWCIj1lGvW9gTc4ZnoI3ZE7OmRijP2vTOirfKLquc016cVePD7mcoN-MHJ-1zu0OfbDoXvtE8gVT-BMNI7j3uRk1aQfuM7bog9xr--MrkQXVMOabk-C9yP_KBgHYeyGbwo2-a6rrOZfpEgOgr1JEAdHwfDBjYfem4L-0PUHbYWos5C0XJKRyHORcr0lH2lBFyCb5-ZTuN9n1vsUCs3Zlkyrssw4SPJINRcFzfhL_Yd8LkshdYV3moOaWT_OBDwUGCJ1-wJkWuLpII9gyJes3nmaJ8qzhntJ8pH0CCsOa4IGpFWi76bNjhEmJLZRKJHxtC7pblrNlea6MsGlTIAyoyUkz4QWW7NKS5rgrQGZX9XeP6_qiwQGUkJ6tEERJkVOnkR5cuYDV1ethX-gCqMRo12lkVonFJkid-QzDjtJpphfwwKdI1qQvN6CSw_-PJMbmOol4Iqz7Yi_Xua8R1Kzl-RrJTT93QTXQconHJuaG6m6efQjNeXhUUC-It-4Xh6TXC13d7tDV2aod-c4lpIlgU2SVYqv4O_m1M-s_f58mff6stPWwWnj4K_r1b3vRysZDguQXYEO4anlhcbvyRA8Hng7AGtuizY-Fo01pNt9Z7Ta2O21wCFuw2PsXAMtw2tjrwkPeq2c34Z-EwZtGDRhvw37rfZBy63Ffs6s_8w1-om7ff3gk6jx8GwmYNRO3QtwcBz7F_D96zC2-TruHgbYJey9DvcO08myrRzPFOWpFe2s-qWOL_4UGK0ybe1ti1ZaTLdFYkX1y8-qSrP7Y05xJuUNuP8FRceYmg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 PM-050-060_Manage_Tendering_Process — PM-050-060_Manage_Tendering_Process

**Swim Lanes**: Procurement Agent | **Tasks**: 4 | **Gateways**: 4

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
        n1["fa:fa-user Edit RFQ"]
        n2["fa:fa-user Publish RFQ"]
        n3["fa:fa-user Follow up with Supplier on the Status of RFQ"]
        n4["fa:fa-user Solve Any Issues/Question on RFQ Event"]
        n5["Receive Supplier Quotations"]
        n6["Manage Quotation"]
        n7{{"fa:fa-code-branch Is Approval Required?"}}
        n8{{"fa:fa-code-branch RFQ Approved?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
        n10{{"fa:fa-code-branch exclusiveGateway"}}
        n11[["fa:fa-folder-open Create Supplier RFQ"]]
        n12[["fa:fa-folder-open Issue RFQ"]]
    end
    n11 --> n12
    n1 --> n7
    n7 -->|"Yes"| n8
    n8 -->|"No"| n9
    n2 --> n3
    n3 --> n4
    n9 --> n1
    n10 --> n2
    n7 -->|"No"| n10
    n6 --> n11
    n4 --> n5
    n12 --> n9
    n8 -->|"Yes"| n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
    class n9 gateway
    class n10 gateway
    class n11 subProc
    class n12 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVluP4jYU_itWRiNegjZXAnloxQBZrdStdoZtq2rZB5M4YI2xU9vhUpb_vsckAcJkXlqEIs7Hdzk-iQ1HKxUZsWLr8fFIOdUxOvb0mmxIL0a9JVakZ6MK-BNLipeMqJ7h5ILrOf33THODYm9oBkvwhrKDQedkJQj645ONxiBkNlKYq74ikuY9u1dIusHyMBFMSMN-IMPcyc9p9VdPQmZEXgmOE7lpCFJGObnCfhREQWJ0iqSCZy3TPMyHedo7meaY2KVrLPW5_VKRz3j_F830GuocM0WAs9Yb9hteEmbWqGVpsLSU22YYVJkcDgObFzilfAV44AAkMX-9QqFzOqHT4-OCX0LR1-mCI3ilDCs1JTlSGuDZVqOcMhY_BJNxEjq20lK8kvjBm0VT37NTs5IYlu7YZrj9HaGrtY6XgmU1tb8za4i9Ym_Lfew5tjzA9S6L8OyaNBl4Q294SXqK3Ik7aZLyPP9fSTBX-RWr1zpr5ideMr1kueEgnDhv_ZplToNo7N7PicgtTcmNaZIk_uw6qtkgdJ33TZ8Sf-BM7kxXWJMdPlwNR5PgYpiEUeJG7xpWefddlssvUqSNoT8Lk_BiGD25ydh71zAYu8Gw7hB8VhIXa2TcSgnbjms0XsG1-t68uPttYeU4znHfjBvNMqrRS_K8sL7fkLw26Uu5ZFSt3_L8Ni8RDJ5ZVBZoR_UazcuiYBRwwRGcAmiusS4VEvlbo6BtNBdsS9CYH9AnpUqiPjzDRVPwgTeI0WxrVtWyCMHihaSEgvKS_FwKCAWhapMHQP6MOV6RK6XNiI7HpiVzyPWXsE3TNfSDxkUhxRYz9EL-Kakk2a8L63S6kQ67pabvSvtWMuqWkH3KSgUr-lg9c3cq1_lvMvfbZdw57FEi-6IgHE0kAf51eNVduh2K63Urz3epzYdjo_oAcajf_8WIG6Cqo7qMTPljYf1N4Cb9gPHV-LDGfxdneFTDXqX269KvyqAuR3VWE-VUtXeXVXu69Vbkg1rW6IKqDhubOnR011rTsnu7pc0Cm6OsBXvdsN8NB91weDn8W_CgG46a06qFDjvRUScKE-yE3ebYasNeA1u2tSFyg2lmxUfr_CcA_ihkJMcl09bJtnCpxfzAUys-_1haZZFBzpRiOMM2FXj6CTPAofo=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 PM-050-070_Create_Supplier_RFQ — PM-050-070_Create_Supplier_RFQ

**Swim Lanes**: Commodity Manager | **Tasks**: 8 | **Gateways**: 0

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
    subgraph Commodity Manager
        n1["fa:fa-user Create Supplier RFQ"]
        n2["fa:fa-user Select RFQ Template and Content"]
        n3["fa:fa-user Complete Event Runtime Setup"]
        n4["fa:fa-user Finalize Bidding Strategy"]
        n5["fa:fa-user Add Supplier"]
        n6["fa:fa-user Prepare Line Items"]
        n7["fa:fa-user Add Supplier Specific Celling Price"]
        n8[["fa:fa-cog Publish RFQ"]]
        n9["Issue RFQ"]
        n10["Manage Quotation"]
    end
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
    n6 --> n7
    n7 --> n8
    n8 --> n9
    n10 --> n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 serviceTask
    class n9 startEvt
    class n10 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV1vozgU_SsWVZUXIvEZKA8rJSRIlWakzqS7-zDdBweuE6vGRrZpm63y39cOhIRM-rQ8RDmHc8_xvWDz6ZSiAidz7u8_Kac6Q58TvYMaJhmabLCCiYs64i8sKd4wUBOrIYLrNf33KPOj5sPKLFfgmrK9ZdewFYD-fHTR3BQyFynM1VSBpGTiThpJayz3uWBCWvUdpMQjx7T-1kLICuRZ4HmJX8amlFEOZzpMoiQqbJ2CUvBqZEpikpJycrCLY-K93GGpj8tvFXzHH3_TSu8MJpgpMJqdrtk3vAFme9SytVzZyrfTMKiyOdwMbN3gkvKt4SPPUBLz1zMVe4cDOtzfv_AhFD0vXzgyV8mwUksgSGlDr940IpSx7C7K50XsuUpL8QrZXbBKlmHglraTzLTuuXa403eg253ONoJVvXT6bnvIgubDlR9Z4Llyb36vsoBX56R8FqRBOiQtEj_381MSIeR_JZm5ymesXvusVVgExXLI8uNZnHu_-53aXEbJ3L-eE8g3WsKFaVEU4eo8qtUs9r2vTRdFOPPyK9Mt1vCO92fDhzwaDIs4KfzkS8Mu73qV7eZJivJkGK7iIh4Mk4VfzIMvDaO5H6X9Co3PVuJmh3JR16Kieo--Y463ILv79uL-rxeH4IzgqR03yiWYdtC6bRpGDf5Z_Hhx_rnQB2P9GhiU2srQM9QNs8WYVyaSa-B6XBteZQlTAKZg9Wak6GfLNa1NNui2GRdG48KCcszMeYEWtKrMNkFrLU3wdj-uisdV86oa-hoLZ2Phk4QGS0DfzNmAHjXUaixPvvZF6wZKSmiJcmDMLu1JmhduXJ_-GgxKYRTthlG160d9KXwwukelWvj9Mfieudc9TfSjFRprKvggMXu0-8N9NJ3-YZ5aD4MOhj0MOxj1MOpg3MO4g7MezjqY9DDpYNrDtIMPp1yvw5c70K7mtKdHdHCbDm_T0W06vk3PbtPJbTq9PCJGdx6GQ3bckTfwjuvUIGtMKyf7dI6fOfMprIDglmnn4Dq41WK956WTHT8HTttU5q1dUmx2ad2Rh_8AksxI4w==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.9 PM-050-080_Issue_RFQ — PM-050-080_Issue_RFQ

**Swim Lanes**: Commodity Manager | **Tasks**: 6 | **Gateways**: 2

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
    subgraph Commodity Manager
        n1["fa:fa-user Define Initial RQF Requirements"]
        n2["fa:fa-user Issue RFQ"]
        n3["fa:fa-user Release RFQ for Distribution"]
        n4["fa:fa-user Respond to Supplier Question"]
        n5["fa:fa-user Monitor and Track Responses"]
        n6["Receive RFQ Information in Ariba"]
        n7["Manage Tendering Process"]
        n8["Create Supplier RFQ"]
        n9{{"fa:fa-code-branch Modification in Material Requirement?"}}
        n10{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n8 --> n6
    n6 --> n10
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n9
    n5 --> n7
    n9 -->|"No"| n5
    n10 --> n1
    n9 -->|"Yes"| n10
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n7 startEvt
    class n8 startEvt
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVd9vwjYQ_lesVBUvQcpPAnnYRAOZKq3TCt2maezBJDZYTWxmOy2M8r_vTBLSUPq0PCDuy9333Z19l6OViZxYsXV_f2Sc6RgdB3pLSjKI0WCNFRnYqAZ-x5LhdUHUwPhQwfWS_Xt2c4Pd3rgZLMUlKw4GXZKNIOi3RxtNIbCwkcJcDRWRjA7swU6yEstDIgohjfcdGVOHntWaVw9C5kR2Do4TuVkIoQXjpIP9KIiC1MQpkgme90hpSMc0G5xMcoV4z7ZY6nP6lSJPeP8Hy_UWbIoLRcBnq8viZ7wmhalRy8pgWSXf2mYwZXQ4NGy5wxnjG8ADByCJ-WsHhc7phE739yt-EUUvsxVH8GQFVmpGKFIa4PmbRpQVRXwXJNM0dGylpXgl8Z03j2a-Z2emkhhKd2zT3OE7YZutjteiyBvX4bupIfZ2e1vuY8-x5QF-r7QIzzulZOSNvfFF6SFyEzdplSil_0sJ-ipfsHpttOZ-6qWzi5YbjsLE-crXljkLoql73Sci31hGPpGmaerPu1bNR6HrfE_6kPojJ7ki3WBN3vGhI5wkwYUwDaPUjb4lrPWus6zWv0qRtYT-PEzDC2H04KZT71vCYOoG4yZD4NlIvNuiRJSlyJk-oCfM8YbI-r15uPvXyqI4pnho2o1AHyYCPcL0wpyhxXOKFuSfikkYWq7Vyvr7U6zXj31UqiJokT73vfy-14IUBFaB8UNUgCKDWti60kzwfmBwHah2MJNIC7SsdruCAfZcEfU1MOwHPgmoBpQwBL9InL02VIpc1TOCuAXJCHur03vkkGCJjQBi3KyeNe5HRBBR9xS9wGDAPuIbZA6PqCvuMXgmksBd6bL_0qrJ8dhmbjbpcA27INtCATmjLLsk8gQs8nw83dH8uLJOp8_n6tzmIvusqBRU-FN9bbswyL_-w8doOPwB2tGYo9p0m3vK3dr2GtOrTb8x_doMGjOozUljhrUZNebEmB8r6xexsj7gbavgNJJXbn-aE_voUjmPjEmoXRU92LsN-7fh4DYc3oajy87twePb8KRdEv20nRa2bKskcNNYbsVH6_yFhK9oTiiuCm2dbAtXWiwPPLPi85fEqnY5RM4YhgEva_D0H48CXzE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.10 PM-050-090_Conduct_Pre-bid_Quotation_Meeting — PM-050-090_Conduct_Pre-bid_Quotation_Meeting

**Swim Lanes**: Commodity Manager · Sourcing Manager | **Tasks**: 6 | **Gateways**: 0

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
    subgraph Commodity Manager
        n6["Identify Material Requirements"]
        n8["Identify Potential Suppliers"]
    end
    subgraph Sourcing Manager
        n1["fa:fa-user Announce Tender"]
        n2["fa:fa-user Identify Participants List"]
        n3["fa:fa-user Prepare Pre-Bid Meeting Checklist"]
        n4["fa:fa-user Send Out Pre-bid Invitations"]
        n5["fa:fa-user Conduct Supplier Summit/Pre-bid Meeting"]
        n7["Identify Approved Suppliers"]
    end
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n7
    n8 --> n6
    n6 --> n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n7 startEvt
    class n8 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVU2P2jAU_CtWVohLUPNJaA6VIBBppa66Ktv2UHowyTNYJHbqOLAU8d9rkxAIy_ZSDpCZzJs3ftjJwUh4CkZo9HoHyqgM0aEv15BDP0T9JS6hb6Ka-I4FxcsMyr7WEM7knP45yWyveNUyzcU4p9les3NYcUDfHk00VoWZiUrMykEJgpK-2S8EzbHYRzzjQqsfYEQscurW3JpwkYK4CCwrsBNflWaUwYV2Ay_wYl1XQsJZ2jElPhmRpH_U4TK-S9ZYyFP8qoQn_PqDpnKtMMFZCUqzlnn2GS8h02uUotJcUonteRi01H2YGti8wAllK8V7lqIEZpsL5VvHIzr2egvWNkUv0wVD6pNkuCynQFApFT3bSkRoloUPXjSOfcsspeAbCB-cWTB1HTPRKwnV0i1TD3ewA7pay3DJs7SRDnZ6DaFTvJriNXQsU-zV900vYOmlUzR0Rs6o7TQJ7MiOzp0IIf_VSc1VvOBy0_SaubETT9tetj_0I-ut33mZUy8Y27dzArGlCVyZxnHszi6jmg1923rfdBK7Qyu6MV1hCTu8vxh-jLzWMPaD2A7eNaz73aasls-CJ2dDd-bHfmsYTOx47Lxr6I1tb9QkVD4rgYs1inie85TKPXrCDK9A1Pf1hw1_LozHFJikRN-WoM8X-gq_KyrUQWWyXBi_rvSja_0zl_pKFcyrosgoiIta7ZObGHNeCb2r76SwlSvBIcED_aejMWO8YgmgF-WihJ0ETld7CaPOAE1ogVVm9JmWslvmdsueBRRYgP4dTGiKngCkzhatIdlkb6q9bvVc5UJfKnkqX6ryR7alEkvK2c28_G5hpJ4qVSLbeamLPKfyw9mnidH1CK5nPi4KwbeQ_mvkzEaDwSc1qgY6NXQb6NbQa6BXQ7-Bfg2DBo5qOGzgsIbXJ0u3O5_VDu3cp937tHef9u_TQfvQ69CjljZMIweRY5oa4cE4vXXUmykFgqtMGkfTwJXk8z1LjPD0dDaqIlXbf0qx2q15TR7_AmCcLc4=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.11 PM-050-100_Receive_Supplier_Quotations — PM-050-100_Receive_Supplier_Quotations

**Swim Lanes**: Commodity Manager | **Tasks**: 4 | **Gateways**: 0

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
    subgraph Commodity Manager
        n1["fa:fa-user Perform Preliminary Review of Quotation"]
        n2["fa:fa-user Communicate to Supplier"]
        n3["fa:fa-user Respond to Supplier Query"]
        n4[["fa:fa-cog Receive Supplier Quotations"]]
        n5["Process Supplier Quotations"]
        n6["Manage Tendering Process"]
    end
    n6 --> n4
    n4 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 startEvt
    class n6 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVMuO2jAU_RUrI8QmSHkSmkUlCESq1JGmZdouhi5Mcg3WJHZkOzyK-PfaJIRHh1WziLjH53F9cXywMp6DFVu93oEyqmJ06Ks1lNCPUX-JJfRt1AA_saB4WYDsGw7hTM3pnxPNDaqdoRksxSUt9gadw4oD-vHFRmMtLGwkMZMDCYKSvt2vBC2x2Ce84MKwn2BEHHJKa5cmXOQgLgTHidws1NKCMrjAfhREQWp0EjLO8htTEpIRyfpH01zBt9kaC3Vqv5bwjHe_aK7Wuia4kKA5a1UWX_ESCrNHJWqDZbXYnIdBpclhemDzCmeUrTQeOBoSmL1foNA5HtGx11uwLhS9ThcM6ScrsJRTIEgqDc82ChFaFPFTkIzT0LGlEvwd4idvFk19z87MTmK9dcc2wx1sga7WKl7yIm-pg63ZQ-xVO1vsYs-xxV6_77KA5ZekZOiNvFGXNIncxE3OSYSQ_0rScxWvWL63WTM_9dJpl-WGwzBx_vU7b3MaRGP3fk4gNjSDK9M0Tf3ZZVSzYeg6j00nqT90kjvTFVawxfuL4ack6AzTMErd6KFhk3ffZb18ETw7G_qzMA07w2jipmPvoWEwdoNR26H2WQlcrVHCy5LnVO3RM2Z4BaJZNw9z3xYWwTHBAzNu9AKCcFGiFwEFLSnTXwD6DhsKW8QJ-lZzhRXlbGH9vvLwbj1MXM1opueCFEfzuqoKqkNvNP6t5jvISn9w13ydBmJ_qwreOlnGV1qVAd3AtaRtUGrdtTDUOjNUkPIB-4o81ORmUuhVH3d9y7AVatUdUy80P9gQDQafdW9tGTRle_aY25ReW3pN6bel35Th1REwkvPRv4G9j2H_Yzi4Pu03K2F3X9zAww62bKsEUWKaW_HBOl3Y-lLPgeC6UNbRtnCt-HzPMis-XWxWXeX6z55SrM9b2YDHv1eS8To=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.12 PM-050-110_Process_Supplier_Quotations — PM-050-110_Process_Supplier_Quotations

**Swim Lanes**: Commodity Manager | **Tasks**: 5 | **Gateways**: 0

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
    subgraph Commodity Manager
        n1["fa:fa-user Process Supplier Quotations"]
        n2["fa:fa-user Analyze Supplier Quotations"]
        n3["fa:fa-user Validate Changes in Quotation"]
        n4["fa:fa-user Finalize The Quote"]
        n5["fa:fa-user Resolve any Changes in Quotation"]
        n6["Perform Price Simulation"]
        n7["Receive Supplier Quotations"]
    end
    n7 --> n1
    n1 --> n2
    n2 --> n3
    n4 --> n6
    n5 --> n4
    n3 --> n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 startEvt
    class n7 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV1vmzAU_SsWVcULkfgMGQ-TUhKkSavULV33sOzBgevEqrEj26RNo_z32YEkpUu3SeMBcQ73nON7ZczOKUUFTuZcX-8opzpDO1evoAY3Q-4CK3A91BIPWFK8YKBcW0ME1zP6cigL4vWzLbNcgWvKtpadwVIA-vbJQ2MjZB5SmKuBAkmJ67lrSWsst7lgQtrqKxgRnxzSulc3QlYgzwW-nwZlYqSMcjjTURqncWF1CkrBq54pSciIlO7eLo6Jp3KFpT4sv1Fwi5-_00qvDCaYKTA1K12zz3gBzPaoZWO5spGb4zCosjncDGy2xiXlS8PHvqEk5o9nKvH3e7S_vp7zUyi6n8w5MlfJsFITIEhpQ083GhHKWHYV5-Mi8T2lpXiE7CqcppMo9ErbSWZa9z073MET0OVKZwvBqq508GR7yML1syefs9D35Nbc32QBr85J-TAchaNT0k0a5EF-TCKE_FeSmau8x-qxy5pGRVhMTllBMkxy_3e_Y5uTOB0Hb-cEckNLeGVaFEU0PY9qOkwC_33TmyIa-vkb0yXW8IS3Z8MPeXwyLJK0CNJ3Ddu8t6tsFndSlEfDaJoUyckwvQmKcfiuYTwO4lG3QuOzlHi9Qrmoa1FRvUW3mOMlyPa9vXjwY-4QnBE8sONGNhiUQrNmvWbUEF8aobGmgqu58_OVLuzrxhyz7Qv8XRf1dQ-Y0coMEOUrzJegEOVnaV8Z95UFNZHm0ED3KzhIoF-e9Mu_ghJsAwjz7T9kDY34DiQRsjYjMVsGzWjdsAuVqan8CiXQzZ-bN59N-8BTNBh8NIPvYNDCsINhC6MOxi0cdjBpYdzBqIXJqw1kDY8fTo8OL9PRZTq-TCeX6eHpBOrR6Yl2PKcGWWNaOdnOOfwCzG-iAoIbpp295-BGi9mWl052OCqdZm13xYRis4Prltz_Apn4Cbw=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.13 PM-050-120_Perform_Price_Simulation — PM-050-120_Perform_Price_Simulation

**Swim Lanes**: Commodity Manager | **Tasks**: 8 | **Gateways**: 0

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
    subgraph Commodity Manager
        n1["fa:fa-user Define Scenarios"]
        n2["fa:fa-user Retrieve Supplier Bids"]
        n3["fa:fa-user Analyze Supplier Bids"]
        n4["fa:fa-user Perform Price Simulation"]
        n5["fa:fa-user Score Supplier Based on Weightage"]
        n6["fa:fa-user Finalize Evaluation of Quotes"]
        n7["fa:fa-user Make Decision on Awarding"]
        n8["fa:fa-user Initiate Processing of Supplier Quotations"]
        n9["Supplier Selection"]
        n10["Perform Total Cost Model Analysis"]
    end
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
    n6 --> n7
    n7 --> n9
    n8 --> n1
    n10 --> n8
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 startEvt
    class n10 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVctu4zgQ_BVCQeCLDOhpKTos4JeAATZAZpzdHDZ7oCXSJkKRBknZ8QT-92lKshx5nL2sDoar1NXVbJKtD6eQJXEy5_7-gwlmMvQxMltSkVGGRmusychFLfE3VgyvOdEjG0OlMCv2swnzo927DbNcjivGj5ZdkY0k6K9vLpqCkLtIY6HHmihGR-5op1iF1XEuuVQ2-o6k1KONW_dqJlVJ1CXA8xK_iEHKmSAXOkyiJMqtTpNCinKQlMY0pcXoZIvj8lBssTJN-bUmj_j9hZVmC5hirgnEbE3F_8Rrwu0ajaotV9Rqf24G09ZHQMNWO1wwsQE-8oBSWLxdqNg7ndDp_v5V9KboefEqEDwFx1ovCEXaAL3cG0QZ59ldNJ_msedqo-Qbye6CZbIIA7ewK8lg6Z5rmzs-ELbZmmwtedmFjg92DVmwe3fVexZ4rjrC75UXEeXFaT4J0iDtnWaJP_fnZydK6f9ygr6qZ6zfOq9lmAf5ovfy40k8937Pd17mIkqm_nWfiNqzgnxKmud5uLy0ajmJfe_rpLM8nHjzq6QbbMgBHy8JH-ZRnzCPk9xPvkzY-l1XWa-flCzOCcNlnMd9wmTm59Pgy4TR1I_SrkLIs1F4t0VzWVWyZOaIHrHAG6La9_YR_j-vDsUZxWPbbgT-cCPQqiACrqjUr86_n4KDYfAPYhQjewivdzvOgJmx8koSDiVTgfnx538qoqHiiSgqVYWeFOwcWrGq5tgwKYaieChaFVJ9NoHZUyIp0EtzEqEFQ_VkqM4ZVAnzCC33mNeNG5IUfa-lIVfFJkPlI34j0MOC6UYj0PSAVQk3eahKh6pvMCsZnCJkt51oDfHWry_fGjdVXJk_QJo-aEU4KX5vjO9B0LmHz5CHw3HQBj3C4OHtdsAo6jVwu9s_wkfj8R-w5R0MWhh2MGxh1MGohXEH4xZOOjhpYdLBpIUPHUxb6J99vRann26FreY8DQZ0cJsOb9PRbTq-TU9u08ltOr1NP_Szebgcr-cd16mIqjArnezDab6O8AUtCcU1N87JdXBt5OooCidrviJOvSvhrCwYhstdteTpF0PxX-k=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.14 PM-050-130_Perform_Total_Cost_Model_Analysis — PM-050-130_Perform_Total_Cost_Model_Analysis

**Swim Lanes**: Procurement Agent | **Tasks**: 4 | **Gateways**: 0

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
        n1["fa:fa-user Evaluate Supplier Bid Based on all the Cost Attributes"]
        n2["fa:fa-user Add Weightage to Performance Metrics in Supplier's Quotation"]
        n3["fa:fa-user Analyse Supplier Performance Based on Weightage"]
        n4["fa:fa-user Score Supplier Based on Total Cost"]
        n5["Perform Price Simulation"]
        n6["Manage Quotation"]
        n7[["fa:fa-folder-open Receive Supplier Quotations"]]
        n8[["fa:fa-folder-open Process Supplier Quotations"]]
    end
    n6 --> n7
    n7 --> n8
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n8 --> n1
    n4 --> n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 startEvt
    class n6 startEvt
    class n7 subProc
    class n8 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVU2PozgQ_SsWrRYXIvEZWA4rJSRIK01LM5PencP0HhwoJ1Y7NrJNujOt_Pe1AyEhm97LckB5j6r3qiou-HAqUYOTO4-PH5RTnaMPV29hB26O3DVW4HqoI_7CkuI1A-XaGCK4XtFfp7Agbt5tmOVKvKPsYNkVbASgP__w0MwkMg8pzNVEgaTE9dxG0h2Wh0IwIW30A2TEJye3_tFcyBrkJcD306BKTCqjHC50lMZpXNo8BZXg9UiUJCQjlXu0xTHxVm2x1KfyWwVP-P0HrfXWYIKZAhOz1Tv2Ba-B2R61bC1XtXJ_HgZV1oebga0aXFG-MXzsG0pi_nqhEv94RMfHxxc-mKLnxQtH5qoYVmoBBClt6OVeI0IZyx_iYlYmvqe0FK-QP4TLdBGFXmU7yU3rvmeHO3kDutnqfC1Y3YdO3mwPedi8e_I9D31PHsz9xgt4fXEqpmEWZoPTPA2KoDg7EUL-l5OZq3zG6rX3WkZlWC4GryCZJoX_b71zm4s4nQW3cwK5pxVciZZlGS0vo1pOk8D_XHReRlO_uBHdYA1v-HAR_K2IB8EyScsg_VSw87utsl1_laI6C0bLpEwGwXQelLPwU8F4FsRZX6HR2UjcbJFVa6VZO67RbGPu3XN78eDni0NwTvDEjhst95i1piG0apuGUcPMaY3mZndrJDjCjCGzwKgQykhpLem61aBenL-vJMOx5Kyu0Y_TCcAbQFqgryCJkDvMK0BPYDQqhSgfHF2FvrVCY00FHwtHN8Ics4O6KvVaeCh5sB5rxWOtVSXkddPn7GdTCDu1O05PTHpvZ8ZrzhRa0V3L7hQ9NZFPmNveP2kr_TnUQsyKgJyIBjj6DhXQ_VVRQ7qd97VAdl_A_u2g1H8LmHXufvApmkx-N9X0MO1g1sOgg2EPww5GPYw6GPcw62C_fjzuYHJ1zq3geb9HdHifju7T8X06Gd6II3p6n07PGzdiszPreM4OzKmitZN_OKfPl_nE1UBwy7Rz9BzcarE68MrJT695p21qs0ELis327Try-A8jeUgy" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.15 PM-050-140_Supplier_Onboarding — PM-050-140_Supplier_Onboarding

**Swim Lanes**: Supplier Administrator | **Tasks**: 4 | **Gateways**: 0

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
    subgraph Supplier Administrator
        n1["fa:fa-user Add Supplier to RFQ"]
        n2["fa:fa-user Ensure Supplier RFQ Contact Set Up"]
        n3["fa:fa-user Onboard Supplier"]
        n4[["fa:fa-cog Receive Supplier Data"]]
        n5["Create Supplier RFQ"]
        n6["Manage Quotation"]
    end
    n6 --> n3
    n4 --> n2
    n1 --> n5
    n3 --> n4
    n2 --> n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 startEvt
    class n6 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVMuOmzAU_RWLUcSGSDxDyqJSQoJUqaO2k5l2MeniBuzEGmIjY_JolH-vHQiEdGZVFoh7OI_ri_HJSHmGjcgYDE6UURmhkyk3eIvNCJkrKLFpoRr4CYLCKselqTmEM7mgfy40xy8OmqaxBLY0P2p0gdcco5cvFpooYW6hElg5LLGgxLTMQtAtiGPMcy40-wGPiU0uac2rKRcZFh3BtkMnDZQ0pwx3sBf6oZ9oXYlTzrKeKQnImKTmWTeX8326ASEv7VclfoTDL5rJjaoJ5CVWnI3c5l9hhXO9RikqjaWV2F2HQUudw9TAFgWklK0V7tsKEsDeOiiwz2d0HgyWrA1Fz7MlQ-pKcyjLGSaolAqe7yQiNM-jBz-eJIFtlVLwNxw9uPNw5rlWqlcSqaXblh7ucI_peiOjFc-zhjrc6zVEbnGwxCFybUsc1f0uC7OsS4pH7tgdt0nT0Imd-JpECPmvJDVX8QzlW5M19xI3mbVZTjAKYvtfv-syZ344ce7nhMWOpvjGNEkSb96Naj4KHPtj02nijez4znQNEu_h2Bl-iv3WMAnCxAk_NKzz7rusVt8FT6-G3jxIgtYwnDrJxP3Q0J84_rjpUPmsBRQbtKiKIqdYoEm2Vf-l0oLkoibpizmvS4NARGCoZ65oWaeRHD0lP5bG7xu-2-fPWVkJ3EkUH8Xqw0Mq0QJL9FL05V5f_o2tOIgusk_2X1t2ytfoCaeY7m7CZiBBKW4lgVLEAqvv0uup7ztSpEdgsMboR8UlSMpZy1CbvH5gIzQcflYtN6Vfl25TOnUZNKVXl35TunV5uwu15Lqve7D7Puy9D_u3W7n3JmgPgx48amHDMrZYbIFmRnQyLqexOrEzTKDKpXG2DKgkXxxZakSXU8uoikxNckZBbaZtDZ7_AmP94XY=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.16 PM-050-150_Supplier_Selection — PM-050-150_Supplier_Selection

**Swim Lanes**: Commodity Manager | **Tasks**: 2 | **Gateways**: 0

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
    subgraph Commodity Manager
        n1["Execute Supplier Selection"]
        n2["Communicate Selection Decision to Supplier"]
        n3["Maintain Supplier Profile"]
        n4["Manage Quotation"]
    end
    n4 --> n1
    n1 --> n2
    n2 --> n3
    class n3 startEvt
    class n4 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVMuK2zAU_RXhIXjjgJ9x6kUh8QMKHWhJH4umC0W-TsTIkpHkSdKQf6-UhzNJmVUNNr7H555z78H2wSGiBidzRqMD5VRn6ODqDbTgZshdYQWuh87ADywpXjFQruU0gusF_XOiBXG3szSLVbilbG_RBawFoO-fPDQzjcxDCnM1ViBp43puJ2mL5T4XTEjLfoJp4zcnt8ujuZA1yBvB99OAJKaVUQ43OErjNK5snwIieH0n2iTNtCHu0Q7HxJZssNSn8XsFz3j3k9Z6Y-oGMwWGs9Et-4xXwOyOWvYWI718vYZBlfXhJrBFhwnla4PHvoEk5i83KPGPR3QcjZZ8MEXfiiVH5iAMK1VAg5Q2cPmqUUMZy57ifFYlvqe0FC-QPYVlWkShR-wmmVnd92y44y3Q9UZnK8HqC3W8tTtkYbfz5C4LfU_uzfXBC3h9c8on4TScDk7zNMiD_OrUNM1_OZlc5TesXi5eZVSFVTF4Bckkyf1_9a5rFnE6Cx5zAvlKCbwRraoqKm9RlZMk8N8XnVfRxM8fRNdYwxbvb4If8ngQrJK0CtJ3Bc9-j1P2qy9SkKtgVCZVMgim86Cahe8KxrMgnl4mNDpribsNykXbiprqPXrGHK9Bnp_bgwe_lk65A9JrQIu-6xgFiRbAgGgq-NL5_YYbGq7V6jkl2PKvNFQAocreaDGo3PdGpvcZU67NeTMye5ot4Z4an6h2UPS1FxrfDWJev_MNj9F4_NEscCmDcxleyvBcRm-yNdXwpdzB8QA7ntOCbDGtnezgnH5V5ndWQ4N7pp2j5-Bei8WeEyc7fdJO39UmiYJik3R7Bo9_AZ_XnVE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.17 PM-050-160_Maintain_Supplier_Profile — PM-050-160_Maintain_Supplier_Profile

**Swim Lanes**: Commodity Manager | **Tasks**: 2 | **Gateways**: 2

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
    subgraph Commodity Manager
        n1["fa:fa-user Update Key Supplier Data"]
        n2["Maintain Supplier Profile"]
        n3["Maintain Source List"]
        n4["Identify Supplier Rationalization Opportunities"]
        n5["Supplier Selection"]
        n6["Maintain Supplier Master Data"]
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n5 --> n7
    n6 --> n7
    n7 --> n2
    n2 --> n1
    n1 --> n8
    n8 --> n3
    n8 --> n4
    class n1 userTask
    class n3 startEvt
    class n4 startEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P2joQ_StWVitegpRPkpuHK7GBVNXt6lalvX0ofRiSCVhr7Mh2Fijiv9cmfGXLPt1IQZmTM-fMDLazd0pRoZM5j497yqnOyH6gV7jGQUYGC1A4cEkH_AeSwoKhGlhOLbie0V9Hmh81W0uzWAFrynYWneFSIPn20SVjk8hcooCroUJJ64E7aCRdg9zlgglp2Q-Y1l59dDu9ehKyQnkleF7il7FJZZTjFQ6TKIkKm6ewFLzqidZxndbl4GCLY2JTrkDqY_mtwmfYfqeVXpm4BqbQcFZ6zT7BApntUcvWYmUrX8_DoMr6cDOwWQMl5UuDR56BJPCXKxR7hwM5PD7O-cWUfJ3MOTFXyUCpCdZEaQNPXzWpKWPZQ5SPi9hzlZbiBbOHYJpMwsAtbSeZad1z7XCHG6TLlc4WglUn6nBje8iCZuvKbRZ4rtyZ3zdeyKurUz4K0iC9OD0lfu7nZ6e6rv-Xk5mr_Arq5eQ1DYugmFy8_HgU596feuc2J1Ey9t_OCeUrLfFGtCiKcHod1XQU-977ok9FOPLyN6JL0LiB3VXwrzy6CBZxUvjJu4Kd39sq28VnKcqzYDiNi_gimDz5xTh4VzAa-1F6qtDoLCU0K5KL9VpUVO_IM3BYouze24v7P-ZODVkNQztu8q2pTDvkH9yRWds0jBpsAhrmzs-bpMAkPQPl2txXninalIx9atijilaWSD5RpfusyLA-Vsg1rW-Mv4CmggOjv44P5N-mEVK35mShqPoCsRG45M2QYWkz-pzR3aqfQem7TSb7_Xk09lgbLszGLFcEtyVrFX3FD93_PncOh5us9JoFUoqNGgLTpAEJjCH7I8fspu6Bx2Q4_Nu4nsJRP0y6MDiFQRee1jf3uzA9hWkXhv0wullmNuW8vXpweDlLenB0H47vw6P7cHLeKj00PaOO66xRroFWTrZ3jp8J8ympsIaWaefgOtBqMdvx0smOx6nTHtfqhIJZ5esOPPwGIDIU5A==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.18 PM-050-170_Identify_Approved_Suppliers — PM-050-170_Identify_Approved_Suppliers

**Swim Lanes**: Commodity Manager | **Tasks**: 5 | **Gateways**: 3

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
    subgraph Commodity Manager
        n1["Define Approval Criteria"]
        n2["Assess Supplier Based on Criteria"]
        n3["Identify Approved Supplier"]
        n4["Document Approved Supplier Data"]
        n5["Provide Feedback to Supplier"]
        n6(["fa:fa-stop Remove Supplier from RFx Process"])
        n7["Supplier Onboarding"]
        n8["Conduct Pre-bid Quotation Meeting"]
        n9{{"fa:fa-code-branch Is Criteria Met by Supplier?"}}
        n10{{"fa:fa-code-branch Supplier Meets Criteria after Feedback?"}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n4
    n4 --> n7
    n9 -->|"Yes"| n3
    n9 -->|"No"| n5
    n10 -->|"No"| n6
    n10 -->|"Yes"| n11
    n8 --> n1
    n1 --> n11
    n11 --> n2
    n2 --> n9
    n5 --> n10
    class n6 endEvt
    class n7 startEvt
    class n8 startEvt
    class n9 gateway
    class n10 gateway
    class n11 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2PokgU_SsVOh13E0wAQZSH3SjKppPt2d1xPrIZ96GAKq00VJGqwtZ1_O9zSwE_un0aHtR7OPecey_eYm9lIidWZD0-7hlnOkL7nl6TkvQi1EuxIj0bnYAvWDKcFkT1DIcKrhfs_yPN9autoRkswSUrdgZdkJUg6POTjSaQWNhIYa76ikhGe3avkqzEcheLQkjDfiAj6tCjW3NrKmRO5JngOKGbBZBaME7O8CD0Qz8xeYpkgudXojSgI5r1Dqa4Qrxmayz1sfxakWe8_cpyvYaY4kIR4Kx1WfyJU1KYHrWsDZbVctMOgynjw2FgiwpnjK8A9x2AJOYvZyhwDgd0eHxc8s4UfZotOYIrK7BSM0KR0gDPNxpRVhTRgx9PksCxlZbihUQP3jycDTw7M51E0Lpjm-H2XwlbrXWUiiJvqP1X00PkVVtbbiPPseUOPm-8CM_PTvHQG3mjzmkaurEbt06U0p9ygrnKT1i9NF7zQeIls87LDYZB7LzVa9uc-eHEvZ0TkRuWkQvRJEkG8_Oo5sPAde6LTpPB0IlvRFdYk1e8OwuOY78TTIIwccO7gie_2yrr9G8pslZwMA-SoBMMp24y8e4K-hPXHzUVgs5K4mqNYlGWImd6h54xxysiT_fNxd1vSwtMYQ3QpKqk2OACxZJpWC28tP67YHrAnChFlEKLuqoKRiSawlLnSPA7KQNIecoJ14zuGnmgt9nXXN8UIrK6BPpbLpphfSMeQALMacNyghJC8hRnL0iLO_LDX4BOcURxX2lRoY-kBIOzPpWiRB-TLTKjhx4h-9eL9BCyO-5fPBVY5rCg1x4jIMVwbNSZBhnST1mO_qmFxprBiJ4J0W9Sxvt9W5Y5O_spbH-2Rk-qmyjkaZTuukp_X1qHw-UDdN6X6Ko1vhdymMJ3N7A3au77amSbFbViG_LH6d9-ToPz4PSDD1C__xs8yCb0T2HYhGMTfl9a_xKY7Xdg3-AfxBEOGth1rvHhLd7quM2S89HJrw3dJuziBvCa2DuF4yYMGvrlMoJrc9xdgWF33l7Bo_fhcXtAXKHQxruw28KWbZVElpjlVrS3ji9NeLHmhOK60NbBtnCtxWLHMys6vlysusohc8Yw7Hx5Ag8_AMLMZFM=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.19 PM-050_Manage_Quotation — PM-050_Manage_Quotation

**Swim Lanes**:  | **Tasks**: 3 | **Gateways**: 8

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
    n1["Conduct Pre-Bid Quote Meeting"]
    n2["Identify Approved Supplier"]
    n3["Identify Preferred and Secondary Suppliers"]
    n4(["fa:fa-play Supplier Data Created (Graphite)"])
    n5(["fa:fa-play Material Master Creation"])
    n6(["fa:fa-stop Remove Supplier From RFx Process"])
    n7(["fa:fa-stop Material Master Created"])
    n8["Create and Maintain Purchase Requisitions"]
    n9["Maintain Supplier Certification and Monitor Performance"]
    n10{{"fa:fa-code-branch Do Supplier Meet Intel Requirements?"}}
    n11{{"fa:fa-code-branch exclusiveGateway"}}
    n12{{"fa:fa-code-branch exclusiveGateway"}}
    n13{{"fa:fa-code-branch exclusiveGateway"}}
    n14{{"fa:fa-code-branch exclusiveGateway"}}
    n15{{"fa:fa-code-branch exclusiveGateway"}}
    n16{{"fa:fa-code-branch Material Master Required?"}}
    n17{{"fa:fa-code-branch exclusiveGateway"}}
    n18[["fa:fa-folder-open Identify Potential New Suppliers"]]
    n19[["fa:fa-folder-open Determine Material Specifications"]]
    n20[["fa:fa-folder-open Establish Material Profile"]]
    n21[["fa:fa-folder-open Identify Potential Suppliers"]]
    n22[["fa:fa-folder-open Supplier Onboarding"]]
    n23[["fa:fa-folder-open Create Supplier RFQ"]]
    n24[["fa:fa-folder-open Issue RFQ"]]
    n25[["fa:fa-folder-open Manage Tendering Process"]]
    n26[["fa:fa-folder-open Receive Supplier Quotations"]]
    n27[["fa:fa-folder-open Assess Suppliers"]]
    n28[["fa:fa-folder-open Supplier Selection"]]
    n29[["fa:fa-folder-open Maintain Supplier Profile"]]
    n30[["fa:fa-folder-open Maintain Source List"]]
    n31[["fa:fa-folder-open Identify Supplier Rationalization Opportunities"]]
    n32[["fa:fa-folder-open Manage Contracts"]]
    n9 --> n18
    n18 --> n17
    n19 --> n20
    n20 --> n21
    n21 --> n1
    n1 --> n10
    n10 -->|"Yes"| n2
    n10 --> n6
    n2 --> n11
    n4 --> n12
    n12 --> n11
    n12 --> n3
    n11 --> n22
    n22 --> n13
    n13 --> n23
    n23 --> n24
    n24 --> n25
    n25 --> n26
    n26 --> n27
    n27 --> n28
    n28 --> n14
    n14 --> n29
    n29 --> n15
    n15 --> n30
    n15 --> n31
    n31 --> n13
    n30 --> n32
    n32 --> n8
    n3 --> n14
    n5 --> n16
    n17 --> n19
    n16 -->|"Yes"| n17
    n16 -->|"No"| n7
    class n4 startEvt
    class n5 startEvt
    class n6 endEvt
    class n7 endEvt
    class n8 startEvt
    class n9 startEvt
    class n10 gateway
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 subProc
    class n19 subProc
    class n20 subProc
    class n21 subProc
    class n22 subProc
    class n23 subProc
    class n24 subProc
    class n25 subProc
    class n26 subProc
    class n27 subProc
    class n28 subProc
    class n29 subProc
    class n30 subProc
    class n31 subProc
    class n32 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV22P2kYQ_isrRycSCSS_YuBDKw5wFCmXXI60VZXrh8UewyrGdnfX95IL_71jWK-Ns9f01JM4mcfzPPOyM2PzZMVFAtbMurh4YjmTM_I0kDvYw2BGBhsqYDAkJ-B3yhndZCAGtU1a5HLNvh3NHL98qM1qLKJ7lj3W6Bq2BZDf3g3JHInZkAiai5EAztLBcFBytqf8cVFkBa-tX8EktdOjN3XrsuAJ8NbAtkMnDpCasRxa2Av90I9qnoC4yJMz0TRIJ2k8ONTBZcV9vKNcHsOvBFzRhz9YInf4PaWZALTZyX32nm4gq3OUvKqxuOJ3TTGYqP3kWLB1SWOWbxH3bYQ4zb-2UGAfDuRwcXGba6fk8_I2J_gXZ1SIJaRESIRXd5KkLMtmr_zFPArsoZC8-AqzV-4qXHruMK4zmWHq9rAu7uge2HYnZ5siS5Tp6L7OYeaWD0P-MHPtIX_E_z1fkCetp8XYnbgT7ekydBbOovGUpun_8oR15Z-p-Kp8rbzIjZbalxOMg4X9o16T5tIP506_TsDvWAwd0SiKvFVbqtU4cOznRS8jb2wveqJbKuGePraC04WvBaMgjJzwWcGTv36U1eaaF3Ej6K2CKNCC4aUTzd1nBf25409UhLnz5dZaYBtXsSTXHEaXLCGfqkICuQKQ2F-31l_K1EXTdwnkkqWPZF6WvLiDhKyrsswY8NbO69qhZgqcoyHN0bgZGU0TLc9_jcSUzlI6KjPampAllZQsOGARE_L6Lafljkl4g8w3ihr0qFdoWi8BvBB4dSKzIu9Qxi1FyKIkN7DHfFqnES_25CZ6IHWdQYgONexRjd4g6TAmdZWP6LEMV5TlEj_kuuI4rgLQ-98VE6yOsVORKdK0rY5sARxLy-JjRie9Ajdpwck18LTge5rH0Io49tNTE269e0cb3B7xjiyLVrI-a_Iul5CdIuG4f3Mpfr21DodGxjHLwEOcVYLdwdtTj3cp7ssp3ssp_sspwcspYzOlf_aqfMlZ6cKXu5t80T2W4k4EPipKyEk7VziieIWOP8D92TTpc5-aJZaAce7xmdbGvi4h1h3V1XBts8YKnyabjIlO_jgmuIygS3b-cw6m-F3XTNdN-zHfFJQnpx2lWZ6ZpaZPk2-iT12W_0yoQlTQtw3Mtlc0p1sgn_HhhxXJt53FoaljM_UGYmDd5VNv4B8PIzSz50KgG3MNJz-p4RoyiNVm1KTpcwn2N9GPZ-7ZP-MWuPKAvGdCdmk_a5X23I5loRn7dlp_H8uy4LLC_cegm7nn_usp4SNPchrLLmVKRqNf6tHTM6iAUE_UCWjeQvBCAY5ueUVpGOqrrXdxDXy_tf6sg_2OhLMb-FRqhBSxEfLVd23fN2gAT69rFZqrx0kxtIWnLDw9Ogrw9VQoINCtrwAd5lgBoe5RBUx0Byq3vl7XymKq201ZBHo7q1TsPuDodunl4qnyea4-_hPQhOH1olCKzlivaAVM9b7vnVTbBc2dD8XxRth5NasPqnnRPoMDMzxWr8pnYGgCJ2aBqRnGdlKvnOewY4ZdM-yZYd8MB2Z4bIZDMzxp3mzP4akRxvEzwo4Zds2wZ4Z9MxyY4bEZDs2wOUvXnKVnztIzZ-npLK2htccHPWWJNXuyjj-p8Wd3AimtMmkdhhatZLF-zGNrdvzpaVVlgkeyZHTL6f4EHv4BKSP_XQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Commodity Manager | PM-050-010_Identify_Need_for_RFQ, PM-050-020_Determine_Material_Specifications, PM-050-030_Establish_Material_Profile, PM-050-030_Establish_Material_Profile_(Copy), PM-050-040_Identify_Potential_Suppliers, PM-050-050_Identify_Supplier_Rationalization_Opportunities, PM-050-070_Create_Supplier_RFQ, PM-050-080_Issue_RFQ, PM-050-090_Conduct_Pre-bid_Quotation_Meeting, PM-050-100_Receive_Supplier_Quotations, PM-050-110_Process_Supplier_Quotations, PM-050-120_Perform_Price_Simulation, PM-050-150_Supplier_Selection, PM-050-160_Maintain_Supplier_Profile, PM-050-170_Identify_Approved_Suppliers,  | |
| Procurement Agent | PM-050-060_Manage_Tendering_Process, PM-050-130_Perform_Total_Cost_Model_Analysis,  | |
| Sourcing Manager | PM-050-090_Conduct_Pre-bid_Quotation_Meeting,  | |
| Supplier Administrator | PM-050-140_Supplier_Onboarding,  | |
|  | PM-050_Manage_Quotation | |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for PM-050. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
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

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for PM-050.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for PM-050.

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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for PM-050:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for PM-050:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (378 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

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

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>PM-050 — Manage Quotation</span></div>
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

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

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
*PM-050 — Architecture Document (TOGAF BDAT) · Procure To Pay · Generated: March 2026*

