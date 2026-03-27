<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-72 — IP</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-72 · Forecast to Stock</p>
  <p style="font-size:14px; color:#888;">IAO Program · Release 2<br/>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-72 IP** within the IAO program. It includes 4 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Forecast to Stock |
| **Capability** | E2E-72 - IP |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Forecast to Stock |
| **L2 Capability** | E2E-72 - IP |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-72 Process Migration | Migrate IP business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-72 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **4 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-72 IP.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-72-_Intel_Foundry_-_Request_and_Response_process_with_planning_integration_(Process_for_Type_A_a | E2E-72-_Intel_Foundry_-_Request_and_Response_process_with_planning_integration_(Process_for_Type_A_a | Boundary Apps, External Partners/
Supplier
, SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | 12 | 6 |
| 2 | E2E-72A-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | E2E-72A-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | Boundary Apps, External Partners/
Supplier
, SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | 19 | 10 |
| 3 | E2E-72B-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | E2E-72B-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | Boundary Apps, External Partners/
Supplier
, SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | 19 | 10 |
| 4 | E2E-72C-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | E2E-72C-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | Boundary Apps, External Partners/
Supplier
, SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | 19 | 10 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-72-_Intel_Foundry_-_Request_and_Response_process_with_planning_integration_(Process_for_Type_A_a — E2E-72-_Intel_Foundry_-_Request_and_Response_process_with_planning_integration_(Process_for_Type_A_a

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | **Tasks**: 12 | **Gateways**: 6

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
        n1["Receive inventory request in Planning Hub"]
        n2["Fetch Inventory Data from Speed"]
        n3["Fetch BOM Data from MDG"]
        n4["Fetch Inventory demand from BY"]
        n5["Receive Updates via PDH"]
        n13(["fa:fa-play Initiate Inventory request process"])
        n19{{"fa:fa-arrows-alt parallelGateway"}}
        n20{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n6["PO Received at Supplier"]
        n7["Order Acknowledgement sent to S/4"]
        n8["Send and Receive Forecast communication commit"]
        n15(["fa:fa-play Forecast communication from ECA"])
        n16(["fa:fa-stop Forecast communicated"])
    end
    subgraph SAP S/4  Intel Foundry Purchase Req – Purchase Order 
        n9[["fa:fa-cog Create Purchase Req"]]
        n10[["fa:fa-cog Use 'MD04' Fiori App to show PR and Stock levels"]]
        n11[["fa:fa-cog PR converted to PO (Based on Planning Design Horizon)"]]
        n12[["fa:fa-cog Do Excel Upload or Manual Creation"]]
        n14(["fa:fa-play Initiate Excel Upload or Manual Creation"])
        n17["intermediateThrowEvent"]
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n23{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n11 --> n21
    n3 --> n20
    n19 --> n2
    n2 --> n20
    n6 --> n7
    n18 --> n11
    n21 -->|"3A4  (EDI 850) E2Open"| n6
    n19 --> n4
    n13 --> n19
    n9 --> n10
    n21 --> n17
    n10 --> n18
    n14 --> n12
    n12 --> n23
    n23 --> n9
    n4 --> n22
    n1 --> n22
    n22 --> n5
    n5 --> n23
    n20 --> n1
    n19 --> n3
    n7 -->|"3A4 (EDI  855)
Order Confirmation E2Open"| n18
    n8 --> n16
    n15 --> n8
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 endEvt
    class n17 startEvt
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV22P2jgQ_itWqhVdCdS8EpYPJ_GWdqWuFpXunU7lPpjEAWuNnToO7HbLf79xSEKSEp3U4wOSH88843lmxpg3IxQRMcbGzc0b5VSN0VtP7cie9Maot8Ep6fXRGfgTS4o3jKQ9bRMLrlb0R25mucmLNtNYgPeUvWp0RbaCoKf7PpqAI-ujFPN0kBJJ416_l0i6x_J1JpiQ2vodGcVmnEcrtqZCRkReDEzTt0IPXBnl5AI7vuu7gfZLSSh41CCNvXgUh72TPhwTx3CHpcqPn6XkAb_8RSO1g3WMWUrAZqf27DPeEKZzVDLTWJjJQykGTXUcDoKtEhxSvgXcNQGSmD9fIM88ndDp5mbNq6Do85c1R_AJGU7TOYlRqgBeHBSKKWPjd-5sEnhmP1VSPJPxO3vhzx27H-pMxpC62dfiDo6EbndqvBEsKkwHR53D2E5e-vJlbJt9-QrfrViER5dIs6E9skdVpKlvzaxZGSmO4_8VCXSVX3H6XMRaOIEdzKtYljf0ZuavfGWac9efWG2diDzQkNRIgyBwFhepFkPPMrtJp4EzNGct0i1W5IhfL4R3M7ciDDw_sPxOwnO89imzzVKKsCR0Fl7gVYT-1AomdiehO7HcUXFC4NlKnOzQVGR5L6NJkqTnPf3h1re18YWEhB4IovxAuBJgJMn3jKQKELRkmHPoQ_Qp26yNf2quNrgGRIU7dF85zrHCKJZij1YJIVHTwakcpo8PNdOH-cemoXuFOSJ7zKOzw_Tvpr1XS-IpiaAYKTpQjJbzT01Dy3kPpjEex3iQMCjYPVxRFOxrgcrcE9CfpCkQ3NYZ7t7eSgYspTimA8zAGEvMGGEfz42wNk6nulLm7zjZV50oD1mWQqa_eMFUtoq-eFFEcszQEu4GTmT6Aa2yJGGUSFSLNARNlo-oUDBCWFVmTfl8MHzUtyiahM9cHBmJtnCTcwVTBV9KoNUHt-kyApcVnAzp4pU1CoQkIQaNQ7HfZ5yGWFHB8xVVrYp5rYp1-OZ9sZhN2uUaXtxTJZJr7nmb3nZpuJosdVYIOkQRBv4wR9Aly0zCRZwSyOk7Wme2aTkX7KxR7Rh336pThGKLZpLonqtzwBEaaZtNjyew6j3MTbeHAiok1WOs9U534oiWX3J1V0qEz4iRA_zetOmsJh14wG_bgUhIXtNA9d9P4SQRErWJn5OUbjn6BPF-CH7b5rSbnHMB_RaCRE8JExiYJHrAPIPuy9OFIrUJ3K5h_G-eRo11W1KojtyTSPt_3cG0LPQ8t3ppdJko_UoZbOB3Fi4Z8tI1UudBtH5nep3fnV4oFhoM_tBxC8Ap1mZpcFcAxdpu7Q_Pa780H53XVsln5wF-rg1nAn39fjG_RyPPvEUL-zEhoO5PoGiFcst1cRbrrgCKfctscOuilB5mAYxKwC2A8vhWeX6n5CiClDEKB7tyaK3tgsAr1l6brzxCK6ly36_JkasBcnjQYecxngkeU7k_XzM1iaqESnkrzYr4o9pvuhaq9vJo7IBCnVtW95bdveVUr8Em7nbgXgc-LF56TdTvsB6Vz6AmfHcVhppcha3rsH0ddkrY6Bt7mH9MI2P8ZuT_L-A_SERinDFlnPoGzpRYvfLQGOfvcCPLnwlziuGW35_B07_-GfTz" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-72A-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T — E2E-72A-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | **Tasks**: 19 | **Gateways**: 10

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
        n1["Receive inventory request in Planning Hub"]
        n2["Fetch Inventory Data from Speed"]
        n3["Fetch BOM Data from MDG"]
        n4["Fetch Inventory demand from BY"]
        n5["Receive Updates via PDH"]
        n20(["fa:fa-play Initiate Inventory request process"])
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n32{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n6["PO Received at Supplier"]
        n7["Order Acknowledgement sent to S/4"]
        n8["Perform Supplier Activities"]
        n22(["fa:fa-stop PO Updated to Supplier"])
        n27{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4  Intel Foundry Purchase Req – Purchase Order 
        n9[["fa:fa-cog Create Purchase Req"]]
        n10[["fa:fa-cog Use MD04 Fiori App to show PR and Stock levels"]]
        n11[["fa:fa-cog PR converted to PO"]]
        n12[["fa:fa-cog Check if PR Approved as per Planning design"]]
        n13[["fa:fa-cog Validate Vendor through Routing tables"]]
        n14[["fa:fa-cog Check if Supplier is E2E Open enabled"]]
        n15[["fa:fa-cog Move PO's to Staging"]]
        n16[["fa:fa-cog Send PO's to E2Open"]]
        n17[["fa:fa-cog B2B config (OpenText)"]]
        n18[["fa:fa-cog PO’s sent to WebSuite"]]
        n19[["fa:fa-cog Send PO's to Ariba P2P"]]
        n21(["fa:fa-stop PO Sent"])
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch Supplier E2Open Enabled?"}}
        n25{{"fa:fa-code-branch Supplier is B2B enabled"}}
        n26{{"fa:fa-code-branch Has ANID"}}
        n30{{"fa:fa-arrows-alt parallelGateway"}}
        n31{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n10 --> n12
    n11 --> n30
    n3 --> n29
    n2 --> n29
    n6 --> n7
    n23 --> n11
    n30 -->|"3A4  (EDI 850) E2Open"| n6
    n28 --> n3
    n29 --> n1
    n1 --> n32
    n30 --> n13
    n13 --> n14
    n14 --> n24
    n24 -->|"Yes"| n16
    n15 --> n25
    n25 -->|"Yes"| n17
    n7 -->|"3A4 (EDI  855)
Order Confirmation E2Open"| n23
    n17 --> n27
    n18 --> n27
    n27 --> n8
    n8 --> n22
    n12 --> n23
    n16 --> n21
    n25 -->|"No"| n31
    n26 -->|"Yes"| n19
    n24 --> n26
    n26 -->|"No"| n15
    n19 -->|"All PO’s sent
 to WebSuite for viewing"| n31
    n5 --> n9
    n32 --> n5
    n31 --> n18
    n28 --> n4
    n28 --> n2
    n4 --> n32
    n20 --> n28
    n9 --> n10
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 startEvt
    class n21 endEvt
    class n22 endEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWNtu2zgQ_RVCReAWsFFdLdsPu_BNbYCmMeJeUDT7QEuUTUSWVJKyk6b-9x3Koiyx9u62mwcDnJlz5sqRlGcjzCJijIyrq2eaUjFCzx2xIVvSGaHOCnPS6aKj4BNmFK8SwjvSJs5SsaTfSzPLzR-lmZQFeEuTJyldknVG0MfrLhoDMOkijlPe44TRuNPt5IxuMXuaZknGpPULMojNuPRWqSYZiwg7GZimb4UeQBOakpPY8V3fDSSOkzBLoxZp7MWDOOwcZHBJtg83mIky_IKTG_z4mUZiA-cYJ5yAzUZsk3d4RRKZo2CFlIUF26liUC79pFCwZY5Dmq5B7pogYjh9OIk883BAh6ur-7R2it7d3acI_sIEcz4jMeICxPOdQDFNktELdzoOPLPLBcseyOiFPfdnjt0NZSYjSN3syuL29oSuN2K0ypKoMu3tZQ4jO3_ssseRbXbZE_xqvkganTxN-_bAHtSeJr41tabKUxzH_8sT1JV9wPyh8jV3AjuY1b4sr-9NzZ_5VJoz1x9bep0I29GQNEiDIHDmp1LN-55lXiadBE7fnGqkayzIHj-dCIdTtyYMPD-w_IuER396lMVqwbJQETpzL_BqQn9iBWP7IqE7ttxBFSHwrBnON2iSFeUso3Ge86NO_qXW13vjjoSE7gii6Y6kIgMjRr4VhAuQoEWC0xTmEL0tVvfGXw2oDdCAiHCDrmvgDAuMYpZt0TInJGoDnBowub1pmN7M3rQN3TPMEdniNDoCJl_a9l4jiY95BM3gaEcxWszeaiGbL8E0xqMY9_IEGnYNK4qCfcORyj2H-hPOgeBVk2Hw_KwYMGPZnvdwAsaY4SQhyZvjINwbh0MTNPwNkGOfBdE0TAoOmf6EglupNX3-KAhLcYIWsBtSwvhrtCzyPKGEoYanPtRkcYuqCkYIi9qsXT4fDG_lFkXj8CHN9gmJ1rDJUwG3Cn5Ehpav3TZkILkJizO2Pfkeh4LuoPCEa-2xT-3hIssRRHXsZ1SSn4JqtcQ_FUo-fHorWJ8wO-Txv1dqOV7I2BHMgSAJCuRtgVlYFAzWLSdQm2_ovrBNyznJjpVoBDL8-vUUxxpNGZGT1eSAyJv5WmYb8RGsbmamiwKaMSqvqkybb7I9WtwhOf5LkYUPKCE7eKboZFabDBDw_NoRVlVvcasDbC3eDQFuGkskuGZZOQsc5ZBlvQUiwuk61ZmcNtMnnFDZNfQJKp0xJDYsK9YbdJcVQpKI8rmvk7gXwqnHhnI0t-foNicptFByRDqH1-a4gRwg8Q4vx0fgNXjXIf02ZAkh15C5LZ3pCL-NmNgTWemYrtFLaf6BPIpXOmagNee2nKYhr2_OZ7JaFlQQHTj8h_DgRWgFW85eaCDb-vkeAVDoF8f51YtzhLnnYXWfjlVD82OL_tTh3r_Aoc2ypHWH2-j-efRbGNTx--uZvkTN39m81q-B6nUCFxr1en_Iq6UE1lHgVA_41Dme7WF1trVz_3j2lbqytyyFLz38uDecMWyrl_PZNRp45qt6Un8AhcIOKt_qPKy4VGyV2m5Ry9usDJRzVwncKlolsN0qmi_yOv-Qt0mZepWpp0w93VTl6DcyKhOCjDyY0-N-ncqbxbZY0CxtZmnXUfqVJ8VnDTSBXVkMqrPS101STagpqy7Ylh78-6x07tSKvp7VsFUaaaGbVhyWqow1rBTjJNEWA1g0VgOCpyi815B9ucWaYVTFVr6dKiHlwalabQ200XC1s6qIq42GXY2GrQjUKDXfW6W08Xbd0sDFuKiyLqvsyyrnssq9rPIuq_qXVf5l1eCy6nI1oJzqc60tt6pPq7bUPit11FdHW-yeF3vnxf3zYv-8eHBePDwrhnVyVmydF9tKbHSNLYELTyNj9GyU_yowRkZEYlwkwjh0DVyIbPmUhsao_KQ2ivINcUYxvMptj8LD33KXEic=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-72B-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T — E2E-72B-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | **Tasks**: 19 | **Gateways**: 10

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
        n1["Receive inventory request in Planning Hub"]
        n2["Fetch Data from Speed"]
        n3["Fetch BOM Data from MDG"]
        n4["Fetch Inventory demand from BY"]
        n5["Receive Updates via PDH"]
        n20(["fa:fa-play Request Response Process Initiated"])
        n27{{"fa:fa-arrows-alt parallelGateway"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n31{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n6["PO Received at Supplier"]
        n7["Order Acknowledgement sent to S/4"]
        n8["Perform Supplier Activities"]
        n21(["fa:fa-stop PO updated to Supplier"])
        n26{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4  Intel Foundry Purchase Req – Purchase Order 
        n9[["fa:fa-cog Create Purchase Req"]]
        n10[["fa:fa-cog Use 'MD04' Fiori App to show PR and Stock levels"]]
        n11[["fa:fa-cog PR converted to Sub-Con PO"]]
        n12[["fa:fa-cog Check if PR Approved as per Planning design"]]
        n13[["fa:fa-cog Validate Vendor through Routing tables"]]
        n14[["fa:fa-cog Check if Supplier is E2E Open enabled"]]
        n15[["fa:fa-cog Move PO's to Staging"]]
        n16[["fa:fa-cog Send PO's to E2Open"]]
        n17[["fa:fa-cog B2B config (OpenText)"]]
        n18[["fa:fa-cog PO’s sent to WebSuite"]]
        n19[["fa:fa-cog Send PO's to Ariba P2P"]]
        n22{{"fa:fa-code-branch exclusiveGateway"}}
        n23{{"fa:fa-code-branch Supplier E2Open Enabled?"}}
        n24{{"fa:fa-code-branch Supplier is B2B enabled"}}
        n25{{"fa:fa-code-branch Has ANID"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n10 --> n12
    n11 --> n29
    n27 --> n2
    n2 --> n28
    n6 --> n7
    n22 --> n11
    n27 --> n3
    n28 --> n1
    n20 --> n27
    n14 --> n23
    n15 --> n24
    n7 -->|"3A4 (EDI  855)
Order Confirmation E2Open"| n22
    n3 -->|"MDG feeds data to S4"| n28
    n17 --> n26
    n29 -->|"3A4  (EDI 850) E2Open"| n6
    n13 --> n14
    n23 -->|"Yes"| n16
    n30 --> n18
    n24 -->|"Yes"| n17
    n24 -->|"No"| n30
    n12 --> n22
    n19 -->|"All PO’s sent
 to WebSuite for viewing"| n30
    n18 --> n26
    n25 -->|"No"| n19
    n5 --> n9
    n1 --> n31
    n4 --> n31
    n27 --> n4
    n31 --> n5
    n9 --> n10
    n29 --> n13
    n25 -->|"Yes"| n15
    n26 --> n8
    n8 --> n21
    n23 -->|"No"| n25
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 startEvt
    class n21 endEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV1uP2jgU_itWqhGtBGquJPCwK25pR-p00NCLqs4-mMQBa0KctR2Y2Rn--x6TOJAUdrddHpB8zvm-c3eSZyNiMTGGxtXVM82oHKLnjlyTDekMUWeJBel0USn4gjnFy5SIjrJJWCYX9K-DmeXmj8pMyUK8oemTki7IihH0-bqLRgBMu0jgTPQE4TTpdDs5pxvMnyYsZVxZvyJBYiYHb5VqzHhM-NHANH0r8gCa0owcxY7v-m6ocIJELIsbpImXBEnU2avgUraL1pjLQ_iFIDf48SuN5RrOCU4FAZu13KQf8JKkKkfJCyWLCr7VxaBC-cmgYIscRzRbgdw1QcRx9nAUeeZ-j_ZXV_dZ7RR9uLvPEPyiFAsxJQkSEsSzrUQJTdPhK3cyCj2zKyRnD2T4yp75U8fuRiqTIaRudlVxeztCV2s5XLI0rkx7O5XD0M4fu_xxaJtd_gT_LV8ki4-eJn07sIPa09i3JtZEe0qS5H95grryT1g8VL5mTmiH09qX5fW9ifkjn05z6vojq10nwrc0IiekYRg6s2OpZn3PMi-TjkOnb05apCssyQ4_HQkHE7cmDD0_tPyLhKW_dpTFcs5ZpAmdmRd6NaE_tsKRfZHQHVluUEUIPCuO8zUas-Iwy2iU56LUqV9mfb837khE6JYgmm1JJhkYcfJnQYQECZqnOMtgDtH7Ynlv_HECtQEaEhmt0RRLjBLONmiRExI3zZzabHx7c2J6M33XNHRrw-s6kJhscBaXgPG3pr13EvrnPIYWCLSlGM2n71uBmq_BNMHDBPfyFNp0V6V3R0TOMkGQqjURAhxTSYFIpfDmlMF_ftYMmHO2Ez2cSpRjjtOUpO_K9t8b-_0pKPgFkGOdBdEsSgsBmf6Agl1stXr2KAnPcIrmcCNkhIu3aFHkeUoJRyee-lCT-S2qKhgjLGuzZvl8MLxVdycaRQ8Z26UkXsH9nUnYJfiTDC3euk1IoLgJTxjfHH2PIkm3UF8iWu2xju0RkuUIoioO_YwP5MegGi3pHwulHjm9JVyaMDvk8b9XajGaq9gR9F2SFIVqR2Do5gWHSxbGAuYE3Re2aTlHWVmJk0AG378f41ihCSfguMEBkZ_ma5lNxGew6txMTbeDQso4VSuqEhdrtkPzO6QWYCFZ9IBSsoVnSZvOatIBAp5bW8Lr-i17EwaLfNsG2q3I1wR80EQxQAicHaZCoBzyrW-BmAi6ytpMTpPpC06p6h_6AjVnHMk1Z8Vqje5YIRWJPDz32yTuhXDqAaICzewZus1JBs1UHHGbw2ty3EAOkHhHHAoh8Qq8tyH9JmQBIdeQma2ctRF-EzG2x6riCV2h18r8E3mUb9qYoNWk28NcDUS9Q1_JclFQSdrAwT-EBy9CS7jv7HkLZNs_uxslzDkPqxtQlgPNytr_3oa7_wKH_qla1a1ror3z6PcwgaOP19O2-eBXLlfz50D1jQE7i3q939TOaIFVCuxBJbD9SqDP1TGozv3y7Gt1pbesFt7R56Ay0OcqAlszWG4l0AjLqwRuJTgwvtwbzshFr2fTa4QCz4M7tLzCJmpk-QZLCpeDHvQXFVkFdyo4PKhRAo91gWL18Fab5JaWOjdL597XwQ5OXJe-A898c-pGm1pOlaeO2tZ-v6kr4kVtqA5IN0H7td22qd_WfGQHhWNqd7ovdSN1qKM0ba0lWJwsJoKnGbxfkN3hDmlwBu30vaZ3Sw9J1SF9rGbI0T12W2c9E7o0TgXwqvOgqofZKLuqaTuQukAaalfzqEupU7DaXahSsL2TN1Tl-eQ9uqGBTbmosi6r7Msq57LKvazyLqv6l1X-ZVVwWXW5GrC1-sOsKbeqj6im1NZfEk2xc17snhd758X982L_vDg4Lx6cFcNinhVbWmx0jQ2Bu4bGxvDZOHz-G0MjJgkuUmnsuwYuJFs8ZZExPHwmG-X735RieFHblML937fjBm8=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E-72C-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T — E2E-72C-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | **Tasks**: 19 | **Gateways**: 10

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
        n1["Receive inventory request in Planning Hub"]
        n2["Fetch Data from Speed"]
        n3["Fetch BOM Data from MDG"]
        n4["Fetch Inventory demand from BY"]
        n5["Receive Updates via PDH"]
        n20(["fa:fa-play Request Response Process Initiated"])
        n27{{"fa:fa-arrows-alt parallelGateway"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n31{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n6["PO Received at Supplier"]
        n7["Order Acknowledgement sent to S/4"]
        n8["Perform Supplier Activities"]
        n21(["fa:fa-stop PO Posted to Supplier"])
        n26{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4  Intel Foundry Purchase Req – Purchase Order 
        n9[["fa:fa-cog Create Purchase Req"]]
        n10[["fa:fa-cog Use MD04 Fiori App to show PR and Stock levels"]]
        n11[["fa:fa-cog PR converted to Sub-Con PO"]]
        n12[["fa:fa-cog Check if PR Approved as per Planning design"]]
        n13[["fa:fa-cog Validate Vendor through Routing tables"]]
        n14[["fa:fa-cog Check if Supplier is E2E Open enabled"]]
        n15[["fa:fa-cog Move PO's to Staging"]]
        n16[["fa:fa-cog Send PO's to E2Open"]]
        n17[["fa:fa-cog B2B config (OpenText)"]]
        n18[["fa:fa-cog PO’s sent to WebSuite"]]
        n19[["fa:fa-cog Send PO's to Ariba P2P"]]
        n22{{"fa:fa-code-branch exclusiveGateway"}}
        n23{{"fa:fa-code-branch Supplier E2Open Enabled?"}}
        n24{{"fa:fa-code-branch Supplier is B2B enabled"}}
        n25{{"fa:fa-code-branch Has ANID ?"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n10 --> n12
    n11 --> n29
    n27 --> n2
    n2 --> n28
    n6 --> n7
    n22 --> n11
    n27 --> n3
    n28 --> n1
    n1 --> n31
    n14 --> n23
    n23 -->|"No"| n25
    n15 --> n24
    n7 -->|"3A4 (EDI  855)
Order Confirmation E2Open"| n22
    n3 -->|"MDG feeds data to S4"| n28
    n17 --> n26
    n26 --> n8
    n29 -->|"3A4  (EDI 850) E2Open"| n6
    n23 -->|"Yes"| n16
    n24 -->|"Yes"| n17
    n18 --> n26
    n29 --> n13
    n24 -->|"No"| n30
    n12 --> n22
    n8 --> n21
    n25 -->|"Yes"| n15
    n25 -->|"No"| n19
    n31 --> n5
    n4 --> n31
    n27 --> n4
    n20 --> n27
    n5 --> n9
    n9 --> n10
    n13 --> n14
    n30 --> n18
    n19 -->|"All PO’s sent
 to WebSuite for viewing"| n30
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 startEvt
    class n21 endEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV1uP2jgU_itWqopWAjVXEnjYFbe0I3U6aOhFVdkHkzhgTYiztgMzO-W_7zGJA0lhd9vlASnnnO87Vx8nz0bEYmIMjZcvn2lG5RA9d-SGbElniDorLEini0rBZ8wpXqVEdJRNwjK5oH8dzSw3f1RmShbiLU2flHRB1oygTzddNAJg2kUCZ6InCKdJp9vJOd1i_jRhKePK-gUJEjM5eqtUY8Zjwk8GpulbkQfQlGbkJHZ813dDhRMkYlncIE28JEiizkEFl7J9tMFcHsMvBLnFj19oLDfwnOBUELDZyG36Hq9IqnKUvFCyqOA7XQwqlJ8MCrbIcUSzNchdE0QcZw8nkWceDujw8uUyq52i9_fLDMEvSrEQU5IgIUE820mU0DQdvnAno9Azu0Jy9kCGL-yZP3XsbqQyGULqZlcVt7cndL2RwxVL48q0t1c5DO38scsfh7bZ5U_w3_JFsvjkadK3AzuoPY19a2JNtKckSf6XJ6gr_4jFQ-Vr5oR2OK19WV7fm5g_8uk0p64_stp1InxHI3JGGoahMzuVatb3LPM66Th0-uakRbrGkuzx04lwMHFrwtDzQ8u_Slj6a0dZrOacRZrQmXmhVxP6Yysc2VcJ3ZHlBlWEwLPmON-gMSuOs4xGeS5Knfpl1relcU8iQncE0WxHMsnAiJM_CyIkSNA8xVkGc4jeFaul8ccZ1AZoSGS0QVMsMUo426JFTkjcNHNqs_Hd7Znp7fRt09CtDW_qQGKyxVlcAsZfm_beWeif8hhaINCOYjSfvmsFar4C0wQPE9zLU2jTfZXePRE5ywRBqtZECHBMJQUilcLrcwb_-VkzYM7ZXvRwKlGOOU5Tkr4t2780DodzUPALIMe6CKJZlBYCMv0BBWex1erZoyQ8wymaw0bICBdv0KLI85QSjs489aEm8ztUVTBGWNZmzfL5YHindicaRQ8Z26ckXsP-ziScJfiTDC3euE1IoLgJTxjfnnyPIkl3UF8iWu2xTu0RkuUIopozAV04cp9ianSkf6qTunF6K9iZMDrk8b8XajGaq9ARtF2SFIXqiMDMzQsOOxamAsYELQvbtJyTrCzEWSCDb99OcazRhBNw3OCAyM_Ttcwm4hNY3U5NF4WUcarOp0pbbNgeze-Rmv6FZNEDSskOLpI2mdUkAwRcWjvC6-qtehMGp_iuDbRbcW8I-KCJYoAQODuOhEA5ZFuvgJgIus7aTE6T6TNOqTqM6DNUnHEkN5wV6w26Z4VUJPJ46bdJ3Cvh1NNDBZrZM3SXkwxaqTjiNofX5LiFHCDxjjgWQuI1eG9D-k3IAkKuITNbOWsj_CZibI9VxRO6Rq-U-UfyKF-3MUGrSXfHqRqI-gB9IatFQSVpAwf_EB68Ba1g2dnzFsi2f_ZklDDnMqxuQFkONCtr_3sb7v4LHPqnalW3ron2LqPfwQSOPtxM0Q_uBr-yW82fA9UbA84s6vV-U6dGC6xSYA8qge1XAv1cPQbVc7989rW60ltWC-_o56Ay0A4rdf3sVg5qgKME35fGB7Y0vquSakuvsnQrgV8ZOiMXvZpNbxAKPA92a7naJmqY-RZLCmtDHwHFpzPTfuD-Rgnc9gLF6k5XZ8wtLXXOlq5JX8dYVUEb2IOzUMpYAs98fe62307vq9od39XR1Rq3rdFFtoK2_0FVVKeNrYrmmBqq-6ez1lR1v7y2V6-tqTgtPSJO1UNt6LZaqkdA98muhs7W-VSN1Hw6mTpmpxJoAkdPbd0QXe9Rmra2EFic7SEENze8S5H9cWWeFeb4gqpcn71GNzRwUq6qrOsq-7rKua5yr6u866r-dZV_XRVcV12vBrRQf5c15Vb1DdWU2vpDoil2Lovdy2Lvsrh_WexfFgeXxYOLYpizi2JLi42usSWwU2hsDJ-N49e_MTRikuAilcaha-BCssVTFhnD41eyURxf56cUw4vathQe_gaaUQYI" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-72-_Intel_Foundry_-_Request_and_Response_process_with_planning_integration_(Process_for_Type_A_a, E2E-72A-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T, E2E-72B-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T, E2E-72C-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | |
| External Partners/
Supplier
 | E2E-72-_Intel_Foundry_-_Request_and_Response_process_with_planning_integration_(Process_for_Type_A_a, E2E-72A-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T, E2E-72B-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T, E2E-72C-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | |
| SAP S/4  Intel Foundry
Purchase Req – Purchase Order
 | E2E-72-_Intel_Foundry_-_Request_and_Response_process_with_planning_integration_(Process_for_Type_A_a, E2E-72A-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T, E2E-72B-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T, E2E-72C-_FTS_-_Intel_Product_-_Request_and_Response_process_with_planning_integration_(Process_for_T | |

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

#### 4.2.1 Current-State — Current-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E72CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E72CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E72CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E72CDAA_e_g_XEUS -.-> E2E72CDAD_e_g_Azure_SQL
    end
    style E2E72CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E72CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E72CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E72CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E72CDAA_e_g_MES_300 -.-> E2E72CDAD_e_g_SAP_HANA
    end
    style E2E72CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E72CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E72CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9P2kAUx_-VyxnCloCrYGE20eRoyzSpxlncltilOdpXuHi0TXtVEPnfd9cCbkid8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHHoArB0-SylOG_qAZo2MOeVNlR0ksXPZUChzp6VyFKduQzhhfKKsLkwTQ7UULEZnImysVwZPHYEozUWoUOVzS-U8Wiqk8R5TnIGOmYsYdOgauComsULZYdu-mNGDxRBq7ujRlNL5_MR3rqxVaNRpevC2BRgMvRnIFnOa5BRGiaTpI5ihinBsHA90aDoetXGTJPRgHmtbvD3rrY_tR9WR00nkrSHiSKXfX0nf1wrG54Gs5ols90t_Kdey-1e3Uyh0NdLuj7chBwl_aGw4H-kDf6pmmJletXq-n3F5cKebFeJLRdIps2UbHtIjp-OBPfPJUZOC73507DyMP_66i1QpZBoFgSbyFptYmnZTZv-xbVybC4eQQqd9SwDCMiunrHGun4icPe0X4tRvKZxgce0UEmnxlJVYGIRnk4c9KssT6Vheofdg-q6tUJUIcrlmIBYdaEBvYRO0tbFtT-1_YR-n8f3hdcu2fkyvyIbqXtut3NW0DWB6RPL6H8bbsG4hlDFIx7yG87mQf5E2p9zDexH4I8f6y6PT07HkNyCqZoi-IXF_I55Bx8PBz_UexMzoHJrL9u7-IBaGGLDIiiNyY5xcj2xzd3tjIsb_ZV1bNNJ2bF6vjq7mTNOUsoMq7f3SOb9XMyaKCqpt4_4gc35bydhy2k6jtsAgq-erK2DuO6g039HW1t_RPTk5eocctPINsRlmIjSUub3z5fxFCRAsu8KqFaSESdxEH2CgvZVykIRVgMSqJzirj6g_ylfVd" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E72FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E72FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E72FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E72FDAA_e_g_XEUS -.-> E2E72FDAD_e_g_Azure_SQL
    end
    style E2E72FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E72FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E72FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E72FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E72FDAA_e_g_MES_300 -.-> E2E72FDAD_e_g_SAP_HANA
    end
    style E2E72FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E72FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E72FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9P2kAUx_-VyxnCloCrYGE20eSg7TSpxlncltilOdpXuHi0TXtVEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHHoArB0-SylOG_qAZo2MOeVNlR0ksXPZUChzp6VyFKZtNZ4wvlNWFSQLo9qKFiEzkzZWK4MljMKWZKDWKHC7p_CcLxVSeI8pzkDFTMeMOHQNXhURWKFssu3dTGrB4Io1dXZoyGt-_mI711QqtGg0vrkug0cCLkVwBp3luQoRomg6SOYoY58bBQDdt227lIkvuwTjQtH5_0Fsf24-qJ6OTzltBwpNMubumvq0XjocLvpYjutkj_VquY_XNbmev3NFAtzralhwk_KU92x7oA73WGw41ufbq9XrK7cWVYl6MJxlNp8iSbXRskwwdH_yJT56KDHz3u3PnYeTh31W0WiHLIBAsiWtoam3SSZn9y7p1ZSIcTg6R-i0FDMOomL7OMbcqfvKwV4Rfu6F8hsGxV0SgyVdWYmUQkkEe_qwkS6xvdYHah-2zfZWqRIjDNQux4LAXxAY2UbuGbWlq_wv7KJ3_D69Lrv1zckU-RPfScv2upm0AyyOSx_cwrsu-gVjGIBXzHsLrTnZB3pR6D-NN7IcQ7y6LTk_PnteAzJIp-oLI9YV82oyDh5_3fxRbo3NgItu_-4tYEGrIJCOCyM3w_GJkDUe3NxZyrG_Wlblnms7Ni9Xx1dxJmnIWUOXdPTrHN_fMyaSCqpt494gc35LyVhy2k6jtsAgq-erK2DmO6g039HW1a_onJyev0OMWnkE2oyzExhKXN778vwghogUXeNXCtBCJu4gDbJSXMi7SkAowGZVEZ5Vx9QduSfWH" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-72-R001 | Report | IP operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-72-C001 | Conversion | Legacy data migration for IP | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-72.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E72C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E72C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E72CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E72CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E72C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E72CMW_e_g_Azure_Service_Bus
    E2E72CMW_e_g_Azure_Service_Bus --> E2E72C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTuek74M_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUP0yo9cQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-72.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E72F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E72F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E72FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E72FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E72F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E72FMW_e_g_Azure_Service_Bus
    E2E72FMW_e_g_Azure_Service_Bus --> E2E72F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTudk4IM_9UeO55_q-jZrAG0Eh9NDJH1I-iShYRiywp8S_HLuvE-jlePL0NFDHmy-Zin4HqRPNADfyviHrzvuFEw5Cq1RSKIK2rJqVXbbydn7MRe-w-S8R6K3vcXgrCBWALQGXEzSo94F7RUO7x4doaEdB_Lvp3d1eXFEe0VW1ZVFPojIe312BZVj13sbazmbnRdBMpnXQ_kcUAZj7W2PEtvEX2FUkmot1JbWTZMfA5a7NeIDfd-Ib4eam1D9O5O806wuTKVGH5qD6Mh1fjiX9je61PVlb1dby0wSRgOswJ80l-uPHqotNCrb5Mu2cX3bqXaIrY4fJxLyFqlWvghxrophPGmTMwkkzThsujRcp5Hzv9UmpaiFKO_CttRvI-z5-fnOWaY1tDmkc0yJZiy1_PaSdx-BEGdMaKuGhjMRe4so0Iz8UtGyRG4UbIplEeaFcfUPGao9iQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 5.3 Change Impact Summary

| Change Type | Flow Chain | Detail |
|-------------|-----------|--------|
| **UNCHANGED** | e.g. MES Route to ICOST | No change |

**Totals**: 0 new - 0 removed - 0 modified - 1 unchanged

### 5.4 Component Overview

#### System Inventory

| System | IAPM ID | Status |
|--------|---------|--------|
| e.g. MES 300 | - | N/A |
| e.g. XEUS | - | N/A |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-72-I001 | Interface | IP inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-72-E001 | Enhancement | IP custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-72-F001 | Form/Report | IP operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### 6.1.1 Current-State — Current-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E72CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E72CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E72CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E72CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E72CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E72CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E72CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E72CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhCRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1tslZKpWrzB4t77_z49Vl4j1OeAXbwYLCnBRUO2mtiDRvQHKQtSQ2ajrQa0qaiYjeHO2AqwTjvM13pd1JRsmRQa2p1zgsR0YcOMByVW1WmtJBsKNspNYIVB3RzpSNXLmRaqyoYv0_XpBIdo6nhmmx_0EysZZwTVoOsWYsNm5MlMLWRqBqlFdJ9VJKUFispjgwpVaS4PUq20baoHQzi4rAF-ubFBZIjZaSuZ5AjUpYe36KcMuacefYsDEO9FhW_BefMMCYTb_wUfrhXnhyz3OopZ7xSaWtmv-aVjIgj0J8GY__jAWhNp4HlvwRaR-DQswPTeAUEzo68MPRszz7wfN-Q46TB8Vil46In1s1yVZFyjQIzmJj-Yr5IIFkl7kNTQbIgJPoV47gxx8YwbnIw5M7nq3PUpZFKx_h3D1IjoxWkgvICzb8e1Wey25F_BjeK2WHUtwQ4jtM3vF8DRfbkTewYnDT2T8188_BRMko-u1_cxDRMqzt_NrUyOWfE_rsL0cUIqTqk6t7diOsgSizDeO6FDJEM39mOF1b_Q0feol9efnp8MjvrzocukLu4knNIGcT48eRVYR1voNoQmmFnj7s3Qr4wGeSkYQK3OiaN4NGuSLHT_ca4KTMiYEaJvJ5NL7Z_AIWLbmI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E72FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E72FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E72FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E72FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E72FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E72FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E72FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E72FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhCRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1tslZKpWrzB4t77_z49Vl4jxOeAnbwYLCnBRUO2mtiAzloDtJWpAZNR1oNSVNRsVvAHTCVYJz3ma70O6koWTGoNbU644UI6UMHGI7KrSpTWkByynZKDWHNAd1c6ciVC5nWqgrG75MNqUTHaGq4JtsfNBUbGWeE1SBrNiJnC7ICpjYSVaO0QroPS5LQYi3FkSGlihS3R8k22ha1g0FUHLZA37yoQHIkjNT1HDJEytLjW5RRxpwzz54HQaDXouK34JwZxmTijZ_CD_fKk2OWWz3hjFcqbc3t17ySEXEEzqb-ePbxALSmU9-avQRaR-DQs33TeAUEzo68IPBszz7wZjNDjpMGx2OVjoqeWDerdUXKDfJNf2IGy8Uyhngduw9NBfGSkPBXhKPGHBvDqMnAkDufr89Rl0YqHeHfPUiNlFaQCMoLtPh6VJ_Jbkf-6d8oZodR3xLgOE7f8H4NFOmTN7FjcNLYPzXzzcOH8Sj-7H5xY9Mwre786dRK5ZwS--8uhBcjpOqQqnt3I679MLYM47kXMkQyfGc7Xlj9Dx15i355-enxyey8Ox-6QO7ySs4BZRDhx5NXhXWcQ5UTmmJnj7s3Qr4wKWSkYQK3OiaN4OGuSLDT_ca4KVMiYE6JvJ68F9s_qFxueg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**RICEFW Status Summary** — E2E Tower (0 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| **Total** | **0** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| **Total** | **0** |

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

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-72 — IP</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*No timeline data available for this capability.*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**RAID Summary:** 15 open items (0 capability-specific, 15 tower-level), 56 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 3 | 3 |
| P2 - Medium | 0 | 10 | 10 |
| P3 - Low | 0 | 2 | 2 |
| **Total** | **0** | **15** | **15** |

**Other E2E Tower RAID Items** (15 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03681 | Risk | P1 - High | ITC Execution: Planning run availability - Prerequisite for ... | In Progress | E2E | 2026-03-27 |
| 03762 | Risk | P1 - High | FTS-IF (esp SCP) related test cases/sequencing are not accur... | In Progress | FTS IF | 2026-04-03 |
| 01733 | Risk | P2 - Medium | Tariffs impacts Item/BOM design which is impacting ERP/SCP (... | In Progress | E2E | 2026-03-06 |
| 03592 | Risk | P2 - Medium | Lack of Defined IMO Owner for CBA Mask Billing and Materials... | In Progress | E2E | 2026-03-27 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03628 | Risk | P2 - Medium | R3 Returns Rework Process Causing Finance Double Counting in... | In Progress | E2E | 2026-03-27 |
| 03642 | Issue | P2 - Medium | E2E Process with Anafi on order/invoice point.  Need IFS SC ... | In Progress | E2E | 2026-03-24 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03753 | Risk | P2 - Medium | PDF-SMH IF test cases are not available in JIRA | To Be Reviewed | B-Apps | 2026-03-25 |
| 03756 | Risk | P2 - Medium | LE101-1001 Operation Support Ownership for SIMS/Tester Front... | In Progress | E2E | 2026-04-24 |
| 03769 | Action | P2 - Medium | Need a Labs SPOC owner to define IP Labs enterprise and mate... | In Progress | E2E | 2026-04-17 |
| 03216 | Action | P3 - Low | Mask Expense vs. Invoice | In Progress | E2E | 2026-03-06 |
| 03315 | Risk | P3 - Low | BPMG – SCP L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-03-27 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 1 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 1 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*E2E-72 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

