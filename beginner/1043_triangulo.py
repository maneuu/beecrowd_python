"""Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

"""
def main():
    A, B, C = map(float,input().split())

    # A soma de dois lados deve ser maior que o terceiro lado para todas as combinações. Caso seja um triângulo.

    if A + B > C and A + C > B and B + C > A: #Não é triângulo
        print(f"Perimetro = {A + B + C:.1f}")
        
    else: # É triângulo
        print(f"Area = {((A + B) * C) / 2:.1f}")

main()