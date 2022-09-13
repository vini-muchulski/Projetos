#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
from operator import itemgetter
from time import sleep

jogadores = {"Jogador 1": random.randint(1,6),
             "Jogador 2": random.randint(1,6),
             "Jogador 3": random.randint(1,6),
             "Jogador 4": random.randint(1,6),}



rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(rank)

p = 0
for i,v in rank:
    p +=1
    print(f"{p}° lugar - ",i, "==",v)
    sleep(1)


