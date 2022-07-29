from datetime import datetime, timedelta

class Dia:
    def __init__(self):
        self.dia_cadastro = datetime.today()
        self.momento_do_cadastro = (self.dia_cadastro.strftime("%d/%m/%Y %H:%M"))

    def __str__(self):
        return self.momento_do_cadastro

    def mes_cadastro(self):
        meses = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.dia_cadastro.month
        return meses[mes_cadastro-1]


    def semana_dia (self):
        semana_dia_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        semana_dia = self.dia_cadastro.weekday()
        return semana_dia_lista[semana_dia]

    def tempo_de_cadastro(self):
        tempo_de_cadastro = datetime.today() - self.dia_cadastro
        return tempo_de_cadastro