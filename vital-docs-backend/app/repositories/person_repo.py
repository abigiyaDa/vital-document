from sqlalchemy.orm import Session
from app.models.person import Person
from app.schemas.person import PersonCreate, PersonUpdate

class PersonRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: PersonCreate) -> Person:
        obj = Person(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, person_id: int) -> Person | None:
        return self.db.query(Person).filter(Person.person_id == person_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Person]:
        return self.db.query(Person).offset(skip).limit(limit).all()

    def update(self, person_id: int, data: PersonUpdate) -> Person | None:
        obj = self.get_by_id(person_id)
        if not obj:
            return None
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(obj, field, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, person_id: int) -> bool:
        obj = self.get_by_id(person_id)
        if not obj:
            return False
        self.db.delete(obj)
        self.db.commit()
        return True