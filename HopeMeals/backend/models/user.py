from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name: str
    email: str
    phone: str
    location: Optional[str] = None
    role: str  # "donor", "volunteer", "ngo"
    created_at: datetime = datetime.utcnow()
