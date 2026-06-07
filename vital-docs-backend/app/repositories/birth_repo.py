from sqlalchemy.orm import Session
from app.models.birth import Birth
from app.models.birth_parent import BirthParent
from app.schemas.birth import BirthCreate, BirthParentCreate

class BirthRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: BirthCreate) -> Birth:
        obj = Birth(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, birth_id: int) -> Birth | None:
        return self.db.query(Birth).filter(Birth.birth_id == birth_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Birth]:
        return self.db.query(Birth).offset(skip).limit(limit).all()

    def create_parent(self, data: BirthParentCreate) -> BirthParent:
        obj = BirthParent(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_parents_by_birth(self, birth_id: int) -> list[BirthParent]:
        return self.db.query(BirthParent).filter(BirthParent.birth_id == birth_id).all()