class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
         self.cpf = documento
        else:
         raise ValueError("Erro de CPF")

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False