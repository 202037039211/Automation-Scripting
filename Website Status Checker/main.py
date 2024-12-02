import requests
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Configuration
URLS = ["http://example.com"]  # List of URLs to monitor
CHECK_INTERVAL = 30  # Interval in seconds (e.g., 300 seconds = 5 minutes)
LOG_FILE = "website_status_log.txt"
EMAIL_ALERTS = True  # Set to True to enable email alerts
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_USER = "/"  # Your email address
SMTP_PASS = "/"  # Your email password
ALERT_EMAIL = "/"  # Recipient's email address

def check_website(url):
    """Check website status and return True if it's online, else False."""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

def log_status(url, status):
    """Log the website status to a file with a timestamp."""
    with open(LOG_FILE, "a") as f:
        log_entry = f"{datetime.now()} - {url} - {'UP' if status else 'DOWN'}\n"
        f.write(log_entry)

def send_email_alert(url):
    """Send an email alert if a website is down."""
    if EMAIL_ALERTS:
        msg = MIMEText(f"ALERT! The website {url} is down.")
        msg["Subject"] = f"Website Down Alert: {url}"
        msg["From"] = SMTP_USER
        msg["To"] = ALERT_EMAIL
        
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASS)
                server.sendmail(SMTP_USER, ALERT_EMAIL, msg.as_string())
            print(f"Alert email sent for {url}.")
        except Exception as e:
            print(f"Failed to send email alert for {url}. Error: {e}")

def monitor_websites():
    """Main function to monitor websites at regular intervals."""
    while True:
        for url in URLS:
            status = check_website(url)
            log_status(url, status)
            if not status:
                print(f"Website down: {url}")
                send_email_alert(url)
            else:
                print(f"Website is up: {url}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_websites()

