<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">O-060 — Manage and Track Orders (IP)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Order To Cash (IP) (OTC-IP) Tower<br/>
  Capability O-060 · O Order Management (IP)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **O-060 Manage and Track Orders (IP)** within the IAO program. It includes 6 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Order To Cash (IP) (OTC-IP) |
| **Process Group** | O Order Management (IP) |
| **Capability** | O-060 - Manage and Track Orders (IP) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 5 Reports, 71 Interfaces, 20 Conversions, 167 Enhancements, 28 Forms, 1 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Order To Cash (IP) |
| **L1 Process** | O Order Management (IP) |
| **L2 Capability** | O-060 - Manage and Track Orders (IP) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | IP Order Management Transformation | Transform Intel Products order management onto S/4 HANA with integrated pricing and ATP | IDM 2.0 Products Revenue | High |
| 2 | Customer Experience Improvement | Reduce order processing time and improve order visibility for IP customers | Customer Centricity | High |
| 3 | Returns & Rebate Automation | Automate returns processing, rebate management, and chargeback handling | Revenue Assurance | Medium |
| 4 | O-060 Process Migration | Migrate Manage and Track Orders (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Order Management (Intel Products) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Processing Time | < 2 hours | Time from order receipt to order confirmation | 6 hours (current) | Order Management Lead |
| Customer Credit Decision Time | < 15 minutes | Automated credit check and approval for standard orders | 2 hours (manual) | Credit Manager |
| Returns Processing Cycle | < 3 business days | End-to-end returns receipt to credit memo issuance | 7 business days (current) | Returns Manager |
| O-060 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **6 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for O-060 Manage and Track Orders (IP).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | O-060-010_Receive_Customer_Order_Inquiry_(IP) | O-060-010_Receive_Customer_Order_Inquiry_(IP) | Customer Business Analyst | 8 | 15 |
| 2 | O-060-020_Receive_Request_for_Status_by_User_(IP) | O-060-020_Receive_Request_for_Status_by_User_(IP) | Customer Business Analyst | 8 | 15 |
| 3 | O-060-110_Review_Status_and_Determine_Options_(IP) | O-060-110_Review_Status_and_Determine_Options_(IP) | Customer Business Analyst | 14 | 4 |
| 4 | O-060-130_Create_Backorder_(Delinquent_)_(IP) | O-060-130_Create_Backorder_(Delinquent_)_(IP) | Customer Business Analyst | 22 | 19 |
| 5 | O-060-170_Change_Order_(IP) | O-060-170_Change_Order_(IP) | Customer Business Analyst | 8 | 15 |
| 6 | O-060-180_Cancel_Order_(IP) | O-060-180_Cancel_Order_(IP) | Customer Business Analyst | 11 | 15 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 O-060-010_Receive_Customer_Order_Inquiry_(IP) — O-060-010_Receive_Customer_Order_Inquiry_(IP)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 8 | **Gateways**: 15

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Upload Approved Document into Sales Order"]
        n2["fa:fa-user Apply Changes"]
        n3["fa:fa-user Receive Customer Order Inquiry"]
        n4["fa:fa-user Determine Changes to Apply"]
        n5["fa:fa-user Validate internal inquiry"]
        n6[["fa:fa-cog Check Order NCNRR Conditions"]]
        n7[["fa:fa-cog Check If Order Is In Cancellation Window"]]
        n8[["fa:fa-cog Apply Changes"]]
        n9(["fa:fa-play Customer Request Received for Change"])
        n10(["fa:fa-play Order Change Request Received from Customer via EDI"])
        n11(["fa:fa-play Order Change Request Received from Customer via Web Order Management"])
        n12(["fa:fa-play Receive Internal Inquiry"])
        n13(["fa:fa-play Order Change Request Received from Customer via Dassian"])
        n14(["fa:fa-stop Customer Informed about Rejection of Change Request via Email"])
        n15(["fa:fa-stop Customer Informed about Rejection of Change Request via EDI or WOM"])
        n16["Cancel Order"]
        n17["Allocate Product to Orders"]
        n18["Approve/Release Order (IP)"]
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch Is Order Subjected to NCNR?"}}
        n21{{"fa:fa-code-branch Is Order Inside Cancellation Window?"}}
        n22{{"fa:fa-code-branch Change Approved?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n25{{"fa:fa-code-branch Manual/ Automated Changes?"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch Inquiry related to change in RDD and Quantity to Existing Sales Order?"}}
        n28{{"fa:fa-code-branch Change related to reduction in QTY"}}
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n30{{"fa:fa-code-branch Is Delivery Note Available for SO1 OR SO2?"}}
        n31{{"fa:fa-code-branch exclusiveGateway"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n33{{"fa:fa-code-branch exclusiveGateway"}}
        n34[["fa:fa-folder-open Inform Plant/Warehouse of Order Change/Cancellation"]]
        n35[["fa:fa-folder-open A Check Credit Rating and Limits (IP)"]]
    end
    n9 --> n19
    n3 --> n33
    n10 --> n19
    n11 --> n19
    n20 -->|"Yes"| n32
    n6 --> n20
    n7 --> n21
    n23 --> n29
    n1 --> n24
    n22 -->|"Yes"| n1
    n2 --> n26
    n28 -->|"No"| n6
    n29 --> n15
    n29 -->|"For B2B"| n18
    n24 --> n30
    n34 --> n31
    n31 --> n25
    n32 --> n22
    n21 -->|"Yes"| n32
    n4 --> n31
    n30 -->|"Yes"| n34
    n19 --> n3
    n12 --> n5
    n5 --> n33
    n33 --> n27
    n13 --> n19
    n8 --> n26
    n26 --> n35
    n35 --> n17
    n27 -->|"Yes"| n28
    n27 -->|"No"| n24
    n20 -->|"No"| n7
    n22 -->|"No"| n14
    n25 -->|"Automated 
Changes"| n8
    n25 -->|"Manual
 Changes"| n2
    n30 -->|"No"| n4
    n21 -->|"No"| n24
    n28 -->|"Yes"| n16
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 endEvt
    class n15 endEvt
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
    class n34 subProc
    class n35 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWFtv2zYU_iuEisAtYCO6WoofNji-DAbapHXaBkWzB1qibC405erixEv933dokZJFyxuQzg-J9fGc71x5RPrFCJOIGAPj4uKFcpoP0EsnX5E16QxQZ4Ez0umiEviKU4oXjGQdIRMnPL-jfx_ELHfzLMQENsVrynYCvSPLhKAvsy4agiLrogzzrJeRlMadbmeT0jVOd6OEJamQfkOC2IwP1uTSdZJGJK0FTNO3Qg9UGeWkhh3f9d2p0MtImPCoQRp7cRCHnb1wjiVP4Qqn-cH9IiMf8PM9jfIVPMeYZQRkVvmavccLwkSMeVoILCzSrUoGzYQdDgm72-CQ8iXgrglQivljDXnmfo_2FxcPvDKKPo8fOIJPyHCWjUmMshzgyTZHMWVs8MYdDaee2c3yNHkkgzf2xB87djcUkQwgdLMrktt7InS5ygeLhEVStPckYhjYm-du-jywzW66g7-aLcKj2tKobwd2UFm69q2RNVKW4jj-JUuQ1_Qzzh6lrYkztafjypbl9b2Recqnwhy7_tDS80TSLQ3JEel0OnUmdaomfc8yz5NeT52-OdJIlzgnT3hXE16N3Ipw6vlTyz9LWNrTvSwWH9MkVITOxJt6FaF_bU2H9llCd2i5gfQQeJYp3qzQqMjyZE1SdF1k0O9ZhoYcs12Wl3Liw63vD0aMBzHuibSjLxuW4AgNN5s02ZIIjZOwWBOeI8rzBN1h2LroVuypB-PPIxa7yQLqbIdGK8yXJGtKOk3JOQkJ3ZLa1QM5mvEfBU13TVW3qTomOUnXEJcyhMDDg-WmmtdU-4oZjaB0IiKSQj7gS4ux_vdKLUyWYIKEj9K5m9HNfI5GMCdoThMuAjzW9Ns0Z7GKLIPg0AjzkDCGhT66pzxKnjSWoMmiZ_RY9OptJbph0JBVLufkR0GyXCU5QnGSSg6geHfcBabGUTpbyrbwpMm6NrOlGE3GM53S-kXKe7KQOh8wx0si2lC3YWs2VDvNVG3rRmroOb_o2xi2LMVcp3VrWhDe1DozDqlfAxVeJIVg_ouEh9onsW71kM01pkwn9_4v8vEMQR_c337QLfTBQNmZbXvc8mF5yFgSit0DkyoqwlzsuYOsts2tQAiXU-RyThiBU4DM8tvZx3ea8NXLS93sEekt4F0YrhB5DhlMri35oxy1D8Z-fzx0zHa1mRxR6K5YiFRAZsBLsWt_1xms_2CY8YxGpG27nlDZ7VSyAGqgnqg5rwvdfZ2a164GG6zA7BINC-goLBImJ82Ju_3X2fXP5LncnSglDMsyhWW-KEfz8RhhHqFPBeY5zXdidfJMsxwOSMdvohMfg3-txJGtlIgWFjUFc58-f9OJXteWzvm2HBMGahDwTQJbaLiFXS5Ow4e5fHdrods5_LP1gBzrdX7Yr1N7XUc6bv3CiuHAR9JesiFcDif0kUERL-9xSlYJvIbFaDqeuZfHO0x7vTleO_NQvlpHUEYKYw8fGkN0zHu6pnmmBo3kgvNr-YVfoV7vNzF15LNTPjuOfLZMTcCyNMA-SPx8ML6Jl_FPkWu50i8l1ZmW-_LZUprSmF1xy2dXCdgadaUpBfvqOZCCN8lBrsJVeF4DAMEpdNm1fV2yBmrVldErjx0FKMOOclEROsoVFbRtnUvHCddJ4lTclnS7KoI0oox6WpEclUhfKThakQI9YbI2ThWH5LQUhe1r3tmBviKTXZfLbC74ehklblUKnlyoZ-0Dr851IBnoguVwBvRYytYTKu24eklOHA70_uofXUNEP6rrVwO222GnHXbbYa8d7h_fzxor_tmV4OzKVXUrbsZlnsGtM7h9BnfO4K68ITdRrxXtn-Hwz-DBGfxKXUKbtTLbYasdttthpx1222GvHe63w347HLTD7VE67VE67VE67VE67VHCDJSX8SbsKdjoGnDyhlN6ZAxejMNPW8bAiEiMC5Yb-66BYXff7XhoDA4_ARnFRtw5xxTDzXxdgvt_AMD9BBI=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 O-060-020_Receive_Request_for_Status_by_User_(IP) — O-060-020_Receive_Request_for_Status_by_User_(IP)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 8 | **Gateways**: 15

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Upload Approved Document into Sales Order"]
        n2["fa:fa-user Apply Changes"]
        n3["fa:fa-user Receive Customer Order Inquiry"]
        n4["fa:fa-user Determine Changes to Apply"]
        n5["fa:fa-user Validate internal inquiry"]
        n6[["fa:fa-cog Check Order NCNRR Conditions"]]
        n7[["fa:fa-cog Check If Order Is In Cancellation Window"]]
        n8[["fa:fa-cog Apply Changes"]]
        n9(["fa:fa-play Customer Request Received for Change"])
        n10(["fa:fa-play Order Change Request Received from Customer via EDI"])
        n11(["fa:fa-play Order Change Request Received from Customer via Web Order Management"])
        n12(["fa:fa-play Receive Internal Inquiry"])
        n13(["fa:fa-play Order Change Request Received from Customer via Dassian"])
        n14(["fa:fa-stop Customer Informed about Rejection of Change Request via Email"])
        n15(["fa:fa-stop Customer Informed about Rejection of Change Request via EDI or WOM"])
        n16["Cancel Order"]
        n17["Allocate Product to Orders"]
        n18["Approve/Release Order (IP)"]
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch Is Order Subjected to NCNR?"}}
        n21{{"fa:fa-code-branch Is Order Inside Cancellation Window?"}}
        n22{{"fa:fa-code-branch Change Approved?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n25{{"fa:fa-code-branch Manual/ Automated Changes?"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch Inquiry related to change in RDD and Quantity to Existing Sales Order?"}}
        n28{{"fa:fa-code-branch Change related to reduction in QTY"}}
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n30{{"fa:fa-code-branch Is Delivery Note Available for SO1 OR SO2?"}}
        n31{{"fa:fa-code-branch exclusiveGateway"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n33{{"fa:fa-code-branch exclusiveGateway"}}
        n34[["fa:fa-folder-open Inform Plant/Warehouse of Order Change/Cancellation"]]
        n35[["fa:fa-folder-open A Check Credit Rating and Limits (IP)"]]
    end
    n9 --> n19
    n3 --> n33
    n10 --> n19
    n11 --> n19
    n20 -->|"Yes"| n32
    n6 --> n20
    n7 --> n21
    n23 --> n29
    n1 --> n24
    n22 -->|"No"| n14
    n22 -->|"Yes"| n1
    n2 --> n26
    n29 --> n15
    n29 -->|"For B2B"| n18
    n24 --> n30
    n34 --> n31
    n31 --> n25
    n32 --> n22
    n21 -->|"Yes"| n32
    n4 --> n31
    n30 -->|"Yes"| n34
    n19 --> n3
    n12 --> n5
    n5 --> n33
    n33 --> n27
    n13 --> n19
    n8 --> n26
    n26 --> n35
    n35 --> n17
    n28 -->|"Yes"| n16
    n28 -->|"No"| n6
    n27 -->|"Yes"| n28
    n27 -->|"No"| n24
    n20 -->|"No"| n7
    n21 -->|"No"| n24
    n30 -->|"No"| n4
    n25 -->|"Automated 
Changes"| n8
    n25 -->|"Manual
 Changes"| n2
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 endEvt
    class n15 endEvt
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
    class n34 subProc
    class n35 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWFtv2zYU_iuEisAtYCO6WoofNji-DAbapHXaBkWzB1qibC405erixEv933dokZJFyxuQzg-J9fGc71x5RPrFCJOIGAPj4uKFcpoP0EsnX5E16QxQZ4Ez0umiEviKU4oXjGQdIRMnPL-jfx_ELHfzLMQENsVrynYCvSPLhKAvsy4agiLrogzzrJeRlMadbmeT0jVOd6OEJamQfkOC2IwP1uTSdZJGJK0FTNO3Qg9UGeWkhh3f9d2p0MtImPCoQRp7cRCHnb1wjiVP4Qqn-cH9IiMf8PM9jfIVPMeYZQRkVvmavccLwkSMeVoILCzSrUoGzYQdDgm72-CQ8iXgrglQivljDXnmfo_2FxcPvDKKPo8fOIJPyHCWjUmMshzgyTZHMWVs8MYdDaee2c3yNHkkgzf2xB87djcUkQwgdLMrktt7InS5ygeLhEVStPckYhjYm-du-jywzW66g7-aLcKj2tKobwd2UFm69q2RNVKW4jj-JUuQ1_Qzzh6lrYkztafjypbl9b2Recqnwhy7_tDS80TSLQ3JEel0OnUmdaomfc8yz5NeT52-OdJIlzgnT3hXE16N3Ipw6vlTyz9LWNrTvSwWH9MkVITOxJt6FaF_bU2H9llCd2i5gfQQeJYp3qzQqMjyZE1SdF1k0O9ZhoYcs12Wl3Liw63vD0aMBzHuibSjLxuW4AgNN5s02ZIIjZOwWBOeI8rzBN1h2LroVuypB-PPIxa7yQLqbIdGK8yXJGtKOk3JOQkJ3ZLa1QM5mvEfBU13TVW3qTomOUnXEJcyhMDDg-WmmtdU-4oZjaB0IiKSQj7gS4ux_vdKLUyWYIKEj9K5m9HNfI5GMCdoThMuAjzW9Ns0Z7GKLIPg0AjzkDCGhT66pzxKnjSWoMmiZ_RY9OptJbph0JBVLufkR0GyXCU5QnGSSg6geHfcBabGUTpbyrbwpMm6NrOlGE3GM53S-kXKe7KQOh8wx0si2lC3YWs2VDvNVG3rRmroOb_o2xi2LMVcp3VrWhDe1DozDqlfAxVeJIVg_ouEh9onsW71kM01pkwn9_4v8vEMQR_c337QLfTBQNmZbXvc8mF5yFgSit0DkyoqwlzsuYOsts2tQAiXU-RyThiBU4DM8tvZx3ea8NXLS93sEekt4F0YrhB5DhlMri35oxy1D8Z-fzx0zHa1mRxR6K5YiFRAZsBLsWt_1xms_2CY8YxGpG27nlDZ7VSyAGqgnqg5rwvdfZ2a164GG6zA7BINC-goLBImJ82Ju_3X2fXP5LncnSglDMsyhWW-KEfz8RhhHqFPBeY5zXdidfJMsxwOSMdvohMfg3-txJGtlIgWFjUFc58-f9OJXteWzvm2HBMGahDwTQJbaLiFXS5Ow4e5fHdrods5_LP1gBzrdX7Yr1N7XUc6bv3CiuHAR9JesiFcDif0kUERL-9xSlYJvIbFaDqeuZfHO0x7vTleO_NQvlpHUEYKYw8fGkN0zHu6pnmmBo3kgvNr-YVfoV7vNzF15LNTPjuOfLZMTcCyNMA-SPx8ML6Jl_FPkWu50i8l1ZmW-_LZUprSmF1xy2dXCdiS-iY5MFsnC8pmRSkZ-upZxec1ANCcQptd29eldqBWXRm-ctlRgDLgKB8VoaNMqqht61w-TrhOMqfis6TbVRWkEWXU06rkqEz6SsHRqhToiZHFcao4JKelKOxAz3FfX5FlqXBf07ADfUVq1BU2mwu-nkRdwdEUKiJP4vXYfuDVEREEA12wnPOAHkvZR9cQ0Y_q-tWA7XbYaYfddthrh_vH97PGin92JTi7clXdiptxmWdw6wxun8GdM7grb8hN1GtF-2c4_DN4cAa_UpfQZq3Mdthqh-122GmH3XbYa4f77bDfDgftcHuUTnuUTnuUTnuUTnuUMALlZbwJewo2ugacvOGUHhmDF-Pw05YxMCIS44Llxr5rYNiSdzseGoPDT0BGsRF3zjHFcDNfl-D-H6gTBBI=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 O-060-110_Review_Status_and_Determine_Options_(IP) — O-060-110_Review_Status_and_Determine_Options_(IP)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 14 | **Gateways**: 4

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Check Sales Order Blocks/ Holds/Flags"]
        n2["fa:fa-user Block Sales Order for Intel Hold"]
        n3["fa:fa-user Block Sales Order for QSpec Order Hold"]
        n4["fa:fa-user Block Sales Order for CUST Customer Hold"]
        n5["fa:fa-user Sales Order for Fixed Material Flag"]
        n6["fa:fa-user Sales Order for Fixed Plant Flag"]
        n7["fa:fa-user Sales Order for Do Not Improve (DNI) Flag"]
        n8["fa:fa-user Block Sales Order for Build/ Prepayment Hold"]
        n9["fa:fa-user Block Sales Order for Milestone Billing Hold"]
        n10["fa:fa-user Apply Delivery Block for Sales Order"]
        n11[["fa:fa-cog Block Sales Order for MSL Hold"]]
        n12[["fa:fa-cog Block sales Order for Credit Block"]]
        n13[["fa:fa-cog Block sales Order for GTS Block"]]
        n14[["fa:fa-cog Block Sales Order for Contract Hold"]]
        n15(["fa:fa-play Request Received to Review Status and Determine Options"])
        n16["Analyze / Determine reason for block or hold (IP)"]
        n17["Review Block/Credit Hold (IP)"]
        n18["Change Order"]
        n19["Cancel Order"]
        n20["Inform Plant/Warehouse of Order Change/Cancellation"]
        n21["A Request Pre-payment, Down-payment or Letter of Credit (LOC)"]
        n22{{"fa:fa-code-branch Type of Block/ Holds/ Flags?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n25{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n13 --> n16
    n12 --> n17
    n11 --> n23
    n2 --> n23
    n15 --> n1
    n1 --> n22
    n23 --> n25
    n25 --> n19
    n25 --> n18
    n3 --> n23
    n4 --> n23
    n14 --> n23
    n5 --> n23
    n6 --> n23
    n7 --> n23
    n25 --> n20
    n22 -->|"Fixed
 Plant Flag"| n6
    n22 -->|"Fixed
 Material Flag"| n5
    n22 -->|"MSL Hold"| n11
    n22 -->|"Credit Hold"| n12
    n22 -->|"GTS Hold"| n13
    n22 -->|"Contract Hold"| n14
    n22 -->|"CUST 
Customer Hold"| n4
    n22 -->|"Do Not Improve
 (DNI) Flag"| n7
    n8 --> n24
    n9 --> n24
    n24 --> n21
    n22 -->|"Milestone Billing Hold"| n9
    n22 -->|"Intel Hold"| n2
    n22 -->|"Build/ Prepayment Hold"| n8
    n10 --> n23
    n22 -->|"Delivery Block"| n10
    n22 -->|"QSpec
 Order Hold"| n3
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
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 startEvt
    class n16 startEvt
    class n17 startEvt
    class n18 startEvt
    class n19 startEvt
    class n20 startEvt
    class n21 startEvt
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV21z2jgQ_isadzKkMzD4FQMf7gZM3GYmbXNHev1Q7oNiy-CJsH2SgNCU_96VXwAL-4a540NiPdp9VrvaXUlvWpCGRBtrNzdvcRKLMXrriBVZk84YdZ4xJ50uKoC_MIvxMyW8I2WiNBHz-EcuZtjZqxSTmI_XMd1LdE6WKUFf77toAoq0izhOeI8TFkedbidj8RqzvZfSlEnpd2QY6VFurZyapiwk7CSg664ROKBK44ScYMu1XduXepwEaRLWSCMnGkZB5yAXR9NdsMJM5MvfcPIJv36LQ7GCcYQpJyCzEmv6gJ8JlT4KtpFYsGHbKhgxl3YSCNg8w0GcLAG3dYAYTl5OkKMfDuhwc7NIjkbR02yRIPgFFHM-IxHiAuC7rUBRTOn4ne1NfEfvcsHSFzJ-Z965M8vsBtKTMbiud2VwezsSL1di_JzSsBTt7aQPYzN77bLXsal32R7-KrZIEp4seQNzaA6Plqau4RleZSmKov9lCeLKnjB_KW3dWb7pz462DGfgePolX-XmzHYnhhonwrZxQM5Ifd-37k6huhs4ht5OOvWtge4ppEssyA7vT4Qjzz4S-o7rG24rYWFPXeXm-ZGlQUVo3Tm-cyR0p4Y_MVsJ7YlhD8sVAs-S4WyFvA0X6ZowNN1wyHfO0STBdM9FISd_ifF9oUV4HOGeDDvyViR4QXMMJYq-yNpBU5oGL7yPPsIu8r5P8ZIvtL_PGMw6Qy5fY4hShu4TQWjOUVe2rlH-Y56RoBxfUtjXUHhf50-neFySOHUSVd2PX0mIPsGOyzaEZBTq-oNr9B8pTkSDsvvvyrMUfU4Ful9nLN0SdDv7fP--gWV4TRymm5iGffTISIb3awLLuYzF6BqiTzGMRZoQNIV0hZ7VQGTodaZJltE9mhEabwnbl8SS7IxcYTC-HymCdNm2lvlDZb2mbDYpczUzGAljUUyqBNY1BB-e5s3a9jVr96BRMhyIRgec2yNDRqHV_En-2UDU4X9AIIYhEil8b2OyQ3OBxYYjnIQQYEjTNRQ8-pKJOE1kvb4_p5XJmneCHwT1z8QZwTxN8mU954uFjxUsC93eP75XNkbmbGk6d6xfxvFji7zMTm-FkyVp3GeZcx5OAmgSDdOmTKT7BBa2Loqo_w0zskohq1AaldEs2PsFC8XSc4VF9rrJMYhQA72yCLpQY7ukGkm3H4iAqEjy0q_bhy-e4pNpvr2dNjgkvWc4woMVetpn-bKKuJSNMy9Y_vtCOxzOKaxmCvIaUOjZW_KhOGRUNfu_qTknNcxYuuM9TAXKMMOUEnqhBEd-8QGVgHq932TqVIBZAm4FGAVgWiVgKmPDKTWqcTlvVvKlCdOpgEphpALDErAUE7ZqUgUcZTxQxq7qQ6WgV0Du1c-Fljd0AM9b-k8gbJNTjg4QdVTRUxf7KcOpTp_VVyFhqhKyEZ2mrQuCeqeRMvaFjDwmF4lyUILohWT9UILZ82MJFKq8GJYRrAhGytis9ujC4bYTBshHquz59QLmL0LTduyBbJVMhq5u_tHV2oFVRO4iIfI7CoDntxQQtM7ueDLnq7ttDTabYasZtpthpxkeNMNuMzxshkfNMISsGTfOb9z1KbN9ymqfstunnOMrqI4PWnC3BR-24KNm3NRbcKMFN6sHQx22mmG7GXYqWOtqUJ9rHIfa-E3L39bw_g5JhDdUaIeuhjcine-TQBvnb1Btk4WgOYsxPA3WBXj4BWm24d8=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 O-060-130_Create_Backorder_(Delinquent_)_(IP) — O-060-130_Create_Backorder_(Delinquent_)_(IP)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 22 | **Gateways**: 19

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Save Sales Order"]
        n2["fa:fa-user Update Sales Order"]
        n3["fa:fa-user Save Sales Order"]
        n4["fa:fa-user Save Sales Order"]
        n5[["fa:fa-cog Check S/4 to BY Order Validation Business Rules"]]
        n6[["fa:fa-cog Capture Order in Backlog Report"]]
        n7[["fa:fa-cog Update Backlog Report"]]
        n8[["fa:fa-cog Manage Backorder"]]
        n9[["fa:fa-cog Capture Order in Backlog Report"]]
        n10[["fa:fa-cog Capture Order in Backlog Report"]]
        n11[["fa:fa-cog Calculate CDD based on CMAD"]]
        n12[["fa:fa-cog Check Supply"]]
        n13[["fa:fa-cog Check Allocation"]]
        n14[["fa:fa-cog Update Sales Order"]]
        n15[["fa:fa-cog Save Sales Order"]]
        n16[["fa:fa-cog Update Change Log Report"]]
        n17[["fa:fa-cog Save Sales Order"]]
        n18[["fa:fa-cog Generate Error Report"]]
        n19[["fa:fa-cog Capture Order in Backlog Report"]]
        n20[["fa:fa-cog Manage Backorder"]]
        n21[["fa:fa-cog Trigger PO2/SO2"]]
        n22[["fa:fa-cog Check SOLI Relevance"]]
        n23(["fa:fa-stop Order Captured in Backlog Report Successfully"])
        n24(["fa:fa-stop Backorder Managed Successfully"])
        n25(["fa:fa-stop Exit Sales Order Screen"])
        n26(["fa:fa-stop Exit Sales Order Screen"])
        n27(["fa:fa-stop Exit Sales Order Screen"])
        n28["Create Order Confirmation"]
        n29["Create Order Acknowledgment"]
        n30["Create Order Acknowledgment"]
        n31["Create Order Confirmation"]
        n32["Create Order Acknowledgment"]
        n33["Process Order"]
        n34["Create Delivery Note"]
        n35["Create Plant-to-Plant Transfer Order"]
        n36["Determine How to Allocate Inventory between Backorders"]
        n37["Create Standard Order"]
        n38{{"fa:fa-code-branch BY relevance passed?"}}
        n39{{"fa:fa-code-branch exclusiveGateway"}}
        n40{{"fa:fa-code-branch Has CMAD been provided?"}}
        n41{{"fa:fa-code-branch Has User Accepted BY Proposal?"}}
        n42{{"fa:fa-code-branch Has BY sent a new CMAD?"}}
        n43{{"fa:fa-code-branch Save/Exit Sales Order?"}}
        n44{{"fa:fa-code-branch Save/Exit Sales Order?"}}
        n45{{"fa:fa-code-branch Save/Exit Sales Order?"}}
        n46{{"fa:fa-code-branch Has an Error Code been Provided by BYOP?"}}
        n47{{"fa:fa-code-branch exclusiveGateway"}}
        n48{{"fa:fa-code-branch Should SOLI be sent to BY?"}}
        n49{{"fa:fa-arrows-alt parallelGateway"}}
        n50{{"fa:fa-arrows-alt parallelGateway"}}
        n51{{"fa:fa-arrows-alt parallelGateway"}}
        n52{{"fa:fa-arrows-alt parallelGateway"}}
        n53{{"fa:fa-arrows-alt parallelGateway"}}
        n54{{"fa:fa-arrows-alt parallelGateway"}}
        n55{{"fa:fa-arrows-alt parallelGateway"}}
        n56{{"fa:fa-arrows-alt parallelGateway"}}
        n57[["fa:fa-folder-open Contact Customer and Resolve PO Discrepancies (IP)"]]
    end
    n2 --> n39
    n37 --> n22
    n49 --> n29
    n4 --> n50
    n50 --> n30
    n50 --> n6
    n39 --> n5
    n8 --> n24
    n51 --> n28
    n51 --> n9
    n11 --> n41
    n6 --> n20
    n1 --> n51
    n52 --> n13
    n13 --> n53
    n12 --> n53
    n52 --> n12
    n43 -->|"Exit"| n25
    n43 -->|"Save"| n3
    n9 --> n42
    n41 -->|"Yes"| n1
    n44 -->|"Save"| n17
    n14 --> n15
    n15 --> n54
    n16 --> n10
    n54 --> n16
    n54 --> n31
    n7 --> n57
    n49 --> n7
    n3 --> n49
    n17 --> n55
    n55 --> n32
    n10 --> n56
    n18 --> n47
    n19 --> n8
    n45 -->|"Save"| n4
    n55 --> n19
    n47 --> n45
    n57 --> n2
    n53 --> n40
    n20 --> n23
    n56 --> n33
    n21 --> n35
    n56 --> n21
    n56 --> n34
    n22 --> n48
    n42 -->|"No"| n56
    n48 -->|"Yes"| n39
    n38 -->|"Yes"| n52
    n5 --> n38
    n48 -->|"No"| n36
    n38 -->|"No"| n43
    n44 -->|"Exit"| n26
    n41 -->|"No"| n44
    n45 -->|"Exit"| n27
    n46 -->|"No"| n47
    n40 -->|"Yes"| n11
    n40 -->|"No"| n46
    n46 -->|"Yes"| n18
    n42 -->|"Yes"| n14
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
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 serviceTask
    class n20 serviceTask
    class n21 serviceTask
    class n22 serviceTask
    class n23 endEvt
    class n24 endEvt
    class n25 endEvt
    class n26 endEvt
    class n27 endEvt
    class n28 startEvt
    class n29 startEvt
    class n30 startEvt
    class n31 startEvt
    class n32 startEvt
    class n33 startEvt
    class n34 startEvt
    class n35 startEvt
    class n36 startEvt
    class n37 startEvt
    class n38 gateway
    class n39 gateway
    class n40 gateway
    class n41 gateway
    class n42 gateway
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
    class n57 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWe1v4jYY_1einE7dJNDFjp1QPmyiULaT7tbquLtpWvfBJA5ENQlyApR1_d_3BOwAxp5W2g9V83ue3_Pul6TPflKm3O_7798_50Ve973nq3rOF_yq711NWcWvOt4e-M5kzqaCV1eNTlYW9ST_e6eGyPKpUWuwMVvkYtugEz4rufftY8cbAFF0vIoVVbfiMs-uOldLmS-Y3A5LUcpG-x3vZUG286ZEN6VMuTwoBEGMEgpUkRf8AIcxicm44VU8KYv0xGhGs16WXL00wYlyk8yZrHfhryr-mT39nqf1HJ4zJioOOvN6IT6xKRdNjrVcNViykmtdjLxq_BRQsMmSJXkxA5wEAElWPB4gGry8eC_v3z8UrVPv6-ih8OAnEayqRjzzqhrg23XtZbkQ_XdkOBjToFPVsnzk_Xf4Nh6FuJM0mfQh9aDTFLe74flsXvenpUiVanfT5NDHy6eOfOrjoCO38NvwxYv04GkY4R7utZ5uYjREQ-0py7I3eYK6yq-selS-bsMxHo9aX4hGdBic29Npjkg8QGaduFznCT8yOh6Pw9tDqW4jigK30ZtxGAVDw-iM1XzDtgeD10PSGhzTeIxip8G9PzPK1fRelok2GN7SMW0NxjdoPMBOg2SASE9FCHZmki3n3nBV1eWCS-9mVcG8V5U3KJjYVvVer_kp0J8Pfsb6Ges2ZfcmbM3hF6xQ765ZOg_-X0fK-FT52zKFGrjVw9fYJq9Rpn-22kk584Zznjx6kw_Eq0vv5o89w_vORA4B5mVxKMCXFVgEW8fGIsMYW9YryZWRHMgseRQg-MKXpawNcnxKViX5T0rvlPKZFWy2p5Qq02Pt67dEh4I3sZHJFslKNPkNRyOv2dhTD4o7_DwYmUxsbdBquRRbUzW0qQ6EKJNd70x1Yi346aScEIxZsQzWiXpktT-cswKa9MlZqvh1XowZ-IUXXDZ-bqUspcPFmyYBB6-aOmy0_qvMZzNwc3-HP0zusKltb_fdp48QjOBrViTcpIQ_tBTYpZYqDZVUep4PTE-SwBLOVmI3Qz8eGyOGsTYtlWf6n2xqsG-f8vq4ed4kkZwXJi26jBZfRusBayh5MySqVGWR5XKhF8mx7rWpO0gei3IjeDpb8KI2dungVdro_8cR4ldZbo6L5gBs9mnbaUIO1kZc5Gsut95vZc0NNXpQuxcMriF12d39AUMMt8cMwrBZj4A24jWXCzgpvF_LTXOWqG2Iex-LNQRcgscprzfQnsOIVYah-OB_UrPmMplaHfaenw9rJuXdKUSXzJvjS-o14y3hasDTnx_8l5dj6rWdyp8SAQfdmv-yv5oYNBLYab-yareHQ2qQ11KW6zw9d0qQm_2t2vU24csalhpkAG1clhUTZ0aw2wjQKqixx7yCb3YBnbFDO7vZbD-Yy-iMTN5Cpm8hR-6kWaG2_CEI9g24Vw3wpluoyd39mbn4su475m0yL1ci3W_WU75vwe4Wdeb3aOoYxLypukzUMKKSCcGF3SsNLiGhS0j4ElJ4CYlcQqKXkKJLSEdXkQxevbjslkuYK9ina5bUh7cC2JvgbK1KAVeV-ztvlFdw8CxhKHKY5B8-3v94OLLh5W__R4G9bvenZgtSz2G8BzBWALlWgNYg-2eqXnfgD2XCBCJtUlmg6rmnDBKtjxTQMwDtEalnot4Di0gRtEclp1pOVVYo1Aqh0mgBbAAtpc17R_nnwW-2gwf_n-ZeYYqa7WIn0lZUpqQ1gpTmH81bCijqCAkxTaBYh6YKjLQ7RFWsumBI5Y_aimtKZACh9qe6SmOjq_pZ1Ye0JdcEHQRVQYQ6NaS6TLVPpPpK2kSUD91WQs2ciWEctTOm3JPWvR5L_awD1iXAKhzcNlQVKdQAVlMSUkMDI5Oi48JqKEibAlYp_FbuEmiTJz2j0YcFZUpom4Py1jNtKONhZJpQAhKaU3SY0cicPM0hZhcOnHYoIoPTCgJzjJEp0ZTItNVSzmrYSsjRh5NmMesPRicwtsOhHSZ2mB5_OjqRRE5J7JT0nJJrpwSWjVOE3CLsFoVuEXGL3JVA7lIgdy2QuxjIXQ3srgZ2VwO7q4FD9WHzFCVWlFrRyIrGVrTXfrI9xa_teBg4cOTAsQMPHThx4NSBRw48duA9_ZX0FL62wrA3WGFkh7EdDu0wscPUDkd2OLbD9iyJPUtqz5Las6T2LKk9S2rPktqzpPYs4ehUX6L9jg_3xAXLU7__7O_-geP3_ZRnbCVq_6Xjs1VdTrZF4vd3_-jwV7uPZaOczSRb7MGXfwH4MATz" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 O-060-170_Change_Order_(IP) — O-060-170_Change_Order_(IP)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 8 | **Gateways**: 15

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Upload Approved Document into Sales Order"]
        n2["fa:fa-user Apply Changes"]
        n3["fa:fa-user Receive Customer Order Inquiry"]
        n4["fa:fa-user Determine Changes to Apply"]
        n5["fa:fa-user Validate internal inquiry"]
        n6[["fa:fa-cog Check Order NCNRR Conditions"]]
        n7[["fa:fa-cog Check If Order Is In Cancellation Window"]]
        n8[["fa:fa-cog Apply Changes"]]
        n9(["fa:fa-play Customer Request Received for Change"])
        n10(["fa:fa-play Order Change Request Received from Customer via EDI"])
        n11(["fa:fa-play Order Change Request Received from Customer via Web Order Management"])
        n12(["fa:fa-play Receive Internal Inquiry"])
        n13(["fa:fa-play Order Change Request Received from Customer via Dassian"])
        n14(["fa:fa-stop Customer Informed about Rejection of Change Request via Email"])
        n15(["fa:fa-stop Customer Informed about Rejection of Change Request via EDI or WOM"])
        n16["Cancel Order"]
        n17["Allocate Product to Orders"]
        n18["Approve/Release Order (IP)"]
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch Is Order Subjected to NCNR?"}}
        n21{{"fa:fa-code-branch Is Order Inside Cancellation Window?"}}
        n22{{"fa:fa-code-branch Change Approved?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n25{{"fa:fa-code-branch Manual/ Automated Changes?"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch Inquiry related to change in RDD and Quantity to Existing Sales Order?"}}
        n28{{"fa:fa-code-branch Change related to reduction in QTY"}}
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n30{{"fa:fa-code-branch Is Delivery Note Available for SO1 OR SO2?"}}
        n31{{"fa:fa-code-branch exclusiveGateway"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n33{{"fa:fa-code-branch exclusiveGateway"}}
        n34[["fa:fa-folder-open Inform Plant/Warehouse of Order Change/Cancellation"]]
        n35[["fa:fa-folder-open A Check Credit Rating and Limits (IP)"]]
    end
    n9 --> n19
    n3 --> n33
    n10 --> n19
    n11 --> n19
    n20 -->|"Yes"| n32
    n6 --> n20
    n7 --> n21
    n23 --> n29
    n1 --> n24
    n22 -->|"No"| n14
    n22 -->|"Yes"| n1
    n27 -->|"Yes"| n28
    n2 --> n26
    n28 -->|"Yes"| n16
    n28 -->|"No"| n6
    n29 --> n15
    n29 -->|"For B2B"| n18
    n24 --> n30
    n34 --> n31
    n31 --> n25
    n30 -->|"No"| n4
    n32 --> n22
    n21 -->|"Yes"| n32
    n27 -->|"No"| n24
    n4 --> n31
    n30 -->|"Yes"| n34
    n19 --> n3
    n12 --> n5
    n5 --> n33
    n33 --> n27
    n25 -->|"Automated 
Changes"| n8
    n25 -->|"Manual
 Changes"| n2
    n21 -->|"No"| n24
    n20 -->|"No"| n7
    n13 --> n19
    n8 --> n26
    n26 --> n35
    n35 --> n17
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 endEvt
    class n15 endEvt
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
    class n34 subProc
    class n35 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWNtu2zgQ_RVCReAWsBFdLcUPu3B8WRhok9ZpGxTNPtASZXNDU64uTryp_32HFilbtLQLpOuHxDqcOYczHI5IvxhhEhFjYFxcvFBO8wF66eQrsiadAeoscEY6XVQCX3FK8YKRrCNs4oTnd_Tvg5nlbp6FmcCmeE3ZTqB3ZJkQ9GXWRUNwZF2UYZ71MpLSuNPtbFK6xululLAkFdZvSBCb8UFNDl0naUTSo4Fp-lbogSujnBxhx3d9dyr8MhImPKqRxl4cxGFnLybHkqdwhdP8MP0iIx_w8z2N8hU8x5hlBGxW-Zq9xwvCRIx5WggsLNKtSgbNhA6HhN1tcEj5EnDXBCjF_PEIeeZ-j_YXFw-8EkWfxw8cwSdkOMvGJEZZDvBkm6OYMjZ4446GU8_sZnmaPJLBG3vijx27G4pIBhC62RXJ7T0Rulzlg0XCImnaexIxDOzNczd9HthmN93BX02L8OioNOrbgR1USte-NbJGSimO419Sgrymn3H2KLUmztSejisty-t7I_OcT4U5dv2hpeeJpFsakhPS6XTqTI6pmvQ9y2wnvZ46fXOkkS5xTp7w7kh4NXIrwqnnTy2_lbDU02dZLD6mSagInYk39SpC_9qaDu1WQndouYGcIfAsU7xZoVGR5cmapOi6yKDeswwNOWa7LC_txIdb3x-MGA9i3BNpR182LMERGm42abIlERonYbEmPEeU5wm6w7B10a3YUw_Gnycsdp0F3NkOjVaYL0lWt3TqlnMSErolx6keyNGM_yhouqu7unXXMclJuoa4lBCCGR6U625e3e0rZjSCpRMRkRTyAV8axPrfK7cwWYIECR_l5G5GN_M5GkGfoDlNuAjw1NNv8pzFKrIMgkMjzEPCGBb-6J7yKHnSWII6i57RU9Ort5XphkFBVrmckx8FyXKV5AjFSSo5gOLdaRWYGkc52dK2gSdN1keZLcVoMp7plNYvUt6ThfT5gDleElGGuoataahymqm1PRZSzc_5xbmNYctSzHVa90gLxpujz4xD6tdAhRdJIZj_IuFh7ZNYVz1kc40p08m9_4t8PENQB_e3H3SFPgiUldm0xy0fhoeMJaHYPdCpoiLMxZ472Grb3AqEcdlFLueEETgFyCy_nX18pxlfvbwciz0ivQW8C8MVIs8hg861JX-UrfbB2O9Pm47Z7DaTLQrdFQuRCsgMzFLs2t91Bus_GGY8oxFp2q5nVHYzlVwA1VDP3JzXhe6-zs1rdoMNVmB2iYYFVBQWCZOd5my6_dfp-i15LncnSgnDcpnCMl-Uo_l4jDCP0KcC85zmOzE6eaZZDgek0zfR2RyDf12JE62UiBIWawpynz5_04leV5ZOe1mOCQM3CPgmgS003MIuF6fhQ1--u7XQ7Rz-2XpAjvW6edivc3tdRTru8YUVw4GPpL1kQ7hsTugjg0W8vMcpWSXwGhat6bTnXp7uMO315njNzEP5ah3BMlJoe_hQGKJi3tM1zTPVaCQXnF_LL_wK9Xq_ia4jn53y2XHks2VqBpalAfbB4ueD8U28jH-KXMuRfmmpzrTcl8-W8pRidsUtn11lYEvqm-TAbJ0NKM2K0tcG7ECNSO6-eg50irMRqVrhKldeDQDDKZTstX1d0lSCrkylCt9RgJqso-JVhI5ZV1bhOmryKrO21ZbzKgGSosrlmfjZsilLS8ZZlYBUV7P0tBJx1DL6ag6epD620AdeHddAKtANy54L6KnVWbB6SLaWLqVvOVqJBvray8p0qsTLmCz_5Boi6lFdv2qw3Qw7zbDbDHvNcP_0flYb8VtHgtaRq-pWXI_LbMGtFtxuwZ0W3JU35DrqNaL9Fg6_BQ9a8Ct1Ca2vldkMW82w3Qw7zbDbDHvNcL8Z9pvhoBlujtJpjtJpjtJpjtJpjhLalryM12FPwUbXgJM3nNIjY_BiHH7aMgZGRGJcsNzYdw0MbeBux0NjcPgJyCg24s45phhu5usS3P8Duc8EEg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 O-060-180_Cancel_Order_(IP) — O-060-180_Cancel_Order_(IP)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 11 | **Gateways**: 15

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Apply Charges"]
        n2["fa:fa-user Apply Rejection Reason"]
        n3["fa:fa-user Save Order"]
        n4[["fa:fa-cog Release inventory supply and allocation from S4 to BYOP"]]
        n5[["fa:fa-cog Apply Rejection Reason"]]
        n6[["fa:fa-cog Check Order NCNRR Conditions"]]
        n7[["fa:fa-cog Check If Order Is In Cancellation Window"]]
        n8[["fa:fa-cog Review Cancellation Request"]]
        n9[["fa:fa-cog Send Cancelation details to Cancelation Report"]]
        n10["Review Cancellation Request"]
        n11["Upload Approved Document Into Sales Order"]
        n12(["fa:fa-play Customer Request Received for Cancelation"])
        n13(["fa:fa-play Order Cancellation Request Received from Customer via EDI"])
        n14(["fa:fa-play Order Cancellation Request Received from Customer via Web Order Management"])
        n15(["fa:fa-play Order Cancellation Request Received from Customer via My Samples"])
        n16(["fa:fa-stop Cancel Order Confirmation is Sent to Customer via Email/EDI/WOM"])
        n17(["fa:fa-stop Customer informed that cancellation request has been rejected via email."])
        n18(["fa:fa-stop Customer informed about Rejection of cancelation in WOM via hard error in..."])
        n19["Approve/Release Order (IP)"]
        n20{{"fa:fa-code-branch Is Delivery Note Available?"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-code-branch Is Order Subjected to NCNRR?"}}
        n23{{"fa:fa-code-branch Is Order Inside Cancellation Window?"}}
        n24{{"fa:fa-code-branch Cancellation Approval?"}}
        n25{{"fa:fa-code-branch Charges Required?"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch exclusiveGateway"}}
        n28{{"fa:fa-code-branch exclusiveGateway"}}
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n30{{"fa:fa-code-branch exclusiveGateway"}}
        n31{{"fa:fa-code-branch Is Purchase Order Request Source EDI or WOM?"}}
        n32{{"fa:fa-code-branch exclusiveGateway"}}
        n33{{"fa:fa-code-branch Is Sales Order Confirmed?"}}
        n34{{"fa:fa-code-branch exclusiveGateway"}}
        n35[["fa:fa-folder-open Inform Plant/Warehouse of Order Change/Cancellation (IP)"]]
    end
    n10 --> n29
    n24 -->|"Yes"| n25
    n1 --> n26
    n25 -->|"Yes"| n1
    n25 -->|"No"| n26
    n26 --> n11
    n21 --> n31
    n23 -->|"Yes"| n24
    n22 -->|"Yes"| n24
    n24 -->|"No"| n17
    n6 --> n22
    n7 --> n23
    n5 --> n32
    n12 --> n10
    n13 --> n28
    n14 --> n28
    n28 --> n8
    n8 --> n29
    n29 --> n33
    n11 --> n30
    n9 --> n16
    n32 --> n3
    n2 --> n32
    n31 -->|"Yes"| n5
    n23 -->|"No"| n30
    n33 -->|"Yes"| n6
    n30 --> n20
    n3 --> n4
    n4 --> n9
    n15 --> n28
    n27 --> n34
    n34 -->|"For B2B"| n19
    n34 --> n18
    n20 -->|"Yes"| n35
    n35 --> n21
    n33 -->|"No"| n21
    n22 -->|"No"| n7
    n20 -->|"No"| n21
    n31 -->|"No"| n2
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n12 startEvt
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 endEvt
    class n17 endEvt
    class n18 endEvt
    class n19 startEvt
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
    class n35 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWG1v4jgQ_itWVhW7ErRJnBDgw514KSek64vK7lWr7X0wiQO5hphzAi3X5b_fmNghcZNbiVs-tOTxzPPMjMd2zJvhs4AaA-Pi4i1KomyA3lrZiq5pa4BaC5LSVhvlwB-ER2QR07QlbEKWZPPon6OZ5WxehZnApmQdxXuBzumSUfRl1kZDcIzbKCVJ2kkpj8JWu7Xh0Zrw_ZjFjAvrD7QXmuFRTQ6NGA8oPxmYpmf5LrjGUUJPMPYcz5kKv5T6LAkqpKEb9kK_dRDBxezFXxGeHcPfpvSGvD5GQbaC55DEKQWbVbaOfycLGoscM74VmL_lO1WMKBU6CRRsviF-lCwBd0yAOEmeT5BrHg7ocHHxlBSi6PPkKUHw8WOSphMaojQD-HqXoTCK48EHZzycumY7zTh7poMP9rU3wXbbF5kMIHWzLYrbeaHRcpUNFiwOpGnnReQwsDevbf46sM0238NfTYsmwUlp3LV7dq9QGnnW2BorpTAM_5cS1JV_Jumz1LrGU3s6KbQst-uOzfd8Ks2J4w0tvU6U7yKflkin0ym-PpXquutaZjPpaIq75lgjXZKMvpD9ibA_dgrCqetNLa-RMNfTo9wu7jnzFSG-dqduQeiNrOnQbiR0hpbTkxECz5KTzQqNt2nG1pSj0TaFfk9TNExIvE-z3E58EuvbkxGSQUg6ouxouNnEezSGdlvS9Mn4s2Rp11k-0L-on0UsgW8kZUnVBVdd5mRH0Z1YkVUz51th57MlMMXARVGU7GiSMb6HjI5iJAkQiWPmk6NiyNkazR2UMTT6encPnGVSt0raGG7Zp1v1Ga-o_5wHjG7Htw8PaAybQyT8U83Tq_OchdJ5lqJZgsYk8Wkc58E_RknAXjSWnl6IXURfqn4P9O8thRmsOvarjnNYrNIt9wpoRqI4FaUqww90w7jOZZnA9d_SZWvRQF82MSOBqDFnOxqgCfO3a5g7yBoU5wQ2_Lp5t-yPRdibGJZS0bBSCv77NBKMIePlyIHnU5kIa0R52euiL1GK9ikUdxFB15OZTuz8FOJHupCeNyQhSypqoyu5P0XpZg_lXm_i4-Kt8HdP_GC_kcxKhiVhxNe5TJSKBsqOzVIpzxp66AqKdPV4d6PTezq98owSmLs1BJutSIb8cj5c5rMiKVpQKgCxPMFWyFEhd6nr9H6oQxZsm5VWOgulqswO1t7dzVEBdrkAUc6Z8L68fKfVBynZ01dqU8rr9XF2_0nbHc23t9MSDGhnAee5vxJLf0JjmC3Yxm5ZRtFwB2mJd6Bfn4zDocxg1TPQVz-G_XtHf8sPHN3NbhTOY51vF7KqMKHHbeydMv4BxSxJo4DWbWDvqJx6qoprXlMSv3N2G5zz4-jY_xGnwTu_7nmV885z653n1j_LDZvnuVmNU3q_5fA6WbSy2lTmDHAq9kAE6wGWiF5lbJ8XSXNzlQ4GtQO9n1zsnCdbOv9DeAGlvMM2sMXMjtsEuo9Jkl09Ek5XDN5NxCYh41iRZEmvKv0qV7tc7nC25l_gpESdzi9iaiVgOwL4_mR8Ffvvd9HRylRadpWlq1la-sAtyxkKj25OYRWWkhMXANbVHTViN444VTnLkwNSzbblsyefsXx2pbgat2wZnqkALD16CnA0wO7lgHru6dXsSw2laamMlYY0sFSNsAxCOdhakNjS6uDqpZNlKBSwXtNCSs19YZk_q8LKZFUulqsnLwuKlQNWMzGF5TeyR_l09Cuj4vxT_qYWGFa5YCVl6TmolrL0tpADns6tOxT1UwOlG4zocXVzq8B2PYzrYad8WauMuI0j3cYRr3Gk1zjSbxyBHlc37iqOG3CnAXcb8K68ZVdRrxbt1aL9emaYUXldrcJWPWzXw7geduphtx7u1sNePdyrh_u1MK7PEtdnieuzxPVZ4vosYbHJa7vRNuA1FN5ZA2PwZhx_7TIGRkBDso0z49A2yDZj833iG4Pjr0LGdhMA4SQicFlf5-DhX8MkDKE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Customer Business Analyst | O-060-010_Receive_Customer_Order_Inquiry_(IP), O-060-020_Receive_Request_for_Status_by_User_(IP), O-060-110_Review_Status_and_Determine_Options_(IP), O-060-130_Create_Backorder_(Delinquent_)_(IP), O-060-170_Change_Order_(IP), O-060-180_Cancel_Order_(IP) | |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for O-060. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
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
| OTCR0967 | Report | Developing a report for the 2DN model where we can view the E2E flow in one r... | 10. Object Complete |  |  | 03.Medium |
| LOGR1252 | Report | 2DN - Inbound Escort Report | 10. Object Complete |  |  | 02.High |
| LOGR1236 | Report | 2DN - Outbound Escort Report | 06. Dev In Progress |  |  | 02.High |
| LOGR1173 | Report | 2DN - Outbound Manifest Report | 10. Object Complete |  |  | 03.Medium |
| LOGR1172 | Report | 2DN - Inbound Manifest Report | 10. Object Complete |  |  | 03.Medium |
| OTCM028_IP | Conversion | Open Quantity Contract | 10. Object Complete | ECC | S4 | N/A |
| OTCC1341 | Conversion | Payer Profile Data Conversion | 10. Object Complete |  |  | 03.Medium |
| OTCC1340 | Conversion | Payer Segment Data Conversion | 10. Object Complete |  |  | 03.Medium |
| OTCC1339 | Conversion | Payer Relationship Data Conversion | 10. Object Complete |  |  | 03.Medium |
| OTCC1232 | Conversion | Intel Federal Data conversion for Contract ITD costs | 10. Object Complete |  |  | 03.Medium |
| OTCC1231 | Conversion | Intel Federal Data conversion for Bill Plans | 10. Object Complete |  |  | 03.Medium |
| OTCC1229 | Conversion | Data conversion of open Federal Contracts from ECC to Dassian S4. | 10. Object Complete |  |  | 03.Medium |
| OTCC1228 | Conversion | Data conversion for Federal Contracts - Contract Fees/Retention/Incentive Fee... | 10. Object Complete |  |  | 03.Medium |
| OTCC1227 | Conversion | Data conversion for Intel Federal Contract WBS Assignments | 10. Object Complete |  |  | 03.Medium |
| OTCC0803 | Conversion | Open Credit Case Conversion | 10. Object Complete |  |  | 02.High |
| OTCC0802 | Conversion | Custom Z table(DH) DH tables data conversion from ECC to S4 for IP | 10. Object Complete |  |  | 02.High |
| OTCC0717 | Conversion | Pricing Condition records conversion | 10. Object Complete |  |  | 01.Very High |
| OTCC0679 | Conversion | Open Dispute Case Conversion | 10. Object Complete |  |  | 02.High |
| OTCC0678 | Conversion | Collection Master Conversion | 10. Object Complete |  |  | 02.High |
| OTCC0636 | Conversion | Output Condition (Sales) Conversion for IP R3 release | 10. Object Complete |  |  | 01.Very High |
| OTCC0564 | Conversion | Customer Material Info Record Conversion for IP R3 release | 10. Object Complete |  |  | 03.Medium |
| OTCC0563 | Conversion | Open Sales Order Conversion for IP R3 release | 10. Object Complete |  |  | 02.High |
| LOGM007_IP | Conversion | Storage Bin Upload | 10. Object Complete | WIINGS | EWM | N/A |
| LOGM006_IP | Conversion | Product Master conversion (additional EWM attribution) | 10. Object Complete | WIINGS, ECC WM | EWM | N/A |
| LOGC1313 | Conversion | Conversion of stock upload program | 10. Object Complete |  |  | 03.Medium |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for O-060.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for O-060.

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

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| OTCW1683 | Workflow | Additional WRICEF for Credit Limit Request Workflow | 10. Object Complete |  | NA | 03.Medium |
| OTCR0967 | Report | Developing a report for the 2DN model where we can view the E2E flow in one r... | 10. Object Complete |  | NA | 03.Medium |
| OTCM028_IP | Conversion | Open Quantity Contract | 10. Object Complete | ECC → S4 | NA | N/A |
| OTCI1721 | Interface | Outbound Interface changes to send data from S4 to SF | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| OTCI1720 | Interface | Inbound Interface to Update Original Flag Interface from SFDC to S4. | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| OTCI1649 | Interface | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI1648 | Interface | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI1598 | Interface | An outbound Interface to Read the EEPM and DECODER Matrix from S4 to OL | 06. Dev In Progress |  | APIGEE | 02.High |
| OTCI1568 | Interface | Inbound Interface from WOM to S4 HANA to send Shipment and tracking information | 10. Object Complete |  | MULESOFT | 03.Medium |
| OTCI1498 | Interface | Inbound Interface from WOM to S4 HANA to send Customer Hierarchy | 10. Object Complete |  | MULESOFT | 03.Medium |
| OTCI1423 | Interface | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI1259 | Interface | Outbound interface from S4 HANA to WOM to send the product information | 10. Object Complete | S/4 → E-Commerce Cloud | APIGEE | 04.Low |
| OTCI1192 | Interface | Interface for BP Status query in GTS - CAAS | 10. Object Complete | GTS → MULESOFT | APIGEE | 03.Medium |
| OTCI1191 | Interface | Interface for Transactional status query in GTS - CAAS | 10. Object Complete | GTS → MULESOFT | APIGEE | 03.Medium |
| OTCI1190 | Interface | Interface for Product Create/ Change in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | APIGEE | 02.High |
| OTCI1189 | Interface | Interface for Product Classification Query in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | APIGEE | 03.Medium |
| OTCI1188 | Interface | Interface for Transactional Create/ Change in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | APIGEE | 03.Medium |
| OTCI1187 | Interface | Interface for BP Create/ Change in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | MULESOFT | 02.High |
| OTCI1180 | Interface | EMS_Inbound Interface for Capturing Hardware SO and Line-Item Details into se... | 10. Object Complete | OL → S/4 | APIGEE | 03.Medium |
| OTCI1179 | Interface | EMS_Outbound interface to OL (Orchestration layer) for activation key generat... | 10. Object Complete | S/4 → OL | APIGEE | 03.Medium |
| OTCI1178 | Interface | Interface from Sales Force (SF) to S4 to read the business rules | 10. Object Complete | SF → S/4 | MULESOFT | 03.Medium |
| OTCI0876 | Interface | Inbound interface to S4 HANA from PDH system to get dampened and Non Dampened... | 10. Object Complete | PDH → S/4 | BODS | 03.Medium |
| OTCI0716 | Interface | PIP 2A1 Interface to Distribute | 10. Object Complete |  | MULESOFT | 03.Medium |
| OTCI0711 | Interface | IP - Inbound Interface from CSAR to SAP | 10. Object Complete | CSAR → S/4 | NA | 02.High |
| OTCI0682 | Interface | Inbound Interface for Receiving PO details from B2B Customer | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| OTCI0661 | Interface | Inbound KL Order Creation from ALPS to S/4 | 10. Object Complete | ALPS (Intel Product Validation Labs Planning) → S/4 | MULESOFT | 03.Medium |
| OTCI0565 | Interface | Outbound Interface development for Invoice data from S4 to CHM | 10. Object Complete | S/4 → CHM | NA | 03.Medium |
| OTCI0540 | Interface | Inbound Interface from WOM to S4 HANA to fetch the list of order Acknowledgem... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| OTCI0488 | Interface | Interface development direction inbound for Credit or Debit Memo Requests cre... | 10. Object Complete | CHM → S/4 | NA | 03.Medium |
| OTCI0439 | Interface | Enable PIP 3A6 – transmit order status to the B2B customer (outbound interface) | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| OTCI0438 | Interface | Enable PIP 3A7 – transmit significant sales order changes to the B2B customer... | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| OTCI0435 | Interface | Inbound interface from IRC2 (Intel Registration Center) B-app to S4 against o... | 10. Object Complete | IRC2 → S/4 | MULESOFT | 03.Medium |
| OTCI0426 | Interface | Outbound interface to IRC2 (Intel registration center) B-app upon order create | 10. Object Complete | S/4 → IRC2 | MULESOFT | 03.Medium |
| OTCI0417 | Interface | Interface to Maintain Customer Part numbers in CMIR in S4 through WOM | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| OTCI0414 | Interface | Order create 4B3 - Consignment Issue | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI0413 | Interface | WOM users should be able to verify/simulate orders details before submitting ... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| OTCI0298 | Interface | Enable capture of changes on the Return Request from Salesforce into relevant... | 10. Object Complete | SalesForce → S/4 | MULESOFT | 03.Medium |
| OTCI0296 | Interface | Enable EDI : Billing Output Generation | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| OTCI0294 | Interface | Inbound interface between Sales Force and S4 needed to create Return Order fo... | 10. Object Complete | SalesForce → S/4 | MULESOFT | 02.High |
| OTCI0291 | Interface | Outbound Interface from S4 to Salesforce to update the Return Order status in... | 10. Object Complete | S/4 → SalesForce | MULESOFT | 02.High |
| OTCI0258 | Interface | Enable EDI 855 – Order Acknowledgment to B2B customer | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| OTCI0257 | Interface | Enable EDI 865 – Order change acknowledgment to B2B customer | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| OTCI0085 | Interface | Outbound Interface from S4HANA to WOM to Share order confirmation data | 10. Object Complete | S/4 → WOM | MULESOFT | 02.High |
| OTCI0082 | Interface | Interface between MyDeals and S4 needed for pricing feeds | 10. Object Complete | MyDeals → S/4 | MULESOFT | 02.High |
| OTCI0081 | Interface | Interface between IPAR and S4 needed for pricing feeds | 10. Object Complete | IPAR → S/4 | MULESOFT | 02.High |
| OTCI0061 | Interface | Enable WOM - Order Change | 10. Object Complete | Commerce Cloud → S/4 | MULESOFT | 01.Very High |
| OTCI0060 | Interface | Enable EDI - Order Change | 10. Object Complete | OpenText → S/4 | MULESOFT | 02.High |
| OTCI0058 | Interface | Enable MySamples - Sample Order Change | 10. Object Complete | MySamples → S/4 | MULESOFT | 02.High |
| OTCI0040 | Interface | Enable MySamples - Sample Order Create | 10. Object Complete | MySamples → S/4 | MULESOFT | 02.High |
| OTCI0038 | Interface | Enable EDI - Order Create | 10. Object Complete | OpenText → S/4 | MULESOFT | 02.High |
| OTCI0037 | Interface | Enable WOM - Order Create | 10. Object Complete | Commerce Cloud → S/4 | MULESOFT | 01.Very High |
| OTCF1714 | Form | Intel Federal Form for Progress Pay (Output type SF1443) | 10. Object Complete |  | NA | 03.Medium |
| OTCF1629 | Form | Returns Credit Memo Output item level consolidation | 10. Object Complete |  | NA | 03.Medium |
| OTCF0681_IP | Form | Form development for Intercompany Invoice. | 10. Object Complete |  | NA | 02.High |
| OTCF0680 | Form | Process IFL Customer Invoice | 10. Object Complete |  | NA | 03.Medium |
| OTCF0460_IP | Form | Form Development for Invoice list. | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCF0054_IP | Form | Customer Billing output (Invoice/ Credit/ Debit/ Proforma Invoice) | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCF0046_IP | Form | Send/Transmit Invoice | 10. Object Complete | NA → NA | NA | 02.High |
| OTCF0004_IP | Form | Order acknowledgment and confirmation to the customer | 10. Object Complete | NA → NA | NA | 02.High |
| OTCE1710 | Enhancement | Addition of Custom Fiori Tile/Dashboard - MRB,Pending,NPR,Freight Determinati... | 07. FUT Roadblock |  | NA | 01.Very High |
| OTCE1709 | Enhancement | Addition of Custom Fiori Tile/Dashboard - Case routing,Required field,Return ... | 06. Dev In Progress |  | NA | 01.Very High |
| OTCE1703 | Enhancement | PRMP Role needs to be sent to CHM from S4 to create Channel Partner Role in CHM | 10. Object Complete |  | NA | 02.High |
| OTCE1668_IP | Enhancement | Enhancement to transfer Customs value from S4 to GTS for Sales orders and del... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1605 | Enhancement | Custom Routine for VAS Billing with Hardware | 10. Object Complete |  | NA | 03.Medium |
| OTCE1585 | Enhancement | Addition of Custom Fiori Tile/Dashboard - EEPM,Decoder,Approval Matrix | 06. Dev In Progress |  | NA | 01.Very High |
| OTCE1505 | Enhancement | Automated Import declaration creation | 10. Object Complete |  | NA | 03.Medium |
| OTCE1421 | Enhancement | Data Enhancement for NL Import Broker | 10. Object Complete |  | NA | 03.Medium |
| OTCE1420 | Enhancement | NL Broker delivery filtration and Import worklist creatio | 10. Object Complete |  | NA | 03.Medium |
| OTCE1248 | Enhancement | IFL Enhancements Add custom fields to enable Dassian flow down | 10. Object Complete |  | NA | 04.Low |
| OTCE1199 | Enhancement | Enhancement to determine PO number based on SoldTo & MMID maintained in a BRF... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1198 | Enhancement | Enhancement to AIF capabilities on access and notifications | 10. Object Complete |  | NA | 02.High |
| OTCE1115 | Enhancement | EMS_Enhancement for S4 validation of hardware and service warranty orders lin... | 10. Object Complete |  | NA | 02.High |
| OTCE1112 | Enhancement | Enhancement to restrict ‘plant code’ changes in sale orders in change mode fo... | 10. Object Complete |  | NA | 04.Low |
| OTCE1110 | Enhancement | Enhancement to determine the correct source system for integrating B-App data... | 10. Object Complete |  | NA | 02.High |
| OTCE1109 | Enhancement | Enhancement to capture the changes in the compliance status of the transactio... | 10. Object Complete |  | NA | 02.High |
| OTCE1108 | Enhancement | 2DN_Enhancement to create KB order from staging table & to update staging tab... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1098 | Enhancement | BOT to extract input and validate mandatory fields and transform the data int... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1097 | Enhancement | BOT to manage ad hoc execution schedules, create an audit trail and capture e... | 10. Object Complete |  | NA | 04.Low |
| OTCE1096 | Enhancement | BOT to orchestrate triggers for its execution, create an audit trail and capt... | 10. Object Complete |  | NA | 02.High |
| OTCE1095 | Enhancement | BOT to manage queue functionality for human approval of the first document of... | 10. Object Complete |  | NA | 01.Very High |
| OTCE1094 | Enhancement | BOT to identify the type of request and open the corresponding Order Type in ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1093 | Enhancement | BOT to manage its execution schedule, create an audit trail and capture evide... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1092 | Enhancement | BOT for extracting input data from email validating mandatory fields and tran... | 10. Object Complete |  | NA | 02.High |
| OTCE1028 | Enhancement | Determine Confirmed Delivery date in sales orders at schedule line level base... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1027 | Enhancement | Enhancement for Sold To and ShipTo determination for SO2 & KB order sales ord... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1026 | Enhancement | Enhancement for copying Data / referencing from SO1 to SO2 for SO PO 2DN model. | 10. Object Complete |  | NA | 03.Medium |
| OTCE0975 | Enhancement | Implementation of an enhancement to restrict deletion of the material line it... | 10. Object Complete |  | NA | 04.Low |
| OTCE0966 | Enhancement | Implementation of an enhancement to add DNI(Do not improve) flag to SO1 after... | 10. Object Complete |  | NA | 04.Low |
| OTCE0965 | Enhancement | Implementation of an enhancement to replicate sales order blocks and holds fr... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0844 | Enhancement | Enhancement to create Fiori report which will expose custom table data (Non d... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0795 | Enhancement | Custom Z table(DH) creation & updates to the outbound order acknowledgements | 10. Object Complete |  | NA | 03.Medium |
| OTCE0794 | Enhancement | BOT for compilation of invoices in scheduled mode using pre-defined template | 10. Object Complete |  | NA | 03.Medium |
| OTCE0742 | Enhancement | Create CHM condition records(ZADC & ZSDC) from Order SIM output | 10. Object Complete |  | NA | 02.High |
| OTCE0741 | Enhancement | Enhancement to standard SAP report V_NLN to generate prices for Order SIM by ... | 10. Object Complete |  | NA | 02.High |
| OTCE0737 | Enhancement | Implement Standard BADI to activate Credit Limit Request Workflow | 10. Object Complete |  | NA | 04.Low |
| OTCE0721 | Enhancement | BOT Enhancement to Bulk Create Credit/Debit | 10. Object Complete |  | NA | 04.Low |
| OTCE0720 | Enhancement | BOT for compilation of invoices in ad-hoc mode to the customer request via e-... | 10. Object Complete |  | NA | 01.Very High |
| OTCE0719 | Enhancement | Utility program for open sales order conversion for IP OM team, that will be ... | 06. Dev In Progress |  | NA | 01.Very High |
| OTCE0718 | Enhancement | Pricing routines for Order SIM price calculations | 10. Object Complete |  | NA | 03.Medium |
| OTCE0715 | Enhancement | PIP 2A1 Interface: Custom Program to update Price catalogue | 10. Object Complete |  | NA | 03.Medium |
| OTCE0714 | Enhancement | Requirement is to Update CPN when there is a change in MMID of SOLI MMID trig... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0713 | Enhancement | IP End customer CI :Custom Validations to be accommodated for Price masking c... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0712 | Enhancement | Sold to party & Ship to party customer codes determination based on DUNS & DU... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0683 | Enhancement | Enhancement request for adding End customer partner in Pricing Catalogue and ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0658 | Enhancement | IP-Intel Federal To capture DPAS Rating from Dassian table on Sales Order and... | 10. Object Complete |  | NA | 04.Low |
| OTCE0654 | Enhancement | Enhancement for idoc validation and creation of custom basic type, segment fo... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0651_IP | Enhancement | Enrich the delivery data transfer data from S/4 IP to GTS with the 'new' vs '... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0650 | Enhancement | Enhancement for Legal Control Exception Scenarios | 10. Object Complete |  | NA | 03.Medium |
| OTCE0642 | Enhancement | Enrich Intrastat dispatch declaration with missing transactions and missing d... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0641 | Enhancement | Enhancement to determine transportation zone based on country key and region ... | 10. Object Complete |  | NA | 04.Low |
| OTCE0640 | Enhancement | Enhancement to support inbound interface 4B3 consignment issue | 10. Object Complete |  | NA | 03.Medium |
| OTCE0614_IP | Enhancement | Implement Standard Credit/Collection BADI | 10. Object Complete |  | NA | 03.Medium |
| OTCE0579 | Enhancement | Enhancement to extend standard table which will record fixed plant and fixed ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0578 | Enhancement | Enhancement to create custom table which will log Blue Yonder Order promiser ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0577 | Enhancement | List of fields that needs to be mapped to Order promiser Adaptor for order co... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0576 | Enhancement | Enhancement to update the B2B PO number at the return Order | 10. Object Complete |  | NA | 04.Low |
| OTCE0575 | Enhancement | Enhancement to create custom table and field and determining actions on retur... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0524 | Enhancement | Enhancement to support inbound interface from IRC2 (Intel Registration Center... | 10. Object Complete |  | NA | 04.Low |
| OTCE0523 | Enhancement | Enhancement to put user status hold on IRC2 (Intel Registration Center) relev... | 10. Object Complete |  | NA | 04.Low |
| OTCE0522 | Enhancement | Enhancement to put billing block at the line-item level for IRC2 (Intel Regis... | 10. Object Complete |  | NA | 04.Low |
| OTCE0489 | Enhancement | Enhancement to support outbound interface from S4 to IRC2 (Intel registration... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0444 | Enhancement | Credit/Debit Memo Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| OTCE0443 | Enhancement | Enhancement to include the API custom field, S4 custom fields and append to t... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0440 | Enhancement | Implement NCNR (non-cancellable / non reschedule) and NCNRR (non-cancellable ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0406 | Enhancement | Implement a warning and hold for the sales order line item having material wi... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0404 | Enhancement | Enhancement to capture business rules for entitlement and Warranty of return ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0398_IP | Enhancement | Enhance data transfer from SAP S4/HANA to SAP GTS for Customs Declaration Cre... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0191 | Enhancement | Generate Order e-Ack’s in sales order to customer in accordance with specific... | 10. Object Complete | NA → NA | NA | 04.Low |
| OTCE0088 | Enhancement | Determine sale orders to trigger availability check with BY | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0087 | Enhancement | Implement sales order cancellation control on order changes through B2B & WOM | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0086 | Enhancement | Implement Minimum order quantity (MOQ) and Delivery unit increment check vali... | 10. Object Complete | NA → NA | NA | 04.Low |
| OTCE0084 | Enhancement | Notification when Multiple Schedule lines are created | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0083 | Enhancement | Price Swamp program for order repricing | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0080 | Enhancement | IP: Pricing Date determination based on RGID and CGID | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0079 | Enhancement | Implement duplicate PO check validations for order create and change | 10. Object Complete | NA → NA | NA | 04.Low |
| OTCE0021 | Enhancement | Credit hold release dashboard at line-item level | 10. Object Complete | NA → NA | NA | 01.Very High |
| OTCE0002_IP | Enhancement | Populate Incoterms and Shipping conditions from Ship to party | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCC1341 | Conversion | Payer Profile Data Conversion | 10. Object Complete |  | NA | 03.Medium |
| OTCC1340 | Conversion | Payer Segment Data Conversion | 10. Object Complete |  | NA | 03.Medium |
| OTCC1339 | Conversion | Payer Relationship Data Conversion | 10. Object Complete |  | NA | 03.Medium |
| OTCC1232 | Conversion | Intel Federal Data conversion for Contract ITD costs | 10. Object Complete |  | NA | 03.Medium |
| OTCC1231 | Conversion | Intel Federal Data conversion for Bill Plans | 10. Object Complete |  | NA | 03.Medium |
| OTCC1229 | Conversion | Data conversion of open Federal Contracts from ECC to Dassian S4. | 10. Object Complete |  | NA | 03.Medium |
| OTCC1228 | Conversion | Data conversion for Federal Contracts - Contract Fees/Retention/Incentive Fee... | 10. Object Complete |  | NA | 03.Medium |
| OTCC1227 | Conversion | Data conversion for Intel Federal Contract WBS Assignments | 10. Object Complete |  | NA | 03.Medium |
| OTCC0803 | Conversion | Open Credit Case Conversion | 10. Object Complete |  | NA | 02.High |
| OTCC0802 | Conversion | Custom Z table(DH) DH tables data conversion from ECC to S4 for IP | 10. Object Complete |  | NA | 02.High |
| OTCC0717 | Conversion | Pricing Condition records conversion | 10. Object Complete |  | NA | 01.Very High |
| OTCC0679 | Conversion | Open Dispute Case Conversion | 10. Object Complete |  | NA | 02.High |
| OTCC0678 | Conversion | Collection Master Conversion | 10. Object Complete |  | NA | 02.High |
| OTCC0636 | Conversion | Output Condition (Sales) Conversion for IP R3 release | 10. Object Complete |  | NA | 01.Very High |
| OTCC0564 | Conversion | Customer Material Info Record Conversion for IP R3 release | 10. Object Complete |  | NA | 03.Medium |
| OTCC0563 | Conversion | Open Sales Order Conversion for IP R3 release | 10. Object Complete |  | NA | 02.High |
| LOGR1252 | Report | 2DN - Inbound Escort Report | 10. Object Complete |  | NA | 02.High |
| LOGR1236 | Report | 2DN - Outbound Escort Report | 06. Dev In Progress |  | NA | 02.High |
| LOGR1173 | Report | 2DN - Outbound Manifest Report | 10. Object Complete |  | NA | 03.Medium |
| LOGR1172 | Report | 2DN - Inbound Manifest Report | 10. Object Complete |  | NA | 03.Medium |
| LOGM007_IP | Conversion | Storage Bin Upload | 10. Object Complete | WIINGS → EWM | NA | N/A |
| LOGM006_IP | Conversion | Product Master conversion (additional EWM attribution) | 10. Object Complete | WIINGS, ECC WM → EWM | NA | N/A |
| LOGI1534_IP | Interface | BRF+ Extractor( API interface) to fetch the data saved in the BRF+ decision t... | 10. Object Complete |  | NA | 03.Medium |
| LOGI1312 | Interface | Label printing data in XML format from SAP EWM to Spectrum/Loftware | 10. Object Complete | S/4 → SPECTRUM | NA | 02.High |
| LOGI1300 | Interface | Discrepancy check for FAC receipts | 10. Object Complete |  | MULESOFT | 02.High |
| LOGI1271 | Interface | Duplicate ULT checks for Non-CPU returned products | 10. Object Complete | S/4 → ECA | NA | 02.High |
| LOGI1270 | Interface | IWRAP interface for CWP availibilty check(Inbound interface) | 10. Object Complete | IWRAP → S/4 | APIGEE | 02.High |
| LOGI1263 | Interface | Retrieve the GES scanned CPU entitlement check details | 10. Object Complete | Entitlement Orchestration Layer → S/4 | NA | 02.High |
| LOGI1262 | Interface | Entitlement Output processing to perform discrepancy checks | 10. Object Complete | Entitlement Orchestration Layer → S/4 | NA | 03.Medium |
| LOGI1261 | Interface | Discrepancy resolution results to be sent from Salesforce to SAP | 10. Object Complete | SalesForce → S/4 | APIGEE | 03.Medium |
| LOGI1067 | Interface | 2DN - S4 – Interface from S/4 to MPL for packing list. | 10. Object Complete | S/4 → MPL | SFT | 03.Medium |
| LOGI1066 | Interface | 2DN - Interface to capture Data for 1st Delivery in 2DN X-Dock Model | 10. Object Complete |  | MULESOFT | 03.Medium |
| LOGI0875 | Interface | Interface from WOM to S4 HANA to fetch the list of Deliveries for a particula... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| LOGI0874 | Interface | Interface from WOM to S4 HANA to fetch the ASN information of delivery. | 10. Object Complete | WOM → S/4 | MULESOFT | 02.High |
| LOGI0842_IP | Interface | Interface from SAP S4 to DBaaS to Fetch Actual COF for FVR batch and COA for ... | 10. Object Complete | S/4 → DBaaS | MULESOFT | 03.Medium |
| LOGI0800_IP | Interface | Interface to send shipment information to custom broker | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0664 | Interface | Trigger ZCUS (export customs clearance output) and ZXCI to send outputs - ZSI... | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| LOGI0663_IP | Interface | Trigger ZCUS (export customs clearance output) and ZXCI to send outputs - ZSI... | 10. Object Complete |  | MULESOFT | 02.High |
| LOGI0630_IP | Interface | TM - GTT: GXS sending carrier events back to GTT app “Shipment Tracking”. IP | 10. Object Complete |  | NA | 03.Medium |
| LOGI0612_IP | Interface | Customer ASN interface from outbound delivery | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0610 | Interface | 3B2 Post goods issue interface for Outbound delivery to SAP | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0609 | Interface | 3B13 interface for pick/pack updates for outbound delivery to SAP | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0607 | Interface | 3B14R Cancellation Request from S/4 to 3PL | 10. Object Complete | S/4 → 3PL | MULESOFT | 03.Medium |
| LOGI0418 | Interface | 3B12 Request to 3PL on FO creation | 10. Object Complete | 3PL → S/4 | MULESOFT | 02.High |
| LOGI0415 | Interface | 3B14C Cancellation Confirmation from 3PL to S/4 | 10. Object Complete | 3PL → S/4 | MULESOFT | 03.Medium |
| LOGF1632 | Form | TM:Trigger order details/collection details email from a freight order to the... | 10. Object Complete |  | NA | 03.Medium |
| LOGF1630 | Form | COO Label - print a Country of Origin (COO) label for the outbound shipment o... | 10. Object Complete |  | NA | 03.Medium |
| LOGF1583 | Form | Consolidated Export Commercial Invoice – Finished Goods (IP) | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF1283 | Form | Packing list form for IP returns (outbound) | 10. Object Complete |  | NA | 03.Medium |
| LOGF1282 | Form | Commercial invoice form for IP returns (outbound) | 10. Object Complete |  | NA | 03.Medium |
| LOGF1258 | Form | Commercial invoice form for returns logistics | 10. Object Complete |  | NA | 02.High |
| LOGF1257 | Form | Packing list form for Returns Logistics | 10. Object Complete |  | NA | 02.High |
| LOGF1224 | Form | Enhancement to create Scrapping form Document | 10. Object Complete |  | NA | 03.Medium |
| LOGF1220 | Form | Enhancement to generate Shipping labels | 10. Object Complete |  | NA | 03.Medium |
| LOGF1219 | Form | Enhancement to create Physical inventory form | 10. Object Complete |  | NA | 03.Medium |
| LOGF1216 | Form | Enhancement to generate picklist | 10. Object Complete |  | NA | 03.Medium |
| LOGF1149_IP | Form | Consolidated Packing list for Chengdu | 10. Object Complete |  | NA | 02.High |
| LOGF0805 | Form | EIAJ form to be generated for OEM customers (Japan) | 10. Object Complete |  | NA | 02.High |
| LOGF0353_IP | Form | Generate Consolidated Export Commercial Invoice - Finished Goods (IF and IP) | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0349_IP | Form | ISM - Generate Packing List - IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0348_IP | Form | Shipper Letter of instruction (Localization requirement for US) | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0345_IP | Form | Bailment CI and End-Customer CI for IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0344_IP | Form | Generate Export CI for IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0343_IP | Form | Generate Itemised Packing Lists | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0342_IP | Form | Generate Packing Lists for Finished Goods - IP and IF | 10. Object Complete | NA → NA | NA | 02.High |
| LOGE1713 | Enhancement | Copy Control Routine for Customer Master Special Instructions | 08. FUT In Progress |  | NA | 03.Medium |
| LOGE1609 | Enhancement | Enhancement for Fiori App development to maintain business rules for Dynamic ... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1608 | Enhancement | Enhancement for Fiori App development to maintain business rules for Static D... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1567 | Enhancement | TM - GTT: SAP S/4 Return Deliveries relevant for TM are not propagating to BN... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1535 | Enhancement | New custom Fiori application for Undo Disposition and Confirm Disposition | 06. Dev In Progress |  | NA | 02.High |
| LOGE1509_IP | Enhancement | Tendering- FIORI app for Approval Hierarchy (Assign Delegate) | 10. Object Complete |  | NA | 04.Low |
| LOGE1507 | Enhancement | Custom enhancement to enable the integration of both IF(BI1) /IP(DI0) TM syst... | 10. Object Complete |  | NA | 02.High |
| LOGE1488_IP | Enhancement | Invoice notification- Notification to carrier for POD and internal notificati... | 10. Object Complete |  | NA | 02.High |
| LOGE1487_IP | Enhancement | Carrier notification- Carrier contact table BRF+ maintenance | 10. Object Complete |  | NA | 02.High |
| LOGE1486_IP | Enhancement | Carrier notification- Cancellation email | 10. Object Complete |  | NA | 02.High |
| LOGE1485_IP | Enhancement | Carrier notification- Acceptance and Rejection email | 10. Object Complete |  | NA | 02.High |
| LOGE1484_IP | Enhancement | Invoice notification- Notification to carrier for Invoice | 10. Object Complete |  | NA | 02.High |
| LOGE1483_IP | Enhancement | Invoice notification- Notification to carrier for dispute | 10. Object Complete |  | NA | 02.High |
| LOGE1482_IP | Enhancement | Tendering- Internal Notification mail | 10. Object Complete |  | NA | 03.Medium |
| LOGE1481_IP | Enhancement | Tendering- Approval Process with Purchase group determination | 10. Object Complete |  | NA | 03.Medium |
| LOGE1462_IP | Enhancement | TM - GTT: Send Event # Estimated Time of Arrival (ETA) as a separate event fr... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1461_IP | Enhancement | TM - GTT: To propagate events to S/4 TM Freight order reported by GXS by Bypa... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1460_IP | Enhancement | TM - GTT: Additional field needs to be captured in S/4 TM Freight Order “Note... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1459_IP | Enhancement | TM - GTT: Additional field values sent by carrier through GXS are required in... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1316 | Enhancement | Mass Upload Program for HAWB/MAWB/ETA update in Freight order | 10. Object Complete |  | NA | 02.High |
| LOGE1314 | Enhancement | Enhancement to create Credit Memo Request for the Goods Receipt quantity on p... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1311 | Enhancement | Virtual Receiving | 10. Object Complete |  | NA | 03.Medium |
| LOGE1310 | Enhancement | Batch job to determine disposition based on static disposition rule table | 10. Object Complete |  | NA | 03.Medium |
| LOGE1301 | Enhancement | Enhancement for updating HAWB (House Air waybill) information in EWM Transpor... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1298 | Enhancement | Receiving unexpected returned products in the Custom Receiving Screen | 10. Object Complete |  | NA | 02.High |
| LOGE1297_IP | Enhancement | Disable the Amount field within Subcontracting tab in Freight Order for CW Lo... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1281 | Enhancement | Batch job to determine disposition based on dynamic disposition rule table | 10. Object Complete |  | NA | 03.Medium |
| LOGE1280 | Enhancement | Custom screen to request assignment of OPID to planner and capture the detail... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1277 | Enhancement | Generate Docking report | 10. Object Complete |  | NA | 02.High |
| LOGE1269 | Enhancement | To Perform Undisposition for already dispositioned RMA | 10. Object Complete |  | NA | 01.Very High |
| LOGE1268 | Enhancement | Enhancement to create Ship instruction screen.​ | 10. Object Complete |  | NA | 03.Medium |
| LOGE1266 | Enhancement | Custom Receiving screen (ZPRDI) to have functionalities to process receiving ... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1265 | Enhancement | Custom screen to capture shipment unloading details (Docking) | 10. Object Complete |  | NA | 02.High |
| LOGE1260 | Enhancement | Resolution for Discrepancy to be determined based on Business Rules | 10. Object Complete |  | NA | 01.Very High |
| LOGE1256_IP | Enhancement | TM - GTT: Document type T54 (House Airway Bill) number to GTT | 10. Object Complete |  | NA | 03.Medium |
| LOGE1251_IP | Enhancement | More determinization of input entry criteria to be added for dedicated carrie... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1250_IP | Enhancement | Creating new Carrier selection strategy methods ZPRE_TAL and ZPOST_TAL to cal... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1221 | Enhancement | Custom Fiori screen to capture shipping details and start the shipping process. | 10. Object Complete |  | NA | 02.High |
| LOGE1214 | Enhancement | Update price variance category and its reason in Difference Analyzer | 10. Object Complete |  | NA | 03.Medium |
| LOGE1197_IP | Enhancement | Carrier notification- Tendering initiation email | 10. Object Complete |  | NA | 02.High |
| LOGE1196_IP | Enhancement | Invoice notification- Notification to carrier for POD and internal notificati... | 10. Object Complete |  | NA | 02.High |
| LOGE1150 | Enhancement | TM:Custom BRF+ table for choosing the right the MTR ( Means of transport) dur... | 10. Object Complete |  | NA | 04.Low |
| LOGE1148 | Enhancement | 2DN - Trigger Auto packing in 2nd DN of 2DN X-Dock Model | 10. Object Complete |  | NA | 03.Medium |
| LOGE1147 | Enhancement | 2DN - S4 – Error Handling program in 2DN X-Dock Model | 10. Object Complete |  | NA | 02.High |
| LOGE1130 | Enhancement | Enhancement to Re-Plan the De-linked Freight Units based on Hawb Numbers | 10. Object Complete |  | NA | 02.High |
| LOGE1116 | Enhancement | 2DN - Enhancement to capture required fields of 1st Delivery in 2DN X-Dock Model | 10. Object Complete |  | NA | 03.Medium |
| LOGE1114 | Enhancement | 2DN - Post 3PL 3B2 or manual Goods Issue from CW or IW - Wrapper Program to c... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0979 | Enhancement | Pre-alert summary report for the EMEA customer | 10. Object Complete |  | NA | 03.Medium |
| LOGE0838 | Enhancement | Enhancement to update the address and bp form the Custom Partner Function to ... | 10. Object Complete |  | NA | 04.Low |
| LOGE0797_IP | Enhancement | Pre alert notification to Customer | 10. Object Complete |  | NA | 03.Medium |
| LOGE0796_IP | Enhancement | Custom transaction to trigger CUSDEC | 10. Object Complete |  | NA | 02.High |
| LOGE0793 | Enhancement | Upload program to update pick/pack information in sap in case of 3B13 PIP fai... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0792_IP | Enhancement | Enhancement to Update Custom Table form Master data and Manage SOP Data Commu... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0791_IP | Enhancement | Creation of Proforma Invoice ZF8 from Freight Order and Save ITN Number in De... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0772_IP | Enhancement | Develop Fiori app to View/Edit/Add SOP data(CMDB). | 10. Object Complete |  | NA | 02.High |
| LOGE0766_IP | Enhancement | TM - GTT: Routing of events from GTT to correct S4 system | 10. Object Complete |  | NA | 03.Medium |
| LOGE0765_IP | Enhancement | Calling a new BRF+ for Carrier exclusion during Carrier Selection process. Eg... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0690 | Enhancement | TM - GTT: Boundary App - MySample for GTT: re-purposing. Applicable for Intel... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0673_IP | Enhancement | Data code extractor to be extended on S4 TM side​ | 10. Object Complete |  | NA | 03.Medium |
| LOGE0632_IP | Enhancement | TM: Custom Determination Class to access Source and Destination country in FU... | 10. Object Complete |  | NA | 04.Low |
| LOGE0631 | Enhancement | TM - GTT: ETA calculated date to be captured in GTT Delivery App. IP | 10. Object Complete |  | NA | 04.Low |
| LOGE0628_IP | Enhancement | CRF freight orders, should have a custom event type “Shipped –CRF". This cust... | 10. Object Complete |  | NA | 04.Low |
| LOGE0627 | Enhancement | TM - GTT: Boundary App - WOM fields in GTT for WOM/MySample re-purposing. App... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0626_IP | Enhancement | FO subcontracting screen for tendering enhancement. Fields include- send for ... | 10. Object Complete |  | NA | 04.Low |
| LOGE0625_IP | Enhancement | Tendering- FIORI app for Approval Hierarchy (Assign Delegate) | 10. Object Complete |  | NA | 04.Low |
| LOGE0613 | Enhancement | Development of LCSR tool in Fiori | 10. Object Complete |  | NA | 01.Very High |
| LOGE0611 | Enhancement | 1. Custom fields in Delivery to store Number of Pallets & IPLA indicator fiel... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0608 | Enhancement | Custom logic to fetch the details from different source and save in the custo... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0581 | Enhancement | Incoterm Location 1 ID field update for Outbound delivery | 10. Object Complete |  | NA | 04.Low |
| LOGE0547_IP | Enhancement | Mass upload – Custom TM program for below items. Resource Downtime upload.Not... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0546_IP | Enhancement | Mass upload – Custom TM program for below items. Schedule and Default Routes ... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0514 | Enhancement | After 3B13 is triggered and Pick & Pack is completed in deliveries, and the H... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0513 | Enhancement | After 3B12 is triggered and YDN0 output type is triggered in the deliveries, ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0512 | Enhancement | Update Freight Order Number to the delivery documents after carrier is assign... | 10. Object Complete | ECD → S4 | NA | 03.Medium |
| LOGE0511_IP | Enhancement | Mass upload – Custom TM program for below items. Mass upload program to creat... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0510 | Enhancement | TM: To show TPT of each stage in a multileg Shipment (Default Routes) and fil... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0478_IP | Enhancement | Generate Automated Carrier Pre-Alert (ZPRC) from SAP TM. | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0459_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0458_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0457_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0456_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection UI enhanceme... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0455 | Enhancement | In SAP TM, Post schedule lines updated, enhancement to unblock the Freight unit | 10. Object Complete |  | NA | 03.Medium |
| LOGE0454 | Enhancement | In SAP TM, Enhancement to add a Planning Block in the Freight Unit with the B... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0453 | Enhancement | In SAP TM, When the Incoterm Location1 ID field is populated in the delivery ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0402 | Enhancement | In SAP TM, Goods Value to be populated in the Alternate Quantity in the Freig... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0341_IP | Enhancement | Billing document creation to be triggered from the Output of outbound delivery | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0281_IP | Enhancement | Add custom fields Customer Window, Back Dated order fields in Freight Unit St... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0065_IP | Enhancement | Create single line delivery for a confirmed sales order confirmed schedule line | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0064_IP | Enhancement | Add custom fields Customer Window, Back Dated order fields(And its date chang... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGC1313 | Conversion | Conversion of stock upload program | 10. Object Complete |  | NA | 03.Medium |

**Summary**: 5 Reports, 71 Interfaces, 20 Conversions, 167 Enhancements, 28 Forms, 1 Workflows

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for O-060:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for O-060:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (292 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 282 | 96.6% |
| 06. Dev In Progress | 8 | 2.7% |
| 07. FUT Roadblock | 1 | 0.3% |
| 08. FUT In Progress | 1 | 0.3% |
| **Total** | **292** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 5 |
| Interface (I) | 71 |
| Conversion (C) | 20 |
| Enhancement (E) | 167 |
| Form (F) | 28 |
| Workflow (W) | 1 |
| **Total** | **292** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 18 |
| 02.High | 75 |
| 03.Medium | 165 |
| 04.Low | 31 |
| N/A | 3 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| OTCI1721 | 02.Interface | Outbound Interface changes to send data from S4 to SF | 06. Dev In Progress | 03.Medium |
| OTCI1720 | 02.Interface | Inbound Interface to Update Original Flag Interface from SFDC to S4. | 06. Dev In Progress | 03.Medium |
| OTCI1598 | 02.Interface | An outbound Interface to Read the EEPM and DECODER Matrix from S4 to OL | 06. Dev In Progress | 02.High |
| OTCE1710 | 04.Enhancement | Addition of Custom Fiori Tile/Dashboard - MRB,Pending,NPR,Freight Determination ... | 07. FUT Roadblock | 01.Very High |
| OTCE1709 | 04.Enhancement | Addition of Custom Fiori Tile/Dashboard - Case routing,Required field,Return Loc... | 06. Dev In Progress | 01.Very High |
| OTCE1585 | 04.Enhancement | Addition of Custom Fiori Tile/Dashboard - EEPM,Decoder,Approval Matrix | 06. Dev In Progress | 01.Very High |
| OTCE0719 | 04.Enhancement | Utility program for open sales order conversion for IP OM team, that will be use... | 06. Dev In Progress | 01.Very High |
| LOGR1236 | 01.Report | 2DN - Outbound Escort Report | 06. Dev In Progress | 02.High |
| LOGE1713 | 04.Enhancement | Copy Control Routine for Customer Master Special Instructions | 08. FUT In Progress | 03.Medium |
| LOGE1535 | 04.Enhancement | New custom Fiori application for Undo Disposition and Confirm Disposition | 06. Dev In Progress | 02.High |

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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-060 — Manage and Track Orders (IP)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*292 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| OTCW1683 | Additional WRICEF for Credit Limit Request Workflow | Dec-25 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 1. On Track |
| OTCR0967 | Developing a report for the 2DN model where we can view the E2E flow in one report. | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 1. On Track |
| OTCM028_IP | Open Quantity Contract | Feb-25 (100%) | — | — | Feb-25 (100%) |  |
| OTCI1721 | Outbound Interface changes to send data from S4 to SF | Feb-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1720 | Inbound Interface to Update Original Flag Interface from SFDC to S4. | Feb-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1649 | Service Interface and Enhancement of the outbound proxy sent to NL brokers - Final Tax Assessment | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1648 | Service Interface and Enhancement of the outbound proxy sent to NL brokers - Declaration Notifications | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1598 | An outbound Interface to Read the EEPM and DECODER Matrix from S4 to OL | Sep-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1568 | Inbound Interface from WOM to S4 HANA to send Shipment and tracking information | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| OTCI1498 | Inbound Interface from WOM to S4 HANA to send Customer Hierarchy | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Sep-25 (100%) |  |
| OTCI1423 | Service Interface and Enhancement of the outbound proxy sent to NL brokers - Declaration Request | Jul-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1259 | Outbound interface from S4 HANA to WOM to send the product information | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCI1192 | Interface for BP Status query in GTS - CAAS | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1191 | Interface for Transactional status query in GTS - CAAS | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1190 | Interface for Product Create/ Change in GTS - CAAS | May-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Dec-25 (100%) | 2. At Risk |
| OTCI1189 | Interface for Product Classification Query in GTS - CAAS | Jun-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1188 | Interface for Transactional Create/ Change in GTS - CAAS | May-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Feb-26 (100%) | 2. At Risk |
| OTCI1187 | Interface for BP Create/ Change in GTS - CAAS | May-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1180 | EMS_Inbound Interface for Capturing Hardware SO and Line-Item Details into service sales order Text at Item Level and from OL (Orchestration layer) to S4 to remove the billing block | Jun-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCI1179 | EMS_Outbound interface to OL (Orchestration layer) for activation key generation of service warranty order and to send the validation result as part of call made from EH portal to S4 for validating the hardware and service warranty orders. | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCI1178 | Interface from Sales Force (SF) to S4 to read the business rules | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) | 1. On Track |
| OTCI0876 | Inbound interface to S4 HANA from PDH system to get dampened and Non Dampened orders and update Non-Dampened orders with new CMAD and Dampened orders in custom table | Mar-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| OTCI0716 | PIP 2A1 Interface to Distribute | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCI0711 | IP - Inbound Interface from CSAR to SAP | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Nov-25 (100%) | 1. On Track |
| OTCI0682 | Inbound Interface for Receiving PO details from B2B Customer | Jan-25 (100%) | Mar-25 (100%) | Mar-25 (100%) | Aug-25 (100%) | 1. On Track |
| OTCI0661 | Inbound KL Order Creation from ALPS to S/4 | Apr-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCI0565 | Outbound Interface development for Invoice data from S4 to CHM | Dec-24 (100%) | Jun-25 (100%) | Jun-25 (100%) | Sep-25 (100%) | 5. Not Dispositioned |
| OTCI0540 | Inbound Interface from WOM to S4 HANA to fetch the list of order Acknowledgements/confirmations for a particular customer. | Apr-25 (100%) | May-25 (100%) | May-25 (100%) | Oct-25 (100%) | 1. On Track |
| OTCI0488 | Interface development direction inbound for Credit or Debit Memo Requests creation through CHM (Channel Management) | Oct-24 (100%) | Jun-25 (100%) | Jun-25 (100%) | Sep-25 (100%) | 1. On Track |
| OTCI0439 | Enable PIP 3A6 – transmit order status to the B2B customer (outbound interface) | Dec-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Jul-25 (100%) |  |

*... and 262 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**Mapped sub-tower(s):** 5.1 OTC IP - ALL, 5.10 OTC IP - Logistics Management Outbound, 5.11 OTC IP - Order Management, 5.12 OTC IP - TM, 5.13 OTC IP - Returns (Logistics Management), 5.3 OTC IP - Billing and Rebates, 5.4 OTC IP - Returns, 5.6 OTC IP - Credit and Collections, 5.8 OTC IP - EWM, 5.9 OTC IP - GTS, 8.4 FTS IP - Logistics & Inventory Management

**RAID Summary:** 19 open items (2 capability-specific, 17 tower-level), 220 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 3 | 3 |
| P2 - Medium | 1 | 11 | 12 |
| P3 - Low | 1 | 3 | 4 |
| **Total** | **2** | **17** | **19** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03712 | Risk | P2 - Medium | LOGE0627, LOGE0690 | In Progress | OTC IP | 2026-04-03 |
| 03627 | Risk | P3 - Low | Inconsistency Response from EH -API B-App | Not Started | B-Apps |  |

**Other OTC-IP Tower RAID Items** (17 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03755 | Risk | P1 - High | Coding for 2DN and AIF enhancements. | In Progress | Technology | 2026-03-27 |
| 03767 | Risk | P1 - High | Day 1 OTC Execution - APOP production cutover for allocation... | In Progress | OTC IP | 2026-04-24 |
| 01733 | Risk | P2 - Medium | Tariffs impacts Item/BOM design which is impacting ERP/SCP (... | In Progress | E2E | 2026-03-06 |
| 03060 |  | P2 - Medium | Resource shift across Intel / Accenture Managed Services | In Progress | CM & Comms | 2026-03-27 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03635 | Risk | P2 - Medium | Gaps in mapping of ITC test cases to automated controls and ... | Not Started | OTC IP | 2026-03-27 |
| 02456 | Action | P2 - Medium | clarify who is D for the R3 org design between SMG and CPG a... | In Progress | OTC IP | 2026-03-27 |
| 02486 | Action | P2 - Medium | Tier 1/Tier 2 customer support | Not Started | OTC IP | 2026-03-31 |
| 02491 | Action | P2 - Medium | Clearly defined demand and sales ops roles (especially in BM... | In Progress | OTC IP | 2026-03-27 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03749 | Action | P2 - Medium | Logistics Data Intake and Creation Process Definition | In Progress | Test Management | 2026-03-27 |
| 03760 | Risk | P2 - Medium | Require confirmation from OT/B2B team to confirm on 3B2 ASN | Roadblock / At Risk | B-Apps |  |
| 03315 | Risk | P3 - Low | BPMG – SCP L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-03-27 |
| 03317 | Risk | P3 - Low | BPMG – E2E L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-05-29 |
| 02488 | Action | P3 - Low | contractual demand policy (including cloud customers) | In Progress | OTC IP | 2026-04-17 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*O-060 — Architecture Document (TOGAF BDAT) · Order To Cash (IP) · Generated: March 2026*

