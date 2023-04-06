import tkinter as tk

"""processa a data futura inserida pelo usario"""
def quantos_dias_faltam():

    data = entrada_data.get()

    import time
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


    data_restante = (f"{anos_restantes} anos - {meses_restantes} meses e {dias_restantes} dias restantes")

    lb_valor_palavra_cod.config(text=data_restante)


    """
    print(f"{anos_restantes} anos - {meses_restantes} meses e {dias_restantes} dias restantes")
    print("\n-----------------------------\n")
    """



"""MAIN"""

tela = tk.Tk()
tela.title("Quantos dias faltam?")

lb_palavra = tk.Label(tela,text='Digite uma data (no formata DD/MM/YYYY):  ', font = 'Helvetica, 16')
lb_palavra.grid(row=0,column=0,pady=5,padx=5)

lb_palavra_cod = tk.Label(tela,text='Tempo restante', font = 'Helvetica, 16')
lb_palavra_cod.grid(row=0,column=1,pady=5,padx=5)

lb_valor_palavra_cod = tk.Label(tela,text='----', font = 'Helvetica, 16')
lb_valor_palavra_cod.grid(row=1,column=1,pady=5,padx=5)

entrada_data = tk.Entry(tela, relief='solid', borderwidth=2,font='Helvetica, 10')
entrada_data.grid(row=1, column=0,sticky="we",pady=5,padx=5)

botao_codificar= tk.Button(tela, text="Calcular", relief="raised", font = 'Helvetica, 16', bg='#0bf555',command=quantos_dias_faltam)
botao_codificar.grid(row=2, column=0,sticky="we",pady=5,padx=5)

tela.mainloop()





