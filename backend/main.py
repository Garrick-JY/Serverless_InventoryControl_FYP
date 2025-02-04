from fastapi import FastAPI
from backend.app.routes import inventory_routes

# Initialize FastAPI app
app = FastAPI(title="Serverless Inventory API")

# Register routes with `/api/` as the global prefix
app.include_router(inventory_routes, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the Serverless Inventory API"}
