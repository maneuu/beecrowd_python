def main():
    while True:
        x, y = map(int, input().split())
        if x == y:
            break
        if x < y:
            print("Crescente")
        else:
            print("Decrescente")

main()
