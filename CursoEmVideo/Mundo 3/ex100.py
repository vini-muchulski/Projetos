"Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."

from random import randint

def gera_numeros(lista):

    for elemento in range(0, 5):
        a = randint(1, 10)
        lista.append(a)
    return lista

def soma_par(lista):

    soma_pares = 0
    for elemento in lista:
        if elemento%2 == 0:
            soma_pares +=elemento

    print(lista)
    print(f"A soma dos pares é = {soma_pares}")

lista = []

gera_numeros(lista)
soma_par(lista)





