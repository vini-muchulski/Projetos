#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input("Digite a velocidade do veículo: "))

if velocidade>80:
    valor_multa= (velocidade-80)*7
    print("Você cometeu uma infração de velocidade! O valor da multa é {} R$".format(valor_multa))
else:
    print("Você está dentro do limite de velocidade")
