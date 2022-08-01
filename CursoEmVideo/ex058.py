#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random

segundo = random.randint(1,10)
tentativa = False

tentativa_total = 0

while not tentativa:
    primeiro = int(input("Digite um numero: "))

    if primeiro>segundo:
        print("ERROU!")
        print("O valor chutado é MAIOR que o número do gerado")

    if primeiro<segundo:
        print("ERROU!")
        print("O valor chutado é MENOR que o número do gerado")

    tentativa_total += 1

    if primeiro == segundo:
        print("ACERTOU!")
        print("Os valores  são iguais. Total de tentativas: {}".format(tentativa_total))
        print("FIM DE JOGO")
        tentativa = True



