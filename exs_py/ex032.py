"32 - Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário"

num = int(input("Digite um número: "))

for i in range (0,11):
    print(f"{num} X {i} = {num*i}")
    