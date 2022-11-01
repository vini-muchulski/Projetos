"36 - Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado."

frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()

frase_concatenada = "".join(palavras)

print(frase_concatenada)


frase_invertida = ""

for letra in range(len(frase_concatenada)-1,-1,-1):
    frase_invertida +=frase_concatenada[letra]

if(frase_invertida == frase_concatenada):
    print("É palindromo")

else:
    print("Não é palindromo")