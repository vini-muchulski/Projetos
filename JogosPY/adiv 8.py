import math
import random


print("Olá, usuário(a). Bem vindo ao jogo de adivinhação - "
    "Sua pontuação inicial é de 10 pontos e a cada tentativa errada um ponto é reduzido")

numero_random = random.randrange(1,11)
numero_secreto = round(numero_random)

dificuldade = int(input("Digite o nível de dificuldade desejado: [1] Fácil - [2] Médio - [3] Difícil : "))
if(int(dificuldade)==1):
    tentativas= 7
if(int(dificuldade)==2):
    tentativas= 5
if(int(dificuldade)==3):
    tentativas= 3


for rodada in range (1,int(tentativas)+1):


    print("Rodada {} de {}" .format(rodada, tentativas))
    chute = int(input("Digite um valor entre 1 e 10: "))

    if(chute<1 or chute>10):
        print("O valor digitado é incompatível ")
        continue

    pontos: int = 11 - rodada
    if (numero_secreto == int(chute)):
        print("Você acertou! Sua pontuação foi {}".format(pontos))
        break
    pontos: int = 10 - rodada
    print("O valor chutado foi {}, sua pontuação restante é de {}".format(chute, pontos))
    if (chute > numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é maior que o designado")
    elif (chute < numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é menor que o designado")

print("O valor gerado foi ", numero_secreto)
print("Fim de jogo, sua pontuação final foi de {}".format(pontos))
