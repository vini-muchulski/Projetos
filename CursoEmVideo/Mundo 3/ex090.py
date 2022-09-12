#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
name = str(input("Digite o nome: ")).title()
nota = float(input("Qual a média: "))

dicit = {"nome": name, "media": nota}

status = "Aprovado"

if nota<7:
    status = "Reprovado"

"""for k,v in dicit.items():
    print(dicit)"""

print(f"Nome: {dicit['nome']} \nMédia: {dicit['media']} \nStatus: {status}")