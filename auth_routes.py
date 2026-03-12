from fastapi import APIRouter,Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuariosSchema, LoginSchema
from sqlalchemy.orm import Session
#rotas auth

auth_router = APIRouter(prefix="/auth",tags=["auth"])#toda rota começa com "/auth"




def criar_token(id_usuario: int ):
    token = f"dhhddlfk{id_usuario}"
    return token

def autenticar_usuario(email,senha,session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario:
        return False
    elif not  bcrypt_context.verify(senha,usuario.senha):
        return False

    return usuario 


@auth_router.get("/")
async def home():
    """
    esse é uma rota de autenticação
    """
    return {}

@auth_router.post("/conta")
async def criar_conta(usuario_schema : UsuariosSchema ,session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400,detail ="email ja cadastrado ")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome , usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"usuario cadastrado com sucesso {usuario_schema.email}"}
    
@auth_router.post("/login")# login -> email e senha -> token JWT(json web token) gera um token -> jsshdkhsdkhjd
async def login(login_schema: LoginSchema,session: Session = Depends(pegar_sessao)):

    usuario = autenticar_usuario(login_schema.email,login_schema.senha, session)
    

    if not usuario:
        raise HTTPException(status_code=400, detail = 'Usuario não encontrado ou credenciais invalidas')
    else:

        access_token = criar_token(usuario.id)
        return {
            "access_token": access_token,
            "token_type" : "Bearer"

            }
    #JWT Bearer
    #headers = { " Access-Token ": "Bearer-token"}
    





    


