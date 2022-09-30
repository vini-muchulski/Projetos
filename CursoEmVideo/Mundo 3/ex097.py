"Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.   "


def escreva(letras):
     tamanho = len(letras)+4

     print(tamanho*"=")
     print(f"  {frase}  " )
     print(tamanho * "=")

frase = str(input("Digite a frase: "))


escreva(frase)