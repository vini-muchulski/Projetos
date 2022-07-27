import re

padrao = "[0-9][a-z][0-9]"
texto = "avkdbw 2v7"

busca = re.search(padrao,texto)

print(busca)
print(busca.group())