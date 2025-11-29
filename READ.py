import sqlite3

try:
    banco = sqlite3.connect("Banco_escolar.db")
    cursor = banco.cursor()

    cursor.execute(
        "SELECT * FROM Alunos WHERE curso = ? AND idade > ?",
        ('EET', 30)
    )

    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print("Nenhum registro encontrado.")
    else:
        for i in alunos:
            print(i)
            # Exemplo: acessar idade i[1] já que 1 é a posição em que idade se encontra.
            # print(i[1])

except sqlite3.Error as e:
    print("Erro no banco:", e)

finally:
    banco.close()
