import os
import uuid
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from models.donation import FoodDonation
from database import donations_collection, ngos_collection, volunteers_collection
from services.cloudinary_upload import upload_food_image
from services.ai_food_classifier import classify_food
from services.qr_verification import generate_hashed_qr_code
from notifications.sms_alerts import send_sms_alert
from notifications.email_notifications import send_donation_email, send_ngo_email, send_volunteer_email
from datetime import datetime

router = APIRouter()

async def find_nearest_ngo(pickup_location: str):
    """
    ✅ Find the nearest NGO based on location from the database.
    ✅ If no NGO exists at the given location, fetch any available NGO.
    ✅ If no NGO exists at all, return None.
    """
    nearest_ngo = await ngos_collection.find_one({"location": pickup_location})
    if not nearest_ngo:
        nearest_ngo = await ngos_collection.find_one({})  # Assign any available NGO
    return nearest_ngo

async def find_nearest_volunteer(pickup_location: str):
    """
    ✅ Find the nearest volunteer based on location from the database.
    ✅ If no volunteer exists at the given location, fetch any available volunteer.
    ✅ If still no volunteers exist, create a default volunteer entry and assign them.
    """
    nearest_volunteer = await volunteers_collection.find_one({"location": pickup_location})
    
    # ✅ If no volunteer found at location, find ANY volunteer
    if not nearest_volunteer:
        nearest_volunteer = await volunteers_collection.find_one({})
    
    # ✅ If STILL no volunteer exists, create a default volunteer and assign
    if not nearest_volunteer:
        default_volunteer = {
            "name": "Default Volunteer",
            "email": "test198711022006@gmail.com",
            "phone": "+918826417060",
            "assigned_donations": [],
            "created_at": datetime.utcnow(),
            "location": "unknown"
        }
        result = await volunteers_collection.insert_one(default_volunteer)
        default_volunteer["_id"] = str(result.inserted_id)  # Convert to string
        return default_volunteer

    return nearest_volunteer

@router.post("/create")
async def create_donation(
    donor_id: str = Form(...),
    donor_email: str = Form(...),
    pickup_location: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # ✅ Securely upload food image to Cloudinary
        uploaded_image_url = await upload_food_image(file)
        if not uploaded_image_url:
            raise HTTPException(status_code=500, detail="Image upload failed")

        # ✅ AI-Based Food Classification with ViT and LLAMA-3 via Groq
        food_classification = classify_food(uploaded_image_url)

        # ✅ Ensure the uploaded image is food
        if not food_classification.get("is_food", False):
            raise HTTPException(status_code=400, detail="The uploaded image is not recognized as food.")

        # ✅ Ensure only fresh/slightly stale food is accepted
        freshness_status = food_classification.get("freshness", "fresh")
        if freshness_status in ["expired", "rotten"]:
            raise HTTPException(status_code=400, detail="The food is too spoiled to be donated.")

        # ✅ Capture vegetarian/non-vegetarian status
        vegetarian_status = food_classification.get("vegetarian", "unknown")

        # ✅ Find the nearest NGO & volunteer (or fallback)
        nearest_ngo = await find_nearest_ngo(pickup_location)
        nearest_volunteer = await find_nearest_volunteer(pickup_location)

        # ✅ Error Handling: If NO NGOs exist
        if not nearest_ngo:
            raise HTTPException(status_code=400, detail="No NGOs available to handle this donation.")

        ngo_email = nearest_ngo["email"]
        ngo_name = nearest_ngo["name"]
        volunteer_email = nearest_volunteer["email"]
        volunteer_name = nearest_volunteer["name"]

        # ✅ Generate **Highly Secure Hashed QR Codes** (Without Links)
        hashed_qr_supplier, qr_code_image_supplier = generate_hashed_qr_code(f"{uuid.uuid4()}_{donor_id}", pickup_location)
        hashed_qr_ngo, qr_code_image_ngo = generate_hashed_qr_code(f"{uuid.uuid4()}_NGO", pickup_location)
        hashed_qr_volunteer, qr_code_image_volunteer = generate_hashed_qr_code(f"{uuid.uuid4()}_VOLUNTEER", pickup_location)

        # ✅ Store donation data in MongoDB
        donation_data = {
            "donor_id": donor_id,
            "donor_email": donor_email,
            "food_type": food_classification,
            "freshness": freshness_status,
            "vegetarian": vegetarian_status,
            "pickup_location": pickup_location,
            "image_url": uploaded_image_url,  # ✅ Food image stored from Cloudinary
            "status": "pending",
            "assigned_ngo": ngo_email,
            "assigned_volunteer": volunteer_email,
            "qr_codes": {
                "supplier": {"hashed": hashed_qr_supplier, "image": qr_code_image_supplier},
                "ngo": {"hashed": hashed_qr_ngo, "image": qr_code_image_ngo},
                "volunteer": {"hashed": hashed_qr_volunteer, "image": qr_code_image_volunteer}
            },
            "created_at": datetime.utcnow(),
        }

        result = await donations_collection.insert_one(donation_data)
        donation_id = str(result.inserted_id)

        # ✅ **Send Emails with Hashed QR, Freshness & Image**
        send_donation_email(
            receiver_email=donor_email,
            donor_name="Food Donor",
            food_details=food_classification,
            pickup_location=pickup_location,
            qr_code_url=qr_code_image_supplier,
            freshness_status=freshness_status,
            image_url=uploaded_image_url
        )

        send_ngo_email(
            receiver_email=ngo_email,
            ngo_name=ngo_name,
            donor_name="Food Donor",
            food_details=food_classification,
            pickup_location=pickup_location,
            qr_code_url=qr_code_image_ngo,
            freshness_status=freshness_status,
            image_url=uploaded_image_url
        )

        send_volunteer_email(
            receiver_email=volunteer_email,
            volunteer_name=volunteer_name,
            donor_name="Food Donor",
            food_details=food_classification,
            pickup_location=pickup_location,
            qr_code_url=qr_code_image_volunteer,
            freshness_status=freshness_status,
            image_url=uploaded_image_url
        )

        # ✅ Send SMS Alert to Admin
        send_sms_alert("+918826417060", f"New food donation at {pickup_location}. Assigned to {ngo_name} & {volunteer_name}.")

        return {
            "message": "Food donation created successfully!",
            "donation_id": donation_id,
            "qr_codes": {
                "supplier": hashed_qr_supplier,
                "ngo": hashed_qr_ngo,
                "volunteer": hashed_qr_volunteer
            },
            "assigned_to": {
                "ngo": ngo_name,
                "volunteer": volunteer_name
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
