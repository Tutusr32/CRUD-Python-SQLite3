📚 Sistema de Estudos — SQLite + Python

CRUD completo para estudos de banco de dados

Este repositório contém meus experimentos práticos com SQLite usando Python, incluindo operações de SELECT, INSERT, UPDATE e DELETE, todos seguindo boas práticas como comandos parametrizados, tratamento de erros e controle de impacto (rowcount).

O objetivo é consolidar fundamentos reais de CRUD e preparar terreno para integrações futuras com MySQL.

🚀 Tecnologias Utilizadas

Python 3

SQLite3 (nativo do Python)

📌 Funcionalidades Implementadas
✔️ SELECT com filtros

Busca com parâmetros

Uso correto de fetchall()

Retorno formatado

✔️ UPDATE seguro

Parâmetros com ?

Verificação de linhas afetadas

Tratamento de erro

✔️ DELETE com controle de impacto

Deleção parametrizada

Aviso quando nenhum registro for removido

🧠 Exemplos de Código
🔍 SELECT com parâmetros
cursor.execute(
    "SELECT * FROM Alunos WHERE curso = ? AND idade > ?",
    ('EET', 30)
)
alunos = cursor.fetchall()

✏️ UPDATE seguro
cursor.execute(
    "UPDATE Alunos SET idade = ? WHERE nome = ?",
    (43, "Fernando de Noronha")
)

❌ DELETE com tupla correta
cursor.execute(
    "DELETE FROM Alunos WHERE nome = ?",
    ("Roberto Silva",)
)

⚠️ Boas Práticas Aplicadas

Uso de placeholders para evitar SQL injection

Tuplas corretas para parâmetros

Tratamento de exceções com try/except

rowcount para saber se a operação teve impacto

commit() e close() sempre garantidos

📂 Estrutura do Repositório
/meu_projeto_sqlite
│── create.py
│── select.py
│── update.py
│── delete.py
└── Banco_escolar.db

🎯 Objetivo do Projeto

Criar uma base sólida no CRUD com SQLite, com foco em:

dominar a integração Python ↔ Banco

evoluir para MySQL e sistemas maiores

construir código limpo, seguro e profissional
