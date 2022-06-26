from datetime import datetime
from datetime import date

data_atual = date.today()
data_atual = data_atual.strftime('%d/%m/%Y')
print("Dia {}".format(data_atual))

date_hora= datetime.now()
date_hora= date_hora.strftime('%H:%M')

print(date_hora)
