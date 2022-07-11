#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma=0
valor=0
for i in range(1,7):
    numb = int(input(f"Digite o {i} valor: "))
    if numb%2==0:
        soma =soma + numb
        valor = valor +1

print("O somátorio de {} valores foi {}".format(valor, soma))


