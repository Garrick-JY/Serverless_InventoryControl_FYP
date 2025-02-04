from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db import get_db
from backend.app.models import SKU, SerialNumber, StockMovement, StockMovementLog
from backend.app.schema import (
    SKUCreate,
    SKUResponse,
    SerialNumberCreate,
    SerialNumberResponse,
    StockMovementCreate,
    StockMovementResponse,
    StockMovementLogCreate,
    StockMovementLogResponse,
)

inventory_routes = APIRouter()

# Create SKU
@inventory_routes.post("/sku", response_model=SKUResponse)
def create_sku(sku: SKUCreate, db: Session = Depends(get_db)):
    # Check if SKU already exists
    existing_sku = db.query(SKU).filter(SKU.sku == sku.sku).first()
    if existing_sku:
        raise HTTPException(status_code=400, detail="SKU already exists")

    new_sku = SKU(**sku.dict())
    db.add(new_sku)
    db.commit()
    db.refresh(new_sku)
    return new_sku

# Create Serial Number
@inventory_routes.post("/serial-number", response_model=SerialNumberResponse)
def create_serial_number(serial: SerialNumberCreate, db: Session = Depends(get_db)):
    # Check if Serial Number already exists
    existing_serial = db.query(SerialNumber).filter(SerialNumber.serial_number == serial.serial_number).first()
    if existing_serial:
        raise HTTPException(status_code=400, detail="Serial Number already exists")

    new_serial = SerialNumber(**serial.dict())
    db.add(new_serial)
    db.commit()
    db.refresh(new_serial)
    return new_serial
