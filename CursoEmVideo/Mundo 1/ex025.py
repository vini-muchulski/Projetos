 # programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Qual seu nome? "))
nome = nome.lower()
nome = nome.strip()
nome_silva = nome.find("silva")

if (nome_silva!= -1):
    print("Você possui um sobrenome comum")

else:
    print("Vc não é um Silva")