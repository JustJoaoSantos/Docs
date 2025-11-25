#include <stdio.h>

//Constantes
#define DESCONTO_PER 9

// Prototype
float calcular_salario_bruto(float*, float*);
float calcular_salario_liquido(float*, float*);
float calcular_desconto(float*);
void inserir_dados(float*, float*);

int main() {
    // Declaracao de Variaveis
    int op;
    float valor_hora;
    float horas_trabalhadas;
    float valor_desconto = 0.0f;
    float salario_bruto = 0.0f;
    float salario_liquido = 0.0f;

    do {
        printf("\nEscolha a Operacao: \n");
        printf("1 - Inserir Dados \n");
        printf("2 - Calcular Salario Bruto \n");
        printf("3 - Calcular Descontos \n");
        printf("4 - Calcular Salario Liquido\n");
        printf("5 - Para mostrar o salario e o desconto\n");
        printf("0 - Para encerrar o Programa\n> ");

        //fflush(stdin);
        scanf("%d", &op);

        if (op < 0 || op > 4) {
            op = 5;
        }

        //Selecao de Operacao
        switch(op) {
            case 0:
                printf("Encerrando programa\n");
                break;

            case 1: //Insersao de dados
                inserir_dados(&horas_trabalhadas, &valor_hora);
                break;

            case 2: 
                salario_bruto = calcular_salario_bruto(&horas_trabalhadas, &valor_hora);
                break;
            
            case 3:
                valor_desconto = calcular_desconto(&salario_bruto);
                break;

            case 4:
                salario_liquido = calcular_salario_liquido(&salario_bruto, &valor_desconto);
                break;

            case 5:
                if (salario_bruto <= 0.0f) {
                    printf("\nValor Invalido, Por favor faca o calculo de salario bruto primeiro!\n");
                
                } else {
                    printf("\nSalario Bruto: R$%.2f \n", salario_bruto);
                }

                if (valor_desconto <= 0.0f) {
                    printf("Valor Invalido, Por favor faca o calculo do desconto primeiro!\n");
                
                } else {
                    printf("Valor do Desconto: R$%.2f \n", valor_desconto);
                }

                if (salario_liquido <= 0.0f) {
                    printf("Valor Invalido, Por favor faca o calculo de salario liquido primeiro!\n");
                
                } else {
                    printf("Salario Liquido: R$%.2f \n", salario_liquido);
                }
                
                break;

            default:
                printf("Operacao invalida tente novamente\n");
                break;
    }
    

    } while (op != 0);

    return 0;
}

// Declaracao das funcoes
void inserir_dados(float* horas_trabalhadas, float* valor_hora) {
    printf("Insira o valor por hora: ");
    scanf("%f", valor_hora);

    printf("Insira as horas trabalhadas neste mes: ");
    scanf("%f", horas_trabalhadas);

    if (*valor_hora < 0 || (*horas_trabalhadas) < 0 || (*horas_trabalhadas) > 720) {
        printf("Dados Invalidos, tente novamente\n");
        *horas_trabalhadas = 0; 
        *valor_hora = 0;
        return;
    
    }

    printf("Dados Resgistrados com sucesso!\n");
}

float calcular_salario_bruto(float* horas_trabalhadas, float* valor_hora) {
    if (*horas_trabalhadas <= 0 || *valor_hora <= 0) {
        printf("Valores muito baixos para serem trabalhados, insira um valor valido primeiro!\n");
        return 0.0f;
    }

    return (*horas_trabalhadas) * (*valor_hora);
    printf("\nCalculo do Salario Bruto realizado com sucesso!");
}

float calcular_desconto(float* salario_bruto) {
    if (*salario_bruto <= 0) {
        printf("Valores muito baixos para serem trabalhados, insira um valor valido primeiro!\n");
        return 0.0f;
    }

    return DESCONTO_PER * ((*salario_bruto) / 100);
    printf("\nCalculo do Desconto realizado com sucesso!");
}

float calcular_salario_liquido(float* salario_bruto, float* valor_desconto) {
    if (*salario_bruto <= 0 || *valor_desconto <= 0) {
        printf("Valores muito baixos para serem trabalhados, insira um valor valido primeiro!\n");
        return 0.0f;
    }

    return (*salario_bruto) - (*valor_desconto);
    printf("\nCalculo do Salario Liquido realizado com sucesso!");
}