print("Olá, usuário(a). Bem vindo ao jogo de adivinhação")

numero_secreto = 7
tentativas= 3


for rodada in range (1,tentativas+1):

    print("Rodada {} de {}" .format(rodada, tentativas))
    chute = int(input("Digite um valor entre 1 e 20: "))
    print("O valor chutado foi {}" .format(chute))
    if(chute<1 or chute>20):
        print("O valor digitado é incompatível ")
        continue

    if (numero_secreto == int(chute)):
        print("Você acertou!")
        break
    if (chute > numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é maior que o designado")
    elif (chute < numero_secreto):
            print("Você não acertou, tente novamente! O numero chutado é menor que o designado")
print("Fim de jogo")
