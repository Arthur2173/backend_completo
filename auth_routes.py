from fastapi import APIRouter

#rotas auth

auth_router = APIRouter(prefix="/auth",tags=["auth"])


@auth_router.get("/")
async def auth():
    """
    esse é uma rota de autenticação
    """
    return {}