n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

opcao = 0
while opcao !=5:
    print("""
    
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    
    """)

    opcao = int(input("Qual opção deseja? "))
    if opcao == 1:
        s = n1+n2
        print(s)

    if opcao == 2:
        s = n1*n2
        print(s)

    if opcao == 3:
        if n1>n2:
            print("O primeiro valor é o maior")

        if n1<n2:
            print("O segundo valor é o maior")

        else:
            print("Os valores são iguais")

    if opcao == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))




