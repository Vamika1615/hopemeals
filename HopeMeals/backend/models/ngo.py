from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class NGO(BaseModel):
    name: str
    email: str
    phone: str
    location: str
    volunteers: List[str] = []
    created_at: datetime = datetime.utcnow()
