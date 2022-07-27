import re

class Telefone:
    def __init__(self,numero):
        self.numero = numero

    def valida_numero(self,numero):
        padrao = "[0-9]{2}9[0-9]{4,5}[0-9]{4}"
        busca = re.search(padrao, numero)
        busca_len = len(busca.group())

        if busca_len == 11:
            return self.numero
        else:
            raise ValueError("Número inválido")
