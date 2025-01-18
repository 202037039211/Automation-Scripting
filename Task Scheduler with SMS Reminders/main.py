import schedule
import time
from twilio.rest import Client
import datetime

# Twilio credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = "/"
TWILIO_AUTH_TOKEN = "/"
TWILIO_PHONE_NUMBER = "/"  # Your Twilio phone number
TARGET_PHONE_NUMBER = "/"  # Recipient's phone number

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_reminder(message):
    """Send reminder message via Twilio."""
    try:
        # Send SMS message
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=TARGET_PHONE_NUMBER
        )
        # Log reminder sent time
        print(f"Reminder sent: {message} at {datetime.datetime.now()}")
    except Exception as e:
        # Handle errors if reminder fails to send
        print(f"Failed to send reminder: {e}")

# Task reminders
def daily_task():
    """Send daily reminder message."""
    send_reminder("Daily Reminder: Check your emails and plan your day!")

def hourly_task():
    """Send hourly reminder message."""
    send_reminder("Hourly Reminder: Stay hydrated and take short breaks!")

# Schedule tasks
schedule.every().day.at("10:28").do(daily_task)   # Daily reminder at 10:28 AM
schedule.every().hour.do(hourly_task)             # Hourly reminder

def run_scheduler():
    """Run the scheduler continuously."""
    print("Task Scheduler started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()  # Run pending tasks
        time.sleep(1)  # Wait for 1 second before checking for new tasks

if __name__ == "__main__":
    run_scheduler()  # Start the scheduler when the script is executed
