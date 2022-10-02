"Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: – Quantidade de notas                                                                                                                                                  – A maior nota                                                                                                                                                                – A menor nota                                                                                                                                                              – A média da turma                                                                                                                                                      – A situação (opcional)"

def notas(*nota):
    notas = list()

    for n in nota:
        notas.append(n)

    menor = sorted(notas)
    menor = menor[0]

    maior = sorted(notas, reverse=True)
    maior = maior[0]

    somatorio = 0
    for e in notas:
        somatorio +=e

    media = somatorio/len(notas)

    dicit = {"total": len(notas), "media": media, "menor": menor, "maior": maior}
    return dicit

resp = notas(9,3,6,10,8,8,2)
print(resp)



