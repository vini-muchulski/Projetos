"Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."

def maior(n1,n2,n3):

    maior = n1
    menor = n1

    if n2>n1 and n2>n3:
        maior = n2

    if n3>n1 and n3>n2:
        maior = n3

    if n2<n1 and n2<n3:
        menor = n2

    if n3 < n1 and n2 > n3:
        menor = n3

    print(f"O menor é {menor} e o maior é {maior}")

maior(5,3,4)


def maiores(*numeros):
    i = maior_ = 0
    for valor in numeros:
        if i == 0:
            maior_ =  valor
        else:
            if valor>maior_:
                maior_ = valor

    print(f"O maior valo r foi {maior_}")


maiores(1,2,3,4,5,6,6,7,8)