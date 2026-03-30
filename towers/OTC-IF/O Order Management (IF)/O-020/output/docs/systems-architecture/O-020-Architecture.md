<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">O-020 — Capture Orders (IF)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Order To Cash (IF) (OTC-IF) Tower<br/>
  Capability O-020 · O Order Management (IF)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **O-020 Capture Orders (IF)** within the IAO program. It includes 6 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Order To Cash (IF) (OTC-IF) |
| **Process Group** | O Order Management (IF) |
| **Capability** | O-020 - Capture Orders (IF) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 11 Interfaces, 64 Enhancements, 11 Forms, 1 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: "loose"` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Order To Cash (IF) |
| **L1 Process** | O Order Management (IF) |
| **L2 Capability** | O-020 - Capture Orders (IF) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Foundry Customer Order Digitization | Digitize end-to-end order capture, pricing, and fulfillment for Intel Foundry customers | IDM 2.0 Foundry Revenue | High |
| 2 | Global Trade Compliance Automation | Automate export/import compliance screening and customs declarations | Global Trade Operations | High |
| 3 | Revenue Recognition Accuracy | Ensure compliant revenue recognition aligned with ASC 606 through S/4 HANA billing | Finance & Compliance | Medium |
| 4 | O-020 Process Migration | Migrate Capture Orders (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Order Management (Intel Foundry) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order-to-Cash Cycle Time | < 5 business days | End-to-end cycle from order capture to cash application | 8 business days (legacy) | OTC Process Owner |
| Trade Compliance Screening Rate | 100% | Orders screened for denied parties and export controls | 99.2% (current) | Global Trade Manager |
| Billing Accuracy | > 99.8% | Invoices generated without errors requiring credit/re-bill | 98.5% (current) | Billing Manager |
| O-020 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **6 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for O-020 Capture Orders (IF).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | O-020-110_Create_Service_Contract_Order_(IF) | O-020-110_Create_Service_Contract_Order_(IF) | Customer Business Analyst | 15 | 3 |
| 2 | O-020-120_Create_Customer_Contract_Order_(IF) | O-020-120_Create_Customer_Contract_Order_(IF) | Customer Business Analyst | 15 | 3 |
| 3 | O-020-140_Create_No-charge_Order_(IF) | O-020-140_Create_No-charge_Order_(IF) | Customer Business Analyst | 7 | 2 |
| 4 | O-020-150_Create_Subsequent_Delivery_Free_of_Charge_(FOC)_Order_(IF) | O-020-150_Create_Subsequent_Delivery_Free_of_Charge_(FOC)_Order_(IF) | Customer Business Analyst | 8 | 3 |
| 5 | O-020-190_Create_Sample_Order_(IF) | O-020-190_Create_Sample_Order_(IF) | Customer Business Analyst | 1 | 1 |
| 6 | O-020-200_Create_Prototype_Order_(IF) | O-020-200_Create_Prototype_Order_(IF) | Customer Business Analyst, Pricing Manager | 14 | 8 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 O-020-110_Create_Service_Contract_Order_(IF) — O-020-110_Create_Service_Contract_Order_(IF)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 15 | **Gateways**: 3

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Validate Order"]
        n2["fa:fa-user Fix Exception"]
        n3["fa:fa-user Change Contract"]
        n4["fa:fa-user Receive Service Contract Details"]
        n5["fa:fa-user Create Service Contract Order"]
        n6["fa:fa-user Determine Order Type"]
        n7["fa:fa-user Derive MMID using CPN"]
        n8["fa:fa-user Create Call-off Order"]
        n9[["fa:fa-cog Calculate Pricing"]]
        n10[["fa:fa-cog Create Service Contract Order"]]
        n11[["fa:fa-cog Validate Order"]]
        n12[["fa:fa-cog Capture Service Contract Details"]]
        n13[["fa:fa-cog Determine Order Type"]]
        n14[["fa:fa-cog Derive MMID using CPN"]]
        n15[["fa:fa-cog Calculate Pricing"]]
        n16(["fa:fa-play Service Contract Details Received Manually"])
        n17(["fa:fa-play Customer Contract Details Received Electronically via EDI"])
        n18["Process Order"]
        n19{{"fa:fa-code-branch Any Exceptions?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n2 --> n3
    n3 --> n20
    n10 --> n11
    n5 --> n1
    n4 --> n6
    n6 --> n5
    n12 --> n13
    n13 --> n10
    n16 --> n4
    n7 --> n9
    n20 --> n8
    n11 --> n14
    n1 --> n7
    n21 --> n19
    n14 --> n15
    n9 --> n21
    n15 --> n21
    n17 --> n12
    n8 --> n18
    n19 -->|"No"| n20
    n19 -->|"Yes"| n2
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
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 startEvt
    class n17 startEvt
    class n18 startEvt
    class n19 gateway
    class n20 gateway
    class n21 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVluP4jYY_StWRiNaKUhxLgTy0AoCqUbqbEdlulW19ME4DlhjEmQnDCzLf69NLuBM0mpVHkbzHZ9zvktix2cDZzExAuPx8UxTmgfgPMi3ZEcGARiskSADE5TAZ8QpWjMiBoqTZGm-pF-vNOjuj4qmsAjtKDspdEk2GQF_PJlgKoXMBAKlYigIp8nAHOw53SF-CjOWccV-IOPESq7ZqqVZxmPCbwTL8iH2pJTRlNxgx3d9N1I6QXCWxppp4iXjBA8uqjiWveMt4vm1_EKQZ3T8k8b5VsYJYoJIzjbfsV_RmjDVY84LheGCH-phUKHypHJgyz3CNN1I3LUkxFH6doM863IBl8fHVdokBa_zVQrkDzMkxJwkQOQSXhxykFDGggc3nEaeZYqcZ28keLAX_tyxTaw6CWTrlqmGO3wndLPNg3XG4oo6fFc9BPb-aPJjYFsmP8m_rVwkjW-ZwpE9tsdNppkPQxjWmZIk-V-Z5Fz5KxJvVa6FE9nRvMkFvZEXWh_96jbnrj-F7TkRfqCY3JlGUeQsbqNajDxo9ZvOImdkhS3TDcrJOzrdDCeh2xhGnh9Bv9ewzNeusli_8AzXhs7Ci7zG0J_BaGr3GrpT6I6rCqXPhqP9FoSFyLMd4WBWCPm-CwGmKWInkZc89Uvhl5WRoCBBQzV28BkxGsvGwG9q46yMv--otk6N6BEsjpjsc5qlOtPRmeEWpRsCQvlOcIRznevq3N8JJvRAwLJ8ZI0IzEmOKBO62Gsl4kTV_kHb0cxIV0p3wndySCUXvJ72RBf4bQFXZT4_P82Bmu4GhC-fdMW4s7gQMTbMkqSrqMmXRoKzjaLiginRC6fqXJDsezq0Wvz_aF_TQl374cFrZLtd2D4v-L8-JE3u6PKeYWsSty3pHrem8b5zfKMfGv6eyZ3c1079UsbgGaWFfH4n6fTjvZPfcmp2Xr_VghEsN3NKsTIEB4rAYv7UNlbvkDoU1ObteGHg5Hy-tRyT4Vp-RfBW7vPTbW-Kn1fG5XK_ka1uFTliJod7IL-UR1tbBr9XJr8Z5T-pDYbDn-TBUIVOGdZHv3yTSwBWJ3fqVXEVumU4qsJRGXq1unKHtT2s_GHjXyncKvbLcFJXV6Uf13RY6Wt-Ffs1v16vDWBVIKxLmlQN1g1Arw1UJUC7AsZV3NRwtfi2Mj5lK-Pb_azqhb-IKFfuviOq1Pr7qcF2N-x0w2437HXDo27Y74bH3fDk_iutd2T1L8H-Jbt_yelfcvuXvP6lUXMV03G_Bx_34JP6VqE_O6sbhjVsmIY8bHaIxkZwNq43bXkbj0mCCpYbF9NARZ4tTyk2guuN1Cj26qyfUyQvCrsSvPwDrUmqtQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 O-020-120_Create_Customer_Contract_Order_(IF) — O-020-120_Create_Customer_Contract_Order_(IF)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 15 | **Gateways**: 3

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Validate Order"]
        n2["fa:fa-user Calculate Pricing"]
        n3["fa:fa-user Fix Exception"]
        n4["fa:fa-user Change Customer Contract"]
        n5["fa:fa-user Capture Customer Contract Details"]
        n6["fa:fa-user Create Customer Contract Order"]
        n7["fa:fa-user Derive MMID using CPN"]
        n8["fa:fa-user Create Call-off Order"]
        n9[["fa:fa-cog Determine Order Type"]]
        n10[["fa:fa-cog Create Customer Contract Order"]]
        n11[["fa:fa-cog Validate Order"]]
        n12[["fa:fa-cog Capture Customer Contract Details"]]
        n13[["fa:fa-cog Determine Order Type"]]
        n14[["fa:fa-cog Calculate Pricing"]]
        n15[["fa:fa-cog Derive MMID using CPN"]]
        n16(["fa:fa-play Customer Contract Received Manually"])
        n17(["fa:fa-play Customer Contract Details Received Electronically via EDI"])
        n18["Process Order"]
        n19{{"fa:fa-code-branch Any Exceptions?"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n4
    n4 --> n20
    n10 --> n11
    n6 --> n1
    n5 --> n9
    n9 --> n6
    n12 --> n13
    n13 --> n10
    n16 --> n5
    n7 --> n2
    n8 --> n18
    n20 --> n8
    n21 --> n19
    n15 --> n14
    n1 --> n7
    n11 --> n15
    n2 --> n21
    n14 --> n21
    n17 --> n12
    n19 -->|"Yes"| n20
    n19 -->|"No"| n3
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
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 serviceTask
    class n16 startEvt
    class n17 startEvt
    class n18 startEvt
    class n19 gateway
    class n20 gateway
    class n21 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2P4jYU_StWRiNaKUhxPkjIQysIpBqpsx11pltVSx-M44A1JkF2wkBZ_ntt4gAJibar8jCae3zPuR_xtX00cJ4QIzQeH480o0UIjoNiTTZkEILBEgkyMEEFfEacoiUjYqB80jwrXuk_ZzfobvfKTWEx2lB2UOgrWeUE_PFkgokkMhMIlImhIJymA3Ow5XSD-CHKWc6V9wMJUis9R9NL05wnhF8dLMuH2JNURjNyhR3f9d1Y8QTBeZY0RFMvDVI8OKnkWP6B14gX5_RLQZ7R_k-aFGtpp4gJIn3WxYb9ipaEqRoLXioMl3xXN4MKFSeTDXvdIkyzlcRdS0IcZe9XyLNOJ3B6fFxkl6DgbbbIgPxhhoSYkRSIQsLzXQFSylj44EaT2LNMUfD8nYQP9tyfObaJVSWhLN0yVXOHH4Su1kW4zFmiXYcfqobQ3u5Nvg9ty-QH-bcVi2TJNVI0sgM7uESa-jCCUR0pTdP_FUn2lb8h8a5jzZ3YjmeXWNAbeZF1r1eXOXP9CWz3ifAdxeRGNI5jZ35t1XzkQatfdBo7Iytqia5QQT7Q4So4jtyLYOz5MfR7Bat47SzL5QvPcS3ozL3Yuwj6UxhP7F5BdwLdQGcodVYcbdcgKkWRbwgH01LI_S4EmGSIHURR-alfBr8sjBSFKRqqtoPPiNFEFgZ-U4OzMP6-cbWbrhFiuGTK94VTtWub3k7TO6Z7MN9jsi1onjU93ZbuGmUrck0-kluJI1w0SV47mW1R8g4WmJECUSaa7FGLzYmq457c0QW_SZ3Js2hHwPPz0wyoLq9A9PKpyQi6gyHGhnmadsUYf7lQcL5SJRC-kV-w8gVvhy2RhFsGtJqUb1bUIMMm-W4TNJztVqT_0PkG3_n-4tx2yPud1_D32iG6v1GDM_rhwtkyOdb39fxOMJE6CXhGWSm_3kFK_Hgr4X9TQrfkKjVnBMuRzihWgmBHEZjPntrCagepo0GNcMd2gePj8VpvQoZLeZfgtZz2w3XmxM8L43S6HWerm0X2mMku7cgv1QHXpsHvpcmbo_onc8Bw-JMceG26lVlfAHITVwDU53c20rY2vcoca3NcmaOabWtvpwZ0OHjR13qetn0dX5uBdg-0bet0LjbUDnUCUCcE64K0g1-bNaEOqDO064Kg2wZ0SrDOCZ6L_Low_iJykL7eNqte-ZSfF5yb20RlUt-iDdjuhp1u2O2GvW541A373XDQDY9v7-pmRVb_EuxfsvuXnP4lt3_J618aXR5kTdzvwYMefFy_LZrfzuqGYQ0bpiEPmw2iiREejfN7W77JE5KikhXGyTRQWeSvhwwb4fldapRbdcrPKJLPhU0Fnv4FOYat1w==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 O-020-140_Create_No-charge_Order_(IF) — O-020-140_Create_No-charge_Order_(IF)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 7 | **Gateways**: 2

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Confirm FOC Order"]
        n2["fa:fa-user Validate Order"]
        n3["fa:fa-user Derive MMID using CPN"]
        n4["fa:fa-user Determine Order Type"]
        n5["fa:fa-user Create Order"]
        n6[["fa:fa-cog Check GTS"]]
        n7[["fa:fa-cog Check Inventory Availability"]]
        n8(["fa:fa-play Order Details Received"])
        n9["Process Delivery"]
        n10["Order Acknowledgement"]
        n11["Order Confirmation"]
        n12{{"fa:fa-arrows-alt parallelGateway"}}
        n13{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n1 --> n13
    n2 --> n3
    n3 --> n6
    n5 --> n2
    n8 --> n4
    n7 --> n12
    n6 --> n7
    n12 --> n10
    n12 --> n1
    n13 --> n9
    n13 --> n11
    n4 --> n5
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 startEvt
    class n9 startEvt
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2PokgU_SsVOh13Ekz4FJuHTRRk0sn0zmTtnX0Y56GEQisWVaSq0GaN_32rBFRYfdiMD8Z76pxzP4CLRyNlGTJC4_n5iCmWITiO5BYVaBSC0RoKNDJBA3yHHMM1QWKkOTmjcon_OdNsr_zQNI0lsMCk1ugSbRgCf72aYKaExAQCUjEWiON8ZI5KjgvI64gRxjX7CU1zKz9na4_mjGeIXwmWFdipr6QEU3SF3cALvETrBEoZzXqmuZ9P83R00sURdki3kMtz-ZVAb_Djb5zJrYpzSARSnK0syBe4RkT3KHmlsbTi-24YWOg8VA1sWcIU043CPUtBHNLdFfKt0wmcnp9X9JIUvMcrCtQnJVCIGOVASAUv9hLkmJDwyYtmiW-ZQnK2Q-GTswhi1zFT3UmoWrdMPdzxAeHNVoZrRrKWOj7oHkKn_DD5R-hYJq_V9yAXotk1UzRxps70kmke2JEddZnyPP-lTGqu_B2KXZtr4SZOEl9y2f7Ej6z_-nVtxl4ws4dzQnyPU3RjmiSJu7iOajHxbeux6TxxJ1Y0MN1AiQ6wvhq-RN7FMPGDxA4eGjb5hlVW62-cpZ2hu_AT_2IYzO1k5jw09Ga2N20rVD4bDsstiCohWYE4mFdC3e9CgBmFpBay4ekPtX-sjByGORzrsYOI0RzzAiRfI_BVPzsr4-cN2-mzv0OCMzWGe1S3T43VM7tH4O3tNQa6mg2Ivv3RV3hDhUS8UHU37uC9LlFf4A9q5-hBLZMfF2bKVOYtSnfg8_tSsW5pwT3aK90jKhmvwWwPMYFrTLCsB8rpbxdlSdQ90VSsOlAKAf5EKVLNZ0r06Ub0ojT6gusLEyOiGLzu121bitJ4zdIdZQeCso1ao1QOePaF115AKDGjA5JzPHZFQs7ZQYwhkaCEHBKCyOfmdl4Zp9OtyP1_IrUlmh_UBuPx79qgjZ0m7kK3CSdt6Deh04bTJvTaMGi9uuNJEwddqtbbtoZAF7fZXgax3RG8JvZvnkjdQbeJerBzH3bvw9592L8PT25XVe8keHgyvbwGevDLfdi2HuD2A9zpFl0fdjvYMA21YgqIMyM8Gue3vPonkKEcVkQaJ9OAlWTLmqZGeH4bGlWpV0aMoVpSRQOe_gVT0pYz" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 O-020-150_Create_Subsequent_Delivery_Free_of_Charge_(FOC)_Order_(IF) — O-020-150_Create_Subsequent_Delivery_Free_of_Charge_(FOC)_Order_(IF)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 8 | **Gateways**: 3

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Validate Order"]
        n2["fa:fa-user Determine Order Type"]
        n3["fa:fa-user Create Order"]
        n4["fa:fa-user Confirm Subsequent Delivery FOC Order"]
        n5["fa:fa-user Remove Delivery Block"]
        n6["fa:fa-user Reject Order"]
        n7[["fa:fa-cog Check GTS"]]
        n8[["fa:fa-cog Check Inventory Availability"]]
        n9(["fa:fa-play Return Order Referenced"])
        n10(["fa:fa-stop Order Rejected"])
        n11["Process Delivery"]
        n12["Order Acknowledgement"]
        n13["Order Confirmation"]
        n14{{"fa:fa-code-branch Order Approved?"}}
        n15{{"fa:fa-arrows-alt parallelGateway"}}
        n16{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n2 --> n3
    n3 --> n1
    n9 --> n2
    n4 --> n16
    n8 --> n15
    n1 --> n7
    n7 --> n8
    n6 --> n10
    n5 --> n11
    n14 -->|"Yes"| n5
    n14 -->|"No"| n6
    n15 --> n4
    n15 --> n12
    n16 --> n13
    n16 --> n14
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 startEvt
    class n10 endEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 gateway
    class n15 gateway
    class n16 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2P4jYU_StWRiNaCaR8EiYPrSCQ1UpttxqmW1VLH0xyAy7GTm0HhrL899okAZKFh6p5QNzjc8_9sH2To5XyDKzIen4-EkZUhI49tYYt9CLUW2IJvT6qgM9YELykIHuGk3Om5uSfM83xi3dDM1iCt4QeDDqHFQf028c-GmtH2kcSMzmQIEje6_cKQbZYHGJOuTDsJxjldn6OVi9NuMhAXAm2HTppoF0pYXCFvdAP_cT4SUg5y1qieZCP8rR3MslRvk_XWKhz-qWEn_H77yRTa23nmErQnLXa0p_wEqipUYnSYGkpdk0ziDRxmG7YvMApYSuN-7aGBGabKxTYpxM6PT8v2CUoepsuGNJPSrGUU8iRVBqe7RTKCaXRkx-Pk8DuSyX4BqIndxZOPbefmkoiXbrdN80d7IGs1ipacprV1MHe1BC5xXtfvEeu3RcH_duJBSy7RoqH7sgdXSJNQid24iZSnuf_K5Luq3jDclPHmnmJm0wvsZxgGMT2t3pNmVM_HDvdPoHYkRRuRJMk8WbXVs2GgWM_Fp0k3tCOO6IrrGCPD1fBl9i_CCZBmDjhQ8EqXjfLcvmr4Gkj6M2CJLgIhhMnGbsPBf2x44_qDLXOSuBijeJSKr4FgSal1OddSjRmmB6kqnjmYc6XhZXjKMcD03b0GVOS6cLQJ3NxFtafN1S3TZ2CArHVuhUXvR0KaDt4bYdYwANlv0PkLCdii-blUsLfJTClg1GyA3FAyaf4nkLQVniFLd_B1WtCebppewy7Hn9Bqu5Jh18uzJSvULyGdIM-vM0165Y2ukf7yHY6e64zGO8woXhJKFGHjufLdxfPguoD9QqqFKzu6ivkIIClkGmv7283zr666W0uLnxTx7dss8_mdJlT0LSlXadj9rcSGacbxvcUspWe2Ux1eN6FV28UVoSzDsk_Hq_tyGCw1OMtXddJjotC6P3JflxYp9OtV3D1wkLwvRxgqlCBBaYU6IfqxnWdhv_NSQ-y6g9z0WDwgz6mtelVZj082EtlurXp16vD2h7VdlDbTmWHtRlW5qg2hzW7vvMsqO0mmHOW_7qw_gC5sL5qQnfhF37Gm_BOreB3bKfJ12lCel3Av5k7Ju9m3rZg9z7s3Yf9-3BwHx7eh8PbOd1aGT1cebm8A9tF2fX7qo06D9juA9x7gPvN8G_DwX142MBW39LTeItJZkVH6_xBpD-aMshxSZV16lu4VHx-YKkVnT8crLIws3hKsJ7n2wo8_QtKB_JC" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 O-020-190_Create_Sample_Order_(IF) — O-020-190_Create_Sample_Order_(IF)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 1 | **Gateways**: 1

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
    subgraph Customer Business Analyst
        n1["fa:fa-user Create Order"]
        n2(["fa:fa-play Order Details Received"])
        n3["Proceed with Standard Order Process"]
        n4["Proceed with No-charge Order Process"]
        n5{{"fa:fa-code-branch Sample Order is chargeable?"}}
        n6[["fa:fa-folder-open Determine Order Type"]]
    end
    n6 --> n1
    n1 --> n5
    n5 -->|"No"| n4
    n5 -->|"Yes"| n3
    n2 --> n6
    class n1 userTask
    class n2 startEvt
    class n3 startEvt
    class n4 startEvt
    class n5 gateway
    class n6 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVNuO0zAQ_RUrq6ogJVKuTckDqE0bCQkWRBcQ2vLgJuPWWuci2-mFbv4du016g-WFPETxyZlzPKOZ2RtpmYERGb3enhZURmjflyvIoR-h_gIL6JvoCHzDnOIFA9HXHFIWckZ_HWiOX201TWMJzinbaXQGyxLQ1_cmGqlAZiKBC2EJ4JT0zX7FaY75Li5ZyTX7DobEJge39te45BnwM8G2QycNVCijBZxhL_RDP9FxAtKyyK5ESUCGJO03-nKs3KQrzOXh-rWAj3j7nWZypc4EMwGKs5I5-4AXwHSOktcaS2u-7opBhfYpVMFmFU5psVS4byuI4-LpDAV206Cm15sXJ1P0MJkXSD0pw0JMgCAhFTxdS0QoY9GdH4-SwDaF5OUTRHfuNJx4rpnqTCKVum3q4loboMuVjBYly1qqtdE5RG61Nfk2cm2T79T7xguK7OwUD9yhOzw5jUMnduLOiRDyX06qrvwBi6fWa-olbjI5eTnBIIjtP_W6NCd-OHJu6wR8TVO4EE2SxJueSzUdBI79sug48QZ2fCO6xBI2eHcWfBP7J8EkCBMnfFHw6Hd7y3rxmZdpJ-hNgyQ4CYZjJxm5Lwr6I8cftjdUOkuOqxWKayHLHDga10L1uxBoVGC2E_LI00_hPM4NgiOCLV12FHNQaaFPemzmxs8LovvqxKyYSvtAQROQmDKBvkAKdA2Zinl9EeSpGJ0TQIY2VK7QTGI9XlkbfvgnxLWTfxt0X1p6AJbwr6hgv-_up7eRtVDzlCpDnFesC6QCHYX0Dno3N5rmQmDweEqQqI4FbpUVFDpD4LkqX6vxsKtAObfWaiqOH8UAWdZbVc_26ByPQXsM9PF5btyXc-NZpXgD_wBxwL0Wd4_Rg4sO0ZLdZFzB7mkNXMHe32H_73DQtfMVOuh60jAN1Uc5ppkR7Y3DKlfrPgOCayaNxjRwLcvZrkiN6LDyjLrKlN6EYtWJ-RFsfgOFVvfb" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 O-020-200_Create_Prototype_Order_(IF) — O-020-200_Create_Prototype_Order_(IF)

**Swim Lanes**: Customer Business Analyst · Pricing Manager | **Tasks**: 14 | **Gateways**: 8

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
    subgraph Customer Business Analyst
        n1["Override Price"]
        n3["fa:fa-user Validate Order"]
        n4["fa:fa-user Derive MMID using CPN"]
        n5["fa:fa-user Determine Order Type"]
        n6["fa:fa-user Create Order"]
        n7["fa:fa-user Fix Exception / Release Hold"]
        n8["fa:fa-user Change Order"]
        n9[["fa:fa-cog Check GTS"]]
        n10[["fa:fa-cog Confirm Prototype Order"]]
        n11[["fa:fa-cog Perform FSCM Credit Check"]]
        n12[["fa:fa-cog Check Inventory Availability"]]
        n13[["fa:fa-cog Check Inventory Availability"]]
        n14[["fa:fa-cog Calculate Pricing"]]
        n15(["fa:fa-play Order Details Received"])
        n16(["fa:fa-play Price Override Required"])
        n17["Process Order"]
        n18["Order Confirmation"]
        n19["Order Acknowledgement"]
        n20{{"fa:fa-code-branch Any Exceptions?"}}
        n21{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-code-branch exclusiveGateway"}}
        n23{{"fa:fa-code-branch Customer Credit Check Passed?"}}
        n24{{"fa:fa-code-branch exclusiveGateway"}}
        n26{{"fa:fa-arrows-alt parallelGateway"}}
        n27{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Pricing Manager
        n2["Approve Overridden Price"]
        n25{{"fa:fa-code-branch Overridden Price Approved?"}}
    end
    n3 --> n4
    n4 --> n9
    n5 --> n6
    n6 --> n3
    n15 --> n5
    n21 --> n7
    n7 --> n8
    n8 --> n22
    n20 -->|"No"| n22
    n26 --> n17
    n26 --> n18
    n16 --> n1
    n1 --> n2
    n20 -->|"Yes"| n21
    n25 -->|"Yes"| n24
    n23 -->|"Yes"| n12
    n11 --> n23
    n13 --> n21
    n24 --> n11
    n2 --> n25
    n9 --> n14
    n14 --> n24
    n27 --> n10
    n27 --> n19
    n10 --> n20
    n22 --> n26
    n12 --> n27
    n25 -->|"No (Hold)"| n21
    n23 -->|"No (Hold)"| n13
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 serviceTask
    class n10 serviceTask
    class n11 serviceTask
    class n12 serviceTask
    class n13 serviceTask
    class n14 serviceTask
    class n15 startEvt
    class n16 startEvt
    class n17 startEvt
    class n18 startEvt
    class n19 startEvt
    class n20 gateway
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1uP4jYU_itWViN2JVDjXCEPrZhAtiN1ZkfLdKtq6YNJHLDGxNQxt7L899rECSSTPHTKA9L5zved43OJCScjZgk2AuPu7kQyIgJw6okVXuNeAHoLlONeHxTAN8QJWlCc9xQnZZmYkX8uNOhsDoqmsAitCT0qdIaXDIPfH_pgLIW0D3KU5YMcc5L2-r0NJ2vEjyGjjCv2BzxMzfSSTbvuGU8wvxJM04exK6WUZPgK277jO5HS5ThmWVILmrrpMI17Z3U4yvbxCnFxOf42x4_o8AdJxEraKaI5lpyVWNPf0AJTVaPgW4XFW74rm0FylSeTDZttUEyypcQdU0IcZa9XyDXPZ3C-u5tnVVLwMplnQH5iivJ8glOQCwlPdwKkhNLggxOOI9fs54KzVxx8sKb-xLb6saokkKWbfdXcwR6T5UoEC0YTTR3sVQ2BtTn0-SGwzD4_yu9GLpwl10yhZw2tYZXp3ochDMtMaZr-r0yyr_wF5a8619SOrGhS5YKu54bm23hlmRPHH8NmnzDfkRjfBI2iyJ5eWzX1XGh2B72PbM8MG0GXSOA9Ol4DjkKnChi5fgT9zoBFvuYpt4tnzuIyoD11I7cK6N_DaGx1BnTG0BnqE8o4S442KxBuc8HWmIP7bS73Pc_BOEP0mIuCpz4Z_D43vuww5yTB4JnLLs2Nv278tvSnKEjRQI0FfEOUJLJw8EU9WHWqU6dO5FO6w-Dx8WECVP4lCJ-f6gq3qRCYr-VJi-jg5bhpnMarC0KOO87i14kROYDpIcYbQVgGfgJfMcXyXgK_ytWsC4eNDCuULVszjL5XzJjJ2lY4fgWfX2aSdUuDZoPHspTwtWw1E0zIAqvYNRWsq54xT5lURbPwUVWdEFFkbOqstlM9ZDucCcaPYLxDhKIFoUQcm1L7_VKnIUU03lI1GbVQcvJNvvux4m-ofISKccvxyxS5HE6M5eaowXy6VXkN1WVbQbW8X_HfW8LfytQqqOdK7X_LHKGaeHEAPRuklqRBGlWkcfyasT3FyVL-nmWizrPM0-naiQQPFvJWj1fyuTte9y__ZW6cz7cq2K7Ch5jKJ2eHPxdXTVNmvU9mt8uq2-J2v8CzvJxw8ubEzvtSe1cZ4pzt8wGiAmwQR5Ri2iHy_5tI_lA17kG9heARZWgp538TW451vNlwtqsWKcFZ2z1oue0VN1VAh7ttWXWizAaDwc_yptSmU5gjbbqF6WnTK0xbm1C7XW1bsLB9bfuFOdTmsDAtq6SbCvgxN57Y3Phx69B5oN8EylCwBEpbh25G_hPnReiSaLlNT1m5ZTc8sIwGy-hV3bpp16i6bbACNKHszEj7y2RQC67Zda-g2QTKUUBTSypGmaScDiwBv1nsEwMf1Q_Lp0Yz7FY_tG9eA9SGlK8_Ndhph9122GuH_XZ42A6Pbl-bah7ZnE4X7HZZ3S672-V0u9zqBbiOex2434EPO_BROy73Xb_71WHYDlvtsN0OO-2w2w577bBfwkbfkDf6GpHECE7G5S-Y_JuW4BRtqTDOfQNtBZsds9gILn9VjO1Gvd1NCJI357oAz_8CA6lJew==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Customer Business Analyst | O-020-110_Create_Service_Contract_Order_(IF), O-020-120_Create_Customer_Contract_Order_(IF), O-020-140_Create_No-charge_Order_(IF), O-020-150_Create_Subsequent_Delivery_Free_of_Charge_(FOC)_Order_(IF), O-020-190_Create_Sample_Order_(IF), O-020-200_Create_Prototype_Order_(IF) | |
| Pricing Manager | O-020-200_Create_Prototype_Order_(IF) | |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for O-020. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.

### 4.3 Data Lineage

Data lineage traces the origin and transformation path of key data objects across integrated systems.

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|

> *Lineage detail will be refined when tower architects validate source/target schema object mappings.*

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| O-020-R001 | Report | Capture Orders (IF) operational report | Planned | SAP S/4HANA | Analytics | Medium |
| O-020-C001 | Conversion | Legacy data migration for Capture Orders (IF) | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for O-020.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for O-020.

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

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| OTCW0638 | Workflow | Dispute Write-off Workflow | 10. Object Complete |  | NA | 03.Medium |
| OTCI1162 | Interface | Inbound interface to change the sales order via Build Instructions | 10. Object Complete |  | MULESOFT | 03.Medium |
| OTCI1161 | Interface | Inbound interface from BY-PDH to S4 to update CMAD in IF sales orders | 10. Object Complete | BY → S/4 | BODS | 03.Medium |
| OTCI1126 | Interface | Inbound interface to create and change sales order via Subcon, STO & SIMS PO | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI0442 | Interface | IF: Interface requirement from SAC to S4 | 10. Object Complete | SAC → S/4 | BODS | 03.Medium |
| OTCF0681_IF | Form | Form development for Intercompany Invoice. | 10. Object Complete |  | NA | 03.Medium |
| OTCF0460_IF | Form | Form Development for Invoice list. | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCF0431 | Form | Generate Custom Late Payment Interest Charge Output Form | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCF0290 | Form | Dunning output form customization | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE1698 | Enhancement | Additional material attributes for transfer from MDG to GTS to support produc... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE1668_IF | Enhancement | Enhancement to transfer Customs value from S4 to GTS for Sales orders and del... | 10. Object Complete |  | NA | 04.Low |
| OTCE1662 | Enhancement | BADI Enhancement for Dispute Write off (workflow Trigger) | 10. Object Complete |  | NA | 03.Medium |
| OTCE1658 | Enhancement | Dispute Write-off Enhancement | 10. Object Complete |  | NA | 04.Low |
| OTCE1655 | Enhancement | Enhancement to AIF capabilities on access and notifications | 10. Object Complete |  | NA | 03.Medium |
| OTCE1625 | Enhancement | Credit hold release dashboard at line-item level | 10. Object Complete | NA → NA | NA | 01.Very High |
| OTCE1558 | Enhancement | Business users want the capability to have CMIR updated for the specific Mate... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1557 | Enhancement | Business users want the capability to have sales order updated for the specif... | 10. Object Complete |  | NA | 02.High |
| OTCE1200 | Enhancement | Enhancement to transfer fields from Sales Orders to Purchase Requisition duri... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1124 | Enhancement | Enhancement to support Inbound interface to change the ship to party record a... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1123 | Enhancement | Determine Confirmed Delivery date in sales orders at schedule line level base... | 06. Dev In Progress |  | NA | 02.High |
| OTCE1122 | Enhancement | Enhancement for IMR to update the Repair Sales Order post Repair work order i... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1106 | Enhancement | Enhancement to support Inbound interface and manual upload to create the sale... | 10. Object Complete |  | NA | 02.High |
| OTCE1013 | Enhancement | SIMS Enhancement to determine the order type based on the Material Characteri... | 10. Object Complete |  | NA | 04.Low |
| OTCE0974 | Enhancement | Screen enhancement to populate the assignment priority at SO line item | 10. Object Complete |  | NA | 04.Low |
| OTCE0659 | Enhancement | IF : Apply a Delivery Block Hold for Items with Multiple Schedule lines (MSL)... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0651_IF | Enhancement | Enrich the delivery data transfer data from S/4 IF to GTS with the 'new' vs '... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0614_IF | Enhancement | Implement Standard Credit/Collection BADI | 10. Object Complete |  | NA | 04.Low |
| OTCE0486 | Enhancement | Price Swamp: For Order Repricing | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0235 | Enhancement | Credit and Collections - Credit Check Step Configuration | 10. Object Complete | NA → NA | NA | 04.Low |
| OTCE0234 | Enhancement | Implement mapping between customer’s risk class and credit check steps | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGI1688 | Interface | To capture correct Country of Assembly and Country of Fabrication on FVR and ... | 10. Object Complete |  | MuleSoft | 03.Medium |
| LOGI1534_IF | Interface | BRF+ Extractor( API interface) to fetch the data saved in the BRF+ decision t... | 10. Object Complete |  | NA | 04.Low |
| LOGI0871 | Interface | Interface for Label printing, So in this interface when user will click on pr... | 10. Object Complete | SPECTRUM → S/4 | NA | 02.High |
| LOGI0842_IF | Interface | Interface from SAP S4 to DBaaS to Fetch Actual COF for FVR batch and COA for ... | 10. Object Complete | S/4 → DBaaS | MULESOFT | 04.Low |
| LOGI0800_IF | Interface | Interface to send shipment information to custom broker | 10. Object Complete | S/4 → OpenText | MULESOFT | 04.Low |
| LOGI0663_IF | Interface | Trigger ZCUS (export customs clearance output) and ZXCI to send outputs - ZSI... | 10. Object Complete |  | MULESOFT | 03.Medium |
| LOGI0630_IF | Interface | TM - GTT: GXS sending carrier events back to GTT app “Shipment Tracking”. IF. | 10. Object Complete |  | NA | 04.Low |
| LOGF1673 | Form | Consolidated Export CI for Wafer Die (Ireland) | 10. Object Complete |  | NA | 03.Medium |
| LOGF1672 | Form | Consolidated Export CI for Finished Goods (Ireland) | 10. Object Complete |  | NA | 03.Medium |
| LOGF1149_IF | Form | Consolidated Packing list for Chengdu | 10. Object Complete |  | NA | 03.Medium |
| LOGF0873 | Form | CI/PL document should be printed based on R3 process. | 10. Object Complete |  | NA | 02.High |
| LOGF0356 | Form | Generate Consolidated Bailment Commercial Invoice - Finished Goods (IF and IP) | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0355 | Form | Generate Consolidated Bailment Commercial Invoice - Wafer/Die (IF and IP) | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0349_IF | Form | ISM - Generate Packing List - IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE1624 | Enhancement | Development of LCSR tool in Fiori | 10. Object Complete |  | NA | 01.Very High |
| LOGE1509_IF | Enhancement | Tendering- FIORI app for Approval Hierarchy (Assign Delegate) | 10. Object Complete |  | NA | 03.Medium |
| LOGE1488_IF | Enhancement | Invoice notification- Notification to carrier for POD and internal notificati... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1487_IF | Enhancement | Carrier notification- Carrier contact table BRF+ maintenance | 10. Object Complete |  | NA | 03.Medium |
| LOGE1486_IF | Enhancement | Carrier notification- Cancellation email | 10. Object Complete |  | NA | 03.Medium |
| LOGE1485_IF | Enhancement | Carrier notification- Acceptance and Rejection email | 10. Object Complete |  | NA | 03.Medium |
| LOGE1484_IF | Enhancement | Invoice notification- Notification to carrier for Invoice | 10. Object Complete |  | NA | 03.Medium |
| LOGE1483_IF | Enhancement | Invoice notification- Notification to carrier for dispute | 10. Object Complete |  | NA | 03.Medium |
| LOGE1482_IF | Enhancement | Tendering- Internal Notification mail | 10. Object Complete |  | NA | 04.Low |
| LOGE1481_IF | Enhancement | Tendering- Approval Process with Purchase group determination | 10. Object Complete |  | NA | 04.Low |
| LOGE1462_IF | Enhancement | TM - GTT: Send Event # Estimated Time of Arrival (ETA) as a separate event fr... | 10. Object Complete |  | NA | 04.Low |
| LOGE1461_IF | Enhancement | TM - GTT: To propagate events to S/4 TM Freight order reported by GXS by Bypa... | 10. Object Complete |  | NA | 04.Low |
| LOGE1460_IF | Enhancement | TM - GTT: Additional field needs to be captured in S/4 TM Freight Order “Note... | 10. Object Complete |  | NA | 04.Low |
| LOGE1459_IF | Enhancement | TM - GTT: Additional field values sent by carrier through GXS are required in... | 10. Object Complete |  | NA | 04.Low |
| LOGE1297_IF | Enhancement | Disable the Amount field within Subcontracting tab in Freight Order for CW Lo... | 10. Object Complete |  | NA | 04.Low |
| LOGE1256_IF | Enhancement | TM - GTT: Document type T54 (House Airway Bill) number to GTT | 10. Object Complete |  | NA | 04.Low |
| LOGE1251_IF | Enhancement | More determinization of input entry criteria to be added for dedicated carrie... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1250_IF | Enhancement | Creating new Carrier selection strategy methods ZPRE_TAL and ZPOST_TAL to cal... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1197_IF | Enhancement | Carrier notification- Tendering initiation email | 10. Object Complete |  | NA | 03.Medium |
| LOGE1196_IF | Enhancement | Invoice notification- Notification to carrier for POD and internal notificati... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0841 | Enhancement | Enhancement to display an error message in the pack transaction within SAP Ex... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0797_IF | Enhancement | Pre alert notification to Customer | 10. Object Complete |  | NA | 04.Low |
| LOGE0796_IF | Enhancement | Custom transaction to trigger CUSDEC | 10. Object Complete |  | NA | 03.Medium |
| LOGE0792_IF | Enhancement | Enhancement to Update Custom Table form Master data and Manage SOP Data Commu... | 10. Object Complete |  | NA | 04.Low |
| LOGE0791_IF | Enhancement | Creation of Proforma Invoice ZF8 from Freight Order and Save ITN Number in De... | 10. Object Complete |  | NA | 04.Low |
| LOGE0782 | Enhancement | Enhancement to RF Loading Screen for 3PV Validation | 10. Object Complete |  | NA | 02.High |
| LOGE0775 | Enhancement | Enhancement in packing transaction. Should allow user to launch Interface for... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0772_IF | Enhancement | Develop Fiori app to View/Edit/Add SOP data(CMDB). | 10. Object Complete |  | NA | 03.Medium |
| LOGE0766_IF | Enhancement | TM - GTT: Routing of events from GTT to correct S4 system | 10. Object Complete |  | NA | 04.Low |
| LOGE0765_IF | Enhancement | Calling a new BRF+ for Carrier exclusion during Carrier Selection process. Eg... | 10. Object Complete |  | NA | 04.Low |
| LOGE0673_IF | Enhancement | Data code extractor to be extended on S4 TM side​ | 10. Object Complete |  | NA | 04.Low |
| LOGE0632_IF | Enhancement | TM: Custom Determination Class to access Source and Destination country in FU... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0628_IF | Enhancement | CRF freight orders, should have a custom event type “Shipped –CRF". This cust... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0626_IF | Enhancement | FO subcontracting screen for tendering enhancement. Fields include- send for ... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0625_IF | Enhancement | Tendering- FIORI app for Approval Hierarchy (Assign Delegate) | 10. Object Complete |  | NA | 03.Medium |
| LOGE0547_IF | Enhancement | Mass upload – Custom TM program for below items. Resource Downtime upload.Not... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0546_IF | Enhancement | Mass upload – Custom TM program for below items. Schedule and Default Routes ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0511_IF | Enhancement | Mass upload – Custom TM program for below items. Mass upload program to creat... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0478_IF | Enhancement | Generate Automated Carrier Pre-Alert (ZPRC) from SAP TM. | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0459_IF | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0458_IF | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0457_IF | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0456_IF | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection UI enhanceme... | 10. Object Complete | NA → NA | NA | 04.Low |

**Summary**: 11 Interfaces, 64 Enhancements, 11 Forms, 1 Workflows

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for O-020:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for O-020:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (87 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 86 | 98.9% |
| 06. Dev In Progress | 1 | 1.1% |
| **Total** | **87** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Interface (I) | 11 |
| Enhancement (E) | 64 |
| Form (F) | 11 |
| Workflow (W) | 1 |
| **Total** | **87** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 2 |
| 02.High | 8 |
| 03.Medium | 48 |
| 04.Low | 29 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| OTCE1123 | 04.Enhancement | Determine Confirmed Delivery date in sales orders at schedule line level based o... | 06. Dev In Progress | 02.High |

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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>O-020 — Capture Orders (IF)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*87 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| OTCW0638 | Dispute Write-off Workflow | Aug-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 2. At Risk |
| OTCI1162 | Inbound interface to change the sales order via Build Instructions | Mar-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Mar-26 (100%) | 2. At Risk |
| OTCI1161 | Inbound interface from BY-PDH to S4 to update CMAD in IF sales orders | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 1. On Track |
| OTCI1126 | Inbound interface to create and change sales order via Subcon, STO & SIMS PO | Apr-25 (100%) | Jul-25 (100%) | Jul-25 (100%) | Jan-26 (100%) | 4. Completed |
| OTCI0442 | IF: Interface requirement from SAC to S4 | Sep-24 (100%) | Mar-25 (100%) | Mar-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCF0681_IF | Form development for Intercompany Invoice. | Nov-24 (100%) | Mar-25 (100%) | Mar-25 (100%) | Jul-25 (100%) |  |
| OTCF0460_IF | Form Development for Invoice list. | Sep-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Jan-25 (100%) |  |
| OTCF0431 | Generate Custom Late Payment Interest Charge Output Form | Aug-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | May-25 (100%) |  |
| OTCF0290 | Dunning output form customization | Jul-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Mar-25 (100%) |  |
| OTCE1698 | Additional material attributes for transfer from MDG to GTS to support product classification | Nov-24 (100%) | Mar-25 (100%) | Mar-25 (100%) | Dec-25 (100%) |  |
| OTCE1668_IF | Enhancement to transfer Customs value from S4 to GTS for Sales orders and delivery documents | Jan-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 1. On Track |
| OTCE1662 | BADI Enhancement for Dispute Write off (workflow Trigger) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 2. At Risk |
| OTCE1658 | Dispute Write-off Enhancement | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 2. At Risk |
| OTCE1655 | Enhancement to AIF capabilities on access and notifications | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Jan-26 (100%) | 1. On Track |
| OTCE1625 | Credit hold release dashboard at line-item level | Jul-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Feb-26 (100%) | 1. On Track |
| OTCE1558 | Business users want the capability to have CMIR updated for the specific Materials which will go under FERT To HALB Conversion during R3 Cutover, this activity will be specific for IF system, CMIR to be deleted automatically for materials which will undergo FERT to HALB Conversion and new records to be created for new Material code | Oct-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCE1557 | Business users want the capability to have sales order updated for the specific Materials which will go under FERT To HALB Conversion during R3 Cutover, this activity will be specific for IF system, orders to be updated automatically. | Oct-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | Jan-26 (100%) | 4. Completed |
| OTCE1200 | Enhancement to transfer fields from Sales Orders to Purchase Requisition during Sales Order creation and change. | Jul-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCE1124 | Enhancement to support Inbound interface to change the ship to party record at the sales order | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Jan-26 (100%) | 3. Off Track |
| OTCE1123 | Determine Confirmed Delivery date in sales orders at schedule line level based on CMAD received from Blue yonder | Jun-25 (100%) | Nov-25 (60%) | Nov-25 (60%) | Nov-25 (100%) | 4. Completed |
| OTCE1122 | Enhancement for IMR to update the Repair Sales Order post Repair work order is complete | Mar-25 (100%) | Apr-25 (100%) | Apr-25 (100%) | Jun-25 (100%) | 4. Completed |
| OTCE1106 | Enhancement to support Inbound interface and manual upload to create the sales order via Build Instructions | Jun-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCE1013 | SIMS Enhancement to determine the order type based on the Material Characteristic | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Oct-25 (100%) | 1. On Track |
| OTCE0974 | Screen enhancement to populate the assignment priority at SO line item | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Sep-25 (100%) |  |
| OTCE0659 | IF : Apply a Delivery Block Hold for Items with Multiple Schedule lines (MSL) which have price differences identified | Jan-25 (100%) | Mar-25 (100%) | Mar-25 (100%) | Mar-25 (100%) |  |
| OTCE0651_IF | Enrich the delivery data transfer data from S/4 IF to GTS with the 'new' vs 'used indicator | Jul-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCE0614_IF | Implement Standard Credit/Collection BADI | Mar-25 (100%) | Aug-25 (100%) | Apr-25 (100%) | Sep-25 (100%) |  |
| OTCE0486 | Price Swamp: For Order Repricing | Sep-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |
| OTCE0235 | Credit and Collections - Credit Check Step Configuration | Jul-24 (100%) | Jan-25 (100%) | Jan-25 (100%) | Jun-25 (100%) |  |
| OTCE0234 | Implement mapping between customer’s risk class and credit check steps | Jul-24 (100%) | Dec-24 (100%) | Dec-24 (100%) | Feb-25 (100%) |  |

*... and 57 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**Mapped sub-tower(s):** 4.10 OTC IF - Logistics Management Outbound, 4.11 OTC IF - Order Management, 4.12 OTC IF - TM, 4.3 OTC IF - Billing and Rebates, 4.6 OTC IF - Credit and Collections, 4.8 OTC IF - EWM, 4.9 OTC IF - GTS, 7.6 FTS IF - Logistics & Inventory Management

**RAID Summary:** 14 open items (1 capability-specific, 13 tower-level), 175 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 1 | 1 |
| P2 - Medium | 0 | 10 | 10 |
| P3 - Low | 1 | 2 | 3 |
| **Total** | **1** | **13** | **14** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03381 | Risk | P3 - Low | New requirement raised for enabling Israel as virtual site | Not Started | OTC IF | 2026-03-31 |

**Other OTC-IF Tower RAID Items** (13 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03592 | Risk | P2 - Medium | Lack of Defined IMO Owner for CBA Mask Billing and Materials... | In Progress | E2E | 2026-03-27 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03628 | Risk | P2 - Medium | R3 Returns Rework Process Causing Finance Double Counting in... | In Progress | E2E | 2026-03-27 |
| 03634 | Risk | P2 - Medium | Gaps in mapping of ITC test cases to automated controls and ... | Not Started | OTC IF | 2026-03-27 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03749 | Action | P2 - Medium | Logistics Data Intake and Creation Process Definition | In Progress | Test Management | 2026-03-27 |
| 03756 | Risk | P2 - Medium | LE101-1001 Operation Support Ownership for SIMS/Tester Front... | In Progress | E2E | 2026-04-24 |
| 03758 | Action | P2 - Medium | IMR Repair Order Creation Ownership | In Progress | PTP |  |
| 03763 | Risk | P2 - Medium | IP to IF Regression Testing for LE Merge | Not Started | B-Apps | 2026-03-26 |
| 03315 | Risk | P3 - Low | BPMG – SCP L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-03-27 |
| 03317 | Risk | P3 - Low | BPMG – E2E L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-05-29 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*O-020 — Architecture Document (TOGAF BDAT) · Order To Cash (IF) · Generated: March 2026*

