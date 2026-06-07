import enum
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from app.core.database import Base

class RegType(str, enum.Enum):
    birth = "birth"
    death = "death"
    marriage = "marriage"
    divorce = "divorce"
    adoption = "adoption"

class Registration(Base):
    __tablename__ = "registration"
    reg_id      = Column(Integer, primary_key=True, autoincrement=True)
    officer_id  = Column(Integer, ForeignKey("officer.officer_id"), nullable=False)
    reg_date    = Column(Date, nullable=False)
    reg_place   = Column(String(200), nullable=False)
    reg_type    = Column(Enum(RegType), nullable=False)