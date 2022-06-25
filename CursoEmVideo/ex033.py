#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
prim= int(input("Digite um primeiro valor: " ))
sec = int(input("Digite um segundo valor: "))
ter = int(input("Digite um terceiro valor: "))
minimo = prim

if sec<prim and sec<ter:
    minimo= sec
if ter<prim and ter<sec:
    minimo=ter

maximo = prim
if sec>prim and sec>ter:
    maximo=sec
if ter>prim and ter>sec:
    maximo=ter

print("O valor máximo é {} ".format(maximo))
print("O valor mínimo é {} ".format(minimo))