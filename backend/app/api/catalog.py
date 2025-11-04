# app/api/catalog.py
from fastapi import APIRouter
from app.db.database import SessionLocal
from app.db.models import Dataset

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.post("/seed")
def seed():
    db = SessionLocal()
    ds = Dataset(name="users", source="postgres")
    db.add(ds); db.commit(); db.refresh(ds)
    return {"id": ds.id, "name": ds.name}