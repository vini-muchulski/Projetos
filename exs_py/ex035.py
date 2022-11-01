"""34 - Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos:"""

cont_impares = 0
soma_impares = 0

for i in range(0,101):
    if(i%2==1):
        soma_impares +=i
        cont_impares +=1

print(f"A soma dos impares = {soma_impares} --- Total de numeros impares = {cont_impares}")
