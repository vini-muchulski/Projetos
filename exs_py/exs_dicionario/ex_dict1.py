
inicio = int(input("------ 1 para iniciar - 0 para break ------ \n"))
lista = []
while (inicio !=0):

    nome = str(input("Digite o nome do aluno - 0 para break: "))

    if(nome == "0"):
        break

    media = float(input("Digite a media do aluno "))

    if (media>=7):
        status = "Aprovado"

    else: 
        status = "Reprovado"
    if (nome != "0"):
        dicionario = dict(aluno=nome,nota_final = media, status =status )
        lista.append(dicionario)

    else:
        break

print(lista)


