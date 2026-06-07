import enum
from sqlalchemy import Column, Integer, Enum, ForeignKey
from app.core.database import Base

class RelationshipTypeEnum(str, enum.Enum):
    biological = "biological"
    surrogate  = "surrogate"
    unknown    = "unknown"

class BirthParent(Base):
    __tablename__ = "birth_parent"
    birth_parent_id   = Column(Integer, primary_key=True, autoincrement=True)
    birth_id          = Column(Integer, ForeignKey("birth.birth_id"), nullable=False)
    mother_id         = Column(Integer, ForeignKey("person.person_id"))
    father_id         = Column(Integer, ForeignKey("person.person_id"))
    relationship_type = Column(Enum(RelationshipTypeEnum), nullable=False, default=RelationshipTypeEnum.biological)
    guardian_id       = Column(Integer, ForeignKey("person.person_id"))