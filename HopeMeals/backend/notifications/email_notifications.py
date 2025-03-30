import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from jinja2 import Template

# ✅ Load environment variables
load_dotenv()

# ✅ SMTP Configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# ✅ Validate required SMTP variables
if not all([SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD]):
    raise ValueError("⚠️ Missing SMTP configuration in environment variables.")

# ✅ Ensure PORT is an integer
SMTP_PORT = int(SMTP_PORT)

def send_email(receiver_email: str, subject: str, template_str: str, **template_data):
    """
    ✅ Sends an HTML email using SMTP with Jinja2 templating.
    """
    try:
        # ✅ Render the email template with dynamic data
        template = Template(template_str)
        html_content = template.render(**template_data)

        # ✅ Create email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(html_content, "html", "utf-8"))

        # ✅ Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # ✅ Secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, receiver_email, msg.as_string())

        print(f"✅ Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"❌ Failed to send email to {receiver_email}: {e}")

# ✅ Send Email to Donor (Food Donation Confirmation)
def send_donation_email(receiver_email, donor_name, food_details, pickup_location, qr_code_url, freshness_status, image_url):
    html_template = """
    <html>
    <body style="font-family: Arial, sans-serif;">
        <h2 style="color:#3498db;">Food Donation Confirmation</h2>
        <p>Hello <b>{{ donor_name }}</b>,</p>
        <p>Thank you for your generous food donation!</p>
        <p><b>Food Details:</b> {{ food_details }}</p>
        <p><b>Pickup Location:</b> {{ pickup_location }}</p>
        <p><b>Food Freshness:</b> {{ freshness_status }}</p>
        <p><b>Donation Image:</b> <br> <img src="{{ image_url }}" width="300px" style="border: 2px solid black;"></p>
        <p><b>QR Code for Verification:</b> <a href="{{ qr_code_url }}" target="_blank">Scan Here</a></p>
        <br>
        <p style="color:green;">Together, we can reduce food waste and feed the needy.</p>
        <p>Best Regards,</p>
        <p><b>AI-Powered Food Distribution System</b></p>
    </body>
    </html>
    """
    send_email(receiver_email, "Food Donation Confirmation", html_template,
               donor_name=donor_name, food_details=food_details, pickup_location=pickup_location, 
               qr_code_url=qr_code_url, freshness_status=freshness_status, image_url=image_url)


# ✅ Send Email to NGO (Pickup Request)
def send_ngo_email(receiver_email, ngo_name, donor_name, food_details, pickup_location, qr_code_url, freshness_status, image_url):
    html_template = """
    <html>
    <body style="font-family: Arial, sans-serif;">
        <h2 style="color:#e67e22;">Urgent: Food Pickup Request</h2>
        <p>Hello <b>{{ ngo_name }}</b>,</p>
        <p>A new food donation is available for pickup.</p>
        <p><b>Donor Name:</b> {{ donor_name }}</p>
        <p><b>Food Details:</b> {{ food_details }}</p>
        <p><b>Pickup Location:</b> {{ pickup_location }}</p>
        <p><b>Food Freshness:</b> {{ freshness_status }}</p>
        <p><b>Donation Image:</b> <br> <img src="{{ image_url }}" width="300px" style="border: 2px solid black;"></p>
        <p><b>QR Code for Pickup:</b> <a href="{{ qr_code_url }}" target="_blank">Scan Here</a></p>
        <br>
        <p>Best Regards,</p>
        <p><b>AI-Powered Food Distribution System</b></p>
    </body>
    </html>
    """
    send_email(receiver_email, "Urgent: Food Pickup Request", html_template,
               ngo_name=ngo_name, donor_name=donor_name, food_details=food_details, pickup_location=pickup_location, 
               qr_code_url=qr_code_url, freshness_status=freshness_status, image_url=image_url)


# ✅ Send Email to Volunteer (Pickup Assignment with QR Code)
def send_volunteer_email(receiver_email, volunteer_name, donor_name, food_details, pickup_location, qr_code_url, freshness_status, image_url):
    html_template = """
    <html>
    <body style="font-family: Arial, sans-serif;">
        <h2 style="color:#27ae60;">New Pickup Assignment</h2>
        <p>Hello <b>{{ volunteer_name }}</b>,</p>
        <p>You have been assigned a food pickup task.</p>
        <p><b>Pickup Location:</b> {{ pickup_location }}</p>
        <p><b>Donor Name:</b> {{ donor_name }}</p>
        <p><b>Food Details:</b> {{ food_details }}</p>
        <p><b>Food Freshness:</b> {{ freshness_status }}</p>
        <p><b>Donation Image:</b> <br> <img src="{{ image_url }}" width="300px" style="border: 2px solid black;"></p>
        <p><b>QR Code for Verification:</b> <a href="{{ qr_code_url }}" target="_blank">Scan Here</a></p>
        <br>
        <p>Best Regards,</p>
        <p><b>AI-Powered Food Distribution System</b></p>
    </body>
    </html>
    """
    send_email(receiver_email, "New Pickup Assignment", html_template,
               volunteer_name=volunteer_name, donor_name=donor_name, food_details=food_details, pickup_location=pickup_location, 
               qr_code_url=qr_code_url, freshness_status=freshness_status, image_url=image_url)
