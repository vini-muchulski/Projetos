x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

if x<y+z and y<x+z and z<y+x :
    print("Essas retas obedecem a condição de existência de um triangulo")
    if x==y==z:
        print("Classificação: Equilátero")
    elif x==y or y==z or z==x:
        print("Classificação: Isóceles ")
    elif x !=y or y !=z or z !=x:
        print("Classificação: Escaleno ")
else:
    print("Essas retas NÃO  obedecem a condição de existência de um triangulo")