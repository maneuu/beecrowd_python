from math import sqrt

# Solicita ao usuário o número inteiro
n = int(input())

# Calcula o valor da sequência de Fibonacci usando a fórmula de Binet
phi = (1 + sqrt(5)) / 2  # Número de ouro (φ)
psi = (1 - sqrt(5)) / 2  # Complemento de φ
fibonacci = (phi**n - psi**n) / sqrt(5)

# Exibe o resultado formatado com uma casa decimal
print(f"{fibonacci:.1f}")
