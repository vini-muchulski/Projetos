url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

p = url.find("?")
print(p)

base = url[:p]
print(base)

parametros = url[p+1:]
print(parametros)
