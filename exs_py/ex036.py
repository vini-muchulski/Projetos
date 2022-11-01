"35 - Crie um programa que pede ao usuário que o mesmo digite um número qualquer, em seguida retorne se esse número é primo ou não, caso não, retorne também quantas vezes esse número é divisível "

numero = int(input("Digite um numero: "))
divisores = 0

for i in range(1,numero+1):
    if(numero%i==0):
        divisores +=1


if (divisores ==2):
    print(f"O numero {numero} é primo! Divisivel 1 e {numero}")

else:
    print(f"O numero {numero} NAO é primo! Total de divisores = {divisores}")
