# Salsabila Amin Operations & Treasury Management

Official operations, automated document processing, and SAP FI/AR reconciliation workflow repository for **S.R. Electronics Park** (Authorized Dealer for Butterfly Marketing Limited and Minister-Myone Group).

---

## 🏢 Business Entity & Governance

* **Entity Name:** S.R. Electronics Park
* **Proprietor:** MD. AL AMIN SOHAG
* **Parent Principals:** Butterfly Marketing Limited & Minister-Myone Group
* **Dealer Codes:** 
  * **Minister-Myone Group:** `DEAL002905`
  * **Butterfly Marketing Limited:** `3000002272`
* **Primary Scope:** High-value procurement settlement, RTGS/EFT fund reconciliation, multi-entity liquidity monitoring, and SAP S/4HANA financial posting.

---

## 🛠 Active Workflows & Core Infrastructure

1. **Financial Auditing & Reconciliation (`sap.html` / `Dashboard.jsx`):**
   * Real-time tracking of dealer deposits, Journal Vouchers (JV), and bank clearances.
   * Certified audit tracking ref: `SR-BML-2026-RTGS-RECON-FINAL`.
   * Live deposit clearing management (e.g., DBBL Hatboaliya Branch BDT 3,00,000/- deposit clearance).
   * Automated AI-assisted audit notices and discrepancy clearance pipelines utilizing Gemini API integration.

2. **Procurement Lifecycle Management:**
   * Purchase Order `#e000010109` tracking for **৳1.43 Crore (৳14.3M)** ECO+ and Butterfly Refrigerator units.
   * Automated document compilation via GitHub Actions (`.github/workflows/compile_pdfs.yml`).

3. **Notification Engine (`scripts/send_email.py`):**
   * Instant email dispatch to treasury audit officers upon successful ledger posting.

---

## 📁 Repository Structure
* `index.html` / `portal.html` - Live Enterprise Portal & Transaction Settlement Gateway
* `Dashboard.jsx` - React Central ERP & AI Audit Dashboard
* `sap.html` - SAP FI-BL Financial Reconciliation Module
* `scripts/` - Automated Python audit scripts and notification dispatchers
