from odmantic import Model, Reference
from typing import Optional
from modelos.treino_model import Treino

class Exercicio(Model):
    nome: str
    descricao: Optional[str] = None
    intervalo_descanso: int
    series: int
    repeticoes_serie: int
    treino: Treino = Reference()