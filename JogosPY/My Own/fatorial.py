#Codigo com a função de calcular o fatorial de um input inteiro

numero = int(input("Digite o valor do numero: "))
fatorial = numero
b = numero-1

while True:
     print("------", fatorial)

     if b==0:
          break

     fatorial = fatorial * b
     b -= 1


print(fatorial)















