from fastapi import APIRouter
from modelos.treino_model import Treino
from controles import treino_control
from database import get_engine

router = APIRouter(
    prefix="", # Prefixo para todas as rotas
    tags=["Treinos"], # Tag para documentação automática
)

engine = get_engine()

@router.get("/treinos")
async def get_treinos(pagina: int):
    return await treino_control.select_treinos(engine, pagina)

@router.get("/treinos/id{treino_id}")
async def get_treino_id(treino_id: str):
    return await treino_control.select_treino_id(treino_id, engine)

@router.get("/treinos/dia/{dia_semana}")
async def get_treinos_dia_semana(dia_semana: str):
    return await treino_control.select_treinos_dia_semana(dia_semana, engine)

@router.post("/treinos")
async def post_treino(aluno_id: str, treinador_id: str, treino: Treino):
    return await treino_control.insert_treino(aluno_id, treinador_id, treino, engine)

@router.delete("/treinos/{treino_id}")
async def delete_treino(treino_id: str):
    return await treino_control.delete_treino(treino_id, engine)

@router.put("/treinos/{treino_id}")
async def put_treino(treino_id: str, treino: Treino):
    return await treino_control.update_treino(treino_id, treino, engine)