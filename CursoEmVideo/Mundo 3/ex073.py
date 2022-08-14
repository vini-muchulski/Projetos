tupla = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print(f"Os 5 primeiros colocados foram {tupla[:5]}")
print("--------------------------------")
print(f"Os últimos 4 colocados foram {tupla[-4:]}")
print("--------------------------------")
print("Times em ordem alfabética:", sorted(tupla))
print("--------------------------------")
print(f"A internacional está em {tupla.index('Internacional')+1}° lugar")
