"Escreva uma função int reverse (int n) que recebe um número inteiro e retorna um número inteiro com a ordem dos dígitos invertida."

def reverse(numero):
    numero =str(numero)
    lista_vazia = list()
    for i in range(0,len(numero)):
        lista_vazia.append(numero[i])
    
    lista_reverse = list()
    contador = 1
    for i in range(len(lista_vazia),0,-1):
        lista_reverse.append(lista_vazia[len(lista_vazia)-contador])
        contador +=1
    
    for i in range(0,len(lista_reverse)):
        print(lista_reverse[i], end="")


    

reverse(123456789)