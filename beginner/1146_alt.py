def main():
    while True:
        X = int(input())
        if X == 0:
            break
        print(" ".join(str(num) for num in range(1, X + 1)))

main()
