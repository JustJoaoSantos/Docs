# U1A1 - Definicao e representacao de algoritmos
- Algoritmo 
	- Sequencia logica e finita de passos (instrucoes) para resolver um determinado problema.

- Variaveis
	- elementos que podem ser alterados (sofrer variacoes) e estao relacionados a identificacao de informacoes.
	- ja uma atribuicao (->) serve para designar valores as variaveis, ou seja, para atribuir informacoes a elas 
		- nome <- "joao"
		- valor1 <- 22
		
- Metodos de exemplificar algoritmos 
	- Linguagem Natural
		1. Receber dados
		2. Executar operacao 1
		3. Mostrar resultado
		
	-  Diagrama de Bloco / Fluxograma
		- Colecao de simbolos graficos, onde cada um desses simbolos representa acoes especificas a serem executadas pelo computador.
		- Simbolos padronizados pela ANSI(Instituto Nacional Americano de Padroes)
		- Regras:
			- Estar atento aos níveis.
			- O diagrama de blocos (fluxograma) deve começar de cima para baixo e da esquerda para direita.
			- Ficar atento para não cruzar as linhas, principalmente as linhas de fluxos de dados.
			- As instruções devem seguir um fluxo lógico. 
		- Exemplo:
			- (inicio) -> [x] -> [y] -> [Se y != 0] -> (verdadeiro) -> [z = x/z] -> [z] -> (fim)
													-> (falso) -> ["Divisao por zero"] -> (fim)
	
	- Portugol
		```portugol 
		Algoritmo Operacoes
		
		Inicio 
			Inteiro: A, B, resultado;
			Operacao 1;
			escreva(resultado);
		Fim
		```
		
# U1A2 - Conceito basico de linguagem de programacao
- Estrutura de um programa em C 
	- Bibliotecas: 
		- Contem conjunto de funcoes e instrucoes previamente estabelecidas que podem ser usadas pelo programa
	- Funcao main: 
		- A execucao do programa inicia-se pela funcao main 
	- Retorno da funcao main: 
		- Indica o fim da execucao da funcao main
```C
# include <stdio.h>  	//Bibliotecas

int main() {  			//Funcao main 
	return 0; 			//Retorno da funcao main
}
```

	
- Entrada e Saidas
	- Dados(Entrada) -> Processamento -> Informacao(Saida)
	- Entrada:
		- scanf("tipo de dados", endereco da variavel);
		- scanf("%d", &x);
		- scanf("%d %d", &x, &y);
	
	- Saida 
		- printf("conteudo/tipo de dado", lista de variavel/argumentos)
		- printf("hello world");
		- printf("resultado = %d", soma);
		- printf("raizes sao %f e %f", x, y);
		
- Codigos e Valores 
	- %d : int 
	- %f : float
	- %c : char
	- %s : string
	- %e : numero em notacao cientifica
	
# U1A3 - Variaveis e Constantes
- Variaveis 
	- localizacao temporaria na memoria onde um valor pode ser armazenado e utilizado por um programa 
	- esta localizacao na memoria e identificda por meio de enderecos de memeoria

- Declaracao de variavel 
	- <tipo> <identificador>
		- e.g int numero, string nome, etc
		
- Tipos 
	- Int: inteiro 
	- Float: real
	- Char: 1 character
	- String: array de characters 
	- Bool: True, False
	
- Constantes 
	- variavel que permanece inalterado ao longo do programa
	- pode ser definido de duas formas:
	```c 
	#define nome_da_constante "valor da constante"
	
	const string nome_da_constante;
	```
	
# U1A4 - Operadores e expressoes
- Operadores 
	- Podemos utilizar operadores aritimeticos, relacionais e logicos ao mesmo tempo em uma expressao
	- porem, devemos ficar atentos a sua ordem de precedencia
	- Ordem de precedencia 
		- 1. ()
		- 2. ++, --
		- 3. *, /, %, 
		- 4. +, -
		- 5. <, <=, >, >=, ==, !=
		- 6. &&, ||, !

- Operadores Unarios
	- ++ : incremento +1
	- -- : decremento -1
	
- Operadores Aritmeticos
	- * : multiplicacao
	- / : divisao
	- % : modulo ou resto da divisao
	- + : soma
	- - : subtracao
	
- Operadores Relacionais
	- < : menor que
	- > : maior que 
	- <= : menor ou igual a 
	- >= : maior ou igual a 
	- == : igual a 
	- != : diferente de 
	
- Operadores Logicos
	- && : Conjuncao, 'and' ou 'e', true se ambos forem true 
	- || : Disjuncao, 'or' ou 'ou', true se um for true 
	- ! : Negacao, 'not' ou 'nao', true -> false, false -> true 
	
- Operadores Unarios
	- ++ : incremento +1
	- -- : decremento -1
	- ++x : pre-incremento: +1 antes de utilizar o valor 
	- x++ : pos-incremento: +1 depois de utilizar o valor 
	- --x : pre-decremento: -1 antes de utilizar o valor 
	- x-- : pos-decremento: -1 depois de utilizar o valor 
	
	
# U2A1 - Estruturas de decisao condicional / Controle de Fluxo
- If: tem a funcao de tomar uma decisao e criar um desvio no programa 
- else: juntamente utilizamos o 'else', o qual indica caso contrario.

- exemplo:
	```c 
	if (condicao) {
		// bloco true


	} else if (condicao) {
		// bloco true 
		
	} else {
		// bloco false
	}

	```

- Estruturas condicionais encadeadas ou aninhadas
	- quando uma estrutura de decisao esta dentro de outra estrutura de decisao
	
	
- Operador ternario ?
	- simplificacao do comando if-else com apenas um comando 
	- tipicamente utilzado para atribuicoes condicionais 
	- expressao condicional ? expressao_true : expressao_false;
	- exemplo:
		```c 
		// if salario > 1000, salario = salario * 1.05 else salario = salario * 1.07
		salario = salario > 1000 ? salario * 1.05 : salario * 1.07;
		```
	
- Estrutura switch-case 
	- estrutura condicional de selecao de casos;
	- avalia sucessivamente o valor de uma expressao em relacao a uma lista de constantes 
	- exemplo:
		```c 
		switch (variavel) {
			case constante1:
				// block 
				break;
			
			case constante2:
				// block 
				break;
				
			default:
				// block 
				break;
		}

		```

# U2A2 - Estruturas de repeticao / Laços de repeticao
- while: estrutura de repeticao com teste no inicio 
- exemplo:
	```c 
	while (condicao) {
		// block
	}
	```
	
- do-while: estrutura de repeticao com teste no final
- exemplo:
	```c 
	do {
		// block 
	
	} while (condicao);
	```
	
- Condicao de parada: lacos precisam de uma condicao de parada para previnir o loop infinito
	- contador / acumulador / incremento / decremento
	
# U2A3 - Estruturas deterministicas
- Laco de repeticao for
	- comumente utilizado para iterar uma instrucao por um numero pre-definido de vezes
	- possivel determinar a quantidade de repeticoes
	- exemplo:
		```c 
		for (inicializacao; condicao; incremento) {
			// block 
		}
		```
	
- operador virgula no comando for 
	- pode-se usar (,) como separador de comandos,
	- ele permite utilzar uma lista de expressoes para serem executadas sequencialmente
	- exemplo:
		```c
		for (i = 0, j = 100; i < j; i++, j--) {
			printf("i = %d e j = %d \n", i, j);
		}
		```
		
# U2A4 - Controle de repeticao
- break 
	- encerra o fluxo de execucao de um laco ou switch, 
	- faz com que a execucao do programa continue na primeira linha seguinte aao laco interronpido
	
- continue 
	- interrompe apenas a repeticao (iteracao) corrente.
	- e passa para a proxima repeticao do laco, se ela existir
	
- goto 
	- salto condicional para um local especificado por uma palavra-chave no codigo 
		'''c 
		destino:
			// blcok
		...
		goto destino;
		'''
	- 'destino' é uma palavra definido pelo programador
	- este local pode ser na frente ou atras do goto, mas deve estar dentro da mesma funcao.
	- o goto pode tornar o codigo complexo e dificio de entender, por isto nao e muito utilizado.
	- o teorema da programacao estruturada provou que goto nao é necessario para escrever um programa.

# U3A1 - vetores / arrays
- vetores ou arrays sao uma serie de variaveis indexadas que podem ser acesadas por um indice inteiro 
- e.g.: int vetor[n]
	- uma variavel do tipo int que armazena n valores, nos indices de 0 a n -1

- declaracao de vetor 
	- tipo_de_dado nome_vetor[tamanho];
	- exemplo:
		```c 
		int lista[5];
		char nome[30];
		float valor[10];
		
		int v[3] = {5, 10, 20} 		//vetor com 3 valores
		int v[] = {5, 10, 20} 		//vetor com 3 valores, tamanho 3 automatico
		int v[10] = {5, 10, 20}; 	// restante preenche com zero 
		int v[]; 					// erro de compilacao
		```
		
- lendo uma lista (array) ao contrario 
	```c 
	int array[5] = {1, 2, 3, 4, 5};
	for (int i = 4; i >= 0; i--) {
		printf("%d", array[i]);
	}
	```
	
- utilizando char arrays e scanf 
```c 
// declarando char array 
char frase[101];

printf("\n Digite uma frase:");

fflush(stdin); //limpando entrada 
fgets(frase, 101, stdin); //fgets(destino, tamanho, fluxo), usando fgets para armazenar entrada na array frase
printf("\n Frase digitada: %s", frase);
```

# U3A2 - Matrizes, 2 Dimensional Arrays 
- cada linha de uma matriz é um vetor-linho de n numeros, e a matriz é um vetor de m vetores-linha 
- para exemplificar:
 | M[0][0] | M[0][1] | ... | M[0][n] |
 | M[1][0] | M[1][1] | ... | M[1][n] |
 |  ...	   |	...	 | ... |		 |
 | M[m][0] | M[m][1] | ... | M[m][n] |
 
- declaracao de matrizes 
	- tipo nome_matriz [linhas][colunas];
	- e.g.:
		```c 
		int valores[3][2] = { {2, 3}, {5, 7}, {9, 11} };
		int valores [][2] = { {2, 3}, {5, 7}, {9, 11} };
		int valores [][] = { {2, 3}, {5, 7}, {9, 11} }; // erro de compilacao 
		```
		
- acesso a elementos em matrizes 
	```c 
	int mat[4][3];
	
	// percorrendo linha 
	for (i = 0; i < 4; i++) {
	
		//percorrendo coluna 
		for (j = 0; j < 3; j++) {
			printf("mat[%d][%d]: ", i, j);
			
			//usando input do usuario para inicializar matriz
			scanf("%d", &mat[i][j]);
		}
	}
	```

- criando uma matriz identidade (matrizes a qual sao preechidas com 0, com excessao da linha diagonal principal que e preechida com 1) e.g 
	```c 
	int matriz[5][5];
	
	for (int i = 0; i < 5; i++) {
		for (int j = 0; i < 5; j++) {
			if (i == j) {
				matriz[i][j] = 1;
			
			} else {
				matriz[i][j] = 0;
			}
		}
	}
	
	// Mostrando matriz 
	for (int i = 0; i < 5; i++) {
		for (int j = 0; i < 5; j++) {
			printf("%d " , matriz[i][j]);
		}
		// cria um espaco para separar linhas.
		printf("\n");
	}
	```
	
# U3A3 - Structs
- criando e declarando uma struct 
	```c 
	//criacao da struct 
	struct Cadastro {
		char nome[30];
		int idade;
		char rua[50];
		int numero;
	};
	
	//declaracao no main 
	struct Cadastro c1;
	```
	
- criando e declarando struct como type 
	```c 
	//criacao da struct como tipo
	typedef struct {
		char nome[30];
		int idade;
		char rua[50];
		int numero;
	} Cadastro;
	
	//declaracao no main 
	Cadastro c1;
	```
	
- acesso aos dados 
	- cada campo(variavel) da estrutura pode ser acessado com o operador "." (ponto)
	- exemplo:
		```c 
		struct Cadastro c1;
		
		// Inicializando dados diretamente em declaracao
		struct Cadastro c2 = {"Joao", 20, "Corina", 20403300};
		
		strcpy(c1.nome, "Joao"); //Atribuicao direta
		c1.idade = 32;
		
		fgets(c1.rua, 30, stdin); //insercao pelo teclado
		scanf("%d", &c1.numero);
		```
		
- atribuicao 
	```c 
	struct Ponto {
		int x;
		int y;
	};
	
	struct Ponto x;
	struct Ponto y;
	
	x = y;
	```
	
- Aninhamento
	```c 
	struct Endereco {
		char rua[50];
		int numero;
	};
	
	struct Cadastro {
		char nome[50];
		int idade;
		struct Endereco end;
	};
	```
	
- Vetores 
	```c 
	struct Cadastro {
		char nome[30];
		int idade;
	};
	
	struct Cadastro c[4];
	
	c[0].idade = 18;
	```
	
# U3A4 - Ponteiros / Pointers
- sao utilizados para fazer manipulacao direta de enderecos de memoria 
- usa-se (*) : para declarar um ponteiro 
- usa-se (&) : para acessar o endereco de memoria 
	- <tipo> *<nome_do_ponteiro>
	- e.g int *ptr_numero;
- exemplo:
	```c 
	int *ptr;
	int valor = 10;
	
	ptr = &valor; // alocando endereco de 'valor' a 'ptr'
	
	// %x para valores hexadecimais, ptr esta em hexadecimal
	printf("Endereco usando valor = %x", &valor);
	printf("Endereco = %x", ptr);
	printf("Endereco = %p", ptr); //pode-se usar tambem %p para formatar o valor de um ponteiro (enderco)
	printf("Valor usando ptr = %d", *ptr);
	```
	
- ponteiro para vetores 
	```c 
	int v[5] = {10, 50, 30, 15, 20};
	int *ptr;
	
	ptr = v; //a variavel de um vetor é o endereco do primeiro elemento do vetor, i.e v = &v[0]
	
	//ou 
	
	ptr = &v[0];
	
	ptr++ // ira apontar para o segundo endereco do vetor 'v', i.e ptr = &v[0 +1] 
	```
	
- por seguranca, inicie sempre os ponteiros. se nao souber para onde apontar aponte para NULL
	- int *ptr = NULL;
	- neste exemplo, o ponteiro ptr que é iniciado e nao *p, embora a atribuicao demonstre o contrario
	
# U4A1 - Funcoes e procedimentos
- sao fragmentos de codigo autonomos incorporado em um programa maior, designado para desempenhar uma tarefa especifica 
- vantagens 
	- reutilizacao eficiente de codigo 
	- manutencao da limpeza e clareza do programa.
	
- Sintaxe:
	<tipo de retorno> <nome> (<parametros>) {
		<comandos da funcao>
		<Retorno> (nao obrigatorio)
	}
	
- exemplo:
	```c 
	//funcao void / chamado de procedimento (funcao sem retorno)
	void imprimir() {
		printf("Output da funcao imprimir");
	}
	
	//prototype da funcao com retorno 
	int soma(int a, int b);
	
	
	int main() {
		//chamando funcao void 
		imprimir()
		
		//chamando funcao soma 
		int resultado = soma(5, 2);
		printf(resultado);
		
		return 0;
	}
	//declaracao da funcao com retorno
	int soma(int a, int b) {
		return a + b;
	}
	
	```
	
# U4A2 - Passagem de parametros por valor 
- Escopos de variavel 
	- Local:
		- variavel valida apenas dentro de uma funcao ou bloco especifico
		- declaradas dentro da funcao ou bloco.
	
	- Global:
		- variavel valida em qualquer local do codigo 
		- declarada fora dos blocos e funcoes (incluindo o main)
		
- passagem de valores por valor
	- ao passar um valor para a funcao como parametro, a funcao fara uma copia do valor e armazenara no parametro
	- exemplo 
		```c 
		void funcao( int a ) {
			//a é a copia de A
		}
		
		int main() {
			int A = 6;
			funcao(A);  //funcao faz uma copia de A passando o valor copiado para o parametro
		}
		```
		
# U4A3 - Passagem de parametros por referencia
- passagens de parametros por referencia 
	- sintaxe:
		```c 
		//definicao 
		int funcao(int* param1, int* param2) {
			//alterando valor da variavel a qual o ponteiro param1 referencia
			*param1 = 20;
		}
		
		//chamada
		int n1, n2;
		resul = funcao(&n1, &n2);

		```
		
- passagem de vetor e matrizes 
	- a passagem de um vetor/matriz sempre é realizada implicitamente por referencia 
	- sintaxe:
		```c 
		// definicao da funcao
		int funcao1 ( int v1[] ); //vetor esta sendo implicitamente referenciado, mesmo que int* v1.
		int funcao2 ( int* v1 );
		
		//chamada de funcao 
		int n1[3] = {3, 4, 5}
		resul1 = funcao (n1); //nao precisa de '&' porque o vetor e um ponteiro para o primeiro valor da vetor
		```
		
- passagem de structs 
	- dentro da funcao, utilizamos o operador '->' para referenciar os campos da estrutura passada 
	- sintaxe:
		```c 
		//definicao da struct 
		typedef struct {
			int num;
		} Teste;
		
		//definicao da funcao 
		void registra ( Teste* var ) {
			var->num = 10;
		}
		
		//chamada da funcao
		struct Teste t1;
		registra(&t1);
		```
		
# U4A4 - Recursividade
- e uma estrategia que pode ser utilzada sempre que uma funcao pode ser escrita em funcao dela propria
- exemplo: calculo fatorial
	- n! = n * (n - 1) * (n - 2) * (n - 3) ... 2 * 1 
	- E (n -1)! = n * (n - 1) * (n - 2) * (n - 3) ... 2 * 1 
	- entao: n! = n * (n - 1)!
- exemplo:
	```c 
	int fatorial (int n) {
		if (n == 0) { //chamado caso BASE, i.e condicao de parada
			return 1;
			
		} else {
			return n * fatorial( n - 1 );
		}
	}
	```
	
- Exemplo: Decimal Para Binario
	```c 
	void decimalParaBinario ( int decimal ) {
		if (decimal > 0) {
			decimalParaBinario( decimal / 2 );
			printf("%d", decimal % 2); // so ira ser executado quando a recursividade terminar
		}
	}
	```
	
# U4A5 - TAD
- TAD: tipos abstratos de dados
- sao modelos matematicos de estruturas de dados que definem:
	- o tipo de dado a ser armazenado;
	- as operacoes e seus respectiveis tipos 
	- relacoes e restricoes dos dados;
- sintaxe:
	```c 
	//======== tad_circulo.h =======//
	//definicao 
	typedef struct {
		float x, y; // centro
		float raio;
	} Circulo;
	
	
	// cabecario/header das funcoes 
	void inicializa(Circulo*, float, float, float);
	float calcularArea(Circulo*);
	
	//======== tad_circulo.c =======//
	#include "tad_curculo.h"
	#include <stdio.h>
	
	float calcularArea(Circulo* circ) {
		return 3.14 * circ->raio * circ->raio;
	}
	
	void inicializa(Circulo* circ, float x, float y, float r) {
		circ->x = x;
		circ->y = y;
		circ->raio = r;
	}
	
	//========= main.c ===========//
	#include "tad_circulo.h"
	#include <stdio.h>
	
	int main(void) {
		Circulo a;
		float res;
		
		inicializa(&a, 0, 0, w1);
		res = calcularArea(&a);
		printf(".2f", res);
	}
	```