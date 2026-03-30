<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-08 — E2E-08</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-08 · Forecast to Stock</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-08 E2E-08** within the IAO program. It includes 8 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Forecast to Stock |
| **Capability** | E2E-08 - E2E-08 |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Forecast to Stock |
| **L2 Capability** | E2E-08 - E2E-08 |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-08 Process Migration | Migrate E2E-08 business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-08 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **8 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-08 E2E-08.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-08A_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_One_Step_Transfer | E2E-08A_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_One_Step_Transfer | External Partners , SAP S/4 Intel Product | 2 | 0 |
| 2 | E2E-08B_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_Two_Step_Transfer | E2E-08B_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_Two_Step_Transfer | SAP S/4 Intel Product | 3 | 0 |
| 3 | E2E-08C_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_Two_Step_Transfer | E2E-08C_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_Two_Step_Transfer | SAP S/4 Intel Product | 3 | 0 |
| 4 | E2E-08D_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_One_Step_Transfer | E2E-08D_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_One_Step_Transfer | External Partners , SAP S/4 Intel Product | 2 | 0 |
| 5 | E2E-08E_R3_Material_Movement_(Non-Inventory)_–_Same_LE | E2E-08E_R3_Material_Movement_(Non-Inventory)_–_Same_LE | SAP S/4 Intel Product  | 6 | 1 |
| 6 | E2E-08F_R3_Inventory_Stock_Transfer_Inter_Plant_of_Same_Company_Code_(Inventory)_–_Within_Same_LE | E2E-08F_R3_Inventory_Stock_Transfer_Inter_Plant_of_Same_Company_Code_(Inventory)_–_Within_Same_LE | External Partners , SAP S/4 Receiving Plant , SAP S/4 Sending Plant | 11 | 2 |
| 7 | E2E-08G_R3_TM_Embedded_with_3PL | E2E-08G_R3_TM_Embedded_with_3PL | Boundary Apps , External Partners/B2B, SAP S/4 Intel Product Shipping Location  | 12 | 5 |
| 8 | E2E-08H_R3_TM_Steps | E2E-08H_R3_TM_Steps | Boundary Apps , External Partners/B2B, SAP S/4 Intel Product Shipping Location  | 13 | 5 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-08A_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_One_Step_Transfer — E2E-08A_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_One_Step_Transfer

**Swim Lanes**: External Partners  · SAP S/4 Intel Product | **Tasks**: 2 | **Gateways**: 0

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
    subgraph External Partners 
        n3(["fa:fa-play Trigger Inventory Transfer"])
    end
    subgraph SAP S/4 Intel Product
        n1[["fa:fa-cog Create MIGO Transfer"]]
        n2[["fa:fa-cog Perform Physical Movement of Goods"]]
        n4(["fa:fa-stop Physical Movements of Goods Completed"])
    end
    n3 --> n1
    n1 --> n2
    n2 --> n4
    class n1 serviceTask
    class n2 serviceTask
    class n3 startEvt
    class n4 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVMuO2jAU_RUrI5RWCmqehGZRCQIZjdRRkZi2i2EWJrkGaxw7ss2riH-vwyM8pqzqRSQf33OOz43trZWLAqzEarW2lFOdoK2t51CCnSB7ihXYDjoAv7CkeMpA2XUNEVyP6Z99mRdW67qsxjJcUrap0THMBKCfTw7qGSJzkMJctRVISmzHriQtsdykgglZVz9Al7hk73Zc6gtZgDwXuG7s5ZGhMsrhDAdxGIdZzVOQC15ciZKIdElu7-rNMbHK51jq_fYXCp7x-jct9NzMCWYKTM1cl-w7ngKrM2q5qLF8IZenZlBV-3DTsHGFc8pnBg9dA0nM389Q5O52aNdqTXhjil4GE47MyBlWagAEKW3g4VIjQhlLHsK0l0Wuo7QU75A8-MN4EPhOXidJTHTXqZvbXgGdzXUyFaw4lrZXdYbEr9aOXCe-68iN-d54AS_OTmnH7_rdxqkfe6mXnpwIIf_lZPoqX7B6P3oNg8zPBo2XF3Wi1P2od4o5COOed9snkEuaw4VolmXB8NyqYSfy3Pui_SzouOmN6AxrWOHNWfBrGjaCWRRnXnxX8OB3u8vFdCRFfhIMhlEWNYJx38t6_l3BsOeF3eMOjc5M4mqOhmsNkmOGRuaYcJAKHQrqwYNPrxOL4ITgdsVMjBdJZzOQ6IkvgWsha8RcNgJyYr19PhDNGbixGPdGaPwlNCwNxkeKYpHrCxfvtXHJxQylEkzX0PPT449L-bcLhn_NGIEkQpZoNN8ompssz2JpHhKukSDoUYhC3fDDcy6lRfWRqBomSkVZMdBQ_CMiD1C7_c0kOE69w9Q_Tv3DNLz4h3XNxUm7WvHvrgTNLb6Cw-OFsxyrBFliWljJ1to_ouahLYDgBdPWzrHwQovxhudWsn9srEVVmBYPKDY_qDyAu7_3g86O" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-08B_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_Two_Step_Transfer — E2E-08B_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_Two_Step_Transfer

**Swim Lanes**: SAP S/4 Intel Product | **Tasks**: 3 | **Gateways**: 0

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
    subgraph SAP S/4 Intel Product
        n1["fa:fa-user Create MIGO Transfer in Issue SLOC"]
        n2[["fa:fa-cog Perform Physical Movement of Goods"]]
        n3[["fa:fa-cog Post MIGO to Transfer from in-Transfer Balance at Receiving SLOC"]]
        n4(["fa:fa-play Initiate MIGO Transfer"])
        n5(["fa:fa-stop Transfer Completed"])
    end
    n4 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n5
    class n1 userTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 startEvt
    class n5 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVF1v2jAU_StWqopNClo-G5aHSRBIhbSq1ei2h3YPxrkGq44d2Q4tq_jvcwgklKpPy0OUe3zPOffe2H51iCzASZ3Ly1cmmEnR68CsoYRBigZLrGHgohb4hRXDSw560ORQKcyC_d2n-VH10qQ1WI5LxrcNuoCVBPRz7qKxJXIXaSz0UINidOAOKsVKrLaZ5FI12Rcwoh7dux2WJlIVoPoEz0t8ElsqZwJ6OEyiJMobngYiRfFGlMZ0RMlg1xTH5TNZY2X25dcabvDLb1aYtY0p5hpsztqU_DteAm96NKpuMFKrzXEYTDc-wg5sUWHCxMrikWchhcVTD8Xebod2l5ePojNF99NHgexDONZ6ChRpY-HZxiDKOE8vomycx56rjZJPkF4Es2QaBi5pOklt657bDHf4DGy1NulS8uKQOnxuekiD6sVVL2nguWpr32deIIreKbsKRsGoc5okfuZnRydK6X852bmqe6yfDl6zMA_yaeflx1dx5r3XO7Y5jZKxfz4nUBtG4EQ0z_Nw1o9qdhX73seikzy88rIz0RU28Iy3veDXLOoE8zjJ_eRDwdbvvMp6eackOQqGsziPO8Fk4ufj4EPBaOxHo0OFVmelcLVGi_EdWnyJ0FwY4MhqFzUxbU7zCP_h0aE4pXjYjBxlCmxL6GZ-fYvu7W7U1IJMoLnWNaDF99vs0flzQg8eOj6RK3QHikpVorv1VjOCObqRG3vkhUGSomspC23pp_zwjC-1ac2N7P2pkqUtYtgBE8yxIICwQT-AANvY83Is7lQ9-tSpV9z-prm9mNi7_izp8wkp7knayKovI5NlxcFA0RPsgWg_RISGw292nIfQb8PgEAZtGB7CsA3jk5_fUI6b_g0cnO7cNyvhhytRdyu8gePDAXZcpwRVYlY46auzv5TtxV0AxTU3zs51cG3kYiuIk-4vL6euCju1KcN2T5UtuPsH9QDlDw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.3 E2E-08C_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_Two_Step_Transfer — E2E-08C_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_Two_Step_Transfer

**Swim Lanes**: SAP S/4 Intel Product | **Tasks**: 3 | **Gateways**: 0

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
    subgraph SAP S/4 Intel Product
        n1["fa:fa-user Create MIGO Transfer in Issue SLOC"]
        n2[["fa:fa-cog Perform Physical Movement of Goods"]]
        n3[["fa:fa-cog Post MIGO to Transfer from in-Transfer Balance at Receiving SLOC"]]
        n4(["fa:fa-play Initiate MIGO Transfer"])
        n5(["fa:fa-stop Transfer Completed"])
    end
    n4 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n5
    class n1 userTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 startEvt
    class n5 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVF1v2jAU_StWqopNClo-G5aHSRBIhbSq1ei2h3YPxrkGq44d2Q4tq_jvcwgklKpPy0OUe3zPOffe2H51iCzASZ3Ly1cmmEnR68CsoYRBigZLrGHgohb4hRXDSw560ORQKcyC_d2n-VH10qQ1WI5LxrcNuoCVBPRz7qKxJXIXaSz0UINidOAOKsVKrLaZ5FI12Rcwoh7dux2WJlIVoPoEz0t8ElsqZwJ6OEyiJMobngYiRfFGlMZ0RMlg1xTH5TNZY2X25dcabvDLb1aYtY0p5hpsztqU_DteAm96NKpuMFKrzXEYTDc-wg5sUWHCxMrikWchhcVTD8Xebod2l5ePojNF99NHgexDONZ6ChRpY-HZxiDKOE8vomycx56rjZJPkF4Es2QaBi5pOklt657bDHf4DGy1NulS8uKQOnxuekiD6sVVL2nguWpr32deIIreKbsKRsGoc5okfuZnRydK6X852bmqe6yfDl6zMA_yaeflx1dx5r3XO7Y5jZKxfz4nUBtG4EQ0z_Nw1o9qdhX73seikzy88rIz0RU28Iy3veDXLOoE8zjJ_eRDwdbvvMp6eackOQqGsziPO8Fk4ufj4EPBaOxHo0OFVmelcLVGi_EdWnyJ0FwY4MhqFzUxbU7zCP_h0aE4pXjYjBxlCmxL6GZ-fYvu7W7U1IJMoLnWNaDF99vs0flzQg8eOj6RK3QHikpVorv1VjOCObqRG3vkhUGSomspC23pp_zwjC-1ac2N7P2pkqUtYtgBE8yxIICwQT-AANvY83Is7lQ9-tSpV9z-prm9mNi7_izp8wkp7knayKovI5NlxcFA0RPsgWg_RISGw292nIfQb8PgEAZtGB7CsA3jk5_fUI6b_g0cnO7cNyvhhytRdyu8gePDAXZcpwRVYlY46auzv5TtxV0AxTU3zs51cG3kYiuIk-4vL6euCju1KcN2T5UtuPsH9QDlDw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 E2E-08D_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_One_Step_Transfer — E2E-08D_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_One_Step_Transfer

**Swim Lanes**: External Partners  · SAP S/4 Intel Product | **Tasks**: 2 | **Gateways**: 0

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
    subgraph External Partners 
        n3(["fa:fa-play Trigger Inventory Transfer"])
    end
    subgraph SAP S/4 Intel Product
        n1[["fa:fa-cog Create MIGO Transfer"]]
        n2[["fa:fa-cog Perform Physical Movement of Goods"]]
        n4(["fa:fa-stop Physical Movements of Goods Completed"])
    end
    n3 --> n1
    n1 --> n2
    n2 --> n4
    class n1 serviceTask
    class n2 serviceTask
    class n3 startEvt
    class n4 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVMuO2jAU_RUrI5RWCmqehGZRCQIZjdRRkZi2i2EWJrkGaxw7ss2riH-vwyM8pqzqRSQf33OOz43trZWLAqzEarW2lFOdoK2t51CCnSB7ihXYDjoAv7CkeMpA2XUNEVyP6Z99mRdW67qsxjJcUrap0THMBKCfTw7qGSJzkMJctRVISmzHriQtsdykgglZVz9Al7hk73Zc6gtZgDwXuG7s5ZGhMsrhDAdxGIdZzVOQC15ciZKIdElu7-rNMbHK51jq_fYXCp7x-jct9NzMCWYKTM1cl-w7ngKrM2q5qLF8IZenZlBV-3DTsHGFc8pnBg9dA0nM389Q5O52aNdqTXhjil4GE47MyBlWagAEKW3g4VIjQhlLHsK0l0Wuo7QU75A8-MN4EPhOXidJTHTXqZvbXgGdzXUyFaw4lrZXdYbEr9aOXCe-68iN-d54AS_OTmnH7_rdxqkfe6mXnpwIIf_lZPoqX7B6P3oNg8zPBo2XF3Wi1P2od4o5COOed9snkEuaw4VolmXB8NyqYSfy3Pui_SzouOmN6AxrWOHNWfBrGjaCWRRnXnxX8OB3u8vFdCRFfhIMhlEWNYJx38t6_l3BsOeF3eMOjc5M4mqOhmsNkmOGRuaYcJAKHQrqwYNPrxOL4ITgdsVMjBdJZzOQ6IkvgWsha8RcNgJyYr19PhDNGbixGPdGaPwlNCwNxkeKYpHrCxfvtXHJxQylEkzX0PPT449L-bcLhn_NGIEkQpZoNN8ompssz2JpHhKukSDoUYhC3fDDcy6lRfWRqBomSkVZMdBQ_CMiD1C7_c0kOE69w9Q_Tv3DNLz4h3XNxUm7WvHvrgTNLb6Cw-OFsxyrBFliWljJ1to_ouahLYDgBdPWzrHwQovxhudWsn9srEVVmBYPKDY_qDyAu7_3g86O" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.5 E2E-08E_R3_Material_Movement_(Non-Inventory)_–_Same_LE — E2E-08E_R3_Material_Movement_(Non-Inventory)_–_Same_LE

**Swim Lanes**: SAP S/4 Intel Product  | **Tasks**: 6 | **Gateways**: 1

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
    subgraph SAP S/4 Intel Product 
        n1[["fa:fa-cog Perform Outbound Delivery"]]
        n2[["fa:fa-cog Perform Goods Issue and Update Inventory"]]
        n3[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n4[["fa:fa-cog Perform Pick and Pack Updates"]]
        n5[["fa:fa-cog Perform Post Goods Issue"]]
        n6[["fa:fa-cog Confirmation of Service (NLAG)"]]
        n7(["fa:fa-play Trigger Outbound Delivery Via ISM"])
        n8(["fa:fa-stop Service Confirmation"])
        n9["E2E-08G R3 Inventory Stock Transfer (Non Inventory Scenario)"]
        n10{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n10
    n10 --> n2
    n10 --> n3
    n2 --> n4
    n4 --> n5
    n5 --> n6
    n6 --> n8
    n7 --> n1
    n3 --> n9
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
    class n9 startEvt
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVU1v4joU_StWqoqOFDT5JGkWI1EgVaXpDHpp5y2GWZjEBqvGRrYDZRD__dkkQEib1csC5dx7z7kf2Dd7K-cFshLr9nZPGFEJ2PfUEq1QLwG9OZSoZ4PK8AsKAucUyZ6JwZypjPw9hrnB-t2EGVsKV4TujDVDC47A65MNhppIbSAhk32JBME9u7cWZAXFbsQpFyb6BsXYwcdsteuBiwKJS4DjRG4eaiolDF3MfhREQWp4EuWcFVeiOMQxznsHUxzl23wJhTqWX0r0DN__JYVaaowhlUjHLNWKfodzRE2PSpTGlpdicxoGkSYP0wPL1jAnbKHtgaNNArK3iyl0DgdwuL2dsXNS8DKeMaCfnEIpxwgDqbR5slEAE0qTm2A0TEPHlkrwN5TceJNo7Ht2bjpJdOuObYbb3yKyWKpkzmlRh_a3pofEW7_b4j3xHFvs9G8rF2LFJdNo4MVefM70ELkjd3TKhDH-X5n0XMULlG91romfeun4nMsNB-HI-ah3anMcREO3PSckNiRHDdE0Tf3JZVSTQeg63aIPqT9wRi3RBVRoC3cXwftRcBZMwyh1o07BKl-7ynI-FTw_CfqTMA3PgtGDmw69TsFg6AZxXaHWWQi4XoJsOAXZ1wA8MYUo0NpFmStQBZmHub9_zywMEwz7OV-AKRKYixX4Wao5L1kBxoiSDRK7mfXnT4PmfU575LyQ4EnKEgGo2a_rQo9IZ98gpvgHFf9aZSSQiU7F8dCAV71Hjionw09zk1sSweeFTEn-duROoX6pypAtathB5VI1G2mxBq2aOcNErKAinAGOQVadM3D34_vw8UuLG92duWuqz82LIIsFEh-nDX4RCJ6yZ83_0uDHF75UfH1O1iyiRbnXjIk36TvxI_jHv_wTIFNcT-ZFrxyJdQl3P3T9DW-OmF7U3HTQPC3Ofn-qAArBt7IPqQJrKCCliD5W92FmHQ4VSW-M6oW5oN__ZgRO2KkMXgv7NfYqGNQwqGBYw7CCgxoOKhjXMKpz1dCv4H3jrpl6GhvhyuN1evxOT9DpCTs9g05PdN7qV-a4XsBXxvvPY_U46-Vk2dYK6bNBCivZW8dPsP5MFwjDkirrYFuwVDzbsdxKjp8qqzxeljGBeoOsKuPhP2iFfoE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 E2E-08F_R3_Inventory_Stock_Transfer_Inter_Plant_of_Same_Company_Code_(Inventory)_–_Within_Same_LE — E2E-08F_R3_Inventory_Stock_Transfer_Inter_Plant_of_Same_Company_Code_(Inventory)_–_Within_Same_LE

**Swim Lanes**: External Partners  · SAP S/4 Receiving Plant  · SAP S/4 Sending Plant | **Tasks**: 11 | **Gateways**: 2

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
    subgraph External Partners 
        n10[["fa:fa-cog Perform 3PL Shipping"]]
        n11[["fa:fa-cog Perform 3PL Receiving"]]
        n18{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 Receiving Plant 
        n6[["fa:fa-cog Create Stock Transfer Order (STO)"]]
        n7[["fa:fa-cog Convert Stock Transfer Requisition to STO"]]
        n8[["fa:fa-cog Create Inbound Delivery"]]
        n9[["fa:fa-cog Perform Goods Receipt and Update Inventory"]]
        n12(["fa:fa-play STR Creation Initiated"])
        n15(["fa:fa-stop Goods Receipt Performed"])
    end
    subgraph SAP S/4 Sending Plant
        n1[["fa:fa-cog Create Outbound Delivery"]]
        n2[["fa:fa-cog Create Freight Unit and Freight Order"]]
        n3[["fa:fa-cog Perform GTS Trade Compliance"]]
        n4[["fa:fa-cog Pick and Pack Updates"]]
        n5[["fa:fa-cog Perform Post Goods Issue (PGI)"]]
        n13(["fa:fa-stop GTS Trade Compliance Performed"])
        n14(["fa:fa-stop Pick and Pack Updates Completed"])
        n16["E2E-08H R3 Inventory Stock Transfer (Inventory Scenario)"]
        n17{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n6 --> n7
    n7 --> n1
    n17 --> n10
    n1 -->|"EDI: 3B12"| n17
    n17 --> n2
    n17 --> n3
    n10 --> n18
    n18 -->|"EDI: 3B13"| n4
    n5 --> n8
    n8 -->|"EDI: 3B2"| n11
    n11 -->|"EDI: 4B2"| n9
    n18 -->|"EDI: 3B2"| n5
    n9 --> n15
    n12 --> n6
    n3 --> n13
    n2 --> n16
    n4 --> n14
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 startEvt
    class n13 endEvt
    class n14 endEvt
    class n15 endEvt
    class n16 startEvt
    class n17 gateway
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVltv4jgU_itWqoqOBJpcSZqHlSiQLlJXRU278zDMg0kcsGrsrO3Qsgz_fR2ScPEk-7DLQ9VzvvN95-JLvDcSliIjNG5v95hiGYJ9T67RBvVC0FtCgXp9UDn-hBzDJUGiV8ZkjMoY_30Ms9z8swwrfRHcYLIrvTFaMQTeZn0wUkTSBwJSMRCI46zX7-UcbyDfjRlhvIy-QUFmZsdsNfTAeIr4OcA0fSvxFJVgis5ux3d9Nyp5AiWMpleimZcFWdI7lMUR9pGsIZfH8guB_oCf33Aq18rOIBFIxazlhjzBJSJlj5IXpS8p-LYZBhZlHqoGFucwwXSl_K6pXBzS97PLMw8HcLi9XdBTUvD0sqBA_RIChZigDAip3NOtBBkmJLxxx6PIM_tCcvaOwht76k8cu5-UnYSqdbNfDnfwgfBqLcMlI2kdOvgoewjt_LPPP0Pb7POd-qvlQjQ9ZxoP7cAOTpkefGtsjZtMWZb9r0xqrvwVivc619SJ7GhyymV5Q29s_qrXtDlx_ZGlzwnxLU7QhWgURc70PKrp0LPMbtGHyBmaY010BSX6gLuz4P3YPQlGnh9ZfqdglU-vsljOOUsaQWfqRd5J0H-wopHdKeiOLDeoK1Q6Kw7zNZh-SsQpJGCutglFXIAqoPxRy_z-fWFkMMzgIGErMEc8Y3wDnPkTiNc4z9U-XBg_flxSrG7KC0oQ3rZwgv2-4UDO2YcYQCJBDjkkBJHHaogL43CoSGqbaV3EozmIv7rnDGBOIJWXvQyv6xpzpGRBLFnyDl7VuRIZ4uC5vArAXfz6_EWr0dfojG6ROm4a_wX9VWCBJWYUSAaUjiYTtFYxo0tW0BRMEMFKdqeR7ttH-shYKqqWcwmg4r_laSW3RVSyX3Qs--4klBO1LePXl6qEst6ZupWxoqeK9eWS5Z1ZQrJcy1tXc0nrXp9YQafVuczROpbnQv7rXOxWVsSPVwp4U_0cp9I4jourSTgdo32Ny0VNkVroTU4wpAnSmK7GxGoflNnmUP1TLYTQKF57sjkTsh7qTIgCgbv540zff5ajr0JLiW2LUbFdjd1abqWEWrbAULGn9nRgBr-DF-e8wfT9f3eBJIiqLzkrG7mU8v_jWadDMBj8pg5ibfqVWV_jSre2zcZR2j9V2ZNZCJwHy14YP8swLd7WbKexzVovaByBJugcBd0a9qrwJloLrpOfir0qzq3h-45MFerV6H1dV2NbduUY1rZT400jNWw1uFvb7sWXpZzWxffvCrE7EacTcTsRrxMZdiJ-JxJ0IvediFrYTqh7CmrKzUPq2u_Uj55rr9vq9Vq9ww5lv3k9XLuDxm30jQ3iG4hTI9wbx6ezel6nKIMFkcahb8BCsnhHEyM8PjGN4njKJxiqO3lTOQ__AGK4nNg=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 E2E-08G_R3_TM_Embedded_with_3PL — E2E-08G_R3_TM_Embedded_with_3PL

**Swim Lanes**: Boundary Apps  · External Partners/B2B · SAP S/4 Intel Product Shipping Location  | **Tasks**: 12 | **Gateways**: 5

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
        n1[["fa:fa-cog Carrier Invoice Reconciliation/ Dispute Management"]]
    end
    subgraph External Partners/B2B
        n10[["fa:fa-cog Book/Tender to Carrier SAP BN4L-FC"]]
        n11[["fa:fa-cog Capture Execution events via BN4L-GTT"]]
        n12[["fa:fa-cog Capture Carrier Invoices (via EDI only"]]
        n13(["fa:fa-play Capture Execution Initiated"])
        n14(["fa:fa-play Capture Carrier Invoices Initiated"])
    end
    subgraph SAP S/4 Intel Product Shipping Location 
        n2[["fa:fa-cog Create/ Update Freight Unit and Order"]]
        n3[["fa:fa-cog Execute Freight Order and Status Updates Post GI"]]
        n4[["fa:fa-cog Perform Carrier Selection and Calculate Charges"]]
        n5[["fa:fa-cog Create/ Update Freight Settlement Document"]]
        n6[["fa:fa-cog Create Service PO/ Entry Sheet"]]
        n7[["fa:fa-cog Post Accrual to Freight Expense Account(s)"]]
        n8[["fa:fa-cog Allocate Freight Costs to Delivery Items (CO/PA) or Material Valuation"]]
        n9[["fa:fa-cog Receive reconciled Carrier Invoice(s)"]]
        n15(["fa:fa-stop Accrual Posted"])
        n16(["fa:fa-stop Freight Costs Allocated"])
        n17["E2E-08E R3 Material Movement (Non-Inventory) – Same LE"]
        n18{{"fa:fa-arrows-alt parallelGateway"}}
        n19{{"fa:fa-arrows-alt parallelGateway"}}
        n20{{"fa:fa-arrows-alt inclusiveGateway"}}
        n21{{"fa:fa-arrows-alt inclusiveGateway"}}
        n22{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n2 --> n20
    n20 --> n4
    n4 --> n18
    n18 --> n10
    n18 --> n21
    n21 --> n3
    n10 --> n20
    n11 --> n21
    n3 --> n22
    n5 --> n6
    n6 --> n19
    n19 --> n7
    n19 --> n8
    n22 --> n5
    n9 --> n22
    n1 --> n9
    n7 --> n15
    n8 --> n16
    n12 --> n1
    n13 --> n11
    n14 --> n12
    n17 --> n2
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 startEvt
    class n14 startEvt
    class n15 endEvt
    class n16 endEvt
    class n17 startEvt
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV11v4joQ_StWVhWtBCIJCQEergQhWVVqd9HS3fuw3Qc3cSCqsSPboWUr_vsd54OPQKR79_IA-MzMOTOTsZN8GBGPiTExbm4-UpaqCfroqDXZkM4EdV6wJJ0uKoEfWKT4hRLZ0T4JZ2qZ_i7cLCd7124aC_EmpTuNLsmKE_T9voumEEi7SGIme5KINOl0O5lIN1jsfE650N6fyCgxk0KtMs24iIk4OpimZ0UuhNKUkSM88BzPCXWcJBFn8Rlp4iajJOrsdXKUv0VrLFSRfi7JI37_O43VGtYJppKAz1pt6AN-IVTXqESusSgX27oZqdQ6DBq2zHCUshXgjgmQwOz1CLnmfo_2NzfP7CCKHr49MwSfiGIp5yRBUgEcbBVKUkonnxx_GrpmVyrBX8nkkx1484HdjXQlEyjd7Orm9t5IulqryQunceXae9M1TOzsvSveJ7bZFTv4bmgRFh-V_KE9skcHpZln-ZZfKyVJ8r-UoK_iCcvXSisYhHY4P2hZ7tD1zUu-usy5402tZp-I2KYROSENw3AQHFsVDF3LbCedhYOh6TdIV1iRN7w7Eo5950AYul5oea2EpV4zy_xlIXhUEw4CN3QPhN7MCqd2K6EztZxRlSHwrATO1mjG82KW0TTLJCqN-sOsnz-fjQRPEtyL-Ar5WIiUCHTPthzahL7pTRClNMUq5ayP5qnMckXQI2Z4BbuYqWfj16-SD8aioRq8KyIYpmgBw8mIkP2ZPTsVN8_VZ5y_9p-ABzJQ_JDMcrpAsy_OQy_0j2olwUX6mcoFAWES5TpjRLaQo0TbFJcUn5-emhz2dY5GKyS61STB_B5xRndNksHtgSSjMAqXmdzDcQhtJDGE3p2GOi2hFwlcYbjsuW7Wsu-AsyLQeMHjPFJouU6zDI4T9MCj4lKezkCzAYKASB99z2L4RaEo9i76DuoIsxh91Qdpo_7BOUVZ9TG2CCmClwqrXFbcEi24VOjzfYPNOWdbEJFwsTnOA6EkKorQjD6mUU51pj4cjSsiG2Tuv6puSZSixUCjOY_y88kueIbXeCCuOE_Q4msfBUzBDluuCWnGeo2CdNXTKBI57A0Y9DqJ4D0jTBJtgv2qbuVdg2d0zjOlVF_OYxU-EEvNOCc03RLI5l6RDYyu_7W_mN4hLmDnwp6EGyj6gWlejEJDY3yuAScAASokqpOAxM3BvEzTco8jLRXPDrXqwi83wLDhfV5NXeRFmAdRgR30zFGAvg2OhT3ybXkhb79w1oMk4T8Xuzv0nNumNUBLvCHoIQC6U7bRx0edBJTH32QPU4UyLDClhH4uT_hnY78_DRr_QZBtXg1KWURzCZ1uibL-KMr-j1GH84TZqNf7S2dbr80ScKq1Uy6tUbW2RhVgNgDbqhmsEhjUDmZDwrIaEYNqbVdrt1wPq-WwUhzX8eMS8BrrOkW7qsmt1uMGfSVf03kVfe1eF1jLWxVdna1VpWsdgLpHB4GK0j653WvZk4eSM4vdahm0WpxWi9tqGbZavFbLqNUybrXAFW81tXfBam8DtLx-8D3HnRbcrR5ez9HhVdRr4RjVz3vn8PgqDNvmKmxdh-0aNrrGhogNTmNj8mEUb0zwVhWTBOdUGfuugXPFlzsWGZPizcLIi_vZPMXwGLApwf0_bDBCJw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.8 E2E-08H_R3_TM_Steps — E2E-08H_R3_TM_Steps

**Swim Lanes**: Boundary Apps  · External Partners/B2B · SAP S/4 Intel Product Shipping Location  | **Tasks**: 13 | **Gateways**: 5

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
        n1[["fa:fa-cog Carrier Invoice Reconciliation/ Dispute Management"]]
    end
    subgraph External Partners/B2B
        n11[["fa:fa-cog Book/Tender to Carrier SAP BN4L-FC"]]
        n12[["fa:fa-cog Capture Execution events via BN4L-GTT"]]
        n13[["fa:fa-cog Capture Carrier Invoices (via EDI only"]]
        n14(["fa:fa-play Capture Execution Initiated"])
        n15(["fa:fa-play Capture Carrier Invoices Initiated"])
    end
    subgraph SAP S/4 Intel Product Shipping Location 
        n2[["fa:fa-cog Create/ Update Freight Unit and Order"]]
        n3[["fa:fa-cog Execute Freight Order and Status Updates Post GI"]]
        n4[["fa:fa-cog Perform Carrier Selection and Calculate Charges"]]
        n5[["fa:fa-cog Create/ Update Freight Settlement Document"]]
        n6[["fa:fa-cog Create Service PO/ Entry Sheet"]]
        n7[["fa:fa-cog Post Accrual to Freight Expense Account(s)"]]
        n8[["fa:fa-cog Allocate Freight Costs to Delivery Items (CO/PA) or Material Valuation"]]
        n9[["fa:fa-cog Receive reconciled Carrier Invoice(s)"]]
        n10[["fa:fa-cog Send Outbound Delivery and Freight Order to 3PL"]]
        n16(["fa:fa-stop Accrual Posted"])
        n17(["fa:fa-stop Freight Costs Allocated"])
        n18["E2E-08F R3 Inventory Stock Transfer Inter Plant of Same Company Code..."]
        n19{{"fa:fa-arrows-alt parallelGateway"}}
        n20{{"fa:fa-arrows-alt parallelGateway"}}
        n21{{"fa:fa-arrows-alt inclusiveGateway"}}
        n22{{"fa:fa-arrows-alt inclusiveGateway"}}
        n23{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n2 --> n21
    n21 --> n4
    n4 --> n19
    n19 --> n11
    n19 --> n10
    n22 --> n3
    n11 --> n21
    n12 --> n22
    n3 --> n23
    n5 --> n6
    n6 --> n20
    n20 --> n7
    n20 --> n8
    n23 --> n5
    n9 --> n23
    n1 --> n9
    n7 --> n16
    n8 --> n17
    n13 --> n1
    n14 --> n12
    n15 --> n13
    n18 --> n2
    n10 -->|"EDI 940 / RNET 3B12"| n22
    class n1 serviceTask
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 startEvt
    class n15 startEvt
    class n16 endEvt
    class n17 endEvt
    class n18 startEvt
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV9tu2zgQ_RVCReAUsGNdLdsPC9iyVQRIWyNOuw9NHxiJsoXQokBSTtLU_75DXW3ZAna7fkjAGc6ZM4fDi961gIVEm2pXV-9xEsspeu_JLdmR3hT1nrAgvT4qDN8xj_ETJaKn5kQskev4Vz7NsNNXNU3ZfLyL6ZuyrsmGEfTtto9mEEj7SOBEDAThcdTr91Ie7zB_8xhlXM3-QMaRHuXZStec8ZDwZoKuu0bgQCiNE9KYLdd2bV_FCRKwJDwBjZxoHAW9gyJH2UuwxVzm9DNBPuPXv-NQbmEcYSoIzNnKHb3DT4SqGiXPlC3I-L4SIxYqTwKCrVMcxMkG7LYOJo6T58bk6IcDOlxdPSZ1UnR3_5gg-AUUC7EgERISzMu9RFFM6fSD7c18R-8LydkzmX4wl-7CMvuBqmQKpet9Je7ghcSbrZw-MRqWUwcvqoapmb72-evU1Pv8Df62cpEkbDJ5I3NsjutMc9fwDK_KFEXR_8oEuvIHLJ7LXEvLN_1FnctwRo6nn-NVZS5sd2a0dSJ8HwfkCNT3fWvZSLUcOYbeDTr3rZHutUA3WJIX_NYATjy7BvQd1zfcTsAiX5tl9rTiLKgAraXjOzWgOzf8mdkJaM8Me1wyBJwNx-kWzVmW9zKapalAhVP9EuPHj0ctwtMIDwK2QR7mPCYc3SZ7BjKhe7UJgpjGWMYsGaJFLNJMEvQZJ3gDuziRj9rPnwUetEUr6_JVEp5gilbQnAnhYjg358fJW9nnjD0PHwAHGEhWk1nPVmj-xb4b-F6TrQAw2_RTmXECiUmQKcaI7IGjQPsYFxCfHh7aGNZljJYUAl0rkOXiFrGEvrVB7OsaJKXQCudMbuE4BBlJCKEfj0OdjtAzAhcQzjVXYq2HNkyWBITnLMwCidbbOE3hOEF3LMiX8rgH2iJyAkmG6Fsawn_k83zvom-QHeEkRF_VQdqqv6VhUXUTm4fkwWuJZSZKbIFWTEj06baFZp-irQiPGN81_UAoCfIiFKKHaZBRxdSDo3FDRAvM-VfVrYmUNG9otGBBdtrZOc7oEg7E5ecJWn0domUiYYett4S0Y91WQarqWRDwDPYGNHpFYvmakkQQ5YL9Kq_FxxbO-BRnRqlazqYKD4CFQlwQGu8JsLmVZAet630drmYfEeOwc2FPwgWKvmOa5a3QyjE5zQEnAAEoxMuTgITtxjynaeinGGui2iaTT-oUarip1TvtEGBure7aaKNmgwjJ0lo5JeP5dnJbs0-1qSQ7CxtD1NJcDvSxj-4tVRu0AFPrKVnwjB7gThZRXjToh1YUQ6ewCK3xDhqP7VKcwM6Fq_zm5gagj5En7-8VIRCOvYgBphKlmGNKCf1U3B2P2uFwvCX1PwkyLgbFSUAzAZJ3RJl_FGX9x6j6pEpMNBj8pdhWY6Mw2OXYLobGpBwbk9JgtA16hVBCWtUEo5XCqHKapcEqx1WEU4xH5XBUuusEemFwW-NxNS7xnHI8acGXfKqK3JJ_lW5cjit4o4Sr6VeSVPSNkq9RJygh6gk5wd_Q0nBfTWwdDdH9l-UDsuaAof1ulMifHIrg0cPoxGN2eqxOj93pcTo9o06P2-kZd3omnR5QptPVrYLRLYPRrQOsW_UuP7U7HfZR-bY-tboXreMOjEn1HD1dRv2y2bhsNi-brcqs9bUd4Tsch9r0Xcs_6OCjLyQRzqjUDn0NZ5Kt35JAm-YfPlqWX7eLGMMrZVcYD_8AikBzEA==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| External Partners  | E2E-08A_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_One_Step_Transfer, E2E-08D_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_One_Step_Transfer, E2E-08F_R3_Inventory_Stock_Transfer_Inter_Plant_of_Same_Company_Code_(Inventory)_–_Within_Same_LE,  | |
| SAP S/4 Intel Product | E2E-08A_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_One_Step_Transfer, E2E-08B_R3_Inventory_Stock_Transfer_from_SLOC_to_SLOC_-_Two_Step_Transfer, E2E-08C_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_Two_Step_Transfer, E2E-08D_R3_Inventory_Stock_Transfer_Plant_to_Plant_(Same_LE)_-_One_Step_Transfer,  | |
| SAP S/4 Intel Product  | E2E-08E_R3_Material_Movement_(Non-Inventory)_–_Same_LE,  | |
| SAP S/4 Receiving Plant  | E2E-08F_R3_Inventory_Stock_Transfer_Inter_Plant_of_Same_Company_Code_(Inventory)_–_Within_Same_LE,  | |
| SAP S/4 Sending Plant | E2E-08F_R3_Inventory_Stock_Transfer_Inter_Plant_of_Same_Company_Code_(Inventory)_–_Within_Same_LE,  | |
| Boundary Apps  | E2E-08G_R3_TM_Embedded_with_3PL, E2E-08H_R3_TM_Steps | |
| External Partners/B2B | E2E-08G_R3_TM_Embedded_with_3PL, E2E-08H_R3_TM_Steps | |
| SAP S/4 Intel Product Shipping Location  | E2E-08G_R3_TM_Embedded_with_3PL, E2E-08H_R3_TM_Steps | |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
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

    subgraph E2E08CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E08CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E08CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E08CDAA_e_g_XEUS -.-> E2E08CDAD_e_g_Azure_SQL
    end
    style E2E08CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E08CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E08CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E08CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E08CDAA_e_g_MES_300 -.-> E2E08CDAD_e_g_SAP_HANA
    end
    style E2E08CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E08CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E08CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnSLQFXwYI20eSg7TSpxlncltilOdpXuHi0TXudIPK_764F3BCc8S5puPfj-14_rzkWOEwjwCZuNBYsYcJEC01MYAqaibQRLUBrIq2AsMyZmLvwG7hy8DStPVXod5ozOuJQaCo7ThPhsadK4MjIZipM2Rw6ZXyurB6MU0B3l01EZCLXliqCp4_hhOai0igLuKKzHywSE3mOKS9AxkzElLt0BFwVEnmpbIns3stoyJKxNHYMacpp8vBiOjaWS7RsNPxkUwIN-36C5Ao5LQoLYkSzrJ_OUMw4Nw_6huU4TrMQefoA5oGu93r97urYelQ9me1s1gxTnubK3bGMbb1oNJjzlRwxrC7pbeTads_qtPfKHfUNu61vyUHKX9pznL7RNzZ6g4Eu1169ble5_aRWLMrROKfZBNltWz8ZWGTgBhCMA_JU5hB439x7HyMf_6qj1YpYDqFgabKBptY6nVTZP-07TybC4fgQqd9SwDTNmunrHGur4icf-2V00onkMwqP_TIGXb6yEquCkAzy8WclWWF9qwvUOmyd76tUJ0ISrViIOYe9INawidob2Lau9r-wj7LZ__B65Ca4INfkQ3SvbC_o6PoasDwieXwP403ZNxDLGKRi3kN41ckuyOtS72G8jv0Q4t1l0dnZ-fMKkFUxRV8QubmUT4dx8PHz_o9ia3QujGX7938RCyMdWWRIELkdXFwO7cHw7tZGrv3Vvrb2TNO9fbG6gZo7yTLOQqq8u0fnBtaeOVlUUHUT7x6RG9hS3k6iVhq3XBZDLV9fGTvHUb_hmr6h9ob-6enpK_S4iaeQTymLsLnA1Y0v_y8iiGnJBV42MS1F6s2TEJvVpYzLLKICLEYl0WltXP4ByO71Tw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E08FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E08FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E08FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E08FDAA_e_g_XEUS -.-> E2E08FDAD_e_g_Azure_SQL
    end
    style E2E08FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E08FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E08FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E08FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E08FDAA_e_g_MES_300 -.-> E2E08FDAD_e_g_SAP_HANA
    end
    style E2E08FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E08FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E08FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlY9P2kAUx_-VyxnCloCrYEGbaHLQdppU4yxuS-zSHO0rXDzapr1OEPnfd9dC3RCc8S5puPfj-14_rzmWOEhCwAZuNJYsZsJAy6aYwgyaBmqOaQ7NFmrmEBQZEwsHfgNXDp4klacM_U4zRscc8qbKjpJYuOypFDjS07kKUzabzhhfKKsLkwTQ3WULEZnImysVwZPHYEozUWoUOVzR-Q8Wiqk8R5TnIGOmYsYdOgauComsULZYdu-mNGDxRBq7ujRlNH54MR3rqxVaNRpeXJdAo4EXI7kCTvPchAjRNB0kcxQxzo2DgW7att3KRZY8gHGgaf3-oLc-th9VT0YnnbeChCeZcndNfVsvHA8XfC1HdLNH-rVcx-qb3c5euaOBbnW0LTlI-Et7tj3QB3qtNxxqcu3V6_WU24srxbwYTzKaTpHVsbQT2yRDxwd_4pOnIgPf_ebcexh5-FcVrVbIMggES-IamlqbdFJm_7TuXJkIh5NDpH5LAcMwKqavc8ytip887BXhSTeUzzA49ooINPnKSqwMQjLIw5-VZIn1rS5Q-7B9vq9SlQhxuGYhFhz2gtjAJmrXsC1N7X9hH6Xz_-F1yY1_Qa7Jh-heWa7f1bQNYHlE8vgexnXZNxDLGKRi3kN43ckuyJtS72G8if0Q4t1l0dnZ-fMakFkyRV8QubmUT5tx8PDz_o9ia3QOTGT7938RC0INmWREELkdXlyOrOHo7tZCjvXVujb3TNO5fbE6vpo7SVPOAqq8u0fn-OaeOZlUUHUT7x6R41tS3orDdhK1HRZBJV9dGTvHUb3hhr6udk3_9PT0FXrcwjPIZpSF2Fji8saX_xchRLTgAq9amBYicRdxgI3yUsZFGlIBJqOS6Kwyrv4ARKL1eQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-08-R001 | Report | E2E-08 operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-08-C001 | Conversion | Legacy data migration for E2E-08 | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-08.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E08C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E08C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E08CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E08CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E08C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E08CMW_e_g_Azure_Service_Bus
    E2E08CMW_e_g_Azure_Service_Bus --> E2E08C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonjt7t--BP_ZHj-ae6vs0aQBvB4fQQSR-SPkloGIas8KcEv5w779No5fgydPSQB5uvWQq-B-kTDcC3Mv7h6447BVOOQmsUkqiCtqxald12cvZ-zIXvMDnvkehtbzE4K4gVAK0BF5P0qHdBe4XDu0dHaGjHgfz76V1dXhzRXpFVdWWRDyLyXp9dQeXY9d7GWs5m50WQTOb1UD4HlMFYe9ujxDbxVxiVpFoLtaV10-THgOVujfhA3zfi26HmJlT_ziTvNKsLU6nRh-YgOnKdH86l_Y0udX3Z29XWMpOE0QAr8CfN5fqjh2oLjco2-bJtXN92qh1iq-PHiYS8RaqVL0Kcq2IYT9rkTAJJMw6bLg3XaeT8b7VJKWohyruwLfXbCHt-fr5zlmkNbQ7pHFOiGUstv73k3UcgxBkT2qqh4UzE3iIKNCO_VLQskRsFm2JZhHlhXP0Du289aQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-08.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E08F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E08F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E08FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E08FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E08F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E08FMW_e_g_Azure_Service_Bus
    E2E08FMW_e_g_Azure_Service_Bus --> E2E08F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1vokAQ_isbGuMXbemLLyWNCQhevGDblL7c5byQlR100xUIu7S11v9-u2DFYht7a4Jh5plnlmdmdpdaEBPQDK1WW9KICgMt62IGc6gbqD7BHOoNVOcQZCkVCxeegCkHi-PCk0PvcUrxhAGvq-gwjoRHX3OC43byomDKNsBzyhbK6sE0BnQ3bCBTBrIG4jjiTQ4pDesrhWbxczDDqcj5Mg4j_PJAiZjJ9xAzDhIzE3Pm4gkwlVSkmbJF8ku8BAc0mkrjmS5NKY4eS1NLX63QqlYbR5sU6NYaR0iuWg01m3JDwYyOsIAmjXhCUyCIiwUDFDDMOXCJKeD5uw0hmmScRsA5yldIGTMOBnJZrQYXafwIxoHV7bZ1a_3afFZfYpwkL40gZnFqHOi6XuHESYLKVXBaLcW64dT1Tsdq_wcnwQLvctrdPZzHHzjffQRzKV6KF1JT1KpkmlNCGDzjFLYVsdtmqYjTaQ9Ktm_sHmK2o4jSeEvlfl_X93EWrDybTFOczJDp_hlr44x0T4l8ktMWMq-v3WHfvB1eXSLX_O3cjLW_RZBaRDZEIGgcIfemtDonjt4d-OBP_ZHj-ae6vs0aQBvB4fQQSR-SPkloGIas8KcEv5w779No5fgydPSQB5uvWQq-B-kTDcC3Mv7h6447BVOOQmsUkqiCtqxald12cvZ-zIXvMDnvkehtbzE4K4gVAK0BF5P0qHdBe4XDu0dHaGjHgfz76V1dXhzRXpFVdWWRDyLyXp9dQeXY9d7GWs5m50WQTOb1UD4HlMFYe9ujxDbxVxiVpFoLtaV10-THgOVujfhA3zfi26HmJlT_ziTvNKsLU6nRh-YgOnKdH86l_Y0udX3Z29XWMpOE0QAr8CfN5fqjh2oLjco2-bJtXN92qh1iq-PHiYS8RaqVL0Kcq2IYT9rkTAJJMw6bLg3XaeT8b7VJKWohyruwLfXbCHt-fr5zlmkNbQ7pHFOiGUstv73k3UcgxBkT2qqh4UzE3iIKNCO_VLQskRsFm2JZhHlhXP0DAe89gQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-08-I001 | Interface | E2E-08 inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-08-E001 | Enhancement | E2E-08 custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-08-F001 | Form/Report | E2E-08 operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
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

    subgraph E2E08CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E08CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E08CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E08CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E08CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E08CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E08CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E08CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iQgoFVKp2is26QxIQeOxKqDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuDe2AqwTjvM13pd1JRsmBQa2p1zgsR0ccOMByVG1WmtJCsKdsqNYIlB3R7rSNXLmRaqyoYf0hXpBIdo6nhhmx-0EysZJwTVoOsWYk1m5EFMLWRqBqlFdJ9VJKUFkspjgwpVaS4O0q20baoHQzi4rAF-ubFBZIjZaSup5AjUpYe36CcMuacefY0DEO9FhW_A-fMMC4vvfE-_PCgPDlmudFTznil0tbUfs0rGRFHoD8Jxv7HA9CaTALLfwm0jsChZwem8QoInB15YejZnn3g-b4hx0mD47FKx0VPrJvFsiLlCgVmYEz8-WyeQLJM3MemgmROSPQrxnFjjo1h3ORgyJ3Pl-eoSyOVjvHvHqRGRitIBeUFmn09qs9ktyP_DG4Vs8OobwlwHKdveL8GimzvTWwZnDT2T8188_BRMko-u1_cxDRMqzt_NrEyOWfE_rsL0cUIqTqk6t7diJsgSizDeO6FDJEM39mOF1b_Q0feol9dfXram51250MXyJ1fyzmkDGL8dPKqsI7XUK0JzbCzw90bIV-YDHLSMIFbHZNG8GhbpNjpfmPclBkRMKVEXs-6F9s_ebBuWg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E08FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E08FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E08FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E08FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E08FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E08FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E08FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E08FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRD6iRIQKuUTtFYt0ljQg4ciVWDEZg2acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3DPTCVYJz3ma70O6koWTKoNbU644UI6WMHGI7KjSpTWkByyrZKDWHFAd1e68iVC5nWqgrGH5I1qUTHaGq4IZsfNBVrGWeE1SBr1iJnc7IEpjYSVaO0QroPS5LQYiXFkSGlihR3R8k22ha1g0FUHLZA37yoQHIkjNT1DDJEytLjG5RRxpwzz54FQaDXouJ34JwZxuWlN96HHx6UJ8csN3rCGa9U2prZr3klI-IInE788fTjAWhNJr41fQm0jsChZ_um8QoInB15QeDZnn3gTaeGHCcNjscqHRU9sW6Wq4qUa-SbvjEJFvNFDPEqdh-bCuIFIeGvCEeNOTaGUZOBIXc-X52jLo1UOsK_e5AaKa0gEZQXaP71qD6T3Y78079VzA6jviXAcZy-4f0aKNK9N7FlcNLYPzXzzcOH8Sj-7H5xY9Mwre786cRK5ZwS--8uhBcjpOqQqnt3I278MLYM47kXMkQyfGc7Xlj9Dx15i3519elpb3bWnQ9dIHdxLeeAMojw08mrwjrOocoJTbGzw90bIV-YFDLSMIFbHZNG8HBbJNjpfmPclCkRMKNEXk_ei-0fnIFucg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
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

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-08 — E2E-08</span></div>
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
*E2E-08 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

