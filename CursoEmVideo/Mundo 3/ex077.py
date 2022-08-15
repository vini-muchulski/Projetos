#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ("apeiron", "homem", "foguete", "engenharia", "aviacao", "fisiculturismo")

for palavra in tupla:
    print(f"\nEm {palavra.upper()} existem: ",end="")

    for letra in palavra:
        if letra in "aeiou":
            print(letra,end=" ")
