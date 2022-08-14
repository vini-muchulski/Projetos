#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

while True:
    numb = int(input("Digite um numero: "))
    par_impar = str(input("Par ou ímpar? [P/I]: ")).strip().upper()
    compt_numb = random.randint(0,10)

    razao = numb + compt_numb
    cont = 0

    if razao%2 == 0 and par_impar =="P":
        cont+=1
    elif razao%2 == 1 and par_impar =="I":
        cont += 1
    else:
        break

print(f"FIM DE JOGO! O computador jogou {compt_numb} e você jogou {numb}. O total foi {razao}. Você fez {cont} vitórias consecutivas!")





