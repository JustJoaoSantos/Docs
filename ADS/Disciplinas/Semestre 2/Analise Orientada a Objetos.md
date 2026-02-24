# Linguagem de Modelagem Unificada UML
## U1A1 - Fundamentos da UML 
- UML: Linguagem padronizada para a modelagem de software
- Caracteristicas da UML:
	- Combina os conceitos comuns de linguagens OO (Orientadas a Objeto)
	- Compativel com o desenvolvimneto de software, desde os requisitoss ate as etapas finais do desenvolvimneto
	- Compativel com diversos escopos
	
- Objetivos da UML:
	- Modelar diferentes linguagens e situacoes
	- Padrao para o desenvolvimento de software 
	- Simplicidade
	
- Objetivos dos Modelos da UML 
	- Capturar e definir com precisao os requisitos do software 
	- Auxiliar o inicio do projeto do sistema
	- Solucao que contenha as decisoes de projeto 
	- Explorar diferentes solucoes 
	- Permitir o facil entendimento de projetos complexos
	
- Nivel de Abstracao
	- Alto:
		- Tem o objetivo de ser claro e simples, apresentar os conceitos ao cliente para tomada de decisao 
	- Medio:
		- Deve Guiar o desenvolvimento apresentado, sem detalhar demais, as classes, os objetos e as interacoes
	- Baixo:
		- Demonstrara como deve ser desenvolvido o sistema propriamente dito. Necessita de diagramas e modelos com a especificacao completa de cada modulo, interacao e outras informacoes que possam ser necessarias
		
- Fluxo de Desenvolvimento 
	- Pode ser utilizada em qualquer fluxo de desenvolvimento 
	- Apresentacao visual da semantica do sistema 
	- Contexto
	
## U1A2 - Tecnicas de Modelagem da UML 
- Diagramas da UML 
	- Diagramas Estruturais
		- Classes (Mais Utilizado)
			- refere-se às classes criadas em softwares desenvolvidos em linguagens orientadas a objetos
		- Objetos 
			- mostra os objetos e seus relacionamentos durante a execução do software
		- Pacotes
			-  ilustra os subsistemas dentro do software desenvolvido e as principais áreas de cada sistema. No diagrama de pacotes, é possível distinguir e identificar interfaces de usuário, bancos de dados, módulos de segurança e pacotes administrativos
		- Estrutura Composta 
			- semelhante ao de objetos, mas foca nas relações entre objetos e componentes do software durante a execução
		- Componente 
			- modela a relação entre os componentes usados no software. Por exemplo, ao incluir a biblioteca "math.h" em uma função matemática na linguagem C, ela é considerada um componente
		- Instalacao (Implantacao)
			- descreve a infraestrutura de hardware e software necessária para a execução adequada do software em desenvolvimento
		- Perfil
			- Um perfil adapta uma classe para um domínio ou plataforma específica, como a diferenciação entre um servidor e um dispositivo móvel. Esse diagrama é usado para descrever os diferentes perfis necessários no desenvolvimento de software
		
	- Diagramas Comportamentais
		- Casos de Uso (Mais Utilizado)
			- oferece uma visão geral das funcionalidades do sistema do ponto de vista dos usuários. Ele facilita a identificação e correção de omissões ou erros nas descrições das funcionalidades
		- Atividade 
			- detalhar os fluxos de processos dentro do sistema. Ele não apenas apresenta os fluxos normais, mas também os alternativos e as exceções
		- Maquina de estados
		- Diagramas de Integracao:
			- Sequencia
			- Comunicacao 
			- Tempo
			- Visao geral de interacao
				- mostra as relações em alto nível que ocorrerão no sistema, destacando como os diferentes diagramas UML interagem e as dependências entre eles

## U1A3 - Processo de Desenvolvimento de Software com UML 
- Processo Unificado (PU ou UP)
	- Processo -> quem, o que, como e quando 
	- UP (Unified Process)
	- RUP (Rational Unified Process)
	- Interativo e incremental
	- Dirigido por uma lista de casos de uso 
	- Focado na arquitetura do sistema 
	- Orientado a riscos
	
- Organizacao do processo Unificado | Anexo: organizacao_do_proceco_unificado.png
	- fases: Concepcao, Elaboracao, Construcao, Transicao, Producao
	- Comunicacao -> (Concepcao) -> Planejamento -> (Elaboracao) -> Modelagem -> Construcao(Construcao) -> (Transicao) -> Entrega -> Incremento de software(Producao)
	
- Fluxo de Trabalho
	- Etapas 1 e 2 (Concepcao e Elaboracao)
		- Casos de uso 
		- Sequencia 
		- Colaboracao
		- Atividades
		- Maquina de estado 
		
	- Etapas 3 (Construcao)
		- Classes 
		- Sequencia 
		- Colaboracao 
		- Atividades 
		- Maquinas de estado 
		- Instalacao 
		
	- Etapas 4 (Transicao)
		- Transicao 
		- Sequencia 
		- Colaboracao 
		- Componentes 
		
- Regras de consistencia de diagramas UML 
	1. O número de objetos no diagrama de sequência deve corresponder ao número de classes no diagrama de classes.
	2. Atualizações no diagrama de classes devem ser refletidas corretamente no diagrama de sequência.
	3. Se uma relação de dependência é expressa no diagrama de classes, deve haver pelo menos uma passagem de mensagem entre os objetos dessas classes no diagrama de sequência. Se não houver, a relação de dependência no diagrama de classes deve ser removida.
	4. O nome dos métodos deve ser consistente entre os diagramas de classes e sequência.
	5. Diagramas de classes e sequência devem ser sincronizados. Qualquer alteração no diagrama de classes deve ser imediatamente atualizada no diagrama de sequência.
	6. Objetos nos diagramas de comunicação e sequência devem seguir um padrão de nomenclatura.
	7. Cada situação no diagrama de casos de uso deve ter uma operação correspondente no diagrama de classes.
	8. Cada caso de uso deve ter um substantivo e um verbo associados.
	9. Cada caso de uso deve ocorrer pelo menos uma vez no diagrama de sequência.
	10. Todos os atores de um caso de uso no diagrama de sequência devem ser representados.
	11. Cada caso de uso deve ter pelo menos um diagrama de sequência.
	12. Cada diagrama de sequência deve ter um diagrama de tempo correspondente.
	13. Os participantes no diagrama de tempo devem estar representados no diagrama de sequência correspondente.
	
## U1A4 - Conceitos fundamentais do paradigma orientada a objetos 
- Paradigmas de programacao
	- Imperativo e.g C 
	- Declarativo:
		- Funcional e.g SQL
		- Logico e.g Lisk
	- Orientado a Objetos (OO) e.g C++, Java
	- Baseados em Eventos
	
- Classificacao e Abstracao 
	- Abstracao: Selecao de alguns aspectos de dominio do problema a modelar, desconsiderando os irrelevantes para o nivel de abstracao em questao
	- e.g Carro: possui 4 rodas, acelera, freia.
	
- Paradigma Orientado a Objetos 
	- Java, C++, C#, PHP
	- Relacionamento entre classes e objetos e o Relacionamento entre eles:
		- Heranca
		- Polimorfismo
		- Agregacao
		- Composicao
		
	- Classes: Define comportamento de seus objtos - atravez de metodos - e os estados possiveis destes objetos - atraves de atributos.
	- Objeto: Instancia de uma classe 
	- Heranca: As classes compartilham seus atributos, metodos e outros membros da classe entre si.
	- Polimorfismo: Metodos que tem a mesma assinatura, mas comportamentos distintos
	- Encapsulamento: proibicao do acesso direto ao objeto 
	
# Modelagem Essencial de Analise com UML 
## U2A1 - Diagrama de Casos de Uso 
- Casos de Uso: descrevem as diversas maneiras pelas quais os usuários podem interagir com o sistema, ou seja, como cada usuário pode utilizá-lo. 
- Ator: representam os usuários do sistema, indicando quem irá interagir com ele
- Relacionamentos: mostram como cada caso de uso se conecta a outros casos de uso ou a atores.
	- Linha: associacao
	- Generalizacao: herda as caracteristicas do caso de uso pai
		- (Caso Filho) -> (Caso Pai) 
	- Seta Pontilhada: Include (Ira ser executado em seguida), Extend (Pode ou nao Ocorrer)
		- (caso que esta sendo executado) -> (caso que sera executado em seguida)
		
- Multiplicidade de associacao
	- Jogador (Ator) [2..4] ------- [0..1] Jogar Jogo (Caso de Uso)
		- [2..4] : minimo 2 maximo 4 jogadores
		- [0..1] : minino 0 maximo 1 Jogo
		
- Criterios basicos na criacao do Caso de Uso 
	1. O diagrama deve ser o mais simples possível.
	2. O diagrama também deve ser o mais completo possível.
	3. Um caso de uso deve ter todas as suas interações representadas.
	4. Se o diagrama for muito extenso, é possível representar apenas as partes essenciais.
	5. Um diagrama de casos de uso deve modelar ao menos um módulo do sistema de forma completa. 
	
## U2A2 - Diagrama de Classes 
- Atributos 
- Metodos 
- Classes 
- Objeto 
- Public (+)
- Private (-)
- Protected (#)
- Package (~)

- e.g classe 
	Cartao de Credito
	_____________________
	-Numero
	-tipo 
	-Data de expir.
	-Codigo de seguranca
	_____________________
	+Autorizar()
	
- e.g classe abstrata, obs. titulo escrito em italico
	Ex de Classe Abstrata
	_____________________
	-Atributo 1
	-Atributo 2
	_____________________
	+getAtributo1()
	+setAtributo2(Atributo2) : void
	
- e.g interface 
	<<Interface>>
	Ex. de Interface
	_____________________
	-Atributo da Interface 
	_____________________
	+getAtributo da Interface()
	+setAtributo da Interface(Atributo da Interface) : void
	
- relacionamentos 
	- setas pontilhadas(--->) : implementacao
	- setas (->) : heranca 
	
- multiplicidade 
	- n..m : significa n para m instancias entre classes 
	- n..* : indica n para muitos
	- 1 : exatamente uma instancia 
	- 1..* - uma ou mais instancias que podem estar relacionadas
	
- Composicao 
	- janela <>----- botao
	
- Agregacao 
	- Carro <>------ Estepe
	
## U2A3 - Diagrama de Atividades 
- Inicial: representado por uma esfera preta
- Final: representado por uma esfera com ponto preto no meio
- Terminal: representado por 
- Condicional: representado por um losango
- Acao: representado por um retangulo com bordas aredondadas
- Transicao: representado por uma seta
- join/fork : representado por um retangulo preto 
- raias/swimlanes: para separar fluxos das atividades

## U2A4 - Diagrama de Maquina de Estados 
- Estado Inicial: representado por uma esfera preta
- Estado Final: representado por uma esfera com ponto preto no meio
- Escolha: representado por um losango
- Estado: representado por um retangulo com bordas aredondadas
- Transicao: representado por uma seta
- join/fork : representado por um retangulo preto 

- Clausulas
	- Do: representa uma atividade realizada durante o tempo em que o objeto se encontra no estado 
	- Entry: Representa as acoes realizadas no momento em que o objeto assume o novo estado 
	- Exit: Representa as acoes executadas quando o objeto esta mudando de estado 

- Elementos importantes
	- Identificar os estados relevantes para os objetos da classe 
	- Identificar os eventos e as transicoes de estado que ele ocasiona 
	- Verificar se ha fatores que influenciam nos eventos que ocasionam a transicao entre os estados 
	- Definir o estado inicial e os eventuais estados finais 
	
- Conceitos basicos importantes 
	- Eventos: são acontecimentos que alteram o estado dos objetos, resultantes de ações internas ou externas. 
	- Estados: são abstrações que representam condições dos objetos em um dado instante de execução com duração limitada, mostrando a resposta de um objeto a um evento
	- Transições de estado: são as mudanças de estado de um objeto em resposta a um evento. 
	
## U3A1 - Diagrama de Sequencia
- lifeline: representa a existência de um elemento (objeto ou ator) participante da realização do caso de uso em um período de tempo.
- actor: representa os mesmos atores já criados no diagrama de casos de uso
- objeto: representa os objetos que participam da realização do caso de uso;
- foco de controle: representa o período de tempo durante o qual um elemento executa uma ação, diretamente ou não.
- mensagem sincrona: quando o emissor aguarda o retorno para continuar com a interação
- mensagem assincrona: quando o emissor continua enviando mensagens sem aguardar o retorno, com isso o elemento receptor da mensagem assíncrona não precisa atendê-la imediatamente
- mensagem de retorno: objeto envia ao outro em resposta à mensagem recebida após a execução de uma ação
- mensagem reflexiva ou automensagem: mensagem indicativa de que o objeto remetente da mensagem é também o receptor.
- mensagem construtora:  indica o momento em que o objeto passa a existir no sistema, ou seja, o objeto é instanciado ao longo do processo por uma mensagem enviada
- mensagem destrutora: indica a destruição do objeto no decorrer da interação, o qual não se mostra mais necessário no processo
- quadro de interacao: representa uma interação independente, possibilitando isolar um diagrama de sequência com um contexto específico, formando uma fronteira para que possa ser integrado aos demais diagramas de sequência
- nota ou comentario: serve para escrever observações aos elementos que compõe o diagrama de sequência, contendo informações úteis para os desenvolvedores

- Elementos que compoe o diagrama de Sequencia 
	- boundary: denominado de classe de fronteira, representa a interface do sistema;
	- control: denominado de classe de controle, serve de intermediario entre as classes definidas como <<boundary>> e <<entity>>
	- entity: denominado de classe de entidade, mostra que as classes do sistema tambem sao emtidades.
	
- Fragmentos 
	- ref: interacao independente;
	- alt: escolha entre duas ou mais acoes;
	- opt: modela a construcao procedimental do tipo se...entao;
	- loop: representa que uma interacao deve ser realizada zero ou mais vezes.
	
- Passos para construir um diagrama de sequencia
	1. Utilize os cenários descritos na documentação do caso de uso para identificar os objetos envolvidos na execução do caso de uso.
	2. Consulte o diagrama de classes para determinar as classes correspondentes aos objetos identificados anteriormente.
	3. Reexamine os cenários na documentação do caso de uso para reconhecer as mensagens trocadas entre os objetos das classes estabelecidas.
	4. Analise as operações das classes definidas para garantir que elas estejam alinhadas com as mensagens identificadas anteriormente.
	5. Elabore o diagrama de sequência, iniciando com o cabeçalho que inclui o ator principal interagindo com o caso de uso e os objetos das classes determinadas. Se necessário, divida o diagrama em fragmentos de interação ou fragmentos combinados.
	6. Verifique a consistência do diagrama de sequência com o diagrama de casos de uso e refine a descrição dos cenários com base no conhecimento adquirido durante a construção do diagrama de interação, se necessário.
	7. Assegure que o diagrama de sequência esteja consistente com o diagrama de classes. Com base no conhecimento obtido na construção do diagrama de interação, aperfeiçoe as classes de objetos que compõem o diagrama adicionando novos atributos, operações e associações conforme necessário. Geralmente, a ferramenta CASE utilizada para modelar o diagrama atualiza automaticamente o diagrama de classes, incluindo as operações nas classes dos objetos que foram complementadas.	

- Exemplo:
	- segue anexo: Anexos/U3A1_diagrama_sequencia_classe.png
	- segue anexo: Anexos/U3A1_diagrama_sequencia_diagrama.png
	```Descricao 
	Consultar Saldo:
		Inserir os dados;
		Dados devem ser validados;
		Informar a senha;
		Senha deve ser valida;
		Apresentar o Saldo.
	```
	
## U3A2 - Diagrama de Componentes 
- Estereotipos
    - Executable: identifica o componente como um arquivo executável, que pode ser um módulo compilado em Java, por exemplo, operando por meio de uma máquina virtual.
    - Library: refere-se a coleções de funções e sub-rotinas que podem ser usadas por múltiplos componentes executáveis, originadas tanto da linguagem de programação quanto desenvolvidas pelos próprios programadores.
    - Table: aponta para bases de dados físicas que armazenam as informações geradas pelo sistema.
    - Doc: relaciona-se a arquivos de texto usados por outros componentes, como manuais de instrução.
    - File: pode denotar qualquer outro tipo de arquivo que faça parte do sistema, incluindo código-fonte.

- Interface requeridas: representado por um circulo, demonstra a necessidade de um componente para outro.

- Exemplo:
	- segue anexo: Anexos/U3A2_diagrama_componentes.png
	```Descricao 
	Desenvolva o diag. de componentes para um sistema de controle de hotelaria, de acordo com as seguintes definicoes:
		1. Como de praxe, necessario haver um modulo de manutencao para gerenciar os cadastros de funcionarios, categorias, quartos, etc;
		2. necessario tambem implementar um modulo para realizar as reservas de quartos pelos hospedes. da mesma forma e preciso existir um modulo para gerenciar o aluguel dos quartos;
		3. O aluguel de um quarto pode implicar na solicitacao de servicos ou no consumo de itens do frigobar, assim e necessario haver alguma forma de registrar esses pedidos.
	```
	
## U3A3 - Diagrama de Objetos 
- Representacao do objeto:
	- O nome do objeto em letras minúsculas, seguido de dois pontos (:) e o nome da classe a qual pertence, com a primeira letra de cada palavra em maiúscula. Esse é o formato mais detalhado.
    - O nome do objeto é omitido, retendo apenas os dois pontos e o nome da classe.
    - Apenas o nome do objeto, sem os dois pontos.
	
- vinculos: monstram a conexao de dois objetos
- dependencia: monstra a dependecia de dois ou mais objetos 
- instancia: representado pela linha de dependecia com estereotipo <<instantiate>>

- Exemplo:
	- segue anexo: Anexos/U3A3_diagrama_objeto.png 
	
## U3A4 - Diagrama de Pacotes e Diagrama de Comunicacao 
### Diagrama de Pacotes 
- ilustra a organizacao dos elementos de um modelo em pacotes e a interdependecia entre eles 
- Os pacotes servem para agrupar elementos, atribuindo-lhes nomes. Eles podem simbolizar um sistema, um subsistema, uma biblioteca, ou uma fase de um processo de desenvolvimento, entre outras possibilidades. Um pacote pode, inclusive, incluir outros pacotes dentro de si.



### Diagrama de Comunicacao
> parecido com o diagrama de sequencia porem menos detalhado e mais facil de modificar

- lifeline: representa a existência de um elemento (objeto ou ator) participante da realização do caso de uso em um período de tempo.
- actor: representa os mesmos atores já criados no diagrama de casos de uso
- multiobjeto:  representa uma coleção de objetos de uma mesma classe, participando da interação
- Mensagem: representa a solicitação que um elemento envia para o outro com o objetivo de executar uma ação entre os elementos do diagrama, em geral, demonstrando a chamada de operações dos objetos.
- mensagem reflexiva ou automensagem: mensagem indicativa de que o objeto remetente da mensagem é também o receptor.
- Nota ou comentário: é utilizado para descrever observações aos elementos que compõe o diagrama de sequência, contendo informações úteis para os desenvolvedores

- exemplo:
	- segue anexo Anexos/U3A4_diagrama_comunicacao_guia.png 
	- segue anexo Anexos/U3A4_diagrama_comunicacao.png
	```Descricao:
	Utilize um diagrama de comunicacao para ilustrar as interacoes entre os diferentes objetos (Cliente, Interface_Banco, Controlador_Banco e Conta_Comum)
	1. O cliente insere seu cartao na interface do banco;
	2. O cliente informa sua senha na interface do banco;
	3. A interface do banco deve comunicar o numero da conta e a senha ao controlador do banco;
	4. O controlador do banco deve verificar a existencia da conta e validar a senha fornecida;
	5. Apos a validacao, o controlador do banco deve solicitar o saldo da conta e retornar essa informacao para a interface do banco;
	6. A interface do banco deve exibir o saldo da conta para o cliente.
	```
	
## U4A1 - Modelagem Inicial
- Importancia da Modelagem 
	- Crise de software;
	- Restringe o foco a um unico aspecto por vez;
	- Quanto mais complexo o sistema, maior a importancia da modelagem.
	
- Fase de Concepcao 
	- O planejamento do projeto;
	- A definicao da ideia inicial do negocio;
	- A delimitacao do escopo do sistema;
	- O entendimento do contexo do sistema;
	- A definicao dos principais casos de uso do sistema.
	
- Tecnicas de modelagem da UML 
	- Diagramas de casos de uso para modelar os requisitos;
	- Diagrama de Atividades para representar o comportamento de cada requisito funcional do sistema;
	- Diagrama de sequencia para especificar o cenario de cada funcionalidade identificada como requisito funcional.
	
- Diagrama de Atividade para gerar os requisitos 
	- Diagrama de Atividade simples para locacao de veiculos, segue anexo: Anexo/U4A1_Diagrama_Atividade.png
	- Requisitos:
		- RF1|Cadastro de filial: o sistema deve prover um cadastro de filiais da locadora de veiculos. o cadastro sera mantido pelo administrador do sistema.
		- RF2|Cadastro de cliente:
		- RF3|Cadastro de empresa:
		- RF4|Cadastro de grupo de carro:
		- RF5|Cadastro de carro:
		- RF6|Controle de reserva de carro:
		- RF7|Controle de aluguel de carro:
		- RF8|Emissao de contrato de aluguel:
		- RF9|Controle de devolucao de carro:
		- RF10|Emissao de nota fiscal de aluguel:
	- Diagrama de Caso de Uso feito baseado nos requisitos levantados, segue anexo: Anexo/U4A1_Diagrama_Caso_Uso.png
	- Diagrama simples de classe baseado no diagrama de caso de uso, segue anexo: Anexo_U4A1_Diagrama_Classe.png
	
## U4A2 - Modelagem Complementar
- Diagrama de Estrutura Composta
	- Identificar a arquitetura do conjunto de elementos que interagem entre si durante a execucao do sistema;
	- Estrutura interna de um componente;
	- Mostra a interligacao entre as instancias e o tempo de execucao 
	- segue anexo: Anexo/U4A2_diagrama_estruc_composta.png
	
- Diagrama de maquina de estados 
	- segue anexo: Anexo/U4A2_diagrama_maq_estados.png 
	
- Diagrama de atividades 
	- segue anexo: Anexo/U4A2_diagrama_Atividade.png 

- Diagrama de Sequencia 
	- seque anexo: Anexo/U4A2_diagrama_sequencia.png 