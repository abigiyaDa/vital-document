from pydantic import BaseModel
from datetime import date
from app.models.registration import RegType

class RegistrationCreate(BaseModel):
    officer_id: int
    reg_date: date
    reg_place: str
    reg_type: RegType

class RegistrationResponse(RegistrationCreate):
    reg_id: int
    class Config:
        from_attributes = True