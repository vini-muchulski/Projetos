#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random

jogadores = {"Jogador 1": random.randint(1,6),
             "Jogador 2": random.randint(1,6),
             "Jogador 3": random.randint(1,6),
             "Jogador 4": random.randint(1,6),}



for k in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f"{k} = ", jogadores[k])

print(jogadores)
