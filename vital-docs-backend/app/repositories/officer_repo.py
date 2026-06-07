from sqlalchemy.orm import Session
from app.models.officer import Officer
from app.schemas.officer import OfficerUpdate

class OfficerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: Officer) -> Officer:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, officer_id: int) -> Officer | None:
        return self.db.query(Officer).filter(Officer.officer_id == officer_id).first()

    def get_by_username(self, username: str) -> Officer | None:
        return self.db.query(Officer).filter(Officer.username == username).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Officer]:
        return self.db.query(Officer).offset(skip).limit(limit).all()

    def update(self, officer_id: int, data: OfficerUpdate) -> Officer | None:
        obj = self.get_by_id(officer_id)
        if not obj:
            return None
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(obj, field, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, officer_id: int) -> bool:
        obj = self.get_by_id(officer_id)
        if not obj:
            return False
        self.db.delete(obj)
        self.db.commit()
        return True