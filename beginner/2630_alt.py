for i in range(int(input())):
    conversao = input()  # min / max / mean / eye
    valores_rgb = [int(X) for X in input().split()]

    operacoes = {
        "max": max(valores_rgb),
        "min": min(valores_rgb),
        "mean": int(sum(valores_rgb) / 3),
        "eye": int(valores_rgb[0] * 0.3 + valores_rgb[1] * 0.59 + valores_rgb[2] * 0.11)
    }

    print(f"Caso #{i+1}: {operacoes[conversao]}")
