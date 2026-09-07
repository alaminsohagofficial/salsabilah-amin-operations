// server.js - Salsabilah Amin Empires Enterprise Backend
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(bodyParser.json());

// In-memory Treasury Live Status & Ledger Mock
const treasuryData = {
    success: true,
    data: {
        minister_dealer: "DEAL002905",
        minister_balance: "+ BDT 3,30,56,297.00 Cr",
        butterfly_dealer: "3000002272",
        butterfly_balance: "BDT 3,14,29,000.00",
        last_sync: new Date().toISOString()
    }
};

// API Endpoint: Live Treasury Status
app.get('/api/v1/treasury/live-status', (req, res) => {
    res.json(treasuryData);
});

// API Endpoint: Disputes Records
app.get('/reconciliation/disputes', (req, res) => {
    res.json({
        success: true,
        records: [
            { dispute_id: "DSP-2026-01", dbbl_trace_id: "TRC-101", dealer_id: "DEAL002905", amount_bdt: 250000, status: "PENDING_SAP_SYNC" },
            { dispute_id: "DSP-2026-02", dbbl_trace_id: "TRC-102", dealer_id: "3000002272", amount_bdt: 180000, status: "UNDER_AI_AUDIT" }
        ]
    });
});

// API Endpoint: Gemini AI Dispute Audit Analysis
app.post('/reconciliation/disputes/analyze', (req, res) => {
    const { dealer_id, central_ledger, partner_invoices } = req.body;
    
    // Logic simulation for audit
    res.json({
        success: true,
        audit_notice_ref: `SR-AUDIT-2026-${Math.floor(Math.random() * 90000 + 10000)}`,
        dealer_id: dealer_id || "DEAL002905",
        analysis: {
            is_balanced: false,
            total_discrepancy_bdt: 20000,
            audit_summary: "Minor ledger variance identified in invoice trace ID TRC-102. Fully compliant with Bangladesh Bank RTGS guidelines after automated adjustment."
        }
    });
});

app.listen(PORT, () => {
    console.log(`Salsabilah Enterprise Server running on port ${PORT}`);
});
