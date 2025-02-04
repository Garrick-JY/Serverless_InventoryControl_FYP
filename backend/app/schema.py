from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Pydantic Model for SKU
class SKUCreate(BaseModel):
    sku: str = Field(..., example="PROD123REDL")
    item_name: str
    category: str
    subcategory: Optional[str] = None
    color: str
    size: str
    quantity: int = 0
    unit_price: float
    supplier_name: Optional[str] = None
    shelf_location: Optional[str] = None
    date_added: Optional[datetime] = None

class SKUResponse(SKUCreate):
    date_added: datetime

    class Config:
        orm_mode = True


# Pydantic Model for SerialNumber
class SerialNumberCreate(BaseModel):
    serial_number: str = Field(..., example="PROD123REDL001")
    sku: str
    item_name: str
    date_added: Optional[datetime] = None
    manufacturing_date: datetime
    batch_number: Optional[str] = None
    stock_placement: Optional[str] = None

class SerialNumberResponse(SerialNumberCreate):
    date_added: datetime

    class Config:
        orm_mode = True


# Pydantic Model for StockMovement
class StockMovementCreate(BaseModel):
    mid: str = Field(..., example="MOV123")
    rid: str
    movement_type: str
    quantity: Optional[int] = None
    source_location: Optional[str] = None
    dest_location: Optional[str] = None
    request_by: str
    request_date: Optional[datetime] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approve_date: Optional[datetime] = None
    reject_reason: Optional[str] = None
    executed_by: Optional[str] = None
    executed_date: Optional[datetime] = None
    movement_status: str
    notes: Optional[str] = None

class StockMovementResponse(StockMovementCreate):
    request_date: datetime

    class Config:
        orm_mode = True


# Pydantic Model for StockMovementLog
class StockMovementLogCreate(BaseModel):
    lid: str = Field(..., example="LOG001")
    mid: str
    action: str
    performed_by: str
    date: Optional[datetime] = None
    notes: Optional[str] = None

class StockMovementLogResponse(StockMovementLogCreate):
    date: datetime

    class Config:
        orm_mode = True
