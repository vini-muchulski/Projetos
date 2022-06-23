nome = input("Digite seu nome completo: ").strip()
print("Analisando...")

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
contagem = len(nome) - (nome.count(" "))

prim_nome = nome.split()
cont_prim = len(nome.split()[0])

print(prim_nome)


print("""Seu nome completo em maiusculas é {} 
Seu nome completo em minusculas é {}
Seu nome possui {} letras
Seu primeiro nome é {} e possui {} letras""".format(nome_maiusculo, nome_minusculo, contagem, prim_nome[0], cont_prim))