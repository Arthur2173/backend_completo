from pydantic import BaseModel
from typing import Optional

class UsuariosSchema(BaseModel):

    nome:str
    email: str
    senha: str
    ativo : Optional[bool]
    admin : Optional[bool]

    class Config:
        from__attributes = True
