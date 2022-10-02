"Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"

def LeiaInt(frase):
    status = False
    while status==False:

        num = input(frase)
        if num.isnumeric():
            status = True
            print(f"O valor digitado foi {num}")
            return num
        else:
            print("\033[0;31mDigite um valor inteiro! \033[m")

v = LeiaInt("Digite um valor: ")