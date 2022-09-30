"Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."

def area(largura,comprimento):
     areaa = largura * comprimento
     print(f" A area é {areaa} m2")

larg = float(input("Digite a largura: "))
comp = float(input("Digite o comprimento: "))

area(larg,comp)



