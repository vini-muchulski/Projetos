"Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."

def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    status = ["VOTO OBRIGATÓRIO","OPCIONAL","NÃO VOTA"]

    if 65>idade>=18:
        print(f"Idade: {idade}  Voto: {status[0]}")

    elif 18>idade>=16 or idade>65:
        print(f"Idade: {idade}  Voto: {status[1]}")

    else:
        print(f"Idade: {idade}  Voto: {status[2]}")

ano = int(input("Digite seu ano de nascimento: "))

(voto(ano))
