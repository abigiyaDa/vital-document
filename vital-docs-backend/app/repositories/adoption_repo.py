from sqlalchemy.orm import Session
from app.models.adoption import Adoption
from app.models.adoption_parent import AdoptionParent
from app.schemas.adoption import AdoptionCreate, AdoptionParentCreate

class AdoptionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: AdoptionCreate) -> Adoption:
        obj = Adoption(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, adoption_id: int) -> Adoption | None:
        return self.db.query(Adoption).filter(Adoption.adoption_id == adoption_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Adoption]:
        return self.db.query(Adoption).offset(skip).limit(limit).all()

    def add_parent(self, data: AdoptionParentCreate) -> AdoptionParent:
        obj = AdoptionParent(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_parents(self, adoption_id: int) -> list[AdoptionParent]:
        return self.db.query(AdoptionParent).filter(AdoptionParent.adoption_id == adoption_id).all()