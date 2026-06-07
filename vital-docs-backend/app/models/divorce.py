from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.core.database import Base

class Divorce(Base):
    __tablename__ = "divorce"
    divorce_id   = Column(Integer, primary_key=True, autoincrement=True)
    reg_id       = Column(Integer, ForeignKey("registration.reg_id"), nullable=False)
    marriage_id  = Column(Integer, ForeignKey("marriage.marriage_id"), nullable=False)
    divorce_date = Column(Date, nullable=False)
    court_name   = Column(String(200), nullable=False)
    evidence_id  = Column(Integer, ForeignKey("evidence.evidence_id"))