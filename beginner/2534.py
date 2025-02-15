while True:
    try:
        N, Q = [int(X) for X in input().split()]
        N_list = [int(input()) for _ in range(N)]
        N_list.sort(reverse=True)

        for i in range(Q):
            posicao = int(input()) - 1
            print(N_list[posicao])

    except EOFError: break