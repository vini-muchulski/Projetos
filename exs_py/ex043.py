
lista_precos = list()
lista_itens = list()

for i in range (0,3):
    lista_itens.append(str(input(f"Digite o nome do produto {i+1}: ")))
    lista_precos.append(int(input(f"Digite o valor do item: ")))

dicionario = dict(keys = lista_itens, values = lista_precos)

for chave in dicionario.keys():
  print(f'Chave = {chave} e Valor = {dicionario[chave]}')