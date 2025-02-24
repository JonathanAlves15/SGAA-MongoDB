from odmantic import Model, Field
from modelos.treinador_model import Treinador

class Aluno(Model):
    nome: str
    idade: int
    email: str
    ano_inscricao: int
    ativo: int = Field(default=1)
    treinadores: list[Treinador] = []