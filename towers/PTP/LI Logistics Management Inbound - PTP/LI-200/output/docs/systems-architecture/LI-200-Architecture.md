<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">LI-200 — Determine Discrepant Material Disposition</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Procure To Pay (PTP) Tower<br/>
  Capability LI-200 · LI Logistics Management Inbound - PTP</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **LI-200 Determine Discrepant Material Disposition** within the IAO program. It includes 12 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Procure To Pay (PTP) |
| **Process Group** | LI Logistics Management Inbound - PTP |
| **Capability** | LI-200 - Determine Discrepant Material Disposition |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 3 Reports, 171 Interfaces, 16 Conversions, 171 Enhancements, 7 Forms, 10 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Procure To Pay |
| **L1 Process** | LI Logistics Management Inbound - PTP |
| **L2 Capability** | LI-200 - Determine Discrepant Material Disposition |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Procurement Process Standardization | Standardize procurement processes across direct, indirect, and services on S/4 HANA + Ariba | IDM 2.0 Procurement Excellence | High |
| 2 | Supplier Collaboration Enhancement | Enable digital supplier collaboration for consignment, subcontracting, and quality management | Supplier Ecosystem | High |
| 3 | Payment Automation | Automate invoice verification, three-way matching, and payment execution | Finance Efficiency | Medium |
| 4 | LI-200 Process Migration | Migrate Determine Discrepant Material Disposition business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Procurement | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| PO Cycle Time | < 24 hours | Requisition approval to PO dispatch to supplier | 48 hours (current) | Procurement Lead |
| Invoice Automation Rate | > 80% | Invoices processed without manual intervention (touchless) | 45% (current) | AP Manager |
| Supplier On-Time Delivery | > 95% | Supplier adherence to confirmed delivery date | 89% (current) | Supplier Management |
| LI-200 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **12 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for LI-200 Determine Discrepant Material Disposition.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | LI-200-010_Determine_Material_Disposition | LI-200-010_Determine_Material_Disposition | Procurement Buyer, Warehouse Clerk | 6 | 5 |
| 2 | LI-200-020_Issue_Return_Notice_for_Rework | LI-200-020_Issue_Return_Notice_for_Rework | Buyer, Factory Engineer, Maintenance Planner, PR Requestor, Warehouse Clerk | 24 | 9 |
| 3 | LI-200-040_Rework_Material | LI-200-040_Rework_Material | Intel Engineer, Maintenance Planner, Quality Analyst, Warehouse Clerk | 6 | 6 |
| 4 | LI-200-050_Bill_Supplier_for_Rework | LI-200-050_Bill_Supplier_for_Rework | Invoicing Specialist, Procurement Buyer | 5 | 3 |
| 5 | LI-200-060_Issue_Return_Notice_for_Repair | LI-200-060_Issue_Return_Notice_for_Repair | Buyer, Factory Engineer, Maintenance Planner, PR Requestor, Warehouse Clerk | 24 | 9 |
| 6 | LI-200-080_Repair_Material | LI-200-080_Repair_Material | Intel Engineer, Maintenance Planner, Quality Analyst, Warehouse Clerk | 6 | 6 |
| 7 | LI-200-090_Bill_Supplier_for_Repair | LI-200-090_Bill_Supplier_for_Repair | Invoicing Specialist, Procurement Buyer | 5 | 3 |
| 8 | LI-200-100_Issue_Waiver_Request | LI-200-100_Issue_Waiver_Request | Procurement Buyer, Warehouse Clerk | 3 | 3 |
| 9 | LI-200-120_Reverse_Goods_Receipt_Against_Purchase_Order | LI-200-120_Reverse_Goods_Receipt_Against_Purchase_Order | Inventory Manager | 6 | 5 |
| 10 | LI-200-130_Send_Credit_Memo_to_Supplier | LI-200-130_Send_Credit_Memo_to_Supplier | Accounts Payable Accountant | 8 | 4 |
| 11 | LI-200-140_Scrap_Material | LI-200-140_Scrap_Material | Buyer, Inventory Manager | 7 | 5 |
| 12 | LI-200-150_Notify_Supplier | LI-200-150_Notify_Supplier | Procurement Buyer, Warehouse Clerk | 3 | 5 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 LI-200-010_Determine_Material_Disposition — LI-200-010_Determine_Material_Disposition

**Swim Lanes**: Procurement Buyer · Warehouse Clerk | **Tasks**: 6 | **Gateways**: 5

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
    subgraph Procurement Buyer
        n3["fa:fa-user Generate Waiver Request"]
        n4["fa:fa-user Rework or Repair PO Created"]
        n5["fa:fa-user Create Return PO for Credit or Replacement"]
        n6["fa:fa-user Align Supplier for Material Disposition"]
        n7["Return Material to Supplier for Repair"]
        n8["Scrap Material"]
        n9["Return Material to Supplier"]
        n10["Return Material to Supplier for Rework"]
        n11["Receive Materials and Services - PTP"]
        n16{{"fa:fa-code-branch Accept Materials?"}}
        n17{{"fa:fa-code-branch Can Material Be Reworked or Repaired?"}}
        n18{{"fa:fa-code-branch Return Material?"}}
        n19{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Warehouse Clerk
        n1["fa:fa-user Identify Discrepant Materials"]
        n2["fa:fa-user Notify Procurement Discrepancies"]
        n12["Review Testing Documentation"]
        n13["Move Material to Holding Location"]
        n14["Execute Maintenance Order"]
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n12 --> n15
    n13 --> n15
    n15 --> n1
    n1 --> n2
    n16 -->|"yes"| n3
    n3 --> n11
    n16 -->|"No"| n17
    n17 -->|"Yes"| n4
    n4 --> n19
    n19 --> n7
    n19 --> n10
    n5 --> n9
    n18 -->|"Yes"| n5
    n6 --> n16
    n2 --> n6
    n18 -->|"No"| n8
    n17 -->|"No"| n18
    n14 --> n15
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVttu4zYQ_RVCQeAXG5Bk3ayHFr5pu0CyG8Rpg6LuA01RNhGaVCnKl3r97yVlSbYUuShQPwTh4ZwzM0fkSCcD8RgbofH4eCKMyBCcenKDt7gXgt4KZrjXBxfgNygIXFGc9XRMwplckL-LMMtJDzpMYxHcEnrU6AKvOQa_fu2DsSLSPsggywYZFiTp9XupIFsojlNOudDRDzhIzKTIVm5NuIixuAaYpm8hV1EpYfgKD33HdyLNyzDiLG6IJm4SJKh31sVRvkcbKGRRfp7hZ3h4J7HcqHUCaYZVzEZu6RNcYap7lCLXGMrFrjKDZDoPU4YtUogIWyvcMRUkIPu4Qq55PoPz4-OS1UnB0-uSAfVDFGbZDCcgkwqe7yRICKXhgzMdR67Zz6TgHzh8sOf-bGj3ke4kVK2bfW3uYI_JeiPDFadxGTrY6x5COz30xSG0zb44qr-tXJjF10xTzw7soM408a2pNa0yJUnyvzIpX8UbzD7KXPNhZEezOpfleu7U_KxXtTlz_LHV9gmLHUH4RjSKouH8atXccy3zvugkGnrmtCW6hhLv4fEqOJo6tWDk-pHl3xW85GtXma9eBEeV4HDuRm4t6E-saGzfFXTGlhOUFSqdtYDpBmi1XKhrxySY5EcsLvv6x4Z_LI0EhgkcaLvBF8ywUA2Bd0h2av2K_8pxJpfGnzccp8l5xXsuPgDX_6WQCPDyHUwFVipxk-c2eZcYRZK5YJqU8AKMiSzFKERF1U0ZrykzpmTNwCJPU0rUUos8K109J8CMZCnPiCScNTV8pVEmroMlb6pcumnyAsVbIOVqTWvuj_5dtxlsmf-pCu1ui2gVRITVM6qZGYAsBovLEc_AALy8vbRo3ulUWacn9WClZg3agDFCOJVXoZ-Xxvl8y_O7eVN4U_cEl6Xi-HoUcPxJK-jWatnwiTa60qAQfJ8NIJUghQJSiumXyx28ktSUal2CdyjwhqsTA6YUK0NvtJvn6WusThxJjvrwIKHaYDfWNA21m8xvvODdXrdaAxHcIlt28RB3BO_Bm7pjat6DmWJqHvx8Yi19U5_5zQPXR-UXNVM18YmjLo6-qfMDRrnUNMIkZqoUDL7r12Er1u1-MPiAaJ6pg3bfY9UKGAx-0hoVMGwDbglU68vSrpaeXv9YGkft0g81lsqNSsdqB37jRZzlVxt-ufF7qeCUG06pMKoCRxfAb62tcgyzstI6PmgJVy15Jc8r16UHXptXVhq0C606qDecpmfF-0A7Vb0HG7DdDQ-7Yacbdrthrxv26--MBhx0w6Nu2DLv4NYd3L6DD-_gzh3crV7UTdjrhv1uOOiGRxVs9I0tFltIYiM8GcWnrvocjnECcyqNc9-AueSLI0NGWHwSGnkaK-aMQDWkthfw_A_yxY57" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 LI-200-020_Issue_Return_Notice_for_Rework — LI-200-020_Issue_Return_Notice_for_Rework

**Swim Lanes**: Buyer · Factory Engineer · Maintenance Planner · PR Requestor · Warehouse Clerk | **Tasks**: 24 | **Gateways**: 9

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
    subgraph Buyer
        n8["fa:fa-user Create Rework or Repair PO"]
        n9["fa:fa-user Issue Rework or Repair PO to Supplier"]
        n10["fa:fa-user Create Rework or Repair PO"]
        n11["fa:fa-user Issue Rework or Repair PO to Supplier"]
        n12["fa:fa-user Create Text PO"]
        n13["fa:fa-user Create Rework or Repair PO"]
        n19[["fa:fa-cog Create Return PO"]]
        n20[["fa:fa-cog Create Return PO"]]
        n29["Return Material to Supplier for Rework"]
        n30["Transmit Order to Supplier"]
        n39{{"fa:fa-code-branch exclusiveGateway"}}
        n43{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Factory Engineer
        n24["Perform Repair or Rework In-house"]
        n31["Bill Supplier for Repair"]
        n32["Order Sent to Supplier"]
        n40{{"fa:fa-code-branch Inhouse/External?"}}
    end
    subgraph Maintenance Planner
        n1["fa:fa-user Develop Corrective Action Plan"]
        n2["fa:fa-user Create Rework or Repair Order (Refurbishment Order)"]
        n3["fa:fa-user Create PM Order With Reason Code"]
        n16[["fa:fa-cog Execute Custom Program as Background Job"]]
        n23["Identify Failure Details"]
        n26["Return Material to Supplier for Repair"]
        n27["Scrap Material"]
        n33["Determine Material Disposition"]
        n42{{"fa:fa-arrows-alt Return/ Scrap/ Rework/ Repair?"}}
    end
    subgraph PR Requestor
        n4["fa:fa-user Create Rework or Repair PR"]
        n5["fa:fa-user Create Rework or Repair PR"]
        n6["fa:fa-user Create Service PR for Rework or Repair"]
        n7["fa:fa-user Create Service PO for Rework or Repair"]
        n17[["fa:fa-cog Create Rework or Repair PR"]]
        n18[["fa:fa-cog Create Text PR for Services"]]
        n28["Enable Payment"]
        n34["Order Received"]
        n35{{"fa:fa-code-branch Remote/ Onsite"}}
        n36{{"fa:fa-code-branch exclusiveGateway"}}
        n37{{"fa:fa-code-branch Original or Third-party Supplier?"}}
        n38{{"fa:fa-code-branch Reason Code?"}}
    end
    subgraph Warehouse Clerk
        n14["fa:fa-user Create Inbound Delivery and Replicate to EWM"]
        n15["fa:fa-user Post Goods Receipt for Text PO"]
        n21[["fa:fa-cog Update PM Order with GR Status"]]
        n22[["fa:fa-cog Update PM Order with No GR Status"]]
        n25(["fa:fa-stop PM Order Updated"])
        n41{{"fa:fa-code-branch Material Accepted in EWM and Posted GR?"}}
    end
    n33 --> n23
    n23 --> n1
    n1 --> n42
    n42 -->|"Rework/Repair"| n2
    n40 -->|"Inhouse"| n24
    n24 --> n31
    n7 --> n36
    n8 --> n9
    n36 --> n28
    n11 --> n29
    n35 -->|"Onsite"| n5
    n10 --> n11
    n42 -->|"Scrap"| n27
    n42 -->|"Return"| n26
    n4 --> n10
    n5 --> n8
    n9 --> n36
    n6 --> n7
    n35 -->|"Remote"| n4
    n32 --> n37
    n37 -->|"Third Party Supplier"| n34
    n37 -->|"Original Supplier"| n35
    n34 --> n6
    n40 -->|"External"| n32
    n42 --> n40
    n2 --> n3
    n3 --> n14
    n14 --> n41
    n41 -->|"Yes"| n21
    n41 -->|"No"| n22
    n22 --> n25
    n12 --> n43
    n13 --> n39
    n43 --> n15
    n15 --> n39
    n39 --> n30
    n20 --> n18
    n17 --> n13
    n18 --> n12
    n19 --> n39
    n16 --> n38
    n21 --> n16
    n38 -->|"Reason Codes: 
1. REPAIR
2. CLEAN HOT-QUENCH"| n17
    n38 -->|"Reason Code: 
1. DECONTAMINATE SCRAP"| n20
    n38 -->|"Reason Code: 
1. RETURN"| n19
    n43 --> n39
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
    class n20 serviceTask
    class n21 serviceTask
    class n22 serviceTask
    class n25 endEvt
    class n26 startEvt
    class n27 startEvt
    class n28 startEvt
    class n29 startEvt
    class n30 startEvt
    class n31 startEvt
    class n32 startEvt
    class n33 startEvt
    class n34 startEvt
    class n35 gateway
    class n36 gateway
    class n37 gateway
    class n38 gateway
    class n39 gateway
    class n40 gateway
    class n41 gateway
    class n42 gateway
    class n43 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWFtzokgU_itdTKWcrdIJzUXUh50yiDNuTRJXzaa2JvvQYhOpILgNJLoZ__uehm4UAtlsJg9J-PpcvnPl8qy40YoqA-Xs7NkP_WSAnlvJmm5oa4BaSxLTVhvlwB-E-WQZ0LjFZbwoTOb-P5kYNrY7LsaxMdn4wZ6jc3ofUXQzaaMhKAZtFJMw7sSU-V6r3doyf0PY3o6CiHHpD7TnqV7mTRxdRGxF2VFAVS3smqAa-CE9wrplWMaY68XUjcJVyahnej3PbR04uSB6cteEJRn9NKaXZHfrr5I1XHskiCnIrJNN8I0sacBjTFjKMTdljzIZfsz9hJCw-Za4fngPuKECxEj4cIRM9XBAh7Ozu7Bwir7N7kIEP25A4nhEPRQnADuPCfL8IBh8MOzh2FTbccKiBzr4oDnWSNfaLo9kAKGrbZ7czhP179fJYBkFKyHaeeIxDLTtrs12A01tsz38rvii4eroye5qPa1XeLqwsI1t6cnzvJ_yBHllCxI_CF-OPtbGo8IXNrumrb60J8McGdYQV_NE2aPv0hOj4_FYd46pcromVpuNXoz1rmpXjN6ThD6R_dFg3zYKg2PTGmOr0WDur8oyXU5Z5EqDumOOzcKgdYHHQ63RoDHERk8wBDv3jGzX6CLdU5Zj_Cfsfb9TPDLwSIenGNmMQghoRp8i9oAiBv9tic_Q9PpO-etErV9Wm8RxWquFkgjN0-028MFryQJW3-cZ4593rdW6XtBd8tKd_k6a_e-FohvdH_WSlIW59Km4pv4_cZ5_cXgJgnwRnsaLvIwZ51impfOsL2CtxBs_Qdd8EzbnSe8_Px9JrWhnCYruGtGdG6Sx_0i_5O1-pxwOJ2qGflQjjEVPcYcECdoSRoKABi-UYItUmnRM3CRie-SE97CTS_2qGRDAlDIIcCNzX8SKJmFnHUGdKnHwlrmACarmh2tXRHlr5GmZ0zBpzo2h1udmEmYEzp0dVCUkwefX4rwkfpjQEBQpmgYkDEuhVhp9RB9pEG2RHTFG3QTSj4bwJwoz1TI77W1Nmwf6cUa9lC39eL3hIWfgL5W01NqbXgoLt36yBpskBjI2JKMyCt1ybzs76qagbqdxEm0Q7DfIxgaRGF0Q9-GeRWm4Qr9Fy2rPcxKTFVD0vT20iB-kjEJWEvgvroTffdN4vCy_ZoHi3IXiFHqVRHAS4JOyDXTm0fjIj7dR7PNyVPpEqx2GnNw5ynydi8qcC06v9sx0BlJ_pxRyd9osxhvX1KxMz3yfWrdWbZ7fUjnF4_5BDam2Xjdx_QYT2GpYmnXsS4q9WsX8BpCTF0TiahPy-6UT8udVNCV7PjCVBjGKBTKjLoUpXVUEzPrFMaObKKHn6DqENqKVlap337WJdate7Zr5sFihbSHQxdpnqw4s52RfzMfnqp1eE-di5F_t2VvCaLYWkR1QuCWdVKK-byfhMtsCIxpAcHAnIHAB1Qx8lx_DKDu3l5VmqLTyNIoT9CWKVnFeiG2S1bX2Jq_hcj_cbFel_fbE99uXGZonJElftIT2BuWrqFnf_Fjow1Bvj5q5Jd4_v5xOOq4vRrGLhq5Lt6CH_JCnKcsdzwYgX2Z1dYKthjqdX_mKFYAmAPHQHOL80tDEtaFx4AdfstniktP5A1SliCpExB0xPzSkAyO3qEsPlrjuiuteft2XDLuCYU8yEpS0QsIU_uQAgTtTCqsiHFzln-3fnJr1Mja-o_NDSUvQxuI5PTTza8mqX4lCsLaqHPNhz0zLjOia0C2ELSGcTShsm9MJzVR1oypaDHZZTuZBF_S71RrJp5VcvFxlLiarJihKcyIZkgYW5o0izVjY_5MvUp7HFydXUX4gfWrCh1bUTpKQXrFwq8vKG5JHoWJWJHRZlyIQ2RBFO4n-w4UX0YBYEsP9ilEsiqtLG5poSSzTq_eKchd7Mh6guxB_QjNnOpzAu7v2CdnfnOEV-nq96Px-41zZX7OEYOsVI8LGyLGvrxbDy8nVcOGguT0bTvNkqv-tO3MWN7Or3FU1kTLE7C2UD798-y7BWj2s18NGPWzWw9162KqHe_Vwvx6GZVCPN8SJGwLFDZHihlBxQ6zQRyffIspHVvNRr_mo33gEfd94hJuPtOYjU3wEKqPd4jNUGbca8F4D3q_HdbUBxw241oDrDbjRgJvyC08Z7tbDVj3cq4f7tTCs6FoY18NaPaxLWGkrG3h3If5KGTwr2fdXZaCsqEfSIFEObYWkSTTfh64yyL5TKmn2DDLyCX9Hy8HDv-gpv7Y=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 LI-200-040_Rework_Material — LI-200-040_Rework_Material

**Swim Lanes**: Intel Engineer · Maintenance Planner · Quality Analyst · Warehouse Clerk | **Tasks**: 6 | **Gateways**: 6

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
    subgraph Intel Engineer
        n6["Perform Repair or Rework Inhouse"]
    end
    subgraph Maintenance Planner
        n5["fa:fa-user Complete Rework or Repair Order"]
        n11["Bill Supplier for Rework"]
        n12["Receive Materials and Services - PTP"]
        n18{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Quality Analyst
        n4["fa:fa-user Inspect Quality Post Rework or Repair"]
        n8(["fa:fa-play Material Sent after Rework/Repair"])
        n10["Return Material to Supplier"]
        n16{{"fa:fa-code-branch Quality meets the standard?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Warehouse Clerk
        n1["fa:fa-user Issue Materials to Rework or Repair Order"]
        n2["fa:fa-user Send Material to Supplier for Repair/ Rework"]
        n3["fa:fa-user Create Goods Receipt"]
        n7(["fa:fa-play Planning Started for Rework or Repair"])
        n9(["fa:fa-stop Material Sent"])
        n13{{"fa:fa-code-branch Remote/ Onsite?"}}
        n14{{"fa:fa-code-branch External / Inhouse"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n7 --> n1
    n1 --> n14
    n14 -->|"External"| n13
    n17 --> n4
    n4 --> n16
    n16 -->|"No"| n10
    n3 --> n5
    n5 --> n18
    n18 --> n12
    n18 --> n11
    n6 --> n17
    n16 -->|"Yes"| n3
    n14 -->|"Inhouse"| n6
    n13 -->|"Remote"| n2
    n8 --> n17
    n15 --> n9
    n2 --> n15
    n13 -->|"Onsite"| n15
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n7 startEvt
    class n8 startEvt
    class n9 endEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVluP4jYU_itWRiNaCTS5EoaHVgxDViPthQ7brqrSB5OcDNEYO7KdAcry32vnSjJBWrU8IPz5fN-5cpKTEbIIjKlxe3tKaCKn6DSQW9jBYIoGGyxgMEQF8AfmCd4QEANtEzMqV8k_uZnlpgdtprEA7xJy1OgKXhig35-GaKaIZIgEpmIkgCfxYDhIebLD_DhnhHFtfQOT2Ixzb-XVA-MR8MbANH0r9BSVJBQa2PFd3w00T0DIaNQSjb14EoeDsw6OsH24xVzm4WcCPuHDtySSW3WOMRGgbLZyRz7iDRCdo-SZxsKMv1XFSIT2Q1XBVikOE_qicNdUEMf0tYE883xG59vbNa2doo_Pa4rUJyRYiEeIkZAKXrxJFCeETG_c-SzwzKGQnL3C9MZe-I-OPQx1JlOVujnUxR3tIXnZyumGkag0He11DlM7PQz5YWqbQ35U3x1fQKPG03xsT-xJ7enBt-bWvPIUx_H_8qTqyr9i8Vr6WjiBHTzWvixv7M3N93pVmo-uP7O6dQL-loRwIRoEgbNoSrUYe5Z5XfQhcMbmvCP6giXs8bERvJ-7tWDg-YHlXxUs_HWjzDZLzsJK0Fl4gVcL-g9WMLOvCrozy52UESqdF47TLXqiEgha0Bc17MCLS_2h47_WxhJ4zPgOPUOKE44YV7_2jL8q1papFqyNvwuGanxH9xNOlDLFNAS0JJjSlrinxGM8jfFINxLN2S4lIKGSzx3lLr_o_2btJudaliI_qPzRKktTkih-XEfWMbWV6TOEkLyBikiCXhACYRqhVdFugUZo-XXZoU1Opyo-zDnbixEmEqWYY0KAfCiaujbO52vZ_5ZhksgjmlFMjkJeaLvtzJ-oSCGUNWHJhHxXhXZ0k59qiZSo2aryUilRiXCsTqXCXU3_-TI7My-KzDhtuJLV1ezUYtzUQm_w0UbtoLDJcAcgBVKLWy8avRWjX5vCFAp-vwIcQpIJ1ZkfqOc3zCGfODQnoLp8od6ppxDZZatVXj8yU3ZbRVUy6q1NOWla5q534pzOYHNQKugDY5FA-SCmsk3wO93M_ytqvaOV3tsQXcx2ayAuO3rfaAjJ0vZEdLvv9HfjGXZMwh36QkUi4V0P3X7W4qA8qRlHd81KaBO9_9x86qPR6BclUR6t8uhWZ1cD39dGFcTa-K7zq65LemXulvRxdT8u6Z9ZQSxXLXUKQ688eiVvUvEmJWB3gSrQcXn2u57-BJG7croZ1LVTl3V8TnlZdCa_q1xOuh7KIO_Ls13ee12tortFvt7Fo0VXt3qktmC7H3b6Ybcf9vphv343acGTfvi-fLtoR232G1vWFdy-gjvVo7oNu_2w1w-P-2G_H55UsDE0dsB3OImM6cnI34HVe3IEMc6INM5DA2eSrY40NKb5u6KRpZFiPiZYLcddAZ7_BZIql0A=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 LI-200-050_Bill_Supplier_for_Rework — LI-200-050_Bill_Supplier_for_Rework

**Swim Lanes**: Invoicing Specialist · Procurement Buyer | **Tasks**: 5 | **Gateways**: 3

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
    subgraph Invoicing Specialist
        n5["fa:fa-user Receive Credit Note from Supplier"]
        n10["Process Receipts"]
    end
    subgraph Procurement Buyer
        n1["fa:fa-user Calculate the Associated Costs"]
        n2["fa:fa-user Rework or Repair PO with Maintenance Cost"]
        n3["fa:fa-user Rework or Repair PO 0$ to Receive Material"]
        n4["fa:fa-user Create Service PO to Supplier for Payment"]
        n6(["fa:fa-play Rework or Repair Liability Assessed"])
        n7["Enable Payment"]
        n8["Receive Materials and Services - PTP"]
        n9["Enable Payment"]
        n11{{"fa:fa-code-branch Rework or Repair Inhouse/External?"}}
        n12{{"fa:fa-code-branch Is Material Under Warranty?"}}
        n13{{"fa:fa-code-branch Is Material Under Warranty?"}}
        n14[["fa:fa-folder-open Receive Materials and Services - PTP"]]
    end
    n6 --> n1
    n1 --> n11
    n11 -->|"Inhouse"| n13
    n12 -->|"No"| n2
    n13 -->|"No"| n4
    n5 --> n10
    n4 --> n7
    n3 --> n8
    n2 --> n14
    n14 --> n9
    n13 -->|"Yes"| n5
    n12 -->|"Yes"| n3
    n11 -->|"External Supplier"| n12
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 startEvt
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqllluPozYUx7-KxXSUViIq15DhoVXCBGmkmW202e2q2vTBAZNY49jINrlsNt-9NgESGEZbaXmI4r_P-Z0LcMzJSFiKjNC4vz9himUITgO5QVs0CMFgBQUamOAi_A05hiuCxEDbZIzKBf5WmtleftBmWovhFpOjVhdozRD4_GSCiXIkJhCQiqFAHGcDc5BzvIX8GDHCuLa-Q-PMyspo1daU8RTxq4FlBXbiK1eCKbrKbuAFXqz9BEoYTVvQzM_GWTI46-QI2ycbyGWZfiHQCzx8wancqHUGiUDKZiO35BmuENE1Sl5oLSn4rm4GFjoOVQ1b5DDBdK10z1ISh_T1KvnW-QzO9_dL2gQFzx-XFKgrIVCIR5QBIZU820mQYULCOy-axL5lCsnZKwrvnFnw6DpmoisJVemWqZs73CO83shwxUhamQ73uobQyQ8mP4SOZfKj-u3EQjS9RopGztgZN5GmgR3ZUR0py7KfiqT6yj9B8VrFmrmxEz82sWx_5EfWW15d5qMXTOxunxDf4QTdQOM4dmfXVs1Gvm29D53G7siKOtA1lGgPj1fgQ-Q1wNgPYjt4F3iJ182yWM05S2qgO_NjvwEGUzueOO8CvYntjasMFWfNYb4BT3THsH6ewCJHiXp_sJAXE31R_-vSyGCYwaHuOPiIEoR3CEQcpViCD0wikHG2BYsizwlGfGn8e-NtW8pd54uEuPjmUjQm6mnpJKNNC65mAJVgWhwV7obVziSCJCmIai9QQwNMhGAqeYlSEDFxE6N0dbpF7Bl_BUz_yyHmYP4X2GO5AS8QU4kopAkqMW2K-2OK9QuQrGnSi8pHT6Q2xuvUwZEuYnF5-jREEepugkzh5_CoG9KmjH5tMDlRD9ibbJ7VDMUEy6PujWo_ShXgtxtCoAAzqgdtf4Sx2u9WIgCkaZ2rAEMw_zRvez38gGrbp1OduD4Qhis10pLN2_yf6IapBv0-O6jQFJI_l8b5fAty-kFPoskWfKZqsIMvkKsteXxDcH-a4H1t7kKmBhjiQ5YjCv5n27qvAR2B4fAPha2WdrVs1qXwfWlUvVka33UV9a5T7X5g5YZT625b9yrdr-jVhKHeZR1US_eyHFdLp7Kuve3K_KEb5R8kyjB-N616w-1WU9_hmxmi63JuJp_uRT3xW7LTL7v9stcv-_3yqDk6W3LQL4_75Yd-2bbe0e36yGjLTr_s9stefUwYprFFfAtxaoQno_y6Ul9gKcpgQaRxNg1YSLY40sQIy68Qo8hTBXzEUM3j7UU8_wdDqhUM" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 LI-200-060_Issue_Return_Notice_for_Repair — LI-200-060_Issue_Return_Notice_for_Repair

**Swim Lanes**: Buyer · Factory Engineer · Maintenance Planner · PR Requestor · Warehouse Clerk | **Tasks**: 24 | **Gateways**: 9

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
    subgraph Buyer
        n8["fa:fa-user Create Rework or Repair PO"]
        n9["fa:fa-user Issue Rework or Repair PO to Supplier"]
        n10["fa:fa-user Create Rework or Repair PO"]
        n11["fa:fa-user Issue Rework or Repair PO to Supplier"]
        n12["fa:fa-user Create Text PO"]
        n13["fa:fa-user Create Rework or Repair PO"]
        n19[["fa:fa-cog Create Return PO"]]
        n20[["fa:fa-cog Create Return PO"]]
        n29["Return Material to Supplier for Rework"]
        n30["Transmit Order to Supplier"]
        n39{{"fa:fa-code-branch exclusiveGateway"}}
        n43{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Factory Engineer
        n24["Perform Repair or Rework In-house"]
        n31["Bill Supplier for Repair"]
        n32["Order Sent to Supplier"]
        n40{{"fa:fa-code-branch Inhouse/External?"}}
    end
    subgraph Maintenance Planner
        n1["fa:fa-user Develop Corrective Action Plan"]
        n2["fa:fa-user Create Rework or Repair Order (Refurbishment Order)"]
        n3["fa:fa-user Create PM Order With Reason Code"]
        n16[["fa:fa-cog Execute Custom Program as Background Job"]]
        n23["Identify Failure Details"]
        n26["Return Material to Supplier for Repair"]
        n27["Scrap Material"]
        n33["Determine Material Disposition"]
        n42{{"fa:fa-arrows-alt Return/ Scrap/ Rework/ Repair?"}}
    end
    subgraph PR Requestor
        n4["fa:fa-user Create Rework or Repair PR"]
        n5["fa:fa-user Create Rework or Repair PR"]
        n6["fa:fa-user Create Service PR for Rework or Repair"]
        n7["fa:fa-user Create Service PO for Rework or Repair"]
        n17[["fa:fa-cog Create Rework or Repair PR"]]
        n18[["fa:fa-cog Create Text PR for Services"]]
        n28["Enable Payment"]
        n34["Order Received"]
        n35{{"fa:fa-code-branch Remote/ Onsite"}}
        n36{{"fa:fa-code-branch exclusiveGateway"}}
        n37{{"fa:fa-code-branch Original or Third-party Supplier?"}}
        n38{{"fa:fa-code-branch Reason Code?"}}
    end
    subgraph Warehouse Clerk
        n14["fa:fa-user Create Inbound Delivery and Replicate to EWM"]
        n15["fa:fa-user Post Goods Receipt for Text PO"]
        n21[["fa:fa-cog Update PM Order with GR Status"]]
        n22[["fa:fa-cog Update PM Order with No GR Status"]]
        n25(["fa:fa-stop PM Order Updated"])
        n41{{"fa:fa-code-branch Material Accepted in EWM and Posted GR?"}}
    end
    n33 --> n23
    n23 --> n1
    n1 --> n42
    n42 -->|"Rework/Repair"| n2
    n40 -->|"Inhouse"| n24
    n24 --> n31
    n7 --> n36
    n8 --> n9
    n36 --> n28
    n11 --> n29
    n35 -->|"Onsite"| n5
    n10 --> n11
    n42 -->|"Scrap"| n27
    n42 -->|"Return"| n26
    n4 --> n10
    n5 --> n8
    n9 --> n36
    n6 --> n7
    n35 -->|"Remote"| n4
    n32 --> n37
    n37 -->|"Third Party Supplier"| n34
    n37 -->|"Original Supplier"| n35
    n34 --> n6
    n40 -->|"External"| n32
    n42 --> n40
    n2 --> n3
    n3 --> n14
    n14 --> n41
    n41 -->|"Yes"| n21
    n41 -->|"No"| n22
    n22 --> n25
    n12 --> n43
    n13 --> n39
    n43 --> n15
    n15 --> n39
    n39 --> n30
    n20 --> n18
    n17 --> n13
    n18 --> n12
    n19 --> n39
    n43 --> n39
    n16 --> n38
    n21 --> n16
    n38 -->|"Reason Codes: 
1. REPAIR
2. CLEAN HOT-QUENCH"| n17
    n38 -->|"Reason Code: 
1. RETURN"| n19
    n38 -->|"Reason Code: 
1. DECONTAMINATE SCRAP"| n20
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
    class n20 serviceTask
    class n21 serviceTask
    class n22 serviceTask
    class n25 endEvt
    class n26 startEvt
    class n27 startEvt
    class n28 startEvt
    class n29 startEvt
    class n30 startEvt
    class n31 startEvt
    class n32 startEvt
    class n33 startEvt
    class n34 startEvt
    class n35 gateway
    class n36 gateway
    class n37 gateway
    class n38 gateway
    class n39 gateway
    class n40 gateway
    class n41 gateway
    class n42 gateway
    class n43 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWFtzokgU_itdTKWcrdIJzUXUh50yiDNuTRJXzaa2JvvQYhOpILgNJLoZ__uehm4UAtlsJg9J-PpcvnPl8qy40YoqA-Xs7NkP_WSAnlvJmm5oa4BaSxLTVhvlwB-E-WQZ0LjFZbwoTOb-P5kYNrY7LsaxMdn4wZ6jc3ofUXQzaaMhKAZtFJMw7sSU-V6r3doyf0PY3o6CiHHpD7TnqV7mTRxdRGxF2VFAVS3smqAa-CE9wrplWMaY68XUjcJVyahnej3PbR04uSB6cteEJRn9NKaXZHfrr5I1XHskiCnIrJNN8I0sacBjTFjKMTdljzIZfsz9hJCw-Za4fngPuKECxEj4cIRM9XBAh7Ozu7Bwir7N7kIEP25A4nhEPRQnADuPCfL8IBh8MOzh2FTbccKiBzr4oDnWSNfaLo9kAKGrbZ7czhP179fJYBkFKyHaeeIxDLTtrs12A01tsz38rvii4eroye5qPa1XeLqwsI1t6cnzvJ_yBHllCxI_CF-OPtbGo8IXNrumrb60J8McGdYQV_NE2aPv0hOj4_FYd46pcromVpuNXoz1rmpXjN6ThD6R_dFg3zYKg2PTGmOr0WDur8oyXU5Z5EqDumOOzcKgdYHHQ63RoDHERk8wBDv3jGzX6CLdU5Zj_Cfsfb9TPDLwSIenGNmMQghoRp8i9oAiBv9tic_Q9PpO-etErV9Wm8RxWquFkgjN0-028MFryQJW3-cZ4593rdW6XtBd8tKd_k6a_e-FohvdH_WSlIW59Km4pv4_cZ5_cXgJgnwRnsaLvIwZ51impfOsL2CtxBs_Qdd8EzbnSe8_Px9JrWhnCYruGtGdG6Sx_0i_5O1-pxwOJ2qGflQjjEVPcYcECdoSRoKABi-UYItUmnRM3CRie-SE97CTS_2qGRDAlDIIcCNzX8SKJmFnHUGdKnHwlrmACarmh2tXRHlr5GmZ0zBpzo2h1udmEmYEzp0dVCUkwefX4rwkfpjQEBQpmgYkDEuhVhp9RB9pEG2RHTFG3QTSj4bwJwoz1TI77W1Nmwf6cUa9lC39eL3hIWfgL5W01NqbXgoLt36yBpskBjI2JKMyCt1ybzs76qagbqdxEm0Q7DfIxgaRGF0Q9-GeRWm4Qr9Fy2rPcxKTFVD0vT20iB-kjEJWEvgvroTffdN4vCy_ZoHi3IXiFHqVRHAS4JOyDXTm0fjIj7dR7PNyVPpEqx2GnNw5ynydi8qcC06v9sx0BlJ_pxRyd9osxhvX1KxMz3yfWrdWbZ7fUjnF4_5BDam2Xjdx_QYT2GpYmnXsS4q9WsX8BpCTF0TiahPy-6UT8udVNCV7PjCVBjGKBTKjLoUpXVUEzPrFMaObKKHn6DqENqKVlap337WJdate7Zr5sFihbSHQxdpnqw4s52RfzMfnqp1eE-di5F_t2VvCaLYWkR1QuCWdVKK-byfhMtsCIxpAcHAnIHAB1Qx8lx_DKDu3l5VmqLTyNIoT9CWKVnFeiG2S1bX2Jq_hcj_cbFel_fbE99uXGZonJElftIT2BuWrqFnf_Fjow1Bvj5q5Jd4_v5xOOq4vRrGLhq5Lt6CH_JCnKcsdzwYgX2Z1dYKthjqdX_mKFYAmAPHQHOL80tDEtaFx4AdfstniktP5A1SliCpExB0xPzSkAyO3qEsPlrjuiuteft2XDLuCYU8yEpS0QsIU_uQAgTtTCqsiHFzln-3fnJr1Mja-o_NDSUvQxuI5PTTza8mqX4lCsLaqHPNhz0zLjOia0C2ELSGcTShsm9MJzVR1oypaDHZZTuZBF_S71RrJp5VcvFxlLiarJihKcyIZkgYW5o0izVjY_5MvUp7HFydXUX4gfWrCh1bUTpKQXrFwq8vKG5JHoWJWJHRZlyIQ2RBFO4n-w4UX0YBYEsP9BrcFgEW1dWlUEz2KZb71XlH_YnHGA3QX4k9o5kyHE3iZ1z4h-5szvEJfrxed32-cK_trliFsvWKksLG4mV3l4v3_Fh859vXVYng5uRouHDS3Z8NpXozTt1A-_PLtuwRr9bBeDxv1sFkPd-thqx7u1cP9ehiWQT3eECduCBQ3RIobQsUNsULbnHyLKB9ZzUe95qN-4xH0feMRbj7Smo9M8RGojHaLz1Bl3GrAew14vx7X1QYcN-BaA6434EYDbsovPGW4Ww9b9XCvHu7XwrCia2FcD2v1sC5hpa1s4N2F-Ctl8Kxk31-VgbKiHkmDRDm0FZIm0Xwfusog-06ppNkzyMgn_B0tBw__Ak4Iv7Y=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 LI-200-080_Repair_Material — LI-200-080_Repair_Material

**Swim Lanes**: Intel Engineer · Maintenance Planner · Quality Analyst · Warehouse Clerk | **Tasks**: 6 | **Gateways**: 6

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
    subgraph Intel Engineer
        n6["Perform Repair or Rework Inhouse"]
    end
    subgraph Maintenance Planner
        n5["fa:fa-user Complete Rework or Repair Order"]
        n11["Bill Supplier for Rework"]
        n12["Receive Materials and Services - PTP"]
        n18{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Quality Analyst
        n4["fa:fa-user Inspect Quality Post Rework or Repair"]
        n8(["fa:fa-play Material Sent after Rework/Repair"])
        n10["Return Material to Supplier"]
        n16{{"fa:fa-code-branch Quality meets the standard?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Warehouse Clerk
        n1["fa:fa-user Issue Materials to Rework or Repair Order"]
        n2["fa:fa-user Send Material to Supplier for Repair/ Rework"]
        n3["fa:fa-user Create Goods Receipt"]
        n7(["fa:fa-play Planning Started for Rework or Repair"])
        n9(["fa:fa-stop Material Sent"])
        n13{{"fa:fa-code-branch Remote/ Onsite?"}}
        n14{{"fa:fa-code-branch External / Inhouse"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n7 --> n1
    n1 --> n14
    n17 --> n4
    n4 --> n16
    n16 -->|"No"| n10
    n3 --> n5
    n5 --> n18
    n18 --> n12
    n18 --> n11
    n6 --> n17
    n16 -->|"Yes"| n3
    n14 -->|"Inhouse"| n6
    n13 -->|"Remote"| n2
    n8 --> n17
    n15 --> n9
    n2 --> n15
    n13 -->|"Onsite"| n15
    n14 -->|"External"| n13
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n7 startEvt
    class n8 startEvt
    class n9 endEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVluP4jYU_itWRiNaCTS5EoaHVgxDViPthQ7brqrSB5OcDNEYO7KdAcry32vnSjJBWrV5QPg753znmhOfjJBFYEyN29tTQhM5RaeB3MIOBlM02GABgyEqgD8wT_CGgBhonZhRuUr-ydUsNz1oNY0FeJeQo0ZX8MIA_f40RDNlSIZIYCpGAngSD4aDlCc7zI9zRhjX2jcwic0491aKHhiPgDcKpulboadMSUKhgR3f9d1A2wkIGY1apLEXT-JwcNbBEbYPt5jLPPxMwCd8-JZEcqvOMSYClM5W7shHvAGic5Q801iY8beqGInQfqgq2CrFYUJfFO6aCuKYvjaQZ57P6Hx7u6a1U_TxeU2RekKChXiEGAmp4MWbRHFCyPTGnc8CzxwKydkrTG_shf_o2MNQZzJVqZtDXdzRHpKXrZxuGIlK1dFe5zC108OQH6a2OeRH9dvxBTRqPM3H9sSe1J4efGtuzStPcRz_L0-qrvwrFq-lr4UT2MFj7cvyxt7cfM9Xpfno-jOrWyfgb0kIF6RBEDiLplSLsWeZ10kfAmdszjukL1jCHh8bwvu5WxMGnh9Y_lXCwl83ymyz5CysCJ2FF3g1of9gBTP7KqE7s9xJGaHieeE43aInKoGgBX1Rww68EOqHjv9aG0vgMeM79AwpTjhiXP3bM_6qrLZMtWBt_F1YqMZ3eD_hRDFTTENAS4IpbZF7ijzG0xiPdCPRnO1SAhIq-txR7vKLfjdrN7mtZSnjB5U_WmVpShJlH9eRdVRtpfoMISRvoCKSoBeEQJhGaFW0W6ARWn5ddswmp1MVH-ac7cUIE4lSzDEhQD4UTV0b5_O17H_LMEnkEc0oJkchL7jdduZPVKQQytpgyYR8V4V2dJOfaoqUqNmq8lIpUYlwrE4lw11t_vNldmZeFJlx2thKVlezU4txUwu9wUcbtYPCJsMdgBRILW69aPRWjH5tClMw-P0McAhJJlRnfqCe3zCHfOLQnIDq8gV7p55CZJetVnn9yEzZbRZVyai3NuWkaZq73olzOoPNQbGgD4xFAuWDmMq2gd_pZv6uqPWOVnpvQ3Qx262BuOzofcMhJEvbE9HtvtPfjWfYMQl36AsViYR3PXT7rRYH5UnNOLprVkLb0PvPzac-Go1-URTl0SqPbnUu5dXZLeXjSj7WwPe18Zmtje967kuBUyh65dEr7SaV3aQE7C5QRTIuz37X058gcldOJXBLQV0cJazjc0phUfpcVrmcdD2UQd6XZ7uUe12uon1Fvl43iqpbhdi5-LTo6laf1BZs98NOP-z2w14_7Nd3kxY86Yfvy9tFO2qzX9myruD2FdypPtVt2O2HvX543A_7_fCkgo2hsQO-w0lkTE9GfgdW9-QIYpwRaZyHBs4kWx1paEzzu6KRpZGyfEywWo67Ajz_Cxfal0A=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 LI-200-090_Bill_Supplier_for_Repair — LI-200-090_Bill_Supplier_for_Repair

**Swim Lanes**: Invoicing Specialist · Procurement Buyer | **Tasks**: 5 | **Gateways**: 3

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
    subgraph Invoicing Specialist
        n5["fa:fa-user Receive Credit Note from Supplier"]
        n10["Process Receipts"]
    end
    subgraph Procurement Buyer
        n1["fa:fa-user Calculate the Associated Costs"]
        n2["fa:fa-user Rework or Repair PO with Maintenance Cost"]
        n3["fa:fa-user Rework or Repair PO 0$ to Receive Material"]
        n4["fa:fa-user Create Service PO to Supplier for Payment"]
        n6(["fa:fa-play Rework or Repair Liability Assessed"])
        n7["Enable Payment"]
        n8["Receive Materials and Services - PTP"]
        n9["Enable Payment"]
        n11{{"fa:fa-code-branch Rework or Repair Inhouse/External?"}}
        n12{{"fa:fa-code-branch Is Material Under Warranty?"}}
        n13{{"fa:fa-code-branch Is Material Under Warranty?"}}
        n14[["fa:fa-folder-open Receive Materials and Services - PTP"]]
    end
    n6 --> n1
    n1 --> n11
    n11 -->|"External Supplier"| n12
    n11 -->|"Inhouse"| n13
    n12 -->|"Yes"| n3
    n12 -->|"No"| n2
    n13 -->|"No"| n4
    n5 --> n10
    n4 --> n7
    n3 --> n8
    n2 --> n14
    n14 --> n9
    n13 -->|"Yes"| n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 startEvt
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqllm-P4jYQxr-Kle2KVgpq_hI2L1pBINJKu1d03PVUHX1hEgesDXZkO8tyHN-9Y0gChKyu0vEC4cczvxk_JJPsjYSnxAiN-_s9ZVSFaN9Ta7IhvRD1lliSnolOwt9YULzMiezpmIwzNaffjmG2V7zpMK3FeEPznVbnZMUJ-vxoohEk5iaSmMm-JIJmPbNXCLrBYhfxnAsdfUeGmZUdq1VbYy5SIs4BlhXYiQ-pOWXkLLuBF3ixzpMk4Sy9gmZ-NsyS3kE3l_NtssZCHdsvJXnGb19oqtawznAuCcSs1SZ_wkuS6zMqUWotKcVrbQaVug4Dw-YFTihbge5ZIAnMXs6Sbx0O6HB_v2BNUfT0ccEQfJIcSzkhGZIK5OmrQhnN8_DOi0axb5lSCf5CwjtnGkxcx0z0SUI4umVqc_tbQldrFS55nlah_a0-Q-gUb6Z4Cx3LFDv4btUiLD1XigbO0Bk2lcaBHdlRXSnLsp-qBL6KT1i-VLWmbuzEk6aW7Q_8yLrl1ceceMHIbvtExCtNyAU0jmN3erZqOvBt633oOHYHVtSCrrAiW7w7Ax8irwHGfhDbwbvAU712l-VyJnhSA92pH_sNMBjb8ch5F-iNbG9YdQiclcDFGj2yV0719YTmBUng_qFSnUL0h_lfF0aGwwz3tePoI0kIfSUoEiSlCn3giqBM8A2al0WRUyIWxr8X2bYF6bpfIuUpt1CyCYGrpdWMDi0FzACm0LjcAe6Cdd1JhPOkzMFeBEMDjaTk0LwiKYq4vKhxTHXah9hy8YK4_lVgKtDsL7Slao2eMWWKMMwScsRcU9wfU6xfkOKNSc_Qj55I1xivdQ5B9CHmp6tPQ4BQu4kywM_wThtyTRn82mCKHC6wm26eYIbSnKqd9gbsJykAfrsgBACYMj1ouysMYb99EokwS-teJeqj2afZddbDD6i2vd_XjesHQn8JIy1Z3_b_yNYcDPp9-galGc7_XBiHwyXI6QY9yqZb9JnBYEdfsIAttbshuD9N8L42_0IGA4yIPi8IQ__TtvZtwAao3_8DsNXSrpbN-ih8B4MrTy7uuu_akXZc5eFp1613nWr3HyKPOzcbH_hRb3Dute5Vul-1V40o5p3WQbV0T8thtXSq6DrbrsIf2lXqtvyLyae9qCf-lex0y2637HXLfrc8aB6dV3LQLQ-75Ydu2bbe0e36kXEtO92y2y179WPCMI0NERtMUyPcG8e3K3gDS0mGy1wZB9PApeLzHUuM8PgWYpRFCsAJxTCPNyfx8B97LRUM" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 LI-200-100_Issue_Waiver_Request — LI-200-100_Issue_Waiver_Request

**Swim Lanes**: Procurement Buyer · Warehouse Clerk | **Tasks**: 3 | **Gateways**: 3

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
    subgraph Procurement Buyer
        n2["Generate Waiver Request"]
        n3["Receive Approvals for the waiver Request"]
        n4["Repair Material"]
        n5["Transfer Material from Quality Inspection to Stock (IF)"]
        n6["Return Material to Supplier - PTP"]
        n7["Scrap Material"]
        n8["Rework Material"]
        n10{{"fa:fa-code-branch Approved?"}}
        n11{{"fa:fa-code-branch Return Material / Scrap Material?"}}
        n12{{"fa:fa-code-branch Repair/ Rework/ Accept ?"}}
    end
    subgraph Warehouse Clerk
        n1["fa:fa-user Identify Damaged Material"]
        n9["Determine Material Disposition"]
    end
    n9 --> n1
    n2 --> n3
    n3 --> n10
    n10 -->|"No"| n11
    n10 -->|"Yes"| n5
    n12 -->|"Accept"| n2
    n1 --> n12
    n12 -->|"Rework"| n8
    n12 -->|"Repair"| n4
    n11 -->|"Return Material"| n6
    n11 -->|"Scrap Material"| n7
    class n1 userTask
    class n4 startEvt
    class n5 startEvt
    class n6 startEvt
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
    class n10 gateway
    class n11 gateway
    class n12 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl2P6jYQ_StWVitaKWiTkBA2D61YINVK91bbZdtVdemDScZgEeLUdmApl__ecUj4WuhLeUD4zJlzZia2ydZKRApWZN3fb3nOdUS2LT2HJbQi0ppSBS2b7IE_qOR0moFqGQ4TuR7zfyqa6xcfhmawmC55tjHoGGYCyO_PNuljYmYTRXPVViA5a9mtQvIllZuByIQ07DvoMYdVbnXoScgU5JHgOKGbBJia8RyOcCf0Qz82eQoSkadnoixgPZa0dqa4TKyTOZW6Kr9U8JV-vPNUz3HNaKYAOXO9zL7QKWSmRy1LgyWlXDXD4Mr45DiwcUETns8Q9x2EJM0XRyhwdjuyu7-f5AdT8uV1khP8JBlVagiMKI3waKUJ41kW3fmDfhw4ttJSLCC680bhsOPZiekkwtYd2wy3vQY-m-toKrK0prbXpofIKz5s-RF5ji03-H3hBXl6dBp0vZ7XOzg9he7AHTROjLH_5YRzlW9ULWqvUSf24uHByw26wcD5rNe0OfTDvns5J5ArnsCJaBzHndFxVKNu4Dq3RZ_iTtcZXIjOqIY13RwFHwf-QTAOwtgNbwru_S6rLKcvUiSNYGcUxMFBMHxy4753U9Dvu36vrhB1ZpIWc2LUSonHLtfkqdyA3MfNJ_e-TaxfIAeJXZB3ylcgySv8XYLSE-uvE2IHia-QADJIvyikWOFGJ0xIgiearP8j068yC8ol-You5gCfEwIkvOG2VwyOFMKkWJLfSppxvSHPuSog0VzkRAsy1iJZkB-e4x_PhbqVky5lfpQx9LIoMo7abfLy9nKeEmLKOMEx3aitV0muhVzcILjOdjuxGI0YbZvrrz3FTpJ5PSNIf55Yu90p373Ov6z7gZyX9UnHu6VjJv1A9kU_kH6SQKHJSTqe4IsN8k4lzAWeNzLIQC5OXb41HuY0kucU9xBnGzKkSzqD9MZMHjFrCBhZ4vV6bGnIVSEUN0_xwD8Ukz-SdvsndKyX3n7ZqZedOlofFvxhgO8T61cxsb6bsV4G_gRVRYIm4NWB_USqmNfEanXvkrufYsXtfY6ZSVcxv4m5h9jZ06xI3UvS5b5DTnhyF5iymjvwDPYPF_4ZHFyHu9fh8Drcuw4_Xodx2PX1dw6712GvgS3bWuLuoDy1oq1VvRLga0MKjJaZtna2RUstxps8saLqr9MqixQzh5zihl3uwd2_xBqsZg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.9 LI-200-120_Reverse_Goods_Receipt_Against_Purchase_Order — LI-200-120_Reverse_Goods_Receipt_Against_Purchase_Order

**Swim Lanes**: Inventory Manager | **Tasks**: 6 | **Gateways**: 5

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
        n1["fa:fa-user Identify Material Document against PO"]
        n2["fa:fa-user Perform Goods Receipt"]
        n3["fa:fa-user Perform Goods Receipt to Blocked stock"]
        n4[["fa:fa-cog Post Material Document Cancellation (Mvt. Type 102)"]]
        n5["Move Material to Holding Location"]
        n6["Move Material to Holding Location"]
        n7(["fa:fa-stop GR Completed"])
        n8["Return Material to Supplier"]
        n9["Send Credit Memo to Supplier"]
        n10["Inspect Material for Damage (Prior to Receipt)"]
        n11["Check Material for Proper Quantity"]
        n12{{"fa:fa-code-branch Quantity and Quality Check Status?"}}
        n13{{"fa:fa-code-branch Is the Material Correct or Incorrect?"}}
        n14{{"fa:fa-code-branch Cancel the receipt?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17[["fa:fa-folder-open Determine Material Disposition"]]
    end
    n15 --> n8
    n1 --> n4
    n2 --> n7
    n5 --> n15
    n3 --> n6
    n4 --> n9
    n10 --> n16
    n11 --> n16
    n16 --> n12
    n6 --> n17
    n17 --> n14
    n12 -->|"Pass"| n2
    n12 -->|"Fail"| n13
    n14 -->|"No"| n1
    n14 -->|"Yes"| n15
    n13 -->|"Correct Material"| n3
    n13 -->|"Incorrect Material"| n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n7 endEvt
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVltvq0YQ_isrosiJhCuuxuGhVYJNaumkdeO0VXXch_Wy2KvALloWJ66P_3sHc7EhjtQLDzbzzTffzM4OLHuNiIhqvnZ9vWecKR_tB2pDUzrw0WCFczrQUQX8hiXDq4Tmg5ITC64W7K8jzXSy95JWYiFOWbIr0QVdC4p-nenoHgITHeWY58OcShYP9EEmWYrlLhCJkCX7io5jIz5mq10PQkZUngiG4ZnEhdCEcXqCbc_xnLCMyykRPOqIxm48jsngUBaXiDeywVIdyy9y-oTff2eR2oAd4ySnwNmoNPmCVzQp16hkUWKkkNumGSwv83Bo2CLDhPE14I4BkMT89QS5xuGADtfXS94mRS-TJUdwkQTn-YTGKFcAT7cKxSxJ_CsnuA9dQ8-VFK_Uv7Km3sS2dFKuxIelG3rZ3OEbZeuN8lciiWrq8K1cg29l77p89y1Dlzv47eWiPDplCkbW2Bq3mR48MzCDJlMcx_8rE_RVvuD8tc41tUMrnLS5THfkBsZHvWaZE8e7N_t9onLLCD0TDcPQnp5aNR25pvG56ENoj4ygJ7rGir7h3UnwLnBawdD1QtP7VLDK16-yWM2lII2gPXVDtxX0Hszw3vpU0Lk3nXFdIeisJc42aMa3lCshd-gJc7ymsvKXFze_LrUY-zEelu1GswiYLC6ZipaPGpoIUqQAIrzGjOcKzX9ean-eKVhdhTmVsZApehQiytEzJZRlqhth_4MIpAR6SAR5pRGMN_x3JZyvrQYRazQXUNjHkgPMCU0SrJjg6OZpq75DL7uMItOwbkHvXNAFvSexpScVKOBHmFh4DNEXQY4a3RpG_z7Eu2nLhkVl6PEZBSLNEqpoBMzbM-oYmM9UFZJ39BdFliUMtrCjewfkBTyZKJA0YtAKmorP2aYB9BnPM0rOugZ7gCY4hflAN3PJwAKBejduewLl1AQbSl674TC2GWzoLwWGIVK7XpC135_2LKLDFbzpyKZlIwz1g5GU95X4QmFV5D8stcPhXMi-LDTLERwup4oCIWW5QihsxkllfNByLmtVk3PUk1ULPkS6lyPpO0mKnG3pY_Ve6IeN_luYdxr4GEaMyiG0mqMJTI5M4RA7m36WZyJn9fDVOwCzUd1A3Wg4_B7mq7Er06lNqzK92qzJplvbdmWPatOpzLtGy6jpjd80-8CoBqwaaOwmoenVQFOQeazo21Kbw-txqX2DEvueELPk6DHtxuXUrp9E5ejjf9BKq12YadeeZmqafh5pdp_VDlSX5569ysvWNkdYB7Yuw_Zl2Dk_tToerz6LO-C4_RjowHeXYdiwy7j5CW41x10Xti_DzmXYvQyPLsNecyBqupbCsGMWaf5eO35HwrdmRGNcJEo76BoulFjsONH84_eWVmQRCE4YhmMwrcDD3_gLW50=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.10 LI-200-130_Send_Credit_Memo_to_Supplier — LI-200-130_Send_Credit_Memo_to_Supplier

**Swim Lanes**: Accounts Payable Accountant | **Tasks**: 8 | **Gateways**: 4

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
    subgraph Accounts Payable Accountant
        n1["fa:fa-user Process Invoices in Read soft"]
        n2["fa:fa-user Reject Invoice"]
        n3["fa:fa-user Receive Supplier Submitted credit memo info in Boundary Apps"]
        n4["fa:fa-user Process Credit memo info in Read Soft"]
        n5["fa:fa-user Receive Supplier Submitted credit memo info in Boundary Apps"]
        n6["fa:fa-user Process Credit memo info in Read Soft"]
        n7[["fa:fa-cog Post Credit Memo"]]
        n8[["fa:fa-cog Post Credit Memo"]]
        n9(["fa:fa-play Credit Memo Process Initiated"])
        n10(["fa:fa-stop No Credit Memo"])
        n11(["fa:fa-stop Credit memo Linked to Invoice"])
        n12(["fa:fa-stop Credit memo will be cleared in Next Payment Run"])
        n13(["fa:fa-stop Refund Requested"])
        n14{{"fa:fa-code-branch Business Activity"}}
        n15{{"fa:fa-code-branch Scenario?"}}
        n16{{"fa:fa-code-branch Scenario?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n14 -->|"Goods Returned to Supplier"| n15
    n1 --> n2
    n2 --> n10
    n15 -->|"Invoice Posted- 
Not Paid"| n3
    n3 --> n4
    n4 --> n7
    n7 --> n11
    n5 --> n6
    n6 --> n8
    n8 --> n12
    n17 --> n5
    n15 -->|"Invoice Paid"| n17
    n9 --> n14
    n15 -->|"Invoice is not
posted in SAP"| n1
    n16 -->|"Not Continuing the 
business with Supplier"| n13
    n14 -->|"Over Paid to Supplier"| n16
    n16 -->|"Continuing the Business 
with Supplier"| n17
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 startEvt
    class n10 endEvt
    class n11 endEvt
    class n12 endEvt
    class n13 endEvt
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNq1VluPozYY_SsWq1FaiUjcyfDQKjdWK-3Ojibb9mHTBwdM4g6xKTa5NJv_3s8BEmBIpdWqeUjiwznnu9jYPmkRj4kWaA8PJ8qoDNBpIDdkSwYBGqywIAMdlcDvOKd4lRIxUJyEM7mg_1xoppMdFE1hId7S9KjQBVlzgn77oKMxCFMdCczEUJCcJgN9kOV0i_PjlKc8V-x3ZJQYySVa9WjC85jkN4Jh-GbkgjSljNxg23d8J1Q6QSLO4pZp4iajJBqcVXIp30cbnMtL-oUgn_DhDxrLDYwTnAoCnI3cph_xiqSqRpkXCouKfFc3gwoVh0HDFhmOKFsD7hgA5Zi93iDXOJ_R-eFhya5B0ZfZkiH4RCkWYkYSJCTA851ECU3T4J0zHYeuoQuZ81cSvLPm_sy29EhVEkDphq6aO9wTut7IYMXTuKIO96qGwMoOen4ILEPPj_DdiUVYfIs09ayRNbpGmvjm1JzWkZIk-aFI0Nf8CxavVay5HVrh7BrLdD13arz1q8ucOf7Y7PaJ5DsakYZpGIb2_Naqueeaxn3TSWh7xrRjusaS7PHxZvg4da6GoeuHpn_XsIzXzbJYPec8qg3tuRu6V0N_YoZj666hMzadUZUh-KxznG3QOIp4waRAz_io3roawEyWTPVh5telluAgwUPVeKRSIEKgD2zHoWcCUYZeCI6R4Ilcan82lFZb-UL-IpGshW2q3aVGhO4IWhRZllIAFsVqS6UkMYpyElOJtmTLIXSivtAEslYvJRpnmWgbO_3ZT3tcLlUs3lTh_l-peT-cmv_1ahHxNXrmQtbyTyAHcpM9-i72409XdpbCMm4wG2uASgrLPAbtz80lY9zEQvIMPfFOpBbb7LCbHfhI2Su0VvLGummJrf8Q7-FNQSsCrxDBAKtOPpGDVOt9S5hELwXr2tkduxeSwATCz98FET2VOqfTrakxGa5gm442aFIIOEGgReNI0h2Vx6V2Pjd1br9uEREGZyD_tcv3vpPv9_PJIUohtR15X-5ONxns3-UfqAkNh798W2rvOY8FlC6LnJVzUC_6pfZN1VALFB9e92polUPTqB-7lV81g5eVR-IhWrInriaDxhc_u-Lbpd6phk459KuhX7lXezhzy7FXDb1yOKqGo4pd52ZWcvdubnU2Zh3wsbJw7kmoQIzDjpldylKLbDF-Lj1qiVdJVL1TOPooK-AYR3DngSas6rWyp3LTabHdnZPPO7VVQJJvp8PrRutEuq7JJeuJ5DdOGzWl9Snbgq1-2O6HnX7Y7Ye9fthvns6tJ6O7Tx6vN592UUZ1S2mjZi9q9aJ2L-rUh30bdvthrx_2a1jTtS3JtzDHWnDSLvdiuDvHJMFFKrWzruFC8sWRRVpwuT9qRRaDckYxHOvbEjz_C_G6owE=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.11 LI-200-140_Scrap_Material — LI-200-140_Scrap_Material

**Swim Lanes**: Buyer · Inventory Manager | **Tasks**: 7 | **Gateways**: 5

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
    subgraph Buyer
        n8(["fa:fa-play Receive Disposition"])
        n12(["fa:fa-stop Send Exemption Report"])
        n13(["fa:fa-stop Supplier Colab"])
        n16["Notify Warehouse of Disposition"]
        n19["Exemption Data Received"]
        n20["Scrap Data Received"]
    end
    subgraph Inventory Manager
        n1["fa:fa-user Generate Material Disposition Number"]
        n2["fa:fa-user Perform Goods Receipt"]
        n3["fa:fa-user Perform Goods Receipt to Blocked stock"]
        n4["fa:fa-user Perform Scrap Adjustment in SAP"]
        n5["Move Material to Holding Location"]
        n6["Move Material to Holding Location"]
        n7["Move Material to Secured Scrap Storage Area"]
        n9(["fa:fa-stop GR Completed"])
        n10(["fa:fa-stop Initiate Return to Vendor Process"])
        n11(["fa:fa-stop Scrap Adjustment Done"])
        n14["Notification Sent To Buyer"]
        n15["Notification Sent To Buyer"]
        n17["Inspect Material for Damage (Prior to Receipt)"]
        n18["Check Material for Proper Quantity"]
        n21{{"fa:fa-code-branch Quantity and Quality Check Status?"}}
        n22{{"fa:fa-code-branch Is the Material Correct or Incorrect?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n25{{"fa:fa-arrows-alt inclusiveGateway"}}
        n26[["fa:fa-folder-open Determine Material Disposition"]]
    end
    n25 --> n14
    n19 --> n12
    n8 --> n16
    n14 --> n19
    n23 --> n11
    n23 --> n15
    n15 --> n20
    n20 --> n13
    n2 --> n9
    n5 --> n10
    n3 --> n6
    n6 --> n25
    n1 --> n7
    n7 --> n4
    n4 --> n23
    n17 --> n24
    n18 --> n24
    n24 --> n21
    n21 -->|"Pass"| n2
    n21 -->|"Fail"| n22
    n22 -->|"Incorrect Material"| n5
    n22 -->|"Correct Material"| n3
    n25 --> n26
    n26 --> n1
    n16 --> n26
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n8 startEvt
    class n9 endEvt
    class n10 endEvt
    class n11 endEvt
    class n12 endEvt
    class n13 endEvt
    class n14 startEvt
    class n15 startEvt
    class n16 startEvt
    class n17 startEvt
    class n18 startEvt
    class n19 startEvt
    class n20 startEvt
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV1uP2jgU_itWqhGtBFLuAR52xS2zI3Wq2aHbPpR9MIkD3kniyHYYKOW_7zG5QDJhtd3lAfDn833n4mPHOWoBC4k21u7ujjSlcoyOPbklCemNUW-NBen1UQF8wZzidUxET9lELJVL-v1sZtjZXpkpzMcJjQ8KXZINI-iPhz6aADHuI4FTMRCE06jX72WcJpgfZixmXFm_I8NIj87eyqkp4yHhFwNd94zAAWpMU3KBLc_2bF_xBAlYGjZEIycaRkHvpIKL2WuwxVyew88FecT7rzSUWxhHOBYEbLYyiT_iNYlVjpLnCgtyvquKQYXyk0LBlhkOaLoB3NYB4jh9uUCOfjqh093dKq2dos_zVYrgE8RYiDmJkJAAL3YSRTSOx-_s2cR39L6QnL2Q8Ttz4c0tsx-oTMaQut5XxR28ErrZyvGaxWFpOnhVOYzNbN_n-7Gp9_kBvlu-SBpePM1cc2gOa09Tz5gZs8pTFEX_yxPUlX_G4qX0tbB805_XvgzHdWb6W70qzbntTYx2nQjf0YBcifq-by0upVq4jqHfFp36lqvPWqIbLMkrPlwERzO7FvQdzze8m4KFv3aU-fqJs6AStBaO79SC3tTwJ-ZNQXti2MMyQtDZcJxt0TQ_EF5g6pMO339baREeR3iQxRD5MwkI3RE0pyJjgkrK0pX254crhmFeKEKyDC2hDdBiT5JMWYNCxrhsk6w2Kc-ymBKOYFPhddvaBeNPTNLogL5iTrYM1h-xqBXVNWMEjEsMcyxxlUrYtDR1sFwGUIwbVpBNq2YP6Y6kkvEDesQp3jTqZ9RpqRZF9yQlHJoALCVRx9N1yOhTnqyB3YynKfBEeMR4gu4ZC0URXCabDOtfMJBkaBqz4IWEcCLAb1PC7pYoyjIJ_8qFTCBlRFO0nDw1uQ5wH9nuKkXw9RvsZzik0EcW4Ler4_48xeuiLAmcmpBREecSlgRWAx4DBDfJo1az3T9DmyVZTOR5nRutprdsH-BhRdUKPhOZ81S5_QItwaBKsBGJEG0Bo93Z7SLOWUraJLtqcFokrzYRHOas3J_N3nZ-xlgV7iEVGQnkpXawutDtiarW-ydOYQRpla3yoSUwBIHZlgQvTTpkn0Gr_J7jVFJ5aDWxcTxWRVDP_cEanlzBtrZGGI4IGMTqfyG-lFjm4teVdjpdC5ndQg8CwWXhEtGMca4yhMAe0qAYvNGyurXIPohzAXv-vjit2zT7v9GcCw1zzl7FAMdqB_0zy_1Wd08EG4LwAZQZDjBoVZ7AhaTzIIHitw8r8I8Gg19Ua5WAMSoBswSG5ditDOwSGFUSVgkYbcCpKKWT6vkMf0oLqwKKcSVZBVXZl4JVCG4pV-sXY68cesWwyqiM16x8GeW8Wac8bAFmRakzOnv4sdKesNrJPwBpz_iYxsVMPWWWU3Wr1atyNnTadrMuK6u1UGZVBLOsQhWj4TYNzpcBVZvqEtSAzW7Y6obtbnhYXxsb8Ki84TXj0DtRoxM1O1GrE7W7g4Ce68bdG7h3A7-RJOyTThxauxs3qmteEza7Yasbtrthpxt2q4ug1tcSOBgwDbXxUTu_P8E7VkginMdSO_U1nEu2PKSBNj6_Z2h5FoLgnGK4yiQFePoblg0-eg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.12 LI-200-150_Notify_Supplier — LI-200-150_Notify_Supplier

**Swim Lanes**: Procurement Buyer · Warehouse Clerk | **Tasks**: 3 | **Gateways**: 5

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
    subgraph Procurement Buyer
        n2["fa:fa-user Notify Supplier for Material Disposition"]
        n3["fa:fa-user Notify Warehouse to Accept Material"]
        n6["Receive Materials and Services - PTP"]
        n7["Return Material to Supplier - PTP"]
        n8["Scrap Material"]
        n9["Communication Sent"]
        n10["Supplier Agreement Received"]
        n12{{"fa:fa-code-branch Accept Material?"}}
        n13{{"fa:fa-code-branch Return?"}}
        n14{{"fa:fa-code-branch Waiver Approved and Created?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Warehouse Clerk
        n1["fa:fa-user Notify Procurement for Discrepancies"]
        n4(["fa:fa-play Discrepant Material Identified"])
        n5(["fa:fa-stop Material Received into Warehouse"])
        n11{{"fa:fa-code-branch Any Discrepancies Found?"}}
    end
    n4 --> n1
    n1 --> n11
    n11 -->|"No"| n5
    n11 -->|"Yes"| n2
    n3 --> n6
    n2 --> n9
    n13 -->|"Yes"| n7
    n13 -->|"No"| n8
    n9 --> n10
    n10 --> n12
    n12 -->|"Yes"| n14
    n12 -->|"No"| n15
    n14 -->|"Yes"| n3
    n15 --> n13
    n14 -->|"No"| n15
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
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl2P4jYU_StWRiNaKUj5JJCHVkwg1Uq7q9Gy7agqfTCJA9YEO7KdGViW_97rkA_IhKfygORz7zn33mM7yclIeEqM0Hh8PFFGVYhOI7UjezIK0WiDJRmZ6AL8hQXFm5zIkc7JOFMr-qNKs73ioNM0FuM9zY8aXZEtJ-jPTyaaAzE3kcRMjiURNBuZo0LQPRbHiOdc6OwHMs2srKpWh564SInoEiwrsBMfqDllpIPdwAu8WPMkSThLb0QzP5tmyeism8v5e7LDQlXtl5J8wYcXmqodrDOcSwI5O7XPP-MNyfWMSpQaS0rx1phBpa7DwLBVgRPKtoB7FkACs9cO8q3zGZ0fH9esLYo-f1szBL8kx1IuSIakAnj5plBG8zx88KJ57FumVIK_kvDBWQYL1zETPUkIo1umNnf8Tuh2p8INz9M6dfyuZwid4mCKQ-hYpjjCf68WYWlXKZo4U2faVnoK7MiOmkpZlv2vSuCr-I7la11r6cZOvGhr2f7Ej6yPes2YCy-Y232fiHijCbkSjePYXXZWLSe-bd0XfYrdiRX1RLdYkXd87ARnkdcKxn4Q28FdwUu9fpfl5lnwpBF0l37st4LBkx3PnbuC3tz2pnWHoLMVuNghrVYKuHZMoafySMQlrn_M-WdtZDjM8Fjbjb5yRbMjWpVFkVNYZ1ygLzCgvnVoQWXBJVWUs7Xx75WIOyjyggXZcUCQ4mieJKRQrdYtfwL8byQh9I20GRJhlqLVZcckGqPn78-3rKBiqVKwrkWo1PY-QJkCZZWAKXcamUE84vt9yWiC9ZzQAFO3ObalRZoi860gF2frAdJetnM6Nebop-N4A_c72fX9-H1tnM_XNHeYdpn3Q7Y3nP2CoSHosSgEh84qRyNBoGb6QcIfliCHJC8lyPxxOeYdDR4EvXPWbXiUE_F6rT54QK7PpT5ocL4SQQqoS4m8tdH7pVUocrhsbWpnIfqUghDNaLUFv16R_Y4sFe_2vt0yRBkcnLb9Ht2272whO962jGJesmtnW4uYh8bj30CqXtr1sl1XwM-18ZWvjZ_QcR__WxsCAacOuBeBSb10LstZQ3N7tKAfqOtMa3xW92M1eVYNNPVsp6doe_1ILWm3vXs9itsE_Frc7Wf2JKonojareRPcwM4w7A7DXvuSvIH9-n12A06Gc4NheDoMz4ZhcHYYt5sXyS3sDMPuMOwNw34DG6axJ2KPaWqEJ6P6FIPPtZRkuMyVcTYNXCq-OrLECKtPFqMsUmAuKIYbvr-A5_8AjsIgXA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Procurement Buyer | LI-200-010_Determine_Material_Disposition, LI-200-050_Bill_Supplier_for_Rework, LI-200-090_Bill_Supplier_for_Repair, LI-200-100_Issue_Waiver_Request, LI-200-150_Notify_Supplier | |
| Warehouse Clerk | LI-200-010_Determine_Material_Disposition, LI-200-020_Issue_Return_Notice_for_Rework, LI-200-040_Rework_Material, LI-200-060_Issue_Return_Notice_for_Repair, LI-200-080_Repair_Material, LI-200-100_Issue_Waiver_Request, LI-200-150_Notify_Supplier | |
| Buyer | LI-200-020_Issue_Return_Notice_for_Rework, LI-200-060_Issue_Return_Notice_for_Repair, LI-200-140_Scrap_Material,  | |
| Factory Engineer | LI-200-020_Issue_Return_Notice_for_Rework, LI-200-060_Issue_Return_Notice_for_Repair,  | |
| Maintenance Planner | LI-200-020_Issue_Return_Notice_for_Rework, LI-200-040_Rework_Material, LI-200-060_Issue_Return_Notice_for_Repair, LI-200-080_Repair_Material,  | |
| PR Requestor | LI-200-020_Issue_Return_Notice_for_Rework, LI-200-060_Issue_Return_Notice_for_Repair,  | |
| Intel Engineer | LI-200-040_Rework_Material, LI-200-080_Repair_Material,  | |
| Quality Analyst | LI-200-040_Rework_Material, LI-200-080_Repair_Material,  | |
| Invoicing Specialist | LI-200-050_Bill_Supplier_for_Rework, LI-200-090_Bill_Supplier_for_Repair,  | |
| Inventory Manager | LI-200-120_Reverse_Goods_Receipt_Against_Purchase_Order, LI-200-140_Scrap_Material,  | |
| Accounts Payable Accountant | LI-200-130_Send_Credit_Memo_to_Supplier,  | |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for LI-200. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for LI-200.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for LI-200.

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

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
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

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for LI-200:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for LI-200:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-200 — Determine Discrepant Material Disposition</span></div>
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
*LI-200 — Architecture Document (TOGAF BDAT) · Procure To Pay · Generated: March 2026*

