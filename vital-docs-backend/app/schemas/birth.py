from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional
from app.models.birth import AttendantEnum
from app.models.birth_parent import RelationshipTypeEnum

class BirthCreate(BaseModel):
    reg_id: int
    child_id: int
    birth_date: date
    birth_place: str
    birth_weight_kg: Optional[Decimal] = None
    attendant_profession: Optional[AttendantEnum] = None
    evidence_id: Optional[int] = None

class BirthParentCreate(BaseModel):
    birth_id: int
    mother_id: Optional[int] = None
    father_id: Optional[int] = None
    relationship_type: RelationshipTypeEnum = RelationshipTypeEnum.biological
    guardian_id: Optional[int] = None

class BirthResponse(BirthCreate):
    birth_id: int
    class Config:
        from_attributes = True

class BirthParentResponse(BirthParentCreate):
    birth_parent_id: int
    class Config:
        from_attributes = True