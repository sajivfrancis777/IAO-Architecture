<div style="text-align:center; padding-top:60px;">
  <h1 style="font-size:36px; margin-top:24px;">Finance Plan To Report (FPR)</h1>
  <h2 style="font-size:24px;">TOGAF BDAT — Aggregated Architecture View</h2>
  <p style="font-size:18px; color:#555;">Tower: Finance Plan To Report (FPR) · R1 – R5</p>
  <p style="font-size:14px; color:#888;">IAO Program · R1 – R5<br/>
  Generated: April 2026<br/>
  Sajiv Francis</p>
  <p style="font-size:12px; color:#aaa;">IAO Architecture Pipeline — Intel Confidential</p>
</div>

<style>
@media print {
  @page { size: A4; margin: 0; }
  .mermaid { page-break-inside: avoid; break-inside: avoid; overflow: visible; }
  pre, table, blockquote { page-break-inside: avoid; break-inside: avoid; }
  h2, h3, h4 { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
  a[title="View full diagram"],
  a[title="Open full-size SVG"] {
    color: #0071c5 !important;
    text-decoration: underline !important;
    font-size: 10pt !important;
  }
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
  margin-top: auto;
  padding: 6px 0;
  background: #fff;
}
@media print {
  .page-footer {
    display: none !important;
  }
}
.page-footer a { color: #00aeef; text-decoration: none; font-weight: 500; }
.page-footer a:hover { color: #0071c5; text-decoration: underline; }
nav.toc { margin: 16px 0 24px 0; }
nav.toc ol, nav.toc ul { list-style: none; padding-left: 0; margin: 0; }
nav.toc > ol > li { margin-bottom: 6px; font-weight: 600; font-size: 14px; }
nav.toc > ol > li > ul { padding-left: 28px; margin-top: 4px; }
nav.toc > ol > li > ul > li { font-weight: 400; font-size: 13px; margin-bottom: 2px; }
nav.toc a { color: #0071c5; text-decoration: none; }
nav.toc a:hover { text-decoration: underline; }
</style>

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

<a id="toc"></a>

## Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. Capability Inventory](#2-capability-inventory)
- [3. Current-State Architecture](#3-current-state-architecture)
   - [3.1 Application Architecture](#31-application-architecture)
   - [3.2 Data Architecture](#32-data-architecture)
   - [3.3 Technology Architecture](#33-technology-architecture)
- [4. Future-State Architecture](#4-future-state-architecture)
   - [4.1 Application Architecture](#41-application-architecture)
   - [4.2 Data Architecture](#42-data-architecture)
   - [4.3 Technology Architecture](#43-technology-architecture)
- [5. Transformation Analysis](#5-transformation-analysis)
   - [5.1 System Landscape Changes](#51-system-landscape-changes)
   - [5.2 Integration Complexity Delta](#52-integration-complexity-delta)
   - [5.3 Release-over-Release Changes](#53-release-over-release-changes)
- [6. Capability Detail Reference](#6-capability-detail-reference)

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

## 1 Executive Summary

This **L0** summary aggregates architecture diagrams from **19** L2 capabilities across **Tower: Finance Plan To Report (FPR) · R1 – R5**.

The diagrams below show the consolidated current-state and future-state system landscape **without duplicates** — each system and connection appears only once even when shared across capabilities. For detailed data flows, integration patterns, technology stacks, and business architecture, refer to the individual L2 capability documents linked in [§6 Capability Detail Reference](#6-capability-detail-reference).

| Metric | Current-State | Future-State | Delta |
|--------|:---:|:---:|:---:|
| **Unique Systems** | 26 | 42 | +16 |
| **System Connections** | 31 | 53 | +22 |
| **Total Flow Hops** | 36 | 114 | +78 |
| **Capabilities Covered** | 19 | 19 | — |

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

## 2 Capability Inventory

The following **19** capabilities are aggregated in this summary.
Click a capability ID to view its full TOGAF BDAT architecture document.

| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |
|:---:|:---:|---|---|:---:|:---:|
| 1 | [DC-010](towers/FPR/DC Manage Accounting and Control Data/DC-010/output/docs/systems-architecture/DC-010-Architecture.html) | Perform Transaction Processing | DC Manage Accounting and Control Data | 0 | 0 |
| 2 | [DC-020](towers/FPR/DC Manage Accounting and Control Data/DC-020/output/docs/systems-architecture/DC-020-Architecture.html) | Manage the General Ledger | DC Manage Accounting and Control Data | 0 | 0 |
| 3 | [DC-030](towers/FPR/DC Manage Accounting and Control Data/DC-030/output/docs/systems-architecture/DC-030-Architecture.html) | Perform Closing | DC Manage Accounting and Control Data | 0 | 0 |
| 4 | [DC-040](towers/FPR/DC Manage Accounting and Control Data/DC-040/output/docs/systems-architecture/DC-040-Architecture.html) | Perform Fixed Asset Accounting | DC Manage Accounting and Control Data | 0 | 0 |
| 5 | [DC-050](towers/FPR/DC Manage Accounting and Control Data/DC-050/output/docs/systems-architecture/DC-050-Architecture.html) | Project Accounting | DC Manage Accounting and Control Data | 0 | 0 |
| 6 | [DC-060](towers/FPR/DC Manage Accounting and Control Data/DC-060/output/docs/systems-architecture/DC-060-Architecture.html) | Manage Taxes | DC Manage Accounting and Control Data | 0 | 0 |
| 7 | [DC-100](towers/FPR/DC Manage Accounting and Control Data/DC-100/output/docs/systems-architecture/DC-100-Architecture.html) | Revenue Recognition | DC Manage Accounting and Control Data | 0 | 0 |
| 8 | [DC-110](towers/FPR/DC Manage Accounting and Control Data/DC-110/output/docs/systems-architecture/DC-110-Architecture.html) | Manage Intercompany | DC Manage Accounting and Control Data | 0 | 0 |
| 9 | [DC-120](towers/FPR/DC Manage Accounting and Control Data/DC-120/output/docs/systems-architecture/DC-120-Architecture.html) | Maintenance & Management Accounting | DC Manage Accounting and Control Data | 0 | 0 |
| 10 | [DS-010](towers/FPR/DS Provide Decision Support/DS-010/output/docs/systems-architecture/DS-010-Architecture.html) | Perform Overhead Accounting and Allocation | DS Provide Decision Support | 0 | 0 |
| 11 | [DS-020](towers/FPR/DS Provide Decision Support/DS-020/output/docs/systems-architecture/DS-020-Architecture.html) | Perform Product Costing and Inventory Valuation | DS Provide Decision Support | 36 | 114 |
| 12 | [DS-030](towers/FPR/DS Provide Decision Support/DS-030/output/docs/systems-architecture/DS-030-Architecture.html) | Perform Customer and Product Profitability Analysis | DS Provide Decision Support | 0 | 0 |
| 13 | [MB-060](towers/FPR/MB Plan and Manage Business/MB-060/output/docs/systems-architecture/MB-060-Architecture.html) | Plan the Business | MB Plan and Manage Business | 0 | 0 |
| 14 | [MB-070](towers/FPR/MB Plan and Manage Business/MB-070/output/docs/systems-architecture/MB-070-Architecture.html) | Prepare Budgets | MB Plan and Manage Business | 0 | 0 |
| 15 | [MR-010](towers/FPR/MR Manage Capital and Risk/MR-010/output/docs/systems-architecture/MR-010-Architecture.html) | Manage Liquidity | MR Manage Capital and Risk | 0 | 0 |
| 16 | [MR-020](towers/FPR/MR Manage Capital and Risk/MR-020/output/docs/systems-architecture/MR-020-Architecture.html) | Manage Capital Structure | MR Manage Capital and Risk | 0 | 0 |
| 17 | [MR-030](towers/FPR/MR Manage Capital and Risk/MR-030/output/docs/systems-architecture/MR-030-Architecture.html) | Manage Financial Risk | MR Manage Capital and Risk | 0 | 0 |
| 18 | [MR-070](towers/FPR/MR Manage Capital and Risk/MR-070/output/docs/systems-architecture/MR-070-Architecture.html) | In-House Banking | MR Manage Capital and Risk | 0 | 0 |
| 19 | [OR-140](towers/FPR/OR Receivables Management/OR-140/output/docs/systems-architecture/OR-140-Architecture.html) | Process Receipts | OR Receivables Management | 0 | 0 |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

## 3 Current-State Architecture

Aggregated current-state: **26** systems, **31** connections, **36** flow hops.

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 3.1 Application Architecture

> System-to-system integration flows. Color indicates IAPM lifecycle status (green = deployed, blue = developing, red = end-of-life).

```mermaid
graph TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["📦 Application Layer — Systems Integration"]
        direction LR
        SCA_APIGEE["📦 APIGEE"]
        SCA_Azure_ADF["📦 Azure ADF"]
        SCA_BOBJ["📦 BOBJ"]
        SCA_CFIN_S_4["📦 CFIN S/4"]
        SCA_CIBR["📦 CIBR"]
        SCA_Corp___IP_S_4["📦 Corp / IP S/4"]
        SCA_DataBricks["📦 DataBricks"]
        SCA_EATS["📦 EATS"]
        SCA_ECA["📦 ECA"]
        SCA_EDW["📦 EDW"]
        SCA_FCA["📦 FCA"]
        SCA_Finance_HANA["📦 Finance HANA"]
        SCA_ICOST["📦 ICOST"]
        SCA_Legacy_MDG["📦 Legacy MDG"]
        SCA_MARS["📦 MARS"]
        SCA_MES_300["📦 MES 300"]
        SCA_PEGA["📦 PEGA"]
        SCA_SAP_BODS["📦 SAP BODS"]
        SCA_SAP_ECC["📦 SAP ECC"]
        SCA_SAP_IBP["📦 SAP IBP"]
        SCA_SAP_PO["📦 SAP PO"]
        SCA_SPEED["📦 SPEED"]
        SCA_SideCar["📦 SideCar"]
        SCA_SnowFlake["📦 SnowFlake"]
        SCA_WorkStream["📦 WorkStream"]
        SCA_XEUS["📦 XEUS"]
    end

    SCA_APIGEE -->|"APIGEE"| SCA_PEGA
    SCA_Azure_ADF -->|"ADF Pipeline"| SCA_DataBricks
    SCA_CIBR -->|"Internal"| SCA_ICOST
    SCA_CIBR -->|"SAP PO"| SCA_SAP_PO
    SCA_Corp___IP_S_4 -->|"SLT"| SCA_ECA
    SCA_DataBricks -->|"Internal"| SCA_SnowFlake
    SCA_EATS -->|"Internal"| SCA_ICOST
    SCA_ECA -->|"Internal"| SCA_CIBR
    SCA_ECA -->|"Internal"| SCA_ICOST
    SCA_EDW -->|"ETL"| SCA_CIBR
    SCA_EDW -->|"ETL"| SCA_ICOST
    SCA_FCA -->|"Direct"| SCA_ICOST
    SCA_Finance_HANA -->|"APIGEE"| SCA_APIGEE
    SCA_Finance_HANA -->|"Direct"| SCA_BOBJ
    SCA_Finance_HANA -->|"SAP PO"| SCA_SAP_PO
    SCA_ICOST -->|"SAP BODS"| SCA_SAP_BODS
    SCA_Legacy_MDG -->|"MDG"| SCA_SAP_ECC
    SCA_MARS -->|"Internal"| SCA_ICOST
    SCA_MES_300 -->|"Direct"| SCA_XEUS
    SCA_SAP_BODS -->|"SAP BODS"| SCA_SAP_ECC
    SCA_SAP_ECC -->|"Replication"| SCA_CFIN_S_4
    SCA_SAP_ECC -->|"ETL"| SCA_EDW
    SCA_SAP_ECC -->|"SLT"| SCA_Finance_HANA
    SCA_SAP_ECC -->|"SLT"| SCA_SideCar
    SCA_SAP_IBP -->|"Direct"| SCA_ECA
    SCA_SAP_PO -->|"SAP PO"| SCA_SAP_ECC
    SCA_SPEED -->|"Direct"| SCA_EDW
    SCA_SPEED -->|"SAP PO"| SCA_SAP_PO
    SCA_SideCar -->|"CIF"| SCA_Azure_ADF
    SCA_WorkStream -->|"Direct"| SCA_MARS
    SCA_XEUS -->|"Internal"| SCA_ICOST

    class SCA_APIGEE app
    class SCA_Azure_ADF app
    class SCA_BOBJ app
    class SCA_CFIN_S_4 app
    class SCA_CIBR app
    class SCA_Corp___IP_S_4 app
    class SCA_DataBricks app
    class SCA_EATS app
    class SCA_ECA app
    class SCA_EDW app
    class SCA_FCA app
    class SCA_Finance_HANA app
    class SCA_ICOST app
    class SCA_Legacy_MDG app
    class SCA_MARS app
    class SCA_MES_300 app
    class SCA_PEGA app
    class SCA_SAP_BODS app
    class SCA_SAP_ECC app
    class SCA_SAP_IBP app
    class SCA_SAP_PO app
    class SCA_SPEED app
    class SCA_SideCar app
    class SCA_SnowFlake app
    class SCA_WorkStream app
    class SCA_XEUS app
    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px
```

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 3.2 Data Architecture

> Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef dbCloud fill:#90CAF9,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef dbData fill:#80CBC4,stroke:#00695C,stroke-width:2px,color:#004D40
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph SCDCL_Azure_Data_Lake_ADLS[" "]
        direction TB
        SCDA_ECA["ECA"]:::appBox
        SCDD_Azure_Data_Lake_ADLS[("🗄️ Azure Data Lake (ADLS)")]:::dbCloud
        SCDA_ECA -.-> SCDD_Azure_Data_Lake_ADLS
    end
    style SCDCL_Azure_Data_Lake_ADLS fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_Delta_Lake[" "]
        direction TB
        SCDA_DataBricks["DataBricks"]:::appBox
        SCDD_Delta_Lake[("🗄️ Delta Lake")]:::dbCloud
        SCDA_DataBricks -.-> SCDD_Delta_Lake
    end
    style SCDCL_Delta_Lake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_N_A_API_Gateway[" "]
        direction TB
        SCDA_APIGEE["APIGEE"]:::appBox
        SCDD_N_A_API_Gateway[("🗄️ N/A (API Gateway)")]:::dbCyl
        SCDA_APIGEE -.-> SCDD_N_A_API_Gateway
    end
    style SCDCL_N_A_API_Gateway fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_N_A_ETL[" "]
        direction TB
        SCDA_Azure_ADF["Azure ADF"]:::appBox
        SCDD_N_A_ETL[("🗄️ N/A (ETL)")]:::dbCyl
        SCDA_Azure_ADF -.-> SCDD_N_A_ETL
    end
    style SCDCL_N_A_ETL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_Oracle_DB[" "]
        direction TB
        SCDA_ICOST["ICOST"]:::appBox
        SCDA_Legacy_MDG["Legacy MDG"]:::appBox
        SCDA_MES_300["MES 300"]:::appBox
        SCDA_SAP_BODS["SAP BODS"]:::appBox
        SCDA_SAP_ECC["SAP ECC"]:::appBox
        SCDA_SAP_PO["SAP PO"]:::appBox
        SCDA_WorkStream["WorkStream"]:::appBox
        SCDA_XEUS["XEUS"]:::appBox
        SCDD_Oracle_DB[("🗄️ Oracle DB")]:::dbCyl
        SCDA_ICOST -.-> SCDD_Oracle_DB
        SCDA_Legacy_MDG -.-> SCDD_Oracle_DB
        SCDA_MES_300 -.-> SCDD_Oracle_DB
        SCDA_SAP_BODS -.-> SCDD_Oracle_DB
        SCDA_SAP_ECC -.-> SCDD_Oracle_DB
        SCDA_SAP_PO -.-> SCDD_Oracle_DB
        SCDA_WorkStream -.-> SCDD_Oracle_DB
        SCDA_XEUS -.-> SCDD_Oracle_DB
    end
    style SCDCL_Oracle_DB fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_PostgreSQL[" "]
        direction TB
        SCDA_PEGA["PEGA"]:::appBox
        SCDD_PostgreSQL[("🗄️ PostgreSQL")]:::dbCyl
        SCDA_PEGA -.-> SCDD_PostgreSQL
    end
    style SCDCL_PostgreSQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_SAP_HANA[" "]
        direction TB
        SCDA_BOBJ["BOBJ"]:::appBox
        SCDA_CFIN_S_4["CFIN S/4"]:::appBox
        SCDA_Corp_IP_S_4["Corp / IP S/4"]:::appBox
        SCDA_Finance_HANA["Finance HANA"]:::appBox
        SCDA_SideCar["SideCar"]:::appBox
        SCDD_SAP_HANA[("🗄️ SAP HANA")]:::dbData
        SCDA_BOBJ -.-> SCDD_SAP_HANA
        SCDA_CFIN_S_4 -.-> SCDD_SAP_HANA
        SCDA_Corp_IP_S_4 -.-> SCDD_SAP_HANA
        SCDA_Finance_HANA -.-> SCDD_SAP_HANA
        SCDA_SideCar -.-> SCDD_SAP_HANA
    end
    style SCDCL_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_SAP_HANA_Cloud[" "]
        direction TB
        SCDA_SAP_IBP["SAP IBP"]:::appBox
        SCDD_SAP_HANA_Cloud[("🗄️ SAP HANA Cloud")]:::dbData
        SCDA_SAP_IBP -.-> SCDD_SAP_HANA_Cloud
    end
    style SCDCL_SAP_HANA_Cloud fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_SQL_Server[" "]
        direction TB
        SCDA_CIBR["CIBR"]:::appBox
        SCDA_EATS["EATS"]:::eolBox
        SCDA_FCA["FCA"]:::appBox
        SCDA_MARS["MARS"]:::appBox
        SCDA_SPEED["SPEED"]:::appBox
        SCDD_SQL_Server[("🗄️ SQL Server")]:::dbCyl
        SCDA_CIBR -.-> SCDD_SQL_Server
        SCDA_EATS -.-> SCDD_SQL_Server
        SCDA_FCA -.-> SCDD_SQL_Server
        SCDA_MARS -.-> SCDD_SQL_Server
        SCDA_SPEED -.-> SCDD_SQL_Server
    end
    style SCDCL_SQL_Server fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_Snowflake_Cloud_DW[" "]
        direction TB
        SCDA_SnowFlake["SnowFlake"]:::appBox
        SCDD_Snowflake_Cloud_DW[("🗄️ Snowflake Cloud DW")]:::dbCloud
        SCDA_SnowFlake -.-> SCDD_Snowflake_Cloud_DW
    end
    style SCDCL_Snowflake_Cloud_DW fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SCDCL_Teradata_Oracle_DB[" "]
        direction TB
        SCDA_EDW["EDW"]:::appBox
        SCDD_Teradata_Oracle_DB[("🗄️ Teradata / Oracle DB")]:::dbData
        SCDA_EDW -.-> SCDD_Teradata_Oracle_DB
    end
    style SCDCL_Teradata_Oracle_DB fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    SCDD_Oracle_DB ==>|"Direct"| SCDD_SQL_Server
    SCDD_SQL_Server ==>|"Internal"| SCDD_Oracle_DB
    SCDD_SQL_Server ==>|"SAP PO"| SCDD_Oracle_DB
    SCDD_SQL_Server ==>|"Direct"| SCDD_Teradata_Oracle_DB
    SCDD_Oracle_DB ==>|"SLT"| SCDD_SAP_HANA
    SCDD_SAP_HANA ==>|"CIF"| SCDD_N_A_ETL
    SCDD_N_A_ETL ==>|"ADF Pipeline"| SCDD_Delta_Lake
    SCDD_Delta_Lake ==>|"Internal"| SCDD_Snowflake_Cloud_DW
    SCDD_SAP_HANA ==>|"SLT"| SCDD_Azure_Data_Lake_ADLS
    SCDD_Azure_Data_Lake_ADLS ==>|"Internal"| SCDD_SQL_Server
    SCDD_Azure_Data_Lake_ADLS ==>|"Internal"| SCDD_Oracle_DB
    SCDD_Oracle_DB ==>|"Replication"| SCDD_SAP_HANA
    SCDD_Oracle_DB ==>|"ETL"| SCDD_Teradata_Oracle_DB
    SCDD_Teradata_Oracle_DB ==>|"ETL"| SCDD_Oracle_DB
    SCDD_Teradata_Oracle_DB ==>|"ETL"| SCDD_SQL_Server
    SCDD_SQL_Server ==>|"Direct"| SCDD_Oracle_DB
    SCDD_SAP_HANA ==>|"APIGEE"| SCDD_N_A_API_Gateway
    SCDD_N_A_API_Gateway ==>|"APIGEE"| SCDD_PostgreSQL
    SCDD_SAP_HANA ==>|"SAP PO"| SCDD_Oracle_DB
    SCDD_SAP_HANA_Cloud ==>|"Direct"| SCDD_Azure_Data_Lake_ADLS

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ On-Prem DB")]:::dbCyl
        L_DC[("🗄️ Cloud DB")]:::dbCloud
        L_DD[("🗄️ Data Platform")]:::dbData
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Technology Architecture

> Applications grouped by hosting platform. Cloud platforms marked with ☁️.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph SCPP_Azure_Data_Factory_Cloud["☁️ Azure Data Factory Cloud"]
        direction LR
        SCPA_Azure_ADF["Azure ADF"]:::appBox
    end
    style SCPP_Azure_Data_Factory_Cloud fill:#BBDEFB,stroke:#1565C0,stroke-width:3px,color:#0D47A1

    subgraph SCPP_Databricks_Cloud_SaaS["☁️ Databricks Cloud SaaS"]
        direction LR
        SCPA_DataBricks["DataBricks"]:::appBox
    end
    style SCPP_Databricks_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SCPP_Google_Apigee_Cloud["☁️ Google Apigee Cloud"]
        direction LR
        SCPA_APIGEE["APIGEE"]:::appBox
    end
    style SCPP_Google_Apigee_Cloud fill:#FFE0B2,stroke:#E65100,stroke-width:3px,color:#BF360C

    subgraph SCPP_Intel_Custom_On_Premise["🖥️ Intel Custom On-Premise"]
        direction LR
        SCPA_CIBR["CIBR"]:::appBox
        SCPA_EATS["EATS"]:::eolBox
        SCPA_FCA["FCA"]:::appBox
        SCPA_ICOST["ICOST"]:::appBox
        SCPA_MARS["MARS"]:::appBox
        SCPA_SPEED["SPEED"]:::appBox
    end
    style SCPP_Intel_Custom_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_Intel_ECA_Platform_Azure_Cloud["☁️ Intel ECA Platform Azure Cloud"]
        direction LR
        SCPA_ECA["ECA"]:::appBox
    end
    style SCPP_Intel_ECA_Platform_Azure_Cloud fill:#BBDEFB,stroke:#1565C0,stroke-width:3px,color:#0D47A1

    subgraph SCPP_Intel_EDW_On_Premise["🖥️ Intel EDW On-Premise"]
        direction LR
        SCPA_EDW["EDW"]:::appBox
    end
    style SCPP_Intel_EDW_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_Intel_MES_On_Premise["🖥️ Intel MES On-Premise"]
        direction LR
        SCPA_MES_300["MES 300"]:::appBox
        SCPA_WorkStream["WorkStream"]:::appBox
    end
    style SCPP_Intel_MES_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_Intel_Middleware_On_Premise["🖥️ Intel Middleware On-Premise"]
        direction LR
        SCPA_XEUS["XEUS"]:::appBox
    end
    style SCPP_Intel_Middleware_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_Pega_Cloud_SaaS["☁️ Pega Cloud SaaS"]
        direction LR
        SCPA_PEGA["PEGA"]:::appBox
    end
    style SCPP_Pega_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SCPP_SAP_BusinessObjects_On_Premise["🖥️ SAP BusinessObjects On-Premise"]
        direction LR
        SCPA_BOBJ["BOBJ"]:::appBox
    end
    style SCPP_SAP_BusinessObjects_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_SAP_Data_Services_On_Premise["🖥️ SAP Data Services On-Premise"]
        direction LR
        SCPA_SAP_BODS["SAP BODS"]:::appBox
    end
    style SCPP_SAP_Data_Services_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_SAP_ECC_6_0_On_Premise["🖥️ SAP ECC 6.0 On-Premise"]
        direction LR
        SCPA_SAP_ECC["SAP ECC"]:::appBox
    end
    style SCPP_SAP_ECC_6_0_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_SAP_ECC_MDG_On_Premise["🖥️ SAP ECC MDG On-Premise"]
        direction LR
        SCPA_Legacy_MDG["Legacy MDG"]:::appBox
    end
    style SCPP_SAP_ECC_MDG_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_SAP_HANA_Sidecar_On_Premise["🖥️ SAP HANA Sidecar On-Premise"]
        direction LR
        SCPA_Finance_HANA["Finance HANA"]:::appBox
        SCPA_SideCar["SideCar"]:::appBox
    end
    style SCPP_SAP_HANA_Sidecar_On_Premise fill:#B2DFDB,stroke:#00695C,stroke-width:3px,color:#004D40

    subgraph SCPP_SAP_IBP_Cloud_SaaS["☁️ SAP IBP Cloud SaaS"]
        direction LR
        SCPA_SAP_IBP["SAP IBP"]:::appBox
    end
    style SCPP_SAP_IBP_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SCPP_SAP_Process_Orchestration_On_Premise["🖥️ SAP Process Orchestration On-Premise"]
        direction LR
        SCPA_SAP_PO["SAP PO"]:::appBox
    end
    style SCPP_SAP_Process_Orchestration_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_SAP_S_4HANA_Central_Finance["🖥️ SAP S/4HANA Central Finance"]
        direction LR
        SCPA_CFIN_S_4["CFIN S/4"]:::appBox
    end
    style SCPP_SAP_S_4HANA_Central_Finance fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_SAP_S_4HANA_On_Premise["🖥️ SAP S/4HANA On-Premise"]
        direction LR
        SCPA_Corp_IP_S_4["Corp / IP S/4"]:::appBox
    end
    style SCPP_SAP_S_4HANA_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SCPP_Snowflake_Cloud_SaaS["☁️ Snowflake Cloud SaaS"]
        direction LR
        SCPA_SnowFlake["SnowFlake"]:::appBox
    end
    style SCPP_Snowflake_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    SCPP_Intel_MES_On_Premise ==>|"Direct"| SCPP_Intel_Middleware_On_Premise
    SCPP_Intel_Middleware_On_Premise ==>|"Internal"| SCPP_Intel_Custom_On_Premise
    SCPP_Intel_MES_On_Premise ==>|"Direct"| SCPP_Intel_Custom_On_Premise
    SCPP_Intel_Custom_On_Premise ==>|"SAP PO"| SCPP_SAP_Process_Orchestration_On_Premise
    SCPP_SAP_Process_Orchestration_On_Premise ==>|"SAP PO"| SCPP_SAP_ECC_6_0_On_Premise
    SCPP_Intel_Custom_On_Premise ==>|"Direct"| SCPP_Intel_EDW_On_Premise
    SCPP_SAP_ECC_MDG_On_Premise ==>|"MDG"| SCPP_SAP_ECC_6_0_On_Premise
    SCPP_SAP_ECC_6_0_On_Premise ==>|"SLT"| SCPP_SAP_HANA_Sidecar_On_Premise
    SCPP_SAP_HANA_Sidecar_On_Premise ==>|"CIF"| SCPP_Azure_Data_Factory_Cloud
    SCPP_Azure_Data_Factory_Cloud ==>|"ADF Pipeline"| SCPP_Databricks_Cloud_SaaS
    SCPP_Databricks_Cloud_SaaS ==>|"Internal"| SCPP_Snowflake_Cloud_SaaS
    SCPP_SAP_S_4HANA_On_Premise ==>|"SLT"| SCPP_Intel_ECA_Platform_Azure_Cloud
    SCPP_Intel_ECA_Platform_Azure_Cloud ==>|"Internal"| SCPP_Intel_Custom_On_Premise
    SCPP_Intel_Custom_On_Premise ==>|"SAP BODS"| SCPP_SAP_Data_Services_On_Premise
    SCPP_SAP_Data_Services_On_Premise ==>|"SAP BODS"| SCPP_SAP_ECC_6_0_On_Premise
    SCPP_SAP_ECC_6_0_On_Premise ==>|"Replication"| SCPP_SAP_S_4HANA_Central_Finance
    SCPP_SAP_ECC_6_0_On_Premise ==>|"ETL"| SCPP_Intel_EDW_On_Premise
    SCPP_Intel_EDW_On_Premise ==>|"ETL"| SCPP_Intel_Custom_On_Premise
    SCPP_SAP_HANA_Sidecar_On_Premise ==>|"APIGEE"| SCPP_Google_Apigee_Cloud
    SCPP_Google_Apigee_Cloud ==>|"APIGEE"| SCPP_Pega_Cloud_SaaS
    SCPP_SAP_HANA_Sidecar_On_Premise ==>|"Direct"| SCPP_SAP_BusinessObjects_On_Premise
    SCPP_SAP_HANA_Sidecar_On_Premise ==>|"SAP PO"| SCPP_SAP_Process_Orchestration_On_Premise
    SCPP_SAP_IBP_Cloud_SaaS ==>|"Direct"| SCPP_Intel_ECA_Platform_Azure_Cloud

    subgraph SCPLegend["📐 PLATFORM LEGEND"]
        direction LR
        SCPLC["☁️ Cloud"]
        SCPLS["🔮 SaaS"]
        SCPLO["🏢 On-Prem"]
        SCPLD["💾 Data Platform"]
        SCPLM["🔗 Middleware"]
    end
    style SCPLegend fill:#F5F5F5,stroke:#999,stroke-width:1px
    style SCPLC fill:#BBDEFB,stroke:#1565C0,stroke-width:3px,color:#0D47A1
    style SCPLS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C
    style SCPLO fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    style SCPLD fill:#B2DFDB,stroke:#00695C,stroke-width:3px,color:#004D40
    style SCPLM fill:#FFE0B2,stroke:#E65100,stroke-width:3px,color:#BF360C
```

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

## 4 Future-State Architecture

Aggregated future-state: **42** systems, **53** connections, **114** flow hops.

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 4.1 Application Architecture

> System-to-system integration flows. Color indicates IAPM lifecycle status (green = deployed, blue = developing, red = end-of-life).

```mermaid
graph TB
    %% -- ArchiMate-inspired style classes --
    classDef business      fill:#FFFFB5,stroke:#B8860B,stroke-width:2px,color:#000
    classDef app           fill:#B5FFFF,stroke:#0077B6,stroke-width:2px,color:#000
    classDef data          fill:#B5D8FF,stroke:#0077B6,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef middleware    fill:#FFD6A5,stroke:#E76F00,stroke-width:2px,color:#000
    classDef eol           fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#000

    subgraph AL["📦 Application Layer — Systems Integration"]
        direction LR
        SFA_ATCR["📦 ATCR"]
        SFA_CFIN_S_4_HANA["📦 CFIN S/4 HANA"]
        SFA_Capacity_Forecast_Data_Store["📦 Capacity Forecast Data Store"]
        SFA_Corp___IP_S_4_HANA["📦 Corp / IP S/4 HANA"]
        SFA_DMOCR["📦 DMOCR"]
        SFA_DXCR["📦 DXCR"]
        SFA_ECA_ADLS["📦 ECA-ADLS"]
        SFA_ECA_DataBricks["📦 ECA-DataBricks"]
        SFA_ECA_SnowFlake["📦 ECA-SnowFlake"]
        SFA_ECM__Windchill_["📦 ECM (Windchill)"]
        SFA_FCS["📦 FCS"]
        SFA_GraphiteConnect["📦 GraphiteConnect"]
        SFA_ICS__Phoenix_["📦 ICS (Phoenix)"]
        SFA_IF_Blue_Yonder["📦 IF Blue Yonder"]
        SFA_IF_PDH_Consumptional["📦 IF PDH Consumptional"]
        SFA_IF_PDH_Foundational["📦 IF PDH Foundational"]
        SFA_IF_PDH_Raw["📦 IF PDH Raw"]
        SFA_IF_S_4_HANA["📦 IF S/4 HANA"]
        SFA_IP_Blue_Yonder["📦 IP Blue Yonder"]
        SFA_IP_PDH_Consumptional["📦 IP PDH Consumptional"]
        SFA_IP_PDH_Foundational["📦 IP PDH Foundational"]
        SFA_IP_PDH_Raw["📦 IP PDH Raw"]
        SFA_MARS["📦 MARS"]
        SFA_MES_300["📦 MES 300"]
        SFA_PDF_SMH["📦 PDF-SMH"]
        SFA_PDH_Consumptional["📦 PDH Consumptional"]
        SFA_PDH_Foundational["📦 PDH Foundational"]
        SFA_PDH_Raw["📦 PDH Raw"]
        SFA_PDM_Translator["📦 PDM Translator"]
        SFA_Power_BI__DARC_["📦 Power BI (DARC)"]
        SFA_SAP_Ariba["📦 SAP Ariba"]
        SFA_SAP_BOBJ["📦 SAP BOBJ"]
        SFA_SAP_IBP["📦 SAP IBP"]
        SFA_SAP_PAPM["📦 SAP PAPM"]
        SFA_SAP_S_4_MDG["📦 SAP S/4 MDG"]
        SFA_SAP_SAC["📦 SAP SAC"]
        SFA_SCS["📦 SCS"]
        SFA_SPEED["📦 SPEED"]
        SFA_SideCar["📦 SideCar"]
        SFA_WSPW["📦 WSPW"]
        SFA_WorkStream["📦 WorkStream"]
        SFA_XEUS["📦 XEUS"]
    end

    SFA_ATCR -->|"Direct"| SFA_Capacity_Forecast_Data_Store
    SFA_CFIN_S_4_HANA -->|"SLT"| SFA_SideCar
    SFA_Capacity_Forecast_Data_Store -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo)"| SFA_ECA_ADLS
    SFA_Corp___IP_S_4_HANA -->|"SLT"| SFA_SideCar
    SFA_DMOCR -->|"Direct"| SFA_Capacity_Forecast_Data_Store
    SFA_DXCR -->|"Direct"| SFA_Capacity_Forecast_Data_Store
    SFA_ECA_ADLS -->|"Unity Catalog"| SFA_ECA_DataBricks
    SFA_ECA_DataBricks -->|"Snowflake Connector / Snowpipe"| SFA_ECA_SnowFlake
    SFA_ECA_SnowFlake -->|"MuleSoft/BODS"| SFA_CFIN_S_4_HANA
    SFA_ECA_SnowFlake -->|"MuleSoft/BODS"| SFA_Corp___IP_S_4_HANA
    SFA_ECA_SnowFlake -->|"MuleSoft/BODS"| SFA_IF_S_4_HANA
    SFA_ECA_SnowFlake -->|"Snowflake Connector / Snowpipe"| SFA_Power_BI__DARC_
    SFA_ECA_SnowFlake -->|"Remote Function Adapter / MuleSoft / SAP Integration Suite"| SFA_SAP_PAPM
    SFA_ECM__Windchill_ -->|"PDM Translator"| SFA_PDM_Translator
    SFA_FCS -->|"Direct"| SFA_Capacity_Forecast_Data_Store
    SFA_GraphiteConnect -->|"MuleSoft & Reltio"| SFA_SAP_S_4_MDG
    SFA_ICS__Phoenix_ -->|"Direct"| SFA_Capacity_Forecast_Data_Store
    SFA_IF_Blue_Yonder -->|"ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule)"| SFA_IF_PDH_Raw
    SFA_IF_PDH_Consumptional -->|"Snowflake Connector / Snowpipe"| SFA_ECA_SnowFlake
    SFA_IF_PDH_Foundational -->|"Unity Catalog"| SFA_IF_PDH_Consumptional
    SFA_IF_PDH_Raw -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo)"| SFA_IF_PDH_Foundational
    SFA_IF_S_4_HANA -->|"SLT"| SFA_CFIN_S_4_HANA
    SFA_IF_S_4_HANA -->|"SLT"| SFA_SideCar
    SFA_IP_Blue_Yonder -->|"ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule)"| SFA_IP_PDH_Raw
    SFA_IP_PDH_Consumptional -->|"Snowflake Connector / Snowpipe"| SFA_ECA_SnowFlake
    SFA_IP_PDH_Foundational -->|"Unity Catalog"| SFA_IP_PDH_Consumptional
    SFA_IP_PDH_Raw -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo)"| SFA_IP_PDH_Foundational
    SFA_MARS -->|"Direct"| SFA_PDF_SMH
    SFA_MES_300 -->|"Direct"| SFA_XEUS
    SFA_PDF_SMH -->|"EAI Connector"| SFA_IF_S_4_HANA
    SFA_PDH_Consumptional -->|"Snowflake Connector / Snowpipe"| SFA_ECA_SnowFlake
    SFA_PDH_Foundational -->|"Unity Catalog"| SFA_IP_PDH_Consumptional
    SFA_PDH_Raw -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo)"| SFA_IP_PDH_Foundational
    SFA_PDM_Translator -->|"PDM Translator"| SFA_SAP_S_4_MDG
    SFA_SAP_Ariba -->|"Apigee / MuleSoft"| SFA_Corp___IP_S_4_HANA
    SFA_SAP_Ariba -->|"Apigee / MuleSoft"| SFA_IF_S_4_HANA
    SFA_SAP_IBP -->|"ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule)"| SFA_IF_PDH_Raw
    SFA_SAP_PAPM -->|"SAP Integration Suite / Smart Data Integration/BTP Destinations (HTTP)"| SFA_Corp___IP_S_4_HANA
    SFA_SAP_PAPM -->|"SAP Integration Suite / Smart Data Integration/BTP Destinations (HTTP)"| SFA_IF_S_4_HANA
    SFA_SAP_S_4_MDG -->|"DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC)"| SFA_Corp___IP_S_4_HANA
    SFA_SAP_S_4_MDG -->|"DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC)"| SFA_IF_S_4_HANA
    SFA_SAP_SAC -->|"SAP Odata services with connector"| SFA_CFIN_S_4_HANA
    SFA_SAP_SAC -->|"SAP Odata services with connector"| SFA_Corp___IP_S_4_HANA
    SFA_SAP_SAC -->|"SAC Data Export Service (API) - Direct Write (Speed Layer in Snowflake / Use ADF / MuleSoft for DataBricks"| SFA_ECA_SnowFlake
    SFA_SAP_SAC -->|"SAP Odata services with connector"| SFA_IF_S_4_HANA
    SFA_SCS -->|"Direct"| SFA_Capacity_Forecast_Data_Store
    SFA_SPEED -->|"ADF Rest API / SFTP(Blob)"| SFA_ECA_ADLS
    SFA_SPEED -->|"PDM Translator"| SFA_PDM_Translator
    SFA_SideCar -->|"ADF Rest API / SFTP(Blob)"| SFA_ECA_ADLS
    SFA_SideCar -->|"1×"| SFA_SAP_BOBJ
    SFA_WSPW -->|"Direct"| SFA_ECA_SnowFlake
    SFA_WorkStream -->|"Direct"| SFA_MARS
    SFA_XEUS -->|"Direct"| SFA_PDF_SMH

    class SFA_ATCR app
    class SFA_CFIN_S_4_HANA app
    class SFA_Capacity_Forecast_Data_Store app
    class SFA_Corp___IP_S_4_HANA app
    class SFA_DMOCR app
    class SFA_DXCR app
    class SFA_ECA_ADLS app
    class SFA_ECA_DataBricks app
    class SFA_ECA_SnowFlake app
    class SFA_ECM__Windchill_ app
    class SFA_FCS app
    class SFA_GraphiteConnect app
    class SFA_ICS__Phoenix_ app
    class SFA_IF_Blue_Yonder app
    class SFA_IF_PDH_Consumptional app
    class SFA_IF_PDH_Foundational app
    class SFA_IF_PDH_Raw app
    class SFA_IF_S_4_HANA app
    class SFA_IP_Blue_Yonder app
    class SFA_IP_PDH_Consumptional app
    class SFA_IP_PDH_Foundational app
    class SFA_IP_PDH_Raw app
    class SFA_MARS app
    class SFA_MES_300 app
    class SFA_PDF_SMH app
    class SFA_PDH_Consumptional app
    class SFA_PDH_Foundational app
    class SFA_PDH_Raw app
    class SFA_PDM_Translator app
    class SFA_Power_BI__DARC_ app
    class SFA_SAP_Ariba app
    class SFA_SAP_BOBJ app
    class SFA_SAP_IBP app
    class SFA_SAP_PAPM app
    class SFA_SAP_S_4_MDG app
    class SFA_SAP_SAC app
    class SFA_SCS app
    class SFA_SPEED app
    class SFA_SideCar app
    class SFA_WSPW app
    class SFA_WorkStream app
    class SFA_XEUS app
    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px
```

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Architecture

> Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef dbCloud fill:#90CAF9,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef dbData fill:#80CBC4,stroke:#00695C,stroke-width:2px,color:#004D40
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph SFDCL_Azure_Analysis_Services[" "]
        direction TB
        SFDA_Power_BI_DARC["Power BI (DARC)"]:::appBox
        SFDD_Azure_Analysis_Services[("🗄️ Azure Analysis Services")]:::dbCloud
        SFDA_Power_BI_DARC -.-> SFDD_Azure_Analysis_Services
    end
    style SFDCL_Azure_Analysis_Services fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_Azure_Data_Lake_ADLS[" "]
        direction TB
        SFDA_ECA_ADLS["ECA-ADLS"]:::appBox
        SFDD_Azure_Data_Lake_ADLS[("🗄️ Azure Data Lake (ADLS)")]:::dbCloud
        SFDA_ECA_ADLS -.-> SFDD_Azure_Data_Lake_ADLS
    end
    style SFDCL_Azure_Data_Lake_ADLS fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_Delta_Lake[" "]
        direction TB
        SFDA_ECA_DataBricks["ECA-DataBricks"]:::appBox
        SFDD_Delta_Lake[("🗄️ Delta Lake")]:::dbCloud
        SFDA_ECA_DataBricks -.-> SFDD_Delta_Lake
    end
    style SFDCL_Delta_Lake fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_N_A_Middleware[" "]
        direction TB
        SFDA_PDF_SMH["PDF-SMH"]:::appBox
        SFDD_N_A_Middleware[("🗄️ N/A (Middleware)")]:::dbCyl
        SFDA_PDF_SMH -.-> SFDD_N_A_Middleware
    end
    style SFDCL_N_A_Middleware fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_N_A_SaaS[" "]
        direction TB
        SFDA_GraphiteConnect["GraphiteConnect"]:::appBox
        SFDD_N_A_SaaS[("🗄️ N/A (SaaS)")]:::dbCyl
        SFDA_GraphiteConnect -.-> SFDD_N_A_SaaS
    end
    style SFDCL_N_A_SaaS fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_Oracle_DB[" "]
        direction TB
        SFDA_ECM_Windchill["ECM (Windchill)"]:::appBox
        SFDA_ICS_Phoenix["ICS (Phoenix)"]:::appBox
        SFDA_IF_PDH_Consumptional["IF PDH Consumptional"]:::appBox
        SFDA_IF_PDH_Foundational["IF PDH Foundational"]:::appBox
        SFDA_IF_PDH_Raw["IF PDH Raw"]:::appBox
        SFDA_IP_PDH_Consumptional["IP PDH Consumptional"]:::appBox
        SFDA_IP_PDH_Foundational["IP PDH Foundational"]:::appBox
        SFDA_IP_PDH_Raw["IP PDH Raw"]:::appBox
        SFDA_MES_300["MES 300"]:::appBox
        SFDA_PDH_Consumptional["PDH Consumptional"]:::appBox
        SFDA_PDH_Foundational["PDH Foundational"]:::appBox
        SFDA_PDH_Raw["PDH Raw"]:::appBox
        SFDA_WorkStream["WorkStream"]:::appBox
        SFDA_XEUS["XEUS"]:::appBox
        SFDD_Oracle_DB[("🗄️ Oracle DB")]:::dbCyl
        SFDA_ECM_Windchill -.-> SFDD_Oracle_DB
        SFDA_ICS_Phoenix -.-> SFDD_Oracle_DB
        SFDA_IF_PDH_Consumptional -.-> SFDD_Oracle_DB
        SFDA_IF_PDH_Foundational -.-> SFDD_Oracle_DB
        SFDA_IF_PDH_Raw -.-> SFDD_Oracle_DB
        SFDA_IP_PDH_Consumptional -.-> SFDD_Oracle_DB
        SFDA_IP_PDH_Foundational -.-> SFDD_Oracle_DB
        SFDA_IP_PDH_Raw -.-> SFDD_Oracle_DB
        SFDA_MES_300 -.-> SFDD_Oracle_DB
        SFDA_PDH_Consumptional -.-> SFDD_Oracle_DB
        SFDA_PDH_Foundational -.-> SFDD_Oracle_DB
        SFDA_PDH_Raw -.-> SFDD_Oracle_DB
        SFDA_WorkStream -.-> SFDD_Oracle_DB
        SFDA_XEUS -.-> SFDD_Oracle_DB
    end
    style SFDCL_Oracle_DB fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_SAP_HANA[" "]
        direction TB
        SFDA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
        SFDA_Corp_IP_S_4_HANA["Corp / IP S/4 HANA"]:::appBox
        SFDA_IF_S_4_HANA["IF S/4 HANA"]:::appBox
        SFDA_SAP_BOBJ["SAP BOBJ"]:::eolBox
        SFDA_SAP_PAPM["SAP PAPM"]:::appBox
        SFDA_SAP_S_4_MDG["SAP S/4 MDG"]:::appBox
        SFDA_SideCar["SideCar"]:::appBox
        SFDD_SAP_HANA[("🗄️ SAP HANA")]:::dbData
        SFDA_CFIN_S_4_HANA -.-> SFDD_SAP_HANA
        SFDA_Corp_IP_S_4_HANA -.-> SFDD_SAP_HANA
        SFDA_IF_S_4_HANA -.-> SFDD_SAP_HANA
        SFDA_SAP_BOBJ -.-> SFDD_SAP_HANA
        SFDA_SAP_PAPM -.-> SFDD_SAP_HANA
        SFDA_SAP_S_4_MDG -.-> SFDD_SAP_HANA
        SFDA_SideCar -.-> SFDD_SAP_HANA
    end
    style SFDCL_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_SAP_HANA_Cloud[" "]
        direction TB
        SFDA_SAP_Ariba["SAP Ariba"]:::appBox
        SFDA_SAP_IBP["SAP IBP"]:::appBox
        SFDA_SAP_SAC["SAP SAC"]:::appBox
        SFDD_SAP_HANA_Cloud[("🗄️ SAP HANA Cloud")]:::dbData
        SFDA_SAP_Ariba -.-> SFDD_SAP_HANA_Cloud
        SFDA_SAP_IBP -.-> SFDD_SAP_HANA_Cloud
        SFDA_SAP_SAC -.-> SFDD_SAP_HANA_Cloud
    end
    style SFDCL_SAP_HANA_Cloud fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_SQL_Server[" "]
        direction TB
        SFDA_ATCR["ATCR"]:::appBox
        SFDA_Capacity_Forecast_Data_Store["Capacity Forecast Data Store"]:::appBox
        SFDA_DMOCR["DMOCR"]:::appBox
        SFDA_DXCR["DXCR"]:::appBox
        SFDA_FCS["FCS"]:::eolBox
        SFDA_IF_Blue_Yonder["IF Blue Yonder"]:::appBox
        SFDA_IP_Blue_Yonder["IP Blue Yonder"]:::appBox
        SFDA_MARS["MARS"]:::appBox
        SFDA_PDM_Translator["PDM Translator"]:::appBox
        SFDA_SCS["SCS"]:::eolBox
        SFDA_SPEED["SPEED"]:::appBox
        SFDA_WSPW["WSPW"]:::appBox
        SFDD_SQL_Server[("🗄️ SQL Server")]:::dbCyl
        SFDA_ATCR -.-> SFDD_SQL_Server
        SFDA_Capacity_Forecast_Data_Store -.-> SFDD_SQL_Server
        SFDA_DMOCR -.-> SFDD_SQL_Server
        SFDA_DXCR -.-> SFDD_SQL_Server
        SFDA_FCS -.-> SFDD_SQL_Server
        SFDA_IF_Blue_Yonder -.-> SFDD_SQL_Server
        SFDA_IP_Blue_Yonder -.-> SFDD_SQL_Server
        SFDA_MARS -.-> SFDD_SQL_Server
        SFDA_PDM_Translator -.-> SFDD_SQL_Server
        SFDA_SCS -.-> SFDD_SQL_Server
        SFDA_SPEED -.-> SFDD_SQL_Server
        SFDA_WSPW -.-> SFDD_SQL_Server
    end
    style SFDCL_SQL_Server fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph SFDCL_Snowflake_Cloud_DW[" "]
        direction TB
        SFDA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
        SFDD_Snowflake_Cloud_DW[("🗄️ Snowflake Cloud DW")]:::dbCloud
        SFDA_ECA_SnowFlake -.-> SFDD_Snowflake_Cloud_DW
    end
    style SFDCL_Snowflake_Cloud_DW fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    SFDD_Oracle_DB ==>|"Direct"| SFDD_N_A_Middleware
    SFDD_N_A_Middleware ==>|"EAI Connector"| SFDD_SAP_HANA
    SFDD_Oracle_DB ==>|"Direct"| SFDD_SQL_Server
    SFDD_SQL_Server ==>|"Direct"| SFDD_N_A_Middleware
    SFDD_Oracle_DB ==>|"PDM Translator"| SFDD_SQL_Server
    SFDD_SQL_Server ==>|"PDM Translator"| SFDD_SAP_HANA
    SFDD_SQL_Server ==>|"ADF Rest API / SFTP(Blob)"| SFDD_Azure_Data_Lake_ADLS
    SFDD_Azure_Data_Lake_ADLS ==>|"Unity Catalog"| SFDD_Delta_Lake
    SFDD_Delta_Lake ==>|"Snowflake Connector / Snowpipe"| SFDD_Snowflake_Cloud_DW
    SFDD_N_A_SaaS ==>|"MuleSoft & Reltio"| SFDD_SAP_HANA
    SFDD_SAP_HANA ==>|"ADF Rest API / SFTP(Blob)"| SFDD_Azure_Data_Lake_ADLS
    SFDD_SQL_Server ==>|"ADF / DB Unity Catalog / Th..."| SFDD_Azure_Data_Lake_ADLS
    SFDD_Snowflake_Cloud_DW ==>|"MuleSoft/BODS"| SFDD_SAP_HANA
    SFDD_SQL_Server ==>|"Direct"| SFDD_Snowflake_Cloud_DW
    SFDD_SQL_Server ==>|"ADF / DB Unity Catalog / Co..."| SFDD_Oracle_DB
    SFDD_Oracle_DB ==>|"Snowflake Connector / Snowpipe"| SFDD_Snowflake_Cloud_DW
    SFDD_Snowflake_Cloud_DW ==>|"Remote Function Adapter / M..."| SFDD_SAP_HANA
    SFDD_SAP_HANA_Cloud ==>|"SAC Data Export Service (AP..."| SFDD_Snowflake_Cloud_DW
    SFDD_SAP_HANA_Cloud ==>|"SAP Odata services with con..."| SFDD_SAP_HANA
    SFDD_SAP_HANA_Cloud ==>|"ADF / DB Unity Catalog / Co..."| SFDD_Oracle_DB
    SFDD_SAP_HANA_Cloud ==>|"Apigee / MuleSoft"| SFDD_SAP_HANA
    SFDD_Snowflake_Cloud_DW ==>|"Snowflake Connector / Snowpipe"| SFDD_Azure_Analysis_Services

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ On-Prem DB")]:::dbCyl
        L_DC[("🗄️ Cloud DB")]:::dbCloud
        L_DD[("🗄️ Data Platform")]:::dbData
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Technology Architecture

> Applications grouped by hosting platform. Cloud platforms marked with ☁️.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph SFPP_Blue_Yonder_Cloud_SaaS["☁️ Blue Yonder Cloud SaaS"]
        direction LR
        SFPA_IF_Blue_Yonder["IF Blue Yonder"]:::appBox
        SFPA_IP_Blue_Yonder["IP Blue Yonder"]:::appBox
    end
    style SFPP_Blue_Yonder_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_Databricks_on_ECA_Azure_Cloud["☁️ Databricks on ECA Azure Cloud"]
        direction LR
        SFPA_ECA_DataBricks["ECA-DataBricks"]:::appBox
    end
    style SFPP_Databricks_on_ECA_Azure_Cloud fill:#BBDEFB,stroke:#1565C0,stroke-width:3px,color:#0D47A1

    subgraph SFPP_GraphiteConnect_Cloud_SaaS["☁️ GraphiteConnect Cloud SaaS"]
        direction LR
        SFPA_GraphiteConnect["GraphiteConnect"]:::appBox
    end
    style SFPP_GraphiteConnect_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_Intel_Custom_On_Premise["🖥️ Intel Custom On-Premise"]
        direction LR
        SFPA_ATCR["ATCR"]:::appBox
        SFPA_Capacity_Forecast_Data_Store["Capacity Forecast Data Store"]:::appBox
        SFPA_DMOCR["DMOCR"]:::appBox
        SFPA_DXCR["DXCR"]:::appBox
        SFPA_FCS["FCS"]:::eolBox
        SFPA_MARS["MARS"]:::appBox
        SFPA_SCS["SCS"]:::eolBox
        SFPA_SPEED["SPEED"]:::appBox
        SFPA_WSPW["WSPW"]:::appBox
    end
    style SFPP_Intel_Custom_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_ECA_Platform_Azure_Cloud["☁️ Intel ECA Platform Azure Cloud"]
        direction LR
        SFPA_ECA_ADLS["ECA-ADLS"]:::appBox
    end
    style SFPP_Intel_ECA_Platform_Azure_Cloud fill:#BBDEFB,stroke:#1565C0,stroke-width:3px,color:#0D47A1

    subgraph SFPP_Intel_ICS_Phoenix_On_Premise["🖥️ Intel ICS (Phoenix) On-Premise"]
        direction LR
        SFPA_ICS_Phoenix["ICS (Phoenix)"]:::appBox
    end
    style SFPP_Intel_ICS_Phoenix_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_MES_On_Premise["🖥️ Intel MES On-Premise"]
        direction LR
        SFPA_MES_300["MES 300"]:::appBox
        SFPA_WorkStream["WorkStream"]:::appBox
    end
    style SFPP_Intel_MES_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_Middleware_On_Premise["🖥️ Intel Middleware On-Premise"]
        direction LR
        SFPA_XEUS["XEUS"]:::appBox
    end
    style SFPP_Intel_Middleware_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_PDF_SMH_Middleware_On_Premise["🖥️ Intel PDF-SMH Middleware On-Premise"]
        direction LR
        SFPA_PDF_SMH["PDF-SMH"]:::appBox
    end
    style SFPP_Intel_PDF_SMH_Middleware_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_PDH_On_Premise["🖥️ Intel PDH On-Premise"]
        direction LR
        SFPA_IF_PDH_Consumptional["IF PDH Consumptional"]:::appBox
        SFPA_IF_PDH_Foundational["IF PDH Foundational"]:::appBox
        SFPA_IF_PDH_Raw["IF PDH Raw"]:::appBox
        SFPA_IP_PDH_Consumptional["IP PDH Consumptional"]:::appBox
        SFPA_IP_PDH_Foundational["IP PDH Foundational"]:::appBox
        SFPA_IP_PDH_Raw["IP PDH Raw"]:::appBox
        SFPA_PDH_Consumptional["PDH Consumptional"]:::appBox
        SFPA_PDH_Foundational["PDH Foundational"]:::appBox
        SFPA_PDH_Raw["PDH Raw"]:::appBox
    end
    style SFPP_Intel_PDH_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_PDM_On_Premise["🖥️ Intel PDM On-Premise"]
        direction LR
        SFPA_PDM_Translator["PDM Translator"]:::appBox
    end
    style SFPP_Intel_PDM_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Microsoft_Power_BI_SaaS["☁️ Microsoft Power BI SaaS"]
        direction LR
        SFPA_Power_BI_DARC["Power BI (DARC)"]:::appBox
    end
    style SFPP_Microsoft_Power_BI_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_PTC_Windchill_On_Premise["🖥️ PTC Windchill On-Premise"]
        direction LR
        SFPA_ECM_Windchill["ECM (Windchill)"]:::appBox
    end
    style SFPP_PTC_Windchill_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_Analytics_Cloud_SaaS["☁️ SAP Analytics Cloud SaaS"]
        direction LR
        SFPA_SAP_SAC["SAP SAC"]:::appBox
    end
    style SFPP_SAP_Analytics_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_SAP_Ariba_Cloud_SaaS["☁️ SAP Ariba Cloud SaaS"]
        direction LR
        SFPA_SAP_Ariba["SAP Ariba"]:::appBox
    end
    style SFPP_SAP_Ariba_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_SAP_BusinessObjects_On_Premise["🖥️ SAP BusinessObjects On-Premise"]
        direction LR
        SFPA_SAP_BOBJ["SAP BOBJ"]:::eolBox
    end
    style SFPP_SAP_BusinessObjects_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_HANA_Sidecar_On_Premise["🖥️ SAP HANA Sidecar On-Premise"]
        direction LR
        SFPA_SideCar["SideCar"]:::appBox
    end
    style SFPP_SAP_HANA_Sidecar_On_Premise fill:#B2DFDB,stroke:#00695C,stroke-width:3px,color:#004D40

    subgraph SFPP_SAP_IBP_Cloud_SaaS["☁️ SAP IBP Cloud SaaS"]
        direction LR
        SFPA_SAP_IBP["SAP IBP"]:::appBox
    end
    style SFPP_SAP_IBP_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_SAP_MDG_On_Premise["🖥️ SAP MDG On-Premise"]
        direction LR
        SFPA_SAP_S_4_MDG["SAP S/4 MDG"]:::appBox
    end
    style SFPP_SAP_MDG_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_PaPM_On_Premise["🖥️ SAP PaPM On-Premise"]
        direction LR
        SFPA_SAP_PAPM["SAP PAPM"]:::appBox
    end
    style SFPP_SAP_PaPM_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_S_4HANA_Central_Finance["🖥️ SAP S/4HANA Central Finance"]
        direction LR
        SFPA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
    end
    style SFPP_SAP_S_4HANA_Central_Finance fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_S_4HANA_On_Premise["🖥️ SAP S/4HANA On-Premise"]
        direction LR
        SFPA_Corp_IP_S_4_HANA["Corp / IP S/4 HANA"]:::appBox
        SFPA_IF_S_4_HANA["IF S/4 HANA"]:::appBox
    end
    style SFPP_SAP_S_4HANA_On_Premise fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Snowflake_on_ECA_Cloud["☁️ Snowflake on ECA Cloud"]
        direction LR
        SFPA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
    end
    style SFPP_Snowflake_on_ECA_Cloud fill:#B2DFDB,stroke:#00695C,stroke-width:3px,color:#004D40

    SFPP_Intel_MES_On_Premise ==>|"Direct"| SFPP_Intel_Middleware_On_Premise
    SFPP_Intel_Middleware_On_Premise ==>|"Direct"| SFPP_Intel_PDF_SMH_Middleware_On_Premise
    SFPP_Intel_PDF_SMH_Middleware_On_Premise ==>|"EAI Connector"| SFPP_SAP_S_4HANA_On_Premise
    SFPP_SAP_S_4HANA_On_Premise ==>|"SLT"| SFPP_SAP_S_4HANA_Central_Finance
    SFPP_Intel_MES_On_Premise ==>|"Direct"| SFPP_Intel_Custom_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"Direct"| SFPP_Intel_PDF_SMH_Middleware_On_Premise
    SFPP_PTC_Windchill_On_Premise ==>|"PDM Translator"| SFPP_Intel_PDM_On_Premise
    SFPP_Intel_PDM_On_Premise ==>|"PDM Translator"| SFPP_SAP_MDG_On_Premise
    SFPP_SAP_MDG_On_Premise ==>|"DRF (Data Replication Frame..."| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"PDM Translator"| SFPP_Intel_PDM_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"ADF Rest API / SFTP(Blob)"| SFPP_Intel_ECA_Platform_Azure_Cloud
    SFPP_Intel_ECA_Platform_Azure_Cloud ==>|"Unity Catalog"| SFPP_Databricks_on_ECA_Azure_Cloud
    SFPP_Databricks_on_ECA_Azure_Cloud ==>|"Snowflake Connector / Snowpipe"| SFPP_Snowflake_on_ECA_Cloud
    SFPP_GraphiteConnect_Cloud_SaaS ==>|"MuleSoft & Reltio"| SFPP_SAP_MDG_On_Premise
    SFPP_SAP_S_4HANA_On_Premise ==>|"SLT"| SFPP_SAP_HANA_Sidecar_On_Premise
    SFPP_SAP_S_4HANA_Central_Finance ==>|"SLT"| SFPP_SAP_HANA_Sidecar_On_Premise
    SFPP_SAP_HANA_Sidecar_On_Premise ==>|"ADF Rest API / SFTP(Blob)"| SFPP_Intel_ECA_Platform_Azure_Cloud
    SFPP_Intel_Custom_On_Premise ==>|"ADF / DB Unity Catalog / Th..."| SFPP_Intel_ECA_Platform_Azure_Cloud
    SFPP_Snowflake_on_ECA_Cloud ==>|"MuleSoft/BODS"| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Intel_ICS_Phoenix_On_Premise ==>|"Direct"| SFPP_Intel_Custom_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"Direct"| SFPP_Snowflake_on_ECA_Cloud
    SFPP_Blue_Yonder_Cloud_SaaS ==>|"ADF / DB Unity Catalog / Co..."| SFPP_Intel_PDH_On_Premise
    SFPP_Intel_PDH_On_Premise ==>|"Snowflake Connector / Snowpipe"| SFPP_Snowflake_on_ECA_Cloud
    SFPP_Snowflake_on_ECA_Cloud ==>|"Remote Function Adapter / M..."| SFPP_SAP_PaPM_On_Premise
    SFPP_SAP_Analytics_Cloud_SaaS ==>|"SAC Data Export Service (AP..."| SFPP_Snowflake_on_ECA_Cloud
    SFPP_SAP_Analytics_Cloud_SaaS ==>|"SAP Odata services with con..."| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Snowflake_on_ECA_Cloud ==>|"MuleSoft/BODS"| SFPP_SAP_S_4HANA_Central_Finance
    SFPP_SAP_Analytics_Cloud_SaaS ==>|"SAP Odata services with con..."| SFPP_SAP_S_4HANA_Central_Finance
    SFPP_SAP_PaPM_On_Premise ==>|"SAP Integration Suite / Sma..."| SFPP_SAP_S_4HANA_On_Premise
    SFPP_SAP_IBP_Cloud_SaaS ==>|"ADF / DB Unity Catalog / Co..."| SFPP_Intel_PDH_On_Premise
    SFPP_SAP_Ariba_Cloud_SaaS ==>|"Apigee / MuleSoft"| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Snowflake_on_ECA_Cloud ==>|"Snowflake Connector / Snowpipe"| SFPP_Microsoft_Power_BI_SaaS
    SFPP_SAP_HANA_Sidecar_On_Premise ==> SFPP_SAP_BusinessObjects_On_Premise

    subgraph SFPLegend["📐 PLATFORM LEGEND"]
        direction LR
        SFPLC["☁️ Cloud"]
        SFPLS["🔮 SaaS"]
        SFPLO["🏢 On-Prem"]
        SFPLD["💾 Data Platform"]
        SFPLM["🔗 Middleware"]
    end
    style SFPLegend fill:#F5F5F5,stroke:#999,stroke-width:1px
    style SFPLC fill:#BBDEFB,stroke:#1565C0,stroke-width:3px,color:#0D47A1
    style SFPLS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C
    style SFPLO fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    style SFPLD fill:#B2DFDB,stroke:#00695C,stroke-width:3px,color:#004D40
    style SFPLM fill:#FFE0B2,stroke:#E65100,stroke-width:3px,color:#BF360C
```

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

## 5 Transformation Analysis

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 5.1 System Landscape Changes

| Category | Count | Systems |
|----------|:---:|---|
| **New Systems** | 35 | ATCR, CFIN S/4 HANA, Capacity Forecast Data Store, Corp / IP S/4 HANA, DMOCR, DXCR, ECA-ADLS, ECA-DataBricks, ECA-SnowFlake, ECM (Windchill), FCS, GraphiteConnect, ICS (Phoenix), IF Blue Yonder, IF PDH Consumptional, IF PDH Foundational, IF PDH Raw, IF S/4 HANA, IP Blue Yonder, IP PDH Consumptional, IP PDH Foundational, IP PDH Raw, PDF-SMH, PDH Consumptional, PDH Foundational, PDH Raw, PDM Translator, Power BI (DARC), SAP Ariba, SAP BOBJ, SAP PAPM, SAP S/4 MDG, SAP SAC, SCS, WSPW |
| **Retiring Systems** | 19 | APIGEE, Azure ADF, BOBJ, CFIN S/4, CIBR, Corp / IP S/4, DataBricks, EATS, ECA, EDW, FCA, Finance HANA, ICOST, Legacy MDG, PEGA, SAP BODS, SAP ECC, SAP PO, SnowFlake |
| **Continuing Systems** | 7 | — |

**New Connections (51):**

| Source | Target |
|---|---|
| ATCR | Capacity Forecast Data Store |
| CFIN S/4 HANA | SideCar |
| Capacity Forecast Data Store | ECA-ADLS |
| Corp / IP S/4 HANA | SideCar |
| DMOCR | Capacity Forecast Data Store |
| DXCR | Capacity Forecast Data Store |
| ECA-ADLS | ECA-DataBricks |
| ECA-DataBricks | ECA-SnowFlake |
| ECA-SnowFlake | CFIN S/4 HANA |
| ECA-SnowFlake | Corp / IP S/4 HANA |
| ECA-SnowFlake | IF S/4 HANA |
| ECA-SnowFlake | Power BI (DARC) |
| ECA-SnowFlake | SAP PAPM |
| ECM (Windchill) | PDM Translator |
| FCS | Capacity Forecast Data Store |
| GraphiteConnect | SAP S/4 MDG |
| ICS (Phoenix) | Capacity Forecast Data Store |
| IF Blue Yonder | IF PDH Raw |
| IF PDH Consumptional | ECA-SnowFlake |
| IF PDH Foundational | IF PDH Consumptional |
| IF PDH Raw | IF PDH Foundational |
| IF S/4 HANA | CFIN S/4 HANA |
| IF S/4 HANA | SideCar |
| IP Blue Yonder | IP PDH Raw |
| IP PDH Consumptional | ECA-SnowFlake |
| IP PDH Foundational | IP PDH Consumptional |
| IP PDH Raw | IP PDH Foundational |
| MARS | PDF-SMH |
| PDF-SMH | IF S/4 HANA |
| PDH Consumptional | ECA-SnowFlake |
| PDH Foundational | IP PDH Consumptional |
| PDH Raw | IP PDH Foundational |
| PDM Translator | SAP S/4 MDG |
| SAP Ariba | Corp / IP S/4 HANA |
| SAP Ariba | IF S/4 HANA |
| SAP IBP | IF PDH Raw |
| SAP PAPM | Corp / IP S/4 HANA |
| SAP PAPM | IF S/4 HANA |
| SAP S/4 MDG | Corp / IP S/4 HANA |
| SAP S/4 MDG | IF S/4 HANA |
| SAP SAC | CFIN S/4 HANA |
| SAP SAC | Corp / IP S/4 HANA |
| SAP SAC | ECA-SnowFlake |
| SAP SAC | IF S/4 HANA |
| SCS | Capacity Forecast Data Store |
| SPEED | ECA-ADLS |
| SPEED | PDM Translator |
| SideCar | ECA-ADLS |
| SideCar | SAP BOBJ |
| WSPW | ECA-SnowFlake |
| XEUS | PDF-SMH |

**Removed Connections (29):**

| Source | Target |
|---|---|
| APIGEE | PEGA |
| Azure ADF | DataBricks |
| CIBR | ICOST |
| CIBR | SAP PO |
| Corp / IP S/4 | ECA |
| DataBricks | SnowFlake |
| EATS | ICOST |
| ECA | CIBR |
| ECA | ICOST |
| EDW | CIBR |
| EDW | ICOST |
| FCA | ICOST |
| Finance HANA | APIGEE |
| Finance HANA | BOBJ |
| Finance HANA | SAP PO |
| ICOST | SAP BODS |
| Legacy MDG | SAP ECC |
| MARS | ICOST |
| SAP BODS | SAP ECC |
| SAP ECC | CFIN S/4 |
| SAP ECC | EDW |
| SAP ECC | Finance HANA |
| SAP ECC | SideCar |
| SAP IBP | ECA |
| SAP PO | SAP ECC |
| SPEED | EDW |
| SPEED | SAP PO |
| SideCar | Azure ADF |
| XEUS | ICOST |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Integration Complexity Delta

Systems with connectivity changes (and top hub systems):

| System | Current Connections | Future Connections | Delta |
|---|:---:|:---:|:---:|
| APIGEE | 2 | 0 | **-2** |
| ATCR | 0 | 1 | **+1** |
| Azure ADF | 2 | 0 | **-2** |
| BOBJ | 1 | 0 | **-1** |
| CFIN S/4 | 1 | 0 | **-1** |
| CFIN S/4 HANA | 0 | 4 | **+4** |
| CIBR | 4 | 0 | **-4** |
| Capacity Forecast Data Store | 0 | 7 | **+7** |
| Corp / IP S/4 | 1 | 0 | **-1** |
| Corp / IP S/4 HANA | 0 | 6 | **+6** |
| DMOCR | 0 | 1 | **+1** |
| DXCR | 0 | 1 | **+1** |
| DataBricks | 2 | 0 | **-2** |
| EATS | 1 | 0 | **-1** |
| ECA | 4 | 0 | **-4** |
| ECA-ADLS | 0 | 4 | **+4** |
| ECA-DataBricks | 0 | 2 | **+2** |
| ECA-SnowFlake | 0 | 11 | **+11** |
| ECM (Windchill) | 0 | 1 | **+1** |
| EDW | 4 | 0 | **-4** |
| FCA | 1 | 0 | **-1** |
| FCS | 0 | 1 | **+1** |
| Finance HANA | 4 | 0 | **-4** |
| GraphiteConnect | 0 | 1 | **+1** |
| ICOST | 8 | 0 | **-8** |
| ICS (Phoenix) | 0 | 1 | **+1** |
| IF Blue Yonder | 0 | 1 | **+1** |
| IF PDH Consumptional | 0 | 2 | **+2** |
| IF PDH Foundational | 0 | 2 | **+2** |
| IF PDH Raw | 0 | 3 | **+3** |
| IF S/4 HANA | 0 | 8 | **+8** |
| IP Blue Yonder | 0 | 1 | **+1** |
| IP PDH Consumptional | 0 | 3 | **+3** |
| IP PDH Foundational | 0 | 3 | **+3** |
| IP PDH Raw | 0 | 2 | **+2** |
| Legacy MDG | 1 | 0 | **-1** |
| PDF-SMH | 0 | 3 | **+3** |
| PDH Consumptional | 0 | 1 | **+1** |
| PDH Foundational | 0 | 1 | **+1** |
| PDH Raw | 0 | 1 | **+1** |
| PDM Translator | 0 | 3 | **+3** |
| PEGA | 1 | 0 | **-1** |
| Power BI (DARC) | 0 | 1 | **+1** |
| SAP Ariba | 0 | 2 | **+2** |
| SAP BOBJ | 0 | 1 | **+1** |
| SAP BODS | 2 | 0 | **-2** |
| SAP ECC | 7 | 0 | **-7** |
| SAP PAPM | 0 | 3 | **+3** |
| SAP PO | 4 | 0 | **-4** |
| SAP S/4 MDG | 0 | 4 | **+4** |
| SAP SAC | 0 | 4 | **+4** |
| SCS | 0 | 1 | **+1** |
| SideCar | 2 | 5 | **+3** |
| SnowFlake | 1 | 0 | **-1** |
| WSPW | 0 | 1 | **+1** |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

### 5.3 Release-over-Release Changes

Changes between adjacent releases — additions and retirements of applications, databases, and technology platforms.

#### R1 -> R2

*No changes detected between releases.*

#### R2 -> R3

**Applications:**

| Change | Applications |
|---|---|
| **Added** | ATCR, CFIN S/4 HANA, Capacity Forecast Data Store, Corp / IP S/4 HANA, DMOCR, DXCR, ECA-ADLS, ECA-DataBricks, ECA-SnowFlake, ECM (Windchill), FCS, GraphiteConnect, ICS (Phoenix), IF Blue Yonder, IF PDH Consumptional, IF PDH Foundational, IF PDH Raw, IF S/4 HANA, IP Blue Yonder, IP PDH Consumptional, IP PDH Foundational, IP PDH Raw, MARS, MES 300, PDF-SMH, PDH Consumptional, PDH Foundational, PDH Raw, PDM Translator, Power BI (DARC), SAP Ariba, SAP BOBJ, SAP IBP, SAP PAPM, SAP S/4 MDG, SAP SAC, SCS, SPEED, SideCar, WSPW, WorkStream, XEUS |
| **Retired** | e.g. MES 300, e.g. XEUS |

**Databases:**

| Change | Databases |
|---|---|
| **Added** | Azure Analysis Services, Azure Data Lake (ADLS), Delta Lake, N/A (Middleware), N/A (SaaS), SAP HANA, SAP HANA Cloud, SQL Server, Snowflake Cloud DW |
| **Retired** | e.g. Azure SQL, e.g. SAP HANA |

**Technology Platforms:**

| Change | Platforms |
|---|---|
| **Added** | Blue Yonder Cloud SaaS, Databricks on ECA Azure Cloud, GraphiteConnect Cloud SaaS, Intel Custom On-Premise, Intel ECA Platform Azure Cloud, Intel ICS (Phoenix) On-Premise, Intel PDF-SMH Middleware On-Premise, Intel PDH On-Premise, Intel PDM On-Premise, Microsoft Power BI SaaS, PTC Windchill On-Premise, SAP Analytics Cloud SaaS, SAP Ariba Cloud SaaS, SAP BusinessObjects On-Premise, SAP HANA Sidecar On-Premise, SAP IBP Cloud SaaS, SAP MDG On-Premise, SAP PaPM On-Premise, SAP S/4HANA Central Finance, SAP S/4HANA On-Premise, Snowflake on ECA Cloud |
| **Retired** | e.g. Azure PaaS, e.g. S/4 HANA 2023 |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>Finance Plan To Report (FPR)</span></div>
<div style="page-break-before: always;"></div>

## 6 Capability Detail Reference

For detailed architecture information, navigate to the individual L2 capability documents.
Each L2 document contains the full TOGAF BDAT analysis including:

- **Business Architecture** — BPMN process flows, business drivers, success criteria
- **Data Architecture** — Source-to-target data flows with DB platforms
- **Application Architecture** — Integration patterns, middleware, protocols
- **Technology Architecture** — Platform inventory, deployment topology
- **RICEFW / Clean Core** — SAP development object tracking

| # | Capability | L1 Process | Architecture Doc |
|:---:|---|---|---|
| 1 | Perform Transaction Processing | DC Manage Accounting and Control Data | [DC-010](towers/FPR/DC Manage Accounting and Control Data/DC-010/output/docs/systems-architecture/DC-010-Architecture.html) |
| 2 | Manage the General Ledger | DC Manage Accounting and Control Data | [DC-020](towers/FPR/DC Manage Accounting and Control Data/DC-020/output/docs/systems-architecture/DC-020-Architecture.html) |
| 3 | Perform Closing | DC Manage Accounting and Control Data | [DC-030](towers/FPR/DC Manage Accounting and Control Data/DC-030/output/docs/systems-architecture/DC-030-Architecture.html) |
| 4 | Perform Fixed Asset Accounting | DC Manage Accounting and Control Data | [DC-040](towers/FPR/DC Manage Accounting and Control Data/DC-040/output/docs/systems-architecture/DC-040-Architecture.html) |
| 5 | Project Accounting | DC Manage Accounting and Control Data | [DC-050](towers/FPR/DC Manage Accounting and Control Data/DC-050/output/docs/systems-architecture/DC-050-Architecture.html) |
| 6 | Manage Taxes | DC Manage Accounting and Control Data | [DC-060](towers/FPR/DC Manage Accounting and Control Data/DC-060/output/docs/systems-architecture/DC-060-Architecture.html) |
| 7 | Revenue Recognition | DC Manage Accounting and Control Data | [DC-100](towers/FPR/DC Manage Accounting and Control Data/DC-100/output/docs/systems-architecture/DC-100-Architecture.html) |
| 8 | Manage Intercompany | DC Manage Accounting and Control Data | [DC-110](towers/FPR/DC Manage Accounting and Control Data/DC-110/output/docs/systems-architecture/DC-110-Architecture.html) |
| 9 | Maintenance & Management Accounting | DC Manage Accounting and Control Data | [DC-120](towers/FPR/DC Manage Accounting and Control Data/DC-120/output/docs/systems-architecture/DC-120-Architecture.html) |
| 10 | Perform Overhead Accounting and Allocation | DS Provide Decision Support | [DS-010](towers/FPR/DS Provide Decision Support/DS-010/output/docs/systems-architecture/DS-010-Architecture.html) |
| 11 | Perform Product Costing and Inventory Valuation | DS Provide Decision Support | [DS-020](towers/FPR/DS Provide Decision Support/DS-020/output/docs/systems-architecture/DS-020-Architecture.html) |
| 12 | Perform Customer and Product Profitability Analysis | DS Provide Decision Support | [DS-030](towers/FPR/DS Provide Decision Support/DS-030/output/docs/systems-architecture/DS-030-Architecture.html) |
| 13 | Plan the Business | MB Plan and Manage Business | [MB-060](towers/FPR/MB Plan and Manage Business/MB-060/output/docs/systems-architecture/MB-060-Architecture.html) |
| 14 | Prepare Budgets | MB Plan and Manage Business | [MB-070](towers/FPR/MB Plan and Manage Business/MB-070/output/docs/systems-architecture/MB-070-Architecture.html) |
| 15 | Manage Liquidity | MR Manage Capital and Risk | [MR-010](towers/FPR/MR Manage Capital and Risk/MR-010/output/docs/systems-architecture/MR-010-Architecture.html) |
| 16 | Manage Capital Structure | MR Manage Capital and Risk | [MR-020](towers/FPR/MR Manage Capital and Risk/MR-020/output/docs/systems-architecture/MR-020-Architecture.html) |
| 17 | Manage Financial Risk | MR Manage Capital and Risk | [MR-030](towers/FPR/MR Manage Capital and Risk/MR-030/output/docs/systems-architecture/MR-030-Architecture.html) |
| 18 | In-House Banking | MR Manage Capital and Risk | [MR-070](towers/FPR/MR Manage Capital and Risk/MR-070/output/docs/systems-architecture/MR-070-Architecture.html) |
| 19 | Process Receipts | OR Receivables Management | [OR-140](towers/FPR/OR Receivables Management/OR-140/output/docs/systems-architecture/OR-140-Architecture.html) |

