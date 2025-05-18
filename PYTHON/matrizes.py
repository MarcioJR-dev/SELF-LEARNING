import random

def gerar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(1, 100))  # Valores entre 1 e 100
        matriz.append(linha)
    return matriz

# Exemplo de uso
linhas = 3
colunas = 4
matriz = gerar_matriz(linhas, colunas)

# Exibindo a matriz
for linha in matriz:
    print(linha)
