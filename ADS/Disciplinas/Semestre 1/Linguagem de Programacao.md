# Python
- Criado por Guido van Rossum em 1991
- Linguagem de Alto nivel
- POO (Programacao Orientada a objeto)
- codigo facil de ler e escrever
- linguagem interpretada
- case sensitive
- tipagem dinamica

## PEP 8 - Convencao
- PEP8 (Python Enhancement Proposal 8): guia de estilo para programacao em Python

- indentacao de 4 espacos (nao tabs)
- variaveis e funcoes: minusculas em snake_case, e.g minha_variavel
- classes: letras maiusculas em snake_case, e.g Minha_Classe
- recomenda-se manter linhas de ate 79 characteres de comprimento
- importacoes devem ser organizadas de forma organizada e agrupadas em secoes

## Variaveis 
- declaracao de variavies 
```python 
var_string = 'var value'
var_int = 12
var_float = 3.2
var_bool = True 
```

## Comentarios
```python 
# isso e um comentario de linha unica
```

## U1A2 - Condicionais
- Operadores Relacionais
	- == : igual
	- != : diferente
	- is : identidade do objeto 
	- is not : negacao da identidade do objeto 
	- < : estritamente menor que
	- <= : menor ou igual que 
	- > : estritamente maior que 
	- >= : maior ou igual que 
	
- estrutura logica 
	- and : ambos devem ser true 
	- or : apenas um deve ser positivo
	- not : inverte o estado booleano, i.e true se torna false, false se torna true.
	
### Estrutura Condicionais 
- if
```python
if a > b:
	print(a)
```

- else 
```python 
if a > b:
	print(a)
else:
	print(b)
```

- elif 
```python 
if a > b:
	print(a)
elif a == b:
	print('a equals b')
else:
	print(b)
```

- condicional shortcut
```python 
media = 10
result = "aprovado" if media >= 7 else "reprovado"
```

## U1A3 - Estrutura de repeticao
- for 
```python 
numeros = [1, 2, 3, 4, 5]

for num in numeros:
	print(num)
	
for x in range(5):
	print(x)
```

- while
```python 
num = int(input("digite um numero"))

while num != 0:
	num = num + 1
	print(num)
```

- range 
	- range(x): conta de 0 ate x - 1
```python
for x in range(5);
	print(x)
```

	- range(x, y): conta de x ate y - 1
```python 
for y in range (2, 7)
	print(y)
```

	- range(x, y, n): conta de x ate y contando a cada n casas
```python 
for z in range(3, 7, 2)
	print(z)
```

- break 
	- interrompe o loop independente de condicao
```python 
for n in range(1, 11)
	if n % 2 == 0;
		break 
	print(n)
```

## U1A4 - Funcoes 
- funcoes built-in
	- blocos pre-implementados pela linguagem, e.g print(), int(), etc.

- funcoes anonimas
	- a.k.a funcoes lambda, usadas para acoes simples que serao usadas apenas uma vez
```python 
soma = lambda a, b: a + b 
resultado = soma(3, 4)
print(resultado)
```

### funcoes definidas pelo usuario
```python
def function_name(a, b):
	return_value = a + b 
	return return_value 
```

## U2A1 - Dados
- sequencias
	- x in s: true caso um item de s seja igual a x
	- s + t: concatenacao
	- n * s: adiciona a si mesmo n vezes
	- s[i]: acessa valor na posicao i da sequencia 
	- s[i:j]: acessa valores de da posicao i ate j
	- s[i:j:k]: acessa valores da posicao i ate j, com passo k
	- len(s): comprimento de s
	- min(s): menor valor de s 
	- max(s): maior valor de s 
	- s.count(x): numero total de ocorrencias de x em s
	
```python 
texto = "este e uma sequencia de string"

print(f"{'string' in texto}")
print(f"as 5 primeiras letras do texto, de 0 a 4: {testo[:5]}")
print(f"tamanho: {len(texto)}")
```

- listas
	- estruturas conhecidas por sua mutabilidade, com dados podendo ser removido, adicionado ou modificado
	
```python 
lista_de_cores = ['red', 'blue', 'green']
```

- map
	- mapeando uma funcao de uma lista em outra
```python 
proce_dolar = [100, 50, 75]
taxa_de_cambio = 5.25
preco_reais = list(map(lambda x: x * taxa_de_cambio, preco_dolar))
```

- filter
	- filtrando uma lista baseado em uma funcao 
```python 
nun = [1, 2, 6, 7, 9, 10]
num_pares = list(filter(lambda x: x % 2 == 0, num))
```


- tuplas
	- estruturas imutaveis
	
```python 
Tupla_vogais = ('a', 'e', 'i', 'o', 'u')
```

## U2A2 - 
- objetos tipo set 
	- conjunto ou set sao estruturas de dados que habilitam operacoes de conjuntos como: uniao, intersecao, diferenca e mais.
	
```python 
meu_conjunto = set()

# adicionando elementos
meu_conjunto.add(10)
meu_conjunto.add(20)

# exibindo conjunto inteiro
print(meu_conjunto)

# removendo elementos 
meu_conjunto.remove(10)
```

- mapping
	- foco em dicionairos, dados que estebelecem uma relacao chave-valor

```python 
# criacao de dict vazio, em seguida adicionando chave e valor
dict_1 = {}
dict_1['nome'] = "maria"
dict_1['idade'] = 25

# criacao de um dicionario com pares chave:valor
dict_2 = {"nome": "maria", "idade":25}

# criacao de um dict com uma lista de tuplas representando pares chave:valor
dict_3 = dict([("nome", "maria"), ("idade", 25')])

# criacao de um dict usando a funcao zip() e duas listas, uma para chave outra para valor
dict_4 = dict(zip(["nome", "idade"], ["maria", 25]))
```

- Array NumPy
	- numpy: biblioteca essencia para computacao cientifica, oferece amba gama de funcionaidades, incluindo arrays multidimensionais e funcoes sofisticadas.

```python 
# importar biblioteca 
import numpy as np

# criando array numpy
my_array = np.array([1, 2, 3, 4])

# soma de todos os elementos 
sum_of_elements = np.sum(my_array)

# eleva ao quadrado todos os elementos individualmente
squared_array = my_array ** 2

# acessa elemento pelo index
element_at_index = my_array[2]
```

## U2A3 - Classes e metodos
- classes 
	- modelos para criacao de objetos 
	- atributos: dados que representam o estado do objeto 
	- metodo: definem o comportamento do objeto, aka funcoes 
	- encapsulamento: combina atributos e metodos em uma entidade, permitindo a manipulacao e acesso da mesma
	- heranca: permite que uma classe herde atributos e metodos de outra classe 
	- polimorfismo: refere-se a capacidade de varias classes responderem de forma diferente a mesma mensagem
	
```python 
class Pessoa:
	# constructor
	def _init_(self, nome, idade):
		self.nome = nome
		self.idade = idade 
	
	def comprimentar(self):
		return f"ola, meu nome e {self.nome}"
		
	def aniversario(self):
		self.idade++

pessoa1 = Pessoa("joao", 30)
pessoa1.comprimentar()
pessoa1.aniversario()
```

- heranca 
```python
class ClassePai:
	def _init_(self, nome):
		self.nome = nome 
		
	def barulho(self):
		pass 
		
class ClasseFilha(ClassePai):
	def _init_(self, nome):
		super()._init_(nome)

```

## U2A4 - modulos e bibliotecas 
- modulo/biblioteca: componentes de codigo que servem como bibliotecas ou conjunto de funcoes em python

- biblioteca 'math'
```python
# primeira forma de importacao
import math 

math.sqrt(25)
math.log2(1024)
math.cos(45)

# importando com shortcut 
import math as m 

m.sqrt(25)
m.log2(1024)
m.cos(45)

# importando somente funcoes que seram utilizadas
from math import sqrt, log2, cos 

sqrt(25)
log2(1024)
cos(45)
```

- modulos built-in
	- embutidos no interpretador
	- e.g math, os, svs, Random, datetime, etc

- modulos de terceiros
	- criados por terceiros e disponibilizados via PyPi
	- e.g pip install requests
	
- modulos proprios
	- criados pelo desenvolvedor
	
- Matplotlib
	- biblioteca de visualizacao para criar graficos e visalizacaoes de dados de maneira flexivel e personalisavel
	
```python 
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
```

## U3A1 - Aplicacao de Banco de Dados com python
- SQL (Structured Query Language)
- fornece funcionalidades como: agregacoes, consultas, etc.
- categorias principais SQL 
	- DDL (Linguagem de definicao de dados)
	- DML (Linguagem de manupulacao de dados)
	- DCL (Linguagem de controle de dados)
	
- SQlite
	- Biblioteca de banco de dados escrita em C, que oferece um mecanismo de banco de dados SQL completo, embora compacto e de alta confiabilidade

- Conexao com banco de dados usando SQlite
```python 
import sqlite3

# 1. conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect("exemplo.db")

# 2. criar um objeto cursor, usaod para executar comando SQL no banco de dados
cursor = conn.cursor()

# 3. definir o comando SQL para criar a tabela
create_table = ```
CREATE TABLE IF NOT EXISTS Produtos (
	id INTERGER PRIMARY KEY,
	nome TEXT NOT NULL,
	preco REAL NOT NULL 
```);
===

# 4. executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. confirmar as alteracoes (commit)
conn.commit()

# 6. fechar a conexao com o banco de dados 
conn.close()
``` 

- CRUD (Create, Read, Updade, Delete)
	- passos para efetuar uma das operacoes CRUD:
	- estabelecer a conexao com um banco ->
	- criar um cursor e executar o comando ->
	- gravar a operacao ->
	- fechar o cursor e a conexao.

- Adicionar produto
```python 
import sqlite3 

conn = sqlite3.connect("exemplo.db")

cursor = conn.cursor()

novo_produto = ("Camiseta", 19.99, 50)

inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

cursor.execute(inserir_produto, novo_produto)

conn.commit()

conn.close()
```

- visualizar produto
```python 
import sqlite3 

conn = sqlite3.connect("exemplo.db")

cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM Produtos"

cursor.execute(selecionar_produtos)

produtos = cursor.fetchall()

for produto in produtos:
	print(produto)

conn.close()
```

- atualizar produto
```python 
import sqlite3 

conn = sqlite3.connect("exemplo.db")

cursor = conn.cursor()

novo_preco = 24.99

produto_id = 1 # supondo que queremos editar o produto de ID 1

atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"

curosr.execute(atualizar_preco, (novo_preco, produto_id))

conn.commit()

conn.close()
```

- excluir produto
```python 
import sqlite3 

conn = sqlite3.connect("exemplo.db")

cursor = conn.cursor()

produto_id = 1

excluir_produto = "DELETE FROM Produtos WHERE id = ?"

cursor.execute(excluir_produto, (produto_id))

conn.commit()

conn.close()
```

## U3A2 - Biblioteca Pandas
- Projetada para simplificar manipulacao e analise de dados organizados em tabelas e series temporais.

- DataFrame e series: estruturas de dados flexiveis
- Manipulacao de Dados: filtragem, selecao, ordenacao, agrupamento e agregacao.
- Leitura e escrita de dados: CSV, Excel, SQL, HDF5, etc. tornando-o uma ferradmenta versatil
- Tratamento de dados ausentes: simplifica o tratamento de dados faltantes.
- Visualizacao de dados: integrado com bibliotecas de visualzacao, como Matplotlib e Seaborn
- integracao com Numpy: construido sobre a biblioteca NumPy, combinacao de calculos e manipulacao.

- Series 
	- estrutura unidimensional capas de armazenar qualquer tipo de Dados
	- criando uma serie, principal parametro sendo "Data"
```python 
import pandas as pd

# craindo lista de valores 
exemplo1 = [10, 20, 30, 45]

# crando serie a partir de lista
series1 = pd.Series(data = exemplo1)

# mostrando series
print(series1)

# ------------------------------------

# criando um dicionario 
exemplo2 = {'A': 100, 'B': 200, 'C':300}

# criando uma series a partir de um dicionario
series2 = pd.Series(data = exemplo2)

# visualizar serie 
print(series2)
```

- Lendo arquivos com Pandas 
```python 
import panda as pd 

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))
```

## U3A3 - Manipulacao de dados com Biblioteca Pandas
- Metodos para leitura e escrita Pandas
Tipo de Dado 	| Descricao do Dado 		| Metodo para Leitura 	| Metodo para Escrita
	Texto   	|   	CSV		 			| read_csv() 	  	|	to_csv()
	Texto    	|  fixe-width texto file 	| read_fwf() 			|
	Texto 		| 		JSON 				| read_json() 			| to_json()
	Texto 		| 		HTML 				| read_html() 			| to_html()
	Texto 		| 		Latex				| 						| styler.to_latex() 
	Texto 		| 		XML 				| read_xml() 			| to_xml() 
	Texto 		| 		Local Clipboard		| read_clipboard()		| to_clipboard()
	Binario 	| 		MS Excel 			| read_excel() 			| to_excel() 
	Binario		| 		OpenDocument 		| read_excel() 			|
	Binario 	|		HDF5 Format 		| read_hdf() 			| to_hdf() 
	SQL			|		SQL					| read_sql()			| to_sql()

- Captura, transformacao e extracao de Dados
```python 
import pandas as pd

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
print(df_selic.info())
print(df_selic)

# verificar duplicidade de linhas, com drop_duplicate(), inplace = sobrescreve a variavel df_selic
df_selic.drop_duplicates(keep="last", inplace=True)

# adicionando colunas
from datetime import date as dt

data_extracao = date.today()

df_selic["data_extracao"] = data_extracao 
df_selic["responsavel"] = "Joao"

print(df_selic.info())
print(df_selic)

# buscando informacao por indice, i.e index 0
df_selic.loc[0]

# buscando multiplas linhas por indices
df_selic.loc[[0, 20, 70]]

# buscando a partir de uma condicao
teste = df_selic["valor"] < 0.01
print(type(teste))
print(teste)
```

## U3A4 - Visualizacao de dados em python 
- Matplotlib 
	- desempenha um papel central na criacao de graficos em python, sendo amplamente adotada em projetos de visualizacao de dados.
	
```python 
import matplotlib.pyplot as plt
import random 

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1, dados2)
plt.bar(dados1, dados2)
```

- Pandas 
	- as principais struturas de dados da biblioteca (Series e DataFrames) possuem o metodo plot(), construido com base no matplolib e que permite criar graficos a partir dos dados nas estruturas.
	
```python 
import pandas as pd
dados = {
	'Produto': ['A', 'B', 'C']
	'qtde_vendida': [33, 50, 45]
}

df = pd.DataFrame(dados)
df.plot(x='Produto', y='qtde_vendida', kind='bar') # possiveis kind: 'bar', 'pie', 'line'
```

- Seaborn 
	- biblioteca construida sobre a base do matplotlib para criacao de graficos especializados
	
```python 
import seaborn as sns
import matplotlib.pyplot as plt 

sns.set(style='whitegrid') #opcoes: darkgrid, whitegrid, dark, white, ticks

# carregando sample database da lib seaborn
df_tips = sns.load_dataset('tips')
pirnt(df_tips)

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0]) # sem estimator, padrao: media
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
```

## U4A1 - Web Dev com python
- oferece frameworks robustos como Django e flexiveis como flask, alem de suportar integracao facil com bibliotecas como react, vue.js e angular
- dev web em python enfrenta desafios como escalabilidade e seguranca, mas oferece oportunidades para inovacao
- fastAPI e django se destacam no desenvolvimento eficiente e rapido de APIs

- Front-End com python 
```python
from IPython.display import HTML

# criando pagina HTML com Python
html_code = '''
<!DOCTYPE html>
<html>
<head>
	<title> exemplo front-end com python </title>
</head>
<body>
	<h1> Ola, mundo </h1>
	<p> esta e uma pagina web criado usando python </p>
</body>
</html>
'''

HTML(html_code)
```

- Back-End com Python
```python 
from flask import Flask

# criando aplicativo flask
app = Flask(__name__)

# rota para pagina inicial
@app.route('/')
def hello():
	return 'Bem-vindo ao back-end simples com flask'

# executa a aplicacao no host e na porta especificada
if __name__ == '__main__':
	app.run(host='localhost', port=5000)
```

## U4A2 - Dev Mobile com Python
- python com sintaxe clara, destaca-se com o uso de frameworks como Kivy, Beeware e Flutter que oferecem suporte a linguagem.
- vantagems: comnunidade ativa, vasta biblioteca de modulos e agilidade proporcionada pela liguagem
- desvantegens: desempenho comparado com linguagems nativas e possiveis limitacoes de acesso a recursos especificos do dispositivo.

- KivyMD
	- emerge como ferramenta para desenvolvimento mobile com pythonk,
	- extencao do kivy, estendendo as capacidades do kivy ao integrar os principios de design do material design do google, proporcionando uma experiencia visualmente atraente e consistente em dispositivos moveis
	
```python 
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.lavel import label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

Builder.load_string('''
<TabsLayout>:
	TabbedPanel:
		do_default_tab: False
		TabbedPanelItem:
			text: 'Tab 1'
			BoxLayout:
				orientation: 'vertical'
				Label:
					text: 'Content for Tab 1'
		TabbedPanelItem:
			text: 'Tab 2'
			BoxLayout:
				orientation: 'vertical'
				Label:
					text: 'Content for Tab 2'
''')

class TabsLayout(BoxLayout):
	pass 
	
class TabsApp(App):
	def build(self):
		return TabsLayout()
		
# funcao de initializacao
def run_kivy_app():
	app = TabsApp()
	app.run()
	
# chamada da funcao de inicializacao
run_kivy_app()

```

## U4A3 - Testes automatizados com Python
- Assertions
	- sao utilizadas para verificar condicoes essenciais durante a execucao do codigo.

```python 
def divite(x, y):
	assert y != 0, "divisao por zero!"
	return x / y

result = divide(0, 2)
print(result)

def calcular_media(notas):
	assert len(notas) > 0, "a lista de notas nao pode estar vazia"
	
	soma = sum(notas)
	media = soma / len(notas)
	return media 
	
# 1. lista d enotas vazia 
notas_vazias = []
media = calcular_media(notas_vazias) # isso lancara uma AssertionError

# 2. lista de notas validas
notas_validas = [8, 7, 2, 1, 9]
media = calcular_media(notas_validas) # isso funcionara corretamente

print(media) 
```

- Dectest
	- modulo em python que permite incorporar testes diretamente na documentacao do codigo, aproveitando os exemplos presentes na documentacao para verificar se o codigo funciona comforme o esperado.

```python 
import doctest

def square(x):
	'''
	retorna o quadrado de um numero.
	
	Exemplos:
	>>> square(3)
	9
	>>> square(-2)
	4
	>>> square(0)
	0
	'''
	return x * x
	
doctest.testmod()
```

- Unittest
	- oferece uma estrutura de teste mais avancada, permitindo a organizacao de testes em classes e metodos, alem de fornecer assertions mais poderosas.
	
```python
import unittest 

def add(a, b):
	return a + b 

class TestAddition(unittest.TestCase):
	def test_add_positive_number(self):
		self.assertEqual(add(2, 3), 5)
	
	def test_add_negative_number(self):
		self.assertEqual(add(-2, -3), -5)
		
if __name__ == '__main__':
	import unittest 
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
	print('os testes foram executados com sucesso')
```

## U4A4 - Machine Learning com python 
- Teoria Machine Learning 
	- area da IA que visa desenvolver algoritmos capazes de aprender com dados e realizar tarefas sem programacao explicita
	- envolve abordagem como aprendizado supervisionado, nao supervisionado e por reforco
	- modelos:
		- arvores de decisao: modelo de tomada de decisao baseado em condicoes,
		- Redes Neurais: inspirada no funcionamento do cerebro, sao usadas para problemas complexos,
		- SVM: Support Vector Machines, para classificacao e regressao,
		- K-Means: algoritmo de agrupamento usado no aprendizado nao supervisionado

- Tipos de Treinamento
	- os tipos de treinamento sao estrategias fundamentais no desenvolvimento de modelos de Machine Learning
	- Supervisionado: o modelo e alimentado com um conjunto de dados rotulados, consistindo em pares de entrada e saida esperada. e.g classificacao de e-mails como 'spam' ou 'nao spam'
	- Nao Supervisionado: lida com dados nao-rotulados. e.g agrupamento de clientes com base em padroes de compra
	- Por reforco: envolve um agente interagindo com um ambiente dinamico. e.g treinar um agente de IA para jogar um jogo e ganhar pontos ao realizar acoes corretas.

- Tensorflow
	- biblioteca opensource que facilita a implementacao de modelos de machine learning e deep learning. sua estrutura flexivel permite a criacao e treinamento de modelos complexos, sendo amplamente utilizada na comunidade de aprendizado de maquina.

```python 
# ==== SUPERVISIONADO ====
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

 

# Dados de exemplo
X_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

 

# Modelo de Regressão Linear Simples
model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

 

# Treinamento do modelo
model.fit(X_train, y_train, epochs=1000, verbose=0)

 

# Previsão
X_new = tf.constant([[5.0]])
prediction = model.predict(X_new)
print(“Predição:”, prediction[0][0])

plt.ylabel('Notas')
plt.show()

# ===== NAO SUPERVISIONADO ======
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Dados de exemplo
X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

 

# Modelo Autoencoder Simples
input_layer = Input(shape=(2,))
encoded = Dense(units=1)(input_layer)
decoded = Dense(units=2)(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

 

# Treinamento do modelo não supervisionado
autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

 

# Previsão
prediction_unsupervised = autoencoder.predict(X_unsupervised)
print(“Predição Não Supervisionada:”, prediction_unsupervised)

# ===== POR REFORCO =======
import tensorflow as tf
import gym

# Ambiente CartPole do Gym
env = gym.make('CartPole-v1')

# Modelo Simples para Aprendizado por Reforço
model_reinforcement = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation='relu', input_shape=(env.observation_space.shape[0],)),
    tf.keras.layers.Dense(env.action_space.n, activation='linear')
])

model_reinforcement.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# Treinamento por Reforço (exemplo fictício)
max_episodes = 1000  # Defina o número máximo de episódios

for episode in range(max_episodes):
    state = env.reset()

    done = False

    while not done:

        action = env.action_space.sample()

        next_state, reward, done, _ = env.step(action)

        target = reward + 0.95 * tf.reduce_max(model_reinforcement.predict(next_state.reshape(1, -1)))

        target_f = model_reinforcement.predict(state.reshape(1, -1))

        target_f[0][action] = target

        model_reinforcement.fit(state.reshape(1, -1), target_f, epochs=1, verbose=0)

        state = next_state

    # Condição de parada

    if episode % 10 == 0:
        average_reward = sum(reward for _ in range(10)) / 10.0

        print(f'Episode {episode}, Average Reward: {average_reward}')

        # Adicionando uma condição de parada
        if average_reward == 1:  # Pode ajustar esse valor conforme necessário

            print(f'Solved after {episode} episodes!')

            break

```