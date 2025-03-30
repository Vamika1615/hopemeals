from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms_alert(phone_number, message):
    """
    Sends an SMS alert using Twilio API.
    """
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=phone_number
        )
        print(f"SMS sent successfully to {phone_number}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")
