# Banco de Dados
> Colacao organizada de informacoes(dados) estruturadas.

* e.g API -> Banco de dados <- Web <- Cliente

## Bancos de dados relacional
> Mais utilizado atualmente, armazenando dados estruturados, sendo organizado em tabelas, com colunas e linhas, que se relacionam entre si
e.g SQL server, Oracle database, MySQL, etc.

### Tabelas
> Sao dados estruturados e organizados logicamente em formato de linha e coluna

## Banco de dados nao-relacional
> os dados nao sao armazenados em tabelas mas de maneira nao estruturadas(.mp3, posts, .txt, .json) ou semi-estruturados 
e.g mongoDB

* existem varios tipos: document db, key-value db, wide-column stores e graph db. 

## DBMS
> Database Management System, software utilizado para acessar, manipular e monitorar um sistema de banco de dados.

### SQL Server Management Studio
#### SQL Server Configuration Manager
* SQL Server Services -> SQL Server -> Proprieties -> Services -> Start Mode:
	* Automatic / Manual
	* se deixado automatico o servido sera ligado durante a inicializacao da maquina/Computador.

## Linguagem SQL
> Structured Query Language: usado para consulta e manipulacao de dados.

### SQL Commands
* DDL: Data Definition Language
	* Create, Drop, Alter, Truncate
	
* DCL: Data Control Language
	* Grant, Revoke
	
* DML: Data Manipulation Language	
	* Insert, Update, Delete

* TCL: transaction ControlLanguage
	* Commit, Rollback, Save Point

* DQL: Data Query Language
	* Select
	
* Comentarios:
```sql 
--Isso e um Comentario.
```

#### Tipos de Dados
* char(n): valor fixo, maximo permitido 8000 characters
* varchar(n): variavel com valor maximo, maximo permitido 8000 characters
* varchar(max): variavel com valor maximo de 1,073,741,824 chars 
* text: variavel com valor maximo de 2GB of text data 
* bit: 0, 1 ou NULL
* int: numeros inteiros
* decimal: valores monetarios
* float(n): numeros reais
* datetime: datas iniciando em 1753 ate ano 9999
* datetime2: datas inicianod em 0001 ate ano 9999 e hora

#### DDL
* Criando uma tabela:
```sql 
CREATE TABLE Produtos (
	Id int IDENTITY(1,1) PRIMARY KEY NOT NULL,		--IDENTITY se autoincrementa
	Nome varchar(255) NOT NULL,
	Cor varchar(50) NULL,
	Preco decimal(13, 2) NOT NULL,   --(numero max, casa decimal max)
	Tamanho varchar(5) NULL,
)	Genero char(1) NULL			--passando um character (M/F)
```

#### DQL
* selecionar tudo da tabela clientes:
```sql
SELECT * FROM Clientes
```

* selecionar apenas as colunas desejadas da tabela clientes:
```sql 
SELECT Nome, Sobrenome, Email FROM Clientes
```

* selecionar dados especificos de colunas especificas:
> NT* Ordem: SELECT -> WHERE -> ORDER BY
> NT** String = ''(Aspas Simples)
```sql 
SELECT * FROM Clientes 
WHERE Nome = 'Adam'
```
* Selecionando por Duas Colunas 
```sql 
WHERE Nome = 'Adam' AND Sobrenome = "Reynolds'
```

* Selecionando por uma coluno ou outra
```sql 
WHERE Nome = 'Adam' OR Sobrenome = "Reynolds'
```

* Filtrar por primeira letra, se o dado na coluna Nome comeca com 'G'
```sql 
WHERE Nome LIKE 'G%'
```

* Filtrar por dado que possui a letra 'G'
```sql 
WHERE Nome LIKE '%G%'
```


* Ordenar a tabela selecionada previamente pela coluna Nome me ordem ascendente.
```sql
ORDER BY Nome
```

* Ordenar a tabela selecionada previamente pela coluna Nome. em ordem decrescente
```sql
ORDER BY Nome DESC
```

* Ordenar pelo nome e depois pelo sobrenome
```sql 
ORDER BY Nome, Sobrenome 
```

#### DML
* Insertindo um dado na tabela clientes
> NT* Voce e obrigado a obdecer a ordem da coluna que voce especificou.
```sql 
INSERT INTO Clientes (Nome, Sobrenome, Email, AceitaComunicados, DataCadastro)
VALUES ('Leonardo', 'Silva', 'email@email.com', 1, GETDATE())
```

* inserindo um dado na tabela de forma resumida:
> NT* Voce e obrigado a obdecer a ordem da colunas.
```sql 
INSERT INTO Clientes VALUES ('Leonardo', 'Silva', 'email@email.com', 1, GETDATE())
```

* Atualizando um dado
```sql 
UPDATE Clientes
SET Email = 'emailatualizado@email.com', AceitaComunicados = 0
Where Id = 1003
```

* Deletar dado
```sql 
DELETE Clientes 
WHERE Id = 1001
```

#### TCL
* Cria um Check Point
```sql 
BEGIN TRAN 
```

* Volta para check point 
```sql
ROLLBACK
```



### Built-in Functions
* Contando linhas na tabela 
```sql 
SELECT COUNT(*) QuantProdutos FROM Produtos  --Retorna o numero de linhas(todas) na tabela Produtos. nomiando a coluna de contagem como QuantProdutos.
```

* Contando linhas com condicao
```sql 
SELECT COUNT(*) QuantProdutos FROM Produtos WHERE Genero = 'U'
```

* Somando Valores de uma coluna, contando que sejam numeros:
```sql 
SELECT SUM(Preco) PrecoTotal FROM Produtos  --Retorna a soma de todas as colunas preco, da tabela produtos, nomeando a nova tabela de PrecoTotal
```

* Selecionando o Maximo e Minimo valor da tabela:
```sql 
SELECT MAX(Preco) ProdutoMaisCaro FROM Produtos --retorna o maior valor na tabela preco, em uma coluna chamada ProdutoMaisCaro.
```

```sql 
SELECT MIN(Preco) ProdutoMaisBarato FROM Produtos
```

* Retorna a Media de todos os valores da coluna expecificada:
```sql 
SELECT AVG(Preco) Media FROM Produtos 
```

* Concatenando Colunas 
```sql 
SELECT Nome + ' - ' + Cor FROM Produtos   --Retorna as Colunas Nome e Cor Concatenadas com um '-'
```

* Tratamento de String
```sql 
SELECT UPPER(Nome) NomeMaiusculo, LOWER(Cor) Minusculo FROM Produtos --Torna a coluna Em Maiusculo/Minuscolo e coloca elas na coluna designada.
```

* Adicionar nova coluna 
```sql 
ALTER TABLE Produtos 
ADD DataCadastro DATETIME2    --Altera a tabela Produtos, adicionando a coluna DataCadastro com tipo DATETIME2.
```

* Deletando uma coluna:
```sql
ALTER TABLE Produtos 
DROP COLUMN DataCadastro --Deleta a Coluna DataCadastro
```

* Formatando data:
```sql 
SELECT FORMAT(DataCadastro, 'dd/MM/yyyy hh:mm') Data FROM Produtos
```

* Agrupando Dados, retorna a linha e quantidade de item da coluna especificada.
```sql 
SELECT Tamanho, COUNT(*) Quantidade --retorna a coluna Tamanho e quantidade de cada tamanho nomeando a nova coluna Quantidade.
FROM Produtos 
WHERE Tamanho <> '' -- Tamanho Diferente '<>' de vazio
GROUP BY Tamanho -- agrupe pela coluna Tamanho.
ORDER BY Quantidade DESC 	--
```

* Foreign Key 
```sql
CREATE TABLE Enderecos (
	Id int PRIMARY KEY INDENTITY(1,1) NOT NULL,
	IdCliente int NULL,
	Rua varchar(255) NULL,
	Bairro varchar(255) NULL,
	Cidade varchar(255) NULL,
	Estado char(2) NULL,
	
	CONSTRAINT FK_Enderecos_Clientes FOREIGN KEY(IdCliente)
	REFERENCES Clientes(Id)   --Restricao FK_Enderecos_Clientes se referencia a tabela cliente, coluna Id.
)
```

* requere duas tabelas como uma 
```sql 
SELECT * FROM Clientes 
INNER JOIN Enderecos ON Clientes.Id = Enderecos.IdCliente --Junta a tabela de endereco na tabela de cliente onde o id do cliente e igual a IdCliente da tabela enderecos.
WHERE Clientes.Id = 4
```