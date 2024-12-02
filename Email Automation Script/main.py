import requests
import csv

# Configuration: Set your Mailgun domain and API key
MAILGUN_DOMAIN = 'your-mailgun-domain'  # Replace with your Mailgun domain
MAILGUN_API_KEY = 'your-mailgun-api-key'  # Replace with your Mailgun API key
MAILGUN_API_URL = f'https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages'

def send_email(recipient, subject, message):
    """
    Function to send an email using the Mailgun API.

    :param recipient: Email address of the recipient
    :param subject: Subject of the email
    :param message: Body of the email
    :return: Response object from Mailgun API
    """
    response = requests.post(
        MAILGUN_API_URL,
        auth=('api', MAILGUN_API_KEY),
        data={
            'from': f'Your Name <postmaster@{MAILGUN_DOMAIN}>',
            'to': recipient,
            'subject': subject,
            'text': message
        }
    )
    return response

def load_recipients(file_path):
    """
    Function to load email addresses from a CSV file.

    :param file_path: Path to the CSV file containing the email addresses
    :return: List of email addresses
    """
    recipients = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:  # Ensure the row is not empty
                    recipients.append(row[0])  # Assuming email addresses are in the first column
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
    return recipients

def main():
    """
    Main function to load recipients and send emails.
    """
    subject = "Your Subject Here"
    message = "This is a test message from your automated email tool."
    
    # Load recipient email addresses from CSV
    recipients = load_recipients('recipients.csv')
    
    if not recipients:
        print("No recipients found. Exiting...")
        return

    # Send emails to all recipients
    for recipient in recipients:
        response = send_email(recipient, subject, message)
        if response.status_code == 200:
            print(f"Email sent to {recipient}")
        else:
            print(f"Failed to send email to {recipient}: {response.status_code}, {response.text}")

if __name__ == '__main__':
    main()
