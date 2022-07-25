
#from validate_docbr import CPF, CNPJ
from cpf_cnpj import CpfCnpj
#pff = Cpf("01234567890")
#print(cpff)

cnpj_ex = "86754794000102"
cpf_ex = "80924689072"

#cnpj = CNPJ()
#print(cnpj.validate(cnpj_ex))


documento = CpfCnpj(cpf_ex,"cpf")
print(documento)








