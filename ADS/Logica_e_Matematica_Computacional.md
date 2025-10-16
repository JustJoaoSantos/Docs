# U1A1 - Fundamentos da Logica e Matematica Computacional

## Proposicoes
> afirmacao que pode ser classificada como verdadeira ou falsa
- pode ser dividida em simples ou compostas

- Proposicoes Simples
	- o sol é um estrela. (V)
	- 2 + 2 = 4. (V)
	- 5 é um numero primo (V)
	- A Terra é Plana. (F)

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
> sao uma sequencia de proposicoes em que uma conclusao sera afirmada com base em premissas, seguindo algumas regras logicas
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
	- '~' : Negacao, false se torna verdadeiro e vice-versa, pode-se usar tambem <-
	- '^' : Conjuncao. em programacao, a conjuncao e representada por 'AND' ou '&'
	- 'V' : Disjuncao, equivale a 'OU' em programaca.
	- '->': Condicional, em portugues corresponde a 'se..., entao...'
	- '<->': Bicondicional, em portugues corresponde a 'se, e somente se, ...'

## Inferencia Logica
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
		
# U1A2 - Arranjos matematicos 
## Diferenca entre arrajos
- Arranjos Simples 
	- A ordem dos elementos e importante
	- um elemento escolhido nao pode ser escolhido novamente para a mesma posicao no arranjo
	- por exemplo: ao organizaras letras A, B e C em um arranjo simples de 3 elementos, as permutacoes seriam ABC, ACB, BAC, BCA, CAB e CBA. Nao ha repeticao dos elementos
	
- Arranjos com repeticao 
	- A ordem dos elementos ainda e importante, mas arepeticao se encontra permitida, o que significa que um elemento pode aparecer varias vezes no arranjo 
	- exemplo: ao organizar as letras A, B e C em um arranjo de repeticao de 3 elementos:
	- AAA, AAB, AAC, ABA, ABB, ACC, BAA, BAB, BAC, BBA, BBB, BCA, BCA, CAA, CAB, CAC, CBA< CBB e CCA. neste caso os elementos podem se repetir

## Arrajos Simples / Arranjos sem repeticao
> categoria de conceitosna matematica que envolvem a organizacao e selecao de elementos de um conjunto.
- a ordem e levado em consideracao
- Formula: A(n,k) = n! / (n - k)!     
	- ! = fatorial
	- n = quantidade de elementos
	- k = step, quantidade de elementos por possibiildade
- Exemplos:
	- Considere o conjunto A = {1, 2, 3, 4}
	- vamos determinar o numero de arranjos desses quatro elementos (n = 4) tomados dois a dois (p = 2).
	- Formula: 
		- A(4,2) = n! / (n - p)!
		- A(4,2) = 4! / (4 - 2)! 
		- A(4,2) = 4! / 2!
		- A(4,2) = (4 * 3 * 2 * 1) / (2 * 1)
		- A(4,2) = 24 / 2
		- A(4,2) = 12
	- de fato, discriminando todos os arranjos chegamos a 12 possibilidades:
		- (1,2) (1,3) (1,4) (2,1) (2,3) (2,4) (3,1) (3,2) (3,4) (4,1) (4,2) (4,3)

## Arranjos com Repeticao
> tipo de agrupamento da analise combinatoria
- sao agrupamentos ordenados com p elementos entre n elementos de um conjunto, permitindo repeticoes
- formula: A(n,p) = n^p   
	- n = numero de elementos do conjunto.
	- p = quantidade de elementos por agrupamento
	- ^ = Elevado, e.g 3^3 = 3 * 3 * 3 = 9
- Exemplo:
	- em um banco, a senha do cartao e composta por 4 numeros, que podem ser repetidos ou nao, entao, qual e a quantidade de senhas possiveis para este cartao?
	- existem 10 algarismos de 0 ate 9, entao n = 10, e seram escolhidos 4 deles, entao p = 4. dessa forma:
	- AR(10,4) = 10^4 
	- AR(10,4) = 10 * 10 * 10 * 10
	- AR(10,4) = 10.000

# U1A3 - Permutacoes 
> sao arranjos de elementos de um conjunto em uma ordem especifica 
- representao todas as diferentes maneiras de organizar os elemetos do conjunto 
- a ordem dos elementos e fundamental

- Formula: P(n) = n!
	- P = Permutacao
	- n = Elemento 
	- ! = Fatorial 

- Exemplos:
	- Quantos anagramas podem ser formados com as letras da palavra 'brasil'
	- 'BRASIL' = 6 elementos 
	- P(6) = 6!
	- P(6) = 6 * 5 * 4 * 3 * 2 * 1
	- P(6) = 720
	
	- Quantas permutacoes distintas podem ser formadas usando todasas letras da palavra 'MATE'
	- 'MATE' = 4 elementos 
	- P(4) = 4!
	- P(4) = 4 * 3 * 2 * 1
	- P(4) = 24
	
# U1A4 - Combinacoes
> Calcula o numero de maneiras diferentes de escolher um subconjunto de elementos de um conjunto maior, onde a ordem dos elementos nao importa 
- Concentram em selecionar grupos de elementos sem considerar a ordem em que esses elementos sao escolhidos 

- Formula: C(n,k) = n! / k! (n - k)!
	- C : combinacoes 
	- n : numero total de elementos no conjunto original 
	- k : numero de elementos que voce deseja escolher para formar o subconjunto 
	- ! : fatorial 
	
- Exemplo:
	- Calcule todas as combinacoes possiveis de 10 elementos tomados de 4 em 4
	- n = 10, k = 4
	- C(10,4) = 10! / 4!(10 - 4)!
	- C(10,4) = 10! / 4!6!
	- C(10,4) = (10 * 9 * 8 * 7 * 6!) / 4!6!     NT*: remove os dois 6! que se repetem
	- C(10,4) = (10 * 9 * 8 * 7) / 4!
	- C(10,4) = 5040 / 24
	- C(10,4) = 210
	
	- um trio deve ser formado por um gerente, um supervisor e um operador. de quantos modos diferentes este trio pde ser formado se ha 10 pessoas disponiveis?
	- n = 10, k = 3
	- A(n,p) = 10! / (10-3)!
	- A(n,p) = 10! / 7!
	- A(n,p) = 10 * 9 * 8 * 7 / 7!   NT* corta-se o 7 do divisor e o 7 do dividendo durante a simplificacao
	- A(n,p) = 10 * 9 * 8 
	- A(n,p) = 720
	
# U1A5 - Combinacoes, Arranjos e Permutacoes 
- Diferencas e quando usa-las
	- permutacoes: o numero de elementos se encontra igual ao numero de posicoes disponiveis
	- arranjo: o numero de elementos se encontra maior do que o numero de posicoes disponiveis 
	- se concentram na selecao de elementos sem levar em consideracao a ordem em que sao selecionadas

# U2A1 - Algebra de Conjuntos
- sao categorias que agrupam numeros com caracteristicas semelhantes
- fornecem uma estrutura fundamental para a organizacao e classificacao dos numeros em matematica 
- exemplos:
	- Conjuntos numericos:
		- ∅ : Nulo : 0 ou vazio, e.g A = {}
		- N : Naturais : 1, 2, 3, ...
		- Z : Inteiros : -1, 0, 1, ...
		- Q : Racionais : -1, -1.1, 0, 1, 1.1, ...
		- I : Irracionais : √3, √2, √1, e, π
		- R : Reais : compostos pelos conjuntos numericos N, Z, Q e I 
		- C : Complexos : conjunto R + Numeros Imaginarios (i)
		
## Notacao de Conjuntos 
	- A e B
	- A uniao B
	- A intersecao B 
	- A menos B 
	
- Operacoes
	- Uniao (U): novo conjunto que contem todos os elementos que estao em A ou em B ou em ambos.
		- denotada por A U B
		- Se A = {1, 2, 3} e B = {3, 4, 5}
		- Entao A U B = {1, 2, 3, 4, 5}
		
	- Intersecao (∩): novo conjunto que contem apenas os elementos que estao em ambos os conjuntos 
		- denotada por A ∩ B 
		- Se A = {1, 2, 3} e B = {3, 4, 5}
		- Entao A ∩ B : {3}
	
	- Diferenca simetrica (Δ): novo conjunto contendo elementos que pertencem a um dos conjuntos, mas nao a ambos
		- denotado por delta(Δ)
		- Se A = {1, 2, 3} e B = {2, 3, 4}
		- Entao A Δ B = {1, 4}
		
	- Diferenca (-): novo conjunto contendo os elementos de A removendo os numeros pertencentes a B 
		- denotado por A - B 
		- Se A = {1, 2, 3, 4, 5} e B = {3, 4, 5, 6, 7}
		- Entao A - B = {1, 2}
		
# U2A2 - Conjuntos numericos 
> Conjuntos podem ser definidos como colecoes nao ordenadas de objetos que podewm ser, relacionados
- exemplos:
	- Conjunto A = {verde, amarelo, azul, branco}
	- normalmente utiliza-se letras maiusculas do alfabeto para representar conjuntos 

- conceitos 
	- B = {2, 4, 6,...}
		- pode-se deduzir a partir do padrao que o conjunto B, e um conjunto infinito de numeros inteiros positivos pares 
	- C = {x| x e um numero inteiro e 4 < x <= 9}
		- le-se C e o conjunto de todos os x, tal que x e inteiro, maior que 4 e menor ou igual a 9
		- entao C = {5, 6, 7, 8, 9}
	- diagramas de Venn: consistem de circulos que podem estar intersectados, os quais representam os conjuntos.

## Cardinalidade
- representado pelo simbolo '||', representa a quantidade total de elementos em um conjunto.
- a relacao de pertinencia indicada pelo simbolo '∈' e a relacao de nao pertinencia pelo simbolo '∉'
- exemplo:
	- A = {verde, amarelo, azul, branco}
		- podemos afirmar que verde ∈ A e que vermelho ∉ A
		- a relacao pode ser lida como 'e membro de', 'esta em', 'e elemento de' ou 'pertence a'
		
	- A = {verde, amarelo, azul, branco}
		- cardinalidade de A e igual a 4, ou seja |A| = 4.
		- o conjunto C = {x | X e um numero inteiro e 4 < x <= 9}
		- entao C = {5, 6, 7, 8, 9}
		- a cardinalidade de C e igual a 5, ou seja, |C| = 5
		
	
## Quantificadores
- sao elementos fundamentais em logica e matematica que nos permitem expressar proposicoes envolvendo variaveis
- existem dois tipos:
	- Quantificador universal (∀)
	- Quantificador existencial (∃)
	
- Quantificador universal: lido 'para todo' ou 'qualquer que seja'
	- a forma geral para essa notacao e ∀ x E A, afirmacoes sobre x
	- a primeira afirmacao 'todo inteiro e par ou impar' ficaria representada como ∀ x E Z, x é par ou x é impar

- Quantificador existencial: lido como 'ha' ou 'existe'
	- a forma geral para essa notacao e ∃x E A, afirmacoes sobre x.
	- a segunda afirmacao 'existe um numero natural que e primo e par' ficaria representado como ∃ Ex N, x é primo e par
	
- Pertence (∈): se um conjunto pertence a outro
	- A ∈ B, A pertence a B

- Nao Pertence (ɇ): um conjunto nao pertence a outro
	- A ɇ B, A nao pertence a B

- Subconunto (⃀): se todos os elementos de um conjunto estao presentes em outro.

- Subconjunto: se todos os elementos pertencentes aos conjunto A tambem pertencem a B dizemos: 

- Exemplo:
	- quantos subconjunto tem o conjunto A = {a, b, c} 
	- como a cardinalidade de A = 3 (|A| = 3), qualquer subconjunto de A pode ter de zero a tres elementos 
	- subconjuntos: 
		- ∅
		- {a}, {b}, {c}
		- {a, b}, {a, c}, {b, c}
		- {a, b, c}
		- total de possibilidades: 8
		
# U2A3 - algebra de conjuntos 
- Exemplos:
	- Uma certa escola de idioma constatou que:
		- 150 alunos estudam ingles
		- 95 alunos estudam espanhol
		- 30 alunos estudam ingles e espanhol 
	1. quantos estudam ingles
	2. quantos estudam apenas 1 idioma 
	3. quantos estudam ingles ou espanhol 
	
	- resposta:
		- A = 150, B = 95, C = A ∩ B = 30
		1. A - B = 150 - 30 = 120
		2. A - C U B - C = (150 - 30) + (95 - 30) = 185
		3. A Δ B = 120(A - C) + 30(C) + 65(B - C) = 215 
		
- Exemplo 2:
	- Uma pesquisa foi realizada com 500 pessoas e os dados obtidos foram:
		- 300 pessoas gostam de futebol
		- 280 pessoas gostam de basquete
		- 50 pessoas nao gostam destes esporte
	1. quantas pessoas gostam de futebol e basquete 
	
	- resposta:
		- A = 300, B = 280, C = 50,  A ∩ B = X 
		- x = 300 - x + x + 280 - x + 50 = 500
		- 630 - X = 500
		- X = 630 - 500 
		- x = 130
		
- Exemplo 3:
	- Uma pesquisa foi feita com 600 leitores, os resultados encontrados foram:
		- 300 leem o jornal A;
		- 220 leem o jornal B;
		- 150 leem o jornal C;
		- 100 leem o jornais A e B;
		- 80 leem os jornais B e C;
		- 50 leem os jornais A e C;
		- 20 leem os jornais A, B e C;
	1. quantos leitores leem apenas 1 jornal 
	2. quantos leitores leem apenas 2 jornais 
	3. quantos leitores leem o jornal A, B ou C
	
	- resposta:
		- A ∩ B ∩ C = 20
		- A ∩ B = 100 - 20 = 80
		- B ∩ C = 80 - 20 = 60
		- A ∩ C = 30
		- A = 300 - 80 - 20 - 30 = 170
		- B = 220 - 80 - 20 - 60 = 60
		- C = 150 - 30 - 20 - 60 = 40
		
# U2A4 - Aplicacao de teoria de conjuntos
## Complemento de conjunto 
- A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} e B = {1, 2, 3, 5, 8, 9}
- O complemento de B em relacao a A consiste no conjunto constituido por todos os elementos pertencentes a A que nao pertencem a B 
- portanto ᶜAB = {4, 6, 7, 10}
- em outras palavras, podemos dizer que o complemento de B em relacao a A consiste no conjunto formado por elementos que pertencem exclusivamente a A, quando comparados com os elementos de B

- A = {2, 7, 9, 13} e B = {3, 5, 10, 12}
- estes 2 conjuntos sao conjuntos disjuntos pois a intersecao entre eles e um conjunto vazio

- Outro fato que tambem merece atencao diz respeito a maneira como o conjunto complementar e representado simbolicamente
	- A - B, tem de ser diferente de B - A
	- entao: A = {2, 7, 9, 13} e B = {3, 5, 10, 12}
	- A - B = {2, 7, 9, 13}, ja que todos os elementos de A tambem estao em A e nao em B 
	- B - A = {3, 5, 10, 12}, ja que todos os elementos de B tambem estao em B e nao em A 
	
## Diferenca simetrica
- Diferenca simetrica de A e B é o conjunto de todos os elementos que pertencem a A mas nao pertence a B
- pode ser representada como:
	- A Δ B = (A - B) U (B - A). seja A = {1, 2, 3, 4, 5, 6, 7} e B = {5, 6, 7, 8, 9}
	- A diferenca simetrica de A Δ B seria:
	- A Δ B = (A - B) U (B - A) = (1, 2, 3, 4) U (8, 9) = (1, 2, 3, 4, 8, 9)
	
- Produto Cartesiano
	- operacao que combina elementos de dois conjuntos, formando pares ordenados que representam todas as possiveis combinacoes desses elementos.
	- e.g A = {2, 3} e B = {4, 5}
	- o produto cartesiano A X B:
	- A X B = {(2, 4), (2, 5), (3, 4), (3, 5)}
	
## Relacoes arbitrarias entre conjuntos
- Dado:
	- Conjunto exclusivamente A: (10)
	- Conjutno exclusivamente B: (01)
	- a interseccao dos conjutnos A e B: (11)
	- objetos que nao pertencem a nenhum dos conjuntos A e B: 00
	
- Exemplo:
	- A = {10, 11}
	- B = {01, 11}
   | XEA | XEB | XEA∩B 
00 |  F  |  F  | F
01 | F   | V   | F
10 | V   | F   | F 
11 | V   | V   | V

# U3A1 - Logica proposicional 
- ramo da logica que estuda a combinacao de proposicoes usando conectivos logicos como 'e', 'ou' e 'nao'
- composta por proposicoes e conectivos logicos que permitem criar uma serie de series de formulas que quando escritas corretamente sao chamadas FBFs (Formulas bem-formuladas)

## Premissas e Conclusoes 
- argumento de uma profesora sobre o desempenho de um certo aluno:
	- "e logico que Pedro sera aprovado nos exames, pois ele e inteligente e estuda muito e todos os alunos inteligentes e estudiosos sao aprovados"
- este argumento foi construido embasado por premissas(razoes) e que levam a uma unica conclusao
	- Premissas:
		1. Pedro e inteligente 
		2. Pedro estuda muito 
		3. Todos os alunos inteligentses e estudiosos sao aprovados 
	- Conclussao:
		- pedro sera aprovado 
		
- Para ser um argumento e preciso existir uma conclusao, logo nem toda frase e um argumento 
	- "Segure Firme" : nao possui premissas e conclusoes, pois se trata de uma sentenca imperativa (ordem)
	
# U3A2 - Conectivos e classificacao textual

## Conectivo Logico de Conjuncao 
- Tambem pode ser visto como AND ou pelo simbolo ^
- sua valoracao sera verdadeira somente quando ambas as proposicoes simples forem verdadeiras 
	- V ^ V = V 
	- V ^ F = F 
	- F ^ V = F 
	- F ^ F = F 

## Conectivo Logico de Disjuncao 
- Tambem pode ser visto como OR ou pelo simbolo V 
- sua valoracao sera falsa somente quando ambas as proposicoes forem falsas 
	- V v V = V 
	- V v F = V 
	- F v V = V 
	- F v F = F

## Conectivo logico de Negacao 
- Tambem pode ser visto como NOT, ou pelo simbolos: ~, ' 
- troca o valor-verdade da proposicao  
	- V' = F 
	- ~F = V 
	
## Conectivo logico Condicional ( implicacao logica)
- escrito como se...entao ou usando o simbolo ->
- A condicional significa que a verdade da primeira proposicao implica a verdade da segunda proposisao
- exemplo:
	- P: Joao estuda para a prova.
	- R: Joao passa de ano 
	- Proposicao P -> R (le-se Se P, entao R), deve ser traduzida como:
		- Se Joao estudar para a prova, entao passara de ano 
		- proposicao B esta condicionada a proposicao A, ou seja, depende da condicao A para acontecer
		
## Conectivo logico Bicondicional (Implicacao logica) - se e somente se
- escrito como se e somente se, e o simbolo <->
- ele é verdadeiro quanod ambas as proposicoes tem o mesmo valor de verdade (ambas verdadeiras ou ambas falsas)
	- V <-> V = V 
	- F <-> F = V 
	- F <-> V = F 
	- V <-> F = F 

## Formula bem Faturada (FBF)
- expressao que segue corretamente as regras gramaticas de um sistem formal, como a logica matematica 
- Ordem de execucao:
	1. parenteses
	2. negacao (~)
	3. conjunsao e disjunsao (V/^)
	4. condicional (->)
	5. bicondicional (<->)
- exemplo:
	- Valoracao da formula ~(A v B)
		- SE A = V, B = V ENTAO
		- A v B = V 
		- ~V = F 
		
		- SE A = V, B = F ENTAO
		- A v B = V
		- ~V = F 
		
		- SE A = F, B = F ENTAO
		- A v B = F 
		- ~F = V 
		
# U3A3 - Metodos dedutivos
- Logica Proposicional 
	- ramo da logica que estuda a combinacao de proposicoes usando conectivos logicos como 'e', 'ou' e 'nao'
	- ela permite analisar a validade de argumentos e expressoes complexas, sem considerar o conteudo especifico das proposicoes.
	- composta por proposicoes e conectivos logicos que permitem criar uma serie de series de formulas que quando escritas corretamente sao chamadas
	
- exemplo:
	- "dom predro proclamou a independencia do brasil e thomas escreveu a declaracao de independencia dos estados unidos. portanto todo dia tem 24 horas."
		- A: dom pedro proclamou a independencia 
		- B: thomas escrevel a declaracao 
		- C: todo dia tem 24 horas 
	
		- nosso conhecimento nos permite valorar as tres proposicoes, logo A, B e C sao verdadeiras 
		- embora, tanto as hipoteses quanto a conclusao sejam verdadeiras, o argumento é invalido pois a conclusao nada tem a ver com as hipoteses 
		
	- "Se george foi o primeiro presidente, entao john foi o primeiro vice-presidente. George foi o primeiro presidente, logo John foi o primeiro vice-presidente"
		- A: Se george foi o primeiro presidente, entao john foi o primeiro vice-presidente
		- B: George foi o primeiro presidente
		- Conclusao: John foi o primeiro vice-presidente 
		- representacao simbolica: (A -> B) ^ A -> B
		
# U3A4 - Inferencia logica 
## Regras de equivalencia de deducao para logica proposicional 
- sao principios que permitem simplificar ou transformar expressoes logicas de maneira a preservar a equivalencia logica 
- sao usadas para manipular e simplificar formumas para facilitar analises

	Expressao (FBF) | Equivalente (FBF) | Nome/Abreviacao
	P v Q        	|  Q v P 			| Comutavidade/com 
	P ^ Q  			| Q ^ P 			|
	(P v Q) v R 	| P v (Q v R) 		| Associatividade/ass 
	(P ^ Q) ^ R 	| P ^ (Q ^ R) 		|
	~(P v Q) 		| ~P ^ ~Q 			| Leis de De Morgan/De Morgan
	~(P ^ Q) 		| ~P V ~Q 			|
	P -> Q 			| ~P v Q 			| Condicional/cond 
	P 				| <-(<-P) 			| Dupla negacao/dn
	P <-> Q 		|(P -> Q) ^ (Q -> P)| Definicao de equivalencia/que
	
- Permitem derivar conclusoes a partir de premissas em argumentos formais, um exemplo e a regra de modus ponens:
	- Modus Ponens:
		- premissas: P->Q, P 
		- Conclusao: Q 
		
		- e.g 
			- P: sair na chuva 
			- Q: se molhar 
			- P -> Q, P : se eu sair na chuva vou me molhar
			
- Regras de Inferencia 
		De (FBF) 	| Podemos deduzir (FBF) | Nome/Abreviacao 
	   P -> Q, P 	|         Q 			| Modus Ponens/MP 
	P -> Q, <- Q	|         <-P 			| Modus Tollens/MT 
	P -> Q, Q -> R  |       P -> R 			| Silogismo Hipotetico/SH 
	     P, Q 		|       P ^ Q 			| Conjuncao/conj 
	     P ^ Q 		|        P,Q 			| Simplificacao/simp 
	      P 		|       P ^ Q 			| Adicao/ad
	
# U3A5 - Fundamentos da Logica 
- Argumento: sequencia de proposicoes, na qual uma é uma conclusao e as demais sao premissas.
- Proposicoes: declaracoes que expressam pensamentos completos e podem ser verdadeiro ou false.
- Premissas: afirmacoes que aceitamos como verdadeiras para construir um argumento. servem de base para chegar a uma conclusao.


- ~p 		: nao p 
- p ^ q 	: p e q 
- p v q 	: p ou q 
- p -> q 	: se p entao q 
- p <-> q 	: p se e somente se q

# U4A1 - Fundamentos da tabela verdade 
## Definicao 
- representacao tabular que mostra todas as combinacoes possiveis de valores de verdade para proposicoes logicas, indicando os resultados das operacoes logica correspondente
- comum usar 0 para falso e 1 para verdadeiro 
- exemplo: tabela verdade com 2 entradas (A e B), e uma expressao logica AND(^)
| A | B | A^B 
| 0 | 0 | 0
| 0 | 1 | 0
| 1 | 0 | 0
| 1 | 1 | 1

exemplo: suponha a seguinte expressao logica que envolve proposicoes intermediarias
	- A, B e C sao variaveis de entrada 
	- X = A ^ B
	- Y = B v C 
	- Z = X ^ Y
| A | B | C | X | Y | Z 
| 0 | 0 | 0 | 0 | 0 | 0
| 0 | 0 | 1 | 0 | 1 | 0
| 0 | 1 | 0 | 0 | 1 | 0
| 0 | 1 | 1 | 0 | 1 | 0
| 1 | 0 | 0 | 0 | 0 | 0
| 1 | 0 | 1 | 0 | 1 | 0
| 1 | 1 | 0 | 1 | 1 | 1
| 1 | 1 | 1 | 1 | 1 | 1

## Tabela verdade para lei do Morgan
- Estabelece que a negacao de um conjuracao (E) se encontra equivalente a disjuncao (OU) das negacoes das proposicoes individuais, e a negacao de uma disjuncao se encontra equivalente a conjuncao das negacoes das proposicoes 
| A | B | ~(A ^ B) | (~A) v (~B) |
| 0 | 0 |    1     |      1      |
| 0 | 1 |    1     |      1      |
| 1 | 0 |    1     |      1      |
| 1 | 1 |    0     |      0      |

## Exemplos 
- Suponha que temos as variaveis P e Q e queremos demonstrar a segunda lei de Morgan ~(P v Q) = ~P ^ ~Q.
- Crie uma tabela verdade que valide essa lei.

| P | Q | ~(P v Q) | ~P ^ ~Q 
| 0 | 0 | 0' -> 1  |    1
| 0 | 1 | 1' -> 0  |    0
| 1 | 0 | 1' -> 0  |    0
| 1 | 1 | 1' -> 0  |    0

# U4A2 - Construcao da tabela verdade 
- Nas colunas colocaremos as proposicoes (quantas forem necessarias)
- Em seguida as operacoes logicas das quais queremos obter resultados
- nas Linhas colocaremos os valores logicos ( V ou F) tanto para as proposicoes quanto para os resultados das formulas 
- Usamos 0 e 1 para falso ou verdade.