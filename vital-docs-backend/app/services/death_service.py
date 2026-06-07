from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.death_repo import DeathRepository
from app.schemas.death import DeathCreate

class DeathService:
    def __init__(self, db: Session):
        self.repo = DeathRepository(db)

    def register(self, data: DeathCreate):
        return self.repo.create(data)

    def get_all(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_by_id(self, death_id: int):
        obj = self.repo.get_by_id(death_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Death record not found")
        return obj