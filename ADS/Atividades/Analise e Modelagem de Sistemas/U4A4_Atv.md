# Diagrama de Classes : Sistema Bancario

- O banco possui um conjunto de filiais em uma relacao de composicao;
- A classe banco gerencia as filiais com funcoes de adicionar, remover, obter dados de uma filial especifica ou obter dados de todas as filiais;
- A classe filial possui um codigo e uma cidade. em uma filial e possivel adicionar uma conta corrente, remover uma conta corrente ou obter informacoes dessa conta.
- Uma conta possui u numero e um saldo como seus atributos, e possivel realizar transacoes de debito e credito alem de consultar o saldo.
- Dois tipos de conta sao definido: a conta poupanca e a conta corrente;
- Um cliente pode ter 0 ou 1 conta de cada tipo;
- O cliente pode solicitar emprestimo, sendo que este estara vinculado a uma filial.