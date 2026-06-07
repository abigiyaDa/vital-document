import enum
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from app.core.database import Base

class InformantRelationshipEnum(str, enum.Enum):
    spouse    = "spouse"
    parent    = "parent"
    child     = "child"
    sibling   = "sibling"
    relative  = "relative"
    neighbour = "neighbour"
    authority = "authority"
    other     = "other"

class Death(Base):
    __tablename__ = "death"
    death_id               = Column(Integer, primary_key=True, autoincrement=True)
    reg_id                 = Column(Integer, ForeignKey("registration.reg_id"), nullable=False)
    person_id              = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    death_date             = Column(Date, nullable=False)
    death_place            = Column(String(200), nullable=False)
    cause_of_death         = Column(String(500))
    informant_person_id    = Column(Integer, ForeignKey("person.person_id"))
    informant_relationship = Column(Enum(InformantRelationshipEnum))
    evidence_id            = Column(Integer, ForeignKey("evidence.evidence_id"))