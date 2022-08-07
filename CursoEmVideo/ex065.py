#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


cont = 0
somatorio = 0
continua = "S"
maior = menor = 0

while continua in "Ss":
    numb = int(input("Digite um número: "))
    cont += 1
    somatorio += numb
    continua = str(input("Deseja continuar? [S/N]: ")).upper()

    if cont ==1:
        maior = menor = numb

    else:
        if numb>maior:
            maior = numb

        elif menor>numb:
            menor = numb

media = somatorio/cont
print("{} números foram gerados e a média entre eles foi {:.2f}.".format(cont, media))

if cont>= 2 and maior != menor:
    print("O menor número foi {} e o maior foi {}".format( menor, maior))


