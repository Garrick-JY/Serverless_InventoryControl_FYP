from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.db import Base

# SKU Table
class SKU(Base):
    __tablename__ = "sku"
    sku = Column(String(50), primary_key=True, unique=True, index=True)  # Specify length
    item_name = Column(String(255), nullable=False)  # Specify length
    category = Column(String(100), nullable=False)  # Specify length
    subcategory = Column(String(100), nullable=True)  # Specify length
    color = Column(String(50), nullable=False)  # Specify length
    size = Column(String(50), nullable=False)  # Specify length
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, nullable=False)
    supplier_name = Column(String(255), nullable=True)  # Specify length
    shelf_location = Column(String(100), nullable=True)  # Specify length
    date_added = Column(DateTime, default=datetime.utcnow)

    serial_numbers = relationship("SerialNumber", back_populates="sku_details")
    stock_movements = relationship("StockMovement", back_populates="sku_details")

# SerialNumber Table
class SerialNumber(Base):
    __tablename__ = "serial_number"
    serial_number = Column(String(50), primary_key=True, unique=True, index=True)  # Specify length
    sku = Column(String(50), ForeignKey("sku.sku"), nullable=False)  # Match length of SKU.sku
    item_name = Column(String(255), nullable=False)  # Specify length
    date_added = Column(DateTime, default=datetime.utcnow)
    manufacturing_date = Column(DateTime, nullable=False)
    batch_number = Column(String(50), nullable=True)  # Specify length
    stock_placement = Column(String(100), nullable=True)  # Specify length

    sku_details = relationship("SKU", back_populates="serial_numbers")
    stock_movements = relationship("StockMovement", back_populates="serial_number_details")

# StockMovement Table
class StockMovement(Base):
    __tablename__ = "stock_movement"
    mid = Column(String(50), primary_key=True, unique=True, index=True)  # Specify length
    sku = Column(String(50), ForeignKey("sku.sku"), nullable=True)  # Match length of SKU.sku
    serial_number = Column(String(50), ForeignKey("serial_number.serial_number"), nullable=True)  # Match length
    movement_type = Column(String(50), nullable=False)  # Specify length
    quantity = Column(Integer, nullable=True)
    source_location = Column(String(100), nullable=True)  # Specify length
    dest_location = Column(String(100), nullable=True)  # Specify length
    request_by = Column(String(255), nullable=False)  # Specify length
    request_date = Column(DateTime, default=datetime.utcnow)
    approval_status = Column(String(50), nullable=True)  # Specify length
    approved_by = Column(String(255), nullable=True)  # Specify length
    approve_date = Column(DateTime, nullable=True)
    reject_reason = Column(String(255), nullable=True)  # Specify length
    executed_by = Column(String(255), nullable=True)  # Specify length
    executed_date = Column(DateTime, nullable=True)
    movement_status = Column(String(50), nullable=False)  # Specify length
    notes = Column(String(500), nullable=True)  # Specify length

    sku_details = relationship("SKU", back_populates="stock_movements")
    serial_number_details = relationship("SerialNumber", back_populates="stock_movements")
    movement_logs = relationship("StockMovementLog", back_populates="movement_details")

# StockMovementLog Table
class StockMovementLog(Base):
    __tablename__ = "stock_movement_log"
    lid = Column(String(50), primary_key=True, unique=True, index=True)  # Specify length
    mid = Column(String(50), ForeignKey("stock_movement.mid"), nullable=False)  # Match length
    action = Column(String(50), nullable=False)  # Specify length
    performed_by = Column(String(255), nullable=False)  # Specify length
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String(500), nullable=True)  # Specify length

    movement_details = relationship("StockMovement", back_populates="movement_logs")
