while True:
    N = int(input())
    if N == -1:
        break
    print(N - 1 if N > 0 else 0)
