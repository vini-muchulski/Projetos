#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split()
juntar = "".join(palavras)
inverso =""

for letra in range(len(juntar)-1, -1,-1):
    inverso +=((juntar[letra]))


if inverso == juntar:
    print(f"{juntar} é palíndromo")

else:
    print(f"{inverso} e {juntar} NÃO são palíndromos")

inverso = juntar[::-1]

print(inverso)



