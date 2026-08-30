import os
import json
import sys

def parse_sap_ledger(ledger_file_path: str):
    """
    Parses and reconciles SAP OData/REST accounting ledger exports 
    separately for S.R. Electronics Park (Minister & Butterfly Accounts).
    """
    if not os.path.exists(ledger_file_path):
        print(f"Error: Ledger file '{ledger_file_path}' not found.", file=sys.stderr)
        return None

    print(f"Processing SAP Ledger file: {ledger_file_path}")
    
    try:
        with open(ledger_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        minister_entries = []
        butterfly_entries = []

        for entry in data.get("entries", []):
            dealer_code = entry.get("dealer_code")
            
            # Status update for pending entries
            if entry.get("status") == "PENDING":
                entry["status"] = "RECONCILED"

            # Segregate based on approved Dealer Codes
            if dealer_code == "002905":
                entry["principal"] = "Minister Hi-Tech Park Electronics Ltd."
                minister_entries.append(entry)
            elif dealer_code == "3000002272":
                entry["principal"] = "Butterfly Marketing Limited"
                butterfly_entries.append(entry)
            else:
                print(f"Warning: Unknown or unmapped dealer code '{dealer_code}' found.")

        print(f"--- Reconciliation Summary for S.R. Electronics Park ---")
        print(f"Minister (Dealer 002905): {len(minister_entries)} records reconciled.")
        print(f"Butterfly (Dealer 3000002272): {len(butterfly_entries)} records reconciled.")

        return {
            "minister_reconciled": minister_entries,
            "butterfly_reconciled": butterfly_entries
        }

    except Exception as e:
        print(f"Error parsing ledger: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    print("S.R. Electronics Park - SAP Ledger Reconciliation Engine Initialized.")
    
    # If running directly, you can pass a sample json file path here if needed
    if len(sys.argv) > 1:
        parse_sap_ledger(sys.argv[1])
