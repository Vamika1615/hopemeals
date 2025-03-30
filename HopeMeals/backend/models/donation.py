from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FoodDonation(BaseModel):
    donor_id: str
    food_type: Optional[str] = None
    portion_size: Optional[str] = None
    freshness: Optional[str] = None
    pickup_location: str
    assigned_volunteer: Optional[str] = None
    status: str = "pending"  # "pending", "assigned", "completed"
    created_at: datetime = datetime.utcnow()
