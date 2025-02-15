A,B,C = [int(n) for n in input().split()]

condicoes = [
    A + B > C,
    A + C > B,
    B + C > A
]

if all(condicoes):
    retangulo =f"Retangulo: {'s' if (A ** 2 + B ** 2 == C ** 2) else 'N'}"

    equilatero = A ==  B == C
    isoceles = A == B or C == A or B == C
    escaleno = A != B and B != C and A != C
    if equilatero:
        print("Valido-Equilatero")
        print(retangulo)
    elif isoceles:
        print("Valido-Isoceles")
        print(retangulo)
    elif escaleno:
        print("Valido-Escaleno")
        print(retangulo)
else:
    print("Invalido")