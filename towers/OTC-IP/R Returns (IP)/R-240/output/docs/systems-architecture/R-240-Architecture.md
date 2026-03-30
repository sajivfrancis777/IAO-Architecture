<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">R-240 — Manage Storage & Internal Movement of Inventory (IP)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Order To Cash (IP) (OTC-IP) Tower<br/>
  Capability R-240 · R Returns (IP)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **R-240 Manage Storage & Internal Movement of Inventory (IP)** within the IAO program. It includes 8 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Order To Cash (IP) (OTC-IP) |
| **Process Group** | R Returns (IP) |
| **Capability** | R-240 - Manage Storage & Internal Movement of Inventory (IP) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 1 Forms |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Order To Cash (IP) |
| **L1 Process** | R Returns (IP) |
| **L2 Capability** | R-240 - Manage Storage & Internal Movement of Inventory (IP) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | IP Order Management Transformation | Transform Intel Products order management onto S/4 HANA with integrated pricing and ATP | IDM 2.0 Products Revenue | High |
| 2 | Customer Experience Improvement | Reduce order processing time and improve order visibility for IP customers | Customer Centricity | High |
| 3 | Returns & Rebate Automation | Automate returns processing, rebate management, and chargeback handling | Revenue Assurance | Medium |
| 4 | R-240 Process Migration | Migrate Manage Storage & Internal Movement of Inventory (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Order Management (Intel Products) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Processing Time | < 2 hours | Time from order receipt to order confirmation | 6 hours (current) | Order Management Lead |
| Customer Credit Decision Time | < 15 minutes | Automated credit check and approval for standard orders | 2 hours (manual) | Credit Manager |
| Returns Processing Cycle | < 3 business days | End-to-end returns receipt to credit memo issuance | 7 business days (current) | Returns Manager |
| R-240 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **8 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for R-240 Manage Storage & Internal Movement of Inventory (IP).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | R-240-020_-_Perform_Cycle_Count_(IP) | R-240-020_-_Perform_Cycle_Count_(IP) | Warehouse Operator | 9 | 2 |
| 2 | R-240-030_-_Perform_Physical_Inventory_Count_(IP) | R-240-030_-_Perform_Physical_Inventory_Count_(IP) | Warehouse Operator | 9 | 2 |
| 3 | R-240-040_-_Update_Inventory_Value_(IP) | R-240-040_-_Update_Inventory_Value_(IP) | Inventory Area Manager, Logistics Ground Controller | 5 | 3 |
| 4 | R-240-050_-_Reconcile_Inventory_Count_(IP) | R-240-050_-_Reconcile_Inventory_Count_(IP) | Inventory Area Manager | 2 | 0 |
| 5 | R-240-070_-_Identify_Need_to_Move_Material_within_Facility_(IP) | R-240-070_-_Identify_Need_to_Move_Material_within_Facility_(IP) | Warehouse Operator | 13 | 1 |
| 6 | R-240-080_-_Receive_Request_for_Material_Movement_(IP) | R-240-080_-_Receive_Request_for_Material_Movement_(IP) | Warehouse Operator | 8 | 1 |
| 7 | R-240-090_-_Create_Transfer_posting_for_Plant-to-Plant_Transfer_(IP) | R-240-090_-_Create_Transfer_posting_for_Plant-to-Plant_Transfer_(IP) | Ground Controller | 8 | 0 |
| 8 | R-240-100_-_Create_Transfer_posting_for_Intra-Facility_Transfer_(IP) | R-240-100_-_Create_Transfer_posting_for_Intra-Facility_Transfer_(IP) | Warehouse Operator | 4 | 0 |

### 3.2 Business Process Diagrams

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.1 R-240-020_-_Perform_Cycle_Count_(IP) — R-240-020_-_Perform_Cycle_Count_(IP)

**Swim Lanes**: Warehouse Operator | **Tasks**: 9 | **Gateways**: 2

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
    subgraph Warehouse Operator
        n1["fa:fa-user Identify Bins via Warehouse Monitor"]
        n2["fa:fa-user Create Cycle Count (CC) Inventory Document via Batch Job or Manual"]
        n3["fa:fa-user Activate Physical Inventory Document"]
        n4["fa:fa-user Assign Counter for Counting"]
        n5["fa:fa-user Post Count of Physical Inventory Document."]
        n6["fa:fa-user Set Recount Status in Inventory Document"]
        n7["fa:fa-user Request for Approval for Post Count"]
        n8["fa:fa-user Perform Blind Count via RF Devices or Desktop"]
        n9[["fa:fa-cog Create New Physical Inventory Document"]]
        n10(["fa:fa-play Physical Inventory Cycle Count Initiated"])
        n11["Update Inventory Value (IP)"]
        n12{{"fa:fa-code-branch Recounting Required ?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n4
    n1 --> n2
    n6 --> n9
    n5 --> n11
    n10 --> n1
    n2 --> n13
    n9 --> n13
    n13 --> n3
    n12 -->|"No"| n7
    n12 -->|"Yes"| n6
    n7 --> n5
    n4 --> n8
    n8 --> n12
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 serviceTask
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVluP4jYY_StWRiNmpFDlSiAPrSCQalad7WjYi6qlDyb5AtYEO7UdLmX577WTcAllug_lAeWcfOd8FztO9kbCUjBC4_5-TyiRIdp35BJW0AlRZ44FdExUE18wJ3ieg-jomIxROSV_V2G2V2x1mOZivCL5TrNTWDBAn59MNFTC3EQCU9EVwEnWMTsFJyvMdxHLGdfRd9DPrKzK1twaMZ4CPwdYVmAnvpLmhMKZdgMv8GKtE5AwmrZMMz_rZ0nnoIvL2SZZYi6r8ksBz3j7laRyqXCGcwEqZilX-W94DrnuUfJSc0nJ18dhEKHzUDWwaYETQheK9yxFcUzfzpRvHQ7ocH8_o6ek6NN4RpH6JTkWYgwZElLRk7VEGcnz8M6LhrFvmUJy9gbhnTMJxq5jJrqTULVumXq43Q2QxVKGc5anTWh3o3sInWJr8m3oWCbfqf-rXEDTc6ao5_Sd_inTKLAjOzpmyrLsf2VSc-WfsHhrck3c2InHp1y23_Mj699-xzbHXjC0r-cEfE0SuDCN49idnEc16fm29b7pKHZ7VnRlusASNnh3NhxE3skw9oPYDt41rPNdV1nOXzhLjobuxI_9k2EwsuOh866hN7S9flOh8llwXCzRV8xhydQ40e8FcCwZrwP0j9rfZkaGwwx39bzRUwpUkmyHRoQKtCb4Qv3M1EOtxMafF3qnrY84qHmgaJfk6p-VVKKHKHpET3StjBnfoTFLypW6rsxHWCZL9IHNEePoGdMS5217t20_TCRZ6wQvy50gCc5vGLcNvCsDIciC1pUpmKm01bV62to6v617YUI2_bDsv7L_1LbptW2mINGrOlu0z1RiWQpE6A97CNomr_BXCaocXfywKDhbq0o0OBfZ1vevegGuoldopE6_tGlKL8ZrjMagHxChV2MM4k2you00-HayStjiuNofYfODBbn0sK2Hk0mRqyfnhvRy_zypXUdUmlT5PF766K37uUh1BWflF5yXgB6eXh7bldvOfn8uPYXuXB20au81q6HWv5or4ZCiX2bG4XCpdW9rYZvkpSBr-LU-A84ydUrWF9RF3e7Pahs20K6h08BeDQcN9Gto28doqyEa7DTQbfDgCttNthOuBN9nxkc2M76rjXTN_wGiutFrbgS13m-gV8N-A_tNOufixNItHU_qFu3cpt3btHeb9m_Tvdt0cJvu36YHl--DdkfW6ZXa5u13eOf4FmjT7pE2TGMFfIVJaoR7o_oEUp9JKWS4zKVxMA1cSjbd0cQIq08Fo6y29ZhgdYKvavLwDzY4-ww=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.2 R-240-030_-_Perform_Physical_Inventory_Count_(IP) — R-240-030_-_Perform_Physical_Inventory_Count_(IP)

**Swim Lanes**: Warehouse Operator | **Tasks**: 9 | **Gateways**: 2

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
    subgraph Warehouse Operator
        n1["fa:fa-user Retrieve Applicable Bins Via Warehouse Monitor"]
        n2["fa:fa-user Create Physical Inventory (PI) Document"]
        n3["fa:fa-user Activate PI Document"]
        n4["fa:fa-user Assign Counter for Counting"]
        n5["fa:fa-user Enter Count Via RF Scanner or in Desktop"]
        n6["fa:fa-user Post Counted Results in Physical Inventory (PI) Document"]
        n7["fa:fa-user Set Recount Status in PI Document"]
        n8[["fa:fa-cog Create New PI Document (Automatic)"]]
        n9["Identify Physical Inventory Counting Required"]
        n10(["fa:fa-play Counting of Physical Inventory Initiated"])
        n11["Update Inventory Value (IP))"]
        n12{{"fa:fa-code-branch Recounting Required ?"}}
        n13{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n1 --> n2
    n9 --> n1
    n4 --> n5
    n5 --> n12
    n7 --> n8
    n3 --> n4
    n13 --> n3
    n6 --> n11
    n12 -->|"No"| n6
    n8 --> n13
    n2 --> n13
    n12 -->|"Yes"| n7
    n10 --> n9
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 serviceTask
    class n10 startEvt
    class n11 startEvt
    class n12 gateway
    class n13 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVtuO4jgQ_RUrrRaNFKRcCZ2HXXHLCmlnBg0zPRoN-2AcB6wOdtZ2uCzDv6-dCyQMPKw2Dyh1fM6pchFXcjIQi7ERGs_PJ0KJDMGpIzd4izsh6KygwB0TlMAb5ASuUiw6mpMwKhfkn4Jme9lB0zQWwS1Jjxpd4DXD4OvMBEMlTE0gIBU9gTlJOmYn42QL-XHMUsY1-wkPEispslVLI8ZjzK8Eywps5CtpSii-wm7gBV6kdQIjRuOWaeIngwR1zrq4lO3RBnJZlJ8L_AEevpFYblScwFRgxdnIbfonXOFU71HyXGMo57u6GUToPFQ1bJFBROha4Z6lIA7p-xXyrfMZnJ-fl_SSFHyZLClQF0qhEBOcACEVPN1JkJA0DZ-88TDyLVNIzt5x-ORMg4nrmEjvJFRbt0zd3N4ek_VGhiuWxhW1t9d7CJ3sYPJD6FgmP6rfm1yYxtdM474zcAaXTKPAHtvjOlOSJP8rk-or_wLFe5Vr6kZONLnksv2-P7Z-9au3OfGCoX3bJ8x3BOGGaRRF7vTaqmnft63HpqPI7VvjG9M1lHgPj1fD17F3MYz8ILKDh4Zlvtsq89WcM1QbulM_8i-GwciOhs5DQ29oe4OqQuWz5jDbgG-Q4w1T7QSfMsyhZLwk6IvaP5ZGAsME9nS_wWcsOcE7DIZZlhKkDykYESrAG4ENow9MnW_lY_zVsHLaVmOOVWvAfHMUyigFM7rDVImO4GU-64IJQ_lWAW0Pt-0xRJLsCpfZA4F3IxCCrCkYs5xKFSaMl_fqNLV1fls3LegFtdjq5wgsEKRUgcqCUDDB4l2yrG3Sb5vMmZBV6lh1UuSpFFr731oQtE0XWCovVFS2kFDmpeWjfgx-XOSIres_4SPeNyXgZZhLtoWSoK6SN_WvSj6LFYckx3uF191UNf2dE47jdnrbernkz1LY4LPknt1MPUdEVahtuk0f_Vx-zWJd_JX9BtMcg5fZvNu9SeucTtdtx7i3UmMUberGNesFvy-N87mpde9r8QGluSA7_Ed5wq8yNQPLG2qDXu839eRX4WsZVnOHemXoV6FfrdbsoIwHVeiWoVdbV7Fbxf1KXZvbjgZ-Lo2PbGn8VOsVPqh4tc65iS-671gUwqBesErma2Me6R3Wc7gFO_dh9z7s3Yf9-3D_PhzchwfNsd4u3bq8Gdu4_QB36mHeht0aNkxji_kWktgIT0bxJaO-dmKcQHXSjbNpQHWqFkeKjLB44xt58QBPCFSDeFuC538BsUnlsQ==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.3 R-240-040_-_Update_Inventory_Value_(IP) — R-240-040_-_Update_Inventory_Value_(IP)

**Swim Lanes**: Inventory Area Manager · Logistics Ground Controller | **Tasks**: 5 | **Gateways**: 3

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
    subgraph Inventory Area Manager
        n1["fa:fa-user Analyze Post Difference"]
        n2["fa:fa-user Select the Correct Variance Category and the Reason."]
        n4[["fa:fa-cog Adjust Difference in S/4"]]
        n5[["fa:fa-cog Post Material Document for Loss or Gain in Inventory"]]
        n9{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph Logistics Ground Controller
        n3[["fa:fa-cog Adjust Difference in EWM"]]
        n6["- Reconcile Inventory Count (IP)"]
        n7["- Perform Cycle Count (IP)"]
        n8{{"fa:fa-code-branch Differences in Quantity During Posting ?"}}
        n10{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n3 --> n8
    n8 -->|"No"| n10
    n1 --> n9
    n10 --> n6
    n9 --> n5
    n9 --> n4
    n7 --> n3
    n2 --> n1
    n8 -->|"Yes"| n2
    n4 --> n10
    n5 --> n10
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 serviceTask
    class n6 startEvt
    class n7 startEvt
    class n8 gateway
    class n9 gateway
    class n10 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV2P6jYQ_StWVitaKbRJSAjkoRUbyGql3WpbbntVXfpgnAm4a2xkO7BcLv-9dhI-QhepUiNEmOOZc2ZOsLN3iMjBSZz7-z3lVCdo39FLWEEnQZ05VtBxUQ38gSXFcwaqY3MKwfWUfq3S_HD9btMsluEVZTuLTmEhAP3-5KKRKWQuUpirrgJJi47bWUu6wnKXCiakzb6DQeEVlVqz9CBkDvKc4HmxTyJTyiiHM9yLwzjMbJ0CInjeIi2iYlCQzsE2x8SWLLHUVfulghf8_pnmemniAjMFJmepV-wZz4HZGbUsLUZKuTmaQZXV4caw6RoTyhcGDz0DSczfzlDkHQ7ocH8_4ydR9Gk848hchGGlxlAgpQ082WhUUMaSuzAdZZHnKi3FGyR3wSQe9wKX2EkSM7rnWnO7W6CLpU7mguVNandrZ0iC9bsr35PAc-XOfF9pAc_PSmk_GASDk9JD7Kd-elQqiuJ_KRlf5Ses3hqtSS8LsvFJy4_6Uer9m-845jiMR_61TyA3lMAFaZZlvcnZqkk_8r3bpA9Zr--lV6QLrGGLd2fCYRqeCLMozvz4JmGtd91lOX-VghwJe5Moi06E8YOfjYKbhOHIDwdNh4ZnIfF6iZ74BrgWcmd2D2D0gjlegKyT7MX9LzOnwEmBu9ZzNOKY7b4CehVKozEtCpDACcycvy5qgnbNFBgQjczuRqmQ0v6uNrmpQ6lxaGHlMc-rjN8AK8F_aBOGX06MRCzQKP-7bMkjytH0x9AUXVZF7aqq5RejZ48JNBakXJnRUSEkehZKIXN_xIbIfE6uXDEO9_sjI5ZSbFUXM43WWGLGgD3WT3vmHA51jdkPV3Y_iwVVmhKFHqUozcip2QRSmOpLz3v_YdzJ55er5vqmqGv8M6cToQwuHm1qpDT67un1-7atcVXxCtJ4sELpjjC4mTs4j25P8u7cnEVkedGUsl39WmKuqd6hcSnNIVV5bu8_n02p_1Xeh05STlip6AZuW8l7qNv9yfTThAMbfps5v4iZ880SN7hfpw2PoVfH_SYe1mHUDsMmjOuw14RBHfpXkn-CqjSDBg-btGMLUTuuNrFt7Hh4teDgY7h3eTC1VsKbK9HNlf7pddCC44_hwfH8aqHDD1HjbwM7rrMCucI0d5K9U73SzWs_hwKXTDsH18GlFtMdJ05Svfqccp2byjHFZousavDwD7PCmTM=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.4 R-240-050_-_Reconcile_Inventory_Count_(IP) — R-240-050_-_Reconcile_Inventory_Count_(IP)

**Swim Lanes**: Inventory Area Manager | **Tasks**: 2 | **Gateways**: 0

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
    subgraph Inventory Area Manager
        n1["fa:fa-user Write-off Adjustment for Losses or Gains"]
        n2[["fa:fa-cog Update Inventory"]]
        n3(["fa:fa-stop Inventory Count Reconciliation Completed"])
        n4["Update Inventory Value (IP)"]
    end
    n4 --> n2
    n2 --> n1
    n1 --> n3
    class n1 userTask
    class n2 serviceTask
    class n3 endEvt
    class n4 startEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVNlu4jAU_RUrFaKVgpSVMHkYCQIZVWqlaujyUObBJNfgqWMj26EwiH8fmyUsoz6NH6Lc4-Nz7r1eNk4hSnBSp9XaUE51ijZtPYcK2ilqT7GCtov2wCuWFE8ZqLblEMH1mP7Z0fxosbI0i-W4omxt0THMBKCXexf1zULmIoW56iiQlLTd9kLSCst1JpiQln0DPeKRndthaiBkCfJE8LzEL2KzlFEOJzhMoiTK7ToFheDlhSiJSY8U7a1NjonPYo6l3qVfK3jEqzda6rmJCWYKDGeuK_aAp8BsjVrWFitquTw2gyrrw03DxgtcUD4zeOQZSGL-cYJib7tF21ZrwhtT9DyccGRGwbBSQyBIaQOPlhoRylh6E2X9PPZcpaX4gPQmGCXDMHALW0lqSvdc29zOJ9DZXKdTwcoDtfNpa0iDxcqVqzTwXLk23ysv4OXJKesGvaDXOA0SP_OzoxMh5L-cTF_lM1YfB69RmAf5sPHy426cef_qHcscRknfv-4TyCUt4Ew0z_NwdGrVqBv73teigzzsetmV6Axr-MTrk-C3LGoE8zjJ_eRLwb3fdZb19EmK4igYjuI8bgSTgZ_3gy8Fo74f9Q4ZGp2ZxIs5uudL4FrItbk9gNEj5ngGck-yg_vvE4fglOCO7Tl6k1RDRxCC-uXvWunKrEZESPQglAKFzN8PTLmaOL_ORIL3RqUQM_SyKE1jTt6GfM4Obxu20mJxlmMmamP3017AgjKKNRXcgNWCgYbSyNydyURG5doJvWJWA7q9f7prMjSndv_DI9TpfDfZHsJgHx5OCvf3YXi2JRY8HsULODg_Txcz4eGWXIBRc00d16lAVpiWTrpxdg-ieTRLILhm2tm6Dq61GK954aS7h8OpdxUOKTb7We3B7V9dwL6s" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.5 R-240-070_-_Identify_Need_to_Move_Material_within_Facility_(IP) — R-240-070_-_Identify_Need_to_Move_Material_within_Facility_(IP)

**Swim Lanes**: Warehouse Operator | **Tasks**: 13 | **Gateways**: 1

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
    subgraph Warehouse Operator
        n1["fa:fa-user Create Posting Change Warehouse Task to Move to Blocked Stock"]
        n2["fa:fa-user Confirm Posting Change Task via RF Scanner /Manual to Change Stock Type to..."]
        n3["fa:fa-user Create Posting Change Warehouse Task to Change Stock Type for FG"]
        n4["fa:fa-user Confirm Warehouse Task via RF Scanner /Manual to Change Stock Type for FG"]
        n5["fa:fa-user Perform ADPROD Transaction for Bin to Bin Transfer"]
        n6["fa:fa-user Confirm Bin to Bin Movement Warehouse Task"]
        n7["fa:fa-user Perform Scrapping of FG Stock"]
        n8[["fa:fa-cog Post Material Document After Scrapping FG"]]
        n9[["fa:fa-cog Post Material Document for Changing Stock Type for FG"]]
        n10[["fa:fa-cog Create WT for Bin to Bin Movement"]]
        n11[["fa:fa-cog Post Material Document"]]
        n12["Move Stock to Disposal Bin"]
        n13["Identify Need to Move Stock for FG"]
        n14(["fa:fa-play Identification of Business Scenario Initiated"])
        n15(["fa:fa-stop Stock Type Changed"])
        n16(["fa:fa-stop Material Location Changed"])
        n17(["fa:fa-stop Scrapping Completed"])
        n18{{"fa:fa-code-branch Business Scenario ?"}}
    end
    n3 --> n4
    n9 --> n15
    n4 --> n9
    n1 --> n2
    n8 --> n17
    n2 --> n12
    n12 --> n7
    n7 --> n8
    n18 -->|"Stock Type Transfer (To Blocked/Hold Stock)"| n3
    n5 --> n10
    n10 --> n6
    n6 --> n11
    n11 --> n16
    n13 --> n18
    n14 --> n13
    n18 -->|"Transfer Material 
from Bin to Bin"| n5
    n18 -->|"Scrapping"| n1
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
    class n14 startEvt
    class n15 endEvt
    class n16 endEvt
    class n17 endEvt
    class n18 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVl1vozgU_SsWVZUZKelgAiHlYVf5KDuVpjvVJLt9mOyDAyaxSmxkSNtsJv99r8EQoESa3c1D6T2-99x7jz-PRiBCanjG9fWRcZZ56NjLtnRHex7qrUlKe31UAH8Sycg6pmlP-USCZwv2d-6G7eRNuSnMJzsWHxS6oBtB0R_3fTSBwLiPUsLTQUoli3r9XiLZjsjDTMRCKu8rOo7MKM-mh6ZChlSeHUzTxYEDoTHj9AwPXdu1fRWX0kDwsEEaOdE4CnonVVwsXoMtkVle_j6lD-TtiYXZFuyIxCkFn222i7-QNY1Vj5ncKyzYy5dSDJaqPBwEWyQkYHwDuG0CJAl_PkOOeTqh0_X1ildJ0XK-4gh-QUzSdE4jlGYA371kKGJx7F3Zs4nvmP00k-KZelfWnTsfWv1AdeJB62ZfiTt4pWyzzby1iEPtOnhVPXhW8taXb55l9uUB_rZyUR6eM81G1tgaV5mmLp7hWZkpiqL_lQl0lUuSPutcd0Pf8udVLuyMnJn5nq9sc267E9zWicoXFtAaqe_7w7uzVHcjB5uXSaf-cGTOWqQbktFXcjgT3s7sitB3XB-7FwmLfO0q9-tHKYKScHjn-E5F6E6xP7EuEtoTbI91hcCzkSTZoici6VaAnOhrQiXJhCwc1I_j7ysjIl5EBkpvNJMU-kGPIs1gAaLZlvANrTHk2mUCPYgXqr7TWATPNESLDL4r468as9ViFjxictemzglfGEHffLQICOfg-umB8D2JFb_2yunR8pCopDc3N81Mw__Ww3vuSEjk_9Ykt7vbaNH9mw66sjjNLI9UgtcOTeaP377O0RIOhZQEGRM8j54ynosPn3woorJJN-ouuhanJnBHedZqpEnjdle1CGBdJUpbEUEnXZM__l6FBmKTzwV6gFlRxzeai2Cf555EgNToclXqNLc_RaMkyWVWHF1C1ymx2eTUq-Vp2Va2VKgdj3-mpnaQ2gz5ninKgxRzliYihRDI1dQOq_V8HwILiw7odwrbq9xxRXTXAsL2h6qsJIbzSBOwgOTLBmZquk_huktTEJxyuIEFuodbmkHpIXB9rJM5Z7I0E0ld1GI9v4sYtSIqRb4IXcGFQLedqloNM7FLYtpR3fh4PM9ASAdr2APBtqO_X1fG6VREwr1V_MOHaDD4Bfa1Nm8LEzvatgv7Vpu4MC1tjrW3q21L2-U41kA57hbmuBzO43-sjJqg5Q5GH5bVefrpM1yWheofV8YPKFoTODqfWRKaBTDS9kiP43Jc149LB6zbx1VJumE8bNdYFVbNJbxCpKgfI3ltzrvmyinMh-u3sNKzvNcbsNUND7thuxt2uuFRN-x2w-P6M6ExcntxBGbh4hC-PGRXL7cm7uhXVhMddaJuJzounyVG39hRuSMsNLyjkT--4YEe0ojs48w49Q2yz8TiwAPDyx-pxj4JIXLOCLwddgV4-gf-LL2H" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.6 R-240-080_-_Receive_Request_for_Material_Movement_(IP) — R-240-080_-_Receive_Request_for_Material_Movement_(IP)

**Swim Lanes**: Warehouse Operator | **Tasks**: 8 | **Gateways**: 1

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
    subgraph Warehouse Operator
        n1["fa:fa-user Create Posting Change Warehouse Task to Move Stock to Blocked Stock"]
        n2["fa:fa-user Confirm Posting Change Task via RF Scanner /Manual to Change Stock Type to..."]
        n3["fa:fa-user Perform ADPROD Transaction for Bin to Bin Transfer"]
        n4["fa:fa-user Confirm Bin to Bin Movement Warehouse Task"]
        n5[["fa:fa-cog Create WT for Bin to Bin Movement"]]
        n6[["fa:fa-cog Post Material Document"]]
        n7["Receive Request to Initiate Scrapping."]
        n8["Move Stock to Disposal Bin for Scrapping"]
        n9(["fa:fa-play Request for Material Movement Initiated"])
        n10(["fa:fa-stop Planning for Scrapping is Completed"])
        n11(["fa:fa-stop Material Location Changed"])
        n12{{"fa:fa-code-branch Business Scenario?"}}
    end
    n1 --> n2
    n8 --> n10
    n3 --> n5
    n5 --> n4
    n4 --> n6
    n6 --> n11
    n7 --> n1
    n2 --> n8
    n9 --> n12
    n12 -->|"Bin to Bin Transfer"| n3
    n12 -->|"Scrapping"| n7
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 serviceTask
    class n6 serviceTask
    class n9 startEvt
    class n10 endEvt
    class n11 endEvt
    class n12 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVk1v4zYQ_SuEgsAtIKeSLFmODi38JWCBDTaI0-aw7oGmKJuITKoklcT1-r93qC9bWudUH2zN48x7w-Fo6KNFREKtyLq9PTLOdISOA72jezqI0GCDFR3YqAL-wpLhTUbVwPikgusV-7d0c_38w7gZLMZ7lh0MuqJbQdGfX2w0hcDMRgpzNVRUsnRgD3LJ9lge5iIT0njf0EnqpKVavTQTMqHy7OA4oUsCCM0Yp2d4FPqhH5s4RYngSYc0DdJJSgYnk1wm3skOS12mXyj6gD9eWKJ3YKc4UxR8dnqffcUbmpk9alkYjBTyrSkGU0aHQ8FWOSaMbwH3HYAk5q9nKHBOJ3S6vV3zVhQ9L9YcwYdkWKkFTZHSAC_fNEpZlkU3_nwaB46ttBSvNLrxluFi5NnE7CSCrTu2Ke7wnbLtTkcbkSW16_Dd7CHy8g9bfkSeY8sDfPe0KE_OSvOxN_EmrdIsdOfuvFFK0_R_KUFd5TNWr7XWchR78aLVcoNxMHd-5mu2ufDDqduvE5VvjNAL0jiOR8tzqZbjwHU-J53Fo7Ez75Fusabv-HAmvJ_7LWEchLEbfkpY6fWzLDaPUpCGcLQM4qAlDGduPPU-JfSnrj-pMwSercT5Dr1gSXcCyom-5VRiLWTlYD7c_b62UhyleGjqjeaSwn7Qo1AaGhDNd5hv6QVDWTst0IN4o2ilBSmtWQYPNKmAtfX3Bb_X4xc8ZXLfFyhp3xhGTzFaEcw5uP72gHmBM8Nfe1V6z4ecAnh3d9dVGnWVHqlMBShNF49P3xboGd4rhYlmgiPA0YzxMnP4KZdSKrt0_vXEL-JMDfaU6155ujTB95aHiG1T35fnfhINGURfho-74aZs6AEYzBhEC0GKKzEhhDxRQhkc0RP9p6AQAypfYCQzI74i0BY5VL9XwAnEdc91wVQuFCiZDE3CbWg38v6XNss8g3ehUTUhbbZtuZpEEiD59bIVnTON0iJHjxl0gumSjjRiCk5jn2f0CoXbo2jVvwqCy8OveumnQO94PBc6ocMNNAXZoVmh4IpQCuQph1tL_LG2TqcqEEZh9cBdNBz-Dr1em5PKdOs3m48qO6jNoDL92vQrc1yb4zq4Hl48rO3a9CpzUpv39Woj7ZbrP9bW1f7-Abn0HS-OFJbDi2Fk9tUM4Q7sXYdH12H_OhxcjuPOyvjTlfv2quum6dTXUhd1r6JeM7Et29pTuccssaKjVf4vgf8uCU1xkWnrZFu40GJ14MSKyvvbKvIEIhcMw1jdV-DpPw252KI=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

#### BUSINESS ARCHITECTURE — 3.2.7 R-240-090_-_Create_Transfer_posting_for_Plant-to-Plant_Transfer_(IP) — R-240-090_-_Create_Transfer_posting_for_Plant-to-Plant_Transfer_(IP)

**Swim Lanes**: Ground Controller | **Tasks**: 8 | **Gateways**: 0

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
    subgraph Ground Controller
        n1["fa:fa-user Create Warehouse Task to Pick the Outbound Delivery"]
        n2["fa:fa-user Confirm Warehouse Task to complete the Picking"]
        n3["fa:fa-user Complete Post Goods Issue in EWM"]
        n4["fa:fa-user Initiate STO Creation"]
        n5["fa:fa-user Post Material Document for the Transfer"]
        n6["fa:fa-user Create Outbound Delivery"]
        n7[["fa:fa-cog Distribute Outbound Delivery to EWM"]]
        n8["Move Inventory to the Designated Location (if applicable)"]
        n9(["fa:fa-play Plant to Plant Transfer posting Initiated"])
        n10(["fa:fa-stop Inventory Transfer Completed"])
    end
    n2 --> n3
    n1 --> n2
    n7 --> n1
    n5 --> n8
    n8 --> n10
    n9 --> n4
    n3 --> n5
    n6 --> n7
    n4 --> n6
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 serviceTask
    class n9 startEvt
    class n10 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVdFuozoQ_RWLqsquRCQgEFIeVkohrCpt1Urp3T5s74MDdmLV2MiGtNkq_37HQEjIproPy0PCHGbOzBzb4w8rkzmxIuv6-oMJVkXoY1RtSEFGERqtsCYjG7XAT6wYXnGiR8aHSlEt2e_GzfXLd-NmsBQXjO8MuiRrSdA_dzaaQyC3kcZCjzVRjI7sUalYgdUullwq431FZtShTbbu061UOVFHB8cJ3SyAUM4EOcKT0A_91MRpkkmRD0hpQGc0G-1NcVy-ZRusqqb8WpN7_P7M8moDNsVcE_DZVAX_gVeEmx4rVRssq9X2IAbTJo8AwZYlzphYA-47ACksXo9Q4Oz3aH99_SL6pOgpeREInoxjrRNCka4AXmwrRBnn0ZUfz9PAsXWl5CuJrrxFmEw8OzOdRNC6Yxtxx2-ErTdVtJI871zHb6aHyCvfbfUeeY6tdvB7louI_Jgpnnozb9Znug3d2I0PmSilf5UJdFVPWL92uRaT1EuTPpcbTIPY-ZPv0Gbih3P3XCeitiwjJ6Rpmk4WR6kW08B1Pie9TSdTJz4jXeOKvOHdkfAm9nvCNAhTN_yUsM13XmW9elQyOxBOFkEa9IThrZvOvU8J_bnrz7oKgWetcLlB35WsRY5iWAslOSeq_W4e4f56sSiOKB4buVGsCLSDnrEiGwkIarSqJHpkGfxvCHqoq1VDlxDOtkTtXqx_T_i8Mz4pKFPFBcJMFiUnkMuQGnbY70OqyTlVF_AodYW-S5lrdKd1TRATaPF8Pwz2h8F3MI6Y6Wz59NA2yaQYRgTDiCbLPYSYgYMSmdUFEbDvpWoqfoJjqilIOeCYXlTzfyQLf_VRmVyjhMHislV9KdAI17Z6SjCD-Hu5JdDlFmqUrZ-pMiGarQXUkKMfMmuaRl8YRbgsOcvMBP46rOXmS19LyWFTP3IMTZv1b14OXaMS1IEF63XNgebr6bZyjkS6kuVJaT3HYUFPYmG4tC_CQ-PxN9gDnem2pteZYWt251sErTnrzFn3tTtY4qa1_c6ctGbQmdPWDDvTb83pyaE06Q_DaAB7l-HJZdi_DAeX4ellODwdYoMvN_01MCzd6Ua2ZVsFUQVmuRV9WM01DFd1TiiueWXtbQvXlVzuRGZFzXVl1WUOK5swDFOkaMH9f5rWhJE=" title="View Full Diagram">&#128065; View Full Diagram</a></div>

#### BUSINESS ARCHITECTURE — 3.2.8 R-240-100_-_Create_Transfer_posting_for_Intra-Facility_Transfer_(IP) — R-240-100_-_Create_Transfer_posting_for_Intra-Facility_Transfer_(IP)

**Swim Lanes**: Warehouse Operator | **Tasks**: 4 | **Gateways**: 0

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
    subgraph Warehouse Operator
        n1["fa:fa-user Perform ADPROD/ADGI Transaction for Bin to Bin Transfer"]
        n2["fa:fa-user Confirm Bin to Bin Movement Warehouse Task"]
        n3[["fa:fa-cog Create WT for Bin to Bin Movement"]]
        n4[["fa:fa-cog Post Material Document"]]
        n5(["fa:fa-play Request for Intra Facility Transfer Initiated"])
        n6(["fa:fa-stop Material Location Changed"])
    end
    n1 --> n3
    n3 --> n2
    n2 --> n4
    n4 --> n6
    n5 --> n1
    class n1 userTask
    class n2 userTask
    class n3 serviceTask
    class n4 serviceTask
    class n5 startEvt
    class n6 endEvt
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVV1v2jAU_StWKsQmBS2fhOVhEiRkqtSqqLD1oezBJDZYDXZmO3wM8d9nkxACa5-WB8g9vvece09i52CkLENGaHQ6B0KJDMGhK1dojboh6C6gQF0TVMBPyAlc5Eh0dQ5mVE7Jn1Oa7RU7naaxBK5JvtfoFC0ZAj_uTTBUhbkJBKSiJxAnuGt2C07WkO8jljOus-_QAFv4pFYvjRjPEL8kWFZgp74qzQlFF9gNvMBLdJ1AKaPZFSn28QCn3aNuLmfbdAW5PLVfCvQIdy8kkysVY5gLpHJWcp0_wAXK9YySlxpLS745m0GE1qHKsGkBU0KXCvcsBXFI3y6Qbx2P4NjpzGkjCmbxnAJ1pTkUIkYYCKng8UYCTPI8vPOiYeJbppCcvaHwzhkHseuYqZ4kVKNbpja3t0VkuZLhguVZndrb6hlCp9iZfBc6lsn36vdGC9HsohT1nYEzaJRGgR3Z0VkJY_xfSspXPoPirdYau4mTxI2W7ff9yPqX7zxm7AVD-9YnxDckRS3SJEnc8cWqcd-3rY9JR4nbt6Ib0iWUaAv3F8KvkdcQJn6Q2MGHhJXebZflYsJZeiZ0x37iN4TByE6GzoeE3tD2BnWHimfJYbECL5CjFVN2gqcCcSgZrxL0Re3XuYFhiGFP-w0miGPG12AYT56f4i_D-Ps9mKlXUsBUEkaBWgQjQoFkp7_TEkZ8bvxqcTrXnBGjmCjOVt0j26hjgMpWb_qpXNO4rw1PypYg4khZDV5mt02cyVR1u9y7Lp8wIcGjYtAnCIhZWr5T439qaopcPdRn9LtEqk4r3lPJIUjUzsyJ3DejK5xIongzxfW5xdW_cAnJiov2A0vhycxoBemyXac2V3VDbdDrfVMW1KFbhU4dOlXo1aFXhf069Kuw_fZrwvN-uoKd92G3vVeuVrwPV_zmHLqC-_WRYZjGGvE1JJkRHozTZ0B9KjKEYZlL42gasJRsuqepEZ6OS6MsMuVYTKB6i9cVePwL0mkK6g==" title="View Full Diagram">&#128065; View Full Diagram</a></div>

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Warehouse Operator | R-240-020_-_Perform_Cycle_Count_(IP), R-240-030_-_Perform_Physical_Inventory_Count_(IP), R-240-070_-_Identify_Need_to_Move_Material_within_Facility_(IP), R-240-080_-_Receive_Request_for_Material_Movement_(IP), R-240-100_-_Create_Transfer_posting_for_Intra-Facility_Transfer_(IP) | |
| Inventory Area Manager | R-240-040_-_Update_Inventory_Value_(IP), R-240-050_-_Reconcile_Inventory_Count_(IP),  | |
| Logistics Ground Controller | R-240-040_-_Update_Inventory_Value_(IP),  | |
| Ground Controller | R-240-090_-_Create_Transfer_posting_for_Plant-to-Plant_Transfer_(IP),  | |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for R-240. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
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
| R-240-R001 | Report | Manage Storage & Internal Movement of Inventory (IP) operational report | Planned | SAP S/4HANA | Analytics | Medium |
| R-240-C001 | Conversion | Legacy data migration for Manage Storage & Internal Movement of Inventory (IP) | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for R-240.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for R-240.

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

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| LOGF0349_IP | Form | ISM - Generate Packing List - IF/IP | 10. Object Complete | NA → NA | NA | 02.High |

**Summary**: 1 Forms

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for R-240:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for R-240:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (1 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-27)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 1 | 100.0% |
| **Total** | **1** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Form (F) | 1 |
| **Total** | **1** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 02.High | 1 |

**Tower Context:** OTC-IP has 292 total RICEFW objects (282 complete, 10 active/other)

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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>R-240 — Manage Storage & Internal Movement of Inventory (IP)</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*1 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| LOGF0349_IP | ISM - Generate Packing List - IF/IP | Aug-24 (100%) | Feb-25 (100%) | Feb-25 (100%) | Apr-25 (100%) |  |

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-27*

**Mapped sub-tower(s):** 8.4 FTS IP - Logistics & Inventory Management

**RAID Summary:** 19 open items (0 capability-specific, 19 tower-level), 220 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 3 | 3 |
| P2 - Medium | 0 | 12 | 12 |
| P3 - Low | 0 | 4 | 4 |
| **Total** | **0** | **19** | **19** |

**Other OTC-IP Tower RAID Items** (19 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 03755 | Risk | P1 - High | Coding for 2DN and AIF enhancements. | In Progress | Technology | 2026-03-27 |
| 03767 | Risk | P1 - High | Day 1 OTC Execution - APOP production cutover for allocation... | In Progress | OTC IP | 2026-04-24 |
| 01733 | Risk | P2 - Medium | Tariffs impacts Item/BOM design which is impacting ERP/SCP (... | In Progress | E2E | 2026-03-06 |
| 03060 |  | P2 - Medium | Resource shift across Intel / Accenture Managed Services | In Progress | CM & Comms | 2026-03-27 |
| 03712 | Risk | P2 - Medium | LOGE0627, LOGE0690 | In Progress | OTC IP | 2026-04-03 |
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
| 03627 | Risk | P3 - Low | Inconsistency Response from EH -API B-App | Not Started | B-Apps |  |
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
*R-240 — Architecture Document (TOGAF BDAT) · Order To Cash (IP) · Generated: March 2026*

