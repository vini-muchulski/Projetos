"Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo"

def contador(inicio,fim,passo):
    if fim>inicio:
        while inicio<=fim:
            print(inicio)
            inicio = inicio + passo

    else:
        while inicio>=fim:
            print(inicio)
            inicio = inicio - passo

contador(10,1,2)

