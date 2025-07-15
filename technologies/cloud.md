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
			
- Redes 
	- Amazon VPC
		- Virtual Private Cloud,
		- permite construir e configurar redes virtuais na AWS,
		- sub-redes: privadas e publicas,
		- "Todo comeca dentro de um VPC"
		
	- Gateway
		- recebe requests da internet e redireciona para uma sub-rede publica
		
	- VPG: virtual private gateway
		- permite o trafego de dados sigilosos pela internet por meio de um vpn
		
	- Network ACLs
		- tambem chamado de lista de controle de acesso ou LCA
			- controla trafego de entrada e saida de sub-redes,
			- comportamentos stateless - regras individuais para entrada e saida
			- por padrao,permite todo trafego de entrada e saida
			
	- grupus de seguranca
		- controla trafego de entrada e saida de instancia EC2,
		- comportamento Stateful - regras de entradas sao lembradas e usadas para saida
		- por padrao, nega todo o trafego de entrada e permite todo trafego de saida
		
# Armazenamento e Database AWS 
## Armazenamento de dados em nuvem
- Tipos de armazenamentos:
	- Object Storage (armazenamento de objetos)
		- dados como objetos (arquivos e metadados)
		- dados nao estruturados
		- casos de uso: data lakes, midias, backup e recuperacao
		
	- File Storage  (armazenamento de arquivos)
		- sistemas de arquivo compartilhados,
		- permite acesso por meio de servidores, aplicacoes e usuarios,
		- caso de uso: ferramentas de desenvolvimento, diretorios pessoais
		
	- Block storage (armazenamento de blocos
		- armazenamentos de blocos: HDD, SSD
		- dispositivos com diferentes configuracoes de leitura e escrita,
		- caso de uso: maquinas virtuais, containers, banco de dados
		
- EBS - Amazon Elastic Block Store
	- armazenamento em blocos,
	- block, blocos = HD, fisico,
	- projetado para funcionar em conjunto com a instancia EC2
	- anexe o volume a uma instancia EC2
	- se a uma falha ou desativacao da instancia EC2 os dados estarao salvos
	
	- Volume Instance Store, Instancia EC2
		- armazenamento de blocos
		- ideal para dados de armazenamento temporario
		- discos anexados fisicamente ao computado do host
		- perda de dados em caso de : falha de disco, instancia parada, host desliga, etc.
		
- S3
	- composisao de um objeto 
		- chave: nome/id de um objeto
		- valor: dado do objeto 
		- metadados: pares de chave/valor que compoem o objeto
		
	- buckets S3 
		- container para objeto armazenado no S3 
		- sem limitacao em numero de objetos 
		- objetos podem ter ate 5TB de tamanho 
		- uma conta pode ter ate 100 buckets
		
	- classes de armazenamento:
		- S3 Standard
			- projetado para dados acessados com frequencia,
			- custo mais alto
			- uso: sites, distriuicao de conteudo e analise de dados 
		
		- S3 standard-infrequent access
			- chamado tambem de stardard-IA
			- semelhante ao S3 stardard
			- ideal para dados acessados com pouca frequencia 
			- taxa por GB de armazenamento e recuperacao mais baixo
			
		- S3 one zone-infrequent access 
			- menor preco que s3 stardard-IA 
			- armaena dados em uma unica zona de diponibilidade
		
		- s3 intelligent-tiering
			- ideal para dados com padroes de acesso desconhecidos ou em alteracao
			- processo automatico de classe 
		- S3 glacier instant retrieval 
			- ideal para dados de longa duracao, raramente acessados mas que exigem recuperacao rapida (milissegundos)
			- oferece acesso tao rapido quanto standard e standard-IA
		
		- S3 glacier fliexible retrieval
			- ideal para dados que nao requerem acesso imediados
			- ideal para caso de uso de backups nao urgentes
			- usuario pode escolher qual velicidade de recuperacao			
			
		- S3 glacier Deep archive
			- suport a retencao e preservacao digital de longo prazo para dados que podem ser acessados 1 ou 2 vezes por ano
			- recuperacao de dados em ate 12 horas
			
- EFS - Amazon Elastic File System
	- Fornece um sistema de arquivo 
	- servless e totalmente elastico,
	- escala ate petabytes
	- aumenta e diminui conforme adicao e remocao de arquivo 
	- compativel com protocolo NFS (network file system)
	- pode sera cessado por EC2 ,lambda, ECS 
	- classes de armazenamento: padrao Standard e stadard IA
	
- Amazon Relational Database service
	- facilita configuracao e provisionamento de hardware,
	- patches automatizados,
	- backup,
	- redundancia,
	- failover e recuperacao e desastres
	- mechanismos compatives:
		- mySQL
		- postgreeSQL
		- MariaDB
		- Oracle 
	
- Amazon Aurora
	- servless,
	- mecanismos compativeis: postgreSQL e mySQL
	- preco 1/10 de outros vendors,
	- replicacao multi-regional 
	- ate 15 replicas de leituras,
	- backups continou via S3
	
- Amazon DocumentDB
	- BD de documentos,
	- gerenciamento de conteudo,
	- catologos, perfis de usuarios,
	
- amazon neptune
	- redes sociais, mecanismos de recomendacao, etc,
	
- amazon QLDB
	- quantum ledger database,
	- banco de dados servico ledger,
	- imutabilidade,
	- indicado para historicos
	
- amazon dynamondb accelerator
	- tambem chamado de dax
	- camada de cache nativa para otimizar tempo de leitura de dados
	
- amazon elasticache
	- camada de cache sobre banco de dados
	- compativem com redis e memcached
	
- amazon redshift
	- servico de data warehouse para analise de big data
	- oferece coleta de informacoes de muitas fontes de dados,
	- projeta relacoes e tendencias de dados,
	- usando redshift spectrum e possivel rodar comnados SQL em cima de todas as fontees de dados agrupadas