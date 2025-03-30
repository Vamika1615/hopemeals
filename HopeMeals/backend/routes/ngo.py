from fastapi import APIRouter
from database import ngos_collection, donations_collection
from models.ngo import NGO

router = APIRouter()

@router.post("/register")
async def register_ngo(ngo: NGO):
    ngo_data = ngo.dict()
    result = await ngos_collection.insert_one(ngo_data)
    return {"message": "NGO registered successfully!", "ngo_id": str(result.inserted_id)}

@router.get("/available-donations")
async def get_available_donations():
    donations = await donations_collection.find({"status": "pending"}).to_list(length=100)
    return donations

@router.post("/claim-donation/{donation_id}/{ngo_id}")
async def claim_donation(donation_id: str, ngo_id: str):
    updated_donation = await donations_collection.update_one(
        {"_id": donation_id},
        {"$set": {"status": "assigned", "assigned_volunteer": ngo_id}}
    )
    if updated_donation.modified_count == 0:
        return {"message": "Donation not found or already assigned"}
    return {"message": "Donation successfully assigned!"}
