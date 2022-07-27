import re

padrao = "\w{1,50}@[a-z]{3,10}.[a-z]{1,3}"
email = "paripapah vinidias@gmail.com"
busca = re.search(padrao, email)

print(busca.group())
