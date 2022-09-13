#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

infos = {}
infos['nome'] = str(input("Nome do jogador: ")).title()
infos['partidas'] = int(input(f"Quantas partidas o {infos['nome']} jogou? "))
infos['gols']= []
gol = 0
total_gols = 0

for i in range(1,infos['partidas']+1):
    gol =int(input(f"Quantos gols na {i}° partida? "))
    total_gols +=gol
    infos['gols'].append(gol)

infos['Total de gols '] = total_gols

print(infos)


