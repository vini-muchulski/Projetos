import re

class Extrator:
    def __init__(self,url):
        self.url = self.verifica_url(url)
        self.valida_url()

    def verifica_url(self,url):
        if type(url)== str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if self.url == "":
            raise ValueError("URL vazia!!")

        url_padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = url_padrao.match(self.url)

        if match:
            print("A URL está correta!")

        else:
            raise ValueError("Está é uma URL inválida!")

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

    def __len__(self):
        return len(self.url)

url = Extrator("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor = url.get_busca("quantidade")



