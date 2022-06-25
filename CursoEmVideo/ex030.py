#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Digite um número: "))

verif = num%2
if verif==1:
    print("O número é impar")
else:
    print("O número é par")