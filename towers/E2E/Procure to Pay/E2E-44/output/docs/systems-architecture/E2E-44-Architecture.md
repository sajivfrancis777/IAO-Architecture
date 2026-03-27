<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-44 — R3 - Intel Owned Consignment with Planning Integration</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-44 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-44 R3 - Intel Owned Consignment with Planning Integration** within the IAO program. It includes 5 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-44 - R3 - Intel Owned Consignment with Planning Integration |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-44 - R3 - Intel Owned Consignment with Planning Integration |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-44 Process Migration | Migrate R3 - Intel Owned Consignment with Planning Integration business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-44 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **5 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-44 R3 - Intel Owned Consignment with Planning Integration.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-44_R3_CFIN | E2E-44_R3_CFIN | Boundary Apps, CFIN, MBC, SAP S/4 (IP & IF) | 15 | 10 |
| 2 | E2E-44_R3_SAP_Transportation_Management | E2E-44_R3_SAP_Transportation_Management | Boundary Apps, External Partners/
Supplier
, SAP S/4 (IP & IF) | 12 | 6 |
| 3 | E2E_44A_R3_Intel_Owned_Consignment_with_Planning_Integration-Procurement_from_Component_supplier_and | E2E_44A_R3_Intel_Owned_Consignment_with_Planning_Integration-Procurement_from_Component_supplier_and | Boundary Apps, External Partners/Suppliers, SAP S/4HANA IP | 26 | 10 |
| 4 | E2E_44B_R3_-_Intel_Owned_Consignment_with_Planning_Integration-Shipment_of_components_from_Intel_War | E2E_44B_R3_-_Intel_Owned_Consignment_with_Planning_Integration-Shipment_of_components_from_Intel_War | Boundary Apps, External Partner/Supplier, SAP S/4HANA IP | 45 | 28 |
| 5 | E2E_44C_R3_Intel_Owned_Consignment_with_Planning_Integration_-_Subcontracting_Process_with_ODM_Suppl | E2E_44C_R3_Intel_Owned_Consignment_with_Planning_Integration_-_Subcontracting_Process_with_ODM_Suppl | Boundary Apps, External Partners/Supplier, SAP S/4HANA IP | 34 | 14 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-44_R3_CFIN — E2E-44_R3_CFIN

**Swim Lanes**: Boundary Apps · CFIN · MBC · SAP S/4 (IP & IF) | **Tasks**: 15 | **Gateways**: 10

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
        n1["Receive File in Bank"]
        n2["Update Payment Remittance"]
        n17(["fa:fa-stop Payment Data Updated"])
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
        n19(["fa:fa-stop Memo Record Created"])
        n20(["fa:fa-stop APP Doc Reversed"])
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
        n16(["fa:fa-play Supplier Invoice Posted (Component PO and SubCon Purchase Order to ODM)"])
        n18(["fa:fa-stop Payment Details provided back to Source System (IP/IF)"])
    end
    n12 --> n3
    n3 --> n28
    n4 --> n19
    n5 --> n21
    n21 -->|"No"| n23
    n7 --> n22
    n23 --> n6
    n25 --> n5
    n24 -->|"No"| n26
    n9 --> n20
    n10 --> n29
    n26 --> n9
    n29 --> n11
    n28 --> n4
    n11 --> n27
    n27 -->|"Reversal"| n26
    n2 --> n17
    n6 --> n14
    n29 --> n2
    n8 --> n25
    n13 --> n12
    n29 --> n18
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
    n16 --> n13
    class n16 startEvt
    class n17 endEvt
    class n18 endEvt
    class n19 endEvt
    class n20 endEvt
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV99z4jYQ_lc0vklJZqDnnxh4aAcMvslMyDGh106n9EHYcvDEWB5ZJqE5_veubMlg4zz0moc76_O3365Wu2vxrgU0JNpEu7l5j9OYT9B7j-_InvQmqLfFOen1UQX8jlmMtwnJe4IT0ZSv439KmmFnb4ImMB_v4-Qo0DV5pgR9u--jKRgmfZTjNB_khMVRr9_LWLzH7OjRhDLB_kRGkR6V3uSrGWUhYWeCrrtG4IBpEqfkDFuu7dq-sMtJQNOwIRo50SgKeicRXEJfgx1mvAy_yMkSv_0Rh3wH6wgnOQHOju-TB7wlidgjZ4XAgoIdVDLiXPhJIWHrDAdx-gy4rQPEcPpyhhz9dEKnm5tNWjtFD0-bFMFfkOA8n5MI5RzgxYGjKE6SySfbm_qO3s85oy9k8slcuHPL7AdiJxPYut4XyR28kvh5xydbmoSSOngVe5iY2VufvU1Mvc-O8G_LF0nDsydvaI7MUe1p5hqe4SlPURT9L0-QV_Ybzl-kr4Xlm_689mU4Q8fTr_XUNue2OzXaeSLsEAfkQtT3fWtxTtVi6Bj6x6Iz3xrqXkv0GXPyio9nwbFn14K-4_qG-6Fg5a8dZbFdMRooQWvh-E4t6M4Mf2p-KGhPDXskIwSdZ4azHZrRoqxlNM2yvHon_lLjr432RAISHwjy44SgOEUzqL6N9vcFywTWtyyEXaIVPu5JytET2cec4zQgTarh3gI5wpMID3JOs9pgjjlGlUgIJneVDZRSK1LPv3-80LNAbfFGguLSd5E2ndpA8hgR8U1XS7QkewoBBtDxTZ4DPJFXkudo5i1rwRnmwQ6aDR5yEiIKOShyGAtAeypgRDVVhqDyhaSEKX9KRiSwSXVFeqmInVORekYPhDUpIxE7ZYwEvBSTzzEEca03Lo8LNHLheYXmUCOPxX5LGMJpeLlxNCcJESqt49FBwSewXRV1jnwccAqlcQvu-yIvfbSceWhJYX5TdtcSqCrmEJNXMIQAw3r7D_S5xTUvM6VocAAZzXHS4lqlbpbEgSCviwweYVv36YFCv6IVzTmcUMto3Cq2ywRUBXFRa1Up6y0TlUaZ1iu-8f6u-OLTNtjCcIbsLXFa4ESeKTw8ElFV0GG_brTT6VLA7BaQ1RBe8a1uPnkLEijKA_lSDZu2md1t5mEoZqKqqsOd82Puhj9m5nabVcmHNFIGz1nVonDcV9GOzvaYMfqaD3DCUYYZThKSfOB0_ANGlt5pFKcf7e96kkETXdaqGFLLIuHxQAxYOJE0FX1-iDm03g7Ke8DpQPzf7jjnvxteB7OertD6s41u71foJ3TvX9a4MTz3RJbAd6yz-6DTbz26z2hadvHXcuKsiy3Eg1YFg3sJDKWv4pIlht3X-fKu1UrG6KNPA-EwSXIkGiIOwc8WBy9CZE1BF4bBEbzvReifReDXHw-YNGgw-AVOTa6tammO5Nqu1sZYrh35Xt4O4EEA3zfaI91o30UTyheuJJqKKJWHai2VHLW2W0KKOJZCuopYl4AKyRxWQL2WFkYd46gCbKVgSAVXEVzpW3VTMwKZIkPRpT_DbjlUW5XuTLU1Q27dMNsRjtpZ_FN8MsG3cqXw1fT-8WddN9EtHP0goTgUNxxyV5KN2pHdpBvd9EZayl2f50a1cyVoyVzXcZqtOOvjrt-o46uTLc_Z0K-T3XJr6e1aUG7qN4bKvXVx7ythdY1v4q68cjfRUSc67kJNvRM11M21CZvdsNUN292w0w0Pu2G3Gx51w-NOGI5Zwlpf2xO2x3GoTd618ucm_CQNSYRhjGqnvoYLTtfHNNAm5c8yrSjvpfMYw7DcV-DpX1SFiV0=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-44_R3_SAP_Transportation_Management — E2E-44_R3_SAP_Transportation_Management

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4 (IP & IF) | **Tasks**: 12 | **Gateways**: 6

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
        n1["Receive/Send Information in Carrier Invoice Reconciliation/Dispute..."]
        n2["Event updates are received in GTT"]
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n11["Feed Rates/Charges Integrators 3rd party service – Redwood"]
        n12["Carrier"]
        n14(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n15(["fa:fa-play Events Published"])
        n20{{"fa:fa-arrows-alt parallelGateway"}}
        n21{{"fa:fa-arrows-alt parallelGateway"}}
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
        n13(["fa:fa-play Component PO and SubCon PO IBD Integration"])
        n16(["fa:fa-stop TM process ended"])
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n3 --> n4
    n5 --> n18
    n7 --> n8
    n19 --> n5
    n4 --> n19
    n9 --> n10
    n10 --> n16
    n11 --> n20
    n14 --> n11
    n17 --> n1
    n15 --> n12
    n12 --> n21
    n21 --> n17
    n20 --> n17
    n21 --> n2
    n20 --> n19
    n2 -->|"Event Update"| n18
    n18 --> n6
    n8 --> n9
    n13 --> n3
    n6 --> n22
    n1 --> n22
    n22 --> n7
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 endEvt
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVttu4zYQ_RVCQeosYCeiLFmOHwrYshUE2GCNKGkf1n2gJcomQksCSfnSrP-9Q118UZy22_ohyBzNnJk5miH1boRpRI2BcX39zhKmBui9pZZ0RVsD1JoTSVttVAK_EcHInFPZ0j5xmqiA_Vm4YTvbajeN-WTF-E6jAV2kFL0-ttEQAnkbSZLIjqSCxa12KxNsRcTOS3kqtPcV7cdmXGSrHo1SEVFxdDBNF4cOhHKW0CPcdW3X9nWcpGGaRGeksRP347C118XxdBMuiVBF-bmkT2T7O4vUEuyYcEnBZ6lW_CuZU657VCLXWJiLdS0GkzpPAoIFGQlZsgDcNgESJHk7Qo6536P99fUsOSRFX59nCYJfyImUYxojqQCerBWKGeeDK9sb-o7Zlkqkb3RwZU3ccddqh7qTAbRutrW4nQ1li6UazFMeVa6dje5hYGXbttgOLLMtdvC3kYsm0TGT17P6Vv-QaeRiD3t1pjiO_1cm0FW8EPlW5Zp0fcsfH3Jhp-d45ke-us2x7Q5xUycq1iykJ6S-73cnR6kmPQebn5OO_G7P9BqkC6LohuyOhPeefSD0HdfH7qeEZb5mlfl8KtKwJuxOHN85ELoj7A-tTwntIbb7VYXAsxAkW6JRmhezjIZZJstn-pfg7zPjmYaUreldAO8VPSZxKlZEsTRBLEEeEYJRAfA6BdnQs16KkHFWeNyNmcxyRW9vb2fGHye0FtBO1jRRKM8iEEciIigSZaJIEz-8vJyHYPf9fWbEZBCTjj5DOnPYgnCJ6DbkuYSwh1LkmbHfl2FQbqPLyVZRkRCOprAMCRXyDgV5lnHdwWkq3bVPoZBnXdudByu1gBofE0WBSKVCoq6IUAYsu3pi0Cy3TNwFBaJNmkaN4nXDlVaNJ_bN97qtjMOM6PdKpU7GFKgIRYzgWIwQ6K2rORQzXBPG9QEJfF9OCZ0GYaGzRNN8zplc0qjhb5lHXaHAdCM7hCvdG-Gc8g-qlkH454I-vopgOEXBnY1uHqfoF_Ton5bUhQYeKLwfoEG-KI4G9Ap6oJuXpy_n-tlaWEFPPb_pg_yCqwOuUyr0_B7m9rUePxhtj_Aw55qp0vg8vKdndkvD_F-kcnWqVKqDY0CV4nCrwcSP0zAv_vkY1j82E1RTNf2GoGDkB-ML_vd1mmASoA1TSzTMVQojyCnMzIUAbB4zeDoQFlQJNs-LbR0uaBLu0AjWKdEj-DeV4m5jyrx0laWJdoaKtZpBPvdgZsF6HI0PqwNpmvPaOzJJlWbo5Qll1Q7A2HyYV9z_2XOgDLv_T2GWdXHQWfKPh07SRZ3OrzCglemUJu5XtlvatYnvS9upbLtyv6_s6jE2a3-zAno1gEvAOnjUFLgGqpQHuy7JqgGroqg9rIoTuzVgNoE6a9Ohrrug_FGf9uW6zYwfJ0LgfhlSN1KZNQGudOxWdq9KeCi6YVtVE-7JlVmw1F9A57j9Ce58gveqr5tz1K2v-HO4fxm-vwiDdBdhfBm2athoGysKVzKLjMG7UXw7w_d1RGOSc2Xs2waBMyHYJaExKL4xjfLKHTMCC7kqwf1fVJKVCA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E_44A_R3_Intel_Owned_Consignment_with_Planning_Integration-Procurement_from_Component_supplier_and — E2E_44A_R3_Intel_Owned_Consignment_with_Planning_Integration-Procurement_from_Component_supplier_and

**Swim Lanes**: Boundary Apps · External Partners/Suppliers · SAP S/4HANA IP | **Tasks**: 26 | **Gateways**: 10

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
        n15["Organize Transport-Intel Routing Guide (IRG)"]
        n16["ReadSoft Validation/Exception Handling based on rules setup"]
        n17["Incoming invoice/ B2B/OpenText/Web suite"]
        n18["Manual invoices through OCR"]
        n33{{"fa:fa-code-branch exclusiveGateway"}}
        n34{{"fa:fa-code-branch B2B/Manual?"}}
        n35{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/Suppliers
        n19["Update Forecast Communication and Commit"]
        n20["Receive PO at Component Supplier"]
        n21["Commit Order Acknowledgement"]
        n22["Send PO communication to ODM Supplier"]
        n23["Select Carrier via Intel Routing Guide hosted Collaboration Portal"]
        n24["Send Order Shipment"]
        n25["Receive Physical Receipt of Material against PO at ODM Supplier"]
        n26["Supplier Invoicing"]
        n28(["fa:fa-stop PO communication to ODM Supplier Sent"])
        n40{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4HANA IP
        n1["Create Purchase Requisition"]
        n2["Create Manual Purchase Requisition"]
        n3["Approve Purchase Requisition"]
        n4["Create Purchase Order"]
        n5["Trigger GTS Check"]
        n6["Calculate Taxes"]
        n7["Initiate Auto Inbound Delivery"]
        n8["Receive Goods Receipt (Virtual)"]
        n9["Trigger TM Embedded"]
        n10["Evaluate Receipt Settlement (ERS) Self-Billing"]
        n11["Issue Material to ODM Supplier (541)"]
        n12["Post Supplier Invoice"]
        n13["Publish Purchase Order"]
        n14["Acknowledge/Confirm Purchase Order"]
        n27(["fa:fa-play Purchase Requisition Creation Initiated"])
        n29["E2E-44 R3 SAP Transportation Management"]
        n30["E2E-44 R3 CFIN"]
        n31{{"fa:fa-code-branch Invoice Accepted?"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n36{{"fa:fa-arrows-alt parallelGateway"}}
        n37{{"fa:fa-arrows-alt parallelGateway"}}
        n38{{"fa:fa-arrows-alt parallelGateway"}}
        n39{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n2 --> n3
    n22 --> n28
    n36 --> n5
    n24 -->|"ASN E2Open
Manual"| n25
    n25 --> n7
    n7 --> n37
    n37 --> n8
    n37 --> n9
    n8 --> n38
    n38 --> n10
    n38 --> n11
    n33 --> n16
    n17 --> n35
    n35 --> n33
    n34 --> n18
    n34 --> n17
    n10 --> n33
    n31 -->|"Yes"| n12
    n31 -->|"No"| n26
    n26 --> n34
    n18 --> n35
    n6 --> n39
    n5 --> n39
    n13 --> n40
    n14 --> n23
    n20 --> n21
    n23 --> n15
    n9 --> n29
    n12 --> n30
    n36 --> n6
    n39 --> n13
    n40 -->|"WebPO/
E2Open"| n20
    n15 --> n24
    n16 --> n31
    n4 --> n36
    n40 -->|"Manual/ E2Open/
Power BI"| n22
    n21 --> n14
    n1 --> n32
    n32 --> n4
    n27 --> n2
    n3 --> n32
    class n27 startEvt
    class n28 endEvt
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWFtv4jgU_itWRlU7EohcgfKwK6DQQZq2qHRmtBr2wSQOWDV21nFaup3-9z1ObC4ZOpcuD1X8-Vy-c_Fx0mcnFglxes7JyTPlVPXQ86lakTU57aHTBc7JaQNVwGcsKV4wkp9qmVRwNaP_lmJemG20mMbGeE3Zk0ZnZCkI-jRpoD4osgbKMc-bOZE0PW2cZpKusXwaCiakln5Huqmblt7M1kDIhMidgOt2vDgCVUY52cFBJ-yEY62Xk1jw5MBoGqXdND590eSYeIxXWKqSfpGTK7z5QhO1gnWKWU5AZqXW7CNeEKZjVLLQWFzIB5sMmms_HBI2y3BM-RLw0AVIYn6_gyL35QW9nJzM-dYp-ng75wh-McN5fkFSlCuARw8KpZSx3rtw2B9HbiNXUtyT3jt_1LkI_EasI-lB6G5DJ7f5SOhypXoLwRIj2nzUMfT8bNOQm57vNuQT_K35IjzZeRq2_a7f3XoadLyhN7Se0jT9X54gr_IO5_fG1ygY--OLrS8vakdD93t7NsyLsNP36nki8oHGZM_oeDwORrtUjdqR575udDAO2u6wZnSJFXnETzuD58Nwa3AcdcZe51WDlb86y2IxlSK2BoNRNI62BjsDb9z3XzUY9r2waxiCnaXE2QoNRFH2MupnWV7t6R_3oq9z50YuMYfDh-6g8fJMSNWccEUYuhWFgh5ElwVNCDqb3F6-nzt_76u3Qf2W4GQmUoU-Y0YTrKjgrdEmJpl-Qh8wT5g2ok9_ggCRBZx6KIQqspq1Dlib8FistTzlDwIq1UIDf9C6yQi_IxvV-kIWEBVVpKbaBdUrzAvMrGKO1EqKYrlCN8PbQ-kgeH6eOynupbip51VzAYHHK0Q2MSty-kAuq4LOnZeXfbXwuJomWPn-s64R_a4jOFu10o02ikgOcU3hhHMi89asyDJG4Wk_AeeQgE8ZpJ-gsZAkxrlCQ7FeF5zGZU0QFKJEqDrMhu-WRYwJ8EHTG4RLxUxwwhWyvmoqHqhUttCNnquoH99z8chIsoTZzusefBCfQWjafHxASgl0c3H1mpug1GMkBkpYShBADxSjY925ErkiOkDG8ELIyvoUehmzmtHQkqmYz1Y0O0I52k_K6ikHwuBSA5lCIkVXkGl9ESG8xJRDsqvM_SAYfVbsFoSgmxTo14S6Z19tw-RKZD9NGJpV1N_vGQndXddB1sRj3sRMoQxLzBhhv9Bzs_4UzVrhh_51H02m-22m6y6J7rJpIeEuygkk5Z-C5lSzqwWzEzZH8-c6uuIwo6R4-BUP4RE6ZVUPxXQt7yRdLiFfl3czNFyR-P5QRBdniFlcMG3sDm9IfihQzSbgoPf7BZRhwhd6qqILwqBJ5NOhfHevfy6FSPJt85x9plJBNmqz9HyP5N0VGq0XJElIUptz-qyOHjArNA1rcUaUYuW5Q2ej29l7AFjaHMDl8V2DebqCkzwvyK6D6y11FoVefdDrWk7hiKFaB9fnsK7ftFgwmq9-WBJPl25vaLSGgqdUrn-o5Hd2pyNjcOEe6xBUNoR-sOVKaufD16ke-aNmGKLboGz27c1XaUK74mODLHAPNIfjyXVNwDs-8E2yYEzqe5Ek310U_ttupPbvnfRKqfMWpe5blM7fOIi4j5rNP8CAXZq13zVA0K6AyAqEev0NWmp2jUa-fl2Y82rozJ1vepxbwahS7Jh1xziy68AA3dr63Ky7Rn67bwDPrQOeBQIDtA3gWZ-WU2A4BTbcIDQq3TpgaXpuXcUzCfhLD65v-sTWd65FlQrLwzc5DEJrtFsjZgVs8FFt7ZnQQhu8Z3j628IZnr7Nhm-zYX2cG4GtTVt6t1ZqSzswGp71EbomQHg3nN605tzUvwx2y8xw97fB2uAsM0M9aNfNVm3UMm0F9qfiEebfYFJ5sHn2PcNr68EY3BbCRGb3fdMH2_1D-fJjoJSy33aHeNd8hx2i58elA_cV3LMfL4ewfxwOjsPhcTg6DrePw53jcPc4fH4UhpoZ2Gk4ayLXmCZO79kp_-Pg9JyEpLhgynlpOBiu8NkTj51e-WXuFOW78wXF8Aa0rsCX_wAK7SXe" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E_44B_R3_-_Intel_Owned_Consignment_with_Planning_Integration-Shipment_of_components_from_Intel_War — E2E_44B_R3_-_Intel_Owned_Consignment_with_Planning_Integration-Shipment_of_components_from_Intel_War

**Swim Lanes**: Boundary Apps · External Partner/Supplier · SAP S/4HANA IP | **Tasks**: 45 | **Gateways**: 28

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
    subgraph Boundary Apps
        n35["Receive/Send Information in Carrier Invoice Reconciliation/Dispute..."]
        n66{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partner/Supplier
        n36["Carrier Confirmation Routing Guide/CRM"]
        n37["Picking"]
        n38["Packing"]
        n39["Loading"]
        n40["Post Physical Receipt of Material against STO at ODM Supplier"]
        n41["Pick Order Shipment Goods (Carrier)"]
        n42["Feed Rates/Charges Integrators 3rd party service – Redwood"]
        n43["Book/Tender to Carrier via BN4L"]
        n44["SAP BN4L"]
        n45["Carrier"]
        n48(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n49(["fa:fa-play Initiate Carrier via BN4L"])
        n50(["fa:fa-play Events Published"])
        n56(["fa:fa-stop Execution events via BN4L-GTT Captured"])
        n67{{"fa:fa-code-branch exclusiveGateway"}}
        n68{{"fa:fa-code-branch exclusiveGateway"}}
        n79{{"fa:fa-arrows-alt parallelGateway"}}
        n80{{"fa:fa-arrows-alt parallelGateway"}}
        n81{{"fa:fa-arrows-alt parallelGateway"}}
        n82{{"fa:fa-arrows-alt parallelGateway"}}
        n83{{"fa:fa-arrows-alt parallelGateway"}}
        n84{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4HANA IP
        n1["Create Stock Transport Order"]
        n2["Finalize Intel Carriers Based on STO"]
        n3["Trigger GTS Check"]
        n4["Create Outbound Delivery"]
        n5["Calculate Taxes"]
        n6["TM Embedded"]
        n7["Pick, Pack and Update"]
        n8["Post Goods Issue"]
        n9["Export Invoice (Performa)"]
        n10["Commercial Invoice (Proforma)"]
        n11["Check ATP (Product Allocation Availability Check)"]
        n12["Create Auto Inbound Delivery"]
        n13["Receive Goods Receipt(Virtual)"]
        n14["Issue Material to ODM Supplier (541)"]
        n15["IC Invoice Trading Str. Dependent"]
        n16["Calculate Taxes"]
        n17["Create/ Update Freight Unit and Order"]
        n18["Select Carrier"]
        n19["Calculate Charges"]
        n20["Feed Rates/Charges: Freight forwarders (SAP TM)"]
        n21["Execute Freight Order and Status Updates post GI"]
        n22["Receive Reconciled Carrier Invoice(s)"]
        n23["Create/ Update Freight Settlement Document"]
        n24["Create Service PO/ Entry Sheet"]
        n25["Allocate Freight Costs to Delivery Items (CO/PA) or Material Valuation"]
        n26["Post Accrual to Freight Expense Account(s)"]
        n27["Feed Rates/Charges: Freight forwarders (Within TM)"]
        n28["Generate Stock Transport Order"]
        n29["Initiate GTS (Export Declaration)"]
        n30["Confirm STO"]
        n31["Manage STO"]
        n32["Create Stock Transport Request"]
        n33["Create Manual Stock Transport Request"]
        n34["Approve Stock Transport Request"]
        n46(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n47(["fa:fa-play Initiate Manual Stock Transport Request Creation"])
        n51(["fa:fa-stop Commercial Invoice Generated"])
        n52(["fa:fa-stop Export invoice Generated"])
        n53(["fa:fa-stop Material Issued to ODM Supplier"])
        n54(["fa:fa-stop Accrual to Freight Expense Account(s) Posted"])
        n55(["fa:fa-stop Freight Costs to Delivery Items (CO/PA) or Material Valuation Allocated"])
        n57{{"fa:fa-code-branch Cross Border?"}}
        n58{{"fa:fa-code-branch exclusiveGateway"}}
        n59{{"fa:fa-code-branch exclusiveGateway"}}
        n60{{"fa:fa-code-branch exclusiveGateway"}}
        n61{{"fa:fa-code-branch exclusiveGateway"}}
        n62{{"fa:fa-code-branch exclusiveGateway"}}
        n63{{"fa:fa-code-branch Product Allocation Available?"}}
        n64{{"fa:fa-code-branch exclusiveGateway"}}
        n65{{"fa:fa-code-branch exclusiveGateway"}}
        n69{{"fa:fa-arrows-alt parallelGateway"}}
        n70{{"fa:fa-arrows-alt parallelGateway"}}
        n71{{"fa:fa-arrows-alt parallelGateway"}}
        n72{{"fa:fa-arrows-alt parallelGateway"}}
        n73{{"fa:fa-arrows-alt parallelGateway"}}
        n74{{"fa:fa-arrows-alt parallelGateway"}}
        n75{{"fa:fa-arrows-alt parallelGateway"}}
        n76{{"fa:fa-arrows-alt parallelGateway"}}
        n77{{"fa:fa-arrows-alt parallelGateway"}}
        n78{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n69
    n69 --> n3
    n4 --> n70
    n70 --> n6
    n7 --> n71
    n71 --> n57
    n57 -->|"Yes"| n59
    n57 -->|"No"| n10
    n37 --> n38
    n38 --> n79
    n58 --> n8
    n79 --> n39
    n69 --> n64
    n41 --> n40
    n13 --> n72
    n72 --> n15
    n14 --> n53
    n17 --> n75
    n18 --> n19
    n19 --> n20
    n20 --> n74
    n21 --> n76
    n22 --> n23
    n23 --> n24
    n24 --> n73
    n73 --> n25
    n25 --> n55
    n42 --> n81
    n48 --> n42
    n66 --> n35
    n81 --> n66
    n74 --> n66
    n75 --> n66
    n62 --> n22
    n35 --> n62
    n46 --> n27
    n27 --> n61
    n43 --> n82
    n81 --> n61
    n44 --> n56
    n50 --> n45
    n45 -->|"FO & HAWB Mapping"| n66
    n5 --> n77
    n28 --> n78
    n80 --> n84
    n29 --> n51
    n83 --> n58
    n83 --> n59
    n8 --> n67
    n77 --> n28
    n3 --> n77
    n78 --> n2
    n70 --> n80
    n2 --> n36
    n11 --> n63
    n63 -->|"Yes"| n30
    n31 --> n64
    n63 -->|"No"| n31
    n69 --> n5
    n78 --> n60
    n30 --> n60
    n71 --> n60
    n60 --> n4
    n64 --> n11
    n36 --> n80
    n84 --> n67
    n84 --> n37
    n39 -->|"Goods Issue against
Delivery note"| n83
    n71 --> n58
    n10 --> n29
    n59 -->|"HAWB attached 
for TM Processing"| n9
    n67 --> n41
    n12 --> n13
    n72 --> n14
    n6 --> n17
    n75 --> n61
    n61 --> n18
    n15 --> n16
    n76 --> n68
    n74 --> n21
    n76 --> n62
    n73 --> n26
    n26 --> n54
    n82 -->|"Shipment Tracking App 
from R3 onwards"| n68
    n49 --> n43
    n82 --> n61
    n68 --> n44
    n40 -->|"4B2 GR"| n12
    n33 --> n34
    n32 --> n65
    n47 --> n33
    n34 --> n65
    n65 --> n1
    n9 --> n52
    n79 -->|"Label Printing"| n7
    class n46 startEvt
    class n47 startEvt
    class n48 startEvt
    class n49 startEvt
    class n50 startEvt
    class n51 endEvt
    class n52 endEvt
    class n53 endEvt
    class n54 endEvt
    class n55 endEvt
    class n56 endEvt
    class n57 gateway
    class n58 gateway
    class n59 gateway
    class n60 gateway
    class n61 gateway
    class n62 gateway
    class n63 gateway
    class n64 gateway
    class n65 gateway
    class n66 gateway
    class n67 gateway
    class n68 gateway
    class n69 gateway
    class n70 gateway
    class n71 gateway
    class n72 gateway
    class n73 gateway
    class n74 gateway
    class n75 gateway
    class n76 gateway
    class n77 gateway
    class n78 gateway
    class n79 gateway
    class n80 gateway
    class n81 gateway
    class n82 gateway
    class n83 gateway
    class n84 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtWltv2zgW_iuEi25SwGmsKxU_7MKx40yApjFit8Visg-MTNtCZUlDUblsmv--hzKPbNPMTKvZPhTV4bl858pjqS-dOJ_zTr_z_v1LkiWyT16O5Iqv-VGfHN2zkh91yYbwlYmE3ae8PFI8izyT0-S_NZvjF0-KTdHGbJ2kz4o65cucky9XXTIAwbRLSpaVJyUXyeKoe1SIZM3E8zBPc6G43_Fo0VvU1vTReS7mXGwZej3qxAGIpknGt2SP-tQfK7mSx3k231O6CBbRIj56VeDS_DFeMSFr-FXJr9nTt2QuV_C8YGnJgWcl1-knds9T5aMUlaLFlXjAYCSlspNBwKYFi5NsCXS_ByTBsu9bUtB7fSWv79_fZY1RMhvdZQT-xCkryxFfkFIC-eJBkkWSpv13_nAwDnrdUor8O--_cy_oyHO7sfKkD673uiq4J488Wa5k_z5P55r15FH50HeLp6546ru9rniGvw1bPJtvLQ1DN3KjxtI5dYbOEC0tFou_ZQniKmas_K5tXXhjdzxqbDlBGAx7h_rQzZFPB44ZJy4ekpjvKB2Px97FNlQXYeD03lZ6PvbC3tBQumSSP7LnrcKzod8oHAd07NA3FW7smSir-4nIY1ToXQTjoFFIz53xwH1ToT9w_EgjBD1LwYoVOc-rupbJoCjKzZn6k3nB73edWx7z5IGfTiGx5Cpb5GLNZJJnJMnIkAmRcAHkhxziRm5VV8RJmtQcp6OkLCrJP378eNf5z47eMHx5uessWH_BTtREOLmHmo5XhD_FaVWCsctNyO46r68bMbBtYL54klxkLCUTKO2Mi9NpVRQpgNnFHwJ-xDjMs0WC2G_zSkL_kMsqmfPT4e31PkCPguAkib8Dj3ESqRNmOzmDk085mx-c-D0lk5eSTFbPZRID6DqohST5glyDr2pmEbZkSQZM09kNYZLcjK5J49O-PkejIzdqapHpKinWPJPkMs_nJTnWHn8wpFyQGnM-J7dgsTwdwqhY8hJyJzmEVOaiJJ6YkwLi-YydQO4qt-d4gHf-CMoNjR5oPM_z76czyA8AkXlTEQ8JI-ef_U-GhA8S08HEdhRsc2WcRMe_Y7UUKTSSKn5eKuSJhEoDj87h7pgTlVd4bDwbPLAkVbcI6Puwq_DMUIiKbOh3BYOeIXjxAGEvyaS6T5Nyxecmf7jlL2VeQNHyuKoLkG8k0dDJ5WwG1gtZiQMtIf3VbtmIRa3E6NlWDKKRP5YnLJWqKlia8tQuFPXaCDlthNw2Ql4bIf_XhA5HlCr06an_2-DzgFxNdlSr_h0KripuKnPo4xmkpixyuLrrjt6v_7pvExh1sAHV3ZpinZbbwoehYYwjkJqJZLmEcr6cTclwxePvRmNtYdxU8l5dAmTEUygN8bzPuenNNK5SxTxjT7w0Jrqydk0u1vd8PufGnMBh2iVqcBIGZr4Uc9C0zxbhlNyMsauyrAwONWEvnuo44Y1zPOGivpKMaeeomTvM12suYjVct_wit_LXOVExIoPZpGabV7EkgzTN482doccJ3G4wH2tWU4e7DeiggmF4lf1ZUB1ve7tqn_W1cPw1EbJiqalfJawOy_bSACu7FwU5DnzHFFPZuxo2IYBiU3cUlJ74CNAKNbszaciEf5VxhzbOnup0krGoFznyBeZpnWZLNTsqzVOecgiuddw7Z3um9TA3WqJnvcv6DQJI8SNTxuE6VG04uzaC4jp1LalxvMW9uU4V8Klksiq1XyUp6rK8MlS4O_nDzQcgGUvRcWma9t6O3JRLmfL6Mh_lcbU-SIy707RTfUdPbk7JRSZhf5uuODcFVPZ1FW_tDMGhUhUPlia5knytdoeb08ngA8nFtsS-srSqO8BQHGK_DuJYVJtaRP3QpTwruTqCDpCHMaC_kMBviVzBsnmYQ1VKlxyWv5-dpKq0msteTcVjPU5GHLZrUXtpGPE2g6TeHS1TVpXRNcvYklsO3bfn_C3_o-KlkStvWxkQ_kzF9OfkVFHA7i7yh5-05If_752KvrVT_bkjpHZ3U1x7q5NjrE6WWY6pP1i73IO1qzaZ_JWcZ8g1LVAP3bk5bE1x3xD_qb4gqoUOoQSGrr_VuHiLHZp5Y7UcihxqYfNS5F_GXhS02yuDs3ZbbK-dmNNOzG0n5tnF3l4iUm6GNfTbmQ7aibXZ8mmbLZ-22fJpmy2fttnyqd9GKGgjFLYRom2Eopa_XDKHnJz8U1WHfg7PNgRPP_ubR6rfSME_tAA-63MHn7XCgGpCUHP8uOv8W610P9RYME8-5_WBgzY8rdSLkBBpK42oJiADRdSmG6GPfmhcPhpxPK3TRR3uhuAEyKF9DzAWDjrbcGgYDpp1tFl8cQn_0CKIw9U4KAbQ1WZdtOJqYG4jgjlADoociMMNNFIk-FpphGnxNVIfvQ1DHTEUibASmsz6JiEwCCFCR6UeciDB11ZcrAZXhzBsgGlfItfE0XBgGtBsoGPqN94GupDGN-Qf5LfBt3O4EYuifiv3YwevRkcbMFhWWEaR1hw1odf5DBBMpOEGkUnAEtA6QzRCtcduU8wGCqolXKPDoqaGdKbQDQcjhPUQekaLeU0nOUYbNKy65zzHaJjAQBU2qnoGATu9IYSYF3zWiXPQhhcankW-ESwkeEjwzjTenTcE-Nr0Lms2oixXrxZ-qHSYcwjD7mh0bjNDUHVdMExKFq9g47tT77vhlwfux1hFzWTR-fTRKwfnhmcOkiYQ-pmajdQEX4N1GrCaw2l6T-sII6M7XcfkcM0p0UwazREgrsjVEWheJ8OyXr_nVp8FVCREvia3HvwkUL_MNrXVIPB1xfjenrpdt3DoNEO4pw365y65vN1M_WZ4aLwecnuor-lzvBfQoucbHCHGTT9jUbt79wQAqD_DQYqTTGKC6c43l3py4Se0fTp9gx69QT-z02GI2emO_py2T3WtVM9K9a3UwEoNrVSKX7D2yZGdfGYlwzSwkh072bWTPTvZt5MDOzm0k-1ehnYvQ7uX1O4ltXtJ7V5Su5fU7iW1e0ntXlK7l9TuJbV7Gdm9jOxeRnYvI7uXUeNlp9uB3_trlsw7_ZdO_Z8COv3OnC9YlcrOa7fDKplPn7O4068_nneq-k3aKGFLwdYb4uv_AKiA1Vs=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 E2E_44C_R3_Intel_Owned_Consignment_with_Planning_Integration_-_Subcontracting_Process_with_ODM_Suppl — E2E_44C_R3_Intel_Owned_Consignment_with_Planning_Integration_-_Subcontracting_Process_with_ODM_Suppl

**Swim Lanes**: Boundary Apps · External Partners/Supplier · SAP S/4HANA IP | **Tasks**: 34 | **Gateways**: 14

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
    subgraph Boundary Apps
        n31["Organize Transport-Intel Routing Guide (IRG)"]
        n32["ReadSoft Validation/Exception Handling based on rules setup"]
        n33["Incoming invoice/ B2B/OpenText/Web suite"]
        n34["Manual invoices through OCR"]
        n48{{"fa:fa-code-branch exclusiveGateway"}}
        n49{{"fa:fa-code-branch B2B/Manual?"}}
        n50{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/Supplier
        n19["Receive PO at ODM Supplier"]
        n20["Commit Order Acknowledgement"]
        n21["Send PO communicatio n to 3PL"]
        n22["Select Carrier via Intel Routing Guide hosted Collaboration Portal"]
        n23["Pick Up Goods (Carrier) Order shipment"]
        n24["Run MRP at ODM End"]
        n25["Execute Real-time Consumption"]
        n26["Copy ASN to 3PL"]
        n27["Receive Physical Receipt at 3PL"]
        n28["Send Shipment to EC via OTC process for direct ship – Manual"]
        n29["Perform ODM Supplier Invoicing"]
        n30["Execute Forecast Communication and Commit"]
        n36(["fa:fa-play Initiate Run MRP at ODM End"])
        n37(["fa:fa-play ODM Updates Received"])
        n39(["fa:fa-stop PO communication to 3PL Sent"])
        n40(["fa:fa-stop Shipment Sent"])
        n46{{"fa:fa-code-branch exclusiveGateway"}}
        n47{{"fa:fa-code-branch exclusiveGateway"}}
        n54{{"fa:fa-arrows-alt parallelGateway"}}
        n55{{"fa:fa-arrows-alt parallelGateway"}}
        n56{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4HANA IP
        n1["Create Subcon Purchase Order"]
        n2["Trigger GTS Check"]
        n3["Calculate Taxes"]
        n4["Post consumption movement 543"]
        n5["Inbound Delivery with House Air Waybill Number (HAWB)"]
        n6["TM Embedded"]
        n7["Receive Goods Receipt at ODM Location"]
        n8["Stock Transport Order Supplying Loc. – ODM/Rece. Loc. Intel WH"]
        n9["Receive Stock Transport Order"]
        n10["Receive Inbound Delivery at Intel WH"]
        n11["Receive Goods Receipt Stock Unrestricted (Intel WH)"]
        n12["Evaluate Receipt Settlement (ERS) Self-Billing"]
        n13["Post Supplier Invoice"]
        n14["Publish Purchase Order"]
        n15["Acknowledge/Confirm Purchase Order"]
        n16["Create Subcon Purchase Requisition"]
        n17["Create Subcon Purchase Requisition (Manual)"]
        n18["Approve Subcon Purchase Requisition"]
        n35(["fa:fa-play Initiate Creation of Subcon Purchase Requisition (Manual)"])
        n38(["fa:fa-stop Consumption Movement Posted"])
        n41["E2E-44 R3 CFIN"]
        n42["E2E-44 R3 SAP Transportation Management"]
        n43{{"fa:fa-code-branch exclusiveGateway"}}
        n44{{"fa:fa-code-branch Invoice Accepted?"}}
        n45{{"fa:fa-code-branch exclusiveGateway"}}
        n51{{"fa:fa-arrows-alt parallelGateway"}}
        n52{{"fa:fa-arrows-alt parallelGateway"}}
        n53{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n51
    n51 --> n2
    n21 --> n39
    n19 --> n20
    n24 --> n25
    n4 --> n38
    n25 -->|"New RICEFW"| n4
    n54 --> n5
    n5 --> n52
    n52 --> n6
    n26 --> n46
    n52 --> n46
    n52 --> n43
    n27 --> n55
    n55 --> n28
    n28 --> n40
    n7 --> n8
    n8 --> n9
    n9 --> n10
    n10 --> n11
    n11 --> n12
    n44 -->|"Yes"| n13
    n13 --> n41
    n47 --> n29
    n44 -->|"No"| n47
    n6 --> n42
    n51 --> n3
    n3 --> n53
    n2 --> n53
    n14 --> n56
    n15 --> n22
    n22 --> n31
    n56 -->|"WebPO/
E2Open"| n19
    n56 -->|"Manual/ E2Open/
Power BI"| n21
    n48 --> n32
    n33 --> n50
    n50 --> n48
    n49 --> n34
    n49 --> n33
    n34 --> n50
    n12 --> n48
    n29 --> n49
    n53 --> n14
    n31 --> n23
    n36 --> n24
    n23 --> n54
    n54 --> n26
    n55 --> n43
    n46 --> n27
    n43 --> n7
    n37 --> n47
    n32 --> n44
    n20 --> n15
    n17 --> n18
    n16 --> n45
    n35 --> n17
    n18 --> n45
    n45 --> n1
    class n35 startEvt
    class n36 startEvt
    class n37 startEvt
    class n38 endEvt
    class n39 endEvt
    class n40 endEvt
    class n41 startEvt
    class n42 startEvt
    class n43 gateway
    class n44 gateway
    class n45 gateway
    class n46 gateway
    class n47 gateway
    class n48 gateway
    class n49 gateway
    class n50 gateway
    class n51 gateway
    class n52 gateway
    class n53 gateway
    class n54 gateway
    class n55 gateway
    class n56 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWNtu4zgS_RVCjUbSgD0WdfHtYRa2YycBOolhpydYjPeBliibiCxqKSlxNp1_36JEKjYjD6YzeWi0SnXqeqpI69UKeEitofX16ytLWD5Er2f5lu7o2RCdrUlGz1qoEvxBBCPrmGZnUifiSb5k_yvVsJfupZqUzciOxS9SuqQbTtGP6xYaATBuoYwkWTujgkVnrbNUsB0RLxMecyG1v9B-ZEelN_VqzEVIxbuCbfdw4AM0Zgl9F7s9r-fNJC6jAU_CI6ORH_Wj4OxNBhfz52BLRF6GX2T0huwfWJhv4TkicUZBZ5vv4u9kTWOZYy4KKQsK8aSLwTLpJ4GCLVMSsGQDcs8GkSDJ47vIt9_e0NvXr6ukdoruL1YJgr8gJll2QSOU5SCePuUoYnE8_OJNRjPfbmW54I90-MWZ9i5cpxXITIaQut2SxW0_U7bZ5sM1j0Ol2n6WOQyddN8S-6Fjt8QL_Gv4okn47mnSdfpOv_Y07uEJnmhPURT9I09QV3FPskfla-rOnNlF7Qv7XX9if7Sn07zweiNs1omKJxbQA6Oz2cydvpdq2vWxfdroeOZ27YlhdENy-kxe3g0OJl5tcOb3Zrh30mDlz4yyWM8FD7RBd-rP_Npgb4xnI-ekQW-Evb6KEOxsBEm3aMyLkstolKZZ9U7-JS7-c2XdiQ1JYPjQPRAvS7nI29dJTmO04EUOHESXBQspOr9eXH5bWf85hDsAX1ASLnmUoz9IzEKSM550pvuApvJ_6IokYSyNyOkPEUhEAVMPjciL1LDmgrXrJOA7qc-SJw6d6qCxM-7cpTS5p_u880DXkBXLqQH1AHpDkoLEGpihfCt4sdmiu8niWNvrv76urIgMI9KW-6q9hsSDLaL7IC4y9kQvq4aurLe3Q9igGSYDrHz_y0D49q86gtkyWjfd51QkkNccJjyhIussizSNGRUHjvCgbERAwSaa3yGSo7uLG1RrHqXv2KA84bsdAy25FdEoeEz4c0zDDWzmJDfUJUeWEJg0DM3ZFQkLZJtRgnKO3Pl3Q98p9WMa5GhChAD_6IkR1MSpLc9yYAWs2JisuSjJg-bAQBIbRiU35ix4RD9SdMl5mKFzZfybSiLbsrQhesmMRZGgm8Vcl2UKRT5W8kFpuqdBkVMEfI7bOdtRCCvJil3JY0O_W1YwhXla3jYXoXfYkO1LBiWD5KUgzWUcHxF9XealSkQank7K2t3dT1AKG4FmGYq4QCETsrwyZbQqHBu7qGKgYVPSYk4FQHZHhIBmyCGBRhhzZB8UYsbBCcmgiwdNTxAMNKrYY2C7539qsqcxrMNruAAwIivaVP5vh9CeAZVqP1JYJjDGqoofMIN3TJbz1GSnJidaVpw4xHq2ga1L3qTc_dy26H0K5nvvMOA3f87aJM5RSgSJYxqfAPmfAXV_DfRxNS1Hc7TseFej2xG6nh-uIzkegsreL4t1IGe6EHBzyWg1qwZLQftesM0GeHl5v0STLQ0eDW5JgyQOiljavCd7mhkrXRIdlglQoJ5ZtONP5T5Dvuceq_vlSbOWpyK6oDF0A87GZ5Zv0RWHSwcaMYEeyMsazl90W-zWENn51ehhbJx_cg3cA6FBIQypsVQON0C1sQ7GXxL8O6-Iegwr10DOYdPVx7FacOXwvsjlCcjf9NyDpY40_Fslrbbsw9Wx0cPjodH4sTq2D_Q_1AnCb_aC8cmUK6c_EkHh3sICufTPtRGjqFjyYfpE4qLcHdoAzfO46ub5dLH8BoI4ao-hQR-WGHY1GYx1Z1wacEmaYh2zbPuXBMWSLgdnZAcOhojBSv1LUPf0ECzofwuWsY_Nx72_BULn1bY3Kye5Azc8wZ9-wafrn9rbZSDSHY_-bjRHG7pvbNmD8xTd6Nmcl1cAc-dKJk2dadvz0MJFk9n1rTHvzpGC3EQ1o6uYISbSdJ3x3M-tc68ZppgFVyh546WheQX0_M8dA_gzG935DMj95DGQYNRu_y5DVc--Ejjq2VHP7kADBkrB1hqeEvhKoJ7dvlbwpeDnyrqlz2hxPZnOHlbWT9DTLhVA4331qEPwnUrQ1fa61bPXNRQ-ClwN6SmbtQ_lxKmD7CuITksh9Hv1WldBFQFrbWwrga4jVnXDOgvPU1X4tzz2fsoNp1Vd5VpjPeXbGZjYW15Vrqde6Eo4Rve0aWXZr-tgPGNdel05rOtS919B3JogXRUL_Iqb33VWydSRP-yqlAamUrVUOqhSAu05f4ZVPr4u9Z06Y1VeV7t1deS6wL4qsKcb4qkWuJ4pqJP3DBvYMWw4CuLVcSu3WBt19TjURlXJHa3h6EhNOjtdg2s1Gz1tQ7fRUzb0s6sIUPfZ1ZHXXjXfNKGxgmCdG9bc0BquCgNro7hvaHha4-BLRonTH6aO5d0T8t4JeV99dDqWDpqknt0oxc2WPeeE3NVfdY7FXrPYbxZ3m8W9ZnG_WTxoFAOpG8W4Wew0i5uz9Juz9Juz9OssrZa1o2JHWGgNX63yM681tEIakSLOrbeWRYqcL1-SwBqWn0OtovyJd8EI_J7YVcK3_wOJR8Hn" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-44_R3_CFIN, E2E-44_R3_SAP_Transportation_Management, E2E_44A_R3_Intel_Owned_Consignment_with_Planning_Integration-Procurement_from_Component_supplier_and, E2E_44B_R3_-_Intel_Owned_Consignment_with_Planning_Integration-Shipment_of_components_from_Intel_War, E2E_44C_R3_Intel_Owned_Consignment_with_Planning_Integration_-_Subcontracting_Process_with_ODM_Suppl | |
| CFIN | E2E-44_R3_CFIN,  | |
| MBC | E2E-44_R3_CFIN,  | |
| SAP S/4 (IP & IF) | E2E-44_R3_CFIN, E2E-44_R3_SAP_Transportation_Management,  | |
| External Partners/
Supplier
 | E2E-44_R3_SAP_Transportation_Management,  | |
| External Partners/Suppliers | E2E_44A_R3_Intel_Owned_Consignment_with_Planning_Integration-Procurement_from_Component_supplier_and,  | |
| SAP S/4HANA IP | E2E_44A_R3_Intel_Owned_Consignment_with_Planning_Integration-Procurement_from_Component_supplier_and, E2E_44B_R3_-_Intel_Owned_Consignment_with_Planning_Integration-Shipment_of_components_from_Intel_War, E2E_44C_R3_Intel_Owned_Consignment_with_Planning_Integration_-_Subcontracting_Process_with_ODM_Suppl | |
| External Partner/Supplier | E2E_44B_R3_-_Intel_Owned_Consignment_with_Planning_Integration-Shipment_of_components_from_Intel_War,  | |
| External Partners/Supplier | E2E_44C_R3_Intel_Owned_Consignment_with_Planning_Integration_-_Subcontracting_Process_with_ODM_Suppl | |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
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

    subgraph E2E44CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E44CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E44CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E44CDAA_e_g_XEUS -.-> E2E44CDAD_e_g_Azure_SQL
    end
    style E2E44CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E44CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E44CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E44CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E44CDAA_e_g_MES_300 -.-> E2E44CDAD_e_g_SAP_HANA
    end
    style E2E44CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E44CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E44CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9vmkAUx_-Vyy3GLdGOquhK0iaH4NqENl2x25KykBMeeukJBI5Va_3fdwdKN6td07uEeO_H9z0-j5wrHCQhYAM3GisWM2GgVVPMYA5NAzUnNIdmCzVzCIqMiaUDv4ErB0-SylOGfqcZoxMOeVNlR0ksXPZYChzr6UKFKduIzhlfKqsL0wTQ7UULEZnIm2sVwZOHYEYzUWoUOVzSxQ8Wipk8R5TnIGNmYs4dOgGuComsULZYdu-mNGDxVBq7ujRlNL5_NvX09RqtGw0vrkugsenFSK6A0zy3IEI0Tc1kgSLGufHB1K3RaNTKRZbcg_FB0wYDs785th9UT0YnXbSChCeZcnctfVcvnAyXfCNHdKtPBrVcxx5Y3c5BuWNTtzvajhwk_Lm90cjUTb3WGw41uQ7q9fvK7cWVYl5MphlNZ8ju2L3e0CJDxwd_6pPHIgPf_ebceRh5-FcVrVbIMggES-IamlrbdFJm_7RvXZkIR9MjpH5LAcMwKqYvc6ydih897BXhl24on2HQ84oINPnKSqwMQjLIw5-UZIn1tS5Q-6h9dqhSlQhxuGEhlhwOgtjCJmrXsG1N7X9hH6eL_-F1ybV_Tq7Iu-he2q7f1bQtYHlE8vgWxnXZVxDLGKRi3kJ408k-yNtSb2G8jX0X4v1l0enp2dMGkFUyRZ8Rub6QzxHj4OGnwx_FzugcmMr27_4iFoQassiYIHIzPL8Y28Px7Y2NHPurfWUdmKZz82x1fDV3kqacBVR594_O8a0Dc7KooOom3j8ix7elvB2H7SRqOyyCSr66MvaOo3rDLX1d7Zr-ycnJC_S4heeQzSkLsbHC5Y0v_y9CiGjBBV63MC1E4i7jABvlpYyLNKQCLEYl0XllXP8BySb1Tw==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E44FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E44FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E44FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E44FDAA_e_g_XEUS -.-> E2E44FDAD_e_g_Azure_SQL
    end
    style E2E44FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E44FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E44FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E44FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E44FDAA_e_g_MES_300 -.-> E2E44FDAD_e_g_SAP_HANA
    end
    style E2E44FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E44FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E44FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9vmkAUx_-Vyy3GLdGOquhK0ianwNqENl2x25KykBMeeukJBI5Va_3fdwdKN6td07uEeO_H9z0-j5wrHCQhYAM3GisWM2GgVVPMYA5NAzUnNIdmCzVzCIqMiaUDv4ErB0-SylOGfqcZoxMOeVNlR0ksXPZYChzr6UKFKZtN54wvldWFaQLo9qKFiEzkzbWK4MlDMKOZKDWKHC7p4gcLxUyeI8pzkDEzMecOnQBXhURWKFssu3dTGrB4Ko1dXZoyGt8_m3r6eo3WjYYX1yXQeOjFSK6A0zw3IUI0TYfJAkWMc-PDUDdt227lIkvuwfigaYPBsL85th9UT0YnXbSChCeZcndNfVcvnIyWfCNHdLNPBrVcxxqY3c5BueOhbnW0HTlI-HN7tj3Uh3qtNxppch3U6_eV24srxbyYTDOazpDVsXo92yQjxwd_6pPHIgPf_ebceRh5-FcVrVbIMggES-IamlrbdFJm_7RuXZkIR9MjpH5LAcMwKqYvc8ydih897BXhl24on2HQ84oINPnKSqwMQjLIw5-UZIn1tS5Q-6h9dqhSlQhxuGEhlhwOgtjCJmrXsC1N7X9hH6eL_-F1ybV_Tq7Iu-heWq7f1bQtYHlE8vgWxnXZVxDLGKRi3kJ408k-yNtSb2G8jX0X4v1l0enp2dMGkFkyRZ8Rub6QT5tx8PDT4Y9iZ3QOTGX7d38RC0INmWRMELkZnV-MrdH49sZCjvXVujIPTNO5ebY6vpo7SVPOAqq8-0fn-OaBOZlUUHUT7x-R41tS3orDdhK1HRZBJV9dGXvHUb3hlr6udk3_5OTkBXrcwnPI5pSF2Fjh8saX_xchRLTgAq9bmBYicZdxgI3yUsZFGlIBJqOS6Lwyrv8ARNr1eQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-44-R001 | Report | R3 - Intel Owned Consignment with Planning Integration operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-44-C001 | Conversion | Legacy data migration for R3 - Intel Owned Consignment with Planning Integration | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-44.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E44C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E44C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E44CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E44CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E44C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E44CMW_e_g_Azure_Service_Bus
    E2E44CMW_e_g_Azure_Service_Bus --> E2E44C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1P4kAQ_iubGsIX0Kq82RiSlpYLl6LG-nKX49Is3SlsXNqmu1UR-e-32yLFotFbkpLOPPPM9pmZ3ZUWxAQ0Q6vVVjSiwkCrupjDAuoGqk8xh3oD1TkEWUrF0oVHYMrB4rjw5NA7nFI8ZcDrKjqMI-HRl5zguJM8K5iyDfGCsqWyejCLAd2OGsiUgayBOI54k0NKw_paoVn8FMxxKnK-jMMYP99TIubyPcSMg8TMxYK5eApMJRVppmyR_BIvwQGNZtLY0qUpxdFDaWrr6zVa12qTaJsC3ViTCMlVq6FmU24omNMxFtCkEU9oCgRxsWSAAoY5By4xBTx_tyFE04zTCDhH-QopY8bBUC6r3eAijR_AOLB6vY5ubV6bT-pLjJPkuRHELE6NA13XK5w4SVC5Ck6rrVi3nLre7Vqd_-AkWOB9Trv3BefxO843H8FcipfipdQUtSuZFpQQBk84hV1F7I5ZKuJ0O8OS7Ru7h5jtKaI03lF5MND1rzgLVp5NZylO5sh0_0y0SUZ6p0Q-yWkbmVdX7mhg3owuL5Br_nauJ9rfIkgtIhsiEDSOkHtdWp0Tp9Ua-ODP_LHj-ae6vssaQAfB4ewQSR-SPkloGIas8IcEv5xb78No5fg0dHyfB5svWQq-B-kjDcC3Mv7u6467BVOOQhsUkqiCtqxald12cvZBzIXvMDnvkejvbjFoFcQKgDaA82l61D-n_cLh3aEjNLLjQP799C4vzo9ov8iqurLIBxF5q8--oHLs-q8TLWez8yJIJvNqJJ9DymCivX6hxC7xZxiVpFoLtaVN0-THgOXujPhQ_2rEd0PNbaj-nUnea1YXZlKjd81BdOQ6P5wL-xtd6vqyt6utZSYJowFW4A-ay_XH99UWGpdt8mnbuL7tVDvEVsePEwl5i1QrX4Q4l8UwnnRISwJJMw6bLg03aeT877RJKWohypuwbfXbCnt2drZ3lmkNbQHpAlOiGSstv73k3UcgxBkT2rqh4UzE3jIKNCO_VLQskRsFm2JZhEVhXP8Du489aQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-44.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E44F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E44F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E44FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E44FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E44F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E44FMW_e_g_Azure_Service_Bus
    E2E44FMW_e_g_Azure_Service_Bus --> E2E44F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1P4kAQ_iubGsIX0Kq82RiS1pYLl6LG-nKX49Is3SlsXNqmu1UR-e-32yLFosFbkpLOPPPM9pmZ3aUWxAQ0Q6vVljSiwkDLupjBHOoGqk8wh3oD1TkEWUrFwoUnYMrB4rjw5NB7nFI8YcDrKjqMI-HR15zguJO8KJiyDfCcsoWyejCNAd0NG8iUgayBOI54k0NKw_pKoVn8HMxwKnK-jMMIvzxQImbyPcSMg8TMxJy5eAJMJRVppmyR_BIvwQGNptLY0qUpxdFjaWrrqxVa1WrjaJMC3VrjCMlVq6FmU24omNERFtCkEU9oCgRxsWCAAoY5By4xBTx_tyFEk4zTCDhH-QopY8bBQC6r3eAijR_BOLB6vY5urV-bz-pLjJPkpRHELE6NA13XK5w4SVC5Ck6rrVg3nLre7Vqd_-AkWOBdTru3h_P4A-e7j2AuxUvxQmqK2pVMc0oIg2ecwrYidscsFXG6nUHJ9o3dQ8x2FFEab6l8caHr-zgLVp5NpilOZsh0_4y1cUZ6p0Q-yWkbmdfX7vDCvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonTqs18MGf-iPH8091fZs1gA6Cw-khkj4kfZLQMAxZ4U8Jfjl33qfRyvFl6OghDzZfsxR8D9InGoBvZfzD1x13C6YchdYoJFEFbVm1Krvt5OwXMRe-w-S8R6K_vcWgVRArAFoDzifpUf-c9guHd4-O0NCOA_n307u6PD-i_SKr6soiH0TkvT67gsqx67-NtZzNzosgmczroXwOKIOx9rZHiW3irzAqSbUWakvrpsmPAcvdGvGBvm_Et0PNTaj-nUneaVYXplKjD81BdOQ6P5xL-xtd6vqyt6utZSYJowFW4E-ay_VHD9UWGpVt8mXbuL7tVDvEVsePEwl5i1QrX4Q4V8UwnnRISwJJMw6bLg3XaeT8b7VJKWohyruwbfXbCHt2drZzlmkNbQ7pHFOiGUstv73k3UcgxBkT2qqh4UzE3iIKNCO_VLQskRsFm2JZhHlhXP0DAg89gQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-44-I001 | Interface | R3 - Intel Owned Consignment with Planning Integration inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-44-E001 | Enhancement | R3 - Intel Owned Consignment with Planning Integration custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-44-F001 | Form/Report | R3 - Intel Owned Consignment with Planning Integration operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
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

    subgraph E2E44CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E44CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E44CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E44CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E44CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E44CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E44CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E44CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuDe2AqwTjvM13pd1JRsmBQa2p1zgsR0ccOMByVG1WmtJCsKdsqNYIlB3R7rSNXLmRaqyoYf0hXpBIdo6nhhmx-0EysZJwTVoOsWYk1m5EFMLWRqBqlFdJ9VJKUFkspjgwpVaS4O0q20baoHQzi4rAF-ubFBZIjZaSup5AjUpYe36CcMuacefY0DEO9FhW_A-fMMC4vvfE-_PCgPDlmudFTznil0tbUfs0rGRFHoD8Jxv7HA9CaTALLfwm0jsChZwem8QoInB15YejZnn3g-b4hx0mD47FKx0VPrJvFsiLlCgVmMBr589k8gWSZuI9NBcmckOhXjOPGHBvDuMnBkDufL89Rl0YqHePfPUiNjFaQCsoLNPt6VJ_Jbkf-GdwqZodR3xLgOE7f8H4NFNnem9gyOGnsn5r55uGjZJR8dr-4iWmYVnf-bGJlcs6I_XcXoosRUnVI1b27ETdBlFiG8dwLGSIZvrMdL6z-h468Rb-6-vS0NzvtzocukDu_lnNIGcT46eRVYR2voVoTmmFnh7s3Qr4wGeSkYQK3OiaN4NG2SLHT_ca4KTMiYEqJvJ51L7Z_AHnQblo=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E44FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E44FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E44FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E44FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E44FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E44FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E44FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E44FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DPTCVYJz3ma70O6koWTKoNbU644UI6WMHGI7KjSpTWkByyrZKDWHFAd1e68iVC5nWqgrGH5I1qUTHaGq4IZsfNBVrGWeE1SBr1iJnc7IEpjYSVaO0QroPS5LQYiXFkSGlihR3R8k22ha1g0FUHLZA37yoQHIkjNT1DDJEytLjG5RRxpwzz54FQaDXouJ34JwZxuWlN96HHx6UJ8csN3rCGa9U2prZr3klI-IInE788fTjAWhNJr41fQm0jsChZ_um8QoInB15QeDZnn3gTaeGHCcNjscqHRU9sW6Wq4qUa-Sb_mgULOaLGOJV7D42FcQLQsJfEY4ac2wMoyYDQ-58vjpHXRqpdIR_9yA1UlpBIigv0PzrUX0mux35p3-rmB1GfUuA4zh9w_s1UKR7b2LL4KSxf2rmm4cP41H82f3ixqZhWt3504mVyjkl9t9dCC9GSNUhVffuRtz4YWwZxnMvZIhk-M52vLD6HzryFv3q6tPT3uysOx-6QO7iWs4BZRDhp5NXhXWcQ5UTmmJnh7s3Qr4wKWSkYQK3OiaN4OG2SLDT_ca4KVMiYEaJvJ68F9s_nKFucg==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-44 — R3 - Intel Owned Consignment with Planning Integration</span></div>
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
*E2E-44 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

