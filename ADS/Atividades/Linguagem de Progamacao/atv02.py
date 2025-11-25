
import matplotlib.pyplot as plt

# dados 
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# criar um grafico de linha 
plt.plot(x, y)

# adicionar rotulos aos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# adicionar um titulo ao grafico 
plt.title("exemplo de grafico de linha")

# mostrar o grafico 
plt.show()