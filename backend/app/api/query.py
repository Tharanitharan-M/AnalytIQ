from fastapi import APIRouter
from pydantic import BaseModel

from sqlalchemy import text
from app.db.database import SessionLocal
from app.services.llm_service import nl_to_sql

class QueryIn(BaseModel):
    prompt: str

router = APIRouter(prefix="/query", tags=["query"])
class QueryIn(BaseModel):
    prompt: str

@router.get("/test")
def test_query():
    return {"ok": True, "message": "Query endpoint working"}


@router.post("/run_sql")
def run_sql(sql: str):
    # VERY IMPORTANT: demo only; later add whitelist/read-only validator
    db = SessionLocal()
    rows = db.execute(text(sql)).mappings().all()
    return {"rows": [dict(r) for r in rows]}

@router.post("/run")
def run_query(body: QueryIn):
    schema_hint = "orders(id, user_id, amount, status, created_at)"  # later generate this dynamically
    sql = nl_to_sql(body.prompt, schema_hint)

    # naive safety: block mutating statements
    if any(k in sql.lower() for k in ["insert","update","delete","drop","alter"]):
        return {"error":"Unsafe SQL", "sql": sql}

    db = SessionLocal()
    rows = db.execute(text(sql)).mappings().all()
    print("SQL: ", sql)
    return {"prompt": body.prompt, "sql": sql, "rows": [dict(r) for r in rows]}