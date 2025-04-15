#include <stdio.h>

struct produtos{
    char nome[50];
    int preco;
    int quantidade;
};

int main(){
  struct produtos item[5];
  
  for (int i=0; i<5; i++){
    printf("CRIE SEU ITEM");
    printf("Qual nome do item? %d",i+1);
    scanf("%s", item[i].nome);
    printf("Qual preço do item?");
    scanf("%d", &item[i].preco);
    printf("Quantos tem?");
    scanf("%d", &item[i].quantidade);
  };
  printf("Lista de items:\n");
  
   for (int i=0; i<5; i++){
       int fullvalor[i];
     fullvalor[i] = item[i].preco*item[i].quantidade;
     printf("Item numero %d",i+1);
     printf(" Nome: %s, Preço: %d, Quantidade: %d, total:%d.\n",item[i].nome,item[i].preco,item[i].quantidade,fullvalor[i]);
   
    
};
}
