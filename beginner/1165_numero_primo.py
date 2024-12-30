def main():
    num_casos = int(input())

    for _ in range(num_casos):
        numero = int(input())
        divisores = 0

        for num in range(1, numero + 1):
            if numero % num == 0:
                divisores += 1

        if divisores == 2:
            print(f"{numero} eh primo")
        else:
            print(f"{numero} nao eh primo")

main()
