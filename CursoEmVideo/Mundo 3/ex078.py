#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista =[]


for c in range(0,5):

    numero = int(input("Digite um valor para a posição {} : ".format(c)))
    lista.append(numero)



maior_valor = sorted(lista)
menor_valor = sorted(lista, reverse=True)

print("-="*20)
print(lista)
print(f"O maior valor foi {maior_valor[0]}  e menor foi {menor_valor[0]}")

for indice, valor in enumerate(lista):
    if valor == maior_valor[0]:
        print("O maior valor esta na posição ",indice)

    if valor == menor_valor[0]:
        print("O menor valor esta na posição ",indice)

