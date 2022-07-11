#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for i in range (1,6):
    peso = float(input(f"Digite o peso da {i} pessoa: "))
    lista.append(peso)

pesos_ordenados = sorted(lista)

print(pesos_ordenados)

pesos_invertidos = list(reversed(sorted(lista)))

print(f"O menor peso foi {pesos_ordenados[0]} Kg")
print(f"O maior peso foi {(pesos_invertidos[0])} Kg")

