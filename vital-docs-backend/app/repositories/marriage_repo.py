from sqlalchemy.orm import Session
from app.models.marriage import Marriage
from app.models.marriage_witness import MarriageWitness
from app.schemas.marriage import MarriageCreate, MarriageWitnessCreate

class MarriageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: MarriageCreate) -> Marriage:
        obj = Marriage(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, marriage_id: int) -> Marriage | None:
        return self.db.query(Marriage).filter(Marriage.marriage_id == marriage_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Marriage]:
        return self.db.query(Marriage).offset(skip).limit(limit).all()

    def add_witness(self, data: MarriageWitnessCreate) -> MarriageWitness:
        obj = MarriageWitness(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_witnesses(self, marriage_id: int) -> list[MarriageWitness]:
        return self.db.query(MarriageWitness).filter(MarriageWitness.marriage_id == marriage_id).all()