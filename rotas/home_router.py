from fastapi import APIRouter

router = APIRouter(
    prefix="", # Prefixo para todas as rotas
    tags=["Home"], # Tag para documentação automática
)

@router.get("/")
def boas_vindas():
    return {"Mensagem": "Bem Vindo ao SGAA"}