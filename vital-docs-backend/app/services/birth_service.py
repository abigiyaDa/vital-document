from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.birth_repo import BirthRepository
from app.schemas.birth import BirthCreate, BirthParentCreate

class BirthService:
    def __init__(self, db: Session):
        self.repo = BirthRepository(db)

    def register(self, data: BirthCreate):
        return self.repo.create(data)

    def get_all(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_by_id(self, birth_id: int):
        obj = self.repo.get_by_id(birth_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Birth record not found")
        return obj

    def add_parent(self, data: BirthParentCreate):
        if not self.repo.get_by_id(data.birth_id):
            raise HTTPException(status_code=404, detail="Birth record not found")
        return self.repo.create_parent(data)

    def get_parents(self, birth_id: int):
        return self.repo.get_parents_by_birth(birth_id)