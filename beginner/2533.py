while True:
    try:
        M = int(input())
        somatorio_numerador = 0
        somatorio_denominador = 0
        for i in range(M):
            N,C = [int(X) for X in input().split()]
            somatorio_numerador += N * C
            somatorio_denominador += C
        resultado = somatorio_numerador/ (somatorio_denominador * 100)
        print(f"{resultado:.4f}")
    except EOFError: break