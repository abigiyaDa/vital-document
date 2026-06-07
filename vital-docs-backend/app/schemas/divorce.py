from pydantic import BaseModel
from datetime import date
from typing import Optional

class DivorceCreate(BaseModel):
    reg_id: int
    marriage_id: int
    divorce_date: date
    court_name: str
    evidence_id: Optional[int] = None

class DivorceResponse(DivorceCreate):
    divorce_id: int
    class Config:
        from_attributes = True