#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(tupla)

primeiro_elemento = sorted(tupla)
print(f"Valor do menor elemento: {primeiro_elemento[0]}")

maior_elemento = sorted(tupla, reverse=True)
print(f"Valor do maior elemento: {maior_elemento[0]}")


