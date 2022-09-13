#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
 
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


