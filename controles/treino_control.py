from modelos.aluno_model import Aluno
from modelos.treinador_model import Treinador
from modelos.treino_model import Treino
from odmantic import AIOEngine, ObjectId
from fastapi import HTTPException

limit = 2

async def insert_treino(aluno_id: str, treinador_id: str, treino: Treino, engine: AIOEngine):
    """
    Insere um novo treino.
    """
    aluno = await engine.find_one(Aluno, Aluno.id == ObjectId(aluno_id))
    treinador = await engine.find_one(Treinador, Treinador.id == ObjectId(treinador_id))

    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    if not treinador:
        raise HTTPException(status_code=404, detail="Treinador não encontrado encontrado.")
    
    treino.aluno = aluno
    treino.treinador = treinador
    
    await engine.save(treino)

async def select_treinos(engine: AIOEngine, skip: int = 0) -> list[Treino]:
    """
    Busca e retorna todos os treinor.
    """
    treinos = await engine.find(Treino, skip=skip, limit=limit)

    if not treinos:
        raise HTTPException(status_code=404, detail="Nenhum treino encontrado.")
    
    return treinos

async def select_quantidade_treinos(engine: AIOEngine):
    """
    Retorna o número total de todos os treinos.
    """
    count = await engine.count(Treino)
    return {"Quantidade de treinos": count}

async def select_treino_id(treino_id: str, engine: AIOEngine) -> Treino:
    """
    Busca e retorna um treino pelo id.
    """
    treino = await engine.find_one(Treino, Treino.id == ObjectId(treino_id))

    if not treino:
        raise HTTPException(status_code=404, detail="Treino não encontrado.")
    
    return treino

async def select_treinos_dia_semana(treino_dia_semana: str, engine: AIOEngine) -> list[Treino]:
    """
    Busca e retorna um treino pelo dia da semana.
    """
    treinos = await engine.find(Treino, Treino.dia_semana == treino_dia_semana)

    if not treinos:
        raise HTTPException(status_code=404, detail="Nenhum treino encontrado.")
    
    return treinos

async def delete_treino(treino_id: str, engine: AIOEngine):
    """
    Deleta um treino.
    """
    treino = await engine.find_one(Treino, Treino.id == ObjectId(treino_id))

    if not treino:
        raise HTTPException(status_code=404, detail="Treino não encontrado.")
    
    await engine.delete(treino)

async def update_treino(treino_id: str, treino: Treino, engine: AIOEngine):
    """
    Atualiza um treino.
    """
    treino_db = await engine.find_one(Treino, Treino.id == ObjectId(treino_id))

    if not treino_db:
        raise HTTPException(status_code=404, detail="Treino não encontrado.")
    
    treino_db.descricao = treino.descricao
    treino_db.dia_semana = treino.dia_semana
    
    await engine.save(treino_db)