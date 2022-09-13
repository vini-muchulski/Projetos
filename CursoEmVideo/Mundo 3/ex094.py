#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
infos = {}
infos['Nome'] = []
infos['Sexo'] = []
infos['Idade'] = []

nome = 0
idade = 0
sexo = 0
cont = 0
media_idades = 0

while True:
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o genero (M/F): "))
    cont +=1
    media_idades +=idade

    if sexo not in "MmFf":
        print("ERRO! Insira novamente!")
        sexo = str(input("Digite o genero (M/F): "))

    infos['Nome'].append(nome)
    infos['Sexo'].append(sexo)
    infos['Idade'].append(idade)

    continua = str(input("Deseja continuar? [S/N]: "))
    continua = continua.upper()

    if continua != "S":
        break

media_final = media_idades/cont

print(f"Ao todo {cont} pessoas foram cadastradas")
print(f"A média foi {media_final} anos")
print(infos)
    
        

