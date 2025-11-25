# Importacao de bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3 as sq3

# 1. gerar e conectar a um banco de dados
conn = sq3.connect('vendas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        data_venda DATE,
        produto TEXT,
        categoria TEXT,
        valor_venda REAL
    )
''')

# 2. Insercao de dados 
cursor.execute('''
    INSERT INTO vendas (data_venda, produto, categoria, valor_venda) VALUES
        ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
        ('2023-01-05', 'Produto B', 'Roupas', 350.00),
        ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
        ('2023-03-15', 'Produto D', 'Livros', 200.00),
        ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
        ('2023-04-02', 'Produto F', 'Roupas', 400.00),
        ('2023-05-05', 'Produto G', 'Livros', 150.00),
        ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
        ('2023-07-20', 'Produto I', 'Roupas', 600.00),
        ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
        ('2023-09-30', 'Produto K', 'Livros', 300.00),
        ('2023-10-05', 'Produto L', 'Roupas', 450.00),
        ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
        ('2023-12-20', 'Produto N', 'Livros', 250.00);
''')
conn.commit()

# recuperar e preparar dados 
cursor.execute("SELECT * FROM vendas")
vendas = cursor.fetchall()

# fechar conexao
conn.close()

# Criacao de DataFrame para calculos e geracao de grafico
df_vendas = pd.DataFrame(vendas)
df_vendas.rename(columns={1:'data_venda', 2:'produto', 3:'categoria', 4:'valor_venda'}, inplace=True)

# remover duplicatas se necessario
df_vendas.drop_duplicates(keep='last', inplace=True) 
print(df_vendas) # dados brutos


sns.set_theme('paper', 'whitegrid')
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(data=df_vendas, x='produto', y='valor_venda', ax=ax[0])
sns.barplot(data=df_vendas, x='categoria', y='valor_venda', ax=ax[1])
plt.show()

# Criacao de grafico, Vendas por Categoria
'''
sns.set_theme('paper', 'whitegrid')
plt.figure(figsize=(12, 5))
sns.barplot(x='categoria', y='valor_venda', data=df_vendas) # Vendas: Valor por categoria
plt.xlabel('Categoria')
plt.ylabel('Valor da Venda')
plt.title('Valor por Categoria')
plt.show()

#Produto mais vendidos
sns.set_theme('paper', 'whitegrid')
plt.figure(figsize=(10, 5))
sns.barplot(x='produto', y='valor_venda', data=df_vendas) # Vendas: Valor por categoria
plt.xlabel('Produto')
plt.ylabel('Valor da Venda')
plt.title('Valor por Produto')
plt.show()

'''



