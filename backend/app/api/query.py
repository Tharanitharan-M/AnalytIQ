from fastapi import APIRouter

router = APIRouter(prefix="/query", tags=["query"])

@router.get("/test")
def test_query():
    return {"ok": True, "message": "Query endpoint working"}