from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_officer
from app.services.officer_service import OfficerService
from app.schemas.officer import OfficerCreate, OfficerUpdate, OfficerResponse

router = APIRouter()

@router.post("/", response_model=OfficerResponse)
def create(data: OfficerCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return OfficerService(db).create(data)

@router.get("/", response_model=list[OfficerResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return OfficerService(db).get_all(skip, limit)

@router.get("/{officer_id}", response_model=OfficerResponse)
def get_one(officer_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return OfficerService(db).get_by_id(officer_id)

@router.put("/{officer_id}", response_model=OfficerResponse)
def update(officer_id: int, data: OfficerUpdate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return OfficerService(db).update(officer_id, data)

@router.delete("/{officer_id}", status_code=204)
def delete(officer_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    OfficerService(db).delete(officer_id)