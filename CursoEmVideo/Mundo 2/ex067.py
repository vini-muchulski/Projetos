#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input("Digite um valor: "))
    cont = 0

    if numero < 0:
        break
    print("*" * 20)

    while cont <=9:

        cont += 1
        multiplicacao = cont*numero
        print(f"{numero}  X  {cont} = {multiplicacao}")

    print("*"*20)


print(" FIM ")