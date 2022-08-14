#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
d = int(input("Digite um número: "))

tupla = (a,b,c,d)


print(f"Quantas vezes apareceu o valor 9? {tupla.count(9)}")
print(f"Em que posição foi digitado o primeiro valor 3: {tupla.index(3)}")

