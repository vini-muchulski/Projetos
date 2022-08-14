#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numero_random = random.randrange(1,11)
numero_secreto = round(numero_random)

i=1
while i<5:
    print("Tentativa {} de 5".format(i))
    chute = input("Chute um número: ")

    i= i + 1

    if chute == numero_secreto:
        print("Parabéns! Você acertou!")

    else:
        print("Você não acertou!")

print("O número secreto foi {}".format(numero_secreto))





