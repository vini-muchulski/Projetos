#Codigo com a função de calcular o fatorial de um input inteiro

numero = int(input("Digite o valor do numero: "))
fatorial = numero
restou = 0

while True:
     if  numero >1:
          print("------", numero)
          numero -=1
          fatorial = fatorial * (numero)
          restou = fatorial

     if numero == 1:
          break

print(restou)















