def main():
    while True:
        X, Y = [int(num) for num in input().split()]
        if X == 0 or Y == 0:
            break
        if X > 0:
            if Y > 0:
                print("primeiro")
            elif Y < 0:
                print("quarto")

        elif X < 0:
            if Y > 0:
                print("segundo")
            elif Y < 0:
                print("terceiro")
main()