from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.divorce_repo import DivorceRepository
from app.schemas.divorce import DivorceCreate

class DivorceService:
    def __init__(self, db: Session):
        self.repo = DivorceRepository(db)

    def register(self, data: DivorceCreate):
        return self.repo.create(data)

    def get_all(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_by_id(self, divorce_id: int):
        obj = self.repo.get_by_id(divorce_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Divorce record not found")
        return obj