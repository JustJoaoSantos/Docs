# U1A1 - Fundamentos da UML 
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
	
# U1A2 - Tecnicas de Modelagem da UML 
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

# U1A3 - Processo de Desenvolvimento de Software com UML 
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