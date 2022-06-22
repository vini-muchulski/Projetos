import random

def inicializacao():

    print("Olá, usuário(a). Bem vindo ao jogo da forca! ")


def palavra():
    arquivo = open("palavras.txt", "r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))

    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

def lista_letras_acertadas():
    palavra_secreta = palavra()
    return ["_" for letra in palavra_secreta]


def jogo_forca():

    inicializacao()

    palavra_secreta = palavra()

    lista_tarja = lista_letras_acertadas()

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

        print("Carregando...")

        if "_" not in lista_tarja:
            enforcou = True
            acertou = True
            print("Parabéns! :) Você conseguiu! A palavra era {}.".format(palavra_secreta))

            print("Parabéns, você ganhou!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")

        if(tentativas == 0):
            print("Você não conseguiu acertar e ficou sem tentativas! *_* A palavra era {}.".format(palavra_secreta))
            break

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo_forca()
