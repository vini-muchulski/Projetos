import random
def jogo_forca():



    print("Olá, usuário(a). Bem vindo ao jogo da forca! " )

    arquivo = open("palavras.txt", "r")
    palavra =[]

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))

    palavra_secreta = palavra[numero].upper()

    lista_tarja = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 5

    while (not acertou and not enforcou):
        chute = input("Digite uma letra: {} : ".format(lista_tarja))
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if letra.upper() == chute.upper():
                    lista_tarja[posicao] = letra
                posicao = posicao + 1
            print("Ainda possui {} tentativas".format(tentativas))
        else:

            tentativas = tentativas - 1
            print("Restam ainda {} tentativas".format(tentativas))

        if "_" not in lista_tarja:
            enforcou = True
            acertou = True
            print("Parabéns! Você conseguiu! A palavra era {}".format(palavra_secreta))

        if(tentativas == 0):
            print("Você não conseguiu acertar e ficou sem tentativas! A palavra era {}".format(palavra_secreta))
            break


        print("Carregando...")


    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo_forca()