#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
salario = int(input("Olá, digite o seu salário para prosseguir com a negociação: "))
valor_imovel= int(input("Digite o valor do imóvel desejado: "))
tempo = int(input("Digite em quantos anos vc deseja financiar o imovel: "))

prestacao = valor_imovel/(tempo*12)
total_parcelas = tempo*12

if prestacao>(salario*0.3):
    print("NEGADO. Você não possui condiçoes de realizar esse empréstimo! Cada parcela mensal seria de R${:.2f}".format(prestacao ))
else:
    print("APROVADO. O empréstimo foi aprovado! Cada parcela mensal será de R${:.2f} ao longo de {} meses".format(prestacao, total_parcelas))