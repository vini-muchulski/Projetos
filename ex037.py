#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
valor = int(input("Digite um valor inteiro: "))

base = int(input("Qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal: "))

if base == 1:
    print("O valor {} em binário é {}".format(valor, bin(valor)[2:]))
elif base == 2:
    print("O valor {} em octal é {} ".format(valor, oct(valor)[2:]))

elif base == 3:
    print("O valor {} em hexadecimal é {} ".format(valor, hex(valor)[2:]))

else:
    print("Essa opção é inválida!")


