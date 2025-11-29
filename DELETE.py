import sqlite3

try:
    banco = sqlite3.connect("Banco_escolar.db")
    cursor = banco.cursor()

    # Deleta por nome, ROBERTO SILVA da tabela. (Virgula no final da str é para não dar erro de tupla)
    cursor.execute(
        "DELETE FROM Alunos WHERE nome = ?",
        ("Roberto Silva",)
    )

    # Rowcount é para contar a quantidade de linhas, se = 0, não deletou nenhuma linha
    if cursor.rowcount == 0:
        print("Nenhum registro encontrado para deletar.")
    else:
        print(f"{cursor.rowcount} registro(s) deletado(s).")

    banco.commit()

except sqlite3.Error as e:
    print("Erro no banco:", e)

finally:
    banco.close()
