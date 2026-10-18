// server.js - Salsabilah Amin Empires Enterprise Backend
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 5000; // ফ্রন্টএন্ডের সাথে সামঞ্জস্য রেখে পোর্ট 5000 করা হয়েছে

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

// API Endpoint: Payment Initiation Gateway (ফ্রন্টএন্ডের জন্য নতুন যুক্ত করা হয়েছে)
app.post('/api/v1/payment/initiate', (req, res) => {
    const { amount, phone, channel } = req.body;

    // ভ্যালিডেশন চেক
    if (!amount || !phone || !channel) {
        return res.status(400).json({
            success: false,
            message: 'সকল ফিল্ড সঠিকভাবে পূরণ করুন।'
        });
    }

    // পেমেন্ট গেটওয়ে ইউআরএল জেনারেট (এখানে SSLCommerz বা ব্যাংক গেটওয়ের রিডাইরেক্ট লিংক হবে)
    // উদাহরণস্বরূপ একটি ডামি গেটওয়ে পেজ ইউআরএল রিটার্ন করা হচ্ছে
    res.json({
        success: true,
        GatewayPageURL: `https://sandbox.sslcommerz.com/gwprocess/v4/api.php?ref=SALSABILAH_${Date.now()}`,
        trx_id: `TXN-${Math.floor(Math.random() * 900000 + 100000)}`,
        message: 'পেমেন্ট রিকোয়েস্ট সফলভাবে গৃহীত হয়েছে।'
    });
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
