#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

qnt_termos = int(input("Digite qnts termos vc quer ver: "))

termo_zero = 0
termo_inicial = 1

print(" {} -> {}".format(termo_zero, termo_inicial),end=" ")

cont = 3

while cont <= qnt_termos:


    termo_dois = termo_zero + termo_inicial
    print("-> {}".format(termo_dois),end=" ")

    termo_zero =termo_inicial
    termo_inicial = termo_dois
    cont +=1
print("= Fim")
