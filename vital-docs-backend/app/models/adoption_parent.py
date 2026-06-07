from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class AdoptionParent(Base):
    __tablename__ = "adoption_parent"
    adoption_id = Column(Integer, ForeignKey("adoption.adoption_id"), primary_key=True)
    person_id   = Column(Integer, ForeignKey("person.person_id"), primary_key=True)