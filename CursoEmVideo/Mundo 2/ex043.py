peso= float(input("Digite seu peso(kg): "))
altura= float(input("Qual sua altura(m): "))

imc = peso/altura**2

print("O IMC é {:.1f}".format(imc))

if imc <= 18:
    print("Classificação: ABAIXO DO PESO ")

elif imc <= 25:
    print("Classificação: PESO IDEAL")

elif imc <= 30:
    print("Classificação: SOBREPESO")

elif imc <= 40:
    print("Classificação: OBESIDADE")

elif imc > 40:
    print("Classificação: OBESIDADE MÓRBIDA")

