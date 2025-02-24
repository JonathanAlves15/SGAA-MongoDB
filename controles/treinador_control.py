from modelos.treinador_model import Treinador
from odmantic import AIOEngine, ObjectId
from fastapi import HTTPException

limit = 2

async def insert_treinador(treinador: Treinador, engine: AIOEngine):
    """
    Insere um novo treinador.
    """
    await engine.save(treinador)

async def select_treinadores(engine: AIOEngine, skip: int = 0) -> list[Treinador]:
    """
    Busca e retorna todos os treinadores.
    """
    treinadores = await engine.find(Treinador, skip=skip, limit=limit)

    if not treinadores:
        raise HTTPException(status_code=404, detail="Nenhum treinador encontrado.")
    
    return treinadores

async def select_treinadores_nome(treinador_nome: str, engine: AIOEngine) -> list[Treinador]:
    """
    Busca e retorna treinadores pelo nome.
    """
    treinadores = await engine.find(Treinador, Treinador.nome == treinador_nome)

    if not treinadores:
        raise HTTPException(status_code=404, detail="Nenhum treinador encontrado.")
    
    return treinadores

async def select_treinadores_idade(treinador_idade: int, engine: AIOEngine) -> list[Treinador]:
    """
    Busca e retorna treinadores pela idade.
    """
    treinadores = await engine.find(Treinador, Treinador.idade == treinador_idade)

    if not treinadores:
        raise HTTPException(status_code=404, detail="Nenhum treinador encontrado.")
    
    return treinadores

async def select_treinadores_nome_idade(treinador_nome: str, treinador_idade: int, engine: AIOEngine) -> list[Treinador]:
    """
    Busca e retorna treinadores pelo nome e idade.
    """
    treinadores = await engine.find(
        Treinador, 
        Treinador.idade == treinador_idade, 
        Treinador.nome == treinador_nome
    )

    if not treinadores:
        raise HTTPException(status_code=404, detail="Nenhum treinador encontrado.")
    
    return treinadores

async def select_treinadores_ano_inscricao(ano_inscricao: str, engine: AIOEngine) -> Treinador:
    """
    Busca e retorna treinadores pelo ano de inscrição.
    """
    treinador = await engine.find_one(Treinador, Treinador.ano_inscricao == ano_inscricao)

    if not treinador:
        raise HTTPException(status_code=404, detail="Treinador não encontrado.")
    
    return treinador

async def select_quantidade_treinadores(engine: AIOEngine):
    """
    Retorna o número total de todos os treinadores.
    """
    count = await engine.count(Treinador)
    return {"Quantidade de treinadores": count}

async def select_treinador_id(treinador_id: str, engine: AIOEngine) -> Treinador:
    """
    Busca e retorna um treinador pelo id.
    """
    treinador = await engine.find_one(Treinador, Treinador.id == ObjectId(treinador_id))

    if not treinador:
        raise HTTPException(status_code=404, detail="Treinador não encontrado.")
    
    return treinador

async def delete_treinador(treinador_id: str, engine: AIOEngine):
    """
    Deleta um treinador.
    """
    treinador = await engine.find_one(Treinador, Treinador.id == ObjectId(treinador_id))

    if not treinador:
        raise HTTPException(status_code=404, detail="Treinador não encontrado.")
    
    await engine.delete(treinador)
    return {"Mensagem": "Treinador deletado"}

async def update_treinador(treinador_id: str, treinador: Treinador, engine: AIOEngine) -> Treinador:
    """
    Atualiza um treinador.
    """
    treinador_db = await engine.find_one(Treinador, Treinador.id == ObjectId(treinador_id))

    if not treinador_db:
        raise HTTPException(status_code=404, detail="Treinador não encontrado.")
    
    treinador_db.nome = treinador.nome
    treinador_db.idade = treinador.idade
    treinador_db.email = treinador.email
    treinador_db.ativo = treinador.ativo
    
    await engine.save(treinador_db)
    return treinador_db