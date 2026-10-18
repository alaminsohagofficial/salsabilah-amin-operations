import requests
import json
from datetime import datetime

API_URL = "http://localhost:3000/api/v1/sync/ledger"

def sync_ledger_data():
    payload_mhpil = {
        "company": "MHPIL",
        "surplus_amount": 33056297.00
    }
    
    payload_bml = {
        "company": "BML",
        "allocated_funds": 31429000.00
    }

    print(f"[{datetime.now()}] Initiating Real-Time SAP & Bank Ledger Synchronization...")
    
    try:
        res1 = requests.post(API_URL, json=payload_mhpil)
        res2 = requests.post(API_URL, json=payload_bml)
        
        if res1.status_code == 200 and res2.status_code == 200:
            print("Successfully synchronized all brand ledgers in real-time.")
            print("MHPIL Response:", res1.json())
            print("BML Response:", res2.json())
        else:
            print("Sync warning: Response code mismatch.")
    except Exception as e:
        print(f"Error connecting to local/cloud API server: {e}")

if __name__ == "__main__":
    sync_ledger_data()
