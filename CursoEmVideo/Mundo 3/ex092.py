#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import time

ano_atual = time.localtime()[0]

infos = {}
infos['Nome'] = str(input("Digite o nome: ")).title()
infos['Idade: '] = ano_atual - int(input("Qual ano de nascimento: "))
ctps = int(input("Número da CTPS (0 não tem): "))

if ctps == 0:
    infos['Carteira de trabalho: '] = "0"
    print("-=" * 30)
    print(f" Nome: {infos['Nome']} \n Idade: {infos['Idade: ']} \n CTPS = {ctps}")

else:
    infos['Ano_Contratacao'] = int(input("Qual o ano de contratação? "))
    infos['Aposentadora'] = infos['Ano_Contratacao'] + 35
    print("-=" * 30)
    print(f" Nome: {infos['Nome']} \n Idade: {infos['Idade: ']} anos \n CTPS = {ctps} \n Ano de Contratação = {infos['Ano_Contratacao']} \n Ano de Aposentadoria = {infos['Aposentadora']}")








