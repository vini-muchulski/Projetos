#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for numb in range(2,51,2):
    if numb % 2 == 0:
        print(numb, end=" ")
print("Fim!")