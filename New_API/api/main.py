from fastapi import FastAPI
from api.routes.cliente_route import router



api = FastAPI()

#@api.get("/")
#async def root():
#    return {"message": "Hello World"}

api.include_router(router, prefix = "/api", tags = ["Clientes"])