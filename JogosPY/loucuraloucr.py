def jogo_forca():
    print("Olá, usuário(a). Bem vindo ao jogo da forca ")

    palavra_secreta ="aluno"
    lista_tarja = ["_","_","_","_","_"]

    enforcou = False
    acertou = False


    while (not acertou and not enforcou):
        chute = input("Digite uma letra: {} " .format(lista_tarja))
        chute = chute.strip()

        posicao = 0

        for letra in palavra_secreta:

            if letra.upper() == chute.upper():
                lista_tarja[posicao] = letra

            posicao = posicao +1
        print(lista_tarja)
        if lista_tarja == ['a', 'l', 'u', 'n', 'o']:
            enforcou = True
            acertou = True
            print("Parabéns! Você conseguiu")





        print("Jogando...")



    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo_forca()