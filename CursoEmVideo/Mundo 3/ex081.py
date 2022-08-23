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

print(f"A lista possui {len(lista)} elementos")

if 5 in lista:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 NÃO está na lista!")

print(sorted(lista, reverse=True))