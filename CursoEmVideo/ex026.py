#programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: "))
frase = frase.strip()
frase = frase.lower()

print("A letra A apareceu {} vezes".format(frase.count("a")))
