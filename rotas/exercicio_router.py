from fastapi import APIRouter
from modelos.exercicio_model import Exercicio
from controles import exercicio_control
from database import get_engine

router = APIRouter(
    prefix="", # Prefixo para todas as rotas
    tags=["Exercícios"], # Tag para documentação automática
)

engine = get_engine()

@router.get("/exercicios")
async def get_exercicios(pagina: int):
    return await exercicio_control.select_exercicios(engine, pagina)

@router.get("/exercicios/id/{exercicio_id}")
async def get_exercicio_id(exercicio_id: str):
    return await exercicio_control.select_exercicio_id(exercicio_id, engine)

@router.get("/exercicios/nome/{exercicio_nome}", response_model=list[Exercicio])
async def get_exercicios_dia_semana(exercicio_nome: str):
    return await exercicio_control.select_exercicios_nome(exercicio_nome, engine)

@router.post("/exercicios")
async def post_exercicio(treino_id: str, exercicio: Exercicio):
    return await exercicio_control.insert_exercicio(treino_id, exercicio, engine)

@router.delete("/exercicios/{exercicio_id}")
async def delete_exercicio(exercicio_id: str):
    return await exercicio_control.delete_exercicio(exercicio_id, engine)

@router.put("/exercicios/{exercicio_id}")
async def put_exercicio(exercicio_id: str, exercicio: Exercicio):
    return await exercicio_control.update_exercicio(exercicio_id, exercicio, engine)