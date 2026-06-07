from sqlalchemy.orm import Session
from app.models.death import Death
from app.schemas.death import DeathCreate

class DeathRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: DeathCreate) -> Death:
        obj = Death(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, death_id: int) -> Death | None:
        return self.db.query(Death).filter(Death.death_id == death_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Death]:
        return self.db.query(Death).offset(skip).limit(limit).all()