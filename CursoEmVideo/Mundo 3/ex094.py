#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média



from pydoc import visiblename


infos = {}
lista_final = list()

cont = 0
media_idades = 0

while True:
    
    infos['Nome'] = str(input("Digite o nome: "))
    infos['Idade'] = int(input("Digite a idade: "))
    infos['Sexo'] = str(input("Digite o genero (M/F): "))

    if infos['Sexo'] not in "MmFf":  
        while True:
            print("ERRO! Insira novamente!")
            infos['Sexo'] = str(input("Digite o genero (M/F): "))
            if infos['Sexo'] in "MmFf":
                break

    cont +=1
    media_idades +=infos['Idade']
    lista_final.append(infos.copy())

    continua = str(input("Deseja continuar? [S/N]: "))
    continua = continua.upper()
    if continua != "S":
        break

media_final = media_idades/cont

print(f"Ao todo {cont} pessoas foram cadastradas")
print(f"A média foi {media_final} anos")
print(lista_final)

    
        

