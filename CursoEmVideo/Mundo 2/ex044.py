preco= float(input("Qual o valor das compras? R$ "))
opcao= int(input("""
[ 1 ] – à vista dinheiro/cheque: 10% de desconto
[ 2 ] – à vista no cartão: 5% de desconto
[ 3 ] – em até 2x no cartão: preço formal 
[ 4 ] – 3x ou mais no cartão: 20% de juros

Digite a forma de pagamento: """))

if opcao ==1:
    valor = preco*0.9
    print("O valor final foi R$ {:.2f}".format(valor))


elif opcao ==2:
    valor = preco*0.95
    print("O valor final foi R$ {:.2f}".format(valor))

elif opcao ==3:
    valor = preco
    print("O valor final foi R$ {:.2f}".format(valor))

elif opcao ==4:
    parcelas = int(input("Quantas parcelas? "))
    valor = preco*1.2
    valor_parcela = valor/parcelas
    print("O valor final foi R$ {:.2f} com {} parcelas de R$ {:.2f}".format(valor,parcelas, valor_parcela))

else:
    print("OPÇÃO INVÁLIDA. Tente novamente")