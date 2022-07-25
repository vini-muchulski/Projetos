class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
         self.cpf = documento
        else:
         raise ValueError("Erro de CPF")
    def __str__(self):
        return self.mascara_cpf()

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def mascara_cpf(self):
        fatia_cpf1 = self.cpf[:3]
        fatia_cpf2 = self.cpf[3:6]
        fatia_cpf3 = self.cpf[6:9]
        fatia_cpf4 = self.cpf[9:]

        return( "{}.{}.{}-{}".format(
            fatia_cpf1,
            fatia_cpf2,
            fatia_cpf3,
            fatia_cpf4))