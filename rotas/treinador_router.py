from fastapi import APIRouter
from modelos.treinador_model import Treinador
from database import get_engine
from controles import treinador_control

router = APIRouter(
    prefix="", # Prefixo para todas as rotas
    tags=["Treinadores"], # Tag para documentação automática
)

engine = get_engine()

@router.post("/treinadores")
async def post_treinador(treinador: Treinador):
    return await treinador_control.insert_treinador(treinador, engine)

@router.get("/treinadores/quantidade")
async def get_treinadores_quantidade():
    return await treinador_control.select_quantidade_treinadores(engine)

@router.get("/treinadores/id/{treinador_id}")
async def get_treinador_id(treinador_id: str):
    return await treinador_control.select_treinador_id(treinador_id, engine)

@router.get("/treinadores/nome/{treinador_nome}", response_model=Treinador)
async def get_treinadores_nome(treinador_nome: str):
    return await treinador_control.select_treinadores_nome(treinador_nome, engine)

@router.get("/treinadores/idade/{treinador_idade}")
async def get_treinador_idade(treinador_idade: int):
    return await treinador_control.select_treinadores_idade(treinador_idade, engine)

@router.get("/treinadores/nome/{treinador_nome}/idade/{treinador_idade}")
async def get_treinador_nome_idade(treinador_nome: str, treinador_idade: int):
    return await treinador_control.select_treinadores_nome_idade(treinador_nome, treinador_idade, engine)

@router.get("/treinadores/ano/{ano_inscricao}")
async def get_treinador_ano_inscricao(ano_inscricao: int):
    return await treinador_control.select_treinadores_ano_inscricao(ano_inscricao, engine)

@router.get("/treinadores/")
async def get_treinadores(pagina: int):
    return await treinador_control.select_treinadores(engine, pagina)

@router.delete("/treinadores/{treinador_id}")
async def delete_treinador(treinador_id: str):
    return treinador_control.delete_treinador(treinador_id, engine)

@router.put("/treinadores/{treinador_id}")
async def put_treinador(treinador_id: str, treinador: Treinador):
    return treinador_control.update_treinador(treinador_id, treinador, engine)