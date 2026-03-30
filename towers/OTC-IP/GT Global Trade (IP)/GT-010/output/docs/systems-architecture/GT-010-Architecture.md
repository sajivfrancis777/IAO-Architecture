<div class="page-section">
<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">GT-010 — Manage Global Trade Master Data (IP)</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Order To Cash (IP) (OTC-IP) Tower<br/>
  Capability GT-010 · GT Global Trade (IP)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **GT-010 Manage Global Trade Master Data (IP)** within the IAO program. It includes 3 BPMN process diagram(s) in Section 3.
| Dimension | Value |
|-----------|-------|
| **Tower** | Order To Cash (IP) (OTC-IP) |
| **Process Group** | GT Global Trade (IP) |
| **Capability** | GT-010 - Manage Global Trade Master Data (IP) |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 5 Reports, 71 Interfaces, 20 Conversions, 167 Enhancements, 28 Forms, 1 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Order To Cash (IP) |
| **L1 Process** | GT Global Trade (IP) |
| **L2 Capability** | GT-010 - Manage Global Trade Master Data (IP) |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | IP Order Management Transformation | Transform Intel Products order management onto S/4 HANA with integrated pricing and ATP | IDM 2.0 Products Revenue | High |
| 2 | Customer Experience Improvement | Reduce order processing time and improve order visibility for IP customers | Customer Centricity | High |
| 3 | Returns & Rebate Automation | Automate returns processing, rebate management, and chargeback handling | Revenue Assurance | Medium |
| 4 | GT-010 Process Migration | Migrate Manage Global Trade Master Data (IP) business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Order Management (Intel Products) | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Order Processing Time | < 2 hours | Time from order receipt to order confirmation | 6 hours (current) | Order Management Lead |
| Customer Credit Decision Time | < 15 minutes | Automated credit check and approval for standard orders | 2 hours (manual) | Credit Manager |
| Returns Processing Cycle | < 3 business days | End-to-end returns receipt to credit memo issuance | 7 business days (current) | Returns Manager |
| GT-010 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

This capability includes **3 business process(es)** modeled in BPMN 2.0, covering the end-to-end workflow for GT-010 Manage Global Trade Master Data (IP).

| # | Step ID | Process Name | Lanes | Tasks | Gateways |
|---|---------|--------------|-------|-------|----------|
| 1 | GT-010-010_Maintain_Compliance_Master_Data_(IP) | GT-010-010_Maintain_Compliance_Master_Data_(IP) | Trade IT Analyst | 16 | 9 |
| 2 | GT-010-020_Maintain_General_Customs_Master_Data_(IP) | GT-010-020_Maintain_General_Customs_Master_Data_(IP) | Trade IT Analyst | 31 | 22 |
| 3 | GT-010-060_Maintain_Organizational_Structure_Master_Data_(IP) | GT-010-060_Maintain_Organizational_Structure_Master_Data_(IP) | Trade IT Analyst | 3 | 4 |

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.2 Business Process Diagrams


#### BUSINESS ARCHITECTURE — 3.2.1 GT-010-010_Maintain_Compliance_Master_Data_(IP) — GT-010-010_Maintain_Compliance_Master_Data_(IP)

**Swim Lanes**: Trade IT Analyst | **Tasks**: 16 | **Gateways**: 9

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
    subgraph Trade IT Analyst
        n1["fa:fa-user Manage SPL Master - Create Manually"]
        n2["fa:fa-user Manage Embargo Situations"]
        n3["fa:fa-user Manage SPL Master - Change Manually"]
        n4["fa:fa-user Manage SPL Master - Display"]
        n5["fa:fa-user Display SPL Change History"]
        n6["fa:fa-user Display Sanctioned Party Lists"]
        n7["fa:fa-user Display Expiring Sanctioned Party List"]
        n8["fa:fa-user Search Upload Logs"]
        n9["fa:fa-user Display Partner in Embargo Countries"]
        n10["fa:fa-user Create Control Classes"]
        n11["fa:fa-user Create Peculiarity Codes"]
        n12["fa:fa-user Setup Control Settings for SAP HANA Search"]
        n13["fa:fa-user Setup Control Settings for Comparison Terms"]
        n14["fa:fa-user Display Upload Logs Control Classes"]
        n15[["fa:fa-cog Load Sanctioned Party Lists from XML File"]]
        n16[["fa:fa-cog Upload Control Classes"]]
        n17(["fa:fa-play Trade Compliance Master Data Management Triggered"])
        n18(["fa:fa-stop Compliance SPL Master Data Maintained"])
        n19(["fa:fa-stop Embargo Management Done"])
        n20(["fa:fa-stop Control Classes Managed"])
        n21(["fa:fa-stop Settings Controlled"])
        n22(["fa:fa-stop Control Classes Uploaded"])
        n23{{"fa:fa-code-branch Type of Master Data?"}}
        n24{{"fa:fa-code-branch Mode of Management?"}}
        n25{{"fa:fa-code-branch exclusiveGateway"}}
        n26{{"fa:fa-code-branch Type of Maintainence?"}}
        n27{{"fa:fa-code-branch exclusiveGateway"}}
        n28{{"fa:fa-code-branch Embargo Situations Update Required?"}}
        n29{{"fa:fa-code-branch exclusiveGateway"}}
        n30{{"fa:fa-code-branch Control Class or Peculiarity Codes?"}}
        n31{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n17 --> n23
    n16 --> n14
    n12 --> n13
    n15 --> n8
    n1 --> n25
    n3 --> n25
    n4 --> n25
    n25 --> n27
    n8 --> n27
    n5 --> n27
    n27 --> n18
    n29 --> n9
    n14 --> n22
    n10 --> n31
    n11 --> n31
    n31 --> n20
    n13 --> n21
    n24 -->|"Create"| n1
    n24 -->|"Change"| n3
    n2 --> n29
    n9 --> n19
    n28 -->|"Yes"| n2
    n23 -->|"Compliance Sanctioned Party List Master Data"| n26
    n28 -->|"No"| n29
    n26 -->|"Manage SPL Master Data"| n24
    n24 -->|"Display"| n4
    n26 -->|"Upload from XML File"| n15
    n26 -->|"Review Change History"| n5
    n26 -->|"Review SPL near Expiry Date"| n7
    n30 -->|"Peculiarity Code"| n11
    n30 -->|"Control Class"| n10
    n23 -->|"Embargo Management"| n28
    n23 -->|"Creation of Control Classes and Peculiarity Codes"| n30
    n23 -->|"Upload of control classes (Received from Content Provider)"| n16
    n23 -->|"Control Settings Compliance Search"| n12
    n7 --> n27
    n6 --> n27
    n26 -->|"Display Overall SPL Master Data"| n6
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 userTask
    class n10 userTask
    class n11 userTask
    class n12 userTask
    class n13 userTask
    class n14 userTask
    class n15 serviceTask
    class n16 serviceTask
    class n17 startEvt
    class n18 endEvt
    class n19 endEvt
    class n20 endEvt
    class n21 endEvt
    class n22 endEvt
    class n23 gateway
    class n24 gateway
    class n25 gateway
    class n26 gateway
    class n27 gateway
    class n28 gateway
    class n29 gateway
    class n30 gateway
    class n31 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWGuP2jgU_StWqhGtBFLeCXzYFRNgW2mmOyrTfajsB5M4YDUkrBOYYaf8970mdiCO0XS7SDPCx_ec-_CbFyMuEmKMjJubF5rTaoReetWabEhvhHpLXJJeH9XAb5hRvMxI2eM2aZFXc_rPycxyt8_cjGMzvKHZgaNzsioI-vyhj8ZAzPqoxHk5KAmjaa_f2zK6wewQFVnBuPUbEqZmevImum4LlhB2NjDNwIo9oGY0J2fYCdzAnXFeSeIiT1qiqZeGadw78uCy4ileY1adwt-V5B4__06Tag3tFGclAZt1tcnu8JJkPMeK7TgW79heFoOW3E8OBZtvcUzzFeCuCRDD-dcz5JnHIzre3Czyxil6nCxyBJ84w2U5ISkqK4Cn-wqlNMtGb9xoPPPMflmx4isZvbGnwcSx-zHPZASpm31e3METoat1NVoWWSJMB088h5G9fe6z55Ft9tkB_iu-SJ6cPUW-Hdph4-k2sCIrkp7SNP1fnqCu7BGXX4WvqTOzZ5PGl-X5XmR29WSaEzcYW2qdCNvTmFyIzmYzZ3ou1dT3LPO66O3M8c1IEV3hijzhw1lwGLmN4MwLZlZwVbD2p0a5Wz6wIpaCztSbeY1gcGvNxvZVQXdsuaGIEHRWDG_X6JHhhKAPj2ic4-xQVnU3_-TWl4WR4lGKB7za6B7neEXQ_OEOvpYVIAMUMQIZ8q4dzrLDwvjrgm9r-dPNErNVgea02uGKFnnZZjnf4XWN89U1r-7r_AkttxlWeF6bJ2xOROHvPS2rgik0_woN5zFPjiToAdbfAd0BWck00FOnz1vKYIHrNdoSYVtiTjCL1-jzNitwgu6KleJxqPfI1XNo07wZnajY5RWjRBGwzLaCGP8IVjIrMhTxadrhWFrOA4l3GYW9HhKLYKdTWbaaWrXbNo6gVUGJSpQW0DV-QO_HH8cifUXH-W6dqNhsIZ6yyNEjYRs1IFdfvItiv1IH70ujEBcrYABNP09QyooN-uP-Ds1oRkCmpeO3dUQAXd8tUvC2IZ3Crtc9TxkGIY-JXB0TXGGxaDYkh_OE0dWKMJKA4LtLwfAsCMtieyl1sdiEHM0r-OuKDBUROf0uAphAcRSabXZ8t3IXdNWbbSm0ZvQFP-tS7Fc81cXv8pyXl_MYJWSwhJMbVubjYUtQkV5W5-eFcTxeUl099R6-11RZmg7T0zPJc5ztSronv9SnkUrzX4tVjB4Mbcdl8GMuQz2tezZAgRO-W3wif-8ozMJOAMMfCsAx9bTW8CLYEzq7lBqAY_3XAOCSVH-BRYkGg5_4bJGAXwOWKwFbAI2FVwOhbAsFT7Qdpe0qbVvw7UAAodJW-20RoyU92sMaGMoIpAtbAmYNOJYELAVwZNSmtJBhSwv7JPptYdSHxcL4BkadvtOxfOqT5RHlsmVwIlZLtu1QcP_kOyQQZdC2I0UvtjHd3ny5dGsFX9X-WNQdjVNfdHTvImcVV82uuaRAr6sqiT1fOSZ4kTzV9BPZU_LUucOA7TVTHl8OR2l9EznwIGtxOSccUxDU1VGHYKlmrVVV25hq3bs7f12XsDNAfEbAqPCtSd2NcZ7o7hV8gnQcihKCSixUYqHy9hOJCaxcUV_uhB9EcO_eU3gpvqsz8LszR7lTXE4lcTPhRDnlAmWl-erK89szAf26Jwzuu9r541-8E_iuIN9HLdjWw44edvWwp4d9PRzo4VAPD_Uw7Ch6_Eqe1pVErSuZWldShc324lXY7vKvdwXNm7uNh-J93EaHOtQ2tailRW0t6sjHZxt29bCnh309HOjhUA8PtTDsDlrYkrDRNzZwDcc0MUYvxumnIfj5KCEp3mWVcewbeFcV80MeG6PTTyjG7nRVmFAML9tNDR7_BQi1yuo=" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### BUSINESS ARCHITECTURE — 3.2.2 GT-010-020_Maintain_General_Customs_Master_Data_(IP) — GT-010-020_Maintain_General_Customs_Master_Data_(IP)

**Swim Lanes**: Trade IT Analyst | **Tasks**: 31 | **Gateways**: 22

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
    subgraph Trade IT Analyst
        n1["fa:fa-user Manage Business Partner"]
        n2["fa:fa-user Create/Update Employee Partner"]
        n3["fa:fa-user Create/Update Customs Broker"]
        n4["fa:fa-user Upload Customs Offices from XML File"]
        n5["fa:fa-user Upload Customs Offices from Official Format"]
        n6["fa:fa-user Maintain Departure and Destination Points"]
        n7["fa:fa-user Maintain Air Cargo Property by Connection Point"]
        n8["fa:fa-user Upload Customs Currency Exchange Rates"]
        n9["fa:fa-user Maintain Exchange Rates Through Worklist"]
        n10["fa:fa-user Create/Upload Customs Office"]
        n11["fa:fa-user Upload Transportation Points"]
        n12["fa:fa-user Upload Exchange Rates"]
        n13["fa:fa-user Manage Tariff Number"]
        n14["fa:fa-user Display Upload Logs - Tariff Number"]
        n15["fa:fa-user Manage Additional Tariff Numbers"]
        n16["fa:fa-user Display Upload Logs - Additional Tariff Numbers"]
        n17["fa:fa-user Maintain Tariff Number Attributes"]
        n18["fa:fa-user Upload Measures"]
        n19["fa:fa-user Manage Properties for Measure Type"]
        n20["fa:fa-user Display Upload Logs - Measures"]
        n21["fa:fa-user Display Upload Logs - Customs Duty Rates"]
        n22["fa:fa-user Manage Duty Rates"]
        n23["fa:fa-user Determine Duty Rates for Tariff No."]
        n24["fa:fa-user Display Upload Logs - Commodity Codes"]
        n25["fa:fa-user Manage Commodity Codes"]
        n26[["fa:fa-cog Upload Tariff Number"]]
        n27[["fa:fa-cog Upload Additional Tariff Numbers"]]
        n28[["fa:fa-cog Upload Duty Rates"]]
        n29[["fa:fa-cog Upload Commodity Codes"]]
        n30["Maintain Customs Office Numbers Process Details"]
        n31["Maintain Validity of Customs Offices"]
        n32(["fa:fa-play General Customs Master Data Maintainence Triggered"])
        n33(["fa:fa-stop Business Partners Maintained"])
        n34(["fa:fa-stop Transportation Points Managed"])
        n35(["fa:fa-stop Exchange Rates Managed"])
        n36(["fa:fa-stop Tariff Codes Managed"])
        n37(["fa:fa-stop Tariff Codes Displayed"])
        n38(["fa:fa-stop Measures Managed"])
        n39(["fa:fa-stop Commodity Codes Managed"])
        n40(["fa:fa-stop Duty Rates Done"])
        n41(["fa:fa-stop Tariff Number Attributes Maintained"])
        n42{{"fa:fa-code-branch Type of Master Data?"}}
        n43{{"fa:fa-code-branch Type of Business Partner?"}}
        n44{{"fa:fa-code-branch Mode of Upload?"}}
        n45{{"fa:fa-code-branch exclusiveGateway"}}
        n46{{"fa:fa-code-branch Type of Transportation Points?"}}
        n47{{"fa:fa-code-branch Mode of Exchange Rates Maintenance?"}}
        n48{{"fa:fa-code-branch exclusiveGateway"}}
        n49{{"fa:fa-code-branch exclusiveGateway"}}
        n50{{"fa:fa-code-branch exclusiveGateway"}}
        n51{{"fa:fa-code-branch Type of tariff ?"}}
        n52{{"fa:fa-code-branch Mode of Management?"}}
        n53{{"fa:fa-code-branch Mode of Management?"}}
        n54{{"fa:fa-code-branch exclusiveGateway"}}
        n55{{"fa:fa-code-branch exclusiveGateway"}}
        n56{{"fa:fa-code-branch Mode of Management?"}}
        n57{{"fa:fa-code-branch Mode of Management?"}}
        n58{{"fa:fa-code-branch Mode of Management?"}}
        n59{{"fa:fa-code-branch exclusiveGateway"}}
        n60{{"fa:fa-code-branch exclusiveGateway"}}
        n61{{"fa:fa-code-branch exclusiveGateway"}}
        n62{{"fa:fa-code-branch exclusiveGateway"}}
        n63{{"fa:fa-code-branch exclusiveGateway"}}
    end
    n32 --> n42
    n30 --> n45
    n4 --> n45
    n5 --> n45
    n26 --> n52
    n27 --> n53
    n13 --> n54
    n55 --> n17
    n18 --> n56
    n28 --> n57
    n22 --> n63
    n63 --> n23
    n29 --> n58
    n31 --> n50
    n54 --> n59
    n59 --> n63
    n54 --> n55
    n59 --> n55
    n14 --> n36
    n16 --> n37
    n19 --> n60
    n20 --> n60
    n60 --> n38
    n24 --> n61
    n25 --> n61
    n61 --> n39
    n6 --> n48
    n7 --> n48
    n48 --> n34
    n8 --> n49
    n9 --> n49
    n49 --> n35
    n51 -->|"Additional Tariff"| n27
    n57 -->|"Manage"| n22
    n10 --> n44
    n11 --> n46
    n42 -->|"Transportation Points"| n11
    n12 --> n47
    n42 -->|"Exchange Rates"| n12
    n50 --> n33
    n1 --> n50
    n2 --> n50
    n3 --> n50
    n43 -->|"Customs Office"| n10
    n43 -->|"Business Partner"| n1
    n43 -->|"Employee Partner"| n2
    n43 -->|"Customs Broker"| n3
    n53 -->|"Display"| n16
    n58 -->|"Manage"| n24
    n46 -->|"Departure and Destination Point"| n6
    n46 -->|"Connection Point"| n7
    n47 -->|"Customs Currency"| n8
    n57 -->|"Display"| n21
    n44 -->|"Official format"| n5
    n44 -->|"XML File"| n4
    n44 -->|"Process Details"| n30
    n23 --> n62
    n62 --> n40
    n42 -->|"Maintain Business Partners"| n43
    n51 -->|"Tariff"| n26
    n47 -->|"Worklist"| n9
    n21 --> n62
    n15 --> n59
    n17 --> n41
    n52 -->|"Manage"| n14
    n52 -->|"Display"| n13
    n56 -->|"Display"| n19
    n56 -->|"Manage"| n20
    n58 -->|"Display"| n25
    n42 -->|"Duty Rates"| n28
    n42 -->|"Measures"| n18
    n42 -->|"Tariff Codes"| n51
    n42 -->|"Commodity Code"| n29
    n53 -->|"Manage"| n15
    n45 --> n31
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 userTask
    class n5 userTask
    class n6 userTask
    class n7 userTask
    class n8 userTask
    class n9 userTask
    class n10 userTask
    class n11 userTask
    class n12 userTask
    class n13 userTask
    class n14 userTask
    class n15 userTask
    class n16 userTask
    class n17 userTask
    class n18 userTask
    class n19 userTask
    class n20 userTask
    class n21 userTask
    class n22 userTask
    class n23 userTask
    class n24 userTask
    class n25 userTask
    class n26 serviceTask
    class n27 serviceTask
    class n28 serviceTask
    class n29 serviceTask
    class n32 startEvt
    class n33 endEvt
    class n34 endEvt
    class n35 endEvt
    class n36 endEvt
    class n37 endEvt
    class n38 endEvt
    class n39 endEvt
    class n40 endEvt
    class n41 endEvt
    class n42 gateway
    class n43 gateway
    class n44 gateway
    class n45 gateway
    class n46 gateway
    class n47 gateway
    class n48 gateway
    class n49 gateway
    class n50 gateway
    class n51 gateway
    class n52 gateway
    class n53 gateway
    class n54 gateway
    class n55 gateway
    class n56 gateway
    class n57 gateway
    class n58 gateway
    class n59 gateway
    class n60 gateway
    class n61 gateway
    class n62 gateway
    class n63 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlWW1v2zYQ_iuEi8AbYG8iJUqyP2xw_DIUaLZiSdsBzT7QEmULlSWDkpN4qf_7SIuULYo0Mi9Am-jhPXf3HI-URL32oiKmvXHv5uY1zdNqDF771ZpuaH8M-ktS0v4A1MBnwlKyzGjZFzZJkVf36T9HM-htX4SZwBZkk2Z7gd7TVUHBp_cDMOHEbABKkpfDkrI06Q_6W5ZuCNtPi6xgwvodDRMnOUaTQ7cFiyk7GThOACPMqVma0xPsBl7gLQSvpFGRxy2nCU7CJOofRHJZ8RytCauO6e9KekdevqRxtebXCclKym3W1Sb7QJY0ExorthNYtGNPqhhpKeLkvGD3WxKl-YrjnsMhRvJvJwg7hwM43Nw85k1Q8DB7zAH_iTJSljOagLLi8PypAkmaZeN33nSywM6grFjxjY7foXkwc9EgEkrGXLozEMUdPtN0ta7GyyKLpenwWWgYo-3LgL2MkTNge_6_Fovm8SnS1EchCptItwGcwqmKlCTJ_4rE68oeSPlNxpq7C7SYNbEg9vHU6fpTMmdeMIF6nSh7SiN65nSxWLjzU6nmPoaO3entwvWdqeZ0RSr6TPYnh6Op1zhc4GABA6vDOp6e5W75kRWRcujO8QI3DoNbuJggq0NvAr1QZsj9rBjZrsEDIzEF7x_AJCfZvqzqYfGTw6-PvYSMEzIU1QZ3JCcrCm53JV8XZQk-8r7KKXvs_X3GQW3OlFFegZ8_bWP-C8w326zYU2qmupeo011ZFZsS3AppGtFrEz_xICRuGH8kCZ_WEiSs2IC_7j6ARZrRtgP8dgfHC77LgEXBNqRq-_H1gqV5xf-BGd1ywTtGAcljflVWaU6qtMjBx4KblG0vgcXLJOVFIWxVAN4BW8qqPVjuwbTIcxqdnLV9hReVTXeM0Tzag_kL3zxyPrl_8lpr6Yws6bQ54GHNit1qDb4U7FuWlloe0LFMrqHSGhMaJfC2zcttwSp7HSEyMi9pha6x5R_4HSlJwO-7zVLvPag13ywttxlf8DLYh2JVguFFB9gYchLHqVDGO61F1hP23xL-rc5sndcigUlVsXS56xbP3Gx3lJS89XXjkVG27OxULLeCKS542G-1tkDOW4SbYyP4Fq5qytmOLzRDryBkVGA111prRivKNnwnPWMcNatiFz9pDt7UadNisyn4bIuNIe7kYO61yxz_a0OKilWz_rSOblECI-VSF7booZHeKmzLfmS076pq3WxE_zQN3t6AVF6iGyNxp-NzRdJMK4wLzz18Jll6DFYk-o1Do6EfmmyP8_cb5XdCXhPFuiNlJaaXVKRZgXyT5ouApasVZTTmDn889-iePHIX284dujz56XA9jWvcV2WjdMhYI2u3BAvL10PWzXCcJRsnuMSRK6HLCjWW2g5sUUaavdZCFprnaLSzBT0rcqqbQ7OWzu5qnzUPvb6eOj6mwyWftWh93CZFA5610K-PvcPhnOpepuq90-F7Zv4d_1vw68XXYWEzi75EGQ_4RH-rn5N1mn85WWOzdmIHlzPuNC13QnNuQjuewutUjK6iYec6Grxcs6ruNl0bRperVLf-huZVh-lezfSuU3hdM2H_6jyDq5nh1czrmsa_rml8eB0NXUdz_yuNnyvUf_DbJxgOfxFboAIcCWAJeNo11q6RXwNYeUCBBFwJQFcCnnIhfcBAWYTSwlc-FKAskMzTV0596RQpAI0kJVRKoAQcFVZKwSMFjDSnjQXWLBoASgtXZQqlfLfRopyqsMjRAF8CrsoUSac-VADWAF9qcVXqMqqnXATatScL6Kqay2tPORhp154E3Eb6MeT3x17nOfOx913MsrILpF29-OpB1QtQdZNKA0ohnqqfhyTd8gb6XXAUWTVroJP1l1DBUjlgVe6mH7W-QNq1q117royiv1eLKB2j7nmOMNOtukc3omy2gOqUhts0raps5NNaHUZVFYeGSVFz4PmKevkc5cjydVL3gIRbNRMSaJmrI5GjVai3zHnuqKmRJ0ebs6FEng1xK6wbnU6g-Kinj3beOEQFm3mXE-2ruvuqvxy9v5r3ks67QB3X1RfN-Urx9eKcznT4sFqACGrZQKxtV1AtclUpjLqzDD19sNUgTaK-aXSkj563j6P3Vmv2sF6y8_dLYRB2atocJojQneHzV5J66qFu0n6fqMOM9PVxXpsmSVla9_zQWmwM6hi8BSMz7JphzwxjM-yb4cAMh2Z4ZIb55mvGLTqhRSi0KIUWqdCiFVrEQotaaJELLXqRRS-yzatFL7LoRRa9yKKXPxmdfQRpDwX2odA-NLIO8ec49WGqjbvyI1Ib9YwoNqK-EQ2MaGhERybUc4woNKJIfflpw64Z9swwNsO-GQ7McGiGR0aYP3oYYWiGzSqxWSU2q8RmldisEptVYrNKbFbpm1X6ZpW-WaXfqOwNeht-lEvSuDd-7R0_YfPP3DFNyC6reodBj-yq4n6fR73x8VNvb3f8pDVLCf8Ct6nBw7-ov6xj" title="View full diagram">&#128065; View Full Diagram</a></div>


<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


#### BUSINESS ARCHITECTURE — 3.2.3 GT-010-060_Maintain_Organizational_Structure_Master_Data_(IP) — GT-010-060_Maintain_Organizational_Structure_Master_Data_(IP)

**Swim Lanes**: Trade IT Analyst | **Tasks**: 3 | **Gateways**: 4

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
    subgraph Trade IT Analyst
        n1["fa:fa-user Manage Business Partner - Change"]
        n2["fa:fa-user Manage Business Partner - Create"]
        n3["fa:fa-user Manage Business Partner - Display"]
        n4(["fa:fa-play Maintain Organizational Structure Master Data in GTS Triggered"])
        n5(["fa:fa-stop Organizational Structure Master Data Maintained"])
        n6{{"fa:fa-code-branch Way of Maintaining Master Data?"}}
        n7{{"fa:fa-code-branch exclusiveGateway"}}
        n8{{"fa:fa-code-branch exclusiveGateway"}}
        n9{{"fa:fa-code-branch Change?"}}
    end
    n4 --> n6
    n6 -->|"Create"| n2
    n8 --> n3
    n2 --> n9
    n3 --> n5
    n1 --> n8
    n7 --> n1
    n6 -->|"Change"| n7
    n6 -->|"Display"| n8
    n9 -->|"No"| n8
    n9 -->|"Yes"| n7
    class n1 userTask
    class n2 userTask
    class n3 userTask
    class n4 startEvt
    class n5 endEvt
    class n6 gateway
    class n7 gateway
    class n8 gateway
    class n9 gateway
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqlVWuP2jgU_StWRiN2pSDlSUI-7AoCGVXaditBW1WlH0ziBGuMg2xnBsrw3_eaPHgMI422kUDc43vOfXB9szfSMiNGZNzf7ymnKkL7nlqRNelFqLfEkvRMVANfsaB4yYjsaZ-85GpGfx3dbG-z1W4aS_Casp1GZ6QoCfrywUQjIDITScxlXxJB857Z2wi6xmIXl6wU2vuOhLmVH6M1R-NSZEScHCwrsFMfqIxycoLdwAu8RPMkSUueXYjmfh7mae-gk2Plc7rCQh3TryT5iLffaKZWYOeYSQI-K7Vm_-AlYbpGJSqNpZV4aptBpY7DoWGzDU4pLwD3LIAE5o8nyLcOB3S4v1_wLiiaTxYcwZMyLOWE5EgqgKdPCuWUsejOi0eJb5lSifKRRHfONJi4jpnqSiIo3TJ1c_vPhBYrFS1LljWu_WddQ-RstqbYRo5lih18X8UiPDtFigdO6IRdpHFgx3bcRsrz_LciQV_FHMvHJtbUTZxk0sWy_YEfW6_12jInXjCyr_tExBNNyZlokiTu9NSq6cC3rbdFx4k7sOIr0QIr8ox3J8Fh7HWCiR8kdvCmYB3vOstq-VmUaSvoTv3E7wSDsZ2MnDcFvZHthU2GoFMIvFmhucAZQR_maMQx20lVH-uH2z8WRo6jHPd1t9FHzHFB0LiScC-kRJ9hrjjgfRSvMC_Iwvh5RnbeTRYEmnRJdt9LnlC5YXh3yfb-6Oj6EOiUK_igf0WBOf2FFS2hWDSDm5eqShDwkAr0JlhhBH4P8xn0hRYFESQD7T_PxP2TuFTl5n2abQav1Ab7faum12N_CRc8XaFvkHWZdzS47edyfy-Mw-FMJLgtQrYpg449kYd6CK9Y4f9iDW-z6gk4Sww2Qf2De6jf_wsqbcyBNl8WRvu3v8CoNEdh7ek2plObw8Z0a9NvTLs2w8YMatO-jtJMJkQJro660Xk5qQybs0_lTfg7kedSx0upM2mX0QXs3Ibd27DX7ekL2G9W6gU4aNfKBRrcRMOb6LBFDdNYE7HGNDOivXF8_cIrOiM5rpgyDqaBK1XOdjw1ouNryqg2GTAnFMP2WNfg4T88HoDl" title="View full diagram">&#128065; View Full Diagram</a></div>



<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Trade IT Analyst | GT-010-010_Maintain_Compliance_Master_Data_(IP), GT-010-020_Maintain_General_Customs_Master_Data_(IP), GT-010-060_Maintain_Organizational_Structure_Master_Data_(IP) | |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for GT-010. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 4.2 Data Flow Diagrams

> **DATA ARCHITECTURE** — Database-to-database data flows. Applications (blue) sit above their hosting databases (green cylinders). Thick arrows show data movement between databases.





### 4.3 Data Lineage

Data lineage traces the origin and transformation path of key data objects across integrated systems.

| # | Source System | Source Schema/Object | Target System | Target Schema/Object | Transformation |
|---|-------------|---------------------|---------------|---------------------|---------------|

> *Lineage detail will be refined when tower architects validate source/target schema object mappings.*

### 4.4 RICEFW Data Objects

Data-centric RICEFW objects (Reports and Conversions) from the Object Tracker:

| Object ID | Type | Description | Status | Source | Target | Complexity |
|-----------|------|-------------|--------|--------|--------|-----------|
| OTCR0967 | Report | Developing a report for the 2DN model where we can view the E2E flow in one r... | 10. Object Complete |  |  | 03.Medium |
| LOGR1252 | Report | 2DN - Inbound Escort Report | 10. Object Complete |  |  | 02.High |
| LOGR1236 | Report | 2DN - Outbound Escort Report | 06. Dev In Progress |  |  | 02.High |
| LOGR1173 | Report | 2DN - Outbound Manifest Report | 10. Object Complete |  |  | 03.Medium |
| LOGR1172 | Report | 2DN - Inbound Manifest Report | 10. Object Complete |  |  | 03.Medium |
| OTCM028_IP | Conversion | Open Quantity Contract | 10. Object Complete | ECC | S4 | N/A |
| OTCC1341 | Conversion | Payer Profile Data Conversion | 10. Object Complete |  |  | 03.Medium |
| OTCC1340 | Conversion | Payer Segment Data Conversion | 10. Object Complete |  |  | 03.Medium |
| OTCC1339 | Conversion | Payer Relationship Data Conversion | 10. Object Complete |  |  | 03.Medium |
| OTCC1232 | Conversion | Intel Federal Data conversion for Contract ITD costs | 10. Object Complete |  |  | 03.Medium |
| OTCC1231 | Conversion | Intel Federal Data conversion for Bill Plans | 10. Object Complete |  |  | 03.Medium |
| OTCC1229 | Conversion | Data conversion of open Federal Contracts from ECC to Dassian S4. | 10. Object Complete |  |  | 03.Medium |
| OTCC1228 | Conversion | Data conversion for Federal Contracts - Contract Fees/Retention/Incentive Fee... | 10. Object Complete |  |  | 03.Medium |
| OTCC1227 | Conversion | Data conversion for Intel Federal Contract WBS Assignments | 10. Object Complete |  |  | 03.Medium |
| OTCC0803 | Conversion | Open Credit Case Conversion | 10. Object Complete |  |  | 02.High |
| OTCC0802 | Conversion | Custom Z table(DH) DH tables data conversion from ECC to S4 for IP | 10. Object Complete |  |  | 02.High |
| OTCC0717 | Conversion | Pricing Condition records conversion | 10. Object Complete |  |  | 01.Very High |
| OTCC0679 | Conversion | Open Dispute Case Conversion | 10. Object Complete |  |  | 02.High |
| OTCC0678 | Conversion | Collection Master Conversion | 10. Object Complete |  |  | 02.High |
| OTCC0636 | Conversion | Output Condition (Sales) Conversion for IP R3 release | 10. Object Complete |  |  | 01.Very High |
| OTCC0564 | Conversion | Customer Material Info Record Conversion for IP R3 release | 10. Object Complete |  |  | 03.Medium |
| OTCC0563 | Conversion | Open Sales Order Conversion for IP R3 release | 10. Object Complete |  |  | 02.High |
| LOGM007_IP | Conversion | Storage Bin Upload | 10. Object Complete | WIINGS | EWM | N/A |
| LOGM006_IP | Conversion | Product Master conversion (additional EWM attribution) | 10. Object Complete | WIINGS, ECC WM | EWM | N/A |
| LOGC1313 | Conversion | Conversion of stock upload program | 10. Object Complete |  |  | 03.Medium |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for GT-010.


#### Current-State Flow Narrative

*(No current-state flows defined.)*


### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for GT-010.


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

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| OTCW1683 | Workflow | Additional WRICEF for Credit Limit Request Workflow | 10. Object Complete |  | NA | 03.Medium |
| OTCR0967 | Report | Developing a report for the 2DN model where we can view the E2E flow in one r... | 10. Object Complete |  | NA | 03.Medium |
| OTCM028_IP | Conversion | Open Quantity Contract | 10. Object Complete | ECC → S4 | NA | N/A |
| OTCI1721 | Interface | Outbound Interface changes to send data from S4 to SF | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| OTCI1720 | Interface | Inbound Interface to Update Original Flag Interface from SFDC to S4. | 06. Dev In Progress |  | MULESOFT | 03.Medium |
| OTCI1649 | Interface | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI1648 | Interface | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI1598 | Interface | An outbound Interface to Read the EEPM and DECODER Matrix from S4 to OL | 06. Dev In Progress |  | APIGEE | 02.High |
| OTCI1568 | Interface | Inbound Interface from WOM to S4 HANA to send Shipment and tracking information | 10. Object Complete |  | MULESOFT | 03.Medium |
| OTCI1498 | Interface | Inbound Interface from WOM to S4 HANA to send Customer Hierarchy | 10. Object Complete |  | MULESOFT | 03.Medium |
| OTCI1423 | Interface | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI1259 | Interface | Outbound interface from S4 HANA to WOM to send the product information | 10. Object Complete | S/4 → E-Commerce Cloud | APIGEE | 04.Low |
| OTCI1192 | Interface | Interface for BP Status query in GTS - CAAS | 10. Object Complete | GTS → MULESOFT | APIGEE | 03.Medium |
| OTCI1191 | Interface | Interface for Transactional status query in GTS - CAAS | 10. Object Complete | GTS → MULESOFT | APIGEE | 03.Medium |
| OTCI1190 | Interface | Interface for Product Create/ Change in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | APIGEE | 02.High |
| OTCI1189 | Interface | Interface for Product Classification Query in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | APIGEE | 03.Medium |
| OTCI1188 | Interface | Interface for Transactional Create/ Change in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | APIGEE | 03.Medium |
| OTCI1187 | Interface | Interface for BP Create/ Change in GTS - CAAS | 10. Object Complete | MULESOFT → GTS | MULESOFT | 02.High |
| OTCI1180 | Interface | EMS_Inbound Interface for Capturing Hardware SO and Line-Item Details into se... | 10. Object Complete | OL → S/4 | APIGEE | 03.Medium |
| OTCI1179 | Interface | EMS_Outbound interface to OL (Orchestration layer) for activation key generat... | 10. Object Complete | S/4 → OL | APIGEE | 03.Medium |
| OTCI1178 | Interface | Interface from Sales Force (SF) to S4 to read the business rules | 10. Object Complete | SF → S/4 | MULESOFT | 03.Medium |
| OTCI0876 | Interface | Inbound interface to S4 HANA from PDH system to get dampened and Non Dampened... | 10. Object Complete | PDH → S/4 | BODS | 03.Medium |
| OTCI0716 | Interface | PIP 2A1 Interface to Distribute | 10. Object Complete |  | MULESOFT | 03.Medium |
| OTCI0711 | Interface | IP - Inbound Interface from CSAR to SAP | 10. Object Complete | CSAR → S/4 | NA | 02.High |
| OTCI0682 | Interface | Inbound Interface for Receiving PO details from B2B Customer | 10. Object Complete | OpenText → S/4 | MULESOFT | 03.Medium |
| OTCI0661 | Interface | Inbound KL Order Creation from ALPS to S/4 | 10. Object Complete | ALPS (Intel Product Validation Labs Planning) → S/4 | MULESOFT | 03.Medium |
| OTCI0565 | Interface | Outbound Interface development for Invoice data from S4 to CHM | 10. Object Complete | S/4 → CHM | NA | 03.Medium |
| OTCI0540 | Interface | Inbound Interface from WOM to S4 HANA to fetch the list of order Acknowledgem... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| OTCI0488 | Interface | Interface development direction inbound for Credit or Debit Memo Requests cre... | 10. Object Complete | CHM → S/4 | NA | 03.Medium |
| OTCI0439 | Interface | Enable PIP 3A6 – transmit order status to the B2B customer (outbound interface) | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| OTCI0438 | Interface | Enable PIP 3A7 – transmit significant sales order changes to the B2B customer... | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| OTCI0435 | Interface | Inbound interface from IRC2 (Intel Registration Center) B-app to S4 against o... | 10. Object Complete | IRC2 → S/4 | MULESOFT | 03.Medium |
| OTCI0426 | Interface | Outbound interface to IRC2 (Intel registration center) B-app upon order create | 10. Object Complete | S/4 → IRC2 | MULESOFT | 03.Medium |
| OTCI0417 | Interface | Interface to Maintain Customer Part numbers in CMIR in S4 through WOM | 10. Object Complete | S/4 → WOM | MULESOFT | 03.Medium |
| OTCI0414 | Interface | Order create 4B3 - Consignment Issue | 10. Object Complete |  | MULESOFT | 02.High |
| OTCI0413 | Interface | WOM users should be able to verify/simulate orders details before submitting ... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| OTCI0298 | Interface | Enable capture of changes on the Return Request from Salesforce into relevant... | 10. Object Complete | SalesForce → S/4 | MULESOFT | 03.Medium |
| OTCI0296 | Interface | Enable EDI : Billing Output Generation | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| OTCI0294 | Interface | Inbound interface between Sales Force and S4 needed to create Return Order fo... | 10. Object Complete | SalesForce → S/4 | MULESOFT | 02.High |
| OTCI0291 | Interface | Outbound Interface from S4 to Salesforce to update the Return Order status in... | 10. Object Complete | S/4 → SalesForce | MULESOFT | 02.High |
| OTCI0258 | Interface | Enable EDI 855 – Order Acknowledgment to B2B customer | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| OTCI0257 | Interface | Enable EDI 865 – Order change acknowledgment to B2B customer | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| OTCI0085 | Interface | Outbound Interface from S4HANA to WOM to Share order confirmation data | 10. Object Complete | S/4 → WOM | MULESOFT | 02.High |
| OTCI0082 | Interface | Interface between MyDeals and S4 needed for pricing feeds | 10. Object Complete | MyDeals → S/4 | MULESOFT | 02.High |
| OTCI0081 | Interface | Interface between IPAR and S4 needed for pricing feeds | 10. Object Complete | IPAR → S/4 | MULESOFT | 02.High |
| OTCI0061 | Interface | Enable WOM - Order Change | 10. Object Complete | Commerce Cloud → S/4 | MULESOFT | 01.Very High |
| OTCI0060 | Interface | Enable EDI - Order Change | 10. Object Complete | OpenText → S/4 | MULESOFT | 02.High |
| OTCI0058 | Interface | Enable MySamples - Sample Order Change | 10. Object Complete | MySamples → S/4 | MULESOFT | 02.High |
| OTCI0040 | Interface | Enable MySamples - Sample Order Create | 10. Object Complete | MySamples → S/4 | MULESOFT | 02.High |
| OTCI0038 | Interface | Enable EDI - Order Create | 10. Object Complete | OpenText → S/4 | MULESOFT | 02.High |
| OTCI0037 | Interface | Enable WOM - Order Create | 10. Object Complete | Commerce Cloud → S/4 | MULESOFT | 01.Very High |
| OTCF1714 | Form | Intel Federal Form for Progress Pay (Output type SF1443) | 10. Object Complete |  | NA | 03.Medium |
| OTCF1629 | Form | Returns Credit Memo Output item level consolidation | 10. Object Complete |  | NA | 03.Medium |
| OTCF0681_IP | Form | Form development for Intercompany Invoice. | 10. Object Complete |  | NA | 02.High |
| OTCF0680 | Form | Process IFL Customer Invoice | 10. Object Complete |  | NA | 03.Medium |
| OTCF0460_IP | Form | Form Development for Invoice list. | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCF0054_IP | Form | Customer Billing output (Invoice/ Credit/ Debit/ Proforma Invoice) | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCF0046_IP | Form | Send/Transmit Invoice | 10. Object Complete | NA → NA | NA | 02.High |
| OTCF0004_IP | Form | Order acknowledgment and confirmation to the customer | 10. Object Complete | NA → NA | NA | 02.High |
| OTCE1710 | Enhancement | Addition of Custom Fiori Tile/Dashboard - MRB,Pending,NPR,Freight Determinati... | 07. FUT Roadblock |  | NA | 01.Very High |
| OTCE1709 | Enhancement | Addition of Custom Fiori Tile/Dashboard - Case routing,Required field,Return ... | 06. Dev In Progress |  | NA | 01.Very High |
| OTCE1703 | Enhancement | PRMP Role needs to be sent to CHM from S4 to create Channel Partner Role in CHM | 10. Object Complete |  | NA | 02.High |
| OTCE1668_IP | Enhancement | Enhancement to transfer Customs value from S4 to GTS for Sales orders and del... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1605 | Enhancement | Custom Routine for VAS Billing with Hardware | 10. Object Complete |  | NA | 03.Medium |
| OTCE1585 | Enhancement | Addition of Custom Fiori Tile/Dashboard - EEPM,Decoder,Approval Matrix | 06. Dev In Progress |  | NA | 01.Very High |
| OTCE1505 | Enhancement | Automated Import declaration creation | 10. Object Complete |  | NA | 03.Medium |
| OTCE1421 | Enhancement | Data Enhancement for NL Import Broker | 10. Object Complete |  | NA | 03.Medium |
| OTCE1420 | Enhancement | NL Broker delivery filtration and Import worklist creatio | 10. Object Complete |  | NA | 03.Medium |
| OTCE1248 | Enhancement | IFL Enhancements Add custom fields to enable Dassian flow down | 10. Object Complete |  | NA | 04.Low |
| OTCE1199 | Enhancement | Enhancement to determine PO number based on SoldTo & MMID maintained in a BRF... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1198 | Enhancement | Enhancement to AIF capabilities on access and notifications | 10. Object Complete |  | NA | 02.High |
| OTCE1115 | Enhancement | EMS_Enhancement for S4 validation of hardware and service warranty orders lin... | 10. Object Complete |  | NA | 02.High |
| OTCE1112 | Enhancement | Enhancement to restrict ‘plant code’ changes in sale orders in change mode fo... | 10. Object Complete |  | NA | 04.Low |
| OTCE1110 | Enhancement | Enhancement to determine the correct source system for integrating B-App data... | 10. Object Complete |  | NA | 02.High |
| OTCE1109 | Enhancement | Enhancement to capture the changes in the compliance status of the transactio... | 10. Object Complete |  | NA | 02.High |
| OTCE1108 | Enhancement | 2DN_Enhancement to create KB order from staging table & to update staging tab... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1098 | Enhancement | BOT to extract input and validate mandatory fields and transform the data int... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1097 | Enhancement | BOT to manage ad hoc execution schedules, create an audit trail and capture e... | 10. Object Complete |  | NA | 04.Low |
| OTCE1096 | Enhancement | BOT to orchestrate triggers for its execution, create an audit trail and capt... | 10. Object Complete |  | NA | 02.High |
| OTCE1095 | Enhancement | BOT to manage queue functionality for human approval of the first document of... | 10. Object Complete |  | NA | 01.Very High |
| OTCE1094 | Enhancement | BOT to identify the type of request and open the corresponding Order Type in ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1093 | Enhancement | BOT to manage its execution schedule, create an audit trail and capture evide... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1092 | Enhancement | BOT for extracting input data from email validating mandatory fields and tran... | 10. Object Complete |  | NA | 02.High |
| OTCE1028 | Enhancement | Determine Confirmed Delivery date in sales orders at schedule line level base... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1027 | Enhancement | Enhancement for Sold To and ShipTo determination for SO2 & KB order sales ord... | 10. Object Complete |  | NA | 03.Medium |
| OTCE1026 | Enhancement | Enhancement for copying Data / referencing from SO1 to SO2 for SO PO 2DN model. | 10. Object Complete |  | NA | 03.Medium |
| OTCE0975 | Enhancement | Implementation of an enhancement to restrict deletion of the material line it... | 10. Object Complete |  | NA | 04.Low |
| OTCE0966 | Enhancement | Implementation of an enhancement to add DNI(Do not improve) flag to SO1 after... | 10. Object Complete |  | NA | 04.Low |
| OTCE0965 | Enhancement | Implementation of an enhancement to replicate sales order blocks and holds fr... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0844 | Enhancement | Enhancement to create Fiori report which will expose custom table data (Non d... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0795 | Enhancement | Custom Z table(DH) creation & updates to the outbound order acknowledgements | 10. Object Complete |  | NA | 03.Medium |
| OTCE0794 | Enhancement | BOT for compilation of invoices in scheduled mode using pre-defined template | 10. Object Complete |  | NA | 03.Medium |
| OTCE0742 | Enhancement | Create CHM condition records(ZADC & ZSDC) from Order SIM output | 10. Object Complete |  | NA | 02.High |
| OTCE0741 | Enhancement | Enhancement to standard SAP report V_NLN to generate prices for Order SIM by ... | 10. Object Complete |  | NA | 02.High |
| OTCE0737 | Enhancement | Implement Standard BADI to activate Credit Limit Request Workflow | 10. Object Complete |  | NA | 04.Low |
| OTCE0721 | Enhancement | BOT Enhancement to Bulk Create Credit/Debit | 10. Object Complete |  | NA | 04.Low |
| OTCE0720 | Enhancement | BOT for compilation of invoices in ad-hoc mode to the customer request via e-... | 10. Object Complete |  | NA | 01.Very High |
| OTCE0719 | Enhancement | Utility program for open sales order conversion for IP OM team, that will be ... | 06. Dev In Progress |  | NA | 01.Very High |
| OTCE0718 | Enhancement | Pricing routines for Order SIM price calculations | 10. Object Complete |  | NA | 03.Medium |
| OTCE0715 | Enhancement | PIP 2A1 Interface: Custom Program to update Price catalogue | 10. Object Complete |  | NA | 03.Medium |
| OTCE0714 | Enhancement | Requirement is to Update CPN when there is a change in MMID of SOLI MMID trig... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0713 | Enhancement | IP End customer CI :Custom Validations to be accommodated for Price masking c... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0712 | Enhancement | Sold to party & Ship to party customer codes determination based on DUNS & DU... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0683 | Enhancement | Enhancement request for adding End customer partner in Pricing Catalogue and ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0658 | Enhancement | IP-Intel Federal To capture DPAS Rating from Dassian table on Sales Order and... | 10. Object Complete |  | NA | 04.Low |
| OTCE0654 | Enhancement | Enhancement for idoc validation and creation of custom basic type, segment fo... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0651_IP | Enhancement | Enrich the delivery data transfer data from S/4 IP to GTS with the 'new' vs '... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0650 | Enhancement | Enhancement for Legal Control Exception Scenarios | 10. Object Complete |  | NA | 03.Medium |
| OTCE0642 | Enhancement | Enrich Intrastat dispatch declaration with missing transactions and missing d... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0641 | Enhancement | Enhancement to determine transportation zone based on country key and region ... | 10. Object Complete |  | NA | 04.Low |
| OTCE0640 | Enhancement | Enhancement to support inbound interface 4B3 consignment issue | 10. Object Complete |  | NA | 03.Medium |
| OTCE0614_IP | Enhancement | Implement Standard Credit/Collection BADI | 10. Object Complete |  | NA | 03.Medium |
| OTCE0579 | Enhancement | Enhancement to extend standard table which will record fixed plant and fixed ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0578 | Enhancement | Enhancement to create custom table which will log Blue Yonder Order promiser ... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0577 | Enhancement | List of fields that needs to be mapped to Order promiser Adaptor for order co... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0576 | Enhancement | Enhancement to update the B2B PO number at the return Order | 10. Object Complete |  | NA | 04.Low |
| OTCE0575 | Enhancement | Enhancement to create custom table and field and determining actions on retur... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0524 | Enhancement | Enhancement to support inbound interface from IRC2 (Intel Registration Center... | 10. Object Complete |  | NA | 04.Low |
| OTCE0523 | Enhancement | Enhancement to put user status hold on IRC2 (Intel Registration Center) relev... | 10. Object Complete |  | NA | 04.Low |
| OTCE0522 | Enhancement | Enhancement to put billing block at the line-item level for IRC2 (Intel Regis... | 10. Object Complete |  | NA | 04.Low |
| OTCE0489 | Enhancement | Enhancement to support outbound interface from S4 to IRC2 (Intel registration... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0444 | Enhancement | Credit/Debit Memo Approval Workflow | 10. Object Complete |  | NA | 03.Medium |
| OTCE0443 | Enhancement | Enhancement to include the API custom field, S4 custom fields and append to t... | 10. Object Complete |  | NA | 03.Medium |
| OTCE0440 | Enhancement | Implement NCNR (non-cancellable / non reschedule) and NCNRR (non-cancellable ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0406 | Enhancement | Implement a warning and hold for the sales order line item having material wi... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0404 | Enhancement | Enhancement to capture business rules for entitlement and Warranty of return ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0398_IP | Enhancement | Enhance data transfer from SAP S4/HANA to SAP GTS for Customs Declaration Cre... | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0191 | Enhancement | Generate Order e-Ack’s in sales order to customer in accordance with specific... | 10. Object Complete | NA → NA | NA | 04.Low |
| OTCE0088 | Enhancement | Determine sale orders to trigger availability check with BY | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0087 | Enhancement | Implement sales order cancellation control on order changes through B2B & WOM | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0086 | Enhancement | Implement Minimum order quantity (MOQ) and Delivery unit increment check vali... | 10. Object Complete | NA → NA | NA | 04.Low |
| OTCE0084 | Enhancement | Notification when Multiple Schedule lines are created | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0083 | Enhancement | Price Swamp program for order repricing | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0080 | Enhancement | IP: Pricing Date determination based on RGID and CGID | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCE0079 | Enhancement | Implement duplicate PO check validations for order create and change | 10. Object Complete | NA → NA | NA | 04.Low |
| OTCE0021 | Enhancement | Credit hold release dashboard at line-item level | 10. Object Complete | NA → NA | NA | 01.Very High |
| OTCE0002_IP | Enhancement | Populate Incoterms and Shipping conditions from Ship to party | 10. Object Complete | NA → NA | NA | 03.Medium |
| OTCC1341 | Conversion | Payer Profile Data Conversion | 10. Object Complete |  | NA | 03.Medium |
| OTCC1340 | Conversion | Payer Segment Data Conversion | 10. Object Complete |  | NA | 03.Medium |
| OTCC1339 | Conversion | Payer Relationship Data Conversion | 10. Object Complete |  | NA | 03.Medium |
| OTCC1232 | Conversion | Intel Federal Data conversion for Contract ITD costs | 10. Object Complete |  | NA | 03.Medium |
| OTCC1231 | Conversion | Intel Federal Data conversion for Bill Plans | 10. Object Complete |  | NA | 03.Medium |
| OTCC1229 | Conversion | Data conversion of open Federal Contracts from ECC to Dassian S4. | 10. Object Complete |  | NA | 03.Medium |
| OTCC1228 | Conversion | Data conversion for Federal Contracts - Contract Fees/Retention/Incentive Fee... | 10. Object Complete |  | NA | 03.Medium |
| OTCC1227 | Conversion | Data conversion for Intel Federal Contract WBS Assignments | 10. Object Complete |  | NA | 03.Medium |
| OTCC0803 | Conversion | Open Credit Case Conversion | 10. Object Complete |  | NA | 02.High |
| OTCC0802 | Conversion | Custom Z table(DH) DH tables data conversion from ECC to S4 for IP | 10. Object Complete |  | NA | 02.High |
| OTCC0717 | Conversion | Pricing Condition records conversion | 10. Object Complete |  | NA | 01.Very High |
| OTCC0679 | Conversion | Open Dispute Case Conversion | 10. Object Complete |  | NA | 02.High |
| OTCC0678 | Conversion | Collection Master Conversion | 10. Object Complete |  | NA | 02.High |
| OTCC0636 | Conversion | Output Condition (Sales) Conversion for IP R3 release | 10. Object Complete |  | NA | 01.Very High |
| OTCC0564 | Conversion | Customer Material Info Record Conversion for IP R3 release | 10. Object Complete |  | NA | 03.Medium |
| OTCC0563 | Conversion | Open Sales Order Conversion for IP R3 release | 10. Object Complete |  | NA | 02.High |
| LOGR1252 | Report | 2DN - Inbound Escort Report | 10. Object Complete |  | NA | 02.High |
| LOGR1236 | Report | 2DN - Outbound Escort Report | 06. Dev In Progress |  | NA | 02.High |
| LOGR1173 | Report | 2DN - Outbound Manifest Report | 10. Object Complete |  | NA | 03.Medium |
| LOGR1172 | Report | 2DN - Inbound Manifest Report | 10. Object Complete |  | NA | 03.Medium |
| LOGM007_IP | Conversion | Storage Bin Upload | 10. Object Complete | WIINGS → EWM | NA | N/A |
| LOGM006_IP | Conversion | Product Master conversion (additional EWM attribution) | 10. Object Complete | WIINGS, ECC WM → EWM | NA | N/A |
| LOGI1534_IP | Interface | BRF+ Extractor( API interface) to fetch the data saved in the BRF+ decision t... | 10. Object Complete |  | NA | 03.Medium |
| LOGI1312 | Interface | Label printing data in XML format from SAP EWM to Spectrum/Loftware | 10. Object Complete | S/4 → SPECTRUM | NA | 02.High |
| LOGI1300 | Interface | Discrepancy check for FAC receipts | 10. Object Complete |  | MULESOFT | 02.High |
| LOGI1271 | Interface | Duplicate ULT checks for Non-CPU returned products | 10. Object Complete | S/4 → ECA | NA | 02.High |
| LOGI1270 | Interface | IWRAP interface for CWP availibilty check(Inbound interface) | 10. Object Complete | IWRAP → S/4 | APIGEE | 02.High |
| LOGI1263 | Interface | Retrieve the GES scanned CPU entitlement check details | 10. Object Complete | Entitlement Orchestration Layer → S/4 | NA | 02.High |
| LOGI1262 | Interface | Entitlement Output processing to perform discrepancy checks | 10. Object Complete | Entitlement Orchestration Layer → S/4 | NA | 03.Medium |
| LOGI1261 | Interface | Discrepancy resolution results to be sent from Salesforce to SAP | 10. Object Complete | SalesForce → S/4 | APIGEE | 03.Medium |
| LOGI1067 | Interface | 2DN - S4 – Interface from S/4 to MPL for packing list. | 10. Object Complete | S/4 → MPL | SFT | 03.Medium |
| LOGI1066 | Interface | 2DN - Interface to capture Data for 1st Delivery in 2DN X-Dock Model | 10. Object Complete |  | MULESOFT | 03.Medium |
| LOGI0875 | Interface | Interface from WOM to S4 HANA to fetch the list of Deliveries for a particula... | 10. Object Complete | WOM → S/4 | MULESOFT | 03.Medium |
| LOGI0874 | Interface | Interface from WOM to S4 HANA to fetch the ASN information of delivery. | 10. Object Complete | WOM → S/4 | MULESOFT | 02.High |
| LOGI0842_IP | Interface | Interface from SAP S4 to DBaaS to Fetch Actual COF for FVR batch and COA for ... | 10. Object Complete | S/4 → DBaaS | MULESOFT | 03.Medium |
| LOGI0800_IP | Interface | Interface to send shipment information to custom broker | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0664 | Interface | Trigger ZCUS (export customs clearance output) and ZXCI to send outputs - ZSI... | 10. Object Complete | S/4 → OpenText | MULESOFT | 02.High |
| LOGI0663_IP | Interface | Trigger ZCUS (export customs clearance output) and ZXCI to send outputs - ZSI... | 10. Object Complete |  | MULESOFT | 02.High |
| LOGI0630_IP | Interface | TM - GTT: GXS sending carrier events back to GTT app “Shipment Tracking”. IP | 10. Object Complete |  | NA | 03.Medium |
| LOGI0612_IP | Interface | Customer ASN interface from outbound delivery | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0610 | Interface | 3B2 Post goods issue interface for Outbound delivery to SAP | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0609 | Interface | 3B13 interface for pick/pack updates for outbound delivery to SAP | 10. Object Complete | S/4 → OpenText | MULESOFT | 03.Medium |
| LOGI0607 | Interface | 3B14R Cancellation Request from S/4 to 3PL | 10. Object Complete | S/4 → 3PL | MULESOFT | 03.Medium |
| LOGI0418 | Interface | 3B12 Request to 3PL on FO creation | 10. Object Complete | 3PL → S/4 | MULESOFT | 02.High |
| LOGI0415 | Interface | 3B14C Cancellation Confirmation from 3PL to S/4 | 10. Object Complete | 3PL → S/4 | MULESOFT | 03.Medium |
| LOGF1632 | Form | TM:Trigger order details/collection details email from a freight order to the... | 10. Object Complete |  | NA | 03.Medium |
| LOGF1630 | Form | COO Label - print a Country of Origin (COO) label for the outbound shipment o... | 10. Object Complete |  | NA | 03.Medium |
| LOGF1583 | Form | Consolidated Export Commercial Invoice – Finished Goods (IP) | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF1283 | Form | Packing list form for IP returns (outbound) | 10. Object Complete |  | NA | 03.Medium |
| LOGF1282 | Form | Commercial invoice form for IP returns (outbound) | 10. Object Complete |  | NA | 03.Medium |
| LOGF1258 | Form | Commercial invoice form for returns logistics | 10. Object Complete |  | NA | 02.High |
| LOGF1257 | Form | Packing list form for Returns Logistics | 10. Object Complete |  | NA | 02.High |
| LOGF1224 | Form | Enhancement to create Scrapping form Document | 10. Object Complete |  | NA | 03.Medium |
| LOGF1220 | Form | Enhancement to generate Shipping labels | 10. Object Complete |  | NA | 03.Medium |
| LOGF1219 | Form | Enhancement to create Physical inventory form | 10. Object Complete |  | NA | 03.Medium |
| LOGF1216 | Form | Enhancement to generate picklist | 10. Object Complete |  | NA | 03.Medium |
| LOGF1149_IP | Form | Consolidated Packing list for Chengdu | 10. Object Complete |  | NA | 02.High |
| LOGF0805 | Form | EIAJ form to be generated for OEM customers (Japan) | 10. Object Complete |  | NA | 02.High |
| LOGF0353_IP | Form | Generate Consolidated Export Commercial Invoice - Finished Goods (IF and IP) | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0349_IP | Form | ISM - Generate Packing List - IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0348_IP | Form | Shipper Letter of instruction (Localization requirement for US) | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0345_IP | Form | Bailment CI and End-Customer CI for IF/IP | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0344_IP | Form | Generate Export CI for IF/IP | 10. Object Complete | NA → NA | NA | 02.High |
| LOGF0343_IP | Form | Generate Itemised Packing Lists | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGF0342_IP | Form | Generate Packing Lists for Finished Goods - IP and IF | 10. Object Complete | NA → NA | NA | 02.High |
| LOGE1713 | Enhancement | Copy Control Routine for Customer Master Special Instructions | 08. FUT In Progress |  | NA | 03.Medium |
| LOGE1609 | Enhancement | Enhancement for Fiori App development to maintain business rules for Dynamic ... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1608 | Enhancement | Enhancement for Fiori App development to maintain business rules for Static D... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1567 | Enhancement | TM - GTT: SAP S/4 Return Deliveries relevant for TM are not propagating to BN... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1535 | Enhancement | New custom Fiori application for Undo Disposition and Confirm Disposition | 06. Dev In Progress |  | NA | 02.High |
| LOGE1509_IP | Enhancement | Tendering- FIORI app for Approval Hierarchy (Assign Delegate) | 10. Object Complete |  | NA | 04.Low |
| LOGE1507 | Enhancement | Custom enhancement to enable the integration of both IF(BI1) /IP(DI0) TM syst... | 10. Object Complete |  | NA | 02.High |
| LOGE1488_IP | Enhancement | Invoice notification- Notification to carrier for POD and internal notificati... | 10. Object Complete |  | NA | 02.High |
| LOGE1487_IP | Enhancement | Carrier notification- Carrier contact table BRF+ maintenance | 10. Object Complete |  | NA | 02.High |
| LOGE1486_IP | Enhancement | Carrier notification- Cancellation email | 10. Object Complete |  | NA | 02.High |
| LOGE1485_IP | Enhancement | Carrier notification- Acceptance and Rejection email | 10. Object Complete |  | NA | 02.High |
| LOGE1484_IP | Enhancement | Invoice notification- Notification to carrier for Invoice | 10. Object Complete |  | NA | 02.High |
| LOGE1483_IP | Enhancement | Invoice notification- Notification to carrier for dispute | 10. Object Complete |  | NA | 02.High |
| LOGE1482_IP | Enhancement | Tendering- Internal Notification mail | 10. Object Complete |  | NA | 03.Medium |
| LOGE1481_IP | Enhancement | Tendering- Approval Process with Purchase group determination | 10. Object Complete |  | NA | 03.Medium |
| LOGE1462_IP | Enhancement | TM - GTT: Send Event # Estimated Time of Arrival (ETA) as a separate event fr... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1461_IP | Enhancement | TM - GTT: To propagate events to S/4 TM Freight order reported by GXS by Bypa... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1460_IP | Enhancement | TM - GTT: Additional field needs to be captured in S/4 TM Freight Order “Note... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1459_IP | Enhancement | TM - GTT: Additional field values sent by carrier through GXS are required in... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1316 | Enhancement | Mass Upload Program for HAWB/MAWB/ETA update in Freight order | 10. Object Complete |  | NA | 02.High |
| LOGE1314 | Enhancement | Enhancement to create Credit Memo Request for the Goods Receipt quantity on p... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1311 | Enhancement | Virtual Receiving | 10. Object Complete |  | NA | 03.Medium |
| LOGE1310 | Enhancement | Batch job to determine disposition based on static disposition rule table | 10. Object Complete |  | NA | 03.Medium |
| LOGE1301 | Enhancement | Enhancement for updating HAWB (House Air waybill) information in EWM Transpor... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1298 | Enhancement | Receiving unexpected returned products in the Custom Receiving Screen | 10. Object Complete |  | NA | 02.High |
| LOGE1297_IP | Enhancement | Disable the Amount field within Subcontracting tab in Freight Order for CW Lo... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1281 | Enhancement | Batch job to determine disposition based on dynamic disposition rule table | 10. Object Complete |  | NA | 03.Medium |
| LOGE1280 | Enhancement | Custom screen to request assignment of OPID to planner and capture the detail... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1277 | Enhancement | Generate Docking report | 10. Object Complete |  | NA | 02.High |
| LOGE1269 | Enhancement | To Perform Undisposition for already dispositioned RMA | 10. Object Complete |  | NA | 01.Very High |
| LOGE1268 | Enhancement | Enhancement to create Ship instruction screen.​ | 10. Object Complete |  | NA | 03.Medium |
| LOGE1266 | Enhancement | Custom Receiving screen (ZPRDI) to have functionalities to process receiving ... | 10. Object Complete |  | NA | 01.Very High |
| LOGE1265 | Enhancement | Custom screen to capture shipment unloading details (Docking) | 10. Object Complete |  | NA | 02.High |
| LOGE1260 | Enhancement | Resolution for Discrepancy to be determined based on Business Rules | 10. Object Complete |  | NA | 01.Very High |
| LOGE1256_IP | Enhancement | TM - GTT: Document type T54 (House Airway Bill) number to GTT | 10. Object Complete |  | NA | 03.Medium |
| LOGE1251_IP | Enhancement | More determinization of input entry criteria to be added for dedicated carrie... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1250_IP | Enhancement | Creating new Carrier selection strategy methods ZPRE_TAL and ZPOST_TAL to cal... | 10. Object Complete |  | NA | 03.Medium |
| LOGE1221 | Enhancement | Custom Fiori screen to capture shipping details and start the shipping process. | 10. Object Complete |  | NA | 02.High |
| LOGE1214 | Enhancement | Update price variance category and its reason in Difference Analyzer | 10. Object Complete |  | NA | 03.Medium |
| LOGE1197_IP | Enhancement | Carrier notification- Tendering initiation email | 10. Object Complete |  | NA | 02.High |
| LOGE1196_IP | Enhancement | Invoice notification- Notification to carrier for POD and internal notificati... | 10. Object Complete |  | NA | 02.High |
| LOGE1150 | Enhancement | TM:Custom BRF+ table for choosing the right the MTR ( Means of transport) dur... | 10. Object Complete |  | NA | 04.Low |
| LOGE1148 | Enhancement | 2DN - Trigger Auto packing in 2nd DN of 2DN X-Dock Model | 10. Object Complete |  | NA | 03.Medium |
| LOGE1147 | Enhancement | 2DN - S4 – Error Handling program in 2DN X-Dock Model | 10. Object Complete |  | NA | 02.High |
| LOGE1130 | Enhancement | Enhancement to Re-Plan the De-linked Freight Units based on Hawb Numbers | 10. Object Complete |  | NA | 02.High |
| LOGE1116 | Enhancement | 2DN - Enhancement to capture required fields of 1st Delivery in 2DN X-Dock Model | 10. Object Complete |  | NA | 03.Medium |
| LOGE1114 | Enhancement | 2DN - Post 3PL 3B2 or manual Goods Issue from CW or IW - Wrapper Program to c... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0979 | Enhancement | Pre-alert summary report for the EMEA customer | 10. Object Complete |  | NA | 03.Medium |
| LOGE0838 | Enhancement | Enhancement to update the address and bp form the Custom Partner Function to ... | 10. Object Complete |  | NA | 04.Low |
| LOGE0797_IP | Enhancement | Pre alert notification to Customer | 10. Object Complete |  | NA | 03.Medium |
| LOGE0796_IP | Enhancement | Custom transaction to trigger CUSDEC | 10. Object Complete |  | NA | 02.High |
| LOGE0793 | Enhancement | Upload program to update pick/pack information in sap in case of 3B13 PIP fai... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0792_IP | Enhancement | Enhancement to Update Custom Table form Master data and Manage SOP Data Commu... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0791_IP | Enhancement | Creation of Proforma Invoice ZF8 from Freight Order and Save ITN Number in De... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0772_IP | Enhancement | Develop Fiori app to View/Edit/Add SOP data(CMDB). | 10. Object Complete |  | NA | 02.High |
| LOGE0766_IP | Enhancement | TM - GTT: Routing of events from GTT to correct S4 system | 10. Object Complete |  | NA | 03.Medium |
| LOGE0765_IP | Enhancement | Calling a new BRF+ for Carrier exclusion during Carrier Selection process. Eg... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0690 | Enhancement | TM - GTT: Boundary App - MySample for GTT: re-purposing. Applicable for Intel... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0673_IP | Enhancement | Data code extractor to be extended on S4 TM side​ | 10. Object Complete |  | NA | 03.Medium |
| LOGE0632_IP | Enhancement | TM: Custom Determination Class to access Source and Destination country in FU... | 10. Object Complete |  | NA | 04.Low |
| LOGE0631 | Enhancement | TM - GTT: ETA calculated date to be captured in GTT Delivery App. IP | 10. Object Complete |  | NA | 04.Low |
| LOGE0628_IP | Enhancement | CRF freight orders, should have a custom event type “Shipped –CRF". This cust... | 10. Object Complete |  | NA | 04.Low |
| LOGE0627 | Enhancement | TM - GTT: Boundary App - WOM fields in GTT for WOM/MySample re-purposing. App... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0626_IP | Enhancement | FO subcontracting screen for tendering enhancement. Fields include- send for ... | 10. Object Complete |  | NA | 04.Low |
| LOGE0625_IP | Enhancement | Tendering- FIORI app for Approval Hierarchy (Assign Delegate) | 10. Object Complete |  | NA | 04.Low |
| LOGE0613 | Enhancement | Development of LCSR tool in Fiori | 10. Object Complete |  | NA | 01.Very High |
| LOGE0611 | Enhancement | 1. Custom fields in Delivery to store Number of Pallets & IPLA indicator fiel... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0608 | Enhancement | Custom logic to fetch the details from different source and save in the custo... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0581 | Enhancement | Incoterm Location 1 ID field update for Outbound delivery | 10. Object Complete |  | NA | 04.Low |
| LOGE0547_IP | Enhancement | Mass upload – Custom TM program for below items. Resource Downtime upload.Not... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0546_IP | Enhancement | Mass upload – Custom TM program for below items. Schedule and Default Routes ... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0514 | Enhancement | After 3B13 is triggered and Pick & Pack is completed in deliveries, and the H... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0513 | Enhancement | After 3B12 is triggered and YDN0 output type is triggered in the deliveries, ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0512 | Enhancement | Update Freight Order Number to the delivery documents after carrier is assign... | 10. Object Complete | ECD → S4 | NA | 03.Medium |
| LOGE0511_IP | Enhancement | Mass upload – Custom TM program for below items. Mass upload program to creat... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0510 | Enhancement | TM: To show TPT of each stage in a multileg Shipment (Default Routes) and fil... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0478_IP | Enhancement | Generate Automated Carrier Pre-Alert (ZPRC) from SAP TM. | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0459_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0458_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0457_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection -Custom Stra... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0456_IP | Enhancement | In SAP TM, Custom carrier selection strategy - Carrier Selection UI enhanceme... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0455 | Enhancement | In SAP TM, Post schedule lines updated, enhancement to unblock the Freight unit | 10. Object Complete |  | NA | 03.Medium |
| LOGE0454 | Enhancement | In SAP TM, Enhancement to add a Planning Block in the Freight Unit with the B... | 10. Object Complete |  | NA | 03.Medium |
| LOGE0453 | Enhancement | In SAP TM, When the Incoterm Location1 ID field is populated in the delivery ... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0402 | Enhancement | In SAP TM, Goods Value to be populated in the Alternate Quantity in the Freig... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0341_IP | Enhancement | Billing document creation to be triggered from the Output of outbound delivery | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGE0281_IP | Enhancement | Add custom fields Customer Window, Back Dated order fields in Freight Unit St... | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0065_IP | Enhancement | Create single line delivery for a confirmed sales order confirmed schedule line | 10. Object Complete | NA → NA | NA | 04.Low |
| LOGE0064_IP | Enhancement | Add custom fields Customer Window, Back Dated order fields(And its date chang... | 10. Object Complete | NA → NA | NA | 03.Medium |
| LOGC1313 | Conversion | Conversion of stock upload program | 10. Object Complete |  | NA | 03.Medium |

**Summary**: 5 Reports, 71 Interfaces, 20 Conversions, 167 Enhancements, 28 Forms, 1 Workflows

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for GT-010:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.




#### Platform Inventory

Platform landscape inferred from integrated systems for GT-010:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
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

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| OTCW1683 | Additional WRICEF for Credit Limit Request Workflow | Dec-25 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 1. On Track |
| OTCR0967 | Developing a report for the 2DN model where we can view the E2E flow in one r... | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | 1. On Track |
| OTCM028_IP | Open Quantity Contract | Feb-25 (100%) | — | — | Feb-25 (100%) |  |
| OTCI1721 | Outbound Interface changes to send data from S4 to SF | Feb-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1720 | Inbound Interface to Update Original Flag Interface from SFDC to S4. | Feb-26 (100%) | Feb-26 (100%) | Feb-26 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1649 | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1648 | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1598 | An outbound Interface to Read the EEPM and DECODER Matrix from S4 to OL | Sep-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1568 | Inbound Interface from WOM to S4 HANA to send Shipment and tracking information | Aug-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Nov-25 (100%) | 1. On Track |
| OTCI1498 | Inbound Interface from WOM to S4 HANA to send Customer Hierarchy | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Sep-25 (100%) |  |
| OTCI1423 | Service Interface and Enhancement of the outbound proxy sent to NL brokers - ... | Jul-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Mar-26 (100%) | 3. Off Track |
| OTCI1259 | Outbound interface from S4 HANA to WOM to send the product information | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCI1192 | Interface for BP Status query in GTS - CAAS | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1191 | Interface for Transactional status query in GTS - CAAS | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1190 | Interface for Product Create/ Change in GTS - CAAS | May-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Dec-25 (100%) | 2. At Risk |
| OTCI1189 | Interface for Product Classification Query in GTS - CAAS | Jun-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1188 | Interface for Transactional Create/ Change in GTS - CAAS | May-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Feb-26 (100%) | 2. At Risk |
| OTCI1187 | Interface for BP Create/ Change in GTS - CAAS | May-25 (100%) | Oct-25 (100%) | Oct-25 (100%) | Dec-25 (100%) | 4. Completed |
| OTCI1180 | EMS_Inbound Interface for Capturing Hardware SO and Line-Item Details into se... | Jun-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Nov-25 (100%) | 4. Completed |
| OTCI1179 | EMS_Outbound interface to OL (Orchestration layer) for activation key generat... | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Nov-25 (100%) | 4. Completed |
*... and 272 more objects (see full Object Tracker)*

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
<div style="page-break-before: always;"></div>
<div class="page-section">


### 7.2 RAID Log

Standard RAID items for GT-010 (Order To Cash (IP)):

| # | Category | Description | Status | Owner | Priority |
|---|----------|-------------|--------|-------|----------|
| 1 | Risk | Data migration completeness — validate all legacy Manage Global Trade Master Data (IP) data maps to S/4 target structures | Open | Tower Architect | High |
| 2 | Risk | Integration testing coverage — ensure all 0 integrated systems are validated end-to-end | Open | Integration Lead | High |
| 3 | Assumption | Target SAP S/4HANA system available in DEV/QAS per release schedule | Active | SAP Basis | Medium |
| 4 | Issue | API access provisioning — SAP OData, Smartsheet, and IAPM API credentials required for automation | Open | EA Pipeline Team | High |
| 5 | Dependency | Upstream BPMN process models validated and signed off by business process owners | Active | Process Owner | Medium |

> *Live RAID data will be auto-populated from the Smartsheet RAID log via API integration.*

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*GT-010 — Architecture Document (TOGAF BDAT) · Order To Cash (IP) · Generated: March 2026*
<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>GT-010 — Manage Global Trade Master Data (IP)</span></div>
</div>
