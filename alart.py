import smtplib
from email.message import EmailMessage

def send_alert_email(subject, message, recipients):
    # Set up SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    # Sender email credentials
    sender_email = 'praveenamsaking@gmail.com'  # Replace with your Gmail address
    sender_password = 'bdll qrcj lqce ciru'  # Replace with your Gmail password

    # Construct the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipients
    msg.set_content(message)

    # Connect to SMTP server and send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email alert sent successfully.")
    except Exception as e:

        print(f"Failed to send email alert: {str(e)}")

# Example usage:
alert_subject = "Emergency: Patient Alert"
alert_message = "Patient in room 203 requires immediate attention."
recipient_emails = ("kirubapreetta@gmail.com", "goku0735@gmail.com")  # List of recipient email addresses

send_alert_email(alert_subject, alert_message, recipient_emails)
