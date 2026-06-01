import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

log = logging.getLogger(__name__)

def send_email(recipient_email: str, subject: str, body: str):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))

    if not sender_email or not sender_password:
        log.error("Email credentials not set in environment variables. Skipping email.")
        return

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        log.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        log.error(f"Failed to send email to {recipient_email}: {e}")

if __name__ == "__main__":
    # Example usage (will not run without environment variables set)
    # For testing, set SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL in your environment
    test_recipient = os.getenv("RECIPIENT_EMAIL", "test@example.com")
    test_subject = "Test Subject from Investor Outreach Scraper"
    test_body = "This is a test email sent from the Investor Outreach Scraper project."
    send_email(test_recipient, test_subject, test_body)
