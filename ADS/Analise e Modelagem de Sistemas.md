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
	
# U3A1 - Engenharia de requisitos 
- Requisitos de sistemas 
	- condicoes e funcionalidades essenciais que um sistema deve atender para satisfazer as necessidades e expectativas dos usuarios garantindo sua eficiencia e eficacia operacional.

- Qualificacao dos requisitos 
		- Exatidao: requisito do produto a ser desenvolvido
		- Precisao: possui apenas uma unica interpretacao
		- Completude: reflete as decisoes de especificacao que foram acordadas entre as partes envovidas
		- Consistencia: nao pode haver conflitos entre os requisitos e qualquer um dos seus subconjuntos
		- Priorizacao: todo requisito sera rotulado de acordo com a sua importancia
		- Verificabilidade: demonstra a comformidade do produto final com cada requisito elencado.
		- Modificabilidade: deve ter estrutura e estilo que permitam dudancas de forma facil.
		- Rastreabilidade: permite a determinacao dos antecedentes e das implicacoes de todos os requisitos.
		
- Classificacao dos requisitos 
	- Essencial: Ponto focal e central do sistema 
	- Importante: Relevantes mais nao essencial 
	- Desejavel: Interecante porem nao faz difereca se nao tiver
	
- Tipos de requisitos 
	- Funcionais: Acoes executada pelo sistema, funcoes / features 
		- Exemplos:
			- RF001 - O sistema deve manter os dados pessoais e academicos dos alunos.
			- RF002 - O sistema deve apresentar um relatorio de aproveitamento dos alunos.
			- RF003 - O sistema deve permitir que o aluno faca a matricula por disciplina.
	- Nao-funcionais/estruturais:  qualidade do sistema como acessibiliadde, usabilidade, seguranca, etc.		
		- exemplo:
			- RNF001 - O tempo de espera do aluno para visualizar as notas, nao podera exceder os sete segundos.
			- RNF002 - o sistema devera ser implementado utilizando a linguagem de programacao JAVA.
			- RNF003 - A paleta de cor do sistema deverao obdever o padram do logo do cliente.
			
	- Requisitos de domínio: estes determinam as características do domínio do sistema, refletindo as particularidades do ambiente em que o sistema será utilizado. Eles podem impor restrições aos requisitos funcionais ou fornecer cálculos específicos sobre determinados requisitos com base no contexto do domínio do sistema.

- Metricas dos requisitos nao funcionais 
	- Velocidade
	- Tamanho
	- Usabilidade
	- Confiabilidade 
	- Robustez 
	- Portabilidade
	
- Classificacao dos requisitos nao-funcionais 
	- Requisitos de produto
		- estes especificam ou restringem o comportamento do sistema e podem incluir determinações sobre a linguagem de programação a ser utilizada.
		- Requisitos de Usabilidade
		- Requisitos de Eficiencia 
		- Requisitos de Confianca
		- Requisitos de Protecao
		- Requisitos de Desenpenho
		- Requisitos de Espaco
		
	- Requisitos Organizacionais 
		- estes são derivados das políticas e procedimentos da empresa, do cliente e do desenvolvedor.
		- Requisitos Ambientais;
		- Requisitos Operacionais;
		- Requisitos de Desenvolvimento 
		
	- Requisitos externos
		- estes englobam todos os fatores externos ao sistema que podem influenciar no seu desenvolvimento, desde que estejam em conformidade com a legislação vigente.
		- Requisitos Reguladores
		- Requisitos Eticos
		- Requisitos  Legais
		- Requisitos Contabeis
		- Requisitos de Seguranca / Protecao
		
- Engenharia de requisitos 
	1. Analise do problema 
	2. Levantamento dos requisitos 
	3. Elicitacao dos requisitos 
	4. Classificacao dos requisitos 
	5. Priorizacao e Negociacao dos requisitos 
	6. Especificacao dos requisitos
	
# U3A2 - Elicitacao e analise de requisitos
- Etapas da elaboracao do documento de requisitos 
    1. Concepção: define-se o escopo geral do sistema e identificam-se todos os stakeholders envolvidos.
    2. Elicitação: realiza-se a coleta de requisitos funcionais e não funcionais, utilizando técnicas como entrevistas, observação e pesquisa.
    3. Elaboração: detalha-se cada requisito inicialmente expresso em linguagem natural, transformando-os em modelos conceituais, muitas vezes utilizando a Linguagem Unificada de Modelagem (UML), com o objetivo de eliminar erros, omissões, duplicações e inconsistências.
    4. Negociação: identificam-se e tratam-se requisitos conflitantes, realizando-se negociações entre as partes envolvidas para ajustar e/ou eliminar tais requisitos.
    5. Especificação: transformam-se os requisitos em uma visão mais detalhada do sistema, considerando o desenvolvimento da solução.
    6. Validação: realiza-se a validação dos requisitos pelos usuários relevantes, verificando se todas as necessidades foram atendidas, sob a perspectiva do cliente.
    7. Gerenciamento: consiste na verificação contínua, ao longo do processo, da conformidade dos requisitos com o escopo do projeto, bem como na garantia da rastreabilidade, que envolve o controle de possíveis alterações que os requisitos possam sofrer.
	
- Elicitacao de requisitos 
	- Especificar o escopo do problema do sistema;
	- Avaliar as oportunidades de reutilizacao de solucoes existentes;
	- Identificar os stakeholders diretamente envolvidos com o sistema;
	- Elicitar e qualificar os requisitos do sistema;
	- Analisar os requisitos elicitados;
	- Validar os requisitos elicitados.
	
- Levantamento e analise de requisitos 
	- Compreesao do dominio -> Coleta e Classificacao de requisitos -> Negociacao -> Especificacao -> Validacao -> Documentacao de requisitos
	
- Elicitacao de Requisitos 
	- Descoberta de requisitos 
	- Classificacao e organizacao de requisitos 
	- Priorizacao e negociacao de requisitos 
	- Especificacao de requisitos / documentacao 
	
- Tecnicas de Elicitacao de requisitos 
	- Pesquisa 
	- Entrevista 
	- Reunioes 
	- Documentos 
	- Etnografia
	
- Validacao de requisitos 
	- Validade;
	- Consistencia;
	- Completude;
	- Realismo;
	- Ambiguidade;
	- Rastreabilidade.
	- Verificavel;
	
# U3A3 - Modelagem de requisitos
- Objetivos 
	- Descrever o que o cliente solicitou
	- Estabelecer uma base para a criacao do projeto de software 
	- Produzir um conjunto de requisitos que possa ser validado assim que o software estiver concluido
	
- Caracteristicas dos requisitos 
	- Requisitos estao corretos?
		- todos os envolvidos dem verificar se os requisitos estao corretos 
	- Requisitos estao consitentes?
		- Procurar inconsistencia de informacao 
	- Requisitos estao completos? 
		- verificar a existencia de lacunas nos requisitos
	- Requisitos sao realistas?
		- verificar se o que esta sendo solicitado se encontra sendo realmente possivel de ser realizado
	- Requisito descreve algo necessario para o clente?
		- requisito deve focar no que o sistema devera realizar, evitando funcoes desnecessarias.

- Diretrizes na criacao de requisitos 
	1. Estabelecer um formato padrão e garantir sua adoção em todas as definições de requisitos. Padronizar o formato reduz a probabilidade de omissões e facilita a verificação dos requisitos. Sempre que viável, é sugerido expressar o requisito em uma ou duas frases em linguagem natural.
    2. Utilizar a linguagem de maneira consistente para distinguir entre requisitos obrigatórios e desejáveis. Os requisitos obrigatórios são aqueles que o sistema deve obrigatoriamente suportar e geralmente são expressos com o termo "deve". Já os requisitos desejáveis não são essenciais e são indicados pelo termo "pode".
    3. Destacar partes importantes do requisito usando realces de texto, como negrito, itálico ou cor.
    4. Evitar presumir que os leitores tenham conhecimento técnico em engenharia de software. Termos como "arquitetura" e "módulo" podem ser facilmente mal interpretados. Sempre que possível, evitar o uso de jargões, abreviações e acrônimos.
    5. Associar um racional a cada requisito de usuário sempre que possível. O racional deve explicar por que o requisito foi incluído e quem o propôs (a origem do requisito), facilitando a identificação de quem contatar caso o requisito precise ser alterado. O racional dos requisitos é particularmente útil em momentos de mudança, ajudando a discernir quais alterações seriam indesejáveis.


- Notacoes para escrever requisitos 
	- Sentencas em linguagem natural
		- os requisitos sao escritos usando frases numeradas em linguagem natural. cada frase deve espressar um requisitos 
	- Linguagem natural estruturada
		- os requisitos sao escritos em linguagem natural em um formulario ou template. cada campo fornece informacoes sobre um aspecto do requisito 
	- Notacoes graficas 
		- modelos graficos, suplementados por anotacoes em texto, sao utilizados para definir os requisitos funcionais do sistema. sao utilizados com frequencia os diagramas de caso de uso e de sequencia da UML 
	- Especificacoes matematicas 
		- essas notacoes se baseiam em conceitos matematicos como as maquilnas de estado finitos ou conjuntos.
		
- Modelo - REMO 
	- pode ser usado em conjunto com BPMN 
	- e.g 
		- Preecher formulario de matricula do aluno -> formulario de cadastro do aluno 
		- <-requisito gerado-> RF0015 - Cadastrar alunos - o sistema deve manter os dados do aluno.

- Modelo - Diagrama de requisitos (UML)
	- menos utilizado 
	- e.g 
		- <requisito>
			- Entrada de dados 
			- texto: "O aluno devera fornecer os dados ao  sistema"
			- ID: 1.1.1
			
		- <requisito>
			- Disponibilizacao das disciplina 
			- Texto: "O sistema  deve mostrar as disciplinas que o aluno podera cursar"
			- ID: 1.1.2
			
		- <requisito>
			- Processo de matricula 
			- Texto: "o sistema deve fornecer a matricula do aluno via internet"
			- ID: 1.1.3
			
- Modelo - Diagrama de casos de uso (UML)
	- mais utilizado que o diagrama de requisitos 
	- demonstra melhor quem interage com oque 
	- facil de entender
	- e.g 
		- ator: secretaria -> [matricula aluno] -> ator: aluno 
		- ator: secretaria -> [gerar boletos] -> ator: aluno 
			
- Modelo - Descricao de casos de uso (UML)
	- forma mais detalhada do diagrama caso de uso 
	- e.g 
		- Nome do caso de uso: Matricular aluno 
		- Ator principal: aluno 
		- atores secondario: secretaria 
		- resumo: este caso de uso tem por objetivo detalhar o processo de matricula do aluno no sistema 
		- pre-condicoes:
			1. o aluno dera estar matriculado no sistema.
			2. nao podera haver nenhuma pendencia financeira no sistema 
		- Fluxo principal 
			- Acoes do ator:
				1. aluno informa a matricula e senha para se logar ao sistema 
				2. 
				3. 
				4. 
			- acoes do sistema:
				1. sistema devera verificar a matricula e validar a senha do aluno 
				2. 
				3. 
		- Fluxo alternativo:
			- acoes do ator:
				1.
				2.
			- acoes do sistema:
				1.
				2.
				
# U3A4 - Validacao e modificacao nos requisitos 
- Verificacao nos requisitos 
	- validade;
	- consistencia;
	- completude;
	- realismo;
	- verificabilidade
	
- Validacao nos requisitos 
	- Revisoes de requisitos:  uma equipe de revisores examina os requisitos em busca de erros e inconsistências de forma sistemática
	- Prototipacao:  desenvolvimento de um modelo executável do sistema para que os usuários finais e clientes possam experimentá-lo, fornecendo feedback para possíveis mudanças nos requisitos.
	- Geracao de casos de teste: os requisitos devem ser testáveis, e o desenvolvimento de casos de teste revela problemas potenciais nos requisitos. Se um teste é difícil de conceber, pode indicar que os requisitos são complexos e precisam ser reconsiderados.
	
- Gerenciamento de mudancas dos requisitos 
	- Problema identificado -> 
	- Analise do problema e especificacao da mudanca ->
	- Analise da mudanca e estimativa de custo ->
	- Implementacao da mudanca ->
	- Requisitos revisados
	
- Importancia da rastreabilidade 
	- Identificacao de requisitos ausentes;
	- Eliminacao de requisitos desnecessariso;
	- Certificacao e conformidade;
	- Analise de impacto de mudancas;
	- Manutencao de software;
	- Execucao de testes.
	
- Matriz de rastreabilidade 
	- facilita a visualizacao do impacto de uma mudanca 
	- mostra graficamente que requisito depende ou interage com oque 
	
# U4A1 - Linguagem de Modelagem Unificada - UML
- UML (Unified Modeling Language)
	- paradigma Orientada a objetos
	- Nao e uma linguagem de programacao;
	- Linguagem de modelagem, uma notacao destinada a auxiliar engenheiros de software na definicao das caracteristicas do sistema;
	- isso inclui requisitos, comportamento, estrutura logica, dinamica de processos e ate requisitos fisicos relacionados ao hardware no qual o sistema sera implantado.
	
- Modelo de software 
	- representa uma pespectiva de um sistema fisico;
	- Representacao abstrata do sistema com um proposito especifico, como descrever aspectos estruturais ou comportamentasi do software.
	
- Diagramas 
	- Diagrama de estrutura:
		- Diagrama de classes 
		- Diagrama de estrutura compostas 
		- Diagrama de objetos 
		- Diagrama de componentes 
		- Diagrama de instalacao 
		- Diagrama de pacotes
		
	- Diagrama comportamental:
		- diagrama de atividades 
		- Diagrama de casos de uso 
		- Diagrama de maquina de estados 
		- Diagrama de interacoes 
			- Diagrama de sequencia 
			- Diagrama de comunicacao 
			- Diagrama de visao geral da interacao 
			- Diagrama de tempo
			
- Diagrama de classe 
	- mais utilizado na UML 
	- funciona como uma base para a maioria dos outros diagramas 
	- especifica os atributos e metodos associados a cada classe e os relacionamentos e interacoes entre elas 
	
- Diagrama de Pacotes 
	- Representa os subsistemas ou submodulos incluidosem um sistema 
	- util para ilustrar a arquitetura de uma linguagem  
	
- Diagrama de caso de uso 
	- muito utilizado 
	- Levantamento e analise de requisitos do sistema;
	- identificar os atores (sejam usuarios, outros sistemas ou hardware especializado) que interagiram de alguma forma com o software, bem como os servicos ou funcionalidades oferecidas pelo sistema aos atores, denominados casos de uso neste contexto.
	
- Diagrama de atividade 
	- cada diagrama de caso de uso vai virar um diagrama de atividade 
	- descrever os passos necessarios para a conclusao de uma determinada atividade;
	- fluxo de controle durante a execucao da atividade.
	
- Diagrama de maquina de estado 
	- ilustra o comportamento de um elemento através de um conjunto finito de transições de estado, representando essencialmente uma máquina de estados. 
	- Além de descrever o comportamento de uma parte do sistema, quando é denominado máquina de estado comportamental, ele também pode expressar o protocolo de uso de uma parte do sistema ao identificar uma máquina de estado de protocolo.
	- o diagrama de máquina de estados pode ser baseado em um caso de uso, mas também é capaz de rastrear os estados de outros elementos, como uma instância de uma classe.

- Diagrama de sequencia 
	- uma representação comportamental que se concentra na ordem temporal das mensagens trocadas entre os objetos envolvidos em um determinado processo
	- Este diagrama costuma identificar o evento que desencadeia o processo modelado, assim como o ator responsável por esse evento. Ele delineia como o processo deve se desdobrar e ser concluído, através da invocação de métodos por meio de mensagens enviadas entre os objetos.
	
# U4A2 - Diagrama de caso de uso 
- Diagrama de casos de uso 
	- Ferramenta fundamental na engenharia de requisitos e na modelagem de sistema de software 
	- Utilizado em diferentes fases do ciclo de vida do desenvolvimento de software 
	- Proporciona uma visao geral do comportamento do sisteema a ser desenvolvido 
	
- Atores 
	- Os atores representam os papéis desempenhados pelos vários usuários que podem utilizar os serviços e funções do sistema de alguma forma. 
	- Em alguns casos, um ator pode representar hardware especializado ou até mesmo outro software que interaja com o sistema, como em um sistema integrado. 
	- Portanto, um ator pode ser qualquer entidade externa que interaja com o software.
	
- Caso de uso 
	- Os casos de uso servem para capturar os requisitos do sistema, ou seja, englobam os serviços, tarefas ou funcionalidades identificadas como essenciais para o software e que podem ser utilizados pelos atores que interagem com o sistema. 
	- Eles são empregados para expressar e documentar os comportamentos desejados das funções do sistema. 
	- Podem ser divididos em casos de uso primários e secundários. 
	- primário refere-se a um processo crucial que se concentra em um dos requisitos funcionais do software, como efetuar um saque ou gerar um extrato em um sistema bancário. Por outro lado, um caso de uso secundário aborda um processo periférico, como a manutenção de um cadastro

- Associacao 
	- As associações representam as interações ou conexões entre os atores dentro do diagrama, entre os atores e os casos de uso, ou entre os próprios casos de uso. Esses relacionamentos entre os casos de uso recebem nomes específicos, como inclusão, extensão e generalização

- Generalizacao 
	- O relacionamento de generalização/especialização é uma forma de associação entre casos de uso em que dois ou mais casos de uso compartilham características semelhantes, mas apresentam pequenas diferenças entre si. Nesse cenário, costuma-se criar um caso de uso genérico que descreve as características comuns a todos os casos de uso envolvidos, e então relacioná-lo aos casos de uso específicos, cuja documentação incluirá apenas as características distintas de cada um.

- Inclusao 
	- As associações de inclusão indicam uma dependência obrigatória, ou seja, quando um caso de uso possui uma associação de inclusão com outro, a execução do primeiro implica automaticamente a execução do segundo 
	
- Extensao 
	- As associações de extensão são empregadas para descrever cenários opcionais dentro de um caso de uso. Os casos de uso estendidos descrevem situações que ocorrerão apenas sob circunstâncias específicas, dependendo se determinada condição for satisfeita ou não.
	
# U4A3 - Diagrama de atividades 
- Diagrama de atividades 
	- Descreve o fluxo de atividades em um sistema 
	- Enfatiza a sequencia e as condicoes para coordenar comportamentos de baixo nivel 
	- Semelhante a Fluxogramas

- Estado inicial e Final 
	- Estado incial: demostra o inicio do diagrama, so pode ter um 
	- Estado final: demonstra a finalizacao do diagrama, pode-se ter multiplos 

- Fluxo de controle 
	- Representado por uma flexa simples, demonstra o fluxo de acoes 

- Nó  de Decisao / Gateway
	- representado por um losango 
	- similar a um IF, demonstra uma condicao que divide o fluxo 
	
- Fork e Join 
	- Fork: divide um fluxo em varios
	- Join: uni multiplos fluxos em um

- Swimlane / Raias 
	- para demarcar particoes, areas, departamentos, etc.
	
# U4A4 - Diagrama de Classes 
- Mais famoso e mais utilizado 

- Conceito da orientacao a objetos 
	- padrao de desenvolvimentoç
	- Como modelar os problemas do mundo real;
	- Criado por Smaltalk em 1980;
	- Incorporado primeiramente para o C++;
	
- Conceito de orientacao a objetos 
	- Abstracao;
	- Classes;
	- Atributos e metodos;
	- Objetos;
	- Heranca;
	- Encapsulamento;
	- Polimorfismo.
	
- Vantagem da orientacao a objetos 
	- Reutilizacao de codigo;
	- Utilizacao de um unico padrao conceitual para a analise, o projeto e a implementacao;
	- O tempo de desenvolvimento do software e mais rapido;
	- Simplificacao.
	
- Diagrama de Classes 
	   <<entity>>
		Pedido 
	-----------------------
	- identificacao_num: int 
	- data: Date 
	- valor_total: double
	------------------------
	+ registrar_pagamento(): void
	+ expredicao() : void 
	
	- (+) : significa publico
	- (-) : significa privado
	- (nome()) : funcao 
	- (nome : type) : atributo
	
- Associacoes
	- Dependência: este é o tipo de relacionamento mais fraco, representando uma relação semântica entre duas classes. Uma alteração na classe independente pode afetar a classe dependente. Por exemplo, na Figura 3, há uma dependência entre as classes "Produto" e "Receita". Embora existam independentemente, uma mudança na classe "Receita" pode impactar a classe "Produto".
    - Associação: este é o tipo mais comum de relacionamento, indicando que a classe A tem algum tipo de relação com a classe B. É um relacionamento genérico.
    - Agregação: este tipo de relacionamento é mais específico, onde a classe filha pode existir independentemente da classe pai. Na Figura 3, por exemplo, há uma agregação entre a classe "Produto" (pai) e a classe "Cobertura" (filha). Isso significa que, se um objeto do tipo "Produto" deixar de existir, o objeto do tipo "Cobertura" continuará a existir.
    - Composição: este é um tipo específico de associação em que, se o objeto da classe pai for destruído, não faz sentido a existência do outro objeto associado à classe filha. Por exemplo, entre as classes "Pedido" e "Item_de_Pedido", temos um relacionamento de composição, onde os "Itens_de_Pedido" são partes integrantes do "Pedido". Se excluirmos o "Pedido", os "Itens_de_Pedido" também devem ser excluídos. Este relacionamento é representado na Figura 3
    - Generalização/especialização: indica que a classe filha herda as características da classe pai, também conhecida como especialização da classe. As classes Revendedor e Varejo são classes filhas da classe Cliente, conforme mostrado na Figura 3.
    - Multiplicidade: indica quantas instâncias dos objetos estão envolvidos na associação, como está mostrado na Figura 3.