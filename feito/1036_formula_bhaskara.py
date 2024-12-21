'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
'''

valores = input().split()
A, B, C = float(valores[0]), float(valores[1]), float(valores[2])

delta = B**2 - (4 * A * C)
divisao = 2 * A
from math import sqrt
if delta < 0 or divisao == 0:
    print("Impossivel calcular")
else:
# poderia obter a raiz quadrado usando potenciação com ** 0.5
# ex: raiz = 16 ** 0.5  # Resultado: 4.0
    x1 = (-B + sqrt(delta)) / (2 * A)
    x2 = (-B - sqrt(delta)) / (2 * A)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
