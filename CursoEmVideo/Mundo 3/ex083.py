#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite o valor da expressão:"))
lista = []

for carc in expressao:
    if carc =="(":
        lista.append("(")
    if carc ==")":
        if len(lista)>0:
            lista.pop() #pop remove o ultimo elemento de uma lista
        else:
            lista.append(")")
            break


if len(lista)== 0:
    print("Expressão VÁLIDA!")

else:
    print("Expressão INVÁLIDA!")