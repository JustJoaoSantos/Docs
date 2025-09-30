import sqlite3

# CREATE
conn = sqlite3.connect("contatos.db")
cursor = conn.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS Contatos(
		id INTERGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT,
		email TEXT,
		telefone TEXT
	)
''')

dados_exemplo = [
	("Joao", "Joao@email.com", "123-455-3311"),
	("Maria", "Maria@email.com", "356-192-0000")
]

cursor.executemany("INSERT INTO (Contatos (nome, email, telefone) VALUES (?, ?, ?)", dados_exemplo)

conn.commit()

# READ
cursor.execute("SELECT * FROM Contatos")

contatos = cursor.fetchall()

print("Contatos:")

for contato in contatos:
	print(contato)
	
# UPDATE
novo_telefone = "999-999-9999"
contato_id = 2

cursor.execute("UPDATE Contatos SET telefone = ? WHERE id = ?", (novo_telefone, contato_id))

conn.commit()

# DELETE
contado_id_para_excluir = 1

cursor.execute("DELETE FROM Contatos WHERE id = ?", (contado_id_para_excluir))

conn.commit()

# Fechando a conexao
conn.close()