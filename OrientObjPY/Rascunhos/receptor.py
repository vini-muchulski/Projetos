from cpf_cnpj import Doc

valor_input = str(input("Digite o seu CPF: "))

cpf = Doc.cria_doc(valor_input)
print(cpf)