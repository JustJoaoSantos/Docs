import sqlite3 as sq3

# 1. conectar ao banco de dados
conn = sq3.connect('funcionarios.db')

# 2. criar tabela de funcionarios 
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTERGER PRIMARY KEY,
        nome TEXT,
        cargo TEXT,
        salario REAL
    )

''')

# 3. Inserir novos dados 
novo_funcionario = (5, "john", "Analista", 5000.00)

cursor.execute("INSERT INTO funcionarios VALUES(?, ?, ?, ?)", novo_funcionario)

conn.commit()

# 4. consultar e exibir dados
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

print("Funcionarios Cadastrados")

for funcionario in funcionarios:
    print(funcionario)
    
# 5. atualizacao de dados
atualizacao = ("John", 5500.00, 3)

cursor.execute("UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?", atualizacao)
conn.commit()

# 5. deletar dados 
exclusao = 1

cursor.execute("DELETE FROM funcionarios WHERE id = ?", (exclusao,))

conn.commit()

# 6. fechando conexao
conn.close()