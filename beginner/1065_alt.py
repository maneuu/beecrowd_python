def main():
    pares = sum(1 for _ in range(5) if int(input()) % 2 == 0)
    print(f"{pares} valores pares")

main()
