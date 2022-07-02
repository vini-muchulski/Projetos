url = "bytebank.com/cambio?quantidade=220&moedaOrigem=dolar&moedaDestino=real"
#url = ""

# Verifica a URL
url = url.strip()
if url.strip() == "":
    raise ValueError("URL vazia!!")



#  Esquematiza os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

# Busca um parametro
# O Find do parador recebe um segundo valor
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor_quantidade = int(url_parametros[indice_valor:])
else:
    valor_quantidade = int(url_parametros[indice_valor:indice_e_comercial])
print(valor_quantidade)


#-----------------------------------------
origem = "moedaOrigem"
indice = url.find(origem)
posicao = indice + len(origem) + 1
parador = url.find("&", posicao)
if parador == -1:
    moeda_origem = url[posicao:]
    print(moeda_origem)

else:
    moeda_origem= url[posicao: parador]
    print(moeda_origem)

#--------------------------------------------
destino = "moedaDestino"
indice = url.find(destino)
posicao = indice + len(destino) + 1
parador = url.find("&", posicao)
if parador == -1:
    moeda_destino = url[posicao:]
    print(moeda_destino)

else:
    moeda_destino= url[posicao: parador]
    print(moeda_destino)





if moeda_origem == "real" and moeda_destino == "dolar":
    valor = valor_quantidade / 5.5
    print("Você possui R${:.2f}".format(valor))
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor = valor_quantidade * 5.5
    print("Você possui R${:.2f}".format(valor))
else:
    print("Câmbio de {} para {} não está disponível.".format(moeda_origem.title(),moeda_destino.title()))





