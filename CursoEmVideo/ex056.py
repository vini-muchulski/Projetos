#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
veio = 0
nome_veio = ""
mocas = 0

for info in range(1,5):
    nome = str(input("digite o nome: ")).strip().title()
    idade = int(input("digite a idade: "))
    sexo = str(input("Sexo(M/F): ")).strip().title()
    media = media + idade
    if info == 1 and sexo == 'M':
        veio = idade
        nome_veio = nome
    elif sexo == 'M' and idade>veio:
        veio = idade
        nome_veio = nome

    elif sexo == "F" and idade<20:
        mocas += 1

media_geral = media/4
print("A media das idades foi {:.1f}".format(media_geral))
print(f"O véio do grupo é o {nome_veio} e tem {veio} anos")
print("O grupo possui {} moças".format(mocas))


