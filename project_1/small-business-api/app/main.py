from app.api.v1.auth import router as auth_router
from fastapi import FastAPI
from sqlalchemy import text
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

app = FastAPI(
    title="Small Business Inventory API",
    description="An API for managing products, inventory, customers, invoices, and payments.",
    version="1.0.0",
)

app.include_router(auth_router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "message": "Welcome to the Small Business Inventory API",
        "status": "running",
    }


@app.get("/health/database")
def database_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"database": "connected"}
    except Exception:
        return {"database": "disconnected"}

