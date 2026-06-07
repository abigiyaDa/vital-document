from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_officer
from app.services.death_service import DeathService
from app.schemas.death import DeathCreate, DeathResponse

router = APIRouter()

@router.post("/", response_model=DeathResponse)
def register(data: DeathCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return DeathService(db).register(data)

@router.get("/", response_model=list[DeathResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return DeathService(db).get_all(skip, limit)

@router.get("/{death_id}", response_model=DeathResponse)
def get_one(death_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return DeathService(db).get_by_id(death_id)