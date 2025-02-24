## Diagrama

classDiagram
    class ALUNO {
        +string nome
        +int idade
        +string email
        +int ano_inscricao
        +int ativo
    }

    class EXERCICIO {
        +string nome
        +string descricao
        +int intervalo_descanso
        +int series
        +int repeticoes_serie
        +int treino_id
    }

    class TREINADOR {
        +string nome
        +int idade
        +string email
        +int ano_inscricao
        +int ativo
    }

    class TREINO {
        +string descricao
        +string dia_semana
        +int aluno_id
        +int treinador_id
    }

    ALUNO "1" -- "0..*" TREINO : participa_em
    TREINADOR "1" -- "0..*" TREINO : orienta
    TREINO "1" -- "0..*" EXERCICIO : inclui