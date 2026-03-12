from fastapi import APIRouter,Depends
from schemas import PedidoSchema
from dependencies import pegar_sessao
from sqlalchemy.orm import Session
from models import Pedidos



#rotas orders

order_router = APIRouter(prefix="/orders",tags=["orders"]) #toda rota começa com "/orders"


@order_router.get("/")
async def pedidos():
    return{"message": "rota para ver o pedido"} #padrão json

@order_router.post("/criar_pedido")
async def pedido(pedido_schema : PedidoSchema,session: Session = Depends(pegar_sessao) ):
    novo_pedido = Pedidos(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"pedido enviado com sucesso {novo_pedido.id}"}


