from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from app.models.person import SexEnum, EducationEnum

class PersonCreate(BaseModel):
    f_name: str
    m_name: Optional[str] = None
    l_name: str
    sex: SexEnum
    date_of_birth: date
    nationality: Optional[str] = None
    religion: Optional[str] = None
    ethnicity: Optional[str] = None
    education_level: Optional[EducationEnum] = None
    occupation: Optional[str] = None
    phone_number: Optional[str] = None

class PersonUpdate(BaseModel):
    f_name: Optional[str] = None
    m_name: Optional[str] = None
    l_name: Optional[str] = None
    sex: Optional[SexEnum] = None
    date_of_birth: Optional[date] = None
    nationality: Optional[str] = None
    religion: Optional[str] = None
    ethnicity: Optional[str] = None
    education_level: Optional[EducationEnum] = None
    occupation: Optional[str] = None
    phone_number: Optional[str] = None

class PersonResponse(PersonCreate):
    person_id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True