# Task Scheduler with SMS Reminders

This Python script schedules reminders to be sent via SMS using Twilio. It includes daily and hourly reminders for tasks like checking emails and staying hydrated.

## Features:
- **Daily Reminder**: Sends a reminder at 10:28 AM to check emails and plan the day.
- **Hourly Reminder**: Sends an hourly reminder to stay hydrated and take short breaks.
- **Twilio Integration**: Uses Twilio's API to send SMS messages to a recipient.

## Requirements:
- Python 3.x
- `schedule` for task scheduling
- `twilio` for sending SMS messages

## Installation:
1. Clone this repository.

2. Install required libraries:
```bash
pip install schedule twilio
```

3. Replace the Twilio credentials in the script with your own account SID, authentication token, and phone numbers.

4. Run the script with:
```bash
python main.py
```

## Usage:
1. The script will start the task scheduler, which will run in the background.
2. A reminder will be sent every hour, and a daily reminder will be sent at 10:28 AM.
3. Press `Ctrl+C` to exit the scheduler.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.
