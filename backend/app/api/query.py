from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/query", tags=["query"])
class QueryIn(BaseModel):
    prompt: str

@router.post("/run")
def run_query(body: QueryIn):
    # placeholder mapping for demo
    sql = "SELECT date_trunc('month', NOW()) as month, 1234 as total;"
    rows = [{"month": "2025-01-01", "total": 1234}]
    return {"prompt": body.prompt, "sql": sql, "rows": rows}

@router.get("/test")
def test_query():
    return {"ok": True, "message": "Query endpoint working"}

