<div class="page-section">
<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">End-to-End Integrated Processes (E2E) Tower<br/>
  Capability E2E-70 · Procure to Pay</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **E2E-70 R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte** within the IAO program. It includes 4 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | End-to-End Integrated Processes (E2E) |
| **Process Group** | Procure to Pay |
| **Capability** | E2E-70 - R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte |
| **Release** | Release 2 |
| **Total Systems** | 2 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 2 Pending IAPM |
| **RICEFW Objects** | Pending — Smartsheet Object Tracker API integration |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 1 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | End-to-End Integrated Processes |
| **L1 Process** | Procure to Pay |
| **L2 Capability** | E2E-70 - R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | End-to-End Process Integration | Enable cross-tower integrated processes spanning procurement, manufacturing, and fulfillment | IDM 2.0 Process Excellence | High |
| 2 | Intel Foundry Business Enablement | Stand up foundry-specific business processes for external customer engagement | Intel Foundry Services | High |
| 3 | Process Visibility & Monitoring | Provide end-to-end process visibility across tower boundaries with integrated monitoring | Operational Excellence | Medium |
| 4 | E2E-70 Process Migration | Migrate R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte business processes and 2 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Cross-Functional / End-to-End | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| E2E Process Cycle Time | Per process SLA | End-to-end transaction completion within defined SLA per process | Varies by process | E2E Process Owner |
| Cross-Tower Integration Success | > 99% | Transactions completing across tower boundaries without manual intervention | 92% (current) | Integration Lead |
| Process Exception Rate | < 2% | Transactions requiring manual exception handling | 8% (current) | Operations Manager |
| E2E-70 Migration Completeness | 100% flow chains validated | All 1 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **4 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for E2E-70 R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte.

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products) | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products) | Boundary Apps, External Partners/
Supplier, OSAT, SAP S/4 (IP & IF) | 23 | 10 |
| 2 | E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry | E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry | Boundary Apps, External Partners/
Supplier, SAP S/4 (IP & IF) | 27 | 10 |
| 3 | E2E-70_R3_CFIN | E2E-70_R3_CFIN | Boundary Apps, CFIN, MBC, SAP S/4 (IP & IF) | 15 | 10 |
| 4 | E2E-70_R3_SAP_Transportation_Management | E2E-70_R3_SAP_Transportation_Management | Boundary Apps, External Partners/
Supplier
, SAP S/4 (IP & IF) | 12 | 6 |

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.2 Business Process Diagrams


#### BUSINESS ARCHITECTURE — 3.2.1 E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products) — E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products)

**Swim Lanes**: Boundary Apps · External Partners/
Supplier · OSAT · SAP S/4 (IP & IF) | **Tasks**: 23 | **Gateways**: 10

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
        n1["Organize Transport-Intel Routing Guide (IRG)"]
        n2["ReadSoft Validation/Exception Handling based on rules setup"]
        n3["Incoming invoice/ B2B/OpenText/Web suite"]
        n4["Manual invoices through OCR"]
        n28{{"fa:fa-code-branch exclusiveGateway"}}
        n29{{"fa:fa-code-branch B2B/Manual?"}}
        n36{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier
        n15["Receive Manufacturing Order"]
        n16["Update Purchase order Information (Weekly)"]
        n17["Complete Manufacturing against Manufacturing Order"]
        n18["Receive PO at Supplier End"]
        n19["Select Carrier via Intel Routing Guide Hosted Collaboration Portal"]
        n20["Ready to Ship Manufacturing Inventory (Substrates)"]
        n21["Receive Order Shipment from Supplier"]
        n22["Supplier Invoicing"]
        n24(["fa:fa-stop Purchase Order Updated"])
        n37{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph OSAT
        n23["Receive Physical Receipt at OSAT Location"]
        n25(["fa:fa-stop Continued Manufacturing Process at OSAT (Refer E2E-57 OSAT Manu. Process)"])
        n35{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n5["Create Purchase Requisition (Feed from MAAPS)"]
        n6["Create Purchase Order"]
        n7["Trigger GTS Check"]
        n8["Calculate Taxes"]
        n9["Create Inbound Delivery"]
        n10["Trigger TM Embedded"]
        n11["Receive Goods Receipt(Virtual)"]
        n12["Evaluate Receipt Settlement (ERS) Self-Billing"]
        n13["Post Supplier Invoice"]
        n14["Publish Purchase Order"]
        n26["E2E-70 R3 SAP Transportation Management"]
        n27["E2E-70 R3 CFIN"]
        n30{{"fa:fa-code-branch Invoice Accepted?"}}
        n31{{"fa:fa-arrows-alt parallelGateway"}}
        n32{{"fa:fa-arrows-alt parallelGateway"}}
        n33{{"fa:fa-arrows-alt parallelGateway"}}
        n34{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n16 --> n24
    n6 --> n31
    n31 --> n8
    n17 --> n20
    n9 --> n32
    n32 --> n10
    n23 --> n35
    n11 --> n12
    n30 -->|"No"| n22
    n28 --> n2
    n35 --> n25
    n3 --> n36
    n32 --> n23
    n12 --> n28
    n5 --> n6
    n15 --> n17
    n21 -->|"3B2 - WebSuite /(Web ASN)"| n9
    n10 --> n26
    n29 --> n4
    n29 --> n3
    n2 --> n30
    n30 -->|"Yes"| n13
    n13 --> n27
    n14 --> n34
    n34 -->|"3A4 or 3A19WebSuite
 during IAO
E2Open(post IAO)"| n18
    n18 --> n19
    n19 --> n1
    n33 --> n14
    n8 --> n33
    n31 --> n7
    n7 --> n33
    n1 --> n37
    n20 --> n37
    n37 --> n21
    n35 --> n11
    n22 --> n29
    n36 --> n28
    n4 --> n36
    class n24 endEvt
    class n25 endEvt
    class n26 startEvt
    class n27 startEvt
    class n28 gateway
    class n29 gateway
    class n30 gateway
    class n31 gateway
    class n32 gateway
    class n33 gateway
    class n34 gateway
    class n35 gateway
    class n36 gateway
    class n37 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWFtv2kgU_isjV1mIBBtfMfCwKyCQIjUNwrTVquzDYI9hlMHjHY8JbMp_3zPGw8Ulq26Xhwh_nO_cz5lxXo2QR8ToGjc3rzShsotea3JF1qTWRbUFzkitgQ7AZywoXjCS1ZRMzBMZ0L8LMctNt0pMYSO8pmyn0IAsOUGfxg3UAyJroAwnWTMjgsa1Ri0VdI3FbsAZF0r6HWnHZlxYK3_qcxERcRIwTd8KPaAympAT7Piu744ULyMhT6ILpbEXt-OwtlfOMf4SrrCQhft5Rh7x9guN5AqeY8wyAjIruWYf8IIwFaMUucLCXGx0Mmim7CSQsCDFIU2WgLsmQAInzyfIM_d7tL-5mSdHo-jDdJ4g-IQMZ9k9iVEmAR5uJIopY9137qA38sxGJgV_Jt139tC_d-xGqCLpQuhmQyW3-ULociW7C86iUrT5omLo2um2IbZd22yIHfyt2CJJdLI0aNltu3201PetgTXQluI4_l-WIK9ihrPn0tbQGdmj-6Mty2t5A_N7fTrMe9fvWdU8EbGhITlTOhqNnOEpVcOWZ5lvK-2PnJY5qChdYkle8O6ksDNwjwpHnj-y_DcVHuxVvcwXE8FDrdAZeiPvqNDvW6Oe_aZCt2e57dJD0LMUOF2hPs-LXka9NM0Ov6lPYn2dG09iiROYPTSDvstSLmRznEjC0JTnEloQPeQ0Iqg-nj7czo0_z9g2sKcERwGPJfqMGY2wpDy5G25Dkqpv6D1OIqZ0qNmPECAih5mHMsg8vVTmgLJxEvK1EqfJhkOZ7lDf7t89pSSZka28-0IWEBKV5JLpAvMRJzlmmpchuRI8X67Q02Ba8bn9-jo3YtyNcVPtquYCog5XiGxDlmd0Qx4OxZwb-_05rXOdpvw72P69wnBaJwYWgr9kTcwkePiWHRirStWGW0lEAmFNYLgTIrI7FORpyigR5zX0ijKEBJQi5UuMQ5kLlcYntfMu47daIP0phUoRNMkFrJOMoGI3onESc7EuSojqXwh5ZrtKwS0fyAO-ThmRVVt4iWmSyR_woH3m7-QJYXmMCg0hB5fCHRAOCCOhRANIoxLaUIyudeh7nkloMtjXDC-4OAQygX7GrNIDZtm4OyQ5ClY0rXg9TjYkkRzmpR7kC5g0yFZWbX7rLIwizELTGogoFnx9KtUlTQ3NMd5x0a9gsiLk1r_q3skkT0-VOhg61E-l6va84_z_3XFPQW927odzXqrVLqMhdGMBpFIVTsmjDzwscl2JwavEMICDgCY5VOgy2WrTkSw7qqtPSaxawR42Pf8AKcKvWvC2GrZ3NewUC8wYYT8QddCboODOhRU3Qb-g8ehcuxqugSAX4zIlf-U0o4dBGRGIqCj4Y683CSpd0rpCvzITaq5mgi6XEPjDLECDFQmfL0XU1AwwC3OmlM3wlmSXAp2TqXGyUAsf3RMGlRO7ykyZZ9Zmj2i4XpAoItXJO-_vB86jTBe-_pkKCRuvuhxUZw83mOXKBd0kAZGSkWIq6sNpcAsAi5t9ONi-63pLddsEhhhV5qOy7y218Cf5gtFs9a9ZtVX2VR_5Jpo6RZmPZ9xhO0Bj4WXhXYXpXzAHo_HHymllXj8PSodRL1RHIIm-OxWs_9asB5L9MyTnZ0juT84SnCuo2fxNra4SKJ-d8gYGXw5AWxP8klBefpJOSbA1wT4AlhawnVLC0ypKldaRYirg29z4yOfGN7VsNbVdGtOCXvmsVWnVrYpx29G2NKD9LzVoglU-W742aZW-OH2gIri7BOrqgu7q6hrTCz7eFi52NN8s9WuFdpkPt_KsHSr9ccxq7H-oxfBNjZNWXQZna9cst-Rq3Y6rfe25cBlATs_qaIdBJCpPxd7TPBna6jpWT9WYAnAIwjoWtcyzdQyr9PrYBaUvljZdEhyn0ibaV7_ye_mzc0yzWQEc3VdWpdaWBmxdSu2k06rU1r3shuJerlq7fPW5RL2raOv4SnaJ-2_gbf0WcQl3rsJQ66uwdR22r8POddi9DnvX4dZ12New0TDWBG6VNDK6r0bx6g__HohIjHMmjX3DwLnkwS4JjW7ximzkxd3mnmI4m9cHcP8P6dQBLA==" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### BUSINESS ARCHITECTURE — 3.2.2 E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry — E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry

**Swim Lanes**: Boundary Apps · External Partners/
Supplier · SAP S/4 (IP & IF) | **Tasks**: 27 | **Gateways**: 10

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
        n1["Organize Transport-Intel Routing Guide (IRG)"]
        n2["ReadSoft Validation/Exception Handling based on rules setup"]
        n3["Incoming invoice/ B2B/OpenText/Web suite"]
        n4["Manual invoices through OCR"]
        n35{{"fa:fa-code-branch exclusiveGateway"}}
        n36{{"fa:fa-code-branch B2B/Manual?"}}
        n44{{"fa:fa-arrows-alt inclusiveGateway"}}
    end
    subgraph External Partners/ Supplier
        n17["Receive Manufacturing Order"]
        n18["Update Purchase order Information (Weekly)"]
        n19["Complete Manufacturing against Manufacturing Order"]
        n20["Receive PO at Supplier End"]
        n21["Select Carrier via Intel Routing Guide Hosted Collaboration Portal"]
        n22["Ready to Ship Manufacturing Inventory (Substrates)"]
        n23["Receive Order Shipment from Supplier"]
        n24["Supplier Invoicing"]
        n25["PO communication to 3PL"]
        n26["Send ASN Copy to 3PL"]
        n27["Physical Receipt at 3PL"]
        n30(["fa:fa-stop Purchase Order Updated"])
        n31(["fa:fa-stop PO Received"])
        n32(["fa:fa-stop PO Communication Received"])
        n39{{"fa:fa-code-branch exclusiveGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n5["Create Purchase Requisition"]
        n6["Create Purchase Order"]
        n7["Trigger GTS Check"]
        n8["Calculate Taxes"]
        n9["Create Inbound Delivery"]
        n10["Trigger TM Embedded"]
        n11["Receive Goods Receipt Stock Unrestricted"]
        n12["Post Supplier Invoice"]
        n13["Evaluate Receipt Settlement (ERS) Self-Billing"]
        n14["Remain to Unrestricted stock"]
        n15["Move Inventory to Blocked Stock"]
        n16["Publish PO"]
        n28(["fa:fa-stop endEvent"])
        n29(["fa:fa-stop Inventory Moved to Blocked Stock"])
        n33["E2E-70 R3 SAP Transportation Management"]
        n34["E2E-70 R3 CFIN"]
        n37{{"fa:fa-code-branch Invoice Accepted?"}}
        n38{{"fa:fa-code-branch eCoC Approved in MQCS"}}
        n40{{"fa:fa-arrows-alt parallelGateway"}}
        n41{{"fa:fa-arrows-alt parallelGateway"}}
        n42{{"fa:fa-arrows-alt parallelGateway"}}
        n43{{"fa:fa-arrows-alt parallelGateway"}}
    end
    n18 --> n30
    n6 --> n40
    n40 --> n8
    n22 --> n39
    n9 --> n41
    n41 --> n10
    n37 -->|"No"| n24
    n35 --> n2
    n5 --> n6
    n21 --> n1
    n17 --> n19
    n39 --> n23
    n23 -->|"3B2 - WebSuite /(Web ASN)"| n9
    n1 --> n39
    n10 --> n33
    n2 --> n37
    n37 -->|"Yes"| n12
    n12 --> n34
    n20 --> n31
    n19 --> n22
    n38 -->|"Yes"| n14
    n11 --> n38
    n13 --> n35
    n25 --> n32
    n38 --> n13
    n38 -->|"No"| n15
    n8 --> n42
    n42 --> n16
    n16 --> n43
    n43 -->|"3A4 or 3A19WebSuite
 during IAO
E2Open(post IAO)"| n20
    n43 -->|"E2 Open / OpenText"| n25
    n43 --> n21
    n26 --> n27
    n41 -->|"OpenText"| n26
    n14 --> n28
    n15 --> n29
    n36 -->|"B2B"| n3
    n36 --> n4
    n24 --> n36
    n40 --> n7
    n7 --> n42
    n44 --> n35
    n3 --> n44
    n4 --> n44
    n27 --> n11
    class n28 endEvt
    class n29 endEvt
    class n30 endEvt
    class n31 endEvt
    class n32 endEvt
    class n33 startEvt
    class n34 startEvt
    class n35 gateway
    class n36 gateway
    class n37 gateway
    class n38 gateway
    class n39 gateway
    class n40 gateway
    class n41 gateway
    class n42 gateway
    class n43 gateway
    class n44 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWF1z4jgW_Ssqd_UmXQUVf4GBh90CBzJUdTpMnJ6urWEfhC2DK8LyyDKBTee_75VtGaw4NTWzPKTiwz3nfuheSebVCFlEjInx-fNrkiZigl6vxI7sydUEXW1wTq56qAJ-wzzBG0ryK2kTs1QEyX9LM8vNjtJMYgu8T-hJogHZMoK-L3toCkTaQzlO835OeBJf9a4ynuwxP_mMMi6tP5FRbMalt_qrGeMR4WcD0_SscABUmqTkDDue67kLyctJyNKoJRoP4lEcXr3J4Ch7CXeYizL8Iif3-PgjicQOnmNMcwI2O7GnX_GGUJmj4IXEwoIfVDGSXPpJoWBBhsMk3QLumgBxnD6foYH59obePn9ep41T9PVxnSL4hBTn-S2JUS4Anh8EihNKJ59cf7oYmL1ccPZMJp_suXfr2L1QZjKB1M2eLG7_hSTbnZhsGI1q0_6LzGFiZ8ceP05ss8dP8FfzRdLo7Mkf2iN71HiaeZZv-cpTHMf_lyeoK3_C-XPta-4s7MVt48saDAe--V5PpXnrelNLrxPhhyQkF6KLxcKZn0s1Hw4s82PR2cIZmr4musWCvODTWXDsu43gYuAtLO9DwcqfHmWxWXEWKkFnPlgMGkFvZi2m9oeC7tRyR3WEoLPlONuhGSvKXkbTLMur7-QntX5fGw98i1OYPfQEfZdnjIv-MhWEokdWCGhBdFckEUHXy8e7L2vjPxdsG9iPBEcBiwX6DdMkwiJh6c38GJJM_od-wWlEpYac_QgBwguYeVgGUWRtMQfElmnI9tI8SQ8MlukGzezZzUNG0idyFDc_yAZSSgRpM11g3uO0wFTxciR2nBXbHXrwHzU3g9fXtRHjSYz7cq_qbyDrcIfIMaRFnhzIXbWYa-Pt7ZI27KbJ-Crf_9IYrntmYM7ZS97HVECEH_mBsdJWbX4UhKeQ1gqGOyU8v0FBkWU0IfxyDb1yGUICokjGEuNQFFyW8UHuee38rRFYf89gpQhaFRy2k5ygcm9EyzRmfF8uIbr-QcgzPWkLbo2B7LN9RonQfeEtTtJc_HkEtnkR7-oBYdFkheZQg7ax7NCAUBIK5EMZpdEhwairQ39huYAmg_2a4g3jVSIr6GdMNVHVuCckGAp2SaZFvUwPJBUM5uU6KDYwaVCtXG9-5yKNMs1SaQ9EFHO2Py9Vmya7tcl3WfYruNSMBmAEpYFp2BdpElapQKzO6qtmOSzrk0ZoGnyD1LNTt5nskdXulIMWlE1GnQlZ-XeWjnn9u2rbXLDs3CRVjlXryFX6csmydNYDqmvzztR-b-q38vyIOP6rk_t-ooLpCgU3LmxmK_QPtFxc6sua-5y0BuOR_FEkeSLDapdp2GHc0euy7E882W6hcndPAfJ3JHxum8h59DENCyrFnvCR5G2D8dnVMt3IjRzdEgr58pM2neaFt6d7NN9vSBQRbaIs66Jv7xiL8qYfAsHCZ_Q95QRaPgnFO6qcmxVMGdIaWNuQLTka8wOmhQy6USdCUFLOx_X8MfgCAI37Mzji3vW_5ZYx7mFHke18GRHcdJheQksu3T07kIvBBdqMgiUwgg6GXL9VsaFJvoMG1IZlpHVoeeEBXa0h7bFmd_Yug4m6Ymg1dFkme973TPTolL3ZHMHVJMCuhLdlybQhdVtMf7H8phl43bNSLxeahvKEJpF-aDmjD2bMZ768O_AyL1iV-1_9QD_wzM4DL8McU0po97nqWn-HZP8dkvPXSM3mAUcm6vf_KbfGGhhWz656ds0KGNXPtl0TxjUwrgmWIlgVYCkFx5PAz7Xxja2Nn_KUUF8MKku7fq4fh8qTElKhevWz8uzUrm1HMZzakzODKBFcqQJ5o0I31_J2BYfIlzIAxbe0TKw6VafRq589PZN_y33sp9w0FFWZqtxspdVEr4JVFGekiymupQJTNbecGhgo9bpUTltMWurqddEtRa0NXcV068gtVXZLdYCScpuqTl24TSFnao1VacEkqq8V04d1OrflffY6k9soAFW5bVMXmttI2qEbpK6_leGgZSg7QOVbx2R7rSYDqbZAk4Nb2zcVVK3W9M6wFoBLbsl1Wl-AB-W6lnKG2kCoUDy9oK62WHUyrlJ0tWdb9fXl-5yMvX4ZbaPjLtQxO1GrE7U7Uad5zW7j7gf4QL0ZtuFhN-x1w6NueNwJQ-E7Yasbtrthpxt2FWz0jD2BN4UkMiavRvlzDvzkE5EYF1QYbz0DF4IFpzQ0JuXPHkZRXhpvEwy3sH0Fvv0PNTSFTQ==" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### BUSINESS ARCHITECTURE — 3.2.3 E2E-70_R3_CFIN — E2E-70_R3_CFIN

**Swim Lanes**: Boundary Apps · CFIN · MBC · SAP S/4 (IP & IF) | **Tasks**: 15 | **Gateways**: 10

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
        n16(["fa:fa-stop Payment Data Updated"])
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
        n18(["fa:fa-stop Memo Record Created"])
        n19(["fa:fa-stop APP Doc Reversed"])
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
    subgraph SAP S/4 (IP & IF)
        n17(["fa:fa-stop Payment Details provided back to Source System (IP/IF)"])
        n20["E2E-46A R3 Direct procurement with Planning Integration - AT"]
    end
    n12 --> n3
    n3 --> n28
    n4 --> n18
    n5 --> n21
    n21 -->|"No"| n23
    n7 --> n22
    n23 --> n6
    n25 --> n5
    n24 -->|"No"| n26
    n9 --> n19
    n10 --> n29
    n26 --> n9
    n29 --> n11
    n28 --> n4
    n11 --> n27
    n27 -->|"Reversal"| n26
    n2 --> n16
    n6 --> n14
    n29 --> n2
    n8 --> n25
    n13 --> n12
    n29 --> n17
    n20 --> n13
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
    class n16 endEvt
    class n17 endEvt
    class n18 endEvt
    class n19 endEvt
    class n20 startEvt
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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlV1uP4jYU_itWVlNmJejmSoCHVtyyQlpGaNhtVXX6YBJnsCbEyHFg2Fn-e48TO5CQeeiWB4hPvvOd-yF5M0IWEWNk3N290ZSKEXrriC3Zkc4IdTY4I50uKgV_YE7xJiFZR2Jiloo1_V7ALHf_KmFSFuAdTU5SuibPjKBviy4ag2LSRRlOs15GOI073c6e0x3mpylLGJfoD2QQm3FhTd2aMB4RfgGYpm-FHqgmNCUXseO7vhtIvYyELI1qpLEXD-Kwc5bOJewYbjEXhft5Rpb49U8aiS2cY5xkBDBbsUu-4A1JZIyC51IW5vygk0EzaSeFhK33OKTpM8hdE0Qcpy8XkWeez-h8d_eUVkbRl8enFMEnTHCWzUiMMgHi-UGgmCbJ6IM7HQee2c0EZy9k9MGe-zPH7oYykhGEbnZlcntHQp-3YrRhSaSgvaOMYWTvX7v8dWSbXX6C74YtkkYXS9O-PbAHlaWJb02tqbYUx_H_sgR55V9x9qJszZ3ADmaVLcvre1Pzlk-HOXP9sdXME-EHGpIr0iAInPklVfO-Z5nvk04Cp29OG6TPWJAjPl0Ih1O3Igw8P7D8dwlLe00v882Ks1ATOnMv8CpCf2IFY_tdQndsuQPlIfA8c7zfognLi15G4_0-K-_JT2r9_WQ8kpDQA0EBTQiiKZpA9z0Z_1yhbEB920cQJVrh046kAj2SHRUCpyGpQ63-PYBjPIpxLxNsXynMsMCoJIlA5WOpA63U8HQaLB6u-Bxgm7-SML-2nad1oy6AppxI_8arJVqSHQMHQ5j4Os4DnMwryTI0mS4rwgkW4RaGDS4yEiEGOcgzWAsAe8xhRdVZ-sDymaSEa3uaRiawDvVlepn0XTCZes4OhNchA-k745yEoiBT1xScuOUbFuUCjkxaXqEZ9MhDvtsQjnAaXQeOZiQhkqVRHhMYAgLhaq8zFOBQMGiNezDflXnpouVkipYM9jfjHxsEZcccKDmCIjgYVeF_Yc8NrH2dKQ2DAuxZhpMG1il49wkNJXid7-ESwlqkBwbzilYsE1ChhtKg0WzXCSgb4qrXSpVhQ0WnUaW1ibettzeNl39tvQ0sZ8jeEqc5TlRN4eKByK6CCfv9yTifrwnsdgLVDdEN3mnHk9cwgaY8kM_lsmmque1qUwzNTHRXtZjzfs5c_-fU_Ha1MvmQRsbhel-OKJT7xtvBRR9zzo5ZDycC7THHSUKSd4wOf0LJMVuVaPpefLebDIbouvHkklrmiaA9uWChImkq5_xABYzeFtq7J1hP_jYnzvvvirfOrMcrtP7kovvFCv2CFkFtJvz3djYRMOIZkp1KIxj1DQ5f5Cpbs5zDUK5PmSA7yflJMjYmR66auT3vuf0xenTQjBY7ThY356TgP1IBeyjBaSqX7yIVBJwtVl8Pjb_eRgMbBfV6v0F11Nkpj_ZAnd3ybOmzp-6rpwC4kIIfT8YDezJ-yGFTN3wFtDVQMff1WTF5-uw2iDRwqDwYao9NxawFdr8UVGetUfk4KAWuZrAUg68BvrKtp6bugUqRpc_KnuU2DOpQlTlbh2ap0C276WHlgIrJcppp_Uv-V4IzGqnlq_Hi4VfTtNE9tFYvYTiSjzbkYwG2KstuHW61w2t5KtJwWRhlKjShoxzV7WDbDT-r-ld3dD2r7KvCW-Zt9htmHbPZHNqMc_18J0ujHqHrUr9VOmiVDtukUBf9GlCXW_oJtS6228VOu9htF3vt4n672G8XD9rFw1YxVFWJja6xI3yHaWSM3ozitRJePSMSY1iXxrlr4Fyw9SkNjVHx-mXkxfPnjGLYM7tSeP4Xr56AuA==" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### BUSINESS ARCHITECTURE — 3.2.4 E2E-70_R3_SAP_Transportation_Management — E2E-70_R3_SAP_Transportation_Management

**Swim Lanes**: Boundary Apps · External Partners/
Supplier
 · SAP S/4 (IP & IF) | **Tasks**: 12 | **Gateways**: 6

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
        n13(["fa:fa-play Process Initiated Based on Rate/Charges Available"])
        n14(["fa:fa-play Events Published"])
        n21{{"fa:fa-arrows-alt parallelGateway"}}
        n22{{"fa:fa-arrows-alt parallelGateway"}}
    end
    subgraph SAP S/4 (IP & IF)
        n3["Generate Freight Unit (TM)"]
        n4["Create Freight Order (TM)"]
        n5["Perform Carrier Updates and Calculate Charges"]
        n6["Execute Freight Order (TM)"]
        n7["Post Freight Settlement Document (TM)"]
        n8["Create Service PO for FSD (TM)"]
        n9["Post SES with Auto Release (TM)"]
        n10["Create Cost Distribution/Agency Business Document (TM)"]
        n15(["fa:fa-stop TM process ended"])
        n16["E2E-46A R3 Direct procurement with Planning Integration - AT"]
        n18{{"fa:fa-code-branch exclusiveGateway"}}
        n19{{"fa:fa-code-branch exclusiveGateway"}}
        n20{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n3 --> n4
    n5 --> n18
    n7 --> n8
    n19 --> n5
    n6 --> n20
    n4 --> n19
    n9 --> n10
    n10 --> n15
    n11 --> n21
    n13 --> n11
    n17 --> n1
    n14 --> n12
    n12 --> n22
    n22 --> n17
    n21 --> n17
    n22 --> n2
    n1 --> n20
    n21 --> n19
    n2 -->|"Event Update"| n18
    n16 --> n3
    n18 --> n6
    n8 --> n9
    n20 --> n7
    class n13 startEvt
    class n14 startEvt
    class n15 endEvt
    class n16 startEvt
    class n17 gateway
    class n18 gateway
    class n19 gateway
    class n20 gateway
    class n21 gateway
    class n22 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVttu2zgQ_RVCRdYtYCeiLpbjhwV8UxGgQY0o2X2o94GWKJsoTQkk5cum_vcd6uJbnMW264cgczRzZuZohtSrFWcJtfrWzc0rE0z30WtLL-mKtvqoNSeKttqoAv4gkpE5p6plfNJM6Ij9XbphL98aN4OFZMX4zqARXWQUvTy00QACeRspIlRHUcnSVruVS7YicjfKeCaN9wfaS-20zFY_GmYyofLoYNsBjn0I5UzQI-wGXuCFJk7ROBPJGWnqp700bu1NcTzbxEsidVl-oegj2f7JEr0EOyVcUfBZ6hX_QuaUmx61LAwWF3LdiMGUySNAsCgnMRMLwD0bIEnE9yPk2_s92t_czMQhKfryNBMIfjEnSo1pipQGeLLWKGWc9z94o0Ho222lZfad9j84k2DsOu3YdNKH1u22EbezoWyx1P15xpPatbMxPfSdfNuW275jt-UO_l7koiI5Zhp1nZ7TO2QaBniER02mNE3_VybQVT4T9b3ONXFDJxwfcmG_64_st3xNm2MvGOBLnahcs5iekIZh6E6OUk26PrbfJx2GbtceXZAuiKYbsjsS3o-8A2HoByEO3iWs8l1WWcynMosbQnfih_6BMBjicOC8S-gNsNerKwSehST5Eg2zopxlNMhzVT0zP4G_zawnGlO2pncRvFf0INJMrohmmUBMoBGRklEJ8DoD2dCTWYqYcVZ63I2ZygtNb29vZ9ZfJ7QO0E7WVGhU5AmIoxCRFMkqUWKIPz8_n4fg4PV1ZqWkn5KOOUM6c9iCeInoNuaFgrDPlcgza7-vwqDciy4nW02lIBxNYRkEleoORUWec9PBaSrTdUihkCdT290IVmoBNT4ITYFIZ1IhVyYoB5ZdMzFoVjg2dkGBZJNlyUXxpuFaq4sn7sdvTVs5hxkx75Uqk4xpUBGKGMKxmCDQ21RzKGawJoybAxL4Pp0SeheEpc4KTYs5Z2pJkwt_Bx91hQKzjeoQrk1vhHPK36haBTk_F_T2VUSDKYruPPTxYYp-Qw_haUkuNPCZwvsBGhTK8mhAL6AH-vj8-OlcP88IK-mp51dzkF9x9cF1SqWZ38PcvjTjB6M9IjwuuGGqNT4P75qZ3dK4-A-pApMqU_rgGFGtOdxqMPHjLC7Kf96G9Y7NRPVUTb8iKBiF0fiK_32TJppEaMP0Eg0KncEIcgozcyUA28cMIxMIC6olmxfltg4WVMQ7NIR1EmYE_6VS7B-nTOksR8-PKK8nF172mynDpXrOpON1B-jJhbyw7LoMKWSlS1n_lBMh4Fo77Jo5ZzpocHkY9H72MKjC7n8pzLF_-egRLup0focxrU2_MnGvtoPKbkx8X9l-bXcrs7n3hFeH39d27Y6b59iugYYA45oBN0BdED4AdQkHu8nhNIBTUzSAUwM4aAB8CTQhDcVFG4eApo_S_0dzJ1RLObN-nAiFayncxu5Vdre2a_NAWAsRnFycZfPNd9A57r2D-_W3zDnafcc7aC76c7h3Hb6_CkPhV2F8HXYa2GpbKwoXM0us_qtVfkHDV3ZCU1Jwbe3bFoGTIdqJ2OqXX5pWdfGOGYEtW1Xg_h8uS5b8" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Boundary Apps | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products), E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry, E2E-70_R3_CFIN, E2E-70_R3_SAP_Transportation_Management | |
| External Partners/
Supplier | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products), E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry,  | |
| OSAT | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products),  | |
| SAP S/4 (IP & IF) | E2E-70A_Procurement_for_External_Subcontracting_-_OSAT_-_(Intel_Products), E2E-70B_Procurement_for_Internal_Manufacturing_-_Intel_Foundry, E2E-70_R3_CFIN, E2E-70_R3_SAP_Transportation_Management | |
| CFIN | E2E-70_R3_CFIN,  | |
| MBC | E2E-70_R3_CFIN,  | |
| External Partners/
Supplier
 | E2E-70_R3_SAP_Transportation_Management | |

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

    subgraph E2E70CDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E70CDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E70CDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E70CDAA_e_g_XEUS -.-> E2E70CDAD_e_g_Azure_SQL
    end
    style E2E70CDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E70CDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E70CDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E70CDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E70CDAA_e_g_MES_300 -.-> E2E70CDAD_e_g_SAP_HANA
    end
    style E2E70CDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E70CDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E70CDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlYtO2zAUhl_FMqq0SS0LLWlHJJCc20AKiJGyTSJT5CZOa-EmUeKMltJ3n50brDQMYUuRfS7_cb4TORsYJCGBGuz1NjSmXAMbD_IFWRIPasCDM5yLVV-schIUGeVrh_whrHKyJGm8ZcoPnFE8YySXbqETJTF36WMtdaSmqypY2m28pGxdeVwyTwi4vegDJASE-LaMYslDsMAZr9WKnFzi1U8a8oW0RJjlRMYt-JI5eEZYWZZnRWmNxWu5KQ5oPJfmkSqNGY7vXxiP1e0WbHs9L25rganuxUCMgOE8N0kEcJrqyQpElDHtQFdN27b7Oc-Se6IdKMpkoo_r7eBBHk0bpqt-kLAkk-6Rqe7qhTNjzWo5pJpjNGnlhtbEHA075Y501RoqO3IkYc_Hs21d1dVWzzAUMTr1xmPp9uJKMS9m8wynC2CJYyiGiQzHJ_7cR49FRnz3u3PnQYHwdxUtR0gzEnCaxC00OZp0VGb_sm5dkUgO54dAroWApmkV09c55k7FTx70ivDrKBTPMDj2iogo4pWlWBkERJAHP0vJEutbpwCDw8FZV6UqkcRhzYKvGekE0cBGcrawLUXOf2EfiS_-P3hddO2foyv0IbqXluuPFKUBLLZAbN_DuC37BmIRA2TMewjXJ9kHuSn1HsZN7IcQ7y8LTk_PnmpAZskUfAHo-kI8bcrE3fTU_VHstM4hc3H8uxfEglABJpoigG6M84upZUxvbyzgWN-sK7Ojm87Ns9XxZd9RmjIaYOnd3zrHNzv6ZGKOqyt6X4sc3xLyVhwOkmjg0IhU8tWVsbcd1Rs29FU5W_onJyev0MM-XJJsiWkItU31ExD_kpBEuGBcXOMQFzxx13EAtfJihkUaYk5MigXRZWXc_gX4yv7F" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

    subgraph E2E70FDACL_e_g_Azure_SQL[" "]
        direction TB
        E2E70FDAA_e_g_XEUS["e.g. XEUS"]:::appBox
        E2E70FDAD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCyl
        E2E70FDAA_e_g_XEUS -.-> E2E70FDAD_e_g_Azure_SQL
    end
    style E2E70FDACL_e_g_Azure_SQL fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    subgraph E2E70FDACL_e_g_SAP_HANA[" "]
        direction TB
        E2E70FDAA_e_g_MES_300["e.g. MES 300"]:::appBox
        E2E70FDAD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbCyl
        E2E70FDAA_e_g_MES_300 -.-> E2E70FDAD_e_g_SAP_HANA
    end
    style E2E70FDACL_e_g_SAP_HANA fill:#FAFAFA,stroke:#E0E0E0,stroke-width:1px

    E2E70FDAD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| E2E70FDAD_e_g_Azure_SQL

    subgraph Legend["📐 DATA ARCHITECTURE LEGEND"]
        direction LR
        L_A["Application"]:::appBox
        L_D[("🗄️ Database")]:::dbCyl
        L_E["End-of-Life"]:::eolBox
    end
    style Legend fill:#F5F5F5,stroke:#999,stroke-width:1px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqdlQ1L4zAYx79KiAzuYPPqZrezoJCt7SlU8ey8O7BHydp0C2ZNadNzc-67X9I3vbl6YgIleV7-T_p7SrqBAQ8JNGCns6ExFQbYeFAsyJJ40AAenOFMrrpylZEgT6lYO-QPYaWTcV57i5QfOKV4xkim3FIn4rFw6WMldaQnqzJY2W28pGxdelwy5wTcXnQBkgJSfFtEMf4QLHAqKrU8I5d49ZOGYqEsEWYZUXELsWQOnhFWlBVpXlhj-VpuggMaz5V5oCtjiuP7F8ZjfbsF207Hi5taYDr2YiBHwHCWmSQCOEnGfAUiyphxMNZN27a7mUj5PTEONG00Gg-rbe9BHc3oJ6tuwBlPlXtg6rt64WyyZpUc0s0hGjVyfWtkDvqtckdj3eprO3KEs-fj2fZYH-uN3mSiydGqNxwqtxeXilk-m6c4WQBLHkOzTTRxfOLPffSYp8R3vzt3HpQIf5fRaoQ0JYGgPG6gqVGnoyL7l3XrykRyOD8Eai0FDMMomb7OMXcqfvKgl4dfB6F8hsGxl0dEk6-sxIogIIM8-FlJFljfOgXoHfbO2iqViSQOKxZizUgriBo2UrOBbWlq_gv7SH7x_8Hromv_HF2hD9G9tFx_oGk1YLkFcvsexk3ZNxDLGKBi3kO4Osk-yHWp9zCuYz-EeH9ZcHp69lQBMgum4AtA1xfyaVMm76an9o9ip3UOmcvj370gFoQaMNEUAXQzOb-YWpPp7Y0FHOubdWW2dNO5ebY6vuo7ShJGA6y8-1vn-GZLn0wscHlF72uR41tS3orDHo96Do1IKV9eGXvbUb5hTV9Xs6F_cnLyCj3swiVJl5iG0NiUPwH5LwlJhHMm5DUOcS64u44DaBQXM8yTEAtiUiyJLkvj9i90fv7v" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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
| E2E-70-R001 | Report | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte operational report | Planned | SAP S/4HANA | Analytics | Medium |
| E2E-70-C001 | Conversion | Legacy data migration for R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte | Planned | Legacy ERP | SAP S/4HANA | High |

> *Pending: Smartsheet API integration to auto-populate live RICEFW data (see Build Requirements).*

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for E2E-70.This view is generated from `CurrentFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E70C_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E70C_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E70CMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E70CDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E70C_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E70CMW_e_g_Azure_Service_Bus
    E2E70CMW_e_g_Azure_Service_Bus --> E2E70C_e_g_XEUS


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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVWtP2zAU_StWUL-1IzzaQoQqpU06dUoBLQM2LVPkxretNTeJYgco0P--67jQ0IJgrpQm93Gufe6x_WglGQPLsRqNR55y5ZDHyFJzWEBkOSSyJlTiWxPfJCRlwdUygFsQximy7NlbpVzTgtOJAKndiDPNUhXyhzXUQSe_N8HaPqQLLpbGE8IsA3I1ahIXAUSTSJrKloSCTyNrVWWI7C6Z00KtkUsJY3p_w5maa8uUCgk6bq4WIqATENUUVFFW1hSXGOY04elMm49tbSxo-rdmbNurFVk1GlH6Uov86EcpwdFokFYL55bM-ZgqaPFU5rwARqRaCiCJoFKCxBgTXn17MCWTUvIUpCTVmHIhnL0hjn67KVWR_QVnr39y0rH768_WnV6Qc5jfN5NMZIWzZ9v2FibNc7IZBrPf1qgvmLbd7fY7_4HJqKK7mN7JB5gHrzCffYxKJK-gS-SUtLcqLThjAu5oAXVGvI67YcTvdoYbtE_MHjKxw4jmuMbyYGDbH2EaVFlOZgXN58QNfkdWVLKTI4ZPdtQm7uVlMBq4P0YX5yRwf_nfI-uPSdKDoSASxbOUBN83Vv_Q79qDGOJZPPbD-Mi266gJdAh8mX0h6CPoQ0DHcbDDbwL89K_CN7O1493U8U2V7D6UBcQhFLc8gbhfylerO-gapCqKrKMIRhnYTde20T2_Qh9kUsW-wCMgVb36FJNjA6wDyDrgbFLs9854zzjCa7JPRl6W4N-38OL8bJ_3TFWtSlMPUvbcn11Ccdv1niKrQvOqJiCSeznC55ALPHuePmCiDvxejC6y3Qs9pbVoqmOgH9S2-ND-aIvXU92XVPszO3lHrAHMkKNX4mA2Cfyv_rn3CZUGMWp7W1pungueUB38hriCeHyzLaHxRibvyiaIPX9bIZ4-fvxU4eWy3XmT4l-YzXjYYccYyFrZtBXw6boM7v-aTDakGlKeiW3r3wuxp6enO2eZ1bQWUCwoZ5bzaC40vBcZTGkpFF5DFi1VFi7TxHKqi8Uqc5woeJxiExbGuPoHlMNG5Q==" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### Current-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for E2E-70.This view is generated from `FutureFlows.xlsx` (1 flow hops across 1 flow chains).

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
        E2E70F_e_g_MES_300["📦 e.g. MES 300"]:::app
        E2E70F_e_g_XEUS["📦 e.g. XEUS"]:::app
        E2E70FMW_e_g_Azure_Service_Bus["🔗 e.g. Azure Service Bus"]:::middleware
        E2E70FDE_e_g_Cost_Element>"📄 e.g. Cost Element<br/><i>e.g. CSV / IDoc / JSON</i>"]:::data
    end

    E2E70F_e_g_MES_300 -->|"e.g. Direct / API / File"| E2E70FMW_e_g_Azure_Service_Bus
    E2E70FMW_e_g_Azure_Service_Bus --> E2E70F_e_g_XEUS


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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVVWtP2zAU_StWUL-1Izz6IEKVUpJOnVJAhI1NyxS58W1rzU2i2AEK9L_vOi40tCCYK6XJfZxrn3tsP1pJxsByrEbjkadcOeQxstQcFhBZDomsCZX41sQ3CUlZcLUM4BaEcYose_ZWKT9owelEgNRuxJlmqQr5wxrqoJPfm2BtH9IFF0vjCWGWAfk-ahIXAUSTSJrKloSCTyNrVWWI7C6Z00KtkUsJY3p_w5maa8uUCgk6bq4WIqATENUUVFFW1hSXGOY04elMm49tbSxo-rdmbNurFVk1GlH6UotcD6KU4Gg0SKuFc0vmfEwVtHgqc14AI1ItBZBEUClBYowJr749mJJJKXkKUpJqTLkQzt4Qx6DdlKrI_oKzN-j1OvZg_dm60wtyDvP7ZpKJrHD2bNvewqR5TjbDYA7aGvUF07a73UHnPzAZVXQX0-t9gHnwCvPZx6hE8gq6RE5Je6vSgjMm4I4WUGfE67gbRvxuZ7hB-8TsIRM7jGiOayyfndn2R5gGVZaTWUHzOXGD35EVlax3xPDJjtrEvbwMRmfu9ejinATuL_8qsv6YJD0YCiJRPEtJcLWx-od-1x7GEM_isR_GR7ZdR02gQ-DL7AtBH0EfAjqOgx1-E-Cn_z18M1s73k0d31TJ7kNZQBxCccsTiAelfLW6g65BqqLIOopglIHddG0b3fMr9LNMqtgXeASkql-fYnJsgHUAWQecTor9_invG0f4g-yTkZcl-PctvDg_3ed9U1Wr0tSDlD33Z5dQ3Hb9p8iq0LyqCYjkXo7wOeQCz56nD5ioA78Xo4ts90JPaS2a6hgYBLUtPrQ_2uL1VPcl1f7MTt4RawAz5OiVOJhNAv-rf-59QqVBjNrelpab54InVAe_Ia4gHt9sS2i8kcm7sgliz99WiKePHz9VeLlsd96k-BdmMx522DEGslY2bQV8ui6D-78mkw2phpRnYtv690LsycnJzllmNa0FFAvKmeU8mgsN70UGU1oKhdeQRUuVhcs0sZzqYrHKHCcKHqfYhIUxrv4B2zRG_Q==" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### Future-State Flow Narrative

| # | Flow Chain | Path | Interface | Freq |
|---|-----------|------|-----------|------|
| 1 | e.g. MES Route to ICOST | e.g. MES 300 → e.g. XEUS | e.g. Direct / API / File | e.g. Near Real-Time |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

<div class="page-footer"><span>Page 20</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.5 RICEFW Inventory

RICEFW objects for this capability will be auto-populated from the Smartsheet S/4 Object Tracker.

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| E2E-70-I001 | Interface | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte inbound data interface | Planned | Legacy → SAP S/4HANA | MuleSoft / CPI | Medium |
| E2E-70-E001 | Enhancement | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte custom business logic | Planned | SAP S/4HANA | N/A | Medium |
| E2E-70-F001 | Form/Report | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte operational output | Planned | SAP S/4HANA | N/A | Low |

> *Pending: Smartsheet API integration to auto-populate live RICEFW inventory (see Build Requirements).*

<div class="page-footer"><span>Page 21</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.6 Integration Patterns

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. MES Route to ICOST | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert |

<div class="page-footer"><span>Page 22</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

    subgraph E2E70CPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E70CPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E70CPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E70CPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E70CPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E70CPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E70CPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E70CPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlF1r2zAUhv-KUMld1ip2nGSGDmzHZoV0hHndBvMwin2ciMqWseU1aZr_PsnOR1tIoWy6ENL7Hj06OkLa4kSkgG3c621ZwaSNthGWK8ghwjaK8ILWatRXoxqSpmJyM4M_wDuTC3Fw2yXfacXogkOtbcXJRCFD9rhHDYblugvWekBzxjedE8JSALq76SNHARR810Zx8ZCsaCX3tKaGW7r-wVK50kpGeQ06biVzPqML4O22smpatVDHCkuasGKp5SHRYkWL-2eiRXY7tOv1ouK4F_rmRgVSLeG0rqeQIVqWrlijjHFuX7jWNAiCfi0rcQ_2BSHjsTvaTz886NRso1z3E8FFpW1zar3mlZzKE9Cb-CPv4xFoTia-6b0EmifgwLV8g7wCguAnXhC4lmsdeZ5HVDub4Gik7ajoiHWzWFa0XCHf8MfEm8_mMcTL2HlsKojnlIa_Ihw1xogMoiYDona-XF6i1kbajvDvDqRbyipIJBMFmn09qQey05J_-nea2WL0WAFs2-4K3q2BIt3nJjcczib2T8V88_BhPIw_O1-c2CCG2Z4_nZip6lNqPa9CeDVEOg7puHcX4tYPY5OQQy3UFKnpO8vxItX_UJG36NfXn572yU7b86Er5MxvVB8wrt7709mrwn2cQ5VTlmJ7230b6vdJIaMNl-rhY9pIEW6KBNvtU8ZNmVIJU0bV9eSduPsLmbZ31g==" title="View full diagram">&#128065; View Full Diagram</a></div>


> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>


<div class="page-footer"><span>Page 23</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

    subgraph E2E70FPLP_e_g_Azure_PaaS["☁️ e.g. Azure PaaS"]
        direction LR
        E2E70FPLA_e_g_XEUS["e.g. XEUS"]:::appBox
    end
    style E2E70FPLP_e_g_Azure_PaaS fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    subgraph E2E70FPLP_e_g_S_4_HANA_2023["🖥️ e.g. S/4 HANA 2023"]
        direction LR
        E2E70FPLA_e_g_MES_300["e.g. MES 300"]:::appBox
    end
    style E2E70FPLP_e_g_S_4_HANA_2023 fill:#C8E6C9,stroke:#388E3C,stroke-width:3px,color:#1B5E20

    E2E70FPLP_e_g_S_4_HANA_2023 ==>|"e.g. Direct / API / File"| E2E70FPLP_e_g_Azure_PaaS

```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtlF1r2zAUhv-KUMld1ip2nGSGDuzEZoV0hHndBvMwin2ciMqWseU1aer_PsnOR1tIoWy6ENL7Hj06OkLa4VgkgG3c6-1YzqSNdiGWa8ggxDYK8ZJWatRXowriumRyO4c_wDuTC3Fw2yXfacnokkOlbcVJRS4D9rhHDYbFpgvWuk8zxredE8BKALq76SNHARS8aaO4eIjXtJR7Wl3BLd38YIlcayWlvAIdt5YZn9Ml8HZbWdatmqtjBQWNWb7S8pBosaT5_TPRIk2Dml4vzI97oW9umCPVYk6ragYpokXhig1KGef2hWvNfN_vV7IU92BfEDIeu6P99MODTs02ik0_FlyU2jZn1mtewak8AacTbzT9eASak4lnTl8CzRNw4FqeQV4BQfATz_ddy7WOvOmUqHY2wdFI22HeEat6uSppsUae4Y2Jv5gvIohWkfNYlxAtKA1-hTisjREZhHUKRO18ubpErY20HeLfHUi3hJUQSyZyNP96Ug9kpyX_9O40s8XosQLYtt0VvFsDebLPTW45nE3sn4r55uGDaBh9dr44kUEMsz1_MjET1SfUel6F4GqIdBzSce8uxK0XRCYhh1qoKVLTd5bjRar_oSJv0a-vPz3tk52150NXyFncqN5nXL33p7NXhfs4gzKjLMH2rvs21O-TQEprLtXDx7SWItjmMbbbp4zrIqESZoyq68k6sfkLvId37g==" title="View full diagram">&#128065; View Full Diagram</a></div>


> **Legend**: <span style="background:#C8E6C9;padding:2px 8px;border:2px solid #388E3C;font-size:9pt">🖥️ Platform</span> · <span style="background:#B5DFFF;padding:2px 8px;border:2px solid #0077B6;font-size:9pt">📦 Application</span> · <span style="background:#FFB5B5;padding:2px 8px;border:2px solid #CC0000;font-size:9pt">⛔ End-of-Life</span> · <span style="background:#FFF9C4;padding:2px 8px;border:2px solid #F9A825;font-size:9pt">📋 Unassigned</span>


#### Platform Inventory

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 24</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
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

<div class="page-footer"><span>Page 25</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

Project delivery milestones for E2E-70 RICEFW objects:

| Phase | Planned Start | Planned End | Status | Notes |
|-------|---------------|-------------|--------|-------|
| Functional Specification (FS) | Per project plan | Per project plan | In Progress | Tower-level FS schedule |
| Technical Design (TDD) | FS + 2 weeks | FS + 6 weeks | Planned | Dependent on FS completion |
| Build & Unit Test (TUT) | TDD + 1 week | TDD + 8 weeks | Planned | Includes S/4 + Middleware |
| Functional User Test (FUT) | Build + 1 week | Build + 4 weeks | Planned | Tower-led validation |
| Go-Live (Release 2) | Per release plan | Per release plan | Planned | End-to-End Integrated Processes release |

> *Detailed object-level timelines will be auto-populated from the Smartsheet Object Tracker via API integration.*

<div class="page-footer"><span>Page 26</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 7.2 RAID Log

Standard RAID items for E2E-70 (End-to-End Integrated Processes):

| # | Category | Description | Status | Owner | Priority |
|---|----------|-------------|--------|-------|----------|
| 1 | Risk | Data migration completeness — validate all legacy R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte data maps to S/4 target structures | Open | Tower Architect | High |
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
*E2E-70 — Architecture Document (TOGAF BDAT) · End-to-End Integrated Processes · Generated: March 2026*
<div class="page-footer"><span>Page 27</span><span><a href="#toc">↑ Back to TOC</a></span><span>E2E-70 — R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte</span></div>
</div>
