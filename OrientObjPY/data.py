
class Data:
    def __init__(self, dia, mes , ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano

    def exibir_data(self):
        print("A data é {}/{}/{}" .format(self.dia,self.mes,self.ano))
