#include <stdio.h>

struct Aluno{
    
    char nome [50];
    int idade;
    int alturacm;
    
};

int main()
{
    struct Aluno estudante;
    printf("Qual seu nome?");
    scanf("%s",estudante.nome);
    printf("Qual sua idade?");
    scanf("%d",&estudante.idade);
    printf("Qual ua altura??");
    scanf("%d",&estudante.alturacm);
    
    printf("olá %s, você tem %d anos e esta medindo %d",estudante.nome,estudante.idade,estudante.alturacm);
    
    return 0;
}
