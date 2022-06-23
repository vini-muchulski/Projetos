# programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Qual cidade você nasceu? "))
cidade = cidade.lower()
cidade = cidade.title()
listagem = cidade.split()
santos = cidade.find("Santos")

if (listagem[0] == "Santos") and (santos==0):
    print("Vc nasceu em santos")

else:
    print("Vc n nasceu em santos")

