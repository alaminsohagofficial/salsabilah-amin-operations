import os
import requests
import google.generativeai as genai

# ১. API ক্রেডেনশিয়াল কনফিগারেশন
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BANK_API_ENDPOINT = os.getenv("BANK_API_ENDPOINT")  # যেমন: DBBL / RTGS গেটওয়ে
BANK_API_TOKEN = os.getenv("BANK_API_TOKEN")

genai.configure(api_key=GEMINI_API_KEY)

# আধুনিক এবং দ্রুতগতির মডেল ব্যবহার করা হয়েছে
model = genai.GenerativeModel('gemini-1.5-flash')

def fetch_banking_transactions():
    """ব্যাংকিং কোর/এপিআই থেকে লাইভ লেনদেন সংগ্রহ"""
    headers = {"Authorization": f"Bearer {BANK_API_TOKEN}"}
    try:
        response = requests.get(f"{BANK_API_ENDPOINT}/v1/transactions/latest", headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Banking API Error: {e}")
    return None

def analyze_with_gemini(transaction_data):
    """Gemini API দিয়ে ট্রানজেকশন অডিট ও লেজার ক্লাসিফিকেশন"""
    prompt = f"""
    Analyze the following banking transaction data and classify it for ERP Ledger:
    {transaction_data}
    Output format: JSON with Dealer Code, Cleared Amount, and Matching SAP Reference.
    """
    response = model.generate_content(prompt)
    return response.text

def run_pipeline():
    print("Initiating Banking & AI Pipeline...")
    tx_data = fetch_banking_transactions()
    
    if tx_data:
        insights = analyze_with_gemini(tx_data)
        print("Gemini API Ledger Processing Completed:")
        print(insights)
    else:
        print("No new banking transactions or running in test mode.")

if __name__ == "__main__":
    run_pipeline()
