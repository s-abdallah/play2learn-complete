import sendgrid
from sendgrid.helpers.mail import Mail
import os
import ssl
import urllib3


def send_email(to_email, subject, message):
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))

    # Disable SSL verification
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    ssl._create_default_https_context = ssl._create_unverified_context

    from_email = "your_email@example.com"
    content = Mail(
        from_email=from_email, to_emails=to_email, subject=subject, html_content=message
    )

    try:
        response = sg.send(content)
        return response.status_code
    except Exception as e:
        print(f"Error: {e}")
