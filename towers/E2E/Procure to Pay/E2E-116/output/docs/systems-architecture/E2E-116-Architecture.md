<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-116 — R3 Wafer Reclaim Process</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-116 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-116 R3 Wafer Reclaim Process** within the IAO program. It includes 2 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-116 - R3 Wafer Reclaim Process |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: "loose"` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-116 - R3 Wafer Reclaim Process |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-116 Process Migration | Migrate R3 Wafer Reclaim Process business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-116 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **2 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-116 R3 Wafer Reclaim Process.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-116A_R3__Outbound_(Return)_Straddle_&amp;_End_State | E2E-116A_R3__Outbound_(Return)_Straddle_&amp;_End_State | EWM, External Partners/ Supplier, SAP S/4 Intel Foundry | 21 | 4 |
| 2 | E2E-116B_R3__Inbound_(Reclaim) | E2E-116B_R3__Inbound_(Reclaim) | Boundary Apps, EWM, External Partners/ Supplier, SAP S/4 Intel Foundry | 18 | 5 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-116A_R3__Outbound_(Return)_Straddle_&amp;_End_State — E2E-116A_R3__Outbound_(Return)_Straddle_&amp;_End_State

**Swim Lanes**: EWM · External Partners/ Supplier · SAP S/4 Intel Foundry | **Tasks**: 21 | **Gateways**: 4

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
    subgraph EWM
        n3["Inbound Delivery EWM"]
        n4["Unloading EWM"]
        n5["Post Goods Receipt EWM"]
        n6["Post Goods Receipt EWM"]
        n7["Put-Away Confirmation with exception Codes"]
        n8["Create /Confirm Put-Away Task EWM"]
        n9["Outbound Delivery Order (EWM)"]
        n10["Create and Confirm Picking and Packing (EWM)"]
        n11["Post Goods Issue (EWM)"]
        n24(["fa:fa-stop Put-Away Task created/Confirmed"])
        n26{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph External Partners/ Supplier
        n1["PO received at Supplier End"]
        n2["Shipment notification to Supplier"]
        n23(["fa:fa-stop Supplier Notified"])
    end
    subgraph SAP S/4 Intel Foundry
        n12["Wafer to be reclaimed Inventory Updated"]
        n13["Custom FIORI App to enter Lot details"]
        n14["Inventory Transfer from IM S.Loc.(F501) to S.Loc (EWM) RS2 or AS1"]
        n15["Inventory updated at Rec. S.Loc"]
        n16["Create Return Purchase Order (Generic MMID)"]
        n17["Trigger GTS Check"]
        n18["Calculate Taxes"]
        n19["Purchase Order created"]
        n20["Return Delivery"]
        n21["Post Goods Issue/ Returns"]
        n22(["fa:fa-play Initiate Return"])
        n25(["fa:fa-stop Inventory Updated"])
        n27{{"fa:fa-arrows-alt parallelGateway"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n29{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n3 --> n4
    n4 --> n5
    n5 --> n26
    n26 --> n6
    n15 --> n25
    n6 --> n7
    n7 --> n8
    n8 --> n24
    n16 --> n27
    n27 --> n18
    n27 --> n17
    n19 --> n28
    n22 --> n16
    n9 --> n10
    n10 --> n11
    n2 --> n23
    n26 --> n15
    n14 --> n3
    n13 --> n12
    n17 --> n29
    n18 --> n29
    n29 --> n19
    n20 --> n9
    n11 --> n21
    n21 -->|"Via Websuite"| n2
    n28 --> n20
    n28 --> n1
    n12 --> n14
    class n22 startEvt
    class n23 endEvt
    class n24 endEvt
    class n25 endEvt
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV11v4jgU_StWRhUzEkzjkBDgYSUaSIXUbqvSmT5s98EkDlg1duQ4LWyH_752YgdIqbQfPFS9J-fcL99rwruT8BQ7Y-fi4p0wIsfgvSPXeIM7Y9BZogJ3uqAGfiJB0JLioqM5GWdyQf6qaNDPt5qmsRhtCN1pdIFXHIMf8y6YKCHtggKxoldgQbJOt5MLskFiF3HKhWZ_wcPMzapo5tEVFykWB4LrhjAJlJQShg9wP_RDP9a6AiecpSdOsyAbZklnr5Oj_C1ZIyGr9MsC36LtE0nlWtkZogVWnLXc0Bu0xFTXKEWpsaQUr7YZpNBxmGrYIkcJYSuF-66CBGIvByhw93uwv7h4Zk1QcPPwzID6JBQVxRRnoJAKnr1KkBFKx1_8aBIHbreQgr_g8RdvFk77XjfRlYxV6W5XN7f3hslqLcdLTlND7b3pGsZevu2K7dhzu2Kn_rZiYZYeIkUDb-gNm0hXIYxgZCNlWfa_Iqm-ikdUvJhYs37sxdMmFgwGQeR-9GfLnPrhBLb7hMUrSfCR0ziO-7NDq2aDALqfO72K-wM3ajldIYnf0O7gcBT5jcM4CGMYfuqwjtfOslzeC55Yh_1ZEAeNw_AKxhPvU4f-BPpDk6HysxIoX4PZ022N6A_r__HszNmSlywFU0zJKxa7iuL8ecTyFesHoxylag4_Pg7U43teSHDNeVqAB5xgksuPvME_5IWaV8reRHcy4iwjYoMk4Qy8EbkGeJvgvDIjtTDFqXaotJHA6hjApZGCxld11h_CjZTkrpStJtzpSwJ8Vexvp3ToHkIgpWiikORFt0dj96j-_5wcnnZhXhQlPkf0_K-KmaFxhnqF5HmrjKTKILVF4lSpvx3LB-_vVo6E4G9FD1EJciQQpZhe14P67Oz3tUitcntSthILhqiqRkiGRXEJFmWeU4LFcT26nDsg9GG-4hQg2bDAjKWtmhR5sSb5BjMJGJckI0l9spIfnJ9K-q02NN5_r_THhX-sYTG5B4tLH8yZxBTE-ojF7jh7ndETypQ7lcES6zooIqqdSvKqsuRqFH7kqW516xz16kSlSmkD4vndwxxM8lw7USLl7YZLkGKJCG0NKPSrlbO-H9UNX-jwmVCO5rdg8f2GJ9-_qjsbfqu6ou16PsDDwgNcgMkCtnwGJz7LOl99FGrHvtcuWorBYYgfsCwFU-Ml1DdKge3kX2N15iQBt7fzaXuG9YY-CrJaKeL14wJEa5y8tDjVJiKalFQHeUTb9qrCUbXnJ1HNVLdGQG-cydLuZ4txbqkuTWWtsJ53GKicqnWaq7cTcmhEe4-C1vydm4sTQfjvFq8WDf-LaHRWRFhCy0J16fMdZ33Q6_2mLnZj-rUZGDOoTW9gbG9QA9aGlmAF5nlozLA2h8YcGraNBg3ds3zPCOCwDVgGHBlJw_AMw-ZkCNC1CtcA0CqMh36rKGiLgKYLlgBNk6BnAZOVN7LAsAV4NosGMFk0CmgUTVYV8OvZ-UkQeMLLoiQSPzu_1BPLsEHcFmBdQNsK_-jdoeqQfRU8xfvmte0U9c-iwVl0YN9zTuHwPDw8D48s7HSdDVbf8CR1xu9O9ZNA_WxIcYZKKp1910Gl5IsdS5xx9ers1PfblCB1x29qcP83lDDF6A==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 E2E-116B_R3__Inbound_(Reclaim) — E2E-116B_R3__Inbound_(Reclaim)

**Swim Lanes**: Boundary Apps · EWM · External Partners/ Supplier · SAP S/4 Intel Foundry | **Tasks**: 18 | **Gateways**: 5

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
        n1["Receive Manual invoices through OCR"]
        n2["Receive Incoming invoice/ B2B/OpenText/Web suite"]
        n3["ReadSoft Validation/Exception Handling based on rules setup"]
        n24{{"fa:fa-code-branch B2B or OCR?"}}
        n25{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph EWM
        n8["Inbound Delivery distribution to EWM"]
        n9["Unloading EWM"]
        n10["Post Goods Receipt EWM"]
        n11["Put-Away Confirmation with Exception Codes"]
        n12["Create/Confirm Put-Away Task EWM"]
        n22(["fa:fa-stop Put-Away task Created/Confirmed"])
        n28{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph External Partners/ Supplier
        n4["Raise Invoice (Supplier End)"]
        n5["Purchase order received at Supplier End"]
        n6["Acknowledgement/ Review Purchase order"]
        n7["Goods Picked up (Carrier) Order Shipment"]
        n19(["fa:fa-play Acknowledge/ Review PO"])
        n20(["fa:fa-play Initiate Goods Pickup"])
        n21(["fa:fa-stop PO received"])
        n26{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4 Intel Foundry
        n13["Post Supplier invoice"]
        n14["Blanket Purchase Order"]
        n15["IBD against Blanket PO"]
        n16["GR against Inbound Delivery"]
        n17["Post Goods Receipt EWM"]
        n18["Evaluated Receipt Settlement (ERS) Self-Billing"]
        n23(["fa:fa-stop Invoice posted"])
        n27{{"fa:fa-code-branch Invoice Accepted?"}}
    end
    n25 --> n3
    n1 --> n25
    n24 -->|"OCR"| n1
    n3 --> n27
    n26 --> n4
    n4 --> n24
    n2 --> n25
    n27 -->|"Yes"| n13
    n24 -->|"B2B"| n2
    n27 -->|"No"| n26
    n5 --> n21
    n19 --> n6
    n20 --> n7
    n6 -->|"Via Web Suite"| n14
    n14 -->|"Via Web Suite"| n5
    n7 -->|"ASN via Web Suite"| n15
    n15 --> n8
    n8 --> n9
    n9 --> n10
    n10 --> n28
    n28 --> n11
    n28 --> n16
    n17 --> n18
    n18 --> n25
    n11 --> n12
    n12 --> n22
    n13 --> n23
    class n19 startEvt
    class n20 startEvt
    class n21 endEvt
    class n22 endEvt
    class n23 endEvt
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1tv4jgU_itWqopWApGEhFAedsQt3UrToSpz0WrYB5M4YNXYkeMA3Q7_fY-TmEtKpZGmD1X9-XzfudnH6ZsViZhYfev6-o1yqvroraFWZE0afdRY4Iw0mqgEvmNJ8YKRrKFtEsHVjP5XmDleutNmGgvxmrJXjc7IUhD07aGJBkBkTZRhnrUyImnSaDZSSddYvo4EE1JbX5FeYieFt2prKGRM5NHAtgMn8oHKKCdHuBN4gRdqXkYiweMz0cRPeknU2OvgmNhGKyxVEX6ekUe8-0FjtYJ1gllGwGal1uwzXhCmc1Qy11iUy40pBs20Hw4Fm6U4onwJuGcDJDF_OUK-vd-j_fX1nB-cos_Pc47gJ2I4y8YkQZkCeLJRKKGM9a-80SD07WampHgh_St3Eow7bjPSmfQhdbupi9vaErpcqf5CsLgybW11Dn033TXlru_aTfkKv2u-CI-PnkZdt-f2Dp6GgTNyRsZTkiR_5AnqKr_i7KXyNemEbjg--HL8rj-y3-uZNMdeMHDqdSJyQyNyIhqGYWdyLNWk6zv2x6LDsNO1RzXRJVZki1-Pgncj7yAY-kHoBB8Klv7qUeaLJykiI9iZ-KF_EAyGTjhwPxT0Bo7XqyIEnaXE6QoNRV6cZTRI06zc0z_c-Tm3nklE6IagR8xzzBDlGwEVypBaSZEvV2g6ep5b_56Q3BPSA4_EGs6pobXR0B22pynhX8lOtX-QBQRBFTlX6BQKOJ6JRKHvmNEYKyp4e7KLSKr_Qn9jHjOtq4dGjACROQwL6J_K01o43tvb3EpwP8EtPX1aC7g_0UoHgoTU4X-aW_v9KcO_zCC7iOUZpHVfNvRIgyNfq-jkx-OJYg8SeuALXWU0JgwkoNYxhR7RRV4kpERBOYv8DljfOBM41pm-23Zs2H8SmUL3QsQZKmqeqguGuo1PuWoN9CkcCZ5QuS4qirZUQayHso4g26xG1u0cSQIptysqOmgV9-SdP9e9-WnqlymRHu2Vti_FYqNGYmDfntJ7x_JjKcU2a2GmUIolZoyw3yn-ThHJ4bA-wdTjRGZtNMvTlFEiT_x4-pRhmulTWhxOdGOs0ITHt-dJ-UUNJcxXIBSPBZLlIY8RVuiUeU7sAnEQvXCxZSRewtPGVRt6taFki84Fz3kB8MrGPtHoBbzkKboZQUHAyy2aFhHMVjTVgrWW3R3rnzIo-4n7o-tpvex2jfUADzSFYqNjFMXdOiM59VZPD2Wpm3b__FbNBk9o1vYgNEUYCvV9kq-nmXfMlTj0oxo8tQrp3g8ZvKNEHZswfd8ER7f9YThGeIkpB90DaVoz1G2-fz7Y1W97zTr43aurJ8dkg1mur8zBbkaUYsVRQjeT59ktACxpDeE5gElRu4ydWofMYU_B_fsmBZebZEiDSI8KEn-60CWYm6jV-gvGd7V2yqXrm31PA7_mVvFk_AKDaqNTGQbGsFsCXrX2qn2zduvCQSX8j55eWrhTdwnTvthx65QvosS71UaVg2tic-5KwOy7drk2sXYrne8UI_2czcrnTAdhwnW8D21MBiaawewL2rxXMmZOFV2vWvfK5V21rEJ1bGNexeoae7ciOE4dMOk5QQUYitOrFdup2uqYUjqmHQfA9LNz8t1SVNJ8hp7hUNHLuFN9Sp6j7kW0cxH1zLfXOexfhruX4eAy3DOw1bTWBB5UGlv9N6v47wX-w4lJgnOmrH3TwrkSs1ceWf3iK9_KU_ieIWOKYaitS3D_P3F1Bwc=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| EWM | E2E-116A_R3__Outbound_(Return)_Straddle_&amp;_End_State, E2E-116B_R3__Inbound_(Reclaim) | |
| External Partners/ Supplier | E2E-116A_R3__Outbound_(Return)_Straddle_&amp;_End_State, E2E-116B_R3__Inbound_(Reclaim) | |
| SAP S/4 Intel Foundry | E2E-116A_R3__Outbound_(Return)_Straddle_&amp;_End_State, E2E-116B_R3__Inbound_(Reclaim) | |
| Boundary Apps | E2E-116B_R3__Inbound_(Reclaim) | |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
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

    subgraph E2E116CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E116CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E116CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E116CDAA_e_g_XEUS -.-> E2E116CDAD_e_g_Azure_SQL
    end
    style E2E116CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E116CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E116CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E116CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E116CDAA_e_g_MES_300 -.-> E2E116CDAD_e_g_SAP_HANA
    end
    style E2E116CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E116CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E116CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYFumzAQhl_FchVlk5KOJCVZkVrJCWStRKuupNukMiEHjsSqAwjMmjTNu8-GhG5Z6KraEsLnu__O3yGzxn4cADZwo7FmERMGWjfFHBbQNFBzSjNotlAzAz9PmVjZ8Au42uBxXO4Urt9oyuiUQ9ZU0WEcCYc9FQIdPVkqN2Ub0wXjK2V1YBYDurtsISIDeXOjPHj86M9pKgqNPIMruvzOAjGX65DyDKTPXCy4TafAVSKR5soWyeqdhPosmkljT5emlEYPL6YTfbNBm0bDjaoUaDJ0IySHz2mWmRAimiTDeIlCxrlxNNTN8XjcykQaP4BxpGmDwbC_XbYfVU1GN1m2_JjHqdrumfq-XjAdrfhWjuhmnwwqua41MHvdWrnOULe62p4cxPylvPF4qA_1Sm800uSo1ev31bYblYpZPp2lNJkjq2t1Ov2RSUa2B97MI095Cp7z1b53MXLxz9JdjYCl4AsWRxU1Nap4UoT_sO4cGQnHs2Ok3qWCYRgl1QNB5l7ODy528-BzL5DPwD9x8xA0eWqlVjgh6eTij0qzIPtqHah93D6vzVWGQhRsgYgVh3oaO-REzQq5pan5N_JOsvwvZIfceBfkmryP8ZXleD1N22GWSySXbyJdJX4FtPRByudNnLe1HES9S_Ym0jvnd4GuSYzOzs6ft5TMgiz6hMjNpXyOGQcXP7_ydey10IaZPMH9H9j8QEMmmRBEbkcXlxNrNLm7tZBtfbGuzZqm2rcvVttT7SdJwplP1e7hBtqeWdMskwqq7uXDfbI9S8pbUdCOw7bNQijlywvkYEfKE-7462pW_E9PT_-Bj1t4AemCsgAba1zc__LvEUBIcy7wpoVpLmJnFfnYKK5onCcBFWAyKokuSuPmN4Cc9-8=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E116FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E116FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E116FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E116FDAA_e_g_XEUS -.-> E2E116FDAD_e_g_Azure_SQL
    end
    style E2E116FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E116FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E116FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E116FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E116FDAA_e_g_MES_300 -.-> E2E116FDAD_e_g_SAP_HANA
    end
    style E2E116FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E116FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E116FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYFumzAQhl_FchVlk5KOJCVZkVrJCbBWolVX0m1SmZADR2LVAQRmTZrm3WdDQrcs6araEsLnu__O3yGzwkESAjZwo7FiMRMGWjXFDObQNFBzQnNotlAzh6DImFg68Au42uBJUu2Urt9oxuiEQ95U0VESC5c9lQIdPV0oN2Wz6ZzxpbK6ME0A3V22EJGBvLlWHjx5DGY0E6VGkcMVXXxnoZjJdUR5DtJnJubcoRPgKpHICmWLZfVuSgMWT6Wxp0tTRuOHF9OJvl6jdaPhxXUKNB56MZIj4DTPTYgQTdNhskAR49w4GuqmbdutXGTJAxhHmjYYDPubZftR1WR000UrSHiSqe2eqe_qhZPRkm_kiG72yaCW61oDs9c9KNcZ6lZX25GDhL-UZ9tDfajXeqORJsdBvX5fbXtxpZgXk2lG0xmyulan07dNMnJ88Kc-eSoy8N2vzr2HkYd_Vu5qhCyDQLAkrqmpUceTMvyHdefKSDieHiP1LhUMw6io7gkyd3J-8LBXhJ97oXyGwYlXRKDJUyu10glJJw9_VJol2VfrQO3j9vnBXFUoxOEGiFhyOExji5yoWSO3NDX_Rt5JF_-F7JIb_4Jck_cxvrJcv6dpW8xyieTyTaTrxK-Alj5I-byJ86aWvai3yd5Eeuv8LtAHEqOzs_PnDSWzJIs-IXJzKZ824-Dh51e-jp0WOjCVJ7j_A1sQasgkY4LI7ejicmyNxne3FnKsL9a1eaCpzu2L1fFV-0machZQtbu_gY5vHmiWSQVV9_L-Pjm-JeWtOGwnUdthEVTy1QWytyPVCbf8dTVr_qenp__Axy08h2xOWYiNFS7vf_n3CCGiBRd43cK0EIm7jANslFc0LtKQCjAZlUTnlXH9G_1S-Bk=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-116-R001 | Report | R3 Wafer Reclaim Process operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-116-C001 | Conversion | Legacy data migration for R3 Wafer Reclaim Process | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-116.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E116C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E116C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E116CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E116CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E116C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E116CMW_e_g_Azure_Service_Bus
    E2E116CMW_e_g_Azure_Service_Bus --> E2E116C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVf1P6jAU_VeaGcIvoENl4GJINjZeeBlqnB_v5fGylPUCjWVb1k5F5H9_7YaML6OvJCO7Pffc7tzTdqGFMQHN1CqVBY2oMNGiKqYwg6qJqiPMoVpDVQ5hllIx9-AZmJpgcVzM5NAHnFI8YsCrKnscR8KnbzlBw0heFUzFenhG2VxFfZjEgO77NWTJRFZDHEe8ziGl4-pSoVn8Ek5xKnK-jMMAvz5SIqbyfYwZB4mZihnz8AiYKirSTMUi-SV-gkMaTWTwXJehFEdPZaipL5doWakMo3UJdGcPIyRHpYLqdbmgcEoHWECdRjyhKRDExZwBChnmHLjEFPD83YExGmWcRsA5yseYMmYe9eSwmzUu0vgJzCO73TZ0e_Vaf1FfYp4mr7UwZnFqHum6vsOJkwSVo-C0m4p1zanrrZZt_AcnwQLvczrtLzgbW5wfcwRzKV6K51JT1NypNKOEMHjBKWwq4hhWqYjbMnol2zdWDzHbU0RpvKFyt6vrX3EWrDwbTVKcTJHl_Rlqw4y0z4h8krMmsm5uvH7XuutfXyHP-u3eDrW_RZIaRBoiFDSOkHdbRt1Tt9EwugEEk2Dg-sGZrm_ShmAgOJ4cIzmH5JxkNE1Ttvgwwy_33j-YriY-zx085tnWW5ZC4EP6TEMI7IxvfWCjVVDlKLRCIYkqeMvG7dE7bk7fjbkIXCb3fCQ6m4sMzwtmBUArwOUoPelc0k4x4T-gE9R34lD-_fSvry5PaKcoq5xZFISIfPTogKhy73Xeh1pO5-SdkFTWTV8-e5TBUHv_Sowt6s9AqsxeR9SyVubJjwPb29jqPf2rrb6Zaq1T9e_s6D3TejCROm1ZhOjIc3-4V8433OoF0uO7BrOShNEQK_ABi3nB4HHXR4PSK596xwscd9cljjqG3EjI22S3-0WKe11sylODnEsgqcfjukfHqzLyHNiwSilqIcqHsE31Wwt7cXGxd6ZpNW0G6QxTopkLLb_F5B1IYIwzJrRlTcOZiP15FGpmfrloWSIXCg7FsgmzIrj8B6-sPuk=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-116.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E116F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E116F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E116FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E116FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E116F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E116FMW_e_g_Azure_Service_Bus
    E2E116FMW_e_g_Azure_Service_Bus --> E2E116F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVf1P6jAU_VeaGcIvoENl4GJINjdeeBlqnB_v5fGylPUCjWVb1k5F5H9_7YaML4OvJCO7Pffc7tzTdq6FMQHN1CqVOY2oMNG8KiYwhaqJqkPMoVpDVQ5hllIx8-AFmJpgcVzM5NBHnFI8ZMCrKnsUR8Kn7zlBw0jeFEzFunhK2UxFfRjHgB56NWTJRFZDHEe8ziGlo-pCoVn8Gk5wKnK-jEMfvz1RIibyfYQZB4mZiCnz8BCYKirSTMUi-SV-gkMajWXwXJehFEfPZaipLxZoUakMolUJdG8PIiRHpYLqdbmgcEL7WECdRjyhKRDExYwBChnmHLjEFPD83YERGmacRsA5yseIMmYedeWwmzUu0vgZzCO73TZ0e_laf1VfYp4mb7UwZnFqHum6vsWJkwSVo-C0m4p1xanrrZZt_AcnwQLvcjrtA5yNDc7POYK5FC_FM6kpam5VmlJCGLziFNYVcQyrVMRtGd2S7Rurh5jtKKI0XlP56krXD3EWrDwbjlOcTJDl_Rlog4y0z4h8krMmsm5vvd6Vdd-7uUae9du9G2h_iyQ1iDREKGgcIe-ujLqnbqNhdAMIxkHf9YMzXV-nDcFAcDw-RnIOyTnJaJqmbPF-hl_ug783XU18ndt_yrOt9yyFwIf0hYYQ2Bnf-MBGq6DKUWiJQhJV8JaN26F33Jz-KuYicJnc85HorC8yPC-YFQAtAZfD9KRzSTvFhP-ITlDPiUP599O_ub48oZ2irHJmURAi8tmjPaLKvdf5GGg5nZN3QlJZtz357FIGA-3jkBgb1F-BVJmdjqhlLc2THwe2t7bVu_qhrb6eaq1S9e_s6B3TejCWOm1YhOjIc3-418433OoF0uPbBrOShNEQK_Aei3lB_2nbR_3SK196xwscd9sljjqG3EjI22S7-0WKe1NsylODnEsgqcejukdHyzLyHFizSilqIcqnsE31Wwl7cXGxc6ZpNW0K6RRToplzLb_F5B1IYIQzJrRFTcOZiP1ZFGpmfrloWSIXCg7FsgnTIrj4B_ZxPwE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-116-I001 | Interface | R3 Wafer Reclaim Process inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-116-E001 | Enhancement | R3 Wafer Reclaim Process custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-116-F001 | Form/Report | R3 Wafer Reclaim Process operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
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

    subgraph E2E116CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E116CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E116CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E116CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E116CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E116CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E116CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E116CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJBJohdRIQ0CqlUzTWbdKYkANHYtXBCMyaNOW_z4YuWSulUrX5g8W9d358fi28xxnPAbt4NNrTkgoX7TWxhg1oLtKWpAFNR1oDWVtTsZvDL2AqwTgfMn3pV1JTsmTQaGp1wUsR04ceMJ5UW1WmtIhsKNspNYYVB3R7rSNPLmRapyoYv8_WpBY9o23ghmy_0VysZVwQ1oCsWYsNm5MlMLWRqFullbL7uCIZLVdSnBhSqkl5d5Rso-tQNxol5WEL9MVPSiRHxkjTzKBApKp8vkUFZcw98-1ZFEV6I2p-B-6ZYVxe-s5T-O5e9eSa1VbPOOO1Slsz-yWvYkQcgcE0dIL3B6A1nYZW8BxoHYFj3w5N4wUQODvyosi3ffvACwJDjpMNOo5KJ-VAbNrlqibVGoVmOB47wWK-SCFdpd5DW0O6ICT-keCkNR1jnLQFGHLr89U56tNIpRP8cyCpkdMaMkF5ieafj-oB7fXo7-GtgvYc9S0JrusOlg-LoMyfuhM7Bqdb-yc_Xz9_nE7Sj94nLzUN0-otyKdWLuec2H8bEV9MkKpDqu7tXtyEcWoZxh87ZIhk-FZHnjX7H0x5FX919eHxqd1Zf0R0gbzFtZwjyiDBj6fvC-t4A_WG0By7e9y_FfKlyaEgLRO40zFpBY93ZYbd_nfGbZUTATNK5B1tBrH7DY7zb9o=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E116FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E116FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E116FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E116FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E116FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E116FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E116FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E116FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlGFvmzAQhv-K5SriC2sJBJohdRIkoFVKp2is26QxIQeOxKrBCMyaNOW_z4YuWSulUrX5g8W9d358fi28xynPALt4NNrTkgoX7TWxgQI0F2kr0oCmI62BtK2p2C3gFzCVYJwPmb70K6kpWTFoNLU656WI6EMPGE-qrSpTWkgKynZKjWDNAd1e68iTC5nWqQrG79MNqUXPaBu4IdtvNBMbGeeENSBrNqJgC7ICpjYSdau0UnYfVSSl5VqKE0NKNSnvjpJtdB3qRqO4PGyBvvhxieRIGWmaOeSIVJXPtyinjLlnvj0Pw1BvRM3vwD0zjMtL33kK392rnlyz2uopZ7xWaWtuv-RVjIgjcDYNnNn7A9CaTgNr9hxoHYFj3w5M4wUQODvywtC3ffvAm80MOU426DgqHZcDsWlX65pUGxSYwXjshMvFMoFknXgPbQ3JkpDoR4zj1nSMcdzmYMitz9fnqE8jlY7xz4GkRkZrSAXlJVp8PqoHtNejvwe3Ctpz1LckuK47WD4sgjJ76k7sGJxu7Z_8fP38UTJJPnqfvMQ0TKu3IJtamZwzYv9tRHQxQaoOqbq3e3ETRIllGH_skCGS4VsdedbsfzDlVfzV1YfHp3bn_RHRBfKW13IOKYMYP56-L6zjAuqC0Ay7e9y_FfKlySAnLRO40zFpBY92ZYrd_nfGbZURAXNK5B0Vg9j9BrIYb_I=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
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

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-116 — R3 Wafer Reclaim Process</span></div>
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
*E2E-116 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

