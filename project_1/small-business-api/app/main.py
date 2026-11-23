from fastapi import Depends, FastAPI, status
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.v1.auth import router as auth_router
from app.api.v1.customers import router as customers_router
from app.api.v1.inventory import router as inventory_router
from app.api.v1.products import router as products_router
from app.db.dependencies import get_db

app = FastAPI(
    title="Small Business Inventory API",
    description="An API for managing products, inventory, customers, invoices, and payments.",
    version="1.0.0",
)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(products_router, prefix="/api/v1")
app.include_router(inventory_router, prefix="/api/v1")
app.include_router(customers_router, prefix="/api/v1")

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
        # 503 (not 200) so load balancers / monitoring tools see the app as unhealthy.
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"database": "disconnected"},
        )

