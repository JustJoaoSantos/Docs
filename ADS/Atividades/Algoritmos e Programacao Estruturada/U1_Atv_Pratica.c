#include <stdio.h>

int main() {
    int n1, n2, n3;

    printf("Digite um numero inteiro: ");
    scanf("%d", &n1);

    printf("Digite um segundo numero inteiro: ");
    scanf("%d", &n2);

    printf("Digite um terceiro numero inteiro: ");
    scanf("%d", &n3);

    printf("%d + %d + %d = %d \n", n1, n2, n3, n1 + n2 + n3);
    printf("%d - %d - %d = %d \n", n1, n2, n3, n1 - n2 - n3);
    printf("%d * %d * %d = %d \n", n1, n2, n3, n1 * n2 * n3);

    if (n1 != 0 && n2 != 0 && n3 != 0) {
        printf("%d / %d / %d = %d \n", n1, n2, n3, n1 / n2 / n3);
    } else {
        printf("Nao foi possivel fazer divisao por 0\n");
    }

    if (n1 > n2) {
        printf("Numero 1 maior que numero 2 \n");
    } else {
        printf("Numero 1 nao e maior que numero 2 \n");
    }

    if (n2 < n3) {
        printf("Numero 2 menor que numero 3 \n");
    } else {
        printf("Numero 2 nao e menor que numero 3 \n");
    }

    if (n1 > 0 && n2 % 2 == 0) {
        printf("Numero 1 positivo e numero 2 par\n");
    }

    return 0;
}