def criacao_conta(numero,nome, saldo,limite):

    conta = {"numero": numero, "nome": nome, "saldo":int(saldo), "limite":limite}
    return conta

def deposito(conta, valor):

    conta["saldo"] = conta["saldo"] + valor

def saldo(conta):
    print("O saldo final é {}" .format(conta["saldo"]))




