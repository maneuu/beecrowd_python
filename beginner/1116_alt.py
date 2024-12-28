def main():
    for _ in range(int(input())):
        X, Y = map(int, input().split())
        print("divisao impossivel" if Y == 0 else f"{X / Y:.1f}")

main()
