class Extrator:
    def __init__(self,url):
        self.url = self.verifica_url(url)
        self.valida_url()

    def verifica_url(self,url):
        return url.strip()

    def valida_url(self):
        if self.url.strip() == "":
            raise ValueError("URL vazia!!")

    def get_base(self):
        url_parametros = self.url.find("?")
        base = self.url[:url_parametros]
        return base

    def get_parametros(self):
        url_parametros = self.url.find("?")
        parametros = self.url[url_parametros + 1:]
        print("Parametros da URL: ", parametros)
        return parametros

    def get_busca(self, busca):
        parametro_oo = busca
        indice = self.url.find(parametro_oo)
        posicao = indice + len(parametro_oo) + 1
        parador = self.url.find("&", posicao)
        if parador == -1:
            print(self.url[posicao:])

        else:
            print(self.url[posicao: parador])

extrator = Extrator("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
