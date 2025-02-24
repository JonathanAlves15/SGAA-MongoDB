from fastapi import FastAPI
from rotas import aluno_router, treino_router, exercicio_router, home_router, treinador_router

app = FastAPI()

app.title = "Sistema de Gerenciamento de Alunos em Academias"

app.include_router(aluno_router.router)
app.include_router(home_router.router)
app.include_router(treino_router.router)
app.include_router(exercicio_router.router)
app.include_router(treinador_router.router)