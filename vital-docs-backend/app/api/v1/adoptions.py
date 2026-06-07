from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_officer
from app.services.adoption_service import AdoptionService
from app.schemas.adoption import AdoptionCreate, AdoptionParentCreate, AdoptionResponse, AdoptionParentResponse

router = APIRouter()

@router.post("/", response_model=AdoptionResponse)
def register(data: AdoptionCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return AdoptionService(db).register(data)

@router.get("/", response_model=list[AdoptionResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return AdoptionService(db).get_all(skip, limit)

@router.get("/{adoption_id}", response_model=AdoptionResponse)
def get_one(adoption_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return AdoptionService(db).get_by_id(adoption_id)

@router.post("/{adoption_id}/parents", response_model=AdoptionParentResponse)
def add_parent(adoption_id: int, data: AdoptionParentCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    data.adoption_id = adoption_id
    return AdoptionService(db).add_parent(data)

@router.get("/{adoption_id}/parents", response_model=list[AdoptionParentResponse])
def get_parents(adoption_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return AdoptionService(db).get_parents(adoption_id)