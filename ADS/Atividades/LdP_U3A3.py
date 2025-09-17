import pandas as pd

# Criando um dataframe com 5 linhas de codigo
data = {
	'nome': ['produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E'],
	'quantidade de itens comprados': [3, 5, 2, 21, 0],
	'tipo de item': ['eletronico', 'vestuario', 'alimento', 'eletronico', 'alimento'],
	'receita total': [120, 80, 60, 120, 90]
}

df = pd.DataFrame(data)
print(df)

# removendo duplicatas 
df.drop_duplicates(keep='last', inplace=True)
print(df)

# Calculando a coluna 'preco de items'
df['preco do item'] = df['receita total'] / df['quantidade de itens comprados']

# Selecionando preco do item acima de 50 reais
items_acima_de_50 = df[df['preco do item'] > 50]

print("items acima de 50 reails")
print(items_acima_de_50)