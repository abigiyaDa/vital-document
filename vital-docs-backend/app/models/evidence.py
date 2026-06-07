import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class DocTypeEnum(str, enum.Enum):
    hospital_record     = "hospital_record"
    court_order         = "court_order"
    church_certificate  = "church_certificate"
    id_document         = "id_document"
    photo               = "photo"
    other               = "other"

class Evidence(Base):
    __tablename__ = "evidence"
    evidence_id  = Column(Integer, primary_key=True, autoincrement=True)
    file_url     = Column(String(500), nullable=False)
    doc_type     = Column(Enum(DocTypeEnum), nullable=False)
    uploaded_by  = Column(Integer, ForeignKey("officer.officer_id"), nullable=False)
    uploaded_at  = Column(DateTime, server_default=func.now())