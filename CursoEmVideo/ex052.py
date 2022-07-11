#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite o primeiro termo de uma Progressão Aritimética: "))

x = True
for numero in range(2,num):
    if num%numero != 0:
        print(f" {num} NÃO  divísível por {numero}")
    else:
        x = False
        print(f"  {num} divísível por {numero}")


if x == True:
    print(f"{num} é primo")

else:
    print(f"{num} NÃO é primo")


