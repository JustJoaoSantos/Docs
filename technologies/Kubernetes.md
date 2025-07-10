# Kubernetes
> Kubernetes / K8s : ferramenta open source de orquestracao de containers, originalmente desenvolvida pelo google.
- As K8s ajudam na organizacao e administracao de aplicacoes em containers, estas aplicacoes podem estar em diferentes ambientes de implementacal, como:
	- infraentrutra local,
	- maquinas virtuais,
	- cloud publica,
	- cloud hibrida
- Usado para:
	- migracao de aplicacoes monoliticas para microservicos,
	- disponibilidade da aplicacao (diminuicao downtime),
	- escalabilidade e alta performance,
	- recuperacao de desastre (backup/restore)
- ciclo de utilizacao:
	1. cria um cluster kubernetes,
	2. implantar um aplicativo,
	3. explorar o aplicativo,
	4. exponha o aplicativo publicamente,
	5. escale o aplicativo,
	6. atualize o aplicativo
	
## Arquitetura basica
- Kubernet cluster: conjunto de nodes que executam aplicativos em containers 
- Node: servidor que executa aplicativos dentro de um 'pods', pode ser uma maquina virtual ou fisica
- Pod: menor unidade do kubernetes, abstracao de container, normalmente executado um container por pod
