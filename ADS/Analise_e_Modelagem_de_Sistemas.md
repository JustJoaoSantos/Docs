# U1A1 - Fundamentos da analise e modelagem de sistemas
- Sistemas: conjuntos de componentes inter-relacionados, trabalhando juntos para coletar, processar, armazenar e disseminar informacao.
- Evolucao do software
	- 1950 - 1960: sistemas operacionais(MSDOS, macintosh), Linguagem de programacao(Cobol)
	- 1960 - 1970: Crise do software, paradigmas de programacao 
	- 1980: PC (desktop), evolucao da internet
	- 1990: Internet, JAVA, Linux
	- 2000: sistemas operacionais graficos, internet
	- 2020: Computacao em nuvem, IA
	
- Fases do processo da analise de sistema 
	- Analise 
	- Projeto 
	- Implementacao 
	- Testes 
	- Documentacao (feito durante todo o processo)
	- Manutencao (pode ser tambem a incersao de uma nova funcionalidade)
	
- Principio da analise de sistemas 
	- Dominio da Informacao;
	- Comportamento do Software;
	- Diagramas;
	- Informacoes e detalhes
	
- Analista de Sistema 
	- Interage com o Cliente;
	- Levanta os requisitos do software para analisar e propor solucoes 
	- Cria e modela o software;
	- Orienta os programadores;
	- Acompanha e executa testes;
	- Garante a qualidade final do software;
	- Implanta o software desenvolvido.
	
# U1A2 - Processos de software 
- Processo de Software 
	- Criar uma padronizacao;
	- Reutilizacao;
	- Retem o conhencimento na empresa;
	- Guiar e definir as atividades de um projeto de software;
	- Determina as tarefas;
	- Reduz os riscos.
	
- Parametros a serem determinados ao estabelecer um processo de software:
    1. O evento que marca o início do processo.
    2. A matriz de responsabilidades atribuídas.
    3. As atividades a serem realizadas, juntamente com a ordem em que devem ser executadas.
    4. As entradas e saídas associadas a cada atividade.
    5. As regras e políticas que devem ser seguidas durante a execução das atividades.
    6. A infraestrutura necessária para a realização do processo.
    7. Os resultados produzidos ao final de cada processo.
	
- Atividades fundamentais do projeto 
	- Especificacao do software;
	- Projeto e Implementacao de software;
	- Validacao de software;
	- Evolucao de software.
	
	- Fase:
		- Planejamento
		
	- Atividades:
		- Levantamento de requisitos;
		- especificacao dos requisitos;
		- estimativas de prazos;
		- estimativa de recursos;
		
	- Resultados:
		- Documentacao do lenvantamento de requisitos;
		- Documentacao da especificacao de requisitso;
		- Plano de acao para determinar prazos;
		- Alocacao de recursos para criacao do software.
		
- Qualidade de Software 
	- CMMI, SPICE, MS.BR, ISOs
	
# U1A3 - Modelos de Processo de software
## Modelos Tradicionais
- Modelo Cascata:
	- Finaliza um processo para iniciar o proximo
	- So entrega ao cliente quando o projeto estiver completo
	- Comunicacao -> Planejamento -> Modelagem -> Construcao -> Entrega.
	
- Modelo Incremental
	- Descricao geral -> 
	- Desemvolvimento <-> Especificacao <-> Versao inicial 
	- Desenvolvimento <-> Versoes intermediarias
	- Desenolvimento <-> Validacao -> Versao final
	
- Modelo Evolucionario - Espiral
	- Cria um projeto(Sistema de supermercado) sistema por sistema(e.g sistema de cadastro) estes sendo completos e passados para o cliente.
	- trabalhando com versoes 

## Modelo de processo especializado
- Os modelos de processos especializados combinam elementos de um ou mais Modelos de Processos Prescritivos e são aplicados em situações que demandam uma abordagem de Engenharia de Software mais específica e detalhada.
- Modelo baseado em componentes: 
	- este modelo é frequentemente utilizado em projetos de software comercial, onde componentes de software pré-fabricados são empregados. Tais componentes, vendidos individualmente ou em conjunto, são projetados para reutilização em diversos projetos. Cada componente é uma unidade independente do software e pode ser substituído ou modificado conforme necessário.
- Modelo de métodos formais: 
	- este modelo envolve a criação de especificações matemáticas formais do software. Ele ajuda a identificar e eliminar problemas como ambiguidade, incompletude e inconsistência, fornecendo uma base sólida para a verificação de código e a detecção de erros que poderiam passar despercebidos.
- Desenvolvimento de software orientado a aspectos: 
	- esta abordagem metodológica define, especifica, projeta e constrói aspectos do software. O código é organizado de acordo com sua importância, com as classes orientadas a objetos sendo um exemplo. Os requisitos são modelados de maneira a abranger várias funcionalidades do sistema.
- Modelo de processo unificado: 
	- também conhecido como RUP (Rational Unified Process), este modelo combina características dos modelos prescritivos tradicionais com alguns princípios da metodologia Ágil. É considerado um modelo iterativo e incremental.
- Modelos de processos pessoal e de equipe: 
	- esses modelos focam no desenvolvimento de software como um esforço coletivo da equipe. No modelo de processo de software pessoal, a ênfase é na medição individual do trabalho produzido e na qualidade resultante. Já o modelo de processo de software de equipe visa criar uma equipe auto-organizada e autodirigida, com o objetivo de produzir software de alta qualidade.

## Modelo de Desenvolvimento agil 
- Metodologia Ageis
	- cliente esta envolvido durante todo o projeto
	- se ouve mais as pessoas doque os processos 
	- sao incrementais e evolutivos
	
- Metodologia agil XP ( extreme programming)
	- Planejamento -> projeto -> codificacao -> testes -> entrega.
	- Historias do usuario
	- Programacao em pares
	- Refatoracao
	
- Metodologia agil SCRUM
	- Backlog do produto (principais funcionalidades do produto)
	- Backlog da sprint (funcionalidades a ser adicionada durante a sprint)
	- Duracao da sprint: 2 - 4 semanas
	- reuniao a cada 24 horas, a.k.a daily
	- nova funcionalidade a cada sprint
	
# U1A4 - Processo Unificado 
## Modelo de Processo Unificado 
- foco em diagramacao mais robusta
- Processo Unificado 
	- abordagem iterativa e incrementaao, promovendo colaboracao entre equipes e a entrega continua de valor ao cliente.
	
- estruturado em 4 fases pricipais:
	- Concepcao: estabelece a visao geral do projeto
	- Elaboracao: refinamento dos requisitos e arquitetura do sistema
	- Construcao: desenvolvimento ativo do sistema
	- Transicao: dedicada a implantacao do sistema 
	
- aspectos do processo unificado 
	- caso de uso sao os elementos centrais;
	- foco na arquitetura;
	- iterativo e incremental 
	
- Elementos do Processo unificado 
	- Papel / Trabalhador (Quem?)
	- Artefaco (O que?)
	- Atividades (Como?) a.k.a Quem vai gerar O que?
	- Disciplina (Quando) a.k.a workflow
	
- Fluxo de Interacao 
	- Disciplina fundamentais 
		- modelagem de negocios;
		- requisitos;
		- analise e projeto;
		- implementacao;
		- testes;
		- implantacao 
	- Disciplinas de suporte
		- configuracao e ger. de mudancas;
		- gerenciamento do projeto;
		- ambiente
	
## Ciclo de vida do software 
- Concepcao -> construcao -> implantacao -> implementacao -> maturidade / utilizacao plena -> declinio -> manutencao -> declinio -> morte

# U2A1 - Fundamentos de processos de negocios 
- Classificacao de processos de negocios 
	- Macroprocesso 
		- oque a empresa faz em sua finalidade
		- fabricar automovel
		- desenvolvimento de software
	- Processo 
		- desenvolvimento produto, producao
		- desenvolvimento de web, de aplicativo
	- Sub processo 
		- design, seguranca, pintura, montagem
		- ux, ui, design, web design 
		
- Tipos de processos de negocios 
	- Processos primarios;
	- Processo de suporte;
		- processos que auxiliao os primarios, e.g RH
	- Processo de gerenciamento.

- Beneficios do processo de negocios 
	- Alinhamento dos processos com a estrategia organizacional;
	- Melhoria da qualidade dos processos e dos produtos;
	- Reducao de custos por se desenvolver um olhar mais critico;
	- Muitos processos tem reducao de sua complexidade e tornam-se mais simples, facilitando a interacao entre as areas.
	- Processos nao essenciais podem ser automatizados;
	- Aumento do envolvimento e comprimetimento dos stakeholders
	- Mehor delegacao de responsabilidades;
	- Visao funcional e visao de processos.
	
- visao funcional
	- niveis hierarquicos:
		- presidencia > Diretoria > Gerencia 
	- estruturas organizacionais 
		- presidencia -> diretoria 1 -> gerencia 1
		
# U2A2 - Gerenciamento de processo de negocios
- Visao fisica de funcoes 
	- Funcoes e Atividades 
	- e.g 
		- vendas -> obter pedido
		- financas -> pagar fornecedor / cobrar clente
		- distribuicao -> entregar produtos 

- Visao logica dos processos 
	- Subprocessos e atividades
	- Oque acontece e quando acontece 
	- e.g
		- da venda a entrega 
		- obter pedido do clente -> cobrar clente -> entregar produto ao cliente
		
- BPM 
	- construcao do processo de ponta a ponta 
	- Processo:
		- simplificacao do trabalho -> Controle da qualidade, seis sigma, Lean
		- Gestao de negocios 
		- tecnologia da informacao -> BPMS
		
- Gestao de Negocios 
	- Controles estrategicos;
		- generico de longo prazo 
		- mudar empresa
	- Controles taticos;
		- detalhacao maior, de longo a medio prazo
		- mudar departamento
	- Controles operacionais
		- analiticos, voltados a atividades 
		- mudar processo, atividade

- Alinhamento do processo de negocios
	- Organizacoes existem para entregar valor para os clentes por meio de seus produtos e/ou servicos ->
	- objetivos organizacionais devem, portanto estar conectados a entrega de valor para os clientes ->
	- processos de negocios sao os meios pelos quais produtos e servicoe sao criados e entreges para os clientes ->
	- gerenciamento de processos de negocios estabelece a forma pela qual processos de negocios sao gerenciados, executados e tranformados ->
	- portanto objetivos organizacionais podem ser atingidos por meio de um gerenciamento centrado em processos de negocios.
	
- CMMI 
	- N1 - Inicial : Nao possui nada definido.
	- N2 - Gerenciado : Capacidade de gestao de projetos 
	- N3 - Definido : Processo comum adaptado as necessidaders dos projetos 
	- N4 - Gerenciado quantitativamente: Capacidade de planejar estatisticamente a qualidade 
	- N5 - Em otimizacao: Capacidade de prevenir defeitos e inovar

- Mudanca Cultural / organizacional
	- Mudar o comportamento dos membros da organizacao;
	- Justificar a mudanca de comportamento necessaria;
	- Comunicar mensagens culturais sobre a mudanca;
	- Contratar e socializar novos integrantes;
	- Remover integrantes que nao se adaptam.
	
- BPMS: Em outras palavras, contribui para a automatização das ações e do fluxo de informações dentro dos processos
- SOA: Arquitetura orienta a servicos 

# U2A3 - Modelagem de processos de negocios 
- Funcoes dos modelos 
	- Organizacao (estruturacao)
	- Descorberta (aprendizagem)
	- Previsao (estimativas)
	- Medicao (quantificacao)
	- Explicacao (ensino, demonstracao)
	- Verificacao (validacao)
	- Controle (estabelecimento de restricoes e objetivos)

- Conteudo dos modelos 
	- Atividades;
	- Fluxo de trabalho;
	- Recursos;
	- Decisoes;
	- Eventos;
	- Tempo;
	- Responsabilidades;
	- Objetivos 
	
- Diagrama: 
	- Um diagrama apresenta os elementos principais de um fluxo de processo, 
	- simplificando detalhes menores para facilitar a compreensão dos fluxos de trabalho
- Mapa: 
	- Um mapa oferece uma visão abrangente dos principais componentes do processo, 
	- acrescentando mais precisão do que um diagrama.
- Modelos:
	- Um modelo implica a representação de um estado específico do negócio (atual ou futuro) e dos recursos correspondentes, 
	- como pessoas, informações, instalações, automação, finanças e insumos.

- Arquitetura de negocios
	- Modela os processo de negocios em um nivel conceitual
	- Enfoca as capacidade de negocio, ou seja "O Que" a empresa faz 
	- Concentra-se na criacao de modelos de negoci para a eficacia operacional
	
- Arquitetura de processos 
	- Define "Como" os produtos, servicos ou entregaveis sao construidos e entregues.
	- Detalha as atividades necessarias para alcancar as capacidades de negocios.
	- Preocupa-se com a eficiencia na gestao e execucao das atividades fisicas.
	
- Notacoes de modelagem de negocios 
	- BPMN (Business Process Model and Notation) 
	- Fluxograma:  representação visual que utiliza símbolos gráficos para descrever a sequência de atividades em um processo.
	- EPC (Event-Driven Process Chain)
	- UML (Unifed Modeling Language)
	
- Importancia da modelagem
	- Melhorar processos;
	- Eliminar ou automatizar processos;
	- Documentar processos
	
# U2A4 - Business Process Model and Notation (BPMN)
- Elementos da BPMN - Basicos 
	- Atividade 
	- Evento 
	- Gateway 
	- Conector 
	
- Elementos da BPMN - Subprocessos 
	- Sub processo colapsado simples 
	- Sub processo transacional 
	- Subprocesso com marcador de loop
	- subprocesso com marcador de multiplas instancias
	- etc...
	
- elementos da BPMN - eventos 
	- Nada (simples)
	- Link (conector)
	- Multiplo 
	- Mensagem 
	- Regra 
	- Marca tempo 
	- etc...
	
- Elementos da BPMN - Gateways 
	- exclusivo (XOR) baseado em dados
	- Exclusivo (XOR) baseado em evento 
	- Inclusivo (OR) para multipla escolha
	
- Elementos da BPMN - Conectores 
	- Direcao de sequencia de fluxo 
	- Direcao do fluxo de mensagem 
	- Associacao de elemetos
	
- Elementos da BPMN - Outros
	- Piscina (Pool)
	- Raias 
	- Objeto de dados 
	- Grupo
	- Anotacao
	
