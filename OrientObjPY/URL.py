url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

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













#parametro_moeda= "moedaOrigem"
#moeda_origem = url.find(parametro_moeda)
#moeda_origem = moeda_origem + len(parametro_moeda)
#parador= url.find("&")
#if parador == -1:
    #x = url[moeda_origem:]
    #print(x,"+++++")
#else:
    #x =url[moeda_origem:parador]
    #print(x,"------")

#print("Moeda origem: ",moeda_origem_final)

#parametro_destino= "moedaDestino"
#parador= url.find("&")

#Destino = url.find(parametro_destino)
#Posicao = Destino + len(parametro_destino)
#moeda_destino=url[Posicao+1:parador]

#print("Moeda destino: ",moeda_destino)



