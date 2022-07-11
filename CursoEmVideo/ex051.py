#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
import time
pa = int(input("Digite o primeiro termo de uma Progressão Aritimética: "))
razao = int(input("Digite a RAZÃO da Progressão Aritimética: "))


print("-"*40)
time.sleep(1)
print("Progressão Aritimética De 10 Termos.... Carregando")
time.sleep(1.4)
print("-"*40)

#somatorio de uma Progressão Aritimética
x = pa + 9*razao


for termo in range(pa,x+1, razao):
    print(termo, end=" | ")




for termo in range(1,10):
    print(f"{pa} ", end="--> ")
    pa = pa + razao

print(pa)





