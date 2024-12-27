def main():
    valores = [float(input()) for _ in range(6)]
    positivos = sum(1 for valor in valores if valor > 0)
    print(f"{positivos} valores positivos")

main()
