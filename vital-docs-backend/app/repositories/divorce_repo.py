from sqlalchemy.orm import Session
from app.models.divorce import Divorce
from app.schemas.divorce import DivorceCreate

class DivorceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: DivorceCreate) -> Divorce:
        obj = Divorce(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, divorce_id: int) -> Divorce | None:
        return self.db.query(Divorce).filter(Divorce.divorce_id == divorce_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Divorce]:
        return self.db.query(Divorce).offset(skip).limit(limit).all()