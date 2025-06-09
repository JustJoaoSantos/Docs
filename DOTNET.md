# Dotnet
## Environment
```mermaid
flowchart LR;
    Linguagem'C#'-->Database'SQL';
    Database'SQL'-->Conteiner'Docker';
    Conteiner'Docker'-->Cloud'AWS';
    Cloud'AWS'-->Linguagem'C#';
```

## Estrutura de projeto
* Um Solution(.sln) pode guardar varios projetos csharp(.csproj) oque permite um projeto interagir e usar classes de outros projetos, e.g projetos auxiliares
* e.g:
.snl -> auxiliar.csproj 
			|		|
	proj1.csproj  proj2.csproj
	

## Compilers
* Compilador: Converte linguagem de alto nivel para baixo nivel, e.g C# -> Binary
* Transpilador: converte linguagem de alto nivel para alto nivel, e.g typescript -> javascript

```mermaid
flowchart LR;
    code --> LexiconAnalyzer --> SyntaxAnalyzer --> ILGenerator --> CodeOptimizer --> BinaryGenerator
```

* Para criar um nova solucao:
```shell
dotnet new sln -n "NOMEDASOLUCAO"
```

* Para adicionar um projeto existente a uma solucao:
```shell
cd "PATH_TO_PROJECT_ROOT"
dotnet sln "PATH_TO_SLN" add "PATH_TO_CSPROJ"
```

* Para Permitir um Projeto Reconhecer outro:
```shell
dotnet add "PATH_TO_TARGET_CSPROJ" reference "PATH_TO_REFERENCED_CSPROJ"
```

* Para Criar um novo projeto (console)
```shell
dotnet new console
```
	
* Para criar um projeto em uma versao especifica:
```shell
dotnet new console --framework net5.0
```

* Para Compilar um projeto
```shell
dotnet build
```

* Para Rodar e Compilar Um projeto:
```shell
dotnet run
```

* Compilador Dotnet:
```mermaid
flowchart LR;
c#Code --> C#Compiler --> IL_AKA_IntermediaryLanguage Code_.exe_AND.dll --> JITCompiler_AKA_JustInTime --> NativeCode_AKA_Binary
```

* verificar .net no cmd: "dotnet --info"

## C# 
* Exemple:
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjectName.FolderName {
	public class ClassName {
		public string Property {get; set;}
		public void Method(int argument){}
	}
}
```

* Exemple Program(driver file) .Net6+:
```csharp
Console.writeLine("Hello World");
```

* Exemple Program(Driver file) .Net5 and lower:
```csharp
using System;

namespace NAMESCAPE.NAME {
	class Program {
		static void Main(string[] args) {
			Console.writeLine("Hello world");
		}
	}
}
```

### Sintaxe e Convencoes
* Nomeclaturas:
	- Metodos/Funcoes sao escritas Capitalizadas em PascalCame
	- Classes sao escritas Capitalizadas em PascalCase
	- Nome do arquivo da classe e da classe devem ser iguais
	- Propriedades/Atributos sao escritos Capitalizados em PascalCase
	- Variaveis sao escritos em camelCase
	- abreviacoes sao contra as convencoes do C#

* Cases:
	- camelCase
	- PascalCase
	- snake_case
	- spinal-case

### Comentarios
* Unica Linha: //Comentary
* Multipla Linha: /*Comentary*/
* Documentar  Classes, Metodos, etc.: <summary>
* e.g summary on class
```csharp
///<summary>
///
///</summary>
class ClassName {}
```

* e.g summary on method:
```csharp
///<summary>
///
///</summary>
///<param name="x">comentary about param </param>
///<returns>commentary about return</returns>
public int MethodName(int x){
	Console.WriteLine(x);
	return x - 1;
}
```

### Propriedades/Variaveis
* criando uma variavel (Scopo Global)
```csharp
string PropertyName = "Value";
```

* criando uma propriedade (Scopo de Classe)
```csharp
public string PropertyName{get; set;}
```

### Datatype
* string: char array, a.k.a cadeia de character. e.g "textos", 'textos'
* char: unicode character, e.g 'a'
* bool: boolean, e.g true, false				|false
* byte: 8-bit unsigned int, e.g 0 to 255
* decimal: melhor para valores monetarios		|0.0M
* float: 32-bit single-precision float point	|0.0f
* double: 64-bit double-presicio float point 	|0.0D
* short: 16-bit signed int
* int: 32-bit signed int 
* long: 64-bit signed int 
* uint: 32-bit unsigned int 
* ulong: 64-bit unsigned int 
* DateTime: struct com data vimdo do sistema


#### Casting / Conversao de Tipo
* Convert:
```csharp
int a = Convert.ToInt32("5");
```
*NT.: convert: automaticamente converte null para 0, ao contrario do Parse

* Parse:
```csharp
int b = int.Parse("5");
```

* cast de string:
```csharp
int numero = 5;
string a = numero.ToString();
```

* cast implicito:
```csharp
int a = 5;
double b = 5;
```
*NT.: <int> a esta sendo convertido para <double> a

* Cast com tratamento de erro
```csharp
string a = "15c";
int b = 0;
int.TryParse(a, out b);
```
*NT.: mesmo que a conversao de erro, o TryParse ira retornar o segundo valor expecificado e continua o programa

### Manipulacao de Dados
* Concatenaçao/Interpolaçao de String:
```csharp
string concatenacao = "contatenando" + " duas strings";
string interpolacao = $"{Var} Concatenando uma propriedade com uma string";
```

* Formatar para valor Monetario:
```csharp
decimal money = 1000.45M;

Console.writeLine($"{money:C"); //Formatacao 'Currency' para valor movetario do pais do sistema
```
> NT* Output:R$ 1.000,45

* Alterando Localizacao (Locale) do Codigo:
```csharp
using System.Globalization;

CultureInfo.DefaultThreadCurrentCulture = new CultureInfo("en-US");  //Trava Cultura para todo o sistema

Console.writeLine(money.ToString("C", CultureInfo.CreateSpecificCulture("pt-BR")));
```

* Tratamento de String
```csharp
int numero = 2000
Console.WriteLine(numero.ToString("N2")); //Numero com 2 Casas Decimais
Console.writeLine(numero.ToString("P")); //Porcentagem
Console.writeLine(numero.ToString("##-###")); //Personalizado, # = Digito
```

### DateTime
* Convertendo Data Personalizada para DateTime com tratamento de erro
```csharp
string dataString = "2022-04-17 18:00";

bool sucesso = DateTime.TryParseExact(dataString, "yyyy-MM-dd HH:mm", CultureInfo.InvariantCulture, DateTimeStyles.None, out DateTime data);
if (sucesso) {
	Console.WriteLine($"Convertido com sucesso para: {data});

} else {
	Console.WriteLine("Falha na Conversao");
}
```

*
### Operadores
#### Ordem dos Operadores
1. ()
2. *, /
3. +, -

#### Operadores de Atribuicao
* '=' 	: atribui um valor a uma variavel
* '+=' 	: soma e atribui um valor a uma variavel, i.e a = a + b
* '-=' 	: subtrai e atribui um valor a uma variavel, i.e a = a - b
* '/=' 	: divide e atribui um valor a uma variavel, i.e a = a / b 
* '*='	: multiplica e atribui um valor a uma variavel, i.e a = a * b
* 'a++' : adiciona 1 a variavel, i.e a = a + 1
* 'a--' : subtrai 1 a variavel, i.e a = a - 1

#### Operadores Logicos
* '&&' 	: AND, E, e.g true && true 
* '||'	: OR, OU, e.g true || false
* '=='	: iqual a 
* '!'	: NOT, nao e.g !choveu
* '>='	: maior que 
* '<='	: menor que 

#### Operadores Condicionais / Flow Control
* If...Else:
```csharp
if (CONDITION) {
	TRUE_BLOCK;

} else if (CONDITION) {
	TRUE_BLOCK;
	
} else {
	FALSE_BLOCK;
}
```

* Switch Case:
```csharp
switch (CONDITION) {
	case CONDITION:
		TRUE_BLOCK;
		break;
	
	default:
		FALSE_BLOCK;
		break;
}
```

#### Operadores aritimeticos
* Adicao: '+', e.g x + y
* Subtracao: '-', e.g x - y
* Multiplicacal: '*', e.g x * y
* Divisao: '/' e.g x / y
* Modulo: '%', i.e resto de divisao, e.g x % y
* Potencia: 'Math.Pow()', e.g Math.Pow(x, y)
* Seno, Coseno, Tangente: Math.Sin(x), Math.Cos(x), Math.Tan(x)
* Raiz Quadrada: Math.sqrt(x);

### Estruturas de Repeticao / Loops
* For:
```csharp
for (int i = 0; i <= 10; i++) {
	CODE_BLOCK
}
```

* While:
```csharp
int i = 0;
while (i <= 10) {
	CODE_BLOCK
	i++;
}
```
*NT.: Pode ser interonpido com 'break;'

* Do While:
```csharp
do {
	CODE_BREAK
	i++;
} while (i <= 9);
```
*NT.: Pode ser Iterronpido com 'break;'

### Colecoes
#### Arrays
* Implementando um Array:
```csharp
int[] arrayConst = new int[4]; //Declarando um array e o tamanho dele
int[] array = new int[] {42, 71, 22, 30}; //Declarando um array o tamanho pela quantidade de elementos adicinados durante a declaracao.

arrayConst[0] = 12; //Modificando o valor no index especificado, erro se index nao valido.
arrayConst[1] = 22;
arrayConst[2] = 32;
arrayConst[3] = 42;

foreach(int item in arrayConst) {
	Console.WriteLine(item); //Percorre a partir do primeiro (index 0)
}

for(int i = 0; i < array.Length; i++) {
	Console.WriteLine(array[i]); //percorrendo um array com Length().
}

Array.Resize(ref array, 8); //redimenciona o array 'array' para 8

Array.Copy(arrayConst, array, 4); //copia os items do arrayConst para array ate o index 4.
```

#### Listas / Lists
* Vantagem de Uma Lista:
	1. Gerencia Tamanho automaticamente.
	
* Implementando uma Lista:
```csharp
List<int> = lista = new List<int>(); //Declarando uma lista 

lista.Add(12); //Adiciona um item ao final lista
lista.Add(45);
lista.Add(22);
lista.Add(30);

foreach(int item in lista) {
	Console.WriteLine(item); //Percorre a partir do primeiro
}

lista.Remove(45); //Remove o valor especificado
```

#### Fila / Queue
* FIFO: First In First Out
* Implementando uma fila:
```csharp
Queue<int> fila = new Queue<int>();  //Declarando uma fila

file.Enqueue(21); //adicionando um elemento a fila
fila.Enqueue(30);
fila.Enqueue(42);
fila.Enqueue(12);

foreach(int item in fila) {
	Console.WriteLine(item); //Percorre a partir do primeiro elemento
}

fila.Dequeue(); //Remove o primeiro elemento da lista
```

#### Pilha / Stack 
* LIFO: Last In First Out 
* Implementando uma pilha:
```csharp
Stack<int> pilha = new Stack<int>(); //Declarando uma pilha

pilha.Push(22);
pilha.Push(32);
pilha.Push(52);
pilha.Push(12);

foreach(int item in pilha) {
	Console.WriteLine(item); //Percorre a partir do ultimo elemento
}

pilha.Pop(); //Remove o ultimo elemento da pilha
```

#### Dicionarios / Dictionary
* Armazena dados em pares de Chave:Valor.
* Implementando Dictionary:
```csharp
Dictionary<string, string> estados = new Dictionary<string, string>(); //Declarando um Dicionario com chave 'string' e valor 'string'.

estados.Add("BA", "Bahia"); //Adicionando uma chave:valor para o dicionario.
estados.Add("SP", "Sao Paulo");
estados.Add("MG", "Minas Gerais");
estados.Add("AL", "Alagoas");

foreach(var item in estados) {  //var reconhece que Data Type e: KeyValuePair<string, string> item
	Console.WriteLine($"Chave: {item.Key}, Valor: {item.Value}");
}

estados["SP"]; //retorna o valor com chave 'SP'.

estados["SP"] = "Sao Paulooooo"; //Altera o valor pela chave. NT* Chaves nao podem ser alteradas.

estados.Remove("BA"); //Remove elementos pela chave.

estados.ContainsKey("BA"); //Verifica se a Chave 'BA' ja existe.
```

### Funcoes/Metodos
```csharp
public void MethodName(){}
```

* Output:
```csharp
Console.writeLine($"Hi, i'm {variable}");
```

* Input:
```csharp
Console.ReadLine();
```

* Console:
```csharp
Console.Clear();
```

* Encerrar Programa:
```csharp
Environment.Exit(0);
```

### Excecoes / Exceptions
> o erro retornado (exception) é chamado 'stack trace'
* excecao ao ler um arquivo:
```csharp
string[] linhas = File.ReadAllLines("Path_To_File");
foreach(string linha in linhas) {
	Console.WriteLine(linha);
}
```

* Tratamento de excecao com Excecao Generica:
```csharp
try {
	string[] linhas = File.ReadAllLines("Path_To_File");
	
	foreach(string linha in linhas) {
		Console.WriteLine(linha);
	}
	
} catch(Exception excep) {
	Console.WriteLine($"Ocorreu uma excecao generica. {excep.Message}");
}

```

* Excecoes Genericas e Especificas:
	* Generico: Exception 
	* Especifica: FileNotFoundException
```csharp
try {
	string[] linhas = File.ReadAllLines("Path_To_File");
	
	foreach(string linha in linhas) {
		Console.WriteLine(linha);
	}
	
} catch(FileNotFoundException excep) {
		Console.WriteLine($"Arquivo nao encontrado. {excep.Message}");
		
} catch(DirectoryNotFoundException excep) {
	Console.WriteLine($"Caminho da pasta nao encontrado. {excep.Message}");
	
} catch(Exception excep) {
	Console.WriteLine($"Ocorreu uma excecao generica. {excep.Message}");
}

```

* Finally
```csharp
try {
	string[] linhas = File.ReadAllLines("Path_To_File");
	
	foreach(string linha in linhas) {
		Console.WriteLine(linha);
	}
	
} catch(Exception excep) {
	Console.WriteLine($"Ocorreu uma excecao generica. {excep.Message}");

} finally {
	Console.WriteLine("A Tentativa foi executada com sucesso.");
}
		
```

### Classes
* Exemplo:
```csharp
public class ClassName {
	public string Property {get; set;}
	public void Methods() {}
}
```

* Instanciando uma Classe:
```csharp
Using NamespaceName;
ClassName classInstanceName = new ClassName();
```

* Validacao de Propriedades
```csharp
public class Pessoa {
	private string _nome;
	
	public string Nome {
		get => _nome.ToUpper(); //A maneira resumida e recomendade de retornar uma simples linha
		
		set {
			if (value == "") {
				throw new ArgumentException("o valor nao pode ser vazil");
			}
		}
	}
	
}
```

* Construtores
```csharp
public class Pessoa {
	public Pessoa() {
		//Padrao, permite nao ter input ao instanciar a classe
	}
	
	public Pessoa(string property) {
		//Obriga passa parametro ao instaciar a class, pode ter mais de um construtor
		Property = property;
	}

	public string Property {get; set;}
	public string Method(){}
}

Pessoa pessoaInstancia01 = new Pessoa("Nome");
Pessoa pessoaInstancia02 = new Pessoa();
```