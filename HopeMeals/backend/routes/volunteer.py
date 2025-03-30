from fastapi import APIRouter
from database import volunteers_collection
from models.volunteer import Volunteer

router = APIRouter()

@router.post("/register")
async def register_volunteer(volunteer: Volunteer):
    volunteer_data = volunteer.dict()
    result = await volunteers_collection.insert_one(volunteer_data)
    return {"message": "Volunteer registered successfully!", "volunteer_id": str(result.inserted_id)}

@router.get("/")
async def get_volunteers():
    volunteers = await volunteers_collection.find().to_list(length=100)
    return volunteers
