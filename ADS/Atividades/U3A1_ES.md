Para exercitarmos o que foi aprendido, vamos imaginar o seguinte problema: um sistema de inscrição on-line permite que os usuários se inscrevam em eventos, preenchendo um formulário que inclui um campo de data para inserir a data de nascimento. Alguns usuários reportaram problemas ao inserir suas datas de nascimento, no qual o sistema rejeita datas válidas ou aceita datas inválidas. O sistema precisa validar corretamente as datas, considerando anos bissextos, a quantidade correta de dias em cada mês e anos históricos válidos.

Por isso, você deve criar um conjunto de casos de teste focados na validação do campo de data de nascimento no formulário de inscrição do sistema. Seus casos de teste devem explorar diferentes cenários de entrada de data para identificar problemas na lógica de validação do sistema.

Para cada caso de teste, você deve especificar:

    Nome do Caso de Teste: uma descrição breve e descritiva.
    Pré-condições: qualquer configuração ou estado do sistema necessário antes da execução do teste.
    Passos: passos detalhados para executar o teste.
    Dados de Teste: a data específica que será testada.
    Resultado Esperado: o que se espera que aconteça se a validação da data estivesse funcionando corretamente (aceitação da data válida ou rejeição da data inválida).
    Critérios para Falha: descrição específica do que seria considerado uma falha no teste (por exemplo, aceitação de uma data inválida).
	
	=============================================================================
	Gabarito: Casos de Teste para Validação de Data de Nascimento

Caso de Teste 1: Data Válida Não Bissexto

    Nome do Caso de Teste: Validar Data de Nascimento Comum Não Bissexto
     Precondições: O formulário de inscrição está carregado e o campo de data de nascimento está vazio.
    Passos:

    Clique no campo de data de nascimento.
    nsira a data "15/2/1946".
    Envie o formulário.

    Dados de Teste: 15/2/1946.
    Resultado Esperado: o sistema deve aceitar a data como válida e permitir a submissão do formulário.
    Critérios para Falha: o sistema rejeita a data ou impede a submissão do formulário.

Caso de Teste 2: Data Inválida com Dia Inexistente

     Nome do Caso de Teste: validar Data de Nascimento com Dia Inexistente
    Precondições: o formulário de inscrição está carregado e o campo de data de nascimento está vazio.
    Passos:

    Clique no campo de data de nascimento.
    Insira a data "30/2/2022".
    Envie o formulário.

    Dados de Teste: 30/2/2022.
    Resultado Esperado: o sistema deve rejeitar a data como inválida e impedir a submissão do formulário.
    Critérios para Falha: o sistema aceita a data e permite a submissão do formulário.

Caso de Teste 3: Data Inválida com Mês Inexistente

    Nome do Caso de Teste: validar Data de Nascimento com Mês Inexistente
    Precondições: o formulário de inscrição está carregado e o campo de data de nascimento está vazio.
    Passos:

    Clique no campo de data de nascimento.
    Insira a data "15/13/2023".
    Envie o formulário.

    Dados de Teste: 15/13/2023.
    Resultado Esperado: o sistema deve rejeitar a data como inválida e impedir a submissão do formulário.
    Critérios para Falha: o sistema aceita a data e permite a submissão do formulário.

Caso de Teste 4: Data Válida Bissexto

    Nome do Caso de Teste: validar Data de Nascimento em Ano Bissexto
    Precondições: o formulário de inscrição está carregado e o campo de data de nascimento está vazio.
    Passos:

    Clique no campo de data de nascimento.
    Insira a data "29/2/2016".
    Envie o formulário.

    Dados de Teste: 29/2/2016.
    Resultado Esperado: o sistema deve aceitar a data como válida e permitir a submissão do formulário.
    Critérios para Falha: o sistema rejeita a data ou impede a submissão do formulário.

Caso de Teste 5: Data Inválida Não Bissexto

    Nome do Caso de Teste: validar Data de Nascimento Não Bissexto Inexistente
    Precondições: o formulário de inscrição está carregado e o campo de data de nascimento está vazio.
    Passos:

    Clique no campo de data de nascimento.
    Insira a data "29/2/2015".
    Envie o formulário.

    Dados de Teste: 29/2/2015.
    Resultado Esperado: o sistema deve rejeitar a data como inválida e impedir a submissão do formulário.
    Critérios para Falha: o sistema aceita a data e permite a submissão do formulário.