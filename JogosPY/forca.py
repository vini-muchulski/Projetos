def jogo_forca():
    print("Olá, usuário(a). Bem vindo ao jogo da forca! Você possui 10 tentativas! ")

    palavra_secreta = "vini".upper()
    lista_tarja = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 10


    while (not acertou and not enforcou):
        chute = input("Digite uma letra: {} : " .format(lista_tarja))
        chute = chute.strip().upper()


        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if letra.upper() == chute.upper():
                    lista_tarja[posicao] = letra
                posicao = posicao +1
            print("Ainda possui {} tentativas".format(tentativas))
        else:

            tentativas = tentativas - 1
            print("Restam ainda {} tentativas".format(tentativas))

        if "_" not in lista_tarja:
            enforcou = True
            acertou = True
            print("Parabéns! Você conseguiu! A palavra era {}".format(palavra_secreta))

        if(tentativas == 0):
            print("Você não conseguiu acertar e ficou sem tentativas")
            break


        print("Carregando...")


    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo_forca()
