A, B, C = [int(n) for n in input().split()]

condicoes = [
    A + B > C,
    A + C > B,
    B + C > A
]

if all(condicoes):
    maior_lado = max(A, B, C)
    retangulo = 'S' if (
        (maior_lado == A and B ** 2 + C ** 2 == A ** 2) or
        (maior_lado == B and A ** 2 + C ** 2 == B ** 2) or
        (maior_lado == C and A ** 2 + B ** 2 == C ** 2)
    ) else 'N'

    match (A == B, B == C, A == C):
        case (True, True, True):
            print("Valido-Equilatero")
        case (False, False, False):
            print("Valido-Escaleno")
        case _:
            print("Valido-Isoceles")
    print(f"Retangulo: {retangulo}")
else:
    print("Invalido")