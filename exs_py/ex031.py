"31 - Crie um programa que realiza a Progressão Aritmética de 20 elementos, com primeiro termo e razão definidos pelo usuário"

primeiro_termo = int(input("Digiteo primeiro termo da PA: "))
razao= int(input("Digite a razao: "))
pa = primeiro_termo
print(pa)

for i in range(0,20-1):
    pa = pa + razao
    print(pa)