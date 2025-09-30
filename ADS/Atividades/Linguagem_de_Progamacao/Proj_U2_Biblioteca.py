import matplotlib.pyplot as plt

# Variaveis
biblioteca = []
generos = []

# Livros
class Livro:
    # Constructor
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor 
        self.genero = genero 
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Genero: {self.genero}, Quantidade: {self.quantidade}"

# Funcao de cadastro de livros
def cadastrar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)

    # adicionando livro e genero as respectivas listas
    biblioteca.append(novo_livro)
    generos.append(genero)

    print(f"\n{titulo} foi adicionado a biblioteca.")

# Funcao de listagem de livros
def listar_livros():
    print("\n" + 10*"=" + " Livros " + 10*"=")

    # Listando todos os elementos (livro) dentra da lista 'biblioteca'
    for livro in biblioteca:
        print(livro)

    print("\n" + 28*"=")

# Funcao de Busca de livros
def buscar_livro(titulo):
    print(28*"-")
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            print("Titulo Encontrado")
            print(livro)
            return
        
    print(f"Nao foi encontrado nenhum livro de titulo [{titulo}] nesta biblioteca.")
    print(28*"-")

# Pre-Cadastro de livros
cadastrar_livro("All you need is Kill", "Hiroshi Sakurazaka", "Aventura", 20)
cadastrar_livro("The King in Yellow", "Robert W. Chambers", "Horror Cosmico", 30)
cadastrar_livro("Call of Cthulhu", "H. P. Lovecraft", "Horror Cosmico", 50)
cadastrar_livro("Do Androids Dream of Electric Sheep?", "Philip K. Dick", "Cyberpunk", 10)
cadastrar_livro("I Have no Mouth and I Must Scream", "Harlan Ellison", "Sci-fi")
#listar_livros()

#buscar_livro("Do Androids Dream of Electric Sheep?")

#buscar_livro("all you need is kill")

while True:
    print(10*"=" + " MENU " + 10*"=")
    print (
        "[0] Encerra o programa\n"
        "[1] Cadastrar um Novo Livro\n"
        "[2] Listar Livros na Biblioteca\n"
        "[3] Buscar Livro\n"
        "[4] Gerar Relatorio de Quantidade de Livro por Genero"
    )
    code = input("> ")
    print()

    if code == '0':
        print("Encerrando programa...\n")
        break

    elif code == '1':
        print(10*"=" + " CADASTRO " + 10*"=")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        quantidade = input("Quantidade: ")

        if not quantidade.isnumeric():
            print("\nQuantidade nao numerico, valor padrao usado.")
            quantidade = 0
        
        cadastrar_livro(titulo, autor, genero, quantidade)
       
    elif code == '2':
        listar_livros()

    elif code == '3':
        buscar_livro(input("Buscar por Titulo: "))

    elif code == '4':
        # Remover duplicatas e organizar generos
        generos = list(set(generos))

        # contagem de livro por genero
        contagem_por_genero = [generos.count(genero) for genero in generos]

        # criar um grafico de barra
        plt.bar(generos, contagem_por_genero)
        plt.xlabel("Generos")
        plt.ylabel("Numero de Livros")
        plt.title("Distribuicao de Livros por Genero")

        # adicionar rotulos aos pontos de dados
        for i, valor in enumerate(contagem_por_genero):
            plt.text(generos[i], valor, str(valor), ha="center", va="bottom")

        plt.show()

    else:
        print("Codigo nao encontrado, por favor tente novamente\n")