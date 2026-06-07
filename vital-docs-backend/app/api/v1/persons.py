from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_officer
from app.services.person_service import PersonService
from app.schemas.person import PersonCreate, PersonUpdate, PersonResponse

router = APIRouter()

@router.post("/", response_model=PersonResponse)
def create(data: PersonCreate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return PersonService(db).create(data)

@router.get("/", response_model=list[PersonResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return PersonService(db).get_all(skip, limit)

@router.get("/{person_id}", response_model=PersonResponse)
def get_one(person_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return PersonService(db).get_by_id(person_id)

@router.put("/{person_id}", response_model=PersonResponse)
def update(person_id: int, data: PersonUpdate, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    return PersonService(db).update(person_id, data)

@router.delete("/{person_id}", status_code=204)
def delete(person_id: int, db: Session = Depends(get_db), _=Depends(get_current_officer)):
    PersonService(db).delete(person_id)