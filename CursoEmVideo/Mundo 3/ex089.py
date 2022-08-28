#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []

while True:
    aluno = str(input("Nome: "))
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = (nota2+nota1)/2
    lista.append([aluno,[nota1,nota2],media])

    continua = str(input("Deseja continuar? [S/N]: "))
    continua = continua.upper()

    if continua != "S":
        break
while True:
    c = 0
    for e in lista:
        print(f"Número: {c} - Nome: {e[0]} - Média: {e[2]}")
        c +=1

    valor = int(input("Digite a nota do aluno que vc quer ver: [999 para interromper] "))
    if valor == 999:
        break
    else:
        print(lista[valor][1])

