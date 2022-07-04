#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
primeiro = int(input("Digite um numero: "))
segundo = int(input("Digite o segundo numero: "))

if primeiro>segundo:
    print("O PRIMEIRO valor é maior")
elif primeiro == segundo:
    print("Os valores  são iguais")
else:
    print("O SEGUNDO valor é maior")