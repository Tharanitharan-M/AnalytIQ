from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import query

app = FastAPI(title="AnalytIQ Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(query.router)