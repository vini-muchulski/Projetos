url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#url = ""

# Verifica a URL
url = url.strip()
if url.strip() == "":
    raise ValueError("URL vazia!!")


#  Esquematiza os parametros
url_parametros = url.find("?")
base = url[:url_parametros]
parametros = url[url_parametros+1:]
print("Parametros da URL: ", parametros)

# Busca um parametro
# O Find do parador recebe um segundo valor
parametro_oo = "quantidade"
indice = url.find(parametro_oo)
posicao = indice + len(parametro_oo) + 1
parador = url.find("&", posicao)
if parador == -1:
    print(url[posicao:])

else:
    print(url[posicao: parador])
















