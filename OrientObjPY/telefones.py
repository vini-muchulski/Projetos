import re

class Telefone:
    def __init__(self,numero):
        if self.valida_numero(numero):
            self.numero = numero
            print(numero)

        else:
            raise ValueError("Número inválido")

    def valida_numero(self, numero):
        padrao = "[0-9]{2,3}[0-9]{2}9[0-9]{4,5}[0-9]{4}"
        busca = re.findall(padrao, numero)

        if busca:
            return True
        else:
            return False

