from datetime import datetime, timedelta

class Dia:
    def __init__(self):
        self.dia_cadastro = datetime.today()
        self.dia_cadastro = str(self.dia_cadastro)


    def __str__(self):
        return self.dia_cadastro