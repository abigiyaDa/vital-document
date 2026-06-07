import enum
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, Numeric, UniqueConstraint
from app.core.database import Base

class AttendantEnum(str, enum.Enum):
    doctor                   = "doctor"
    midwife                  = "midwife"
    nurse                    = "nurse"
    traditional_birth_attendant = "traditional_birth_attendant"
    none                     = "none"
    other                    = "other"

class Birth(Base):
    __tablename__ = "birth"
    birth_id             = Column(Integer, primary_key=True, autoincrement=True)
    reg_id               = Column(Integer, ForeignKey("registration.reg_id"), nullable=False, unique=True)
    child_id             = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    birth_date           = Column(Date, nullable=False)
    birth_place          = Column(String(200), nullable=False)
    birth_weight_kg      = Column(Numeric(4, 2))
    attendant_profession = Column(Enum(AttendantEnum))
    evidence_id          = Column(Integer, ForeignKey("evidence.evidence_id"))