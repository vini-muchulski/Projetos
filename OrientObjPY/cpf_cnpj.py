from validate_docbr import CPF,CNPJ

class CpfCnpj:
    def __init__(self, documento, classe_doc):
        self.classe_doc = classe_doc
        documento = str(documento)
        if self.classe_doc == "cpf":
            if self.cpf_valido(documento):
             self.cpf = documento
            else:
             raise ValueError("Erro de CPF")

        elif self.classe_doc == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido!")
        else:
            raise ValueError("Documentos Inválidos!")


    def __str__(self):
        return self.mascara_cpf()

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            print("Cpf válido")
            validador = CPF()
            return validador.validate(cpf)

        else:

            raise ValueError("Quantidade de dígitos incompatível")

    def mascara_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def cnpj_valido(self,cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("CNPJ Inválido!")
