<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-88 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-88 R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme** within the IAO program. It includes 6 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-88 - R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: "loose"` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-88 - R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-88 Process Migration | Migrate R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-88 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **6 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-88 R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-88A_R3_Portfolio_and_Project_Management | E2E-88A_R3_Portfolio_and_Project_Management | Boundary Apps, SAC, SAP S/4 (IP & IF) | 15 | 6 |
| 2 | E2E-88B_R3_Project_Systems_1 | E2E-88B_R3_Project_Systems_1 | Boundary Apps, SAP S/4 (IP & IF) | 25 | 14 |
| 3 | E2E-88C_R3_Procurement | E2E-88C_R3_Procurement | Boundary Apps, External Partners/
Supplier
, SAP S/4 (IP & IF) | 24 | 11 |
| 4 | E2E-88D_R3_CFIN | E2E-88D_R3_CFIN | Boundary Apps, CFIN, MBC, SAP S/4 (IP & IF) | 15 | 10 |
| 5 | E2E-88E_R3_SAP_Transportation_Management | E2E-88E_R3_SAP_Transportation_Management | Boundary Apps, External Partners/
Supplier
, SAP S/4 (IP & IF) | 12 | 6 |
| 6 | E2E-88F_R3_Project_Systems_2 | E2E-88F_R3_Project_Systems_2 | SAP S/4 (IP & IF) | 9 | 6 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-88A_R3_Portfolio_and_Project_Management — E2E-88A_R3_Portfolio_and_Project_Management

**Swim Lanes**: Boundary Apps · SAC · SAP S/4 (IP & IF) | **Tasks**: 15 | **Gateways**: 6

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps
        n1["Convert PMIS/Hexagon Strategic Capital Plan to Tactical Operational Plan"]
        n2["Plan SAP IBP Supply Planning"]
        n3["Create/Approve PMIS/Hexagon Project"]
        n17(["fa:fa-stop Input for Supply Planning Received"])
        n20{{"fa:fa-code-branch Construction Project?"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAC
        n14["Project Financial Planning"]
        n15["Perform Strategic Capital Planning / Budgeting"]
    end
    subgraph SAP S/4 (IP & IF)
        n4["Load Capital budgets into Portfolio/Buckets"]
        n5["Create Project"]
        n6["Distribute Original Budget to Item"]
        n7["Create Capital Funding structure Portfolio/Buckets"]
        n8["Create Portfolio item (Proposal)"]
        n9["Evaluate Proposal (Scoring and Prioritization)"]
        n10["Approve Proposal"]
        n11["Convert to Project (PPM Item"]
        n12["Route for Budget Approval"]
        n13["Approve Project Budget"]
        n16(["fa:fa-play Initiate Capital funding structure"])
        n18(["fa:fa-stop Budget allocated to portfolio line item"])
        n19["E2E-88B R3 Project System"]
        n21{{"fa:fa-code-branch exclusiveGateway"}}
        n23{{"fa:fa-arrows-alt parallelGateway"}}
        n24{{"fa:fa-arrows-alt parallelGateway"}}
        n25{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n7 --> n24
    n8 --> n9
    n9 --> n10
    n21 --> n11
    n11 --> n14
    n14 --> n12
    n13 --> n25
    n25 --> n5
    n25 --> n6
    n24 --> n4
    n24 --> n15
    n16 --> n7
    n10 --> n21
    n12 --> n13
    n15 --> n23
    n22 --> n2
    n22 --> n3
    n2 --> n17
    n20 -->|"Yes"| n1
    n1 --> n22
    n3 --> n21
    n6 --> n18
    n20 -->|"No"| n8
    n4 --> n23
    n23 --> n20
    n5 --> n19
    class n16 startEvt
    class n17 endEvt
    class n18 endEvt
    class n19 startEvt
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVttu4zYQ_RVCi9RZwEZ0tWQ_tPBNXQNJ14i3LYq6D7RE2WxoUaAox16v_71DifJFcVB064cgPJw5Z-aQI-lgRDwmRt-4uzvQlMo-OrTkmmxIq49aS5yTVhtVwG9YULxkJG-pmISnck6_lmGWm-1UmMJCvKFsr9A5WXGCfp220QASWRvlOM07ORE0abVbmaAbLPYjzrhQ0R9IkJhJqaa3hlzERJwDTNO3Ig9SGU3JGXZ813dDlZeTiKfxFWniJUEStY6qOMZfozUWsiy_yMkT3v1OY7mGdYJZTiBmLTfsES8JUz1KUSgsKsS2NoPmSicFw-YZjmi6Atw1ARI4fTlDnnk8ouPd3SI9iaLH50WK4BcxnOdjkqBcAjzZSpRQxvof3NEg9Mx2LgV_If0P9sQfO3Y7Up30oXWzrcztvBK6Wsv-krNYh3ZeVQ99O9u1xa5vm22xh78NLZLGZ6VR1w7s4KQ09K2RNaqVkiT5X0rgq_iC8xetNXFCOxyftCyv643Mt3x1m2PXH1hNn4jY0ohckIZh6EzOVk26nmW-TzoMna45apCusCSveH8m7I3cE2Ho-aHlv0tY6TWrLJYzwaOa0Jl4oXci9IdWOLDfJXQHlhvoCoFnJXC2RkNelHcZDbIsr_bUL7X-XBgjnm4J3KnZ03T-8Ins8IqnaC4FNLWiERrhjErM0IzhFEmOvuBI0giAzxmBGMpTvbkw_rpgtoG5TJkPZmg6nKF5kWVsX0amcLGvox1VhyAg-QAVCr4l1-WAG3-TSF4nWf49pCW4n-BOLnmGpmlWwL3koimGnklE6JbEQPDxskjzcKgZ1IOrs4TRi9YILAF7i0h1V2v_tDCOx8tc-5yLheCveQcziTIsMGOE_VzdiXMSTE3jUOaD0WU3rnKs0kIhTaEQqp1965flqWAioNfNO2dV9v2AhkW8IvKS4FYhcDwPLrqfztAPaBpeWqSqeuQ4PnEvS8Ic0RQuw4wLmXBG-cOwiF4Avi7TOx3r7RPswv6YgtV0WUDMZ0FXVF2nqmh126aSbK5z_DNnXVIIl1t1W51ZIci_1RVc1FVHIgpS6B7qzHiO2cfrjB5kTLaYFbqXMgbdzyMulDJOY0ApLCT9Wg5FI98ygeB0tXV-I-RyGJW3-i7cz2ZPN3yw1IQ9c-WbuvHaskriDbVzrV7yVhmNwO55pDIGj7QpvMTppddJ0-vGSFlBYyh1YTAUPAKiWLWWnUxXb9_S-SZNabg96QTBED07p6Ln-_yNE7Z1e4rJLmJFDmP_ZharNOe_DXCV5H5Pkvedj4rUR53Oj0pVr4Nq3dPLXrW09PsDnNCAfu3BPxqoCSxXA3YNOFrCqzm8Cmiuu_VaM7iNtVUnWN0K8Ou1qRVORdk6w6kBLWHXgK0j7Mb6tK8Jagm7lPi2MP4gMOnfYKdm1jw1kdMoRZdqBU2iX3jJU-Nus8CaqHZed2D1Lt7kpRX1h9k17uuPqGs0uIn2bnNAqfq74xq2bsP2bdi5Dbu3Ya-GjbaxIWKDaWz0D0b5QQ8f_TFJcMGkcWwbuJB8vk8jo19--BpFFkPmmGJ442wq8PgPKIvDnQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-88B_R3_Project_Systems_1 — E2E-88B_R3_Project_Systems_1

**Swim Lanes**: Boundary Apps · SAP S/4 (IP & IF) | **Tasks**: 25 | **Gateways**: 14

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TD
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps
        n1["Receive WBS Detail Information"]
        n2["Initiate Procurement"]
        n3["Receive Information Hexagon/Smart Reference Design (SRD)"]
        n4["Initiate Change Order"]
        n5["Approve Change Order"]
        n35{{"fa:fa-arrows-alt parallelGateway"}}
        n36{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n6["Create Project"]
        n7["Create Work Breakdown Structure and NWA"]
        n8["Assign Cost Centre/Operative Indicators"]
        n9["Define other Objects and Fields (Including EUID from EMS"]
        n10["Establish Original Budget at Level 1 WBS"]
        n11["Establish Original Project Budget at Lower Level WBS Element"]
        n12["Analyze Budgetary Needs for Project"]
        n13["Release Budget"]
        n14["Release WBS Element/NWA"]
        n15["Issue Material"]
        n16["Post Capital Labor"]
        n17["Purchase Requirement/Purchase Orders"]
        n18["Valuate Goods Receipt"]
        n19["Reserve Material"]
        n20["Receive Invoice"]
        n21["Update Interest/Overheads"]
        n22["Process Month/End Transactions"]
        n23["Run Periodic Reports"]
        n24["Obtain Acceptance to place Assets in Service"]
        n25["Purchase Documents"]
        n26(["fa:fa-stop Purchase Documents Updated"])
        n27["E2E-88C R3 Procurement"]
        n28["E2E-88F R3 Project Systems 2"]
        n29["E2E-88F R3 Project Systems 2"]
        n30["E2E-88A R3 Portfolio and Project Management"]
        n31{{"fa:fa-code-branch Additional Breakdown Required?"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n33{{"fa:fa-code-branch Additional Budgetary Control Needed?"}}
        n34{{"fa:fa-code-branch exclusiveGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
        n39{{"fa:fa-arrows-alt parallelGateway"}}
        n40{{"fa:fa-arrows-alt parallelGateway"}}
        n41{{"fa:fa-arrows-alt parallelGateway"}}
        n42{{"fa:fa-arrows-alt inclusiveGateway"}}
        n43{{"fa:fa-arrows-alt inclusiveGateway"}}
        n44{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n6 --> n7
    n7 --> n37
    n37 --> n8
    n11 --> n32
    n32 --> n33
    n33 -->|"Yes"| n12
    n12 --> n13
    n34 --> n14
    n42 --> n16
    n42 --> n18
    n15 --> n43
    n16 --> n43
    n18 --> n43
    n9 --> n38
    n38 --> n10
    n19 --> n43
    n10 --> n31
    n31 -->|"Yes"| n11
    n42 --> n15
    n42 --> n44
    n43 --> n39
    n44 --> n19
    n8 --> n9
    n13 -->|"Availability 
Control 
Activated"| n34
    n42 --> n41
    n1 --> n2
    n31 -->|"No"| n32
    n33 -->|"No"| n34
    n37 --> n1
    n3 --> n4
    n35 --> n3
    n4 --> n5
    n42 --> n20
    n20 --> n43
    n5 --> n44
    n2 --> n36
    n30 --> n6
    n21 --> n22
    n22 --> n23
    n23 --> n24
    n39 --> n21
    n24 --> n28
    n14 --> n42
    n40 --> n25
    n25 --> n26
    n38 --> n29
    n41 --> n17
    n17 --> n40
    n40 --> n27
    n36 --> n41
    n39 -->|"Planning tool may vary based on Commodity"| n35
    n36 --> n35
    class n26 endEvt
    class n27 startEvt
    class n28 startEvt
    class n29 startEvt
    class n30 startEvt
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
    class n42 gateway
    class n43 gateway
    class n44 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWFtv2zYU_iuEii4dYCOiLr49bHB82QIsTRC3K4Z6D7RE2Vxk0iNpJ16a_75DmVRsVunQzA-G9emc79wPJT8GmchpMAjevn1knOkBejzTK7qmZwN0tiCKnrXQAfidSEYWJVVnRqYQXM_YP5UYTjYPRsxgU7Jm5d6gM7oUFH28bKEhKJYtpAhXbUUlK85aZxvJ1kTuR6IU0ki_ob0iLCpr9taFkDmVzwJh2MVZCqol4_QZjrtJN5kaPUUzwfMT0iItekV29mScK8V9tiJSV-5vFb0iD59YrldwXZBSUZBZ6XX5G1nQ0sSo5dZg2VbuXDKYMnY4JGy2IRnjS8CTECBJ-N0zlIZPT-jp7ds5r42iD-M5R_DJSqLUmBZIaYAnO40KVpaDN8loOE3DltJS3NHBm2jSHcdRKzORDCD0sGWS276nbLnSg4UocyvavjcxDKLNQ0s-DKKwJffw7dmiPH-2NOpEvahXW7ro4hEeOUtFUfwvS5BX-YGoO2trEk-j6bi2hdNOOgq_5nNhjpPuEPt5onLHMnpEOp1O48lzqiadFIcvk15M40448kiXRNN7sn8m7I-SmnCadqe4-yLhwZ7v5XZxI0XmCONJOk1rwu4Fng6jFwmTIU561kPgWUqyWaELsa16GQ03G3W4Zz4cf54HtzSjbEfRp4sZGlNNWIkueSHkmmgm-Dz480g-AvlLmGsGESPj4lbCLHN9KhUfsR5RoV_pA1kKfj5bmx6-pQWVlGcUrCq25Ojd7Hb84ylTcmxvtCJ8SdG1GeRTsRTEIDIpdt-SitPHx3lQkEFB2kRKca_apNRoQyQpS1r-cqjiPHh6OlbqfJ8SDIeX-9nwBs3OE_Tu8gb9gC6nPx6xd8DxkaQ2m3_RzMtk9_n-JyHv0AX8vsvFPUczWCiZhvQjwnP0_tPwVLFnMqKqtI6E0mgERZL0_HpDJdSiqkvOMqKFVKeKfVCEFoSliAQsaomuF8YtVZmZMlrmCiLhWbnNYT2hycfLMSqkWKPJ1eyUCYdANYHFtCiZWkFB2JJxUqKLbb6kGhGNfqM7WiJsOs9Txc2qNkfHFOIefDwQmQaelA39iE3bDoFg_w-1umYW3lMKwUB7NuceH9q4pHBsWS1PIDkSODJ-_lU1sGnQS6W2FF1BLc0B5gmYRripCkU2TEOocHAIr3-x6YabrYQjAAze0r-37DB95zVYdb1XUWx64XdSbk0X_SIExFwN58YPp1-FYzbkS25G4clk7wSsUk_CVO7jJje2LjlwUKXPr3dUrijJPcciUxazRKhS6AqOidX5BJrsAxx_imRmY_gKVUW2HN2AbwL6FwLZCKl9MVOX6wVsMo6GWUY3mpgtowXalAR-wFxQaGi4OzucBp56epzmMew4k2PfRufdZ7cWlBYb9LUCOqQhB8XjkY9MFSfRpN3rjdBt_PIWjXq14NQKVs0_2ytN1wpFnnj_u8TjsBYfVuKQx0KUTFSD7pSvCCfLpg2Pn7eieeJrL6Bo2QoN85yZwpkxr1eV7dT8Z3-1Rs0k9AG2i4IWe2Ejx_9tu57xEbSVFGU16w0eJK_zoPuag6T3GqX-K5SS8DVK-DVKUaMS499MXxK_Siv5Tq36JOYd1G7_BIepveweLmN3HVugZ68xtgKRE4gsEDsgNsCXefAHhb3wxZwwTteK4lo0sUBigcRJdHygtp8egMRx4I4P9Dygbx10FLEVwKHT6PsUoVXBTgX7MWHfwdQDkjqm2JL1HeCidoD1x11il8DhDp43yYKVTO_RnLtxnfMhHAC7w_r8YrLom3bO2VpFfhTvxUEx8kvmbiRe9es8WAPu0hbD5c0G5qfCvbrADy_RqZcr10uu_LFVcNeRi8h5HjkTjjGyLka1j7a4kYshsl5GdUtZIHGkibUauUAi62fU8VooqmtqHcNubrDNXBL6pPVkdbxqHTyFKtyUhHPzAKkFlHsNL087s67NXwQ5Euahdb2GE17vD8VKPUIHVG9Mxmn7UnqKduvX4lO89wLeb8ahQs04dm9-p3DUDMfNcNIMp81wpxnuNsO9ZrjfCEP1GuHmKJPmKJPmKJM6yqAVrCm8ELI8GDwG1V9BwSDIaUG2pQ6eWgHZajHb8ywYVH-ZBNvqKWrMCLxNrQ_g079YZJaH" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-88C_R3_Procurement — E2E-88C_R3_Procurement

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4 (IP & IF) | **Tasks**: 24 | **Gateways**: 11

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps
        n1["Purchase Order Collaboration SIRFIS/Web Suite"]
        n2["Receive Information"]
        n3["Receive Manual invoices through OCR"]
        n4["Receive Incoming invoice/ B2B/OpenText/Web suite"]
        n5["ReadSoft Validation/Exception Handling based on rules setup"]
        n29{{"fa:fa-code-branch B2B or OCR?"}}
        n30{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n21["Confirm/Select Carriers"]
        n22["Organize Transport"]
        n23["Order Shipment Goods Picked (Carrier)"]
        n24["Receive Supplier invoice"]
        n32{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n6["Create Purchase Requisition with WBS"]
        n7["Approve Purchase Requisition"]
        n8["Create Purchase Order with WBS"]
        n9["Trigger GTS Check GTS Trade Compliance"]
        n10["Calculate Tax"]
        n11["Publish Purchase Order"]
        n12["Acknowledge/Confirm Purchase Order"]
        n13["Perform Inbound Delivery with House Air Waybill number HAWB"]
        n14["Receive Goods Receipt to Val. Blocked stock"]
        n15["Receive Goods Receipt from Val. Blocked to Unrestricted (Consumption upon GR)"]
        n16["Post Goods Receipt Cost against WBS"]
        n17["Create Equipment Master"]
        n18["Update Equipment Master for Bill of Material Components"]
        n19["TM Embedded"]
        n20["Post Supplier invoice"]
        n25(["fa:fa-stop Equipment Master Updated"])
        n26["E2E-88E R3 SAP Transportation Management"]
        n27["E2E-88D R3 CFIN"]
        n28["E2E-88B R3 Project Systems 1"]
        n31{{"fa:fa-code-branch Invoice Accepted?"}}
        n33{{"fa:fa-arrows-alt parallelGateway"}}
        n34{{"fa:fa-arrows-alt parallelGateway"}}
        n35{{"fa:fa-arrows-alt parallelGateway"}}
        n36{{"fa:fa-arrows-alt Based on Business Rule"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
        n39{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n7 --> n8
    n33 --> n9
    n33 --> n10
    n6 --> n7
    n9 --> n34
    n8 --> n33
    n10 --> n34
    n34 --> n11
    n11 --> n1
    n22 --> n23
    n21 --> n22
    n1 --> n12
    n12 --> n21
    n15 --> n36
    n13 --> n37
    n16 --> n35
    n35 --> n15
    n36 -->|"Based on 
Business Rule"| n17
    n18 --> n25
    n19 --> n26
    n36 --> n32
    n17 --> n2
    n5 --> n31
    n31 -->|"Yes"| n20
    n32 --> n24
    n24 --> n29
    n31 -->|"No"| n32
    n28 --> n6
    n23 -->|"ASN update via Web Suite"| n13
    n2 --> n18
    n20 --> n27
    n4 --> n30
    n3 --> n30
    n29 -->|"OCR"| n3
    n29 -->|"B2B"| n4
    n30 --> n5
    n37 --> n19
    n37 --> n14
    n39 --> n16
    n14 --> n38
    n38 --> n35
    n38 --> n39
    class n25 endEvt
    class n26 startEvt
    class n27 startEvt
    class n28 startEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWF1zokgU_StdTGWdqdJVQER92C01krFqMrFCZlJb4z600GhvsJvthsRsxv--t6FBJWS2atYHTR_uud_3AnkxAh4SY2xcXLxQRtMxemmlW7IjrTFqrbEkrTYqgK9YULyOiWwpmYiz1Kf_5GJmP9krMYV5eEfjZ4X6ZMMJ-rJoowkQ4zaSmMmOJIJGrXYrEXSHxfOMx1wo6XdkGPWi3Jq-NOUiJOIo0Ou5ZuAANaaMHGHb7bt9T_EkCTgLz5RGTjSMgtZBORfzp2CLRZq7n0lyjff3NEy3cI5wLAnIbNNd_AmvSaxiTEWmsCATj2UyqFR2GCTMT3BA2Qbwfg8ggdnDEXJ6hwM6XFysWGUUfbpdMQSfIMZSXpIIyRTg-WOKIhrH43f92cRzem2ZCv5Axu-suXtpW-1ARTKG0HttldzOE6GbbTpe8zjUop0nFcPYSvZtsR9bvbZ4hu-aLcLCo6XZwBpaw8rS1DVn5qy0FEXR_7IEeRV3WD5oW3Pbs7zLypbpDJxZ77W-MszLvjsx63ki4pEG5ESp53n2_Jiq-cAxe28rnXr2oDerKd3glDzh56PC0axfKfQc1zPdNxUW9upeZuul4EGp0J47nlMpdKemN7HeVNifmP2h9hD0bAROtmjKs7yX0SRJZHFNfZj5bWUsMwFNJQm6UROCoN1jvOYCp5Qz5C9uvYXfvSdr5Gc0JSvjzxO6BfRbEhD6SNCCRVzscta5kH0idI1ZhmNE2SOHKkiUbgXPNlt0M7s9J_XPNAd8B7NQ0rpoak27Nwlhd2Sf5r7J1745uQYc-jxK0Vcc0zD3rTvfByTJY_uIWRgrvWoxhQgQkcFCgh5Js6QW6OjlZWVEeBzhjtpwnTXMaLBVjiAulPu_r4zD4TTqXjOD7IM4kxDWVdE0RxqMVa1q831KBIN8LWG4GRGyC0VIkphCmU6dU1WccRZRsev6JCZBimZYCBCTtTBUwW7EBjPYtegOPJIJF2lNyM6FVC_4W5rsCEvRFeehREsaPECi3mvlH2q805pVfuqa1VrC-v_J8SdL5Hf76P1iiX5BC-_Dif6BSoggoARV3X1L_s6opHnln2i6RfdT_9wrF1gwH4I_NtPOpYcNNoqsNWsfgfydoJsNSFzd-Wi2JcFD_hfUISQwdzvIGKShliuzpwzhOMhiZesO72vXixlex1Rua57UBFXxJ8ED408xCTekq1vmxyTVDEsi1GzDIK7VHkGXJIYawTbJI_3IYU2jCRXoHj-vYWMhlu3WEOXHyf20pu20RYqeyk9JilKuhvRXNI153mQyhd8a23mTHQm-O-eDvi9MENiSNEjzpuVMZrti8rMEvq5uaw1sqrZZcpnWlM8UhDeYMvh9VVfTPTbCHHqlGJhrLNNXuVQt8yUJmyQRJBhNVfJ4BBAg8JCT9wRnIFWbYzNvpms0hzyHIQlrg9gr4_jxFFrO-2_lFEK6k9dOFc4q9afTZak8za15Zzico1s7n8RqlxS3DdjzeEOUqppJt6JeKurMW3yuSQwriamSgPvgX2qh-c_g0U4is7ZJzOZNsigCRpNAbXsSvlrP9pEH24w_yQ6OU5RggeOYxK_2T0Hq_wzJ-RnSoJE0LW9UU9iSjEjoUbhj1bnuzxgc_gxp1Eii7D-3OHNRp_MbLFF9tO3iPKqdTf1kxAbF2dXHUXG0-_o81Gdbn81eTcDua4VmKWFqQJ8tqzhbpQpLC1hWydCE6lwyKpWONjooAR2FXbpt6jBsp3RLU8wKyCW-r4yq1CtWK_Z3tXNKhTpwq-SbOjPW4EyhuuWWEjr15bl0uozCNrUHfxCZGyufykGFZpZJtXRSrVGd-5nn1Mqopf0svbJsLTjxP8M2zlfiI8Xo5DlThVnVQmepbBdLl9cq86AdsStXa2drpO3lD5rKs_oFeJLLL1QNo01UhdFpM0d1oGLo1JtV-Uuvqi4f1stfAqOTFwBVTf2OdY4Oqre8c9x9Ax--gY_KF5YzGAJuhM1m2GqG7Wa43ww7zfCgGXab4WEzXEVptI0dgTcTGhrjFyP_54MxNkIS4SxOjUPbwFnK_WcWGOP8Jd0o-vGSYnjQ3BXg4V92wCXz" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E-88D_R3_CFIN — E2E-88D_R3_CFIN

**Swim Lanes**: Boundary Apps · CFIN · MBC · SAP S/4 (IP & IF) | **Tasks**: 15 | **Gateways**: 10

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps
        n1["Receive File in Bank"]
        n2["Update Payment Remittance"]
        n16(["fa:fa-stop Payment Data Updated"])
    end
    subgraph CFIN
        n3["Execute Payment Run"]
        n4["Create APM Memo Record"]
        n5["Process BCM Payment Batching Based on Business Rules"]
        n6["Generate APM Payment File"]
        n7["Route to Approver"]
        n8["Correct APM Correction File"]
        n9["Reverse APP Doc Number and Memo Record Deletion"]
        n10["Fetch Payments Factory (APM, BCM, MBC Monitor)"]
        n11["Review Failed Payment Log"]
        n12["Generate Payment Proposal"]
        n13["Replicate Supplier Invoice Posting"]
        n18(["fa:fa-stop Memo Record Created"])
        n19(["fa:fa-stop APP Doc Reversed"])
        n21{{"fa:fa-code-branch Manual Approval Necessary?"}}
        n22{{"fa:fa-code-branch Approved?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch Can Be Corrected?"}}
        n25{{"fa:fa-code-branch exclusiveGateway"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch Reversal or Reprocessing?"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph MBC
        n14["Multi-Bank Connectivity (host-to-host)"]
        n15["Multi-Bank Connectivity (host-to-host)"]
    end
    subgraph SAP S/4 (IP & IF)
        n17(["fa:fa-stop Payment Details provided back to Source System (IP/IF)"])
        n20["E2E-88C R3 Procurement"]
    end
    n12 --> n3
    n3 --> n28
    n4 --> n18
    n5 --> n21
    n21 -->|"No"| n23
    n7 --> n22
    n23 --> n6
    n25 --> n5
    n24 -->|"No"| n26
    n9 --> n19
    n10 --> n29
    n26 --> n9
    n29 --> n11
    n28 --> n4
    n11 --> n27
    n27 -->|"Reversal"| n26
    n2 --> n16
    n6 --> n14
    n29 --> n2
    n8 --> n25
    n13 --> n12
    n29 --> n17
    n20 --> n13
    n21 -->|"Yes"| n7
    n1 -->|"PAIN.002 (Pay-load file)"| n15
    n14 -->|"PAIN.001 (Pay-load file)"| n1
    n28 -->|"Reprocessing"| n25
    n30 --> n8
    n22 -->|"Yes"| n23
    n22 -->|"No"| n24
    n15 --> n10
    n27 -->|"Reprocessing"| n30
    n24 -->|"Yes"| n30
    class n16 endEvt
    class n17 endEvt
    class n18 endEvt
    class n19 endEvt
    class n20 startEvt
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV11v6kYQ_SsrX6UkEvT6ExseWoHBV5FChEJvq6r0YbHXwYrxWus1Cc3lv3cW7xpsnIemPCTe4zNnZmdnhuVdC2lEtLF2c_OeZAkfo_ce35Id6Y1Rb4ML0uujCvgdswRvUlL0BCemGV8l_5xohp2_CZrAArxL0oNAV-SZEvT9vo8mYJj2UYGzYlAQlsS9fi9nyQ6zg09TygT7C_FiPT55k6-mlEWEnQm67hqhA6ZpkpEzbLm2awfCriAhzaKGaOzEXhz2jiK4lL6GW8z4KfyyIAv89kcS8S2sY5wWBDhbvksf8IakYo-clQILS7ZXyUgK4SeDhK1yHCbZM-C2DhDD2csZcvTjER1vbtZZ7RQ9PK0zBJ8wxUUxIzEqOMDzPUdxkqbjL7Y_CRy9X3BGX8j4izl3Z5bZD8VOxrB1vS-SO3glyfOWjzc0jSR18Cr2MDbztz57G5t6nx3gb8sXyaKzJ39oeqZXe5q6hm_4ylMcx__LE-SV_YaLF-lrbgVmMKt9Gc7Q8fVrPbXNme1OjHaeCNsnIbkQDYLAmp9TNR86hv6x6DSwhrrfEn3GnLziw1lw5Nu1YOC4geF-KFj5a0dZbpaMhkrQmjuBUwu6UyOYmB8K2hPD9mSEoPPMcL5FU1qeahlN8ryo3olPZvy11p5ISJI9QUGSEpRkaArVt9b-vmCZwPqeR7BLtMSHHck4eiK7hHOchaRJNYa3QI7xOMaDgtO8NphhjlElEoHJXWUDpdSK1A_uHy_0LFCbv5GwvPRdZk2nNpB8RkR8k-UCLciOQoAhdHyT5wBP5JUUBZr6i1pwinm4hWaDh4JEiEIOygLGAtCeShhRTZUhqHwjGWHKn5IRCWxSXZFeKmLnVKSe0T1hTYonYqeMkZCfxORzAkFc641OxwUahfC8RDOokcdytyEM4Sy63DiakZQIldbx6KAQENiuirpAAQ45hdK4Bfd9kZc-Wkx9tKAwvym7awlUFbNPyCsYQoBRvf0H-tzimpeZUjQ4gJwWOG1xrZNuniahIK_KHB5hW_fZnkK_oiUtOJxQy8hrFdtlAqqCuKi1ymTUMlFplGlt803j_V3xxVfbYAPDGbK3wFmJU3mm8PBIRFVBh_261o7HSwGzW0BWQ3TFt7r55C1MoSj35Fs1bNpmdreZj6GYiaqqDnfO59wNP2fmdptVyYc0UgbPedWicNxX0Xpne8wYfS0GOOUoxwynKUk_cDr6hJGldxol2Uf7u55k0ESXhSeG1KJMeTIQAxZOJMtEn-8TDq23hfIecDoQ_9sd5_x3w-tgVpMlWn210e39Ev2E7oNGT7gfzWzCocULJCo1iaDVNzh8EaNsRUsGTbk6FJzshOZXodjqHDFq5uZ84Hk-erJE38Plhwjh6zhhVqDB4BfIu1xb1dL05Nqu1oZaO_K9_H6HBwH8WGuPdK39EG0kX7iSaCqiVB6qtVRy1NpuCSniSEYwUhHrUlkB5rAC6rWyqGP0KsBWCoZUcBXBlb5VPzQjkCky1Fr6M-yWQ7VV6c5UWzPk1g2zHWEdgNyTYbXT-qf4FoRgFFPhy8n948-6bqJbKJpBSnEkLi3k7kQ2as92k2500xt5OqXhPAqqVChBSwaqysE0W3HW51-_UedZZ18evKFfZ7_l1tLbxaHcWJc3N3E08nLcRN1O1OtER10onIu64DdxQ909m7DZDVvdsN0NO93wsBt2u2GvGx51wnCqEtb62o6wHU4ibfyunX4wwo_KiMQYBqF27Gu45HR1yEJtfPphpZWnm-UswTDudhV4_BfnQHNM" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 E2E-88E_R3_SAP_Transportation_Management — E2E-88E_R3_SAP_Transportation_Management

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4 (IP & IF) | **Tasks**: 12 | **Gateways**: 6

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart LR
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph Boundary Apps
        n1["Receive/Send Information in Carrier Invoice Reconciliation/Dispute..."]
        n2["Event updates are received in GTT"]
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n11["Feed Rates/Charges Integrators 3rd party service – Redwood"]
        n12["Carrier"]
        n13(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n14(["fa:fa-play Events Published"])
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n3["Generate Freight Unit (TM)"]
        n4["Create Freight Order (TM)"]
        n5["Perform Carrier Updates and Calculate Charges"]
        n6["Execute Freight Order (TM)"]
        n7["Post Freight Settlement Document (TM)"]
        n8["Create Service PO for FSD (TM)"]
        n9["Post SES with Auto Release (TM)"]
        n10["Create Cost Distribution/Agency Business Document (TM)"]
        n15(["fa:fa-stop TM process ended"])
        n16["E2E-88C R3 Procurement"]
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n4
    n5 --> n18
    n7 --> n8
    n19 --> n5
    n6 --> n20
    n4 --> n19
    n9 --> n10
    n10 --> n15
    n11 --> n21
    n13 --> n11
    n17 --> n1
    n14 --> n12
    n12 --> n22
    n22 --> n17
    n21 --> n17
    n22 --> n2
    n1 --> n20
    n21 --> n19
    n2 -->|"Event Update"| n18
    n16 --> n3
    n18 --> n6
    n8 --> n9
    n20 --> n7
    class n13 startEvt
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVttu4zYQ_RVCQeosYCeiLpbjhwK2bAUBNlgjStqHdR9oibKJ0JJAUr4063_vUBff4hTdrR-CzNHMmZnD4eXdiLKYGn3j-vqdpUz10XtLLeiStvqoNSOSttqoAv4ggpEZp7KlfZIsVSH7u3TDTr7RbhoLyJLxrUZDOs8oen1sowEE8jaSJJUdSQVLWu1WLtiSiK2f8Uxo7yvaS8ykzFZ_GmYipuLgYJoejlwI5SylB9j2HM8JdJykUZbGJ6SJm_SSqLXTxfFsHS2IUGX5haRPZPMni9UC7IRwScFnoZb8K5lRrntUotBYVIhVIwaTOk8KgoU5iVg6B9wxARIkfTtArrnbod319TTdJ0Vfn6cpgl_EiZQjmiCpAB6vFEoY5_0rxx8ErtmWSmRvtH9ljb2RbbUj3UkfWjfbWtzOmrL5QvVnGY9r185a99C38k1bbPqW2RZb-HuWi6bxIZPftXpWb59p6GEf-02mJEn-VybQVbwQ-VbnGtuBFYz2ubDbdX3zI1_T5sjxBvhcJypWLKJHpEEQ2OODVOOui83PSYeB3TX9M9I5UXRNtgfCe9_ZEwauF2DvU8Iq33mVxWwisqghtMdu4O4JvSEOBtanhM4AO726QuCZC5Iv0DAryllGgzyX1Tf9S_H3qfFMI8pW9C6EdUWPaZKJJVEsSxFLkU-EYFQAvMpANvSsN0XEOCs97kZM5oWit7e3U-OvI1oLaMcrmipU5DGIIxERFIkqUayJH15eTkOw9_4-NRLST0hHnyGdGeyCaIHoJuKFhLCHSuSpsdtVYVDuWZfjjaIiJRxNYDOkVMg7FBZ5znUHx6l01wGFQp51bXc-bKk51PiYKgpEKhMS2SJGObBsm4lB08IysQ0KxOssi8-K1w3XWp19sW--N23lHGZEryuVOhlToCIUMYRjMUagt65mX8xgRRjXByTwfTkmdM4IS50lmhQzzuSCxmf-Fj7oCgVma9khXOneCOeUf1C1CrJ-LujjUoSDCQrvHHTzOEG_ocfguCQbGnigsD5AgwJRHg3oFfRANy9PX071c7Swgh57ftMH-QVXF1wnVOj53c_tazN-MNo-4VHBNVOt8Wl4V8_shkbFf0jl6VSZVHvHkCrF4VaDiR9lUVH-8zGsd2gmrKdq8g1BwSgIRxf875s04ThEa6YWaFCoDEaQU5iZCwHYPGTwdSBsUCXYrCh362BO02iLhrCdUj2C_1Ipdg9TJlWWo5cnlNeTC4v9YcpwqZ417vR6Pnq2yykvRCnIGXHvZ7d5FXb_S2GW-cuHSmqjTud3GMDadCsT92rbq-zGxPeV7dZ2tzKbGy116vD72q7dcfMdmzXQEGBcM-AGqAvCe6AuYW83OawGsGqKBrBqAHsNgM-BJqShOGtjH9D0Ufr_aE77artNjR9HQuFaCruxe5Xdre3a3BPWQnhHV2LZfPPCOcWdT3C3fqWcot1PvL3mCj-Fe5fh-4swFH4Rxpdhq4GNtrGkcOWy2Oi_G-XbGN7PMU1IwZWxaxsE9ny4TSOjX74hjepKHTECJ-2yAnf_APLjiZA=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 E2E-88F_R3_Project_Systems_2 — E2E-88F_R3_Project_Systems_2

**Swim Lanes**: SAP S/4 (IP & IF) | **Tasks**: 9 | **Gateways**: 6

> **Legend**: <span style="color:#000;background:#4CAF50;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● Start</span> · <span style="color:#fff;background:#C62828;padding:2px 6px;border-radius:10px;font-weight:bold;font-size:9pt">● End</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">User Task</span> · <span style="background:#FFF3E0;padding:2px 6px;border:1px solid #E65100;font-size:9pt">Service Task</span> · <span style="background:#FFF9C4;padding:2px 6px;border:1px solid #F57F17;font-size:9pt">◇ Gateway</span> · <span style="background:#F3E5F5;padding:2px 6px;border:1px solid #7B1FA2;font-size:9pt">Sub-Process</span>

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial, sans-serif","primaryColor": "#e8f0fe", "primaryBorderColor": "#0071c5","lineColor": "#37474F", "secondaryColor": "#f5f8fc"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "curve": "basis", "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TD
    classDef startEvt fill:#4CAF50,stroke:#2E7D32,color:#000,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef endEvt fill:#C62828,stroke:#B71C1C,color:#fff,font-weight:bold,stroke-width:2px,rx:20,ry:20
    classDef userTask fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef serviceTask fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef gateway fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#E65100
    classDef subProc fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    subgraph SAP S/4 (IP & IF)
        n1["Create Settlement Rules"]
        n2["Run Settlements"]
        n3["Place Assets in Service"]
        n4["Obtain Acceptance for Project Closure"]
        n5["Capitalize Final Asset"]
        n6["Create Final Asset"]
        n7["Update UTP/Depreciation Start Date (DSD) on Final Asset"]
        n8["Post Cap Asset Creation and accounting entry"]
        n9["Retire Assets"]
        n10(["fa:fa-stop Project is Closed"])
        n11(["fa:fa-stop Asset capitalized"])
        n12["E2E-88B R3 Project Systems 1"]
        n13["E2E-88B R3 Project Systems 1"]
        n14{{"fa:fa-code-branch Settlement Required?"}}
        n15{{"fa:fa-code-branch Availability Control Activated"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
        n19{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n2
    n2 --> n15
    n15 --> n3
    n14 -->|"Yes"| n16
    n16 --> n1
    n3 --> n17
    n17 --> n4
    n4 --> n10
    n14 -->|"No"| n15
    n5 --> n11
    n17 --> n5
    n12 --> n18
    n18 -->|"EUID updates"| n6
    n18 -->|"UTP Date from WBS"| n7
    n19 --> n8
    n8 --> n9
    n7 --> n19
    n6 --> n19
    n9 --> n16
    n13 --> n14
    class n10 endEvt
    class n11 endEvt
    class n12 startEvt
    class n13 startEvt
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVluP4jYU_itWRlNmpaDNlYQ8tIKEVCO13dEw01VV-mAcZ3DHxKntwLAs_702uTBk4WFbHhDnO9_5ziUcO3sDsQwbkXF7uycFkRHYD-QKr_EgAoMlFHhgghr4HXIClxSLgebkrJBz8uVIs73yTdM0lsI1oTuNzvELw-D53gQTFUhNIGAhhgJzkg_MQcnJGvJdzCjjmn2Dw9zKj9ka15TxDPMTwbICG_kqlJICn2A38AIv1XECI1ZkZ6K5n4c5Ghx0cZRt0QpyeSy_EvhX-PaZZHKl7BxSgRVnJdf0F7jEVPcoeaUxVPFNOwwidJ5CDWxeQkSKF4V7loI4LF5PkG8dDuBwe7souqTgKVkUQH0QhUIkOAdCKni2kSAnlEY3XjxJfcsUkrNXHN04syBxHRPpTiLVumXq4Q63mLysZLRkNGuow63uIXLKN5O_RY5l8p367uXCRXbKFI-c0Am7TNPAju24zZTn-f_KpObKn6B4bXLN3NRJky6X7Y_82PpWr20z8YKJ3Z8T5huC8DvRNE3d2WlUs5FvW9dFp6k7suKe6AuUeAt3J8Fx7HWCqR-kdnBVsM7Xr7JaPnCGWkF35qd-JxhM7XTiXBX0JrYXNhUqnRcOyxWYTx7A_KMH7u4fwA_gPv1Q-_WnsP9cGDHHqgcwx1JStZyFBI-V2s2F8dc7oqOIj1XxjtUjuIrwQCHCYCIElgIQTT4O_JzoKeKnpYTKP0EIlxIWKihnHKi2_8ZIgpgyUfFemK8rhSWRkKqzAqSkgLROdc4bnTq6ygkU57nMNOf56eFjgkuOEYGSMFWzXiaQaN9dMk8-AIVdFQp100yokmFZ-8ExtxaCRQYgQqwqpNpltTiS786jx3qmWBLezuzcbVt3ipDDKIdDIVnZzYeI44hwpvhnD9PuBdQVoW5q3wTopzpzZsMwnIJHt0sw3wmJ1wLYvYLc76N7-31bjr4Zhkt1tqHV2R8N_1Op9rOfFsbh8D7Uvxw62UBC4ZJQIncgVocLZ-q5IEk26nllfZHRZRH8hmglyAb_XK9uPyw4hUHO2VYMIZWghBxSiumVoPC_BI2_L0idvfWPwgbD4Y9qKRvTqU3bb91-Dbit7Wn768L4Q6_1Vz2a1jNqQhvbbcyg9Qc14DW21_itvvJvrBZuS2gqsO2eUFdiW3PYAmGjNHu-T0B13M662FGfoXa2XtCcszX4PJ0faV3J41q5FQ5rc9yYTR12a496dhN9mlA7Eu_dOa0n0FyF56h9EXW6K_ocd6_gXnurnMP-ZXh0GQ4uw-FleNzChmmsMV9DkhnR3ji-rqlXugznsKLSOJgGrCSb7wpkRMfXGqN-VAmB6rZZ1-DhX3VNF8g=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-88A_R3_Portfolio_and_Project_Management, E2E-88B_R3_Project_Systems_1, E2E-88C_R3_Procurement, E2E-88D_R3_CFIN, E2E-88E_R3_SAP_Transportation_Management,  | |
| SAC | E2E-88A_R3_Portfolio_and_Project_Management,  | |
| SAP S/4 (IP & IF) | E2E-88A_R3_Portfolio_and_Project_Management, E2E-88B_R3_Project_Systems_1, E2E-88C_R3_Procurement, E2E-88D_R3_CFIN, E2E-88E_R3_SAP_Transportation_Management, E2E-88F_R3_Project_Systems_2 | |
| External Partners/
Supplier
 | E2E-88C_R3_Procurement, E2E-88E_R3_SAP_Transportation_Management,  | |
| CFIN | E2E-88D_R3_CFIN,  | |
| MBC | E2E-88D_R3_CFIN,  | |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

#### 4.2.1 Current-State — Current-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E88CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E88CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E88CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E88CDAA_e_g_XEUS -.-> E2E88CDAD_e_g_Azure_SQL
    end
    style E2E88CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E88CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E88CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E88CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E88CDAA_e_g_MES_300 -.-> E2E88CDAD_e_g_SAP_HANA
    end
    style E2E88CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E88CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E88CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYEGbaHLQMk2qcRa3JXZpjvYVLh5t014niPzvu2uhbkid8S5puPfj-14_rzlW2I8DwAZuNFYsYsJAq6aYwRyaBmpOaAbNFmpm4OcpE0sbfgNXDh7HpacI_U5TRiccsqbKDuNIOOypEDjSk4UKU7YRnTO-VFYHpjGgu8sWIjKRN9cqgseP_oymotDIM7iiix8sEDN5DinPQMbMxJzbdAJcFRJprmyR7N5JqM-iqTR2dWlKafTwYjrW12u0bjTcqCqBxgM3QnL5nGaZCSGiSTKIFyhknBsHA90cjUatTKTxAxgHmtbvD3qbY_tR9WR0kkXLj3mcKnfX1Hf1gslwyTdyRDd7pF_Jday-2e3Uyh0NdKuj7chBzF_aG40G-kCv9IZDTa5avV5Pud2oVMzyyTSlyQxZHevkZGiSoe2BN_XIU56C53yz712MXPyrjFYrYCn4gsVRBU2tbTopsn9ad45MhMPpIVK_pYBhGCXT1znmTsVPLnbz4KQbyGfgH7t5CJp8ZSVWBCEZ5OLPSrLA-lYXqH3YPq-rVCZCFGxYiCWHWhBb2ETtCralqf0v7KNk8T-8DrnxLsg1-RDdK8vxupq2BSyPSB7fw7gq-wZiGYNUzHsIbzrZB3lb6j2Mt7EfQry_LDo7O3_eADILpugLIjeX8jliHFz8XP9R7IzOhqls__4vYn6gIZOMCSK3w4vLsTUc391ayLa-WtdmzTTt2xer7am5kyThzKfKu390tmfWzMmkgqqbeP-IbM-S8lYUtOOwbbMQSvnyytg7jvINt_R1tSv6p6enr9DjFp5DOqcswMYKFze-_L8IIKQ5F3jdwjQXsbOMfGwUlzLOk4AKMBmVROelcf0HE6T1vw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E88FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E88FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E88FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E88FDAA_e_g_XEUS -.-> E2E88FDAD_e_g_Azure_SQL
    end
    style E2E88FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E88FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E88FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E88FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E88FDAA_e_g_MES_300 -.-> E2E88FDAD_e_g_SAP_HANA
    end
    style E2E88FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E88FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E88FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYEGbaHLQdppU4yxuS-zSHO0rXDzapr1OEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHfgNXDp4klacM_U4zRscc8qbKjpJYuOypFDjS07kKUzabzhhfKKsLkwTQ3WULEZnImysVwZPHYEozUWoUOVzR-Q8Wiqk8R5TnIGOmYsYdOgauComsULZYdu-mNGDxRBq7ujRlNH54MR3rqxVaNRpeXJdAo4EXI7kCTvPchAjRNB0kcxQxzo2DgW7att3KRZY8gHGgaf3-oLc-th9VT0YnnbeChCeZcndNfVsvHA8XfC1HdLNH-rVcx-qb3c5euaOBbnW0LTlI-Et7tj3QB3qtNxxqcu3V6_WU24srxbwYTzKaTpHVsU5ObJMMHR_8iU-eigx895tz72Hk4V9VtFohyyAQLIlraGpt0kmZ_dO6c2UiHE4OkfotBQzDqJi-zjG3Kn7ysFeEJ91QPsPg2Csi0OQrK7EyCMkgD39WkiXWt7pA7cP2-b5KVSLE4ZqFWHDYC2IDm6hdw7Y0tf-FfZTO_4fXJTf-BbkmH6J7Zbl-V9M2gOURyeN7GNdl30AsY5CKeQ_hdSe7IG9KvYfxJvZDiHeXRWdn589rQGbJFH1B5OZSPm3GwcPP-z-KrdE5MJHt3_9FLAg1ZJIRQeR2eHE5soaju1sLOdZX69rcM03n9sXq-GruJE05C6jy7h6d45t75mRSQdVNvHtEjm9JeSsO20nUdlgElXx1ZewcR_WGG_q62jX909PTV-hxC88gm1EWYmOJyxtf_l-EENGCC7xqYVqIxF3EATbKSxkXaUgFmIxKorPKuPoDj0n16Q==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-88-R001 | Report | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-88-C001 | Conversion | Legacy data migration for R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-88.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "16px", "fontFamily": "Segoe UI, Arial, sans-serif"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        E2E88C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E88C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E88CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E88CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E88C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E88CMW_e_g_Azure_Service_Bus
    E2E88CMW_e_g_Azure_Service_Bus --> E2E88C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTrfb98Gf-iPH8091fZs1gDaCw-khkj4kfZLQMAxZ4U8Jfjl33qfRyvFl6OghDzZfsxR8D9InGoBvZfzD1x13CqYchdYoJFEFbVm1Krvt5Oz9mAvfYXLeI9Hb3mJwVhArAFoDLibpUe-C9gqHd4-O0NCOA_n307u6vDiivSKr6soiH0TkvT67gsqx672NtZzNzosgmczroXwOKIOx9rZHiW3irzAqSbUWakvrpsmPAcvdGvGBvm_Et0PNTaj-nUneaVYXplKjD81BdOQ6P5xL-xtd6vqyt6utZSYJowFW4E-ay_VHD9UWGpVt8mXbuL7tVDvEVsePEwl5i1QrX4Q4V8UwnrTJmQSSZhw2XRqu08j532qTUtRClHdhW-q3Efb8_HznLNMa2hzSOaZEM5ZafnvJu49AiDMmtFVDw5mIvUUUaEZ-qWhZIjcKNsWyCPPCuPoHd9Y9qQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-88.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

#### APPLICATION ARCHITECTURE — Architecture Diagram (ArchiMate-Inspired)

> **Click any system node** to open its IAPM application page.
> **Legend**: <span style="background:#C8E6C9;padding:2px 6px;border:1px solid #2E7D32;font-size:9pt">Deployed</span> · <span style="background:#E3F2FD;padding:2px 6px;border:1px solid #1565C0;font-size:9pt">Developing</span> · <span style="background:#FFCDD2;padding:2px 6px;border:1px solid #C62828;font-size:9pt">End-of-Life</span> · <span style="background:#ECEFF1;padding:2px 6px;border:1px solid #78909C;font-size:9pt;border-style:dashed">No IAPM Match</span>

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "16px", "fontFamily": "Segoe UI, Arial, sans-serif"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["🔵 APPLICATION LAYER"]
        direction LR
        E2E88F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E88F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E88FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E88FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E88F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E88FMW_e_g_Azure_Service_Bus
    E2E88FMW_e_g_Azure_Service_Bus --> E2E88F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTrc78MGf-iPH8091fZs1gDaCw-khkj4kfZLQMAxZ4U8Jfjl33qfRyvFl6OghDzZfsxR8D9InGoBvZfzD1x13CqYchdYoJFEFbVm1Krvt5Oz9mAvfYXLeI9Hb3mJwVhArAFoDLibpUe-C9gqHd4-O0NCOA_n307u6vDiivSKr6soiH0TkvT67gsqx672NtZzNzosgmczroXwOKIOx9rZHiW3irzAqSbUWakvrpsmPAcvdGvGBvm_Et0PNTaj-nUneaVYXplKjD81BdOQ6P5xL-xtd6vqyt6utZSYJowFW4E-ay_VHD9UWGpVt8mXbuL7tVDvEVsePEwl5i1QrX4Q4V8UwnrTJmQSSZhw2XRqu08j532qTUtRClHdhW-q3Efb8_HznLNMa2hzSOaZEM5ZafnvJu49AiDMmtFVDw5mIvUUUaEZ-qWhZIjcKNsWyCPPCuPoHvkc9wQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
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

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-88-I001 | Interface | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-88-E001 | Enhancement | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-88-F001 | Form/Report | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### 6.1.1 Current-State — Current-State Platform Architecture

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E88CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E88CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E88CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E88CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E88CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E88CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E88CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E88CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2tJCClD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DPTCVYJz3ma70O6koWTKoNbU644UI6WMHGI7LjSpTWkByyrZKDWHFAd1e68iVC5nWqgrGH5I1qUTHaGq4IZsfNBVrGWeE1SBr1iJnc7IEpjYSVaO0QroPS5LQYiXFsSGlihR3R8ky2ha1g0FUHLZA37yoQHIkjNT1DDJEytLjG5RRxpwzz5oFQaDXouJ34JwZxuWlN9mHHx6UJ2dUbvSEM16ptDmzXvNKRsQROLX9yfTjAWjatm9OXwLNI3DoWf7IeAUEzo68IPAszzrwplNDjpMGJxOVjoqeWDfLVUXKNfJHvm1PF_NFDPEqdh-bCuIFIeGvCEfNaGIMoyYDQ-58vjpHXRqpdIR_9yA1UlpBIigv0PzrUX0mux35p3-rmB1GfUuA4zh9w_s1UKR7b2LL4KSxf2rmm4cP43H82f3ixiNjZHbnT20zlXNKrL-7EF6MkapDqu7djbjxw9g0jOdeyBDJ8J3teGH1P3TkLfrV1aenvdlZdz50gdzFtZwDyiDCTyevCus4hyonNMXODndvhHxhUshIwwRudUwawcNtkWCn-41xU6ZEwIwSeT15L7Z_ANcIbpo=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E88FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E88FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E88FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E88FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E88FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E88FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E88FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E88FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhJQhdRIkoFVKp2is26QxIQeOxKqDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbxYLCjBRUu2mliBWvQXKQtSA2ajrQa0qaiYjuDe2AqwTjvM13pd1JRsmBQa2p1zgsR0ccOMByVG1WmtJCsKdsqNYIlB3R7rSNPLmRaqyoYf0hXpBIdo6nhhmx-0EysZJwTVoOsWYk1m5EFMLWRqBqlFdJ9VJKUFkspjgwpVaS4O0q20baoHQzi4rAF-ubHBZIjZaSup5AjUpY-36CcMuae-fY0DEO9FhW_A_fMMC4v_fE-_PCgPLlmudFTznil0tbUfs0rGRFH4MQJxpOPB6DlOIE1eQm0jsChbwem8QoInB15Yejbvn3gTSaGHCcNjscqHRc9sW4Wy4qUKxSYgeOE89k8gWSZeI9NBcmckOhXjOPGHBvDuMnBkDufL89Rl0YqHePfPUiNjFaQCsoLNPt6VJ_JXkf-GdwqZodR3xLgum7f8H4NFNnem9gyOGnsn5r55uGjZJR89r54iWmYVnf-zLEyOWfE_rsL0cUIqTqk6t7diJsgSizDeO6FDJEM39mOF1b_Q0feol9dfXram51250MXyJtfyzmkDGL8dPKqsI7XUK0JzbC7w90bIV-YDHLSMIFbHZNG8GhbpNjtfmPclBkRMKVEXs-6F9s_-dlusg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
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

<div class="page-footer"><span>Page 27</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-88 — R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme</span></div>
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
*E2E-88 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

