
#from validate_docbr import CPF, CNPJ
#from cpf_cnpj import Doc
""" #pff = Cpf("01234567890")
#print(cpff)

cnpj_ex = "86754794000102"
cpf_ex = "80924689072"

#cnpj = CNPJ()
#print(cnpj.validate(cnpj_ex))


documento = Doc.cria_doc(cnpj_ex)
print(documento) """

from api_cep import BuscaEndereco

cep = 86754294

obj_cep = BuscaEndereco(cep)

print(obj_cep)












