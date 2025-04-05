import smtplib
from email.mime.text import MIMEText
import os
from services.logger import logger

def send_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = os.getenv("ALERT_FROM_EMAIL")
    msg["To"] = os.getenv("ALERT_TO_EMAIL")

    try:
        with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
            server.starttls()
            server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
            server.sendmail(msg["From"], [msg["To"]], msg.as_string())
    except Exception as e:
        logger.error("Error sending email alert: %s", str(e))