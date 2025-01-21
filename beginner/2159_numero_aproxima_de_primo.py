from math import log

# Entrada do usuário
n = int(input())

# Cálculo do valor mínimo (P) e máximo (M)
P = n / log(n)
M = 1.25506 * (n / log(n))

# Exibição dos resultados com uma casa decimal
print(f'{P:.1f} {M:.1f}')

# GPT