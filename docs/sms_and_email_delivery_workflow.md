# SMS & Email Delivery Architecture

## Workflow Pipeline
1. **Trigger Event:** SAP ERP ledger change or automated billing update.
2. **API Fetch:** Python script loads credentials safely from GitHub Secrets.
3. **Dispatch:** HTTP POST request sent to Telecommunications API.
4. **Log:** Status recorded in GitHub Action logs without revealing secret keys.
