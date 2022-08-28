lista_par = []
lista_impar = []

for i in range(1,8):
    numero = int(input(f"Digite o {i}° número: "))
    if numero%2 == 0 :
        if numero not in lista_par:
         lista_par.append(numero)

    else:
        if numero not in lista_impar:
         lista_impar.append(numero)


print("Lista de impares: ",sorted(lista_impar))
print("Lista de pares: ", sorted(lista_par))