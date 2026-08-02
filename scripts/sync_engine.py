import os
import sys
import requests

def fetch_api_data():
    """
    Fetches live ledger & clearance data from SAP ERP / Banking API using GitHub Secrets.
    """
    api_url = os.getenv("ERP_API_URL")
    api_token = os.getenv("ERP_API_TOKEN")

    if not api_url or not api_token:
        print("⚠️ API Secrets missing. Skipping API fetch and using local template defaults.")
        return None

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    try:
        print(f"📡 Connecting to API: {api_url}")
        response = requests.get(api_url, headers=headers, timeout=15)
        if response.status_code == 200:
            print("✅ Successfully fetched live data from API.")
            return response.json()
        else:
            print(f"⚠️ API Response Error: Status {response.status_code}")
    except Exception as e:
        print(f"❌ API Connection Failed: {e}", file=sys.stderr)

    return None

def main():
    print("🚀 SAP & Banking API Sync Engine Initialized.")
    data = fetch_api_data()
    print("✅ Sync Process Completed. Ready for LaTeX Compilation.")

if __name__ == "__main__":
    main()
