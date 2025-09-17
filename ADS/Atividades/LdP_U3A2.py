import pandas as pd

# criar um dicionario com nomes e idades
dados = {
	"Nome": ["Alice", "Bob", "David", "Carol", "Eve"],
	"Idade": [25, 30, 22, 35, 28]
}

# Criar uma series a partir do dicionario 
serie_idades = pd.Series(dados["Idade"], index=dados["Nome"])

# Exibir a serie de idades 
print("Serie de Idades")
print(serie_idades)

# Calcular a media das idades 
media_idades = serie_idades.mean()

print("\nMedia de Idades: ", media_idades)