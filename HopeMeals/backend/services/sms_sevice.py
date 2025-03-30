from twilio.rest import Client
import os

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_sms_alert(admin_number, message):
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=admin_number
    )
