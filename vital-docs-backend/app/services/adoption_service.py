from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.adoption_repo import AdoptionRepository
from app.schemas.adoption import AdoptionCreate, AdoptionParentCreate

class AdoptionService:
    def __init__(self, db: Session):
        self.repo = AdoptionRepository(db)

    def register(self, data: AdoptionCreate):
        return self.repo.create(data)

    def get_all(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_by_id(self, adoption_id: int):
        obj = self.repo.get_by_id(adoption_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Adoption record not found")
        return obj

    def add_parent(self, data: AdoptionParentCreate):
        return self.repo.add_parent(data)

    def get_parents(self, adoption_id: int):
        return self.repo.get_parents(adoption_id)