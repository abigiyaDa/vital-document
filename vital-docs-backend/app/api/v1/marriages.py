from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_officer
from app.services.marriage_service import MarriageService
from app.schemas.marriage import MarriageCreate, MarriageWitnessCreate, MarriageResponse, MarriageWitnessResponse

router = APIRouter()

@router.post("/", response_model=MarriageResponse)
def register(data: MarriageCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return MarriageService(db).register(data)

@router.get("/", response_model=list[MarriageResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return MarriageService(db).get_all(skip, limit)

@router.get("/{marriage_id}", response_model=MarriageResponse)
def get_one(marriage_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return MarriageService(db).get_by_id(marriage_id)

@router.post("/{marriage_id}/witnesses", response_model=MarriageWitnessResponse)
def add_witness(marriage_id: int, data: MarriageWitnessCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    data.marriage_id = marriage_id
    return MarriageService(db).add_witness(data)

@router.get("/{marriage_id}/witnesses", response_model=list[MarriageWitnessResponse])
def get_witnesses(marriage_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return MarriageService(db).get_witnesses(marriage_id)