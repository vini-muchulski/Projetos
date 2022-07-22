from cpf import Cpf
#cpf = str(input('Digite um CPF'))
cpf = "25634614627"

fatia_cpf1 = cpf[:3]
fatia_cpf2 = cpf[3:6]
fatia_cpf3 = cpf[6:9]
fatia_cpf4 = cpf[9:]

print(fatia_cpf4)
objeto_cpf = Cpf(cpf)