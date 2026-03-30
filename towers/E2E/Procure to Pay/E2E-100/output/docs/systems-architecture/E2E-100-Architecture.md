<div class="page-section">
<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-100 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-100 R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box** within the IAO program. It includes 2 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-100 - R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-100 - R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-100 Process Migration | Migrate R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-100 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **2 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-100 R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-100_R3_CFIN | E2E-100_R3_CFIN | Boundary Apps, CFIN, MBC, SAP S/4HANA IP | 15 | 10 |
| 2 | E2E-100_R3_SAP_Transportation_Management | E2E-100_R3_SAP_Transportation_Management | Boundary Apps, External Partners/
Supplier
, SAP S/4HANA IP | 12 | 6 |

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.2 Business Process Diagrams


#### BUSINESS ARCHITECTURE — 3.2.1 E2E-100_R3_CFIN — E2E-100_R3_CFIN

**Swim Lanes**: Boundary Apps · CFIN · MBC · SAP S/4HANA IP | **Tasks**: 15 | **Gateways**: 10

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
        n1["Receive File in Bank"]
        n2["Update Payment Remittance"]
        n17(["fa:fa-stop Payment Data Updated"])
    end
    subgraph CFIN
        n3["Execute Payment Run"]
        n4["Create APM Memo Record"]
        n5["Process BCM Payment Batching Based on Business Rules"]
        n6["Generate APM Payment File"]
        n7["Route to Approver"]
        n8["Correct APM Correction File"]
        n9["Reverse APP Doc Number and Memo Record Deletion"]
        n10["Fetch Payments Factory (APM, BCM, MBC Monitor)"]
        n11["Review Failed Payment Log"]
        n12["Generate Payment Proposal"]
        n13["Replicate Supplier Invoice Posting"]
        n19(["fa:fa-stop Memo Record Created"])
        n20(["fa:fa-stop APP Doc Reversed"])
        n21{{"fa:fa-code-branch Manual Approval Necessary?"}}
        n22{{"fa:fa-code-branch Approved?"}}
        n23{{"fa:fa-code-branch exclusiveGateway"}}
        n24{{"fa:fa-code-branch Can Be Corrected?"}}
        n25{{"fa:fa-code-branch exclusiveGateway"}}
        n26{{"fa:fa-code-branch exclusiveGateway"}}
        n27{{"fa:fa-code-branch Reversal or Reprocessing?"}}
        n28{{"fa:fa-arrows-alt parallelGateway"}}
        n29{{"fa:fa-arrows-alt parallelGateway"}}
        n30{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph MBC
        n14["Multi-Bank Connectivity (host-to-host)"]
        n15["Multi-Bank Connectivity (host-to-host)"]
    end
    subgraph SAP S/4HANA IP
        n16(["fa:fa-play Supplier Payment Process initiated"])
        n18(["fa:fa-stop Payment Details provided back to Source System (IP/IF)"])
    end
    n12 --> n3
    n3 --> n28
    n4 --> n19
    n5 --> n21
    n21 -->|"No"| n23
    n7 --> n22
    n23 --> n6
    n25 --> n5
    n24 -->|"No"| n26
    n9 --> n20
    n10 --> n29
    n26 --> n9
    n29 --> n11
    n11 --> n27
    n27 -->|"Reversal"| n26
    n2 --> n17
    n6 --> n14
    n29 --> n2
    n8 --> n25
    n13 --> n12
    n29 --> n18
    n21 -->|"Yes"| n7
    n1 -->|"PAIN.002 (Pay-load file)"| n15
    n14 -->|"PAIN.001 (Pay-load file)"| n1
    n28 -->|"Reprocessing"| n25
    n30 --> n8
    n22 -->|"Yes"| n23
    n22 -->|"No"| n24
    n15 --> n10
    n27 -->|"Reprocessing"| n30
    n24 -->|"Yes"| n30
    n16 --> n13
    n28 --> n4
    class n16 startEvt
    class n17 endEvt
    class n18 endEvt
    class n19 endEvt
    class n20 endEvt
    class n21 gateway
    class n22 gateway
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1tv4kYU_isjryISCbq-YsNDK27eIi0RCt1WVenDYI_DKMZjjcckNMt_7xk8Y8A4D93ykHiOv_Od-7H9bkQsJsbQuLt7pxkVQ_TeEVuyI50h6mxwQTpdVAl-x5ziTUqKjsQkLBMr-s8JZrn5m4RJWYh3ND1I6Yo8M4K-zbtoBIppFxU4K3oF4TTpdDs5pzvMDxOWMi7Rn0iQmMnJmro1Zjwm_AwwTd-KPFBNaUbOYsd3fTeUegWJWBZfkSZeEiRR5yidS9lrtMVcnNwvC7LAb3_QWGzhnOC0IIDZil36FW9IKmMUvJSyqOR7nQxaSDsZJGyV44hmzyB3TRBxnL2cRZ55PKLj3d06q42ir0_rDMEvSnFRTEmCCgHi2V6ghKbp8JM7GYWe2S0EZy9k-Mme-VPH7kYykiGEbnZlcnuvhD5vxXDD0lhBe68yhqGdv3X529A2u_wAfxu2SBafLU36dmAHtaWxb02sibaUJMn_sgR55b_h4kXZmjmhHU5rW5bX9ybmLZ8Oc-r6I6uZJ8L3NCIXpGEYOrNzqmZ9zzI_Jh2HTt-cNEifsSCv-HAmHEzcmjD0_NDyPySs7DW9LDdLziJN6My80KsJ_bEVjuwPCd2R5QbKQ-B55jjfojErT72MRnleVPfkL7P-WhtPJCJ0T1BIU4JohsbQfWvj7wuUDahveQxRoiU-7Egm0BPZUSFwFpFrqOXfAzjBwwT3CsHyWmGKBUYVSQwqD5UOtFLD00k4f7zgc4Bt9kai8tJ2mV0bdQE04UT6N1ou0ILsGDgYwcRf4zzAybySokDjyaImHGMRbWHY4KIgMWKQg7KAtQCwpxJW1DVLH1i-kIxwbU_TyAReQ32ZXiZ9F0ymnrM94deQQPrOOCeROJGpawpO3PINTuUCjkJaXqIp9MhjudsQjnAWXwaOpiQlkqVRHhMYQgLhaq8LFOJIMGiNezDflXnposV4ghYM9jfjDw2CqmP2lLyCIjgY1-F_Zc8NrH2ZKQ2DAuSswGkD65x485RGErwqc7iEsObZnsG8oiUrBFSooTRoNNtlAqqGuOi1qpXNhopOo0rrDd56f9d4-WjrbWA5Q_YWOCtxqmoKF49EdhVM2C9r43i8JLDbCVQ3xDd4px1P3qIUmnJPvlTLpqnmtqtNMDQz0V3VYs77MXP9H1Pz29Wq5EMaGYfrvBpRKPeNt8FZH3POXoseTgXKMcdpStIPjA5-QMkxW5Vo9lF8t5sMhuiyV-WSWpSpoD25YKEiWSbnfE8FjN4W2rsnWE_-b06c998Vb51ZjZZo9dn9dfQ4QvPlJX3_PBB5Cg-xevQuBva0MeX7HG0ZKSv4aOUTARuiQLLRaQybYoOjF7kJV6zkMNOrQyHIDt3Pl5_n4UPLQwE2COr1foZqqLNTHe1And3qbA3U2VP31VMfLqTg-9p4ZGvjuxwudcNXQFsDFXNfnxWTp89ug0gDB4rI1B6bSqBdsvuVoD4rDUv7aFlKw9cIX9nSU3FtUaXE0nDFb7kNAzq0QB11KJYK1bKbHgXNrP0pH31gW5vS8uVo_viTadroHkrdSxmO5ZsKeTiBrdqQew232uHaaFBHfZ7_KnJN6Kjc1n7aDT_r8tZ3dLl0cixVV8u8TXbDrGM2a6_N1HcsnXvnKgjoy4v3uRNMv55fy331Kn0tDVqlgzapbbZKLf1Gei2228VOu9htF3vt4n672G8XB-3iQasYyq7ERtfYEb7DNDaG78bpMxI-NWOSYFiPxrFr4FKw1SGLjOHpc8soT--bU4phCe4q4fFfwlR9cQ==" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### BUSINESS ARCHITECTURE — 3.2.2 E2E-100_R3_SAP_Transportation_Management — E2E-100_R3_SAP_Transportation_Management

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4HANA IP | **Tasks**: 12 | **Gateways**: 6

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
        n1["Receive/Send Information in Carrier Invoice Reconciliation/Dispute..."]
        n2["Event updates are received in GTT"]
        n17{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph External Partners/ Supplier 
        n11["Feed Rates/Charges Integrators 3rd party service – Redwood"]
        n12["Carrier"]
        n14(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n15(["fa:fa-play Events Published"])
        n20{{"fa:fa-arrows-alt parallelGateway"}}
        n21{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4HANA IP
        n3["Generate Freight Unit (TM)"]
        n4["Create Freight Order (TM)"]
        n5["Perform Carrier Updates and Calculate Charges"]
        n6["Execute Freight Order (TM)"]
        n7["Post Freight Settlement Document (TM)"]
        n8["Create Service PO for FSD (TM)"]
        n9["Post SES with Auto Release (TM)"]
        n10["Create Cost Distribution/Agency Business Document (TM)"]
        n13(["fa:fa-play Transportation Management Process initiated with Inbound Del."])
        n16(["fa:fa-stop TM process ended"])
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n22{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    n3 --> n4
    n5 --> n18
    n7 --> n8
    n19 --> n5
    n4 --> n19
    n9 --> n10
    n10 --> n16
    n11 --> n20
    n14 --> n11
    n17 --> n1
    n15 --> n12
    n12 --> n21
    n21 --> n17
    n20 --> n17
    n21 --> n2
    n20 --> n19
    n2 -->|"Event Update"| n18
    n18 --> n6
    n8 --> n9
    n6 --> n22
    n1 --> n22
    n22 --> n7
    n13 --> n3
    class n13 startEvt
    class n14 startEvt
    class n15 startEvt
    class n16 endEvt
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVttu2zgQ_RVCReAWsBNJlizHDwv4pm6AZmtE6e5DvQ-0RNlEaUogKV-a-t93KIm-KM7udtcPQeZo5szM0XCoFyvOEmINrJubF8qpGqCXllqRNWkNUGuBJWm1UQX8jgXFC0ZkS_ukGVcR_V66OV6-024aC_Gasr1GI7LMCPry0EZDCGRtJDGXHUkETVvtVi7oGov9OGOZ0N7vSD-10zJb_WiUiYSIk4NtB07sQyijnJzgbuAFXqjjJIkznlyQpn7aT-PWQRfHsm28wkKV5ReSPOLdHzRRK7BTzCQBn5Vas094QZjuUYlCY3EhNkYMKnUeDoJFOY4pXwLu2QAJzL-dIN8-HNDh5mbOj0nRp6c5R_CLGZZyQlIkFcDTjUIpZWzwzhsPQ99uSyWyb2Twzp0Gk67bjnUnA2jdbmtxO1tClys1WGQsqV07W93DwM13bbEbuHZb7OFvIxfhySnTuOf23f4x0yhwxs7YZErT9H9lAl3FM5bf6lzTbuiGk2Mux-_5Y_s1n2lz4gVDp6kTERsakzPSMAy705NU057v2G-TjsJuzx43SJdYkS3enwjvx96RMPSD0AneJKzyNassFjORxYawO_VD_0gYjJxw6L5J6A0dr19XCDxLgfMVGmVFOctomOeyeqZ_3Pk6t55ITOiG3EXwXtEDTzOxxopmHFGOxlgISgTAmwxkQ0_6UMSU0dLjbkJlXihye3s7t_48o3WBdrohXKEiT0AcibAgSFSJEk388fn5MsQJXl7mVooHKe7oHdJZwCmIV4jsYlZICPtYiTy3DocqDMptdDndKSI4ZmgGh4ETIe9QVOQ50x2cp9JdhwQKedK13Y3hSC2hxgeuCBCpTEjUFQnKgWVvJgbNC9d2uqBAss2ypFG8brjWqvHEe__VtJUzmBH9XonUyagCFaGIEazFBIHeuppjMcMNpkwvSOD7cE7oNwhLnSWaFQtG5YokDX_XPukKBWZb2cFM6d4wY4S9UrUKcn4u6PWriIYzFN15vw5_G6KH2Rl1F6r_SODlAAcKRbkX0BcQA71_fvxwKZ6nVRXk3POz3uJXXH1wnRGhh_c4tF_M7MFcjzGLC6aZaoEvw3t6YHckLv5FqkCnyqQ6OkZEKQZXGoz7JIuL8p_XYf1TM1E9UrPPCApGYTS54n9v0kTTCG2pWqFhoTKYP0ZgYK4EOPYpw1gHwulUgi6K8qgOl4THezSCs8T1_P1NpU63MWLPcBRlnglV7YVHzPGy6tdMMz1Oc1npA1_ohYMmhN0257d3Ipcqy9HzI8prFhijV_Pr9H92L1Rh9_8pzHWvDj7l_7iEeBd1Or_AzNamX5lOv7aDyjamc1_Zfm17tft9bdePHdv42zXQM4BTAe7Rw1A4BqhTHm1TkmsAt6YwHm7N6QQGsJuAydp0MHWXlD_M9q9O4Nz6cSaE069CTCO1aQh6dYJjkQ3brYs2FTm17t2zK7REzRfRJe69gftv4L36a-cSDcyVfwn3r8P3V2GQ7irsXIddA1tta03giqaJNXixym9p-N5OSIoLpqxD28KwJqI9j61B-c1pVVfwhGLYzOsKPPwFPmmdZg==" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-100_R3_CFIN, E2E-100_R3_SAP_Transportation_Management | |
| CFIN | E2E-100_R3_CFIN,  | |
| MBC | E2E-100_R3_CFIN,  | |
| SAP S/4HANA IP | E2E-100_R3_CFIN, E2E-100_R3_SAP_Transportation_Management | |
| External Partners/
Supplier
 | E2E-100_R3_SAP_Transportation_Management | |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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

    subgraph E2E100CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E100CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E100CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E100CDAA_e_g_XEUS -.-> E2E100CDAD_e_g_Azure_SQL
    end
    style E2E100CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E100CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E100CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E100CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E100CDAA_e_g_MES_300 -.-> E2E100CDAD_e_g_SAP_HANA
    end
    style E2E100CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E100CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E100CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYtumzAUhl_F8hRpk5KOJCVZkVrJXLJWolVX0m1SmZADJrHqYARmTZrm3WcDoV0Wuqq2hMy5_Mf-DjIbGPKIQAN2OhuaUGGAjQ_FgiyJDw3gwxnO5aorVzkJi4yKtUt-E1Y5Gec7b5nyHWcUzxjJlVvqxDwRHn2spfp6uqqClX2Cl5StK49H5pyA24suQFJAim_LKMYfwgXORK1W5OQSr37QSCyUJcYsJypuIZbMxTPCyrIiK0prIo_lpTikyVyZh7oyZji5f2E81rdbsO10_KSpBaamnwA5Qobz3CYxwGlq8hWIKWPGB1O3J5NJNxcZvyfGB00bj81R_dp7UFszBumqG3LGM-Ue2vq-XjSz1qyWQ7o9QuNGbuCM7eGgVa5v6s5A25MjnD1vbzIxdVNv9CxLk6NVbzRSbj-pFPNiNs9wugDOwOlrmmUjyw1IMA_QY5GRwPvm3vlQMvxVhasR0YyEgvKkoaZGk4_K9J_OrSczydH8CKi1VDAMo6J6IMneq_nRh34RfRlG8hmFx34RE02eWqmVQUAG-fCT0izJvroP0DvqnbXWqlJJEtVAxJqRdho75EjNBrmjqfk38r787v8H2UPXwTm6Qu9jfOl4wVDTdpjlK5CvbyLdFH4FtIwBKuZNnOu9HES9K_Ym0rvgd4FuKQxOT8-eakp2SRZ8Buj6Qj4nlMmL6umVr2OvhS6ZyxPcvcAWRhqw0RQBdGOdX0wda3p74wDX-epc2S1NdW-erW6g2o_SlNEQK-_hBrqB3dIsGwtcXdiH-uQGjpR3kqjH455LY1LJVxfIwY5UJ9zx19Vs-J-cnPwDH3bhkmRLTCNobKpfgvyzRCTGBRPyUoe4ENxbJyE0ymsaFmmEBbEplkSXlXH7BzslASA=" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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

    subgraph E2E100FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E100FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E100FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E100FDAA_e_g_XEUS -.-> E2E100FDAD_e_g_Azure_SQL
    end
    style E2E100FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E100FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E100FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E100FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E100FDAA_e_g_MES_300 -.-> E2E100FDAD_e_g_SAP_HANA
    end
    style E2E100FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E100FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E100FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYtumzAUhl_F8hRpk5KOJCVZkVrJBFgr0aor6TapTMgBk1h1MAKzJk3z7rOB0C4LXVVbQuZc_mN_B5kNDHlEoAE7nQ1NqDDAxodiQZbEhwbw4QznctWVq5yERUbF2iW_CaucjPOdt0z5jjOKZ4zkyi11Yp4Ijz7WUn09XVXByu7gJWXryuOROSfg9qILkBSQ4tsyivGHcIEzUasVObnEqx80EgtliTHLiYpbiCVz8YywsqzIitKayGN5KQ5pMlfmoa6MGU7uXxiP9e0WbDsdP2lqganpJ0COkOE8t0gMcJqafAViypjxwdQtx3G6ucj4PTE-aNp4bI7q196D2poxSFfdkDOeKffQ0vf1otlkzWo5pFsjNG7kBvbYGg5a5fqmbg-0PTnC2fP2HMfUTb3Rm0w0OVr1RiPl9pNKMS9m8wynC2AP7L6mORaauAEJ5gF6LDISeN_cOx9Khr-qcDUimpFQUJ401NRo8lGZ_tO-9WQmOZofAbWWCoZhVFQPJFl7NT_60C-iL8NIPqPw2C9ioslTK7UyCMggH35SmiXZV_cBeke9s9ZaVSpJohqIWDPSTmOHHKnZILc1Nf9G3pff_f8ge-g6OEdX6H2ML20vGGraDrN8BfL1TaSbwq-AljFAxbyJc72Xg6h3xd5Eehf8LtAthcHp6dlTTckqyYLPAF1fyKdDmbyonl75OvZa6JK5PMHdC2xhpAELTRFAN5Pzi6k9md7e2MC1v9pXVktT3Ztnqxuo9qM0ZTTEynu4gW5gtTTLwgJXF_ahPrmBLeXtJOrxuOfSmFTy1QVysCPVCXf8dTUb_icnJ__Ah124JNkS0wgam-qXIP8sEYlxwYS81CEuBPfWSQiN8pqGRRphQSyKJdFlZdz-AbfbAUo=" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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
| E2E-100-R001 | Report | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-100-C001 | Conversion | Legacy data migration for R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-100.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E100C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E100C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E100CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E100CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E100C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E100CMW_e_g_Azure_Service_Bus
    E2E100CMW_e_g_Azure_Service_Bus --> E2E100C_e_g_XEUS


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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVWtv2jAU_StWKr7B6j6gbVQhBRImptBWTbduWqbIxBewZpIodtqyjv--65gWCq3aGSkk93Gufe6x_eikOQfHdRqNR5EJ7ZLH2NEzmEPsuCR2xkzhWxPfFKRVKfQihDuQ1inz_Mlbp3xjpWBjCcq4EWeSZzoSf1ZQB53iwQYb-4DNhVxYTwTTHMjXYZN4CCCbRLFMtRSUYhI7yzpD5vfpjJV6hVwpGLGHW8H1zFgmTCowcTM9lyEbg6ynoMuqtma4xKhgqcimxnxMjbFk2e8NY5sul2TZaMTZcy1y04szgqPRIK0Wzi2diRHT0BKZKkQJnCi9kEBSyZQChTE2vP72YULGlRIZKEXqMRFSunsDHL12U-ky_w3uXu_0tEN7q8_WvVmQe1g8NNNc5qW7RyndwmRFQdbDYvbaBvUZk9KTk17nPzA502wX0z99B_PgBeaTjzOF5JVsgZyS9lalueBcwj0rYZMRv-OtGQlOOoM12gdmD7ncYcRwvMFyv0_pe5gWVVXjacmKGfHCn7ETV_z0iOOTH7WJd3UVDvvezfDygoTej-A6dn7ZJDM4CiLVIs9IeL22BofBAaX9BJJpMgqi5IjSTdgUOgQ-TT8R9BH0IaLrutji1xG-B1-jV9ON4-3c0W2d7f2pSkgiKO9ECkmvUi8WeHBioeoosooiGGVx143bgfeDGr6fK50EEo-BTHc3J5keW2QTQFYB5-Nyv3suutYRfSP7ZOjnKf59iS4vzvdF15Y1yrQFIeNPPXqFVNx73b-xU8P5dScQyrsa4nMgJB5Af98j4wX0W0GmzE5HzLRW4qmPg164sdUH9L2tvpnqPafSj-zoHdGGMEWeXkiEUxIGn4ML_wNqDRPU-LbAvKKQImUm-BWJhcnodltHo7VW3tROmPjBtkp8cwwFmcZLZrv7NiW4tJvysMOPMZC38kkrFJNVGTwHNqSyJtWS8kRs2_yeiT07O9s505ymM4dyzgR33Ed7seH9yGHCKqnxOnJYpfNokaWOW18wTlXgRMEXDJswt8blP0cKSDU=" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-100.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E100F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E100F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E100FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E100FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E100F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E100FMW_e_g_Azure_Service_Bus
    E2E100FMW_e_g_Azure_Service_Bus --> E2E100F_e_g_XEUS


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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVWtP2zAU_StWUL-1wzxaIEKVUpJOnVJAy4BNyxS58W1rzU2i2AEK9L_vOi60tCCYK6XJfZxrn3tsPzppzsFxnUbjUWRCu-QxdvQUZhA7LomdEVP41sQ3BWlVCj0P4Rakdco8f_bWKdesFGwkQRk34ozzTEfiYQm11ynubbCx99lMyLn1RDDJgVwNmsRDANkkimWqpaAU49hZ1Bkyv0unrNRL5ErBkN3fCK6nxjJmUoGJm-qZDNkIZD0FXVa1NcMlRgVLRTYx5kNqjCXL_q4Z23SxIItGI85eapEfvTgjOBoN0mrh3NKpGDINLZGpQpTAidJzCSSVTClQGGPD628fxmRUKZGBUqQeYyGlu9PH0Ws3lS7zv-Du9I6PO7S3_GzdmQW5-8V9M81lXro7lNINTFYUZDUsZq9tUF8wKT066nX-A5MzzbYx_eMPMPdeYT77OFNIXsnmyClpb1SaCc4l3LES1hnxO96KkeCo01-hfWL2kMstRgzHayyfnVH6EaZFVdVoUrJiSrzwd-zEFT8-4PjkB23iXV6GgzPvx-DinITer-B77PyxSWZwFESqRZ6R8PvKGuwHe5T2E0gmyTCIkgNK12FT6BD4MvlC0EfQh4iu62KL30b4GVxFb6Ybx_u5w5s623uoSkgiKG9FCkmvUq8WuHdkoeoosowiGGVxV43bgveDGv4sVzoJJB4Dme6uTzI9tMgmgCwDTkflbvdUdK0juia7ZODnKf59iy7OT3dF15Y1yrQFIePPPXqDVNx73afYqeH8uhMI5V0O8NkXEg-gp4_IeAX9XpAps9URM62leOrjoBeubfU-_Wirr6d6L6n0Mzt6S7QhTJCnVxLhlITB1-Dc_4RawwQ1vikwryikSJkJfkNiYTK82dTRcKWVd7UTJn6wqRLfHENBpvGS2ey-TQku7Kbc7_BDDOStfNwKxXhZBs-BNamsSLWkPBPbNr8XYk9OTrbONKfpzKCcMcEd99FebHg_chizSmq8jhxW6TyaZ6nj1heMUxU4UfAFwybMrHHxD43PSE0=" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-100-I001 | Interface | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-100-E001 | Enhancement | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-100-F001 | Form/Report | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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

    subgraph E2E100CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E100CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E100CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E100CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E100CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E100CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E100CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E100CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlNFq2zAUhl9FqOQuaxU7TjNDB7Zjs0I6wrxug3kYxT5ORGXL2PKaNM27T7LdpC2kUDZdCOn_jz4dHSHtcCJSwDYeDHasYNJGuwjLNeQQYRtFeElrNRqqUQ1JUzG5ncMf4J3JhXhy2yXfacXokkOtbcXJRCFD9tCjRuNy0wVrPaA549vOCWElAN1eD5GjAAq-b6O4uE_WtJI9ranhhm5-sFSutZJRXoOOW8ucz-kSeLutrJpWLdSxwpImrFhpeUy0WNHi7plokf0e7QeDqDjshb65UYFUSzit6xlkiJalKzYoY5zbZ641C4JgWMtK3IF9RsjlpTvppx_udWq2UW6GieCi0rY5s17zSk7lEehN_Yn38QA0p1Pf9F4CzSNw5Fq-QV4BQfAjLwhcy7UOPM8jqp1McDLRdlR0xLpZriparpFv-CNCvMV8EUO8ip2HpoJ4QWn4K8JRY0zIKGoyIGrr89U5am2k7Qj_7ki6payCRDJRoPnXo3pAOy36p3-roS1HjxXBtu2u5N0iKNI-O7nlcDq1f6rn2-cP43H82fnixAYxzLYE6dRMVZ9S63khwosx0nFIx72_Fjd-GJuEPJVDTZGavrciL5L9D0V5E3919emxT3fWHhFdIGdxrfqAcfXsH0_fFx7iHKqcshTbu-77UL9QChltuFQfAKaNFOG2SLDdPmnclCmVMGNU3VHeifu_tEN5Jg==" title="View full diagram">&#128065; View Full Diagram</a></div>


> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>


<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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

    subgraph E2E100FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E100FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E100FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E100FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E100FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E100FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E100FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E100FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlNFq2zAUhl9FqOQuaxU7TjNBB3Zis0I6wrxug3kYxT5ORGXL2PKaNM27T7LTpC2kUDZdCOn_jz4dHSFtcSJTwBT3eltecEXRNsJqBTlEmKIIL1itR309qiFpKq42M_gDojOFlE9uu-Q7qzhbCKiNrTmZLFTIH_aowbBcd8FGD1jOxaZzQlhKQLfXfeRqgIbv2igh75MVq9Se1tRww9Y_eKpWRsmYqMHErVQuZmwBot1WVU2rFvpYYckSXiyNPCRGrFhx90x0yG6Hdr1eVBz2Qt-8qEC6JYLV9RQyxMrSk2uUcSHomedMgyDo16qSd0DPCLm89Eb76Yd7kxq1ynU_kUJWxranzmteKZg6AidjfzT5eADa47FvT14C7SNw4Dm-RV4BQYojLwg8x3MOvMmE6HYywdHI2FHREetmsaxYuUK-5Q8ICeazeQzxMnYfmgriOWPhrwhHjTUig6jJgOitz5fnqLWRsSP8uyOZlvIKEsVlgWZfj-oB7bbon_6tgbYcM9YESmlX8m4RFOk-O7URcDq1f6rn2-cP42H82f3ixhax7LYE6dhOdZ8y53khwoshMnHIxL2_Fjd-GNuEPJVDT5GevrciL5L9D0V5E3919elxn-60PSK6QO78WvcBF_rZP56-L9zHOVQ54ymm2-770L9QChlrhNIfAGaNkuGmSDBtnzRuypQpmHKm7yjvxN1f12h5Pg==" title="View full diagram">&#128065; View Full Diagram</a></div>


> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>


#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
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

<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

Project delivery milestones for E2E-100 RICEFW objects:

| Phase | Planned Start | Planned End | Status | Notes |
|-------|---------------|-------------|--------|-------|
| Functional Specification (FS) | Per project plan | Per project plan | In Progress | Tower-level FS schedule |
| Technical Design (TDD) | FS + 2 weeks | FS + 6 weeks | Planned | Dependent on FS completion |
| Build & Unit Test (TUT) | TDD + 1 week | TDD + 8 weeks | Planned | Includes S/4 + Middleware |
| Functional User Test (FUT) | Build + 1 week | Build + 4 weeks | Planned | Tower-led validation |
| Go-Live (Release 2) | Per release plan | Per release plan | Planned | End-to-End Integrated Processes release |

> *Detailed object-level timelines will be auto-populated from the Smartsheet Object Tracker via API integration.*

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 7.2 RAID Log

Standard RAID items for E2E-100 (End-to-End Integrated Processes):

| # | Category | Description | Status | Owner | Priority |
|---|----------|-------------|--------|-------|----------|
| 1 | Risk | Data migration completeness — validate all legacy R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box data maps to S/4 target structures | Open | Tower Architect | High |
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
*E2E-100 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*
<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-100 — R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box</span></div>
</div>
