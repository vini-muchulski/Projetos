#Crie um programa que leia a idade de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
menor = 0
maior = 0

x = 18
for i in range(1,8):
    idade = int(input(f"Digite a {i} idade: "))
    if idade<x:
        menor +=1

    else:
        maior+=1

print(f"{maior} pessoas são maiores de idade e {menor} são menores de idade")
