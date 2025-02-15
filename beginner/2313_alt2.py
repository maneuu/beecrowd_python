def eh_triangulo_valido(A, B, C):
    return A + B > C and A + C > B and B + C > A

def tipo_triangulo(A, B, C):
    if A == B == C:
        return "Valido-Equilatero"
    elif A == B or B == C or A == C:
        return "Valido-Isoceles"
    else:
        return "Valido-Escaleno"

def verifica_retangulo(A, B, C):
    maior_lado = max(A, B, C)
    if maior_lado == A:
        return 'S' if (B ** 2 + C ** 2 == A ** 2) else 'N'
    elif maior_lado == B:
        return 'S' if (A ** 2 + C ** 2 == B ** 2) else 'N'
    else:
        return 'S' if (A ** 2 + B ** 2 == C ** 2) else 'N'

A, B, C = [int(n) for n in input().split()]

if eh_triangulo_valido(A, B, C):
    tipo = tipo_triangulo(A, B, C)
    retangulo = f"Retangulo: {verifica_retangulo(A, B, C)}"
    print(tipo)
    print(retangulo)
else:
    print("Invalido")