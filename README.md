erDiagram
    ALUNO {
        string nome
        int idade
        string email
        int ano_inscricao
        int ativo
    }
    
    EXERCICIO {
        string nome
        string descricao
        int intervalo_descanso
        int series
        int repeticoes_serie
        int treino_id
    }

    TREINADOR {
        string nome
        int idade
        string email
        int ano_inscricao
        int ativo
    }

    TREINO {
        string descricao
        string dia_semana
        int aluno_id
        int treinador_id
    }

    ALUNO ||--o{ TREINO: "Executa"
    TREINADOR ||--o{ TREINO: "Orienta"
    TREINO ||--o{ EXERCICIO: "Tem"