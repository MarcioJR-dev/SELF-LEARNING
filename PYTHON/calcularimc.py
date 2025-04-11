nome = input("Digite seu nome:")
peso = float(input("Digite seu peso em KG:"))
altura = float(input("Digite sua altura em metros:"))

imc = peso/(altura**2)

print(f"Olá {nome} você está pesando {peso}kg e medindo {altura}!")
if imc >= 18.5 and imc <= 24.9:
 print("Peso ideal.")
elif imc < 18.5:
 print ("Abaixo do peso.")
elif imc >= 25 and imc <= 29.9:
 print ("sobrepeso.")
else:
 print ("obeso.")
