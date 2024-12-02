# Email Automation Script

This Python script automates the process of sending emails to a list of recipients. The email addresses are loaded from a CSV file, and the emails are sent using the Mailgun API.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Configuration

Before running the script, configure the following:

1. **Mailgun Settings**:
   - Replace `your-mailgun-domain` with your actual Mailgun domain.
   - Replace `your-mailgun-api-key` with your actual Mailgun API key.

2. **CSV File**:
   - The script assumes the CSV file is named `recipients.csv`, with email addresses in the first column (no headers).

## How to Use

1. **Save the script**:
   Save the script as `main.py` on your local machine.

2. **Configure Mailgun**:
   Update the `MAILGUN_DOMAIN` and `MAILGUN_API_KEY` variables with your Mailgun details.

3. **Prepare the Recipients File**:
   Create a CSV file named `recipients.csv` with email addresses in the first column.

4. **Run the script**:
```bash
python main.py
```

5. **Check the results**:
   The script will send an email to each recipient and print a success message or an error if the email fails.


### How to Test the Script:
1. **Prepare the CSV file**:
   - Create a `recipients.csv` file with a list of email addresses.

2. **Run the script**:
   - Run the script and check the console for success or failure messages for each recipient.

3. **Check your Mailgun account**:
   - Verify that emails are being sent through your Mailgun account.
