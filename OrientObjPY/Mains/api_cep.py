class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep

        else:
            raise ValueError("CEP Inválido")

    def __str__(self):
        return self.mascara_cep()

    def cep_eh_valido(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def mascara_cep(self):
        cep_formatado = "{}-{}".format(self.cep[:5],self.cep[5:8])
        cep_formatado = str(cep_formatado)
        return cep_formatado