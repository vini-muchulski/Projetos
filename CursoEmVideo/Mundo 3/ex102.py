"Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."

def fatorial(num,show=False):
    total = 1
    for i in range(num,0,-1):

        if show == True:
            if i>1:
                print(f"{num} x", end=" ")

            else:
                print(f"{num} =", end=" ")

        total = total * num
        num = num - 1

    return total

print(fatorial(3,True))
