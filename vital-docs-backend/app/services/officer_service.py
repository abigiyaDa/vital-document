from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.officer_repo import OfficerRepository
from app.models.officer import Officer
from app.schemas.officer import OfficerCreate, OfficerUpdate
from app.core.security import hash_password

class OfficerService:
    def __init__(self, db: Session):
        self.repo = OfficerRepository(db)

    def create(self, data: OfficerCreate) -> Officer:
        if self.repo.get_by_username(data.username):
            raise HTTPException(status_code=400, detail="Username already taken")
        officer = Officer(
            full_name=data.full_name,
            username=data.username,
            password_hash=hash_password(data.password),
            assigned_place=data.assigned_place,
            role=data.role,
        )
        return self.repo.create(officer)

    def get_all(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_by_id(self, officer_id: int) -> Officer:
        obj = self.repo.get_by_id(officer_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Officer not found")
        return obj

    def update(self, officer_id: int, data: OfficerUpdate) -> Officer:
        obj = self.repo.update(officer_id, data)
        if not obj:
            raise HTTPException(status_code=404, detail="Officer not found")
        return obj

    def delete(self, officer_id: int):
        if not self.repo.delete(officer_id):
            raise HTTPException(status_code=404, detail="Officer not found")