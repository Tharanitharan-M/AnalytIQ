from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.database import Base

class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    source = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())