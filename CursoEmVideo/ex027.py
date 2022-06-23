#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input("Digite seu nome completo: ").strip()).title()
nome_split = nome.split()
np = nome_split[0]


print(f"""Olá, seu nome é {nome}
Seu primeiro nome é {np}
Seu último nome é {nome_split[len(nome_split)-1]}""")
