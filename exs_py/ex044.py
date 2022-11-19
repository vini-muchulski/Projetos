



dicionario = dict()

for i in range (0,3):
    x = (str(input(f"Digite o nome do produto {i+1}: ")))
    dicionario[f"{x}"] = (int(input(f"Digite o valor do item: ")))

print(dicionario)

