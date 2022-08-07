"""Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato."""

custo_total = 0
qnts_1000 = 0
mais_barato_preco =0
mais_barato_nome =0
contador_produtos = 0

while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Qual o preço do produto: R$ "))

    contador_produtos +=1
    custo_total+= preco

    if contador_produtos ==1:
        mais_barato_nome = nome
        mais_barato_preco = preco

    if preco < mais_barato_preco:
        mais_barato_nome = nome
        mais_barato_preco = preco

    if preco>=1000:
        qnts_1000 +=1

    continua = str(input("Deseja continuar [S/N]: ")).strip().upper()
    if continua =="N":
        break

print("*"*20)
print(f"O custo total foi {custo_total}, o produto mais barato foi {mais_barato_nome} custando R$ {mais_barato_preco} e {qnts_1000} produtos custaram mais que R$ 1000")

