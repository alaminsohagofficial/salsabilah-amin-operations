# Google Workspace & Domain Operations Guide
**Admin Email:** alaminsohag2024@gmail.com

## Managed Domains
- `salsabilah.com`
- `salsabilahelectronics.com`

## Infrastructure & Billing Workflow
- **Billing Management:** Associated Billing IDs are referenced via Repository Encrypted Secrets (`GOOGLE_BILLING_ID`).
- **Automated Alerts:** Dispatched via `scripts/sms_gateway_trigger.py` on invoice updates or domain renewals.
