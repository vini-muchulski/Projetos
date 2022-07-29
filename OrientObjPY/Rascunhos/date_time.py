import time
from datetime import datetime, timedelta
from datas_br import Dia

#print(datetime.today())

cadastro = Dia()

print(cadastro.mes_cadastro())
print(cadastro.semana_dia())

time.sleep(2)
cadastro = Dia()
print(cadastro)

print(cadastro.tempo_de_cadastro())


#hoje = datetime.today()
#hoje_format = hoje.strftime("%d/%m/%Y %H:%M")
#print(hoje_format)
'''
hoje = datetime.today()
time.sleep(2)

amanha = datetime.today() + timedelta(days=2)

print(amanha - hoje)'''