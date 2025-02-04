from fastapi import FastAPI
from backend.app.routes import inventory_routes
from backend.app.db import Base, engine  # Adjust import paths as necessary
from backend.app.models import SKU, SerialNumber, StockMovement, StockMovementLog

# Initialize FastAPI app
app = FastAPI(title="Serverless Inventory API")

# Register routes with `/api/` as the global prefix
app.include_router(inventory_routes, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the Serverless Inventory API"}

# Create tables
Base.metadata.create_all(bind=engine)
