import qrcode
import cloudinary
import cloudinary.uploader
import os
import hashlib
from dotenv import load_dotenv
from io import BytesIO
from fastapi import HTTPException

load_dotenv()

# ✅ Configure Cloudinary for secure QR storage
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def generate_hashed_qr_code(donation_id: str, pickup_location: str):
    """
    ✅ Generates a QR code with a **hashed** and **secure** value (No direct links).
    ✅ Uploads the QR code image to Cloudinary and returns its URL.
    """
    # ✅ Create a **highly secure SHA-256 hash** of the donation data
    qr_data = f"donation_id={donation_id}&location={pickup_location}"
    hashed_qr_data = hashlib.sha256(qr_data.encode()).hexdigest()

    # ✅ Generate QR Code with the hashed data
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(hashed_qr_data)
    qr.make(fit=True)

    # ✅ Convert QR to an image
    img = qr.make_image(fill="black", back_color="white")

    # ✅ Save the QR image to memory buffer
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)

    # ✅ Upload to Cloudinary (Inside a dedicated folder)
    try:
        response = cloudinary.uploader.upload(
            buffered,
            folder="qr_codes/",
            public_id=f"donation_{donation_id}",
            overwrite=True
        )
        return hashed_qr_data, response["secure_url"]  # ✅ Returning **hashed value** + QR image URL
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"QR Code upload failed: {str(e)}")


async def verify_qr_code(hashed_qr_value: str):
    """
    ✅ Verifies if a **hashed QR value exists** in the database.
    ✅ Ensures only **secure hashed QR values are accepted**.
    """
    from database import donations_collection

    # ✅ Search for the donation with this hashed QR value
    donation = await donations_collection.find_one({"qr_codes.hashed": hashed_qr_value})
    if not donation:
        raise HTTPException(status_code=404, detail="Invalid QR Code")

    # ✅ Mark the donation as **verified**
    await donations_collection.update_one(
        {"qr_codes.hashed": hashed_qr_value},
        {"$set": {"status": "verified"}}
    )

    return {
        "message": "✅ QR Code Verified Successfully!",
        "donation_id": donation["_id"],
        "status": "verified"
    }
