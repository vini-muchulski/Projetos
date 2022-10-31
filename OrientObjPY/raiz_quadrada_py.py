"calcula uma raiz dado um indice e valor"

raiz = float(input("Digite um numero real: "))
indice = float(input("Digite um numero real: "))

def raiz_quadrada(raiz,indice):
  xis = raiz**(1/indice)
  return xis


yplison = raiz_quadrada(raiz,indice)
print("Raiz =", yplison)


