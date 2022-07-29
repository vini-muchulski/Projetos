import re

#formato = "dd9nnnnwwww"

numero = "51936715223"
padrao = "[0-9]{2}9[0-9]{4,5}[0-9]{4}"

busca = re.findall(padrao, numero)
busca_scr = re.search(padrao, numero)


print(busca)
print(len(busca_scr.group()))