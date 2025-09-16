from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os

from api.schemas.venta import VentaClienteResponse
from api.services.ss_cliente import get_clientes

router = APIRouter()
security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials):
    if credentials.username != os.getenv("API_USER2") or credentials.password != os.getenv("API_PASSWORD2"):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return credentials.username


@router.get("/Clientes", response_model=list[VentaClienteResponse])
def obtener_clientes(credentials: HTTPBasicCredentials = Depends(security)):
    verify_credentials(credentials)
    return get_clientes()