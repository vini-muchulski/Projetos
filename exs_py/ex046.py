cadastro = dict()
lista_cadastros = list()

qnt_pessoas = int(input("Digite o numero de pessoas que deseja cadastrar: "))

for i in range(0,qnt_pessoas):
    cadastro["nome"] = str(input("Digite seu nome: "))
    cadastro["idade"] = int(input("Idade: "))
    cadastro["pais"] = str(input("Seu pais de origem: "))
    cadastro["estado civil"] = str(input("Estado civil "))

    lista_cadastros.append(cadastro.copy())

print(cadastro)
print(lista_cadastros)