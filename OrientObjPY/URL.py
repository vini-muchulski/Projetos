url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

p = url.find("?")
print(p)

base = url[:p]
print(base) 

parametros = url[p+1:]
print("Parametros da URL: ", parametros)

parametro_moeda= "moedaOrigem"
moeda_origem = url.find(parametro_moeda)
moeda_origem = moeda_origem + len(parametro_moeda)
moeda_origem_final = url[moeda_origem+1:]
print("Moeda origem: ",moeda_origem_final)

parametro_destino= "moedaDestino"
parador= url.find("&")

Destino = url.find(parametro_destino)
Posicao = Destino + len(parametro_destino)
moeda_destino=url[Posicao+1:parador]

print("Moeda destino: ",moeda_destino)



