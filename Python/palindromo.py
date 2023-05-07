''' codigo para verificar se uma dada palavra é um palindromo '''

palavra = "RADAR"

tamanho = len(palavra)

string_reversa = ""

for i in range(0,tamanho):
  tamanho_reverso = tamanho - 1 - i
  
  string_reversa += palavra[tamanho_reverso]


print(string_reversa)

if (string_reversa == palavra):
  print(f"A palavra '{palavra}' é um palindromo!")

else:
  print(f"A palavra '{palavra}' NÃO é um palindromo!")