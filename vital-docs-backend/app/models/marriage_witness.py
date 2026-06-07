import enum
from sqlalchemy import Column, Integer, Enum, ForeignKey
from app.core.database import Base

class WitnessSideEnum(str, enum.Enum):
    bride   = "bride"
    groom   = "groom"
    neutral = "neutral"

class MarriageWitness(Base):
    __tablename__ = "marriage_witness"
    witness_id   = Column(Integer, primary_key=True, autoincrement=True)
    marriage_id  = Column(Integer, ForeignKey("marriage.marriage_id"), nullable=False)
    person_id    = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    witness_side = Column(Enum(WitnessSideEnum), nullable=False)