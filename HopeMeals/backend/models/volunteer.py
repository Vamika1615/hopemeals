from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Volunteer(BaseModel):
    name: str
    email: str
    phone: str
    assigned_donations: Optional[List[str]] = []
    created_at: datetime = datetime.utcnow()
