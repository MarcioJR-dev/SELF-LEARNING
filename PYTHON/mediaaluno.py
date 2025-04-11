nome = input("Qual seu nome?:")
ProvaUm = int(input("Qual foi sua nota da primeira prova?:"))
ProvaDois = int(input("Qual foi sua nota da segunda prova?:"))

Media = (ProvaUm+ProvaDois)/2
print (f"Olá {nome}, sua média foi {Media}")

if Media >= 5 and Media < 7:
    print("Recuperação!")
elif Media < 5:
    print("Reprovado!")
else:
    print("Aprovado!")
