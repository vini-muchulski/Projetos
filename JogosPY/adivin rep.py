print("Olá, usuário(a). Bem vindo ao jogo de adivinhação")

numero_secreto = 7
tentativas= 3
rodada = 1
tent = 3

while (tent > 0):
    print("Rodada", rodada, "de", tentativas)
    chute = int(input("Digite um valor: "))
    print("O valor chutado foi {}" .format(chute))
    tent = tent - 1
    rodada = rodada + 1
    if (numero_secreto == int(chute)):
        print("Você acertou!")
    else:
        if (chute > numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é maior que o mesmo designado")
        elif (chute < numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é menor que o mesmo designado")




