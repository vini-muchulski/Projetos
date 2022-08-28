#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import time
from random import randint


print("-="*20)
numero = int(input("Digite o numero de jogos: "))
print("-="*20)
print("-----GERANDO SEUS NÚMEROS-------")

jogo = []

for game in range(0, numero):
    for i in range(0, 6):
        num_megasena = randint(1, 60)
        jogo.append(num_megasena)

    print(jogo)
    jogo.clear()

    time.sleep(0.5)

print("-----BOA SORTE-------")
