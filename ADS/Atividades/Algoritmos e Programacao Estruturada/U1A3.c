#include <stdio.h>

#define IMPOSTO 10
#define DESCONTO 5

void main() {
	//Declaracao de Variaveis
	float preco;
	
	printf("Digite o preco do produto: \n> ");
	scanf("%f", &preco);
	
	printf("Uma taxa de %d sera aplicada\n", IMPOSTO);
	printf("Um desconto de %d sera aplicado\n", DESCONTO);
	
	float preco_corrigido = preco + (IMPOSTO * (preco / 100));
	float preco_descontado = preco_corrigido - (DESCONTO * (preco_corrigido / 100));
	
	printf("Preco corrigido: %.2f\n", preco_corrigido);
	printf("preco Corrigido com desconto: %.2f", preco_descontado);
}
