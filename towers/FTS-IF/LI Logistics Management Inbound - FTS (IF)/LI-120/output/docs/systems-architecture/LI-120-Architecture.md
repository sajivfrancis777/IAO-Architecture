<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">LI-120 — Receive Materials and Services - FTS (IF)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Forecast to Stock (IF) (FTS-IF) Tower<br/>
  Capability LI-120 · LI Logistics Management Inbound - FTS (IF)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **LI-120 Receive Materials and Services - FTS (IF)** within the IAO program. It includes 8 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Forecast to Stock (IF) (FTS-IF) |
| **Process Group** | LI Logistics Management Inbound - FTS (IF) |
| **Capability** | LI-120 - Receive Materials and Services - FTS (IF) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 2 Reports, 18 Interfaces, 3 Conversions, 19 Enhancements, 9 Forms, 3 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Forecast to Stock (IF) |
| **L1 Process** | LI Logistics Management Inbound - FTS (IF) |
| **L2 Capability** | LI-120 - Receive Materials and Services - FTS (IF) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Intel Foundry Supply Chain Integration | Integrate Intel Foundry manufacturing and logistics into unified S/4 HANA supply chain | IDM 2.0 Foundry Enablement | High |
| 2 | Warehouse & Logistics Modernization | Modernize warehouse management and shipping processes with EWM integration | Supply Chain Digital Transformation | High |
| 3 | Production Planning Optimization | Enable MRP-driven production planning with real-time material availability | Manufacturing Excellence | Medium |
| 4 | LI-120 Process Migration | Migrate Receive Materials and Services - FTS (IF) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Supply Chain (Intel Foundry) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Fulfillment Lead Time | < 48 hours | Time from production completion to shipment dispatch | 72 hours (legacy) | Logistics Manager |
| Inventory Accuracy | > 99.5% | Physical vs system inventory match rate | 97.8% (current) | Warehouse Manager |
| MRP Planning Cycle | < 4 hours | End-to-end MRP run including exception processing | 8 hours (legacy) | Planning Lead |
| LI-120 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **8 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for LI-120 Receive Materials and Services - FTS (IF).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | LI-120-040_Unload_Material_Received_-_FTS_(IF) | LI-120-040_Unload_Material_Received_-_FTS_(IF) | Warehouse Operator | 1 | 0 |
| 2 | LI-120-040_Unload_Material_Received_-_FTS_(IF)_(Copy) | LI-120-040_Unload_Material_Received_-_FTS_(IF)_(Copy) | Warehouse Operator | 1 | 0 |
| 3 | LI-120-060_Process_Damaged_Goods_-_FTS_(IF) | LI-120-060_Process_Damaged_Goods_-_FTS_(IF) | Warehouse Operator | 12 | 2 |
| 4 | LI-120-080_Receive_Material_Against_Advanced_Shipping_Notification_(ASN)_-_FTS_(IF) | LI-120-080_Receive_Material_Against_Advanced_Shipping_Notification_(ASN)_-_FTS_(IF) | Warehouse Operator | 9 | 1 |
| 5 | LI-120-170_Check_Material_for_Proper_Quantity_-_FTS_(IF) | LI-120-170_Check_Material_for_Proper_Quantity_-_FTS_(IF) | Warehouse Operator | 10 | 3 |
| 6 | LI-120-180_Move_Material_to_Holding_Location_-_FTS_(IF) | LI-120-180_Move_Material_to_Holding_Location_-_FTS_(IF) | Warehouse Operator | 3 | 1 |
| 7 | LI-120-190_Resolve_Discrepancies_-_FTS_(IF) | LI-120-190_Resolve_Discrepancies_-_FTS_(IF) | Warehouse Operator | 6 | 3 |
| 8 | LI-120-220_Receive_Actual_Count_Quantity_-_FTS_(IF) | LI-120-220_Receive_Actual_Count_Quantity_-_FTS_(IF) | Warehouse Operator | 1 | 0 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 LI-120-040_Unload_Material_Received_-_FTS_(IF) — LI-120-040_Unload_Material_Received_-_FTS_(IF)

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
        n1["Unload Material Received"]
        n2(["fa:fa-stop Goods Receipt Posted"])
        n3["Receive Material Against Advanced Shipping Notification (ASN)"]
    end
    n1 --> n2
    n3 --> n1
    class n2 endEvt
    class n3 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVMtu2zAQ_BVCgaEEkAE9LVeHAopsFQWaNKiT5lD3QFNLi4hMCiT9quF_L-l3XORUHQRxNDuzOyK1cYiowMmcTmfDONMZ2ri6hhm4GXInWIHroT3wE0uGJw0o13Ko4HrE_uxoQdyuLM1iJZ6xZm3REUwFoJevHspNYeMhhbnqKpCMup7bSjbDcl2IRkjLvoE-9enO7fDqXsgK5Jng-2lAElPaMA5nOErjNC5tnQIiePVOlCa0T4m7tc01YklqLPWu_bmCB7x6ZZWuzZriRoHh1HrWfMMTaOyMWs4tRuZycQyDKevDTWCjFhPGpwaPfQNJzN_OUOJvt2jb6Yz5yRQ9D8YcmYs0WKkBUKS0gYcLjShrmuwmLvIy8T2lpXiD7CYcpoMo9IidJDOj-54Nt7sENq11NhFNdaB2l3aGLGxXnlxloe_JtblfeQGvzk5FL-yH_ZPTfRoUQXF0opT-l5PJVT5j9XbwGkZlWA5OXkHSSwr_X73jmIM4zYPrnEAuGIEL0bIso-E5qmEvCfyPRe_LqOcXV6JTrGGJ12fBT0V8EiyTtAzSDwX3ftddzidPUpCjYDRMyuQkmN4HZR5-KBjnQdw_dGh0phK3NXrFEmph4kTfW5BYC7kn2IsHv8bOC28ErtCDmcQeL_QDCLAFVGPn9wUzvDVUijOKu0qLFn0RolJ7bqvRk1B6V3F3URKZioPYWT2fYsaVRnm1wJxAhUY1a1uz3dGj0IwygjUTHN3mo8e7Uwdm2-0feIC63c-mm8My2i8vP7V5edim78DodE4cz5mBnGFWOdnG2f2RzF-rAornjXa2noPnWozWnDjZ7uQ687Yy3Q8YNoHO9uD2L5cUlho=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.2 LI-120-040_Unload_Material_Received_-_FTS_(IF)_(Copy) — LI-120-040_Unload_Material_Received_-_FTS_(IF)_(Copy)

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
        n1["Unload Material Received"]
        n2(["fa:fa-stop Goods Receipt Posted"])
        n3["Receive Material Against Advanced Shipping Notification (ASN)"]
    end
    n1 --> n2
    n3 --> n1
    class n2 endEvt
    class n3 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVMtu2zAQ_BVCgaEEkAE9LVeHAopsFQWaNKiT5lD3QFNLi4hMCiT9quF_L-l3XORUHQRxNDuzOyK1cYiowMmcTmfDONMZ2ri6hhm4GXInWIHroT3wE0uGJw0o13Ko4HrE_uxoQdyuLM1iJZ6xZm3REUwFoJevHspNYeMhhbnqKpCMup7bSjbDcl2IRkjLvoE-9enO7fDqXsgK5Jng-2lAElPaMA5nOErjNC5tnQIiePVOlCa0T4m7tc01YklqLPWu_bmCB7x6ZZWuzZriRoHh1HrWfMMTaOyMWs4tRuZycQyDKevDTWCjFhPGpwaPfQNJzN_OUOJvt2jb6Yz5yRQ9D8YcmYs0WKkBUKS0gYcLjShrmuwmLvIy8T2lpXiD7CYcpoMo9IidJDOj-54Nt7sENq11NhFNdaB2l3aGLGxXnlxloe_JtblfeQGvzk5FL-yH_ZPTfRoUQXF0opT-l5PJVT5j9XbwGkZlWA5OXkHSSwr_X73jmIM4zYPrnEAuGIEL0bIso-E5qmEvCfyPRe_LqOcXV6JTrGGJ12fBT0V8EiyTtAzSDwX3ftddzidPUpCjYDRMyuQkmN4HZR5-KBjnQdw_dGh0phK3NXrFEmph4kTfW5BYC7kn2IsHv8bOC28ErtCDmcQeL_QDCLAFVGPn9wUzvDVUijOKu0qLFn0RolJ7bqvRk1B6V3F3URKZioPYWT2fYsaVRnm1wJxAhUY1a1uz3dGj0IwygjUTHN3mo8e7Uwdm2-0feIC63c-mm8My2i8vP7V5edim78DodE4cz5mBnGFWOdnG2f2RzF-rAornjXa2noPnWozWnDjZ7uQ687Yy3Q8YNoHO9uD2L5cUlho=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 LI-120-060_Process_Damaged_Goods_-_FTS_(IF) — LI-120-060_Process_Damaged_Goods_-_FTS_(IF)

**Swim Lanes**: Warehouse Operator | **Tasks**: 12 | **Gateways**: 2

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
        n1["fa:fa-user Perform Goods Receipt"]
        n2["fa:fa-user Create Warehouse Task to Blocked Stock Type"]
        n3["fa:fa-user Confirm Warehouse Task to Blocked Stock Type"]
        n4["fa:fa-user Cancel Putaway Warehouse Task"]
        n5["fa:fa-user Move FG Stock to Hold Storage Bin"]
        n6[["fa:fa-cog Create Inbound Delivery"]]
        n7[["fa:fa-cog Distribute Inbound Delivery"]]
        n8[["fa:fa-cog Create Inbound Delivery with Blocked Stock Type"]]
        n9[["fa:fa-cog Distribute Inbound Delivery to EWM with Blocked Stock Type"]]
        n10["Receive FG Physical Boxes in Staging Area"]
        n11["Move FG stock to Investigation Location"]
        n12["Move Blocked Stock to Hold Storage Bin"]
        n13(["fa:fa-play Identifying Damaged Box Initiated"])
        n14(["fa:fa-stop Stock Type is Changed"])
        n15(["fa:fa-stop Stock Moved to Hold Location"])
        n16["Determine Put-away Location - R2_Interim State (IF)"]
        n17{{"fa:fa-code-branch Damaged?"}}
        n18{{"fa:fa-code-branch Type of MPL XML Trigger?"}}
    end
    n6 --> n7
    n7 --> n10
    n8 --> n9
    n2 --> n3
    n13 --> n18
    n10 --> n1
    n1 --> n17
    n11 --> n15
    n17 -->|"Yes"| n4
    n9 --> n2
    n18 -->|"QMEL Hold"| n8
    n4 --> n5
    n5 --> n11
    n3 --> n12
    n12 --> n14
    n18 -->|"Unrestricted Waybill"| n6
    n17 -->|"No"| n16
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n13 startEvt
    class n14 endEvt
    class n15 endEvt
    class n16 startEvt
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVu-P4jYQ_VesnFbcSSAlISHZfGi1_Mh1peW6vd3rtjqqyiQTsDbYyDHsUo7_veMQQ8KBbqvyAfDzvPdmxo6drZWIFKzIurraMs5URLYtNYcFtCLSmtICWm2yB36nktFpDkVLx2SCqwf2TxnmeMtXHaaxmC5YvtHoA8wEkC-3bXKDxLxNCsqLTgGSZa12aynZgsrNQORC6uh3EGZ2VrpVU30hU5DHANsOnMRHas44HOFu4AVerHkFJIKnDdHMz8Isae10crl4SeZUqjL9VQFj-vrEUjXHcUbzAjBmrhb5HZ1CrmtUcqWxZCXXphms0D4cG_awpAnjM8Q9GyFJ-fMR8u3djuyurib8YEoehxNO8JPktCiGkJFCITxaK5KxPI_eeYOb2LfbhZLiGaJ37igYdt12oiuJsHS7rZvbeQE2m6toKvK0Cu286Boid_nalq-Ra7flBr9PvICnR6dBzw3d8ODUD5yBMzBOWZb9Lyfsq3ykxXPlNerGbjw8eDl-zx_Y3-uZModecOOc9gnkmiVQE43juDs6tmrU8x37smg_7vbswYnojCp4oZuj4PXAOwjGfhA7wUXBvd9plqvpvRSJEeyO_Ng_CAZ9J75xLwp6N44XVhmizkzS5Zw8UQlzge0kvy5BUiXkPkB_uPN1YmU0ymhH95vcg8yEXJCPQqQF-QwJsKWaWH_VGG6TMZCAHaiZlO1VgvRzkTxDSh4U_pLHzRKaOt0THcEzhs7_Xcg7EaI8gZzcrxTV69LUazL9JnMs1kDij5UROv-CW1aPJJ0B6TPeZPe-HuiJmJlG3PKpWPGUDCFna5Ab5NRJQZM0ZLiUbLr6MTF8kxt5YWp-vmN1ses3Z6HbMHoav1HXsVG33DX7Tt7PNwVLaE764hUKwjhS6QyPNjzIgTbb6eitaJagMEtwy9dQKIZPGROc3Imk_HPCdA2zmeAPV9Dpvj_0YZnjZrlNgSuWbXSGQ7pAUqpTxyyYYtjvFPkf6gLeUQBTXtY6Q1hBBnPKZ9-T_LMkXUB6yLlWaYPbQ-oQFMgFXl16k3fKXW7CSYd8dv--5RjAFrrZuKTvb-MPJ3UH2-1x_VPoTPHWSeam5J8n1m5XDw_Ph5dlioyM7-_IH-M78ijZbAayRsfbYv-H90in8xNu_2oY7IdOdfjxcD--robuftithk63Cg8NYFeAGVdDI-8YwDdAafhtYv0JxcT6hodGNXG9D3RNXFjF_TYe3ZUrUUYbX28fbVT9ysWkYdI8qFV1ON6p_BcuQT9zCe4pPKI2UzzsS6feacKfRIk7vdo1oQs212MDds_D3fOwdx72z8O9-v3ZmAkuzoQXZ64vzuBimxeaJu5VLx9N1D-L9i5oBOa-bsKhga22tcBni7LUirZW-bKKL7QpZHSVK2vXtuhKiYcNT6yofKmzVssUmUNG8a5d7MHdv5TWdxU=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 LI-120-080_Receive_Material_Against_Advanced_Shipping_Notification_(ASN)_-_FTS_(IF) — LI-120-080_Receive_Material_Against_Advanced_Shipping_Notification_(ASN)_-_FTS_(IF)

**Swim Lanes**: Warehouse Operator | **Tasks**: 9 | **Gateways**: 1

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
        n1["fa:fa-user Perform Goods Receipt"]
        n2["fa:fa-user Perform Rejection on Inbound Delivery based on Waybill ID (ASN)"]
        n3[["fa:fa-cog Generate MPL Waybill for Finished Goods"]]
        n4[["fa:fa-cog Receive ASN from MPL"]]
        n5[["fa:fa-cog Create Inbound Delivery with Reference to ASN"]]
        n6[["fa:fa-cog Update Goods Receipt in Inbound Delivery"]]
        n7[["fa:fa-cog Update Open Quantity as zero in Inbound Delivery against same Waybill ID"]]
        n8["Send Offline Communication from Factory to Warehouse with Waybill Details"]
        n9["Receive Goods Physically"]
        n10(["fa:fa-play Request Advance Shipping Notification (ASN) for Finished Goods (FG)"])
        n11(["fa:fa-stop ASN Received"])
        n12(["fa:fa-stop Inbound Delivery is cancelled"])
        n13{{"fa:fa-code-branch Cancel Waybill Request ?"}}
    end
    n3 --> n13
    n5 --> n9
    n9 --> n1
    n1 --> n6
    n6 --> n11
    n4 --> n5
    n7 --> n12
    n2 --> n7
    n8 --> n2
    n13 -->|"Yes"| n8
    n10 --> n3
    n13 -->|"No"| n4
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n10 startEvt
    class n11 endEvt
    class n12 endEvt
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVltv4jgU_itWqoqOFKRcCc3DrmggVaWZTrfMbLUa9sEkJ8TbxM46hjbD8N_XzgUIhadFCHFu33fO50uy1SIWg-Zr19dbQonw0XYgUshh4KPBEpcw0FHj-BNzgpcZlAOVkzAq5uRnnWY6xbtKU74Q5ySrlHcOKwbo-4OOJrIw01GJaTksgZNkoA8KTnLMq4BljKvsKxgnRlKztaE7xmPghwTD8MzIlaUZoXBw257jOaGqKyFiNO6BJm4yTqLBTjWXsbcoxVzU7a9L-ILfX0gsUmknOCtB5qQizz7jJWRqRsHXyhet-aYTg5SKh0rB5gWOCF1Jv2NIF8f09eByjd0O7a6vF3RPir5NFxTJT5ThspxCgkoh3bONQAnJMv_KCSaha-il4OwV_Ctr5k1tS4_UJL4c3dCVuMM3IKtU-EuWxW3q8E3N4FvFu87ffcvQeSV_T7iAxgemYGSNrfGe6c4zAzPomJIk-V9MUlf-DZevLdfMDq1wuucy3ZEbGB_xujGnjjcxT3UCviERHIGGYWjPDlLNRq5pXAa9C-2REZyArrCAN1wdAG8DZw8Yul5oehcBG77TLtfLJ86iDtCeuaG7B_TuzHBiXQR0JqYzbjuUOCuOixS9YA4pk3KirwVwLBhvEtSHmj8WWoL9BA-V3ugJeMJ4ju4Zi0v0DBGQQiy0v48qrPMVz_APRIIwiuT3gS7ZmsZoChnZAK-QOv6xirzgaikHQw9TdDOZP37qY9s_9uARW6F7oKphQF-ePu8rJRsK5f1SphKx7lNiHIM4fZB6iA0gyYYSznIFdlLh9isCDor0wxBvRKQSLgEONAIkmMI8gRr1ob4XsYLqyYnIR4FOULyzKHL5KPpjjakgokK4RD-Bs3NoCK8woaWQ92QOR5KfsIwlyVweaPQ1SdRNiAKW52tKIlyvYy1WiCO5YSo17GEf1UJ0sFMQmGRlfyFvJXQnfDP8U1qVEjnLqn6madzsZy0yeZCe4d81yN4n8QYrmecpKQp5G6JHJkjSNVdvnjN7Ad2E92pTfTqmMA8UpWBFvRXa7uLTXOsk94O2pESRaizLPhbb2-1h3WIYLuVtHqUoqPP3inUT_r7QdrumXK5C84faaDj8TUG1ttvYt61524Zb02zMUWuO2mgXdhrbbU2vDVutbTW215rjxuyiZt3Kr4X2F8jV_SXjXcBoEu3TxEdW5zlHN5pqsbvJe27rvNs-vqV7EedixL0YGV2MeBcjcrrugdr3m-3Dr--1znrt7rmg6VoOPMck1vytVr_9yDekGBK8zoS20zW8Fmxe0Ujz67cEbV2f9SnB8vLOG-fuPwjv9uU=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 LI-120-170_Check_Material_for_Proper_Quantity_-_FTS_(IF) — LI-120-170_Check_Material_for_Proper_Quantity_-_FTS_(IF)

**Swim Lanes**: Warehouse Operator | **Tasks**: 10 | **Gateways**: 3

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
        n1["fa:fa-user Perform Goods Receipt for Good Condition Box"]
        n2["fa:fa-user Perform Goods Receipt for Repacked Box"]
        n3[["fa:fa-cog Create Inbound Delivery"]]
        n4[["fa:fa-cog Distribute Inbound Delivery"]]
        n5["Receive Physical Boxes In Staging Area"]
        n6["Count and Verify Physical Boxes Against Labels"]
        n7["Open and Inspect the Stock"]
        n8["Check Condition of Physical Boxes"]
        n9["Repack Damaged Box"]
        n10["Move Damaged Stock to Hold Location"]
        n11(["fa:fa-play Quantity Check Initiated"])
        n12["Resolve Discrepancies (IF)"]
        n13["Determine Put-away Location (IF)"]
        n14["Resolve Discrepancies (IF)"]
        n15["Determine Put-away Location (IF)"]
        n16{{"fa:fa-code-branch Condition of Physical Box ?"}}
        n17{{"fa:fa-code-branch Damaged Stock ?"}}
        n18{{"fa:fa-code-branch Count Mismatch ?"}}
    end
    n3 --> n4
    n5 --> n8
    n8 --> n16
    n7 --> n17
    n4 --> n5
    n6 --> n18
    n1 --> n13
    n10 --> n14
    n17 -->|"No"| n9
    n16 -->|"Good Box"| n6
    n9 --> n2
    n2 --> n15
    n18 -->|"Yes"| n12
    n16 -->|"Damaged  Box"| n7
    n18 -->|"No"| n1
    n17 -->|"Yes"| n10
    n11 --> n3
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl1v2zYU_SuEisAtIAP6tBQ9bHBkawvQdFnTtRjqPdAUZROWSYOkk3iO__su9WFbSoytmB-C3MN7zrm8Iq-0t4jIqZVYV1d7xplO0H6gl3RNBwkazLGiAxvVwFcsGZ6XVA1MTiG4fmB_V2lusHk2aQbL8JqVO4M-0IWg6I9bG42BWNpIYa6GikpWDOzBRrI1lrtUlEKa7Hc0LpyicmuWboTMqTwlOE7kkhCoJeP0BPtREAWZ4SlKBM87okVYxAUZHExxpXgiSyx1Vf5W0Tv8_I3leglxgUtFIWep1-VHPKel2aOWW4ORrXxsm8GU8eHQsIcNJowvAA8cgCTmqxMUOocDOlxdzfjRFH2ZzDiCHymxUhNaIKUBnj5qVLCyTN4F6TgLHVtpKVY0eedNo4nv2cTsJIGtO7Zp7vCJssVSJ3NR5k3q8MnsIfE2z7Z8TjzHljv42_OiPD85pSMv9uKj003kpm7aOhVF8b-coK_yC1arxmvqZ142OXq54ShMndd67TYnQTR2-32i8pEReiaaZZk_PbVqOgpd57LoTeaPnLQnusCaPuHdSfA6DY6CWRhlbnRRsPbrV7md30tBWkF_GmbhUTC6cbOxd1EwGLtB3FQIOguJN0v0DUu6FNBO9NuGSqyFrBPMj7vfZ1aBkwIPTb_RPZWFkGv0ixC5Qp8poWwDT1vICkEp3AqmmeDoRjzPrL_OhLz_KvSZwule0fy1hP_9qEHEAqWSQm_RLZ-LLc_RhJbskcodcM5JQZc0YdAbNt_-OzEEXlXXI0X3y51iBJemJqqAiR40XsAVhIFDcbfKEfBSENYIg_hXM4R2fYHxAjOuNKonQJcfAR8eBK_ot1xtKNEIxiJYCrLq5sbGa0nJ6qzzoui5dSnX1bZMi9EEr_HirUa7DiTdCdh4m1J5Iy3Qr3BL0UdBsPHqsdz3x1ZvSjjyv28x10zvUF3iLcx8Bk8sB9qHc55XlaREaQyZIhLK44RBn97fZh96Jj4kT6imcg2zGd1v9RCb69WW9BYl-BH98Mf1R_v96YjldDiHGU2Wlx8J-nlmHQ7nCtHbCt3uv2LFl3zN4btjao01hGc0GM71P9xHw-FPcDmaMKzDuAnjOnRHTRw1cdTEQR2HTThqllu628R-GzsN0Nq5leDLzPokZtYLnMkWHzV4NUyqYwmrbRXXtYrXhF4j2lbhxg35T3PkX8y56su2_TxKR31uU5DbL_So6bQrzSb9s-lsdt6-lTqw9zbsn79xOivBxRXwbV_nXdy7gPsX8OACHl7AR-2brAtHb8NxC1u2tYa7hFluJXur-rqDL8CcFnhbautgW3irxcOOEyupvoKs7SYH5oRheDmta_DwDyTLMCc=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 LI-120-180_Move_Material_to_Holding_Location_-_FTS_(IF) — LI-120-180_Move_Material_to_Holding_Location_-_FTS_(IF)

**Swim Lanes**: Warehouse Operator | **Tasks**: 3 | **Gateways**: 1

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
        n1["fa:fa-user Create Warehouse Task to Move Material to Holding Location"]
        n2["fa:fa-user Perform Goods Receipt"]
        n3["fa:fa-user Confirm Warehouse Task to Move Material to Holding Location via RF Scanner"]
        n4(["fa:fa-stop Material Moved to Holding Location"])
        n5["Determine Put-away Location (IF)"]
        n6["Check Material For Proper Quantity"]
        n7{{"fa:fa-code-branch Move Physical Box to Hold Location ?"}}
    end
    n2 --> n7
    n1 --> n3
    n3 --> n4
    n7 -->|"No"| n5
    n6 --> n2
    n7 -->|"Yes"| n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 endEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVU2P0zAQ_StWVquClEr5bEoOoDZtAImFZbuAEOXgOnZjbWpHttNtKf3v2E3aNGX3AjlEmZeZ92bGmcnOQjzDVmxdX-8ooyoGu57K8Qr3YtBbQIl7NqiBr1BQuCiw7Bkfwpma0V8HNzcoN8bNYClc0WJr0Blecgy-vLfBSAcWNpCQyb7EgpKe3SsFXUGxTXjBhfG-wkPikINa82rMRYZF6-A4kYtCHVpQhlvYj4IoSE2cxIizrENKQjIkqLc3yRX8EeVQqEP6lcQ3cPONZirXNoGFxNonV6viA1zgwtSoRGUwVIn1sRlUGh2mGzYrIaJsqfHA0ZCA7KGFQme_B_vr6zk7iYL7yZwBfaECSjnBBEil4elaAUKLIr4KklEaOrZUgj_g-MqbRhPfs5GpJNalO7Zpbv8R02Wu4gUvssa1_2hqiL1yY4tN7Dm22Or7hRZmWauUDLyhNzwpjSM3cZOjEiHkv5R0X8U9lA-N1tRPvXRy0nLDQZg4f_Mdy5wE0ci97BMWa4rwGWmapv60bdV0ELrO86Tj1B84yQXpEir8CLct4askOBGmYZS60bOEtd5lltXiVnB0JPSnYRqeCKOxm468ZwmDkRsMmww1z1LAMgffoMA51-0En0osoOKidjAXc3_MLQJjAvum3yARWNdzFnJoluLghq8xuNHvzAAa4J0-Tv2Ngg8cQUU5m1s_z2i9Lu0tFoSLFXjLeSbBHUaYlqob4V8kwhmhOuIfMgFrCsFdCmYIMoZFVyZ4cdKRipctkaHNnins5RlBqOMnWAet9O4At5XqQ3P8J_EX79OXXcmBjkhyjB5asZTrngiujwN8riBTVG27MdFud0zTLNX-Qq8FlNe13-ZbSZFmGfPNMeFW_83c2u9rJj2r9QPzQL__WrM2plubfmP6tRk0ZmTM33PrI59bv3XBDTyovbwLr-9YHtzOh80oHMe3A3tPw_7TcNBsmw4YntZdBx48DUfH-bRsa6XPDNLMinfW4S-k_1QZJrAqlLW3LVgpPtsyZMWHbW1VZaYjJxTqIVrV4P4Pkcg05g==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.7 LI-120-190_Resolve_Discrepancies_-_FTS_(IF) — LI-120-190_Resolve_Discrepancies_-_FTS_(IF)

**Swim Lanes**: Warehouse Operator | **Tasks**: 6 | **Gateways**: 3

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
        n1["fa:fa-user Perform Goods Receipt (GR)"]
        n2["fa:fa-user Reject Inbound Delivery"]
        n3["fa:fa-user Use Process Code To Update Delivery"]
        n4["Check for Discrepancy"]
        n5["Check if Quantity is Missing"]
        n6["Receive Actual Quantity"]
        n7(["fa:fa-stop Inbound Delivery Completed"])
        n8["Determine Put-away Location (IF)"]
        n9["Check Material for Proper Quantity - FTS (IF)"]
        n10{{"fa:fa-code-branch Discrepancy?"}}
        n11{{"fa:fa-code-branch Quantity Missing?"}}
        n12{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n2 --> n7
    n4 --> n10
    n5 --> n11
    n3 --> n6
    n6 --> n12
    n12 --> n1
    n11 -->|"Full Quantity Missing"| n2
    n11 -->|"Partial Quantity  Missing"| n3
    n1 --> n8
    n10 -->|"No"| n12
    n10 -->|"Yes"| n5
    n9 --> n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n7 endEvt
    class n8 startEvt
    class n9 startEvt
    class n10 gateway
    class n11 gateway
    class n12 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVltv4jgY_StWqoqOFKRcCc3DrmggVaXpbLe0Mxot-2AcB7w1dmQ7FJbhv69NLhBKn5aHqt_xOd_lEH9hZyGeYSu2rq93hBEVg11PLfEK92LQm0OJezaogO9QEDinWPYMJ-dMTcm_B5obFBtDM1gKV4RuDTrFC47B64MNRlpIbSAhk32JBcl7dq8QZAXFNuGUC8O-wsPcyQ_V6qM7LjIsjgTHiVwUaiklDB9hPwqiIDU6iRFnWSdpHubDHPX2pjnK39ESCnVov5T4EW5-kEwtdZxDKrHmLNWKfoVzTM2MSpQGQ6VYN2YQaeowbdi0gIiwhcYDR0MCsrcjFDr7PdhfX89YWxS8jGcM6A-iUMoxzoFUGp6sFcgJpfFVkIzS0LGlEvwNx1feJBr7no3MJLEe3bGNuf13TBZLFc85zWpq_93MEHvFxhab2HNssdV_z2phlh0rJQNv6A3bSneRm7hJUynP8_9VSfsqXqB8q2tN_NRLx20tNxyEifMxXzPmOIhG7rlPWKwJwidJ0zT1J0erJoPQdT5Pepf6Ayc5S7qACr_D7THhbRK0CdMwSt3o04RVvfMuy_mT4KhJ6E_CNGwTRnduOvI-TRiM3GBYd6jzLAQsluAHFHjJtZ3gjwILqLioCObD3L9mVg7jHPaN3-AJi5yLFbjnPJPgGSNMCgVu7p-_zKy_T2ReV_aM_8FIgQc25yXLwBhTssZi29X4Xc2rbsgMiqUEib4H4IWD1yLTdn6iD7Q-WWKkvzwuwJhIJHABGTqjhS2N5ODPEjJF1BYQCR6JlPpWddkDzT6MucZghFQJaavpEqObtn2pePFhVj3DqqBY4UzrvpwIh1o31rhY6WUDnkrVh-Z5-coRVIQzcPOQnpl7207wqN0wG-8wsTZLf3_HkfogfZlekLvObte0ajZyf653ClqeOvb7zNrvTyXuZUlbq_bug867rMMbREupfbmvbsdRpvdH9Q_zQL__m_a1DoMqdOvrwMI6ri8x86t4UIeD-tirY7dO19Bd18S_ZlZaUvphjpn1SzdwTn3Sa5ScPACgQ_cbelVo2IROrf7GD7RjR83BTywPJ2F9cFslCE7uvcna7LsO7F2G_ctwVK_nDjhs3w8d-PYyrLuuN1oXdi_DXgNbtrXSjzgkmRXvrMNbXv8SyHAOS6qsvW3BUvHpliErPrwNrfJw1ccE6iW1qsD9f198mg4=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 LI-120-220_Receive_Actual_Count_Quantity_-_FTS_(IF) — LI-120-220_Receive_Actual_Count_Quantity_-_FTS_(IF)

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
        n1["Receive Actual Quantity after Resolving Discrepancy"]
        n2(["fa:fa-play Receipt of Actual Quantity Initiated"])
        n3(["fa:fa-stop Actual Quantity Received"])
    end
    n1 --> n3
    n2 --> n1
    class n2 startEvt
    class n3 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqllEuP2jAUhf-KlRFKKwUpT0KzqASBSCO1ajtMO4vShXGuwRpjR7bDQBH_vTbvYTSrZoHw4d7v-B4cbz0ia_AKr9PZMsFMgba-WcAS_AL5M6zBD9BB-IUVwzMO2nc1VAozYX_3ZVHarF2Z0yq8ZHzj1AnMJaCf9wEa2EYeII2F7mpQjPqB3yi2xGpTSi6Vq76DPg3p3u3401CqGtSlIAzziGS2lTMBFznJ0zytXJ8GIkX9Ckoz2qfE37nNcflCFliZ_fZbDV_x-onVZmHXFHMNtmZhlvwLngF3MxrVOo20anUKg2nnI2xgkwYTJuZWT0MrKSyeL1IW7nZo1-lMxdkUPY6mAtmHcKz1CCjSxsrjlUGUcV7cpeWgysJAGyWfobiLx_koiQPiJins6GHgwu2-AJsvTDGTvD6Wdl_cDEXcrAO1LuIwUBv7eeMFor44lb24H_fPTsM8KqPy5EQp_S8nm6t6xPr56DVOqrganb2irJeV4VveacxRmg-i25xArRiBK2hVVcn4EtW4l0Xh-9BhlfTC8gY6xwZe8OYC_FSmZ2CV5VWUvws8-N3usp19V5KcgMk4q7IzMB9G1SB-F5gOorR_3KHlzBVuFugJK1hIGyf61oDCRqpDgXtE9HvqPQABtgI0IKbFHP1osTDMbBCmBhR6AC35yh5HNGKaKGiwIJup9-cKEn-wFIoLirsNt1nsgY1Bkr5h3tuLgdnIakv4eIVILghtZPOm77jHqzZ7Eg9fRIS63c8WcVzGh-X1v-_E01vySk6OB9oLvCWoJWa1V2y9_SVlL7IaKG658XaBh1sjJxtBvGL_MnttU9spRgzbjJcHcfcPDG2dzA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Warehouse Operator | LI-120-040_Unload_Material_Received_-_FTS_(IF), LI-120-040_Unload_Material_Received_-_FTS_(IF)_(Copy), LI-120-060_Process_Damaged_Goods_-_FTS_(IF), LI-120-080_Receive_Material_Against_Advanced_Shipping_Notification_(ASN)_-_FTS_(IF), LI-120-170_Check_Material_for_Proper_Quantity_-_FTS_(IF), LI-120-180_Move_Material_to_Holding_Location_-_FTS_(IF), LI-120-190_Resolve_Discrepancies_-_FTS_(IF), LI-120-220_Receive_Actual_Count_Quantity_-_FTS_(IF) | |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for LI-120. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
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
| LOGC0972_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  |  | 02.High |
| LOGC0946_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  |  | 02.High |
| FTSC1550 | Conversion | Inventory Conversion | 02. FS Unplanned |  |  | 03.Medium |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for LI-120.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for LI-120.

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

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| LOGW1078_IF | Workflow | ISM Workflows - Capital/AMT | 10. Object Complete |  | NA | 03.Medium |
| LOGW1077_IF | Workflow | ISM Workflows - EIMS/Lab | 10. Object Complete |  | NA | 03.Medium |
| LOGW1076_IF | Workflow | ISM Workflows - Non-inventory | 10. Object Complete |  | NA | 03.Medium |
| LOGR1176_IF | Report | ISM - International Traffic Report | 10. Object Complete |  | NA | 03.Medium |
| LOGR0833_IF | Report | Email Notification for deletion of Shipping Memos | 10. Object Complete |  | NA | 04.Low |
| LOGI1718 | Interface | To align on batch attributes for straddle in S4 | 08. FUT In Progress |  | NA | 03.Medium |
| LOGI1677 | Interface | Send 4C1 Inventory Reconciliation Snapshot to IP | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1676 | Interface | Send 4C1 Inventory movement Stock type change and cycle count to IP | 10. Object Complete |  | SFT | 03.Medium |
| LOGI1555 | Interface | Straddle Plant to be automatically complete the Goods Receipt and write of th... | 09. FUT Overdue |  | MuleSoft | 03.Medium |
| LOGI1091 | Interface | STO based Outbound Delivery Notification Confirmation for Delivery Note Deletion | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
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
| LOGF1525 | Form | Consolidated Commercial Invoice for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1524 | Form | Commercial Invoice for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1523 | Form | Packing list for WIP | 10. Object Complete |  | NA | 04.Low |
| LOGF1100_IF | Form | Printing of Standard Shipping Label | 10. Object Complete |  | NA | 03.Medium |
| LOGF0359_IF | Form | ISM - Generate Commercial Invoice - IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0358_IF | Form | ISM - Generate Traveler Document - IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0352_IF | Form | ISM - IPLA | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0351_IF | Form | ISM - Custom China Special label | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0350_IF | Form | ISM - India GST DC | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE1690 | Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF a... | 07. FUT Roadblock |  | NA | 03.Medium |
| LOGE1572_IF | Enhancement | SAP GUI T-code to Move stock from Blocked to unblock Status | 10. Object Complete |  | NA | 03.Medium |
| LOGE1569_IF | Enhancement | Enhancement to change billing status based on ship reason in ISM | 10. Object Complete |  | NA | 04.Low |
| LOGE1554 | Enhancement | Straddle Plant to be automatically complete the Goods Receipt and write of th... | 09. FUT Overdue |  | NA | 03.Medium |
| LOGE1453 | Enhancement | Trigger the request for cancellation 3B14R and cancel the demand on STO based... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1450 | Enhancement | Inbound idoc processing logic during 3B2 and 3B13 | 10. Object Complete |  | NA | 03.Medium |
| LOGE1415 | Enhancement | Suppress Batch and serial number validation in MIGO/MB26 for movement type 261 | 08. FUT In Progress |  | NA | 03.Medium |
| LOGE1414 | Enhancement | Creation of outbound Delivery for WIP inventory from STO | 10. Object Complete |  | NA | 03.Medium |
| LOGE1177_IF | Enhancement | India GST E-invoicing | 10. Object Complete |  | NA | 04.Low |
| LOGE1118_IF | Enhancement | ISM – MY Security Check Fiori app - IF | 10. Object Complete |  | NA | 03.Medium |
| LOGE1117_IF | Enhancement | ISM – Employee acknowledgement - IF | 10. Object Complete |  | NA | 03.Medium |
| LOGE1090_IF | Enhancement | PGI confirmation for non-inventory Intel freight shipments via email | 10. Object Complete |  | NA | 04.Low |
| LOGE1080_IF | Enhancement | Email notifications to be triggered as part of ISM Workflows | 10. Object Complete |  | NA | 03.Medium |
| LOGE1054 | Enhancement | Email/Text Trigger to Factory Technician and Post Goods Issue upon all WO con... | 10. Object Complete |  | NA | 02.High |
| LOGE1052_IF | Enhancement | Custom fields required on delivery screen | 10. Object Complete |  | NA | 04.Low |
| LOGE0935_IF | Enhancement | Fiori App - Shipping Memo | 08. FUT In Progress |  | NA | 02.High |
| LOGE0835_IP | Enhancement | Interface to get the AMT (Asset Management Tool) data on the ISM | 10. Object Complete |  | NA | 03.Medium |
| LOGE0239_IF | Enhancement | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 - Table Creation | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0190_IF | Enhancement | Delivery Split for STO in S/4 | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGC0972_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , Batch Characteristi... | 10. Object Complete |  | NA | 02.High |
| LOGC0946_IF | Conversion | Open Inventory Conversion for IP and IF (as applicable) , ECC to S4 | 10. Object Complete |  | NA | 02.High |
| FTSC1550 | Conversion | Inventory Conversion | 02. FS Unplanned |  | NA | 03.Medium |
| LOGI1738 | Interface | Interface to send data to Factory Comm to activate the Mobile text receiving ... | 02. FS Unplanned |  | NA | 02.High |

**Summary**: 2 Reports, 18 Interfaces, 3 Conversions, 19 Enhancements, 9 Forms, 3 Workflows

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for LI-120:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for LI-120:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (54 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 46 | 85.2% |
| 08. FUT In Progress | 3 | 5.6% |
| 09. FUT Overdue | 2 | 3.7% |
| 02. FS Unplanned | 2 | 3.7% |
| 07. FUT Roadblock | 1 | 1.9% |
| **Total** | **54** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 2 |
| Interface (I) | 18 |
| Conversion (C) | 3 |
| Enhancement (E) | 19 |
| Form (F) | 9 |
| Workflow (W) | 3 |
| **Total** | **54** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 02.High | 5 |
| 03.Medium | 35 |
| 04.Low | 14 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| LOGI1718 | 02.Interface | To align on batch attributes for straddle in S4 | 08. FUT In Progress | 03.Medium |
| LOGI1555 | 02.Interface | Straddle Plant to be automatically complete the Goods Receipt and write of the i... | 09. FUT Overdue | 03.Medium |
| LOGE1690 | 04.Enhancement | Custom Enhancement for Storage Location and Storage Type Restriction LOG IF and ... | 07. FUT Roadblock | 03.Medium |
| LOGE1554 | 04.Enhancement | Straddle Plant to be automatically complete the Goods Receipt and write of the i... | 09. FUT Overdue | 03.Medium |
| LOGE1415 | 04.Enhancement | Suppress Batch and serial number validation in MIGO/MB26 for movement type 261 | 08. FUT In Progress | 03.Medium |
| LOGE0935_IF | 04.Enhancement | Fiori App - Shipping Memo | 08. FUT In Progress | 02.High |
| FTSC1550 | 03.Conversion | Inventory Conversion | 02. FS Unplanned | 03.Medium |
| LOGI1738 | 02.Interface | Interface to send data to Factory Comm to activate the Mobile text receiving cap... | 02. FS Unplanned | 02.High |

**Tower Context:** FTS-IF has 265 total RICEFW objects (209 complete, 56 active/other)

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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>LI-120 — Receive Materials and Services - FTS (IF)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*52 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| LOGW1078_IF | ISM Workflows - Capital/AMT | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGW1077_IF | ISM Workflows - EIMS/Lab | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| LOGW1076_IF | ISM Workflows - Non-inventory | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| LOGR1176_IF | ISM - International Traffic Report | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGR0833_IF | Email Notification for deletion of Shipping Memos | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 4. Completed |
| LOGI1718 | To align on batch attributes for straddle in S4 | Feb-26 (100%) | Mar-26 (100%) | Mar-26 (100%) | Mar-26 (5%) | 3. Off Track |
| LOGI1677 | Send 4C1 Inventory Reconciliation Snapshot to IP | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1676 | Send 4C1 Inventory movement Stock type change and cycle count to IP | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| LOGI1555 | Straddle Plant to be automatically complete the Goods Receipt and write of the inventory | Sep-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (45%) | 3. Off Track |
| LOGI1091 | STO based Outbound Delivery Notification Confirmation for Delivery Note Deletion | Mar-25 (100%) | Jul-25 (100%) | Jul-25 (100%) | Sep-25 (100%) |  |
| LOGI1081_IF | Interface + Enhancement - Reprinting of Carrier Label | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) |  |
| LOGI1079_IF | Interface from S4 ISM to Service Now | May-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) |  |
| LOGI1074_IF | Send data via API to retrieve the tracking ID - interface + Enhancement | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) | 3. Off Track |
| LOGI1062 | STO based outbound delivery notification request for delivery note cancellation | Mar-25 (100%) | Jul-25 (100%) | Jul-25 (100%) | Sep-25 (100%) |  |
| LOGI1053 | STO based Outbound Delivery Notification from 3PL to S/4 for confirming Pick/Pack - 3B13 | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Aug-25 (100%) | 3. Off Track |
| LOGI1043 | Inventory Movement from 3PL to S/4 - 4C1 Cycle Count | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) | 1. On Track |
| LOGI1041 | STO based Outbound Delivery PGI confirmation from 3PL to S/4 - 3B2 | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) |  |
| LOGI1040 | STO based Outbound Delivery PGI confirmation for returns from S/4 to 3PL - 3B2 | Apr-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| LOGI1038 | STO based Outbound Delivery Notification from S/4 to 3PL - 3B12 | Mar-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Jul-25 (100%) | 2. At Risk |
| LOGI1037 | Inventory Movement from S/4 to 3PL – 4C1 (Outbound) | May-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Aug-25 (100%) |  |
| LOGI0836_IF | Interface from S4 to NDA (IPLA –Intel Pre Release License Agreements) | Apr-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Jan-26 (100%) | 4. Completed |
| LOGI0237_IF | Inventory Reconciliation snapshot (4C1) from 3PL WMS to SAP S/4 | Jun-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Sep-25 (100%) |  |
| LOGF1525 | Consolidated Commercial Invoice for WIP | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 3. Off Track |
| LOGF1524 | Commercial Invoice for WIP | Aug-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | Feb-26 (100%) | 1. On Track |
| LOGF1523 | Packing list for WIP | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 3. Off Track |
| LOGF1100_IF | Printing of Standard Shipping Label | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) |  |
| LOGF0359_IF | ISM - Generate Commercial Invoice - IF/IP | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |
| LOGF0358_IF | ISM - Generate Traveler Document - IF/IP | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) | 1. On Track |
| LOGF0352_IF | ISM - IPLA | Sep-24 (100%) | May-25 (100%) | May-25 (100%) | Jul-25 (100%) |  |
| LOGF0351_IF | ISM - Custom China Special label | Sep-24 (100%) | May-25 (100%) | May-25 (100%) | Jul-25 (100%) |  |

*... and 22 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**Mapped sub-tower(s):** 7.6 FTS IF - Logistics & Inventory Management

**RAID Summary:** 102 open items (12 capability-specific, 90 tower-level), 439 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 6 | 6 |
| P2 - Medium | 12 | 69 | 81 |
| P3 - Low | 0 | 15 | 15 |
| **Total** | **12** | **90** | **102** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03294 |  | P2 - Medium | Factory portal application is not ready from FTS and this is... | In Progress | FTS IF | 2026-02-27 |
| 02987 |  | P2 - Medium | LOGF1525 - Consolidated Commercial Invoice for WIP Awaiting ... | In Progress | FTS IF | 2025-11-06 |
| 03716 | Risk | P2 - Medium | Raising RAID to track the progress of FUT for LOGE1690 as it... | In Progress | FTS IF | 2026-03-13 |
| 03518 | Action | P2 - Medium | Batch Attributes for WIP Straddle-LOGI1718 | Not Started |  | 2026-02-06 |
| 02419 | Key Decision | P2 - Medium | Batch classification details clarification required LOGC0972... | Not Started | FTS IF | 2025-10-15 |
| 03231 | Risk | P2 - Medium | Need LE Sample Data (Shipping Point & Delivery Route) for va... | Not Started | FTS IF | 2026-02-10 |
| 03704 | Risk | P2 - Medium | ASN Data from CIBR via e2Open needs to incorporate new attri... | In Progress | Data Foundation Program ( | 2026-03-10 |
| 02133 | Action | P2 - Medium | clarification on storage location xref for one to many scena... | Not Started | FTS IF |  |
| 02315 | Action | P2 - Medium | Need Approval on Preload file | Not Started | FTS IF |  |
| 03685 |  | P2 - Medium | Rinchem ITC1 Test Scenario/Case Readiness | In Progress | FTS IF |  |
| 03515 | Risk | P2 - Medium | Need E2E test data for STO of IM to IM (Interfactory shipmen... | In Progress | FTS IF | 2026-03-06 |
| 03779 | Risk | P2 - Medium | Chem 3PL PIP Enhancement to support FTZ | In Progress | FTS IF | 2026-04-17 |

**Other FTS-IF Tower RAID Items** (90 open):

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
| 01857 | Action | P2 - Medium | TF Signavio Flows Update Request | In Progress | FTS IF | 2026-01-30 |
| 03079 | Action | P2 - Medium | Request for PDH Design WTF | In Progress | FTS IP | 2026-03-04 |
| 03128 | Risk | P2 - Medium | Application Health Monitoring | In Progress | FTS IF | 2026-05-13 |
| 03157 |  | P2 - Medium | Split Logic to Segregate IF & IP data from EWM tables | Not Started |  | 2025-12-04 |
| 03205 | Action | P2 - Medium | Provide an update WW50 on the production rollout plan for th... | In Progress | FTS IF | 2026-03-06 |
| 03241 | Risk | P2 - Medium | Materials Planning Policy for Constrained Materials | In Progress | FTS IP | 2026-07-31 |
| 03292 | Risk | P2 - Medium | SCP IF BY ESP Solves during ITC1 | In Progress | FTS IF | 2026-01-09 |
| 03308 | Action | P2 - Medium | Missing information for Anafi material master | Not Started | FTS IF |  |
| 03314 | Risk | P2 - Medium | Executive lock cause performance issues in IF Dev | In Progress | FTS IF | 2026-04-17 |
| 03331 | Risk | P2 - Medium | Clarity on finalized SAP S/4 Plant and storage location mapp... | In Progress | Master Data | 2026-02-20 |
| 03334 | Issue | P2 - Medium | Application Monitoring - Connectors Health Monitoring | In Progress | FTS IF | 2026-05-15 |
| 03368 | Issue | P2 - Medium | Infrastructure resources support PDF SMH ability to provide ... | In Progress | FTS IF | 2026-03-27 |
| 03398 | Action | P2 - Medium | Kafka Admin Password for both IF and IP | In Progress | FTS IF | 2026-04-03 |
| 03703 | Risk | P2 - Medium | For FUT: Factory Automation Apps waiting on Heartbeat Loader... | In Progress | FTS IF | 2026-03-24 |
| 03713 | Risk | P2 - Medium | Lack of TRDI data impacting delivery of ECA report by ITC2 | In Progress | FTS IF | 2026-03-27 |
| 03718 | Risk | P2 - Medium | Storage Location Logic for Non-MMID Parts. | In Progress | PTP | 2026-03-27 |
| 03732 | Risk | P2 - Medium | Production scheduling systems will likely only provide mock ... | Not Started |  | 2026-03-27 |
| 03526 | Action | P2 - Medium | Review process for post-validation of system changes | In Progress | FTS IP | 2026-04-03 |
| 02088 | Risk | P2 - Medium | Equipment Master Conversion help needed | In Progress | FTS IF | 2026-03-31 |
| | | | *... and 60 more tower-level items* | | | |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*LI-120 — Architecture Document (TOGAF BDAT) · Forecast to Stock (IF) · Generated: March 2026*

