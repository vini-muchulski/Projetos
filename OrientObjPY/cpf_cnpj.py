from validate_docbr import CPF,CNPJ

class CpfCnpj:
    def __init__(self, documento, classe_doc):
        self.classe_doc = classe_doc #variavel que serve como esquema para determinar qual tipo de documento será usado
        documento = str(documento)
        if self.classe_doc == "cpf":
            if self.cpf_valido(documento):
             self.cpf = documento #defindo a variavel do documento
            else:
             raise ValueError("Erro de CPF")

        elif self.classe_doc == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento #defindo a variavel do documento
            else:
                raise ValueError("CNPJ Inválido!")
        else:
            raise ValueError("Documentos Inválidos!")

    def __str__(self):
        if self.classe_doc == "cpf":
            return self.mascara_cpf()

        elif self.classe_doc == "cnpj":
            return self.mascara_cnpj()





    def cpf_valido(self, cpf): #validacao pelo numero de caracteres
        if len(cpf) == 11:
            print("Cpf válido")
            validador = CPF()
            return validador.validate(cpf)
        else:

            raise ValueError("Quantidade de dígitos incompatível")

    def mascara_cpf(self): #formata o documento, no caso o CPF
        mascara = CPF()
        return mascara.mask(self.cpf)




    def cnpj_valido(self,cnpj): #validacao pelo numero de caracteres
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("CNPJ Inválido!")

    def mascara_cnpj(self): #formata o documento, no caso o CNPJ
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)
