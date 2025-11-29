Sistema de Estudos — SQLite + Python

CRUD completo para aprendizagem de banco de dados

Este repositório reúne meus estudos práticos com SQLite utilizando Python, cobrindo operações de SELECT, INSERT, UPDATE e DELETE.
Os exemplos seguem boas práticas, incluindo comandos parametrizados, tratamento de erros e verificação de impacto das operações.

O objetivo é consolidar fundamentos de CRUD e criar base sólida para evoluir futuramente para MySQL.

Tecnologias Utilizadas

Python 3

SQLite3 (módulo nativo)

Funcionalidades Implementadas
SELECT com filtros

Consultas com parâmetros

Uso correto de fetchall()

Impressão formatada dos resultados

UPDATE com segurança

Atualização usando placeholders

Verificação de linhas afetadas

Tratamento de erro básico

DELETE com controle de impacto

Exclusão parametrizada

Feedback caso nenhum registro seja removido

Exemplos de Código
SELECT com parâmetros
cursor.execute(
    "SELECT * FROM Alunos WHERE curso = ? AND idade > ?",
    ('EET', 30)
)
alunos = cursor.fetchall()

UPDATE
cursor.execute(
    "UPDATE Alunos SET idade = ? WHERE nome = ?",
    (43, "Fernando de Noronha")
)

DELETE
cursor.execute(
    "DELETE FROM Alunos WHERE nome = ?",
    ("Roberto Silva",)
)

Boas Práticas Aplicadas

Uso de placeholders para evitar SQL injection

Parâmetros sempre em tupla

Tratamento simples de exceções

Acompanhamento do impacto das operações via rowcount

Commit e fechamento garantidos

Estrutura do Repositório
/projeto_sqlite
│── select.py
│── update.py
│── delete.py
└── Banco_escolar.db

Objetivo do Projeto

Criar entendimento sólido sobre manipulação de bancos de dados usando Python, preparar terreno para bancos relacionais mais robustos (como MySQL) e construir código consistente, direto e organizado.
