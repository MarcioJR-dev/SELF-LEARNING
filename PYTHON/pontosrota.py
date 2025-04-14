
def pedirponto():
    pontos = []
    for i in range(5):
        ponto = int(input(f"Digite a localização do ponto {i + 1}: "))
        pontos.append(ponto)
    return pontos
