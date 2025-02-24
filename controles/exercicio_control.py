from modelos.exercicio_model import Exercicio
from modelos.treino_model import Treino
from odmantic import AIOEngine, ObjectId
from fastapi import HTTPException

limit = 2

async def insert_exercicio(treino_id: str, exercicio: Exercicio, engine: AIOEngine):
    """
    Insere um novo exercício.
    """
    treino = await engine.find_one(Treino, Treino.id == ObjectId(treino_id))

    if not treino:
        raise HTTPException(status_code=404, detail="Treino não encontrado.")

    exercicio.treino = treino

    await engine.save(exercicio)

async def select_exercicios(engine: AIOEngine, skip: int = 0) -> list[Exercicio]:
    """
    Busca e retorna todos os exercícios.
    """
    exercicios = await engine.find(Exercicio, skip=skip, limit=limit)

    if not exercicios:
        raise HTTPException(status_code=404, detail="Nenhum exercicio encontrado.")
    
    return exercicios

async def select_quantidade_exercicios(engine: AIOEngine):
    """
    Retorna o número total de todos os exercícios.
    """
    count = await engine.count(Exercicio)
    return {"Quantidade de exercicios": count}

async def select_exercicio_id(exercicio_id: str, engine: AIOEngine) -> Exercicio:
    """
    Busca e retorna um exercício pelo id.
    """
    exercicio = await engine.find_one(Exercicio, Exercicio.id == ObjectId(exercicio_id))

    if not exercicio:
        raise HTTPException(status_code=404, detail="Exercicio não encontrado.")
    
    return exercicio

async def select_exercicios_nome(exercicio_nome: str, engine: AIOEngine) -> list[Exercicio]:
    """
    Busca e retorna exercícios pelo nome.
    """
    exercicios = await engine.find(Exercicio, Exercicio.nome == exercicio_nome)

    if not exercicios:
        raise HTTPException(status_code=404, detail="Nenhum exercicio encontrado.")
    
    return exercicios

async def delete_exercicio(exercicio_id: str, engine: AIOEngine):
    """
    Deleta um exercício.
    """
    exercicio = await engine.find_one(Exercicio, Exercicio.id == ObjectId(exercicio_id))

    if not exercicio:
        raise HTTPException(status_code=404, detail="Exercicio não encontrado.")
    
    await engine.delete(exercicio)

async def update_exercicio(exercicio_id: str, exercicio: Exercicio, engine: AIOEngine):
    """
    Atualiza um exercício.
    """
    exercicio_db = await engine.find_one(Exercicio, Exercicio.id == ObjectId(exercicio_id))

    if not exercicio_db:
        raise HTTPException(status_code=404, detail="Exercicio não encontrado.")
    
    exercicio_db.descricao = exercicio.descricao
    exercicio_db.nome = exercicio.nome
    exercicio_db.intervalo_descanso = exercicio.intervalo_descanso
    exercicio_db.series = exercicio.series
    exercicio_db.repeticoes_serie = exercicio.repeticoes_serie
    
    await engine.save(exercicio_db)