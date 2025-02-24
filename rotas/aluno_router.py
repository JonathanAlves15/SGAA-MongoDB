from fastapi import APIRouter
from modelos.aluno_model import Aluno
from database import get_engine
from controles import aluno_control

router = APIRouter(
    prefix="", # Prefixo para todas as rotas
    tags=["Alunos"], # Tag para documentação automática
)

engine = get_engine()

@router.post("/alunos")
async def post_aluno(treinador_id: list[str], aluno: Aluno):
    await aluno_control.insert_aluno(treinador_id, aluno, engine)

@router.get("/alunos/quantidade")
async def get_alunos_quantidade():
    return await aluno_control.select_quantidade_alunos(engine)

@router.get("/alunos/id/{aluno_id}", response_model=Aluno)
async def get_aluno_id(aluno_id: str):
    return await aluno_control.select_aluno_id(aluno_id, engine)

@router.get("/alunos/nome/{aluno_nome}", response_model=list[Aluno])
async def get_aluno_nome(aluno_nome: str):
    return await aluno_control.select_alunos_nome(aluno_nome, engine)

@router.get("/alunos/idade/{aluno_idade}")
async def get_aluno_iddade(aluno_idade: int):
    return await aluno_control.select_alunos_idade(aluno_idade, engine)

@router.get("/alunos/nome/{aluno_nome}/idade/{aluno_idade}")
async def get_aluno_nome_idade(aluno_nome: str, aluno_idade: int):
    return await aluno_control.select_alunos_nome_idade(aluno_nome, aluno_idade, engine)

@router.get("/alunos/ano/{ano_inscricao}")
async def get_aluno_ano_inscricao(ano_inscricao: int):
    return await aluno_control.select_alunos_ano_inscricao(ano_inscricao, engine)

@router.get("/alunos/")
async def get_alunos(pagina: int):
    return await aluno_control.select_alunos(engine, pagina)

@router.delete("/alunos/{aluno_id}")
async def delete_aluno(aluno_id: str):
    await aluno_control.delete_aluno(aluno_id, engine)

@router.put("/alunos/{aluno_id}")
async def put_aluno(aluno_id: str, aluno: Aluno, treinador_id: list[str] = None):
    await aluno_control.update_aluno(aluno_id, aluno, engine, treinador_id)