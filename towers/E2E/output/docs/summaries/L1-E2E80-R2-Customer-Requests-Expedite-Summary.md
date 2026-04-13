<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-80 R2 Customer Requests Expedite</h1>
  <h2 style="font-size:24px;">TOGAF BDAT — Aggregated Architecture View</h2>
  <p style="font-size:18px; color:#555;">Tower: End-to-End Integrated Processes (E2E) · Process: E2E-80 R2 Customer Requests Expedite · R1 – R5</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-80 R2 Customer Requests Expedite</span></div>
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
- [6. Capability Detail Reference](#6-capability-detail-reference)

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-80 R2 Customer Requests Expedite</span></div>
<div style="page-break-before: always;"></div>

## 1 Executive Summary

This **L1** summary aggregates architecture diagrams from **1** L2 capabilities across **Tower: End-to-End Integrated Processes (E2E) · Process: E2E-80 R2 Customer Requests Expedite · R1 – R5**.

The diagrams below show the consolidated current-state and future-state system landscape **without duplicates** — each system and connection appears only once even when shared across capabilities. For detailed data flows, integration patterns, technology stacks, and business architecture, refer to the individual L2 capability documents linked in [§6 Capability Detail Reference](#6-capability-detail-reference).

| Metric | Current-State | Future-State | Delta |
|--------|:---:|:---:|:---:|
| **Unique Systems** | 2 | 2 | +0 |
| **System Connections** | 1 | 1 | +0 |
| **Total Flow Hops** | 1 | 1 | +0 |
| **Capabilities Covered** | 1 | 1 | — |

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-80 R2 Customer Requests Expedite</span></div>
<div style="page-break-before: always;"></div>

## 2 Capability Inventory

The following **1** capabilities are aggregated in this summary.
Click a capability ID to view its full TOGAF BDAT architecture document.

| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |
|:---:|:---:|---|---|:---:|:---:|
| 1 | [E2E-80](/towers/E2E/E2E-80-R2-Customer-Requests-Expedite/E2E-80/output/docs/systems-architecture/E2E-80-Architecture.html) | R2A Option 1  Customer Requests Expedite - Service Fee with Existing SO | E2E-80 R2 Customer Requests Expedite | 1 | 1 |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-80 R2 Customer Requests Expedite</span></div>
<div style="page-break-before: always;"></div>

## 3 Current-State Architecture

Aggregated current-state: **2** systems, **1** connections, **1** flow hops.


### 3.1 Application Architecture

> System-to-system integration flows. Color indicates IAPM lifecycle status (green = deployed, blue = developing, red = end-of-life).

```mermaid
graph TB
    %% -- ArchiMate 3.2 + Azure style classes --
    classDef business      fill:#FFFFB3,stroke:#F9A825,stroke-width:2px,color:#000
    classDef app           fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef data          fill:#BBDEFB,stroke:#1565C0,stroke-width:1px,color:#0D47A1,stroke-dasharray: 5 5
    classDef middleware    fill:#FFE0B2,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef eol           fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C
    classDef saas          fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    classDef cloud         fill:#BBDEFB,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef onprem        fill:#C8E6C9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20

    subgraph AL["📦 Application Layer — Systems Integration"]
        direction LR
        SCA_e_g__MES_300["📦 e.g. MES 300"]
        SCA_e_g__XEUS["📦 e.g. XEUS"]
    end

    SCA_e_g__MES_300 -->|"e.g. Direct / API / File"| SCA_e_g__XEUS

    class SCA_e_g__MES_300 app
    class SCA_e_g__XEUS app
    style BL fill:#FFFDE7,stroke:#F9A825,stroke-width:2px
    style AL fill:#E3F2FD,stroke:#0078D4,stroke-width:2px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVlG1r2zAQx7-KUOmrpZlsxw_1i4Fsy1BIYSwbDOYRVOuSmPkJS6bL2n73KfHiJGqzsXshkE7_3-lO0j3hvBGAQ7zueLtBn6OsRtqur9HNDaJdvinuuQLkTG30DtFffQdIqm0JKC-5lCD1tkGxnyewQg-9LGqQEu1tVZRleJVqi5yJVF3zA_T0lga2-2d681gItQnt9uckb8qmC68IIQaTty062sCMY-am6cgkxA-S2V-YDvViAyu44iY2ihKWRiPWcj03JudY6wSbzHxqHdyCyw3vOr4NkYtcI1hVCFHCI9cVPKkLI5E9BmOeaxFyMYcodTxi5gBN-ao0aRonyREbe3ZgB5exvhVbJlZyLk0ssyLG_BHrR1ZK7YvYGbVmgYnNy6YX_19x26y4gW3qtoPKeB8B8-LbEWszP3Eun9aKXGbrZzeAZf8w_Ac6_5bhrBeBI_SYg4do25ZFzlXR1GjOt9ChrLeJNUOLrVRQSXRXK9Di3YYMfx94OxNFB_kg-3RcXcR0Ccv1cnnPFkuHEDMcTNdTpH1I-85wo_Ar-7J4U7VzjBKoxSE5M6T-wh-eM7zXJPtDoveIfrzTY1qUkOHn82AHzr76r2n6r77p30mPzqGJRPNjg0hOntaFBnEqpQcpc1I7Tf7VB_AEV9BVvBA4fMJqA9Wu6QlY8b5U-GWCea-axbbOcai6Hia4b3V3gKTg-i6rYfHlNybVltg=" title="View full diagram">&#128065; View Diagram</a></div>



### 3.2 Data Architecture

> Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef dbCyl fill:#C8E6C9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef dbCloud fill:#BBDEFB,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef dbData fill:#B2EBF2,stroke:#00838F,stroke-width:2px,color:#004D40
    classDef eolBox fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C

    subgraph SCDCL_e_g_Azure_SQL[" "]
        direction TB
        SCDA_e_g_XEUS["e.g. XEUS"]:::appBox
        SCDD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCloud
        SCDA_e_g_XEUS -.-> SCDD_e_g_Azure_SQL
    end
    style SCDCL_e_g_Azure_SQL fill:#E8F5E9,stroke:#388E3C,stroke-width:1px

    subgraph SCDCL_e_g_SAP_HANA[" "]
        direction TB
        SCDA_e_g_MES_300["e.g. MES 300"]:::appBox
        SCDD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbData
        SCDA_e_g_MES_300 -.-> SCDD_e_g_SAP_HANA
    end
    style SCDCL_e_g_SAP_HANA fill:#E3F2FD,stroke:#1976D2,stroke-width:1px

    SCDD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| SCDD_e_g_Azure_SQL

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVYtumzAU_RWLKtImJV0CeRCkVgJs1kq0y0q6TSoTcsAkqA4gHmvSNP8-m0eSpqHVNCMhcx_nXp9j7I3gRh4RFKHV2gRhkClgYwvZgiyJLSjAFmY4ZbM2m6XEzZMgW5vkD6Glk0ZR7S1SfuAkwDNKUu5mOH4UZlbwXEH1BvGqDOZ2Ay8Dui49FplHBNxft4HKABj4toii0ZO7wElWoeUpucGrn4GXLbjFxzQlPG6RLamJZ4QWZbMkL6whW5YVYzcI59wsDbgxweHjgbE_2G7BttWyw10tMNXsELDhUpymkPgAx7EWrYAfUKqc6ToaGEY7zZLokShn3e5Ihv3qs_PEW1PEeNV2Ixol3C2pQ_0Iz5vpa1rDyWioj3dwIhpBSWyE62kDJHbfwtEo9ypATYPI0P6zP4gzXOOJSDPEAzxZko138Pqwf9wgieieP8PQIdzj6UNRFuVGPG3U03usvxIxzWfzBMcLYOlQNx3izB31OU-IY303H2yByfu7DOTDCxLiZkEU7gTlg2WqReIvdG-xHHI-Pwd8znIVRSmlfhUOj-p8sgU792TJY2_P7du5T7psjRynCAIsyBY-c7RKmYbqoHPeuTxRoQwnYZWXZmtKTq24IhTJxgDtd5Aky0jSXxPaY79dM4WWOnGu1Fv1Xxm8QZYjdbs1iewTsM8PeNwVe4dGFgN4zI5Fvh2bGzjisa7wAY11WM2iZIgG3LHYG4-GUGxk8U0xcHFx-VIRAQvawBegTq7Z2wgoO_5eTgp9pIlJ5qzfhwNmXK8LoDpVgXqnX11PkT69v0PARF_RLWzQyrzbW02Hq6rGMQ1czL2n1TEd2KDHt7AzScgSQG2_pdf0VabekFoeSoeJr_8FltpUtTh-JhRnfpQsG3aB6SC2NBR6ncjvmIFPyqWVZ81J7Ut262NowJ-d3uPx-I3YQltYkmSJA09QNuX1xm5Jj_g4pxm7oAScZ5G1Dl1BKa4cIY89nBEYYKbmsjRu_wI290jh" title="View full diagram">&#128065; View Diagram</a></div>



### 3.3 Technology Architecture

> Applications grouped by hosting platform. Cloud platforms marked with ☁️.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef platBox fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C

    subgraph SCPP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        SCPA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style SCPP_e_g_Azure_PaaS fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C

    subgraph SCPP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        SCPA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style SCPP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    SCPP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| SCPP_e_g_Azure_PaaS

    subgraph SCPLegend["📐 PLATFORM LEGEND"]
        direction LR
        SCPLC["☁️ Cloud"]
        SCPLS["🔮 SaaS"]
        SCPLO["🏢 On-Prem"]
        SCPLD["💾 Data Platform"]
        SCPLM["🔗 Middleware"]
    end
    style SCPLegend fill:#F5F5F5,stroke:#999,stroke-width:1px
    style SCPLC fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C
    style SCPLS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C
    style SCPLO fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    style SCPLD fill:#B2EBF2,stroke:#00838F,stroke-width:3px,color:#004D40
    style SCPLM fill:#FFE0B2,stroke:#E65100,stroke-width:3px,color:#BF360C
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqllWtvmzAUhv-KRZVvacstCUHqJK5bpaSJSrtNGhNywCSoDkZg2qRp_vtsyI2kqToVJGSfc_z4vD42XgkhiZCgC63WKkkTqoOVL9AZmiNf0IEvTGDBWm3WKlBY5gldDtAzwrUTE7L1VkN-wjyBE4wK7macmKTUS143KEnNFnUwt7twnuBl7fHQlCDweNsGBgMw-LqKwuQlnMGcbmhlgYZw8SuJ6IxbYogLxONmdI4HcIJwNS3Ny8qaMlleBsMknXKzKnJjDtOnA2NHXK_ButXy091c4MH0U8CeEMOisFEMYJaZZAHiBGP9wrKcjuu2C5qTJ6RfiGJPs9VN9_KFp6bL2aIdEkxy7laMrnXEyzCkB0DN6Vr9HVB2erYiN4HKHiiZHUcWj4CI4D3PdS3blnc8qytrsnY2QbMnWRJLsCYW5WSaw2wGPGs8DlAwDYzXMkfBGELvjy_4pdwVJb-MkcgmvZpegcoNuNsX_tYM_kRJjkKakBQM7vdWBjUq6G_nkeMqAm-zsbqu18tch6M02mRElxi9l85GrWnajmt-WA7ltBzn1HqBGvww7oxAFmWlEhxpSsS-EewcyvauVcDjAI_7H-VDxwsUUdyKZ13Aup_X30jwSxuoxp8B39x8e9ukaFeCwDUwxrfs6yaYHea39yry3rIO0JRJOVzJMBLBeGA8uKP7IRg43507-3MLOLCOd6CFSRk1BvMwr1E3mS3e8e7kUaNtVMi-MZLBKL0c52h-Emg3kp8gYEMKwZgd4Zjkp-HDxuxSDwyTKMLoBeZoF3ta3HqZtge4w99dPfv9frOYUrY4Hm596TQ0WduT5Uim4_R2rJ4pucb5baUakqqdsEZf_sftWfZWo-yYrnygUVM09wONqq2esIa7f6UjmnuW0-1IoniWZbpKV7SEtjBH-RwmkaCv6luPXZ4RimGJKbu3BFhS4i3TUNCrm0goswhSZCeQnYp5bVz_A9mNUh4=" title="View full diagram">&#128065; View Diagram</a></div>


<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-80 R2 Customer Requests Expedite</span></div>
<div style="page-break-before: always;"></div>

## 4 Future-State Architecture

Aggregated future-state: **2** systems, **1** connections, **1** flow hops.


### 4.1 Application Architecture

> System-to-system integration flows. Color indicates IAPM lifecycle status (green = deployed, blue = developing, red = end-of-life).

```mermaid
graph TB
    %% -- ArchiMate 3.2 + Azure style classes --
    classDef business      fill:#FFFFB3,stroke:#F9A825,stroke-width:2px,color:#000
    classDef app           fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef data          fill:#BBDEFB,stroke:#1565C0,stroke-width:1px,color:#0D47A1,stroke-dasharray: 5 5
    classDef middleware    fill:#FFE0B2,stroke:#E65100,stroke-width:2px,color:#BF360C
    classDef eol           fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C
    classDef saas          fill:#E1BEE7,stroke:#7B1FA2,stroke-width:2px,color:#4A148C
    classDef cloud         fill:#BBDEFB,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    classDef onprem        fill:#C8E6C9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20

    subgraph AL["📦 Application Layer — Systems Integration"]
        direction LR
        SFA_e_g__MES_300["📦 e.g. MES 300"]
        SFA_e_g__XEUS["📦 e.g. XEUS"]
    end

    SFA_e_g__MES_300 -->|"e.g. Direct / API / File"| SFA_e_g__XEUS

    class SFA_e_g__MES_300 app
    class SFA_e_g__XEUS app
    style BL fill:#FFFDE7,stroke:#F9A825,stroke-width:2px
    style AL fill:#E3F2FD,stroke:#0078D4,stroke-width:2px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVlG1r2zAQx7-KUOmrpZlsxw_1i4EfJCikMJYNBvMIqnVJzPyEJdNlbb_7lHhxErXZ2L0QSKf_73Qn6Z5w3gjAIV53vN2gz3FWI23X1-jmBkVdvinuuQLkTG30DkW_-g6QVNsSUF5yKUHqbYNiP09hhR56WdQgJdrbqijL8Ippi52JVF3zA_T0Ngps98_05rEQahPa7c9J3pRNF14RQgwmb1t0tIGZJNRlbGQS4gfp7C9MJ_ISAyu44iY2jlPK4hFruZ6bkHOsdYJNZ35kHdyCyw3vOr4NkYtcI1hVCFHCI9cVPKkLJbE9BqOeaxFyMYeYOR4xc4CmfFUaxpI0PWITzw7s4DLWtxLLxErOpYmlVkypP2L92GKRfRE7i6xZYGLzsunF_1fcNituYJu67aAy3kdAveR2xNrUT53Lp7Vil9r62Q1g2T8M_yGaf8tw1ovAEXrMwUNR25ZFzlXR1GjOt9ChrLeJNUOLrVRQSXRXK9Di3YYMfx94OxNFB_kg-3RcXbBoCcv1cnlPF0uHEDMcTNdTpH1I-85wo_Ar_bJ4U7VzjBKoxSE5M6T-wh-eM7zXpPtDovco-ninR1aUkOHn82AHzr76r2n6r77p30mPzqGJxPNjg0hPntaFBnEqjQ5S6jCbpf_qA3iCK-gqXggcPmG1gWrX9ASseF8q_DLBvFfNYlvnOFRdDxPct7o7QFpwfZfVsPjyGzwRluo=" title="View full diagram">&#128065; View Diagram</a></div>



### 4.2 Data Architecture

> Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef dbCyl fill:#C8E6C9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef dbCloud fill:#BBDEFB,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef dbData fill:#B2EBF2,stroke:#00838F,stroke-width:2px,color:#004D40
    classDef eolBox fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C

    subgraph SFDCL_e_g_Azure_SQL[" "]
        direction TB
        SFDA_e_g_XEUS["e.g. XEUS"]:::appBox
        SFDD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCloud
        SFDA_e_g_XEUS -.-> SFDD_e_g_Azure_SQL
    end
    style SFDCL_e_g_Azure_SQL fill:#E8F5E9,stroke:#388E3C,stroke-width:1px

    subgraph SFDCL_e_g_SAP_HANA[" "]
        direction TB
        SFDA_e_g_MES_300["e.g. MES 300"]:::appBox
        SFDD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbData
        SFDA_e_g_MES_300 -.-> SFDD_e_g_SAP_HANA
    end
    style SFDCL_e_g_SAP_HANA fill:#E3F2FD,stroke:#1976D2,stroke-width:1px

    SFDD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| SFDD_e_g_Azure_SQL

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVYtumzAU_RWLKtImJV0CeRCkVgJs1kq0y0q6TSoTcsAkqA4gHmvSNP8-m0eSpqHVNCMhcx_nXp9j7I3gRh4RFKHV2gRhkClgYwvZgiyJLSjAFmY4ZbM2m6XEzZMgW5vkD6Glk0ZR7S1SfuAkwDNKUu5mOH4UZlbwXEH1BvGqDOZ2Ay8Dui49FplHBNxft4HKABj4toii0ZO7wElWoeUpucGrn4GXLbjFxzQlPG6RLamJZ4QWZbMkL6whW5YVYzcI59wsDbgxweHjgbE_2G7BttWyw10tMNXsELDhUpymkPgAx7EWrYAfUKqc6ToaGEY7zZLokShn3e5Ihv3qs_PEW1PEeNV2Ixol3C2pQ_0Iz5vpa1rDyWioj3dwIhpBSWyE62kDJHbfwtEo9ypATYPI0P6zP4gzXOOJSDPEAzxZko138Pqwf9wgieieP8PQIdzj6UNRFuVGPG3U03usvxIxzWfzBMcLYBlQNx3izB31OU-IY303H2yByfu7DOTDCxLiZkEU7gTlg2WqReIvdG-xHHI-Pwd8znIVRSmlfhUOj-p8sgU792TJY2_P7du5T7psjRynCAIsyBY-c7RKmYbqoHPeuTxRoQwnYZWXZmtKTq24IhTJxgDtd5Aky0jSXxPaY79dM4WWOnGu1Fv1Xxm8QZYjdbs1iewTsM8PeNwVe4dGFgN4zI5Fvh2bGzjisa7wAY11WM2iZIgG3LHYG4-GUGxk8U0xcHFx-VIRAQvawBegTq7Z2wgoO_5eTgp9pIlJ5qzfhwNmXK8LoDpVgXqnX11PkT69v0PARF_RLWzQyrzbW02Hq6rGMQ1czL2n1TEd2KDHt7AzScgSQG2_pdf0VabekFoeSoeJr_8FltpUtTh-JhRnfpQsG3aB6SC2NBR6ncjvmIFPyqWVZ81J7Ut262NowJ-d3uPx-I3YQltYkmSJA09QNuX1xm5Jj_g4pxm7oAScZ5G1Dl1BKa4cIY89nBEYYKbmsjRu_wLBokkL" title="View full diagram">&#128065; View Diagram</a></div>



### 4.3 Technology Architecture

> Applications grouped by hosting platform. Cloud platforms marked with ☁️.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef platBox fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C

    subgraph SFPP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        SFPA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style SFPP_e_g_Azure_PaaS fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C

    subgraph SFPP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        SFPA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style SFPP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    SFPP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| SFPP_e_g_Azure_PaaS

    subgraph SFPLegend["📐 PLATFORM LEGEND"]
        direction LR
        SFPLC["☁️ Cloud"]
        SFPLS["🔮 SaaS"]
        SFPLO["🏢 On-Prem"]
        SFPLD["💾 Data Platform"]
        SFPLM["🔗 Middleware"]
    end
    style SFPLegend fill:#F5F5F5,stroke:#999,stroke-width:1px
    style SFPLC fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C
    style SFPLS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C
    style SFPLO fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    style SFPLD fill:#B2EBF2,stroke:#00838F,stroke-width:3px,color:#004D40
    style SFPLM fill:#FFE0B2,stroke:#E65100,stroke-width:3px,color:#BF360C
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqllWtvmzAUhv-KRZVvacstCUHqJK5bpaSJSrtNGhNywCSoDkZg2qRp_vtsyI2kqToVJGSfc_z4vD42XgkhiZCgC63WKkkTqoOVL9AZmiNf0IEvTGDBWm3WKlBY5gldDtAzwrUTE7L1VkN-wjyBE4wK7macmKTUS143KEnNFnUwt7twnuBl7fHQlCDweNsGBgMw-LqKwuQlnMGcbmhlgYZw8SuJ6IxbYogLxONmdI4HcIJwNS3Ny8qaMlleBsMknXKzKnJjDtOnA2NHXK_ButXy091c4MH0U8CeEMOisFEMYJaZZAHiBGP9wrKcjuu2C5qTJ6RfiGJPs9VN9_KFp6bL2aIdEkxy7laMrnXEyzCkB0DN6Vr9HVB2erYiN4HKHiiZHUcWj4CI4D3PdS3blnc8qytrsnY2QbMnWRJLsCYW5WSaw2wGPHc8DlAwDYzXMkfBGELvjy_4pdwVJb-MkcgmvZpegcoNuNsX_tYM_kRJjkKakBQM7vdWBjUq6G_nkeMqAm-zsbqu18tch6M02mRElxi9l85GrWnajmt-WA7ltBzn1HqBGvww7oxAFmWlEhxpSsS-EewcyvauVcDjAI_7H-VDxwsUUdyKZ13Aup_X30jwSxuoxp8B39x8e9ukaFeCwDUwxrfs6yaYHea39yry3rIO0JRJOVzJMBLBeGA8uKP7IRg43507-3MLOLCOd6CFSRk1BvMwr1E3mS3e8e7kUaNtVMi-MZLBKL0c52h-Emg3kp8gYEMKwZgd4Zjkp-HDxuxSDwyTKMLoBeZoF3ta3HqZtge4w99dPfv9frOYUrY4Hm596TQ0WduT5Uim4_R2rJ4pucb5baUakqqdsEZf_sftWfZWo-yYrnygUVM09wONqq2esIa7f6UjmnuW0-1IoniWZbpKV7SEtjBH-RwmkaCv6luPXZ4RimGJKbu3BFhS4i3TUNCrm0goswhSZCeQnYp5bVz_A4WYUlo=" title="View full diagram">&#128065; View Diagram</a></div>


<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-80 R2 Customer Requests Expedite</span></div>
<div style="page-break-before: always;"></div>

## 5 Transformation Analysis


### 5.1 System Landscape Changes

| Category | Count | Systems |
|----------|:---:|---|
| **New Systems** | 0 | — |
| **Retiring Systems** | 0 | — |
| **Continuing Systems** | 2 | — |


### 5.2 Integration Complexity Delta

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-80 R2 Customer Requests Expedite</span></div>
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
| 1 | R2A Option 1  Customer Requests Expedite - Service Fee with Existing SO | E2E-80 R2 Customer Requests Expedite | [E2E-80](/towers/E2E/E2E-80-R2-Customer-Requests-Expedite/E2E-80/output/docs/systems-architecture/E2E-80-Architecture.html) |

