import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_treasury_audit_email():
    sender_email = os.environ.get("TREASURY_EMAIL_USER")
    sender_password = os.environ.get("TREASURY_EMAIL_PASS")
    audit_officer_email = os.environ.get("AUDIT_OFFICER_EMAIL")

    if not sender_email or not sender_password or not audit_officer_email:
        print("Error: Required environment variables for email are missing.")
        return

    # S.R. Electronics Park Treasury & Audit Confirmation Details
    subject = "【SR-BML-2026-RTGS-RECON-FINAL】 Treasury & SAP Ledger Posting Confirmation"
    
    body = """
    Dear Audit Officer,

    This is an automated notification from S.R. Electronics Park Operations & Treasury Management.
    
    Dealer Code: 3000002272
    Audit Reference: SR-BML-2026-RTGS-RECON-FINAL
    Scope: High-value procurement settlement, RTGS/EFT fund reconciliation, and SAP S/4HANA financial posting.
    
    Status: 
    - Purchase Order #e000010109 (৳1.43 Crore ECO+ & Butterfly Refrigerator Units) lifecycle updated.
    - Live deposit clearance (DBBL Hatboaliya Branch BDT 3,00,000/-) successfully synchronized with SAP FI/AR ledger.

    Please check the repository dashboard and sap.html for real-time audit verification.

    Best regards,
    Automated Treasury Engine
    S.R. Electronics Park
    """

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = audit_officer_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connecting to SMTP server (e.g., Gmail TLS)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, audit_officer_email, message.as_string())
        server.quit()
        print("Treasury audit confirmation email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_treasury_audit_email()
