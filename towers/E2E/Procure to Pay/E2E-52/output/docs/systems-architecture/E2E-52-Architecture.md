<div class="page-section">
<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-52 · Procure to Pay</p>
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
.page-section {
  display: flex;
  flex-direction: column;
  min-height: calc(100vh - 40px);
  box-sizing: border-box;
}
.page-footer {
  margin-top: auto;
  padding-top: 8px;
  border-top: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: #888;
  padding: 6px 12px;
  background: #fff;
}
@media print {
  .page-section {
    min-height: 100vh;
  }
  .page-footer {
    page-break-inside: avoid;
    break-inside: avoid;
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


<a id="toc"></a>

## Table of Contents

<nav class="toc">
<ol>
  <li><a href="#1-executive-summary">1. Executive Summary</a></li>
  <li><a href="#2-business-context-objectives">2. Business Context &amp; Objectives</a>
    <ul>
      <li><a href="#21-classification">2.1 Classification</a></li>
      <li><a href="#22-business-drivers">2.2 Business Drivers</a></li>
      <li><a href="#23-success-criteria">2.3 Success Criteria</a></li>
      <li><a href="#24-companion-documents">2.4 Companion Documents</a></li>
    </ul>
  </li>
  <li><a href="#3-business-architecture-togaf-b">3. Business Architecture (TOGAF &ldquo;B&rdquo;)</a>
    <ul>
      <li><a href="#31-business-process-overview">3.1 Business Process Overview</a></li>
      <li><a href="#32-business-process-diagrams">3.2 Business Process Diagrams</a></li>
      <li><a href="#33-business-roles-responsibilities">3.3 Business Roles &amp; Responsibilities</a></li>
    </ul>
  </li>
  <li><a href="#4-data-architecture-togaf-d">4. Data Architecture (TOGAF &ldquo;D&rdquo;)</a>
    <ul>
      <li><a href="#41-data-entities-ownership">4.1 Data Entities &amp; Ownership</a></li>
      <li><a href="#42-data-flow-diagrams">4.2 Data Flow Diagrams</a></li>
      <li><a href="#43-data-lineage">4.3 Data Lineage</a></li>
      <li><a href="#44-ricefw-data-objects">4.4 RICEFW Data Objects</a></li>
      <li><a href="#45-data-governance-quality">4.5 Data Governance &amp; Quality</a></li>
    </ul>
  </li>
  <li><a href="#5-application-architecture-togaf-a">5. Application Architecture (TOGAF &ldquo;A&rdquo;)</a>
    <ul>
      <li><a href="#51-current-state-current-state-application-landscape">5.1 Current-State Application Landscape</a></li>
      <li><a href="#52-future-state-future-state-application-landscape">5.2 Future-State Application Landscape</a></li>
      <li><a href="#53-change-impact-summary">5.3 Change Impact Summary</a></li>
      <li><a href="#54-component-overview">5.4 Component Overview</a></li>
      <li><a href="#55-ricefw-inventory">5.5 RICEFW Inventory</a></li>
      <li><a href="#56-integration-patterns">5.6 Integration Patterns</a></li>
    </ul>
  </li>
  <li><a href="#6-technology-architecture-togaf-t">6. Technology Architecture (TOGAF &ldquo;T&rdquo;)</a>
    <ul>
      <li><a href="#61-platform-infrastructure">6.1 Platform &amp; Infrastructure</a></li>
      <li><a href="#62-sap-development-object-status">6.2 SAP Development Object Status</a></li>
      <li><a href="#63-nfrs-design-principles">6.3 NFRs &amp; Design Principles</a></li>
      <li><a href="#64-security-governance">6.4 Security &amp; Governance</a></li>
    </ul>
  </li>
  <li><a href="#7-project-context">7. Project Context</a>
    <ul>
      <li><a href="#71-project-roadmap-go-live-plan">7.1 Project Roadmap &amp; Go-Live Plan</a></li>
      <li><a href="#72-raid-log">7.2 RAID Log</a></li>
      <li><a href="#73-recommendations-next-steps">7.3 Recommendations &amp; Next Steps</a></li>
    </ul>
  </li>
</ol>
</nav>

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-52 Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement** within the IAO program. It includes 1 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-52 - Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-52 - Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-52 Process Migration | Migrate Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-52 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **1 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-52 Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | Boundary Apps, MBC, SAP Ariba, SAP Ariba Network, SAP CFIN, SAP Fieldglass, SAP Fieldglass Network
, SAP S/4 (IP & IF) 
 | 50 | 20 |

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.2 Business Process Diagrams


#### BUSINESS ARCHITECTURE — 3.2.1 E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement — E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement

**Swim Lanes**: Boundary Apps · MBC · SAP Ariba · SAP Ariba Network · SAP CFIN · SAP Fieldglass · SAP Fieldglass Network
 · SAP S/4 (IP & IF) 
 | **Tasks**: 50 | **Gateways**: 20

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
        n4["Validate/Handle Exception Based on Rules setup in Readsoft"]
        n5["Receive Invoice/ B2B/OpenText/Web suite/ Email"]
        n6["Receive File in Bank"]
        n7["Payment Received"]
        n8["Hard Copy to be processed through optical character recognition (OCR)"]
        n54(["fa:fa-stop Payment Data Updated"])
        n61{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph MBC
        n48["Multi-Bank Connectivity (host-to-host)"]
        n49["Multi-Bank Connectivity (host-to-host)"]
    end
    subgraph SAP Ariba
        n16["Create Ariba Operational Contract"]
        n17["Publish Contract Catalogue"]
        n18["Create Text Material without catalogs"]
        n19["Create Indirect Purchase Requisition"]
        n20["Create Non-PO Contract Purchases"]
        n21["Create Integrated Catalog within Spot Buy"]
        n22["Punchout Catalog item"]
        n23["Select Intel Internal Catalog"]
        n24["Select item from Hosted Catalog"]
        n25["Validate Purchase Requisition Budget Check in Ariba (Capital Item Only),..."]
        n26["Create Indirect Purchase Requisition"]
        n27["Approve Indirect Purchase Requisition"]
        n28["Initiate Purchase Order Creation"]
        n29["Purchase Order Created"]
        n30["Replicate Goods Receipt"]
        n31["Reconcile Supplier Invoice"]
        n51(["fa:fa-play Ariba Operational Contract Initiated"])
        n52(["fa:fa-play Initiate Non-PO Contract Purchases"])
        n58(["fa:fa-stop Goods Receipt Replicated"])
        n65{{"fa:fa-code-branch exclusiveGateway"}}
        n75{{"fa:fa-arrows-alt parallelGateway"}}
        n76{{"fa:fa-arrows-alt parallelGateway"}}
        n77{{"fa:fa-arrows-alt parallelGateway"}}
        n78{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP Ariba Network
        n1["Receive Purchase Order"]
        n2["Send Purchase Order Confirmation"]
        n3["Create/Submit/Validate Supplier Invoice"]
    end
    subgraph SAP CFIN
        n37["Replicate Supplier Invoice Posting"]
        n38["Generate Payment Proposal"]
        n39["Execute Payment Run"]
        n40["Create APM Memo Record"]
        n41["Process BCM Payment Batching Based on Business Rules"]
        n42["Generate APM Payment File"]
        n43["Route to Approver"]
        n44["Correct APM Correction File"]
        n45["Reverse APP Doc Number and Memo Record Deletion"]
        n46["Payments Factory (APM, BCM, MBC Monitor)"]
        n47["Review Failed Payment Log"]
        n59(["fa:fa-stop Memo Record Created"])
        n60(["fa:fa-stop APP Doc Reversed"])
        n66{{"fa:fa-code-branch Manual Approval Necessary?"}}
        n67{{"fa:fa-code-branch Approved?"}}
        n68{{"fa:fa-code-branch exclusiveGateway"}}
        n69{{"fa:fa-code-branch Can Be Corrected?"}}
        n70{{"fa:fa-code-branch exclusiveGateway"}}
        n71{{"fa:fa-code-branch exclusiveGateway"}}
        n72{{"fa:fa-code-branch exclusiveGateway"}}
        n73{{"fa:fa-code-branch Reversal or Reprocessing?"}}
        n79{{"fa:fa-arrows-alt parallelGateway"}}
        n80{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP Fieldglass
        n32["Update SOW/Work Order"]
        n33["Validate Document Against SOW and Approval"]
        n34["Create SOW/Work Order"]
        n53(["fa:fa-play SOW/Work Order Creation Initiated"])
    end
    subgraph SAP Fieldglass Network 
        n35["Add Details About Work Performed Against SOW"]
        n36["Submit Timesheet, Expense Receipt, Another Document per SOW"]
    end
    subgraph SAP S/4 (IP & IF)  
        n9["Validate Replicate Requisition Budget Check in SAP S/4 (Capital Item Only),..."]
        n10["Replicate Indirect Purchase Requisition"]
        n11["Replicate Indirect Purchase Order"]
        n12["Calculate Taxes"]
        n13["Post Goods Receipt"]
        n14["Instruct Supplier About Rejected Invoice"]
        n15["Post Supplier invoice"]
        n50[["fa:fa-cog Send Supplier Invoice"]]
        n55(["fa:fa-stop Payment Details provided back to Source System (IP/IF)"])
        n56(["fa:fa-stop Indirect Purchase Requisition Replicated"])
        n57(["fa:fa-stop Taxes Calculated"])
        n62{{"fa:fa-code-branch exclusiveGateway"}}
        n63{{"fa:fa-code-branch Invoice Accepted?"}}
        n64{{"fa:fa-code-branch Indirect Material/Service?"}}
        n74{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n16 --> n17
    n25 --> n9
    n26 --> n27
    n28 --> n11
    n35 --> n36
    n36 --> n33
    n65 --> n25
    n62 --> n64
    n29 --> n75
    n13 --> n30
    n30 --> n58
    n5 --> n61
    n63 -->|"No"| n14
    n15 --> n37
    n38 --> n39
    n39 --> n79
    n40 --> n59
    n79 -->|"Reprocessing"| n70
    n41 --> n66
    n66 -->|"No"| n68
    n66 -->|"Yes"| n43
    n43 --> n67
    n67 -->|"No"| n69
    n70 --> n41
    n67 -->|"Yes"| n68
    n71 --> n45
    n72 --> n44
    n75 --> n32
    n79 --> n40
    n76 --> n10
    n76 --> n28
    n74 --> n29
    n80 --> n47
    n42 --> n48
    n44 --> n70
    n7 --> n54
    n52 --> n20
    n18 --> n65
    n20 --> n3
    n34 --> n18
    n77 --> n21
    n77 --> n22
    n77 --> n23
    n77 --> n24
    n21 --> n78
    n22 --> n78
    n23 --> n78
    n24 --> n78
    n78 --> n65
    n27 --> n76
    n73 -->|"Reversal"| n71
    n73 -->|"Reprocessing"| n72
    n2 --> n62
    n17 --> n19
    n75 --> n1
    n1 --> n2
    n51 --> n16
    n19 --> n77
    n9 --> n26
    n33 --> n62
    n3 --> n31
    n49 --> n46
    n80 --> n55
    n32 --> n35
    n37 --> n38
    n69 -->|"Yes"| n72
    n12 --> n57
    n53 --> n34
    n69 -->|"No"| n71
    n46 --> n80
    n47 --> n73
    n45 --> n60
    n68 --> n42
    n6 -->|"PAIN.002 (Pay-load file)"| n49
    n48 -->|"PAIN.001 (Pay-load file)"| n6
    n80 --> n7
    n10 --> n56
    n11 --> n74
    n74 --> n12
    n64 -->|"Service"| n50
    n64 -->|"Material"| n13
    n63 -->|"Yes"| n15
    n61 --> n4
    n4 --> n63
    n8 --> n61
    n31 --> n5
    class n50 serviceTask
    class n51 startEvt
    class n52 startEvt
    class n53 startEvt
    class n54 endEvt
    class n55 endEvt
    class n56 endEvt
    class n57 endEvt
    class n58 endEvt
    class n59 endEvt
    class n60 endEvt
    class n61 gateway
    class n62 gateway
    class n63 gateway
    class n64 gateway
    class n65 gateway
    class n66 gateway
    class n67 gateway
    class n68 gateway
    class n69 gateway
    class n70 gateway
    class n71 gateway
    class n72 gateway
    class n73 gateway
    class n74 gateway
    class n75 gateway
    class n76 gateway
    class n77 gateway
    class n78 gateway
    class n79 gateway
    class n80 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWVtzm0gW_itdSmVsV0kxzV162C1JthJXxbbKykxqK96HFrQk1ohmobGtdfzf9zR0I2ghz8S7eXDE4dwvXx_gpRewkPZGvY8fX6Ik4iP0csI3dEtPRuhkSXJ60kcV4Q-SRWQZ0_xE8KxYwhfRf0o2bKfPgk3QZmQbxTtBXdA1o-j3qz4ag2DcRzlJ8kFOs2h10j9Js2hLst2UxSwT3B-ovzJWpTV5a8KykGZ7BsPwcOCAaBwldE-2PNuzZ0IupwFLwpbSlbPyV8HJq3AuZk_BhmS8dL_I6TV5_h6FfAPXKxLnFHg2fBt_JUsaixh5VghaUGSPKhlRLuwkkLBFSoIoWQPdNoCUkeRhT3KM11f0-vHjfVIbRV_v7hME_4KY5PkFXaGcA_nykaNVFMejD_Z0PHOMfs4z9kBHH8xL78Iy-4GIZAShG32R3METjdYbPlqyOJSsgycRw8hMn_vZ88g0-tkO_mq2aBLuLU1d0zf92tLEw1M8VZZWq9X_ZAnymn0j-YO0dWnNzNlFbQs7rjM1DvWpMC9sb4z1PNHsMQpoQ-lsNrMu96m6dB1sHFc6mVmuMdWUrgmnT2S3Vzic2rXCmePNsHdUYWVP97JYzjMWKIXWpTNzaoXeBM_G5lGF9hjbvvQQ9Kwzkm7QhBVlL6NxmubVPfEvsX_c9_4gcRRCBOdfSBLGFF0-BzTlEUvQBAY2RPDjroBBhdzxIkURXFIS5mzF73v_bOhyQNcdDWj0SNFV8sggzedoYk7Ob1OafKPP_Pw7XYJLEZhCl1sSxW15tyE_i8CRSHiQPLS5POCak92WJhxJ7rDN4QPHF5KFaMrSHeIMLSlKIZs0F9HwTcaK9QYxCDEgMRLzRAJOM5TBwK8Bs0Tkp7fTuzMtPPsUFK_IaEUGOWcpUl5cEE7Q76lIofDkrBkSfnlRMgIYB0sY7WCD6HMQFzm4_rnqnPve62slBrOlle56Mm0WTER3XcQ8GojcQIxJQgMePUZ8h043LOcDzgbif819e_jrgofOLMZzgb9L0tCMReGmGYVQqnsICp4RkUfIL9jhIsFtb3BZxmIZR_mmZkFTyGTM1gXVmP29AdFH6Bp-iUMAPUV8wwqOgkow1-SGe7mrJIygwBzNiwxKnlNonn8XUV6Wuy1mGnuxG5YM5rd7D5W0ZsnETUucQrKgGVQ8pZvQzIuUcTQpdpqsWaYC2kJEokRgSLYanwV8CxqLIISNuPyblTmuhDR-e88vtKFVxrboCxR475km4TTQoDNR4H24puDlhgYPYj6rep9OSRqBQnQl7Nwm8e6s_-nTJ027-75qiE4B1MrY46_Jiaa5EuPcCuZWbAGodONQZFhW4pBTRxjLKKEqjQFBQPlnxsK8AqNU63MLV6DGkkAg2qJIQQjUSnzUEAbvESaN4Tw5Pk1IRaYjjmNqOuoUvNXKLQ2-hnOt8FAd9gHWOb-KdRWeN8RIlrGnfEBijlJA5Tim8REh9z1C3nuE_F8TegMy0Q3lTyx7aCJU48hrN57WmeUoJ-FBH7NkFWXbjl626mE7XxTLbcTP68E-2oTdvk9nVzdNxV6r93VlaA4AA3ur5o0Yxs80EY1M64MTVpyU5URbAywxhZfPNCgarHeFFp_dAOnx_Bpd0y0TPQpbvsYocjyvjn80mV7XKieEB4DK6_2WM4E2TQRbue5oasxmBMKi0iNWFY1XJP-OCf9h-5DYpVXUFug8ZVmJZkKd_C1AtkNjtVuBllwYn6MLWA5viu0SEg9LWzN6dAGQf9gPtrvfm3I0AwBgsA2eguW-yEpfrBnomgFYsEzfHKqKP0b0CQTBt7CO_at-hDhDDTyanu2xtIUbhiai4pPxHvC73ThzTZICELJKN_y4oaLksPP-XRtp1-tWIAsVHvD77wI2d9gtNiXQaVTV-9CcZ7wPR_H7xMz3iVndYlXNIPssEydFNXYwZAdBDt-Bxb7x_8DiWUTjcC2etJqgI8a72uHR4vb7-XfA6S4gtqzmigRdWpRzMF6TKMm5EC3nUTWhJmzvMestI46lneFt5np76VoC_ixmdQihpl8CXcahgA4O852j8VKsoqXFOc1WLNvCzDdi1MIS0FIdMuhbtKX5hlLeh8dIeOwrN7RycYD3NgmDNz_ZPmuw17S0dfu-OLfR6dUc_YauZmeo6fewWYv9kfTWvlor_CsbK26veb-wfGL8J5IdVceiBackDoq4fNAhz_oZhEXzifP1rY0T2-XeC28HCjBYH89VSe_ov0rM6d4_saP012JR555q_PixH_41KjeTjq2iJeMce3qWPScGJgrBtSWBUsG5uWCQLBiUXS5KBB1wDvXXd1VX0_pmjY7vro6n6Smzj-pqHJxB70NN9whqqt1pHIg3Lx0nkH1MTkarHojPF9XrrQO4td-JnPBwjwaDv4kHdkkwnYowVNeSwawZfCkhX70BvFQEy1UEKWJZkuBKDtNRBLMiuLZSOqwInuLAltRhKKVGRXB8SZA6XeWGW0r8vO_dsPveTzEoSpXyT0VgyQgsFaOlrCuCrYwpgjeUypuHXmnGUw7aWDqk0uC6bYdcX7_xD4EAP8VCqXTIqF3lqutpOmqHpIc21jmV0tqcJx2zVW49mX1bZchTGTJb4Yo8KIJqE51g1lZsSVAe-spDFYutzCoRW4rUKfRk1pVfjpRQ743hTZHMjwrFlEZUAi2pEtduSZ0m1gmmTrB0Qt2cMoGeUmqaOsHSCbZG8A48l1Y81S6eVbdYtWNV7YUPb-sdqCJRQ6WusTSBh1qdlU4Zl-J35DVWLmE1F6qE8tqsJ93STKqpVRZs1Uiu1hWOyoMlvbZqgvTaqsdlqHV2HTCWso7yz1H2bV1Wzk-dTlv2r1-Pr6pHPYsKYBSHK0toK_NqjOfjq5tPhmGiUzj0BjEjoXixT8-q2a4xxW-z4052PU8qMqzyVtdGNaWtDSCu3bOlQXlolPodQ7-rzpYKNC0dTVXScY3dCk5UXDJNStLXcNmS_E7jG4jwo_mppn0L11-72nTzCN06Qrfll6w21emkup1Ur5Pqd1KHXVTX6KRi9UmpTTa7yVY32e4mO91kt5vsdZP9bvKwkwxnUSe5O0qvO0qvO0qvO0qvO0qvO0qvO0qvO0qvO0q_jrLX720pvJWLwt7opVd-7YYv4iFdEfj80nvt90jB2WKXBL1R-VW4V5QPnhcRgaeebUV8_S9SqoHZ" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |
| MBC | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |
| SAP Ariba | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |
| SAP Ariba Network | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |
| SAP CFIN | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |
| SAP Fieldglass | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |
| SAP Fieldglass Network
 | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |
| SAP S/4 (IP & IF) 
 | E2E-52_Purchase_Requisition_to_Payments_for_Indirect_Non-Mfg._&amp;_Mfg._procurement | |

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.


#### 4.2.1 Current-State — Current-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E52CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E52CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E52CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E52CDAA_e_g_XEUS -.-> E2E52CDAD_e_g_Azure_SQL
    end
    style E2E52CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E52CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E52CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E52CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E52CDAA_e_g_MES_300 -.-> E2E52CDAD_e_g_SAP_HANA
    end
    style E2E52CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E52CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E52CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYtO2zAUhl_FMqq0SS0LLWlHJJCc20AKiJGyTSJT5CZOa-EmUeKMltJ3n50brDQMYUuRfS7_cb4TORsYJCGBGuz1NjSmXAMbD_IFWRIPasCDM5yLVV-schIUGeVrh_whrHKyJGm8ZcoPnFE8YySXbqETJTF36WMtdaSmqypY2m28pGxdeVwyTwi4vegDJASE-LaMYslDsMAZr9WKnFzi1U8a8oW0RJjlRMYt-JI5eEZYWZZnRWmNxWu5KQ5oPJfmkSqNGY7vXxiP1e0WbHs9L25rganuxUCMgOE8N0kEcJrqyQpElDHtQFdN27b7Oc-Se6IdKMpkoo_r7eBBHk0bpqt-kLAkk-6Rqe7qhTNjzWo5pJpjNGnlhtbEHA075Y501RoqO3IkYc_Hs21d1dVWzzAUMTr1xmPp9uJKMS9m8wynC2ANLXVomMhwfOLPffRYZMR3vzt3HhQIf1fRcoQ0IwGnSdxCk6NJR2X2L-vWFYnkcH4I5FoIaJpWMX2dY-5U_ORBrwi_jkLxDINjr4iIIl5ZipVBQAR58LOULLG-dQowOBycdVWqEkkc1iz4mpFOEA1sJGcL21Lk_Bf2kfji_4PXRdf-ObpCH6J7abn-SFEawGILxPY9jNuybyAWMUDGvIdwfZJ9kJtS72HcxH4I8f6y4PT07KkGZJZMwReAri_E06ZM3E1P3R_FTuscMhfHv3tBLAgVYKIpAujGOL-YWsb09sYCjvXNujI7uuncPFsdX_YdpSmjAZbe_a1zfLOjTybmuLqi97XI8S0hb8XhIIkGDo1IJV9dGXvbUb1hQ1-Vs6V_cnLyCj3swyXJlpiGUNtUPwHxLwlJhAvGxTUOccETdx0HUCsvZlikIebEpFgQXVbG7V_4rv7F" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">



#### 4.2.2 Future-State — Future-State Data Flows

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "15px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef dbCyl fill:#A5D6A7,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E52FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E52FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E52FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E52FDAA_e_g_XEUS -.-> E2E52FDAD_e_g_Azure_SQL
    end
    style E2E52FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E52FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E52FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E52FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E52FDAA_e_g_MES_300 -.-> E2E52FDAD_e_g_SAP_HANA
    end
    style E2E52FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E52FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E52FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlQ1L4zAYx79KiAzuYPPqZrezoJCt7SlU8ey8O7BHydp0C2ZNadNzc-67X9I3vbl6YgIleV7-T_p7SrqBAQ8JNGCns6ExFQbYeFAsyJJ40AAenOFMrrpylZEgT6lYO-QPYaWTcV57i5QfOKV4xkim3FIn4rFw6WMldaQnqzJY2W28pGxdelwy5wTcXnQBkgJSfFtEMf4QLHAqKrU8I5d49ZOGYqEsEWYZUXELsWQOnhFWlBVpXlhj-VpuggMaz5V5oCtjiuP7F8ZjfbsF207Hi5taYDr2YiBHwHCWmSQCOEnGfAUiyphxMNZN27a7mUj5PTEONG00Gg-rbe9BHc3oJ6tuwBlPlXtg6rt64WyyZpUc0s0hGjVyfWtkDvqtckdj3eprO3KEs-fj2fZYH-uN3mSiydGqNxwqtxeXilk-m6c4WQCrb-l920QTxyf-3EePeUp897tz50GJ8HcZrUZIUxIIyuMGmhp1Oiqyf1m3rkwkh_NDoNZSwDCMkunrHHOn4icPenn4dRDKZxgce3lENPnKSqwIAjLIg5-VZIH1rVOA3mHvrK1SmUjisGIh1oy0gqhhIzUb2Jam5r-wj-QX_x-8Lrr2z9EV-hDdS8v1B5pWA5ZbILfvYdyUfQOxjAEq5j2Eq5Psg1yXeg_jOvZDiPeXBaenZ08VILNgCr4AdH0hnzZl8m56av8odlrnkLk8_t0LYkGoARNNEUA3k_OLqTWZ3t5YwLG-WVdmSzedm2er46u-oyRhNMDKu791jm-29MnEApdX9L4WOb4l5a047PGo59CIlPLllbG3HeUb1vR1NRv6Jycnr9DDLlySdIlpCI1N-ROQ_5KQRDhnQl7jEOeCu-s4gEZxMcM8CbEgJsWS6LI0bv8CdGL-7w==" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 4.3 Data Lineage

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|
| 1 | e.g. MES 300 | e.g. CKMLHD table | e.g. XEUS | e.g. dbo.CostElements | Lineage notes |

### 4.4 RICEFW Data Objects

Reports and Conversions for this capability will be populated from the Smartsheet Object Tracker via automated API extraction.

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| E2E-52-R001 | Report | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-52-C001 | Conversion | Legacy data migration for Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-52.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E52C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E52C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E52CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E52CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E52C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E52CMW_e_g_Azure_Service_Bus
    E2E52CMW_e_g_Azure_Service_Bus --> E2E52C_e_g_XEUS


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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVWtP2zAU_StWUL-1IzzaQoQqpU06dUoBETY2LVPkxretNTeJYgco0P--67jQ0IJgrpQm93Gufe6x_WglGQPLsRqNR55y5ZDHyFJzWEBkOSSyJlTiWxPfJCRlwdUygFsQximy7NlbpfygBacTAVK7EWeapSrkD2uog05-b4K1fUgXXCyNJ4RZBuT7qElcBBBNImkqWxIKPo2sVZUhsrtkTgu1Ri4ljOn9DWdqri1TKiTouLlaiIBOQFRTUEVZWVNcYpjThKczbT62tbGg6d-asW2vVmTVaETpSy1y3Y9SgqPRIK0Wzi2Z8zFV0OKpzHkBjEi1FEASQaUEiTEmvPr2YEompeQpSEmqMeVCOHtDHP12U6oi-wvOXv_kpGP315-tO70g5zC_byaZyApnz7btLUya52QzDGa_rVFfMG272-13_gOTUUV3Mb2TDzAPXmE--xiVSF5Bl8gpaW9VWnDGBNzRAuqMeB13w4jf7Qw3aJ-YPWRihxHNcY3lwcC2P8I0qLKczAqaz4kb_I6sqGQnRwyf7KhN3MvLYDRwr0cX5yRwf_lXkfXHJOnBUBCJ4llKgquN1T_024eDGOJZPPbD-Mi266gJdAh8mX0h6CPoQ0DHcbDDbwL89L-Hb2Zrx7up45sq2X0oC4hDKG55AnG_lK9Wd9A1SFUUWUcRjDKwm65to3t-hT7IpIp9gUdAqnr1KSbHBlgHkHXA2aTY753xnnGEP8g-GXlZgn_fwovzs33eM1W1Kk09SNlzf3YJxW3Xe4qsCs2rmoBI7uUIn0Mu8Ox5-oCJOvB7MbrIdi_0lNaiqY6BflDb4kP7oy1eT3VfUu3P7OQdsQYwQ45eiYPZJPC_-ufeJ1QaxKjtbWm5eS54QnXwG-IK4vHNtoTGG5m8K5sg9vxthXj6-PFThZfLdudNin9hNuNhhx1jIGtl01bAp-syuP9rMtmQakh5Jratfy_Enp6e7pxlVtNaQLGgnFnOo7nQ8F5kMKWlUHgNWbRUWbhME8upLharzHGi4HGKTVgY4-oflLNG5Q==" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-52.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E52F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E52F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E52FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E52FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E52F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E52FMW_e_g_Azure_Service_Bus
    E2E52FMW_e_g_Azure_Service_Bus --> E2E52F_e_g_XEUS


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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVW1P6jAU_ivNDN9A5wuoiyEZbtxwM9Q4X-7N3c1S1gM0lm1ZOxWV_35PV5QJGr0lGdt5eU77nKfts5VkDCzHajSeecqVQ54jS01hBpHlkMgaUYlvTXyTkJQFV_MA7kEYp8iyV2-VckMLTkcCpHYjzjhLVcifllC7nfzRBGt7n864mBtPCJMMyPWgSVwEEE0iaSpbEgo-jqxFlSGyh2RKC7VELiUM6eMtZ2qqLWMqJOi4qZqJgI5AVFNQRVlZU1ximNOEpxNtPrC1saDpXc3YthcLsmg0ovStFrnqRSnB0WiQVgvnlkz5kCpo8VTmvABGpJoLIImgUoLEGBNefXswJqNS8hSkJNUYcyGcrT6OXrspVZHdgbPVOzrq2L3lZ-tBL8jZyx-bSSaywtmybXsNk-Y5WQ2D2Wtr1DdM2z487HX-A5NRRTcxvaMvMHffYb76GJVIXkHnyClpr1WaccYEPNAC6ox4HXfFiH_Y6a_QvjF7yMQGI5rjGsunp7b9FaZBleVoUtB8StzgT2RFJTvaZ_hk-23iXlwEg1P3anB-RgL3t38ZWX9Nkh4MBZEonqUkuFxZ_T2_vdePIZ7EQz-M9227jppAh8D2ZJugj6APAR3HwQ5_CPDLvw4_zNaOT1OHt1Wy-1QWEIdQ3PME4l4p361u99AgVVFkGUUwysCuuraO7vkV-mkmVewLPAJS1a1PMTkwwDqALANORsVO94R3jSO8ITtk4GUJ_v0Mz89OdnjXVNWqNPUgZa_92SQUt133JbIqNK9qAiK5FwN89rnAs-flCybqwJ_F6CLrvdBTWoqmOgZ6QW2L9-2vtng91X1Ltb-zkzfEGsAEOXonDmaTwP_hn3nfUGkQo7bXpeXmueAJ1cEfiCuIh7frEhquZPKpbILY89cV4unjx08VXi7rnTcp_rnZjHsddoCBrJWNWwEfL8vg_q_JZEWqIeWV2Lb-vRF7fHy8cZZZTWsGxYxyZjnP5kLDe5HBmJZC4TVk0VJl4TxNLKe6WKwyx4mCxyk2YWaMi3_bJEb9" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


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

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-52-I001 | Interface | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-52-E001 | Enhancement | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-52-F001 | Form/Report | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


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

    subgraph E2E52CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E52CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E52CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E52CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E52CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E52CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E52CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E52CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlF1r2zAUhv-KUMld1jp2nKaCDmzHZoV0hLndBvMwin2ciMqWseU1aZr_PsnOR1tIoWy6ENL7Hj06OkLa4ESkgAnu9TasYJKgTYTlEnKIMEERntNajfpqVEPSVEyup_AHeGdyIfZuu-Q7rRidc6i1rTiZKGTInnaowbBcdcFaD2jO-LpzQlgIQPc3feQogIJv2yguHpMlreSO1tRwS1c_WCqXWskor0HHLWXOp3QOvN1WVk2rFupYYUkTViy0PDS0WNHi4YVoG9st2vZ6UXHYC925UYFUSzit6wlkiJalK1YoY5yTM9eeBEHQr2UlHoCcGcblpTvaTT896tSIWa76ieCi0rY1sd_ySk7lEeiN_ZF3dQBa47Fvea-B1hE4cG3fNN4AQfAjLwhc27UPPM8zVDuZ4Gik7ajoiHUzX1S0XCLf9G3Tm01nMcSL2HlqKohnlIa_Ihw15sgYRE0Ghtr5fHGOWhtpO8K_O5BuKasgkUwUaPrtqO7JTkv-6d9rZovRYwUghHQF79ZAke5yk2sOJxP7p2K-e_gwHsZfnK9ObBqm1Z4_HVup6lNqv6xCeDFEOg7puA8X4tYPY8sw9rVQU6SmHyzHq1T_Q0Xeo19ff37eJTtpz4cukDO7UX3AuHrvzyevCvdxDlVOWYrJpvs21O-TQkYbLtXDx7SRIlwXCSbtU8ZNmVIJE0bV9eSduP0LmaZ31g==" title="View full diagram">&#128065; View Full Diagram</a></div>


> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>


<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">



#### 6.1.2 Future-State — Future-State Platform Architecture

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#B5DFFF,stroke:#0077B6,stroke-width:2px,color:#003D5B
    classDef platBox fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFB5B5,stroke:#CC0000,stroke-width:2px,color:#660000

    subgraph E2E52FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E52FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E52FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E52FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E52FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E52FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E52FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E52FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlF1r2zAUhv-KUMld1jp2nGaGDuzEZoV0hHndBvMwin2ciMqSkeU1aZr_PsnOR1tooWy6ENL7Hj06OkLa4kzkgD3c620pp8pD2wSrFZSQYA8leEFqPerrUQ1ZI6nazOAPsM5kQhzcdsl3IilZMKiNrTmF4CqmD3vUYFitu2CjR6SkbNM5MSwFoNvrPvI1QMN3bRQT99mKSLWnNTXckPUPmquVUQrCajBxK1WyGVkAa7dVsmlVro8VVySjfGnkoWVESfjdE9G1dju06_USftwLfQsSjnTLGKnrKRSIVFUg1qigjHlngTuNoqhfKynuwDuzrMvLYLSffrg3qXl2te5ngglpbGfqvuRVjKgTcDIOR5OPR6AzHofO5DnQOQEHgRva1gsgCHbiRVHgBu6RN5lYur2a4Ghk7IR3xLpZLCWpVii0Q9eO5rN5Cuky9R8aCemckPhXgpPGHlmDpCnA0jufL89RayNjJ_h3BzItpxIyRQVHs68n9UD2W_LP8NYwW4wZa4DneV3BuzXA831uasPg1cT-qZhvHj5Oh-ln_4uf2pbttOfPx06u-5y4T6sQXwyRiUMm7t2FuAnj1LGsQy30FOnpO8vxLNX_UJG36FdXnx73yU7b86EL5M-vdR9Rpt_746tXhfu4BFkSmmNv230b-vfJoSANU_rhY9IoEW94hr32KeOmyomCKSX6espO3P0FvHd37g==" title="View full diagram">&#128065; View Full Diagram</a></div>


> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>


#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 6.2 SAP Development Object Status

| Metric | DEV | QAS | PRD |
|--------|-----|-----|-----|
| Transport Requests | — | — | — |
| Custom Code Objects | — | — | — |
| CDS Views | — | — | — |
| Fiori Apps | — | — | — |
| BAdIs / Enhancements | — | — | — |

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

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

Project delivery milestones for E2E-52 RICEFW objects:

| Phase | Planned Start | Planned End | Status | Notes |
|-------|---------------|-------------|--------|-------|
| Functional Specification (FS) | Per project plan | Per project plan | In Progress | Tower-level FS schedule |
| Technical Design (TDD) | FS + 2 weeks | FS + 6 weeks | Planned | Dependent on FS completion |
| Build & Unit Test (TUT) | TDD + 1 week | TDD + 8 weeks | Planned | Includes S/4 + Middleware |
| Functional User Test (FUT) | Build + 1 week | Build + 4 weeks | Planned | Tower-led validation |
| Go-Live (Release 2) | Per release plan | Per release plan | Planned | End-to-End Integrated Processes release |

> *Detailed object-level timelines will be auto-populated from the Smartsheet Object Tracker via API integration.*

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 7.2 RAID Log

Standard RAID items for E2E-52 (End-to-End Integrated Processes):

| # | Category | Description | Status | Owner | Priority |
|---|----------|-------------|--------|-------|----------|
| 1 | Risk | Data migration completeness — validate all legacy Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement data maps to S/4 target structures | Open | Tower Architect | High |
| 2 | Risk | Integration testing coverage — ensure all 2 integrated systems are validated end-to-end | Open | Integration Lead | High |
| 3 | Assumption | Target SAP S/4HANA system available in DEV/QAS per release schedule | Active | SAP Basis | Medium |
| 4 | Issue | API access provisioning — SAP OData, Smartsheet, and IAPM API credentials required for automation | Open | EA Pipeline Team | High |
| 5 | Dependency | Upstream BPMN process models validated and signed off by business process owners | Active | Process Owner | Medium |

> *Live RAID data will be auto-populated from the Smartsheet RAID log via API integration.*

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 1 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 1 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*E2E-52 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*
<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-52 — Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement</span></div>
</div>
