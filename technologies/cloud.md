# Cloud
> rede de servidores remotos que armazenam e gerencial dados e executam aplicativos e fornecem conteudo.

- ambiente On-Premise
	- datacenter totalmente local, da propria empresa
	
- As a service
	- alugando poder de processamento das maquinas locais a terceiros

- Ambiente cloud
	- datacenter totalmente em nuvem, alugado de outra empresa 
	
- hybrid
	- datacenter local e em nuvel quando necessario.

- infra as a service (IaaS)
	- consumindo infraestrutura como servico, alugando datacenters
	
- Platforms
	- empresas especializadas em alugar IaaS
	- e.g AWS(Amazon), Azure(microsoft), Oracle, Gcp (google)
	
- Regions
	- maquinas espalhadas em zonas e regioes diferentes
	- e.g us-east-1 (norte virginha, EUA), sa-east-1 (Sao Paulo, Brasil)

- Zonas 
	- sub areas de regioes 
	- e.g us-east-1a
	
## AWS 
### Infraestrutura Global AWS
- infraestrutura de datacenters ao redor do mundo que fornecem os servicos aws,
- composto por regioes e zonas de disponibilidade
- vantagens: alta disponibilidade, tolerancia a falhas

- Regioes:
	- locais de hoting do datacenters AWS
	- cada regiao possui locais isolados chamados zonas de disponibilidade,
	- todas regioes sao conectadas por cabos de alta performance

- zonas de disponibilidades:
	- chamadas tambem de AZs (avaliability zones)
	- agrupamento de datacenters isolados dentro de uma regiao 
	- rede, energia e conectividade redundantes,
	- proximas o suficiente para manter baixa latencia, longe o suficiente para evitar que um desastre afete mais de uma AZ,
	- recomendacao: execute pelo menos em duas AZs.
	
- Pontos de presenca:
	- tambem chamado de Edge Locations, locais de borda ou redes de borda,
	- funcionam como ponto especificos pelo globo para distribuir conteudo de forma rapida, baixar a latencia, etc,
	- e.g: Route 53(DNS), Cloud Front(CDN)
	
- Provisionamento de recursos AWS:
	- console de gerenciamento,
		- acesso por portal web, com usuario:senha
	- AWS CLI,
		- instalado na maquina
		- acesso por linha de comando
	- SDKs
		- acesso automatizado, APIs AWS atraves de SDK
		
- Provisionando infraestrutura:
	- Elastic Beanstalk
		- automatiza processo de deploy, 
		
	- Cloud Formation
		- IAC: infraestructure as Code
		- automatizar processo de construcao de ambientes em AWS, com scripts em .json ou .yaml
		
- EC2 - Elastic Compute Cloud
	- Capacidade computacional segura e redimensionavel,
	- computacao: CPU, Memoria, Rede, Armazenamento, OS,
	- Definicao de preco conforme uso e modalidades especificas a necessidade,
	- instancias com tipos otimizados para sua atividade
	
- Instancia: servidor virtual AWS 
	- tipos:
		- uso geral: equilibrio de recursos de computacao, indicado para servidor de app, jogos, backend, db pequenos
		- otimizado para computacao: ideal para cargas de trabalho que exigem processadores de alto desempenho, indicado para os mesmos do geral quando nescesario maior desenpenho,
		- otimizado para memoria: projeto para alto desempenho no processamento de muitos dados,
		- computacao acelerada: usa aceleracao de hardware ou coprocessadores para executar alguns funcoes de forma mais eficiente,
		- otimizado para Armazenamento: ideal para cargas de trabalho que exigem acesso de leitura e gravacao de alto desenpenho

- Amazon EC2 AutoScaling
	- Ajusta a capacidade da instancia EC2 de acordo com a necessidade
	- prove escalabilidade horizontal para seus servicos,
	- melhora a tolerancia a falhas com identificacao de instancias indisponiveis e implantacao de multi-AZ,
	- melhor gerenciamento de custos
	- configuracao:
		- auto scaling group:
			- tamanho minimo: 1u
			- capacidade desejada: 2u
			- tamanho maximo: 4u
			- scala com forme a nescessidade: ira automaticamente definir se usara minimo, desejado ate o maximo e.g 1u ~ 4u
	- abordagem:
		- scaling preditivo
		- scaling dinamico
		- possivel combinar os dois

- ELB - Elastic Load Balancing
	- Balanciamento de carga: algoritimo que determina para qual instancia EC2 uma request sera enviada
	- escopo regional,
	- escala de forma automatica, sem custos,
	- junto ao EC2 autoscaling permite criar aplicacoes com alta disponibilidade
	
- Servicoes de mensageria
	- SQS: Simple Queue Service
		- servicos se comunicam de forma asyncrona
		- segue ordem FIFO (First In First Out)
		- sistema envia uma mensagem para fila, o outro processa e exclui
	- SNS: Simple Notification Service
		- sistema pub/sub,
		- utiliza topicos como estrutura,
		- sistema publica mensagens no topico e assinantes escutam
		
- Computacao sem servidor 
	- tambem chamado Servless
	- o codigo e executado em servidores sem que voce precise provisionar ou gerenciar esses servidores
	- capacidade automaticaemnte ajustada pelo servico, sem a necessidade de nenhuma configuracao
	- e.g AWS Lambda
		- execucao de codigo sem provisionar servidores,
		- codigo organizadoem funcoes,
		- pode-se escolher linguagem de preferencia
		
- Containers em AWS
	- forma padrao de empacotar aplicativo em unico objeto,
	- executado como processos isolados, e.g docker
	- servicoes AWS:
		- ECR - Elastic Container Registry
			- repositorio de imagens de containers
		- ECS - Elastic Container Service 
			- servicos de execucao de container docker da AWS usando clusters
		- EKS - Elastic Kubernetes Service 
			- segunda forma de executar containers com clusters
		- AWS Fargate
			- servico servless para executar aplicacoes de forma mais facil com EKS ou ECS