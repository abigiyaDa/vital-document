from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.marriage_repo import MarriageRepository
from app.schemas.marriage import MarriageCreate, MarriageWitnessCreate

class MarriageService:
    def __init__(self, db: Session):
        self.repo = MarriageRepository(db)

    def register(self, data: MarriageCreate):
        return self.repo.create(data)

    def get_all(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_by_id(self, marriage_id: int):
        obj = self.repo.get_by_id(marriage_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Marriage record not found")
        return obj

    def add_witness(self, data: MarriageWitnessCreate):
        return self.repo.add_witness(data)

    def get_witnesses(self, marriage_id: int):
        return self.repo.get_witnesses(marriage_id)