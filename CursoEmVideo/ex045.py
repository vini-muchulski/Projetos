from random import randint
print("="*10,"JOKENPO","="*10)
print("""0 - Pedra,
1 - Papel,
2 - Tesoura""")

chute =int(input("Digite seu valor: "))
valor_secreto = randint(0,2)
itens =("Pedra","Papel","Tesoura")
joken = itens[valor_secreto]
jog_joken = itens[chute]




if joken == "Pedra":
    if jog_joken == "Papel":
        print("VITÓRIA! O computador jogou {} e você jogou {}".format(joken, jog_joken))
    elif jog_joken=="Tesoura":
        print("DERROTA! O computador jogou {} e você jogou {}".format(joken, jog_joken))

if joken == "Papel":
    if jog_joken == "Tesoura":
        print("VITÓRIA! O computador jogou {} e você jogou {}".format(joken, jog_joken))
    elif jog_joken == "Pedra":
        print("DERROTA! O computador jogou {} e você jogou {}".format(joken, jog_joken))

if joken == "Tesoura":
    if jog_joken == "Pedra":
        print("VITÓRIA! O computador jogou {} e você jogou {}".format(joken, jog_joken))
    elif jog_joken == "Papel":
        print("DERROTA! O computador jogou {} e você jogou {}".format(joken, jog_joken))

if joken == jog_joken:
    print("EMPATE! O computador jogou {} e você jogou {}".format(joken,jog_joken))

