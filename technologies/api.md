# APIs
> Application Programming Interface, forma de comunicacao entre computadores ou programas de computadores, a.k.a software que fornece informacao para outro software.

* e.g api: App <--> API <--> Server.
* e.g api externa: Site ecommerce <--> api de entrega <--> empresa de entraga
* e.g api interna: Frontend <--> Backend <--> Banco de Dados

* Request:
	* http://date.nager.at:
		* GET /api/v3/PublicHolidays/{year}/{CoutryCode}
		* Year: 2017
		* CoutryCode: BR
* Response:
	{
		"date" = "date",
		"title" = "title"
	}
	
## API no .NET
* para criar um projeto API:
```csharp
dotnet new webapi
```

* para executar API -automaticamente recompilando ao perceber mudancas:
```csharp
dotnet watch run
```