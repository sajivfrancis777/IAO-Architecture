<div style="text-align:center; padding-top:20px;">
  <img src="../../../../../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">MDM-130 — Create and Maintain Customers</h1>
  <h2 style="font-size:24px;">Architecture Document (TOGAF BDAT)</h2>
  <p style="font-size:18px; color:#555;">Master Data (MDM) Tower<br/>
  Capability MDM-130 · MDM Manage Master Data</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
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

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

## 1. Executive Summary

This Architecture Document defines the **Business, Data, Application, and Technology** (BDAT) architecture for **MDM-130 Create and Maintain Customers** within the IAO program.
| Dimension | Value |
|-----------|-------|
| **Tower** | Master Data (MDM) |
| **Process Group** | MDM Manage Master Data |
| **Capability** | MDM-130 - Create and Maintain Customers |
| **Release** | Release 3 |
| **Total Systems** | 0 |
| **System Status** | 0 Deployed, 0 Developing, 0 EOL, 0 Pending IAPM |
| **RICEFW Objects** | 5 Reports, 30 Interfaces, 40 Conversions, 61 Enhancements, 10 Workflows |
**Change Summary**: 0 new flow chains, 0 removed, 0 modified, 0 unchanged between Current-State and Future-State states.

> All system nodes in architecture diagrams are **IAPM-linked** — click any node to open its IAPM page. Diagrams require `securityLevel: 'loose'` for click events.

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

## 2. Business Context & Objectives

### 2.1 Classification

| Level | Value |
|-------|-------|
| **L0 Tower** | Master Data |
| **L1 Process** | MDM Manage Master Data |
| **L2 Capability** | MDM-130 - Create and Maintain Customers |

### 2.2 Business Drivers

| # | Driver | Description | Strategic Alignment | Priority |
|---|--------|-------------|---------------------|----------|
| 1 | Master Data Governance | Establish single source of truth for vendor, customer, material, and BOM master data | IDM 2.0 Data Foundation | High |
| 2 | Data Quality Improvement | Implement data quality rules and automated validation for master data creation and changes | Data Governance | High |
| 3 | Cross-System Data Synchronization | Ensure master data consistency across S/4 HANA, MDG, and downstream systems | Enterprise Integration | Medium |
| 4 | MDM-130 Process Migration | Migrate Create and Maintain Customers business processes and 0 integrated systems from legacy to S/4 HANA target architecture | IDM 2.0 Master Data | High |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

### 2.3 Success Criteria

| Metric | Target | Measure | Baseline | Owner |
|--------|--------|---------|----------|-------|
| Master Data Accuracy | > 99% | Master data records passing automated quality validation rules | 94% (current) | Data Governance Lead |
| Data Creation Lead Time | < 4 hours | Vendor/customer/material master data creation cycle time | 2 business days (current) | MDM Operations |
| Data Sync Latency | < 15 minutes | Time for master data changes to propagate to all consuming systems | 4 hours (batch) | Integration Lead |
| MDM-130 Migration Completeness | 100% flow chains validated | All 0 flow chains verified in target state | 0% (pre-migration) | Tower Architect |

### 2.4 Companion Documents

| Document | Description |
|----------|-------------|
| **Business Architecture** | Included in this document (Section 3) — process flows from BPMN diagrams |
| **This Document** | Full BDAT Architecture — Business + Data + Application + Technology |

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

## 3. Business Architecture (TOGAF "B")

### 3.1 Business Process Overview

*(No BPMN files found in input/bpmn/ for this capability.)*

### 3.3 Business Roles & Responsibilities

| Role / Lane | Processes Involved | Description |
|------------|-------------------|-------------|
| Business Process Owner | MDM-130 | Accountable for Create and Maintain Customers business process definition and sign-off |
| Functional Analyst | MDM-130 | Responsible for functional specification and test case design |
| Technical Developer | MDM-130 | Responsible for RICEFW build and unit testing |
| Integration Architect | MDM-130 | Designs and validates integration patterns and middleware flows |

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

## 4. Data Architecture (TOGAF "D")

### 4.1 Data Entities & Ownership

The following data entities are derived from the system integration flows for MDM-130. Tower architects should validate ownership and classification.

| # | Data Entity | Source System | Target System | Data Owner | Classification | Volume | Master/Transaction |
|---|-------------|---------------|---------------|------------|----------------|--------|-------------------|

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

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
| MDCR0025 | Report | Alternate/Preferred BOM Component Change in S4 | 09. FUT Overdue | MDG |  | 03.Medium |
| DATR1430 | Report | Cost Center Approvers report by Supergroup, Group, Division, Subdivision, CCR... | 10. Object Complete |  |  | 03.Medium |
| DATR0787 | Report | Report to send notification to Direct managers about the inactive Cost Center... | 10. Object Complete |  |  | 03.Medium |
| DATR0390_IP | Report | Data Monitor Report between MDG and Reltio | 10. Object Complete | NA | NA | 03.Medium |
| DATR0389_IP | Report | Customer Master Operational Report | 10. Object Complete | NA | NA | 03.Medium |
| MDGM1332 | Conversion | IMO Materials | 10. Object Complete |  |  | N/A |
| DATC1663 | Conversion | Product Hierarchy File 1 and File 2 | 10. Object Complete |  |  | 02.High |
| DATC1640 | Conversion | Material Master MRP View WINGS Conversion | 10. Object Complete |  |  | 04.Low |
| DATC1639 | Conversion | Material Master Plant and Storage Location View WINGS Materials Conversions | 10. Object Complete |  |  | 04.Low |
| DATC1638 | Conversion | Material Master Accounting and Costing View WINGS Materials Conversions | 10. Object Complete |  |  | 04.Low |
| DATC1637 | Conversion | Material Master Purchasing View WINGS Materials Conversions | 10. Object Complete |  |  | 04.Low |
| DATC1617 | Conversion | HAZMAT Profile Conversion | 10. Object Complete |  |  | 03.Medium |
| DATC1604 | Conversion | Initial Load for Objects & Relationships | 10. Object Complete |  |  | 03.Medium |
| DATC1556 | Conversion | Conversion program to load Images of Products in Material Master | 10. Object Complete |  |  | 03.Medium |
| DATC1552 | Conversion | edFIT - PSI BOM Conversion | 03. FS Not Started |  |  | 03.Medium |
| DATC1551 | Conversion | edFIT - Material Master Conversion | 04. FS In Progress |  |  | 03.Medium |
| DATC1237 | Conversion | Material Master Data – Quality Management View Conversion | 10. Object Complete |  |  | 03.Medium |
| DATC1204 | Conversion | Load Vendor as Customer to MDG System | 10. Object Complete |  |  | 03.Medium |
| DATC0859 | Conversion | Convert the Customer Master Contact Person from ECC system to MDG system_IP | 10. Object Complete |  |  | 03.Medium |
| DATC0589 | Conversion | Vendor Master : General Data conversion from ECC to MDG | 10. Object Complete |  |  | 02.High |
| DATC0588 | Conversion | Vendor Master : Company Code Data conversion from ECC to MDG | 10. Object Complete |  |  | 03.Medium |
| DATC0587 | Conversion | Vendor Master : Purchase Org conversion from ECC to MDG | 10. Object Complete |  |  | 03.Medium |
| DATC0586 | Conversion | Vendor Master : Partner Function conversion from ECC to MDG | 10. Object Complete |  |  | 02.High |
| DATC0585 | Conversion | Vendor Master : Tax Data conversion from ECC to MDG | 10. Object Complete |  |  | 03.Medium |
| DATC0584 | Conversion | Vendor Master : Bank Data conversion from ECC to MDG | 10. Object Complete |  |  | 03.Medium |
| DATC0583 | Conversion | Initial load of HRMM data from WCDS to MPipe system, The initial data load wi... | 10. Object Complete | RELTIO | S4 | 02.High |
| DATC0562 | Conversion | Conversion of DUNS table from ECC to S/4 for IP | 10. Object Complete |  |  | 03.Medium |
| DATC0553 | Conversion | Conversion of BOM from SPEED to S4 IF | 10. Object Complete |  |  | 01.Very High |
| DATC0552 | Conversion | Conversion of BOM from SPEED to S4 IP | 10. Object Complete |  |  | 01.Very High |
| DATC0213 | Conversion | Material Master-Work scheduling view | 10. Object Complete |  |  | 03.Medium |
| DATC0184_IP | Conversion | Convert the Customer Master Partner Function view from ECC system to MDG syst... | 10. Object Complete | NA | NA | 03.Medium |
| DATC0182_IP | Conversion | Convert the General data view from ECC system to MDG system_IP. | 10. Object Complete | NA | NA | 03.Medium |
| DATC0179_IP | Conversion | Convert the Customer Master Sales view from ECC system to MDG system_IP. | 10. Object Complete | NA | NA | 03.Medium |
| DATC0178_IP | Conversion | Convert the Customer Master Tax view from ECC system to MDG system_IP. | 10. Object Complete | NA | NA | 04.Low |
| DATC0120_IP | Conversion | Convert the Customer Master Company Code view from ECC system to MDG system_IP. | 10. Object Complete | ECC | MDG | 04.Low |
| DATC0118_IP | Conversion | Convert the Customer Master In House Cash view from ECC system to MDG system_IP. | 10. Object Complete | ECC | MDG | 03.Medium |
| DATC0076_IP | Conversion | Material Master-Classification View | 10. Object Complete |  |  | 03.Medium |
| DATC0075_IP | Conversion | Material Master-Accounting & Costing view | 10. Object Complete |  |  | 03.Medium |
| DATC0074_IP | Conversion | Material Master-Sales Org Views and Sales Text | 10. Object Complete |  |  | 03.Medium |
| DATC0073 | Conversion | Material Master-Warehouse Mgmt Views | 10. Object Complete |  |  | 04.Low |
| DATC0072 | Conversion | Material Master-Purchasing View and PO Text | 10. Object Complete |  |  | 03.Medium |
| DATC0071_IP | Conversion | Material Master-MRP View | 10. Object Complete |  |  | 04.Low |
| DATC0070_IP | Conversion | Material Master-Plant Data/Storage Views | 10. Object Complete |  |  | 03.Medium |
| DATC0069_IP | Conversion | Material Master-Alt UOM | 10. Object Complete |  |  | 04.Low |
| DATC0068_IP | Conversion | Material Master-Basic Data- (including description) Views | 10. Object Complete |  |  | 03.Medium |

### 4.5 Data Governance & Quality

| Concern | Approach |
|---------|----------|
| Data Ownership | Per-entity owners listed in Section 3.1 |
| Data Classification | Financial data classified as Intel Confidential |
| Data Retention | Per Intel corporate retention policies |
| Data Quality | Validated at source; reconciliation at target |

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

## 5. Application Architecture (TOGAF "A")

### 5.1 Current-State — Current-State Application Landscape

#### Overview

The Current-State architecture represents the **current / legacy** landscape for MDM-130.

#### Current-State Flow Narrative

*(No current-state flows defined.)*

### 5.2 Future-State — Future-State Application Landscape

#### Overview

The Future-State architecture represents the **target** landscape for MDM-130.

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

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

### 5.5 RICEFW Inventory

| Object ID | Type | Description | Status | Source → Target | Middleware | Complexity |
|-----------|------|-------------|--------|----------------|-----------|-----------|
| MDGM1332 | Conversion | IMO Materials | 10. Object Complete |  | NA | N/A |
| MDCR0025 | Report | Alternate/Preferred BOM Component Change in S4 | 09. FUT Overdue | MDG | NA | 03.Medium |
| MDCE0024 | Enhancement | Supplier Hierarchy | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0023 | Enhancement | Sales Organization - Extended Itego datamodel + UI to govern assignment to Sa... | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0022 | Enhancement | Sales Region - Custom Itego Object to govern Sales Regions | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0021 | Enhancement | Customer Planning Hierarchy -IF | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0020 | Enhancement | Customer Planning Hierarchy -IP | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0019 | Enhancement | Product Planning Hierarchy -IF | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0018 | Enhancement | Product Planning Hierarchy -IP | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0017 | Enhancement | Commodity- Custom Itego Object with ~100 customer fields + UI to support gove... | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0015 | Enhancement | Asset Location - Extended Itego datamodel with 22 custom fields + UI to suppo... | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0014 | Enhancement | Storage Location - Extended Itego datamodel with 11 custom fields + UI to sup... | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0013 | Enhancement | Plant - Extended Itego datamodel with 13 custom fields + UI to support govern... | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0012 | Enhancement | Sales Org Association - Custom Itego Object with 4 customer fields + UI to su... | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0011 | Enhancement | Holiday Calendar - Custom goveranance | 10. Object Complete | MDG | NA | 03.Medium |
| MDCE0009 | Enhancement | Shipping Point- Custom Itego Object with 6 customer fields + UI to support go... | 10. Object Complete | MDG | NA | 03.Medium |
| DATW1205 | Workflow | Vendor as Customer Workflow | 10. Object Complete |  | NA | 03.Medium |
| DATW1203 | Workflow | Workflow Setup for Mark For Delete Reference Material Governance Process | 10. Object Complete |  | NA | 03.Medium |
| DATW1202 | Workflow | Workflow Setup for Change/Extend Reference Material Governance Process | 10. Object Complete |  | NA | 03.Medium |
| DATW1201 | Workflow | Workflow Setup for Create Reference Material Governance Process | 10. Object Complete |  | NA | 03.Medium |
| DATW0748 | Workflow | Workflow Setup for Material Master Governance Mass Processing | 10. Object Complete |  | NA | 03.Medium |
| DATW0747 | Workflow | Workflow Setup for Material Master Governance in Mark For Delete Process | 10. Object Complete |  | NA | 03.Medium |
| DATW0746 | Workflow | Workflow Setup for Material Master Governance in the Change Process | 10. Object Complete |  | NA | 03.Medium |
| DATW0591 | Workflow | Parallel Approver Workflow Process | 10. Object Complete |  | NA | 03.Medium |
| DATW0207 | Workflow | Create IP Customer process workflow | 10. Object Complete | NA → NA | NA | 02.High |
| DATW0205_IP | Workflow | Change/Extend/Block/Unblock IP Customer Master process workflow | 10. Object Complete | NA → NA | NA | 02.High |
| DATR1430 | Report | Cost Center Approvers report by Supergroup, Group, Division, Subdivision, CCR... | 10. Object Complete |  | NA | 03.Medium |
| DATR0787 | Report | Report to send notification to Direct managers about the inactive Cost Center... | 10. Object Complete |  | NA | 03.Medium |
| DATR0390_IP | Report | Data Monitor Report between MDG and Reltio | 10. Object Complete | NA → NA | NA | 03.Medium |
| DATR0389_IP | Report | Customer Master Operational Report | 10. Object Complete | NA → NA | NA | 03.Medium |
| DATI1727 | Interface | Automated update to DC Sales Status and other Item Sales Data fields​ | 05. FS Overdue |  | NA | 03.Medium |
| DATI1712 | Interface | Import Dot process/stage details from MDG into IF. ​ | 10. Object Complete |  | NA | 03.Medium |
| DATI1618_IP | Interface | Interface to automate the PROC material master creation to read BOM data from... | 06. Dev In Progress |  | NA | 03.Medium |
| DATI1618_IF | Interface | Interface to automate the PROC material master creation to read BOM data from... | 06. Dev In Progress |  | NA | 04.Low |
| DATI1612_IP | Interface | 2A1 interface to send Product Catalog to OpenText for 3PL consumption | 10. Object Complete |  | MuleSoft | 03.Medium |
| DATI1612_IF | Interface | 2A1 interface to send Product Catalog to OpenText for 3PL consumption | 10. Object Complete |  | MuleSoft | 04.Low |
| DATI1607 | Interface | Delta updates to OM Position IDs and Relationships | 10. Object Complete |  | NA | 03.Medium |
| DATI1508 | Interface | Program to update weight of material in the material master | 10. Object Complete |  | NA | 03.Medium |
| DATI1501 | Interface | Inbound Interface to exchange BOM data between PLM Translator to SAP S/4 – In... | 10. Object Complete | PLM → S/4 | MULESOFT | 02.High |
| DATI1489 | Interface | Transfer activity type, WWID data from IFED2.0 to MDG for time keeping employees | 10. Object Complete |  | MULESOFT | 03.Medium |
| DATI1445_IP | Interface | Outbound Interface to exchange BOM data between PLM Translator to SAP S/4 – I... | 10. Object Complete | S/4 → PLM | NA | 02.High |
| DATI1445_IF | Interface | Outbound Interface to exchange BOM data between PLM Translator to SAP S/4 – I... | 10. Object Complete | S/4 → PLM | NA | 03.Medium |
| DATI1416 | Interface | Interface to get MMID from the PLM Translator for the materials created direc... | 10. Object Complete |  | NA | 03.Medium |
| DATI1289_IP | Interface | Program to update weight of material in the material master | 10. Object Complete | S/4 → S/4 MDG | NA | 03.Medium |
| DATI1289_IF | Interface | Program to update weight of material in the material master | 10. Object Complete | S/4 → S/4 MDG | NA | 04.Low |
| DATI1164 | Interface | Update Min Max ROP proposals in IF S4 Hana(PDH to MDG to S4) | 10. Object Complete | Supply Management and Materials Requirements Tool; IF Material PDH → S/4 | BODS | 03.Medium |
| DATI1132_IP | Interface | Interface to exchange Yield and Scrap data between PDH Translator to SAP S/4 ... | 10. Object Complete | PDH → S/4 | BODS | 03.Medium |
| DATI1132_IF | Interface | Interface to exchange Yield and Scrap data between PDH Translator to SAP S/4 ... | 10. Object Complete | PDH → S/4 | BODS | 04.Low |
| DATI0960 | Interface | To transfer HRMM data retrieved by Signature Authority API from source system... | 10. Object Complete | WCDS → S/4 MDG | MULESOFT | 03.Medium |
| DATI0959 | Interface | To transfer HRMM data retrieved by Worker snapshot API from source system WCD... | 10. Object Complete | WCDS → S/4 MDG | MULESOFT | 03.Medium |
| DATI0944 | Interface | Interface to Send/Receive item master Data Asynchronously between PLM Transla... | 10. Object Complete | PLM → S/4 MDG | NA | 03.Medium |
| DATI0943 | Interface | Interface to Send/Receive item master Data between PLM Translator and MDG Syn... | 10. Object Complete | S/4 MDG → PLM | APIGEE | 03.Medium |
| DATI0927 | Interface | Inbound Interface to exchange BOM data between PLM Translator to SAP S/4 – In... | 10. Object Complete | PLM → S/4 | MULESOFT | 02.High |
| DATI0657_IP | Interface | RICEFW2 - Interface between MDG and Reltio to fetch details to support pop-up... | 10. Object Complete |  | MULESOFT | 03.Medium |
| DATI0582 | Interface | Interface to pull Vendor Master from Reltio to MDG | 10. Object Complete | Reltio → S/4 | MULESOFT | 02.High |
| DATI0394_IP | Interface | Inbound Interface from Reltio to MDG to receive BP ID and UCD ID to MDG and u... | 10. Object Complete | Reltio → S/4 MDG | MULESOFT | 03.Medium |
| DATI0394_IF | Interface | Inbound Interface from Reltio to MDG to receive BP ID and UCD ID to MDG and u... | 10. Object Complete | Reltio → S/4 MDG | MULESOFT | 04.Low |
| DATI0393_IP | Interface | Replicating Customer Master data from MDG to cFin,IF and IP systems | 10. Object Complete |  | NA | 04.Low |
| DATI0392_IP | Interface | Outbound Interface from MDG to Reltio to send the Name, Address, URL, BP ID a... | 10. Object Complete |  | MULESOFT | 03.Medium |
| DATI0391_IP | Interface | Interface between MDG and Reltio to fetch details to support pop-up and Data ... | 10. Object Complete |  | MULESOFT | 04.Low |
| DATE1737_IP | Enhancement | Change BOM UI with BOM update Logic that can be run in background & Error pro... | 06. Dev Not Started |  | NA | 01.Very High |
| DATE1737_IF | Enhancement | Change BOM UI with BOM update Logic that can be run in background & Error pro... | 06. Dev Not Started |  | NA | 02.High |
| DATE1736_IP | Enhancement | Create BOM UI with Logic to combine Group BOM and MPV Component Table & Error... | 06. Dev Not Started |  | NA | 02.High |
| DATE1736_IF | Enhancement | Create BOM UI with Logic to combine Group BOM and MPV Component Table & Error... | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1735_IP | Enhancement | Reprocess Errors based on Error Categories (replication / BOM / etc.)​ | 06. Dev Not Started |  | NA | 01.Very High |
| DATE1735_IF | Enhancement | Reprocess Errors based on Error Categories (replication / BOM / etc.)​ | 06. Dev Not Started |  | NA | 02.High |
| DATE1734_IP | Enhancement | Search BOM using Plant and Parent ( User selects components from entire BOM w... | 06. Dev Not Started |  | NA | 02.High |
| DATE1734_IF | Enhancement | Search BOM using Plant and Parent ( User selects components from entire BOM w... | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1733_IP | Enhancement | Search BOM by Keyword and fetch only matching components​ | 06. Dev Not Started |  | NA | 02.High |
| DATE1733_IF | Enhancement | Search BOM by Keyword and fetch only matching components​ | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1732_IP | Enhancement | Maintain MPV Component table (add, update, inactivate)​ | 06. Dev Not Started |  | NA | 02.High |
| DATE1732_IF | Enhancement | Maintain MPV Component table (add, update, inactivate)​ | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1731_IP | Enhancement | Upload records to MPV Keyword or MPV Component table​ | 06. Dev Not Started |  | NA | 02.High |
| DATE1731_IF | Enhancement | Upload records to MPV Keyword or MPV Component table​ | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1730_IP | Enhancement | Create/Maintain Keyword for Plant / or update multiple Keywords into MPV Keyw... | 06. Dev Not Started |  | NA | 02.High |
| DATE1730_IF | Enhancement | Create/Maintain Keyword for Plant / or update multiple Keywords into MPV Keyw... | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1729_IP | Enhancement | Custom Tables – 3x (needed to support entire FS)​ | 06. Dev Not Started |  | NA | 02.High |
| DATE1729_IF | Enhancement | Custom Tables – 3x (needed to support entire FS)​ | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1633 | Enhancement | SIMS External BOM - Update lead time offset for BOM Components | 06. Dev Unplanned |  | NA | 03.Medium |
| DATE1623 | Enhancement | Custom table to store WCDS attributes based on BusinessTitleNm | 10. Object Complete |  | NA | 04.Low |
| DATE1616_IP | Enhancement | Automate External BOM | 06. Dev Not Started |  | NA | 02.High |
| DATE1616_IF | Enhancement | Automate External BOM | 06. Dev Not Started |  | NA | 03.Medium |
| DATE1615 | Enhancement | Automate the PROC material master creation process based on business rules | 06. Dev In Progress |  | NA | 03.Medium |
| DATE1613 | Enhancement | HAZMAT Profile UI | 08. FUT In Progress |  | NA | 03.Medium |
| DATE1611_IP | Enhancement | 2A1 Enhancement to send Product Catalog to OpenText | 10. Object Complete |  | NA | 03.Medium |
| DATE1611_IF | Enhancement | 2A1 Enhancement to send Product Catalog to OpenText | 10. Object Complete |  | NA | 04.Low |
| DATE1499 | Enhancement | Capacity Group/Capacity Corridor Item Attribute Data Source​ | 10. Object Complete |  | NA | 03.Medium |
| DATE1490 | Enhancement | Extend 15 days to termination date and roll back to actual termination for ti... | 10. Object Complete |  | NA | 04.Low |
| DATE1457 | Enhancement | Master Data_Enhancement for Overwriting PC Value Derived from Business Rules | 10. Object Complete |  | NA | 04.Low |
| DATE1417 | Enhancement | UNBW Cross Site | 10. Object Complete |  | NA | 03.Medium |
| DATE1044_IP | Enhancement | Master Data Governance Email Notifications | 10. Object Complete |  | NA | 01.Very High |
| DATE1044_IF | Enhancement | Master Data Governance Email Notifications | 10. Object Complete |  | NA | 01.Very High |
| DATE0926_IP | Enhancement | Enhancement on PROC BOM for Intel Foundry | 10. Object Complete |  | NA | 03.Medium |
| DATE0926_IF | Enhancement | Enhancement on PROC BOM for Intel Product | 10. Object Complete |  | NA | 04.Low |
| DATE0799 | Enhancement | RICEFW for Validations and Derivations where enhancement required for all ref... | 10. Object Complete |  | NA | 03.Medium |
| DATE0759 | Enhancement | Segregation of IF IP workers based on biz segment getting retrieved from WCDS | 10. Object Complete |  | NA | 03.Medium |
| DATE0758 | Enhancement | 1)Standard IDOC Enhancement to map WWID same as CP ID and fill PERNR, | 10. Object Complete |  | NA | 03.Medium |
| DATE0668 | Enhancement | Customizing Technology Node field while Creating Cost Center in MDG system | 10. Object Complete |  | NA | 03.Medium |
| DATE0667_IF | Enhancement | Adding Technology Node while Creating Cost Center in MDG system (cFIn, IF and... | 10. Object Complete |  | NA | 03.Medium |
| DATE0667_CFIN | Enhancement | Adding Technology Node while Creating Cost Center in MDG system (cFIn, IF and... | 10. Object Complete |  | NA | 03.Medium |
| DATE0590 | Enhancement | Material extension using reference material | 10. Object Complete |  | NA | 03.Medium |
| DATE0570 | Enhancement | Adding Cost Center Approvers fields while Creating Cost Center in MDG system | 10. Object Complete |  | NA | 03.Medium |
| DATE0561 | Enhancement | Adding DQM Functionality for Address validation | 10. Object Complete |  | NA | 01.Very High |
| DATE0446 | Enhancement | Derivation of UPI Intelligent description, Material group, Profit center, and... | 10. Object Complete | NA → NA | NA | 03.Medium |
| DATE0395_IP | Enhancement | Pop Up window to be developed on MDG screen to display “Search before Create”... | 10. Object Complete | NA → NA | NA | 03.Medium |
| DATE0313_IP | Enhancement | Customer Master Validations and Derivations | 10. Object Complete |  | NA | 02.High |
| DATE0020 | Enhancement | Material description generation from Classification data | 10. Object Complete | NA → NA | NA | 04.Low |
| DATC1663 | Conversion | Product Hierarchy File 1 and File 2 | 10. Object Complete |  | NA | 02.High |
| DATC1640 | Conversion | Material Master MRP View WINGS Conversion | 10. Object Complete |  | NA | 04.Low |
| DATC1639 | Conversion | Material Master Plant and Storage Location View WINGS Materials Conversions | 10. Object Complete |  | NA | 04.Low |
| DATC1638 | Conversion | Material Master Accounting and Costing View WINGS Materials Conversions | 10. Object Complete |  | NA | 04.Low |
| DATC1637 | Conversion | Material Master Purchasing View WINGS Materials Conversions | 10. Object Complete |  | NA | 04.Low |
| DATC1617 | Conversion | HAZMAT Profile Conversion | 10. Object Complete |  | NA | 03.Medium |
| DATC1604 | Conversion | Initial Load for Objects & Relationships | 10. Object Complete |  | NA | 03.Medium |
| DATC1556 | Conversion | Conversion program to load Images of Products in Material Master | 10. Object Complete |  | NA | 03.Medium |
| DATC1552 | Conversion | edFIT - PSI BOM Conversion | 03. FS Not Started |  | NA | 03.Medium |
| DATC1551 | Conversion | edFIT - Material Master Conversion | 04. FS In Progress |  | NA | 03.Medium |
| DATC1237 | Conversion | Material Master Data – Quality Management View Conversion | 10. Object Complete |  | NA | 03.Medium |
| DATC1204 | Conversion | Load Vendor as Customer to MDG System | 10. Object Complete |  | NA | 03.Medium |
| DATC0859 | Conversion | Convert the Customer Master Contact Person from ECC system to MDG system_IP | 10. Object Complete |  | NA | 03.Medium |
| DATC0589 | Conversion | Vendor Master : General Data conversion from ECC to MDG | 10. Object Complete |  | NA | 02.High |
| DATC0588 | Conversion | Vendor Master : Company Code Data conversion from ECC to MDG | 10. Object Complete |  | NA | 03.Medium |
| DATC0587 | Conversion | Vendor Master : Purchase Org conversion from ECC to MDG | 10. Object Complete |  | NA | 03.Medium |
| DATC0586 | Conversion | Vendor Master : Partner Function conversion from ECC to MDG | 10. Object Complete |  | NA | 02.High |
| DATC0585 | Conversion | Vendor Master : Tax Data conversion from ECC to MDG | 10. Object Complete |  | NA | 03.Medium |
| DATC0584 | Conversion | Vendor Master : Bank Data conversion from ECC to MDG | 10. Object Complete |  | NA | 03.Medium |
| DATC0583 | Conversion | Initial load of HRMM data from WCDS to MPipe system, The initial data load wi... | 10. Object Complete | RELTIO → S4 | NA | 02.High |
| DATC0562 | Conversion | Conversion of DUNS table from ECC to S/4 for IP | 10. Object Complete |  | NA | 03.Medium |
| DATC0553 | Conversion | Conversion of BOM from SPEED to S4 IF | 10. Object Complete |  | NA | 01.Very High |
| DATC0552 | Conversion | Conversion of BOM from SPEED to S4 IP | 10. Object Complete |  | NA | 01.Very High |
| DATC0213 | Conversion | Material Master-Work scheduling view | 10. Object Complete |  | NA | 03.Medium |
| DATC0184_IP | Conversion | Convert the Customer Master Partner Function view from ECC system to MDG syst... | 10. Object Complete | NA → NA | NA | 03.Medium |
| DATC0182_IP | Conversion | Convert the General data view from ECC system to MDG system_IP. | 10. Object Complete | NA → NA | NA | 03.Medium |
| DATC0179_IP | Conversion | Convert the Customer Master Sales view from ECC system to MDG system_IP. | 10. Object Complete | NA → NA | NA | 03.Medium |
| DATC0178_IP | Conversion | Convert the Customer Master Tax view from ECC system to MDG system_IP. | 10. Object Complete | NA → NA | NA | 04.Low |
| DATC0120_IP | Conversion | Convert the Customer Master Company Code view from ECC system to MDG system_IP. | 10. Object Complete | ECC → MDG | NA | 04.Low |
| DATC0118_IP | Conversion | Convert the Customer Master In House Cash view from ECC system to MDG system_IP. | 10. Object Complete | ECC → MDG | NA | 03.Medium |
| DATC0076_IP | Conversion | Material Master-Classification View | 10. Object Complete |  | NA | 03.Medium |
| DATC0075_IP | Conversion | Material Master-Accounting & Costing view | 10. Object Complete |  | NA | 03.Medium |
| DATC0074_IP | Conversion | Material Master-Sales Org Views and Sales Text | 10. Object Complete |  | NA | 03.Medium |
| DATC0073 | Conversion | Material Master-Warehouse Mgmt Views | 10. Object Complete |  | NA | 04.Low |
| DATC0072 | Conversion | Material Master-Purchasing View and PO Text | 10. Object Complete |  | NA | 03.Medium |
| DATC0071_IP | Conversion | Material Master-MRP View | 10. Object Complete |  | NA | 04.Low |
| DATC0070_IP | Conversion | Material Master-Plant Data/Storage Views | 10. Object Complete |  | NA | 03.Medium |
| DATC0069_IP | Conversion | Material Master-Alt UOM | 10. Object Complete |  | NA | 04.Low |
| DATC0068_IP | Conversion | Material Master-Basic Data- (including description) Views | 10. Object Complete |  | NA | 03.Medium |

**Summary**: 5 Reports, 30 Interfaces, 40 Conversions, 61 Enhancements, 10 Workflows

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

### 5.6 Integration Patterns

Integration patterns identified from the system flow analysis for MDM-130:

| # | Pattern | Flow Chain | Middleware | Protocol | Auth |
|---|---------|-----------|-----------|----------|------|

> *Integration pattern details will be refined when tower architects validate middleware assignments.*

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

## 6. Technology Architecture (TOGAF "T")

### 6.1 Platform & Infrastructure

> **TECHNOLOGY / PLATFORM ARCHITECTURE** — Platforms (green) host applications (blue). Thick arrows show platform-to-platform integration flows.

#### Platform Inventory

Platform landscape inferred from integrated systems for MDM-130:

| # | Platform | Type | Systems Using | Environment |
|---|----------|------|--------------|-------------|
| 1 | SAP S/4HANA | On-Premise (HEC) | SAP S/4 modules | DEV, QAS, PRD |
| 2 | SAP BTP (Integration Suite) | Cloud / PaaS | CPI, API Management | DEV, QAS, PRD |
| 3 | MuleSoft Anypoint | Cloud / iPaaS | API-led integrations | DEV, QAS, PRD |

> *Platform assignments will be validated when tower architects populate technology platform columns.*

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

### 6.2 SAP Development Object Status

**Capability RICEFW Status** (146 objects)
*Data source: Smartsheet Object Tracker (cached 2026-03-26)*

| Status | Count | % |
|--------|------:|----:|
| 10. Object Complete | 117 | 80.1% |
| 06. Dev Not Started | 20 | 13.7% |
| 06. Dev In Progress | 3 | 2.1% |
| 09. FUT Overdue | 1 | 0.7% |
| 05. FS Overdue | 1 | 0.7% |
| 06. Dev Unplanned | 1 | 0.7% |
| 08. FUT In Progress | 1 | 0.7% |
| 03. FS Not Started | 1 | 0.7% |
| 04. FS In Progress | 1 | 0.7% |
| **Total** | **146** | **100%** |

**RICEFW by Type:**

| Type | Count |
|------|------:|
| Report (R) | 5 |
| Interface (I) | 30 |
| Conversion (C) | 40 |
| Enhancement (E) | 61 |
| Workflow (W) | 10 |
| **Total** | **146** |

**Technical Complexity:**

| Complexity | Count |
|------------|------:|
| 01.Very High | 7 |
| 02.High | 21 |
| 03.Medium | 95 |
| 04.Low | 22 |
| N/A | 1 |

**Active (Non-Complete) Objects:**

| Object ID | Type | Description | Status | Complexity |
|-----------|------|-------------|--------|------------|
| MDCR0025 | 01.Report | Alternate/Preferred BOM Component Change in S4 | 09. FUT Overdue | 03.Medium |
| DATI1727 | 02.Interface | Automated update to DC Sales Status and other Item Sales Data fields​ | 05. FS Overdue | 03.Medium |
| DATI1618_IP | 02.Interface | Interface to automate the PROC material master creation to read BOM data from S/... | 06. Dev In Progress | 03.Medium |
| DATI1618_IF | 02.Interface | Interface to automate the PROC material master creation to read BOM data from S/... | 06. Dev In Progress | 04.Low |
| DATE1737_IP | 04.Enhancement | Change BOM UI with BOM update Logic that can be run in background & Error proces... | 06. Dev Not Started | 01.Very High |
| DATE1737_IF | 04.Enhancement | Change BOM UI with BOM update Logic that can be run in background & Error proces... | 06. Dev Not Started | 02.High |
| DATE1736_IP | 04.Enhancement | Create BOM UI with Logic to combine Group BOM and MPV Component Table & Error pr... | 06. Dev Not Started | 02.High |
| DATE1736_IF | 04.Enhancement | Create BOM UI with Logic to combine Group BOM and MPV Component Table & Error pr... | 06. Dev Not Started | 03.Medium |
| DATE1735_IP | 04.Enhancement | Reprocess Errors based on Error Categories (replication | BOM | etc.)​ | 06. Dev Not Started | 01.Very High |
| DATE1735_IF | 04.Enhancement | Reprocess Errors based on Error Categories (replication | BOM | etc.)​ | 06. Dev Not Started | 02.High |
| DATE1734_IP | 04.Enhancement | Search BOM using Plant and Parent ( User selects components from entire BOM with... | 06. Dev Not Started | 02.High |
| DATE1734_IF | 04.Enhancement | Search BOM using Plant and Parent ( User selects components from entire BOM with... | 06. Dev Not Started | 03.Medium |
| DATE1733_IP | 04.Enhancement | Search BOM by Keyword and fetch only matching components​ | 06. Dev Not Started | 02.High |
| DATE1733_IF | 04.Enhancement | Search BOM by Keyword and fetch only matching components​ | 06. Dev Not Started | 03.Medium |
| DATE1732_IP | 04.Enhancement | Maintain MPV Component table (add, update, inactivate)​ | 06. Dev Not Started | 02.High |
| DATE1732_IF | 04.Enhancement | Maintain MPV Component table (add, update, inactivate)​ | 06. Dev Not Started | 03.Medium |
| DATE1731_IP | 04.Enhancement | Upload records to MPV Keyword or MPV Component table​ | 06. Dev Not Started | 02.High |
| DATE1731_IF | 04.Enhancement | Upload records to MPV Keyword or MPV Component table​ | 06. Dev Not Started | 03.Medium |
| DATE1730_IP | 04.Enhancement | Create/Maintain Keyword for Plant / or update multiple Keywords into MPV Keyword... | 06. Dev Not Started | 02.High |
| DATE1730_IF | 04.Enhancement | Create/Maintain Keyword for Plant / or update multiple Keywords into MPV Keyword... | 06. Dev Not Started | 03.Medium |
| DATE1729_IP | 04.Enhancement | Custom Tables – 3x (needed to support entire FS)​ | 06. Dev Not Started | 02.High |
| DATE1729_IF | 04.Enhancement | Custom Tables – 3x (needed to support entire FS)​ | 06. Dev Not Started | 03.Medium |
| DATE1633 | 04.Enhancement | SIMS External BOM - Update lead time offset for BOM Components | 06. Dev Unplanned | 03.Medium |
| DATE1616_IP | 04.Enhancement | Automate External BOM | 06. Dev Not Started | 02.High |
| DATE1616_IF | 04.Enhancement | Automate External BOM | 06. Dev Not Started | 03.Medium |
| DATE1615 | 04.Enhancement | Automate the PROC material master creation process based on business rules | 06. Dev In Progress | 03.Medium |
| DATE1613 | 04.Enhancement | HAZMAT Profile UI | 08. FUT In Progress | 03.Medium |
| DATC1552 | 03.Conversion | edFIT - PSI BOM Conversion | 03. FS Not Started | 03.Medium |
| DATC1551 | 03.Conversion | edFIT - Material Master Conversion | 04. FS In Progress | 03.Medium |

### 6.3 NFRs & Design Principles

| Category | Requirement | Target / SLA | Priority |
|----------|-------------|-------------|----------|
| Performance | Master data creation and validation within user expectation | < 5 seconds for save/validate | High |
| Availability | MDM systems available during global business hours | 99.9% (follows-the-sun) | High |
| Scalability | Support master data volume growth from new entities | Handle 5M+ master records | Medium |
| Recoverability | Master data systems recover with data integrity guaranteed | RPO = 0 (no data loss), RTO < 2 hours | High |
| Data Volume | Support comprehensive master data model across domains | 500K+ active material masters | Medium |
| Latency | Master data changes propagate to consuming systems promptly | < 15 minutes replication latency | High |
| Concurrency | Support centralized MDM team plus distributed maintainers | 100+ concurrent MDM users | Medium |

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

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>MDM-130 — Create and Maintain Customers</span></div>
<div style="page-break-before: always;"></div>

## 7. Project Context

### 7.1 Project Roadmap & Go-Live Plan

*144 objects with timeline data (source: Object Tracker)*

| ID | Description | FS | TDD | Build | FUT | Status |
|----|-------------|----|-----|-------|-----|--------|
| MDGM1332 | IMO Materials | Aug-25 (100%) | — | — | Sep-25 (100%) | 2. At Risk |
| MDCR0025 | Alternate/Preferred BOM Component Change in S4 | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | Jan-26 (52%) |  |
| MDCE0024 | Supplier Hierarchy | Nov-25 (100%) | Nov-25 (100%) | Feb-26 (100%) | Jan-26 (100%) |  |
| MDCE0023 | Sales Organization - Extended Itego datamodel + UI to govern assignment to Sales Regions | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| MDCE0022 | Sales Region - Custom Itego Object to govern Sales Regions | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| MDCE0021 | Customer Planning Hierarchy -IF | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| MDCE0020 | Customer Planning Hierarchy -IP | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| MDCE0019 | Product Planning Hierarchy -IF | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| MDCE0018 | Product Planning Hierarchy -IP | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | 4. Completed |
| MDCE0017 | Commodity- Custom Itego Object with ~100 customer fields + UI to support governance | Jul-25 (100%) | Jul-25 (100%) | Jul-25 (100%) | Nov-25 (100%) | 4. Completed |
| MDCE0015 | Asset Location - Extended Itego datamodel with 22 custom fields + UI to support governance | Oct-24 (100%) | Nov-24 (100%) | Feb-25 (100%) | Feb-25 (100%) |  |
| MDCE0014 | Storage Location - Extended Itego datamodel with 11 custom fields + UI to support governance | Oct-24 (100%) | Oct-24 (100%) | Nov-24 (100%) | Nov-24 (100%) |  |
| MDCE0013 | Plant - Extended Itego datamodel with 13 custom fields + UI to support governance | Oct-24 (100%) | Oct-24 (100%) | Nov-24 (100%) | Nov-24 (100%) |  |
| MDCE0012 | Sales Org Association - Custom Itego Object with 4 customer fields + UI to support goverance | Sep-24 (100%) | Oct-24 (100%) | Oct-24 (100%) | Nov-24 (100%) |  |
| MDCE0011 | Holiday Calendar - Custom goveranance | Sep-24 (100%) | Sep-24 (100%) | Oct-24 (100%) | Oct-24 (100%) |  |
| MDCE0009 | Shipping Point- Custom Itego Object with 6 customer fields + UI to support goverance | Oct-24 (100%) | Oct-24 (100%) | Nov-24 (100%) | Nov-24 (100%) |  |
| DATW1205 | Vendor as Customer Workflow | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) |  |
| DATW1203 | Workflow Setup for Mark For Delete Reference Material Governance Process | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) |  |
| DATW1202 | Workflow Setup for Change/Extend Reference Material Governance Process | Apr-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Oct-25 (100%) |  |
| DATW1201 | Workflow Setup for Create Reference Material Governance Process | Mar-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Oct-25 (100%) |  |
| DATW0748 | Workflow Setup for Material Master Governance Mass Processing | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) |  |
| DATW0747 | Workflow Setup for Material Master Governance in Mark For Delete Process | Mar-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) |  |
| DATW0746 | Workflow Setup for Material Master Governance in the Change Process | Mar-25 (100%) | Aug-25 (100%) | Aug-25 (100%) | Sep-25 (100%) |  |
| DATW0591 | Parallel Approver Workflow Process | Oct-24 (100%) | Nov-24 (100%) | Nov-24 (100%) | May-25 (100%) |  |
| DATW0207 | Create IP Customer process workflow | May-25 (100%) | May-25 (100%) | May-25 (100%) | Sep-25 (100%) | 1. On Track |
| DATW0205_IP | Change/Extend/Block/Unblock IP Customer Master process workflow | Nov-24 (100%) | Sep-25 (100%) | Sep-25 (100%) | Oct-25 (100%) | 1. On Track |
| DATR1430 | Cost Center Approvers report by Supergroup, Group, Division, Subdivision, CCRU, profit center, Expense approver, capital approver or consolidator | Jun-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | Sep-25 (100%) | 1. On Track |
| DATR0787 | Report to send notification to Direct managers about the inactive Cost Center Approvers | Jul-25 (100%) | Jun-25 (100%) | Jun-25 (100%) | Jul-25 (100%) |  |
| DATR0390_IP | Data Monitor Report between MDG and Reltio | Jun-25 (100%) | Nov-25 (100%) | Nov-25 (100%) | Dec-25 (100%) | 4. Completed |
| DATR0389_IP | Customer Master Operational Report | Jun-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | Dec-25 (100%) | 1. On Track |

*... and 114 more objects (see full Object Tracker)*

### 7.2 RAID Log

*Live data from Smartsheet Master RAID Log — extracted 2026-03-26*

**Mapped sub-tower(s):** 9A.1 Master Data - ALL, 9A.2 Master Data - BOM, 9A.3 Master Data - Customer, 9A.4 Master Data - Vendor, 9A.5 Master Data - Finance, 9A.6 Master Data - Material, 9A.7 Master Data - Reference, 9A.8 Master Data - HR Mini Master

**RAID Summary:** 19 open items (1 capability-specific, 18 tower-level), 174 closed

| Severity | Capability | Tower-Wide | Total Open |
|----------|----------:|-----------:|-----------:|
| P1 - High | 0 | 2 | 2 |
| P2 - Medium | 1 | 12 | 13 |
| P3 - Low | 0 | 4 | 4 |
| **Total** | **1** | **18** | **19** |

**Capability-Specific RAID Items:**

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03331 | Risk | P2 - Medium | Clarity on finalized SAP S/4 Plant and storage location mapp... | In Progress | Master Data | 2026-02-20 |

**Other MDM Tower RAID Items** (18 open):

| RAID ID | Type | Severity | Title | Status | Assigned To | Due Date |
|---------|------|----------|-------|--------|-------------|----------|
| 03578 | Risk | P1 - High | HBI Process Flow Change impact Assessment | In Progress | FTS IF | 2026-03-27 |
| 03591 | Risk | P1 - High | R3 E2E scenario execution | In Progress | Test Management | 2026-04-03 |
| 01733 | Risk | P2 - Medium | Tariffs impacts Item/BOM design which is impacting ERP/SCP (... | In Progress | E2E | 2026-03-06 |
| 03728 | Risk | P2 - Medium | Awaiting logic and FS details to develop INT-CR1120 from Mas... | In Progress | Master Data | 2026-03-11 |
| 03603 | Risk | P2 - Medium | Inbound (ECC /WIINGS to BODS to ECM) - Missing good sample d... | Roadblock / At Risk | Master Data | 2026-02-27 |
| 03604 | Risk | P2 - Medium | Outbound (ECM to BODS to ECC /WIINGS) - Need actionable expo... | Roadblock / At Risk | Master Data | 2026-03-27 |
| 03625 | Risk | P2 - Medium | Item/ BOM MC1 delta load | In Progress | Cutover | 2026-04-10 |
| 03466 | Action | P2 - Medium | Updated BOM for Substrate CR | In Progress | Master Data | 2026-03-13 |
| 02436 | Action | P2 - Medium | MD Straddle WtFlow:  Change impact #1 Intel Federal’s potent... | Not Started | Master Data | 2026-04-24 |
| 02438 | Action | P2 - Medium | MD Straddle WtFlow:  Breakpoint #4 concern with no clear biz... | In Progress | Master Data | 2026-03-20 |
| 02657 | Action | P2 - Medium | Exception Report | In Progress | FTS IP | 2026-04-03 |
| 03736 | Action | P2 - Medium | Golden Data/Test Data Readiness | In Progress | Master Data | 2026-04-22 |
| 03743 | Issue | P2 - Medium | FD-Share with Entitlements -  Interface File Paths for MC1 | Roadblock / At Risk | PMO | 2026-03-20 |
| 03769 | Action | P2 - Medium | Need a Labs SPOC owner to define IP Labs enterprise and mate... | In Progress | E2E | 2026-04-17 |
| 03317 | Risk | P3 - Low | BPMG – E2E L3/L4 flow standards | In Progress | Business Process Mgmt | 2026-05-29 |
| 03381 | Risk | P3 - Low | New requirement raised for enabling Israel as virtual site | Not Started | OTC IF | 2026-03-31 |
| 03525 | Issue | P3 - Low | Vendor determination in PDH for 2DN PR's & STR's. | Not Started | FTS IP | 2026-03-06 |
| 02610 | Action | P3 - Low | Sample Master Data from S4 | In Progress |  | 2025-10-31 |

### 7.3 Recommendations & Next Steps

| # | Category | Recommendation | Priority | Owner | Target Date | Status |
|---|----------|---------------|----------|-------|-------------|--------|
| 1 | Architecture | Complete extended flow attributes (Data Entity, Integration Pattern, Tech Platform) in Flows tab for full BDAT coverage | High | Tower Architect | 2026-Q2 | Open |
| 2 | Data | Define data ownership and classification for all 0 flow chains to satisfy Data Architecture (TOGAF D) requirements | Medium | Data Architect | 2026-Q3 | Open |
| 3 | Testing | Develop integration test scenarios covering all 0 flow chains for FUT/SIT readiness | High | Test Lead | 2026-Q3 | Open |
| 4 | Business Architecture | Review and validate Business Architecture process steps against latest Signavio/BIC process models | Medium | Business Analyst | 2026-Q2 | Open |
| 5 | Security | Complete security review for API integrations and data flows per Intel Security Architecture standards | Medium | Security Architect | 2026-Q3 | Open |

---
*MDM-130 — Architecture Document (TOGAF BDAT) · Master Data · Generated: March 2026*

