from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DonationCreate(BaseModel):
    amount: float
    payment_method: str
    donor_name: str | None = None
    donor_email: str | None = None
    volunt_id: int 


class DonationResponse(DonationCreate):
    id: int
    volunt_id:int 

    amount: float
    payment_method: str
    donor_name: str
    donor_email: str

    donated_at: Optional[datetime] = None  
    donated_at: datetime

    class Config:
        from_attributes = True
