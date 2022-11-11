aluno = {}
aluno["Nome"] = str(input("Digite o nome do aluno: "))
aluno["media"] = float(input("Media do aluno: "))

if (aluno["media"]>7):
    aluno["status"] = "Aprovado"
else:
    aluno["status"] = "Reprovado"

print(aluno) 