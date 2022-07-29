from validate_docbr import CPF,CNPJ

class Doc: #factory

    @staticmethod
    def cria_doc(doc):
        if len(doc) == 11:
            return Cpf_doc(doc)

        elif len(doc) == 14:
            return Cnpj_doc(doc)

        else:
            raise ValueError("Quantidade de dígitos inválida")



class Cpf_doc:
    def __init__(self,doc):
        if self.cpf_valido(doc):
            self.cpf = doc  # defindo a variavel do documento
        else:
            raise ValueError("Erro de CPF")


    def cpf_valido(self, doc):  # validacao pelo numero de caracteres
        print("Cpf válido")
        validador = CPF()
        return validador.validate(doc)

    def mascara_cpf(self): #formata o documento, no caso o CPF
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.mascara_cpf()



class Cnpj_doc:
    def __init__(self,doc):
        if self.cnpj_valido(doc):
            self.doc = doc

        else:
            raise ValueError("Erro de CNPJ")

    def cnpj_valido(self,doc): #validacao pelo numero de caracteres
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(doc)

    def mascara_cnpj(self): #formata o documento, no caso o CNPJ
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.doc)

    def __str__(self):
        return self.mascara_cnpj()
















