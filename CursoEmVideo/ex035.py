#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

if x<y+z and y<x+z and z<y+x :
    print("Essas retas obedecem a condição de existência de um triangulo")
else:
    print("Essas retas NÃO  obedecem a condição de existência de um triangulo")
