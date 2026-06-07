from sqlalchemy.orm import Session
from app.models.evidence import Evidence
from app.schemas.evidence import EvidenceCreate

class EvidenceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: EvidenceCreate) -> Evidence:
        obj = Evidence(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, evidence_id: int) -> Evidence | None:
        return self.db.query(Evidence).filter(Evidence.evidence_id == evidence_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Evidence]:
        return self.db.query(Evidence).offset(skip).limit(limit).all()