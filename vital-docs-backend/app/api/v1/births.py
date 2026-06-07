from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_officer
from app.services.birth_service import BirthService
from app.schemas.birth import BirthCreate, BirthParentCreate, BirthResponse, BirthParentResponse

router = APIRouter()

@router.post("/", response_model=BirthResponse)
def register(data: BirthCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return BirthService(db).register(data)

@router.get("/", response_model=list[BirthResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return BirthService(db).get_all(skip, limit)

@router.get("/{birth_id}", response_model=BirthResponse)
def get_one(birth_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return BirthService(db).get_by_id(birth_id)

@router.post("/{birth_id}/parents", response_model=BirthParentResponse)
def add_parent(birth_id: int, data: BirthParentCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    data.birth_id = birth_id
    return BirthService(db).add_parent(data)

@router.get("/{birth_id}/parents", response_model=list[BirthParentResponse])
def get_parents(birth_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return BirthService(db).get_parents(birth_id)