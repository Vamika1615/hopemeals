from fastapi import APIRouter
from database import users_collection
from models.user import User

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    user_data = user.dict()
    result = await users_collection.insert_one(user_data)
    return {"message": "User registered successfully!", "user_id": str(result.inserted_id)}

@router.get("/")
async def get_users():
    users = await users_collection.find().to_list(length=100)
    return users
