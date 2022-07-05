class ContaCorrente:
    def __init__(self,nome, codigo, saldo):
        self.nome = nome
        self.codigo = codigo
        self.saldo = saldo

    def deposita(self,valor):
        self.saldo += valor
        print(self.saldo)

    def __str__(self):
        return "[Código: {} - Saldo: {}]".format(self.codigo,self.saldo)

