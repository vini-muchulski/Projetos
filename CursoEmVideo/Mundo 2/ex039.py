#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual-ano
if idade == 18:
    print("Você deve se alistar esse ano!")

elif idade<18:
    falta = 18-idade
    ano_alistamento = atual + falta
    print("Você tem {} anos. Ainda faltam {} ano(s) para você se alistar. Deverá  se alistar em {}!".format(idade, falta,ano_alistamento))

else:
    atraso = idade - 18
    ano_alistamento= atual - atraso
    print("Você tem {} anos. Você já deveria ter se alistado! Está {} ano(s) atrasado! Deveria ter se alistado em {}!".format(idade, atraso, ano_alistamento))