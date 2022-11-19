from datetime import date

ano_atual = date.today().year

inss = {}

inss["Nome"] = str(input("Nome do trabalhador: "))
inss["Idade"] = ano_atual - int(input("Digite o ano de nascimento: "))

inss["Numero"] = int(input("Carteira de Trabalho(0 não tem) = "))

if(inss["Numero"] != 0):
    inss["Ano de Contratacao"] = int(input("Ano de contratacao: "))
    inss["Salário"] = int(input("Salário = "))

for key,valor in inss.items():
    print(f"{key} = {valor}")
