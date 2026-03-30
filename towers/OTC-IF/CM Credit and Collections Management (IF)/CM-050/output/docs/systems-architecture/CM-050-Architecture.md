<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">CM-050 — Manage Customer Credit Exposure (IF)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Order To Cash (IF) (OTC-IF) Tower<br/>
  Capability CM-050 · CM Credit and Collections Management (IF)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **CM-050 Manage Customer Credit Exposure (IF)** within the IAO program. It includes 7 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Order To Cash (IF) (OTC-IF) |
| **Process Group** | CM Credit and Collections Management (IF) |
| **Capability** | CM-050 - Manage Customer Credit Exposure (IF) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 11 Interfaces, 64 Enhancements, 11 Forms, 1 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: "loose"` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Order To Cash (IF) |
| **L1 Process** | CM Credit and Collections Management (IF) |
| **L2 Capability** | CM-050 - Manage Customer Credit Exposure (IF) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Foundry Customer Order Digitization | Digitize end-to-end order capture, pricing, and fulfillment for Intel Foundry customers | IDM 2.0 Foundry Revenue | High |
| 2 | Global Trade Compliance Automation | Automate export/import compliance screening and customs declarations | Global Trade Operations | High |
| 3 | Revenue Recognition Accuracy | Ensure compliant revenue recognition aligned with ASC 606 through S/4 HANA billing | Finance & Compliance | Medium |
| 4 | CM-050 Process Migration | Migrate Manage Customer Credit Exposure (IF) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Order Management (Intel Foundry) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order-to-Cash Cycle Time | < 5 business days | End-to-end cycle from order capture to cash application | 8 business days (legacy) | OTC Process Owner |
| Trade Compliance Screening Rate | 100% | Orders screened for denied parties and export controls | 99.2% (current) | Global Trade Manager |
| Billing Accuracy | > 99.8% | Invoices generated without errors requiring credit/re-bill | 98.5% (current) | Billing Manager |
| CM-050 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **7 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for CM-050 Manage Customer Credit Exposure (IF).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | CM-050-010_Check_Credit_Rating_and_Limits_(IF) | CM-050-010_Check_Credit_Rating_and_Limits_(IF) | Customer Business Analyst | 8 | 4 |
| 2 | CM-050-030_Block_Delivery_(IF) | CM-050-030_Block_Delivery_(IF) | Credit Manager, Customer Business Analyst, System User | 6 | 4 |
| 3 | CM-050-040_Block_Order_(IF) | CM-050-040_Block_Order_(IF) | Credit Manager, Customer Business Analyst | 4 | 3 |
| 4 | CM-050-050_Resolve_Credit_Issues_(IF) | CM-050-050_Resolve_Credit_Issues_(IF) | Credit Manager | 2 | 2 |
| 5 | CM-050-060_Cancel_Order_(IF) | CM-050-060_Cancel_Order_(IF) | Credit Manager, Customer Business Analyst | 4 | 2 |
| 6 | CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF) | CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF) | Accounts Receivable Analyst, Credit Manager, Customer Business Analyst, Logistics Team | 13 | 0 |
| 7 | CM-050-090_Modify_Customer_Profile_(IF) | CM-050-090_Modify_Customer_Profile_(IF) | Credit Manager | 6 | 3 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 CM-050-010_Check_Credit_Rating_and_Limits_(IF) — CM-050-010_Check_Credit_Rating_and_Limits_(IF)

**Swim Lanes**: Customer Business Analyst | **Tasks**: 8 | **Gateways**: 4

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
        n1["Check Inventory Availability"]
        n2[["fa:fa-cog Process Order"]]
        n3[["fa:fa-cog Validate Order Including Credit and GTS Check"]]
        n4[["fa:fa-cog Check Rules"]]
        n5[["fa:fa-cog Check Credit Limit and Validity"]]
        n6[["fa:fa-cog 14 days Horizon Credit Check"]]
        n7[["fa:fa-cog Release Order Block"]]
        n8[["fa:fa-cog Schedule Background Job for Daily/Hourly Credit Check"]]
        n9(["fa:fa-stop Order Blocked Removed Successfully"])
        n10["Cancel Order (IF)"]
        n11["Block Order"]
        n12["Block Delivery (IF)"]
        n13["Create Standard Order"]
        n14{{"fa:fa-code-branch Credit Limit, Check Rules, and Validity Sufficient?"}}
        n15{{"fa:fa-arrows-alt parallelGateway"}}
        n16{{"fa:fa-arrows-alt parallelGateway"}}
        n17{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n13 --> n2
    n15 --> n4
    n15 --> n5
    n4 --> n16
    n5 --> n16
    n7 --> n9
    n16 --> n1
    n2 --> n3
    n1 --> n6
    n8 --> n7
    n6 --> n14
    n3 --> n15
    n14 -->|"Yes"| n8
    n14 -->|"No"| n17
    n17 --> n10
    n17 --> n11
    n17 --> n12
    class n2 serviceTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 serviceTask
    class n8 serviceTask
    class n9 endEvt
    class n10 startEvt
    class n11 startEvt
    class n12 startEvt
    class n13 startEvt
    class n14 gateway
    class n15 gateway
    class n16 gateway
    class n17 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2v4jYQ_StWrq7YlYIa54Nw89AKAtm9q-2HltutqqUPxnHAwsTITuBmWf57bZJAkiWV2vIAzJmZM2fsiZ2TgXlMjMB4fDzRlGYBOA2yDdmRQQAGKyTJwAQl8BkJilaMyIGOSXiaLejXSxh09686TGMR2lFWaHRB1pyA359NMFGJzAQSpXIoiaDJwBzsBd0hUYSccaGjH8g4sZJLtco15SIm4hZgWT7EnkplNCU32PFd3410niSYp3GLNPGScYIHZy2O8SPeIJFd5OeS_Ixe_6BxtlF2gpgkKmaT7dhHtCJM95iJXGM4F4d6MajUdVK1YIs9wjRdK9y1FCRQur1BnnU-g_Pj4zK9FgUvs2UK1AczJOWMJEBmCp4fMpBQxoIHN5xEnmXKTPAtCR7suT9zbBPrTgLVumXqxR0eCV1vsmDFWVyFDo-6h8Dev5riNbAtUxTqu1OLpPGtUjiyx_b4WmnqwxCGdaUkSf5XJbWu4gXJbVVr7kR2NLvWgt7IC63v-eo2Z64_gd11IuJAMWmQRlHkzG9LNR950OonnUbOyAo7pGuUkSMqboRPoXsljDw_gn4vYVmvqzJf_SY4rgmduRd5V0J_CqOJ3UvoTqA7rhQqnrVA-w0Ic5nxHRFgmks171KCSYpYIbMyTn9S-GVphBuCt-A5PZA046IAkwOiDK0oo1mxNP5qRNtfVHiCggQNMV8DLVfT_qqfMhXZDHXaoZ8Ro7FasTJWFcMsj9Wog1CQmGYApTF497IAFy0dKrdNVcr9lKtjpBPo3QusCnyku6rMRUrZWjN51E6GLohRIcF7LuhXntY09_T57cxPhBF16FWdThn_LmHcTljgDYlVO2CK8HYteK5EfuArkHABZmorih_e81yw4p80PL25UqpN3zeLk1hJ2vGD-l3kWG9YkjOm23_bHARLTwJKMWFV8pvn6G17-6GelgvndcubXvvqnRFGD0SN0h0OR9cRRM_CIkP6sI3vsrmn022RYjJcqQMSb1rbaTZnwWxtrmo1SSimaqR_Whrnc5PZuzEjIfhRDhHLwB4JxBhh78rnups0-i9J_r9LUmds-UetEhgOf1QPXG17pe12bK-y3dKEo8r2OrZf2k91-qjyV7Zdmk7tLs06eVyafmXWubWWSiqstcCLmG9L40_9gH5T-V3HL_yCw5oRVvKg1QVgF7Abh6bW3TjaWx6n1-P2erxez6jX4_d6xr2ep-oybYHQul7nbRz24HYP7vTgbn1jtWHvPjy6D_s1bJiGull2iMZGcDIuL3fqBTAmCcpZZpxNA-UZXxQpNoLLS5CR7_XxP6NI3U27Ejz_DU0hMeU=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 CM-050-030_Block_Delivery_(IF) — CM-050-030_Block_Delivery_(IF)

**Swim Lanes**: Credit Manager · Customer Business Analyst · System User | **Tasks**: 6 | **Gateways**: 4

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
    subgraph Credit Manager
        n3["fa:fa-user Create Credit Limit Request"]
        n5[["fa:fa-cog Credit Hold (Block Delivery)"]]
        n6[["fa:fa-cog Release Blocked Delivery"]]
        n9["Customer request received for credit limit enhancement"]
        n11{{"fa:fa-code-branch Credit Limit Exceeded?"}}
        n12{{"fa:fa-code-branch exclusiveGateway"}}
        n13{{"fa:fa-code-branch Credit Limit Request Approved?"}}
        n14[["fa:fa-folder-open Check Credit Rating and Limits"]]
    end
    subgraph Customer Business Analyst
        n1["fa:fa-user Create Delivery"]
        n2["fa:fa-user Billing to Customer"]
        n7(["fa:fa-play Sales Order Created"])
        n10{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph System User
        n4[["fa:fa-cog Create AR Open Item"]]
        n8(["fa:fa-stop Release to Account Receivables"])
    end
    n5 --> n9
    n6 --> n10
    n10 --> n2
    n11 -->|"Yes"| n12
    n12 --> n5
    n7 --> n14
    n14 --> n11
    n2 --> n4
    n9 --> n3
    n3 --> n13
    n13 -->|"Yes"| n6
    n13 -->|"No"| n12
    n11 -->|"No"| n1
    n1 --> n10
    n4 --> n8
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 serviceTask
    class n7 startEvt
    class n8 endEvt
    class n9 startEvt
    class n10 gateway
    class n11 gateway
    class n12 gateway
    class n13 gateway
    class n14 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVm2P4jYQ_itWTivupCDllbD50AoCaU_au6uWXqvq6AfjTCDa4KR2sgvl-O8dkzeSZaVWzYeAn5ln3jwe56SxLALN1-7uTglPCp-cRsUO9jDyyWhDJYx0UgG_UZHQTQpypHTijBer5O-LmunkB6WmsJDuk_So0BVsMyBfP-pkhsRUJ5JyOZYgknikj3KR7Kk4BlmaCaX9DqaxEV-81aJ5JiIQnYJheCZzkZomHDrY9hzPCRVPAst41DMau_E0ZqOzCi7NXtiOiuISfinhEz38nkTFDtcxTSWgzq7Ypw90A6nKsRClwlgpnptiJFL54ViwVU5ZwreIOwZCgvKnDnKN85mc7-7WvHVKHh7XnODDUirlAmIiC4SXzwWJkzT13znBLHQNXRYiewL_nbX0FralM5WJj6kbuiru-AWS7a7wN1ka1arjF5WDb-UHXRx8y9DFEd8DX8CjzlMwsabWtPU098zADBpPcRz_L09YV_ErlU-1r6UdWuGi9WW6EzcwXttr0lw43swc1gnEc8LgymgYhvayK9Vy4prG20bnoT0xgoHRLS3ghR47g_eB0xoMXS80vTcNVv6GUZabX0TGGoP20g3d1qA3N8OZ9aZBZ2Y60zpCtLMVNN-RQECUFOQT5XQLohKqh9vf1lpM_ZiOVa2VHubSqD8ke3w_wl8lyGKt_XnFc7-1RJZtG8LPuL_k_TzN2BNZQJo8gzh-QOI1c9JnPkIKOBfIhQRRSxuw7pEUlLLI9hilqCLCXwaoHJE4E4RVIaSXmIHvKGc4ZvggbtM8nTr3EYw3eNjYrp_x8sAAIoh-XGvn8zXZuk2GA0tLiZH8VDXCkGb_C591lcksz0X2fMO309UtxjKDGGc5cBLsAItdm3qkBc4MQnlUWZVdFfHQDnuiKeccY-cgJZlxmh5xp6-83myPqz260rX6unPsXRVMkbWe-vre-5aQp3h6VhRvA_JFjenaUYSED9fRGP-1_q-zXmGCsCdfZe8YOK_aWeU5eyRfVI0_ImPQj9MueMwtb9sYs50xlpVc7ajqzssd1-XRBsRdMh7_gI1dLyfV0qxHAf6pAKtZm2r9fa39ocx9V83YSKxK063XXm3JaeRODdSzkNf6jfy-Wtr10q61m7VpDxxPhoLP2SAgcyBo8EGKdVzTq-GnlJqh34Ot27B9G3au53xP4r4pmbwp8drbtQdP64uwB97f1sXdrC-JPmzehq3bsH0bdpr7QtM1PGV7mkSaf9Iun1n4KRZBTMu00M66RssiWx050_zL54hW5hEaXCQUz8a-As__AJkIE-0=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 CM-050-040_Block_Order_(IF) — CM-050-040_Block_Order_(IF)

**Swim Lanes**: Credit Manager · Customer Business Analyst | **Tasks**: 4 | **Gateways**: 3

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
    subgraph Credit Manager
        n1["fa:fa-user Credit Limit Request"]
        n2["fa:fa-user Release Order"]
        n4[["fa:fa-cog Schedule Background Job for Daily/Hourly Credit Check"]]
        n5(["fa:fa-stop Order Released Successfully"])
        n10{{"fa:fa-code-branch Credit Limit Request Approved?"}}
        n11{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph Customer Business Analyst
        n3[["fa:fa-cog Block Order"]]
        n6["Resolve Credit Issues (IF)"]
        n7["Customer request received for Credit Limit Enhancement"]
        n8["Check Credit Rating and Limits (IF)"]
        n9{{"fa:fa-code-branch Payment Received?"}}
    end
    n2 --> n5
    n7 --> n1
    n1 --> n11
    n3 --> n9
    n11 --> n10
    n4 --> n11
    n10 -->|"Yes"| n2
    n9 -->|"Yes"| n4
    n9 -->|"No"| n7
    n8 --> n3
    n10 -->|"No"| n6
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 endEvt
    class n6 startEvt
    class n7 startEvt
    class n8 startEvt
    class n9 gateway
    class n10 gateway
    class n11 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl2v4jYQ_StWrq7YlYKahIRAHrqCQNpb3W1X0A9VSx-MMyERxqZ2woWy_Pfa5AOScp-ah0g-PnPOzDhjOBuEx2AExvPzOWNZHqBzL09hB70A9dZYQs9EJfA7FhleU5A9zUk4y5fZP1ea7e6PmqaxCO8yetLoEjYc0G8vJpqoQGoiiZnsSxBZ0jN7e5HtsDiFnHKh2U8wSqzk6lZtTbmIQdwIluXbxFOhNGNwgwe-67uRjpNAOItboomXjBLSu-jkKH8jKRb5Nf1Cwmd8_COL81StE0wlKE6a7-grXgPVNeai0BgpxKFuRia1D1MNW-4xydhG4a6lIIHZ9gZ51uWCLs_PK9aYotfFiiH1EIqlnEGCZK7g-SFHSUZp8OSGk8izTJkLvoXgyZn7s4FjEl1JoEq3TN3c_htkmzQP1pzGFbX_pmsInP3RFMfAsUxxUu-OF7D45hQOnZEzapymvh3aYe2UJMn_clJ9Fb9iua285oPIiWaNl-0NvdD6r15d5sz1J3a3TyAOGYE70SiKBvNbq-ZDz7beF51Gg6EVdkQ3OIc3fLoJjkO3EYw8P7L9dwVLv26WxfqL4KQWHMy9yGsE_akdTZx3Bd2J7Y6qDJXORuB9ikIBcZajz5jhDYhyUz_M_royEhwkuK97XfNes516L-DvAmS-Mv66C3DaAQugoMYa_aKnq810vzZUwjdoSVKICwpoisl2I3jBYvQTX6OECzTDasq_-5EXgp7qHMIUyFYp3kt6HxpJmfN96VrnEKNlQQhImRSUnlTkx_s6rfP5lk0M_bUaMpI-LBhN9nvBDxB_WhmXy72I_VgEjoQWMjvAD-WHcAtTo9I9iUJlvlNZT1UEU9miCcP0pNp88xm0OzelnGybDt_3Y6h4C5CcHqCu5EVKVQP68BJ9bB-Hr7iNuagqFUBA5R1fT6HVizlLVW3qomadD2CkdfTZ1PwFztVFhbA6z2voI_Px48Z9wSdtoBpfpvHpQeeYg_r979XZV0u_XFaDzexqWa8H5Xpcb9f71Ygxt8O3LQ18Wxl_glwZ35RdtTHu4G4H_5lfYb-CR6XuoCtb0YZ3E66Trm-2Fuw8hgf3t1Zrx313x6tu6RY4bH4mWrD_GB49hsf1ddeuyHoM2zVsmIb68HY4i43gbFz_Aqi_CTEkuKC5cTENXOR8eWLECK4_lUaxj1XkLMNqbnYlePkXzCGnQg==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.4 CM-050-050_Resolve_Credit_Issues_(IF) — CM-050-050_Resolve_Credit_Issues_(IF)

**Swim Lanes**: Credit Manager | **Tasks**: 2 | **Gateways**: 2

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
    subgraph Credit Manager
        n1["fa:fa-user Review the Blocked Orders on Credit Release Dashboard"]
        n2["fa:fa-user Determine if any Exceptions can be made to Resolve Credit Issues"]
        n3(["fa:fa-stop Order Processed"])
        n4(["fa:fa-stop Monitor/Check Order Status"])
        n5["Block Order"]
        n6["Remove Block/Credit Hold (IF)"]
        n7{{"fa:fa-code-branch Credit Issue Resolution Required?"}}
        n8{{"fa:fa-code-branch exclusiveGateway"}}
        n9[["fa:fa-folder-open Modify Customer Profile (IF)"]]
        n10[["fa:fa-folder-open Remove Block/Credit Hold (IF)"]]
    end
    n1 --> n2
    n2 --> n7
    n5 --> n8
    n7 -->|"Yes"| n9
    n8 --> n1
    n6 --> n8
    n7 --> n4
    n9 --> n10
    n10 --> n3
    class n1 userTask
    class n2 userTask
    class n3 endEvt
    class n4 endEvt
    class n5 startEvt
    class n6 startEvt
    class n7 gateway
    class n8 gateway
    class n9 subProc
    class n10 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVd-P2jgQ_lesrFa0UlCTkBA2Dz1BIHcr3epOS3unU-mDScZgkdic7fDjKP97bZIA4Vj1oXlAzOeZb2a-eCYHK-UZWJH1-HigjKoIHTpqCQV0ItSZYwkdG1XAX1hQPM9BdowP4UxN6X8nN9df74ybwRJc0Hxv0CksOKDPzzYa6sDcRhIz2ZUgKOnYnbWgBRb7mOdcGO8HGBCHnLLVRyMuMhAXB8cJ3TTQoTllcIF7oR_6iYmTkHKWtUhJQAYk7RxNcTnfpkss1Kn8UsIL3v1NM7XUNsG5BO2zVEX-O55DbnpUojRYWopNIwaVJg_Tgk3XOKVsoXHf0ZDAbHWBAud4RMfHxxk7J0WfxjOG9JPmWMoxECSVhicbhQjN8-jBj4dJ4NhSCb6C6MGbhOOeZ6emk0i37thG3O4W6GKpojnPs9q1uzU9RN56Z4td5Dm22Ovfm1zAskumuO8NvME50yh0YzduMhFCfiqT1lV8wnJV55r0Ei8Zn3O5QT-Inf_zNW2O_XDo3uoEYkNTuCJNkqQ3uUg16Qeu8zbpKOn1nfiGdIEVbPH-QvgU-2fCJAgTN3yTsMp3W2U5_1PwtCHsTYIkOBOGIzcZem8S-kPXH9QVap6FwOsligVkVKEXzPACRHVoHuZ-mVkERwR3jdboFTYUtkhPKBrlPF1Bhv4wcyMRZw3JK-SgJxmNsVzOORbZzPp6xei1GcegQBR6xhAlCLM9muxSWCvKmUQpZmgOqMAZIMU1seT5Bpo8z1KWINvkvXdndqn4uioOGa1ASjCVvL_y9m-8X7heSVx8iJeQrurYqcKqlDeBgY479V85tWvo68NXKPim1uhDXe9v-nKjd8_J-7Z7eDg0RZjd2J3r6U6XrSarzksjiv77b0n12S8z63i8ohncp4FdmpeSbuDX6g7eRD19OStAdHkgunwNTAuRUbJHcallKSoB9VWDpvrr8l3nPsWPFKg59K6o_jAXdbsf9fWoTa8yw9oMKnNQm6Exv82sf8wF-Kb7qPFB5VZPNevfidKvvTafamenqcCpgN7VtJm6mi3Tgr37cK_efi3QvwcG553cgvv34bBZIi10cBd9avZDuw-ngS3b0i-1wDSzooN1-trqL3IGBJe5so62hUvFp3uWWtHpq2SV60ynGVOsl0VRgcfva8x4HA==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 CM-050-060_Cancel_Order_(IF) — CM-050-060_Cancel_Order_(IF)

**Swim Lanes**: Credit Manager · Customer Business Analyst | **Tasks**: 4 | **Gateways**: 2

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
    subgraph Credit Manager
        n2["fa:fa-user Resolve Credit Issues"]
        n3["fa:fa-user Check Credit Limit Availability"]
        n7(["fa:fa-stop Order Cancelled Successfully"])
    end
    subgraph Customer Business Analyst
        n1["fa:fa-user Cancel Order"]
        n4[["fa:fa-cog Block Order"]]
        n5(["fa:fa-stop Cancel Order Request Rejected"])
        n6(["fa:fa-stop Cancel Order Request Rejected"])
        n8["Check Credit Rating and Limits"]
        n9{{"fa:fa-code-branch Is Credit Limit exceeded?"}}
        n10{{"fa:fa-code-branch Credit Issues Resolved?"}}
    end
    n8 --> n9
    n4 --> n3
    n3 --> n2
    n2 --> n10
    n1 --> n7
    n9 -->|"Yes"| n4
    n9 -->|"No"| n5
    n10 -->|"Yes"| n6
    n10 -->|"No"| n1
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 serviceTask
    class n5 endEvt
    class n6 endEvt
    class n7 endEvt
    class n8 startEvt
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2v2jgQ_StWrq7oSkHKJ-HmYSsIRKrUdlel7WpV-mCcCbjXOKztcGEp_31tkkCS5T41D4nmeM6cmbE9OVmkyMCKrcfHE-VUxeg0UBvYwiBGgxWWMLBRBXzFguIVAzkwPnnB1YL-e3Fzg93BuBksxVvKjgZdwLoA9OWdjSaayGwkMZdDCYLmA3uwE3SLxTEpWCGM9wOMcye_qNVL00JkIG4OjhO5JNRURjncYD8KoiA1PAmk4FknaB7m45wMziY5VryQDRbqkn4p4QM-_EUztdF2jpkE7bNRW_Yer4CZGpUoDUZKsW-aQaXR4bphix0mlK81HjgaEpg_36DQOZ_R-fFxya-i6PNsyZF-CMNSziBHUml4vlcop4zFD0EySUPHlkoUzxA_ePNo5ns2MZXEunTHNs0dvgBdb1S8KlhWuw5fTA2xtzvY4hB7ji2O-t3TAp7dlJKRN_bGV6Vp5CZu0ijlef5LSrqv4jOWz7XW3E-9dHbVcsNRmDj_j9eUOQuiidvvE4g9JdAKmqapP7-1aj4KXef1oNPUHzlJL-gaK3jBx1vApyS4BkzDKHWjVwNWev0sy9WfoiBNQH8epuE1YDR104n3asBg4gbjOkMdZy3wboMSARlV6APmeA2iWjQP974trRzHOR6aXqNPIAu2h8b_nZQlyKX1vcXwu4xkA-S58X9Pt_o92WPK8Ioyqo5dbvTmSpaq2KE_zJ1ECeYEGIMMLUpCQMq8ZMwwf6uo-rz1yyk1faup01Lq6yslmnDMjlK1tNxenheRSrGbVPDt6kmKNZqyQhfU-LUdw1727ZC6c__oVin9_QFEQXZL_8Id_QJ3rKmdNn_CSo8GhHlWdby3Q0-n062gDIYrPU_IRm9md5vgQAAyyN4urfO53TjnPr9zJpqT0mZf94mP0XD4u06kNoPK9GvTr0yvNr3KdOtLwN3KjmrzyZg_l9bf5iD-1MF6-MfiAocN2-n5j_oLNaE9GYxoM2s6sHcf9u_DQXu8dFbCemh2wNE9MLoHjq_zvQM_NZOnW4rTwJZt6UuyxTSz4pN1-e3qX3MGOS6Zss62hUtVLI6cWPHl92SVu0wzZxTra7atwPN_HaV6og==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF) — CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF)

**Swim Lanes**: Accounts Receivable Analyst · Credit Manager · Customer Business Analyst · Logistics Team | **Tasks**: 13 | **Gateways**: 0

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
    subgraph Accounts Receivable Analyst
        n6["fa:fa-user A-050 Validate Payment Receipt"]
        n7["fa:fa-user A-100 Validate Payment Receipt"]
        n15(["fa:fa-stop Down Payment Process Completed"])
        n16[["fa:fa-folder-open Post Customer Payment"]]
        n17[["fa:fa-folder-open Receive Customer Down Payment"]]
        n18[["fa:fa-folder-open Receive Customer Down Payment"]]
    end
    subgraph Credit Manager
        n2["fa:fa-user A-060 Remove BUID Status Hold"]
        n3["fa:fa-user A-040 Remove Milestone Billing Plan Block"]
        n4["fa:fa-user A-090 Remove Milestone Billing Plan Block for Balance Value"]
        n5["fa:fa-user A-110 Remove Remaining Billing Plan Blocks and CRED Status Hold"]
    end
    subgraph Customer Business Analyst
        n1["fa:fa-user A-010 Create Sales Order with billing plan relevant Item Cat and add billing..."]
        n8[["fa:fa-cog A-020 Apply BUID and CRED Status Holds on the Line Item"]]
        n9[["fa:fa-cog A-070 Release Order Line-Item (to BY for ATP)"]]
        n10[["fa:fa-cog A-080 Issue Billing to Customer"]]
        n11[["fa:fa-cog A-030 Issue Billing to Customer"]]
        n12[["fa:fa-cog A-130 Create Invoice for Relevant Sales Order Items"]]
        n14(["fa:fa-play Create Standard Order"])
    end
    subgraph Logistics Team
        n13[["fa:fa-cog A-120 Create Delivery Note"]]
    end
    n1 --> n8
    n2 --> n9
    n16 --> n15
    n17 --> n6
    n6 --> n2
    n18 --> n7
    n7 --> n5
    n5 --> n13
    n13 --> n12
    n12 --> n16
    n14 --> n1
    n8 --> n3
    n3 --> n11
    n11 --> n17
    n9 --> n4
    n4 --> n10
    n10 --> n18
    class n1 userTask
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
    class n14 startEvt
    class n15 endEvt
    class n16 subProc
    class n17 subProc
    class n18 subProc
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVltv4jgU_itWqooZCapcCeRhJQhEi9TuVqUzq9V0H0ziQNRgR7YDZSv--x6TC5AEaVbDQ6vz-XzfufjE9qcWsohonnZ__5nQRHrosyc3ZEt6HuqtsCC9PiqA75gneJUS0VM-MaNymfx7cjPs7EO5KSzA2yQ9KHRJ1oygb4s-mgAx7SOBqRgIwpO41-9lPNlifvBZyrjyviOjWI9P0cqlKeMR4WcHXXeN0AFqmlByhi3Xdu1A8QQJGY2uRGMnHsVh76iSS9k-3GAuT-nngjzhj7-SSG7AjnEqCPhs5DZ9xCuSqholzxUW5nxXNSMRKg6Fhi0zHCZ0DbitA8QxfT9Djn48ouP9_Rutg6LHlzeK4BemWIgZiZGQAM93EsVJmnp3tj8JHL0vJGfvxLsz5-7MMvuhqsSD0vW-au5gT5L1Rnorlkal62CvavDM7KPPPzxT7_MD_G3EIjQ6R_KH5sgc1ZGmruEbfhUpjuNfigR95a9YvJex5lZgBrM6luEMHV9v61Vlzmx3YjT7RPguCcmFaBAE1vzcqvnQMfTbotPAGup-Q3SNJdnjw1lw7Nu1YOC4geHeFCziNbPMV8-chZWgNXcCpxZ0p0YwMW8K2hPDHpUZgs6a42yDJmHIcioFeiEhSXbqw0MTitODkIWn-tHhjzctxl6MB6rxaDLQHR19x2kSQYHoGR-2hMpCIpNv2j8XVLdJhaJ-kmo4X2qykCxDM7anNUX1gQiBfLbNUiJJBOSvl-zhj5odw3gRPmAZAT4TEvk5CG4hn1INuFeR3W5u0SRypl9m1NQY_ZIGfEuNrfI5iRKJnjDFa8IvIpmt3RnqEGbLIMr022KGlhLLXKDfIYvrDlstpl0znxI4gyWjoAHDBicOek4xRdOUhe_XKnZLZfxTKihmHE0x2CFRI5GTa12nNTpGrQv_MNwjoNfWFQjTCPkv8-7KOzpbbcU0F3Dow1C1PwGjVSQkA1uipniJoUj0p7pH0D6RG7Qqc8pUTpykZIdhYheSbJGP5Sk9HEWV28PDw3XhF5MTsrWKZepokmXpodjPrvIEYhTBBYoeoYJTqMY8jluirupmSuDyLXNX1MEpyy-Soenfpw2avD5_bY623tIa6WghRH7eZhCo2tpkGy229T_YZpNtWPVGLOiOwSF-yvulavvl7qjiRFPRPh8zsGGHelclVtd8VFDPp0t7fh7ZOhEyCQV6JXh7KW21kjXrZGckhXOAH9AfTJKOD58aaDD4DaahNM3CHFerw8I2nApwC2BY2uW6WS2PCtst7dK7YjulmlW5WyVQ88v4RqVv2CVQ2qV-JVDxq2WjLMeoEhgXtl2alZpe-eslMLq4A1VTqrv_Cja7YasbtrthpxsedsNuNzy6fEpcrYxvrkCtN5eM20vm7SXr9pJdvwmvcad8v12jw-rNcQ273fCogrW-Bt8unNGR5n1qp4c9PP4jEuM8ldqxr-FcsuWBhpp3egBreaYeBLMEwye1LcDjf029z4s=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 CM-050-090_Modify_Customer_Profile_(IF) — CM-050-090_Modify_Customer_Profile_(IF)

**Swim Lanes**: Credit Manager | **Tasks**: 6 | **Gateways**: 3

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
    subgraph Credit Manager
        n1["fa:fa-user Manage Credit Limit"]
        n2["fa:fa-user Maintain the Master Data for Credit Management"]
        n3["fa:fa-user Update the Necessary Changes in the Master Data"]
        n4["fa:fa-user Review Credit Limit Request"]
        n5["fa:fa-user Create Credit Limit Request (SCASE)"]
        n6[["fa:fa-cog Update Credit Limit in BP Master"]]
        n7(["fa:fa-play Start Modification of Customer Profile"])
        n8(["fa:fa-play Credit Limit Request Received"])
        n9(["fa:fa-stop Modification of Customer Profile Completed"])
        n10(["fa:fa-stop Credit Limit Enhancement Request Rejected"])
        n11["Resolve Credit Issues (IF)"]
        n12{{"fa:fa-code-branch Request Approved?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
        n14{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n1
    n1 --> n13
    n8 --> n14
    n14 --> n5
    n4 --> n12
    n7 --> n2
    n5 --> n4
    n6 --> n13
    n13 --> n9
    n12 -->|"No"| n10
    n12 -->|"Yes"| n6
    n2 --> n3
    n11 --> n14
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 serviceTask
    class n7 startEvt
    class n8 startEvt
    class n9 endEvt
    class n10 endEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
    class n14 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVmuPozYU_SsWo1FmJSLxDBk-tEpIqEbaWa0m-1C16QcHTOIOYGo7r2bz33tNgASGUVU10oxyj-85594b23DSIhYTzdfu7080p9JHp4HckIwMfDRYYUEGOroA3zCneJUSMVA5Ccvlgv5dpplOcVBpCgtxRtOjQhdkzQj6-qSjCRBTHQmci6EgnCYDfVBwmmF-DFjKuMq-I-PESEq3amnKeEz4NcEwPDNygZrSnFxh23M8J1Q8QSKWxy3RxE3GSTQ4q-JSto82mMuy_K0gz_jwncZyA3GCU0EgZyOz9CNekVT1KPlWYdGW7-phUKF8chjYosARzdeAOwZAHOevV8g1zmd0vr9f5o0p-jJb5gg-UYqFmJEECQnwfCdRQtPUv3OCSegaupCcvRL_zpp7M9vSI9WJD60buhrucE_oeiP9FUvjKnW4Vz34VnHQ-cG3DJ0f4X_Hi-Tx1SkYWWNr3DhNPTMwg9opSZL_5QRz5V-weK285nZohbPGy3RHbmC81avbnDnexOzOifAdjciNaBiG9vw6qvnINY33RaehPTKCjugaS7LHx6vgY-A0gqHrhab3ruDFr1vldvWZs6gWtOdu6DaC3tQMJ9a7gs7EdMZVhaCz5rjYoICTmEr0jHO8JvyyqD65-WOpJdhP8FDNukqo0z_SjMql9sdNvtXNp7mEPwRnGgIhAZthiVHCeNs0I3lHym5LfS1iGGMp9IlERAg4eijY4HxNBHrr0NZy2lovZEfJvtUGYH9tiejU4LZ5QFA19PHQwyKYLOYf2vzRj0YgYuu6hxYfSp9-rioH8i3be2jYRQr7Z6EOMXpmMU1ohCVlOWIJCrZCsgyqgy0BG4KAyIcbkXFHpLf4F5go3ZG4w328csGj-FdrFLCsSIl8I2QaHaVWFfMcfsao3AI3Ff1Joh4htSFfiGDprpnjkxBAQQ9PYWf6pnU6Xccfk-EKbs5o03hMioIz6PrXpXY-3_Lsfh45ROlWwJx-uxzoLs35rzS4KS9fchsNh7-ARBWaVWhX8biKnXrduQBuFVehaVWxd4nr0L2ENXvUUTcr98c6tlT8c6l9Ykvtp_r1ugu_E1GujKoF6yLQCJrtesuLS3VVX9gt2OqH7X7Y6Yfdfnh0e6O3VrzmmdiCx_3wY_VUa_dj9KJmvwQMr3oQtGG7H3ZqWNM1OGIZprHmn7Ty5QheoGKS4G0qtbOu4a1ki2MeaX75EqFty1tmRjHc7dkFPP8Dj1j9nw==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Customer Business Analyst | CM-050-010_Check_Credit_Rating_and_Limits_(IF), CM-050-030_Block_Delivery_(IF), CM-050-040_Block_Order_(IF), CM-050-060_Cancel_Order_(IF), CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF),  | |
| Credit Manager | CM-050-030_Block_Delivery_(IF), CM-050-040_Block_Order_(IF), CM-050-050_Resolve_Credit_Issues_(IF), CM-050-060_Cancel_Order_(IF), CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF), CM-050-090_Modify_Customer_Profile_(IF) | |
| System User | CM-050-030_Block_Delivery_(IF),  | |
| Accounts Receivable Analyst | CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF),  | |
| Logistics Team | CM-050-070_Request_Pre-payment,_Down-payment_or_Letter_of_Credit_(LOC)_(IF),  | |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for CM-050. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
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
| CM-050-R001 | Report | Manage Customer Credit Exposure (IF) operational report | Planned | SAP S/4HANA | Analytics | Medium |
| CM-050-C001 | Conversion | Legacy data migration for Manage Customer Credit Exposure (IF) | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for CM-050.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for CM-050.

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

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for CM-050:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for CM-050:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
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

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>CM-050 — Manage Customer Credit Exposure (IF)</span></div>
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
*CM-050 — Architecture Document (TOGAF BDAT) · Order To Cash (IF) · Generated: March 2026*

