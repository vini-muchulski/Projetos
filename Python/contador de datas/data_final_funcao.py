import time


"""processa a data futura inserida pelo usario"""
def quantos_dias_faltam(data):
    """tratamento de dados"""
    data.strip()
    if (len(data) != 10):
        raise ValueError("Os valores digitados estao incorretos")

    data_dia = int(data[0:2])

    data_mes = int(data[3:5])

    data_ano = int(data[6:])


    print("\n-----------------------------\n")
    print(f"Data inserida {data_dia}/{data_mes}/{data_ano}")
    print("\n-----------------------------\n")



    """pega a data atual"""

    ano_atual = int(time.strftime("%Y"))
    dia_atual = int(time.strftime("%d"))
    mes_atual = int(time.strftime("%m"))


    """calcula a diferenca de tempos"""
    anos_restantes = abs(data_ano - ano_atual)
    meses_restantes = abs(data_mes - mes_atual)
    dias_restantes = abs(data_dia - dia_atual)

    """verifica se existe a ocorrencia de anos bissextos nesse intervalo de tempo"""

    if(data_ano > ano_atual):
        for ano in range(ano_atual,data_ano+1):
            if (ano%4 == 0 and  (ano % 100 != 0 or ano % 400 == 0)):
                dias_restantes +=1

    if(data_ano < ano_atual):
        for ano in range(ano_atual,data_ano-1,-1):
            if (ano%4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
                dias_restantes -=1



    print(f"{anos_restantes} anos - {meses_restantes} meses e {dias_restantes} dias restantes")
    print("\n-----------------------------\n")




"""MAIN"""
data_informada = str(input("Digite uma data (no formata DD/MM/YYYY):  "))

quantos_dias_faltam(data_informada)





