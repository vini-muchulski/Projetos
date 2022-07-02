import re

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"


url_padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = url_padrao.match(url)

if match:
    print("A URL está correta!")

else:
    raise ValueError("Está é uma URL inválida!")