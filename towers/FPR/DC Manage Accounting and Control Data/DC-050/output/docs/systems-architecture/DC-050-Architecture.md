<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">DC-050 — DC-050</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Finance Plan To Report (FPR) Tower<br/>
  Capability DC-050 · </p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **DC-050 DC-050** within the IAO program. It includes 25 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Finance Plan To Report (FPR) |
| **Process Group** |  |
| **Capability** | DC-050 - DC-050 |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 17 Reports, 86 Interfaces, 25 Conversions, 219 Enhancements, 1 Forms, 18 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: "loose"` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Finance Plan To Report |
| **L1 Process** |  |
| **L2 Capability** | DC-050 - DC-050 |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | S/4 HANA Finance Consolidation | Migrate legacy costing and reporting platforms to unified S/4 HANA finance backbone | IDM 2.0 Core Finance Transformation | High |
| 2 | Real-Time Financial Visibility | Enable real-time cost reporting and variance analysis replacing batch-driven legacy processes | CFO Digital Finance Initiative | High |
| 3 | Regulatory Compliance Readiness | Ensure SOX compliance and audit trail continuity through the ERP transition period | Intel Corporate Compliance | Medium |
| 4 | DC-050 Process Migration | Migrate DC-050 business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Finance | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Month-End Close Cycle Time | < 3 business days | Calendar days from period close trigger to final posting | 5 business days (legacy) | Finance Controller |
| Cost Variance Accuracy | < 0.5% deviation | Variance between standard and actual cost post-migration | 1.2% (ICOST baseline) | Cost Accounting Lead |
| System Availability (Finance) | 99.9% uptime | S/4 HANA finance module availability during business hours | 99.5% (legacy) | IT Operations |
| DC-050 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **25 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for DC-050 DC-050.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | DC-050-110_Perform_Implementation_Audit | DC-050-110_Perform_Implementation_Audit | Capital Analyst | 5 | 0 |
| 2 | DC-050-120_Close_Project | DC-050-120_Close_Project | Batch User, CCF Analyst, CES / Intel Products Capital Finance, Capital Analyst, Capital Enterprise Solutions (CES) Analyst, Capital Finance Analyst, Finance Analyst | 18 | 10 |
| 3 | DC-050-300_Manage_IM_Program_Positions_(PPM_Portfolio_and_Buckets) | DC-050-300_Manage_IM_Program_Positions_(PPM_Portfolio_and_Buckets) | Capital Central Finance Analyst | 6 | 9 |
| 4 | DC-050-310_Manage_IM_Program_Position_Budget_(PPM_Portfolio_and_Buckets) | DC-050-310_Manage_IM_Program_Position_Budget_(PPM_Portfolio_and_Buckets) | Capital Central Finance Analyst | 10 | 6 |
| 5 | DC-050-340_Workflow_project_for_approval | DC-050-340_Workflow_project_for_approval | Capital Analyst | 3 | 2 |
| 6 | DC-050-350_Distribute_Project_budget_to_account_assignment_WBS | DC-050-350_Distribute_Project_budget_to_account_assignment_WBS | Capital Analyst | 5 | 3 |
| 7 | DC-050-410_Simulate_Depreciation | DC-050-410_Simulate_Depreciation | CES / Intel Products Capital Finance, Capital Analyst | 3 | 0 |
| 8 | DC-050-520_Form_Core_Project_Team | DC-050-520_Form_Core_Project_Team | CES / Intel Products Capital Finance, Capital Analyst, Capital Central Finance Analyst | 6 | 6 |
| 9 | DC-050-530_Assign_Resources_to_Tasks | DC-050-530_Assign_Resources_to_Tasks | CES / Intel Products Capital Finance, Capital Analyst | 2 | 2 |
| 10 | DC-050-560_Determine_Total_Planned_Project_Costs | DC-050-560_Determine_Total_Planned_Project_Costs | BU Analyst, Corp. FP&A Analyst | 21 | 3 |
| 11 | DC-050-570_Load_Project_Plan_(Forecast) | DC-050-570_Load_Project_Plan_(Forecast) | BU Analyst, Corp. FP&A Analyst | 18 | 10 |
| 12 | DC-050-580_Validate_Plan | DC-050-580_Validate_Plan | Analyst, Capital Analyst | 14 | 7 |
| 13 | DC-050-590_Copy_Plan_Version | DC-050-590_Copy_Plan_Version | Analyst, Corp. FP&A Analyst | 11 | 7 |
| 14 | DC-050-600_Reload_Cost_Plan | DC-050-600_Reload_Cost_Plan | BU Analyst, Corp. FP&A Analyst | 8 | 7 |
| 15 | DC-050-610_Define_a_Budget | DC-050-610_Define_a_Budget | Capital Analyst | 3 | 4 |
| 16 | DC-050-620_Release_a_Budget | DC-050-620_Release_a_Budget | Capital Analyst | 3 | 4 |
| 17 | DC-050-630_Display_Available_Budget | DC-050-630_Display_Available_Budget | Capital Analyst | 1 | 0 |
| 18 | DC-050-660_Process_month-end_adjustments | DC-050-660_Process_month-end_adjustments | Finance Analyst | 3 | 0 |
| 19 | DC-050-670_Release_WBS | DC-050-670_Release_WBS | Boundary Apps, Capital Finance Project Analyst | 2 | 8 |
| 20 | DC-050-690_Validate_Project_Reports | DC-050-690_Validate_Project_Reports | Capital Analyst | 1 | 2 |
| 21 | DC-050-700_Supplement_Budget | DC-050-700_Supplement_Budget | Capital Finance Project Analyst, Corporate Capital Finance Analyst, Finance Analyst | 5 | 7 |
| 22 | DC-050-720_Run_Periodic_reports_(if_needed) | DC-050-720_Run_Periodic_reports_(if_needed) | Capital Analyst | 6 | 3 |
| 23 | DC-050-740_Obtain_Acceptance_for_Project_Closure | DC-050-740_Obtain_Acceptance_for_Project_Closure | Capital Analyst | 2 | 3 |
| 24 | DC-050-780_Reduce_Budget | DC-050-780_Reduce_Budget | Corporate Capital Finance Analyst | 3 | 3 |
| 25 | DC-050-790_Transfer_Budget | DC-050-790_Transfer_Budget | Capital Analyst, Corporate Capital Finance Analyst | 6 | 3 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 DC-050-110_Perform_Implementation_Audit — DC-050-110_Perform_Implementation_Audit

**Swim Lanes**: Capital Analyst | **Tasks**: 5 | **Gateways**: 0

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
    subgraph Capital Analyst
        n1["fa:fa-user Restrict Labour/Expense booking through user status"]
        n2["fa:fa-user Generate open PO report"]
        n3["fa:fa-user Perform Final Settlements"]
        n4["fa:fa-user Check that all Invoices have been Received"]
        n5["fa:fa-user Check AuC Balances are Zero"]
        n6["Close Project"]
        n7["Run Periodic reports"]
    end
    n3 --> n6
    n1 --> n2
    n7 --> n1
    n4 --> n3
    n2 --> n5
    n5 --> n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 startEvt
    class n7 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVU2P4jgQ_StWWi0uQZtPwuSwEgQyamlW22p6Z6TZnoNxKsSDsSPboWFa_PexSYAOS582hyj1XPVeVbnsvDlEFOCkzv39G-VUp-htoCvYwCBFgyVWMHBRC3zFkuIlAzWwPqXgekF_Hd38qN5ZN4vleEPZ3qILWAlA_zy4aGICmYsU5mqoQNJy4A5qSTdY7jPBhLTedzAuvfKo1i1NhSxAXhw8L_FJbEIZ5XCBwyRKotzGKSCCFz3SMi7HJRkcbHJMvJIKS31Mv1HwF959o4WujF1ipsD4VHrDvuAlMFujlo3FSCO3p2ZQZXW4adiixoTylcEjz0AS8_UFir3DAR3u71_4WRQ9z144Mg9hWKkZlEhpA8-3GpWUsfQuyiZ57LlKS7GG9C6YJ7MwcImtJDWle65t7vAV6KrS6VKwonMdvtoa0qDeuXKXBp4r9-Z9pQW8uChlo2AcjM9K08TP_OykVJbl_1IyfZXPWK07rXmYB_nsrOXHozjz_st3KnMWJRP_uk8gt5TAO9I8z8P5pVXzUex7H5NO83DkZVekK6zhFe8vhJ-y6EyYx0nuJx8StnrXWTbLRynIiTCcx3l8Jkymfj4JPiSMJn407jI0PCuJ6wpluKYaMzThmO2Vblftw_1_X5wSpyUe2majJzC8lGhkBlc08o_5rgauAC2FWJtxRLqSollVx52xQ6cb9eL8eMcX9Pk-Awdp2oOE4UGPfyMJtZC6HxP2Yx5BlkJuUE5NtmgBWjNzYXB9pRT1o7IKyNrkhzXCjKEHvhVmoxWq8NakD0b9CQjQLRR9mvgWzaTJ0BQzzC0DloC-gxT9uJGJy5gwvTFb9RPIVU2JWX5quC2GioKSrvBLDeYUtR88RMPhn4awM_3WDDozac1ukHnUmmFnBq0Zd2bcmtG7ebKEp3PUg4PbcHgbjm7D8W14dL6QenByhh3X2YDcYFo46Ztz_COYv0YBJW6Ydg6ugxstFntOnPR4czpNXZgxmlFsBnrTgoffPJANNA==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 DC-050-120_Close_Project — DC-050-120_Close_Project

**Swim Lanes**: Batch User · CCF Analyst · CES / Intel Products Capital Finance · Capital Analyst · Capital Enterprise Solutions (CES) Analyst · Capital Finance Analyst · Finance Analyst | **Tasks**: 18 | **Gateways**: 10

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
    subgraph Batch User
        n14[["fa:fa-cog Send List of WBS Elements TECO Candidates for Approval (Based on DSD)"]]
    end
    subgraph CCF Analyst
        n16["Send Error Reports via Email to CCF"]
    end
    subgraph CES / Intel Products Capital Finance
        n6["fa:fa-user Resolve WBS Element Closure Error"]
        n31{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Capital Analyst
        n1["Close PPM item (PS/PPM autosync function)"]
        n4["fa:fa-user Run Automatic WBS Element Close Program (via Batch Job)"]
        n5["fa:fa-user Approve WBS Elements for Closed Status"]
        n9[["fa:fa-cog Update WBS System Status to TECO Based on Approval"]]
        n10[["fa:fa-cog Update WBS System Status To TECO Based on Project Definition Finish Date"]]
        n11[["fa:fa-cog Close Individual WBS Elements (L1/L2) X Days After Last TECO Date"]]
        n12[["fa:fa-cog Close the Project Definition"]]
        n13[["fa:fa-cog Send List of Potential WBS Elements to be Closed for Approval (Based on X..."]]
        n20(["fa:fa-stop Email notification sent to Requestor/CES team"])
        n23{{"fa:fa-code-branch Capital Related Expense Project?"}}
        n24{{"fa:fa-code-branch AUC Is Zero?"}}
        n25{{"fa:fa-code-branch exclusiveGateway"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch WBS Element Closed Successfully?"}}
        n28{{"fa:fa-code-branch All Individual WBS Elements Closed?"}}
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n32[["fa:fa-folder-open Perform Implementation Audit"]]
        n33[["fa:fa-folder-open A Run Project Settlement"]]
    end
    subgraph Capital Enterprise Solutions (CES) Analyst
        n15["Send Error Reports via Email to Capital Analyst"]
        n30{{"fa:fa-code-branch Budget Remaining on Level 1?"}}
    end
    subgraph Capital Finance Analyst
        n7["fa:fa-user Approve WBS Elements for TECO"]
    end
    subgraph Finance Analyst
        n2["fa:fa-user Set User Status to CNLD and System Status to TECO"]
        n3["fa:fa-user Set System Status of Project to CLSD"]
        n8[["fa:fa-cog Set Portfolio Item Status to CLSD"]]
        n17["Obtain Approval from Project Manager to Close Project"]
        n18["Identify Project for Deactivation"]
        n19(["fa:fa-stop Project closed"])
        n21["Perform Implementation Audit"]
        n22{{"fa:fa-code-branch CAPEX or OPEX?"}}
    end
    n2 --> n3
    n21 --> n22
    n17 --> n2
    n8 --> n19
    n22 -->|"OPEX"| n18
    n3 --> n8
    n18 --> n17
    n4 --> n24
    n32 --> n23
    n25 --> n32
    n23 -->|"Yes"| n10
    n24 -->|"No"| n25
    n26 --> n13
    n11 --> n27
    n27 -->|"Yes"| n28
    n27 -->|"No"| n30
    n30 -->|"No"| n15
    n15 --> n31
    n16 --> n31
    n31 --> n6
    n28 -->|"No"| n26
    n6 --> n26
    n24 -->|"Yes"| n29
    n33 --> n4
    n10 --> n29
    n30 -->|"Yes"| n16
    n28 -->|"Yes"| n12
    n22 -->|"CAPEX"| n25
    n29 --> n26
    n9 --> n33
    n23 -->|"No"| n14
    n14 --> n7
    n7 --> n9
    n13 --> n5
    n5 --> n11
    n1 --> n20
    n12 --> n1
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n19 endEvt
    class n20 endEvt
    class n21 startEvt
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
    class n32 subProc
    class n33 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWG1z2jgQ_isadzIkM6T1KwY-XAcM3OSGtpnQXHvX3Adhy6CrsTlZJuFS_vutbMlgY_dyPT4ko13t8-yudleIZ81PAqINtYuLZxpTPkTPHb4mG9IZos4Sp6TTRYXgV8woXkYk7Yg9YRLzBf0732bY2yexTchmeEOjvZAuyCoh6P6mi0ZgGHVRiuP0OiWMhp1uZ8voBrO9l0QJE7tfkX6ohzmbVI0TFhB23KDrruE7YBrRmBzFlmu79kzYpcRP4qACGjphP_Q7B-FclDz6a8x47n6Wknf46RMN-BrWIY5SAnvWfBPN8ZJEIkbOMiHzM7ZTyaCp4IkhYYst9mm8Armtg4jh-OtR5OiHAzpcXDzEJSma3z3ECD5-hNN0QkKUchBPdxyFNIqGr2xvNHP0bspZ8pUMX5lTd2KZXV9EMoTQ9a5I7vUjoas1Hy6TKJBbrx9FDENz-9RlT0NT77I9_K1xkTg4Mnk9s2_2S6axa3iGp5jCMPxfTJBX9hGnXyXX1JqZs0nJZTg9x9PP8VSYE9sdGfU8EbajPjkBnc1m1vSYqmnPMfR20PHM6uleDXSFOXnE-yPgwLNLwJnjzgy3FbDgq3uZLW9Z4itAa-rMnBLQHRuzkdkKaI8Muy89BJwVw9s1GmPur9E9RF8oxCc27C9fHrQQD0N87ScrtICDRXOacpSE6NN4gaYRNGrMU_Rx6n1AHo4DGkCoKQoThkbbLUt2OEKXY-jrACUxmiwmVw_aH38UHIBW88LzZmgU42if8lM3euBFzj1lDIDvyDZhQLqjGE03mEaIJ8IUkFuBpwv0Bt3EnEQIEhdkPth7eEs5-DejMY59csLYK8MWBQaEaRLtyGnIyIuSNGOkcKlkzq0t4_n5mLaAXC-hXyG75MmPspTuyM9FOTxoh0Orw9K3hmyAb4KcoNvbd4hyskGXt4s3YoEznqT7GMoii31Ok_iq6phdCyuL0QhMNphT_yw4IhIFzgC8SHRRIL8kyxqmU8UsDp1Uq0NUQw4ZoAXHPEurEINqld1vRQ3lCAsIHeIrjMQp53VWlpOqsGNJFRnSXwj4sQ4IEf9JfI6gxcTlBBkUxUHTNZoAQp3GqNIUSbuBHtjRIIOzq-Tgcm68mZtX6DNA7VM0Cjlka46hl3IXmvDNJny4GxvcrJta32nc24SDR7TuIGR3SdQxtfTv59evX9eoTP2ypEp5spUdGSechtTHeQ5TUVOAf0f-yghsYm9EP3KCNwB2dQpmNXeO6oY7EkGeYA48bUmclol4e-ykAsZuhhnde-gmRb8TlpyZOP-1Zwuz3o-Zuc1mZz0IDZP5PknTMIui_ZnT_ZY4o6i1DgvYM6TBD8VhnZRoCFc3YdcJnAy6JQwqaINuNtuCt6iDURZQXqsfy2qGGOXjSVX6gnBeIH33-pBlMoU5z-BrHVTIIokywQ0NCDV31TRPnZfcLrVxXJ33enPyxlmwIhwAASWGr2qig-ZkB1eQ8fYls1_eSw0-uy8cumK0fOdWbCcwqwSQ_vy7wckk9t7PJwgu_OYZXUvQOVrVSkwledICer6YVAH69XHGYYoxDvVCE3RTpZfWlXEo8vVhyeEYjlMtZMmmZH2HY7wC14S9uvuEouqG0Qecm0BMz3Bf2opETwiGC3eH5Sw-tRnU5qMy8_NGrA9Acbv_S_ecbjdb5uXodvoZgV8f4H9TrcUmur7-CU5GLY1ibZpSYLhSINf9YmkMlEEO8A3SCgwP2jeRHKmyiq1qaShTVwpsiWyr_dIXs3TGkc4pctOSZL-RtODSlcaWmvdJrjAdpehJVgVqqAiVG6ZbAzX7dY0EtRSbpVcVhmIzlMeGEvRqAkvS9xRHv-a4UkjDcl1GWLqpjsCSiVZ5NHRpOqi7W6btjL3UmPVzzUuoltNBzTe5tqz6Oan8lK7JM1e5l8WlHDVkJIpIZtMosyl51TkYsmJO326ipNVrsCK2msV2s9hpFveaxW6zuH_6iqxoBq0aOL1WldGuMttVVrvKblcN5Ou9mlq9UWqUvypU5aZ68FbFVrPYbhY7zeJes9htFvebxYNGMfRLo9hoFpvqFV4VW0qsdbUNYXD3B9rwWct_09KGWkBCnEVcO3Q18VxbwHNNG-a__WhZ_k6ZUCxeXYXw8A-vf_jD" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 DC-050-300_Manage_IM_Program_Positions_(PPM_Portfolio_and_Buckets) — DC-050-300_Manage_IM_Program_Positions_(PPM_Portfolio_and_Buckets)

**Swim Lanes**: Capital Central Finance Analyst | **Tasks**: 6 | **Gateways**: 9

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
    subgraph Capital Central Finance Analyst
        n1["fa:fa-user Create Portfolio"]
        n2["fa:fa-user Maintain Portfolio"]
        n3["fa:fa-user Create Bucket and Sub-Buckets"]
        n4["fa:fa-user Maintain Bucket and Sub-Buckets"]
        n5["fa:fa-user Create Classification Hierarchy"]
        n6[["fa:fa-cog Send Bucket and Sub Bucket Details to SAC System"]]
        n7(["fa:fa-play IM Program Positions needs to be Managed"])
        n8(["fa:fa-stop Sent to SAP SAC"])
        n9["- Manage IM Program Position Budget (PPM Porfolio and Buckets)"]
        n10["Changes Needed are Determined by Affected Teams"]
        n11["Changes are made after Affected Team Communicates and Collaborates with CES Team"]
        n12{{"fa:fa-code-branch exclusiveGateway"}}
        n13{{"fa:fa-code-branch Is Classification Hierarchy Required?"}}
        n14{{"fa:fa-code-branch CAPEX Hierarchy Available?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
        n16{{"fa:fa-code-branch Reorganization Required?"}}
        n17{{"fa:fa-code-branch exclusiveGateway"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
        n19{{"fa:fa-arrows-alt parallelGateway"}}
        n20{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n2
    n2 --> n3
    n12 --> n1
    n13 -->|"No"| n15
    n5 --> n12
    n13 -->|"Yes"| n5
    n7 --> n14
    n14 -->|"Yes"| n12
    n15 --> n9
    n3 --> n18
    n16 -->|"No"| n17
    n18 --> n16
    n19 --> n6
    n17 --> n13
    n4 --> n20
    n20 --> n17
    n20 --> n19
    n16 -->|"Yes"| n10
    n11 --> n4
    n14 -->|"No"| n15
    n10 --> n11
    n18 --> n19
    n6 --> n8
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
    class n9 startEvt
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV2uP4jYU_StWRiN2JZDyJCEfWjGBtCt1VmiZvrT0g0luwBrHobYzDMvy32uThEcmSO0UCQYfn3vOvdfG8eyNpEjBCI37-z1hRIZo35NryKEXot4SC-j1UQX8hjnBSwqipzlZweScfDvSLHfzqmkai3FO6E6jc1gVgH791EdjFUj7SGAmBgI4yXr93oaTHPNdVNCCa_YdBJmZHd3qqYeCp8DPBNP0rcRToZQwOMOO7_purOMEJAVLr0QzLwuypHfQydFim6wxl8f0SwGP-PV3ksq1GmeYClCctczpL3gJVNcoeamxpOQvTTOI0D5MNWy-wQlhK4W7poI4Zs9nyDMPB3S4v1-wkyl6miwYUq-EYiEmkCEhFTx9kSgjlIZ3bjSOPbMvJC-eIbyzp_7EsfuJriRUpZt93dzBFshqLcNlQdOaOtjqGkJ789rnr6Ft9vlOfba8gKVnp2hoB3ZwcnrwrciKGqcsy_6Xk-orf8LiufaaOrEdT05eljf0IvOtXlPmxPXHVrtPwF9IAheicRw703OrpkPPMm-LPsTO0IxaoissYYt3Z8FR5J4EY8-PLf-mYOXXzrJczniRNILO1Iu9k6D_YMVj-6agO7bcoM5Q6aw43qxRhDdEYooiYJKrvzFhmCWAxgzTnZAVW7-Y9XVhZDjM8EA3H0UcVHFoVnCZFZQUC-OvC7J9TX7EhEn1vkV3OrUfyuQZJMIsRfNyOaiG4jrSvWH0b2K9TtdI95pkJMGSFAz9TIBjnqx317HDr6fgpFihudr6Lc9mOAGVEBVIFmg-jtBcdRVyJXap5n84qW2o2i-fHpFaZrVCueqYIDoRgRhAepRZgqqT4RWkSubjhUxwlhGy2OisZOU7094t9kiRB7VSl6MqIF2pAj7MZo964Y7rdqyu7ubH65ZYphKM1pitQKDPKllIEeagGwA8V4dpipY7NM4ySKT6_gQ4by2IZV0o6NAcp4BwpuKv41BU5HnJ9BpppkpJncUULwt-BLZEqp09nR-5LQt7vz8vXAqDpTpTkzWC14SWgrzAT9VPdmEcDpdhTnfYJ3Fzv6Av8HdJOKQ_trXcbq1oPJv-cRE_flH7Rj8J3wh476th2B32BQq-wox8qwq4mbb_PtfgHIY5L7ZigKlEG6xOGwr0RtDoHUG2-d-C1E-2-sIsNBj8oATqoV0NnWa2HlvN2NHj7wvjszrFvuvlqCe8mme3iX-CODIbol8T3YbotohniVpzVI-dOjJo5oetXPxmIqiZwwYYVcBp3CTRlOnWTTCbLpg1wW8Do7b5Ke0m1qo7-qbAdsusRtNq592YDKtxcPEg1AvWXACuYLsbdrphtxv2uuHh5Q3hasY_3bGu4KC-Dl2Bo26uakM3bt3A7eZqcQ073bDbDXvd8LAb9rvhoBsedcJqC9Ww0Tdy9VTAJDXCvXG8-Kt_DlLIcEmlcegbuJTFfMcSIzxekI1yk6rICcH6GVWBh38AknLeSQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 DC-050-310_Manage_IM_Program_Position_Budget_(PPM_Portfolio_and_Buckets) — DC-050-310_Manage_IM_Program_Position_Budget_(PPM_Portfolio_and_Buckets)

**Swim Lanes**: Capital Central Finance Analyst | **Tasks**: 10 | **Gateways**: 6

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
    subgraph Capital Central Finance Analyst
        n1["fa:fa-user Review Original Budget (Portfolio and Bucket)"]
        n2["fa:fa-user Review Updated Budget Values (Portfolio and Bucket)"]
        n3["fa:fa-user Input Original Plan or Budget (Portfolio and Bucket)"]
        n4["fa:fa-user Input Updates to Budget Values (Portfolio and Bucket)"]
        n5["fa:fa-user Update Original Budget (Portfolio and Bucket)"]
        n6["fa:fa-user Make Necessary Changes to the Updated Budget Values"]
        n7["fa:fa-user Distribute Original Budget Values Within BU"]
        n8["fa:fa-user Distribute Original Budget Values to BU's"]
        n9[["fa:fa-cog Consume Original Budget (Portfolio and Bucket)"]]
        n10[["fa:fa-cog Consume Budget Updates (Portfolio and Buckets) from SAC"]]
        n11["-Distribute IM Program Position Budget to Projects/WBS"]
        n12["Manage IM Program Positions (PPM Portfolio and Buckets)"]
        n13{{"fa:fa-code-branch Approved?"}}
        n14{{"fa:fa-code-branch Approved?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
        n17{{"fa:fa-code-branch Are Updates Required?"}}
        n18{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n7 --> n17
    n17 -->|"Yes"| n4
    n8 --> n7
    n17 -->|"No"| n18
    n18 --> n11
    n10 --> n18
    n12 --> n3
    n1 --> n13
    n2 --> n14
    n13 -->|"Yes"| n9
    n14 -->|"Yes"| n10
    n13 -->|"No"| n5
    n15 --> n1
    n5 --> n15
    n3 --> n15
    n14 -->|"No"| n6
    n16 --> n2
    n6 --> n16
    n4 --> n16
    n9 --> n8
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 startEvt
    class n12 startEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlll2P4jYUhv-KldGIrhTUOB8kk4tWEEg10s52tOzsqFp6YRIH3Ak2tR0YyvLfa5MESDZInSkXwHnP8XM-wI73RsJSbITG7e2eUCJDsO_JJV7hXgh6cyRwzwSl8BVxguY5Fj0dkzEqp-SfYxh01686TGsxWpF8p9UpXjAMnu5NMFQLcxMIREVfYE6yntlbc7JCfBexnHEdfYODzMqO2SrXiPEU83OAZfkw8dTSnFB8lh3f9d1YrxM4YTRtQDMvC7Kkd9DF5WybLBGXx_ILgR_Q6zNJ5VLZGcoFVjFLuco_ojnOdY-SF1pLCr6ph0GEzkPVwKZrlBC6ULprKYkj-nKWPOtwAIfb2xk9JQVfxjMK1CvJkRBjnAEhlTzZSJCRPA9v3GgYe5YpJGcvOLyxJ_7Ysc1EdxKq1i1TD7e_xWSxlOGc5WkV2t_qHkJ7_Wry19C2TL5T761cmKbnTNHADuzglGnkwwhGdaYsy_5XJjVX_gWJlyrXxInteHzKBb2BF1k_8uo2x64_hO05Yb4hCb6AxnHsTM6jmgw8aF2HjmJnYEUt6AJJvEW7M_Auck_A2PNj6F8FlvnaVRbzR86SGuhMvNg7Af0RjIf2VaA7hG5QVag4C47WSxChNZEoBxGmkqvPmFBEEwyGFOU7Icto_aLw28zIUJihvh4--Iw3BG_B75ws1JIcjIp0gSX46ZFxmbGcMIBoqtTkBcsPM-PPC5LdSXpap2paaQ36ivICi__Ec5q8e7ou5LmwxxxRwPhbCnS7gGV9Akj2jhK9JrFkvWt4gybpAb1g8AknWAh1IoFoieiiLFIdpt0zbfL8Jm9M1N-HzIuO6qp2n4lcEgpGT01O8FaOnuNTr1XN3bcTJmELEDEqitUbBnXJglY3rGLUv2cnS3wAGWcrMB1GbareB_2L9u4fgNqSajetwCMTRBJG6xSqReX6CydS_Pw8mjZbhXobPCCKFp0MXdijkjuLa5Gc_f7caIr7c_WcSJZguF5ztsHprzPjcLiMd98Y73XH49ckLwTZ4N_KY669bPC-Zf6V6jg-_Waf8d8F4R2VBm9NqR5Z5Rfqg37_F52-suFR-D4z_tBb5rs6FSpHUAb-EPeJHcNgUDuqQAhrwaqEU4RdCk5tV_7artywzgydVkl3tcNtOaDVXlJV59W6V7EruzZrv9OyTxkqzqDWB2WgXdmVCWu_27LvSju4eK7pvuvneUO2u2WnW3a7Za9bHnTLfrccdMt3l7eGZkfWdRc83cmaun1Fd-prRFN2u2WvWx50y363HNSyYRorzFeIpEa4N473c3WHT3GGilwaB9NAhWTTHU2M8HiPNYrjDh0TpA-zUjz8C1pdyds=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 DC-050-340_Workflow_project_for_approval — DC-050-340_Workflow_project_for_approval

**Swim Lanes**: Capital Analyst | **Tasks**: 3 | **Gateways**: 2

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
    subgraph Capital Analyst
        n1["fa:fa-user Release Project and Budget Approval workflow"]
        n2["fa:fa-user Execute Project and Budget Approval Workflow"]
        n3["fa:fa-user Request Another Budget Approval"]
        n4["Distribute IM Program Position Budget to Projects/WBS"]
        n5["Manage IM Program Position Budget (PPM Portfolio and Buckets)"]
        n6{{"fa:fa-code-branch Budget Approved?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n5 --> n7
    n1 --> n2
    n2 --> n6
    n6 -->|"No"| n3
    n7 --> n1
    n3 --> n7
    n6 -->|"Yes"| n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P4jYU_StWRiNaKWjzSWgetoJAqpV2qlHZ3VFV9sEkN-Bi7NR2-CjLf69NEphQZl82DxH3-J5zfC--ztHKeA5WbD0-HgkjKkbHnlrBBnox6i2whJ6NauALFgQvKMieySk4UzPy7znNDcq9STNYijeEHgw6gyUH9PmDjUaaSG0kMZN9CYIUPbtXCrLB4pBwyoXJfoBh4RRnt2ZpzEUO4prgOJGbhZpKCYMr7EdBFKSGJyHjLO-IFmExLLLeyWyO8l22wkKdt19JeML7F5KrlY4LTCXonJXa0I94AdTUqERlsKwS27YZRBofphs2K3FG2FLjgaMhgdn6CoXO6YROj49zdjFFnyZzhvSTUSzlBAoklYanW4UKQmn8ECSjNHRsqQRfQ_zgTaOJ79mZqSTWpTu2aW5_B2S5UvGC07xJ7e9MDbFX7m2xjz3HFgf9vvECll-dkoE39IYXp3HkJm7SOhVF8UNOuq_iE5brxmvqp146uXi54SBMnP_rtWVOgmjk3vYJxJZk8Eo0TVN_em3VdBC6ztui49QfOMmN6BIr2OHDVfCXJLgIpmGUutGbgrXf7S6rxbPgWSvoT8M0vAhGYzcdeW8KBiM3GDY71DpLgcsVSnBJFKZoxDA9SFWvmoe5f82tAscF7ptmoz-Agh5TpO3_hkwhzHI0rvIlKDQqS8G3WmTHxdocxbn19ZWQ1xWa7iGr1PeFXu4K-bc7-qcCqVmM64tD3Ip0uYHmTohuDVkY8w9Pxl-3YIOeuSSKcNbyFW-3Jt-9jGddmVDLPGGGl9-V-On5WS9yoQpOCW8qzNag5M9ducHx2JZkrsf-Qg94tupWAvmvc-t0esWK7rNgn9FKki38Vp-6K0vPZf2Dhajff68VmtCtQ68JvTocNOHAhN_m1u98bn3T7W_gqM5qBoj5XcmW9CfIMyt4dYKNYTu5Hdi7D_v34eByqXXg8D48aKewg0YtatnWBsQGk9yKj9b5C6S_UjkUuKLKOtkWrhSfHVhmxeeb2qrKXDMnBJu_vgZP_wEjgDRN" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.6 DC-050-350_Distribute_Project_budget_to_account_assignment_WBS — DC-050-350_Distribute_Project_budget_to_account_assignment_WBS

**Swim Lanes**: Capital Analyst | **Tasks**: 5 | **Gateways**: 3

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
    subgraph Capital Analyst
        n1["fa:fa-user Distribute Project budget to lower level WBS element"]
        n2["fa:fa-user Execute Report to Validate Budget Amount on WBS Element"]
        n3["fa:fa-user Update the Budget Amount on the Required WBS Element"]
        n4["fa:fa-user Approve Budget for L2 WBS Element"]
        n5["fa:fa-user Approve Budget for L4 WBS Element"]
        n6(["fa:fa-stop Account Assignment/Lower Level WBS is budgeted"])
        n7(["fa:fa-stop L1 WBS element Budgeted"])
        n8["Release a Budget"]
        n9{{"fa:fa-code-branch Distribute Budget to Lower Lever WBS Element? (Small Construction only?)"}}
        n10{{"fa:fa-code-branch Updates Required?"}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n8 --> n9
    n1 --> n11
    n9 -->|"No"| n7
    n2 --> n10
    n10 -->|"Yes"| n6
    n11 --> n2
    n3 --> n11
    n4 --> n5
    n9 -->|"Yes"| n4
    n5 --> n1
    n10 -->|"No"| n3
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 endEvt
    class n7 endEvt
    class n8 startEvt
    class n9 gateway
    class n10 gateway
    class n11 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqllluP4jYUx7-KldGIXSmouRImDx2FQKpKtKqGvWhV-mASB9wxdmo7DJTlu6-dG4QB9aF5QPifc37nYuckRyNlGTJC4_HxiCmWITgO5AZt0SAEgxUUaGCCWvgCOYYrgsRA2-SMygX-tzKzvWKvzbSWwC0mB60u0Joh8PlXE0TKkZhAQCqGAnGcD8xBwfEW8kPMCOPa-gGNcyuvojW3JoxniJ8NLCuwU1-5EkzRWXYDL_AS7SdQymjWg-Z-Ps7TwUknR9hbuoFcVumXAv0G919xJjdqnUMikLLZyC2ZwxUiukbJS62lJd-1zcBCx6GqYYsCppiule5ZSuKQvp4l3zqdwOnxcUm7oODTdEmBulIChZiiHAip5NlOghwTEj54cZT4likkZ68ofHBmwdR1zFRXEqrSLVM3d_iG8HojwxUjWWM6fNM1hE6xN_k-dCyTH9TvVSxEs3OkeOSMnXEXaRLYsR23kfI8_1-RVF_5Jyhem1gzN3GSaRfL9kd-bL3ntWVOvSCyr_uE-A6n6AKaJIk7O7dqNvJt6z50krgjK76CrqFEb_BwBj7FXgdM_CCxg7vAOt51luXqD87SFujO_MTvgMHETiLnLtCLbG_cZKg4aw6LDYhhgSUkIKKQHISs7-qL2n8ujRyGORzqZoMpVly8KiUCKoO_USrBqszWSALJgDp-yoSgHSLg62QBEFEPMpVL468LoNMHzvYo1bQXVDBeUb5AgjPVMTCpwdGWlVQCRivm7BbT7TM_F5W_miPvGVp8Qf-UmKPsPtDrA6Oi4GzX0XLGwdy57-3_t7d333v0oXMXkhUgStMq-UgIvKba_qd51eh512gsml1AmWJ9vIAFV7C5fbkzTUrvvMbK6UXZqIEMYGPUT_LpeGy5eqIPV2ompZvL4zHpjsU5W35Z9TP4sNhCQkDMqPIqU4nV_jBKDs8fl8bpdHkIrdvh6o0W3YY-X_vZt_3QPiWlwDv0S_1knt3U7Kr_0DEYDn9WhTZLu17azcCgT3r9fWn8zpbGd9XnRnYaM6t1sxq7b0hUhqP2RgN0mrV7xffqtX8VrsV4je43btfhmrTci8Gha2gHZk92bsvubdm7Lfu35VHzNuiJwS1x3L2jevJTOz37lVi3ZbuVDdPYIr6FODPCo1F9UaivjgzlsCTSOJkGLCVbHGhqhNWb1yirozTFUA3EbS2efgDhssEj" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 DC-050-410_Simulate_Depreciation — DC-050-410_Simulate_Depreciation

**Swim Lanes**: CES / Intel Products Capital Finance · Capital Analyst | **Tasks**: 3 | **Gateways**: 0

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
    subgraph CES / Intel Products Capital Finance
        n3["fa:fa-user Update Depreciation Simulation Data on WBS Element"]
        n5["Manage Project Periodic Settlement"]
    end
    subgraph Capital Analyst
        n1["fa:fa-user Run Depreciation Forecast Report"]
        n2["fa:fa-user Send Information to SAC"]
        n4["Run Periodic reports"]
    end
    n5 --> n3
    n3 --> n1
    n1 --> n2
    n2 --> n4
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVF1v2jAU_StWKsRL0PJJWB4mQSBSpVWqlnZ9GHswjg1eHTuynQJD_PfZBMJH26flIck9ufecc29s7xwkSuykTq-3o5zqFOz6eoUr3E9BfwEV7rugBX5CSeGCYdW3OURwXdC_hzQ_qjc2zWI5rCjbWrTAS4HB870LxqaQuUBBrgYKS0r6br-WtIJymwkmpM2-wyPikYPa8dNEyBLLc4LnJT6KTSmjHJ_hMImSKLd1CiPByytSEpMRQf29NcfEGq2g1Af7jcIPcPNCS70yMYFMYZOz0hX7DheY2R61bCyGGvl2GgZVVoebgRU1RJQvDR55BpKQv56h2Nvvwb7Xm_NOFDxN5xyYCzGo1BQToLSBZ28aEMpYehdl4zz2XKWleMXpXTBLpmHgIttJalr3XDvcwRrT5UqnC8HKY-pgbXtIg3rjyk0aeK7cmvuNFublWSkbBqNg1ClNEj_zs5MSIeS_lMxc5RNUr0etWZgH-bTT8uNhnHnv-U5tTqNk7N_OCcs3ivAFaZ7n4ew8qtkw9r3PSSd5OPSyG9Il1HgNt2fCr1nUEeZxkvvJp4St3q3LZvEoBToRhrM4jzvCZOLn4-BTwmjsR6OjQ8OzlLBegWxWgC_gnmvMgGEuG6QVyGBNNWQgpxxyhNsSe_Hw19whMCVwYP8AeK5L0yGY4lpiRKGmgoOCVg1rX6dQQ2CeL5MCzJjZ21zPnd8XdLGhe4AcLrEV_4ORBo9m44qSIlBgrW9qzPq6tX90OuaQbZW-oPavnf5o-LXNXJh3qDT4gWshb3wF18WFETYzIkJWbbEWoBhn1zWRqbEqXQPyQKzeu-cxGAy-mWEew7ANjyuS-20YHMOgDaOLlWBzTjvgCg4-hsOP4ag7HK7guIMd16mw6ZmWTrpzDqezOcFLTGDDtLN3HdhoUWw5ctLDKeY0h_UwpdD8naoF9_8AoRPrFQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 DC-050-520_Form_Core_Project_Team — DC-050-520_Form_Core_Project_Team

**Swim Lanes**: CES / Intel Products Capital Finance · Capital Analyst · Capital Central Finance Analyst | **Tasks**: 6 | **Gateways**: 6

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
    subgraph CES / Intel Products Capital Finance
        n4["fa:fa-user Assign Employees (Project WBS)"]
        n5["fa:fa-user Assign Contract Resources"]
        n6["fa:fa-user Assign Person Responsible (Project Manager) to Project WBS"]
        n9["Assign Resources to Tasks"]
        n10["Develop Engineering/Project Design"]
        n12["Validate Project Structure"]
        n16{{"fa:fa-code-branch Used by Construction or Others?"}}
        n18{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Capital Analyst
        n1["fa:fa-user Validate Assignment"]
        n7(["fa:fa-play Form Core Project Team Initiated"])
        n8["Manage IM Program Position Budget (PPM Portfolio and Buckets)"]
        n11["Manage IM Program Positions (PPM Portfolio and Buckets)"]
        n13{{"fa:fa-code-branch Updates Required?"}}
        n14{{"fa:fa-code-branch WBS or PPM Project Hierarchy?"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Capital Central Finance Analyst
        n2["fa:fa-user Assign Resources/Roles for Access Control at Bucket Level (Project Group)"]
        n3["fa:fa-user Update Assigned Resources/Roles for Access Control at Bucket Level (Project..."]
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n11 --> n17
    n1 --> n13
    n13 -->|"No"| n8
    n13 --> n3
    n15 --> n1
    n7 --> n14
    n17 --> n2
    n12 --> n18
    n18 --> n16
    n4 --> n5
    n14 -->|"PPM Project Hierarchy"| n17
    n14 -->|"WBS"| n18
    n6 --> n10
    n16 -->|"Others"| n6
    n5 --> n9
    n16 -->|"Construction"| n4
    n3 --> n15
    n2 --> n15
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
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtVmtvqzYY_isWVZVTKWmBQEj5sCk3ziq1W9Wcy4dlHxwwiVfHZrZpm6X573tNgFxKJk1n-RDJD-_zvHfDxopFQqzQurzcUE51iDYtvSQr0gpRa44VabXRDviGJcVzRlTL2KSC6yn9uzBzvOzNmBkswivK1gadkoUg6OtdGw2AyNpIYa46ikiattqtTNIVluuRYEIa6wvST-208FY-GgqZELk3sO3AiX2gMsrJHu4GXuBFhqdILHhyJJr6aT-NW1sTHBOv8RJLXYSfK_KA377TRC_hnGKmCNgs9Yrd4zlhJkctc4PFuXypikGV8cOhYNMMx5QvAPdsgCTmz3vIt7dbtL28nPHaKbp_mnEEv5hhpcYkRUoDPHnRKKWMhRfeaBD5dltpKZ5JeOFOgnHXbccmkxBSt9umuJ1XQhdLHc4FS0rTzqvJIXSzt7Z8C127Ldfwf-KL8GTvadRz-26_9jQMnJEzqjylafpDnqCu8gtWz6WvSTdyo3Hty_F7_sj-qFelOfaCgXNaJyJfaEwORKMo6k72pZr0fMc-LzqMuj17dCK6wJq84vVe8Hbk1YKRH0ROcFZw5-80ynz-KEVcCXYnfuTXgsHQiQbuWUFv4Hj9MkLQWUicLdFoMkU36I5rwhAoJ3msFRrhjGrMUEQ55jHZUcyPe7_PrBSHKe6YDqCBUnTB0WSVMbEmRKFPoPEniTX6Ppxezaw_Dqh-I3UEQyAxEJ6IErmMiTpm9RpZj0QqwQ0nE1xRuC32nh8wxwsir5AW6CCaY9lbkC21aseGYNp_EoFjg-2YvBAmMjThC7gV4G7hi5tKfEyMzgnJBdI3zGgCE1CHMYVdj3UuyYlxb7OpsjS3ZGcOex4v0VdFEjRfmxqpgkkhZyHRb3BPSvXzzNpuD1X6exUspXhVHcw0yrDEjBH2eTeKexIs6-kslG0fcMzWSh9qH3ehTmxXwhXh-jij4FNNyBjMfyTkCtKQ-1J8IXgFY0c1BZ0E2FcH9D6wd21Edw-GAvGt0KNQtCjBME8WREPHH-GhkDoVjAqEeQJP4mei1cnkOc6_6qn_oNQ906nMlEPBLP2VU0mSD73xmnkwl6ahhfuyML9QIrGMl-sPGsH_1d8RMTtXr3dDv93Gras35eZJwPsZpRD6IIaz2q2xYAjrsnLo3mzMfis_S5FnJ9XsHnvZFbF0BpP_A-6ur69PGuc3N4C8xSxX9IWcLx-MD-p0fjINqIDy3K3OXQO8z6xfxcx6h_E9wiHP6uyXxPIclEevel4CbnV2S4NasF8CvRLwdme_eu6VgTQOVBHbPonKtrgb3w-89EondmXZKy13905hXAVQZnR7anp4ZRWEKseyJE4Vsnt8Ll50psLVC_4IdpvhbjPsNcN-M9xrhoP6A-oI7jfDt82wY5_BnTO4ewbvVl8Ux7DXDPvNcK8ZDprhfgVbbWtF5ArTxAo3VvGpDp_zCUlxzrS1bVs412K65rEVFp-0Vl7s85hic9vuwO0_fgrROQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.9 DC-050-530_Assign_Resources_to_Tasks — DC-050-530_Assign_Resources_to_Tasks

**Swim Lanes**: CES / Intel Products Capital Finance · Capital Analyst | **Tasks**: 2 | **Gateways**: 2

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
    subgraph CES / Intel Products Capital Finance
        n2["fa:fa-user Assign Resources to Tasks to Support - Time Changing"]
    end
    subgraph Capital Analyst
        n1["fa:fa-user Update Technical Assistance Rates for Activity"]
        n3["Develop Engineering/Project Design"]
        n4["Form Core Project Team"]
        n5{{"fa:fa-code-branch Core Project Team is needed?"}}
        n6{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n1 --> n6
    n2 --> n1
    n4 --> n5
    n5 -->|"Yes"| n2
    n6 --> n3
    n5 -->|"No"| n6
    class n1 userTask
    class n2 userTask
    class n3 startEvt
    class n4 startEvt
    class n5 gateway
    class n6 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P4jYU_StWRiNegjafhOahFRNItVK7qhZ2V1Xpg3FuiDuOHdkOA2X577VDAgM789Q8RNyTc8-593LjHB0iCnBS5_HxSDnVKTqOdAU1jFI02mAFIxedga9YUrxhoEaWUwqul_TfjuZHzd7SLJbjmrKDRZewFYC-fHTRzCQyFynM1ViBpOXIHTWS1lgeMsGEtOwHmJZe2bn1j56ELEBeCZ6X-CQ2qYxyuMJhEiVRbvMUEMGLG9EyLqclGZ1scUy8kApL3ZXfKvgd77_RQlcmLjFTYDiVrtlveAPM9qhlazHSyt0wDKqsDzcDWzaYUL41eOQZSGL-fIVi73RCp8fHNb-YotV8zZG5CMNKzaFESht4sdOopIylD1E2y2PPVVqKZ0gfgkUyDwOX2E5S07rn2uGOX4BuK51uBCt66vjF9pAGzd6V-zTwXHkw9zsv4MXVKZsE02B6cXpK_MzPBqeyLP-Xk5mrXGH13HstwjzI5xcvP57Emfej3tDmPEpm_v2cQO4ogVeieZ6Hi-uoFpPY994XfcrDiZfdiW6xhhd8uAr-lEUXwTxOcj95V_Dsd19lu_lDCjIIhos4jy-CyZOfz4J3BaOZH037Co3OVuKmQtliiT6gj1wDQ0a5aIlWKMMN1ZihnHLMCZxT7MWDv9ZOidMSj-0_gGZK0S1Hn0GJVhJQSAtkJ9j9WLZNI8xKjtGK1oCyCvOtWdy18_dZ0GzLfTG974xjdlD6la9_6_ulKcxk0QpIxSmxGaYQs-mmWPTZPFGoFKY6oumO6sPFsZMKjdQcdsBEgxa2IjBHBd9-MN3_A0SjOdiebnMik5MLWaNMSEADcwW4vuXFx-NQpz3uxhvzwpLqxyxEFTK-BRS_rJ3T6ZXC5G0F2BPWKrqDX88bdc26TJH7aDz-2Sj0YXAO-z3n0TmM-zC24fe18yeotfPdsHt8cqaFd7RPomNNXq2jNRxewxs4eBsOL0fRDRy9DcfDu3ODTgbUcZ0aZI1p4aRHp_tumG9LASVumXZOroNbLZYHTpy0O1-dttuYOcVm0-ozePoPHjocNg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.10 DC-050-560_Determine_Total_Planned_Project_Costs — DC-050-560_Determine_Total_Planned_Project_Costs

**Swim Lanes**: BU Analyst · Corp. FP&A Analyst | **Tasks**: 21 | **Gateways**: 3

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
    subgraph BU Analyst
        n1["fa:fa-user Perform Provision of Capital Expense Planning Template to Enter CAPEX Plan"]
        n2["fa:fa-user Adjust Forecast and Categorize into TPF (Auth, Commits, Spends, OCOS)"]
        n3["fa:fa-user Estimate Total Planned Project Costs before Quarterly CPA Submission"]
        n16[["fa:fa-cog Load tool Level/Project Level Forecasted Spends"]]
        n17[["fa:fa-cog Pull in Historical Spends Data to Inform Spending Trend"]]
        n18[["fa:fa-cog Pull in Actuals Spend Data from S4"]]
        n22(["fa:fa-play Determine Total Planned Project Costs Initiated"])
        n24{{"fa:fa-code-branch CAPEX or OPEX?"}}
    end
    subgraph Corp. FP&A Analyst
        n4["fa:fa-user Ensure the IF MD and Investment Type Percentage are Correct"]
        n5["fa:fa-user Ensure the Drivers for Non-project Related Expenses are Available"]
        n6["fa:fa-user Capture the Total Non-project Related Spends by Cost Center"]
        n7["fa:fa-user Capture the Total Project Related Spends by WBS and Partner Cost Center"]
        n8["fa:fa-user Disaggregate to OCOS Subtype Either Equal Distribution or based on..."]
        n9["fa:fa-user Make any Adjustments or Judgements if Required"]
        n10["fa:fa-user Transform the Pre-Allocated Data to Post Allocated by LOB PF by PBA Logic"]
        n11["fa:fa-user Pivot the Total Project Forecasted Spend and See Drill Down by CCRU,..."]
        n12["fa:fa-user --160 Ensure the IP MD and Investment Type Percentage are Correct"]
        n13["fa:fa-user Capture the Total Project Related Spends by WBS and Partner Cost Center"]
        n14["fa:fa-user Make any Adjustments or Judgements if required"]
        n15["fa:fa-user Pivot the total Project Forecasted spend and See Drill Down by CCRU,..."]
        n19[["fa:fa-cog Calculate the RND and OCOS Spending Based on Flip Dates or Percentage"]]
        n20[["fa:fa-cog Calculate the RND and OCOS Spending Based on Flip Dates or Percentage"]]
        n21[["fa:fa-cog Transform the Pre-allocated Data to Post Allocated by LOB PF by PBA logic"]]
        n23(["fa:fa-stop Determine Total Planned Project Costs Completed"])
        n25{{"fa:fa-code-branch IP or IF?"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n22 --> n24
    n24 -->|"CAPEX"| n1
    n1 --> n16
    n16 --> n17
    n17 --> n18
    n18 --> n2
    n2 --> n3
    n24 -->|"OPEX"| n25
    n25 -->|"IF"| n4
    n4 --> n5
    n5 --> n6
    n6 --> n7
    n7 --> n19
    n19 --> n8
    n8 --> n9
    n9 --> n10
    n10 --> n11
    n25 -->|"IP"| n12
    n12 --> n13
    n13 --> n20
    n20 --> n14
    n14 --> n21
    n21 --> n15
    n11 --> n26
    n26 --> n23
    n3 --> n26
    n15 --> n26
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
    class n22 startEvt
    class n23 endEvt
    class n24 gateway
    class n25 gateway
    class n26 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq9WFFz2kYQ_is3yrgkM-DqhASYh3ZAoNQdJ6bBaToT9-GQTnDxIZG7EzZ1-O_dk3RgYaltmpn4wUbf7X3f7t7uHvKjFaYRtYbW2dkjS5gaoseWWtE1bQ1Ra0EkbbVRAfxOBCMLTmVL28Rpoubsr9wMu5sHbaaxgKwZ32l0TpcpRe8v22gEG3kbSZLIjqSCxa12ayPYmoidn_JUaOsXdBDbca5WLo1TEVFxNLDtPg492MpZQo9wt-_23UDvkzRMk6hCGnvxIA5be-0cT-_DFREqdz-T9A15-MAitYLnmHBJwWal1vyKLCjXMSqRaSzMxNYkg0mtk0DC5hsSsmQJuGsDJEhyd4Q8e79H-7Oz2-Qgim4mtwmCn5ATKSc0RlIBPN0qFDPOhy9cfxR4dlsqkd7R4Qtn2p90nXaoIxlC6HZbJ7dzT9lypYaLlEelaedexzB0Ng9t8TB07LbYwe8TLZpERyW_5wycwUFp3Mc-9o1SHMffpAR5FTdE3pVa027gBJODFvZ6nm8_5zNhTtz-CJ_miYotC-kT0iAIutNjqqY9D9vNpOOg27P9E9IlUfSe7I6EF757IAy8foD7jYSF3qmX2WIm0tAQdqde4B0I-2McjJxGQneE3UHpIfAsBdms0Pg9GiWE76QqFvRPgj_eWjEZxqSj84xmVMSpWCNQ3jLJ0gSlMfLJhinC0fRhQxNJ0YyTJIG6RDd0veEQN1IpmiYK9vuj2fSP3ODW-vOJjFOVGUWfMqlQkAoaEvhAkghUFLS3gAGAWAKEN7MAvRxlatVGfrpeMyXbaA4ORPD32r-ev6oqdKsKU6mg5cG1m1S7nrtMIx3XJxoqYJRKogWFYCn6LYO-oYLvkD8boXm2WDOpY68K4N7Hg0SYLtFVSiIIPOXoim4p_9FQ50-H0ECzcBrIKmz9Ktss4xziRr8wqSAJIfhc7EMToohO8GWSn0yO5skX8OGUdVDPOgpVBgOp2FwwxiIFMveEwHFeHgjgaHdoQiEzaxiP_5jISxjzDLKt_Xn1lM59fDz6E9HOAsZauCrLJBXoGv7-fGvt98UmHVG1aP1UbM5RMPthVFO87smZJzKD44SrBV0G6M0kL6vLZEulWtMEBuZuQ3WFh_BAlhQRMAZ-OChVPWqvkXci2JYKieAo0Ns06WzKNLyjug8i0yIy5x5tCeP6fquy96rs0F3K0Bc5riMui2GxyzOOfKrbrcrb_zfeWSPnh_E8T9YMGiHRe5s0BlWNCZNkuRR0WQ4B3Ze6gZTO9JSBNGTvM5SetlSCLTKVzxSB9PeACKXJ-fl5VeGiqvCG3MFBJbtyZOhzlHr_r1m0pMUTiyGizxkTefk97Qa7ynUDxSfzJtI5mQnaGXGehnkuTJfNdORHGHJzdT1GMIrg02w8gq5fsvBE5nSGsm2qatJ-OhLyjM9pXlTQppP0PsnP13_3vv0sLfhkgnY6uGdXKn72LRWPu9-heLD7f85W1J-t15R01ZR0-fVJv6iOU5_wMCsuPBB697bId1H0ZiyPy8JGAWcbXVY0j-l4CKcT1_4OGriq8bwRyFc3Ai8boaLTPd4ecI1t_uPtAdf7htOa28Orvz2g1CHay-DJxVHY9-rt6UPIMwmD-3XxHa3mvoGLD1rqJ31jGcDVwJdbK7-rbq0vUA7lEi5Mcc8890qgb4B-CQwMMCjZDXnx2D3VujZSjmeWvHLpMsgXjHtuwWDMvOLReFQ6ZPwx7lwYdy4KwLhXemeWy1VsG3O7BPAzp2ZFYkxcuAwMm8hwtwzccDmGywSCy0icA7lJr4kNl4BjonPK8Byj0j0xwF4VyL9T63Mz7xIV2KmHu_WwWw979XCvHu7Xw4N6-KIehmOpxxvixA2B4oZIcUOouCFWaIMnb1bVpX7z0qB56aJxCcqocQk3LzmHd-Qq3i3fZ6uoa17qqrBXD_cMbLWtNUw9wiJr-Gjl_-iwhlZEY5JxZe3bFslUOt8loTXM_yFgZZsIdk4Yga-86wLc_w2bMnNC" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.11 DC-050-570_Load_Project_Plan_(Forecast) — DC-050-570_Load_Project_Plan_(Forecast)

**Swim Lanes**: BU Analyst · Corp. FP&A Analyst | **Tasks**: 18 | **Gateways**: 10

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
    subgraph BU Analyst
        n1["fa:fa-user Adjust Forecast and Categorize into Auth, Commits, Spends, OCOS"]
        n2["fa:fa-user Capture Variance Explanation"]
        n3["fa:fa-user Review CAPEX Plan with Leadership"]
        n4["fa:fa-user Transfer to Capital Target at Cube level"]
        n5["fa:fa-user Make finalized forecast to Central Finance"]
        n13[["fa:fa-cog Load Baseline Data from S/4 at Tool Level or Project Level and Forecast Spends"]]
        n14[["fa:fa-cog Load Baseline Data from ECA at Tool Level or Project Level and Forecast Spends"]]
        n19(["fa:fa-play Load Project Plan Initiated"])
        n20(["fa:fa-stop Load Project Plan Completed"])
        n23{{"fa:fa-code-branch CAPEX or OPEX?"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n25{{"fa:fa-code-branch Approved?"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Corp. FP&A Analyst
        n6["fa:fa-user Capture the Project Plan Assumptions for IF"]
        n7["fa:fa-user Capture the Project Plan Assumptions for IP"]
        n8["fa:fa-user Ensure Burden Rates are Updated"]
        n9["fa:fa-user Size the Project Plan According to the Assumptions for Products"]
        n10["fa:fa-user Size the Project Plan According to the Assumptions for Non -Products"]
        n11["fa:fa-user Update the Project Plan – HC and GSD spend Based on PLC Milestone by Project..."]
        n12["fa:fa-user Add to Collections"]
        n15[["fa:fa-cog Load WBS/Project MD Hierarchy and Cost Center MD Hierarchy from MDG into SAC"]]
        n16[["fa:fa-cog Load WBS/Project MD Hierarchy and Cost Center MD Hierarchy from MDG into SAC"]]
        n17[["fa:fa-cog Ensure the IF Related 3 Years Actuals are Available"]]
        n18[["fa:fa-cog Ensure the IP Related Years Years Actuals are Available"]]
        n21(["fa:fa-stop Added to Collections"])
        n22(["fa:fa-stop Project Plan Rejected"])
        n26{{"fa:fa-code-branch IP or IF?"}}
        n27{{"fa:fa-code-branch exclusiveGateway"}}
        n28{{"fa:fa-code-branch Approved?"}}
        n31{{"fa:fa-arrows-alt parallelGateway"}}
        n32{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n19 --> n23
    n24 --> n1
    n1 --> n2
    n2 --> n5
    n3 --> n25
    n25 -->|"Yes"| n4
    n4 --> n20
    n25 -->|"No"| n24
    n23 -->|"OPEX"| n26
    n26 -->|"IF"| n15
    n26 -->|"IP"| n16
    n15 --> n6
    n16 --> n7
    n6 --> n17
    n7 --> n18
    n18 --> n27
    n27 --> n8
    n17 --> n27
    n8 --> n31
    n31 --> n9
    n31 --> n10
    n9 --> n32
    n10 --> n32
    n32 --> n11
    n11 --> n28
    n12 --> n21
    n28 -->|"No"| n22
    n28 -->|"Yes"| n12
    n29 --> n13
    n23 -->|"CAPEX"| n29
    n29 --> n14
    n13 --> n30
    n14 --> n30
    n30 --> n24
    n5 --> n3
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
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 serviceTask
    class n18 serviceTask
    class n19 startEvt
    class n20 endEvt
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq9WG1v2zYQ_iuEiswbYKd6tWx_2CDLVhsgaY06XVc0-0BLlK1GFgWKcuKl_u87SpRsKTLQZsXyITGfu3uOvDfSeVJ8GhBlolxcPEVJxCfoqcc3ZEt6E9Rb4Yz0-qgE_sQswquYZD2hE9KEL6N_CjXNTB-FmsA8vI3ivUCXZE0J-njVRw4Yxn2U4SQbZIRFYa_fS1m0xWzv0pgyof2KjEI1LLxJ0ZSygLCjgqramm-BaRwl5AgbtmmbnrDLiE-ToEEaWuEo9HsHsbmYPvgbzHix_TwjN_jxUxTwDaxDHGcEdDZ8G1_jFYnFGTnLBebnbFcFI8qEnwQCtkyxHyVrwE0VIIaT-yNkqYcDOlxc3CW1U3Q7u0sQ_PgxzrIZCVHGAZ7vOAqjOJ68Ml3Hs9R-xhm9J5NX-tyeGXrfFyeZwNHVvgju4IFE6w2frGgcSNXBgzjDRE8f--xxoqt9toffLV8kCY6e3KE-0ke1p6mtuZpbeQrD8D95griyW5zdS19zw9O9We1Ls4aWqz7nq445M21Ha8eJsF3kkxNSz_OM-TFU86GlqedJp54xVN0W6Rpz8oD3R8Kxa9aEnmV7mn2WsPTX3mW-WjDqV4TG3PKsmtCeap6jnyU0Hc0cyR0Cz5rhdIOmH5GT4Hif8VIgfhLty50S4kmIByLOyAm-5hlHHmXEx_ABJwFy4WRryqAzUZRwipycb_rIpdttxLM-WqZQC_D3vft-eaf8fcKtN7ldnPKcEVR0feITNH9MY5xgHtGkaWg0DT-QXUQekOss5n-hBZigh4hv0DXB0M3ZJkqb1mbT-hY6KQvhA2wdthBxHKNbzNYETseRm68IismOxE0Sq0lyg-8JZALCB2EIUFjFR3CShDPg9EAKp2rSaMaXmsina3RNcYCmMAPFxEEzzDEKGd2i5WtT7OaW0hjOBbtBlCFI_1ficwmIVNR5KYMOvhrOzO9zNnedn-Bs_GvtDNK4L71VLEWWrmD4R1A8AZj-dloX6tE04zTtMIXqSmPSYWo8PR2PGJDBCrLrb2RtwDHew98_7pTD4dTI7DYij36cZ9GOvCl7t21mdZs5acrojgTP3IyP-pgx-pANcMxRiqE6YhJ3OzHUHzOCTLTa2qUsvUTe4heno72H3S0It28z3k6W5dtUdGImihtdec06tl_Ks2jyjJo88yQTNNMc7uUEfYDDZggD8DENZN2c2I6btuKp0LEB34dLHi5N0ZpC2t4RaAe5z7NWn6o_hfwdTdDgjIfWpC2P-NzHXa6rmoHeukUPvlnOUCbar-jjAAH_4tpFNxE8mjiFrl7tK_PLy8uWR70924NiXlEoLL_Yc0vf6hgfn6bL19X-bmbobUQYZv5mX94MFKaDmH9iQp4KizFzM3tTXhhLx20Pj-H_58puupIlJ-J-5cHVEotCQwb6TDDLIMM8h5dbUYTODkexeJ62GUfnGRc1Y8n3_ay61hqKkC7SkbDGNNRbNo1K-kDE5-cjdNg91mDvReM_G2v2y6bn6Memp6G9ZHrqL5yecH2hweB3caFIQDdLQKsUpLwSl0tLLg0prda6JYBvd8pnAkn6Bo8QKZCs1av2qPiOFnp6pagbUiBusFI0rERDKRJT-Zto1GeCRSmoLDSrdFuvh-Xalmu51Kq1LdejSn8kt10p6FKjVrBbCtLAqMJnyPiNW2utCoSMv1EFWFNbgCFDrtUZqVJSb0Jq6JWGPmoFV28LqvRotUTuQzPaeSieFCXNuK1cJU2TdWBUp9LMFmDIY9V5lpkxTl77otiqbzkNWO-GjW7Y7IatbnjYDdvd8KgbHnfDkMtu_Mw5tTMHhfCefFdriszzIuu8aHheZJ8Xjc6LxvW37mbmVPkNuYlqnajeiRrVV8ombHbDVjc87IbtbnjUDY87YajsTljrhvUKVvrKlrAtjgJl8qQU_wdSJkpAQpzHXDn0FZxzutwnvjIp_l-i5MVLaRZheO9uS_DwLyVDuss=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.12 DC-050-580_Validate_Plan — DC-050-580_Validate_Plan

**Swim Lanes**: Analyst · Capital Analyst | **Tasks**: 14 | **Gateways**: 7

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
    subgraph Analyst
        n7["fa:fa-user Access OPEX Forecast/Plan Resource Requirement and $ Amounts by HC, GSD,..."]
        n8["fa:fa-user Refresh Sizing Data in Evergreen Forecast"]
        n9["fa:fa-user Perform CoC Variance, Incorporate Variance Explanations"]
        n10["fa:fa-user Perform WIF Analysis and make Adjustment to Existing Forecast"]
        n11["fa:fa-user Submit OPEX POR for Leadership Approval"]
        n12["fa:fa-user Review and Validate Project TPF"]
        n13["fa:fa-user Trigger Snapshot Approval Process"]
        n14["fa:fa-user Lock Forecast"]
        n17(["fa:fa-stop Validate Plan Process Completed for OPEX"])
        n18["Multi-year Forecast Completed"]
        n22{{"fa:fa-code-branch Did Product Requirements Change or are there Affordability Constraints?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch OPEX POR Approved by Leadership?"}}
        n25{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Capital Analyst
        n1["fa:fa-user Access CAPEX POR (Forecast/Plan) by CPA Authorized, Committed and Spend $..."]
        n2["fa:fa-user Perform CoC Variance and Incorporate Variance Explanations"]
        n3["fa:fa-user Perform WIF Analysis and make Adjustment to Existing Forecast"]
        n4["fa:fa-user Submit CAPEX POR for Leadership Approval"]
        n5["fa:fa-user Review and Validate Project TPF Through CPA Cycle Submission"]
        n6["fa:fa-user Lock Forecast"]
        n15(["fa:fa-play Validate Plan Process Initiated"])
        n16(["fa:fa-stop Validate Plan Process Completed for CAPEX"])
        n19{{"fa:fa-code-branch CAPEX or OPEX?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-code-branch CAPEX POR Approved by Leadership?"}}
    end
    n15 --> n19
    n19 -->|"CAPEX"| n1
    n1 --> n20
    n20 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n21
    n21 -->|"Yes"| n6
    n6 --> n16
    n21 -->|"No"| n20
    n19 -->|"OPEX"| n7
    n7 --> n22
    n22 -->|"Yes"| n23
    n8 --> n9
    n23 --> n8
    n9 --> n10
    n10 --> n11
    n11 --> n12
    n12 --> n24
    n18 --> n25
    n25 --> n13
    n14 --> n17
    n13 --> n14
    n24 -->|"No"| n23
    n24 -->|"Yes"| n25
    n22 -->|"No"| n18
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
    class n15 startEvt
    class n16 endEvt
    class n17 endEvt
    class n18 startEvt
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq1V12TmzYU_Ssa0h0nMzhFfBivH9phsUl3ZtN44m3STrcPMgijLAYqCe-6G__3SiCwYXGbpFM_MNZBOufeI90LPGlhHmFtpl1cPJGM8Bl4GvEEb_FoBkZrxPBIBzXwAVGC1ilmIzknzjO-In9V06BdPMppEgvQlqR7ia7wJsfgl2sdeGJhqgOGMjZmmJJ4pI8KSraI7v08zamc_QJPYyOu1NStq5xGmB4nGIYLQ0csTUmGj7Dl2q4dyHUMh3kWdUhjJ57G4eggg0vzhzBBlFfhlwy_RY8fScQTMY5RyrCYk_BteoPWOJU5clpKLCzprjGDMKmTCcNWBQpJthG4bQiIouz-CDnG4QAOFxd3WSsKbud3GRC_MEWMzXEMGBfwYsdBTNJ09sL2vcAxdMZpfo9nL8yFO7dMPZSZzETqhi7NHT9gskn4bJ2nkZo6fpA5zMziUaePM9PQ6V5ce1o4i45K_sScmtNW6cqFPvQbpTiO_5OS8JXeInavtBZWYAbzVgs6E8c3nvM1ac5t14N9nzDdkRCfkAZBYC2OVi0mDjTOk14F1sTwe6QbxPED2h8JL327JQwcN4DuWcJarx9luV7SPGwIrYUTOC2hewUDzzxLaHvQnqoIBc-GoiIBXobSPeM1Kn-Z-_udFqNZjMbSZOCFIWYMvFsufgVBTnGIGP9-maIMvMcsL2mIxZ8_S0JF6WYcoCwC3wFvm5cZZ2C9Bz_5OnizmuuvX7--0_440Zl2dd7jmGKWAFHs4nSDOeIIkAwsdphuKMZZK95lueyyLDGNc7oFfu6DqpFkoSiu6yzMaZFTsRstChaPhcgCcZJnrMsJjWHSj9eB8ouwKtEtusfAiz6VjFfJ81ywEsZlAsPhQtilXpXrLeG1u8t374HQATcYiYbEElIAryhovkNpj8TsW7cj-KGK6ANKSSTTFKfkEw5FP1gGvcVWd_EtJZuNjCRDBUty3mpKCrn1veV2d_lNHt6fy9V92c5lPC9OgpPHR9GLrdoWKeY4qpKXTgiaV6c88qS8LVNOxnuMaKt2XNnVNc2np0ZXPnTGa9E2wwTMSSRFo1LYcnJkRQQJyjYYCHVEMRAPIXH1YhFNhNYkJXwvlDJRVYiI2T_eaYfDqZo1rIYfw7RkZIff1D2gv8weXtaehHobhCuiho4n4pm687Xqokf3WoCPCsLFfj9vBXCwFfheE-PLTkN4JUP1lx7wSp7kVDy0I13ukTjgcnfl8VwVWPaHZ73A_PcqrtZ_ZSFb_1sd24NlfHTmi-rY-aoyBrcJzctNUlns78MU17KMicS7xJMvr1HnWKPCxf2ZGr0Wb2wE1ZXWKc3JN5R45VKf6HL4HNeOqr7w7PAb31Z68J-0vqj22iISBoLx-AeZQANcSuDznabS_Cyg5lY9tXmZEX8U0IzroaWGVj201dCuh44aKl2zITeh0v0Ns0p1om5MVICT_sSf82peG04b-bsmcFfdcZVWG6jZ0zKbmKf1zMYMU-UwVeNLFUsrqRyArUXKI9hIQWWK2dgAlYTZGGE2O9DEAJVTsAkfqihgw2HaPQus_o02MaefsloCpydvZnJrmzfSDmwOw9YwbA_DzjA8GYbdYXg6DF8Ow2JfhvEzecIzicIzmcIzqYpqar5XuvhEfVt0UXcQnZ7huGxex7tbZAzDcBg2h2FrGLaHYaeBNV3bYrpFJNJmT1r1-Ss-kSMcI_G6ox10DZU8X-2zUJtVn4laWcjuOidIPLq3NXj4G1Sr0Ug=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.13 DC-050-590_Copy_Plan_Version — DC-050-590_Copy_Plan_Version

**Swim Lanes**: Analyst · Corp. FP&A Analyst | **Tasks**: 11 | **Gateways**: 7

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
    subgraph Analyst
        n1["fa:fa-user Access Existing Plan Data"]
        n2["fa:fa-user Copy Exiting Plan Data"]
        n3["fa:fa-user Create an Empty Version"]
        n4["fa:fa-user Copy Only the Data that is Visible Based on the Current Story and Page Filters"]
        n5["fa:fa-user Change the Filter Values for the New Version"]
        n6["fa:fa-user Hard Lock the Forecasted Data and Create a Public Version"]
        n7["fa:fa-user Soft Lock the Forecasted Data and Create a Private/shared Version"]
        n12(["fa:fa-play Copy Plan Version Initiated"])
        n13(["fa:fa-stop Copy Plan Version Completed"])
        n15{{"fa:fa-code-branch Hard Lock Creation Required?"}}
        n16{{"fa:fa-code-branch CAPEX or OPEX?"}}
        n17{{"fa:fa-code-branch Unlock and Edit Required?"}}
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Corp. FP&A Analyst
        n8["fa:fa-user Add the Initial Project Plan as per PLC Material Requirements and Headcount..."]
        n9["fa:fa-user Update the Required Comments"]
        n10["fa:fa-user Identify Deltas through Actuals vs POR Forecast Spend and HC Comparison"]
        n11["fa:fa-user Update the Status Field for WIP or Approved or Archived"]
        n14(["fa:fa-stop Copy Plan Version Completed"])
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-code-branch Approved?"}}
    end
    n12 --> n16
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n19
    n15 -->|"Yes"| n6
    n16 -->|"CAPEX"| n1
    n7 --> n17
    n15 -->|"No"| n7
    n6 --> n18
    n18 --> n13
    n19 --> n15
    n17 -->|"Yes"| n19
    n17 -->|"No"| n18
    n20 --> n8
    n8 --> n9
    n9 --> n10
    n10 --> n11
    n11 --> n21
    n21 -->|"No"| n20
    n21 -->|"Yes"| n14
    n16 -->|"OPEX"| n20
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
    class n12 startEvt
    class n13 endEvt
    class n14 endEvt
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1FzozYQ_isablK3M3YKGIzth3YcbHqZyV08516unaYPMghbjYyoJJy4Of_3rgDZgSOd9uqHBH3a_b7VarWIZyvmCbGm1sXFM82omqLnntqSHelNUW-NJen1UQXcYUHxmhHZ0zYpz9SK_lWaOV7-pM00FuEdZQeNrsiGE_Txuo9m4Mj6SOJMDiQRNO31e7mgOywOIWdcaOs3ZJzaaalWT11xkRBxNrDtwIl9cGU0I2d4GHiBF2k_SWKeJQ3S1E_Hadw76uAYf4y3WKgy_EKSd_jpE03UFsYpZpKAzVbt2A1eE6bXqEShsbgQe5MMKrVOBglb5Tim2QZwzwZI4OzhDPn28YiOFxf32UkU3Xy4zxD8YoalnJMUSQXwYq9QShmbvvHCWeTbfakEfyDTN-4imA_dfqxXMoWl232d3MEjoZutmq45S2rTwaNew9TNn_riaerafXGAvy0tkiVnpXDkjt3xSekqcEInNEppmv4vJcir-BnLh1prMYzcaH7ScvyRH9pf8pllzr1g5rTzRMSexuQFaRRFw8U5VYuR79ivk15Fw5Edtkg3WJFHfDgTTkLvRBj5QeQErxJWeu0oi_VS8NgQDhd-5J8IgysnmrmvEnozxxvXEQLPRuB8i2YZZgepKlT_Mue3eyvF0xQPdJLRLI6JlGjxRKWCskNLhjM0xwrfW7-_8HKbXiHPD9rnn1yGLRdBIFsITBe7XB3QHRGS8qzp43XI3GbsgKB1lBLwgBWiEt1RSaGLoCvoLQniWWkRFkKQTKGV4uIAUgla4g1BEWUK1JpSfktqizMw1SyVObrDrCASpVyU6Hvy2B3zqEn0FosE3fD4oeLigsRYKoixDF_HZDKBlsWa0bibNWiyrniq_i2roHt4-l5CwwCDTnbH_fbEnzOo4DLT5UbW9ugaujgFngQ8v3vpOjy7SsXzDteQ73JGOlz952fjql8XgzU0vHj7ImXlIjTFB_JnQSH8H--t4_ElxaibIpwtF78g2Kpb-P-FU9Dt9DFjWlRnb5FQ9brouNufPMWskHRPfqr6QNtt8l_doMG2zm_IRX6JouU3s46jPG4d5SQpq6PaOQaFwP8gsar2BkuUg83yJkTvQFa_Ss16d3BkZJmFtwQnMS8ydXl52SyYSVPqY57oYtNqJml610umVqXZTc_rBGxoekBzwhQEpbaCFxtoVLEq4PWJ9hItbz-cKhytckhKFVxYFhZcH-QX5ey8Gt5KYVVIONOEJeVZ_nS91HUyy3PB97p1wLOIt7AdSYvU--pCd-2vKhjX6XYzsf7YUSlwlNFg8IM-GQaoxm49rKeH9XBYDb166FVDvx76NdfEcJXA53vrVwL7-hmanZkY1RPlwSun6jduFtQcQZvjPS_tDD6q7cbGblwDJlRnUgMmOidoRXOOM2hqnEhdu-Iw41rD-BkF2_DU5o5ZjGOyaQDXaSqZq8t54hSc187VrUlV476jd8zcdxqw2w0Pu2GvG_a74VE3HHTD42540g1DErvxV9YJFWxusU18WN84m6jXifrmMtaER91w0A2Pu-FJJwyl1Qk7Brb61o6IHaaJNX22yo8f-EBKSIoLpqxj38KF4qtDFlvT8iPBKsq2NacYev-uAo9_A6kuMAw=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.14 DC-050-600_Reload_Cost_Plan — DC-050-600_Reload_Cost_Plan

**Swim Lanes**: BU Analyst · Corp. FP&A Analyst | **Tasks**: 8 | **Gateways**: 7

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
    subgraph BU Analyst
        n1["fa:fa-user Access Existing Plan Data"]
        n2["fa:fa-user Review Actualized and forecasted spends"]
        n3["fa:fa-user Input Judgement to Reconcile Spends, Auth, Commits as Part of TPF"]
        n4["fa:fa-user Reload Adjusted Plan"]
        n9(["fa:fa-play Reload Cost Plan Initiated"])
        n10(["fa:fa-stop Plan Reloaded"])
        n12{{"fa:fa-code-branch Review Successful?"}}
        n13{{"fa:fa-code-branch CAPEX or OPEX?"}}
        n14{{"fa:fa-code-branch Approved?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
        n16{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Corp. FP&A Analyst
        n5["fa:fa-user Revise the Forecast by Adding New Project Plan, Edit Existing Project Plan..."]
        n6["fa:fa-user Add Required Comments for the Plan Changes"]
        n7["fa:fa-user Update the Status Field for WIP or Archived"]
        n8["fa:fa-user Reports to Summarize and Compare the Current Version vs Snapshot Versions..."]
        n11(["fa:fa-stop Plan Reloaded"])
        n17{{"fa:fa-code-branch exclusiveGateway"}}
        n18{{"fa:fa-code-branch Approved?"}}
    end
    n9 --> n13
    n1 --> n2
    n2 --> n12
    n13 -->|"CAPEX"| n16
    n3 --> n14
    n12 -->|"Yes"| n15
    n14 -->|"Yes"| n4
    n15 --> n3
    n14 -->|"No"| n15
    n4 --> n10
    n17 --> n5
    n5 --> n6
    n6 --> n7
    n7 --> n8
    n8 --> n18
    n18 -->|"Yes"| n11
    n18 -->|"No"| n17
    n13 -->|"OPEX"| n17
    n16 --> n1
    n12 -->|"No"| n16
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 startEvt
    class n10 endEvt
    class n11 endEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVm1v2zYQ_iuEgswbIAd6tRR92KDI1pCha426aTfM-0BLlM1GFjWScuy6_u8l9WZLVoB184cE9_Ce547HO1JHJSIxUjzl9vaIM8w9cBzxDdqikQdGK8jQSAUV8BFSDFcpYiPpk5CML_CX0k238r10k1gItzg9SHSB1gSBp0cV-IKYqoDBjI0ZojgZqaOc4i2kh4CkhErvG-QmWlJGq5ceCI0RPTtomqNHtqCmOENn2HQsxwolj6GIZHFHNLETN4lGJ5lcSl6iDaS8TL9g6He4_4RjvhF2AlOGhM-Gb9M3cIVSuUdOC4lFBd01xcBMxslEwRY5jHC2FrilCYjC7PkM2drpBE63t8usDQrevF9mQPyiFDI2RQlgXMCzHQcJTlPvxgr80NZUxil5Rt6NMXOmpqFGciee2LqmyuKOXxBeb7i3Imlcu45f5B48I9-rdO8ZmkoP4m8vFsric6RgYriG20Z6cPRAD5pISZL8r0iirvQDZM91rJkZGuG0jaXbEzvQrvWabU4tx9f7dUJ0hyN0IRqGoTk7l2o2sXXtddGH0JxoQU90DTl6gYez4H1gtYKh7YS686pgFa-fZbGaUxI1gubMDu1W0HnQQ994VdDydcutMxQ6awrzDXh4An4G0wPj1YL8ZfpfSyWBXgLHss7AjyLEGJjtMeOi88A8hRmYQg6Xyt8XLKPLeo92GL0IMi9gKiY4BjCLQUIoiiDjwmS56BfW1TC7Go9ZXnDwWxGvxcWQccCJkBXTF-EUgUXJF2Nf8I0KArLdYs4AZGAuB4Ek4MM87Kpb_QxTAmPgx5-LMiG5ry7h_seWkafiHGtGQBivqvAorjIsDjkWvJ8uK6idmYyTvPKu6NfOxvHYOMtbcrwScx5tmgouirL-SZH-slROp0uiOUwM_PnsD0AoeCf-X5GsYZKf55TsUHzlbw_7o32UFgzv0K9Vk_dpk--lidPsNWdAaH4HwvkP_kCT2tftxhAQTwgI6x4Dq4M43Fi27FtRRzE4n1FUHZwKZjHmFy19sXZ3d9ftgklvHOJYRPunwBTFZduJzmSyscvg5UEHG5itUa-3na7MUx6LCpScBYe8YCDEKC0nBHx6nMvj82m0EZWKuzpuf-M5oSIBMRuLYiteNDFr5aiJ1HJIqwhBQakcoI-IMkwysGNgkcGcbUiLsat96_r3NLHz39rE_dfd2PZHdg_G459l-9e2XtlGbRr1cmPrpgS-LpVyLpbKV9md9ZpZ-1qNr1H7_imPT3razYrVW2kpdqVh9h3fkq6CVcfSGkenApr1WqdJbVKZTm3Wzm5turVYY-tuP3G9v9Lk4_Tr8q4tS7tUB9f7ZWk0JhcPkzyA5kHuwMYwbA7D1jBsD8OTYdgZht1h-L79POpuR6s_ZbqoPogazSvfhc1h2BqG7WF4Mgw7w7DbwIqqbBHdQhwr3lEpv6rFl3eMElikXDmpCiw4WRyySPHKr0-lKO-iKYbi3t1W4OkbtdWp9g==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.15 DC-050-610_Define_a_Budget — DC-050-610_Define_a_Budget

**Swim Lanes**: Capital Analyst | **Tasks**: 3 | **Gateways**: 4

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
    subgraph Capital Analyst
        n1["fa:fa-user Allocate Project Budget - Overall"]
        n2["fa:fa-user Allocate Budget by calendar year"]
        n3["fa:fa-user Validate the Budget Amount"]
        n4["Distribute Project budget to account assignment WBS"]
        n5["Distribute IM Program Position Budget to Projects/WBS"]
        n6{{"fa:fa-code-branch Overall Budget Distribution Required?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8{{"fa:fa-code-branch Any Update Required?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n6 -->|"Yes"| n1
    n1 --> n7
    n2 --> n7
    n7 --> n3
    n3 --> n8
    n8 -->|"No"| n4
    n5 --> n9
    n9 --> n6
    n6 -->|"No"| n2
    n8 -->|"Yes"| n9
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVduu4jYU_RUrR0e8BDVXEvLQUQikGqlzUZmLqtIHx3HAPY5DbYdDhuHfa5MECAMPo-YBZa_stdbeG18OBqpybETG8_OBMCIjcBjJDS7xKAKjDAo8MkELfIGcwIxiMdI5RcXkknw7pdnedq_TNJbCktBGo0u8rjD4_NYEsSJSEwjIxFhgToqROdpyUkLeJBWtuM5-wmFhFSe37tOs4jnmlwTLCmzkKyolDF9gN_ACL9U8gVHF8oFo4RdhgUZHXRytXtEGcnkqvxb4Hdx_JbncqLiAVGCVs5El_R1mmOoeJa81hmq-64dBhPZhamDLLUSErRXuWQrikL1cIN86HsHx-XnFzqbg03zFgHoQhULMcQGEVPBiJ0FBKI2evCROfcsUklcvOHpyFsHcdUykO4lU65aphzt-xWS9kVFW0bxLHb_qHiJnuzf5PnIskzfq98YLs_zilEyc0AnPTrPATuykdyqK4n85qbnyT1C8dF4LN3XS-dnL9id-Yv2o17c594LYvp0T5juC8JVomqbu4jKqxcS3rceis9SdWMmN6BpK_Aqbi-A08c6CqR-kdvBQsPW7rbLOPvIK9YLuwk_9s2Aws9PYeSjoxbYXdhUqnTWH2w1I4JZISEHMIG2EbL_qh9l_rYwCRgUc62GDmNIKqXaA8v8HIwlmdb7GEozBhx3mkNKV8fcV23nA7lhZAxCkWG8j0GDIh2R3SP4CKck1WZ0PvUBcVjWTQ5qnaHOi2idZfVVo1jJkBSBCmgXUMMmalVi9fp0thyL-UOTtO62jZlWCj5UgklSsL0EJdhbilx9kJodD34M--MaZ2rpo08-qlzgbadk_8L814Th_szKOxyup4L4U3iNaC7LDv7WL7IYV3mfFrAGft6dpPvKb_qyf-hvbFzYB4_Gv31fGn1isjO9qDXW4rXHVSRc6wzBoQ7cL3TYMuzDsNN9XJ0mvg_02a9qF0zac3BTSkZwbrb6-6dX20lX2x8oAdu7D7n3YO5-4A9i_D0_6I2KABnfR8C467VHDNErMS0hyIzoYp6tUXbc5LmBNpXE0DVjLatkwZESnK8eoT8tgTqBe3S14_A9_1HJ6" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.16 DC-050-620_Release_a_Budget — DC-050-620_Release_a_Budget

**Swim Lanes**: Capital Analyst | **Tasks**: 3 | **Gateways**: 4

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
    subgraph Capital Analyst
        n1["fa:fa-user Determine Budget Cap for Partial Budget Release"]
        n2["fa:fa-user Release Budget based on budget Cap"]
        n3["fa:fa-user Update Budget Cap"]
        n4["Display Available Budget"]
        n5["Distribute Project budget to account assignment WBS"]
        n6{{"fa:fa-code-branch Update Required?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8{{"fa:fa-code-branch Release Budget Required?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n5 --> n8
    n2 --> n6
    n1 --> n7
    n6 -->|"No"| n9
    n6 -->|"Yes"| n3
    n7 --> n2
    n3 --> n7
    n8 -->|"Yes"| n1
    n9 --> n4
    n8 -->|"No"| n9
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
    class n6 gateway
    class n7 gateway
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P2jgU_StWRiNegpRPwuShKwhktdLuqirtVquyD8a5BneMw9oOA6X899okgUmWeVg1D1HuybnnXF_52ieHlAU4qfP4eGKC6RSdBnoDWxikaLDCCgYuqoG_sGR4xUENLIeWQi_YtwvNj3YHS7NYjreMHy26gHUJ6NNvLpqYRO4ihYUaKpCMDtzBTrItlses5KW07AcYU49e3Jpf01IWIG8Ez0t8EptUzgTc4DCJkii3eQpIKYqOKI3pmJLB2RbHyxeywVJfyq8U_IEPn1mhNyammCswnI3e8t_xCrhdo5aVxUgl920zmLI-wjRsscOEibXBI89AEovnGxR75zM6Pz4uxdUUfZwtBTIP4VipGVCktIHne40o4zx9iLJJHnuu0rJ8hvQhmCezMHCJXUlqlu65trnDF2DrjU5XJS8a6vDFriENdgdXHtLAc-XRvHteIIqbUzYKxsH46jRN_MzPWidK6U85mb7Kj1g9N17zMA_y2dXLj0dx5v1Xr13mLEomfr9PIPeMwCvRPM_D-a1V81Hse2-LTvNw5GU90TXW8IKPN8GnLLoK5nGS-8mbgrVfv8pq9V6WpBUM53EeXwWTqZ9PgjcFo4kfjZsKjc5a4t0GZXjHNOZoIjA_Kl3_tY_wvywdilOKh7bZaAYa5NaMBJpWxRq0zUS0lOi92V9m7lr4A3Aw47x0_nmlFXS1Gk6bYse_QKVAq6tyNz3spn_aFaavr-rosiPDnjG146bxkz1m3J4mDbvLjGumlmxVGUHT2a9AdFuGLhEmpKyERqb7bC22YD4_TxddkdHp1FZnj7jhygwp2bRFfoB_Kyah-GXpnM-vspL7WXAgvFJsD7_WO6eXNb6f1evnW55P_9fTzHP9IWI0HL4z_k0Y1OGoCf06TJpwZMPvS-fPcul8N7Y9-G9QFzxs8KTODpow7IqNe1nN3Iqnmhb1aF3Py9zY-trzogMH9-HwPhxdj9IOHN-HR-3sd9DkLjq-iz61qOM6WzN6mBVOenIud6S5RwuguOLaObsOrnS5OAripJe7xKkuW2_GsBnxbQ2efwCrcGOn" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.17 DC-050-630_Display_Available_Budget — DC-050-630_Display_Available_Budget

**Swim Lanes**: Capital Analyst | **Tasks**: 1 | **Gateways**: 0

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
    subgraph Capital Analyst
        n1["fa:fa-user Run Budget Availability Report"]
        n2["Run Periodic reports"]
        n3["AVAC is set"]
        n4["Execute the Project (Post Transactions)"]
    end
    n4 --> n3
    n1 --> n2
    n3 --> n1
    class n1 userTask
    class n2 startEvt
    class n3 startEvt
    class n4 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVMuK2zAU_RXhIbgFB_yMUy8KjmNDoYVhMm0XTReKLCXqyJKR5Dwa8u-V8nAmaWdVL4zv0bnn6F5fae8gUWMncwaDPeVUZ2Dv6hVusJsBdwEVdj1wAr5BSeGCYeVaDhFcz-jvIy2I262lWayCDWU7i87wUmDw9ZMHcpPIPKAgV0OFJSWu57aSNlDuCsGEtOwHPCY-ObqdlyZC1lheCb6fBigxqYxyfIWjNE7jyuYpjASvb0RJQsYEuQe7OSY2aAWlPm6_U_gL3H6ntV6ZmECmsOGsdMM-wwVmtkYtO4uhTq4vzaDK-nDTsFkLEeVLg8e-gSTkL1co8Q8HcBgM5rw3Bc_TOQfmQQwqNcUEKG3gcq0BoYxlD3GRV4nvKS3FC84ewjKdRqGHbCWZKd33bHOHG0yXK50tBKvP1OHG1pCF7daT2yz0Pbkz7zsvzOurUzEKx-G4d5qkQREUFydCyH85mb7KZ6hezl5lVIXVtPcKklFS-H_rXcqcxmke3PcJyzVF-JVoVVVReW1VOUoC_23RSRWN_OJOdAk13sDdVfBDEfeCVZJWQfqm4Mnvfpfd4lEKdBGMyqRKesF0ElR5-KZgnAfx-LxDo7OUsF2BArZUQwZyDtlO6dOqfXjwY-4QmBE4tM0GTx0Hk65eYg3yNaQMLiijegeecCuknjs_X6WGJtXyH80hFDVFQB5J6pYVGVb-LS8AVab7dxKxWSy3GHUaA3MtAFP1L4w0ePcolJlycxAURJoKrt73iWb8Th88BsPhR-NwDoNTGJ7D6BS-ngDLuczUDRz2B-gGjv4Nxz3seE6DZQNp7WR753ixmcuvxgR2TDsHz4GdFrMdR052vACcrq3NsEwpNP-lOYGHP2FYqoY=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.18 DC-050-660_Process_month-end_adjustments — DC-050-660_Process_month-end_adjustments

**Swim Lanes**: Finance Analyst | **Tasks**: 3 | **Gateways**: 0

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
    subgraph Finance Analyst
        n1["fa:fa-user Execute Journal Entries"]
        n2["fa:fa-user Execute Reassignment of Cost"]
        n3["fa:fa-user Execute Overhead Allocations"]
        n4["Manage Project Periodic Settlement"]
        n5["Execute the Project (Post Transactions)"]
    end
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n5 --> n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVNuO2jAQ_RUrK0QrBSlXQvNQCQKRWrXqqmzbh9IH44zBXWMj2-FSxL_X5hIWyj41D1HmZM45M6Oxdx6RFXi512rtmGAmR7u2mcMC2jlqT7GGto-OwHesGJ5y0G2XQ6UwY_bnkBYmy41Lc1iJF4xvHTqGmQT07YOP-pbIfaSx0B0NitG2314qtsBqW0gulct-gB4N6MHt9GsgVQXqkhAEWUhSS-VMwAWOsyRLSsfTQKSorkRpSnuUtPeuOC7XZI6VOZRfa_iMNz9YZeY2pphrsDlzs-Cf8BS469Go2mGkVqvzMJh2PsIObLzEhImZxZPAQgqL5wuUBvs92rdaE9GYoqfhRCD7EI61HgJF2lh4tDKIMs7zh6Tol2nga6PkM-QP0SgbxpFPXCe5bT3w3XA7a2Czucmnklen1M7a9ZBHy42vNnkU-Gpr3zdeIKqLU9GNelGvcRpkYREWZydK6X852bmqJ6yfT16juIzKYeMVpt20CP7VO7c5TLJ-eDsnUCtG4IVoWZbx6DKqUTcNg9dFB2XcDYob0Rk2sMbbi-C7ImkEyzQrw-xVwaPfbZX19FFJchaMR2mZNoLZICz70auCST9MeqcKrc5M4eUclUxgQQD1BeZbbY5_3SPCnxOP4pzijhs2Gm2A1AbQR1krm4tGwigGeuL9esGJ7nO-gi2fzcQChEGSokJapytifJ_4ZQVqDrhCfc4lwYZJceOYWOJnLPAMkB3MbyAGPdqjLytG0BiM4eBMrzmp5Zwd7JXTEN882rrQkz1kGpOD19uGaFf7-CFC1Om8t62ewugYxqcwPobJKUyP4ctlcwrn9b2Co_twfB9OmpN9BacN7PneAtQCs8rLd97harXXbwUU19x4e9_DtZHjrSBefriCvHpZ2XUdMmw3Y3EE938BlnTVng==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.19 DC-050-670_Release_WBS — DC-050-670_Release_WBS

**Swim Lanes**: Boundary Apps · Capital Finance Project Analyst | **Tasks**: 2 | **Gateways**: 8

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
        n2[["fa:fa-cog Initiate 'WBS Element Release' Automatically"]]
        n3["WBS not Released"]
        n4["Execute the Project (Post Transactions)"]
        n5["WBS Released for Commitment and Actuals"]
        n6["AUC Created Automatically in Background"]
        n7["Validate Project Structure"]
        n8{{"fa:fa-code-branch CAPEX?"}}
        n9{{"fa:fa-code-branch Project Budgeted?"}}
        n10{{"fa:fa-code-branch exclusiveGateway"}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
        n12{{"fa:fa-code-branch EMS"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch CAPEX or OPEX?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Capital Finance Project Analyst
        n1["fa:fa-user Initiate 'WBS Element Release' Manually"]
    end
    n7 --> n10
    n8 -->|"Yes"| n9
    n9 -->|"Yes"| n11
    n9 -->|"No"| n3
    n10 --> n12
    n8 -->|"No"| n11
    n12 -->|"No"| n1
    n13 --> n8
    n1 --> n13
    n11 --> n5
    n5 --> n14
    n15 --> n4
    n6 --> n15
    n3 --> n10
    n14 -->|"CAPEX"| n6
    n14 -->|"OPEX"| n15
    n12 -->|"Yes"| n2
    n2 --> n13
    class n1 userTask
    class n2 serviceTask
    class n3 startEvt
    class n4 startEvt
    class n5 startEvt
    class n6 startEvt
    class n7 startEvt
    class n8 gateway
    class n9 gateway
    class n10 gateway
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVm2PozYQ_isWq1VaiUi8hiwfWhEWqpNue6vLvbS63AfHmMRdYyLb7CbN5b_XJkACZVv1ygckPzPzPDNjj-FooDLDRmjc3h4JIzIEx4nc4gJPQjBZQ4EnJjgDnyAncE2xmGifvGRySf6s3Wxvt9duGkthQehBo0u8KTH4-MYEkQqkJhCQianAnOQTc7LjpID8EJe05Nr7Bs9zK6_VGtOi5BnmFwfLCmzkq1BKGL7AbuAFXqrjBEYly3qkuZ_PczQ56eRo-YK2kMs6_UrgB7j_TDK5VescUoGVz1YW9C1cY6prlLzSGKr4c9sMIrQOUw1b7iAibKNwz1IQh-zpAvnW6QROt7cr1omCt-9XDKgHUSjEPc6BkApOniXICaXhjRdHqW-ZQvLyCYc3ThLcu46JdCWhKt0ydXOnL5hstjJclzRrXKcvuobQ2e1Nvg8dy-QH9R5oYZZdlOKZM3fmndIisGM7bpXyPP9fSqqv_AMUT41W4qZOet9p2f7Mj62_87Vl3ntBZA_7hPkzQfiKNE1TN7m0Kpn5tvU66SJ1Z1Y8IN1AiV_g4UJ4F3sdYeoHqR28SnjWG2ZZrR95iVpCN_FTvyMMFnYaOa8SepHtzZsMFc-Gw90WLMqqPssg2u3E2aYf5nz5sjJyGOZwisoNeKNGlqhiwOTzYgkSquaUSfAeU6xHF0SVLAsoCYKUHlbG169XTK4i0kGs7AIy5XLl4SmPZI9RpfjVFQBUhX9gJMEPj6WQ4IM69AIiSUomfuwH-g11SwvykoO4LAoi6_wgy0CEZKXGrh84U4HRxxjEHKuisn7-gDCwgOhpw3Vv-oGBCvwEKcl0L9o8l2qElQrHfd_58XhpYYana1UI2oI4ekx--3llnE5Xvnfjvq3Coso2WCU6DLOt8Ti8R7QS5Bn_cj6AwzD7-8Kc8bDkYTn0dL9PwPuHlgG1t-9GWmf7_1VLXVODKYjhjkhIQUqYir3sbMQgPQh5rdaNhb6C_m0uHiCrmpEYSLMATKc_6R1s1nO9_rYyfsfqrH5TJ6LB7wa4bQ8Mv5Y17jawbTXEzoC48evibWdgaHH3TDBv1w1fJ9AAfrP2G7vX2hugXc8ae-vvDgq3vSaPepfrVGZD07vW0rF02bd9act1-unWN6cuov1i9GDn-trvWdzuw9mDvXHYH4dn43AwDs_bz0UPvRtF1S6PwvY47IzD7jjsjcN-CxumUWBeQJIZ4dGof9rUj12Gc1hRaZxMA6rrdHlgyAjrnxuj2un78p5ANW3FGTz9Bf0mJ30=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.20 DC-050-690_Validate_Project_Reports — DC-050-690_Validate_Project_Reports

**Swim Lanes**: Capital Analyst | **Tasks**: 1 | **Gateways**: 2

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
    subgraph Capital Analyst
        n1["fa:fa-user Validate Project Reports"]
        n2["Obtain Acceptance for Project Closure"]
        n3["Execute the Project (Post Transactions)"]
        n4["Manage CAPEX Reporting"]
        n5["Run Periodic reports"]
        n6["Run Periodic reports (if needed)"]
        n7{{"fa:fa-code-branch Close Project?"}}
        n8{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n7
    n4 --> n8
    n8 --> n1
    n5 --> n8
    n6 --> n8
    n7 -->|"Yes"| n2
    n7 -->|"No"| n3
    class n1 userTask
    class n2 startEvt
    class n3 startEvt
    class n4 startEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P4jYU_StWRiO2UpDySdI8bMUEUlXqtqOd7e5WSx8ujg3uGDuynQHK8t9r8xEmlHlqHiLu8T3n3HuxnZ2HZU28wru_3zHBTIF2A7MkKzIo0GAOmgx8dAQ-g2Iw50QPXA6Vwjyxfw5pYdJsXJrDKlgxvnXoE1lIgv74xUdjS-Q-0iD0UBPF6MAfNIqtQG1LyaVy2XckpwE9uJ2WHqSqibokBEEW4tRSORPkAsdZkiWV42mCpah7ojSlOcWDvSuOyzVegjKH8ltNPsDmC6vN0sYUuCY2Z2lW_FeYE-56NKp1GG7Vy3kYTDsfYQf21ABmYmHxJLCQAvF8gdJgv0f7-_uZ6EzRp8lMIPtgDlpPCEXaWHj6YhBlnBd3STmu0sDXRslnUtxF02wSRz52nRS29cB3wx2uCVssTTGXvD6lDteuhyJqNr7aFFHgq619X3kRUV-cylGUR3nn9JCFZVienSil_8vJzlV9Av188prGVVRNOq8wHaVl8F-9c5uTJBuH13Mi6oVh8kq0qqp4ehnVdJSGwduiD1U8Csor0QUYsobtRfDHMukEqzSrwuxNwaPfdZXt_FFJfBaMp2mVdoLZQ1iNozcFk3GY5KcKrc5CQbNEJTTMAEdjAXyrzXHVPSL8NvMoFBSGbtjoM3BW23aQ9f-bYIM-kkYqo2feX69IkSX9PjfABBpjTBoDAhNEpepoJZe6VaRPiy1tuiG4tfr2EuiS3z1Kbfe03fYasGFS6B_6xMQSP4CABUHl-HH69VSVPR_9vNTmfWwFerTXgqwZRupW9aM3stA7RpEgpCb1lX-2252n5O634dyWipeHJrsufpp5-_0rTn7hgFJyrYfADWpAAeeE_3zcMheOPVTHHyJEw-F763kKk2OYn8L8GJ72tUj7q6N-mLnw-8z7k9gRfLf_2xX-mzzA8avt5_zPx64HR90d04Pj23ByG05vw6PbcHY-WT00P6Oe762IWgGrvWLnHb4q9stTEwotN97e96A18mkrsFccbl-vbdzWnjCwh2J1BPf_AhInIdI=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.21 DC-050-700_Supplement_Budget — DC-050-700_Supplement_Budget

**Swim Lanes**: Capital Finance Project Analyst · Corporate Capital Finance Analyst · Finance Analyst | **Tasks**: 5 | **Gateways**: 7

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
    subgraph Capital Finance Project Analyst
        n5["fa:fa-user Assign Supplement Budget to Lower Level WBS Element"]
    end
    subgraph Corporate Capital Finance Analyst
        n1["fa:fa-user Allocate Supplemental Budget from Program to Item"]
        n2["fa:fa-user Transfer Supplemental Budget from Item to Project"]
        n3["fa:fa-user Allocate Budget Supplemental by Year"]
        n6["Release a Budget"]
        n7["Execute the Project (Post Transactions)"]
        n8["Workflow project for approval"]
        n9{{"fa:fa-code-branch Yearly Budget Allocation Required?"}}
        n10{{"fa:fa-code-branch Budget Release Required?"}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
        n12{{"fa:fa-code-branch Supplement Budget Required for Lower level WBS Element?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Finance Analyst
        n4["fa:fa-user Approve Workflow for Small Construction"]
        n14{{"fa:fa-code-branch Supplement Budget Require for Small Construction ?"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n8 --> n1
    n1 --> n2
    n2 --> n9
    n9 -->|"Yes"| n3
    n10 -->|"Yes"| n6
    n10 -->|"No"| n7
    n11 --> n12
    n3 --> n11
    n9 -->|"No"| n11
    n13 --> n10
    n12 -->|"Yes"| n14
    n5 --> n13
    n12 -->|"No"| n13
    n15 --> n5
    n14 -->|"Yes"| n4
    n4 --> n15
    n14 -->|"No"| n15
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
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2P4jYU_StWRiNaKUj5JJCHVsCQaqXZajVsd7Ra-mASB9wxdmo7fJTlv9fOF5MQHrblYTT3-N5zzr22k5yNmCXICI3HxzOmWIbgPJBbtEODEAzWUKCBCUrgC-QYrgkSA52TMiqX-J8izfayo07TWAR3mJw0ukQbhsAfH0wwVYXEBAJSMRSI43RgDjKOd5Cf5owwrrMf0Di10kKtWpoxniB-TbCswI59VUowRVfYDbzAi3SdQDGjSYs09dNxGg8u2hxhh3gLuSzs5wJ9hMdXnMitilNIBFI5W7kjz3CNiO5R8lxjcc739TCw0DpUDWyZwRjTjcI9S0Ec0rcr5FuXC7g8Pq5oIwqeX1YUqF9MoBBPKAVCKnixlyDFhIQP3nwa-ZYpJGdvKHxwFsGT65ix7iRUrVumHu7wgPBmK8M1I0mVOjzoHkInO5r8GDqWyU_qb0cL0eSqNB85Y2fcKM0Ce27Pa6U0Tf-Xkpor_wzFW6W1cCMnemq0bH_kz61bvrrNJy-Y2t05Ib7HMXpHGkWRu7iOajHybes-6SxyR9a8Q7qBEh3g6Uo4mXsNYeQHkR3cJSz1ui7z9SfO4prQXfiR3xAGMzuaOncJvantjSuHimfDYbYFc5hhCQmIMIU0RkCx_4ViCaYUkpOQZbb-Uf_bykhhmMKhHj6YCoE3FCzzLCPq1lIJZnmyQRJIBp7ZQWU8oz0i4HW2BIsyY2X8WfKpc9K1wXjGuJrWjaFbI3bHCCEs1pVXK6q8MpNyttM9KZWddvZBol1jo2Bz2myf1RUTqfrnLpum0FTVpNps7h1vFUGLdH0CXxHkbYKRInhBBKknIoBVWTsjUBmLI4pzRasemM2O_fSJCVn6h7HEjIqf24VjVfjK-Jt-WICsqkoZBzBT0R6SdvrkfK570Y_u4Voxx9vCMjnVDVUNKjXwgv7OMUfJryvjcnm_XVY_UcVQN3u33O4vR8eY5ALv0W_lHeuWOf1lt-e1Fi5GUZ5c0j25N6bcHzV1e-TvH3Cvc4iK7UGg2TttdLmDhKhrQ9Vtz4vtbu-e7f1g_3dYwU3r_n9unY7BcPiLoqhCuwydKnTKcFKFEx1-XxlfkVgZ39XVqquszsKou_A7K_CgxisduxZyq9juKFV1DW7XiVYNOB1p26tW_CrT7WbWnM1ClenXsdehrBm9ivEmsWb0370a9CzrV2ILdvphtx_2-mG_Hx413xYtOOiHx_3wpH5Htrux-mG7H3b6Ybcf9vphv4YN09ghvoM4McKzUXyTqu_WBKUwJ9K4mAbMJVueaGyExbebkWeJqnzCUL9lSvDyL-_Rfgc=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.22 DC-050-720_Run_Periodic_reports_(if_needed) — DC-050-720_Run_Periodic_reports_(if_needed)

**Swim Lanes**: Capital Analyst | **Tasks**: 6 | **Gateways**: 3

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
    subgraph Capital Analyst
        n1["fa:fa-user Execute Adhoc Project Structure Reports"]
        n2["fa:fa-user Execute Adhoc Project Line Item Reports"]
        n3["fa:fa-user Execute Adhoc Project Commitment Line Items Report"]
        n4["fa:fa-user Execute Adhoc Summary Reports for Budget, Spends and Commitments"]
        n5["fa:fa-user Execute Adhoc Settlement Report"]
        n6["fa:fa-user Execute Adhoc Summary Reports for Spend and Commitments (F)"]
        n7(["fa:fa-play CAPEX and OPEX Reporting Started"])
        n8(["fa:fa-stop Project Structure Report Validated"])
        n9(["fa:fa-stop Line item Report Validated"])
        n10(["fa:fa-stop Summary information Validated"])
        n11(["fa:fa-stop Commitment Line Item Report Validated"])
        n12(["fa:fa-stop Settlement Report Validated"])
        n13{{"fa:fa-code-branch CAPEX?"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n15{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n1 --> n8
    n2 --> n9
    n6 --> n14
    n7 --> n15
    n14 --> n10
    n4 --> n14
    n15 --> n5
    n3 --> n11
    n15 --> n13
    n15 --> n3
    n15 --> n2
    n15 --> n1
    n5 --> n12
    n13 -->|"Yes"| n4
    n13 -->|"No"| n6
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 startEvt
    class n8 endEvt
    class n9 endEvt
    class n10 endEvt
    class n11 endEvt
    class n12 endEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVm2v2jYY_StWrq5opSDFeSHcfNgEgUyV2q0abbdp7INJHPCu40S2c4FR_nvtvBBIQ9dp-YB4jp9znuPHjp2TEecJNgLj8fFEGJEBOI3kDmd4FIDRBgk8MkENfEKcoA3FYqRz0pzJFfmnSoNucdBpGotQRuhRoyu8zTH4-MYEM0WkJhCIibHAnKQjc1RwkiF-DHOac539gKeplVbVmqF5zhPMuwTL8mHsKSolDHew47u-G2mewHHOkhvR1EunaTw6a3M038c7xGVlvxT4HTr8RhK5U3GKqMAqZycz-hZtMNVzlLzUWFzyl7YZROg6TDVsVaCYsK3CXUtBHLHnDvKs8xmcHx_X7FIUfFisGVBPTJEQC5wCIRW8fJEgJZQGD244izzLFJLnzzh4sJf-wrHNWM8kUFO3TN3c8R6T7U4Gm5wmTep4r-cQ2MXB5IfAtkx-VL-9WpglXaVwYk_t6aXS3IchDNtKaZr-r0qqr_wDEs9NraUT2dHiUgt6Ey-0vtZrp7lw_Rns9wnzFxLjK9Eoipxl16rlxIPWfdF55EyssCe6RRLv0bETfArdi2Dk-RH07wrW9fouy817nsetoLP0Iu8i6M9hNLPvCroz6E4bh0pny1GxAyEqiEQUzBiiRyHrUf0w-OfaSFGQorFuNlgecFxKDGbJTtVXJv7GsQQrtXtjWXIMfsVFzqVYG39dadjfo_FWvWfgjcTZsIbzPRphnmVEZphdyYlG71bO_Zbcqsz0kdAaAWnOwbxMtliaYFWo7S0AYslVtZ5X75viWEqKK49Dxib_1VhlqO8HvIpe3-r6ry7CBVV7MZy9X_5e0X7Rf2pFdaCotVQnBU4U-_UVfdrRhcyLuysPPiFKEvS1wFNPoFof0i33XSK0esy2CYSp6WdIkpzdJ8MeeWiH_KsDu--gv4T3qc7p1FL1zTfeqLM73tXd_3FtnM_Xye5wMj7EtBTkBf9UnyN9mtfREOf5XowRlao991hqv9R_GATj8Q9qcZvQrsOnJpzUIXSb2G9ir2W7DdAcT8ztEaBXAy3BacZhbxw6PaAf231CE7fhZbyq8Hlt_IHVK_lZOeoP_JxX-OTqQNVtaC-SG9gehp1h2B2GvWF4Mgz7l4v6Bp42d-oN-DQEQmsQhYOoPYg67X11C7vDsNfChmlkWL2PJDGCk1F9w6nvvASnqKTSOJsGKmW-OrLYCKpvHaMs9BuzIEhdQVkNnr8A0o4zDw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.23 DC-050-740_Obtain_Acceptance_for_Project_Closure — DC-050-740_Obtain_Acceptance_for_Project_Closure

**Swim Lanes**: Capital Analyst | **Tasks**: 2 | **Gateways**: 3

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
    subgraph Capital Analyst
        n1["Trigger Decision Point 'Close Project' in PPM item by Requestor"]
        n2["Obtain Acceptance for Closure of the Project"]
        n3(["fa:fa-play Acceptance for Project Closure Initiated"])
        n4(["fa:fa-stop Acceptance for Project Closure Obtained"])
        n5(["fa:fa-stop Sent Back to Requestor"])
        n6["Workflow Triggered to Cube Owner for Approval of Closure of Project"]
        n7["Workflow Triggered to Central Capital Finance for Approval of Closure of Project"]
        n8{{"fa:fa-code-branch Approved by Cube Owner?"}}
        n9{{"fa:fa-code-branch Approved by Cube Owner?"}}
        n10{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n2 --> n4
    n3 --> n1
    n1 --> n6
    n6 --> n8
    n7 --> n9
    n8 -->|"Yes"| n7
    n8 -->|"No"| n10
    n9 -->|"Yes"| n2
    n9 -->|"No"| n10
    n10 --> n5
    class n3 startEvt
    class n4 endEvt
    class n5 endEvt
    class n6 startEvt
    class n7 startEvt
    class n8 gateway
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2v4jYQ_StWrq7SSkFKQkIgD60gkGqlbnu13HZVlT4YxwGXYKe2w8ey_PeOSfjKcrVabR4QczxzzsyJPDlYRGTUiq3n5wPjTMfoYOslXVM7RvYcK2o7qAb-xJLheUGVbXJywfWUfTqleUG5M2kGS_GaFXuDTulCUPTHOwcNobBwkMJcdRSVLLcdu5RsjeU-EYWQJvuJ9nM3P6k1RyMhMyqvCa4beSSE0oJxeoW7URAFqalTlAie3ZHmYd7PiX00zRViS5ZY6lP7laLv8e4jy_QS4hwXikLOUq-LX_GcFmZGLSuDkUpuzmYwZXQ4GDYtMWF8AXjgAiQxX12h0D0e0fH5ecYvouh1POMIHlJgpcY0R0oDPNlolLOiiJ-CZJiGrqO0FCsaP_mTaNz1HWImiWF01zHmdraULZY6nosia1I7WzND7Jc7R-5i33XkHn5bWpRnV6Wk5_f9_kVpFHmJl5yV8jz_LiXwVb5itWq0Jt3UT8cXLS_shYn7Jd95zHEQDb22T1RuGKE3pGmadidXqya90HPfJh2l3Z6btEgXWNMt3l8JB0lwIUzDKPWiNwlrvXaX1fxFCnIm7E7CNLwQRiMvHfpvEgZDL-g3HQLPQuJyiRJcMo0LNOS42Ctdn5qHe3_PrFfJFgsq0ZgSppjg6EUwrpGdFEJRBJ38S4m2EYODl_eIabpG8z36QP-rqNJCzqx_bgh9IPx9rjFkDwmhpcacUJQLiQxdJSkSOYIVcOa9r-7-AOU5jnPcKQuwtEXR1Fyo3sGOYeB-Biw_3tAEVxrosPwaTd3vFyxhi2VKwZURJiukxd34t0U9qPko5MpcVtQ4SzNTkVRzkNpycNo0MSxLKTbwUsCPG2se2hK9TQo9SSA5v-GU8cuY36LQPxzOs5oV3pnDEiLLhgKk4IVf-_95Zh2PN8WD7yn23MfVdEeKSrEN_aW-XtcyWED1H-6jTucneN1N2K3D5tJzrw57Tdirw34TRnU4aMK-CT_PrL-omlmf4biF_yZOsNfcVT5o5fstvJ3vubVeeHPXTcfnzX0HB82SvQPDR2DvMUH0GO6fd9UdOniIQsMNbDnWmso1ZpkVH6zT5xs-8RnNcVVo6-hYuNJiuufEik-fOasqM6gcMwzbZ12Dx_8B3gyW0Q==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.24 DC-050-780_Reduce_Budget — DC-050-780_Reduce_Budget

**Swim Lanes**: Corporate Capital Finance Analyst | **Tasks**: 3 | **Gateways**: 3

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
    subgraph Corporate Capital Finance Analyst
        n1["fa:fa-user Return Budget to Level 1 WBS Element"]
        n2["fa:fa-user Return Budget from Item to Program"]
        n3[["fa:fa-cog Transfer Budget Return from Project to Item"]]
        n4(["fa:fa-stop Budget Return not Required"])
        n5["Manage IM Program Position Budget (PPM Portfolio and Buckets)"]
        n6["Execute the Project (Post Transactions)"]
        n7{{"fa:fa-code-branch Budget Return Required?"}}
        n8{{"fa:fa-code-branch Budget Allocated below Level 1 WBS Element?"}}
        n9{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n6 --> n7
    n7 -->|"Yes"| n8
    n8 -->|"Yes"| n1
    n1 --> n3
    n3 --> n9
    n7 -->|"No"| n4
    n9 --> n2
    n2 --> n5
    n8 -->|"No"| n9
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 endEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqllVuP4jYYhv-KldGIWSlIORLIRSsIpBppZzUq066qpRfGscEdY1Pb4VCW_16bhAApszfNBYrffO_zHYidg4NEgZ3UeXw8UE51Cg4dvcQr3ElBZw4V7rigEn6HksI5w6pjY4jgekr_OYX50Xpnw6yWwxVle6tO8UJg8NuzC4bGyFygIFddhSUlHbezlnQF5T4TTEgb_YD7xCOnbPWjkZAFlpcAz0t8FBsroxxf5DCJkii3PoWR4MUNlMSkT1DnaItjYouWUOpT-aXCL3D3lRZ6adYEMoVNzFKv2Gc4x8z2qGVpNVTKzXkYVNk83AxsuoaI8oXRI89IEvL3ixR7xyM4Pj7OeJMUvI1nHJgLMajUGBOgtJEnGw0IZSx9iLJhHnuu0lK84_QhmCTjMHCR7SQ1rXuuHW53i-liqdO5YEUd2t3aHtJgvXPlLg08V-7NbysX5sUlU9YL-kG_yTRK_MzPzpkIIf8rk5mrfIPqvc41CfMgHze5_LgXZ95_eec2x1Ey9NtzwnJDEb6C5nkeTi6jmvRi3_sYOsrDnpe1oAuo8RbuL8BBFjXAPE5yP_kQWOVrV1nOX6VAZ2A4ifO4ASYjPx8GHwKjoR_16woNZyHhegkyIddCmjJBBtdUQwZyyiFHGAw5ZHulq3h7cf_bzCEwJbBrxw9-xbqUHIzKYoE10AJ8xhvMgA--jqZgwsxW5nrm_HkFCH4EIFKswLPGK4syTZr6Vrf28FvjR2IB3sxuUMRwakCNO3GM_y-MTlVZpOFcg6KnBqS0WLcAXNjbv0sqcWGMn66MsfG9QA4XGDy_nIsEr0JRTUXTydPrq3kopCaCUQEgL8wT9I61-nTbUM_gJjuMSjN-c_Y1VT8Zoq76g8iS28bkcLhMosDduQlFy1Yf5x5-njnH45W5_0PzkDGBzPtQAHM-ie29P7UNHNwH4h1ipaIb_Eu1Cy4uc05UN7wHut2fTD_1MrHL7zPnD6xmzndTaq33W3q9eblf2cN6GVbLQYv2RZxMUS0PqqigXgbVMm6lqk2Dqw1o850Pnhs5uC-H14fKzZOoPipvxLg5q2_k3n05OR8uN2r_rjo4q47rrLBcQVo46cE5fW7NJ7nABJZMO0fXgaUW0z1HTnr6LDnlujDOMYX2Ra_E479gH31D" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.25 DC-050-790_Transfer_Budget — DC-050-790_Transfer_Budget

**Swim Lanes**: Capital Analyst · Corporate Capital Finance Analyst | **Tasks**: 6 | **Gateways**: 3

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
    subgraph Capital Analyst
        n1["fa:fa-user Maintain List of Workflow Approvers"]
        n2["fa:fa-user Release Budget Transfer Request to Workflow"]
        n9["Run Periodic reports"]
        n12{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Corporate Capital Finance Analyst
        n3[["fa:fa-cog Return Sender Project Budget to Item"]]
        n4[["fa:fa-cog Allocate Budget from Program to Receiver Item"]]
        n5[["fa:fa-cog Return Budget from Sender Item to Program"]]
        n6[["fa:fa-cog Transfer Supplement Budget from Item to Project"]]
        n7(["fa:fa-stop Budget Transfer Rejected"])
        n8["Execute the Project (Post Transactions)"]
        n10{{"fa:fa-code-branch Budget Transfer Approved?"}}
        n11{{"fa:fa-code-branch Additional Information Required?"}}
    end
    n5 --> n4
    n4 --> n6
    n3 --> n5
    n10 -->|"Yes"| n3
    n6 --> n8
    n10 -->|"No"| n11
    n11 -->|"No"| n7
    n12 --> n2
    n1 --> n12
    n2 --> n10
    n11 -->|"Yes"| n12
    n9 --> n1
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 endEvt
    class n8 startEvt
    class n9 startEvt
    class n10 gateway
    class n11 gateway
    class n12 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVm2P4jYQ_itWVivupCAlISFsPrQCllQr7VWr5Xqn09IPJnHAXWOntsNCOf57x-QFksKnIoE0z8w8z8x44nCwEpESK7Lu7w-UUx2hQ0-vyYb0ItRbYkV6NiqBb1hSvGRE9UxMJrie039OYa6f70yYwWK8oWxv0DlZCYL-eLLRGBKZjRTmqq-IpFnP7uWSbrDcTwUT0kTfkVHmZCe1yjURMiXyHOA4oZsEkMooJ2d4EPqhH5s8RRLB0xZpFmSjLOkdTXFMfCRrLPWp_EKRL3j3naZ6DXaGmSIQs9Yb9oyXhJketSwMlhRyWw-DKqPDYWDzHCeUrwD3HYAk5u9nKHCOR3S8v1_wRhQ9vy44gk_CsFKPJENKAzzbapRRxqI7fzqOA8dWWop3Et15s_Bx4NmJ6SSC1h3bDLf_QehqraOlYGkV2v8wPURevrPlLvIcW-7ht6NFeHpWmg69kTdqlCahO3WntVKWZf9LCeYqv2L1XmnNBrEXPzZabjAMps5_-eo2H_1w7HbnROSWJuSCNI7jwew8qtkwcJ3bpJN4MHSmHdIV1uQD78-ED1O_IYyDMHbDm4SlXrfKYvkiRVITDmZBHDSE4cSNx95NQn_s-qOqQuBZSZyv0RTnVGOGxhyzvdKl13y4-7awMhxluG-Gjb5gyjV80TNVGokMfRfy3ewdGue5FFsi1cL68yLfa-e_EkbgMUeTIl0Rjb7CKqvshP9dEGDUomFs8zwAz2vB0Qs80SKlCZIkF1J31FzvcKj1zE3TX4JAskZkl7BC0S35rTyKhXU8lmmwrN1ZCAnMENdMJaYcWMiV6Qze3s5yK-hCF5KjOZBCT3BEf5FE171Ca0-abKDgy4r9NsOYMZEY7Sopk2JjiKC0jWF4JQmBNuQ1quBqMZdEVWEm15BVvB2aYZumOaJ5kecMbmauW5wXZKbbDln4qSFTWuRXzt0kkRTSPl-kjSBrtiNJAZOA10Ezyk8vQlXZONFUcPW5swDO9QXo6lbbmv563oQy372eP05TavRgG554JuQGG-u0tlS2aJqF4gHq93-BE65MvzSHlTkozaAyXcfYPxfWDwI7_RP8lWNYxo26cb-LU5jr1g637Qhr3CsJvNouTbe2K7frdHnqQprIhyry4jIydPUl3IK96_Dg8oJtefybnuCmZ3jTE1YvoRY4at6CLfjhOgyDru7tNuxeh70atmxrQ2A_aGpFB-v0Xwb-76QkwwXT1tG2cKHFfM8TKzq9860iTyHzkWLzLJbg8V_pQ-xb" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 27</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Capital Analyst | DC-050-110_Perform_Implementation_Audit, DC-050-120_Close_Project, DC-050-340_Workflow_project_for_approval, DC-050-350_Distribute_Project_budget_to_account_assignment_WBS, DC-050-410_Simulate_Depreciation, DC-050-520_Form_Core_Project_Team, DC-050-530_Assign_Resources_to_Tasks, DC-050-580_Validate_Plan, DC-050-610_Define_a_Budget, DC-050-620_Release_a_Budget, DC-050-630_Display_Available_Budget, DC-050-690_Validate_Project_Reports, DC-050-720_Run_Periodic_reports_(if_needed), DC-050-740_Obtain_Acceptance_for_Project_Closure, DC-050-790_Transfer_Budget | |
| Batch User | DC-050-120_Close_Project,  | |
| CCF Analyst | DC-050-120_Close_Project,  | |
| CES / Intel Products Capital Finance | DC-050-120_Close_Project, DC-050-410_Simulate_Depreciation, DC-050-520_Form_Core_Project_Team, DC-050-530_Assign_Resources_to_Tasks,  | |
| Capital Enterprise Solutions (CES) Analyst | DC-050-120_Close_Project,  | |
| Capital Finance Analyst | DC-050-120_Close_Project,  | |
| Finance Analyst | DC-050-120_Close_Project, DC-050-660_Process_month-end_adjustments, DC-050-700_Supplement_Budget,  | |
| Capital Central Finance Analyst | DC-050-300_Manage_IM_Program_Positions_(PPM_Portfolio_and_Buckets), DC-050-310_Manage_IM_Program_Position_Budget_(PPM_Portfolio_and_Buckets), DC-050-520_Form_Core_Project_Team,  | |
| BU Analyst | DC-050-560_Determine_Total_Planned_Project_Costs, DC-050-570_Load_Project_Plan_(Forecast), DC-050-600_Reload_Cost_Plan,  | |
| Corp. FP&A Analyst | DC-050-560_Determine_Total_Planned_Project_Costs, DC-050-570_Load_Project_Plan_(Forecast), DC-050-590_Copy_Plan_Version, DC-050-600_Reload_Cost_Plan,  | |
| Analyst | DC-050-580_Validate_Plan, DC-050-590_Copy_Plan_Version,  | |
| Boundary Apps | DC-050-670_Release_WBS,  | |
| Capital Finance Project Analyst | DC-050-670_Release_WBS, DC-050-700_Supplement_Budget,  | |
| Corporate Capital Finance Analyst | DC-050-700_Supplement_Budget, DC-050-780_Reduce_Budget, DC-050-790_Transfer_Budget | |

<div class="page-footer"><span>Page 28</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for DC-050. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 29</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
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
| FPRR1514_IP | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  |  | 03.Medium |
| FPRR1514_IF | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  |  | 04.Low |
| FPRR1240 | Report | Custom report for Revenue Recognition by Stage for Product/Services Sale​ act... | 10. Object Complete |  |  | 03.Medium |
| FPRR1211 | Report | Report for searching on and viewing government contract timesheets for Intel ... | 10. Object Complete |  |  | 03.Medium |
| FPRR1210 | Report | Report for searching on and viewing government contract timesheet changes for... | 10. Object Complete |  |  | 03.Medium |
| FPRR0907_IP | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  |  | 03.Medium |
| FPRR0907_IF | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  |  | 04.Low |
| FPRR0497 | Report | CFR - Report to support multiple Treasury Funding requests from Multiple Inte... | 10. Object Complete |  |  | 03.Medium |
| FPRR0496 | Report | TPR-Report to support multiple Treasury Payment Requests from Multiple Intel ... | 10. Object Complete |  |  | 03.Medium |
| FPRR0461 | Report | Inter-company Outage Pre-consolidate Report (ACDOCA) | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0380 | Report | GL Interface – Reconciliation Report/Dashboard | 10. Object Complete | NA | NA | 02.High |
| FPRR0327_IP | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA | NA | 02.High |
| FPRR0327_IF | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0288_IP | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0288_IF | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA | NA | 03.Medium |
| FPRR0288_CFIN | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA | NA | 02.High |
| FPRR0027 | Report | In House Cash – Loan Account balance Detailed report | 10. Object Complete | NA | NA | 01.Very High |
| FPRM003 | Conversion | Revenue Recognition Rules | 10. Object Complete |  |  | N/A |
| FPRM002 | Conversion | Revenue Contracts | 10. Object Complete |  |  | N/A |
| FPRM001 | Conversion | Bank Master | 10. Object Complete | ECC | CFIN | N/A |
| FPRC1724_IP | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  |  | 02.High |
| FPRC1724_IF | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  |  | 03.Medium |
| FPRC1565 | Conversion | Convert active delegate relationships for Timesheet approval | 10. Object Complete |  |  | 02.High |
| FPRC1493 | Conversion | Conversion of WIP values as per Component structure in S/4 - IP | 10. Object Complete |  |  | 02.High |
| FPRC1491 | Conversion | Conversion of WIP values as per Component structure in S/4 - Back End IF | 10. Object Complete |  |  | 02.High |
| FPRC1464_IP | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  |  | 02.High |
| FPRC1464_IF | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  |  | 02.High |
| FPRC1442 | Conversion | Conversion of Actual Labor hours for Intel Federal Projects | 10. Object Complete |  |  | 02.High |
| FPRC1441 | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete |  |  | 02.High |
| FPRC1212 | Conversion | Project Actuals Conversion including Intel Federal | 10. Object Complete |  |  | 03.Medium |
| FPRC0908_IP | Conversion | Project Budget Conversion | 10. Object Complete |  |  | 03.Medium |
| FPRC0908_IF | Conversion | Project Budget Conversion | 10. Object Complete |  |  | 03.Medium |
| FPRC0196_IP | Conversion | Asset Transaction data conversion | 10. Object Complete | NA | NA | 02.High |
| FPRC0196_IF | Conversion | Asset Transaction data conversion | 10. Object Complete | NA | NA | 02.High |
| FPRC0195_IP | Conversion | Asset Master data conversion | 10. Object Complete | NA | NA | 03.Medium |
| FPRC0195_IF | Conversion | Asset Master data conversion | 10. Object Complete | NA | NA | 03.Medium |
| FPRC0174_IP | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC | S4 | 02.High |
| FPRC0174_IF | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC | S4 | 03.Medium |
| FPRC0117 | Conversion | Conversion – In House Cash: Current Account creation and Current Account Bala... | 10. Object Complete | ECC | CFIN | 02.High |
| FPRC0116 | Conversion | Conversion – Migration of Existing Bank Guarantees and Intercompany Loans to ... | 10. Object Complete | Quantum | CFIN | 03.Medium |
| FPRC0035_IP | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  | MDG | 03.Medium |
| FPRC0035_IF | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  | MDG | 04.Low |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 30</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for DC-050.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for DC-050.

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

<div class="page-footer"><span>Page 31</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| FPRW1449 | Workflow | TPR : Workflow to handle Memo creation and cancellation process | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRW1444 | Workflow | TFR: Workflow to handle Memo creation and cancellation process | 10. Object Complete |  | NA | 03.Medium |
| FPRW1064_IP | Workflow | Custom Workflow will also be created with some predefined process/rules for a... | 10. Object Complete |  | NA | 01.Very High |
| FPRW1064_IF | Workflow | Custom Workflow will also be created with some predefined process/rules for a... | 10. Object Complete |  | NA | 02.High |
| FPRW0930 | Workflow | Workflow for Counterparty Approval | 10. Object Complete |  | NA | 03.Medium |
| FPRW0906_IP | Workflow | Custom workflow: Change Order Create and Change Approval | 10. Object Complete |  | NA | 03.Medium |
| FPRW0906_IF | Workflow | Custom workflow: Change Order Create and Change Approval | 10. Object Complete |  | NA | 03.Medium |
| FPRW0904_IP | Workflow | Custom Workflow - WBS Element Request approval with WBS Element creation | 10. Object Complete |  | NA | 03.Medium |
| FPRW0904_IF | Workflow | Custom Workflow - WBS Element Request approval with WBS Element creation | 10. Object Complete |  | NA | 03.Medium |
| FPRW0900_IP | Workflow | Custom Workflow: Approval for Project creation and create a Project def and l... | 10. Object Complete |  | NA | 03.Medium |
| FPRW0900_IF | Workflow | Custom Workflow: Approval for Project creation and create a Project def and l... | 10. Object Complete |  | NA | 03.Medium |
| FPRW0445_IP | Workflow | Project budget approval workflow (Capex)​ | 10. Object Complete |  | NA | 03.Medium |
| FPRW0445_IF | Workflow | Project budget approval workflow (Capex)​ | 10. Object Complete |  | NA | 03.Medium |
| FPRW0325_IP | Workflow | Custom workflow to manage the approval process in bulk/individual requests | 10. Object Complete | NA → NA | NA | 02.High |
| FPRW0325_IF | Workflow | Custom workflow to manage the approval process in bulk/individual requests | 10. Object Complete | NA → NA | NA | 02.High |
| FPRW0165_IP | Workflow | Workflow is required to trigger the approvers based on the business requireme... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRW0165_IF | Workflow | Workflow is required to trigger the approvers based on the business requireme... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRW0165_CFIN | Workflow | Workflow is required to trigger the approvers based on the business requireme... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR1514_IP | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  | NA | 03.Medium |
| FPRR1514_IF | Report | To generate reports out of the ITT documents that was created | 10. Object Complete |  | NA | 04.Low |
| FPRR1240 | Report | Custom report for Revenue Recognition by Stage for Product/Services Sale​ act... | 10. Object Complete |  | NA | 03.Medium |
| FPRR1211 | Report | Report for searching on and viewing government contract timesheets for Intel ... | 10. Object Complete |  | NA | 03.Medium |
| FPRR1210 | Report | Report for searching on and viewing government contract timesheet changes for... | 10. Object Complete |  | NA | 03.Medium |
| FPRR0907_IP | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  | NA | 03.Medium |
| FPRR0907_IF | Report | Workflow Status Report ( Order Request / Approval Request / Others ) | 10. Object Complete |  | NA | 04.Low |
| FPRR0497 | Report | CFR - Report to support multiple Treasury Funding requests from Multiple Inte... | 10. Object Complete |  | NA | 03.Medium |
| FPRR0496 | Report | TPR-Report to support multiple Treasury Payment Requests from Multiple Intel ... | 10. Object Complete |  | NA | 03.Medium |
| FPRR0461 | Report | Inter-company Outage Pre-consolidate Report (ACDOCA) | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0380 | Report | GL Interface – Reconciliation Report/Dashboard | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR0327_IP | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR0327_IF | Report | Report to display the requests/change IDs and status of the workflow approval... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0288_IP | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0288_IF | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRR0288_CFIN | Report | Operational Report to display whether supporting documents are attached to JEs | 10. Object Complete | NA → NA | NA | 02.High |
| FPRR0027 | Report | In House Cash – Loan Account balance Detailed report | 10. Object Complete | NA → NA | NA | 01.Very High |
| FPRM003 | Conversion | Revenue Recognition Rules | 10. Object Complete |  | NA | N/A |
| FPRM002 | Conversion | Revenue Contracts | 10. Object Complete |  | NA | N/A |
| FPRM001 | Conversion | Bank Master | 10. Object Complete | ECC → CFIN | NA | N/A |
| FPRI1725_IP | Interface | Interface to be developed to transfer the files from Denodo to FS share path ... | 10. Object Complete |  | Intel MW | 03.Medium |
| FPRI1725_IF | Interface | Interface to be developed to transfer the files from Denodo to FS share path ... | 10. Object Complete |  | Intel MW | 04.Low |
| FPRI1704 | Interface | Automated Tool MUP Excess Capacity calculation and associated PCOS/OCOS Split... | 10. Object Complete |  | BODS | 03.Medium |
| FPRI1670 | Interface | Import Dot process/stage details from MDG into S4. ​ | 10. Object Complete |  | NA | 03.Medium |
| FPRI1669 | Interface | Import Xeus/Mars volumes from ECA into S4.​ | 07. FUT Roadblock |  | BODS | 03.Medium |
| FPRI1504 | Interface | Asset Delete from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1503 | Interface | Asset Display from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1502 | Interface | Asset Change from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1463 | Interface | Interface to upload payroll data from Workday to S/4 IP for legal entity 199 ... | 10. Object Complete |  | MULESOFT | 03.Medium |
| FPRI1447 | Interface | GL Interface –Create Inbound IDOCs to CFIN from IF system | 10. Object Complete | IF → CFIN | NA | 03.Medium |
| FPRI1446 | Interface | GL Interface –Create Inbound IDOCs to CFIN from IP system | 10. Object Complete | IP → CFIN | NA | 03.Medium |
| FPRI1439 | Interface | Receive planned production quantities per production version from ECA to S/4 ... | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1338 | Interface | Outbound Interface to view the Cleared Customer Invoices from CFIN System to ... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI1315 | Interface | Asset Create from EMS to S4 through APIGEE | 10. Object Complete |  | APIGEE | 03.Medium |
| FPRI1306 | Interface | Interface for importing GL transactional data from SAP CFIN system into SAP IF | 10. Object Complete | CFIN → S/4 | NA | 03.Medium |
| FPRI1305 | Interface | Interface for importing GL transactional data from SAP CFIN system into SAP IP | 10. Object Complete | CFIN → S/4 | NA | 03.Medium |
| FPRI1288 | Interface | Activity Inbound interface from ECA to S4 IP | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1287 | Interface | Production quantity update in WAC custom table from ECA to S4 IF | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1286_IP | Interface | Interface between SAP IP and IF boxes for Outbound IDOC flow_IP | 10. Object Complete | MULESOFT → S/4 | SFT | 03.Medium |
| FPRI1286_IF | Interface | Interface between SAP IP and IF boxes for Outbound IDOC flow_IF | 10. Object Complete | MULESOFT → S/4 | SFT | 04.Low |
| FPRI1273 | Interface | Activity Quantity Inbound interface from ECA to S4 IF | 10. Object Complete | ECA → S/4 | MuleSoft | 03.Medium |
| FPRI1241 | Interface | Disti Rebate percentage of gross for Unissued Returns and Intransit Deferral | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FPRI1238 | Interface | Pull Foundry WBS from HAT and create in LE 199 in IP S/4 for Foundry Employee... | 10. Object Complete | Head Count Assignment Tool → S/4 | BODS | 03.Medium |
| FPRI1105 | Interface | Interface for automatic creation of B2B customer related payment advice | 10. Object Complete |  | MULESOFT | 03.Medium |
| FPRI0981_IP | Interface | Interface of SAP PPM module to SPEED | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FPRI0981_IF | Interface | Interface of SAP PPM module to SPEED | 10. Object Complete | ECA → S/4 | BODS | 04.Low |
| FPRI0913_IP | Interface | Export the Planning data from the SAC table to PPM standard tables using the ... | 10. Object Complete | SAC → S/4 | NA | 02.High |
| FPRI0913_IF | Interface | Export the Planning data from the SAC table to PPM standard tables using the ... | 10. Object Complete | SAC → S/4 | NA | 03.Medium |
| FPRI0909_IP | Interface | Interface for importing the Headcount details by Person# and WBS element comb... | 10. Object Complete | ECA → S/4 | BODS | 03.Medium |
| FPRI0909_IF | Interface | Interface for importing the Headcount details by Person# and WBS element comb... | 10. Object Complete | ECA → S/4 | BODS | 04.Low |
| FPRI0895 | Interface | Import Tool Sharing Forecasted Data from FCS to S4 & derive FTQ data by Capex... | 10. Object Complete | FCS → S/4 | BODS | 02.High |
| FPRI0894 | Interface | Planned Volume from IP-BY will be utilized as a KP26 quantity to split 'Overh... | 10. Object Complete | ICS → S/4 | BODS | 02.High |
| FPRI0869 | Interface | Interface for automatic creation of WOM related payment advice | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0867 | Interface | Outbound Interface to view the open & Cleared Customer Invoices from CFIN Sys... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0866 | Interface | Interface to Obtains the payer associated to the sold to from CFIN System to ... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0865 | Interface | Interface to transfer the Uploaded WCP Grant Amount from CFIN to WOM and Defe... | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| FPRI0864_IP | Interface | Interface between SAP IP and IF boxes for Inbound IDOC flow_IP | 10. Object Complete | MULESOFT → S/4 | SFT | 03.Medium |
| FPRI0864_IF | Interface | Interface between SAP IP and IF boxes for Inbound IDOC flow_IF | 10. Object Complete | MULESOFT → S/4 | SFT | 04.Low |
| FPRI0863_IP | Interface | Interface between SAP & ECA to provide information for auto certification in ... | 10. Object Complete | ECA → BLACKLINE | APIGEE;DENODO | 03.Medium |
| FPRI0863_IF | Interface | Interface between SAP & ECA to provide information for auto certification in ... | 10. Object Complete | ECA → BLACKLINE | APIGEE;DENODO | 04.Low |
| FPRI0863_CFIN | Interface | Interface between SAP & ECA to provide information for auto certification in ... | 10. Object Complete | ECA → BLACKLINE | APIGEE;DENODO | 03.Medium |
| FPRI0862 | Interface | Interface to transfer the details of selected invoice from WOM to CFIN ( Inbo... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| FPRI0778_IP | Interface | Continue to auto-certify a BL task when the related JE is approved | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 03.Medium |
| FPRI0778_IF | Interface | Continue to auto-certify a BL task when the related JE is approved | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 03.Medium |
| FPRI0778_CFIN | Interface | Continue to auto-certify a BL task when the related JE is approved | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 02.High |
| FPRI0770_IP | Interface | To enable auto-certify a BL [Blackline] task when the related JE is approved | 10. Object Complete | BLACKLINE → ECA | NA | 03.Medium |
| FPRI0770_IF | Interface | To enable auto-certify a BL [Blackline] task when the related JE is approved | 10. Object Complete | BLACKLINE → ECA | NA | 03.Medium |
| FPRI0770_CFIN | Interface | To enable auto-certify a BL [Blackline] task when the related JE is approved | 10. Object Complete | BLACKLINE → ECA | NA | 02.High |
| FPRI0704 | Interface | IF-IP Integration Actual Cost - Inbound Interface | 10. Object Complete | OpenText → S/4 | SFT | 02.High |
| FPRI0703 | Interface | IF-IP Integration Actual Cost - Outbound Interface | 10. Object Complete | S/4 → OpenText | SFT | 02.High |
| FPRI0696_IP | Interface | Interface between ONESOURCE and Readsoft Process Director built on the back o... | 10. Object Complete | ONESOURCE → READSOFT | NA | 02.High |
| FPRI0696_IF | Interface | Interface between ONESOURCE and Readsoft Process Director built on the back o... | 10. Object Complete | ONESOURCE → READSOFT | NA | 03.Medium |
| FPRI0695 | Interface | Reference Interest Rates - S4 converted data from MDG to CFIN | 10. Object Complete | S/4 MDG → CFIN | NA | 03.Medium |
| FPRI0694 | Interface | Exchange Rates N - S4 converted data from MuleSoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0693 | Interface | Exchange Rates L - S4 converted data from MuleSoft to Treasury Suite | 10. Object Complete | Treasury Suite → MULESOFT | MULESOFT | 03.Medium |
| FPRI0600_IP | Interface | Continuation to use Blackline Account Reconciliations Tool (ART), Blackline M... | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 04.Low |
| FPRI0600_IF | Interface | Continuation to use Blackline Account Reconciliations Tool (ART), Blackline M... | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 04.Low |
| FPRI0600_CFIN | Interface | Continuation to use Blackline Account Reconciliations Tool (ART), Blackline M... | 10. Object Complete | BLACKLINE → S/4 | MULESOFT | 03.Medium |
| FPRI0599_IP | Interface | ServiceNow Asset change | 10. Object Complete | SERVICENOW → S/4 | MULESOFT | 03.Medium |
| FPRI0599_IF | Interface | ServiceNow Asset change | 10. Object Complete | SERVICENOW → S/4 | MULESOFT | 04.Low |
| FPRI0598 | Interface | N rate from Mulesoft to MDG | 10. Object Complete | MULESOFT → S/4 MDG | MULESOFT | 04.Low |
| FPRI0597 | Interface | N rate from Mulesoft to Bloomberg | 10. Object Complete | MULESOFT → BLOOMBERG | MULESOFT | 03.Medium |
| FPRI0596 | Interface | N rate from Mulesoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0554 | Interface | SKF Interface to get file from ECA and send to S4 via BODS - IF | 10. Object Complete | ECA → S/4 | MuleSoft | 02.High |
| FPRI0545 | Interface | IF-IP Integration - Interface to send Cost Idoc from S4 If to S4 IP | 10. Object Complete | S/4 → S/4 | SFT | 03.Medium |
| FPRI0544 | Interface | IF-IP Integration - Interface to receive Cost Idoc from S4 If to S4 IP | 10. Object Complete | S/4 → S/4 | SFT | 03.Medium |
| FPRI0533 | Interface | Reference Interest Rates from MuleSoft to S4 MDG | 10. Object Complete | Bloomberg → S/4 MDG | MULESOFT | 03.Medium |
| FPRI0532 | Interface | Request for Reference Interest Rates from MuleSoft to Bloomberg | 10. Object Complete | MULESOFT → BLOOMBERG | MULESOFT | 03.Medium |
| FPRI0531 | Interface | L Rates from MuleSoft to S4 MDG | 10. Object Complete | Bloomberg → S/4 MDG | MULESOFT | 03.Medium |
| FPRI0530 | Interface | Request for L Rates from MuleSoft to Bloomberg | 10. Object Complete | MULESOFT → BLOOMBERG | MULESOFT | 03.Medium |
| FPRI0529 | Interface | L Rates from MuleSoft to Quantum | 10. Object Complete | MULESOFT → QUANTUM | MULESOFT | 03.Medium |
| FPRI0528 | Interface | L Rates from MuleSoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0527 | Interface | Reference Interest Rates from MuleSoft to Quantum | 10. Object Complete | MULESOFT → QUANTUM | MULESOFT | 03.Medium |
| FPRI0526 | Interface | Reference Interest Rates from MuleSoft to Treasury Suite | 10. Object Complete | MULESOFT → TREASURY SUITE | MULESOFT | 03.Medium |
| FPRI0505 | Interface | Interface – Copp Clark Holiday Calendar Integration with SAP | 10. Object Complete | Copp Clark → S/4 | SFT | 03.Medium |
| FPRI0379 | Interface | GL Interface – File processing in MuleSoft-Payroll | 10. Object Complete | PAYROLL → S/4 | MULESOFT | 02.High |
| FPRI0378_IP | Interface | GL Interface - SAP API IP | 10. Object Complete | API → S/4 | MULESOFT | 02.High |
| FPRI0378_IF | Interface | GL Interface - SAP API IF | 10. Object Complete | API → S/4 | MULESOFT | 03.Medium |
| FPRI0377 | Interface | GL Interface - File Processing in Mulesoft | 10. Object Complete | CONCUR → S/4 | MULESOFT | 02.High |
| FPRI0376 | Interface | GL Interface - File Processing in Mulesoft | 10. Object Complete | ICOST → S/4 | MULESOFT | 02.High |
| FPRI0323_IP | Interface | Create a common API for Asset updates, transfer, retire and Mass upload | 10. Object Complete |  | NA | 02.High |
| FPRI0323_IF | Interface | Create a common API for Asset updates, transfer, retire and Mass upload | 10. Object Complete |  | NA | 03.Medium |
| FPRI0227 | Interface | Outbound Interface from CFIN to QTM in relation to not only QTM payment ackno... | 10. Object Complete | S/4 → Quantum | SFT | 03.Medium |
| FPRI0226 | Interface | Inbound Interface from QTM to CFIN in relation to QTM payment files and MT me... | 10. Object Complete | Quantum → S/4 | SFT | 03.Medium |
| FPRI0224 | Interface | Outbound Interface - SAP to Quantum for Transmitting Cash Management Relevant... | 10. Object Complete | S/4 → Quantum | SFT | 02.High |
| FPRI0188 | Interface | Inbound Interface from EMS to S/4 to create WBS element and Update WBS elemen... | 10. Object Complete | XEUS → S/4 | APIGEE | 02.High |
| FPRF0230 | Form | Invoice output Layout - America | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE1723_IP | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1723_IF | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1722_IP | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1722_IF | Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1711 | Enhancement | BADI Enhancement to change Order Type from Product cost Collector from IP & I... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1706 | Enhancement | Enhancement to create Cash Management relevant data from F110 Payment Run for... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1705 | Enhancement | Enhancement to do Cash App post EBS load with the corresponding payment advice. | 10. Object Complete |  | NA | 03.Medium |
| FPRE1695 | Enhancement | Custom Fiori app - Change WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1671_IP | Enhancement | S4, Perform required calculations, summarizations, mappings and post the allo... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1671_IF | Enhancement | S4, Perform required calculations, summarizations, mappings and post the allo... | 10. Object Complete |  | NA | 04.Low |
| FPRE1661_IP | Enhancement | WBS transfer tool | 07. FUT Roadblock |  | NA | 02.High |
| FPRE1661_IF | Enhancement | WBS transfer tool | 07. FUT Roadblock |  | NA | 03.Medium |
| FPRE1660 | Enhancement | Enhancement for Revenue Recognition by Stage postings for Product/Services Sa... | 10. Object Complete |  | NA | 02.High |
| FPRE1659 | Enhancement | Enhancement for Revenue Recognition by Stage postings for Product/Services Sa... | 10. Object Complete |  | NA | 02.High |
| FPRE1650_IP | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Forecast.​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1650_IF | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Forecast.​ | 10. Object Complete |  | NA | 04.Low |
| FPRE1620_IP | Enhancement | Implement OSS Note 2358961 to allow COGS split based on Aux CCS at time of de... | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE1620_IF | Enhancement | Implement OSS Note 2358961 to allow COGS split based on Aux CCS at time of de... | 99. Rejected/Cancelled/On Hold |  | NA | 04.Low |
| FPRE1600 | Enhancement | Custom Fiori app - Create WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1599_IP | Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO li... | 07. FUT Roadblock |  | NA | 03.Medium |
| FPRE1599_IF | Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO li... | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE1564 | Enhancement | Employee Notification for timesheet entry | 10. Object Complete |  | NA | 03.Medium |
| FPRE1563 | Enhancement | Manager notification for timesheet approval | 10. Object Complete |  | NA | 03.Medium |
| FPRE1562 | Enhancement | Manage Delegates for approval | 10. Object Complete |  | NA | 03.Medium |
| FPRE1561 | Enhancement | Timesheet approval | 10. Object Complete |  | NA | 02.High |
| FPRE1560 | Enhancement | Timesheet entry for Intel Federal employees | 10. Object Complete |  | NA | 01.Very High |
| FPRE1553 | Enhancement | Custom Fiori app - Change WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE1519_IP | Enhancement | Project Change Order - Edit and Submit of draft request with change functiona... | 10. Object Complete |  | NA | 02.High |
| FPRE1519_IF | Enhancement | Project Change Order - Edit and Submit of draft request with change functiona... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1518_IP | Enhancement | Project Change Order - Change existing Purchase Orders during creation of Pro... | 10. Object Complete |  | NA | 02.High |
| FPRE1518_IF | Enhancement | Project Change Order - Change existing Purchase Orders during creation of Pro... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1517_IP | Enhancement | Project Change Order - Create Purchase Orders during creation of Project Chan... | 10. Object Complete |  | NA | 02.High |
| FPRE1517_IF | Enhancement | Project Change Order - Create Purchase Orders during creation of Project Chan... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1516_IP | Enhancement | Enhancement to enable user decision action to be taken from email directly fo... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1516_IF | Enhancement | Enhancement to enable user decision action to be taken from email directly fo... | 10. Object Complete |  | NA | 04.Low |
| FPRE1515_IP | Enhancement | Enhancement to display popup screen to trigger project creation workflow | 10. Object Complete |  | NA | 03.Medium |
| FPRE1515_IF | Enhancement | Enhancement to display popup screen to trigger project creation workflow | 10. Object Complete |  | NA | 04.Low |
| FPRE1513_IP | Enhancement | Generate and download JV file for JE posting | 10. Object Complete |  | NA | 03.Medium |
| FPRE1513_IF | Enhancement | Generate and download JV file for JE posting | 10. Object Complete |  | NA | 04.Low |
| FPRE1513_CFIN | Enhancement | Generate and download JV file for JE posting | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE1512_IP | Enhancement | Query confirm ITT document to determine the Capital/Expense and tax code manu... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1512_IF | Enhancement | Query confirm ITT document to determine the Capital/Expense and tax code manu... | 10. Object Complete |  | NA | 04.Low |
| FPRE1511_IP | Enhancement | Query existing draft ITT document and make changes | 10. Object Complete |  | NA | 03.Medium |
| FPRE1511_IF | Enhancement | Query existing draft ITT document and make changes | 10. Object Complete |  | NA | 04.Low |
| FPRE1510_IP | Enhancement | ITT document creation | 10. Object Complete |  | NA | 03.Medium |
| FPRE1510_IF | Enhancement | ITT document creation | 10. Object Complete |  | NA | 04.Low |
| FPRE1448 | Enhancement | FIORI screen to take care of TPR Display/ Change/ cancellation options | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE1443 | Enhancement | FIORI screen to take care of TFR Display/ Change/ cancellation options | 10. Object Complete |  | NA | 03.Medium |
| FPRE1438 | Enhancement | Update mixing ratio for Procurement alternative for Cross site transfer based... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1419 | Enhancement | Update Procurement alternatives based on production version & PIR for cross s... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1328 | Enhancement | Legal Valuation standard cost calculation enhancement | 99. Rejected/Cancelled/On Hold |  | NA | 03.Medium |
| FPRE1239 | Enhancement | Enhancement for Revenue Recognition by Stage postings for Product/Services Sa... | 10. Object Complete |  | NA | 02.High |
| FPRE1235_IP | Enhancement | Add custom fields to CJI3 and CJI5 reports (SAP S/4HANA Project Systems modul... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1235_IF | Enhancement | Add custom fields to CJI3 and CJI5 reports (SAP S/4HANA Project Systems modul... | 10. Object Complete |  | NA | 04.Low |
| FPRE1209 | Enhancement | Upload adjustments to time sheet entries in bulk for Intel Federal. | 10. Object Complete |  | NA | 02.High |
| FPRE1104_IP | Enhancement | WBS with custom attributes will be created in the PS module. The master data ... | 10. Object Complete |  | NA | 02.High |
| FPRE1104_IF | Enhancement | WBS with custom attributes will be created in the PS module. The master data ... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1025_IP | Enhancement | Custom Fiori app will be created using Free style model to display WBS/AUC re... | 10. Object Complete |  | NA | 03.Medium |
| FPRE1025_IF | Enhancement | Custom Fiori app will be created using Free style model to display WBS/AUC re... | 10. Object Complete |  | NA | 04.Low |
| FPRE0942_IP | Enhancement | Interface of SAP PPM module to ATLAS | 10. Object Complete | S4 → ATLAS | NA | 03.Medium |
| FPRE0942_IF | Enhancement | Interface of SAP PPM module to ATLAS | 10. Object Complete | S4 → ATLAS | NA | 04.Low |
| FPRE0931_IP | Enhancement | Rebuild Boundary Application ITT in S/4 | 10. Object Complete |  | NA | 03.Medium |
| FPRE0931_IF | Enhancement | Rebuild Boundary Application ITT in S/4 | 10. Object Complete |  | NA | 03.Medium |
| FPRE0931_CFIN | Enhancement | Rebuild Boundary Application ITT in S/4 | 10. Object Complete |  | NA | 02.High |
| FPRE0929 | Enhancement | Fiori UI for Counterparty Maintenance and User Exit to trigger replication to... | 10. Object Complete |  | NA | 02.High |
| FPRE0928 | Enhancement | Enhancement for automatic derivation and population of Purpose Of Payment (PO... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0899_IP | Enhancement | Custom Enhancement to disaggregate: Owner CC-DPN $ to WBS elements using Cape... | 10. Object Complete |  | NA | 02.High |
| FPRE0899_IF | Enhancement | Custom Enhancement to disaggregate:Owner CC-DPN $ to WBS elements using Capex... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0892 | Enhancement | Derive ICS FTQ data by Capex WBS L2 & Mfr. Process Node CC​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0891 | Enhancement | Split from primary Cost centers to PCOS & R&D/OCOS | 99. Rejected/Cancelled/On Hold |  | NA | 04.Low |
| FPRE0890_IP | Enhancement | Investment type creation and automatic settlement rule generation for Opex Pr... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0890_IF | Enhancement | Investment type creation and automatic settlement rule generation for Opex Pr... | 10. Object Complete |  | NA | 04.Low |
| FPRE0889_IP | Enhancement | Custom table needs to be created to hold allocation %s based on LOB Profit ce... | 10. Object Complete |  | NA | 04.Low |
| FPRE0889_IF | Enhancement | Custom table needs to be created to hold allocation %s based on LOB Profit ce... | 10. Object Complete |  | NA | 04.Low |
| FPRE0888_IP | Enhancement | Mass Update Fields in WBS Elements | 10. Object Complete |  | NA | 02.High |
| FPRE0888_IF | Enhancement | Mass Update Fields in WBS Elements | 10. Object Complete |  | NA | 03.Medium |
| FPRE0887_IP | Enhancement | WBS Element field synchronization to AUC and Fixed assets - Construction ID -... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0887_IF | Enhancement | WBS Element field synchronization to AUC and Fixed assets - Construction ID -... | 10. Object Complete |  | NA | 04.Low |
| FPRE0886_IP | Enhancement | Project Change Order - Create Project Change Order via custom Fiori Screens w... | 10. Object Complete |  | NA | 02.High |
| FPRE0886_IF | Enhancement | Project Change Order - Create Project Change Order via custom Fiori Screens w... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0885 | Enhancement | Custom Fiori app - Create WBS Element Request Form with ALV Input​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0884_IP | Enhancement | Custom Fiori app - CPA (Project Budget) approval request using PPM Item decis... | 10. Object Complete |  | NA | 02.High |
| FPRE0884_IF | Enhancement | Custom Fiori app - CPA (Project Budget) approval request using PPM Item decis... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0883_IP | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Actuals.​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0883_IF | Enhancement | (FTQ Input to drive Disaggregation to Allocation Cycle) for Actuals.​ | 10. Object Complete |  | NA | 04.Low |
| FPRE0882 | Enhancement | Derive FCS FTQ data by Capex WBS L2 & Mfr. Process Node CC​ | 10. Object Complete |  | NA | 03.Medium |
| FPRE0881 | Enhancement | DMEE User Exits Required in the payment files- APAC​ | 10. Object Complete |  | NA | 04.Low |
| FPRE0880 | Enhancement | Cash concentration functionality for cross-currency current accounts | 07. FUT Roadblock |  | NA | 04.Low |
| FPRE0879 | Enhancement | File Formatting and processing to support MBC and APM integration | 10. Object Complete |  | NA | 04.Low |
| FPRE0877_IP | Enhancement | Automation to set TECO and CLSD status on Project/ WBS | 10. Object Complete |  | NA | 02.High |
| FPRE0877_IF | Enhancement | Automation to set TECO and CLSD status on Project/ WBS | 10. Object Complete |  | NA | 03.Medium |
| FPRE0870 | Enhancement | Smart Exporter Interface to CFIN | 10. Object Complete | EY Smart Exporter Tool → S4 | NA | 04.Low |
| FPRE0827 | Enhancement | MT3xx and MT5xx Files - Adjust SWIFT Parameters for MBC | 10. Object Complete |  | NA | 04.Low |
| FPRE0786 | Enhancement | Enhancement to Mass upload of WOM payment advice. | 10. Object Complete |  | NA | 03.Medium |
| FPRE0785 | Enhancement | Enhancement to upload WCP Grant Amount in CFIN sys | 10. Object Complete |  | NA | 03.Medium |
| FPRE0784_IP | Enhancement | Reclass program for XIU/ SIU to reclass expense to inventory accounts (cost c... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0784_IF | Enhancement | Reclass program for XIU/ SIU to reclass expense to inventory accounts (cost c... | 10. Object Complete |  | NA | 04.Low |
| FPRE0783_IP | Enhancement | Asset creation from PO (S4 / Ariba / EMS, etc.) | 10. Object Complete | Ariba → S4 | NA | 03.Medium |
| FPRE0783_IF | Enhancement | Asset creation from PO (S4 / Ariba / EMS, etc.) | 10. Object Complete | Ariba → S4 | NA | 04.Low |
| FPRE0781_IP | Enhancement | Import Standard Cost from S4 tables into SAC using Custom CDS view. | 10. Object Complete |  | NA | 03.Medium |
| FPRE0781_IF | Enhancement | Import Standard Cost from S4 tables into SAC using Custom CDS view. | 10. Object Complete |  | NA | 04.Low |
| FPRE0780_IP | Enhancement | Read the workday file from AL11 in IP, IF | 10. Object Complete |  | NA | 03.Medium |
| FPRE0780_IF | Enhancement | Read the workday file from AL11 in IP, IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0779_IP | Enhancement | Enhance the details in workday file to meet AE format in IP, IF | 10. Object Complete |  | NA | 03.Medium |
| FPRE0779_IF | Enhancement | Enhance the details in workday file to meet AE format in IP, IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0777_IP | Enhancement | Add a field in ACDOCA to store Cert ID to continue auto-certify a BL task whe... | 10. Object Complete |  | NA | 04.Low |
| FPRE0777_IF | Enhancement | Add a field in ACDOCA to store Cert ID to continue auto-certify a BL task whe... | 10. Object Complete |  | NA | 04.Low |
| FPRE0777_CFIN | Enhancement | Add a field in ACDOCA to store Cert ID to continue auto-certify a BL task whe... | 10. Object Complete |  | NA | 04.Low |
| FPRE0764_IP | Enhancement | Import Headcount details by cost center and update in S4 for HR benefits spen... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0764_IF | Enhancement | Import Headcount details by cost center and update in S4 for HR benefits spen... | 10. Object Complete |  | NA | 04.Low |
| FPRE0763 | Enhancement | Placeholder - BADI for Memo Records with different Planning Levels/Types gene... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0761 | Enhancement | Branch Name and Address for Payments instead of entity Name and Address | 10. Object Complete |  | NA | 03.Medium |
| FPRE0760_IP | Enhancement | SAP RAR and TM Integration to trigger POD Event | 10. Object Complete |  | NA | 03.Medium |
| FPRE0760_IF | Enhancement | SAP RAR and TM Integration to trigger POD Event | 10. Object Complete |  | NA | 04.Low |
| FPRE0702 | Enhancement | Calculation of variance to be loaded for Group Actual Costing | 10. Object Complete |  | NA | 03.Medium |
| FPRE0701_IP | Enhancement | Mixed Costing ratio auto update | 10. Object Complete |  | NA | 03.Medium |
| FPRE0701_IF | Enhancement | Mixed Costing ratio auto update | 10. Object Complete |  | NA | 04.Low |
| FPRE0700_IP | Enhancement | Representative material ID – Q2-Q8 Forecast | 10. Object Complete |  | NA | 03.Medium |
| FPRE0700_IF | Enhancement | Representative material ID – Q2-Q8 Forecast | 10. Object Complete |  | NA | 04.Low |
| FPRE0699 | Enhancement | Enhancement for Excess Capacity – Fixed Spending Adjustment | 10. Object Complete |  | NA | 02.High |
| FPRE0698 | Enhancement | Legal Valuation standard cost calculation enhancement | 10. Object Complete |  | NA | 04.Low |
| FPRE0697 | Enhancement | RAR Balance sheet posting with MM & Sold To ID | 10. Object Complete |  | NA | 03.Medium |
| FPRE0648_IP | Enhancement | RD04 - Intercompany invoice billing posting to different GL accounts | 10. Object Complete |  | NA | 03.Medium |
| FPRE0648_IF | Enhancement | RD04 - Intercompany invoice billing posting to different GL accounts | 10. Object Complete |  | NA | 04.Low |
| FPRE0647_IP | Enhancement | Intercompany - Subledger Posting template & Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| FPRE0647_IF | Enhancement | Intercompany - Subledger Posting template & Approval Workflow | 10. Object Complete |  | NA | 04.Low |
| FPRE0647_CFIN | Enhancement | Intercompany - Subledger Posting template & Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| FPRE0646_IP | Enhancement | An automated solution to record the depreciation amount in a monthly basis fo... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0646_IF | Enhancement | An automated solution to record the depreciation amount in a monthly basis fo... | 10. Object Complete |  | NA | 04.Low |
| FPRE0645_IP | Enhancement | Need to identify a Mass settlement upload tool. Today, the capital life cycle... | 10. Object Complete |  | NA | 01.Very High |
| FPRE0645_IF | Enhancement | Need to identify a Mass settlement upload tool. Today, the capital life cycle... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0624 | Enhancement | Portal Remittance Automation- Retrofitting | 10. Object Complete |  | NA | 04.Low |
| FPRE0623 | Enhancement | Payment Advice Bot Success & Exception Report | 10. Object Complete |  | NA | 04.Low |
| FPRE0622 | Enhancement | Exception Handling & Trigger Set up | 10. Object Complete |  | NA | 04.Low |
| FPRE0621 | Enhancement | Payment Advice CSV Creation & Upload | 10. Object Complete |  | NA | 04.Low |
| FPRE0620 | Enhancement | Model Integration & Export | 10. Object Complete |  | NA | 04.Low |
| FPRE0619 | Enhancement | UiPath OCR - Model Validation | 10. Object Complete |  | NA | 04.Low |
| FPRE0618 | Enhancement | UiPath OCR - Iterative Model Training | 10. Object Complete |  | NA | 04.Low |
| FPRE0617 | Enhancement | UiPath OCR - Classification & Extraction | 10. Object Complete |  | NA | 04.Low |
| FPRE0616 | Enhancement | UiPath OCR - Taxonomy & Digitize | 10. Object Complete |  | NA | 04.Low |
| FPRE0605_IP | Enhancement | H2RA - 13th month bonus & Quarterly Performance Bonus (QPB) bonus accrual pos... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0605_IF | Enhancement | H2RA - 13th month bonus & Quarterly Performance Bonus (QPB) bonus accrual pos... | 10. Object Complete |  | NA | 04.Low |
| FPRE0604_IP | Enhancement | H2RA - Annual Performance Bonus (APB) ER taxes accrual & Quarterly Performanc... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0604_IF | Enhancement | H2RA - Annual Performance Bonus (APB) ER taxes accrual & Quarterly Performanc... | 10. Object Complete |  | NA | 04.Low |
| FPRE0602 | Enhancement | Reclassification of Vendor transactions from Default to Actual within CFIN | 10. Object Complete |  | NA | 03.Medium |
| FPRE0601 | Enhancement | Reclassification of Customer transactions from Default to Actual within CFIN | 10. Object Complete |  | NA | 03.Medium |
| FPRE0574_IP | Enhancement | Margin analysis Dimensions creation | 10. Object Complete |  | NA | 04.Low |
| FPRE0573_IP | Enhancement | Mass Asset Documents Reversal | 10. Object Complete |  | NA | 02.High |
| FPRE0573_IF | Enhancement | Mass Asset Documents Reversal | 10. Object Complete |  | NA | 03.Medium |
| FPRE0572_IP | Enhancement | Mass Asset Capitalization | 10. Object Complete |  | NA | 02.High |
| FPRE0572_IF | Enhancement | Mass Asset Capitalization | 10. Object Complete |  | NA | 03.Medium |
| FPRE0571_IP | Enhancement | DSD Matrix Rules to Update Depreciation Start Date in the Direct Cap Asset Ma... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0571_IF | Enhancement | DSD Matrix Rules to Update Depreciation Start Date in the Direct Cap Asset Ma... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0551 | Enhancement | SKF Actual Driver volume update from actual activity confirmation Automation | 10. Object Complete |  | NA | 03.Medium |
| FPRE0550 | Enhancement | Enhancement to update additive cost in IP based on Idoc of IF cost | 10. Object Complete |  | NA | 03.Medium |
| FPRE0549 | Enhancement | Enhancement to a) update Cost and Production volume in custom table, b) calcu... | 10. Object Complete |  | NA | 03.Medium |
| FPRE0500_IP | Enhancement | Rule for Transaction Price Allocation in BRIM vs SD | 10. Object Complete |  | NA | 03.Medium |
| FPRE0500_IF | Enhancement | Rule for Transaction Price Allocation in BRIM vs SD | 10. Object Complete |  | NA | 03.Medium |
| FPRE0499_IP | Enhancement | Substitution and Validation rule user exit | 10. Object Complete |  | NA | 03.Medium |
| FPRE0499_IF | Enhancement | Substitution and Validation rule user exit | 10. Object Complete |  | NA | 04.Low |
| FPRE0495_IP | Enhancement | Custom Fields in WBS element Master Data | 10. Object Complete |  | NA | 03.Medium |
| FPRE0495_IF | Enhancement | Custom Fields in WBS element Master Data | 10. Object Complete |  | NA | 04.Low |
| FPRE0477 | Enhancement | Rebate for Direct Customer to Rebate of Intransit deferrals for Direct & Dist... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0476 | Enhancement | Accounting for Stock Rotation | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0475 | Enhancement | Accounting for reserves for unissued returns credit note & Rebate Return Accr... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0474 | Enhancement | Accounting for technical return reserve | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0462 | Enhancement | Enhancement to develop automatic creation of payment advice number in the AR ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0430 | Enhancement | Enhancement for automatic creation of MT210 (pre-advice) message for IC settl... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0429_IP | Enhancement | Utility program to look up inactive cost center and derive replacement cost c... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0429_IF | Enhancement | Utility program to look up inactive cost center and derive replacement cost c... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0429_CFIN | Enhancement | Utility program to look up inactive cost center and derive replacement cost c... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0428_IP | Enhancement | Program to replace inactive cost centers in Assets | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0428_IF | Enhancement | Program to replace inactive cost centers in Assets | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0425 | Enhancement | Treasury Funding - Enhancement to support multiple Treasury Funding scenarios... | 10. Object Complete |  | NA | 02.High |
| FPRE0407_IP | Enhancement | Period Close in CFin, IP & IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0407_IF | Enhancement | Period Close in CFin, IP & IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0407_CFIN | Enhancement | Period Close in CFin, IP & IF | 10. Object Complete |  | NA | 03.Medium |
| FPRE0375_IP | Enhancement | GL Interface – IDOC status from IF & IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0375_IF | Enhancement | GL Interface – IDOC status from IF & IP | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0375_CFIN | Enhancement | GL Interface – IDOC status from IF & IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0374_IP | Enhancement | GL Interface- Managing 999+ GL line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0374_IF | Enhancement | GL Interface- Managing 999+ GL line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0374_CFIN | Enhancement | GL Interface- Managing 999+ GL line items | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0373 | Enhancement | GL Interface – Splitting of enriched files and populating staging table | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0372 | Enhancement | GL Interface - Incoming file processing and Simulation | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0360_IP | Enhancement | Reclassify GL Accounts for Balance Carryforwards - IP | 10. Object Complete |  | NA | 04.Low |
| FPRE0360_IF | Enhancement | Reclassify GL Accounts for Balance Carryforwards - IF | 10. Object Complete |  | NA | 04.Low |
| FPRE0328_IP | Enhancement | Validations on Asset updates, transfer and retirement | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0328_IF | Enhancement | Validations on Asset updates, transfer and retirement | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0326_IP | Enhancement | Mass upload tool to asset update, transfer and retire (S4 Fiori functionality... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0326_IF | Enhancement | Mass upload tool to asset update, transfer and retire (S4 Fiori functionality... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0324_IP | Enhancement | Custom Fiori App for Asset update, transfer, scrap, and retire based on Repor... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0324_IF | Enhancement | Custom Fiori App for Asset update, transfer, scrap, and retire based on Repor... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0322_IP | Enhancement | Fiori Dashboard to display/edit pre-paid amortization for PO​ | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0322_IF | Enhancement | Fiori Dashboard to display/edit pre-paid amortization for PO​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0321_IP | Enhancement | Fiori Dashboard to display/edit accruals for PO​ | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0321_IF | Enhancement | Fiori Dashboard to display/edit accruals for PO​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0320_IP | Enhancement | Enhancement to read PO data and create manual accrual object​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0320_IF | Enhancement | Enhancement to read PO data and create manual accrual object​ | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0319_IP | Enhancement | Enhancement for accrual posting notification​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0319_IF | Enhancement | Enhancement for accrual posting notification​ | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0315_IP | Enhancement | Activation of custom enhancement tab on portfolio bucket for custom fields. | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0315_IF | Enhancement | Activation of custom enhancement tab on portfolio bucket for custom fields. | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0314_IP | Enhancement | Smart numbering for portfolio items. | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0314_IF | Enhancement | Smart numbering for portfolio items. | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0289_IP | Enhancement | Update XREF1, XREF2 and XREF3 fields in subledger line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0289_IF | Enhancement | Update XREF1, XREF2 and XREF3 fields in subledger line items | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0289_CFIN | Enhancement | Update XREF1, XREF2 and XREF3 fields in subledger line items | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0287_IP | Enhancement | Need to enhance Fiori screen to capture business process and the approver whi... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0287_IF | Enhancement | Need to enhance Fiori screen to capture business process and the approver whi... | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0287_CFIN | Enhancement | Need to enhance Fiori screen to capture business process and the approver whi... | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0286_IP | Enhancement | Mass upload of the same supporting document as an attachment to multiple JEs | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0286_IF | Enhancement | Mass upload of the same supporting document as an attachment to multiple JEs | 10. Object Complete | NA → NA | NA | 04.Low |
| FPRE0286_CFIN | Enhancement | Mass upload of the same supporting document as an attachment to multiple JEs | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRE0285 | Enhancement | Cash App rules engine for matching incoming payments with payment advice | 10. Object Complete |  | NA | 01.Very High |
| FPRE0284 | Enhancement | Mass upload of payment advice | 10. Object Complete |  | NA | 03.Medium |
| FPRE0282 | Enhancement | RPA BOT for collecting and transforming customer payment advice into standard... | 10. Object Complete |  | NA | 04.Low |
| FPRE0240 | Enhancement | Treasury Payment/funding Request - Enhancement to support multiple Treasury P... | 10. Object Complete | NA → NA | NA | 02.High |
| FPRE0049 | Enhancement | Enhancement - Custom Fields in Manage bank Accounts | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRC1724_IP | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  | NA | 02.High |
| FPRC1724_IF | Conversion | Creation of output template with consumption data | 06. Dev In Progress |  | NA | 03.Medium |
| FPRC1565 | Conversion | Convert active delegate relationships for Timesheet approval | 10. Object Complete |  | NA | 02.High |
| FPRC1493 | Conversion | Conversion of WIP values as per Component structure in S/4 - IP | 10. Object Complete |  | NA | 02.High |
| FPRC1491 | Conversion | Conversion of WIP values as per Component structure in S/4 - Back End IF | 10. Object Complete |  | NA | 02.High |
| FPRC1464_IP | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  | NA | 02.High |
| FPRC1464_IF | Conversion | Project Actuals Conversion (Non- Intel Federal) | 10. Object Complete |  | NA | 02.High |
| FPRC1442 | Conversion | Conversion of Actual Labor hours for Intel Federal Projects | 10. Object Complete |  | NA | 02.High |
| FPRC1441 | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete |  | NA | 02.High |
| FPRC1212 | Conversion | Project Actuals Conversion including Intel Federal | 10. Object Complete |  | NA | 03.Medium |
| FPRC0908_IP | Conversion | Project Budget Conversion | 10. Object Complete |  | NA | 03.Medium |
| FPRC0908_IF | Conversion | Project Budget Conversion | 10. Object Complete |  | NA | 03.Medium |
| FPRC0196_IP | Conversion | Asset Transaction data conversion | 10. Object Complete | NA → NA | NA | 02.High |
| FPRC0196_IF | Conversion | Asset Transaction data conversion | 10. Object Complete | NA → NA | NA | 02.High |
| FPRC0195_IP | Conversion | Asset Master data conversion | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRC0195_IF | Conversion | Asset Master data conversion | 10. Object Complete | NA → NA | NA | 03.Medium |
| FPRC0174_IP | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC → S4 | NA | 02.High |
| FPRC0174_IF | Conversion | Conversion of ECC project hierarchy (WBS element master data) to S/4HANA proj... | 10. Object Complete | ECC → S4 | NA | 03.Medium |
| FPRC0117 | Conversion | Conversion – In House Cash: Current Account creation and Current Account Bala... | 10. Object Complete | ECC → CFIN | NA | 02.High |
| FPRC0116 | Conversion | Conversion – Migration of Existing Bank Guarantees and Intercompany Loans to ... | 10. Object Complete | Quantum → CFIN | NA | 03.Medium |
| FPRC0035_IP | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  → MDG | NA | 03.Medium |
| FPRC0035_IF | Conversion | Convert existing ECC & MDG hierarchy to S4HANA PPM hierarchy (Portfolio & buc... | 10. Object Complete |  → MDG | NA | 04.Low |

**Summary**: 17 Reports, 86 Interfaces, 25 Conversions, 219 Enhancements, 1 Forms, 18 Workflows

<div class="page-footer"><span>Page 32</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for DC-050:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 33</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for DC-050:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 34</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (366 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 349 | 95.4% |
| 07. FUT Roadblock | 10 | 2.7% |
| 99. Rejected/Cancelled/On Hold | 5 | 1.4% |
| 06. Dev In Progress | 2 | 0.5% |
| **Total** | **366** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 17 |
| Interface (I) | 86 |
| Conversion (C) | 25 |
| Enhancement (E) | 219 |
| Form (F) | 1 |
| Workflow (W) | 18 |
| **Total** | **366** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 5 |
| 02.High | 64 |
| 03.Medium | 201 |
| 04.Low | 93 |
| N/A | 3 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| FPRI1669 | 02.Interface | Import Xeus/Mars volumes from ECA into S4.​ | 07. FUT Roadblock | 03.Medium |
| FPRE1723_IP | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock | 04.Low |
| FPRE1723_IF | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA(FM and BRF+) | 07. FUT Roadblock | 04.Low |
| FPRE1722_IP | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock | 04.Low |
| FPRE1722_IF | 04.Enhancement | Intel BRF+ - Create Function Modules in S/4HANA (FM and components) | 07. FUT Roadblock | 04.Low |
| FPRE1661_IP | 04.Enhancement | WBS transfer tool | 07. FUT Roadblock | 02.High |
| FPRE1661_IF | 04.Enhancement | WBS transfer tool | 07. FUT Roadblock | 03.Medium |
| FPRE1599_IP | 04.Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO line ... | 07. FUT Roadblock | 03.Medium |
| FPRE1599_IF | 04.Enhancement | Update existing custom table ZTFPR_ACRENG02 to store the calculation of PO line ... | 07. FUT Roadblock | 04.Low |
| FPRE0880 | 04.Enhancement | Cash concentration functionality for cross-currency current accounts | 07. FUT Roadblock | 04.Low |
| FPRC1724_IP | 03.Conversion | Creation of output template with consumption data | 06. Dev In Progress | 02.High |
| FPRC1724_IF | 03.Conversion | Creation of output template with consumption data | 06. Dev In Progress | 03.Medium |

### 6.3 NFRs & Design Principles

| Category | Requirement | Target / SLA | Priority |
|----------|-------------|-------------|----------|
| Performance | Month-end batch costing/closing completes within SLA window | < 4 hours end-to-end batch window | High |
| Availability | S/4 HANA finance modules available during business hours | 99.9% (Mon-Fri 06:00-22:00 PST) | High |
| Scalability | Support 2x transaction volume growth over 3-year horizon | Handle 500K+ journal entries/day | Medium |
| Recoverability | RPO/RTO for financial systems meets audit requirements | RPO < 1 hour, RTO < 4 hours | High |
| Data Volume | Support growing data volumes from legacy migration + BAU | 50M+ records in material ledger | Medium |
| Latency | Near-real-time posting for financial transactions | < 5 seconds for online postings | Medium |
| Concurrency | Support concurrent month-end users across time zones | 200+ concurrent finance users | Medium |

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

<div class="page-footer"><span>Page 35</span><span><a href="#toc">↑ Back to TOC</a></span><span>DC-050 — DC-050</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*364 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| FPRW1449 | TPR : Workflow to handle Memo creation and cancellation process | Jul-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW1444 | TFR: Workflow to handle Memo creation and cancellation process | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Oct-25 (100%) | 1. On Track |
| FPRW1064_IP | Custom Workflow will also be created with some predefined process/rules for approval/rejection. | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 1. On Track |
| FPRW1064_IF | Custom Workflow will also be created with some predefined process/rules for approval/rejection. | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 1. On Track |
| FPRW0930 | Workflow for Counterparty Approval | Apr-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | 5. Not Dispositioned |
| FPRW0906_IP | Custom workflow: Change Order Create and Change Approval | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 1. On Track |
| FPRW0906_IF | Custom workflow: Change Order Create and Change Approval | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 1. On Track |
| FPRW0904_IP | Custom Workflow - WBS Element Request approval with WBS Element creation | Mar-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW0904_IF | Custom Workflow - WBS Element Request approval with WBS Element creation | Mar-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW0900_IP | Custom Workflow: Approval for Project creation and create a Project def and level n1 after approval using template | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 3. Off Track |
| FPRW0900_IF | Custom Workflow: Approval for Project creation and create a Project def and level n1 after approval using template | Feb-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRW0445_IP | Project budget approval workflow (Capex)​ | Aug-24 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) | 1. On Track |
| FPRW0445_IF | Project budget approval workflow (Capex)​ | Aug-24 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) | 1. On Track |
| FPRW0325_IP | Custom workflow to manage the approval process in bulk/individual requests | Jul-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Mar-25 (100%) |  |
| FPRW0325_IF | Custom workflow to manage the approval process in bulk/individual requests | Jul-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Mar-25 (100%) |  |
| FPRW0165_IP | Workflow is required to trigger the approvers based on the business requirement for Journal entry | May-24 (100%) | Aug-24 (100%) | Aug-24 (100%) | Sep-24 (100%) |  |
| FPRW0165_IF | Workflow is required to trigger the approvers based on the business requirement for Journal entry | May-24 (100%) | Aug-24 (100%) | Aug-24 (100%) | Sep-24 (100%) |  |
| FPRW0165_CFIN | Workflow is required to trigger the approvers based on the business requirement for Journal entry | May-24 (100%) | Aug-24 (100%) | Aug-24 (100%) | Sep-24 (100%) |  |
| FPRR1514_IP | To generate reports out of the ITT documents that was created | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| FPRR1514_IF | To generate reports out of the ITT documents that was created | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| FPRR1240 | Custom report for Revenue Recognition by Stage for Product/Services Sale​ actual revenue vs planned revenue | Mar-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 4. Completed |
| FPRR1211 | Report for searching on and viewing government contract timesheets for Intel Federal. | Apr-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 1. On Track |
| FPRR1210 | Report for searching on and viewing government contract timesheet changes for Intel Federal.​ | Apr-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 4. Completed |
| FPRR0907_IP | Workflow Status Report ( Order Request / Approval Request / Others ) | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) | 2. At Risk |
| FPRR0907_IF | Workflow Status Report ( Order Request / Approval Request / Others ) | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) | 1. On Track |
| FPRR0497 | CFR - Report to support multiple Treasury Funding requests from Multiple Intel teams | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) | 1. On Track |
| FPRR0496 | TPR-Report to support multiple Treasury Payment Requests from Multiple Intel teams | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 1. On Track |
| FPRR0461 | Inter-company Outage Pre-consolidate Report (ACDOCA) | Aug-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Mar-25 (100%) |  |
| FPRR0380 | GL Interface – Reconciliation Report/Dashboard | Aug-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Sep-25 (100%) |  |
| FPRR0327_IP | Report to display the requests/change IDs and status of the workflow approval and Error handling | Jul-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Mar-25 (100%) | 1. On Track |

*... and 334 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**Mapped sub-tower(s):** 3.1 FPR - GL Close & Consolidate, 3.10 FPR - Accounts Receivable & Collections, 3.11 FPR - Project Accounting, 3.2 FPR - Tax, 3.3 FPR - Revenue Recognition & Reporting, 3.4 FPR - Intercompany, 3.5 FPR - Fixed Assets, 3.6 FPR - Cost and Profitability Analysis, 3.7 FPR - Product Costing and Inventory Valuation, 3.8 FPR - Financial Planning & Analysis, 3.9 FPR - Treasury and Cash Management

**RAID Summary:** 18 open items (6 capability-specific, 12 tower-level), 234 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 1 | 1 |
| P2 - Medium | 4 | 10 | 14 |
| P3 - Low | 2 | 1 | 3 |
| **Total** | **6** | **12** | **18** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03633 | Action | P2 - Medium | Conversion RICEFW (FPRC1724_IF/IP) has dependency on the enh... | In Progress | FPR | 2026-03-13 |
| 02226 | Action | P3 - Low | DMEE related FPR objects not ready for development | In Progress | FPR | 2026-03-31 |
| 03729 | Action | P2 - Medium | AN and CC invoices are fetching wrong tax codes and posting ... | In Progress | FPR | 2026-03-23 |
| 02680 | Action | P2 - Medium | T042A table config in IP and IF | In Progress | FPR | 2026-04-03 |
| 03782 | Risk | P2 - Medium | Auto processing of JPMC lockbox BAI2 for AR Cashapp not work... | Not Started | FPR | 2026-04-10 |
| 03473 | Action | P3 - Low | Manual Service PIR creation for IP-IF Service Procurement. | In Progress | FPR | 2026-05-29 |

**Other FPR Tower RAID Items** (12 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03197 | Issue | P2 - Medium | Company Code address disappearing in DI0 250 | Not Started |  |  |
| 03564 | Risk | P2 - Medium | Development of the AMT impacting FPR Capital Tool report | In Progress | FTS IP | 2026-03-27 |
| 03624 | Issue | P2 - Medium | Test Data not provided for CR "INT-Build-CR0918" | In Progress | FPR | 2026-03-20 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03628 | Risk | P2 - Medium | R3 Returns Rework Process Causing Finance Double Counting in... | In Progress | E2E | 2026-03-27 |
| 03629 | Risk | P2 - Medium | Consensus Demand Data for ICOST | In Progress | FTS IP | 2026-03-27 |
| 02799 | Risk | P2 - Medium | Deloite FPR objects FPRXV490, FPRXV038 and FPRXV048 are dela... | In Progress | FPR | 2026-03-25 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03740 | Action | P2 - Medium | Provide count of report with list of names due in ITC1 and I... | In Progress | FPR | 2026-03-20 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03333 |  | P3 - Low | FPR NRT : IF and IP  Power BI Workspace Provisioning | In Progress | Analytics (Reporting) | 2026-01-12 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*DC-050 — Architecture Document (TOGAF BDAT) · Finance Plan To Report · Generated: March 2026*

