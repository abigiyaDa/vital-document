from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.evidence import DocTypeEnum

class EvidenceCreate(BaseModel):
    file_url: str
    doc_type: DocTypeEnum
    uploaded_by: int

class EvidenceResponse(EvidenceCreate):
    evidence_id: int
    uploaded_at: Optional[datetime] = None
    class Config:
        from_attributes = True