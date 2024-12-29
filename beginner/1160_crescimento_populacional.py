def main():
    num_casos = int(input())

    for _ in range(num_casos):
        populacao_a, populacao_b, crescimento_a, crescimento_b = [float(num) for num in input().split()]
        populacao_a = int(populacao_a)
        populacao_b = int(populacao_b)

        anos = 0
        while populacao_a <= populacao_b:
            populacao_a += int(populacao_a * (crescimento_a / 100))
            populacao_b += int(populacao_b * (crescimento_b / 100))
            anos += 1

            if anos > 100:
                print("Mais de 1 seculo.")
                break

        if anos <= 100:
            print(f"{anos} anos.")

main()