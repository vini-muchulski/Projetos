import math
import random


print("Olá, usuário(a). Bem vindo ao jogo de adivinhação")

numero_random = random.randrange(1,11)
numero_secreto = round(numero_random)

tentativas= (input("Digite o número de tentativas a serem realizadas: "))
if(int(tentativas)<1):
    print("Insira um número válido")


for rodada in range (1,int(tentativas)+1):

    print("Rodada {} de {}" .format(rodada, tentativas))
    chute = int(input("Digite um valor entre 1 e 10: "))
    print("O valor chutado foi {}" .format(chute))
    if(chute<1 or chute>10):
        print("O valor digitado é incompatível ")
        continue

    if (numero_secreto == int(chute)):
        print("Você acertou!")
        break
    if (chute > numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é maior que o designado")
    elif (chute < numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é menor que o designado")

print("O valor gerado foi ", numero_secreto)
print("Fim de jogo")
