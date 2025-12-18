from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NGOPartnerCreate(BaseModel):
    ngo_name: str
    registration_no: str
    phone_number: str
    email: str
    password: str
    city: Optional[str] = None
    service_area: Optional[str] = None
    about_ngo: Optional[str] = None

class NGOPartnerUpdate(BaseModel):
    ngo_name: Optional[str] = None
    registration_no: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    city: Optional[str] = None
    service_area: Optional[str] = None
    about_ngo: Optional[str] = None    


class NGOPartnerLogin(BaseModel):
    email: str
    password: str