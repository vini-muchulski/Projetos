#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

prim_termo = int(input("Digite o primeiro termo da P.A. = "))
razao = int(input("Digite o razão da P.A. = "))
termo = 0
an = 1

# an = a1 +r.(n-1)
#som = ((a1+an)/2) *n

while an < 10:
    if an == 1:
        termo = prim_termo + razao
        print("{} -> {} ->".format(prim_termo, termo), end=" ")
    else:
        termo += razao
        print("{} ->".format(termo), end=" ")
    an += 1


print("Fim ")




