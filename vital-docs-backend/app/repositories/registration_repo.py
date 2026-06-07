from sqlalchemy.orm import Session
from app.models.registration import Registration
from app.schemas.registration import RegistrationCreate

class RegistrationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: RegistrationCreate) -> Registration:
        obj = Registration(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, reg_id: int) -> Registration | None:
        return self.db.query(Registration).filter(Registration.reg_id == reg_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Registration]:
        return self.db.query(Registration).offset(skip).limit(limit).all()