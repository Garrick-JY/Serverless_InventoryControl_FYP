from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.db import Base

# SKU Table
class SKU(Base):
    __tablename__ = "sku"
    sku = Column(String, primary_key=True, unique=True, index=True)
    item_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    subcategory = Column(String, nullable=True)
    color = Column(String, nullable=False)
    size = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, nullable=False)
    supplier_name = Column(String, nullable=True)
    shelf_location = Column(String, nullable=True)
    date_added = Column(DateTime, default=datetime.utcnow)

    serial_numbers = relationship("SerialNumber", back_populates="sku_details")
    stock_movements = relationship("StockMovement", back_populates="sku_details")

# SerialNumber Table
class SerialNumber(Base):
    __tablename__ = "serial_number"
    serial_number = Column(String, primary_key=True, unique=True, index=True)
    sku = Column(String, ForeignKey("sku.sku"), nullable=False)
    item_name = Column(String, nullable=False)  # Automatically fetched from SKU
    date_added = Column(DateTime, default=datetime.utcnow)
    manufacturing_date = Column(DateTime, nullable=False)
    batch_number = Column(String, nullable=True)
    stock_placement = Column(String, nullable=True)

    sku_details = relationship("SKU", back_populates="serial_numbers")
    stock_movements = relationship("StockMovement", back_populates="serial_number_details")

# StockMovement Table
class StockMovement(Base):
    __tablename__ = "stock_movement"
    mid = Column(String, primary_key=True, unique=True, index=True)  # Unique movement ID
    rid = Column(String, nullable=False)  # Can reference SKU or Serial Number
    movement_type = Column(String, nullable=False)  # Add, Remove, Transfer
    quantity = Column(Integer, nullable=True)  # Relevant for SKU-based movements
    source_location = Column(String, nullable=True)
    dest_location = Column(String, nullable=True)
    request_by = Column(String, nullable=False)
    request_date = Column(DateTime, default=datetime.utcnow)
    approval_status = Column(String, nullable=True)  # Pending, Approved, Rejected
    approved_by = Column(String, nullable=True)
    approve_date = Column(DateTime, nullable=True)
    reject_reason = Column(String, nullable=True)
    executed_by = Column(String, nullable=True)
    executed_date = Column(DateTime, nullable=True)
    movement_status = Column(String, nullable=False)  # Pending, Completed
    notes = Column(String, nullable=True)

    sku_details = relationship("SKU", back_populates="stock_movements")
    serial_number_details = relationship("SerialNumber", back_populates="stock_movements")
    movement_logs = relationship("StockMovementLog", back_populates="movement_details")

# StockMovementLog Table
class StockMovementLog(Base):
    __tablename__ = "stock_movement_log"
    lid = Column(String, primary_key=True, unique=True, index=True)  # Unique log entry ID
    mid = Column(String, ForeignKey("stock_movement.mid"), nullable=False)
    action = Column(String, nullable=False)  # Initiated, Approved, Rejected
    performed_by = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String, nullable=True)

    movement_details = relationship("StockMovement", back_populates="movement_logs")
