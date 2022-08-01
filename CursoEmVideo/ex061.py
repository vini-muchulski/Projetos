#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

prim_termo = int(input("Digite o primeiro termo da P.A. = "))
razao = int(input("Digite o razão da P.A. = "))
somatorio = 0
termo = 1

# an = a1 +r.(n-1)
#som = ((a1+an)/2) *n

while termo < 10:
    if termo == 1:
        somatorio = prim_termo + razao
        print("{} -> ".format(somatorio), end=" ")
    else:
        somatorio += razao
        print("{} -> ".format(somatorio), end=" ")
    termo += 1



print(somatorio)




