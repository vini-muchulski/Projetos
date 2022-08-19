#Codigo com a função de calcular o fatorial de um input inteiro

numero = int(input("Digite o valor do numero: "))
fatorial = numero


while True:


     print("------", numero)

     b = numero-1
     if b==0:
          break

     fatorial = fatorial * b

     numero -= 1



print(fatorial)















