def main():
    # Entrada e ordenação dos valores
    valores = sorted(map(float, input().split()), reverse=True)
    A, B, C = valores

    # Verificação do tipo de triângulo
    if A >= (B + C):
        print("NAO FORMA TRIANGULO")
    else:
        if A**2 == B**2 + C**2:
            print("TRIANGULO RETANGULO")
        elif A**2 > B**2 + C**2:
            print("TRIANGULO OBTUSANGULO")
        else:  # A**2 < B**2 + C**2
            print("TRIANGULO ACUTANGULO")

        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")
main()