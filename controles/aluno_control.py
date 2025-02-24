from modelos.aluno_model import Aluno
from modelos.treinador_model import Treinador
from odmantic import AIOEngine, ObjectId
from fastapi import HTTPException

limit = 2

async def insert_aluno(treinador_id: list[str], aluno: Aluno, engine: AIOEngine):
    """
    Insere um novo aluno.
    """
    for id in treinador_id:
        treinador = await engine.find_one(Treinador, Treinador.id == ObjectId(id))

        if not treinador:
            raise HTTPException(status_code=404, detail="Treinador não encontrado.")
        
        aluno.treinadores.append(treinador)
    
    await engine.save(aluno)

async def select_alunos(
    engine: AIOEngine, 
    skip: int = 0,
) -> list[Aluno]:
    """
    Busca e retorna todos os alunos.
    """
    alunos = await engine.find(Aluno, skip=skip, limit=limit)

    if not alunos:
        raise HTTPException(status_code=404, detail="Nenhum aluno encontrado.")
    
    return alunos

async def select_alunos_nome(aluno_nome: str, engine: AIOEngine) -> list[Aluno]:
    #alunos = await engine.find(Aluno, Aluno.nome == aluno_nome)
    """
    Seleciona um aluno pelo nome. 
    Contém busca por texto parcial.
    """
    aluno = engine.get_collection(Aluno)

    pipeline = [
        {
            "$match": {
                "nome": {
                    "$regex": f"^{aluno_nome}",
                    "$options": "i"
                }
            }
        }
    ]

    alunos = await aluno.aggregate(pipeline).to_list(length=None)

    if not alunos:
        raise HTTPException(status_code=404, detail="Nenhum aluno encontrado.")
    
    return alunos

async def select_alunos_idade(aluno_idade: int, engine: AIOEngine) -> list[Aluno]:
    """
    Busca e retorna um aluno pela idade.
    """
    alunos = await engine.find(Aluno, Aluno.idade == aluno_idade)

    if not alunos:
        raise HTTPException(status_code=404, detail="Nenhum aluno encontrado.")
    
    return alunos

async def select_alunos_nome_idade(aluno_nome: str, aluno_idade: int, engine: AIOEngine) -> list[Aluno]:
    """
    Busca de retorna um aluno pelo nome e idade.
    """
    alunos = await engine.find(Aluno, Aluno.idade == aluno_idade, Aluno.nome == aluno_nome)

    if not alunos:
        raise HTTPException(status_code=404, detail="Nenhum aluno encontrado.")
    
    return alunos

async def select_quantidade_alunos(engine: AIOEngine):
    """
    Retorna a quantidade total de todos os alunos
    """
    count = await engine.count(Aluno)

    return {"Quantidade de alunos": count}

async def select_aluno_id(aluno_id: str, engine: AIOEngine) -> Aluno:
    """
    Busca e retorna um aluno pelo id.
    """
    aluno = await engine.find_one(Aluno, Aluno.id == ObjectId(aluno_id))

    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    return aluno

async def select_alunos_ano_inscricao(ano_inscricao: str, engine: AIOEngine) -> Aluno:
    """
    Busca e retorna um aluno pelo ano de inscrição.
    """
    aluno = await engine.find_one(Aluno, Aluno.ano_inscricao == ano_inscricao)

    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    return aluno

async def delete_aluno(aluno_id: str, engine: AIOEngine):
    """
    Deleta um aluno.
    """
    aluno = await engine.find_one(Aluno, Aluno.id == ObjectId(aluno_id))

    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    await engine.delete(aluno)

async def update_aluno(aluno_id: str, aluno: Aluno, engine: AIOEngine, treinador_id: list[str] = None):
    """
    Atualiza um aluno.
    """
    aluno_db = await engine.find_one(Aluno, Aluno.id == ObjectId(aluno_id))

    if not aluno_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    aluno_db.nome = aluno.nome
    aluno_db.idade = aluno.idade
    aluno_db.email = aluno.email
    aluno_db.ativo = aluno.ativo

    if treinador_id:
        treinadores: list[Treinador] = []

        for id in treinador_id:
            treinador = await engine.find_one(Treinador, Treinador.id == ObjectId(id))
        
            if not treinador:
                raise HTTPException(status_code=404, detail="Treinador não encontrado.")
        
            treinadores.append(treinador)
        
        aluno_db.treinadores = treinadores
    
    await engine.save(aluno_db)