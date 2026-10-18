import requests
import json
from datetime import datetime

API_URL = "http://localhost:3000/api/v1/sync/ledger"

def sync_enterprise_ledgers():
    payload_mhpil = {
        "company": "MHPIL",
        "dealer_code": "DEAL002905",
        "surplus_amount": 33056297.00
    }
    
    payload_bml = {
        "company": "BML",
        "dealer_code": "3000002272",
        "allocated_funds": 31429000.00
    }

    print(f"[{datetime.now()}] Initiating sync_engine.py - SAP & Bank Ledger Synchronization...")
    
    try:
        res1 = requests.post(API_URL, json=payload_mhpil)
        res2 = requests.post(API_URL, json=payload_bml)
        
        if res1.status_code == 200 and res2.status_code == 200:
            print("Successfully synchronized all brand ledgers via sync_engine.py.")
            print("MHPIL Sync Response:", res1.json())
            print("BML Sync Response:", res2.json())
        else:
            print("Sync warning: Response code mismatch in sync_engine.")
    except Exception as e:
        print(f"Error connecting to local/cloud API server from sync_engine: {e}")

if __name__ == "__main__":
    sync_enterprise_ledgers()
