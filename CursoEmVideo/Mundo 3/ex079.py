#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    numero = int(input("Digite um valor : "))
    if numero not in lista:
        lista.append(numero)
    else:
        print("O valor já está na lista")

    continua = str(input("Deseja continuar? [S/N]: "))
    continua = continua.upper()

    if continua != "S":
        break

print("-="*20)
print(sorted(lista))