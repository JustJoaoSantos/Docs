#include <stdio.h>

void main() {
float valor_bruto = 1000;
int qtd_pessoa = 10;
float desconto = 10;

float valor_liquido = valor_bruto - (desconto * (valor_bruto / 100));

printf("valor bruto: R$%.2f \n", valor_bruto);
printf("Valor liquido: R$%.2f \n", valor_liquido);
printf("Valor por pessoa: R$%.2f", valor_liquido / qtd_pessoa);
}