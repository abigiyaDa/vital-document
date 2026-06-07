import enum
from sqlalchemy import Column, Integer, String, Date, Enum, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class SexEnum(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class EducationEnum(str, enum.Enum):
    none = "none"
    primary = "primary"
    secondary = "secondary"
    diploma = "diploma"
    bachelors = "bachelors"
    masters = "masters"
    phd = "phd"
    other = "other"

class Person(Base):
    __tablename__ = "person"
    person_id       = Column(Integer, primary_key=True, autoincrement=True)
    f_name          = Column(String(100), nullable=False)
    m_name          = Column(String(100))
    l_name          = Column(String(100), nullable=False)
    sex             = Column(Enum(SexEnum), nullable=False)
    date_of_birth   = Column(Date, nullable=False)
    nationality     = Column(String(100))
    religion        = Column(String(100))
    ethnicity       = Column(String(100))
    education_level = Column(Enum(EducationEnum))
    occupation      = Column(String(150))
    phone_number    = Column(String(20))
    created_at      = Column(DateTime, server_default=func.now())