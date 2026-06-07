from pydantic import BaseModel
from typing import Optional
from app.models.officer import OfficerRole

class OfficerCreate(BaseModel):
    full_name: str
    username: str
    password: str
    assigned_place: Optional[str] = None
    role: OfficerRole = OfficerRole.registrar

class OfficerUpdate(BaseModel):
    full_name: Optional[str] = None
    assigned_place: Optional[str] = None
    role: Optional[OfficerRole] = None

class OfficerResponse(BaseModel):
    officer_id: int
    full_name: str
    username: str
    assigned_place: Optional[str] = None
    role: OfficerRole
    class Config:
        from_attributes = True