const express = require('express');
const app = express();
app.use(express.json());

// রিয়েল-টাইম সেন্ট্রাল ট্রেজারি ডাটাবেস স্টেট
let realTimeTreasury = {
    business_name: "S.R. Electronics Park",
    proprietor: "MD. AL AMIN SOHAG",
    last_sync: new Date().toISOString(),
    mhpil: {
        principal: "Minister Hi-Tech Park Electronics Ltd.",
        dealer_code: "002905",
        bank_ref: "IBBL A/C 20503910100020103 & Sonali Bank RTGS",
        net_surplus: 33056297.00,
        status: "LIVE_SYNCED"
    },
    butterfly: {
        principal: "Butterfly Marketing Limited",
        account_code: "3000002272",
        bank_ref: "City Bank & DBBL RTGS",
        allocated_funds: 31429000.00,
        status: "LIVE_SYNCED"
    }
};

// ১. রিয়েল-টাইম ট্রেজারি স্ট্যাটাস এপিআই
app.get('/api/v1/treasury/live-status', (req, res) => {
    realTimeTreasury.last_sync = new Date().toISOString();
    res.json({
        success: true,
        timestamp: realTimeTreasury.last_sync,
        data: realTimeTreasury
    });
});

// ২. এক্সটার্নাল ব্যাংক বা SAP এপিআই থেকে লাইভ ডাটা পুশ/সিঙ্ক করার এন্ডপয়েন্ট
app.post('/api/v1/sync/ledger', (req, res) => {
    const { company, surplus_amount, allocated_funds } = req.body;

    if (company === 'MHPIL' && surplus_amount !== undefined) {
        realTimeTreasury.mhpil.net_surplus = surplus_amount;
        realTimeTreasury.mhpil.status = "UPDATED_VIA_API";
    } else if (company === 'BML' && allocated_funds !== undefined) {
        realTimeTreasury.butterfly.allocated_funds = allocated_funds;
        realTimeTreasury.butterfly.status = "UPDATED_VIA_API";
    } else {
        return res.status(400).json({ success: false, message: "Invalid sync payload format." });
    }

    res.json({
        success: true,
        message: `Real-time synchronization successful for ${company}`,
        current_data: realTimeTreasury
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`S.R. Electronics Park Real-Time API Engine running on port ${PORT}`);
});
