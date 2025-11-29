import sqlite3

# Conecta ao banco (e cria o arquivo se não existir)
banco = sqlite3.connect("Banco_escolar.db")

# Cursor é a ferramenta que executa comandos no banco
cursor = banco.cursor()

# Criação da tabela com estrutura profissional
cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    sexo TEXT,
    curso TEXT,
    contato TEXT
)
""")

# Inserção segura usando parâmetros
cursor.execute("INSERT INTO Alunos (nome, idade, sexo, curso, contato) VALUES ('Fernando de Noronha', 90, 'Masculino', 'ADS', '11999834245')")

# Grava as alterações
banco.commit()

# Fecha a conexão
banco.close()
