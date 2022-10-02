"Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: – Quantidade de notas                                                                                                                                                  – A maior nota                                                                                                                                                                – A menor nota                                                                                                                                                              – A média da turma                                                                                                                                                      – A situação (opcional)"

def notas(*nota):
    notas = list()
    total = 0
    for n in nota:
        notas.append(n)
        total += 1

    menor = sorted(notas)
    menor = menor[0]

    maior = sorted(notas, reverse=True)
    maior = maior[0]

    somatorio = 0
    for e in notas:
        somatorio +=e

    media = somatorio/total

    dicit = {"total": total, "media": media, "menor": menor, "maior": maior}
    return dicit


resp = notas(9,3,6,10,8,8,2)
print(resp)



