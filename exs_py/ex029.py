"29 - Crie um programa que lê um valor de início e um valor de fim, exibindo em tela a contagem dos números dentro desse intervalo. "

inicio = int(input("Digite um valor inicial: "))

fim = int(input("Digite um valor final: "))

for i in range(inicio,fim+1):
    print(i, " ",end="")