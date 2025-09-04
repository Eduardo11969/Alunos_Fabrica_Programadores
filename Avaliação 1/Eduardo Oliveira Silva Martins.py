# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 09/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR
# Eduardo Oliveira Silva Martins


peso = float(input("Digite o peso "))
Altura = float(input("Digite a sua altura "))
imc = peso / Altura**2
print(imc)

if imc <= 18.5 :
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade Grau 3")


