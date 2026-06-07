from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.models.marriage import MarriageTypeEnum
from app.models.marriage_witness import WitnessSideEnum

class MarriageCreate(BaseModel):
    reg_id: int
    groom_id: int
    bride_id: int
    marriage_date: date
    marriage_place: str
    marriage_type: MarriageTypeEnum
    evidence_id: Optional[int] = None

class MarriageWitnessCreate(BaseModel):
    marriage_id: int
    person_id: int
    witness_side: WitnessSideEnum

class MarriageResponse(MarriageCreate):
    marriage_id: int
    class Config:
        from_attributes = True

class MarriageWitnessResponse(MarriageWitnessCreate):
    witness_id: int
    class Config:
        from_attributes = True