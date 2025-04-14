import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(subject, recipients, html_content):
    """Send an email using Gmail SMTP."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Connect to the Gmail SMTP server and send the email
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()  # Start TLS encryption
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, recipients, msg.as_string())

def get_html_template(time_of_day):
    templates = {
        "morning": "templates/good_morning.html",
        "afternoon": "templates/good_afternoon.html",
        "noon": "templates/good_noon.html",
        "evening": "templates/good_evening.html",
        "night": "templates/good_night.html"
    }
    return templates.get(time_of_day)

def fetch_template_and_send_email(time_of_day, recipients):
    template_path = get_html_template(time_of_day)
    if template_path:
        with open(template_path, 'r') as file:
            html_content = file.read()
        send_email(f"Good {time_of_day.capitalize()}", recipients, html_content)
    else:
        print("Invalid time of day provided.")