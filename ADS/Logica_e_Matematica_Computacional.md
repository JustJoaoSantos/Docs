# U1A1 - Fundamentos da Logica e Matematica Computacional
- Aplicacao: IA, Desemvolvimento de algoritimos, etc

## Proposicoes
> afirmacao que pode ser classificada como verdadeira ou falsa
- pode ser dividida em simples ou compostas

- Proposicoes Simples
	- o sol e um estrela. (V)
	- 2 + 2 = 4. (V)
	- 5 e um numero primo (V)
	- A Terra e Plana. (F)

- Proposicoes compostas
	- P ^ Q: o ceu esta azul e o sol esta brilhando
		- Conectivo AND
		- esta proposicao e verdadeira apenas se ambos os eventos ocorrerem ao mesmo tempo
	- R V S: Eu vou a praia ou vou ao parque
		- conectivo OR
		- esta proposicao e verdadeira se eu escolher ir a praia, ao parque ou ambos
	- T -> U: Se estiver chovendo, entao vou levar um guarda-chuva
		- conectivo condicional
		- esta proposicao e falsa apenas se eu nao levar um guarda-chuva quando estiver chovendo
	- V <-> W: Eu gosto de sorvete se, e somente se, estiver calor
		- Conectivo bicondicional
		- esta proposicao e verdadeira se eu gostar de sorvete quando estiver calor e nao gostar de sorvete quando nao estiver calor 

## Premissas
> Afirmacoes iniciais ou suposicoes fundamentais que servem como base para argumentos ou raciocinios
- elas sao usadas como pontos de partida para a deducao logica ou resolucao de problemas computacionais
- exemplos:
	- se hoje e sabado, entao nao e dia util
	- se maria estuda para o exame, entao ela ira se sair bem
	- a soma de dois numeros pares resulta em um numero par 
	- se um algoritmo termina a execucao, entao ele encontrol uma solucao.

## Argumentos 
> sao uma sequencia de proposicoes em que uma conclusao e afirmada com base em premissas, seguindo algumas regras logicas
- objetivo e demostrar a validade ou verdade da conclusao com base nas premissas fornecidas
- exemplos - Logica Proposicional:
	- premissa 1: se chover, a rua estara molhada
	- premissa 2: esta chovendo
	- conclusao: portanto, a rua esta molhada
- exemplos - matematica computacional:
	- premissa 1: todos os numeros multiplos de 3 sao impares
	- premissa 2: 9 e multiplo de 3
	- conclusao: logo, 9 e impar
	
## Silogismo
> sequencia de proposicoes em que uma e um tipo de argumento logico que consiste em 2 premissas e 1 conclusao.
- sao declaracoes que sao supostamente verdadeiras, e a conclusao e uma inferencia que se segue logicamente das premissas.
- Exemplo - Silogismo Categorico
	- Premissa 1: todos os humanos sao mortais.
	- Premissa 2: socrates e humano.
	- conclusao: portando, socrates e mortal.
- Exemplo - Silogismo hipotetico
	- premissa 1: se chover, a rua estara molhada
	- premissa 2: esta chovendo
	- conclusao: portanto, a rua esta molhada
	
## Conectivos Logicos 
> simbolos utilizados na logica para combinar proposicoes e formar expressoes compostas
- os principais conectivos incluem 'e' (conjuncao), 'ou' (disjuncao), 'nao' (negacao), 'se...entao' (implicacao) e 'se, e somente se' (bicondicional)
- eles sao fundamentais para construir argumentos e expressoes logicas mais complexas
- exemplo 
	- '~' : Negacao, pode-se usar tambem <-
	- '^' : Conjuncao. em programacao, a conjuncao e representada por 'AND' ou '&'
	- 'V' : Disjuncao, equivale a 'OU' em programaca.
	- '->': Condicional, em portugues corresponde a 'se..., entao...'
	- '<->': Bicondicional, em portugues corresponde a 'se, e somente se, ...'

## inferencia
> processo que permite chegar a conclusoes a partir de premissas, constituindo a argumentacao logica perfeita
- a inferencia, pode ser de dois tipos: indutiva ou dedutiva
- a inferencia invalida e chamada falacia.

- Inferencia indutiva
	- tipo de raciocinio logico no qual conclusoes gerais sao tiradas com base em observacoes especificas
	- ao contrario da inferencia dedutiva, a indutiva nao garante a certeza das conclusoes, mas busca estabelecer generalizacoes probabilisticas.
	- exemplos:
		- observacoes: todos os alunos que estudaram para o teste obtiveram boas notas.
			- conclusao indutiva: estudar provavelmente leva a boas notas nos testes.

- Inferencia Dedutiva 
	- processo logico em que conclusoes especificas sao derivadas a partir de premissas gerais 
	- esse tipo de raciocinio visa garantir a validade logica das conclusoes, seguindo regras formais
	- exemplos:
		- Premissa 1: todos os homens sao mortais.
		- premissa 2: socrates e um homem
		- conclusao dedutiva: portanto, socrates e mortal 

- Inferencia Falacia 
	- raciocinio logicamente invalido que, muitas vezes de maneira sutil, procura enganar ou persuadir atraves de argumentos defeituosos
	- sao formas de raciocinio que podem parecer convincentes, mas que contem falhas na Logica
	- exemplos:
		- Argumento Inicial: "Devemos investir mais em pesquisa espacial"
		- Versao Distorcida(homem de palha): "Entao voce quer ignorar os problemas na terra e gastar todo o dinheiro no espaco?"
		- Falacia: a versao distorcida nao aborda a proposta original e cria uma representacao simplificada e distorcida para desacreditar o argumento.