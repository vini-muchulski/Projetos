"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print("*"*20)
print("{:^20}".format("Byte Bank"))
print("*"*20)

valor = int(input("Digite o valor a ser sacado: "))
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0

while True:
    while valor>=50:
        valor-=50
        cont_50 +=1
    while valor>=20:
        valor-=20
        cont_20 +=1

    while valor>=10:
        valor-=10
        cont_10 +=1

    while valor>=1:
        valor-=1
        cont_1 +=1

    break

print("""TOTAL DE CÉDULAS: 
50 reais = {} 
20 reais = {} 
10 reais = {} 
1 reais = {}  """.format(cont_50,cont_20,cont_10,cont_1))