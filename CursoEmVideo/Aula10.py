nome = str(input("Digite seu nome de acesso: "))
nome = nome.title().strip()

if nome == "Apeiron":
    print("Hey, Boss. Qual a boa?")
else:
    print("Olá, humano {}".format(nome))