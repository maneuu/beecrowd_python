for i in range(int(input())):
    conversao = input() # min / max / mean / eye 0,3 0,59 0,11
    valores_rgb = [int(X) for X in input().split()]
    if conversao == "max":
        print(f"Caso #{i+1}: {max(valores_rgb)}")
    elif conversao == "min":
        print(f"Caso #{i+1}: {min(valores_rgb)}")
    elif conversao == "mean":
        print(f"Caso #{i+1}: {int(sum(valores_rgb)/3)}")
    elif conversao == "eye":
        resultado = int(valores_rgb[0] * 0.3 + valores_rgb[1] * 0.59 + valores_rgb[2] * 0.11)
        print(f"Caso #{i+ 1}: {resultado}")