from pydantic import BaseModel, EmailStr
from typing import Optional

class ClienteBase(BaseModel):
    nombre:str
    apellido: str
    email: EmailStr
    telefono: Optional[str]
    direccion: Optional[str]

class ClienteResponse(ClienteBase):
    id: int