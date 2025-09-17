# tupla
convidados = ("john", "alexandria", "maria")

# lista de confirmados
confirmados = ["john", "maria"]

# identificar quem ainda nao confirmou
nao_confirmados = [convidados for convidado in convidados if convidado not in confirmados]

# exibir os convidados que ainda nao confirmaram
print("convidados nao confirmados:")
for pessoa in nao_confirmados:
	print(pessoa)
