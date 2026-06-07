from pydantic import BaseModel
from datetime import date
from typing import Optional

class AdoptionCreate(BaseModel):
    reg_id: int
    child_id: int
    adoption_date: date
    adoption_place: Optional[str] = None
    evidence_id: Optional[int] = None

class AdoptionParentCreate(BaseModel):
    adoption_id: int
    person_id: int

class AdoptionResponse(AdoptionCreate):
    adoption_id: int
    class Config:
        from_attributes = True

class AdoptionParentResponse(AdoptionParentCreate):
    class Config:
        from_attributes = True