from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.models.death import InformantRelationshipEnum

class DeathCreate(BaseModel):
    reg_id: int
    person_id: int
    death_date: date
    death_place: str
    cause_of_death: Optional[str] = None
    informant_person_id: Optional[int] = None
    informant_relationship: Optional[InformantRelationshipEnum] = None
    evidence_id: Optional[int] = None

class DeathResponse(DeathCreate):
    death_id: int
    class Config:
        from_attributes = True