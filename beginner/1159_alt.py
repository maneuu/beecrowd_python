def main():
    while True:
        X = int(input())
        if X == 0:
            break

        if X % 2 != 0:
            X += 1
        soma = sum(X + 2 * i for i in range(5))
        print(soma)

main()
