import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

MONGO_URI = os.getenv("MONGO_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.food_distribution
donations_collection = database.get_collection("donations")
users_collection = database.get_collection("users")
ngos_collection = database.get_collection("ngos")
volunteers_collection = database.get_collection("volunteers")

