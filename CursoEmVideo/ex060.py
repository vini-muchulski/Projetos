#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial

fatorial = int(input("Digite o fatorial: "))

repeticoes = fatorial

inicio = fatorial

print('{}! fatorial '.format(inicio))
while repeticoes > 0:
    if repeticoes > 1:
        sinalizador = "x"

    else:
        sinalizador = "="

    print("{} {}".format(repeticoes, sinalizador), end=" ")

    repeticoes -= 1
    if repeticoes > 0:
        fatorial *= repeticoes

print(' {}'.format(fatorial))





