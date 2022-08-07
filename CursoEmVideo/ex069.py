#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

"""A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""


cont_18 = 0
cont_h = 0
cont_m20 = 0

while True:
    idade = int(input("IDADE: "))
    genero = " "
    while genero not in "MF":
        genero = str(input("Genêro [M/F]: ")).strip().upper()


    continua = str(input("Deseja continuar [S/N]: ")).strip().upper()

    if idade>= 18:
        cont_18+=1
    if idade <= 20 and genero =="F":
        cont_m20+=1
    if genero =="M":
        cont_h +=1

    if continua =="N":
        break

print(f"""ANÁLISE DE DADOS:

    Quantas pessoas tem mais de 18 anos = {cont_18}
    Quantos homens foram cadastrados = {cont_h}
    Quantas mulheres tem menos de 20 anos = {cont_m20}""")
