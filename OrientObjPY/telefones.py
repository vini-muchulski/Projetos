import re

class Telefone:
    def __init__(self,numero):
        if self.valida_numero(numero):
            self.numero = numero


        else:
            raise ValueError("Número inválido")

    def valida_numero(self, numero):
        padrao = "([0-9]{2,3})?([0-9]{2})9([0-9]{4,5})([0-9]{4})"
        busca = re.search(padrao, numero)
        dd_int = busca.group(1)

        if busca:
            return True
        else:
            return False

    def formata_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})(9[0-9]{4,5})([0-9]{4})"
        busca = re.search(padrao, self.numero)

        dd_int = "+{} ({}) {}-{}".format(busca.group(1),busca.group(2),busca.group(3),busca.group(4))
        print(dd_int)


