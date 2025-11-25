#include <stdio.h>

void main() {
	int a, b;
	printf("digite o primeiro valor: \n>");
	scanf("%d" , &a);
	
	printf("digite o segundo valor: \n> ");
	scanf("%d", &b);
	
	printf("a media de %d e %d = %f", a, b, (a + b) / 2);
}