listagem = [[],[], []]

cont_par = 0
cont_terc = 0
maior_valor = 0

for i in range(0,3):
    numero = int(input(f"Digite um numero (0,{i}): "))
    listagem[0].append(numero)

    if numero%2 == 0:
        cont_par +=numero

for i in range(0,3):
    numero = int(input(f"Digite um numero (1,{i}): "))
    listagem[1].append(numero)
    if numero%2 == 0:
        cont_par +=numero

    if len(listagem[1]) ==0:
        maior_valor = numero

    if len(listagem[1]) !=0:
        if numero>maior_valor:
         maior_valor = numero

for i in range(0,3):
    numero = int(input(f"Digite um numero (2,{i}): "))
    listagem[2].append(numero)
    if numero%2 == 0:
        cont_par +=numero



print("-="*20)

cont_terc = listagem[0][2]+listagem[1][2]+listagem[2][2]

for a,b,c in listagem[0],listagem[1],listagem[2]:
    print(f"[{a}]",f"[{b}]",f"[{c}]")

print("Soma dos valores da terceira coluna: ", cont_terc)
print("O maior valor da segunda linha: ", maior_valor)
print("Soma de todos os valores pares digitados: ",cont_par)



