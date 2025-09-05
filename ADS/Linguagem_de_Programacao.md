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
var_bool = true 
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