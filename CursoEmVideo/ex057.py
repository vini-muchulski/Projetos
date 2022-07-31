#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
genero = (input("Digite o gênero (M/F) :")).upper().strip()

while genero not in "MF":
    genero = (input("Digite o gênero (M/F) :")).upper().strip()

print(genero)