from fastapi import FastAPI

app = FastAPI(
    title="Small Business Inventory API",
    description="An API for managing products, inventory, customers, invoices, and payments.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Small Business Inventory API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
