from fastapi import APIRouter

#rotas orders

order_router = APIRouter(prefix="/orders",tags=["orders"]) #toda rota começa com "/orders"


@order_router.get("/")
async def orders():
    return{"message": "rota para ver o pedido"} #padrão json