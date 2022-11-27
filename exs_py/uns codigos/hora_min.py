def  hora_para_segundos( horas,minutos,segundos):
    hora_SEC = horas *60 * 60
    minutos_SEC = minutos * 60

    segundos_SEC = segundos + minutos_SEC + hora_SEC
    return segundos_SEC

print(" Total de segundos = {}".format(hora_para_segundos(1,0,0)))