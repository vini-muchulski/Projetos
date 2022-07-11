#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
i = 0
for numb in range(1,500):
    if numb % 3 == 0 and not numb % 2 == 0:
        i = i + numb

print("A soma de todos os valores são {}".format(i))