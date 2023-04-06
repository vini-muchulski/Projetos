

def verifica_se_eh_primo( numero):

    divisores = 0

    for i in range(1,numero+1):
        resultado_da_divisao = numero%i
        
        
        if( resultado_da_divisao == 0):
            
            divisores =  divisores + 1
            

    

    print("divisores = ", divisores)

    return divisores






numero = int(input("digite um numero: "))

resposta = verifica_se_eh_primo(numero)


    
