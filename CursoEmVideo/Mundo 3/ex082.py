#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_imp = []

while True:
    numero = int(input("Digite um valor : "))
    if numero not in lista:
        lista.append(numero)
    else:
        print("O valor já está na lista")

    if numero%2 ==0:
        lista_par.append(numero)

    if numero%2 ==1:
        lista_imp.append(numero)



    continua = str(input("Deseja continuar? [S/N]: "))
    continua = continua.upper()

    if continua != "S":
        break

print("-="*20)

print("LISTA DE VALORES: ",lista)
print("LISTA DE NÚMEROS PARES: ",lista_par)
print("LISTA DE NÚMEROS ÍMPARES: ", lista_imp)