#include <stdio.h>

int main() {
    // Declaracao de Variaveis
    int numeros[5];
    int soma;

    for (int i = 0; i < 5; i++) {
        printf("Digite o valor de posicao %d: ", i);
        scanf("%d", &numeros[i]);
    }

    for (int i = 0; i < 5; i++) {
        printf("%d \n", numeros[i]);
        soma += numeros[i];
    }

    printf("Soma total de todos os valores: %d", soma);

    return 0;
}