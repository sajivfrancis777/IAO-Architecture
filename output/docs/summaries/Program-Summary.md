<div style="text-align:center; padding-top:60px;">
  <h1 style="font-size:36px; margin-top:24px;">IAO Program Architecture Summary</h1>
  <h2 style="font-size:24px;">TOGAF BDAT — Systems Integration Summary</h2>
  <p style="font-size:18px; color:#555;">IDM 2.0 — All Towers (R1 – R5)</p>
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

<div class="page-footer"><span>Page 1</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

<a id="toc"></a>

## Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. Capability Inventory](#2-capability-inventory)
- [3. Current-State Architecture](#3-current-state-architecture)
   - [3.1 System Integration Map](#31-system-integration-map)
   - [3.2 ArchiMate Application View](#32-archimate-application-view)
   - [3.3 Data Entities](#33-data-entities)
   - [3.4 Integration Patterns](#34-integration-patterns)
   - [3.5 Technology Stack](#35-technology-stack)
- [4. Future-State Architecture](#4-future-state-architecture)
   - [4.1 System Integration Map](#41-system-integration-map)
   - [4.2 ArchiMate Application View](#42-archimate-application-view)
   - [4.3 Data Entities](#43-data-entities)
   - [4.4 Integration Patterns](#44-integration-patterns)
   - [4.5 Technology Stack](#45-technology-stack)
- [5. Transformation Analysis](#5-transformation-analysis)
   - [5.1 System Landscape Changes](#51-system-landscape-changes)
   - [5.2 Integration Complexity](#52-integration-complexity)
- [6. System Inventory](#6-system-inventory)

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 1 Executive Summary

This document provides a **Program** summary view of the systems architecture for **IDM 2.0 — All Towers (R1 – R5)**.

| Metric | Current-State | Future-State | Delta |
|--------|:---:|:---:|:---:|
| **Unique Systems** | 28 | 44 | +16 |
| **System Connections** | 32 | 54 | +22 |
| **Total Flow Hops** | 89 | 167 | +78 |
| **Capabilities Covered** | 184 | 184 | — |

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 2 Capability Inventory

The following **184** capabilities are aggregated in this summary.
Click a capability ID to view its full TOGAF BDAT architecture document.

| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |
|:---:|:---:|---|---|:---:|:---:|
| 1 | [E2E-80](towers/E2E/E2E-80 R2 Customer Requests Expedite/E2E-80/output/docs/systems-architecture/E2E-80-Architecture.html) | R2A Option 1  Customer Requests Expedite - Service Fee with Existing SO | E2E · E2E-80 R2 Customer Requests Expedite | 1 | 1 |
| 2 | [E2E-08](towers/E2E/Forecast to Stock/E2E-08/output/docs/systems-architecture/E2E-08-Architecture.html) | E2E-08 | E2E · Forecast to Stock | 1 | 1 |
| 3 | [E2E-110](towers/E2E/Forecast to Stock/E2E-110/output/docs/systems-architecture/E2E-110-Architecture.html) | IMR Flow | E2E · Forecast to Stock | 1 | 1 |
| 4 | [E2E-113](towers/E2E/Forecast to Stock/E2E-113/output/docs/systems-architecture/E2E-113-Architecture.html) | R3 IMR Labs Process | E2E · Forecast to Stock | 1 | 1 |
| 5 | [E2E-117](towers/E2E/Forecast to Stock/E2E-117/output/docs/systems-architecture/E2E-117-Architecture.html) | E2E-117 | E2E · Forecast to Stock | 1 | 1 |
| 6 | [E2E-118](towers/E2E/Forecast to Stock/E2E-118/output/docs/systems-architecture/E2E-118-Architecture.html) | E2E-118 | E2E · Forecast to Stock | 1 | 1 |
| 7 | [E2E-122](towers/E2E/Forecast to Stock/E2E-122/output/docs/systems-architecture/E2E-122-Architecture.html) | E2E-122 | E2E · Forecast to Stock | 1 | 1 |
| 8 | [E2E-45](towers/E2E/Forecast to Stock/E2E-45/output/docs/systems-architecture/E2E-45-Architecture.html) | E2E-45 | E2E · Forecast to Stock | 1 | 1 |
| 9 | [E2E-67](towers/E2E/Forecast to Stock/E2E-67/output/docs/systems-architecture/E2E-67-Architecture.html) | E2E-67 | E2E · Forecast to Stock | 1 | 1 |
| 10 | [E2E-68](towers/E2E/Forecast to Stock/E2E-68/output/docs/systems-architecture/E2E-68-Architecture.html) | -Intel Foundry   NPI planning and execution processes | E2E · Forecast to Stock | 1 | 1 |
| 11 | [E2E-71](towers/E2E/Forecast to Stock/E2E-71/output/docs/systems-architecture/E2E-71-Architecture.html) | E2E-71 | E2E · Forecast to Stock | 1 | 1 |
| 12 | [E2E-72](towers/E2E/Forecast to Stock/E2E-72/output/docs/systems-architecture/E2E-72-Architecture.html) | IP | E2E · Forecast to Stock | 1 | 1 |
| 13 | [E2E-73](towers/E2E/Forecast to Stock/E2E-73/output/docs/systems-architecture/E2E-73-Architecture.html) | R3 Hybrid Manufacturing process with external Wafer Procurement & Internal processing of | E2E · Forecast to Stock | 1 | 1 |
| 14 | [E2E-74](towers/E2E/Forecast to Stock/E2E-74/output/docs/systems-architecture/E2E-74-Architecture.html) | R3 Internal manufacturing process for Finished Goods in Intel Foundry with Planning integrati | E2E · Forecast to Stock | 1 | 1 |
| 15 | [E2E-76](towers/E2E/Forecast to Stock/E2E-76/output/docs/systems-architecture/E2E-76-Architecture.html) | Internal manufacturing process for Finished Goods in Intel Foundry with sales to External cus | E2E · Forecast to Stock | 1 | 1 |
| 16 | [E2E-84](towers/E2E/Forecast to Stock/E2E-84/output/docs/systems-architecture/E2E-84-Architecture.html) | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) | E2E · Forecast to Stock | 1 | 1 |
| 17 | [E2E-94](towers/E2E/Forecast to Stock/E2E-94/output/docs/systems-architecture/E2E-94-Architecture.html) | R3 Intel Foundry Maintenance process through spare parts (SWAP) | E2E · Forecast to Stock | 1 | 1 |
| 18 | [E2E-89](towers/E2E/Master Data/E2E-89/output/docs/systems-architecture/E2E-89-Architecture.html) | R3 Customer Master Data | E2E · Master Data | 1 | 1 |
| 19 | [E2E-90](towers/E2E/Master Data/E2E-90/output/docs/systems-architecture/E2E-90-Architecture.html) | R3 Material Master Data | E2E · Master Data | 1 | 1 |
| 20 | [E2E-91](towers/E2E/Master Data/E2E-91/output/docs/systems-architecture/E2E-91-Architecture.html) | R3 Bill of Material BOM Data | E2E · Master Data | 1 | 1 |
| 21 | [E2E-92](towers/E2E/Master Data/E2E-92/output/docs/systems-architecture/E2E-92-Architecture.html) | R3 Vendor Master Data | E2E · Master Data | 1 | 1 |
| 22 | [IF_Simplified_PO-SO_Model](towers/E2E/Order to Cash/IF_Simplified_PO-SO_Model/output/docs/systems-architecture/IF_Simplified_PO-SO_Model-Architecture.html) | IF Simplified PO-SO Model | E2E · Order to Cash | 1 | 1 |
| 23 | [Order_to_Cash_IF](towers/E2E/Order to Cash/Order_to_Cash_IF/output/docs/systems-architecture/Order_to_Cash_IF-Architecture.html) | Order to Cash (IF) | E2E · Order to Cash | 1 | 1 |
| 24 | [Order_to_Cash_IP](towers/E2E/Order to Cash/Order_to_Cash_IP/output/docs/systems-architecture/Order_to_Cash_IP-Architecture.html) | Order to Cash (IP) | E2E · Order to Cash | 1 | 1 |
| 25 | [E2E-100](towers/E2E/Procure to Pay/E2E-100/output/docs/systems-architecture/E2E-100-Architecture.html) | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box | E2E · Procure to Pay | 1 | 1 |
| 26 | [E2E-103](towers/E2E/Procure to Pay/E2E-103/output/docs/systems-architecture/E2E-103-Architecture.html) | R3 Procurement of WIINGS Replacement Related Commodities | E2E · Procure to Pay | 1 | 1 |
| 27 | [E2E-107](towers/E2E/Procure to Pay/E2E-107/output/docs/systems-architecture/E2E-107-Architecture.html) | R3 - Partner Owned Equipment Order | E2E · Procure to Pay | 1 | 1 |
| 28 | [E2E-112](towers/E2E/Procure to Pay/E2E-112/output/docs/systems-architecture/E2E-112-Architecture.html) | R3 Raw Silicon Procurement | E2E · Procure to Pay | 1 | 1 |
| 29 | [E2E-114](towers/E2E/Procure to Pay/E2E-114/output/docs/systems-architecture/E2E-114-Architecture.html) | R4 SIMS Harvest Process | E2E · Procure to Pay | 1 | 1 |
| 30 | [E2E-115](towers/E2E/Procure to Pay/E2E-115/output/docs/systems-architecture/E2E-115-Architecture.html) | R3 Inter-company Asset Transfer Process | E2E · Procure to Pay | 1 | 1 |
| 31 | [E2E-116](towers/E2E/Procure to Pay/E2E-116/output/docs/systems-architecture/E2E-116-Architecture.html) | R3 Wafer Reclaim Process | E2E · Procure to Pay | 1 | 1 |
| 32 | [E2E-119](towers/E2E/Procure to Pay/E2E-119/output/docs/systems-architecture/E2E-119-Architecture.html) | R3 Shipping Rejects Inventory Movement | E2E · Procure to Pay | 1 | 1 |
| 33 | [E2E-121](towers/E2E/Procure to Pay/E2E-121/output/docs/systems-architecture/E2E-121-Architecture.html) | R3 RM Bailed Inventory Movement (Straddle) | E2E · Procure to Pay | 1 | 1 |
| 34 | [E2E-123](towers/E2E/Procure to Pay/E2E-123/output/docs/systems-architecture/E2E-123-Architecture.html) | TD Substrates Manufacturing Process | E2E · Procure to Pay | 1 | 1 |
| 35 | [E2E-40](towers/E2E/Procure to Pay/E2E-40/output/docs/systems-architecture/E2E-40-Architecture.html) | R3 Sourcing Request-Project to Contracts for Direct-Capital on Ariba with Pricing Updates | E2E · Procure to Pay | 1 | 1 |
| 36 | [E2E-41](towers/E2E/Procure to Pay/E2E-41/output/docs/systems-architecture/E2E-41-Architecture.html) | R3 Sourcing Request | E2E · Procure to Pay | 1 | 1 |
| 37 | [E2E-43](towers/E2E/Procure to Pay/E2E-43/output/docs/systems-architecture/E2E-43-Architecture.html) | Process Procurement Card Invoice | E2E · Procure to Pay | 1 | 1 |
| 38 | [E2E-44](towers/E2E/Procure to Pay/E2E-44/output/docs/systems-architecture/E2E-44-Architecture.html) | R3 - Intel Owned Consignment with Planning Integration | E2E · Procure to Pay | 1 | 1 |
| 39 | [E2E-46](towers/E2E/Procure to Pay/E2E-46/output/docs/systems-architecture/E2E-46-Architecture.html) | R3 Direct procurement with Planning Integration-AT | E2E · Procure to Pay | 1 | 1 |
| 40 | [E2E-47](towers/E2E/Procure to Pay/E2E-47/output/docs/systems-architecture/E2E-47-Architecture.html) | Purchase Requisition to Payments for Direct procurement with planning integration - Fab Mater | E2E · Procure to Pay | 1 | 1 |
| 41 | [E2E-49](towers/E2E/Procure to Pay/E2E-49/output/docs/systems-architecture/E2E-49-Architecture.html) | R3 Purchase Requisition to Payments for procurement with financial planning and asset managem | E2E · Procure to Pay | 1 | 1 |
| 42 | [E2E-50](towers/E2E/Procure to Pay/E2E-50/output/docs/systems-architecture/E2E-50-Architecture.html) | Purchase Requisition to Payments for Indirect - Construction (Small Construction IPCS, Mainte | E2E · Procure to Pay | 1 | 1 |
| 43 | [E2E-51](towers/E2E/Procure to Pay/E2E-51/output/docs/systems-architecture/E2E-51-Architecture.html) | Purchase Requisition to Payments for Indirect Materials (Non-IPN and Non-Inventoried) ​ | E2E · Procure to Pay | 1 | 1 |
| 44 | [E2E-52](towers/E2E/Procure to Pay/E2E-52/output/docs/systems-architecture/E2E-52-Architecture.html) | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement | E2E · Procure to Pay | 1 | 1 |
| 45 | [E2E-53](towers/E2E/Procure to Pay/E2E-53/output/docs/systems-architecture/E2E-53-Architecture.html) | Purchase Requisition to Payments for Indirect procurement (simple material or services like H | E2E · Procure to Pay | 1 | 1 |
| 46 | [E2E-57](towers/E2E/Procure to Pay/E2E-57/output/docs/systems-architecture/E2E-57-Architecture.html) | R3 Subcontracting with Planning integration- Foundry,OSAT,ODM | E2E · Procure to Pay | 1 | 1 |
| 47 | [E2E-59](towers/E2E/Procure to Pay/E2E-59/output/docs/systems-architecture/E2E-59-Architecture.html) | R3 Rework Re-localization in Factory​ | E2E · Procure to Pay | 1 | 1 |
| 48 | [E2E-61](towers/E2E/Procure to Pay/E2E-61/output/docs/systems-architecture/E2E-61-Architecture.html) | R3 Consignment Material - Vendor | E2E · Procure to Pay | 1 | 1 |
| 49 | [E2E-62](towers/E2E/Procure to Pay/E2E-62/output/docs/systems-architecture/E2E-62-Architecture.html) | R3 Vendor Return for Direct Material | E2E · Procure to Pay | 1 | 1 |
| 50 | [E2E-70](towers/E2E/Procure to Pay/E2E-70/output/docs/systems-architecture/E2E-70-Architecture.html) | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte | E2E · Procure to Pay | 1 | 1 |
| 51 | [E2E-88](towers/E2E/Procure to Pay/E2E-88/output/docs/systems-architecture/E2E-88-Architecture.html) | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme | E2E · Procure to Pay | 1 | 1 |
| 52 | [E2E-96](towers/E2E/Procure to Pay/E2E-96/output/docs/systems-architecture/E2E-96-Architecture.html) | R3 Straddle & R4 SIMS Design with Returns | E2E · Procure to Pay | 1 | 1 |
| 53 | [E2E-98](towers/E2E/Procure to Pay/E2E-98/output/docs/systems-architecture/E2E-98-Architecture.html) | R3 Equipment Product Supporting Items (PSI) Procurement | E2E · Procure to Pay | 1 | 1 |
| 54 | [DC-010](towers/FPR/DC Manage Accounting and Control Data/DC-010/output/docs/systems-architecture/DC-010-Architecture.html) | Perform Transaction Processing | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 55 | [DC-020](towers/FPR/DC Manage Accounting and Control Data/DC-020/output/docs/systems-architecture/DC-020-Architecture.html) | Manage the General Ledger | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 56 | [DC-030](towers/FPR/DC Manage Accounting and Control Data/DC-030/output/docs/systems-architecture/DC-030-Architecture.html) | Perform Closing | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 57 | [DC-040](towers/FPR/DC Manage Accounting and Control Data/DC-040/output/docs/systems-architecture/DC-040-Architecture.html) | Perform Fixed Asset Accounting | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 58 | [DC-050](towers/FPR/DC Manage Accounting and Control Data/DC-050/output/docs/systems-architecture/DC-050-Architecture.html) | Project Accounting | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 59 | [DC-060](towers/FPR/DC Manage Accounting and Control Data/DC-060/output/docs/systems-architecture/DC-060-Architecture.html) | Manage Taxes | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 60 | [DC-100](towers/FPR/DC Manage Accounting and Control Data/DC-100/output/docs/systems-architecture/DC-100-Architecture.html) | Revenue Recognition | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 61 | [DC-110](towers/FPR/DC Manage Accounting and Control Data/DC-110/output/docs/systems-architecture/DC-110-Architecture.html) | Manage Intercompany | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 62 | [DC-120](towers/FPR/DC Manage Accounting and Control Data/DC-120/output/docs/systems-architecture/DC-120-Architecture.html) | Maintenance & Management Accounting | FPR · DC Manage Accounting and Control Data | 0 | 0 |
| 63 | [DS-010](towers/FPR/DS Provide Decision Support/DS-010/output/docs/systems-architecture/DS-010-Architecture.html) | Perform Overhead Accounting and Allocation | FPR · DS Provide Decision Support | 0 | 0 |
| 64 | [DS-020](towers/FPR/DS Provide Decision Support/DS-020/output/docs/systems-architecture/DS-020-Architecture.html) | Perform Product Costing and Inventory Valuation | FPR · DS Provide Decision Support | 36 | 114 |
| 65 | [DS-030](towers/FPR/DS Provide Decision Support/DS-030/output/docs/systems-architecture/DS-030-Architecture.html) | Perform Customer and Product Profitability Analysis | FPR · DS Provide Decision Support | 0 | 0 |
| 66 | [MB-060](towers/FPR/MB Plan and Manage Business/MB-060/output/docs/systems-architecture/MB-060-Architecture.html) | Plan the Business | FPR · MB Plan and Manage Business | 0 | 0 |
| 67 | [MB-070](towers/FPR/MB Plan and Manage Business/MB-070/output/docs/systems-architecture/MB-070-Architecture.html) | Prepare Budgets | FPR · MB Plan and Manage Business | 0 | 0 |
| 68 | [MR-010](towers/FPR/MR Manage Capital and Risk/MR-010/output/docs/systems-architecture/MR-010-Architecture.html) | Manage Liquidity | FPR · MR Manage Capital and Risk | 0 | 0 |
| 69 | [MR-020](towers/FPR/MR Manage Capital and Risk/MR-020/output/docs/systems-architecture/MR-020-Architecture.html) | Manage Capital Structure | FPR · MR Manage Capital and Risk | 0 | 0 |
| 70 | [MR-030](towers/FPR/MR Manage Capital and Risk/MR-030/output/docs/systems-architecture/MR-030-Architecture.html) | Manage Financial Risk | FPR · MR Manage Capital and Risk | 0 | 0 |
| 71 | [MR-070](towers/FPR/MR Manage Capital and Risk/MR-070/output/docs/systems-architecture/MR-070-Architecture.html) | In-House Banking | FPR · MR Manage Capital and Risk | 0 | 0 |
| 72 | [OR-140](towers/FPR/OR Receivables Management/OR-140/output/docs/systems-architecture/OR-140-Architecture.html) | Process Receipts | FPR · OR Receivables Management | 0 | 0 |
| 73 | [L-040](towers/FTS-IF/L Logistics and Inventory Management - FTS (IF)/L-040/output/docs/systems-architecture/L-040-Architecture.html) | Receive and Put-away Product - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 0 | 0 |
| 74 | [L-060](towers/FTS-IF/L Logistics and Inventory Management - FTS (IF)/L-060/output/docs/systems-architecture/L-060-Architecture.html) | Manage Storage & Internal Movement of Inventory - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 0 | 0 |
| 75 | [L-110](towers/FTS-IF/L Logistics and Inventory Management - FTS (IF)/L-110/output/docs/systems-architecture/L-110-Architecture.html) | Manage Lots Batches - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 0 | 0 |
| 76 | [L-120](towers/FTS-IF/L Logistics and Inventory Management - FTS (IF)/L-120/output/docs/systems-architecture/L-120-Architecture.html) | Manage Line Replenishment - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 0 | 0 |
| 77 | [LI-120](towers/FTS-IF/LI Logistics Management Inbound - FTS (IF)/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) | Receive Materials and Services - FTS (IF) | FTS-IF · LI Logistics Management Inbound - FTS (IF) | 0 | 0 |
| 78 | [LO-160](towers/FTS-IF/LO Logistics Management Outbound - FTS (IF)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders- FTS (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 0 | 0 |
| 79 | [LO-170](towers/FTS-IF/LO Logistics Management Outbound - FTS (IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Order - FTS  (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 0 | 0 |
| 80 | [LO-180](towers/FTS-IF/LO Logistics Management Outbound - FTS (IF)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - FTS (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 0 | 0 |
| 81 | [LO-190](towers/FTS-IF/L Logistics and Inventory Management - FTS (IF)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 0 | 0 |
| 82 | [M-080](towers/FTS-IF/M Mfg. Schedule and Execution (IF)/M-080/output/docs/systems-architecture/M-080-Architecture.html) | Perform Materials Requirement Planning (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 0 | 0 |
| 83 | [M-090](towers/FTS-IF/M Mfg. Schedule and Execution (IF)/M-090/output/docs/systems-architecture/M-090-Architecture.html) | Schedule Production (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 0 | 0 |
| 84 | [M-100](towers/FTS-IF/M Mfg. Schedule and Execution (IF)/M-100/output/docs/systems-architecture/M-100-Architecture.html) | Execute Production (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 0 | 0 |
| 85 | [M-170](towers/FTS-IF/M Mfg. Schedule and Execution (IF)/M-170/output/docs/systems-architecture/M-170-Architecture.html) | Control and Report Production Operations (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 0 | 0 |
| 86 | [PE-020](towers/FTS-IF/PE Manage Plant, Equipment and Facilities (IF)/PE-020/output/docs/systems-architecture/PE-020-Architecture.html) | Identify Maintenance Structure | FTS-IF · PE Manage Plant, Equipment and Facilities | 0 | 0 |
| 87 | [PE-040](towers/FTS-IF/PE Manage Plant, Equipment and Facilities (IF)/PE-040/output/docs/systems-architecture/PE-040-Architecture.html) | Monitor | FTS-IF · PE Manage Plant, Equipment and Facilities | 0 | 0 |
| 88 | [PE-050](towers/FTS-IF/PE Manage Plant, Equipment and Facilities (IF)/PE-050/output/docs/systems-architecture/PE-050-Architecture.html) | Maintain Work Order Historical Documentation | FTS-IF · PE Manage Plant, Equipment and Facilities | 0 | 0 |
| 89 | [PE-060](towers/FTS-IF/PE Manage Plant, Equipment and Facilities (IF)/PE-060/output/docs/systems-architecture/PE-060-Architecture.html) | Maintain and Manage Master Maintenance Records | FTS-IF · PE Manage Plant, Equipment and Facilities | 0 | 0 |
| 90 | [PE-070](towers/FTS-IF/PE Manage Plant, Equipment and Facilities (IF)/PE-070/output/docs/systems-architecture/PE-070-Architecture.html) | Identify and Plan Plant Maintenance | FTS-IF · PE Manage Plant, Equipment and Facilities | 0 | 0 |
| 91 | [PE-090](towers/FTS-IF/PE Manage Plant, Equipment and Facilities (IF)/PE-090/output/docs/systems-architecture/PE-090-Architecture.html) | Execute Plant Maintenance | FTS-IF · PE Manage Plant, Equipment and Facilities | 0 | 0 |
| 92 | [PLB-020](towers/FTS-IF/PLB Supply Chain Planning (IF)/PLB-020/output/docs/systems-architecture/PLB-020-Architecture.html) | Supply Planning & Management (IF) | FTS-IF · PLB Supply Chain Planning (IF) | 0 | 0 |
| 93 | [Q-140](towers/FTS-IF/Q Quality Management (IF)/Q-140/output/docs/systems-architecture/Q-140-Architecture.html) | Manage Product Disposition (IF) | FTS-IF · Q Quality Management (IF) | 0 | 0 |
| 94 | [L-060](towers/FTS-IP/L Logistics and Inventory Management - FTS (IP)/L-060/output/docs/systems-architecture/L-060-Architecture.html) | Manage Storage and Internal Movement of Inventory - FTS (IP) | FTS-IP · L Logistics and Inventory Management - FTS (IP) | 0 | 0 |
| 95 | [LI-120](towers/FTS-IP/LI Logistics Management Inbound - FTS (IP)/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) | Receive Materials and Services - FTS (IP) | FTS-IP · LI Logistics Management Inbound - FTS (IP) | 0 | 0 |
| 96 | [LO-160](towers/FTS-IP/LO Logistics Management Outbound - FTS (IP)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 0 | 0 |
| 97 | [LO-170](towers/FTS-IP/LO Logistics Management Outbound - FTS (IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Orders - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 0 | 0 |
| 98 | [LO-180](towers/FTS-IP/L Logistics and Inventory Management - FTS (IP)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 0 | 0 |
| 99 | [LO-190](towers/FTS-IP/LO Logistics Management Outbound - FTS (IP)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 0 | 0 |
| 100 | [M-080](towers/FTS-IP/M Mfg. Schedule and Execution (IP)/M-080/output/docs/systems-architecture/M-080-Architecture.html) | Perform Materials Requirement Planning (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | 0 | 0 |
| 101 | [M-090](towers/FTS-IP/M Mfg. Schedule and Execution (IP)/M-090/output/docs/systems-architecture/M-090-Architecture.html) | Schedule Production (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | 0 | 0 |
| 102 | [M-100](towers/FTS-IP/M Mfg. Schedule and Execution (IP)/M-100/output/docs/systems-architecture/M-100-Architecture.html) | Execute Production (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | 0 | 0 |
| 103 | [PLB-020](towers/FTS-IP/PLB Supply Chain Planning (IP)/PLB-020/output/docs/systems-architecture/PLB-020-Architecture.html) | Supply Planning & Management (IP) | FTS-IP · PLB Supply Chain Planning (IP) | 0 | 0 |
| 104 | [PLB-050](towers/FTS-IP/PLB Supply Chain Planning (IP)/PLB-050/output/docs/systems-architecture/PLB-050-Architecture.html) | Responsive Demand and Supply Matching (RDSM) (IP) | FTS-IP · PLB Supply Chain Planning (IP) | 0 | 0 |
| 105 | [Q-140](towers/FTS-IP/Q Quality Management (IP)/Q-140/output/docs/systems-architecture/Q-140-Architecture.html) | Manage Product Disposition (IP) | FTS-IP · Q Quality Management (IP) | 0 | 0 |
| 106 | [MDM-020](towers/MDM/MDM Manage Master Data/MDM-020/output/docs/systems-architecture/MDM-020-Architecture.html) | Create and Maintain Vendors | MDM · MDM-Manage Master Data | 0 | 0 |
| 107 | [MDM-130](towers/MDM/MDM Manage Master Data/MDM-130/output/docs/systems-architecture/MDM-130-Architecture.html) | Create and Maintain Customers | MDM · MDM-Manage Master Data | 0 | 0 |
| 108 | [MDM-140](towers/MDM/MDM Manage Master Data/MDM-140/output/docs/systems-architecture/MDM-140-Architecture.html) | Create and Maintain Reference Data | MDM · MDM-Manage Master Data | 0 | 0 |
| 109 | [MDM-150](towers/MDM/MDM Manage Master Data/MDM-150/output/docs/systems-architecture/MDM-150-Architecture.html) | Maintain Product Related Data | MDM · MDM-Manage Master Data | 0 | 0 |
| 110 | [BR-130](towers/OTC-IF/BR Billing and Rebates (IF)/BR-130/output/docs/systems-architecture/BR-130-Architecture.html) | Billing Revenue (IF) | OTC-IF · BR-Billing and Rebates (IF) | 0 | 0 |
| 111 | [CM-050](towers/OTC-IF/CM Credit and Collections Management (IF)/CM-050/output/docs/systems-architecture/CM-050-Architecture.html) | Manage Customer Credit Exposure (IF) | OTC-IF · CM-Credit &amp; Collections Management (IF) | 0 | 0 |
| 112 | [CM-060](towers/OTC-IF/CM Credit and Collections Management (IF)/CM-060/output/docs/systems-architecture/CM-060-Architecture.html) | Manage Collections (IF) | OTC-IF · CM-Credit &amp; Collections Management (IF) | 0 | 0 |
| 113 | [GT-010](towers/OTC-IF/GT Global Trade (IF)/GT-010/output/docs/systems-architecture/GT-010-Architecture.html) | Manage Global Trade Master Data (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 114 | [GT-020](towers/OTC-IF/GT Global Trade (IF)/GT-020/output/docs/systems-architecture/GT-020-Architecture.html) | Product Classification (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 115 | [GT-030](towers/OTC-IF/GT Global Trade (IF)/GT-030/output/docs/systems-architecture/GT-030-Architecture.html) | Compliance Screening (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 116 | [GT-040](towers/OTC-IF/GT Global Trade (IF)/GT-040/output/docs/systems-architecture/GT-040-Architecture.html) | Manage Licenses (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 117 | [GT-050](towers/OTC-IF/GT Global Trade (IF)/GT-050/output/docs/systems-architecture/GT-050-Architecture.html) | Customs declaration creation Export (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 118 | [GT-070](towers/OTC-IF/GT Global Trade (IF)/GT-070/output/docs/systems-architecture/GT-070-Architecture.html) | Customs Declaration Completion Export | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 119 | [GT-080](towers/OTC-IF/GT Global Trade (IF)/GT-080/output/docs/systems-architecture/GT-080-Architecture.html) | Customs Declaration Communication - Self Filing (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 120 | [GT-110](towers/OTC-IF/GT Global Trade (IF)/GT-110/output/docs/systems-architecture/GT-110-Architecture.html) | Monitor completed declaration (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 121 | [GT-130](towers/OTC-IF/GT Global Trade (IF)/GT-130/output/docs/systems-architecture/GT-130-Architecture.html) | Intrastat Filing (S4) (IF) | OTC-IF · GT Global Trade (IF) | 0 | 0 |
| 122 | [LO-160](towers/OTC-IF/LO Logistics Management Outbound - OTC (IF)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 0 | 0 |
| 123 | [LO-170](towers/OTC-IF/LO Logistics Management Outbound - OTC (IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 0 | 0 |
| 124 | [LO-180](towers/OTC-IF/LO Logistics Management Outbound - OTC (IF)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 0 | 0 |
| 125 | [LO-190](towers/OTC-IF/LO Logistics Management Outbound - OTC (IF)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship Deliver Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 0 | 0 |
| 126 | [O-020](towers/OTC-IF/O Order Management (IF)/O-020/output/docs/systems-architecture/O-020-Architecture.html) | Capture Orders (IF) | OTC-IF · O-Order Management (IF) | 0 | 0 |
| 127 | [O-030](towers/OTC-IF/O Order Management (IF)/O-030/output/docs/systems-architecture/O-030-Architecture.html) | Process Orders (IF) | OTC-IF · O-Order Management (IF) | 0 | 0 |
| 128 | [O-040](towers/OTC-IF/O Order Management (IF)/O-040/output/docs/systems-architecture/O-040-Architecture.html) | Calculate Order Price (IF) | OTC-IF · O-Order Management (IF) | 0 | 0 |
| 129 | [O-060](towers/OTC-IF/O Order Management (IF)/O-060/output/docs/systems-architecture/O-060-Architecture.html) | Manage and Track Orders (IF) | OTC-IF · O-Order Management (IF) | 0 | 0 |
| 130 | [O-070](towers/OTC-IF/O Order Management (IF)/O-070/output/docs/systems-architecture/O-070-Architecture.html) | Manage Backorders (IF) | OTC-IF · O-Order Management (IF) | 0 | 0 |
| 131 | [R-190](towers/OTC-IF/R Returns (IF)/R-190/output/docs/systems-architecture/R-190-Architecture.html) | Manage Returns and Exchanges (IF) | OTC-IF · R-Returns (IF) | 0 | 0 |
| 132 | [R-200](towers/OTC-IF/R Returns (IF)/R-200/output/docs/systems-architecture/R-200-Architecture.html) | Return - Receive Materials and Services (IF) | OTC-IF · R-Returns (IF) | 0 | 0 |
| 133 | [R-210](towers/OTC-IF/R Returns (IF)/R-210/output/docs/systems-architecture/R-210-Architecture.html) | Returns - Determine Discrepant Material Disposition (IF) | OTC-IF · R-Returns (IF) | 0 | 0 |
| 134 | [R-220](towers/OTC-IF/R Returns (IF)/R-220/output/docs/systems-architecture/R-220-Architecture.html) | Returns - Manage In-bound Transportation (IF) | OTC-IF · R-Returns (IF) | 0 | 0 |
| 135 | [BR-130](towers/OTC-IP/BR Billing and Rebates (IP)/BR-130/output/docs/systems-architecture/BR-130-Architecture.html) | Billing Revenue (IP) | OTC-IP · BR-Billing and Rebates (IP) | 0 | 0 |
| 136 | [BR-160](towers/OTC-IP/BR Billing and Rebates (IP)/BR-160/output/docs/systems-architecture/BR-160-Architecture.html) | Manage Rebates (IP) | OTC-IP · BR-Billing and Rebates (IP) | 0 | 0 |
| 137 | [BR-170](towers/OTC-IP/BR Billing and Rebates (IP)/BR-170/output/docs/systems-architecture/BR-170-Architecture.html) | Manage Chargebacks (IP) | OTC-IP · BR-Billing and Rebates (IP) | 0 | 0 |
| 138 | [CM-050](towers/OTC-IP/CM Credit and Collections Management (IP)/CM-050/output/docs/systems-architecture/CM-050-Architecture.html) | Manage Customer Credit Exposure (IP) | OTC-IP · CM-Credit &amp; Collections Management (IP) | 0 | 0 |
| 139 | [CM-060](towers/OTC-IP/CM Credit and Collections Management (IP)/CM-060/output/docs/systems-architecture/CM-060-Architecture.html) | Manage Collections (IP) | OTC-IP · CM-Credit &amp; Collections Management (IP) | 0 | 0 |
| 140 | [GT-010](towers/OTC-IP/GT Global Trade (IP)/GT-010/output/docs/systems-architecture/GT-010-Architecture.html) | Manage Global Trade Master Data (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 141 | [GT-020](towers/OTC-IP/GT Global Trade (IP)/GT-020/output/docs/systems-architecture/GT-020-Architecture.html) | Product Classification (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 142 | [GT-030](towers/OTC-IP/GT Global Trade (IP)/GT-030/output/docs/systems-architecture/GT-030-Architecture.html) | Compliance Screening (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 143 | [GT-040](towers/OTC-IP/GT Global Trade (IP)/GT-040/output/docs/systems-architecture/GT-040-Architecture.html) | Manage Licenses (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 144 | [GT-050](towers/OTC-IP/GT Global Trade (IP)/GT-050/output/docs/systems-architecture/GT-050-Architecture.html) | Customs Declaration Creation Export (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 145 | [GT-060](towers/OTC-IP/GT Global Trade (IP)/GT-060/output/docs/systems-architecture/GT-060-Architecture.html) | Customs declaration creation Import (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 146 | [GT-070](towers/OTC-IP/GT Global Trade (IP)/GT-070/output/docs/systems-architecture/GT-070-Architecture.html) | Customs Declaration Completion Export | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 147 | [GT-080](towers/OTC-IP/GT Global Trade (IP)/GT-080/output/docs/systems-architecture/GT-080-Architecture.html) | Customs Declaration Communication - Self Filing (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 148 | [GT-090](towers/OTC-IP/GT Global Trade (IP)/GT-090/output/docs/systems-architecture/GT-090-Architecture.html) | Customs declaration communication - broker filing (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 149 | [GT-110](towers/OTC-IP/GT Global Trade (IP)/GT-110/output/docs/systems-architecture/GT-110-Architecture.html) | Monitor Completed Declaration (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 150 | [GT-130](towers/OTC-IP/GT Global Trade (IP)/GT-130/output/docs/systems-architecture/GT-130-Architecture.html) | Intrastat Filing (S4) (IP) | OTC-IP · GT-Global Trade (IP) | 0 | 0 |
| 151 | [LO-160](towers/OTC-IP/LO Logistics Management Outbound - OTC (IP)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 0 | 0 |
| 152 | [LO-170](towers/OTC-IP/LO Logistics Management Outbound - OTC (IP)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 0 | 0 |
| 153 | [LO-180](towers/OTC-IP/LO Logistics Management Outbound - OTC (IP)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 0 | 0 |
| 154 | [LO-190](towers/OTC-IP/LO Logistics Management Outbound - OTC (IP)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship Deliver Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 0 | 0 |
| 155 | [O-020](towers/OTC-IP/O Order Management (IP)/O-020/output/docs/systems-architecture/O-020-Architecture.html) | Capture Orders (IP) | OTC-IP · O-Order Management (IP) | 0 | 0 |
| 156 | [O-030](towers/OTC-IP/O Order Management (IP)/O-030/output/docs/systems-architecture/O-030-Architecture.html) | Process Orders (IP) | OTC-IP · O-Order Management (IP) | 0 | 0 |
| 157 | [O-040](towers/OTC-IP/O Order Management (IP)/O-040/output/docs/systems-architecture/O-040-Architecture.html) | Calculate Order Price (IP) | OTC-IP · O-Order Management (IP) | 0 | 0 |
| 158 | [O-060](towers/OTC-IP/O Order Management (IP)/O-060/output/docs/systems-architecture/O-060-Architecture.html) | Manage and Track Orders (IP) | OTC-IP · O-Order Management (IP) | 0 | 0 |
| 159 | [O-070](towers/OTC-IP/O Order Management (IP)/O-070/output/docs/systems-architecture/O-070-Architecture.html) | Manage Backorders (IP) | OTC-IP · O-Order Management (IP) | 0 | 0 |
| 160 | [R-190](towers/OTC-IP/R Returns (IP)/R-190/output/docs/systems-architecture/R-190-Architecture.html) | Manage Returns and Exchanges (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 161 | [R-200](towers/OTC-IP/R Returns (IP)/R-200/output/docs/systems-architecture/R-200-Architecture.html) | Return - Receive Materials and Services (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 162 | [R-220](towers/OTC-IP/R Returns (IP)/R-220/output/docs/systems-architecture/R-220-Architecture.html) | Returns - Manage In-bound Transportation (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 163 | [R-230](towers/OTC-IP/R Returns (IP)/R-230/output/docs/systems-architecture/R-230-Architecture.html) | Returns - Manage Storage & Internal Movement of Inventory (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 164 | [R-240](towers/OTC-IP/R Returns (IP)/R-240/output/docs/systems-architecture/R-240-Architecture.html) | Returns - Manage Storage & Internal Movement of Inventory (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 165 | [R-250](towers/OTC-IP/R Returns (IP)/R-250/output/docs/systems-architecture/R-250-Architecture.html) | Returns - Receive and Put-away Product (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 166 | [R-260](towers/OTC-IP/R Returns (IP)/R-260/output/docs/systems-architecture/R-260-Architecture.html) | Returns - Pick Orders (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 167 | [R-270](towers/OTC-IP/R Returns (IP)/R-270/output/docs/systems-architecture/R-270-Architecture.html) | Returns - Pack Orders (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 168 | [R-280](towers/OTC-IP/R Returns (IP)/R-280/output/docs/systems-architecture/R-280-Architecture.html) | Returns - Ship Orders (IP) | OTC-IP · R-Returns (IP) | 0 | 0 |
| 169 | [R-290](towers/OTC-IP/R Returns (IP)/R-290/output/docs/systems-architecture/R-290-Architecture.html) | Returns - Manage Lots | OTC-IP · R-Returns (IP) | 0 | 0 |
| 170 | [L-040](towers/PTP/L Logistics and Inventory Management - PTP/L-040/output/docs/systems-architecture/L-040-Architecture.html) | Receive and Put-away Product - PTP | PTP · L Logistics and Inventory Management - PTP | 0 | 0 |
| 171 | [L-060](towers/PTP/L Logistics and Inventory Management - PTP/L-060/output/docs/systems-architecture/L-060-Architecture.html) | Manage Storage and Internal Movement of Inventory - PTP | PTP · L Logistics and Inventory Management - PTP | 0 | 0 |
| 172 | [L-110](towers/PTP/L Logistics and Inventory Management - PTP/L-110/output/docs/systems-architecture/L-110-Architecture.html) | Manage Lots Batches - PTP | PTP · L Logistics and Inventory Management - PTP | 0 | 0 |
| 173 | [LI-030](towers/PTP/LI Logistics Management Inbound - PTP/LI-030/output/docs/systems-architecture/LI-030-Architecture.html) | Manage In-bound Transportation - PTP | PTP · LI Logistics Management Inbound - PTP | 0 | 0 |
| 174 | [LI-100](towers/PTP/LI Logistics Management Inbound - PTP/LI-100/output/docs/systems-architecture/LI-100-Architecture.html) | Manage Supplier Consignment Stock | PTP · LI Logistics Management Inbound - PTP | 0 | 0 |
| 175 | [LI-120](towers/PTP/LI Logistics Management Inbound - PTP/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) | Receive Materials and Services - PTP | PTP · LI Logistics Management Inbound - PTP | 0 | 0 |
| 176 | [LI-200](towers/PTP/LI Logistics Management Inbound - PTP/LI-200/output/docs/systems-architecture/LI-200-Architecture.html) | Determine Discrepant Material Disposition | PTP · LI Logistics Management Inbound - PTP | 0 | 0 |
| 177 | [PM-040](towers/PTP/PM Procure Materials and Services (Direct and Indirect)/PM-040/output/docs/systems-architecture/PM-040-Architecture.html) | Maintain Supplier Certification and Monitor Performance | PTP · PM-Procure Materials and Services (Direct &amp; Indirect) | 0 | 0 |
| 178 | [PM-050](towers/PTP/PM Procure Materials and Services (Direct and Indirect)/PM-050/output/docs/systems-architecture/PM-050-Architecture.html) | Manage Quotation | PTP · PM-Procure Materials and Services (Direct &amp; Indirect) | 0 | 0 |
| 179 | [PM-070](towers/PTP/PM Procure Materials and Services (Direct and Indirect)/PM-070/output/docs/systems-architecture/PM-070-Architecture.html) | Create and Maintain Purchase Requisitions | PTP · PM-Procure Materials and Services (Direct &amp; Indirect) | 0 | 0 |
| 180 | [PM-080](towers/PTP/PM Procure Materials and Services (Direct and Indirect)/PM-080/output/docs/systems-architecture/PM-080-Architecture.html) | Purchase Materials and Services | PTP · PM-Procure Materials and Services (Direct &amp; Indirect) | 0 | 0 |
| 181 | [PM-090](towers/PTP/PM Procure Materials and Services (Direct and Indirect)/PM-090/output/docs/systems-architecture/PM-090-Architecture.html) | Manage Contracts | PTP · PM-Procure Materials and Services (Direct &amp; Indirect) | 0 | 0 |
| 182 | [PM-110](towers/PTP/PM Procure Materials and Services (Direct and Indirect)/PM-110/output/docs/systems-architecture/PM-110-Architecture.html) | Procure Subcontracting | PTP · PM-Procure Materials and Services (Direct &amp; Indirect) | 0 | 0 |
| 183 | [PM-150](towers/PTP/PM Procure Materials and Services (Direct and Indirect)/PM-150/output/docs/systems-architecture/PM-150-Architecture.html) | Enable Payment | PTP · PM-Procure Materials and Services (Direct &amp; Indirect) | 0 | 0 |
| 184 | [QI-130](towers/PTP/QI Quality Management (Incoming)/QI-130/output/docs/systems-architecture/QI-130-Architecture.html) | Perform Incoming Quality Assurance | PTP · QI-Quality Management (Incoming) | 0 | 0 |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 3 Current-State Architecture

Aggregated current-state view of **28** systems with **32** unique connections across **89** flow hops.

<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 3.1 System Integration Map

```mermaid
graph LR
    SC_APIGEE["📦 APIGEE"]
    SC_Azure_ADF["📦 Azure ADF"]
    SC_BOBJ["📦 BOBJ"]
    SC_CFIN_S_4["📦 CFIN S/4"]
    SC_CIBR["📦 CIBR"]
    SC_Corp___IP_S_4["📦 Corp / IP S/4"]
    SC_DataBricks["📦 DataBricks"]
    SC_EATS["📦 EATS"]
    SC_ECA["📦 ECA"]
    SC_EDW["📦 EDW"]
    SC_FCA["📦 FCA"]
    SC_Finance_HANA["📦 Finance HANA"]
    SC_ICOST["📦 ICOST"]
    SC_Legacy_MDG["📦 Legacy MDG"]
    SC_MARS["📦 MARS"]
    SC_MES_300["📦 MES 300"]
    SC_PEGA["📦 PEGA"]
    SC_SAP_BODS["📦 SAP BODS"]
    SC_SAP_ECC["📦 SAP ECC"]
    SC_SAP_IBP["📦 SAP IBP"]
    SC_SAP_PO["📦 SAP PO"]
    SC_SPEED["📦 SPEED"]
    SC_SideCar["📦 SideCar"]
    SC_SnowFlake["📦 SnowFlake"]
    SC_WorkStream["📦 WorkStream"]
    SC_XEUS["📦 XEUS"]
    SC_e_g__MES_300["📦 e.g. MES 300"]
    SC_e_g__XEUS["📦 e.g. XEUS"]

    SC_APIGEE -->|"APIGEE | 1 flow"| SC_PEGA
    SC_Azure_ADF -->|"ADF Pipeline | 1 flow"| SC_DataBricks
    SC_CIBR -->|"Internal | 1 flow"| SC_ICOST
    SC_CIBR -->|"SAP PO | 1 flow"| SC_SAP_PO
    SC_Corp___IP_S_4 -->|"SLT | 2 flows"| SC_ECA
    SC_DataBricks -->|"Internal | 1 flow"| SC_SnowFlake
    SC_EATS -->|"Internal | 1 flow"| SC_ICOST
    SC_ECA -->|"Internal | 1 flow"| SC_CIBR
    SC_ECA -->|"Internal | 1 flow"| SC_ICOST
    SC_EDW -->|"ETL | 1 flow"| SC_CIBR
    SC_EDW -->|"ETL | 1 flow"| SC_ICOST
    SC_FCA -->|"Direct | 1 flow"| SC_ICOST
    SC_Finance_HANA -->|"APIGEE | 1 flow"| SC_APIGEE
    SC_Finance_HANA -->|"Direct | 1 flow"| SC_BOBJ
    SC_Finance_HANA -->|"SAP PO | 1 flow"| SC_SAP_PO
    SC_ICOST -->|"SAP BODS | 1 flow"| SC_SAP_BODS
    SC_Legacy_MDG -->|"MDG | 1 flow"| SC_SAP_ECC
    SC_MARS -->|"Internal | 1 flow"| SC_ICOST
    SC_MES_300 -->|"Direct | 1 flow"| SC_XEUS
    SC_SAP_BODS -->|"SAP BODS | 1 flow"| SC_SAP_ECC
    SC_SAP_ECC -->|"Replication | 1 flow"| SC_CFIN_S_4
    SC_SAP_ECC -->|"ETL | 3 flows"| SC_EDW
    SC_SAP_ECC -->|"SLT | 1 flow"| SC_Finance_HANA
    SC_SAP_ECC -->|"SLT | 1 flow"| SC_SideCar
    SC_SAP_IBP -->|"Direct | 1 flow"| SC_ECA
    SC_SAP_PO -->|"SAP PO | 3 flows"| SC_SAP_ECC
    SC_SPEED -->|"Direct | 1 flow"| SC_EDW
    SC_SPEED -->|"SAP PO | 1 flow"| SC_SAP_PO
    SC_SideCar -->|"CIF | 1 flow"| SC_Azure_ADF
    SC_WorkStream -->|"Direct | 1 flow"| SC_MARS
    SC_XEUS -->|"Internal | 1 flow"| SC_ICOST
    SC_e_g__MES_300 -->|"e.g. Direct / API / File | 53 flows"| SC_e_g__XEUS
```

<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 3.2 ArchiMate Application View

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
        SCA_e_g__MES_300["📦 e.g. MES 300"]
        SCA_e_g__XEUS["📦 e.g. XEUS"]
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
    SCA_e_g__MES_300 -->|"e.g. Direct / API / File"| SCA_e_g__XEUS

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
    class SCA_e_g__MES_300 app
    class SCA_e_g__XEUS app
    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px
```

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 3.3 Data Entities

**1** data entities in current-state flows.

| # | Data Entity | Source | Target | Owner | Classification | Volume | Master/Txn |
|:---:|---|---|---|---|---|---|---|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 8</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 3.4 Integration Patterns

**1** integration patterns in current-state.

| # | Pattern | Middleware | Protocol | Auth Method | Flow Chain |
|:---:|---|---|---|---|---|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert | e.g. MES Route to ICOST |

<div class="page-footer"><span>Page 9</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 3.5 Technology Stack

**2** technology platforms in current-state.

| # | Platform | Type | Systems | Environment |
|:---:|---|---|---|---|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 10</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 4 Future-State Architecture

Aggregated future-state view of **44** systems with **54** unique connections across **167** flow hops.

<div class="page-footer"><span>Page 11</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 4.1 System Integration Map

```mermaid
graph LR
    SF_ATCR["📦 ATCR"]
    SF_CFIN_S_4_HANA["📦 CFIN S/4 HANA"]
    SF_Capacity_Forecast_Data_Store["📦 Capacity Forecast Data Store"]
    SF_Corp___IP_S_4_HANA["📦 Corp / IP S/4 HANA"]
    SF_DMOCR["📦 DMOCR"]
    SF_DXCR["📦 DXCR"]
    SF_ECA_ADLS["📦 ECA-ADLS"]
    SF_ECA_DataBricks["📦 ECA-DataBricks"]
    SF_ECA_SnowFlake["📦 ECA-SnowFlake"]
    SF_ECM__Windchill_["📦 ECM (Windchill)"]
    SF_FCS["📦 FCS"]
    SF_GraphiteConnect["📦 GraphiteConnect"]
    SF_ICS__Phoenix_["📦 ICS (Phoenix)"]
    SF_IF_Blue_Yonder["📦 IF Blue Yonder"]
    SF_IF_PDH_Consumptional["📦 IF PDH Consumptional"]
    SF_IF_PDH_Foundational["📦 IF PDH Foundational"]
    SF_IF_PDH_Raw["📦 IF PDH Raw"]
    SF_IF_S_4_HANA["📦 IF S/4 HANA"]
    SF_IP_Blue_Yonder["📦 IP Blue Yonder"]
    SF_IP_PDH_Consumptional["📦 IP PDH Consumptional"]
    SF_IP_PDH_Foundational["📦 IP PDH Foundational"]
    SF_IP_PDH_Raw["📦 IP PDH Raw"]
    SF_MARS["📦 MARS"]
    SF_MES_300["📦 MES 300"]
    SF_PDF_SMH["📦 PDF-SMH"]
    SF_PDH_Consumptional["📦 PDH Consumptional"]
    SF_PDH_Foundational["📦 PDH Foundational"]
    SF_PDH_Raw["📦 PDH Raw"]
    SF_PDM_Translator["📦 PDM Translator"]
    SF_Power_BI__DARC_["📦 Power BI (DARC)"]
    SF_SAP_Ariba["📦 SAP Ariba"]
    SF_SAP_BOBJ["📦 SAP BOBJ"]
    SF_SAP_IBP["📦 SAP IBP"]
    SF_SAP_PAPM["📦 SAP PAPM"]
    SF_SAP_S_4_MDG["📦 SAP S/4 MDG"]
    SF_SAP_SAC["📦 SAP SAC"]
    SF_SCS["📦 SCS"]
    SF_SPEED["📦 SPEED"]
    SF_SideCar["📦 SideCar"]
    SF_WSPW["📦 WSPW"]
    SF_WorkStream["📦 WorkStream"]
    SF_XEUS["📦 XEUS"]
    SF_e_g__MES_300["📦 e.g. MES 300"]
    SF_e_g__XEUS["📦 e.g. XEUS"]

    SF_ATCR -->|"Direct | 1 flow"| SF_Capacity_Forecast_Data_Store
    SF_CFIN_S_4_HANA -->|"SLT | 1 flow"| SF_SideCar
    SF_Capacity_Forecast_Data_Store -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo) | 6 flows"| SF_ECA_ADLS
    SF_Corp___IP_S_4_HANA -->|"SLT | 1 flow"| SF_SideCar
    SF_DMOCR -->|"Direct | 1 flow"| SF_Capacity_Forecast_Data_Store
    SF_DXCR -->|"Direct | 1 flow"| SF_Capacity_Forecast_Data_Store
    SF_ECA_ADLS -->|"Unity Catalog | 8 flows"| SF_ECA_DataBricks
    SF_ECA_DataBricks -->|"Snowflake Connector / Snowpipe | 8 flows"| SF_ECA_SnowFlake
    SF_ECA_SnowFlake -->|"MuleSoft/BODS | 1 flow"| SF_CFIN_S_4_HANA
    SF_ECA_SnowFlake -->|"MuleSoft/BODS | 2 flows"| SF_Corp___IP_S_4_HANA
    SF_ECA_SnowFlake -->|"MuleSoft/BODS | 9 flows"| SF_IF_S_4_HANA
    SF_ECA_SnowFlake -->|"Snowflake Connector / Snowpipe | 1 flow"| SF_Power_BI__DARC_
    SF_ECA_SnowFlake -->|"Remote Function Adapter / MuleSoft / SAP Integration Suite | 5 flows"| SF_SAP_PAPM
    SF_ECM__Windchill_ -->|"PDM Translator | 1 flow"| SF_PDM_Translator
    SF_FCS -->|"Direct | 1 flow"| SF_Capacity_Forecast_Data_Store
    SF_GraphiteConnect -->|"MuleSoft & Reltio | 1 flow"| SF_SAP_S_4_MDG
    SF_ICS__Phoenix_ -->|"Direct | 1 flow"| SF_Capacity_Forecast_Data_Store
    SF_IF_Blue_Yonder -->|"ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule) | 3 flows"| SF_IF_PDH_Raw
    SF_IF_PDH_Consumptional -->|"Snowflake Connector / Snowpipe | 5 flows"| SF_ECA_SnowFlake
    SF_IF_PDH_Foundational -->|"Unity Catalog | 5 flows"| SF_IF_PDH_Consumptional
    SF_IF_PDH_Raw -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo) | 5 flows"| SF_IF_PDH_Foundational
    SF_IF_S_4_HANA -->|"SLT | 2 flows"| SF_CFIN_S_4_HANA
    SF_IF_S_4_HANA -->|"SLT | 1 flow"| SF_SideCar
    SF_IP_Blue_Yonder -->|"ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule) | 3 flows"| SF_IP_PDH_Raw
    SF_IP_PDH_Consumptional -->|"Snowflake Connector / Snowpipe | 2 flows"| SF_ECA_SnowFlake
    SF_IP_PDH_Foundational -->|"Unity Catalog | 2 flows"| SF_IP_PDH_Consumptional
    SF_IP_PDH_Raw -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo) | 2 flows"| SF_IP_PDH_Foundational
    SF_MARS -->|"Direct | 1 flow"| SF_PDF_SMH
    SF_MES_300 -->|"Direct | 1 flow"| SF_XEUS
    SF_PDF_SMH -->|"EAI Connector | 2 flows"| SF_IF_S_4_HANA
    SF_PDH_Consumptional -->|"Snowflake Connector / Snowpipe | 1 flow"| SF_ECA_SnowFlake
    SF_PDH_Foundational -->|"Unity Catalog | 1 flow"| SF_IP_PDH_Consumptional
    SF_PDH_Raw -->|"ADF / DB Unity Catalog / Third Party (e.g., Denodo) | 1 flow"| SF_IP_PDH_Foundational
    SF_PDM_Translator -->|"PDM Translator | 2 flows"| SF_SAP_S_4_MDG
    SF_SAP_Ariba -->|"Apigee / MuleSoft | 1 flow"| SF_Corp___IP_S_4_HANA
    SF_SAP_Ariba -->|"Apigee / MuleSoft | 1 flow"| SF_IF_S_4_HANA
    SF_SAP_IBP -->|"ADF / DB Unity Catalog / Connectors /Third Party (e.g., APIs with Mule) | 2 flows"| SF_IF_PDH_Raw
    SF_SAP_PAPM -->|"SAP Integration Suite / Smart Data Integration/BTP Destinations (HTTP) | 1 flow"| SF_Corp___IP_S_4_HANA
    SF_SAP_PAPM -->|"SAP Integration Suite / Smart Data Integration/BTP Destinations (HTTP) | 1 flow"| SF_IF_S_4_HANA
    SF_SAP_S_4_MDG -->|"DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC) | 3 flows"| SF_Corp___IP_S_4_HANA
    SF_SAP_S_4_MDG -->|"DRF (Data Replication Framework) with Web Services (SOAP/File/Idoc/RFC) | 3 flows"| SF_IF_S_4_HANA
    SF_SAP_SAC -->|"SAP Odata services with connector | 1 flow"| SF_CFIN_S_4_HANA
    SF_SAP_SAC -->|"SAP Odata services with connector | 1 flow"| SF_Corp___IP_S_4_HANA
    SF_SAP_SAC -->|"SAC Data Export Service (API) - Direct Write (Speed Layer in Snowflake / Use ADF / MuleSoft for DataBricks | 3 flows"| SF_ECA_SnowFlake
    SF_SAP_SAC -->|"SAP Odata services with connector | 1 flow"| SF_IF_S_4_HANA
    SF_SCS -->|"Direct | 1 flow"| SF_Capacity_Forecast_Data_Store
    SF_SPEED -->|"ADF Rest API / SFTP(Blob) | 1 flow"| SF_ECA_ADLS
    SF_SPEED -->|"PDM Translator | 1 flow"| SF_PDM_Translator
    SF_SideCar -->|"ADF Rest API / SFTP(Blob) | 1 flow"| SF_ECA_ADLS
    SF_SideCar -->|"1 flow"| SF_SAP_BOBJ
    SF_WSPW -->|"Direct | 1 flow"| SF_ECA_SnowFlake
    SF_WorkStream -->|"Direct | 1 flow"| SF_MARS
    SF_XEUS -->|"Direct | 1 flow"| SF_PDF_SMH
    SF_e_g__MES_300 -->|"e.g. Direct / API / File | 53 flows"| SF_e_g__XEUS
```

<div class="page-footer"><span>Page 12</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 4.2 ArchiMate Application View

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
        SFA_e_g__MES_300["📦 e.g. MES 300"]
        SFA_e_g__XEUS["📦 e.g. XEUS"]
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
    SFA_e_g__MES_300 -->|"e.g. Direct / API / File"| SFA_e_g__XEUS

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
    class SFA_e_g__MES_300 app
    class SFA_e_g__XEUS app
    style BL fill:#FFFFF0,stroke:#B8860B,stroke-width:2px
    style AL fill:#F0FFFF,stroke:#0077B6,stroke-width:2px
```

<div class="page-footer"><span>Page 13</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 4.3 Data Entities

**1** data entities in future-state flows.

| # | Data Entity | Source | Target | Owner | Classification | Volume | Master/Txn |
|:---:|---|---|---|---|---|---|---|
| 1 | e.g. Cost Element | e.g. MES 300 | e.g. XEUS | Data steward | e.g. Intel Confidential | e.g. 10K rows/day | Master / Transaction |

<div class="page-footer"><span>Page 14</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 4.4 Integration Patterns

**1** integration patterns in future-state.

| # | Pattern | Middleware | Protocol | Auth Method | Flow Chain |
|:---:|---|---|---|---|---|
| 1 | e.g. Pub-Sub / P2P / ETL | e.g. Azure Service Bus | e.g. REST / RFC / SFTP | e.g. OAuth / NTLM / Cert | e.g. MES Route to ICOST |

<div class="page-footer"><span>Page 15</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 4.5 Technology Stack

**2** technology platforms in future-state.

| # | Platform | Type | Systems | Environment |
|:---:|---|---|---|---|
| 1 | e.g. Azure PaaS | Cloud / SaaS | e.g. XEUS | DEV,QAS,PRD |
| 2 | e.g. S/4 HANA 2023 | On-Premise | e.g. MES 300 | DEV,QAS,PRD |

<div class="page-footer"><span>Page 16</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 5 Transformation Analysis

<div class="page-footer"><span>Page 17</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 5.1 System Landscape Changes

**New Systems (35):** ATCR, CFIN S/4 HANA, Capacity Forecast Data Store, Corp / IP S/4 HANA, DMOCR, DXCR, ECA-ADLS, ECA-DataBricks, ECA-SnowFlake, ECM (Windchill), FCS, GraphiteConnect, ICS (Phoenix), IF Blue Yonder, IF PDH Consumptional, IF PDH Foundational, IF PDH Raw, IF S/4 HANA, IP Blue Yonder, IP PDH Consumptional, IP PDH Foundational, IP PDH Raw, PDF-SMH, PDH Consumptional, PDH Foundational, PDH Raw, PDM Translator, Power BI (DARC), SAP Ariba, SAP BOBJ, SAP PAPM, SAP S/4 MDG, SAP SAC, SCS, WSPW

**Retiring Systems (19):** APIGEE, Azure ADF, BOBJ, CFIN S/4, CIBR, Corp / IP S/4, DataBricks, EATS, ECA, EDW, FCA, Finance HANA, ICOST, Legacy MDG, PEGA, SAP BODS, SAP ECC, SAP PO, SnowFlake

**Continuing Systems:** 9

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

<div class="page-footer"><span>Page 18</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

### 5.2 Integration Complexity

| System | Current Connections | Future Connections | Delta |
|---|:---:|:---:|:---:|
| APIGEE | 2 | 0 | -2 |
| ATCR | 0 | 1 | +1 |
| Azure ADF | 2 | 0 | -2 |
| BOBJ | 1 | 0 | -1 |
| CFIN S/4 | 1 | 0 | -1 |
| CFIN S/4 HANA | 0 | 4 | +4 |
| CIBR | 4 | 0 | -4 |
| Capacity Forecast Data Store | 0 | 7 | +7 |
| Corp / IP S/4 | 1 | 0 | -1 |
| Corp / IP S/4 HANA | 0 | 6 | +6 |
| DMOCR | 0 | 1 | +1 |
| DXCR | 0 | 1 | +1 |
| DataBricks | 2 | 0 | -2 |
| EATS | 1 | 0 | -1 |
| ECA | 4 | 0 | -4 |
| ECA-ADLS | 0 | 4 | +4 |
| ECA-DataBricks | 0 | 2 | +2 |
| ECA-SnowFlake | 0 | 11 | +11 |
| ECM (Windchill) | 0 | 1 | +1 |
| EDW | 4 | 0 | -4 |
| FCA | 1 | 0 | -1 |
| FCS | 0 | 1 | +1 |
| Finance HANA | 4 | 0 | -4 |
| GraphiteConnect | 0 | 1 | +1 |
| ICOST | 8 | 0 | -8 |
| ICS (Phoenix) | 0 | 1 | +1 |
| IF Blue Yonder | 0 | 1 | +1 |
| IF PDH Consumptional | 0 | 2 | +2 |
| IF PDH Foundational | 0 | 2 | +2 |
| IF PDH Raw | 0 | 3 | +3 |
| IF S/4 HANA | 0 | 8 | +8 |
| IP Blue Yonder | 0 | 1 | +1 |
| IP PDH Consumptional | 0 | 3 | +3 |
| IP PDH Foundational | 0 | 3 | +3 |
| IP PDH Raw | 0 | 2 | +2 |
| Legacy MDG | 1 | 0 | -1 |
| MARS | 2 | 2 | — |
| MES 300 | 1 | 1 | — |
| PDF-SMH | 0 | 3 | +3 |
| PDH Consumptional | 0 | 1 | +1 |
| PDH Foundational | 0 | 1 | +1 |
| PDH Raw | 0 | 1 | +1 |
| PDM Translator | 0 | 3 | +3 |
| PEGA | 1 | 0 | -1 |
| Power BI (DARC) | 0 | 1 | +1 |
| SAP Ariba | 0 | 2 | +2 |
| SAP BOBJ | 0 | 1 | +1 |
| SAP BODS | 2 | 0 | -2 |
| SAP ECC | 7 | 0 | -7 |
| SAP IBP | 1 | 1 | — |
| SAP PAPM | 0 | 3 | +3 |
| SAP PO | 4 | 0 | -4 |
| SAP S/4 MDG | 0 | 4 | +4 |
| SAP SAC | 0 | 4 | +4 |
| SCS | 0 | 1 | +1 |
| SPEED | 2 | 2 | — |
| SideCar | 2 | 5 | +3 |
| SnowFlake | 1 | 0 | -1 |
| WSPW | 0 | 1 | +1 |
| WorkStream | 1 | 1 | — |
| XEUS | 2 | 2 | — |
| e.g. MES 300 | 1 | 1 | — |
| e.g. XEUS | 1 | 1 | — |

<div class="page-footer"><span>Page 19</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 6 System Inventory

| # | System | IAPM ID | Status |
|:---:|---|---|---|
| 1 | APIGEE | 22790 | Deployed |
| 2 | ATCR | - | N/A |
| 3 | Azure ADF | 25794 | Deployed |
| 4 | BOBJ | 17651 | Deployed |
| 5 | CFIN S/4 | 41052 | Deployed |
| 6 | CFIN S/4 HANA | 41052 | Deployed |
| 7 | CIBR | 237 | Deployed |
| 8 | Capacity Forecast Data Store | 37284 | Deployed |
| 9 | Corp / IP S/4 | 41363 | Developing |
| 10 | Corp / IP S/4 HANA | 41363 | Developing |
| 11 | DMOCR | 13284 | Deployed |
| 12 | DXCR | 13284 | Deployed |
| 13 | DataBricks | 41458 | Deployed |
| 14 | EATS | 119 | End of Life |
| 15 | ECA | 43119 | Deployed |
| 16 | ECA-ADLS | 43119 | Deployed |
| 17 | ECA-DataBricks | 43119 | Deployed |
| 18 | ECA-SnowFlake | 43119 | Deployed |
| 19 | ECM (Windchill) | 38775 | Deployed |
| 20 | EDW | 4010 | Deployed |
| 21 | FCA | 44990 | Deployed |
| 22 | FCS | 9297 | End of Life |
| 23 | Finance HANA | 42993 | Deployed |
| 24 | GraphiteConnect | 36398 | Deployed |
| 25 | ICOST | 9008 | Deployed |
| 26 | ICS (Phoenix) | 19477 | Deployed |
| 27 | IF Blue Yonder | 41040 | Deployed |
| 28 | IF PDH Consumptional | 40747 | Deployed |
| 29 | IF PDH Foundational | 40747 | Deployed |
| 30 | IF PDH Raw | 40747 | Deployed |
| 31 | IF S/4 HANA | 41363 | Developing |
| 32 | IP Blue Yonder | 41039 | Deployed |
| 33 | IP PDH Consumptional | 40750 | Developing |
| 34 | IP PDH Foundational | 40750 | Developing |
| 35 | IP PDH Raw | 40750 | Developing |
| 36 | Legacy MDG | 40068 | Deployed |
| 37 | MARS | 33537 | Deployed |
| 38 | MES 300 | 41275 | Deployed |
| 39 | PDF-SMH | 59283 | Developing |
| 40 | PDH Consumptional | 40747 | Deployed |
| 41 | PDH Foundational | 40747 | Deployed |
| 42 | PDH Raw | 40747 | Deployed |
| 43 | PDM Translator | - | N/A |
| 44 | PEGA | 43163 | Deployed |
| 45 | Power BI (DARC) | 63659 | Deployed |
| 46 | SAP Ariba | 19569 | Deployed |
| 47 | SAP BOBJ | 11377 | End of Life |
| 48 | SAP BODS | 19207 | Deployed |
| 49 | SAP ECC | 23736 | Deployed |
| 50 | SAP IBP | 40709 | Deployed |
| 51 | SAP PAPM | 41401 | Developing |
| 52 | SAP PO | 21195 | Deployed |
| 53 | SAP S/4 MDG | 40068 | Deployed |
| 54 | SAP SAC | 37401 | Deployed |
| 55 | SCS | 21327 | End of Life |
| 56 | SPEED | 31517 | Deployed |
| 57 | SideCar | 42993 | Deployed |
| 58 | SnowFlake | 35811 | Deployed |
| 59 | WSPW | 4119 | Deployed |
| 60 | WorkStream | 37871 | Deployed |
| 61 | XEUS | 35612 | Deployed |
| 62 | e.g. MES 300 | - | N/A |
| 63 | e.g. XEUS | - | N/A |

