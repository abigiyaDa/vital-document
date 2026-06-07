from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.person_repo import PersonRepository
from app.schemas.person import PersonCreate, PersonUpdate

class PersonService:
    def __init__(self, db: Session):
        self.repo = PersonRepository(db)

    def create(self, data: PersonCreate):
        return self.repo.create(data)

    def get_all(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_by_id(self, person_id: int):
        obj = self.repo.get_by_id(person_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Person not found")
        return obj

    def update(self, person_id: int, data: PersonUpdate):
        obj = self.repo.update(person_id, data)
        if not obj:
            raise HTTPException(status_code=404, detail="Person not found")
        return obj

    def delete(self, person_id: int):
        if not self.repo.delete(person_id):
            raise HTTPException(status_code=404, detail="Person not found")