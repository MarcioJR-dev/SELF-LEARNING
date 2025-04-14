nome = input("Qual seu nome?")
idade = int(input("Qual sua idade?"))
print(f"olá {nome}, você tem {idade} anos")
--
peso = float(input("Qual seu peso? em kg"))
altura = float(input("Qual sua altura? em metro"))
imc = peso/(altura**2)
print(f"seu imc é {imc}")
if imc <18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("peso normal")
else:
    print("Obeso")

soma = 0
num = None

while num != 0:
    num = int(input("Digite um numero"))
    soma = soma+num

print(f"Soma total:{soma}")
