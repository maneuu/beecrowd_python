def main():
    while True:
        X, Y = map(int, input().split())
        if X == 0 or Y == 0:
            break
        quadrantes = {(1, 1): "primeiro", (1, -1): "quarto", (-1, 1): "segundo", (-1, -1): "terceiro"}
        print(quadrantes[(1 if X > 0 else -1, 1 if Y > 0 else -1)])

main()
