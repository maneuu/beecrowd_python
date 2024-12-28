def main():
    while True:
        valores = sorted(map(int, input().split()))
        if valores[0] <= 0:
            break
        soma = sum(range(valores[0], valores[1] + 1))
        print(*range(valores[0], valores[1] + 1), f"Sum={soma}")

main()
