<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-91 — R3 Bill of Material BOM Data</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-91 · Master Data</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-91 R3 Bill of Material BOM Data** within the IAO program. It includes 1 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Master Data |
| **Capability** | E2E-91 - R3 Bill of Material BOM Data |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Master Data |
| **L2 Capability** | E2E-91 - R3 Bill of Material BOM Data |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-91 Process Migration | Migrate R3 Bill of Material BOM Data business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-91 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **1 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-91 R3 Bill of Material BOM Data.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-91_R3_Bill_of_Material_BOM_Data | E2E-91_R3_Bill_of_Material_BOM_Data | Boundary Apps, Intel Foundry 
SAP S/4, Intel Product 
SAP S/4 | 9 | 3 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 E2E-91_R3_Bill_of_Material_BOM_Data — E2E-91_R3_Bill_of_Material_BOM_Data

**Swim Lanes**: Boundary Apps · Intel Foundry 
SAP S/4 · Intel Product 
SAP S/4 | **Tasks**: 9 | **Gateways**: 3

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
        n3["Fetch Data in PDM Translator"]
        n4["Update IP MD Zone (ECA)"]
        n5["Update Data from ECM"]
        n6["Update IF MD Zone (ECA)"]
        n7["Update in Boundary Apps"]
        n8["fa:fa-user Update ENT HANA BOM"]
        n9["fa:fa-user Fetch Data from Speed"]
        n10(["fa:fa-play Bill of Material Data Update Process Initiated"])
        n11(["fa:fa-play ECM Bill of Material Data Update Process Initiated"])
        n12(["fa:fa-stop Bill of Material Data Updated"])
        n13{{"fa:fa-code-branch IP or IF?"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
        n15{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Intel Foundry  SAP S/4
        n1["Update Intel Foundry BOM Data Master"]
    end
    subgraph Intel Product  SAP S/4
        n2["Update Intel Product BOM Data Master"]
    end
    n10 --> n9
    n9 --> n14
    n14 --> n3
    n15 --> n7
    n7 --> n12
    n8 --> n15
    n4 --> n15
    n6 --> n15
    n3 --> n13
    n13 -->|"Intel Product (IP)"| n2
    n1 --> n6
    n11 --> n5
    n5 --> n14
    n13 -->|"Intel Foundry (IF)"| n1
    n2 --> n4
    class n8 userTask
    class n9 userTask
    class n10 startEvt
    class n11 startEvt
    class n12 endEvt
    class n13 gateway
    class n14 gateway
    class n15 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqlVtuO4kYQ_ZWWRyNmJaP4ihk_JDIGJ0jLBoXZRErIQ2O3h9YYt9XdnoGw_HuqfQHsHTaKlgekOj51Tld1UfioxSwhmq_d3x9pTqWPjgO5JTsy8NFggwUZ6KgGfsec4k1GxEBxUpbLFf2noplOsVc0hUV4R7ODQlfkmRH0ea6jABIzHQmci6EgnKYDfVBwusP8ELKMccW-I-PUSCu35tGE8YTwC8EwPDN2ITWjObnAtud4TqTyBIlZnnREUzcdp_HgpA6Xsbd4i7msjl8KssD7P2gitxCnOBMEOFu5yz7iDclUjZKXCotL_to2gwrlk0PDVgWOaf4MuGMAxHH-coFc43RCp_v7dX42RR9_W-cIPnGGhZiSFAkJ8OxVopRmmX_nhEHkGrqQnL0Q_86aeVPb0mNViQ-lG7pq7vCN0Oet9DcsSxrq8E3V4FvFXud73zJ0foDvnhfJk4tTOLLG1vjsNPHM0AxbpzRNv8sJ-sqfsHhpvGZ2ZEXTs5fpjtzQ-FqvLXPqeIHZ7xPhrzQmV6JRFNmzS6tmI9c0botOIntkhD3RZyzJGz5cBB9D5ywYuV5kejcFa7_-KcvNkrO4FbRnbuSeBb2JGQXWTUEnMJ1xc0LQeea42KIJK6tZRkFRiPqZ-uT2X2stIjLeoimWGNEcLacL9AQDKDIsGV9rf1-xHWB_LhKoFs2XaDFFf7KcoIdZGHzoEt0LsdJNOduhWbjoskZXctG35LwLEU7YraVDHAMxxX6Kh2pyUJMz-_SEfgk-BWjya-8Ej13-VSeqE68KQpJuhmk8nHOKDO58AleEWIoW4KQWU53eOKtLJEKgOaxCCoAS-3CtZvbUoEffqWhdFIVkxTfVvkq2j8c2We3x4QYGAToCl8043NFPa-10uuY77_PJPs5KQV_Jz_UPo5_m_t802Di9gZ7nkmQoUqMAk4BWwRKtfnCuTa6Gq8OFIah7sMACWnK-3lse0PGkjOV7Hlbfo-X-pwfMERoOf4QJbOLHOjSd9rlTA3Ybu3XsNbHX8K0mHjex28ROLx71YruJz_oV8GWtdQt5mC_ht_gFSm15dd6oDZu4lXX7ZXRl2zt4mEe1bLOec6vOc672oKqp3f8d-PF9GDra_gl2cfMGbjV_ZF3Ubrd5F3beh90W1nRtR_gO00Tzj1r1hgNvQQlJcZlJ7aRruJRsdchjza_eBLSympspxTBruxo8_QsQK9ii" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-91_R3_Bill_of_Material_BOM_Data | |
| Intel Foundry 
SAP S/4 | E2E-91_R3_Bill_of_Material_BOM_Data | |
| Intel Product 
SAP S/4 | E2E-91_R3_Bill_of_Material_BOM_Data | |

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
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

    subgraph E2E91CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E91CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E91CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E91CDAA_e_g_XEUS -.-> E2E91CDAD_e_g_Azure_SQL
    end
    style E2E91CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E91CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E91CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E91CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E91CDAA_e_g_MES_300 -.-> E2E91CDAD_e_g_SAP_HANA
    end
    style E2E91CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E91CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E91CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9vmkAUx_-VyzXGLdEOtegkaZNTcG1Cm67YbUlZyAkPvfQEAkertf7vuwOlm9Wu6V1CvPfj-x6fR84V9uMAsIFrtRWLmDDQqi5mMIe6geoTmkG9geoZ-HnKxNKGB-DKweO49BShP2jK6IRDVlfZYRwJhz0VAi09WagwZRvROeNLZXVgGgO6vWggIhN5fa0iePzoz2gqCo08g0u6-MkCMZPnkPIMZMxMzLlNJ8BVIZHmyhbJ7p2E-iyaSmNHl6aURvcvphN9vUbrWs2NqhJoPHAjJJfPaZaZECKaJIN4gULGuXE00M3RaNTIRBrfg3Gkab3eoLs5Nh9VT0Y7WTT8mMepcndMfVcvmAyXfCNHdLNLepVc2-qZnfZBudZAt9rajhzE_KW90WigD_RKbzjU5Dqo1-0qtxuVilk-maY0mSGrbfVbQ5MMbQ-8qUee8hQ857t952Lk4t9ltFoBS8EXLI4qaGpt00mR_cu6dWQiHE-PkfotBQzDKJm-zjF3Kn5ysZsHXzuBfAb-iZuHoMlXVmJFEJJBLv6sJAusb3WBmsfNs0OVykSIgg0LseRwEMQWNlG7gm1pav8Lu5Us_ofXIdfeObkiH6J7aTleR9O2gOURyeN7GFdl30AsY5CKeQ_hTSf7IG9LvYfxNvZDiPeXRaenZ88bQGbBFH1B5PpCPkeMg4ufD38UO6OzYSrbv_uLmB9oyCRjgsjN8PxibA3HtzcWsq1v1pV5YJr2zYvV9tTcSZJw5lPl3T862zMPzMmkgqqbeP-IbM-S8lYUNOOwabMQSvnyytg7jvINt_R1tSv6_X7_FXrcwHNI55QF2Fjh4saX_xcBhDTnAq8bmOYidpaRj43iUsZ5ElABJqOS6Lw0rv8AHAX1aw==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '15px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 35, 'rankSpacing': 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E91FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E91FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E91FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E91FDAA_e_g_XEUS -.-> E2E91FDAD_e_g_Azure_SQL
    end
    style E2E91FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E91FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E91FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E91FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E91FDAA_e_g_MES_300 -.-> E2E91FDAD_e_g_SAP_HANA
    end
    style E2E91FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E91FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E91FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqdlY9vmkAUx_-VyzXGLdEOtegkaZNTYG1Cm67YbUlZyAkPvfQEAkertf7vuwO1m9Wu6V1CvPfj-x6fR84lDpIQsIFrtSWLmTDQsi6mMIO6gepjmkO9geo5BEXGxMKBB-DKwZOk8pShP2jG6JhDXlfZURILlz2VAi09naswZbPpjPGFsrowSQDdXjQQkYm8vlIRPHkMpjQTpUaRwyWd_2ShmMpzRHkOMmYqZtyhY-CqkMgKZYtl925KAxZPpLGjS1NG4_sX04m-WqFVrebF2xJoNPBiJFfAaZ6bECGapoNkjiLGuXE00E3bthu5yJJ7MI40rdcbdNfH5qPqyWin80aQ8CRT7o6p7-qF4-GCr-WIbnZJbyvXtnpmp31QrjXQrba2IwcJf2nPtgf6QN_qDYeaXAf1ul3l9uJKMS_Gk4ymU2S1rX7LNsnQ8cGf-OSpyMB3vzt3HkYe_l1FqxWyDALBkngLTa1NOimzf1m3rkyE48kxUr-lgGEYFdPXOeZOxU8e9orwayeUzzA48YoINPnKSqwMQjLIw5-VZIn1rS5Q87h5dqhSlQhxuGYhFhwOgtjAJmpvYVua2v_CbqXz_-F1ybV_Tq7Ih-heWq7f0bQNYHlE8vgextuybyCWMUjFvIfwupN9kDel3sN4E_shxPvLotPTs-c1ILNkir4gcn0hnzbj4OHnwx_FzugcmMj27_4iFoQaMsmIIHIzPL8YWcPR7Y2FHOubdWUemKZz82J1fDV3kqacBVR594_O8c0DczKpoOom3j8ix7ekvBWHzSRqOiyCSr66MvaOo3rDDX1d7S39fr__Cj1u4BlkM8pCbCxxeePL_4sQIlpwgVcNTAuRuIs4wEZ5KeMiDakAk1FJdFYZV38Al6r1lQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-91-R001 | Report | R3 Bill of Material BOM Data operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-91-C001 | Conversion | Legacy data migration for R3 Bill of Material BOM Data | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-91.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E91C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E91C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E91CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E91CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E91C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E91CMW_e_g_Azure_Service_Bus
    E2E91CMW_e_g_Azure_Service_Bus --> E2E91C_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1P4kAQ_iubGsIX0KLy1hiSlpYLl6LG-nKX49Is3QE2Lm3T3aqI_PfbbZFi0eAtSUlnnnlm-8zM7koLIgKaoVUqKxpSYaBVVcxhAVUDVSeYQ7WGqhyCNKFi6cITMOVgUZR7Mug9TiieMOBVFT2NQuHR14yg0YpfFEzZBnhB2VJZPZhFgO6GNWTKQFZDHIe8ziGh0-paoVn0HMxxIjK-lMMIvzxQIubyfYoZB4mZiwVz8QSYSiqSVNlC-SVejAMazqTxXJemBIePhampr9doXamMw20KdGuNQyRXpYLqdbmhYE5HWECdhjymCRDExZIBChjmHLjE5PDs3YYpmqSchsA5ytaUMmYcDeSymjUukugRjCOr02np1ua1_qy-xDiNX2pBxKLEONJ1vcSJ4xgVK-e0mop1y6nr7bbV-g9OggXe57Q7BzgbHzjffQRzKV6Cl1JT1CxlWlBCGDzjBHYVsVtmoYjTbg0Ktm_sHiK2p4jSeEflfl_XD3HmrDydzBIcz5Hp_hlr45R0zoh8krMmMq-v3WHfvB1eXSLX_O3cjLW_eZBaRDZEIGgUIvemsDqnTrfR98Gf-SPH8890fZc1gBaC49kxkj4kfZLQMAxZ4U8Jfjl33qfRyvFl6OghCzZf0wR8D5InGoBvpfzD1zXaOVOGQhsUkqictqhamd12MvZ-xIXvMDnvoejtbjE4z4kVAG0AF5PkpHdBe7nDu0cnaGhHgfz76V1dXpzQXp5VdWWeD0LyXp99QeXY9d7GWsZmZ0WQTOb1UD4HlMFYezugxC7xVxiVpFwLtaVN02THgOXujPhAPzTiu6HmNlT_ziTvNasLM6nRh-YgOnKdH86l_Y0udX3Z2-XWMuOY0QAr8CfN5fqjh3ILjYo2-bJtXN92yh1iq-PHCYW8RcqVz0Ocq3wYT1vkXAJJPZrWXTrdpJHzv9Mmhai5KO_CNtVvK2y32907y7SatoBkgSnRjJWW3V7y7iMwxSkT2rqm4VRE3jIMNCO7VLQ0lhsFm2JZhEVuXP8D6r09eQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-91.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E91F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E91F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E91FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E91FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E91F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E91FMW_e_g_Azure_Service_Bus
    E2E91FMW_e_g_Azure_Service_Bus --> E2E91F_e_g_XEUS

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqVVW1P4kAQ_iubGsIX0KLy1hiSlpYLl6LG-nKX49Is3QE2Lm3T3aqI_PfbbZFi0eAtSUlnnnlm-8zM7koLIgKaoVUqKxpSYaBVVcxhAVUDVSeYQ7WGqhyCNKFi6cITMOVgUZR7Mug9TiieMOBVFT2NQuHR14yg0YpfFEzZBnhB2VJZPZhFgO6GNWTKQFZDHIe8ziGh0-paoVn0HMxxIjK-lMMIvzxQIubyfYoZB4mZiwVz8QSYSiqSVNlC-SVejAMazqTxXJemBIePhampr9doXamMw20KdGuNQyRXpYLqdbmhYE5HWECdhjymCRDExZIBChjmHLjE5PDs3YYpmqSchsA5ytaUMmYcDeSymjUukugRjCOr02np1ua1_qy-xDiNX2pBxKLEONJ1vcSJ4xgVK-e0mop1y6nr7bbV-g9OggXe57Q7BzgbHzjffQRzKV6Cl1JT1CxlWlBCGDzjBHYVsVtmoYjTbg0Ktm_sHiK2p4jSeEflfl_XD3HmrDydzBIcz5Hp_hlr45R0zoh8krMmMq-v3WHfvB1eXSLX_O3cjLW_eZBaRDZEIGgUIvemsDqnTrcx8MGf-SPH8890fZc1gBaC49kxkj4kfZLQMAxZ4U8Jfjl33qfRyvFl6OghCzZf0wR8D5InGoBvpfzD1zXaOVOGQhsUkqictqhamd12MvZ-xIXvMDnvoejtbjE4z4kVAG0AF5PkpHdBe7nDu0cnaGhHgfz76V1dXpzQXp5VdWWeD0LyXp99QeXY9d7GWsZmZ0WQTOb1UD4HlMFYezugxC7xVxiVpFwLtaVN02THgOXujPhAPzTiu6HmNlT_ziTvNasLM6nRh-YgOnKdH86l_Y0udX3Z2-XWMuOY0QAr8CfN5fqjh3ILjYo2-bJtXN92yh1iq-PHCYW8RcqVz0Ocq3wYT1vkXAJJPZrWXTrdpJHzv9Mmhai5KO_CNtVvK2y32907y7SatoBkgSnRjJWW3V7y7iMwxSkT2rqm4VRE3jIMNCO7VLQ0lhsFm2JZhEVuXP8DMT09kQ==" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
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

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-91-I001 | Interface | R3 Bill of Material BOM Data inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-91-E001 | Enhancement | R3 Bill of Material BOM Data custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-91-F001 | Form/Report | R3 Bill of Material BOM Data operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
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

    subgraph E2E91CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E91CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E91CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E91CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E91CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E91CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E91CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E91CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRF6iQgoFVKp2is26QxIQeOxKqDEZg1acp_nw1pslZKpWrzB4t77_z49Vl4h1OeAXbwYLCjBRUO2mliBWvQHKQtSA2ajrQa0qaiYjuD38BUgnHeZ7rSb6SiZMGg1tTqnBcioo8dYDgqN6pMaSFZU7ZVagRLDujuRkeuXMi0VlUw_pCuSCU6RlPDLdl8p5lYyTgnrAZZsxJrNiMLYGojUTVKK6T7qCQpLZZSHBlSqkhxf5Rso21ROxjExWEL9NWLCyRHykhdTyFHpCw9vkE5Zcw58-xpGIZ6LSp-D86ZYVxeeuN9-OFBeXLMcqOnnPFKpa2p_ZpXMiKOQH8SjP2rA9CaTALLfwm0jsChZwem8QoInB15YejZnn3g-b4hx0mD47FKx0VPrJvFsiLlCgVmcDX057N5AskycR-bCpI5IdHPGMeNOTaGcZODIXc-X56jLo1UOsa_epAaGa0gFZQXaPblqD6T3Y78I7hTzA6jviXAcZy-4f0aKLK9N7FlcNLYPzXzzcNHySj55H52E9Mwre782cTK5JwR--8uRBcjpOqQqnt3I26DKLEM47kXMkQyfGc7Xlj9Dx15i359_fFpb3banQ9dIHd-I-eQMojx08mrwjpeQ7UmNMPODndvhHxhMshJwwRudUwawaNtkWKn-41xU2ZEwJQSeT3rXmz_AJE-bmo=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
<div style="page-break-before: always;"></div>

#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {'theme': 'base', 'securityLevel': 'loose', 'themeVariables': {'fontSize': '14px', 'fontFamily': 'Segoe UI, Arial'}, 'flowchart': {'useMaxWidth': false, 'htmlLabels': true, 'nodeSpacing': 40, 'rankSpacing': 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E91FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E91FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E91FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E91FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E91FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E91FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E91FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E91FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/edit#pako:eNqtlGFvmzAQhv-K5SriC2sJhDRF6iRIQKuUTtFYt0ljQg4ciVWDEZg1acp_nw1pslZKpWrzB4t77_z49Vl4hxOeAnbwYLCjBRUO2mliDTloDtKWpAZNR1oNSVNRsZ3Db2AqwTjvM13pN1JRsmRQa2p1xgsR0scOMByVG1WmtIDklG2VGsKKA7q70ZErFzKtVRWMPyRrUomO0dRwSzbfaSrWMs4Iq0HWrEXO5mQJTG0kqkZphXQfliShxUqKI0NKFSnuj5JttC1qB4OoOGyBvnpRgeRIGKnrGWSIlKXHNyijjDlnnj0LgkCvRcXvwTkzjMtLb7wPPzwoT45ZbvSEM16ptDWzX_NKRsQROJ344-nVAWhNJr41fQm0jsChZ_um8QoInB15QeDZnn3gTaeGHCcNjscqHRU9sW6Wq4qUa-Sb_tUwWMwXMcSr2H1sKogXhIQ_Ixw15tgYRk0Ghtz5fHWOujRS6Qj_6kFqpLSCRFBeoPmXo_pMdjvyD_9OMTuM-pYAx3H6hvdroEj33sSWwUlj_9TMNw8fxqP4k_vZjU3DtLrzpxMrlXNK7L-7EF6MkKpDqu7djbj1w9gyjOdeyBDJ8J3teGH1P3TkLfr19cenvdlZdz50gdzFjZwDyiDCTyevCus4hyonNMXODndvhHxhUshIwwRudUwawcNtkWCn-41xU6ZEwIwSeT15L7Z_ALQPboI=" title="Edit in Mermaid Live">&#9998; Edit in Mermaid Live</a></div>

> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>

#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
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

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-91 — R3 Bill of Material BOM Data</span></div>
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
*E2E-91 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*

