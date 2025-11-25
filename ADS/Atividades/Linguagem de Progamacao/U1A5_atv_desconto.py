valor_produto = float(input("Digite o valor do produto: \n> "))

per_desconto = int(input("Digite a percentagem do produto: \n> "))

if per_desconto <= 100 and per_desconto >= 0:
    valor_final = valor_produto - (valor_produto * (per_desconto / 100))
    print(f"valor final: {valor_final}")
