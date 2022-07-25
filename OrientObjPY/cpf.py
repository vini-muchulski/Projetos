from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
         self.cpf = documento
        else:
         raise ValueError("Erro de CPF")

    def __str__(self):
        return self.mascara_cpf()

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:

            raise ValueError("Quantidade de dígitos incompatível")

    def mascara_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)