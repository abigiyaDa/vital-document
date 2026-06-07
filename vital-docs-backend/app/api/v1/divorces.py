from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_officer
from app.services.divorce_service import DivorceService
from app.schemas.divorce import DivorceCreate, DivorceResponse

router = APIRouter()

@router.post("/", response_model=DivorceResponse)
def register(data: DivorceCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return DivorceService(db).register(data)

@router.get("/", response_model=list[DivorceResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return DivorceService(db).get_all(skip, limit)

@router.get("/{divorce_id}", response_model=DivorceResponse)
def get_one(divorce_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return DivorceService(db).get_by_id(divorce_id)