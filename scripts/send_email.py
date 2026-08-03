import os
import smtplib
from email.mime.text import MIMEText

def send_alert():
    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    receiver = "alaminsohag2024@gmail.com"

    msg = MIMEText("SAP ERP Update & Ledger Reconciliation Complete.")
    msg['Subject'] = "Salsabilah Operations Alert"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    send_alert()
