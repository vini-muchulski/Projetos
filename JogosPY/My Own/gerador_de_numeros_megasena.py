#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import time
from random import randint


print("-="*20)
numero = int(input("Digite o numero de jogos: "))
print("-="*20)
print("-----GERANDO SEUS NÚMEROS-------")

jogo = []
c = 0
i= 0
while c < numero:
    while True:
        num_megasena = randint(1, 60)
        if num_megasena not in jogo:
            jogo.append(num_megasena)
            i+=1
        if len(jogo) == 6:
            break

    print(jogo)
    jogo.clear()
    #time.sleep(0.5)
    c += 1

print("-----BOA SORTE-------")
