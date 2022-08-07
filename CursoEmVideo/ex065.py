#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


cont = 0
somatorio = 0
continua = "S"

while continua =="S":


    numb = int(input("Digite um número: "))
    cont += 1
    somatorio += numb
    continua = str(input("Deseja continuar? [S/N]: ")).upper()

media = somatorio/cont

print(" {} números foram gerados e a média entre eles foi {:.2f}".format(cont, media))


