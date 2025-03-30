from notifications.email_notifications import send_volunteer_email

send_volunteer_email(
    receiver_email="dhruvdawar11022006@gmail.com",
    volunteer_name="Test Volunteer",
    donor_name="John Doe",
    food_details="Vegetarian Meal",
    pickup_location="123 Main Street, Mumbai",
    qr_code_url="https://your_qr_code_link.com"
)
