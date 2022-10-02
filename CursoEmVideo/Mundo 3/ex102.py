"Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."

def fatorial(num,show=False):
    total = 1
    for i in range(num,1,-1):
        total = total * num
        num = num - 1
        print(total)

    if show == True:
        for i in range(num, 1, -1):
            print(f"{num} X")


fatorial(6)
