from odmantic import Model, Field

class Treinador(Model):
    nome: str
    idade: int
    email: str
    ano_inscricao: int
    ativo: int = Field(default=1)