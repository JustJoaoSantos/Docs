#include <stdio.h>

int main() {
    int num = 0;

    // loop principal
    while (1) {
        int usr_num = 0;

        printf("Digite uma numero (ou 0 para encerrar e calcular a soma)");
        scanf("%d", &usr_num);

        if (usr_num == 0) {
            // encerra o loop com entrada 0
            break;
        
        } else {
            // acumula input do usuario
            num = num + usr_num;
            printf("Soma realizada\n");
        }
    }

    printf("Soma de todos os numeros digitados: %d", num);
}