def contar_caracteres(palavra):
    contagem = {}

    for letra in palavra:
        if letra in contagem:
            contagem[letra] +=1

        else:
            contagem[letra] =1
    print(contagem)

palavra_string = str(input("Digite a frase: "))

contar_caracteres(palavra_string)