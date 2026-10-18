import os
import requests
from datetime import datetime

def trigger_enterprise_sms(phone_number: str, message_body: str):
    api_key = os.environ.get("SMS_GATEWAY_API_KEY")
    sender_id = os.environ.get("SMS_SENDER_ID", "SALSABILAH")
    
    if not api_key:
        print("Error: SMS_GATEWAY_API_KEY environment variable is missing.")
        return False

    # Example standard bulk/transactional SMS API payload (e.g., Bangladesh local gateway standard)
    payload = {
        "api_key": api_key,
        "senderid": sender_id,
        "number": phone_number,
        "message": message_body
    }

    print(f"[{datetime.now()}] Dispatching Enterprise SMS to {phone_number}...")
    
    try:
        # Replace with your active SMS Gateway endpoint provider URL
        response = requests.post("https://bulksmsbd.net/api/smsapi", data=payload)
        res_data = response.json()
        
        if response.status_code == 200:
            print(f"SMS Triggered Successfully. Gateway Response: {res_data}")
            return True
        else:
            print(f"SMS Gateway Error Code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Failed to connect to SMS Gateway: {e}")
        return False

if __name__ == "__main__":
    # Test execution for Salsabilah Amin Empires / SR Electronics
    sample_phone = "01700000000"
    sample_msg = "Dear Partner, your SAP FI-BL ledger reconciliation and RTGS payment settlement has been processed successfully."
    # trigger_enterprise_sms(sample_phone, sample_msg)
    print("SMS Gateway Trigger Module Loaded Successfully.")
