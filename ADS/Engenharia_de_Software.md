# Engenharia de software

## U1A1 Software 
- software:
	- instrucoes executaveis (Scripts, programacao)
	- estrutura de dados (Banco de Dados)
	- documentacao
	
- crise de software:
	- projetos que estouram cronograma
	- projetos que estouram o orcamento
	- software de baixa qualidade
	- software de dificio manutencao
	
- processo de software
	- sequencia de passos executados com um objetivo
	- ferramentas -> metodos -> processso -> foco na qualidade
	
	- atividades fundamentais
		- especificacao / levantamento de requisitos
		- projeto e implantacao
		- validacao / testes
		- evolucao / manutencao
		
- modelos
	- modelo cascata
		- comunicacao -> planejamento -> medelagem -> construcao -> entrega
		
	- modelo evolutivo
		> feito de forma ciclica, entrega apos finalizacao
		- comunicacao 
		- planejamento 
		- medelagem
		- contrucao
		- entrega
		
	- modelo incremental
		> durante a estapa de contrucao pode se escolher incrementar outro aspecto do projeto de forma paralela
		- comunicacao
		- planejamento
		- medelagem
		- contrucao 
		- disponibilizacao
		
## U1A2 metodologia agil
	- planejamento incremental e iterativo
	- se adequa as mudancas
	- maior envolvimento do cliente
	
	- motivacoes
		- menos centrada na documentacao,
		- adaptativa
		- aceita mudancas ao longo do desenvolvimento
		
	- SCRUM
		> estrutura agil mais utilizada do mundo
		- gestao e planejamento de software
		- reunioes diarias
		- projetos divididos em ciclo (sprint)
		- entrega incremental
		- envolvimento do cliente
		
		- Equipe de trabalho
			- Scrum Master : facilitador do projeto
			- Dono do produto : responsavel pelo projeto
			- Time Scrum : equipe de desenvolvimento
		- Elementos do Scrum 
			- Sprint : processo de efetiva construcao do software, em ciclos regulares, que variam de duas a quatro semanas
			- Product Backlog : lista que contem todas as funcionalidades desejadas para o produto 
			- Sprint Backlog : Lista de tarefas que a equipe devera executar naquela Sprint
		- Quadro Scrum / CAMBAM
			- TO DO 
			- WORK
			- DONE
			
	- XP (Extreme Programming)
		- rapigo desenvolvimento
		- requisitos se alteram constantemente
		- valores do XP:
			- comunicacao
			- Simplicidade
			- Feedback
			- Coragem
			
		- Ciclo 
			- Planejamento
				- historias de usuario
				- valores 
				- criterios de teste de aceitacao
				- plano de iteracao
			- Projeto 
				- projeto simples
				- cartoes CRC
				- solucoes pontuais
				- prototipos
			- Codificacao
				- programacao m pares
				- teste de unidades
				- integracao continua
			- Testes 
				- teste de unidades
				- integracao continua 
				- teste de aceitacao
			- Versao
				- incremento de software 
				- velocidade de projeto calculada
				
## U1A3 Requisitos 
- Requisitos do usuario 
	- expresso em linguagem normal complementado por diagramas, detalhando os servicos e restricoes

- requisitos do sistemas
	- deescricao mais aprofundada das funcoes, servicos e limitacoes operacionais do sistema
	- o documento de requisito tambem conhecido como especificacao funcional deve descrever de forma precisa oque deve ser feito.

- Classificacao d requisitos 
	- requisitos funcionais
		- oque o sistema deve fornecer, como deve responder a entradas especificas e seu comportamento em certas cituacoes.
		- lista funcionalidade do sistema
			- operacao basica do sistema,
			- clareza na definicao de requisito
			- clara e consistente
			- completude
	
	- requisitos nao-funcionais 
		- restricoes aos servicos ou funcionalidades fornecidas pelo sitemas, como: limitacoes de tempo, restricioes no processo de desenvolvimento e exigencias decorrentes de normas
		- referente a qualidade do sistema
			- confiabilidade, tempo de resposta e eficiencia no uso de recursos
			- frequentimente nao estabelecido pelo usuario
			- acessibilidade
		- metricas:
			- velocidade
			- tamanho
			- facilidade de uso 
			- Confiabilidade
			- robustez
			- portabilidade
			
	- Engenharia de requisitos 
		- engloba identificacao, documentacao e manutencao dos requisitos
		- elicitacao e requisitos 
			- 1. Descoberta de requistos 
			- 2. Classificacao e organizacao de requisitos 
			- 3. priorizacao e negociacao de requisitos 
			- 4. especificacao de requisitos
			
		- Validacao de requisitos 
			- Confirencia de validade: verifica se os requisitos atendem as necessidades reais do cliente.
			- Conferencia de  Consistencia: assegura que nao existam conflitos ou inconsistencias entre os requisitos.
			- Conferencia de completude: confirma que todos os requisitos abrangendo funcoes e restricoes, estejao incluidos no documento.
			- Conferencia de realismo: avalia se os requisitos sao viaveis dentro do orcamento e cronograma especificado
			- Verificabilidade: elabora testes especificos que comprovem que o sistema finalizado atende a demanda do cliente.
			
## U1A4 controle de Versao 
- Planejamento de Gerenciamento de Configuracao
	- Definir o que sera gerenciado e o esquema que sera usado para identificar as entidades;
	- estabelecer o responsavel;
	- estabelecer politicas de gerenciamento de configuracao;
	- especificar de ferramentas;
	- descrever a estrutura do banco de dados.
	
- Gerenciamento de Configuracao de Software (GCS)
	- repositorio: local de armazenamento das versoes
	- baseline: versoes especificas que servem como padroes para comparacao e avaliacao de progreco
	- branch: ramificacoes de um repositorio que permitem desenvolvimento paralelo sem ameacar o projeto principal
	
- items de Configuracao
	- elemento unitario ou grupo de elementos para efeito de controle deversao
		- documentacoes
		- graphs
		- etc.
	- manter rastreabilidade
	- docs que podem ser uteis devem ser controlados pelo gerenciamento de Configuracao
	- esquemas de nomes hierarquizados
	
- gerenciamento de versoes e releases
	- preocupa-se com identificacao e a rastreabilidade das versoes
	- uma versao e uma instancia de um sistema que difere de alguma maneira de outras instancias
	- versoes com pequenas variacoes sao algumas vezes chamadas variantes
	
## U2A1 Qualidade de Software
> Satisfacao do usuario = produto adquado + maxima qualidade + entrega dentro do orcamento e prazo

- niveis de qualidade 
	- organizacional
		- estabelecimento de padroes de trabalho para o desenvolvimento do software
	- projeto
		- desenvolvimento baseado em padroes estabelecidos por gestores de projeto
	- planejamento
		- elaboracao de um plano de qualidade, com designacoes para verificar os requisitos acordados.
	
- Erros
	- falha de software: compoertamento inesperado do sistema
	- erro: execucao incorrentas
	- defeito: falha ou imperfeicao do codigo
	- bug: erros e falhas inesperados, que geralmente sao de maior complexidade
	
- Garantia da qualidade (GQA/SQA)
	- possuir ferramentas e/ou metodos que permital a analises dos desenvolvimentos e dos testes;
	- efetuar revisoes tecnicas nos componentes e na funcionalidade;
	- controlar a documentacao por meio de versionamento;
	- atribuir metodos para se garantir padroes de desenvolvimento e das boas praticas;
	- mecanismos de afericao / praticas para medir
	
	- atividades
		- definir processo
		- controle de alteracoes
		- revisoes e testes
		- metodos e ferramentas
		- auditorias e conformidades
		- medicao e geracao de relatorios
		
	- metricas de Qualidade
		- processo de software -> produto de software -> medicoes de metrica de previsao
		- medicoes de metrica de controle ->
		- decisoes de gerenciamento ->
		
## U2A2 Qualidade de Produto
- Elementos da qualidade do produto
	- Corretude;
	- Eficiencia;
	- Usabilidade;
	- Portabilidade;
	- Interoperabilidade.
	
- Metricas do produto
	- Metricas dinamicas
		- coletadas por medicoes realiazas em tempo de execucao
	- metricas estatica
		- coletadas por meio feitas em representacoes estaticas, como codigo-fonte e docomentacao
		- Metricas:
			- Fan-in, Fan-out, i.e chamadas de funcoes
			- Comprimento do codigo;
			- complexidade ciclomatica, i.e compriencibilidade do codigo;
			- comprimento de identificadores;
			- profundidade de aninhamento conficional
			- indice Fog, i.e media de palavras e sentencas em um documento.

- processo de medicao de produto 
	- escolher medicao a ser efetuadas ->
	- selecionar componentes a serem avaliados ->
	- medir characteristicas de componentes  ->
	- identificar medicoes anomalas ->
	- analisar componentes anomalos
	
- caracteristicas do ISO 9126
	> foco na avaliacao de qualidade
	- portabilidade, 
	- funcionalidade, 
	- confiabilidade, 
	- usabilidade, 
	- eficiencia, 
	- manutenibilidade
	
- caracteristicas do ISO 9000
	> Foco na gestao de qualidade
	- descrever os fundamentos e principios da gestao de qualidade,
	- compreender os processos de implementacaoda gestao de qualidade,
	- avaliar a comformidade do software involvido
	- Foco no cliente
	- lideranca
	- pessoas
	- processos
	- inter-relacionamento
	- melhoria
	- decisao
	- beneficios
	
- Characteristicas do ISO 9001
	> voltado para produto
	- fazer controle documental
	- efetuar o controle de registro da qualidade
	- normatizar a auditoria interna
	- fazer o controle de produtos que nao atendam as conformidades
	- prover acoes corretivas
	- prover acoes preventivas
	
## U2A3 Auditoria de sistema 
- CMMI
	- Capability Maturity Model Integration
	- modelo de referencia que aborda a melhoria de processos 
	- dividido em 5 niveis de maturidade
		- nivel 1 - inicial ->
		- nivel 2 - gerenciado ->
		- nivel 3 - definido ->
		- nivel 4 - gerenciado quantitativamente ->
		- nivel 5 - otimizando
	
	- tres modelos
		- CMMI for development (CMMI-DEV)
		- CMMI for Acquisition (CMMI-ACQ)
		- CMMI for Services (CMMI-SVC)
		
	- contem 22 areas de processos
	- divididas em 4 grupos:
		- gerenciamento de processos
		- gerenciamentos de projetos 
		- Engenharia
		- apoio
		
- MPS.BR 
	- Criado em 2003 pela softex
	- possui 7 niveis de maturidade 
		- nivel G - parcialmente gerenciado 
		- nivel F - gerenciados 
		- nivel E - parcialmente definido 
		- nivel D - definido 
		- nivel C - totalmente definido 
		- nivel B - gerenciado quantitativamente
		- nivel A - Em otimizacao
	
	- compativel com CMMI 
	- tres modelos de referencias:
		- MPS-SW
		- MPS-SV
		- MPS-RH
		
	- conjunto de processos
		- processos de projeto 
			- gerencia de projetos;
			- engenharia de requisitos;
			- projeto e contrucao de produto;
			- integracao de Produto;
			- verificacao e validacao
		- processos organizacionais
			- gerencia de recursos humanos
			- gerencia de configuracao;
			- gerencia organizacional;
			- gerencia de processos;
			- medicao;
			- aquisicao;
			- gerencia de decisoes.
			
## U2A4 Qualidade de Processo
- Auditorias
	- analisa parcialmente ou globalmente os processos, resultados e sugeri acoes corretivas ou melhorias
	- Areas aplicaveis:
		- processos;
		- desenvolvimento;
		- testes;
		- seguranca e protecao dos dados;
		- entrutura de desenvolvimento.
		
- Auditor 
	- Inspecao: efetua inpecoes dos processos dos desenvolvimento
	- Controle: efetua a analise de controle dos processos
	- Risco: verifica de forma abrangente os riscos 
	
- ciclo de vida da auditoria 
	- planejamento do cronograma ->
	- planejamento da auditoria ->
	- conducao ->
	- reporte
	
- Abordagens de auditoria 
	- abordagem ao redor do computador
		- baseado em confrontar documentos fontes com os resultados esperados;
		- utiliza-se rotinas manuais;
		- sua aplicacao envolve custos baixos e diretos;
		- nao se exige conhecimento extenso de TI.
	
	- abordagem atraves do computador 
		- capacita o auditor a verifica com maior frequencia as areas que necessitam de verificacao constante;
		- faz aprovacao dos registros (logs) armazenadas;
		- esta abordagem nao deixa evidencias documentais atraves dos controles dos programas;
		- se for realizada incorretamente pode levar a grande perdas.
		
	- abordagem com o computador
		- mais completa e mais utilizada;
		- utiliza as capacidades logicas e aritmeticas do computador;
		- possibilita a maior perfeicao possivel, fazendo uma compilacao dos processo manuais e automatizados
		
- Auditorias em SI 
	- auditoria em controles organizacionais e operacionais;
	- auditoria de controle de hardware;
	- procedimentos de auditoria de sistemas aplicativos;
	- auditoria de redes de computadores;
	- auditoria de plano de contigencia e de recuperacao de desastres.
	

## U3A1 - Conceitos de testes de software 
- verificacao e validacao (V&V)
	- processo de verificacao e analise;
	- visa estabelecer a confianca que o sistema de sofware esta adequado ao seu proposito;
	- ocorre em cada estagio do processo do software:
		- revisoes de requisitos;
		- revisoes no projeto;
		- inspecoes no codigo;
		- testes do produto.
	
	- verificacao:
		> "estamos desenvolvendo o produto corretamente?"
		- verificar se o software esta de acordo com suas especificacao;
		- verificar se o software atende os requisito 
		
	- validacao:
		> "estamos produzindo o produto correto?"
		- processo;
		- assegurar se o produto atende as expectativas do cliente;
		
- testes de software 
	- consiste em uma sequencia de acoes executadas com o objetivo de encontrar problemas nos softwares;
	- busca encontrar defeitos e nao garantir que o software esteja insento de problemas.
	
	- processo de testes
		- planejamento -> projeto de casos de teste -> execucao -> analise dos resultados
		
	- casos de testes:
		- entrada no programa e a saida correspondente
		
	- Plano de teste:
		- Projetar casos de teste -> casos de teste ->
		- Preparar dados de teste -> dados de teste ->
		- Executar programa com dados de teste -> resultados de teste ->
		- Comparar resultados para os casos de teste ->
		- relatorio de testes
	
	- resultado de casos de teste 
		- passou: todos os passos realizado com sucesso
		- falhou: nem todos os passos foram executados com sucesso
		- bloqueado: o teste nao pode ser executado, pois o seu ambiente nao pode ser configurado.
		
## U3A2 - Estrategias de testes
- Quando Testar
	- Fase do desenvolvimento do software 
		- niveis de teste:
			- teste de unidade;
			- teste de integracao;
			- teste de sistema;
			- teste de aceitacao;
			- teste de regressao;
			
- O que Testar 
	- Tipo de Teste:
		- Teste de funcionalidade;
		- teste de interface;
		- teste de desempenho;
		- teste de carga (estresse)
		- teste de usabilidade;
		- teste de volume;
		- teste de seguranca.
		
- Como testar:
	- teste funcional:
		- criterios 
			- particionamento e equivalencia
			- analise de valores-limites
			- baseado em caso de uso 
		- a.k.a teste de caixa preta;
		- codigo fonte ignorado;
		- preocupacao de como funciona o software 
		- baseada nos requisitos basicos do software
		- Principal:
			- identificacao das funcoes, atraves da analise de requisitos
			- criacao dos casos de testes
		- utilizado para:
			- funcoes incorretas e omitidas;
			- erros de comportamento;
			- erros de desempenho;
			- erros na interface;
			- erros de inicializacao e termino.
			
	- teste estrutural
		- criterios
			- teste de caminhos
			- teste de comandos;
			- teste ramos;
			- teste de condicoes;
			- teste de cond. multiplas
		- a.k.a teste de caixa branca ou caixa de vidro;
		- testes sao derivados do conhencimento da estrutura e da implementacao do software;
		- conhencendo a estrutura do software, auxilia na identificacao de particoes e casos de testes adicionais;
		- grafos

- escala de testes:	
	- teste de unidade -> codigo ->
	- teste de integracao -> projeto ->
	- teste de validacao -> requisitos -> 
	- teste de sistema -> engenharia de sistemas
	
## U3A3 - Tipos de Testes 
- Teste do caminho basico 
	- tecnica de teste de caixa-branca;
	- medida da complexidade logica de um projeto precedural
	- os casos de teste desenvolvidos para exercitar esse conjunto-base garantem que todas as instrucoes de um programa sejam executadas pelo menos uma vez durante o teste;
	- grafo de fluxo
	
- Teste de ciclos 
	- ciclos simples: um ciclo inicia quando outro termina
		1. pula o ciclo inteiramente;
		2. somente uma passagem pelo ciclo;
		3. duas passagens pelo ciclo;
		4. m passagens atraves do ciclo onde m < n;
		5. n - 1, n + 1 passagens atraves do ciclo.
		
	- ciclos aninhado: ciclos existem dentro de outro ciclo
		1. comece pelo ciclo mais interno e defina todos os outros ciclos para seus valores minimos;
		2. execute os testes de ciclo simples para o ciclo mais interno;
		3. prossiga para o proximo ciclo externo, mantendo todos os outros ciclos externos em seus valores minimos e os ciclos aninhados com valores "tipicos";
		4. continue esse processso ate que todos os ciclos tenham sido testados.
		
- Teste de estrutura de controle 
	- foca na avalilacao da logica de controle do programa, verificando as condicoes, loops e ramificacoes para garantir seu funcionamento adequado.
- Teste baseados em modelo (TBM)
	- metodo TT (teste de transicao);
		- se concentra na cobertura de transicoes entre estados em um modelo de maquina de estados finitos (MEF)
	- metodo UIO (unique Input/Output);
		- testes baseados em sequencias de entrada e saidas unicas.
	- metodo W;
		- teste baseado em MEF que visa maximinizar a cobertura de estado no modelo.
	- metodo DS (dominio de sequencia).
		- teste baseado na identificacao e na utilizacao de sequencias de teste que abrangem diferentes dominios de entrada.
		
## U3A4 - Desenvolvimento orientado a testes (TDD)
- TDD: test-Driven Development
- tecnica de programacao que incorpora o teste ao processo de producao de codigo da segunte forma:
	1. escreva o teste;
	2. veja o teste falhar;
	3. veja o teste passar;
	4. refatore o codigo;
	5. implemente o codigo.

- Gerenciamento de testes 
	- como escrever testes quando o sistema faz acesso a um banco de dados?
	- o que o desenvolvedor deve fazer quando nao tiver ideia de como testar uma classe?
	- como saber se foi testado todo o que poderia dar errado?
	
- Automacao de testes 
	- a fase de teste se encontra sendo trabalhosa, por isso, sao necessarias ferramentas de automacao;
	- workbench de teste: conjunto integrado de ferramentas para apoiar o processo de software;
	
	- ferramentas:
		- gerenciador de testes;
		- gerador de dados de testes;
		- oraculo: previzao do resultado dos testes;
		- comparador de arquivos;
		- gerador de relatorios;
		- analisador de ferramentas;
		- simulador: maquina na qual o teste sera realizado.
		
## U4A1 Manutencao e evolucao de software 
- Software Legado
	- programas antigos que precisam ser modificado para satisfazer mudancas nos requisitos de negocios e de plataforma de computacao
	- sistemas legados podem ter uma ma qualidade:
		- projetos nao-extensiveis;
		- codigo complicado;
		- pouca ou documentacao inexistente;
		- historico de modificacao mal gerido.
		
- gestao de modificacao 
	- modificacoes sao inevitaveis;
	- gestao de modificacao:
		- identificar modificacoes;
		- controlar modificacoes;
		- garantir que as modificacoes sejam implementadas corretamente;
		- relatar/documentar as modificacaoes.
		
- manutencao de modificacao 
	- 18% sao adaptacao de software;
	- 17% sao reparos de defeitos;
	- 65% sao adicoes ou modificacoes de funcionalidades
	
- manutencao de software 
	- manutencao corretiva;
	- manutencao adaptativa;
	- manutencao perfectiva;
	- manutencao preventiva (reengenharia);
	
- reengenharia 
	- analise de documentacao ->
	- reconstrucao de documentacao ->
	- engenharia reversa ->
	- reestruturacao do codigo ->
	- reestruturacao dos dados 
	
- evolucao de software
	- processo de identificacao de mudancas ->
	- proposta de mudanca ->
	- processo de evolucao de software ->
	- novo sistema