#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

prim_termo = int(input("Digite o primeiro termo da P.A. = "))
razao = int(input("Digite o razão da P.A. = "))
termo = 0
an = 1
total = 0
vezes_extras = 10


# an = a1 +r.(n-1)
#som = ((a1+an)/2) *n

while vezes_extras !=0:
    total = total + vezes_extras

    while an < total:
        if an == 1:
            termo = prim_termo + razao
            print("{} -> {} ->".format(prim_termo, termo), end=" ")
        else:
            termo += razao
            print("{} ->".format(termo), end=" ")
        an += 1

    vezes_extras = int(input("Quantos termos a mais você quer ver? "))

