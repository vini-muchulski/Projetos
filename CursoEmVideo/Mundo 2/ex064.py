#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int(input("Digite um número [999 para finalizar]: "))

cont = 0
somatorio = 0

while numero != 999:
    somatorio += numero
    cont +=1
    numero = int(input("Digite um número [999 para finalizar]: "))


print("FIM DE JOGO. O somatório foi {} e {} números foram gerados".format(somatorio,cont))