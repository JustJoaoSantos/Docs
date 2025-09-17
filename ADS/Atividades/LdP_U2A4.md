import matplotlib.pyplot as plt

# dados
meses = ["Janeiro", "Fevereiro", "marco", "abril"]
vendas = [120, 90, 150, 200, 320]

# cria grafico de barras
plt.bar(meses, vendas, color='green')

# adicionar rotulos
plt.xlabel("mes")
plt.ylabel("vendas (em unidades)")

# adicionar titulo
plt.title("vendas mensais")

# mostrar
plt.show()