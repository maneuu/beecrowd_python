def main():
    numeros = [float(input()) for _ in range(6)]
    positivos = [n for n in numeros if n > 0]
    print(f"{len(positivos)} valores positivos")
    print(f"{sum(positivos) / len(positivos):.1f}")

main()
