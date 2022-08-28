"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:                                                                                                    A) Quantas pessoas foram cadastradas.                                                                                                                B) Uma listagem com as pessoas mais pesadas.                                                                                                    C) Uma listagem com as pessoas mais leves.
"""

listagem = []
peso_nome = []
cont = 0
maior = menor = 0

while True:
    nome = str(input("Nome: ")).title()
    peso = int(input("Peso: "))
    peso_nome.append(nome)
    peso_nome.append(peso)

    if cont == 0:
        maior = menor = peso_nome[1]

    if peso_nome[1] >= maior:
        peso_nome[1] = maior

    if peso_nome[1] < menor:
        peso_nome[1] = menor

    listagem.append(peso_nome[:])
    peso_nome.clear()

    cont += 1

    print(maior,menor,listagem, peso_nome,peso,cont)


    continua = str(input("Deseja continuar? [S/N]: "))
    continua = continua.upper()

    if continua != "S":
        break

print("-="*20)

print(f"Ao todo {cont} pessoas foram cadastradas")
print(f"Maior peso: {maior}", end=" ")

for elemento in listagem:
    if elemento[1] == maior:
        print(elemento[0])

print(f"Menor peso: {menor}", end=" ")

for elemento in listagem:
    if elemento[1] == menor:
        print(elemento[0])



