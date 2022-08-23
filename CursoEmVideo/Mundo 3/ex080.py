#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
cont_posic = 0
lista = []
for c in range(0,5):
    numero = int(input("Digite um valor : "))

    if c==0:
        lista.append(numero)
        referencia_numero = numero
        referencia_posicao= 0

    if c !=0:
        if numero>lista[len(lista)-1]:
            lista.append(numero)

        else:
            cont = 0
            while cont < len(lista):
                if numero<= lista[cont]:
                    lista.insert(cont, numero)
                    break
                else:
                    cont +=1


print("-="*20)
print(lista)
