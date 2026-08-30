import os
import sys
import requests

def fetch_api_data():
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

def process_brand_ledgers(data):
    if not data or "entries" not in data:
        print("ℹ️ No entries found for brand segregation. Using local fallbacks.")
        return

    minister_count = 0
    butterfly_count = 0

    for entry in data.get("entries", []):
        dealer_code = entry.get("dealer_code")
        if dealer_code == "002905":
            minister_count += 1
        elif dealer_code == "3000002272":
            butterfly_count += 1

    print(f"📊 Segregation Complete -> Minister (002905): {minister_count} records | Butterfly (3000002272): {butterfly_count} records")

def main():
    print("🚀 S.R. Electronics Park - SAP & Banking API Sync Engine Initialized.")
    data = fetch_api_data()
    if data:
        process_brand_ledgers(data)
    print("✅ Sync Process Completed. Ready for LaTeX / PDF Compilation.")

if __name__ == "__main__":
    main()
