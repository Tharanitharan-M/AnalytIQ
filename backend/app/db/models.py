from sqlalchemy import Column, Integer, String, DateTime, func, Numeric
from app.db.database import Base

class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    source = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    amount = Column(Numeric(10,2))
    status = Column(String, index=True)
    created_at = Column(DateTime, server_default=func.now())