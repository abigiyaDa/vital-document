from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.core.database import Base

class Adoption(Base):
    __tablename__ = "adoption"
    adoption_id    = Column(Integer, primary_key=True, autoincrement=True)
    reg_id         = Column(Integer, ForeignKey("registration.reg_id"), nullable=False)
    child_id       = Column(Integer, ForeignKey("person.person_id"), nullable=False)
    adoption_date  = Column(Date, nullable=False)
    adoption_place = Column(String(200))
    evidence_id    = Column(Integer, ForeignKey("evidence.evidence_id"))