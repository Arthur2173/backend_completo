from models import  db
from sqlalchemy.orm import sessionmaker
def pegar_sessao():
    try:
        Session = sessionmaker(bind = db)#criar a conexão com o banco de dados
        session = Session()
        yield session #todo o codigo depois do return não funciona por isso usar o yield
    finally:
        session.close()
