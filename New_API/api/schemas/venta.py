from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class VentaClienteResponse(BaseModel):
    """Schema for client sales data response"""
    id_cliente: int
    fecha_venta: date
    total_venta: Decimal
    
    class Config:
        from_attributes = True
