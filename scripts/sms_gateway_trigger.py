import os
import sys
import requests

def send_sms(phone_number: str, message: str, principal: str = "SR_PARK") -> bool:
    """
    Sends an SMS notification using environment variables for security.
    Supports brand-specific sender ID configuration for S.R. Electronics Park.
    """
    api_url = os.getenv("SMS_GATEWAY_URL")
    api_key = os.getenv("SMS_GATEWAY_API_KEY")
    
    # Dynamic Sender ID based on principal/brand
    if principal == "MINISTER":
        sender_id = os.getenv("MINISTER_SENDER_ID", "MINISTER")
    elif principal == "BUTTERFLY":
        sender_id = os.getenv("BML_SENDER_ID", "BUTTERFLY")
    else:
        sender_id = os.getenv("SMS_SENDER_ID", "SR_PARK")

    if not api_url or not api_key:
        print("Error: SMS credentials not found in environment variables.", file=sys.stderr)
        return False

    payload = {
        "api_key": api_key,
        "sender_id": sender_id,
        "to": phone_number,
        "message": message
    }

    try:
        response = requests.post(api_url, json=payload, timeout=10)
        response.raise_for_status()
        print(f"SMS successfully sent to {phone_number} via {sender_id}")
        return True
    except requests.exceptions.RequestException as err:
        print(f"Failed to send SMS: {err}", file=sys.stderr)
        return False

if __name__ == "__main__":
    print("S.R. Electronics Park - SMS Gateway Trigger Initialized.")
    
    # Command line argument handling for GitHub Actions / Automation triggers
    # Usage: python scripts/sms_gateway_trigger.py <phone> <message> <principal>
    if len(sys.argv) >= 3:
        target_phone = sys.argv[1]
        msg_content = sys.argv[2]
        brand_principal = sys.argv[3] if len(sys.argv) > 3 else "SR_PARK"
        send_sms(target_phone, msg_content, brand_principal)
    else:
        # Default Test Trigger
        recipient = "+8801700000000"
        sms_body = "S.R. Electronics Park: Treasury & SAP Ledger Reconciliation Trigger Test."
        # send_sms(recipient, sms_body, principal="SR_PARK")
