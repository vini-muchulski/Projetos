# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


cont = 0
somatorio = 0

while True:
    numb = int(input("Digite um número [999 para finalizar]: "))
    if numb == 999:
        break
    somatorio += numb
    cont+=1

print(f"O somátório foi {somatorio} e o total de números gerados foi {cont}")

