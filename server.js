const express = require('express');
const app = express();
app.use(express.json());

const treasuryData = {
    business_name: "S.R. Electronics Park",
    proprietor: "MD. AL AMIN SOHAG",
    currency: "BDT",
    mhpil_settlement: {
        principal: "Minister Hi-Tech Park Electronics Ltd.",
        dealer_name: "S.R. Electronics Park",
        dealer_code: "002905",
        sap_doc_cleared: "5100029481",
        total_inflows: 39195000.00,
        total_debits: 8795000.00,
        net_surplus: 33056297.00,
        dispute_status: "CLEARED"
    },
    bml_settlement: {
        principal: "Butterfly Marketing Limited",
        dealer_name: "S.R. Electronics Park",
        account_code: "3000002272",
        memo_ref: "BML/TRS/2026/08/3000002272",
        allocated_funds: 31429000.00,
        active_balance: -209.00,
        credit_status: "RELEASED"
    }
};

app.get('/api/treasury/status', (req, res) => {
    res.json({ success: true, data: treasuryData });
});

app.post('/api/procurement/order', (req, res) => {
    const { principal, amount, itemDetails } = req.body;

    if (principal === 'MHPIL') {
        if (treasuryData.mhpil_settlement.net_surplus >= amount) {
            treasuryData.mhpil_settlement.net_surplus -= amount;
            return res.json({
                success: true,
                message: "Minister Hi-Tech Park procurement order placed successfully using surplus funds.",
                dealer_code: treasuryData.mhpil_settlement.dealer_code,
                remaining_surplus: treasuryData.mhpil_settlement.net_surplus,
                item: itemDetails
            });
        } else {
            return res.status(400).json({ success: false, message: "Insufficient MHPIL surplus funds under dealer code 002905." });
        }
    } else if (principal === 'BML') {
        if (treasuryData.bml_settlement.credit_status === 'RELEASED') {
            return res.json({
                success: true,
                message: "Butterfly Marketing Limited procurement order authorized via released credit line.",
                dealer_code: treasuryData.bml_settlement.account_code,
                item: itemDetails
            });
        } else {
            return res.status(400).json({ success: false, message: "BML credit not released for dealer code 3000002272." });
        }
    } else {
        return res.status(400).json({ success: false, message: "Invalid principal entity specified." });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`S.R. Electronics Park Treasury Engine running on port ${PORT}`);
});
