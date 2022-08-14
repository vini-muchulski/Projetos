#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Digite um número: "))

for num in range(1,11):
    x = numero*num
    print("{} X {} = {}".format(numero,num,x))