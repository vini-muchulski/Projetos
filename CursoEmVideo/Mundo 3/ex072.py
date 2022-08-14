#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ("Zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    digito = int(input("Digite um valor entre 0 e 20: "))
    if digito in range( 0, len(tupla)):
        print("Você digitou", tupla[digito].title())
        break

    else:
        print("Erro!", end=" ")



