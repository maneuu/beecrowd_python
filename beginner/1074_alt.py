def main():
    repeticoes = int(input())
    for _ in range(repeticoes):
        num = int(input())
        if num == 0:
            print("NULL")
        else:
            tipo = "EVEN" if num % 2 == 0 else "ODD"
            positivo_negativo = "POSITIVE" if num > 0 else "NEGATIVE"
            print(f"{tipo} {positivo_negativo}")

main()
