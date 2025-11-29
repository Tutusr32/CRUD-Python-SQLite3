import sqlite3

try:
    banco = sqlite3.connect("Banco_escolar.db")
    cursor = banco.cursor()

    # Faz o UPDATE que troca a idade de acordo com o nome.
    cursor.execute(
        "UPDATE Alunos SET idade = ? WHERE nome = ?",
        (43, 'Fernando de Noronha')
    )

    # Rowcount é para contar a quantidade de linhas, se = 0, não deletou nenhuma linha
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado. Verifique o nome.")
    else:
        print(f"{cursor.rowcount} registro(s) atualizado(s).")

    banco.commit()

except sqlite3.Error as e:
    print("Erro no banco:", e)

finally:
    banco.close()
