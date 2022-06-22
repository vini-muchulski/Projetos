class ContaCorrente:

        def __init__(self, numero, nome, saldo, limite):
            print("Processo 1... {}".format(self))
            self.__numero = numero
            self.__nome = nome
            self.__saldo = saldo
            self.__limite = limite

        def extrato(self):
            print("O saldo de {} é R${}.".format(self.__nome, self.__saldo))

        def depositar(self, valor,):
            self.__saldo = self.__saldo + valor

        def sacar(self, valor,):
            if(valor>=(self.__saldo + self.__limite)):
                print(("Você não possui saldo suficiente! "))

            else:
             self.__saldo = self.__saldo - valor

        def transferir(self,valor, destino):
            self.sacar(valor)
            destino.depositar(valor)

        @property
        def get_saldo(self):
            return self.__saldo

        @property
        def get_nome(self):
            return self.__nome

        @property
        def get_limite(self):
            return self.__limite

        def set_limit(self,limite):
            self.__limite = limite

        @staticmethod
        def banco():
            return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}




