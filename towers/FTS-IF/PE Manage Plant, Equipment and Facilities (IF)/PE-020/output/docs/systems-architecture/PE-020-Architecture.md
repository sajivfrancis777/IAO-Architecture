<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">PE-020 — Identify Maintenance Structure (IF)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Forecast to Stock (IF) (FTS-IF) Tower<br/>
  Capability PE-020 · PE Manage Plant, Equipment and Facilities (IF)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **PE-020 Identify Maintenance Structure (IF)** within the IAO program. It includes 6 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Forecast to Stock (IF) (FTS-IF) |
| **Process Group** | PE Manage Plant, Equipment and Facilities (IF) |
| **Capability** | PE-020 - Identify Maintenance Structure (IF) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 5 Reports, 92 Interfaces, 31 Conversions, 118 Enhancements, 15 Forms, 4 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Forecast to Stock (IF) |
| **L1 Process** | PE Manage Plant, Equipment and Facilities (IF) |
| **L2 Capability** | PE-020 - Identify Maintenance Structure (IF) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Intel Foundry Supply Chain Integration | Integrate Intel Foundry manufacturing and logistics into unified S/4 HANA supply chain | IDM 2.0 Foundry Enablement | High |
| 2 | Warehouse & Logistics Modernization | Modernize warehouse management and shipping processes with EWM integration | Supply Chain Digital Transformation | High |
| 3 | Production Planning Optimization | Enable MRP-driven production planning with real-time material availability | Manufacturing Excellence | Medium |
| 4 | PE-020 Process Migration | Migrate Identify Maintenance Structure (IF) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Supply Chain (Intel Foundry) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Fulfillment Lead Time | < 48 hours | Time from production completion to shipment dispatch | 72 hours (legacy) | Logistics Manager |
| Inventory Accuracy | > 99.5% | Physical vs system inventory match rate | 97.8% (current) | Warehouse Manager |
| MRP Planning Cycle | < 4 hours | End-to-end MRP run including exception processing | 8 hours (legacy) | Planning Lead |
| PE-020 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **6 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for PE-020 Identify Maintenance Structure (IF).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | PE-020-010_Establish_Process_Related_Structures | PE-020-010_Establish_Process_Related_Structures | FTS IF - Design Engineer, FTS IF - Intel Data Admin | 2 | 1 |
| 2 | PE-020-020_Establish_Organization_Related_Structures | PE-020-020_Establish_Organization_Related_Structures | Design Engineer, FTS IF - IT Non Prod Role | 3 | 0 |
| 3 | PE-020-030_Define_Maintenance_Resource_Structure_and_Allocation | PE-020-030_Define_Maintenance_Resource_Structure_and_Allocation | FTS IF - Design Engineer | 3 | 0 |
| 4 | PE-020-040_Define_Maintainable_Item_Listing_Structure | PE-020-040_Define_Maintainable_Item_Listing_Structure | FTS IF - Design Engineer | 1 | 0 |
| 5 | PE-020-050_Define_Maintenance_Information_System_Reporting_Requirements | PE-020-050_Define_Maintenance_Information_System_Reporting_Requirements | FTS IF - Maintenance Technician, FTS IF - PM  - IT Team | 3 | 0 |
| 6 | PE-020-060_Design_Maintenance_Roles_and_Authorization_Profiles | PE-020-060_Design_Maintenance_Roles_and_Authorization_Profiles | FTS IF - PM  - IT Team | 1 | 1 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 PE-020-010_Establish_Process_Related_Structures — PE-020-010_Establish_Process_Related_Structures

**Swim Lanes**: FTS IF - Design Engineer · FTS IF - Intel Data Admin | **Tasks**: 2 | **Gateways**: 1

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
    subgraph FTS IF - Design Engineer
        n1["fa:fa-user Identify Process Related Structures"]
        n4["Establish Policies and Procedures for Management of Physical Assets"]
        n5["Communicate Maintenance Philosophy"]
        n6{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph FTS IF - Intel Data Admin
        n2["fa:fa-user Define Functional Location and Equipment"]
        n3["Establish Organization Related Structures"]
    end
    n2 --> n3
    n4 --> n6
    n5 --> n6
    n6 --> n1
    n1 --> n2
    class n1 userTask
    class n2 userTask
    class n3 startEvt
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVV1vozgU_SsWVZUXIgGBkOFhpZTAqlJHW026Mw-TeXDMNVg1dtY2bdIo_33tkI8m287L8oByT-49597jD7YekRV4mXd7u2WCmQxtB6aBFgYZGiyxhoGPeuA7VgwvOeiBy6FSmDl726eF8Wrt0hxW4pbxjUPnUEtAf9_7aGoLuY80FnqoQTE68AcrxVqsNrnkUrnsG5jQgO7VDn_dSVWBOicEQRqSxJZyJuAMj9I4jUtXp4FIUV2Q0oROKBnsXHNcvpIGK7Nvv9PwFa9_sMo0NqaYa7A5jWn5A14CdzMa1TmMdOrlaAbTTkdYw-YrTJioLR4HFlJYPJ-hJNjt0O72diFOouhpthDIPoRjrWdAkTYWLl4Moozz7CbOp2US-Noo-QzZTVSks1HkEzdJZkcPfGfu8BVY3ZhsKXl1SB2-uhmyaLX21TqLAl9t7PtKC0R1VsrH0SSanJTu0jAP86MSpfR_KVlf1RPWzwetYlRG5eykFSbjJA_-y3cccxan0_DaJ1AvjMA70rIsR8XZqmKchMHnpHflaBzkV6Q1NvCKN2fCL3l8IiyTtAzTTwl7vesuu-WjkuRIOCqSMjkRpndhOY0-JYynYTw5dGh5aoVXDSqf5ui-REM0A81qgQpR220Pqk9zjwh_LjyKM4qHznV0X4EwjG6QawS0Rt-A2zErNLc7mZhOgV54v97Vx7a-sNtwyZlu0KPkjDDQCIuqp6hcCaJSoa9Y4NpeAcIgSdFjs9GMYI6mWoO5Ik0saS7bthM2xYAtZcKAwIKALWRcarlqNpc14-32OIm7jIZLe5xIg2BNeKfZC_zZr9bC2-36KrufP7Pr3qpxNMMGo2nVMvFOJrr0yy6bdRSVnSCGSWHneZC2Zftzb0HxT8dWbuTLXkcXpv2laizYW1_1G79PDYsIDYd_WJpDGPfh-BAml-G4Dw9HQoR9GL3bew48nrkLOPoYHp3unQs4_hhOPobHx_Pj-V4LqsWs8rKtt_9K2C9JBRR33Hg738OdkfONIF62v029blXZyhnDdtXaHtz9C0I_GTQ=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 PE-020-020_Establish_Organization_Related_Structures — PE-020-020_Establish_Organization_Related_Structures

**Swim Lanes**: Design Engineer · FTS IF - IT Non Prod Role | **Tasks**: 3 | **Gateways**: 0

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
    subgraph Design Engineer
        n1["fa:fa-user Identify Maintenance Organization Structure Across the Company"]
        n5["Establish Process Related Structures"]
    end
    subgraph FTS IF - IT Non Prod Role
        n2["fa:fa-user Define Maintenance Plants and Planning Across Organization"]
        n3["fa:fa-user Identify and Define Plant Sections and Locations Across the Plant"]
        n4["Define Maintenance Resource Structure and Allocation"]
    end
    n5 --> n1
    n1 --> n2
    n3 --> n4
    n2 --> n3
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVU1v4jAQ_StWKsQlSPls2BxWooFIldrdVWF3D8sejDMGq8ZGttOWIv772iR8tpw2B5R5mXlv5jFONh6RFXi51-lsmGAmR5uuWcASujnqzrCGro8a4BdWDM846K7LoVKYMXvfpYXJ6s2lOazES8bXDh3DXAL6ee-jgS3kPtJY6J4GxWjX764UW2K1LiSXymXfQJ8GdKfWPrqTqgJ1TAiCLCSpLeVMwBGOsyRLSlengUhRnZHSlPYp6W5dc1y-kgVWZtd-reERv_1mlVnYmGKuweYszJI_4BlwN6NRtcNIrV72ZjDtdIQ1bLzChIm5xZPAQgqL5yOUBtst2nY6U3EQRZPhVCB7EY61HgJF2lh49GIQZZznN0kxKNPA10bJZ8hvolE2jCOfuElyO3rgO3N7r8DmC5PPJK_a1N6rmyGPVm--esujwFdr-3uhBaI6KhW3UT_qH5TusrAIi70SpfS_lKyvaoL1c6s1isuoHB60wvQ2LYKPfPsxh0k2CC99AvXCCJyQlmUZj45WjW7TMLhOelfGt0FxQTrHBl7x-kj4pUgOhGWalWF2lbDRu-yynv1QkuwJ41FapgfC7C4sB9FVwmQQJv22Q8szV3i1QEPQbC7QSMzttoNqnrpLhH-mHsU5xT1nNrqvQBhG1-gRM2FAYEEAfVdzLNg7NkwKNLabTEytAA2Ikloje5xRIZcrLNZT7-8JdWqpR3YxZ5zpBXIDgU1_Am7tqo48-lBlF-ui73IyRvcl6qH7CfpmxS1JhZ4khxOZ6HwC65-d8az_HxwLoxEW1e5W2HO1b_50tPPu4yvGOJZWY8eLxkBcdcP_IAluohN3dnnn7Ill_6TTJ9CyVvbm6LJjHXDe8n70SqSo1_tq_8g2DJswasO4CZM2jJowPlk4V7I_aGdw9Dkcfw4nh3fQGZweYM_3lqCWmFVevvF2HwH7oaiA4pobb-t7uDZyvBbEy3cvS69eVXZThgzbXVg24PYfkscRgQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.3 PE-020-030_Define_Maintenance_Resource_Structure_and_Allocation — PE-020-030_Define_Maintenance_Resource_Structure_and_Allocation

**Swim Lanes**: FTS IF - Design Engineer | **Tasks**: 3 | **Gateways**: 0

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
    subgraph FTS IF - Design Engineer
        n1["fa:fa-user Identify Maintenance Resources Who Perform Maintenance Activities"]
        n2["fa:fa-user Establish and Implement Infinity/TCP Programs and Policies"]
        n3["fa:fa-user Assign/Allocate Maintenance Resources to Maintenance Team (Workcenters)"]
        n4["Define Maintainable Item Listing Structure"]
        n5["Establish Organization Related Structures"]
    end
    n5 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVd9r2zAQ_leES8kGDvPPOvPDIHViCGysLNn6sO5BkU-JqCwFSW6Tlvzvk-Ikrtv1aQYb3-e777s7Sednj8gKvNy7vHxmgpkcPQ_MGmoY5GiwxBoGPmqBX1gxvOSgB86HSmHm7OngFiabrXNzWIlrxncOncNKAvo589HYBnIfaSz0UINidOAPNorVWO0KyaVy3hcwogE9qB0_XUtVgeocgiALSWpDORPQwXGWZEnp4jQQKaoeKU3piJLB3iXH5SNZY2UO6TcavuHtLavM2toUcw3WZ21q_hUvgbsajWocRhr1cGoG005H2IbNN5gwsbJ4ElhIYXHfQWmw36P95eWdOIuixeROIHsRjrWeAEXaWHj6YBBlnOcXSTEu08DXRsl7yC-iaTaJI5-4SnJbeuC75g4fga3WJl9KXh1dh4-uhjzabH21zaPAVzv7fKUFouqUiqtoFI3OStdZWITFSYlS-l9Ktq9qgfX9UWsal1E5OWuF6VVaBG_5TmVOkmwcvu4TqAdG4AVpWZbxtGvV9CoNg_dJr8v4Kiheka6wgUe86wg_F8mZsEyzMszeJWz1XmfZLG-UJCfCeJqW6Zkwuw7LcfQuYTIOk9ExQ8uzUnizRuVijmYlGqIJaLYSaCpWdtuDat3cJcLfdx7FOcVD13U0q0AYRnfoG2bCgMCCAPoBWjaKgEa3a4luQFGp6p7HmBj2wAwDfef9ecEe9dmndr8uOdNrhEWFZvWG25EgDJoJ6sbG7tOiuEG2BTb7Wh98biRn5A1t3Kcda1fdpzHnktg1eSd3I3sfFoBr9OFWqntiUwClP_Y1EqthF8X2qw2ztxtcaGagRl-ZNvaYork938Q0CvqxqY3tav2uVliwJ2yYFDYfblOsusiuNHvA2heRouHwi12boxm2ZnQ0o9aMj2bcmsmLzeRCToeoB0f_huN_w8l5vvTg9Ax7vleDqjGrvPzZOwx4-xOogOKGG2_ve7gxcr4TxMsPg9BrNpWtfsKwW-EW3P8FUIAGaA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.4 PE-020-040_Define_Maintainable_Item_Listing_Structure — PE-020-040_Define_Maintainable_Item_Listing_Structure

**Swim Lanes**: FTS IF - Design Engineer | **Tasks**: 1 | **Gateways**: 0

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
    subgraph FTS IF - Design Engineer
        n1["fa:fa-user Identify Technical Objects that are Subject to Maintenance"]
        n2["Define Maintenance Information System Reporting Requirements"]
        n3["Define Maintenance Resource Structure and Allocation"]
    end
    n3 --> n1
    n1 --> n2
    class n1 userTask
    class n2 startEvt
    class n3 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVMuO2jAU_RUrI8QmSHkSmkUlXpGQOmpVaLsoXRjnmrjj2NR2Biji32vzhnZW9SKyT47Puff62juPyBK83Gu1dkwwk6Nd21RQQztH7QXW0PbREfiKFcMLDrrtOFQKM2W_D7QwWW0czWEFrhnfOnQKSwnoy8RHfbuR-0hjoTsaFKNtv71SrMZqO5RcKsd-gh4N6MHt9GsgVQnqSgiCLCSp3cqZgCscZ0mWFG6fBiJFeSdKU9qjpL13wXG5JhVW5hB-o-EZb76x0lR2TTHXYDmVqfkHvADucjSqcRhp1Ou5GEw7H2ELNl1hwsTS4klgIYXFyxVKg_0e7VutubiYotloLpAdhGOtR0CRNhYevxpEGef5UzLsF2nga6PkC-RP0TgbxZFPXCa5TT3wXXE7a2DLyuQLycsTtbN2OeTRauOrTR4Fvtra74MXiPLqNOxGvah3cRpk4TAcnp0opf_lZOuqZli_nLzGcREVo4tXmHbTYfC33jnNUZL1w8c6gXplBG5Ei6KIx9dSjbtpGLwtOijibjB8EF1iA2u8vQq-GyYXwSLNijB7U_Do9xhls_ikJDkLxuO0SC-C2SAs-tGbgkk_THqnCK3OUuFVhYrZFE0K1EEj0Gwp0FgsbduDOtLcEOH3uUdxTnHHVR1NShCG0S2aAakEI5ijj4ufQIxGpsIGYQVo2hwQZCR6xkwYEFgQmHs_bmQjK2tTsm63HDQRVKoaGyYFmm61gRp9hpVUxva8nf1qmLKPhDD6Xi3-t9pn0LJRdjK114yYxsaGRYn6nEty8Lio2N49TkSMOp33Nu3TMjwuo5uTcOC5A-_g6HLd7uD4Anu-V4NNj5VevvMO7519E0uguOHG2_seboycbgXx8sO74DWr0vbQiGF7XPUR3P8BFJ64pw==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 PE-020-050_Define_Maintenance_Information_System_Reporting_Requirements — PE-020-050_Define_Maintenance_Information_System_Reporting_Requirements

**Swim Lanes**: FTS IF - Maintenance Technician · FTS IF - PM  - IT Team | **Tasks**: 3 | **Gateways**: 0

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
    subgraph FTS IF - Maintenance Technician
        n1["fa:fa-user Review and Update Missing Work Order Data to Capture Relevant Data to the..."]
        n3["Review all the Job Documentation like Spec, task list."]
        n5["Define Maintainable Item Listing Structure"]
    end
    subgraph FTS IF - PM  - IT Team
        n2["fa:fa-user Define responsibility for entering the information and ownership of SAP PM..."]
        n4["Design Maintenance Roles and Authorization Profiles"]
    end
    n5 --> n3
    n3 --> n1
    n2 --> n4
    n1 --> n2
    class n1 userTask
    class n2 userTask
    class n4 startEvt
    class n5 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVdFuozoQ_RWLqsoLqYBAyeVhpZQEqautttpk7z7c7oMDQ7BibGSbpNkq_37HISFNevt0kUCaw_icmcPYvDm5LMBJnNvbNyaYScjbwFRQwyAhgyXVMHBJB_xNFaNLDnpgc0opzJz9OaT5YfNq0yyW0ZrxnUXnsJJAfj66ZIILuUs0FXqoQbFy4A4axWqqdqnkUtnsGxiXXnlQO756kKoAdU7wvNjPI1zKmYAzPIrDOMzsOg25FMUFaRmV4zIf7G1xXG7ziipzKL_V8ERff7HCVBiXlGvAnMrU_BtdArc9GtVaLG_V5mQG01ZHoGHzhuZMrBAPPYQUFeszFHn7Pdnf3r6IXpQspi-C4JVzqvUUSqINwrONISXjPLkJ00kWea42Sq4huQlm8XQUuLntJMHWPdeaO9wCW1UmWUpeHFOHW9tDEjSvrnpNAs9VO3xeaYEozkrpfTAOxr3SQ-ynfnpSKsvyfymhr2pB9fqoNRtlQTbttfzoPkq9j3ynNqdhPPGvfQK1YTm8I82ybDQ7WzW7j3zvc9KHbHTvpVekK2pgS3dnwr_SsCfMojjz408JO73rKtvls5L5iXA0i7KoJ4wf_GwSfEoYTvxwfKwQeVaKNhXJFnPymJEheaJMGBBU5EAWkFeC5YyKLttewv_nxSlpUtKhNZ_8gA2DLaGiID-bAvskT0xrHEzyS6o1-W43FZlSQ4mRJKWNaRXgIg4bKkz_Anf83d3di_P7ndAIhU7snNsU8lUuyVTmbQ3CUMOkIJytgcwbyF1i7CfjTJsrngh50DPcxV1zeNtzhTwaqMk3zLfFznH75ba2fi0O8WcePT8RfD4u0CBav1MKLq05iirQjRSaLRlnBmdAKuQ2eC6hrG2KCYTqrh1ro9wKULpiDZElmU-eUe6DN-GhJ81W4uKD_ZB4Xh5IJq2ppGJ_OlqcFZwU0B-bExEZDr-g2cdw1IXHXSGCLgyPod-FwbtptOBpF17AwX_DYX8SXcBRDzuuUwP6wQoneXMOvwL8XRRQ0pYbZ-86tDVyvhO5kxyOTKc9jN2UUfxKdQfu_wXSXA-k" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.6 PE-020-060_Design_Maintenance_Roles_and_Authorization_Profiles — PE-020-060_Design_Maintenance_Roles_and_Authorization_Profiles

**Swim Lanes**: FTS IF - PM  - IT Team | **Tasks**: 1 | **Gateways**: 1

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
    subgraph FTS IF - PM  - IT Team
        n1["fa:fa-user Define Maintenance Roles Transferred from Infinity to S/4 for Execution of..."]
        n2["Execute Maintenance Order"]
        n3["Create and Maintain Maintenance Master Records"]
        n4["Define Maintenance Information System Reporting Requirements"]
        n5{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n4 --> n1
    n1 --> n5
    n5 --> n2
    n5 --> n3
    class n1 userTask
    class n2 startEvt
    class n3 startEvt
    class n4 startEvt
    class n5 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVE1v2kAQ_SsrRxEXk_ozpj5UIgZXkRo1CrQ9lB4WexZWsXfp7jpAEf-9s5iPQJNTLWF5HjPvzTzt7MYpZAlO6lxfb7jgJiWbjplDDZ2UdKZUQ8clLfCdKk6nFeiOzWFSmBH_s0vzo8XKplkspzWv1hYdwUwC-Xbvkj4WVi7RVOiuBsVZx-0sFK-pWmeykspmX0GPeWyntv_rTqoS1CnB8xK_iLG04gJOcJhESZTbOg2FFOUZKYtZjxWdrW2ukstiTpXZtd9oeKCrH7w0c4wZrTRgztzU1Rc6hcrOaFRjsaJRLwczuLY6Ag0bLWjBxQzxyENIUfF8gmJvuyXb6-uJOIqS8WAiCD5FRbUeACPaIDx8MYTxqkqvoqyfx56rjZLPkF4Fw2QQBm5hJ0lxdM-15naXwGdzk05lVe5Tu0s7QxosVq5apYHnqjW-L7RAlCel7DboBb2j0l3iZ352UGKM_ZcS-qrGVD_vtYZhHuSDo5Yf38aZ9y_fYcxBlPT9S59AvfACXpHmeR4OT1YNb2Pfe5_0Lg9vveyCdEYNLOn6RPgxi46EeZzkfvIuYat32WUzfVSyOBCGwziPj4TJnZ_3g3cJo74f9fYdIs9M0cWc5OMRuc9Jlzw-EHzfj8kYaN0m2Uf4PycOoymjXes5wSZwLcgD5cKAoKIA8iRxWckYz6ZmoBSUhClZk3vB7KKviZFk9CEiTCoyXEHRGC4Fkezm5mbi_HqlFKBSm3DO_9Xu53lqiKmZAnSXUFG22fg7K3ug2mDDT7itqtTn9RHWvzEJtixVTXcNjtZYXmP5QiqD-4Zfvxuu8IIS5oIt3mwOHtlLrjtFK4o5gVVRNZq_wOf2FEyc7batwj1pP0REut1PaPI-9Nsw3odxGwbnYfjqTNiSwy6cwcFx8c_g8G04ehuODwfYcZ0a0BleOunG2V3TeJWXwGhTGWfrOrQxcrQWhZPurjOnWZRYOeAUT1ndgtu_3vfvPg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| FTS IF - Design Engineer | PE-020-010_Establish_Process_Related_Structures, PE-020-030_Define_Maintenance_Resource_Structure_and_Allocation, PE-020-040_Define_Maintainable_Item_Listing_Structure,  | |
| FTS IF - Intel Data Admin | PE-020-010_Establish_Process_Related_Structures,  | |
| Design Engineer | PE-020-020_Establish_Organization_Related_Structures,  | |
| FTS IF - IT Non Prod Role | PE-020-020_Establish_Organization_Related_Structures,  | |
| FTS IF - Maintenance Technician | PE-020-050_Define_Maintenance_Information_System_Reporting_Requirements,  | |
| FTS IF - PM  - IT Team | PE-020-050_Define_Maintenance_Information_System_Reporting_Requirements, PE-020-060_Design_Maintenance_Roles_and_Authorization_Profiles | |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for PE-020. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
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

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for PE-020.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for PE-020.

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

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
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

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for PE-020:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for PE-020:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
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

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>PE-020 — Identify Maintenance Structure (IF)</span></div>
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
*PE-020 — Architecture Document (TOGAF BDAT) · Forecast to Stock (IF) · Generated: March 2026*

