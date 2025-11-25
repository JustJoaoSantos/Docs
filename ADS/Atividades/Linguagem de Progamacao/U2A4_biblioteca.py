import matplotlib.pyplot as plt

# template de livro
class Livro:
    #constructor
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo 
        self.autor = autor 
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor} publicado em {self.ano_publicacao}"
    
# criando lista de livros
biblioteca = []

# lista para armazenar anos de publicacao
anos = []

# adiciona livro a biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)
    print(f"{titulo} foi adicionado a biblioteca")

# listagem de livros na biblioteca
def listar_livros():
    print()
    for livro in biblioteca:
        print(livro)

# populando lista 'biblioteca'
adicionar_livro("All you need is Kill", "Hiroshi Sakurazaka", 2004)
adicionar_livro("The King in Yellow", " Robert W. Chambers", 1895)
adicionar_livro("Call of Cthulhu", "H. P. Lovecraft", 1926)

# listar todos livros na biblioteca
listar_livros()

# grafico por ano
anos = list(set(anos)) # remove duplicatas dos anos
anos.sort()

# contagem de livros por ano
contagem_por_ano = [anos.count(ano) for ano in anos]

# criar um grafico de linha
plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel("Ano de Publicacao")
plt.ylabel("Numero de Livros")
plt.title("Distribuicao de Livros na Biblioteca por Ano de Publicacao")

# Adicionar rotulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos[i], valor, str(valor), ha="center", va="bottom")

plt.grid(True)

plt.show()