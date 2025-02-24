from odmantic import Model, Reference
from modelos.aluno_model import Aluno
from modelos.treinador_model import Treinador
from typing import Optional

class Treino(Model):
    descricao: Optional[str] = None
    dia_semana: str
    aluno: Aluno = Reference()
    treinador: Treinador = Reference()