from pydantic import BaseModel

class VolunteerCreate(BaseModel):
    volunt_name: str
    phone_number: str
    email:str
    password: str
class VolunteerUpdate(BaseModel):
    volunt_name:str=None
    phone_number:str=None
    email:str=None


class VolunteerLogin(BaseModel):
    email: str
    password: str



