def main():
    while True:
        X = int(input())
        if X == 0:
            break

        if X % 2 != 0:
            X += 1
        soma = 0
        for _ in range(5):
            soma += X
            X += 2
        print(soma)

main()