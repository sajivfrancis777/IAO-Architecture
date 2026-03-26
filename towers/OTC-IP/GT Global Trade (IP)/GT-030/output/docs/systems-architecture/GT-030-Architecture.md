<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">GT-030 — Compliance Screening (IP)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Order To Cash (IP) (OTC-IP) Tower<br/>
  Capability GT-030 · GT Global Trade (IP)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **GT-030 Compliance Screening (IP)** within the IAO program. It includes 8 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Order To Cash (IP) (OTC-IP) |
| **Process Group** | GT Global Trade (IP) |
| **Capability** | GT-030 - Compliance Screening (IP) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 5 Reports, 71 Interfaces, 20 Conversions, 167 Enhancements, 28 Forms, 1 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Order To Cash (IP) |
| **L1 Process** | GT Global Trade (IP) |
| **L2 Capability** | GT-030 - Compliance Screening (IP) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | IP Order Management Transformation | Transform Intel Products order management onto S/4 HANA with integrated pricing and ATP | IDM 2.0 Products Revenue | High |
| 2 | Customer Experience Improvement | Reduce order processing time and improve order visibility for IP customers | Customer Centricity | High |
| 3 | Returns & Rebate Automation | Automate returns processing, rebate management, and chargeback handling | Revenue Assurance | Medium |
| 4 | GT-030 Process Migration | Migrate Compliance Screening (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Order Management (Intel Products) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Processing Time | < 2 hours | Time from order receipt to order confirmation | 6 hours (current) | Order Management Lead |
| Customer Credit Decision Time | < 15 minutes | Automated credit check and approval for standard orders | 2 hours (manual) | Credit Manager |
| Returns Processing Cycle | < 3 business days | End-to-end returns receipt to credit memo issuance | 7 business days (current) | Returns Manager |
| GT-030 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **8 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for GT-030 Compliance Screening (IP).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | GT-030-010_Business_Partners_Screening_SPL_(IP) | GT-030-010_Business_Partners_Screening_SPL_(IP) | Boundary Apps, Trade Execution Analyst | 9 | 7 |
| 2 | GT-030-030_Check_if_block_exists_(transactions)_(IP) | GT-030-030_Check_if_block_exists_(transactions)_(IP) | Boundary Apps, Trade Execution Analyst | 6 | 7 |
| 3 | GT-030-050_Business_decision_on_SPL_analysis_result_+_take_action_(IP) | GT-030-050_Business_decision_on_SPL_analysis_result_+_take_action_(IP) | Boundary Apps, Trade Execution Analyst | 6 | 9 |
| 4 | GT-030-060_Business_decision_on_Embargo_analysis_result_+_take_action_(IP) | GT-030-060_Business_decision_on_Embargo_analysis_result_+_take_action_(IP) | Boundary Apps, Trade Execution Analyst | 2 | 2 |
| 5 | GT-030-070_Business_decision_on_License_control_analysis_result_+_take_action_(IP) | GT-030-070_Business_decision_on_License_control_analysis_result_+_take_action_(IP) | Trade Execution Analyst | 2 | 2 |
| 6 | GT-030-090_Recheck_Blocked_Documents_(IP) | GT-030-090_Recheck_Blocked_Documents_(IP) | Boundary Apps, Trade Execution Analyst | 4 | 6 |
| 7 | GT-030-100_Notify_responsible_process_owner_to_proceed_with_transaction_or_cancel_the_order_(IP) | GT-030-100_Notify_responsible_process_owner_to_proceed_with_transaction_or_cancel_the_order_(IP) | Trade Execution Analyst | 3 | 5 |
| 8 | GT-030-110_Manage_Compliance_Reporting_(including_Audit_Trail)_(IP) | GT-030-110_Manage_Compliance_Reporting_(including_Audit_Trail)_(IP) | Trade Execution Analyst | 10 | 5 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 GT-030-010_Business_Partners_Screening_SPL_(IP) — GT-030-010_Business_Partners_Screening_SPL_(IP)

**Swim Lanes**: Boundary Apps · Trade Execution Analyst | **Tasks**: 9 | **Gateways**: 7

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
        n8[["fa:fa-cog Send Query to SAP GTS to get Status"]]
        n9[["fa:fa-cog Receive Status in Middleware"]]
        n10(["fa:fa-play Query Initiated to Find Status of BPs"])
        n12(["fa:fa-stop Status Received in Boundary App"])
    end
    subgraph Trade Execution Analyst
        n1["fa:fa-user Manage Blocked Partners"]
        n2["fa:fa-user Manage Positive List - BPs"]
        n3["fa:fa-user Manage Negative List - BPs"]
        n4[["fa:fa-cog Initial SPL Screening of BPs"]]
        n5[["fa:fa-cog Change BPs Address Screening"]]
        n6[["fa:fa-cog Delta Sanctioned Party List (SPL) Screening of Business Partners (BPs)"]]
        n7[["fa:fa-cog Check Status of BP"]]
        n11(["fa:fa-stop Business Partners Screening SPL Completed"])
        n13["Analyze / Determine reason for block or hold (IP)"]
        n14["Maintain Compliance Master Data (IP)"]
        n15["Maintain / Interface Customer/Vendor/Banks MD (IP)"]
        n16{{"fa:fa-code-branch Type of Screening?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
        n18{{"fa:fa-code-branch Partners Blocked?"}}
        n19{{"fa:fa-code-branch Way of Managing Block Partners?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n17
    n4 --> n17
    n5 --> n17
    n18 -->|"Yes"| n1
    n20 --> n11
    n16 -->|"Change BPs Address"| n5
    n16 -->|"Initial Screening"| n4
    n19 -->|"No Addition to List"| n13
    n19 -->|"In Negative List"| n3
    n19 -->|"In Positive List"| n2
    n14 --> n21
    n15 --> n21
    n21 --> n16
    n3 --> n20
    n2 --> n20
    n18 -->|"No"| n20
    n16 -->|"Delta Screening"| n6
    n10 --> n8
    n1 --> n19
    n9 --> n12
    n7 --> n22
    n22 --> n18
    n8 --> n17
    n17 --> n7
    n22 -->|"Send Status back to Boundary App"| n9
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
    class n12 endEvt
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11v4jgU_StWRhWtBGoSEgI87IqvjCq1I3aYndFqOg8mccCqiZHttGU6_Pe9Dk5C0rAPs0it8PE99-P4-ia8WRGPiTW2rq7eaErVGL111JbsSGeMOmssSaeLTsBXLCheMyI72ibhqVrRn7mZ4-1ftZnGQryj7KDRFdlwgv6-66IJEFkXSZzKniSCJp1uZy_oDovDjDMutPUHMkzsJI9mtqZcxERUBrYdOJEPVEZTUsH9wAu8UPMkiXga15wmfjJMos5RJ8f4S7TFQuXpZ5I84NdvNFZbWCeYSQI2W7Vj93hNmK5RiUxjUSaeCzGo1HFSEGy1xxFNN4B7NkACp08V5NvHIzpeXT2mZVB0__kxRfCJGJZyThIkFcCLZ4USytj4gzebhL7dlUrwJzL-4C6Ced_tRrqSMZRud7W4vRdCN1s1XnMWG9Pei65h7O5fu-J17NpdcYD_jVgkjatIs4E7dIdlpGngzJxZESlJkv8VCXQVX7B8MrEW_dAN52Usxx_4M_u9v6LMuRdMnKZORDzTiJw5DcOwv6ikWgx8x77sdBr2B_as4XSDFXnBh8rhaOaVDkM_CJ3gosNTvGaW2XopeFQ47C_80C8dBlMnnLgXHXoTxxuaDMHPRuD9Fk15lvcymuz38rSnP-nw-_dHK8HjBPcivkErOFr0V0bAUHG0mizRxy8r_XVDFFoprDL5aP34ceZgVHfwmUSEPhNji2iKHmgcM1BHkAbTsa9L6p6Beqe4dzA1KOgZ67AhhXyML56g6VKHvzl34lZOpOL7wtjkEesMzmuv6FBpQ6MvAscELV5JlCnKUzRJMTtIdR6tjKUbEz3gFG8ImjIePUGoJdzAlAid4hnHbeUsuYQyQah7KhXqmcrOaP1W2icCrfZfNK9-HCcxGVot79EqEoSkMFIqJc-Zfp052-JU17aUaBLHgkhZOWgwB3XmnDCF0QqnkVbR6HI4ZXwNidw0MskkDGBwX8iHriHoTSNG0MyORE-1xmg2l9Poi_dhqiy0OjO-2zMCbddsMH0QeSf8JOgWilNE7MATEgRLaJKEC7TWDYDgyxbGG7q-W97UD8XxwMcDpqmCv1MkCvIQOFUJ7tAcg2AtNP-cdguHCcYJBt4sg5p2RNx-hS7m4nYKzwuJHuZtTgZvb5VyMemt4eESQbMf9kQrV6rw56N1PJ4Tg3YieY0YaPlMPp6GXpM2bKeVspvb8i7cqJ33DQYDpJn3vz6rnF56a3px7d9K2nV-j-ZWNCwEf5E9zBTaY4EZI-wdqRw56QD1en9ojc3aa6z9xtoZauDXo_UPgXv7CwCz4drGsgCcgbF8f4Fzot-0K0dEdbvBzCvMRsbsE9duaD4YYTDr23xKpN-0vEvrYyo3a7OqzcDcyi2sjB5uWZXfAFzH1D0wQN8Y2IVBY10q-ImfQtlNIczcqslQeHeMzMNibaKPzHpk1kUBgYlerF2TjlM4GDYP2DCCGgGyyp_IZtCtMbQ-iF9_oEGao7PXB51c8dpUg912uN8Oe-dvSrUd_-LO4OJOcHFneHFndHEHTqN43a3jjnk1raNuK9q_4MO7gPsX8EHx9leHg3Z42A6PWmG43K2w0w67BWx1LXg47DCNrfGblf_agl9kMUlwxpR17Fo4U3x1SCNrnP8qsbJ9DMw5xfAitDuBx38BmORQ3A==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 GT-030-030_Check_if_block_exists_(transactions)_(IP) — GT-030-030_Check_if_block_exists_(transactions)_(IP)

**Swim Lanes**: Boundary Apps · Trade Execution Analyst | **Tasks**: 6 | **Gateways**: 7

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
        n5[["fa:fa-cog Receive Request for Create/Update of Transaction Document from B App"]]
        n6[["fa:fa-cog Receive Initial Compliance Status of Document"]]
        n7(["fa:fa-play Initiate Document Transfer"])
        n9(["fa:fa-stop Document Compliance Status Received"])
    end
    subgraph Trade Execution Analyst
        n1["Create Transactional Data"]
        n2["fa:fa-user Manage Blocked Documents"]
        n3["fa:fa-user Display Technically Incomplete Customs Documents"]
        n4["fa:fa-user Display Documents (Compliance Management)"]
        n8(["fa:fa-stop Block in Transactions Checked"])
        n10["Analyze / Determine reason for block or hold (IP)"]
        n11["Notify responsible process owner to proceed with transaction or cancel the..."]
        n12["Create Sales Orders ( IF)"]
        n13["Change Order (IF)"]
        n14["Create Outbound Delivery (IF)"]
        n15["Create Inbound delivery (IF)"]
        n16["Create Purchase Orders (IF)"]
        n17["Create Sales Order ( IP)"]
        n18["Change Order (IP)"]
        n19["Change Purchase Orders (IF)"]
        n20["Create Outbound Delivery (IP)"]
        n21["Obtain and Record Shipping Notification (IF)"]
        n22["Obtain and Record Shipping Notification (IP)"]
        n23["Create Inbound delivery (IP)"]
        n24["Change Purchase Orders (IP)"]
        n25["Create Purchase Orders (IP)"]
        n26{{"fa:fa-code-branch Type of Block ?"}}
        n27{{"fa:fa-code-branch exclusiveGateway"}}
        n28{{"fa:fa-code-branch exclusiveGateway"}}
        n29{{"fa:fa-code-branch Document Blocked ?"}}
        n30{{"fa:fa-arrows-alt parallelGateway"}}
        n31{{"fa:fa-arrows-alt parallelGateway"}}
        n32{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n30 --> n10
    n30 --> n11
    n12 --> n28
    n14 --> n28
    n13 --> n28
    n16 --> n28
    n15 --> n28
    n17 --> n28
    n18 --> n28
    n19 --> n28
    n20 --> n28
    n21 --> n28
    n22 --> n28
    n23 --> n28
    n24 --> n28
    n25 --> n28
    n7 --> n5
    n29 -->|"Yes"| n26
    n26 -->|"Technically Incomplete Block"| n3
    n6 --> n9
    n5 --> n28
    n28 --> n1
    n1 --> n29
    n29 -->|"No"| n4
    n3 --> n27
    n2 --> n27
    n27 --> n32
    n32 --> n30
    n26 -->|"Compliance Block"| n2
    n4 --> n31
    n31 --> n8
    n31 --> n32
    n32 -->|"Send compliance status to Boundary app"| n6
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
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
    class n19 startEvt
    class n20 startEvt
    class n21 startEvt
    class n22 startEvt
    class n23 startEvt
    class n24 startEvt
    class n25 startEvt
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
    class n31 gateway
    class n32 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlWNuO2zYQ_RVCwcIJYCcSJVmyH1r4pmKB3FBvWhTZPNASZRMrSyoprdfZ-N871NWmpS2a-mG9Opw5M2c4vMjPmp8EVJtqNzfPLGbZFD0Psh3d08EUDTZE0MEQlcAfhDOyiagYSJswibM1-16YGVb6JM0k5pE9i44SXdNtQtGX2yGagWM0RILEYiQoZ-FgOEg52xN-XCRRwqX1K-qGelhEq4bmCQ8obw103TF8G1wjFtMWNh3LsTzpJ6ifxMEFaWiHbugPTjK5KDn4O8KzIv1c0A_k6U8WZDt4DkkkKNjssn30nmxoJDVmPJeYn_PHuhhMyDgxFGydEp_FW8AtHSBO4ocWsvXTCZ1ubu7jJii6W97HCD5-RIRY0hCJDODVY4ZCFkXTV9Zi5tn6UGQ8eaDTV3jlLE089KWSKUjXh7K4owNl21023SRRUJmODlLDFKdPQ_40xfqQH-GvEovGQRtpMcYudptIc8dYGIs6UhiG_ysS1JXfEfFQxVqZHvaWTSzDHtsL_Zqvlrm0nJmh1onyR-bTM1LP88xVW6rV2Db0ftK5Z471hUK6JRk9kGNLOFlYDaFnO57h9BKW8dQs881nnvg1obmyPbshdOaGN8O9hNbMsNwqQ-DZcpLu0DzJi15GszQV5Zj8xPbXr_daSKYhGfnJFv1OfcoeKXz_nVMBU5xwtOAU5L37kgbwhZIQ3UF7CuJnLInRMvHzPY3Bkid7NJf099q3b2cRxt0RbmFzgGWMFsk-jRiJfYrWGclyISPUrAqV87qhSiMod8kBSTVZFKmFlIPjmzPHSesosiRt7a-jV_kFLQN0u1JMiBJQtHqifl4UYRaT6Ciys4AGxCvrdl4tkLskGQHqM1PcpCabHX0gMdlSNI8S_4EGTabi0sm8dFoyURTkjvq7mPkkimRxfCmOQgqLHFTvRR-Z1U3WWKPXZ2Uq85P4m0sWV6lxoQCx-LwAAi12VOpS5sfQwbeo4neK3qElJM33sC0jKKGAAss23BR88M8O9hD0-vazEt-QNf-YZCw8gptIIRqD4wWlsI6ogLY6xCAuS0oASntg2Q525baXgduXGiMEB9Tbt28VftzO6ZrAuYU-yQMFqoNuPTUXOT-LHYlhJgsryPfKxmr5PuXZRi5QUB5B88Ey7bC3W_vbuDQPXjAft-afcw6nhqBNxtfWTqc4qe2qzu61tiubSWvz78Gx_nIlVHYsZ_rTJiPQXARMYcnC2Y7WO5amcGKioglgFRST2hEO_yf3q-jmi_NwZW69VIora_ulWbuyHj8_t3trQEcb6GYf9qdjWmzU5RL89V47nc69nG4v-uRHuQAdv5Wnmerm_pzbpNut2YLrnU5N09RbR8J5chAjEmUoJRy2Nxp1RzONn3HCnU4s7hPWnAiQJBqNfpEbmApU9w7YNkoAuzVgqYCpAmMVsFXAUQFXBSYKgHUVMFRAzRSriWE1dawmVuVl1-NFFj_utb8onDk_ZMfWI-NqpOfIKrqicDErj6ook-pRjYyrCjR1r8Ynaiofk4LWqiessnNqO_W5kmTi2qGyMHVVytkp2aZfu1WlM-v8zCpBV3lW4gDtGtoN-S23KC8qcJI1lzoib10QbHx2jZRS6uvzBWx2w1Y3bJ_fmC9Gxr0jTvM2cgG71YvDBTjpAg29m8EwenDcg5s9uNWD2z34uAfvUQrLsRufdOO4Ry_u0Yt79OIevbhHL-7RCy1dvdJcwk437HbDk04YdshO2OiGcQ1rQ20Pt0LCAm36rBU_IcDPDAENSR5l2mmokTxL1sfY16bFq7aWFy8sS0bg0r4vwdM_ilAnfQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 GT-030-050_Business_decision_on_SPL_analysis_result_+_take_action_(IP) — GT-030-050_Business_decision_on_SPL_analysis_result_+_take_action_(IP)

**Swim Lanes**: Boundary Apps · Trade Execution Analyst | **Tasks**: 6 | **Gateways**: 9

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
        n6[["fa:fa-cog Receive Compliance status from GTS"]]
        n9(["fa:fa-stop Compliance Status Received"])
        n20{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph Trade Execution Analyst
        n1["fa:fa-user Process MD Sanctioned Party List (SPL) Block"]
        n2["fa:fa-user Add Business Partners (BP) toPositive List"]
        n3["fa:fa-user Release SPL Block for Document"]
        n4["fa:fa-user Add BP to Negative List"]
        n5["fa:fa-user Confirm SPL Block for Document"]
        n7(["fa:fa-stop SPL Block User Decision Complete"])
        n8(["fa:fa-stop Compliance Screening Completed"])
        n10["Analyze / Determine reason for block or hold (IP)"]
        n11["Analyze / Determine reason for block or hold (IP)"]
        n12{{"fa:fa-code-branch exclusiveGateway"}}
        n13{{"fa:fa-code-branch Way of Managing Blocked Partners?"}}
        n14{{"fa:fa-code-branch Type of Data?"}}
        n15{{"fa:fa-code-branch Any Other Compliance Blocks?"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-code-branch Release Documents ?"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
        n19{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n11 --> n14
    n4 --> n12
    n2 --> n12
    n13 -->|"Negative List"| n4
    n13 -->|"Positive List"| n2
    n17 -->|"No"| n5
    n16 --> n15
    n5 --> n16
    n17 -->|"Yes"| n3
    n6 --> n9
    n18 --> n7
    n1 --> n12
    n19 --> n8
    n3 --> n16
    n14 -->|"Master Data (MD)"| n13
    n13 -->|"Releasing/Confirming Block"| n1
    n14 -->|"Transactional Data"| n17
    n12 --> n18
    n15 -->|"No"| n19
    n15 -->|"Yes"| n10
    n19 -->|"Send transactional status to Boundary App"| n20
    n18 -->|"Send BP Status to Boundary App"| n20
    n20 --> n6
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 endEvt
    class n8 endEvt
    class n9 endEvt
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtV2uP2jgU_StWqhEzEqh5EsiHXfFKVWlmF5XpVqtOP5jEgWiCHdnODJTy3_c6L0gmrLoPPiB84nPO9fXNtTlqAQuJ5mk3N8eYxtJDx57ckh3peai3xoL0-qgA_sA8xuuEiJ6aEzEqV_H3fJphp3s1TWE-3sXJQaErsmEEff7YRxMgJn0kMBUDQXgc9fq9lMc7zA8zljCuZr8jo0iPcrfy0ZTxkPDzBF13jcABahJTcoYt13ZtX_EECRgNG6KRE42ioHdSwSXsNdhiLvPwM0Ee8P5LHMotjCOcCAJztnKX3OM1SdQaJc8UFmT8pUpGLJQPhYStUhzEdAO4rQPEMX0-Q45-OqHTzc0TrU3R4_yJIvgECRZiTiIkJMCLF4miOEm8d_Zs4jt6X0jOnon3zly4c8vsB2olHixd76vkDl5JvNlKb82SsJw6eFVr8Mx03-d7z9T7_ADfLS9Cw7PTbGiOzFHtNHWNmTGrnKIo-k9OkFf-iMVz6bWwfNOf116GM3Rm-lu9aplz250Y7TwR_hIH5ELU931rcU7VYugY-nXRqW8N9VlLdIMlecWHs-B4ZteCvuP6hntVsPBrR5mtl5wFlaC1cHynFnSnhj8xrwraE8MelRGCzobjdIumLMtrGU3SVBTP1IcOv3590iLsRXgQsA36RAISvxA0Y7s0iTENiCosmQkUcbZDHx5XT9q3bxf88W3NF5Kll8RVQSwlQyDeXRBN_XismJhz9ioGOJEopkGSCZj_oUjpk3Y6FSwoutaaHjkOCVrsSZDJmFE0oTg5CHlhYtTBqUJCKqVECPQwRysIUZFIiJbw4hzQfSwkul0t7-_QNGHBM4R7GW1TaBKGaAphUqWm-JRwgW6nyzsk2ZKJWKokKsmmjNWU-UQSAi0RgWthiiLG0ZwF2Y7QFtXuiGAJbug3AtXXbec0OTNGo5jvfsrObe3rmfNZSc1JEAuV83y_iSSt3R39TVkEnBAKna3mtkvD0IGcb-Z3gt6DlyR8B7lGHLIFnirqdR4L_NhCR0G3H5d3zfgN43_QMM8lqk61wRr6crBFZH-tRgua1U37Ag2CRegBU7xRy8_TWdafqp9f2zp2t87jISVKaI4lfsNxujkTekC_w7HLL3ciD-Ct7fDfrdrtplU1XpWZQG8MR52dIMUcJwlJrtiN_xmp7h5QGWgw-EWltwTscmyWY7M1NiwF_HjSWm_aD6C2p7TefZhSq7iVCstxp8KHpV0FOOV42Cb-SUTOtMoHJXFczRsVY7cat5cxLoBRObbaPnbp84CFVK84lBe6fZjf5aaG1V5qsbFQyO_LvlLXdEFoy0K3pgLnTRcnuXoxr463ynsVoOE0M2aM2w-qjBh6Y43wZAX7DTeuS8fyHIOOeXkWFnukN3JY8aG_rn6CZOpF4MOLM1ylv7q7NGCzG7a6Ybsbdrrh4eXlpvHELa9sDXDUBY67QEOvr5dN3LiCm9WNqAlb3bDdDTvd8LAbdrvhUTc87oRhJ0tY62s7ODBwHGreUcv_r8B_mpBEOEukduprOJNsdaCB5uX3ei1LQ2DOYwxXk10Bnv4ChqIb1g==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 GT-030-060_Business_decision_on_Embargo_analysis_result_+_take_action_(IP) — GT-030-060_Business_decision_on_Embargo_analysis_result_+_take_action_(IP)

**Swim Lanes**: Boundary Apps · Trade Execution Analyst | **Tasks**: 2 | **Gateways**: 2

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
        n2[["fa:fa-cog Receive Status for Embargo Block"]]
        n3(["fa:fa-stop Status Received in Boundary App"])
    end
    subgraph Trade Execution Analyst
        n1["fa:fa-user Process Embargo Block"]
        n4["Recheck Blocked Documents (IP)"]
        n5["Analyze / Determine reason for block or hold (IP)"]
        n6["Analyze / Determine reason for block or hold (IP)"]
        n7{{"fa:fa-code-branch Any Other Compliance Blocks Exist ?"}}
        n8{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n1
    n1 --> n7
    n7 -->|"Yes"| n5
    n7 -->|"No"| n8
    n8 --> n4
    n2 --> n3
    n8 -->|"Send status to Boundary app"| n2
    class n1 userTask
    class n2 serviceTask
    class n3 endEvt
    class n4 startEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVV2v4jYQ_StWrq7YlYKahITQPLTiK9VK23ZVbltVyz4YZwLWdeLIdi6wLP-9YxIIsPc-bR4QPp5zzngynhwcJjNwEufx8cBLbhJy6JkNFNBLSG9FNfRc0gD_UMXpSoDu2ZhclmbBv57C_LDa2TCLpbTgYm_RBawlkL8_uGSMROESTUvd16B43nN7leIFVfupFFLZ6AcY5V5-cmu3JlJloLoAz4t9FiFV8BI6eBCHcZhangYmy-xGNI_yUc56R5uckFu2ocqc0q81_E53__LMbHCdU6EBYzamEB_pCoQ9o1G1xVitXs7F4Nr6lFiwRUUZL9eIhx5CipbPHRR5xyM5Pj4uy4speZotS4IPE1TrGeREG4TnL4bkXIjkIZyO08hztVHyGZKHYB7PBoHL7EkSPLrn2uL2t8DXG5OspMja0P7WniEJqp2rdknguWqPv3deUGad03QYjILRxWkS-1N_enbK8_yHnLCu6onq59ZrPkiDdHbx8qNhNPW-1zsfcxbGY_--TqBeOIMr0TRNB_OuVPNh5Htvi07SwdCb3omuqYEt3XeCP0_Di2AaxakfvynY-N1nWa8-KcnOgoN5lEYXwXjip-PgTcFw7IejNkPUWStabchE1qdeJuOq0s2efcrg8-elk9Mkp30m1-QvYMBfgCwMNbUmuVRkXqyoWksyEZI9L50vX67Yg3cXtjayOtNalYzw8sYY2e8bNnbQXYJPimZA5jtgteGyJOOSir02V2b-xct2BbH1Aa2_y--KESIDc9kAe262MaWZZHUBpdHk3YdP72_jI4w_-X4F8hOZgQFV4HAgCqjGlGw1VlaG4J8NdvIrEsMfl4gPh-6VZNBf4TRgGyzInvyJk1ORqSwqwRGE5lRYgx3Xhvy6dI7HK6FRJ0SVklvdp8KQiioqBIjfmp7tOJd3Ug5Jv_8LFrxd-s0ybpexXX5bOv-BXjrfsGp3-B_yBI9aeNSww3YZNMvB9S6SFuhuZ5htHyO7rqG2a1AtuLogNqPzYLiBg-vbfbMzaGfWDRhehuYNHL0OD1-H4_Plv0FHZ9RxnQJbgPLMSQ7O6cOHH8cMcloL4xxdh9ZGLvYlc5LTB8KpqwyZM07xWhQNePwfsahXuA==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

#### BUSINESS ARCHITECTURE — 3.2.5 GT-030-070_Business_decision_on_License_control_analysis_result_+_take_action_(IP) — GT-030-070_Business_decision_on_License_control_analysis_result_+_take_action_(IP)

**Swim Lanes**: Trade Execution Analyst | **Tasks**: 2 | **Gateways**: 2

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
    subgraph Trade Execution Analyst
        n1["fa:fa-user Process License Control Block"]
        n2["fa:fa-user Change Control Data for Licenses"]
        n3["Recheck Blocked Documents (IP)"]
        n4["Analyze / Determine reason for block or hold (IP)"]
        n5{{"fa:fa-code-branch Method of License Control?"}}
        n6{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n4 --> n5
    n1 --> n6
    n6 --> n3
    n5 -->|"Process Error"| n1
    n5 -->|"Change Legal Control"| n2
    n2 --> n6
    class n1 userTask
    class n2 userTask
    class n3 startEvt
    class n4 startEvt
    class n5 gateway
    class n6 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVU2P4jgQ_StWWi1mpaDNJ2Fz2BEkZDVSjzTa7t05LHMwTplYGBvZTjcMw39fmxBomO7T5IBSj1fvVZU_sveIrMHLvfv7PRPM5Gg_MA2sYZCjwQJrGPioA_7FiuEFBz1wHCqFeWTfj7Qw2WwdzWEVXjO-c-gjLCWgfz75aGITuY80FnqoQTE68AcbxdZY7QrJpXLsOxjTgB7dTn9NpapBXQhBkIUktamcCbjAcZZkSeXyNBAp6itRmtIxJYODK47LF9JgZY7ltxo-4-1XVpvGxhRzDZbTmDV_wAvgrkejWoeRVj33w2Da-Qg7sMcNJkwsLZ4EFlJYrC5QGhwO6HB_PxdnU_RUzgWyD-FY6xIo0sbCs2eDKOM8v0uKSZUGvjZKriC_i2ZZGUc-cZ3ktvXAd8MdvgBbNiZfSF6fqMMX10Mebba-2uZR4Kud_b3xAlFfnIpRNI7GZ6dpFhZh0TtRSn_Jyc5VPWG9OnnN4iqqyrNXmI7SIvhZr2-zTLJJeDsnUM-MwCvRqqri2WVUs1EaBu-LTqt4FBQ3okts4AXvLoJ_FMlZsEqzKszeFez8bqtsF1-UJL1gPEur9CyYTcNqEr0rmEzCZHyq0OosFd406EnhGtBsC6Q1TAo0EZjvtOlY7hHhf3OP4pzioRs6cvagNXqwwxIaUGFXUUmOplyS1dz79iozus4sGiyWl4QSG4yoVL2Svk6ObfLfQBogq04balRK0q5BGI0-fPry2zU_sfxj8d8B_Y5KMKDW9gAjBVjbvpzRwskg-9LY3faGRLrf9wW7y2q4sMeNNOgzmEbWSNLbnj_OvcPhVf7o7XzYEt5q9gx_dbvhkmXPS_ciEjQc_mkrOIVhF45O4agL41OYuvDH3OuXYqaUVHPvh827YZxG_gBLzPuqj8ToRIyujI7bzLn3x-sKjt6G4_MVcwUnb8Npfyau0FGPer63tguHWe3le-_4PbDfjBoobrnxDr6HWyMfd4J4-fHe9NpNbTNLhu12Xnfg4X9FiQ6X" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 GT-030-090_Recheck_Blocked_Documents_(IP) — GT-030-090_Recheck_Blocked_Documents_(IP)

**Swim Lanes**: Boundary Apps · Trade Execution Analyst | **Tasks**: 4 | **Gateways**: 6

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
        n3[["fa:fa-cog Receive Compliance Status"]]
        n6(["fa:fa-stop Status Received in Boundary App"])
    end
    subgraph Trade Execution Analyst
        n1["fa:fa-user Recheck Blocked Document"]
        n2["fa:fa-user Recheck Documents Manually"]
        n4["Recheck Documents in Background (batch jobs)"]
        n5(["fa:fa-stop Documents Released"])
        n7["Check if block exists (transactions) (IP)"]
        n8["Notify responsible process owner to proceed with transaction or cancel the..."]
        n9["Check if block exists (transactions) (IP)"]
        n10["Analyze / Determine reason for block or hold (IP)"]
        n11["Business decision on SPL analysis result + take action (IP)"]
        n12["Business decision on Embargo analysis result + take action (IP)"]
        n13["Business decision on License control analysis result + take action (IP)"]
        n14{{"fa:fa-code-branch Mode of Checking Documents?"}}
        n15{{"fa:fa-code-branch Document Blocked?"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
        n19{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n13 --> n19
    n9 --> n19
    n12 --> n19
    n10 --> n19
    n2 --> n1
    n11 --> n19
    n14 -->|"Manual"| n2
    n1 --> n16
    n16 --> n15
    n4 --> n16
    n17 --> n7
    n17 --> n8
    n19 --> n14
    n14 -->|"Batch Job"| n4
    n15 -->|"No"| n18
    n18 --> n5
    n3 --> n6
    n15 -->|"Yes"| n17
    n18 -->|"Send Compliance status to Boundary App"| n3
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n5 endEvt
    class n6 endEvt
    class n7 startEvt
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl1v4jgU_StWqopWC90kJITysCu-MppVO6rK7K5WwzwYxwEvIY5sp8Aw_Pe9zgeQNDzMLA9Vc3zPOffeONc-GIQH1BgYt7cHFjM1QIeWWtENbQ1Qa4ElbbVRDvyFBcOLiMqWjgl5rGbsWxZmOclOh2nMxxsW7TU6o0tO0Z8f22gIxKiNJI5lR1LBwla7lQi2wWI_5hEXOvqG9kMzzNyKpREXARXnANP0LOICNWIxPcNdz_EcX_MkJTwOKqKhG_ZD0jrq5CK-JSssVJZ-Kukz3v3NArWC5xBHkkLMSm2iJ7ygka5RiVRjJBVvZTOY1D4xNGyWYMLiJeCOCZDA8foMuebxiI63t_P4ZIqeXucxgh-JsJQTGiKpAJ6-KRSyKBrcOOOh75ptqQRf08GNPfUmXbtNdCUDKN1s6-Z2tpQtV2qw4FFQhHa2uoaBnezaYjewzbbYw9-aF42Ds9O4Z_ft_slp5Flja1w6hWH4v5ygr-IzluvCa9r1bX9y8rLcnjs23-uVZU4cb2jV-0TFGyP0QtT3_e703Kppz7XM66Ijv9szxzXRJVZ0i_dnwcexcxL0Xc-3vKuCuV89y3TxIjgpBbtT13dPgt7I8of2VUFnaDn9IkPQWQqcrNCIp9leRsMkkfma_sXdL1_mRogHIe4QvkSvlFD2RtGYb5KI4ZhQNFNYpXJufP16QevdnWhS8aQIKukBYnHFEdj3ORu2Ti2zzwIHFE13lKSK8RgNYxztpbows05eejtokxUlazSKOFmD14STdENjBSYXJLuZVAZL9IzjFEfRvkpzgPY-VpeDyXopdE3oboEVWaF_-ULeV9lurS1nhVcaUZh-wbkTGcGD-HFmxkK00AUhumMSCHcKhoDERPdE3qO7jy81rz5QP3HFwj0SVCYQxWCaogS2DZUS8W0MZSueA9CmLVMrdCGKuEBEv-EIwTx-eHioyj_-fGaWCdzsNX6j6Fc0oYqKDQxZyBNLMA7BOVeEf1YwEZo09EsfpRJoUExACZNZzjGavTwhnO0RJnXlaaTQL0jhNUVFYQ1q9jW16WaBxZL_uGL3muITTJdYUgSHB3yg0Y8rO4fD-ZMMaGcB7Ybt9gz_Ix6i7KXAwXDeXL_PjePxUsFtVigJ5Zfzjtdr5tEdiaDSN_ohH3N1mnemYSH4VnYw1JlgAZ8Xja6Q-j9DemwksfhafqdpA-8LdTq_aYkCeKw9W3YdMGtAGVCuW3WCo4HvcyOfLHPjO3DKtSK2Vz73CsAtAKce4OWAV3vul89l_k7dfZQNpz_4IkvgtOwWy594hlsnoX4uVCZS9KlX5_1DZU70KkRYmUGXLw8MmZ8FMHqqRwCQuxfHnG5KebxXYLsZ7l4e3ZUVt7iQVMBeE-idrkkVuN8MPzbDsDGacesKbl_Bu1dwp7xPVGG3Ge41w14z3G-GH0vYaBsbmNaYBcbgYGQXdbjMBzTEMLuMY9vAqeKzfUyMQXahNdIkAOaEYTjNNzl4_A_vd80_" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 GT-030-100_Notify_responsible_process_owner_to_proceed_with_transaction_or_cancel_the_order_(IP) — GT-030-100_Notify_responsible_process_owner_to_proceed_with_transaction_or_cancel_the_order_(IP)

**Swim Lanes**: Trade Execution Analyst | **Tasks**: 3 | **Gateways**: 5

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
    subgraph Trade Execution Analyst
        n1[["fa:fa-cog Notify Responsible Process Owner to Cancel Document/Approval"]]
        n2[["fa:fa-cog Notify Process Owner to Proceed with Transaction"]]
        n3["Request Partner to Block in MDG"]
        n4(["fa:fa-stop Partner not Blocked"])
        n5(["fa:fa-stop Partner Blocked in MDG"])
        n6(["fa:fa-stop Blocked Transactional Document Managed"])
        n7["Check if block exists (transactions) (IP)"]
        n8["Recheck Blocked Documents (IP)"]
        n9{{"fa:fa-code-branch Partner Needs to be Blocked?"}}
        n10{{"fa:fa-code-branch Course of Action?"}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
        n12{{"fa:fa-code-branch exclusiveGateway"}}
        n13{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n7 --> n12
    n8 --> n12
    n12 --> n10
    n2 --> n11
    n1 --> n11
    n11 --> n13
    n13 --> n9
    n9 -->|"Yes"| n3
    n3 --> n5
    n13 --> n6
    n10 -->|"Approve Document"| n2
    n10 -->|"Cancel Document"| n1
    n9 -->|"No"| n4
    class n1 serviceTask
    class n2 serviceTask
    class n4 endEvt
    class n5 endEvt
    class n6 endEvt
    class n7 startEvt
    class n8 startEvt
    class n9 gateway
    class n10 gateway
    class n11 gateway
    class n12 gateway
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVl1v4jgU_StWqopWCtp8EpqHXdFARiNtu9W0M6vVMA8muQGrxs7aToFl-O_rhIRAgJfdPCDuyT3n3HsT29kaCU_BCI3b2y1hRIVo21MLWEIvRL0ZltAz0R74hgXBMwqyV-ZknKlX8k-VZnv5ukwrsRgvCd2U6CvMOaCvn0000kRqIomZ7EsQJOuZvVyQJRabiFMuyuwbGGZWVrnVtx65SEG0CZYV2ImvqZQwaGE38AIvLnkSEs7SE9HMz4ZZ0tuVxVG-ShZYqKr8QsITXv9JUrXQcYapBJ2zUEv6O54BLXtUoiixpBAfzTCILH2YHthrjhPC5hr3LA0JzN5byLd2O7S7vZ2ygyl6G08Z0ldCsZRjyJBUGp58KJQRSsMbLxrFvmVKJfg7hDfOJBi7jpmUnYS6dcssh9tfAZkvVDjjNK1T-6uyh9DJ16ZYh45lio3-7XgBS1unaOAMneHB6TGwIztqnLIs-19Oeq7iDcv32mvixk48PnjZ_sCPrHO9ps2xF4zs7pxAfJAEjkTjOHYn7agmA9-2ros-xu7Aijqic6xghTet4EPkHQRjP4jt4Krg3q9bZTF7ETxpBN2JH_sHweDRjkfOVUFvZHvDukKtMxc4X6A3gVNAkzUkhSKcoRHDdCPVPqu8mP39-9TIcJjhfsLn6Jkrkm3QF5A5Z5LohYrKikBK9MeKgUCKowizBCga86RYAlO_jPJc8A9Mp8aPH0fKzkXlM7UKgBStiKrqZRInZa0dNVeLfYG_C5AKveh3vmY_Up68I8LQ0_iTZhwRvLuDvVQ8P5AYV3sWpJpwf8TwrzDq7NblmDTokJrko05wOyv0hBmenzkHWiNaQNlJhmZVS7AmUkl0p1odeY_uPr_cn7Y5rOaSVOTGu3GTF_Ifttv2qaTQn2n9ZHHo9Vk_ClkOdgaN3G9TY7c7fmOsyxIRL4QExDM0qso949mXebBOaCHJB3zaL6cuzflvNLelYSH4SvYxVSjHAlMK9IykN7f9Hxagfv_X0reOh53YdmqgXr2sie0moRs3gNsA7h54qOOHMvw5Nf4COTV-6ne9xus0v0MbNLFV8_YLEA7PvRJxulmdZVsl2Z0KnnkFe0f7UtnP0e55cse5eserT4sT0L8EDi6BweFgO4GHl-GHZic-Ldu6DNuXYecy7DawYRpLEEtMUiPcGtW3jP7eSSHDBVXGzjRwofjrhiVGWJ35RpGnmjkmWG_Fyz24-xefNeZ_" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 GT-030-110_Manage_Compliance_Reporting_(including_Audit_Trail)_(IP) — GT-030-110_Manage_Compliance_Reporting_(including_Audit_Trail)_(IP)

**Swim Lanes**: Trade Execution Analyst | **Tasks**: 10 | **Gateways**: 5

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
    subgraph Trade Execution Analyst
        n1["fa:fa-user Analyze Reason for SPL Release"]
        n2["fa:fa-user Display Audit Trail Documents"]
        n3["fa:fa-user Display Audit Trail External Addresses"]
        n4["fa:fa-user Display Audit Trail Partners"]
        n5["fa:fa-user Display Audit Trail General Addresses"]
        n6["fa:fa-user Display Positive List Business Partners (BPs)"]
        n7["fa:fa-user Display Negative List BPs"]
        n8["fa:fa-user Display Released Embargo Documents"]
        n9["fa:fa-user Display Archived Documents"]
        n10[["fa:fa-cog Analyze Embargo Release Reasons"]]
        n11(["fa:fa-play Initiate Compliance Reporting Management"])
        n12(["fa:fa-stop Compliance Reporting Managed"])
        n13{{"fa:fa-code-branch Purpose of Report?"}}
        n14{{"fa:fa-code-branch Type of Detail?"}}
        n15{{"fa:fa-code-branch Type of Report?"}}
        n16{{"fa:fa-code-branch Type of Reporting?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n11 --> n13
    n13 -->|"Audit Trail"| n14
    n13 -->|"Document Level Reporting"| n15
    n16 -->|"Positive"| n6
    n15 -->|"Archived Documents"| n9
    n15 -->|"Embargo Release Reasons"| n10
    n15 -->|"Embargo Release Document"| n8
    n15 -->|"SPL Release Reason"| n1
    n16 -->|"Negative"| n7
    n17 --> n12
    n14 -->|"Partners"| n4
    n14 -->|"Documents"| n2
    n14 -->|"General Addresses"| n5
    n14 -->|"External Addresses"| n3
    n4 --> n17
    n2 --> n17
    n5 --> n17
    n3 --> n17
    n1 --> n17
    n8 --> n17
    n10 --> n17
    n9 --> n17
    n6 --> n17
    n7 --> n17
    n13 -->|"Sanctioned Party List (SPL)"| n16
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 userTask
    class n10 serviceTask
    class n11 startEvt
    class n12 endEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlV11v4jgU_StWqopWClK-Q_OwK74yGqkzQkt352GYB5M4YDXEke1QGIb_vteQ8OGG6UrLA8LH55x7fXPtmJ2RsJQYkXF_v6MFlRHadeSSrEgnQp05FqRjoiPwD-YUz3MiOoqTsUJO6c8DzfbKjaIpLMYrmm8VOiULRtDfn03UB2FuIoEL0RWE06xjdkpOV5hvhyxnXLHvSC-zskO0emrAeEr4mWBZoZ34IM1pQc6wG3qhFyudIAkr0ivTzM96WdLZq-Ry9pYsMZeH9CtBvuDNN5rKJYwznAsCnKVc5c94TnK1RskrhSUVXzfFoELFKaBg0xIntFgA7lkAcVy8niHf2u_R_v5-VpyCopfRrEDwSXIsxIhkSEiAx2uJMprn0Z037Me-ZQrJ2SuJ7pxxOHIdM1EriWDplqmK230jdLGU0ZzlaU3tvqk1RE65MfkmciyTb-Fbi0WK9BxpGDg9p3eKNAjtoT1sImVZ9r8iQV35CxavdayxGzvx6BTL9gN_aL33a5Y58sK-rdeJ8DVNyIVpHMfu-FyqceDb1m3TQewG1lAzXWBJ3vD2bPg09E6GsR_GdnjT8BhPz7KaTzhLGkN37Mf-yTAc2HHfuWno9W2vV2cIPguOyyV64TglaLwhSSUpK1C_wPlWyCNLfQr7-8zIcJThrir6kfCToL8IFsDPGEfTyTMMcwDIzPhxIXWupSMqyhyq0a9SKlVkmqMRS6oVKaS4VrofK8cbSTgkg_ppyokQRLPwPraYwNYoCNeE_sfCTwRkt0MH7Q4TJqika4KeqZBoUAk4YIQ4ZYEeBhPxeO0Utjt9JdBZZ6eJFr_XrqqfUYrGqznmC3ar-E83CsCTJcRMb8ls6_tJmLDFqVOaaHX4unOU-EptP5zUh3Cf4S1BYf-gIVuVOcVFoqQl4xJOP_QFF3hBVBbg83jp45x9hGTl7-SprnV3u_MKUtKdw4GbLNGk4iWDzFlWW_w5M_b7S6HXLnzZlgfViEhom3cq__eqG7GC_6KCRb4Thu1Cskly6MU1-XQ8rc4yOM-PP-DpoG73D1WhBnAV8GtmXGyLmfFLlUJnNO2Cnsma5Of8jnS_oQc1vdklh-mgmfWbcC1NCLwnnXez6VRM6yN2Y36g93T2xXlX-x5t9ZU0u_QwGzazYV1JpwG8ZuGn0wjonj57vd534pYTCWi-Tms7NIHXPFWvzq1J1tHGvjZ2tbGtjXv6vKUBT9o40MahbtA01RRaV72woBNU3bbHk_ABHs3j8WEEF29OlVhzY7iCnXbYbYe9dthvh4N2OGyHe-3wUzsMdby4r1xP2acr3zXu1Neza9Rt7ijXsNcO--1w0A6HDWyYxorwFaapEe2Mwy0f_gmkJMNVLo29aeBKsum2SIzocBs2qjIF5YhiuKSsjuD-X2pU3iI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | GT-030-010_Business_Partners_Screening_SPL_(IP), GT-030-030_Check_if_block_exists_(transactions)_(IP), GT-030-050_Business_decision_on_SPL_analysis_result_+_take_action_(IP), GT-030-060_Business_decision_on_Embargo_analysis_result_+_take_action_(IP), GT-030-090_Recheck_Blocked_Documents_(IP),  | |
| Trade Execution Analyst | GT-030-010_Business_Partners_Screening_SPL_(IP), GT-030-030_Check_if_block_exists_(transactions)_(IP), GT-030-050_Business_decision_on_SPL_analysis_result_+_take_action_(IP), GT-030-060_Business_decision_on_Embargo_analysis_result_+_take_action_(IP), GT-030-070_Business_decision_on_License_control_analysis_result_+_take_action_(IP), GT-030-090_Recheck_Blocked_Documents_(IP), GT-030-100_Notify_responsible_process_owner_to_proceed_with_transaction_or_cancel_the_order_(IP), GT-030-110_Manage_Compliance_Reporting_(including_Audit_Trail)_(IP) | |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for GT-030. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
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

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for GT-030.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for GT-030.

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

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for GT-030:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for GT-030:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (292 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-030 — Compliance Screening (IP)</span></div>
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

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

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
*GT-030 — Architecture Document (TOGAF BDAT) · Order To Cash (IP) · Generated: March 2026*

