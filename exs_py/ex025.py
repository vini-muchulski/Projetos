"25 - Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem dizendo se tal número é PAR ou se é ÍMPAR:"

num = int(input("Digite um valor inteiro: "))

if (num%2 == 0):
    print(num ," é PAR!")

else:
    print(num ," é IMPAR!")