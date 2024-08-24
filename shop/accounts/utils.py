from django.core.mail import send_mail
import requests
from django.conf import settings

def send_welcome_email(subject, message, recipient_list):
    from_email = 'your_email@gmail.com'
    send_mail(subject, message, from_email, recipient_list)





def send_email_via_sender_net(to_email, subject, message):
    url = "https://api.sender.net/v2/email"  # URL درست برای ارسال ایمیل
    headers = {
        "Authorization": f"Bearer {settings.EMAIL_HOST_PASSWORD}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from": {"email": settings.EMAIL_HOST_USER},
        "to": [{"email": to_email}],
        "subject": subject,
        "html": message
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
