import enum
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from app.core.database import Base

class MarriageTypeEnum(str, enum.Enum):
    civil        = "civil"
    religious    = "religious"
    traditional  = "traditional"
    customary    = "customary"
    common_law   = "common_law"

class Marriage(Base):
    __tablename__ = "marriage"
    marriage_id    = Column(Integer, primary_key=True, autoincrement=True)
    reg_id         = Column(Integer, ForeignKey("registration.reg_id"), nullable=False)
    groom_id       = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    bride_id       = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    marriage_date  = Column(Date, nullable=False)
    marriage_place = Column(String(200), nullable=False)
    marriage_type  = Column(Enum(MarriageTypeEnum), nullable=False)
    evidence_id    = Column(Integer, ForeignKey("evidence.evidence_id"))