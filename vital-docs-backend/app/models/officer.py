import enum
from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base

class OfficerRole(str, enum.Enum):
    admin = "admin"
    registrar = "registrar"
    viewer = "viewer"

class Officer(Base):
    __tablename__ = "officer"
    officer_id      = Column(Integer, primary_key=True, autoincrement=True)
    full_name       = Column(String(200), nullable=False)
    username        = Column(String(100), nullable=False, unique=True)
    password_hash   = Column(String(255), nullable=False)
    assigned_place  = Column(String(200))
    role            = Column(Enum(OfficerRole), nullable=False, default=OfficerRole.registrar)