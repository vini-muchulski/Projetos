from datetime import date
ano = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual-ano

print("A idade do atleta é {}".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")

elif idade <=14:
    print("Classificação: INFANTIL")

elif idade <=19:
    print("Classificação: JUNIOR")

elif idade <=25:
    print("Classificação: SENIOR")

elif 25<idade :
    print("Classificação: MASTER")

