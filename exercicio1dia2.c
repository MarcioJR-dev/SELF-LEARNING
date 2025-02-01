#include <stdio.h>
int main() {
int num1,num2,soma,div,multi,sub;

printf("Qual o primeiro número?");
scanf("%d",&num1);

printf("agora o segundo numero");
scanf("%d",&num2);

soma = num1+num2;
div = num1/num2;
multi = num1*num2;
sub = num1-num2;

printf(" a soma é %d, a subtração é %d, a multiplicação é %d e a divisão é %d",soma,sub,multi,div);

return 0;
}