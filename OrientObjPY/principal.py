
#from validate_docbr import CPF, CNPJ
from cpf_cnpj import CpfCnpj
#pff = Cpf("01234567890")
#print(cpff)

cnpj_ex = "86754794000102"

#cnpj = CNPJ()
#print(cnpj.validate(cnpj_ex))


documento = CpfCnpj(cnpj_ex,"cnpj")
validate_docbr.documento(cnpj_ex)








