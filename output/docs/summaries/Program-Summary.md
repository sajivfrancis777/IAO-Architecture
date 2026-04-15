<div style="text-align:center; padding-top:20px;">
  <img src="../../../templates/assets/cover_banner.svg" alt="IAO Architecture" style="width:100%; border-radius:8px;" />
  <h1 style="font-size:36px; margin-top:24px;">IAO Program Architecture Summary</h1>
  <h2 style="font-size:24px;">TOGAF BDAT — Aggregated Architecture View</h2>
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
   - [5.3 Release-over-Release Changes](#53-release-over-release-changes)
- [6. Capability Detail Reference](#6-capability-detail-reference)

<div class="page-footer"><span>Page 2</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 1 Executive Summary

This **Program** summary aggregates architecture diagrams from **184** L2 capabilities across **IDM 2.0 — All Towers (R1 – R5)**.

The diagrams below show the consolidated current-state and future-state system landscape **without duplicates** — each system and connection appears only once even when shared across capabilities. For detailed data flows, integration patterns, technology stacks, and business architecture, refer to the individual L2 capability documents linked in [§6 Capability Detail Reference](#6-capability-detail-reference).

| Metric | Current-State | Future-State | Delta |
|--------|:---:|:---:|:---:|
| **Unique Systems** | 37 | 44 | +7 |
| **System Connections** | 43 | 54 | +11 |
| **Total Flow Hops** | 388 | 429 | +41 |
| **Capabilities Covered** | 184 | 184 | — |

<div class="page-footer"><span>Page 3</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 2 Capability Inventory

The following **184** capabilities are aggregated in this summary.
Click a capability ID to view its full TOGAF BDAT architecture document.

| # | Capability ID | Capability Name | L1 Process Group | Current Hops | Future Hops |
|:---:|:---:|---|---|:---:|:---:|
| 1 | [E2E-80](/towers/E2E/E2E-80-R2-Customer-Requests-Expedite/E2E-80/output/docs/systems-architecture/E2E-80-Architecture.html) | R2A Option 1  Customer Requests Expedite - Service Fee with Existing SO | E2E · E2E-80 R2 Customer Requests Expedite | 1 | 1 |
| 2 | [E2E-08](/towers/E2E/Forecast-to-Stock/E2E-08/output/docs/systems-architecture/E2E-08-Architecture.html) | E2E-08 | E2E · Forecast to Stock | 1 | 1 |
| 3 | [E2E-110](/towers/E2E/Forecast-to-Stock/E2E-110/output/docs/systems-architecture/E2E-110-Architecture.html) | IMR Flow | E2E · Forecast to Stock | 1 | 1 |
| 4 | [E2E-113](/towers/E2E/Forecast-to-Stock/E2E-113/output/docs/systems-architecture/E2E-113-Architecture.html) | R3 IMR Labs Process | E2E · Forecast to Stock | 1 | 1 |
| 5 | [E2E-117](/towers/E2E/Forecast-to-Stock/E2E-117/output/docs/systems-architecture/E2E-117-Architecture.html) | E2E-117 | E2E · Forecast to Stock | 1 | 1 |
| 6 | [E2E-118](/towers/E2E/Forecast-to-Stock/E2E-118/output/docs/systems-architecture/E2E-118-Architecture.html) | E2E-118 | E2E · Forecast to Stock | 1 | 1 |
| 7 | [E2E-122](/towers/E2E/Forecast-to-Stock/E2E-122/output/docs/systems-architecture/E2E-122-Architecture.html) | E2E-122 | E2E · Forecast to Stock | 1 | 1 |
| 8 | [E2E-45](/towers/E2E/Forecast-to-Stock/E2E-45/output/docs/systems-architecture/E2E-45-Architecture.html) | E2E-45 | E2E · Forecast to Stock | 1 | 1 |
| 9 | [E2E-67](/towers/E2E/Forecast-to-Stock/E2E-67/output/docs/systems-architecture/E2E-67-Architecture.html) | E2E-67 | E2E · Forecast to Stock | 1 | 1 |
| 10 | [E2E-68](/towers/E2E/Forecast-to-Stock/E2E-68/output/docs/systems-architecture/E2E-68-Architecture.html) | -Intel Foundry   NPI planning and execution processes | E2E · Forecast to Stock | 1 | 1 |
| 11 | [E2E-71](/towers/E2E/Forecast-to-Stock/E2E-71/output/docs/systems-architecture/E2E-71-Architecture.html) | E2E-71 | E2E · Forecast to Stock | 1 | 1 |
| 12 | [E2E-72](/towers/E2E/Forecast-to-Stock/E2E-72/output/docs/systems-architecture/E2E-72-Architecture.html) | IP | E2E · Forecast to Stock | 1 | 1 |
| 13 | [E2E-73](/towers/E2E/Forecast-to-Stock/E2E-73/output/docs/systems-architecture/E2E-73-Architecture.html) | R3 Hybrid Manufacturing process with external Wafer Procurement & Internal processing of | E2E · Forecast to Stock | 1 | 1 |
| 14 | [E2E-74](/towers/E2E/Forecast-to-Stock/E2E-74/output/docs/systems-architecture/E2E-74-Architecture.html) | R3 Internal manufacturing process for Finished Goods in Intel Foundry with Planning integrati | E2E · Forecast to Stock | 1 | 1 |
| 15 | [E2E-76](/towers/E2E/Forecast-to-Stock/E2E-76/output/docs/systems-architecture/E2E-76-Architecture.html) | Internal manufacturing process for Finished Goods in Intel Foundry with sales to External cus | E2E · Forecast to Stock | 1 | 1 |
| 16 | [E2E-84](/towers/E2E/Forecast-to-Stock/E2E-84/output/docs/systems-architecture/E2E-84-Architecture.html) | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) | E2E · Forecast to Stock | 1 | 1 |
| 17 | [E2E-94](/towers/E2E/Forecast-to-Stock/E2E-94/output/docs/systems-architecture/E2E-94-Architecture.html) | R3 Intel Foundry Maintenance process through spare parts (SWAP) | E2E · Forecast to Stock | 1 | 1 |
| 18 | [E2E-89](/towers/E2E/Master-Data/E2E-89/output/docs/systems-architecture/E2E-89-Architecture.html) | R3 Customer Master Data | E2E · Master Data | 1 | 1 |
| 19 | [E2E-90](/towers/E2E/Master-Data/E2E-90/output/docs/systems-architecture/E2E-90-Architecture.html) | R3 Material Master Data | E2E · Master Data | 1 | 1 |
| 20 | [E2E-91](/towers/E2E/Master-Data/E2E-91/output/docs/systems-architecture/E2E-91-Architecture.html) | R3 Bill of Material BOM Data | E2E · Master Data | 1 | 1 |
| 21 | [E2E-92](/towers/E2E/Master-Data/E2E-92/output/docs/systems-architecture/E2E-92-Architecture.html) | R3 Vendor Master Data | E2E · Master Data | 1 | 1 |
| 22 | [IF_Simplified_PO-SO_Model](/towers/E2E/Order-to-Cash/IF_Simplified_PO-SO_Model/output/docs/systems-architecture/IF_Simplified_PO-SO_Model-Architecture.html) | IF Simplified PO-SO Model | E2E · Order to Cash | 1 | 1 |
| 23 | [Order_to_Cash_IF](/towers/E2E/Order-to-Cash/Order_to_Cash_IF/output/docs/systems-architecture/Order_to_Cash_IF-Architecture.html) | Order to Cash (IF) | E2E · Order to Cash | 1 | 1 |
| 24 | [Order_to_Cash_IP](/towers/E2E/Order-to-Cash/Order_to_Cash_IP/output/docs/systems-architecture/Order_to_Cash_IP-Architecture.html) | Order to Cash (IP) | E2E · Order to Cash | 1 | 1 |
| 25 | [E2E-100](/towers/E2E/Procure-to-Pay/E2E-100/output/docs/systems-architecture/E2E-100-Architecture.html) | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box | E2E · Procure to Pay | 1 | 1 |
| 26 | [E2E-103](/towers/E2E/Procure-to-Pay/E2E-103/output/docs/systems-architecture/E2E-103-Architecture.html) | R3 Procurement of WIINGS Replacement Related Commodities | E2E · Procure to Pay | 1 | 1 |
| 27 | [E2E-107](/towers/E2E/Procure-to-Pay/E2E-107/output/docs/systems-architecture/E2E-107-Architecture.html) | R3 - Partner Owned Equipment Order | E2E · Procure to Pay | 1 | 1 |
| 28 | [E2E-112](/towers/E2E/Procure-to-Pay/E2E-112/output/docs/systems-architecture/E2E-112-Architecture.html) | R3 Raw Silicon Procurement | E2E · Procure to Pay | 1 | 1 |
| 29 | [E2E-114](/towers/E2E/Procure-to-Pay/E2E-114/output/docs/systems-architecture/E2E-114-Architecture.html) | R4 SIMS Harvest Process | E2E · Procure to Pay | 1 | 1 |
| 30 | [E2E-115](/towers/E2E/Procure-to-Pay/E2E-115/output/docs/systems-architecture/E2E-115-Architecture.html) | R3 Inter-company Asset Transfer Process | E2E · Procure to Pay | 1 | 1 |
| 31 | [E2E-116](/towers/E2E/Procure-to-Pay/E2E-116/output/docs/systems-architecture/E2E-116-Architecture.html) | R3 Wafer Reclaim Process | E2E · Procure to Pay | 1 | 1 |
| 32 | [E2E-119](/towers/E2E/Procure-to-Pay/E2E-119/output/docs/systems-architecture/E2E-119-Architecture.html) | R3 Shipping Rejects Inventory Movement | E2E · Procure to Pay | 1 | 1 |
| 33 | [E2E-121](/towers/E2E/Procure-to-Pay/E2E-121/output/docs/systems-architecture/E2E-121-Architecture.html) | R3 RM Bailed Inventory Movement (Straddle) | E2E · Procure to Pay | 1 | 1 |
| 34 | [E2E-123](/towers/E2E/Procure-to-Pay/E2E-123/output/docs/systems-architecture/E2E-123-Architecture.html) | TD Substrates Manufacturing Process | E2E · Procure to Pay | 1 | 1 |
| 35 | [E2E-40](/towers/E2E/Procure-to-Pay/E2E-40/output/docs/systems-architecture/E2E-40-Architecture.html) | R3 Sourcing Request-Project to Contracts for Direct-Capital on Ariba with Pricing Updates | E2E · Procure to Pay | 1 | 1 |
| 36 | [E2E-41](/towers/E2E/Procure-to-Pay/E2E-41/output/docs/systems-architecture/E2E-41-Architecture.html) | R3 Sourcing Request | E2E · Procure to Pay | 1 | 1 |
| 37 | [E2E-43](/towers/E2E/Procure-to-Pay/E2E-43/output/docs/systems-architecture/E2E-43-Architecture.html) | Process Procurement Card Invoice | E2E · Procure to Pay | 1 | 1 |
| 38 | [E2E-44](/towers/E2E/Procure-to-Pay/E2E-44/output/docs/systems-architecture/E2E-44-Architecture.html) | R3 - Intel Owned Consignment with Planning Integration | E2E · Procure to Pay | 1 | 1 |
| 39 | [E2E-46](/towers/E2E/Procure-to-Pay/E2E-46/output/docs/systems-architecture/E2E-46-Architecture.html) | R3 Direct procurement with Planning Integration-AT | E2E · Procure to Pay | 1 | 1 |
| 40 | [E2E-47](/towers/E2E/Procure-to-Pay/E2E-47/output/docs/systems-architecture/E2E-47-Architecture.html) | Purchase Requisition to Payments for Direct procurement with planning integration - Fab Mater | E2E · Procure to Pay | 1 | 1 |
| 41 | [E2E-49](/towers/E2E/Procure-to-Pay/E2E-49/output/docs/systems-architecture/E2E-49-Architecture.html) | R3 Purchase Requisition to Payments for procurement with financial planning and asset managem | E2E · Procure to Pay | 1 | 1 |
| 42 | [E2E-50](/towers/E2E/Procure-to-Pay/E2E-50/output/docs/systems-architecture/E2E-50-Architecture.html) | Purchase Requisition to Payments for Indirect - Construction (Small Construction IPCS, Mainte | E2E · Procure to Pay | 1 | 1 |
| 43 | [E2E-51](/towers/E2E/Procure-to-Pay/E2E-51/output/docs/systems-architecture/E2E-51-Architecture.html) | Purchase Requisition to Payments for Indirect Materials (Non-IPN and Non-Inventoried) ​ | E2E · Procure to Pay | 1 | 1 |
| 44 | [E2E-52](/towers/E2E/Procure-to-Pay/E2E-52/output/docs/systems-architecture/E2E-52-Architecture.html) | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement | E2E · Procure to Pay | 1 | 1 |
| 45 | [E2E-53](/towers/E2E/Procure-to-Pay/E2E-53/output/docs/systems-architecture/E2E-53-Architecture.html) | Purchase Requisition to Payments for Indirect procurement (simple material or services like H | E2E · Procure to Pay | 1 | 1 |
| 46 | [E2E-57](/towers/E2E/Procure-to-Pay/E2E-57/output/docs/systems-architecture/E2E-57-Architecture.html) | R3 Subcontracting with Planning integration- Foundry,OSAT,ODM | E2E · Procure to Pay | 1 | 1 |
| 47 | [E2E-59](/towers/E2E/Procure-to-Pay/E2E-59/output/docs/systems-architecture/E2E-59-Architecture.html) | R3 Rework Re-localization in Factory​ | E2E · Procure to Pay | 1 | 1 |
| 48 | [E2E-61](/towers/E2E/Procure-to-Pay/E2E-61/output/docs/systems-architecture/E2E-61-Architecture.html) | R3 Consignment Material - Vendor | E2E · Procure to Pay | 1 | 1 |
| 49 | [E2E-62](/towers/E2E/Procure-to-Pay/E2E-62/output/docs/systems-architecture/E2E-62-Architecture.html) | R3 Vendor Return for Direct Material | E2E · Procure to Pay | 1 | 1 |
| 50 | [E2E-70](/towers/E2E/Procure-to-Pay/E2E-70/output/docs/systems-architecture/E2E-70-Architecture.html) | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte | E2E · Procure to Pay | 1 | 1 |
| 51 | [E2E-88](/towers/E2E/Procure-to-Pay/E2E-88/output/docs/systems-architecture/E2E-88-Architecture.html) | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme | E2E · Procure to Pay | 1 | 1 |
| 52 | [E2E-96](/towers/E2E/Procure-to-Pay/E2E-96/output/docs/systems-architecture/E2E-96-Architecture.html) | R3 Straddle & R4 SIMS Design with Returns | E2E · Procure to Pay | 1 | 1 |
| 53 | [E2E-98](/towers/E2E/Procure-to-Pay/E2E-98/output/docs/systems-architecture/E2E-98-Architecture.html) | R3 Equipment Product Supporting Items (PSI) Procurement | E2E · Procure to Pay | 1 | 1 |
| 54 | [DC-010](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-010/output/docs/systems-architecture/DC-010-Architecture.html) | Perform Transaction Processing | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 55 | [DC-020](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-020/output/docs/systems-architecture/DC-020-Architecture.html) | Manage the General Ledger | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 56 | [DC-030](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-030/output/docs/systems-architecture/DC-030-Architecture.html) | Perform Closing | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 57 | [DC-040](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-040/output/docs/systems-architecture/DC-040-Architecture.html) | Perform Fixed Asset Accounting | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 58 | [DC-050](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-050/output/docs/systems-architecture/DC-050-Architecture.html) | Project Accounting | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 59 | [DC-060](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-060/output/docs/systems-architecture/DC-060-Architecture.html) | Manage Taxes | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 60 | [DC-100](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-100/output/docs/systems-architecture/DC-100-Architecture.html) | Revenue Recognition | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 61 | [DC-110](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-110/output/docs/systems-architecture/DC-110-Architecture.html) | Manage Intercompany | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 62 | [DC-120](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-120/output/docs/systems-architecture/DC-120-Architecture.html) | Maintenance & Management Accounting | FPR · DC Manage Accounting and Control Data | 2 | 2 |
| 63 | [DS-010](/towers/FPR/DS-Provide-Decision-Support/DS-010/output/docs/systems-architecture/DS-010-Architecture.html) | Perform Overhead Accounting and Allocation | FPR · DS Provide Decision Support | 2 | 2 |
| 64 | [DS-020](/towers/FPR/DS-Provide-Decision-Support/DS-020/output/docs/systems-architecture/DS-020-Architecture.html) | Perform Product Costing and Inventory Valuation | FPR · DS Provide Decision Support | 75 | 116 |
| 65 | [DS-030](/towers/FPR/DS-Provide-Decision-Support/DS-030/output/docs/systems-architecture/DS-030-Architecture.html) | Perform Customer and Product Profitability Analysis | FPR · DS Provide Decision Support | 2 | 2 |
| 66 | [MB-060](/towers/FPR/MB-Plan-and-Manage-Business/MB-060/output/docs/systems-architecture/MB-060-Architecture.html) | Plan the Business | FPR · MB Plan and Manage Business | 2 | 2 |
| 67 | [MB-070](/towers/FPR/MB-Plan-and-Manage-Business/MB-070/output/docs/systems-architecture/MB-070-Architecture.html) | Prepare Budgets | FPR · MB Plan and Manage Business | 2 | 2 |
| 68 | [MR-010](/towers/FPR/MR-Manage-Capital-and-Risk/MR-010/output/docs/systems-architecture/MR-010-Architecture.html) | Manage Liquidity | FPR · MR Manage Capital and Risk | 2 | 2 |
| 69 | [MR-020](/towers/FPR/MR-Manage-Capital-and-Risk/MR-020/output/docs/systems-architecture/MR-020-Architecture.html) | Manage Capital Structure | FPR · MR Manage Capital and Risk | 2 | 2 |
| 70 | [MR-030](/towers/FPR/MR-Manage-Capital-and-Risk/MR-030/output/docs/systems-architecture/MR-030-Architecture.html) | Manage Financial Risk | FPR · MR Manage Capital and Risk | 2 | 2 |
| 71 | [MR-070](/towers/FPR/MR-Manage-Capital-and-Risk/MR-070/output/docs/systems-architecture/MR-070-Architecture.html) | In-House Banking | FPR · MR Manage Capital and Risk | 2 | 2 |
| 72 | [OR-140](/towers/FPR/OR-Receivables-Management/OR-140/output/docs/systems-architecture/OR-140-Architecture.html) | Process Receipts | FPR · OR Receivables Management | 2 | 2 |
| 73 | [L-040](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-040/output/docs/systems-architecture/L-040-Architecture.html) | Receive and Put-away Product - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 2 | 2 |
| 74 | [L-060](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-060/output/docs/systems-architecture/L-060-Architecture.html) | Manage Storage & Internal Movement of Inventory - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 2 | 2 |
| 75 | [L-110](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-110/output/docs/systems-architecture/L-110-Architecture.html) | Manage Lots Batches - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 2 | 2 |
| 76 | [L-120](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-120/output/docs/systems-architecture/L-120-Architecture.html) | Manage Line Replenishment - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | 2 | 2 |
| 77 | [LI-120](/towers/FTS-IF/LI-Logistics-Management-Inbound---FTS-(IF)/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) | Receive Materials and Services - FTS (IF) | FTS-IF · LI Logistics Management Inbound - FTS (IF) | 2 | 2 |
| 78 | [LO-160](/towers/FTS-IF/LO-Logistics-Management-Outbound---FTS-(IF)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders- FTS (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 2 | 2 |
| 79 | [LO-170](/towers/FTS-IF/LO-Logistics-Management-Outbound---FTS-(IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Order - FTS  (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 2 | 2 |
| 80 | [LO-180](/towers/FTS-IF/LO-Logistics-Management-Outbound---FTS-(IF)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - FTS (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 2 | 2 |
| 81 | [LO-190](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship | FTS-IF · LO Logistics Management Outbound - FTS (IF) | 2 | 2 |
| 82 | [M-080](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-080/output/docs/systems-architecture/M-080-Architecture.html) | Perform Materials Requirement Planning (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 2 | 2 |
| 83 | [M-090](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-090/output/docs/systems-architecture/M-090-Architecture.html) | Schedule Production (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 2 | 2 |
| 84 | [M-100](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-100/output/docs/systems-architecture/M-100-Architecture.html) | Execute Production (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 2 | 2 |
| 85 | [M-170](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-170/output/docs/systems-architecture/M-170-Architecture.html) | Control and Report Production Operations (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | 2 | 2 |
| 86 | [PE-020](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-020/output/docs/systems-architecture/PE-020-Architecture.html) | Identify Maintenance Structure | FTS-IF · PE Manage Plant, Equipment and Facilities | 2 | 2 |
| 87 | [PE-040](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-040/output/docs/systems-architecture/PE-040-Architecture.html) | Monitor | FTS-IF · PE Manage Plant, Equipment and Facilities | 2 | 2 |
| 88 | [PE-050](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-050/output/docs/systems-architecture/PE-050-Architecture.html) | Maintain Work Order Historical Documentation | FTS-IF · PE Manage Plant, Equipment and Facilities | 2 | 2 |
| 89 | [PE-060](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-060/output/docs/systems-architecture/PE-060-Architecture.html) | Maintain and Manage Master Maintenance Records | FTS-IF · PE Manage Plant, Equipment and Facilities | 2 | 2 |
| 90 | [PE-070](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-070/output/docs/systems-architecture/PE-070-Architecture.html) | Identify and Plan Plant Maintenance | FTS-IF · PE Manage Plant, Equipment and Facilities | 2 | 2 |
| 91 | [PE-090](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-090/output/docs/systems-architecture/PE-090-Architecture.html) | Execute Plant Maintenance | FTS-IF · PE Manage Plant, Equipment and Facilities | 2 | 2 |
| 92 | [PLB-020](/towers/FTS-IF/PLB-Supply-Chain-Planning-(IF)/PLB-020/output/docs/systems-architecture/PLB-020-Architecture.html) | Supply Planning & Management (IF) | FTS-IF · PLB Supply Chain Planning (IF) | 2 | 2 |
| 93 | [Q-140](/towers/FTS-IF/Q-Quality-Management-(IF)/Q-140/output/docs/systems-architecture/Q-140-Architecture.html) | Manage Product Disposition (IF) | FTS-IF · Q Quality Management (IF) | 2 | 2 |
| 94 | [L-060](/towers/FTS-IP/L-Logistics-and-Inventory-Management---FTS-(IP)/L-060/output/docs/systems-architecture/L-060-Architecture.html) | Manage Storage and Internal Movement of Inventory - FTS (IP) | FTS-IP · L Logistics and Inventory Management - FTS (IP) | 2 | 2 |
| 95 | [LI-120](/towers/FTS-IP/LI-Logistics-Management-Inbound---FTS-(IP)/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) | Receive Materials and Services - FTS (IP) | FTS-IP · LI Logistics Management Inbound - FTS (IP) | 2 | 2 |
| 96 | [LO-160](/towers/FTS-IP/LO-Logistics-Management-Outbound---FTS-(IP)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 2 | 2 |
| 97 | [LO-170](/towers/FTS-IP/LO-Logistics-Management-Outbound---FTS-(IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Orders - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 2 | 2 |
| 98 | [LO-180](/towers/FTS-IP/L-Logistics-and-Inventory-Management---FTS-(IP)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 2 | 2 |
| 99 | [LO-190](/towers/FTS-IP/LO-Logistics-Management-Outbound---FTS-(IP)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship | FTS-IP · LO Logistics Management Outbound - FTS (IP) | 2 | 2 |
| 100 | [M-080](/towers/FTS-IP/M-Mfg.-Schedule-and-Execution-(IP)/M-080/output/docs/systems-architecture/M-080-Architecture.html) | Perform Materials Requirement Planning (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | 2 | 2 |
| 101 | [M-090](/towers/FTS-IP/M-Mfg.-Schedule-and-Execution-(IP)/M-090/output/docs/systems-architecture/M-090-Architecture.html) | Schedule Production (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | 2 | 2 |
| 102 | [M-100](/towers/FTS-IP/M-Mfg.-Schedule-and-Execution-(IP)/M-100/output/docs/systems-architecture/M-100-Architecture.html) | Execute Production (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | 2 | 2 |
| 103 | [PLB-020](/towers/FTS-IP/PLB-Supply-Chain-Planning-(IP)/PLB-020/output/docs/systems-architecture/PLB-020-Architecture.html) | Supply Planning & Management (IP) | FTS-IP · PLB Supply Chain Planning (IP) | 2 | 2 |
| 104 | [PLB-050](/towers/FTS-IP/PLB-Supply-Chain-Planning-(IP)/PLB-050/output/docs/systems-architecture/PLB-050-Architecture.html) | Responsive Demand and Supply Matching (RDSM) (IP) | FTS-IP · PLB Supply Chain Planning (IP) | 2 | 2 |
| 105 | [Q-140](/towers/FTS-IP/Q-Quality-Management-(IP)/Q-140/output/docs/systems-architecture/Q-140-Architecture.html) | Manage Product Disposition (IP) | FTS-IP · Q Quality Management (IP) | 2 | 2 |
| 106 | [MDM-020](/towers/MDM/MDM-Manage-Master-Data/MDM-020/output/docs/systems-architecture/MDM-020-Architecture.html) | Create and Maintain Vendors | MDM · MDM-Manage Master Data | 2 | 2 |
| 107 | [MDM-130](/towers/MDM/MDM-Manage-Master-Data/MDM-130/output/docs/systems-architecture/MDM-130-Architecture.html) | Create and Maintain Customers | MDM · MDM-Manage Master Data | 2 | 2 |
| 108 | [MDM-140](/towers/MDM/MDM-Manage-Master-Data/MDM-140/output/docs/systems-architecture/MDM-140-Architecture.html) | Create and Maintain Reference Data | MDM · MDM-Manage Master Data | 2 | 2 |
| 109 | [MDM-150](/towers/MDM/MDM-Manage-Master-Data/MDM-150/output/docs/systems-architecture/MDM-150-Architecture.html) | Maintain Product Related Data | MDM · MDM-Manage Master Data | 2 | 2 |
| 110 | [BR-130](/towers/OTC-IF/BR-Billing-and-Rebates-(IF)/BR-130/output/docs/systems-architecture/BR-130-Architecture.html) | Billing Revenue (IF) | OTC-IF · BR-Billing and Rebates (IF) | 2 | 2 |
| 111 | [CM-050](/towers/OTC-IF/CM-Credit-and-Collections-Management-(IF)/CM-050/output/docs/systems-architecture/CM-050-Architecture.html) | Manage Customer Credit Exposure (IF) | OTC-IF · CM-Credit and Collections Management (IF) | 2 | 2 |
| 112 | [CM-060](/towers/OTC-IF/CM-Credit-and-Collections-Management-(IF)/CM-060/output/docs/systems-architecture/CM-060-Architecture.html) | Manage Collections (IF) | OTC-IF · CM-Credit and Collections Management (IF) | 2 | 2 |
| 113 | [GT-010](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-010/output/docs/systems-architecture/GT-010-Architecture.html) | Manage Global Trade Master Data (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 114 | [GT-020](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-020/output/docs/systems-architecture/GT-020-Architecture.html) | Product Classification (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 115 | [GT-030](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-030/output/docs/systems-architecture/GT-030-Architecture.html) | Compliance Screening (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 116 | [GT-040](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-040/output/docs/systems-architecture/GT-040-Architecture.html) | Manage Licenses (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 117 | [GT-050](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-050/output/docs/systems-architecture/GT-050-Architecture.html) | Customs declaration creation Export (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 118 | [GT-070](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-070/output/docs/systems-architecture/GT-070-Architecture.html) | Customs Declaration Completion Export | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 119 | [GT-080](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-080/output/docs/systems-architecture/GT-080-Architecture.html) | Customs Declaration Communication - Self Filing (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 120 | [GT-110](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-110/output/docs/systems-architecture/GT-110-Architecture.html) | Monitor completed declaration (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 121 | [GT-130](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-130/output/docs/systems-architecture/GT-130-Architecture.html) | Intrastat Filing (S4) (IF) | OTC-IF · GT Global Trade (IF) | 2 | 2 |
| 122 | [LO-160](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 2 | 2 |
| 123 | [LO-170](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 2 | 2 |
| 124 | [LO-180](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 2 | 2 |
| 125 | [LO-190](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship Deliver Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | 2 | 2 |
| 126 | [O-020](/towers/OTC-IF/O-Order-Management-(IF)/O-020/output/docs/systems-architecture/O-020-Architecture.html) | Capture Orders (IF) | OTC-IF · O-Order Management (IF) | 2 | 2 |
| 127 | [O-030](/towers/OTC-IF/O-Order-Management-(IF)/O-030/output/docs/systems-architecture/O-030-Architecture.html) | Process Orders (IF) | OTC-IF · O-Order Management (IF) | 2 | 2 |
| 128 | [O-040](/towers/OTC-IF/O-Order-Management-(IF)/O-040/output/docs/systems-architecture/O-040-Architecture.html) | Calculate Order Price (IF) | OTC-IF · O-Order Management (IF) | 2 | 2 |
| 129 | [O-060](/towers/OTC-IF/O-Order-Management-(IF)/O-060/output/docs/systems-architecture/O-060-Architecture.html) | Manage and Track Orders (IF) | OTC-IF · O-Order Management (IF) | 2 | 2 |
| 130 | [O-070](/towers/OTC-IF/O-Order-Management-(IF)/O-070/output/docs/systems-architecture/O-070-Architecture.html) | Manage Backorders (IF) | OTC-IF · O-Order Management (IF) | 2 | 2 |
| 131 | [R-190](/towers/OTC-IF/R-Returns-(IF)/R-190/output/docs/systems-architecture/R-190-Architecture.html) | Manage Returns and Exchanges (IF) | OTC-IF · R-Returns (IF) | 2 | 2 |
| 132 | [R-200](/towers/OTC-IF/R-Returns-(IF)/R-200/output/docs/systems-architecture/R-200-Architecture.html) | Return - Receive Materials and Services (IF) | OTC-IF · R-Returns (IF) | 2 | 2 |
| 133 | [R-210](/towers/OTC-IF/R-Returns-(IF)/R-210/output/docs/systems-architecture/R-210-Architecture.html) | Returns - Determine Discrepant Material Disposition (IF) | OTC-IF · R-Returns (IF) | 2 | 2 |
| 134 | [R-220](/towers/OTC-IF/R-Returns-(IF)/R-220/output/docs/systems-architecture/R-220-Architecture.html) | Returns - Manage In-bound Transportation (IF) | OTC-IF · R-Returns (IF) | 2 | 2 |
| 135 | [BR-130](/towers/OTC-IP/BR-Billing-and-Rebates-(IP)/BR-130/output/docs/systems-architecture/BR-130-Architecture.html) | Billing Revenue (IP) | OTC-IP · BR-Billing and Rebates (IP) | 2 | 2 |
| 136 | [BR-160](/towers/OTC-IP/BR-Billing-and-Rebates-(IP)/BR-160/output/docs/systems-architecture/BR-160-Architecture.html) | Manage Rebates (IP) | OTC-IP · BR-Billing and Rebates (IP) | 2 | 2 |
| 137 | [BR-170](/towers/OTC-IP/BR-Billing-and-Rebates-(IP)/BR-170/output/docs/systems-architecture/BR-170-Architecture.html) | Manage Chargebacks (IP) | OTC-IP · BR-Billing and Rebates (IP) | 2 | 2 |
| 138 | [CM-050](/towers/OTC-IP/CM-Credit-and-Collections-Management-(IP)/CM-050/output/docs/systems-architecture/CM-050-Architecture.html) | Manage Customer Credit Exposure (IP) | OTC-IP · CM-Credit and Collections Management (IP) | 2 | 2 |
| 139 | [CM-060](/towers/OTC-IP/CM-Credit-and-Collections-Management-(IP)/CM-060/output/docs/systems-architecture/CM-060-Architecture.html) | Manage Collections (IP) | OTC-IP · CM-Credit and Collections Management (IP) | 2 | 2 |
| 140 | [GT-010](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-010/output/docs/systems-architecture/GT-010-Architecture.html) | Manage Global Trade Master Data (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 141 | [GT-020](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-020/output/docs/systems-architecture/GT-020-Architecture.html) | Product Classification (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 142 | [GT-030](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-030/output/docs/systems-architecture/GT-030-Architecture.html) | Compliance Screening (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 143 | [GT-040](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-040/output/docs/systems-architecture/GT-040-Architecture.html) | Manage Licenses (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 144 | [GT-050](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-050/output/docs/systems-architecture/GT-050-Architecture.html) | Customs Declaration Creation Export (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 145 | [GT-060](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-060/output/docs/systems-architecture/GT-060-Architecture.html) | Customs declaration creation Import (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 146 | [GT-070](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-070/output/docs/systems-architecture/GT-070-Architecture.html) | Customs Declaration Completion Export | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 147 | [GT-080](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-080/output/docs/systems-architecture/GT-080-Architecture.html) | Customs Declaration Communication - Self Filing (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 148 | [GT-090](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-090/output/docs/systems-architecture/GT-090-Architecture.html) | Customs declaration communication - broker filing (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 149 | [GT-110](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-110/output/docs/systems-architecture/GT-110-Architecture.html) | Monitor Completed Declaration (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 150 | [GT-130](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-130/output/docs/systems-architecture/GT-130-Architecture.html) | Intrastat Filing (S4) (IP) | OTC-IP · GT-Global Trade (IP) | 2 | 2 |
| 151 | [LO-160](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) | Pick Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 2 | 2 |
| 152 | [LO-170](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) | Pack Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 2 | 2 |
| 153 | [LO-180](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) | Manage Outbound Transportation - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 2 | 2 |
| 154 | [LO-190](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) | Ship Deliver Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | 2 | 2 |
| 155 | [O-020](/towers/OTC-IP/O-Order-Management-(IP)/O-020/output/docs/systems-architecture/O-020-Architecture.html) | Capture Orders (IP) | OTC-IP · O-Order Management (IP) | 2 | 2 |
| 156 | [O-030](/towers/OTC-IP/O-Order-Management-(IP)/O-030/output/docs/systems-architecture/O-030-Architecture.html) | Process Orders (IP) | OTC-IP · O-Order Management (IP) | 2 | 2 |
| 157 | [O-040](/towers/OTC-IP/O-Order-Management-(IP)/O-040/output/docs/systems-architecture/O-040-Architecture.html) | Calculate Order Price (IP) | OTC-IP · O-Order Management (IP) | 2 | 2 |
| 158 | [O-060](/towers/OTC-IP/O-Order-Management-(IP)/O-060/output/docs/systems-architecture/O-060-Architecture.html) | Manage and Track Orders (IP) | OTC-IP · O-Order Management (IP) | 2 | 2 |
| 159 | [O-070](/towers/OTC-IP/O-Order-Management-(IP)/O-070/output/docs/systems-architecture/O-070-Architecture.html) | Manage Backorders (IP) | OTC-IP · O-Order Management (IP) | 2 | 2 |
| 160 | [R-190](/towers/OTC-IP/R-Returns-(IP)/R-190/output/docs/systems-architecture/R-190-Architecture.html) | Manage Returns and Exchanges (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 161 | [R-200](/towers/OTC-IP/R-Returns-(IP)/R-200/output/docs/systems-architecture/R-200-Architecture.html) | Return - Receive Materials and Services (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 162 | [R-220](/towers/OTC-IP/R-Returns-(IP)/R-220/output/docs/systems-architecture/R-220-Architecture.html) | Returns - Manage In-bound Transportation (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 163 | [R-230](/towers/OTC-IP/R-Returns-(IP)/R-230/output/docs/systems-architecture/R-230-Architecture.html) | Returns - Manage Storage & Internal Movement of Inventory (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 164 | [R-240](/towers/OTC-IP/R-Returns-(IP)/R-240/output/docs/systems-architecture/R-240-Architecture.html) | Returns - Manage Storage & Internal Movement of Inventory (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 165 | [R-250](/towers/OTC-IP/R-Returns-(IP)/R-250/output/docs/systems-architecture/R-250-Architecture.html) | Returns - Receive and Put-away Product (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 166 | [R-260](/towers/OTC-IP/R-Returns-(IP)/R-260/output/docs/systems-architecture/R-260-Architecture.html) | Returns - Pick Orders (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 167 | [R-270](/towers/OTC-IP/R-Returns-(IP)/R-270/output/docs/systems-architecture/R-270-Architecture.html) | Returns - Pack Orders (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 168 | [R-280](/towers/OTC-IP/R-Returns-(IP)/R-280/output/docs/systems-architecture/R-280-Architecture.html) | Returns - Ship Orders (IP) | OTC-IP · R-Returns (IP) | 2 | 2 |
| 169 | [R-290](/towers/OTC-IP/R-Returns-(IP)/R-290/output/docs/systems-architecture/R-290-Architecture.html) | Returns - Manage Lots | OTC-IP · R-Returns (IP) | 2 | 2 |
| 170 | [L-040](/towers/PTP/L-Logistics-and-Inventory-Management---PTP/L-040/output/docs/systems-architecture/L-040-Architecture.html) | Receive and Put-away Product - PTP | PTP · L Logistics and Inventory Management - PTP | 2 | 2 |
| 171 | [L-060](/towers/PTP/L-Logistics-and-Inventory-Management---PTP/L-060/output/docs/systems-architecture/L-060-Architecture.html) | Manage Storage and Internal Movement of Inventory - PTP | PTP · L Logistics and Inventory Management - PTP | 2 | 2 |
| 172 | [L-110](/towers/PTP/L-Logistics-and-Inventory-Management---PTP/L-110/output/docs/systems-architecture/L-110-Architecture.html) | Manage Lots Batches - PTP | PTP · L Logistics and Inventory Management - PTP | 2 | 2 |
| 173 | [LI-030](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-030/output/docs/systems-architecture/LI-030-Architecture.html) | Manage In-bound Transportation - PTP | PTP · LI Logistics Management Inbound - PTP | 2 | 2 |
| 174 | [LI-100](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-100/output/docs/systems-architecture/LI-100-Architecture.html) | Manage Supplier Consignment Stock | PTP · LI Logistics Management Inbound - PTP | 2 | 2 |
| 175 | [LI-120](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) | Receive Materials and Services - PTP | PTP · LI Logistics Management Inbound - PTP | 2 | 2 |
| 176 | [LI-200](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-200/output/docs/systems-architecture/LI-200-Architecture.html) | Determine Discrepant Material Disposition | PTP · LI Logistics Management Inbound - PTP | 2 | 2 |
| 177 | [PM-040](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-040/output/docs/systems-architecture/PM-040-Architecture.html) | Maintain Supplier Certification and Monitor Performance | PTP · PM-Procure Materials and Services (Direct and Indirect) | 2 | 2 |
| 178 | [PM-050](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-050/output/docs/systems-architecture/PM-050-Architecture.html) | Manage Quotation | PTP · PM-Procure Materials and Services (Direct and Indirect) | 2 | 2 |
| 179 | [PM-070](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-070/output/docs/systems-architecture/PM-070-Architecture.html) | Create and Maintain Purchase Requisitions | PTP · PM-Procure Materials and Services (Direct and Indirect) | 2 | 2 |
| 180 | [PM-080](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-080/output/docs/systems-architecture/PM-080-Architecture.html) | Purchase Materials and Services | PTP · PM-Procure Materials and Services (Direct and Indirect) | 2 | 2 |
| 181 | [PM-090](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-090/output/docs/systems-architecture/PM-090-Architecture.html) | Manage Contracts | PTP · PM-Procure Materials and Services (Direct and Indirect) | 2 | 2 |
| 182 | [PM-110](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-110/output/docs/systems-architecture/PM-110-Architecture.html) | Procure Subcontracting | PTP · PM-Procure Materials and Services (Direct and Indirect) | 2 | 2 |
| 183 | [PM-150](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-150/output/docs/systems-architecture/PM-150-Architecture.html) | Enable Payment | PTP · PM-Procure Materials and Services (Direct and Indirect) | 2 | 2 |
| 184 | [QI-130](/towers/PTP/QI-Quality-Management-(Incoming)/QI-130/output/docs/systems-architecture/QI-130-Architecture.html) | Perform Incoming Quality Assurance | PTP · QI-Quality Management (Incoming) | 2 | 2 |

<div class="page-footer"><span>Page 4</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 3 Current-State Architecture

Aggregated current-state: **37** systems, **43** connections, **388** flow hops.


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
        SCA_ADLS["📦 ADLS"]
        SCA_APIGEE["📦 APIGEE"]
        SCA_BOBJ["📦 BOBJ"]
        SCA_BPC["📦 BPC"]
        SCA_CFIN_S_4["📦 CFIN S/4"]
        SCA_CIBR["📦 CIBR"]
        SCA_COMPASS["📦 COMPASS"]
        SCA_Corp___IP_S_4["📦 Corp / IP S/4"]
        SCA_DataBricks["📦 DataBricks"]
        SCA_EATS["📦 EATS"]
        SCA_ECC["📦 ECC"]
        SCA_EDW["📦 EDW"]
        SCA_FCA["📦 FCA"]
        SCA_Finance_HANA["📦 Finance HANA"]
        SCA_ICOST["📦 ICOST"]
        SCA_IF_S_4["📦 IF S/4"]
        SCA_Legacy_MDG["📦 Legacy MDG"]
        SCA_MARS["📦 MARS"]
        SCA_MES_300["📦 MES 300"]
        SCA_MyDeals["📦 MyDeals"]
        SCA_OneMPS["📦 OneMPS"]
        SCA_PEGA["📦 PEGA"]
        SCA_SAP_ECC["📦 SAP ECC"]
        SCA_SAP_IBP["📦 SAP IBP"]
        SCA_SAP_PO["📦 SAP PO"]
        SCA_SDRA_Demand["📦 SDRA Demand"]
        SCA_SPAN["📦 SPAN"]
        SCA_SPEED_LEGACY["📦 SPEED-LEGACY"]
        SCA_SideCar["📦 SideCar"]
        SCA_SnOP["📦 SnOP"]
        SCA_SnowFlake["📦 SnowFlake"]
        SCA_Wafer_Starts["📦 Wafer Starts"]
        SCA_WorkStream["📦 WorkStream"]
        SCA_Workstream["📦 Workstream"]
        SCA_XEUS["📦 XEUS"]
        SCA_e_g__MES_300["📦 e.g. MES 300"]
        SCA_e_g__XEUS["📦 e.g. XEUS"]
    end

    SCA_ADLS -->|"Autoloader"| SCA_DataBricks
    SCA_APIGEE -->|"APIGEE"| SCA_PEGA
    SCA_BPC -->|"Denodo"| SCA_ICOST
    SCA_CIBR -->|"Direct"| SCA_ICOST
    SCA_CIBR -->|"Direct"| SCA_SAP_ECC
    SCA_CIBR -->|"SAP PO"| SCA_SAP_PO
    SCA_CIBR -->|"Direct"| SCA_SPAN
    SCA_COMPASS -->|"Denodo"| SCA_ICOST
    SCA_Corp___IP_S_4 -->|"SLT"| SCA_SideCar
    SCA_DataBricks -->|"Spark Snowflake Connector"| SCA_SnowFlake
    SCA_EATS -->|"Direct"| SCA_ICOST
    SCA_ECC -->|"Direct"| SCA_EDW
    SCA_EDW -->|"Direct"| SCA_CIBR
    SCA_EDW -->|"Direct"| SCA_ICOST
    SCA_FCA -->|"Direct"| SCA_ICOST
    SCA_Finance_HANA -->|"APIGEE"| SCA_APIGEE
    SCA_Finance_HANA -->|"Direct"| SCA_BOBJ
    SCA_Finance_HANA -->|"SAP PO"| SCA_SAP_PO
    SCA_ICOST -->|"Manual"| SCA_CFIN_S_4
    SCA_IF_S_4 -->|"SLT"| SCA_SideCar
    SCA_Legacy_MDG -->|"MDG"| SCA_SAP_ECC
    SCA_MARS -->|"Direct"| SCA_CIBR
    SCA_MARS -->|"Direct"| SCA_ICOST
    SCA_MES_300 -->|"Direct"| SCA_XEUS
    SCA_MyDeals -->|"Denodo"| SCA_ICOST
    SCA_OneMPS -->|"Denodo"| SCA_ICOST
    SCA_SAP_ECC -->|"Direct / ETL"| SCA_EDW
    SCA_SAP_ECC -->|"SLT"| SCA_Finance_HANA
    SCA_SAP_ECC -->|"SLT"| SCA_SideCar
    SCA_SAP_IBP -->|"Direct"| SCA_ADLS
    SCA_SAP_PO -->|"SAP PO"| SCA_SAP_ECC
    SCA_SDRA_Demand -->|"Denodo"| SCA_ICOST
    SCA_SPAN -->|"Denodo"| SCA_ICOST
    SCA_SPEED_LEGACY -->|"Direct"| SCA_EDW
    SCA_SPEED_LEGACY -->|"SAP PO"| SCA_SAP_PO
    SCA_SideCar -->|"CIF"| SCA_ADLS
    SCA_SnOP -->|"Denodo"| SCA_ICOST
    SCA_Wafer_Starts -->|"Denodo"| SCA_ICOST
    SCA_WorkStream -->|"Direct"| SCA_MARS
    SCA_Workstream -->|"Direct"| SCA_MARS
    SCA_XEUS -->|"Direct"| SCA_CIBR
    SCA_XEUS -->|"Direct"| SCA_ICOST
    SCA_e_g__MES_300 -->|"e.g. Direct / API / File"| SCA_e_g__XEUS

    class SCA_ADLS app
    class SCA_APIGEE app
    class SCA_BOBJ app
    class SCA_BPC app
    class SCA_CFIN_S_4 app
    class SCA_CIBR app
    class SCA_COMPASS app
    class SCA_Corp___IP_S_4 app
    class SCA_DataBricks app
    class SCA_EATS app
    class SCA_ECC app
    class SCA_EDW app
    class SCA_FCA app
    class SCA_Finance_HANA app
    class SCA_ICOST app
    class SCA_IF_S_4 app
    class SCA_Legacy_MDG app
    class SCA_MARS app
    class SCA_MES_300 app
    class SCA_MyDeals app
    class SCA_OneMPS app
    class SCA_PEGA app
    class SCA_SAP_ECC app
    class SCA_SAP_IBP app
    class SCA_SAP_PO app
    class SCA_SDRA_Demand app
    class SCA_SPAN app
    class SCA_SPEED_LEGACY app
    class SCA_SideCar app
    class SCA_SnOP app
    class SCA_SnowFlake app
    class SCA_Wafer_Starts app
    class SCA_WorkStream app
    class SCA_Workstream app
    class SCA_XEUS app
    class SCA_e_g__MES_300 app
    class SCA_e_g__XEUS app
    style BL fill:#FFFDE7,stroke:#F9A825,stroke-width:2px
    style AL fill:#E3F2FD,stroke:#0078D4,stroke-width:2px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqVWF1vo0YU_SsjVvvUJIvx5_qhEp-pKztGIVVaNRWaNZMEBYMFWKm72f_eGRgwcC8Jy0Mkn3PuZbjcuWfCd2WXBExZKk8pPTyTO-MhJvz6_JlcXhI93T2HG5ozMr7SyC9E_--YMpLlp4iRXUSzjGVcVkYUvy32SL4dszBmWUaK6zGMouUnh1_G-CLL0-SF8Z9f9YU2lT8vX8Mgf15qh38vdkmUpMtPqqp2ctLDgZyvMqdp2lPHqXOq6nxhTd7JOdZnZidtQHPaTWsYlu0YddrRdDY11XbaUSOtNZnro4oOaPZM05SelmRKpp2b7cMgiNgr5RVs1MVWDa2-mT2bjlS19xkMZzxTu8_AkgiUxnFMyzqnNWfaQlv0p52PzFE3bUZp1k1rjwzbntdp58bI0bXetBN9NFl00-6i5Bj8fMW1bsU7aZP4kLJ9pz8W9sz8WqfV7Lk17l_tyJjaGm-7MnF2_FbuB33994PycAwW44D_3bEZ0Q-HKNzRPExisqYnlpKHo6aOJsQ7ZTnbZ2QV54wHC8GD8k-ZT1xBmLJdGXZ7Rj1T93Vr7YHbcKwVXgjd1bVtA2mBArGxNX7vSgUGha4JdK4JZKazuvE9f9LVCpx4XyYwYGXcAjHHoHC7cXUPlEDCUJ6kB9_3Vy66Gk6SL2Tlokuy-IY30nD3knXjzgwIsvU7sDaBQaEJCskhKLPugcy6BzLH1LsyDkFZGNN4x_zf9BuoLzkiOBC4MrfeXTeiAKHUwUq9ctAar9kT3Z38jXXdDSgZwhkQtNFvQY0FBoW2549VFWhtj3AYyk8WoxF42xIG8m3MNi5YSIkCsWtfg4oLDAg93cV6g8Nofwj5ynAxOYdRubvF1O4Wiq1bvgvYnsYBiOAUKSkY5uo3QM8xRGjblr_mVTD_ggGcuyw5GBgGzKQpiClhKI-3sEAcQ4TJqxPRFwbVkgAh9_SRpb6X0zQHjVNwpORgYJK-eHnK6B6E1QwalPUGZXjQn_YfoEsFBoTMf_L79gy7errq3ThFIHabIqp1L8YbRvpm5Wb8VPjr24OiH3PurjRg_AW-dQZwI6DwrypEmtlbvcXOQu5KUmWxOAmSSlUOrbjpO5Wu8Nyf1cn9iiqrffXW2HtDUorNEncMb9DDNM2uWsP6rs4r90cMHa4SH2j6UnT7o-h2bpBxzBeW1K_kvBHipuMNqSAvEioTdhY37A4VFUeBD1WdO3IHHCRrmCLaWPLXewHtGxQnp_fk7zdGsT6p3ND4SKO6DPJY1dA6A9_12WmrzMJZe3pYuOmA99Ar61RYzhRUWkyHuGPBQ5q9NNohSvl4rdvzY599t0Z7sC1v1LT5IgfIwSuQXo2WoTjCx22b7m2W1rtquPSgYvDhMkx3NueP9y2ifr_HZXGk1lw5PYXgNj1ktU0bHqSvPRZ9tuI0GUPXHSAW_Txg6_TKOgtterLUF6ZadzEfTvyvE0asylC7cWW0xX--Z7vl30cAXroqwohRhuLcXhG4GlAoJ_wOw6XBYVTL0BBBw8EQtrAmDDfRxQtbQWBhIxjcHOsIX05xjHD6nqYxoxG2mLYYLrsDo-Q4RSg5PhFGnKMwvBp0PZSYbD0UH2UY0xhcGC0GFYo3Rg3Gy8mCUWKaoLg81WBka7Rg_HmU9LBZL1tMAQRv7fo-vh1cfmg11uePqFbj81vPR9RmqF6F2mNHc6yPvpUqF8qepXsaBsryu5I_s734MBywR3qMcuXHhUL5ed47xTtlmadHdqEcD_wLKrNCyr937Uvwx_9jP6eo" title="View full diagram">&#128065; View Diagram</a></div>



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

    subgraph SCDCL_ADLS_Azure_Data_Lake[" "]
        direction TB
        SCDA_ADLS["ADLS"]:::appBox
        SCDA_FCA["FCA"]:::eolBox
        SCDD_ADLS_Azure_Data_Lake[("🗄️ ADLS (Azure Data Lake)")]:::dbCloud
        SCDA_ADLS -.-> SCDD_ADLS_Azure_Data_Lake
        SCDA_FCA -.-> SCDD_ADLS_Azure_Data_Lake
    end
    style SCDCL_ADLS_Azure_Data_Lake fill:#E8F5E9,stroke:#388E3C,stroke-width:1px

    subgraph SCDCL_Data_Bricks[" "]
        direction TB
        SCDA_CFIN_S_4["CFIN S/4"]:::appBox
        SCDD_Data_Bricks[("🗄️ Data Bricks")]:::dbCyl
        SCDA_CFIN_S_4 -.-> SCDD_Data_Bricks
    end
    style SCDCL_Data_Bricks fill:#E3F2FD,stroke:#1976D2,stroke-width:1px

    subgraph SCDCL_Delta_Lake_Data_bricks[" "]
        direction TB
        SCDA_DataBricks["DataBricks"]:::appBox
        SCDD_Delta_Lake_Data_bricks[("🗄️ Delta Lake (Data bricks)")]:::dbCloud
        SCDA_DataBricks -.-> SCDD_Delta_Lake_Data_bricks
    end
    style SCDCL_Delta_Lake_Data_bricks fill:#FFF3E0,stroke:#E65100,stroke-width:1px

    subgraph SCDCL_Google_Cloud[" "]
        direction TB
        SCDA_APIGEE["APIGEE"]:::appBox
        SCDD_Google_Cloud[("🗄️ Google Cloud")]:::dbCyl
        SCDA_APIGEE -.-> SCDD_Google_Cloud
    end
    style SCDCL_Google_Cloud fill:#FFFDE7,stroke:#F57F17,stroke-width:1px

    subgraph SCDCL_Legacy_HANA[" "]
        direction TB
        SCDA_BOBJ["BOBJ"]:::appBox
        SCDA_BPC["BPC"]:::appBox
        SCDA_ECC["ECC"]:::eolBox
        SCDA_Finance_HANA["Finance HANA"]:::appBox
        SCDA_Legacy_MDG["Legacy MDG"]:::appBox
        SCDA_SAP_ECC["SAP ECC"]:::appBox
        SCDA_SAP_PO["SAP PO"]:::appBox
        SCDD_Legacy_HANA[("🗄️ Legacy HANA")]:::dbData
        SCDA_BOBJ -.-> SCDD_Legacy_HANA
        SCDA_BPC -.-> SCDD_Legacy_HANA
        SCDA_ECC -.-> SCDD_Legacy_HANA
        SCDA_Finance_HANA -.-> SCDD_Legacy_HANA
        SCDA_Legacy_MDG -.-> SCDD_Legacy_HANA
        SCDA_SAP_ECC -.-> SCDD_Legacy_HANA
        SCDA_SAP_PO -.-> SCDD_Legacy_HANA
    end
    style SCDCL_Legacy_HANA fill:#FCE4EC,stroke:#C62828,stroke-width:1px

    subgraph SCDCL_Legacy_HANA_Cloud[" "]
        direction TB
        SCDA_SAP_IBP["SAP IBP"]:::appBox
        SCDD_Legacy_HANA_Cloud[("🗄️ Legacy HANA Cloud")]:::dbData
        SCDA_SAP_IBP -.-> SCDD_Legacy_HANA_Cloud
    end
    style SCDCL_Legacy_HANA_Cloud fill:#E8EAF6,stroke:#283593,stroke-width:1px

    subgraph SCDCL_MS_SQL[" "]
        direction TB
        SCDA_COMPASS["COMPASS"]:::appBox
        SCDA_ICOST["ICOST"]:::appBox
        SCDA_MyDeals["MyDeals"]:::appBox
        SCDA_OneMPS["OneMPS"]:::appBox
        SCDA_SDRA_Demand["SDRA Demand"]:::appBox
        SCDA_SPAN["SPAN"]:::appBox
        SCDA_SPEED_LEGACY["SPEED-LEGACY"]:::appBox
        SCDA_SnOP["SnOP"]:::appBox
        SCDA_Wafer_Starts["Wafer Starts"]:::appBox
        SCDD_MS_SQL[("🗄️ MS SQL")]:::dbCyl
        SCDA_COMPASS -.-> SCDD_MS_SQL
        SCDA_ICOST -.-> SCDD_MS_SQL
        SCDA_MyDeals -.-> SCDD_MS_SQL
        SCDA_OneMPS -.-> SCDD_MS_SQL
        SCDA_SDRA_Demand -.-> SCDD_MS_SQL
        SCDA_SPAN -.-> SCDD_MS_SQL
        SCDA_SPEED_LEGACY -.-> SCDD_MS_SQL
        SCDA_SnOP -.-> SCDD_MS_SQL
        SCDA_Wafer_Starts -.-> SCDD_MS_SQL
    end
    style SCDCL_MS_SQL fill:#F3E5F5,stroke:#7B1FA2,stroke-width:1px

    subgraph SCDCL_Oracle[" "]
        direction TB
        SCDA_CIBR["CIBR"]:::eolBox
        SCDA_EATS["EATS"]:::eolBox
        SCDA_EDW["EDW"]:::appBox
        SCDA_MARS["MARS"]:::eolBox
        SCDA_MES_300["MES 300"]:::appBox
        SCDA_WorkStream["WorkStream"]:::eolBox
        SCDA_Workstream["Workstream"]:::eolBox
        SCDA_XEUS["XEUS"]:::eolBox
        SCDD_Oracle[("🗄️ Oracle")]:::dbCyl
        SCDA_CIBR -.-> SCDD_Oracle
        SCDA_EATS -.-> SCDD_Oracle
        SCDA_EDW -.-> SCDD_Oracle
        SCDA_MARS -.-> SCDD_Oracle
        SCDA_MES_300 -.-> SCDD_Oracle
        SCDA_WorkStream -.-> SCDD_Oracle
        SCDA_Workstream -.-> SCDD_Oracle
        SCDA_XEUS -.-> SCDD_Oracle
    end
    style SCDCL_Oracle fill:#E0F2F1,stroke:#00695C,stroke-width:1px

    subgraph SCDCL_Oracle_DB[" "]
        direction TB
        SCDD_Oracle_DB[("🗄️ Oracle DB")]:::dbCyl
    end
    style SCDCL_Oracle_DB fill:#FBE9E7,stroke:#BF360C,stroke-width:1px

    subgraph SCDCL_PEGA_Data[" "]
        direction TB
        SCDA_PEGA["PEGA"]:::eolBox
        SCDD_PEGA_Data[("🗄️ PEGA Data")]:::dbCyl
        SCDA_PEGA -.-> SCDD_PEGA_Data
    end
    style SCDCL_PEGA_Data fill:#F1F8E9,stroke:#558B2F,stroke-width:1px

    subgraph SCDCL_S4_HANA[" "]
        direction TB
        SCDA_Corp_IP_S_4["Corp / IP S/4"]:::appBox
        SCDA_IF_S_4["IF S/4"]:::appBox
        SCDD_S4_HANA[("🗄️ S4/HANA")]:::dbData
        SCDA_Corp_IP_S_4 -.-> SCDD_S4_HANA
        SCDA_IF_S_4 -.-> SCDD_S4_HANA
    end
    style SCDCL_S4_HANA fill:#FFF8E1,stroke:#FF8F00,stroke-width:1px

    subgraph SCDCL_S4_HANA_SideCar[" "]
        direction TB
        SCDA_SideCar["SideCar"]:::appBox
        SCDD_S4_HANA_SideCar[("🗄️ S4/HANA (SideCar)")]:::dbData
        SCDA_SideCar -.-> SCDD_S4_HANA_SideCar
    end
    style SCDCL_S4_HANA_SideCar fill:#E1F5FE,stroke:#0277BD,stroke-width:1px

    subgraph SCDCL_Snowflake_Cloud_DW[" "]
        direction TB
        SCDA_SnowFlake["SnowFlake"]:::appBox
        SCDD_Snowflake_Cloud_DW[("🗄️ Snowflake Cloud DW")]:::dbCloud
        SCDA_SnowFlake -.-> SCDD_Snowflake_Cloud_DW
    end
    style SCDCL_Snowflake_Cloud_DW fill:#E8F5E9,stroke:#388E3C,stroke-width:1px

    subgraph SCDCL_e_g_Azure_SQL[" "]
        direction TB
        SCDA_e_g_XEUS["e.g. XEUS"]:::appBox
        SCDD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCloud
        SCDA_e_g_XEUS -.-> SCDD_e_g_Azure_SQL
    end
    style SCDCL_e_g_Azure_SQL fill:#E3F2FD,stroke:#1976D2,stroke-width:1px

    subgraph SCDCL_e_g_SAP_HANA[" "]
        direction TB
        SCDA_e_g_MES_300["e.g. MES 300"]:::appBox
        SCDD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbData
        SCDA_e_g_MES_300 -.-> SCDD_e_g_SAP_HANA
    end
    style SCDCL_e_g_SAP_HANA fill:#FFF3E0,stroke:#E65100,stroke-width:1px

    SCDD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| SCDD_e_g_Azure_SQL
    SCDD_Oracle ==>|"Direct"| SCDD_MS_SQL
    SCDD_MS_SQL ==>|"SAP PO"| SCDD_Legacy_HANA
    SCDD_MS_SQL ==>|"Direct"| SCDD_Oracle
    SCDD_Legacy_HANA ==>|"Direct"| SCDD_Oracle
    SCDD_Oracle ==>|"SAP PO"| SCDD_Legacy_HANA
    SCDD_Legacy_HANA ==>|"SLT"| SCDD_S4_HANA_SideCar
    SCDD_S4_HANA_SideCar ==>|"CIF"| SCDD_ADLS_Azure_Data_Lake
    SCDD_ADLS_Azure_Data_Lake ==>|"Autoloader"| SCDD_Delta_Lake_Data_bricks
    SCDD_Delta_Lake_Data_bricks ==>|"Spark Snowflake Connector"| SCDD_Snowflake_Cloud_DW
    SCDD_S4_HANA ==>|"SLT"| SCDD_S4_HANA_SideCar
    SCDD_MS_SQL ==>|"Manual"| SCDD_Data_Bricks
    SCDD_ADLS_Azure_Data_Lake ==>|"Direct"| SCDD_MS_SQL
    SCDD_Legacy_HANA ==>|"APIGEE"| SCDD_Google_Cloud
    SCDD_Google_Cloud ==>|"APIGEE"| SCDD_PEGA_Data
    SCDD_Legacy_HANA_Cloud ==>|"Direct"| SCDD_ADLS_Azure_Data_Lake
    SCDD_Legacy_HANA ==>|"ETL"| SCDD_Oracle
    SCDD_Legacy_HANA ==>|"Denodo"| SCDD_MS_SQL

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWm1vozgQ_itWVpW6Urub9zdpV-LF9HJKmlzJXu90OSE3cVpUAhEht822_e9nYwNOMIbcbT6AjZ8Zj5-xB3vIa20ZrHBtWLu4eHV9NxqC10UtesIbvKgNwaL2gHakdEVKO7zch250GON_sMcavSBIWmOR31HoogcP72gz0bMO_Mh2f3BVjc72hYHpcwttXO_AWmz8GGDwbXQFNKKAKH-PUV7wffmEwohr2-_wBL3cu6voiT5ZI2-HKe4p2nhj9IC9uNso3MdPfTIse4uWrv9IH7c69GGI_GfhYbvz_g7eLy4WftoXmOsLH5Df0kO7nYnXAG23evAC1q7nDT8YBuxY1tUuCoNnPPxQr_f6ZptXr79T04bN7cvVMvCCkDa3tK5xom_1YBy8RF0fdo1Bqq4Je2arWaiuoXdgs55X5wX7FVeo6ya09P9pn4kilOhrQt1qCvr6rb6l0Nc226cG4sDL-LMswzQzfUa32W_2C_XpvYbRIPYxjbv9w2OItk_ANkxj7Gjm2Ha0H_sQO9RgZ4ye8V-LGvHy3wxPfys3xMvIDfzUr_RHFGixPMHTGxEZDofM0Scoy9AIiFwZhg3mCGPKLblc1Bb7Vb-1ItfVsr3Yr3F9DSgUXMZYENNMsR8XtY9UOXelxE5w_en6a3FneZsrCWCf97WLDh5W0MqdB_tWB2aztdXvw5Zx7LwGWeJyd8XK9NBdPu_O8ZJhjW4d22kTGVoE9ud2obfMo07kDohJZ4iM9YNX0KtAo6BawZ6ASkhrWU3LTElrDHpds1mZNOxxFzDND2fzR8VS1rOKikN5nwV0UnA8icFlTC1Dq2d0ZobIr7RbFdVSgTTOWC1YT1mH3U6jXq_K-k0QPHrYiU0_K6LMRjcQ0pgSFxQcH_UgZ5ZBAOOveKayrgQeRdUK9kRYxpkJeylnVqdnNXpVORvjR7Q8OL9ot9o5lOlT_VeCpzdFENZnBgXNDAUGGhRDroWBmgRG10f-EidW8iqgVYVmPrSJeUNkWAWQikLC1mbcHlICqU2F2NmUQ2dTxaQRKZbPGW4cGw-fMnRtSEgXZoygN897JRwZYSWcyH8lgYz6SnDOe2XsbKqCSteNgEqWjQHb0FBuaSotm_PjDR3CSJ_xuUNK1SaPMuwIU-gk9kgmEjdATmJpCMph020G1KxutinutzqDVlVCJ7Zj_zY-a4cxncw0m24FeUmxWEfG1J4TZHxX4CYHE5PjCUHykgI79fFkRrtnBVWoMO_IyxNvkE-nCa0BVlPJzLRbCiY3JQpC4jx4oxl_xmhSvWZVlZQ_jScfuSlQ92iNQ8eOyOGKEhJXAasq5iv3o3ySTmxAGlX7N-ZJYWIyfTJ3loG4B8tgzHtlKMGFpVDisnJM5rdSLHFTGUb0VQFWupQZIAmILXJG7qTrt6c3LK3yjncaoqV31jnOGOl3dPGSm-LVD7U5XWP0pkKZ9xRk3qvWtnZHNdGbQtME2k6rXqdAaANSUq2QIHy2oxCjDV0faUWhnYJ2osSuTOIP-I1aTW-KkyxnX77qWKNq1REXCLOG4_N-KMWY92UQyn4phrmgDJYRXgW5q4SkNBdgpOuHAZL3X52cGBtCzqU76BjnrR_H1KsvIVMQUnkemHre-YrhEH1JRNDhQDhZ6FarW688ohmJbvEJ75ygQIUInt4U0z1TLR83bY8zBopJH2MyV6cqFfSkmISehtUX8iqdTl9vWlXpsdtnH7qMINw6o1mSViE18BmMZsrcCnlZWlxgZJVkYRKT5KTa7c9lBxTBQIFarlZqVhFMyj9HZMfePsyWG6lZ1VMFXJVjuytsoPCs3XsqwkvljKYySmbBJYd9VO7dGSZPXNJSTmCqg8ethtWxYBa3mr2eblYm0g--rz2azImPAk78Iq7OJZG2PJYATssqPvO9FVCaANlhCNCdgSKzlfYt0prrS8VsDvwzcq_YeeQp3TPPRlSQ7xzwp8dPINs-SGk97kfOaKyHJcCP9vASNpPeBTKPelDweIT7GZlYqpAed8-NtVQu2wvGgy_bEJrHnSlopMf-slgqGHDCY9JDCY0J7D9lVnOdgS9fvr5xIsyYNvLuIUlMcrVcurt8K3S0sFXhWpiCVEY8pggPODjJr70VpHvyEifqxV3cqYqKEkfWVzIo34c9nqcy0pAta-GyxshKZYu_CxU2cy3aPiLf59AKh6kyVfZeAUiGtEXhsxhrA98nPAaZ_qIgKo71LH6OHD1B_p5-dn4r-NRTRkjZPMw7MflC8FaUtM89lguebDflOTi5lSX-z9sM5-Oz1gImn-CDHCkn0ZXI4Tidlca45aoOTG2uAe3O-GU0h8b82x0EJMcBb82CqDu-y56SL5j0C8x267lLRFvlcZZ8Pyo67PjXsxBvpKcdLmkUiPI9gl70ViOipuq75MxD0ToINwXxfOzQj0vQX10H6-uxu8b5o81JFGfsJpG7Y4l5mcFgkAvbtavaBocb5K5qw1f2nw7y15AVXqO9F5F_ZdQQWfr2wV_WhvH_LGr77QpF2HQR8eaGPXz_F4_cT84=" title="View full diagram">&#128065; View Diagram</a></div>



### 3.3 Technology Architecture

> Applications grouped by hosting platform. Cloud platforms marked with ☁️.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef platBox fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C

    subgraph SCPP_ECA_Azure_Platform["☁️ ECA Azure Platform"]
        direction LR
        SCPA_ADLS["ADLS"]:::appBox
        SCPA_DataBricks["DataBricks"]:::appBox
        SCPA_SnowFlake["SnowFlake"]:::appBox
    end
    style SCPP_ECA_Azure_Platform fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C

    subgraph SCPP_Google_Cloud_Platform["☁️ Google Cloud Platform"]
        direction LR
        SCPA_APIGEE["APIGEE"]:::appBox
    end
    style SCPP_Google_Cloud_Platform fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C

    subgraph SCPP_Intel_MES_On_Premise["🖥️ Intel MES On-Premise"]
        direction LR
    end
    style SCPP_Intel_MES_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SCPP_Intel_Middleware_On_Premise["🖥️ Intel Middleware On-Premise"]
        direction LR
    end
    style SCPP_Intel_Middleware_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SCPP_Legacy_Azure_Platform["☁️ Legacy Azure Platform"]
        direction LR
        SCPA_FCA["FCA"]:::eolBox
    end
    style SCPP_Legacy_Azure_Platform fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C

    subgraph SCPP_Linux_Server_Platform["🖥️ Linux Server Platform"]
        direction LR
        SCPA_CIBR["CIBR"]:::eolBox
        SCPA_EDW["EDW"]:::appBox
        SCPA_MARS["MARS"]:::eolBox
        SCPA_MES_300["MES 300"]:::appBox
        SCPA_WorkStream["WorkStream"]:::eolBox
        SCPA_Workstream["Workstream"]:::eolBox
        SCPA_XEUS["XEUS"]:::eolBox
    end
    style SCPP_Linux_Server_Platform fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SCPP_MS_Windows_Server_Platform["🖥️ MS Windows Server Platform"]
        direction LR
        SCPA_COMPASS["COMPASS"]:::appBox
        SCPA_EATS["EATS"]:::eolBox
        SCPA_ICOST["ICOST"]:::appBox
        SCPA_MyDeals["MyDeals"]:::appBox
        SCPA_OneMPS["OneMPS"]:::appBox
        SCPA_SDRA_Demand["SDRA Demand"]:::appBox
        SCPA_SPAN["SPAN"]:::appBox
        SCPA_SPEED_LEGACY["SPEED-LEGACY"]:::appBox
        SCPA_SnOP["SnOP"]:::appBox
        SCPA_Wafer_Starts["Wafer Starts"]:::appBox
    end
    style SCPP_MS_Windows_Server_Platform fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SCPP_PEGA_Cloud_Platform["☁️ PEGA Cloud Platform"]
        direction LR
        SCPA_PEGA["PEGA"]:::eolBox
    end
    style SCPP_PEGA_Cloud_Platform fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SCPP_S4_HANA_Netweaver["🖥️ S4/HANA Netweaver"]
        direction LR
        SCPA_CFIN_S_4["CFIN S/4"]:::appBox
        SCPA_Corp_IP_S_4["Corp / IP S/4"]:::appBox
        SCPA_IF_S_4["IF S/4"]:::appBox
    end
    style SCPP_S4_HANA_Netweaver fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SCPP_S4_HANA_Netweaver_SideCar["🖥️ S4/HANA Netweaver (SideCar)"]
        direction LR
        SCPA_SideCar["SideCar"]:::appBox
    end
    style SCPP_S4_HANA_Netweaver_SideCar fill:#B2EBF2,stroke:#00838F,stroke-width:3px,color:#004D40

    subgraph SCPP_SAP_HANA_Cloud["☁️ SAP HANA Cloud"]
        direction LR
        SCPA_SAP_IBP["SAP IBP"]:::appBox
    end
    style SCPP_SAP_HANA_Cloud fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SCPP_SAP_Netweaver["🖥️ SAP Netweaver"]
        direction LR
        SCPA_BOBJ["BOBJ"]:::appBox
        SCPA_BPC["BPC"]:::appBox
        SCPA_ECC["ECC"]:::eolBox
        SCPA_Finance_HANA["Finance HANA"]:::appBox
        SCPA_Legacy_MDG["Legacy MDG"]:::appBox
        SCPA_SAP_ECC["SAP ECC"]:::appBox
        SCPA_SAP_PO["SAP PO"]:::appBox
    end
    style SCPP_SAP_Netweaver fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

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
    SCPP_Intel_MES_On_Premise ==>|"e.g. Direct / API / File"| SCPP_Intel_Middleware_On_Premise
    SCPP_Linux_Server_Platform ==>|"Direct"| SCPP_MS_Windows_Server_Platform
    SCPP_MS_Windows_Server_Platform ==>|"SAP PO"| SCPP_SAP_Netweaver
    SCPP_MS_Windows_Server_Platform ==>|"Direct"| SCPP_Linux_Server_Platform
    SCPP_SAP_Netweaver ==>|"Direct"| SCPP_Linux_Server_Platform
    SCPP_Linux_Server_Platform ==>|"Direct"| SCPP_SAP_Netweaver
    SCPP_Linux_Server_Platform ==>|"SAP PO"| SCPP_SAP_Netweaver
    SCPP_SAP_Netweaver ==>|"SLT"| SCPP_S4_HANA_Netweaver_SideCar
    SCPP_S4_HANA_Netweaver_SideCar ==>|"CIF"| SCPP_ECA_Azure_Platform
    SCPP_S4_HANA_Netweaver ==>|"SLT"| SCPP_S4_HANA_Netweaver_SideCar
    SCPP_MS_Windows_Server_Platform ==>|"Manual"| SCPP_S4_HANA_Netweaver
    SCPP_Legacy_Azure_Platform ==>|"Direct"| SCPP_MS_Windows_Server_Platform
    SCPP_SAP_Netweaver ==>|"APIGEE"| SCPP_Google_Cloud_Platform
    SCPP_Google_Cloud_Platform ==>|"APIGEE"| SCPP_PEGA_Cloud_Platform
    SCPP_SAP_HANA_Cloud ==>|"Direct"| SCPP_ECA_Azure_Platform
    SCPP_SAP_Netweaver ==>|"ETL"| SCPP_Linux_Server_Platform
    SCPP_SAP_Netweaver ==>|"Denodo"| SCPP_MS_Windows_Server_Platform

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq1WQtvozgQ_isWq0p3UrtLSNqmkfYknr2skoJK93qnywm5wUlRCUQ8tu22_e83xkBIAg5Ns4mEbfz588zYwwzmRZiGLhEGwtHRixd4yQC9TITknizIRBigiXCHY6gdQy0m0zTykucR-UF81umHYdGbDfkLRx6-80lMu4FnFgaJ7f3MqTq95RMD0_sGXnj-M-uxyTwk6PvwGMlAAORvGcoPH6f3OEpytjQmY_x067nJPb0zw35MKO4-WfgjfEf8bNokSrO7AahlL_HUC-b0dk-kNyMcPFRunopvb-jt6GgSlHOhG2USIPhNfRzHGpkhvFwq4ROaeb4_-KSq-qlhHMdJFD6QwSdRPO9rvbx58khFG0jLp-Np6IcR7e7KZ-oG39LHSYWwr5-pFyWhpJ9rXWmdsLsi7CinuiRuEJLQX_EZhqppUsmnnkl9qd8ooHLeUTsgIGOM07t5hJf3yFYty9FV2ZF_phFxLJB4FkaLfyfCJJXOxM4knRFxhgCBMgQqEBPhP0ZFf64XkWnihQEaXa_uAjfwaiMb2GgBQwaDATPyBkrDCVYib_oQA3bV4Iywg_DR8PEDgQFlfRtPAjfXOHn2SZO6uUUVRdMNhbvk3e0lr7PoZRjOfeKofpi6jUZlIJSB3m9Xa3ip69SyWaWd5rViHVz5YZAQ3xnrtmMGjhWRhReTTHe333Xh6uLT3AIZEgESmcFJjtxhgDq16ib8kNNxtPJc1yePGDZPS-XKAQfRsW76g6s6InM8fd7xSGCgPZ8KhioDH1zZvmXPtWblawU6-L4deUH65Ngk-kGidbW31jaDIgZ9t_LqULkGWlpsq1-idO0WQHDlPATH8jV9uNKCw0QdoyuKFAieBjUO420YPdhJRDBVfNXgsFNQXB0R7xrxt_6dSk2LlstftzAH3_Vj27n1Ajd8jNvtgbGNcvzeG8EcW7JNbZHXOAujyzcUSAuOaYeqad8ALCt5G-dZI5BU0S3BahysGZCxRedmFV5M1q4hlJMFDlwalaGFWIs3xpKvKBgKLkrXNWekX8rqPxkamiesyc0RTCtLD0yLt-XxDNbaTiAlpAbJmog120XV5o1z8D1qgco7sgoK2TOnoEOBjhbtHLNGnIOrbPecP-Ur2bkiySPBYN16b7R7XygMlbDWTmgMrxzb6VEvhCqyv_Q4m0UNo6UztIoB0EJf0NDaMWpo5AOGRj2yzrhbiv960zq25xIVtzUx-i3H_97W2Cv-vLanKQqiIgeQdMWQKjlAv9s3ODlAT-s1mUS22FTZrt70LehFmQmy3tZKA-dQyZ5EMB5qLZVeE-Xwiw_0u3wKxH23Pymm8g3oaMHxCMVSKchSeSFPpRi4cgKe4QU4mJLMUDSjZM1skTjMeT451i5hTJ7IQoMXSmQrl4capZSpEWuZOdQy26_2r_N04syL7Blje3Nbk8_zz0UiD91tV5qS5rlcxrBK6HYpuy7OwRN5Sg_PW-Y9kih167d3JjQ8jplLU9x7NF9l1RlPY2rdpP-agAdY8Abir1__eM1F1DKFIF7BkQFcDc-HF9HXuhWpMNa-W7ck5byzVmaoz-7ZFIy9JGzOtCp8nHSMkRZu-Vrjee_h2RCuVo8K37qH70XxDlM1acWjaGmYOkXs0c1qXFO0rnI0RnTGpw6Nkm_7vI5HtKdAO1d7jIOUHlg3cVZtXHtcsf-OrjN4cez3yjnZq1DUn_zVUtUk9RuyVLKSWqX4C1ajjH4z-pgbEfgGELYy6na8gNUigVsNEVNXRNZIvjHM6zGCt0z9SmsXGUbqZmjdThQpzF4LSBJEhc2wS1FmgZrCdUak4gBxC6itCX9HED1Br3_7o_Dx2uyd88oZZYndjlrMTMW3h1P6LwPVxcXFepTqLJ82h6sfCvPrXEXKoHcUXT8vuc6VjiE3x8ue3On1t7jMD3-eWXFpH3ofWecal595dFFZcelnpx1RbORSjO6ZqArHwoJEC-y5wuCFfbCD734umeHUT-CTm4DTJLSfg6kwyD6iCenSxQnRPAxesWA33_4HA_LtCQ==" title="View full diagram">&#128065; View Diagram</a></div>


<div class="page-footer"><span>Page 5</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 4 Future-State Architecture

Aggregated future-state: **44** systems, **54** connections, **429** flow hops.


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
    style BL fill:#FFFDE7,stroke:#F9A825,stroke-width:2px
    style AL fill:#E3F2FD,stroke:#0078D4,stroke-width:2px
```

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq9Wllv2zgQ_iuEiy4cbFJfcZLmYQGdjRdxQ1guksV6ITAWkwiVJUHHptm2_31JHdbBoewmTf0QwDPfDMkZcvgN46-9deDQ3nnvPiLhA1qqKx-xz9u36OgIKdH6wZ2ThKLJuzH6HSn_pRFFcfLkUbT2SBzTmMFyi-y7Tu_QbRq7Po1jlH3uXM87f2Oyjzo5jJMo-EzZ1_fK2XhafD16dJ3k4XwcfjlcB14Qnb8ZDoctnyQMUfXJfWqaMTXNrc_h8PRMP-7wOVFOtJZbhySk7VZVdcNUt25H05OpNmy6HdXc6senyqhUOyR-IFFEns7RFE1bg21cx_HoI2ERrMXFGKrj7WDGyXQ0HErXoJqTk2F7DTTwhNCYpqbrlVvtZHw2PpO7PR1po7bbmJC47dYYqYZxunV7qo5MZSx1e6yMjs_abtdekDo_HvFxO-Itt4EfRnTT2h9nxon2fut2bJzqE_lsR-rUGLNtlzuO09v8PCiXf696q9Q5mzjs75qeICUMPXdNEjfw0SV5ohFapePh6BhZT3FCNzGa-Qllxhyw6v2T--Mfx43oOjdbVFLLVGxlqS2EYZisYc6Bmjn7aFv2sX2hfFTaFlyJrMEx4krRlIRk7SZPthmwaZA4sXW2-W0rYV8FTwUWlVjEsSjDio6DKLRte4blE2MINEAzLJ-dPr8SQ5AJRegNgLwBgIbGIqtfWm0wkx9xOWjAF6pG7vpzDJlVWtDY8oNH0yOfKWS7VQKmc9u-dn2HFVvPs0XjOepv1QeCuakJS2QiAfaB72c3oVrg-2wftk1aasF8plm2jR8C6rtfhCkyJeoXSnGCM9NWvZTafwW-QyPB1kRci3ItZIz1C7bL_DjdhPz4EA9wwTCogZE5MoPUd0innzpE5mZBHiXWTAMZyQ4Hs5KeCnamugKHuwOH9wgc3idweHfg8B6Bw9LAYWng5spC2NxcJgINy54MhwLWsBATC3Css4zML9pwJj5iYgC-I5C7o7grhDvjJwmeLHJYn9vLiPixR1jZFq3mqNKKxsEjjWx1Ztu6stCE456pkTpDfa4WD7ylYFuJ3FvSNmQKlClAE_VK_ROy4HLQYKZiCM_EIBwreA7huRw04Gd2rn-AbPiZZSrYTNFAE0UT4WLttoDabWHD0AUgF4pQ16EaERJeiAX4tYWv21guE4FB9NlKIko2AnyrEYxujE_C-rhMAFL73padYfru_p30IGeG0DCZVWMs6jslvStJF2te_vi26ukZM1v1vu1kSpV5g4oVfqzLZemkjLe_D_8qzBXdZDRJV9Enn5Mvjem94J6Jlg9u5CBMIibt84UdIp36gRMclMOVXKc2nkDL9phkxrheEBTOw15gXq6icNEIQ32lNRrmw-StXCvjXHecc6GC1gQRCyeXhm5I6y4rduaDjK5wOE89agV3yUC90q3t4upb4Tn2Qqqe4aRGMbqt94tJ6wbodrmgm4C9EZipn_c3ikPChHK35VT5CLwyV60RslLGNrc7sSjP9XEapLgYqX1vfQPuusoHo8Ev2I0tRtwKPvoNLajHVlJfQnFhVD4arPkFc2lS6F31YpvYGA2A2qHgWYwe3eQhS89BbQcVHKMxrsB9fsbZAsh416GHpiE4YxN_eSEFJtYYSF5MJVWg00YowE3G_0p5xkCe8SvlGf9YnnFnnvFPzDPuyDPvMMDDWrQNNWROWUBwRj78VsdRIA1lVoWzs4S_Slp-Xk5-TUKaBb7zLgDL8LYhKecZuveU1u6nfa7ivZ2AeSz6lV9Xussrtdwv0PXLd8yG-c_f92rqgbrELENx4vrZ9xj1L5ZLfLBvnF5tYGlsi5yXJ3FhsuaU-17Q6rnWjMiGPrJ25SCP4TW9RRaN_nXX7P8YfetKwQPT9ehg5gTrwcLU9l7uqw4uX7Ki1WJ8lf0zIy49ZmOs2yVGckk919uusNRcanmqjS9hwNJeLBz12YY-QEcor5zoOuJ7o2-FlDrF47rro6rUDdCnmKL88GyJ2B2rCPWH2c7K98yVwjl4Eb3M2vdaOViwTc_PNz8a5hL3VS-47ejv6uY_xooL0vGCoRsORqt0OHRO6_U3e7Dx608MYJwkKareE0Cr7PnPr78w7HdV158YCovsjaDYeoMiAPwMlj62jwvlu0H2_6bq9YD9V7Itbz4LQICudwAIL_bxACpv3CHFDSzfttoSXa2VliCqJhAENLs3AMKbM0Dc7roASLOpggDNbglGiMRKjmtwJTmMEyFY25W7FueHEfvNFu83W9w124z8QvLi6ACqktuCqj3mvc-kO2bcYocQovmaAUEqdidR8qIm03FiJ1FlTEiiK2mDTM3uKUgFH5z8QoAURbkGVFlphuRVCQa0Wc0F5I0KK9M3jfOfkqiX1c9E9NoPDCQ_E6mbKqWpMTHHpr7r1yC9w96GRhviOr3zr73kgW74T18cekdSL-l9P-yRNAmsJ3_dO0-ilB720pBtSqq7hPHTTS78_j8X2v21" title="View full diagram">&#128065; View Diagram</a></div>



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

    subgraph SFDCL_Azure_Analysis_Services[" "]
        direction TB
        SFDA_Power_BI_DARC["Power BI (DARC)"]:::appBox
        SFDD_Azure_Analysis_Services[("🗄️ Azure Analysis Services")]:::dbCloud
        SFDA_Power_BI_DARC -.-> SFDD_Azure_Analysis_Services
    end
    style SFDCL_Azure_Analysis_Services fill:#E8F5E9,stroke:#388E3C,stroke-width:1px

    subgraph SFDCL_Azure_Data_Lake_ADLS[" "]
        direction TB
        SFDA_ECA_ADLS["ECA-ADLS"]:::appBox
        SFDD_Azure_Data_Lake_ADLS[("🗄️ Azure Data Lake (ADLS)")]:::dbCloud
        SFDA_ECA_ADLS -.-> SFDD_Azure_Data_Lake_ADLS
    end
    style SFDCL_Azure_Data_Lake_ADLS fill:#E3F2FD,stroke:#1976D2,stroke-width:1px

    subgraph SFDCL_Delta_Lake[" "]
        direction TB
        SFDA_ECA_DataBricks["ECA-DataBricks"]:::appBox
        SFDD_Delta_Lake[("🗄️ Delta Lake")]:::dbCloud
        SFDA_ECA_DataBricks -.-> SFDD_Delta_Lake
    end
    style SFDCL_Delta_Lake fill:#FFF3E0,stroke:#E65100,stroke-width:1px

    subgraph SFDCL_N_A_Middleware[" "]
        direction TB
        SFDA_PDF_SMH["PDF-SMH"]:::appBox
        SFDD_N_A_Middleware[("🗄️ N/A (Middleware)")]:::dbCyl
        SFDA_PDF_SMH -.-> SFDD_N_A_Middleware
    end
    style SFDCL_N_A_Middleware fill:#FFFDE7,stroke:#F57F17,stroke-width:1px

    subgraph SFDCL_N_A_SaaS[" "]
        direction TB
        SFDA_GraphiteConnect["GraphiteConnect"]:::appBox
        SFDD_N_A_SaaS[("🗄️ N/A (SaaS)")]:::dbCyl
        SFDA_GraphiteConnect -.-> SFDD_N_A_SaaS
    end
    style SFDCL_N_A_SaaS fill:#FCE4EC,stroke:#C62828,stroke-width:1px

    subgraph SFDCL_Oracle_DB[" "]
        direction TB
        SFDA_ECM_Windchill["ECM (Windchill)"]:::appBox
        SFDA_ICS_Phoenix["ICS (Phoenix)"]:::appBox
        SFDA_IF_PDH_Consumptional["IF PDH Consumptional"]:::appBox
        SFDA_IF_PDH_Foundational["IF PDH Foundational"]:::appBox
        SFDA_IF_PDH_Raw["IF PDH Raw"]:::appBox
        SFDA_IP_PDH_Consumptional["IP PDH Consumptional"]:::appBox
        SFDA_IP_PDH_Foundational["IP PDH Foundational"]:::appBox
        SFDA_IP_PDH_Raw["IP PDH Raw"]:::appBox
        SFDA_MES_300["MES 300"]:::appBox
        SFDA_PDH_Consumptional["PDH Consumptional"]:::appBox
        SFDA_PDH_Foundational["PDH Foundational"]:::appBox
        SFDA_PDH_Raw["PDH Raw"]:::appBox
        SFDA_WorkStream["WorkStream"]:::appBox
        SFDA_XEUS["XEUS"]:::appBox
        SFDD_Oracle_DB[("🗄️ Oracle DB")]:::dbCyl
        SFDA_ECM_Windchill -.-> SFDD_Oracle_DB
        SFDA_ICS_Phoenix -.-> SFDD_Oracle_DB
        SFDA_IF_PDH_Consumptional -.-> SFDD_Oracle_DB
        SFDA_IF_PDH_Foundational -.-> SFDD_Oracle_DB
        SFDA_IF_PDH_Raw -.-> SFDD_Oracle_DB
        SFDA_IP_PDH_Consumptional -.-> SFDD_Oracle_DB
        SFDA_IP_PDH_Foundational -.-> SFDD_Oracle_DB
        SFDA_IP_PDH_Raw -.-> SFDD_Oracle_DB
        SFDA_MES_300 -.-> SFDD_Oracle_DB
        SFDA_PDH_Consumptional -.-> SFDD_Oracle_DB
        SFDA_PDH_Foundational -.-> SFDD_Oracle_DB
        SFDA_PDH_Raw -.-> SFDD_Oracle_DB
        SFDA_WorkStream -.-> SFDD_Oracle_DB
        SFDA_XEUS -.-> SFDD_Oracle_DB
    end
    style SFDCL_Oracle_DB fill:#E8EAF6,stroke:#283593,stroke-width:1px

    subgraph SFDCL_SAP_HANA[" "]
        direction TB
        SFDA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
        SFDA_Corp_IP_S_4_HANA["Corp / IP S/4 HANA"]:::appBox
        SFDA_IF_S_4_HANA["IF S/4 HANA"]:::appBox
        SFDA_SAP_BOBJ["SAP BOBJ"]:::eolBox
        SFDA_SAP_PAPM["SAP PAPM"]:::appBox
        SFDA_SAP_S_4_MDG["SAP S/4 MDG"]:::appBox
        SFDA_SideCar["SideCar"]:::appBox
        SFDD_SAP_HANA[("🗄️ SAP HANA")]:::dbData
        SFDA_CFIN_S_4_HANA -.-> SFDD_SAP_HANA
        SFDA_Corp_IP_S_4_HANA -.-> SFDD_SAP_HANA
        SFDA_IF_S_4_HANA -.-> SFDD_SAP_HANA
        SFDA_SAP_BOBJ -.-> SFDD_SAP_HANA
        SFDA_SAP_PAPM -.-> SFDD_SAP_HANA
        SFDA_SAP_S_4_MDG -.-> SFDD_SAP_HANA
        SFDA_SideCar -.-> SFDD_SAP_HANA
    end
    style SFDCL_SAP_HANA fill:#F3E5F5,stroke:#7B1FA2,stroke-width:1px

    subgraph SFDCL_SAP_HANA_Cloud[" "]
        direction TB
        SFDA_SAP_Ariba["SAP Ariba"]:::appBox
        SFDA_SAP_IBP["SAP IBP"]:::appBox
        SFDA_SAP_SAC["SAP SAC"]:::appBox
        SFDD_SAP_HANA_Cloud[("🗄️ SAP HANA Cloud")]:::dbData
        SFDA_SAP_Ariba -.-> SFDD_SAP_HANA_Cloud
        SFDA_SAP_IBP -.-> SFDD_SAP_HANA_Cloud
        SFDA_SAP_SAC -.-> SFDD_SAP_HANA_Cloud
    end
    style SFDCL_SAP_HANA_Cloud fill:#E0F2F1,stroke:#00695C,stroke-width:1px

    subgraph SFDCL_SQL_Server[" "]
        direction TB
        SFDA_ATCR["ATCR"]:::appBox
        SFDA_Capacity_Forecast_Data_Store["Capacity Forecast Data Store"]:::appBox
        SFDA_DMOCR["DMOCR"]:::appBox
        SFDA_DXCR["DXCR"]:::appBox
        SFDA_FCS["FCS"]:::eolBox
        SFDA_IF_Blue_Yonder["IF Blue Yonder"]:::appBox
        SFDA_IP_Blue_Yonder["IP Blue Yonder"]:::appBox
        SFDA_MARS["MARS"]:::appBox
        SFDA_PDM_Translator["PDM Translator"]:::appBox
        SFDA_SCS["SCS"]:::eolBox
        SFDA_SPEED["SPEED"]:::appBox
        SFDA_WSPW["WSPW"]:::appBox
        SFDD_SQL_Server[("🗄️ SQL Server")]:::dbCyl
        SFDA_ATCR -.-> SFDD_SQL_Server
        SFDA_Capacity_Forecast_Data_Store -.-> SFDD_SQL_Server
        SFDA_DMOCR -.-> SFDD_SQL_Server
        SFDA_DXCR -.-> SFDD_SQL_Server
        SFDA_FCS -.-> SFDD_SQL_Server
        SFDA_IF_Blue_Yonder -.-> SFDD_SQL_Server
        SFDA_IP_Blue_Yonder -.-> SFDD_SQL_Server
        SFDA_MARS -.-> SFDD_SQL_Server
        SFDA_PDM_Translator -.-> SFDD_SQL_Server
        SFDA_SCS -.-> SFDD_SQL_Server
        SFDA_SPEED -.-> SFDD_SQL_Server
        SFDA_WSPW -.-> SFDD_SQL_Server
    end
    style SFDCL_SQL_Server fill:#FBE9E7,stroke:#BF360C,stroke-width:1px

    subgraph SFDCL_Snowflake_Cloud_DW[" "]
        direction TB
        SFDA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
        SFDD_Snowflake_Cloud_DW[("🗄️ Snowflake Cloud DW")]:::dbCloud
        SFDA_ECA_SnowFlake -.-> SFDD_Snowflake_Cloud_DW
    end
    style SFDCL_Snowflake_Cloud_DW fill:#F1F8E9,stroke:#558B2F,stroke-width:1px

    subgraph SFDCL_e_g_Azure_SQL[" "]
        direction TB
        SFDA_e_g_XEUS["e.g. XEUS"]:::appBox
        SFDD_e_g_Azure_SQL[("🗄️ e.g. Azure SQL")]:::dbCloud
        SFDA_e_g_XEUS -.-> SFDD_e_g_Azure_SQL
    end
    style SFDCL_e_g_Azure_SQL fill:#FFF8E1,stroke:#FF8F00,stroke-width:1px

    subgraph SFDCL_e_g_SAP_HANA[" "]
        direction TB
        SFDA_e_g_MES_300["e.g. MES 300"]:::appBox
        SFDD_e_g_SAP_HANA[("🗄️ e.g. SAP HANA")]:::dbData
        SFDA_e_g_MES_300 -.-> SFDD_e_g_SAP_HANA
    end
    style SFDCL_e_g_SAP_HANA fill:#E1F5FE,stroke:#0277BD,stroke-width:1px

    SFDD_e_g_SAP_HANA ==>|"e.g. Direct / API / File"| SFDD_e_g_Azure_SQL
    SFDD_Oracle_DB ==>|"Direct"| SFDD_N_A_Middleware
    SFDD_N_A_Middleware ==>|"EAI Connector"| SFDD_SAP_HANA
    SFDD_Oracle_DB ==>|"Direct"| SFDD_SQL_Server
    SFDD_SQL_Server ==>|"Direct"| SFDD_N_A_Middleware
    SFDD_Oracle_DB ==>|"PDM Translator"| SFDD_SQL_Server
    SFDD_SQL_Server ==>|"PDM Translator"| SFDD_SAP_HANA
    SFDD_SQL_Server ==>|"ADF Rest API / SFTP(Blob)"| SFDD_Azure_Data_Lake_ADLS
    SFDD_Azure_Data_Lake_ADLS ==>|"Unity Catalog"| SFDD_Delta_Lake
    SFDD_Delta_Lake ==>|"Snowflake Connector / Snowpipe"| SFDD_Snowflake_Cloud_DW
    SFDD_N_A_SaaS ==>|"MuleSoft & Reltio"| SFDD_SAP_HANA
    SFDD_SAP_HANA ==>|"ADF Rest API / SFTP(Blob)"| SFDD_Azure_Data_Lake_ADLS
    SFDD_SQL_Server ==>|"ADF / DB Unity Catalog / Th..."| SFDD_Azure_Data_Lake_ADLS
    SFDD_Snowflake_Cloud_DW ==>|"MuleSoft/BODS"| SFDD_SAP_HANA
    SFDD_SQL_Server ==>|"Direct"| SFDD_Snowflake_Cloud_DW
    SFDD_SQL_Server ==>|"ADF / DB Unity Catalog / Co..."| SFDD_Oracle_DB
    SFDD_Oracle_DB ==>|"Snowflake Connector / Snowpipe"| SFDD_Snowflake_Cloud_DW
    SFDD_Snowflake_Cloud_DW ==>|"Remote Function Adapter / M..."| SFDD_SAP_HANA
    SFDD_SAP_HANA_Cloud ==>|"SAC Data Export Service (AP..."| SFDD_Snowflake_Cloud_DW
    SFDD_SAP_HANA_Cloud ==>|"SAP Odata services with con..."| SFDD_SAP_HANA
    SFDD_SAP_HANA_Cloud ==>|"ADF / DB Unity Catalog / Co..."| SFDD_Oracle_DB
    SFDD_SAP_HANA_Cloud ==>|"Apigee / MuleSoft"| SFDD_SAP_HANA
    SFDD_Snowflake_Cloud_DW ==>|"Snowflake Connector / Snowpipe"| SFDD_Azure_Analysis_Services

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNqtWvlvo0YU_ldGrrbKSjl8xLFjqZW4ZteVndCQbbaqKzQx4wQFgwW4Sbqb_71vuMEwDNnmhxiG7x3zvTfXg2-9tWfR3qz34cM327XDGfq26oWPdEtXvRla9e5JAFfHcBXQ9d63w9cF_Yc68UPH89KnkcgfxLfJvUMD9hj0bDw3NOx_E1WD8e4lBrN2TLa28xo_MeiDR9GX-TGSQAEof4tQjve8fiR-mGjbB3RJXu5sK3xkLRviBJThHsOtsyD31InMhv4-anWhW8aOrG33gTWPxqzRJ-5TofF8_PaG3j58WLmZLXQrr1wEf2uHBIFKN4jsdrL3gja248x-UhRtjPFxEPreE5391O9Ppup5cnvyzFybDXcvx2vP8Xz2eCRdKBV91r3y6qTqptqFcpmpG2oTdTRsVDeQx9qwf6jO8fZWolCWVQ3LP-ifSkKS6htqMh4W9E1HU8zRd66eVx2knpPzh7Giqrk-5WI4HU4b9cmTgTIA_2KNwf7-wSe7R2RgVVmY0r97n5qSS5zXwA5Mg_r_2Gsa_LXqQaD_jkXYn2X7dB3anpuFlv2BDsnUvWfqm_LcVKUbBQSjeyTP0RFr-AhqZrNZHP-SpNpo_GjVW-2t6ciC_9b6fLXf0P4GRWiUolGKXvU-MgNJBHm-oZPTk1-5lmNp6iZqgvDVoXyikohoUzzW8hQcTafaSClHZADjlhcDli_mgjyBEXVhdAmApkipDFyesMtW0ivWeIxHicyg6IhhP3IJT3054LpssJXoMjxleYSHWM1YHlxOLtShKMsqdRKVXbllvsi-vX4KEobzBg7PBXv17EaAiNhWRnODBV5zAxw2c1A2d-CR1s841C7Gg35flMMrUzKXtmU59Jn4nXjUVWway89selDxCVxxmKtYqWfv6kxCRzmqkJWvTr3tAnVlCxz6ysCcQlWbZBTi8QQPJl0oNAjpNMA_MXk7pIrnuoAB0UpLC5mRPQ6N7DmPwIq1CpFMuoVCBknJU7RzTeGuXc3kXftk7cDkIHcbwkvzznat9SM4EI3gJTrKGprXJ8mcK4apP3rUtV9ADu7QUXLLlcKQcZ9NICvYb3fMJ8LMzjGCZlRqbteCvb1rkaqSYmu7jhvynIvCDU9Cr_dd7-a7Xuu73sl3vei7LuD7UjPMUb8PcLhCcMXB1nWySw9rutehb3nH2nt15_lPRuhTsgV4fsOR-Kp9YbML--HMC_lQqp8Y4udIlTnzQmlkFWaFTHfzeBJB14wjcbFiKMSlIBYiYP19nunv8kzv4FkyBgSQ7-nAO7wXdz3PbQEwS-5mWO06lGGyLbsm4Yv81DgdjS9HoguRIenmZ-lK6rIOKXh-ZRrmeSrI7pFxdo7YPWc8K56_Y1lQFIUmdIZgWhSQh9QuiMIyICDD-idfy7-BAFwidhmj43NoDVqX9GWCZpctuplDS_VTIsAcgjuejG1RhfgMH19xZrYsNvUTGzMY9z6Z19jmmheqQp6lqlsi1C5RiEk7OA2GGJKxL4ZMgiAAjjlvBNaOtxSS7vtGUPMZZ8NtIg-wNOw63MzogNRl0DFJKIfdkyTVouuW5JzLeoKGq7ZElpQ0iSVFICmTHvBTE8XnQE6CZt2qiYlZd4pM-tUFDh1qgXPjbhYralofTu6DQgXs4nIsXB8xfl9E9Rbqd4m8dKvcAJ798CZXwgqZ4Susa6CJBGFceTBCLzrfpo9R-jiuhkSPOVrV5XVkPPrl4b7GsK9cFFbYfg7-c6ZgmFBkZ0_NPz3XiniCeZ41oLiBv9GuSOqCkkvphjnGfrib3aV5CyXjwCHAWrTnXaK8gTe-on4b3H4buqapDMV-edtoQ79jG2j44Y3SPNMaRujvCxQDONtilnLFkZMp7ZB7IvJRdgkBv4rhIMVEYOVcE5LQu0qwpBLBlbNLRMIQ62SUUCJAllIcXP0cmYHS1VHWLgslJRmPLvri86PrPW8cViuNplxTveta4WQasBOXRlmBM7vnjZVDqw1jJgXGyxpS71rrnZn9IrEH9ngEH4BTogd4WijUj8dTeYhFiabmQ1KehgB24ZgJJsdyevpwilrO5mU79axGeuICPYC4jKbWC2SWLHB4LOHy8udUy9dyuMPiFWSm8D2HJyaXF3iizrdVedSyMQ6NIkeCggMVHgX2wkVYuiMa4DHW8h3RcDKR1UYWD4yhX3759XtChBrRBudBSZ_Df2w7MG6_Nwa6fGJOFMU6MrG6AnnNg0RYk-YoqQ2zBf173RlBxGp17qw0dnS1aqy67-hktEn4sI8HopKK0Q2FrWMcHgPf6key491_zLQ0vyFrfJzo_uKyzakCjxzvIdNXfTNUaUxkC_NyGjvmHrTu7F2eQU3zbqn-n6hc7h1qeJsQ_Qw9dmAkc4kqp_IP01RL_BlUMFGJJWi6fTw9PRVWe7iUlDt7Jl-rRqeMqKY9j2HxXilesVeVkljtiPg_MqCRnhu69UKK8N6Np3TJIruQMgPLop-cxEhOkImvcBqNzl7ay86DL0ySF_DwTlovqeP6Wq9YR9cW0xyk7_Sf7fARrT33PX7-QHjq9e3sB0oZa0m6cT1qCoZgpBs_i6is5Qv6AOvcX4UVdW31kSrdSgi-s_g8v9WU2y83Glpon7QrtWGNX9zkrfDan53VdzvHXkfF5fpVHd5nN72ucE90n24b31eApNIgmuxK5aY9FIg2WY0SUoclYeP524bdw8LU2K7atU68zcnC3tDD02xlzxCzm-62xrhYN7u8vDzYJPSOe1vqb4lt9Wbf4m_I4FM0i27I3gnhK7Ae2Yee8eque7Pou67efgf5TlWbQDS3cePbf_Tdy2Y=" title="View full diagram">&#128065; View Diagram</a></div>



### 4.3 Technology Architecture

> Applications grouped by hosting platform. Cloud platforms marked with ☁️.

```mermaid
%%{init: {"theme": "base", "securityLevel": "loose", "themeVariables": {"fontSize": "14px", "fontFamily": "Segoe UI, Arial"}, "flowchart": {"useMaxWidth": false, "htmlLabels": true, "nodeSpacing": 40, "rankSpacing": 50}} }%%
flowchart TB
    classDef appBox fill:#CCE5FF,stroke:#0078D4,stroke-width:2px,color:#003A6C
    classDef platBox fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20
    classDef eolBox fill:#FFCDD2,stroke:#C62828,stroke-width:2px,color:#B71C1C

    subgraph SFPP_Blue_Yonder_Cloud_SaaS["☁️ Blue Yonder Cloud SaaS"]
        direction LR
        SFPA_IF_Blue_Yonder["IF Blue Yonder"]:::appBox
        SFPA_IP_Blue_Yonder["IP Blue Yonder"]:::appBox
    end
    style SFPP_Blue_Yonder_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_Databricks_on_ECA_Azure_Cloud["☁️ Databricks on ECA Azure Cloud"]
        direction LR
        SFPA_ECA_DataBricks["ECA-DataBricks"]:::appBox
    end
    style SFPP_Databricks_on_ECA_Azure_Cloud fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C

    subgraph SFPP_GraphiteConnect_Cloud_SaaS["☁️ GraphiteConnect Cloud SaaS"]
        direction LR
        SFPA_GraphiteConnect["GraphiteConnect"]:::appBox
    end
    style SFPP_GraphiteConnect_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_Intel_Custom_On_Premise["🖥️ Intel Custom On-Premise"]
        direction LR
        SFPA_ATCR["ATCR"]:::appBox
        SFPA_Capacity_Forecast_Data_Store["Capacity Forecast Data Store"]:::appBox
        SFPA_DMOCR["DMOCR"]:::appBox
        SFPA_DXCR["DXCR"]:::appBox
        SFPA_FCS["FCS"]:::eolBox
        SFPA_MARS["MARS"]:::appBox
        SFPA_SCS["SCS"]:::eolBox
        SFPA_SPEED["SPEED"]:::appBox
        SFPA_WSPW["WSPW"]:::appBox
    end
    style SFPP_Intel_Custom_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_ECA_Platform_Azure_Cloud["☁️ Intel ECA Platform Azure Cloud"]
        direction LR
        SFPA_ECA_ADLS["ECA-ADLS"]:::appBox
    end
    style SFPP_Intel_ECA_Platform_Azure_Cloud fill:#BBDEFB,stroke:#0078D4,stroke-width:3px,color:#003A6C

    subgraph SFPP_Intel_ICS_Phoenix_On_Premise["🖥️ Intel ICS (Phoenix) On-Premise"]
        direction LR
        SFPA_ICS_Phoenix["ICS (Phoenix)"]:::appBox
    end
    style SFPP_Intel_ICS_Phoenix_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_MES_On_Premise["🖥️ Intel MES On-Premise"]
        direction LR
        SFPA_MES_300["MES 300"]:::appBox
        SFPA_WorkStream["WorkStream"]:::appBox
    end
    style SFPP_Intel_MES_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_Middleware_On_Premise["🖥️ Intel Middleware On-Premise"]
        direction LR
        SFPA_XEUS["XEUS"]:::appBox
    end
    style SFPP_Intel_Middleware_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_PDF_SMH_Middleware_On_Premise["🖥️ Intel PDF-SMH Middleware On-Premise"]
        direction LR
        SFPA_PDF_SMH["PDF-SMH"]:::appBox
    end
    style SFPP_Intel_PDF_SMH_Middleware_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_PDH_On_Premise["🖥️ Intel PDH On-Premise"]
        direction LR
        SFPA_IF_PDH_Consumptional["IF PDH Consumptional"]:::appBox
        SFPA_IF_PDH_Foundational["IF PDH Foundational"]:::appBox
        SFPA_IF_PDH_Raw["IF PDH Raw"]:::appBox
        SFPA_IP_PDH_Consumptional["IP PDH Consumptional"]:::appBox
        SFPA_IP_PDH_Foundational["IP PDH Foundational"]:::appBox
        SFPA_IP_PDH_Raw["IP PDH Raw"]:::appBox
        SFPA_PDH_Consumptional["PDH Consumptional"]:::appBox
        SFPA_PDH_Foundational["PDH Foundational"]:::appBox
        SFPA_PDH_Raw["PDH Raw"]:::appBox
    end
    style SFPP_Intel_PDH_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Intel_PDM_On_Premise["🖥️ Intel PDM On-Premise"]
        direction LR
        SFPA_PDM_Translator["PDM Translator"]:::appBox
    end
    style SFPP_Intel_PDM_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Microsoft_Power_BI_SaaS["☁️ Microsoft Power BI SaaS"]
        direction LR
        SFPA_Power_BI_DARC["Power BI (DARC)"]:::appBox
    end
    style SFPP_Microsoft_Power_BI_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_PTC_Windchill_On_Premise["🖥️ PTC Windchill On-Premise"]
        direction LR
        SFPA_ECM_Windchill["ECM (Windchill)"]:::appBox
    end
    style SFPP_PTC_Windchill_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_Analytics_Cloud_SaaS["☁️ SAP Analytics Cloud SaaS"]
        direction LR
        SFPA_SAP_SAC["SAP SAC"]:::appBox
    end
    style SFPP_SAP_Analytics_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_SAP_Ariba_Cloud_SaaS["☁️ SAP Ariba Cloud SaaS"]
        direction LR
        SFPA_SAP_Ariba["SAP Ariba"]:::appBox
    end
    style SFPP_SAP_Ariba_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_SAP_BusinessObjects_On_Premise["🖥️ SAP BusinessObjects On-Premise"]
        direction LR
        SFPA_SAP_BOBJ["SAP BOBJ"]:::eolBox
    end
    style SFPP_SAP_BusinessObjects_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_HANA_Sidecar_On_Premise["🖥️ SAP HANA Sidecar On-Premise"]
        direction LR
        SFPA_SideCar["SideCar"]:::appBox
    end
    style SFPP_SAP_HANA_Sidecar_On_Premise fill:#B2EBF2,stroke:#00838F,stroke-width:3px,color:#004D40

    subgraph SFPP_SAP_IBP_Cloud_SaaS["☁️ SAP IBP Cloud SaaS"]
        direction LR
        SFPA_SAP_IBP["SAP IBP"]:::appBox
    end
    style SFPP_SAP_IBP_Cloud_SaaS fill:#E1BEE7,stroke:#7B1FA2,stroke-width:3px,color:#4A148C

    subgraph SFPP_SAP_MDG_On_Premise["🖥️ SAP MDG On-Premise"]
        direction LR
        SFPA_SAP_S_4_MDG["SAP S/4 MDG"]:::appBox
    end
    style SFPP_SAP_MDG_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_PaPM_On_Premise["🖥️ SAP PaPM On-Premise"]
        direction LR
        SFPA_SAP_PAPM["SAP PAPM"]:::appBox
    end
    style SFPP_SAP_PaPM_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_S_4HANA_Central_Finance["🖥️ SAP S/4HANA Central Finance"]
        direction LR
        SFPA_CFIN_S_4_HANA["CFIN S/4 HANA"]:::appBox
    end
    style SFPP_SAP_S_4HANA_Central_Finance fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_SAP_S_4HANA_On_Premise["🖥️ SAP S/4HANA On-Premise"]
        direction LR
        SFPA_Corp_IP_S_4_HANA["Corp / IP S/4 HANA"]:::appBox
        SFPA_IF_S_4_HANA["IF S/4 HANA"]:::appBox
    end
    style SFPP_SAP_S_4HANA_On_Premise fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#1B5E20

    subgraph SFPP_Snowflake_on_ECA_Cloud["☁️ Snowflake on ECA Cloud"]
        direction LR
        SFPA_ECA_SnowFlake["ECA-SnowFlake"]:::appBox
    end
    style SFPP_Snowflake_on_ECA_Cloud fill:#B2EBF2,stroke:#00838F,stroke-width:3px,color:#004D40

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
    SFPP_Intel_MES_On_Premise ==>|"e.g. Direct / API / File"| SFPP_Intel_Middleware_On_Premise
    SFPP_Intel_MES_On_Premise ==>|"Direct"| SFPP_Intel_Middleware_On_Premise
    SFPP_Intel_Middleware_On_Premise ==>|"Direct"| SFPP_Intel_PDF_SMH_Middleware_On_Premise
    SFPP_Intel_PDF_SMH_Middleware_On_Premise ==>|"EAI Connector"| SFPP_SAP_S_4HANA_On_Premise
    SFPP_SAP_S_4HANA_On_Premise ==>|"SLT"| SFPP_SAP_S_4HANA_Central_Finance
    SFPP_Intel_MES_On_Premise ==>|"Direct"| SFPP_Intel_Custom_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"Direct"| SFPP_Intel_PDF_SMH_Middleware_On_Premise
    SFPP_PTC_Windchill_On_Premise ==>|"PDM Translator"| SFPP_Intel_PDM_On_Premise
    SFPP_Intel_PDM_On_Premise ==>|"PDM Translator"| SFPP_SAP_MDG_On_Premise
    SFPP_SAP_MDG_On_Premise ==>|"DRF (Data Replication Frame..."| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"PDM Translator"| SFPP_Intel_PDM_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"ADF Rest API / SFTP(Blob)"| SFPP_Intel_ECA_Platform_Azure_Cloud
    SFPP_Intel_ECA_Platform_Azure_Cloud ==>|"Unity Catalog"| SFPP_Databricks_on_ECA_Azure_Cloud
    SFPP_Databricks_on_ECA_Azure_Cloud ==>|"Snowflake Connector / Snowpipe"| SFPP_Snowflake_on_ECA_Cloud
    SFPP_GraphiteConnect_Cloud_SaaS ==>|"MuleSoft & Reltio"| SFPP_SAP_MDG_On_Premise
    SFPP_SAP_S_4HANA_On_Premise ==>|"SLT"| SFPP_SAP_HANA_Sidecar_On_Premise
    SFPP_SAP_S_4HANA_Central_Finance ==>|"SLT"| SFPP_SAP_HANA_Sidecar_On_Premise
    SFPP_SAP_HANA_Sidecar_On_Premise ==>|"ADF Rest API / SFTP(Blob)"| SFPP_Intel_ECA_Platform_Azure_Cloud
    SFPP_Intel_Custom_On_Premise ==>|"ADF / DB Unity Catalog / Th..."| SFPP_Intel_ECA_Platform_Azure_Cloud
    SFPP_Snowflake_on_ECA_Cloud ==>|"MuleSoft/BODS"| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Intel_ICS_Phoenix_On_Premise ==>|"Direct"| SFPP_Intel_Custom_On_Premise
    SFPP_Intel_Custom_On_Premise ==>|"Direct"| SFPP_Snowflake_on_ECA_Cloud
    SFPP_Blue_Yonder_Cloud_SaaS ==>|"ADF / DB Unity Catalog / Co..."| SFPP_Intel_PDH_On_Premise
    SFPP_Intel_PDH_On_Premise ==>|"Snowflake Connector / Snowpipe"| SFPP_Snowflake_on_ECA_Cloud
    SFPP_Snowflake_on_ECA_Cloud ==>|"Remote Function Adapter / M..."| SFPP_SAP_PaPM_On_Premise
    SFPP_SAP_Analytics_Cloud_SaaS ==>|"SAC Data Export Service (AP..."| SFPP_Snowflake_on_ECA_Cloud
    SFPP_SAP_Analytics_Cloud_SaaS ==>|"SAP Odata services with con..."| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Snowflake_on_ECA_Cloud ==>|"MuleSoft/BODS"| SFPP_SAP_S_4HANA_Central_Finance
    SFPP_SAP_Analytics_Cloud_SaaS ==>|"SAP Odata services with con..."| SFPP_SAP_S_4HANA_Central_Finance
    SFPP_SAP_PaPM_On_Premise ==>|"SAP Integration Suite / Sma..."| SFPP_SAP_S_4HANA_On_Premise
    SFPP_SAP_IBP_Cloud_SaaS ==>|"ADF / DB Unity Catalog / Co..."| SFPP_Intel_PDH_On_Premise
    SFPP_SAP_Ariba_Cloud_SaaS ==>|"Apigee / MuleSoft"| SFPP_SAP_S_4HANA_On_Premise
    SFPP_Snowflake_on_ECA_Cloud ==>|"Snowflake Connector / Snowpipe"| SFPP_Microsoft_Power_BI_SaaS
    SFPP_SAP_HANA_Sidecar_On_Premise ==> SFPP_SAP_BusinessObjects_On_Premise

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

<div style="text-align:center; margin:4px 0 8px 0; font-size:11px;"><a href="https://mermaid.live/view#pako:eNq9W4uPm0YT_1dWrlJdpcvFr3vEUivxzLkyMTKXJlX9Ca3N-sx3GCwevbsm9793FjAGDOvFj14kA8vsb2Z_O7PLDOR7a-5ZpDVovXv33XbtcIC-T1vhkqzItDVA09YMB3B2CWcBmUe-Hb6OyN_ESW46nre5G3f5A_s2njkkoLcBZ-G5oWH_k0J1-uuXRJi2q3hlO6_JHYM8egR9GV4iAQAA_C2Wcrzn-RL7YYoWBUTDL19tK1zSlgV2AkLlluHKGeEZcWK1oR_FrS4My1jjue0-0uZ-mzb62H3KNV63397Q27t3UzfThR7EqYvgb-7gIJDJAuH1WvRe0MJ2nMFPkqRcq-plEPreExn81G7f3sn99PL9MzVt0F2_XM49x_Pp7Z5wI5Xw1g4Oc4B3yo30MQPsKrdyr1sE7G0BO-K10m2XAInnbPFUVZLlboYn3XTvune1Boq3HakDBiaIQTR79PF6iQxV103RiYj5p-daxDclx4ss08DY-Gvamkbdm3ZnGi1Ie4GoFEqkUCyFqNS09b8Ekv5Ztk_moe25aDTZtoIOwRyqeTWAPVTziAAzGAySCSj31Ms9dXZP4lrpKMNXh7CGmDKpdERFuc2YvBU7qlA_M32h07-rYVLGIZ759vwpMD3XVCTBFP6JfJKoLBO6FUbAGAijWDghl5dXqoMCiTEQqICG99sGPnaYZqckiaKsqCIzHnq78VBF0id6aodE8lwXhsVwuZLkAW5XQgAFpRY-gupNPrkLDd2QOKYUBaG3MseuqftkZQckpsa661nwa-HrlKBYGCXCaOy-T4V52REepAkA0wMjACVM19Hw1VQ9QMJBGPuLaYRwCb03t9HmduzYKL7NQJW1caw8PrLkviVi35hSqkSdB34TmWShLMlowoQK0QMDyYiRDCaSoSuKTKXokYH11dC_ghg98PlZzeQftYPUOxkNdB32qIXnr1gLVeJldIHaSB-6UgnyyEjXKHrahJQ6Y0--PCXqhpJh6kuPuPYLZxRCD3SRdvnlgGDMaaSbXB6tCU_Vhp_JgzTF4GQHJA_ghOL32m0atdAfzljB5vlPRugTvKIhl1004a44nHNxZluWQ54xODAndVmHAxj8pnyhEUcPjZioMvJMhOiyahrafXNioON76HgcQal20JPCNaGJafrZ6Lrn5uf-kHVIjVXAo04QrdZUBjvJ8zrFKzSzntoTFNWLXAuXQfKt-zEm-HnbFS7YuUKl7Xoz2_VK2_VGtut523UO26sMb2J1hckN7N0aW2spKwzu_wu_17j9XjtoIdDMBygbBPCQ4fkxERraNjTjQzsnH5o9973AW4Sm7j1DQisOK7OnTAzFYkgcNkqdMmxZmEiUjg3IBW3gfCapMfXkWZP-IJlfbdeaLwF4r5uANMqkD3AVRdK22uLnWQ1dZA2c1NSZfHJ3MQTdFCD6X0N7HjCybZBDmdwBuTbVYwjUVSgSnPHxUGfeyX0kVuTbM7yPAypz4PjjvikD8XkDDkqmnWX8YhTYLgmC8ez_MIxgb6TQcZT6HBAvseax-HtKDD3dza7reKk3-SyRci98BoNtC0oZPhc9tANKOxzCDfSUMN1v0jN-j6kxdZMRdxVR7eYy4rvencrIiPtyn0HLUNT3hA1IHBg00DP1DDjjH37RpLOEiyZ_4vIBkDswLAyzT7VsFs0PfYrFz0HRwLMEhI51jYsEKnggC7qgaykF9JR__CXjzkIATFEcaRJxQx87pmq72J0ziIBZjBeFtANKO_ASIqnDz7FfUBBaYIXr2DPoNT81NWaflSIeN9mw09xTJM9f08Qqzw00oQ9oqDMIyueTua6QUB5O6jldzvWeFw5-Ipt3MZU12Uxq8-6ocS2WIqgUIS3IZtecbFSaefK9h5iPabVXr9h3yNXjVVqL1htsOhQ0LYzFCPzVsaI5J689U_iNi5rddrdXHUax0RvnRVSuyci3RdUYp7ayWjf-goEncP8a4F9__e1HaqIcDwjiXNCH8KvaDjjpj6oZySFWlnQ5QRlFUD4NCfhheJW1RAYsswi5A88uWSZqFGGI0ledtPDxg7X-5RTULJAJpjF6qEQqbU9H0Lvz2mwHa_fF2glorc3jE-xyFelHfaGoYq40bsDdp8HSzJQeFdORT1So59D3tROydux5XChEqo9X5Orqin_q2fwew0EdpiCrYDO8bU7C11Af9AvR8Wa_lODr3hvuKKp9wZjo--LSd9wSUOV4j5kO5pcTORXsLyzSCMm29Cz26MCgdW2vt2tT9cab08X4WCFRpEUOMWhd8Gdg0IEZ53ci7vCuyU1r4MrPqMdg1mXFZ3Ibln9-QLKICo4DTQ_LfGRxa6t53irO6AdxLBtNo7bmjfF_sdLu9eWa77b2UCx5uxQX31FULLX3FU59oohkzt2ErLyQIDVyk2c2wcLrkFBFWnkJLmW7JcevLKKmAxGk5Ksc5WXtwaePBvH_tiHOLgS9oGPvQPap0dHYonqCREGAnu1wieae22g3OdLX6x8pTm8_W1e5PLFVQ70OHvzjGTciWK2pY61wM5p2i2CnDIzKonSqYG0_EmryZjJONLecAVfzVol_I-CpLldlaCPyCFlRPimbW22kj4QHdTzR0Ej5pHyW-XKxkVROZnczeCpmFFLALtmtrlKp8UZqDr8L0t1UV3YE5YLxM5IsC5u9Z0dcK2jv3Oa-tchkd_PEhKbNd8rX9F-WGn78-LGYF3bWL-Xu0lGJdRHruMJwEWt89KfcWyz5qFJJEUvLPglX2uIWS7m57rTbtVii2rtpS63L1or4K2xbrcH35ON--D8CFlngyAnh8_wWjkLPeHXnrUH8wX0rWsMKSWQbQ1Ssksa3fwHtG5Pf" title="View full diagram">&#128065; View Diagram</a></div>


<div class="page-footer"><span>Page 6</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
<div style="page-break-before: always;"></div>

## 5 Transformation Analysis


### 5.1 System Landscape Changes

| Category | Count | Systems |
|----------|:---:|---|
| **Added in Future State** | 36 | ATCR, CFIN S/4 HANA, Capacity Forecast Data Store, Corp / IP S/4 HANA, DMOCR, DXCR, ECA-ADLS, ECA-DataBricks, ECA-SnowFlake, ECM (Windchill), FCS, GraphiteConnect, ICS (Phoenix), IF Blue Yonder, IF PDH Consumptional, IF PDH Foundational, IF PDH Raw, IF S/4 HANA, IP Blue Yonder, IP PDH Consumptional, IP PDH Foundational, IP PDH Raw, PDF-SMH, PDH Consumptional, PDH Foundational, PDH Raw, PDM Translator, Power BI (DARC), SAP Ariba, SAP BOBJ, SAP PAPM, SAP S/4 MDG, SAP SAC, SCS, SPEED, WSPW |
| **Removed from Future State** | 23 | ADLS, APIGEE, BOBJ, BPC, CFIN S/4, COMPASS, Corp / IP S/4, DataBricks, EDW, Finance HANA, ICOST, IF S/4, Legacy MDG, MyDeals, OneMPS, SAP ECC, SAP PO, SDRA Demand, SPAN, SPEED-LEGACY, SnOP, SnowFlake, Wafer Starts |
| **EOL Path (per IAPM)** | 6 | CIBR, EATS, ECC, FCA, PEGA, Workstream |
| **Continuing Systems** | 8 | — |

> **Reconciliation Note:** System lifecycle status is sourced from IAPM (Intel Application Portfolio Management). Systems shown as *Removed from Future State* are not in scope for this release but are **not** decommissioned unless marked *EOL Path* above. EOL decommissioning is planned post-R5.

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

**Connections Not in Future State (40):**

| Source | Target |
|---|---|
| ADLS | DataBricks |
| APIGEE | PEGA |
| BPC | ICOST |
| CIBR | ICOST |
| CIBR | SAP ECC |
| CIBR | SAP PO |
| CIBR | SPAN |
| COMPASS | ICOST |
| Corp / IP S/4 | SideCar |
| DataBricks | SnowFlake |
| EATS | ICOST |
| ECC | EDW |
| EDW | CIBR |
| EDW | ICOST |
| FCA | ICOST |
| Finance HANA | APIGEE |
| Finance HANA | BOBJ |
| Finance HANA | SAP PO |
| ICOST | CFIN S/4 |
| IF S/4 | SideCar |
| Legacy MDG | SAP ECC |
| MARS | CIBR |
| MARS | ICOST |
| MyDeals | ICOST |
| OneMPS | ICOST |
| SAP ECC | EDW |
| SAP ECC | Finance HANA |
| SAP ECC | SideCar |
| SAP IBP | ADLS |
| SAP PO | SAP ECC |
| SDRA Demand | ICOST |
| SPAN | ICOST |
| SPEED-LEGACY | EDW |
| SPEED-LEGACY | SAP PO |
| SideCar | ADLS |
| SnOP | ICOST |
| Wafer Starts | ICOST |
| Workstream | MARS |
| XEUS | CIBR |
| XEUS | ICOST |


### 5.2 Integration Complexity Delta

Systems with connectivity changes (and top hub systems):

| System | Current Connections | Future Connections | Delta |
|---|:---:|:---:|:---:|
| ADLS | 3 | 0 | **-3** |
| APIGEE | 2 | 0 | **-2** |
| ATCR | 0 | 1 | **+1** |
| BOBJ | 1 | 0 | **-1** |
| BPC | 1 | 0 | **-1** |
| CFIN S/4 | 1 | 0 | **-1** |
| CFIN S/4 HANA | 0 | 4 | **+4** |
| CIBR | 7 | 0 | **-7** |
| COMPASS | 1 | 0 | **-1** |
| Capacity Forecast Data Store | 0 | 7 | **+7** |
| Corp / IP S/4 | 1 | 0 | **-1** |
| Corp / IP S/4 HANA | 0 | 6 | **+6** |
| DMOCR | 0 | 1 | **+1** |
| DXCR | 0 | 1 | **+1** |
| DataBricks | 2 | 0 | **-2** |
| EATS | 1 | 0 | **-1** |
| ECA-ADLS | 0 | 4 | **+4** |
| ECA-DataBricks | 0 | 2 | **+2** |
| ECA-SnowFlake | 0 | 11 | **+11** |
| ECC | 1 | 0 | **-1** |
| ECM (Windchill) | 0 | 1 | **+1** |
| EDW | 5 | 0 | **-5** |
| FCA | 1 | 0 | **-1** |
| FCS | 0 | 1 | **+1** |
| Finance HANA | 4 | 0 | **-4** |
| GraphiteConnect | 0 | 1 | **+1** |
| ICOST | 15 | 0 | **-15** |
| ICS (Phoenix) | 0 | 1 | **+1** |
| IF Blue Yonder | 0 | 1 | **+1** |
| IF PDH Consumptional | 0 | 2 | **+2** |
| IF PDH Foundational | 0 | 2 | **+2** |
| IF PDH Raw | 0 | 3 | **+3** |
| IF S/4 | 1 | 0 | **-1** |
| IF S/4 HANA | 0 | 8 | **+8** |
| IP Blue Yonder | 0 | 1 | **+1** |
| IP PDH Consumptional | 0 | 3 | **+3** |
| IP PDH Foundational | 0 | 3 | **+3** |
| IP PDH Raw | 0 | 2 | **+2** |
| Legacy MDG | 1 | 0 | **-1** |
| MARS | 4 | 2 | **-2** |
| MyDeals | 1 | 0 | **-1** |
| OneMPS | 1 | 0 | **-1** |
| PDF-SMH | 0 | 3 | **+3** |
| PDH Consumptional | 0 | 1 | **+1** |
| PDH Foundational | 0 | 1 | **+1** |
| PDH Raw | 0 | 1 | **+1** |
| PDM Translator | 0 | 3 | **+3** |
| PEGA | 1 | 0 | **-1** |
| Power BI (DARC) | 0 | 1 | **+1** |
| SAP Ariba | 0 | 2 | **+2** |
| SAP BOBJ | 0 | 1 | **+1** |
| SAP ECC | 6 | 0 | **-6** |
| SAP PAPM | 0 | 3 | **+3** |
| SAP PO | 4 | 0 | **-4** |
| SAP S/4 MDG | 0 | 4 | **+4** |
| SAP SAC | 0 | 4 | **+4** |
| SCS | 0 | 1 | **+1** |
| SDRA Demand | 1 | 0 | **-1** |
| SPAN | 2 | 0 | **-2** |
| SPEED | 0 | 2 | **+2** |
| SPEED-LEGACY | 2 | 0 | **-2** |
| SideCar | 4 | 5 | **+1** |
| SnOP | 1 | 0 | **-1** |
| SnowFlake | 1 | 0 | **-1** |
| WSPW | 0 | 1 | **+1** |
| Wafer Starts | 1 | 0 | **-1** |
| Workstream | 1 | 0 | **-1** |
| XEUS | 3 | 2 | **-1** |


### 5.3 Release-over-Release Changes

Changes between adjacent releases — additions and removals of applications, databases, and technology platforms. System lifecycle sourced from IAPM.

#### R1 -> R2

*No changes detected between releases.*

#### R2 -> R3

**Applications:**

| Change | Applications |
|---|---|
| **Added** | ATCR, CFIN S/4 HANA, Capacity Forecast Data Store, Corp / IP S/4 HANA, DMOCR, DXCR, ECA-ADLS, ECA-DataBricks, ECA-SnowFlake, ECM (Windchill), FCS, GraphiteConnect, ICS (Phoenix), IF Blue Yonder, IF PDH Consumptional, IF PDH Foundational, IF PDH Raw, IF S/4 HANA, IP Blue Yonder, IP PDH Consumptional, IP PDH Foundational, IP PDH Raw, MARS, MES 300, PDF-SMH, PDH Consumptional, PDH Foundational, PDH Raw, PDM Translator, Power BI (DARC), SAP Ariba, SAP BOBJ, SAP IBP, SAP PAPM, SAP S/4 MDG, SAP SAC, SCS, SPEED, SideCar, WSPW, WorkStream, XEUS |
| **Removed** | e.g. MES 300, e.g. XEUS |

**Databases:**

| Change | Databases |
|---|---|
| **Added** | Azure Analysis Services, Azure Data Lake (ADLS), Delta Lake, N/A (Middleware), N/A (SaaS), SAP HANA, SAP HANA Cloud, SQL Server, Snowflake Cloud DW |
| **Removed** | e.g. Azure SQL, e.g. SAP HANA |

**Technology Platforms:**

| Change | Platforms |
|---|---|
| **Added** | Blue Yonder Cloud SaaS, Databricks on ECA Azure Cloud, GraphiteConnect Cloud SaaS, Intel Custom On-Premise, Intel ECA Platform Azure Cloud, Intel ICS (Phoenix) On-Premise, Intel PDF-SMH Middleware On-Premise, Intel PDH On-Premise, Intel PDM On-Premise, Microsoft Power BI SaaS, PTC Windchill On-Premise, SAP Analytics Cloud SaaS, SAP Ariba Cloud SaaS, SAP BusinessObjects On-Premise, SAP HANA Sidecar On-Premise, SAP IBP Cloud SaaS, SAP MDG On-Premise, SAP PaPM On-Premise, SAP S/4HANA Central Finance, SAP S/4HANA On-Premise, Snowflake on ECA Cloud |
| **Removed** | e.g. Azure PaaS, e.g. S/4 HANA 2023 |

<div class="page-footer"><span>Page 7</span><span><a href="#toc">↑ Back to TOC</a></span><span>IAO Program Architecture Summary</span></div>
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
| 1 | R2A Option 1  Customer Requests Expedite - Service Fee with Existing SO | E2E · E2E-80 R2 Customer Requests Expedite | [E2E-80](/towers/E2E/E2E-80-R2-Customer-Requests-Expedite/E2E-80/output/docs/systems-architecture/E2E-80-Architecture.html) |
| 2 | E2E-08 | E2E · Forecast to Stock | [E2E-08](/towers/E2E/Forecast-to-Stock/E2E-08/output/docs/systems-architecture/E2E-08-Architecture.html) |
| 3 | IMR Flow | E2E · Forecast to Stock | [E2E-110](/towers/E2E/Forecast-to-Stock/E2E-110/output/docs/systems-architecture/E2E-110-Architecture.html) |
| 4 | R3 IMR Labs Process | E2E · Forecast to Stock | [E2E-113](/towers/E2E/Forecast-to-Stock/E2E-113/output/docs/systems-architecture/E2E-113-Architecture.html) |
| 5 | E2E-117 | E2E · Forecast to Stock | [E2E-117](/towers/E2E/Forecast-to-Stock/E2E-117/output/docs/systems-architecture/E2E-117-Architecture.html) |
| 6 | E2E-118 | E2E · Forecast to Stock | [E2E-118](/towers/E2E/Forecast-to-Stock/E2E-118/output/docs/systems-architecture/E2E-118-Architecture.html) |
| 7 | E2E-122 | E2E · Forecast to Stock | [E2E-122](/towers/E2E/Forecast-to-Stock/E2E-122/output/docs/systems-architecture/E2E-122-Architecture.html) |
| 8 | E2E-45 | E2E · Forecast to Stock | [E2E-45](/towers/E2E/Forecast-to-Stock/E2E-45/output/docs/systems-architecture/E2E-45-Architecture.html) |
| 9 | E2E-67 | E2E · Forecast to Stock | [E2E-67](/towers/E2E/Forecast-to-Stock/E2E-67/output/docs/systems-architecture/E2E-67-Architecture.html) |
| 10 | -Intel Foundry   NPI planning and execution processes | E2E · Forecast to Stock | [E2E-68](/towers/E2E/Forecast-to-Stock/E2E-68/output/docs/systems-architecture/E2E-68-Architecture.html) |
| 11 | E2E-71 | E2E · Forecast to Stock | [E2E-71](/towers/E2E/Forecast-to-Stock/E2E-71/output/docs/systems-architecture/E2E-71-Architecture.html) |
| 12 | IP | E2E · Forecast to Stock | [E2E-72](/towers/E2E/Forecast-to-Stock/E2E-72/output/docs/systems-architecture/E2E-72-Architecture.html) |
| 13 | R3 Hybrid Manufacturing process with external Wafer Procurement & Internal processing of | E2E · Forecast to Stock | [E2E-73](/towers/E2E/Forecast-to-Stock/E2E-73/output/docs/systems-architecture/E2E-73-Architecture.html) |
| 14 | R3 Internal manufacturing process for Finished Goods in Intel Foundry with Planning integrati | E2E · Forecast to Stock | [E2E-74](/towers/E2E/Forecast-to-Stock/E2E-74/output/docs/systems-architecture/E2E-74-Architecture.html) |
| 15 | Internal manufacturing process for Finished Goods in Intel Foundry with sales to External cus | E2E · Forecast to Stock | [E2E-76](/towers/E2E/Forecast-to-Stock/E2E-76/output/docs/systems-architecture/E2E-76-Architecture.html) |
| 16 | Intel Foundry - Inventory Transfer  Shipment of goods through Stock transfer (Interim State) | E2E · Forecast to Stock | [E2E-84](/towers/E2E/Forecast-to-Stock/E2E-84/output/docs/systems-architecture/E2E-84-Architecture.html) |
| 17 | R3 Intel Foundry Maintenance process through spare parts (SWAP) | E2E · Forecast to Stock | [E2E-94](/towers/E2E/Forecast-to-Stock/E2E-94/output/docs/systems-architecture/E2E-94-Architecture.html) |
| 18 | R3 Customer Master Data | E2E · Master Data | [E2E-89](/towers/E2E/Master-Data/E2E-89/output/docs/systems-architecture/E2E-89-Architecture.html) |
| 19 | R3 Material Master Data | E2E · Master Data | [E2E-90](/towers/E2E/Master-Data/E2E-90/output/docs/systems-architecture/E2E-90-Architecture.html) |
| 20 | R3 Bill of Material BOM Data | E2E · Master Data | [E2E-91](/towers/E2E/Master-Data/E2E-91/output/docs/systems-architecture/E2E-91-Architecture.html) |
| 21 | R3 Vendor Master Data | E2E · Master Data | [E2E-92](/towers/E2E/Master-Data/E2E-92/output/docs/systems-architecture/E2E-92-Architecture.html) |
| 22 | IF Simplified PO-SO Model | E2E · Order to Cash | [IF_Simplified_PO-SO_Model](/towers/E2E/Order-to-Cash/IF_Simplified_PO-SO_Model/output/docs/systems-architecture/IF_Simplified_PO-SO_Model-Architecture.html) |
| 23 | Order to Cash (IF) | E2E · Order to Cash | [Order_to_Cash_IF](/towers/E2E/Order-to-Cash/Order_to_Cash_IF/output/docs/systems-architecture/Order_to_Cash_IF-Architecture.html) |
| 24 | Order to Cash (IP) | E2E · Order to Cash | [Order_to_Cash_IP](/towers/E2E/Order-to-Cash/Order_to_Cash_IP/output/docs/systems-architecture/Order_to_Cash_IP-Architecture.html) |
| 25 | R3 - Purchase Requisition to Payments for Direct procurement with Planning Integration (Box | E2E · Procure to Pay | [E2E-100](/towers/E2E/Procure-to-Pay/E2E-100/output/docs/systems-architecture/E2E-100-Architecture.html) |
| 26 | R3 Procurement of WIINGS Replacement Related Commodities | E2E · Procure to Pay | [E2E-103](/towers/E2E/Procure-to-Pay/E2E-103/output/docs/systems-architecture/E2E-103-Architecture.html) |
| 27 | R3 - Partner Owned Equipment Order | E2E · Procure to Pay | [E2E-107](/towers/E2E/Procure-to-Pay/E2E-107/output/docs/systems-architecture/E2E-107-Architecture.html) |
| 28 | R3 Raw Silicon Procurement | E2E · Procure to Pay | [E2E-112](/towers/E2E/Procure-to-Pay/E2E-112/output/docs/systems-architecture/E2E-112-Architecture.html) |
| 29 | R4 SIMS Harvest Process | E2E · Procure to Pay | [E2E-114](/towers/E2E/Procure-to-Pay/E2E-114/output/docs/systems-architecture/E2E-114-Architecture.html) |
| 30 | R3 Inter-company Asset Transfer Process | E2E · Procure to Pay | [E2E-115](/towers/E2E/Procure-to-Pay/E2E-115/output/docs/systems-architecture/E2E-115-Architecture.html) |
| 31 | R3 Wafer Reclaim Process | E2E · Procure to Pay | [E2E-116](/towers/E2E/Procure-to-Pay/E2E-116/output/docs/systems-architecture/E2E-116-Architecture.html) |
| 32 | R3 Shipping Rejects Inventory Movement | E2E · Procure to Pay | [E2E-119](/towers/E2E/Procure-to-Pay/E2E-119/output/docs/systems-architecture/E2E-119-Architecture.html) |
| 33 | R3 RM Bailed Inventory Movement (Straddle) | E2E · Procure to Pay | [E2E-121](/towers/E2E/Procure-to-Pay/E2E-121/output/docs/systems-architecture/E2E-121-Architecture.html) |
| 34 | TD Substrates Manufacturing Process | E2E · Procure to Pay | [E2E-123](/towers/E2E/Procure-to-Pay/E2E-123/output/docs/systems-architecture/E2E-123-Architecture.html) |
| 35 | R3 Sourcing Request-Project to Contracts for Direct-Capital on Ariba with Pricing Updates | E2E · Procure to Pay | [E2E-40](/towers/E2E/Procure-to-Pay/E2E-40/output/docs/systems-architecture/E2E-40-Architecture.html) |
| 36 | R3 Sourcing Request | E2E · Procure to Pay | [E2E-41](/towers/E2E/Procure-to-Pay/E2E-41/output/docs/systems-architecture/E2E-41-Architecture.html) |
| 37 | Process Procurement Card Invoice | E2E · Procure to Pay | [E2E-43](/towers/E2E/Procure-to-Pay/E2E-43/output/docs/systems-architecture/E2E-43-Architecture.html) |
| 38 | R3 - Intel Owned Consignment with Planning Integration | E2E · Procure to Pay | [E2E-44](/towers/E2E/Procure-to-Pay/E2E-44/output/docs/systems-architecture/E2E-44-Architecture.html) |
| 39 | R3 Direct procurement with Planning Integration-AT | E2E · Procure to Pay | [E2E-46](/towers/E2E/Procure-to-Pay/E2E-46/output/docs/systems-architecture/E2E-46-Architecture.html) |
| 40 | Purchase Requisition to Payments for Direct procurement with planning integration - Fab Mater | E2E · Procure to Pay | [E2E-47](/towers/E2E/Procure-to-Pay/E2E-47/output/docs/systems-architecture/E2E-47-Architecture.html) |
| 41 | R3 Purchase Requisition to Payments for procurement with financial planning and asset managem | E2E · Procure to Pay | [E2E-49](/towers/E2E/Procure-to-Pay/E2E-49/output/docs/systems-architecture/E2E-49-Architecture.html) |
| 42 | Purchase Requisition to Payments for Indirect - Construction (Small Construction IPCS, Mainte | E2E · Procure to Pay | [E2E-50](/towers/E2E/Procure-to-Pay/E2E-50/output/docs/systems-architecture/E2E-50-Architecture.html) |
| 43 | Purchase Requisition to Payments for Indirect Materials (Non-IPN and Non-Inventoried) ​ | E2E · Procure to Pay | [E2E-51](/towers/E2E/Procure-to-Pay/E2E-51/output/docs/systems-architecture/E2E-51-Architecture.html) |
| 44 | Purchase Requisition to Payments for Indirect Non-Mfg. &amp; Mfg. procurement | E2E · Procure to Pay | [E2E-52](/towers/E2E/Procure-to-Pay/E2E-52/output/docs/systems-architecture/E2E-52-Architecture.html) |
| 45 | Purchase Requisition to Payments for Indirect procurement (simple material or services like H | E2E · Procure to Pay | [E2E-53](/towers/E2E/Procure-to-Pay/E2E-53/output/docs/systems-architecture/E2E-53-Architecture.html) |
| 46 | R3 Subcontracting with Planning integration- Foundry,OSAT,ODM | E2E · Procure to Pay | [E2E-57](/towers/E2E/Procure-to-Pay/E2E-57/output/docs/systems-architecture/E2E-57-Architecture.html) |
| 47 | R3 Rework Re-localization in Factory​ | E2E · Procure to Pay | [E2E-59](/towers/E2E/Procure-to-Pay/E2E-59/output/docs/systems-architecture/E2E-59-Architecture.html) |
| 48 | R3 Consignment Material - Vendor | E2E · Procure to Pay | [E2E-61](/towers/E2E/Procure-to-Pay/E2E-61/output/docs/systems-architecture/E2E-61-Architecture.html) |
| 49 | R3 Vendor Return for Direct Material | E2E · Procure to Pay | [E2E-62](/towers/E2E/Procure-to-Pay/E2E-62/output/docs/systems-architecture/E2E-62-Architecture.html) |
| 50 | R3 - Substrates - (PTP) PR to PO scope for Internal Manufacturing (Intel Foundry) & Exte | E2E · Procure to Pay | [E2E-70](/towers/E2E/Procure-to-Pay/E2E-70/output/docs/systems-architecture/E2E-70-Architecture.html) |
| 51 | R3 Construction materials & equipment procurement process inclusive of OFCI (Like equipme | E2E · Procure to Pay | [E2E-88](/towers/E2E/Procure-to-Pay/E2E-88/output/docs/systems-architecture/E2E-88-Architecture.html) |
| 52 | R3 Straddle & R4 SIMS Design with Returns | E2E · Procure to Pay | [E2E-96](/towers/E2E/Procure-to-Pay/E2E-96/output/docs/systems-architecture/E2E-96-Architecture.html) |
| 53 | R3 Equipment Product Supporting Items (PSI) Procurement | E2E · Procure to Pay | [E2E-98](/towers/E2E/Procure-to-Pay/E2E-98/output/docs/systems-architecture/E2E-98-Architecture.html) |
| 54 | Perform Transaction Processing | FPR · DC Manage Accounting and Control Data | [DC-010](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-010/output/docs/systems-architecture/DC-010-Architecture.html) |
| 55 | Manage the General Ledger | FPR · DC Manage Accounting and Control Data | [DC-020](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-020/output/docs/systems-architecture/DC-020-Architecture.html) |
| 56 | Perform Closing | FPR · DC Manage Accounting and Control Data | [DC-030](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-030/output/docs/systems-architecture/DC-030-Architecture.html) |
| 57 | Perform Fixed Asset Accounting | FPR · DC Manage Accounting and Control Data | [DC-040](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-040/output/docs/systems-architecture/DC-040-Architecture.html) |
| 58 | Project Accounting | FPR · DC Manage Accounting and Control Data | [DC-050](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-050/output/docs/systems-architecture/DC-050-Architecture.html) |
| 59 | Manage Taxes | FPR · DC Manage Accounting and Control Data | [DC-060](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-060/output/docs/systems-architecture/DC-060-Architecture.html) |
| 60 | Revenue Recognition | FPR · DC Manage Accounting and Control Data | [DC-100](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-100/output/docs/systems-architecture/DC-100-Architecture.html) |
| 61 | Manage Intercompany | FPR · DC Manage Accounting and Control Data | [DC-110](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-110/output/docs/systems-architecture/DC-110-Architecture.html) |
| 62 | Maintenance & Management Accounting | FPR · DC Manage Accounting and Control Data | [DC-120](/towers/FPR/DC-Manage-Accounting-and-Control-Data/DC-120/output/docs/systems-architecture/DC-120-Architecture.html) |
| 63 | Perform Overhead Accounting and Allocation | FPR · DS Provide Decision Support | [DS-010](/towers/FPR/DS-Provide-Decision-Support/DS-010/output/docs/systems-architecture/DS-010-Architecture.html) |
| 64 | Perform Product Costing and Inventory Valuation | FPR · DS Provide Decision Support | [DS-020](/towers/FPR/DS-Provide-Decision-Support/DS-020/output/docs/systems-architecture/DS-020-Architecture.html) |
| 65 | Perform Customer and Product Profitability Analysis | FPR · DS Provide Decision Support | [DS-030](/towers/FPR/DS-Provide-Decision-Support/DS-030/output/docs/systems-architecture/DS-030-Architecture.html) |
| 66 | Plan the Business | FPR · MB Plan and Manage Business | [MB-060](/towers/FPR/MB-Plan-and-Manage-Business/MB-060/output/docs/systems-architecture/MB-060-Architecture.html) |
| 67 | Prepare Budgets | FPR · MB Plan and Manage Business | [MB-070](/towers/FPR/MB-Plan-and-Manage-Business/MB-070/output/docs/systems-architecture/MB-070-Architecture.html) |
| 68 | Manage Liquidity | FPR · MR Manage Capital and Risk | [MR-010](/towers/FPR/MR-Manage-Capital-and-Risk/MR-010/output/docs/systems-architecture/MR-010-Architecture.html) |
| 69 | Manage Capital Structure | FPR · MR Manage Capital and Risk | [MR-020](/towers/FPR/MR-Manage-Capital-and-Risk/MR-020/output/docs/systems-architecture/MR-020-Architecture.html) |
| 70 | Manage Financial Risk | FPR · MR Manage Capital and Risk | [MR-030](/towers/FPR/MR-Manage-Capital-and-Risk/MR-030/output/docs/systems-architecture/MR-030-Architecture.html) |
| 71 | In-House Banking | FPR · MR Manage Capital and Risk | [MR-070](/towers/FPR/MR-Manage-Capital-and-Risk/MR-070/output/docs/systems-architecture/MR-070-Architecture.html) |
| 72 | Process Receipts | FPR · OR Receivables Management | [OR-140](/towers/FPR/OR-Receivables-Management/OR-140/output/docs/systems-architecture/OR-140-Architecture.html) |
| 73 | Receive and Put-away Product - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | [L-040](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-040/output/docs/systems-architecture/L-040-Architecture.html) |
| 74 | Manage Storage & Internal Movement of Inventory - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | [L-060](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-060/output/docs/systems-architecture/L-060-Architecture.html) |
| 75 | Manage Lots Batches - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | [L-110](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-110/output/docs/systems-architecture/L-110-Architecture.html) |
| 76 | Manage Line Replenishment - FTS (IF) | FTS-IF · L Logistics and Inventory Management - FTS (IF) | [L-120](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/L-120/output/docs/systems-architecture/L-120-Architecture.html) |
| 77 | Receive Materials and Services - FTS (IF) | FTS-IF · LI Logistics Management Inbound - FTS (IF) | [LI-120](/towers/FTS-IF/LI-Logistics-Management-Inbound---FTS-(IF)/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) |
| 78 | Pick Orders- FTS (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | [LO-160](/towers/FTS-IF/LO-Logistics-Management-Outbound---FTS-(IF)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) |
| 79 | Pack Order - FTS  (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | [LO-170](/towers/FTS-IF/LO-Logistics-Management-Outbound---FTS-(IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) |
| 80 | Manage Outbound Transportation - FTS (IF) | FTS-IF · LO Logistics Management Outbound - FTS (IF) | [LO-180](/towers/FTS-IF/LO-Logistics-Management-Outbound---FTS-(IF)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) |
| 81 | Ship | FTS-IF · LO Logistics Management Outbound - FTS (IF) | [LO-190](/towers/FTS-IF/L-Logistics-and-Inventory-Management---FTS-(IF)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) |
| 82 | Perform Materials Requirement Planning (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | [M-080](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-080/output/docs/systems-architecture/M-080-Architecture.html) |
| 83 | Schedule Production (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | [M-090](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-090/output/docs/systems-architecture/M-090-Architecture.html) |
| 84 | Execute Production (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | [M-100](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-100/output/docs/systems-architecture/M-100-Architecture.html) |
| 85 | Control and Report Production Operations (IF) | FTS-IF · M Mfg. Schedule and Execution (IF) | [M-170](/towers/FTS-IF/M-Mfg.-Schedule-and-Execution-(IF)/M-170/output/docs/systems-architecture/M-170-Architecture.html) |
| 86 | Identify Maintenance Structure | FTS-IF · PE Manage Plant, Equipment and Facilities | [PE-020](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-020/output/docs/systems-architecture/PE-020-Architecture.html) |
| 87 | Monitor | FTS-IF · PE Manage Plant, Equipment and Facilities | [PE-040](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-040/output/docs/systems-architecture/PE-040-Architecture.html) |
| 88 | Maintain Work Order Historical Documentation | FTS-IF · PE Manage Plant, Equipment and Facilities | [PE-050](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-050/output/docs/systems-architecture/PE-050-Architecture.html) |
| 89 | Maintain and Manage Master Maintenance Records | FTS-IF · PE Manage Plant, Equipment and Facilities | [PE-060](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-060/output/docs/systems-architecture/PE-060-Architecture.html) |
| 90 | Identify and Plan Plant Maintenance | FTS-IF · PE Manage Plant, Equipment and Facilities | [PE-070](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-070/output/docs/systems-architecture/PE-070-Architecture.html) |
| 91 | Execute Plant Maintenance | FTS-IF · PE Manage Plant, Equipment and Facilities | [PE-090](/towers/FTS-IF/PE-Manage-Plant,-Equipment-and-Facilities-(IF)/PE-090/output/docs/systems-architecture/PE-090-Architecture.html) |
| 92 | Supply Planning & Management (IF) | FTS-IF · PLB Supply Chain Planning (IF) | [PLB-020](/towers/FTS-IF/PLB-Supply-Chain-Planning-(IF)/PLB-020/output/docs/systems-architecture/PLB-020-Architecture.html) |
| 93 | Manage Product Disposition (IF) | FTS-IF · Q Quality Management (IF) | [Q-140](/towers/FTS-IF/Q-Quality-Management-(IF)/Q-140/output/docs/systems-architecture/Q-140-Architecture.html) |
| 94 | Manage Storage and Internal Movement of Inventory - FTS (IP) | FTS-IP · L Logistics and Inventory Management - FTS (IP) | [L-060](/towers/FTS-IP/L-Logistics-and-Inventory-Management---FTS-(IP)/L-060/output/docs/systems-architecture/L-060-Architecture.html) |
| 95 | Receive Materials and Services - FTS (IP) | FTS-IP · LI Logistics Management Inbound - FTS (IP) | [LI-120](/towers/FTS-IP/LI-Logistics-Management-Inbound---FTS-(IP)/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) |
| 96 | Pick Orders - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | [LO-160](/towers/FTS-IP/LO-Logistics-Management-Outbound---FTS-(IP)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) |
| 97 | Pack Orders - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | [LO-170](/towers/FTS-IP/LO-Logistics-Management-Outbound---FTS-(IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) |
| 98 | Manage Outbound Transportation - FTS (IP) | FTS-IP · LO Logistics Management Outbound - FTS (IP) | [LO-180](/towers/FTS-IP/L-Logistics-and-Inventory-Management---FTS-(IP)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) |
| 99 | Ship | FTS-IP · LO Logistics Management Outbound - FTS (IP) | [LO-190](/towers/FTS-IP/LO-Logistics-Management-Outbound---FTS-(IP)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) |
| 100 | Perform Materials Requirement Planning (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | [M-080](/towers/FTS-IP/M-Mfg.-Schedule-and-Execution-(IP)/M-080/output/docs/systems-architecture/M-080-Architecture.html) |
| 101 | Schedule Production (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | [M-090](/towers/FTS-IP/M-Mfg.-Schedule-and-Execution-(IP)/M-090/output/docs/systems-architecture/M-090-Architecture.html) |
| 102 | Execute Production (IP) | FTS-IP · M Mfg. Schedule and Execution (IP) | [M-100](/towers/FTS-IP/M-Mfg.-Schedule-and-Execution-(IP)/M-100/output/docs/systems-architecture/M-100-Architecture.html) |
| 103 | Supply Planning & Management (IP) | FTS-IP · PLB Supply Chain Planning (IP) | [PLB-020](/towers/FTS-IP/PLB-Supply-Chain-Planning-(IP)/PLB-020/output/docs/systems-architecture/PLB-020-Architecture.html) |
| 104 | Responsive Demand and Supply Matching (RDSM) (IP) | FTS-IP · PLB Supply Chain Planning (IP) | [PLB-050](/towers/FTS-IP/PLB-Supply-Chain-Planning-(IP)/PLB-050/output/docs/systems-architecture/PLB-050-Architecture.html) |
| 105 | Manage Product Disposition (IP) | FTS-IP · Q Quality Management (IP) | [Q-140](/towers/FTS-IP/Q-Quality-Management-(IP)/Q-140/output/docs/systems-architecture/Q-140-Architecture.html) |
| 106 | Create and Maintain Vendors | MDM · MDM-Manage Master Data | [MDM-020](/towers/MDM/MDM-Manage-Master-Data/MDM-020/output/docs/systems-architecture/MDM-020-Architecture.html) |
| 107 | Create and Maintain Customers | MDM · MDM-Manage Master Data | [MDM-130](/towers/MDM/MDM-Manage-Master-Data/MDM-130/output/docs/systems-architecture/MDM-130-Architecture.html) |
| 108 | Create and Maintain Reference Data | MDM · MDM-Manage Master Data | [MDM-140](/towers/MDM/MDM-Manage-Master-Data/MDM-140/output/docs/systems-architecture/MDM-140-Architecture.html) |
| 109 | Maintain Product Related Data | MDM · MDM-Manage Master Data | [MDM-150](/towers/MDM/MDM-Manage-Master-Data/MDM-150/output/docs/systems-architecture/MDM-150-Architecture.html) |
| 110 | Billing Revenue (IF) | OTC-IF · BR-Billing and Rebates (IF) | [BR-130](/towers/OTC-IF/BR-Billing-and-Rebates-(IF)/BR-130/output/docs/systems-architecture/BR-130-Architecture.html) |
| 111 | Manage Customer Credit Exposure (IF) | OTC-IF · CM-Credit and Collections Management (IF) | [CM-050](/towers/OTC-IF/CM-Credit-and-Collections-Management-(IF)/CM-050/output/docs/systems-architecture/CM-050-Architecture.html) |
| 112 | Manage Collections (IF) | OTC-IF · CM-Credit and Collections Management (IF) | [CM-060](/towers/OTC-IF/CM-Credit-and-Collections-Management-(IF)/CM-060/output/docs/systems-architecture/CM-060-Architecture.html) |
| 113 | Manage Global Trade Master Data (IF) | OTC-IF · GT Global Trade (IF) | [GT-010](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-010/output/docs/systems-architecture/GT-010-Architecture.html) |
| 114 | Product Classification (IF) | OTC-IF · GT Global Trade (IF) | [GT-020](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-020/output/docs/systems-architecture/GT-020-Architecture.html) |
| 115 | Compliance Screening (IF) | OTC-IF · GT Global Trade (IF) | [GT-030](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-030/output/docs/systems-architecture/GT-030-Architecture.html) |
| 116 | Manage Licenses (IF) | OTC-IF · GT Global Trade (IF) | [GT-040](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-040/output/docs/systems-architecture/GT-040-Architecture.html) |
| 117 | Customs declaration creation Export (IF) | OTC-IF · GT Global Trade (IF) | [GT-050](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-050/output/docs/systems-architecture/GT-050-Architecture.html) |
| 118 | Customs Declaration Completion Export | OTC-IF · GT Global Trade (IF) | [GT-070](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-070/output/docs/systems-architecture/GT-070-Architecture.html) |
| 119 | Customs Declaration Communication - Self Filing (IF) | OTC-IF · GT Global Trade (IF) | [GT-080](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-080/output/docs/systems-architecture/GT-080-Architecture.html) |
| 120 | Monitor completed declaration (IF) | OTC-IF · GT Global Trade (IF) | [GT-110](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-110/output/docs/systems-architecture/GT-110-Architecture.html) |
| 121 | Intrastat Filing (S4) (IF) | OTC-IF · GT Global Trade (IF) | [GT-130](/towers/OTC-IF/GT-Global-Trade-(IF)/GT-130/output/docs/systems-architecture/GT-130-Architecture.html) |
| 122 | Pick Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | [LO-160](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) |
| 123 | Pack Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | [LO-170](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) |
| 124 | Manage Outbound Transportation - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | [LO-180](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) |
| 125 | Ship Deliver Orders - OTC (IF) | OTC-IF · LO Logistics Management Outbound - OTC (IF) | [LO-190](/towers/OTC-IF/LO-Logistics-Management-Outbound---OTC-(IF)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) |
| 126 | Capture Orders (IF) | OTC-IF · O-Order Management (IF) | [O-020](/towers/OTC-IF/O-Order-Management-(IF)/O-020/output/docs/systems-architecture/O-020-Architecture.html) |
| 127 | Process Orders (IF) | OTC-IF · O-Order Management (IF) | [O-030](/towers/OTC-IF/O-Order-Management-(IF)/O-030/output/docs/systems-architecture/O-030-Architecture.html) |
| 128 | Calculate Order Price (IF) | OTC-IF · O-Order Management (IF) | [O-040](/towers/OTC-IF/O-Order-Management-(IF)/O-040/output/docs/systems-architecture/O-040-Architecture.html) |
| 129 | Manage and Track Orders (IF) | OTC-IF · O-Order Management (IF) | [O-060](/towers/OTC-IF/O-Order-Management-(IF)/O-060/output/docs/systems-architecture/O-060-Architecture.html) |
| 130 | Manage Backorders (IF) | OTC-IF · O-Order Management (IF) | [O-070](/towers/OTC-IF/O-Order-Management-(IF)/O-070/output/docs/systems-architecture/O-070-Architecture.html) |
| 131 | Manage Returns and Exchanges (IF) | OTC-IF · R-Returns (IF) | [R-190](/towers/OTC-IF/R-Returns-(IF)/R-190/output/docs/systems-architecture/R-190-Architecture.html) |
| 132 | Return - Receive Materials and Services (IF) | OTC-IF · R-Returns (IF) | [R-200](/towers/OTC-IF/R-Returns-(IF)/R-200/output/docs/systems-architecture/R-200-Architecture.html) |
| 133 | Returns - Determine Discrepant Material Disposition (IF) | OTC-IF · R-Returns (IF) | [R-210](/towers/OTC-IF/R-Returns-(IF)/R-210/output/docs/systems-architecture/R-210-Architecture.html) |
| 134 | Returns - Manage In-bound Transportation (IF) | OTC-IF · R-Returns (IF) | [R-220](/towers/OTC-IF/R-Returns-(IF)/R-220/output/docs/systems-architecture/R-220-Architecture.html) |
| 135 | Billing Revenue (IP) | OTC-IP · BR-Billing and Rebates (IP) | [BR-130](/towers/OTC-IP/BR-Billing-and-Rebates-(IP)/BR-130/output/docs/systems-architecture/BR-130-Architecture.html) |
| 136 | Manage Rebates (IP) | OTC-IP · BR-Billing and Rebates (IP) | [BR-160](/towers/OTC-IP/BR-Billing-and-Rebates-(IP)/BR-160/output/docs/systems-architecture/BR-160-Architecture.html) |
| 137 | Manage Chargebacks (IP) | OTC-IP · BR-Billing and Rebates (IP) | [BR-170](/towers/OTC-IP/BR-Billing-and-Rebates-(IP)/BR-170/output/docs/systems-architecture/BR-170-Architecture.html) |
| 138 | Manage Customer Credit Exposure (IP) | OTC-IP · CM-Credit and Collections Management (IP) | [CM-050](/towers/OTC-IP/CM-Credit-and-Collections-Management-(IP)/CM-050/output/docs/systems-architecture/CM-050-Architecture.html) |
| 139 | Manage Collections (IP) | OTC-IP · CM-Credit and Collections Management (IP) | [CM-060](/towers/OTC-IP/CM-Credit-and-Collections-Management-(IP)/CM-060/output/docs/systems-architecture/CM-060-Architecture.html) |
| 140 | Manage Global Trade Master Data (IP) | OTC-IP · GT-Global Trade (IP) | [GT-010](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-010/output/docs/systems-architecture/GT-010-Architecture.html) |
| 141 | Product Classification (IP) | OTC-IP · GT-Global Trade (IP) | [GT-020](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-020/output/docs/systems-architecture/GT-020-Architecture.html) |
| 142 | Compliance Screening (IP) | OTC-IP · GT-Global Trade (IP) | [GT-030](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-030/output/docs/systems-architecture/GT-030-Architecture.html) |
| 143 | Manage Licenses (IP) | OTC-IP · GT-Global Trade (IP) | [GT-040](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-040/output/docs/systems-architecture/GT-040-Architecture.html) |
| 144 | Customs Declaration Creation Export (IP) | OTC-IP · GT-Global Trade (IP) | [GT-050](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-050/output/docs/systems-architecture/GT-050-Architecture.html) |
| 145 | Customs declaration creation Import (IP) | OTC-IP · GT-Global Trade (IP) | [GT-060](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-060/output/docs/systems-architecture/GT-060-Architecture.html) |
| 146 | Customs Declaration Completion Export | OTC-IP · GT-Global Trade (IP) | [GT-070](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-070/output/docs/systems-architecture/GT-070-Architecture.html) |
| 147 | Customs Declaration Communication - Self Filing (IP) | OTC-IP · GT-Global Trade (IP) | [GT-080](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-080/output/docs/systems-architecture/GT-080-Architecture.html) |
| 148 | Customs declaration communication - broker filing (IP) | OTC-IP · GT-Global Trade (IP) | [GT-090](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-090/output/docs/systems-architecture/GT-090-Architecture.html) |
| 149 | Monitor Completed Declaration (IP) | OTC-IP · GT-Global Trade (IP) | [GT-110](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-110/output/docs/systems-architecture/GT-110-Architecture.html) |
| 150 | Intrastat Filing (S4) (IP) | OTC-IP · GT-Global Trade (IP) | [GT-130](/towers/OTC-IP/GT-Global-Trade-(IP)/GT-130/output/docs/systems-architecture/GT-130-Architecture.html) |
| 151 | Pick Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | [LO-160](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-160/output/docs/systems-architecture/LO-160-Architecture.html) |
| 152 | Pack Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | [LO-170](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-170/output/docs/systems-architecture/LO-170-Architecture.html) |
| 153 | Manage Outbound Transportation - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | [LO-180](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-180/output/docs/systems-architecture/LO-180-Architecture.html) |
| 154 | Ship Deliver Orders - OTC (IP) | OTC-IP · LO Logistics Management Outbound - OTC (IP) | [LO-190](/towers/OTC-IP/LO-Logistics-Management-Outbound---OTC-(IP)/LO-190/output/docs/systems-architecture/LO-190-Architecture.html) |
| 155 | Capture Orders (IP) | OTC-IP · O-Order Management (IP) | [O-020](/towers/OTC-IP/O-Order-Management-(IP)/O-020/output/docs/systems-architecture/O-020-Architecture.html) |
| 156 | Process Orders (IP) | OTC-IP · O-Order Management (IP) | [O-030](/towers/OTC-IP/O-Order-Management-(IP)/O-030/output/docs/systems-architecture/O-030-Architecture.html) |
| 157 | Calculate Order Price (IP) | OTC-IP · O-Order Management (IP) | [O-040](/towers/OTC-IP/O-Order-Management-(IP)/O-040/output/docs/systems-architecture/O-040-Architecture.html) |
| 158 | Manage and Track Orders (IP) | OTC-IP · O-Order Management (IP) | [O-060](/towers/OTC-IP/O-Order-Management-(IP)/O-060/output/docs/systems-architecture/O-060-Architecture.html) |
| 159 | Manage Backorders (IP) | OTC-IP · O-Order Management (IP) | [O-070](/towers/OTC-IP/O-Order-Management-(IP)/O-070/output/docs/systems-architecture/O-070-Architecture.html) |
| 160 | Manage Returns and Exchanges (IP) | OTC-IP · R-Returns (IP) | [R-190](/towers/OTC-IP/R-Returns-(IP)/R-190/output/docs/systems-architecture/R-190-Architecture.html) |
| 161 | Return - Receive Materials and Services (IP) | OTC-IP · R-Returns (IP) | [R-200](/towers/OTC-IP/R-Returns-(IP)/R-200/output/docs/systems-architecture/R-200-Architecture.html) |
| 162 | Returns - Manage In-bound Transportation (IP) | OTC-IP · R-Returns (IP) | [R-220](/towers/OTC-IP/R-Returns-(IP)/R-220/output/docs/systems-architecture/R-220-Architecture.html) |
| 163 | Returns - Manage Storage & Internal Movement of Inventory (IP) | OTC-IP · R-Returns (IP) | [R-230](/towers/OTC-IP/R-Returns-(IP)/R-230/output/docs/systems-architecture/R-230-Architecture.html) |
| 164 | Returns - Manage Storage & Internal Movement of Inventory (IP) | OTC-IP · R-Returns (IP) | [R-240](/towers/OTC-IP/R-Returns-(IP)/R-240/output/docs/systems-architecture/R-240-Architecture.html) |
| 165 | Returns - Receive and Put-away Product (IP) | OTC-IP · R-Returns (IP) | [R-250](/towers/OTC-IP/R-Returns-(IP)/R-250/output/docs/systems-architecture/R-250-Architecture.html) |
| 166 | Returns - Pick Orders (IP) | OTC-IP · R-Returns (IP) | [R-260](/towers/OTC-IP/R-Returns-(IP)/R-260/output/docs/systems-architecture/R-260-Architecture.html) |
| 167 | Returns - Pack Orders (IP) | OTC-IP · R-Returns (IP) | [R-270](/towers/OTC-IP/R-Returns-(IP)/R-270/output/docs/systems-architecture/R-270-Architecture.html) |
| 168 | Returns - Ship Orders (IP) | OTC-IP · R-Returns (IP) | [R-280](/towers/OTC-IP/R-Returns-(IP)/R-280/output/docs/systems-architecture/R-280-Architecture.html) |
| 169 | Returns - Manage Lots | OTC-IP · R-Returns (IP) | [R-290](/towers/OTC-IP/R-Returns-(IP)/R-290/output/docs/systems-architecture/R-290-Architecture.html) |
| 170 | Receive and Put-away Product - PTP | PTP · L Logistics and Inventory Management - PTP | [L-040](/towers/PTP/L-Logistics-and-Inventory-Management---PTP/L-040/output/docs/systems-architecture/L-040-Architecture.html) |
| 171 | Manage Storage and Internal Movement of Inventory - PTP | PTP · L Logistics and Inventory Management - PTP | [L-060](/towers/PTP/L-Logistics-and-Inventory-Management---PTP/L-060/output/docs/systems-architecture/L-060-Architecture.html) |
| 172 | Manage Lots Batches - PTP | PTP · L Logistics and Inventory Management - PTP | [L-110](/towers/PTP/L-Logistics-and-Inventory-Management---PTP/L-110/output/docs/systems-architecture/L-110-Architecture.html) |
| 173 | Manage In-bound Transportation - PTP | PTP · LI Logistics Management Inbound - PTP | [LI-030](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-030/output/docs/systems-architecture/LI-030-Architecture.html) |
| 174 | Manage Supplier Consignment Stock | PTP · LI Logistics Management Inbound - PTP | [LI-100](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-100/output/docs/systems-architecture/LI-100-Architecture.html) |
| 175 | Receive Materials and Services - PTP | PTP · LI Logistics Management Inbound - PTP | [LI-120](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-120/output/docs/systems-architecture/LI-120-Architecture.html) |
| 176 | Determine Discrepant Material Disposition | PTP · LI Logistics Management Inbound - PTP | [LI-200](/towers/PTP/LI-Logistics-Management-Inbound---PTP/LI-200/output/docs/systems-architecture/LI-200-Architecture.html) |
| 177 | Maintain Supplier Certification and Monitor Performance | PTP · PM-Procure Materials and Services (Direct and Indirect) | [PM-040](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-040/output/docs/systems-architecture/PM-040-Architecture.html) |
| 178 | Manage Quotation | PTP · PM-Procure Materials and Services (Direct and Indirect) | [PM-050](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-050/output/docs/systems-architecture/PM-050-Architecture.html) |
| 179 | Create and Maintain Purchase Requisitions | PTP · PM-Procure Materials and Services (Direct and Indirect) | [PM-070](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-070/output/docs/systems-architecture/PM-070-Architecture.html) |
| 180 | Purchase Materials and Services | PTP · PM-Procure Materials and Services (Direct and Indirect) | [PM-080](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-080/output/docs/systems-architecture/PM-080-Architecture.html) |
| 181 | Manage Contracts | PTP · PM-Procure Materials and Services (Direct and Indirect) | [PM-090](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-090/output/docs/systems-architecture/PM-090-Architecture.html) |
| 182 | Procure Subcontracting | PTP · PM-Procure Materials and Services (Direct and Indirect) | [PM-110](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-110/output/docs/systems-architecture/PM-110-Architecture.html) |
| 183 | Enable Payment | PTP · PM-Procure Materials and Services (Direct and Indirect) | [PM-150](/towers/PTP/PM-Procure-Materials-and-Services-(Direct-and-Indirect)/PM-150/output/docs/systems-architecture/PM-150-Architecture.html) |
| 184 | Perform Incoming Quality Assurance | PTP · QI-Quality Management (Incoming) | [QI-130](/towers/PTP/QI-Quality-Management-(Incoming)/QI-130/output/docs/systems-architecture/QI-130-Architecture.html) |

