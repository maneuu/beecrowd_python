while True:
    try:
        N, M = [int(n) for n in input().split()]
        matriz = []
        for i in range(N):
            linha = [int(n) for n in input().split()]
            matriz.append(linha)


        for i in range(N):
            if 2 in matriz[i]:
                pokemon_y = i + 1
                pokemon_x = matriz[i].index(2) + 1
            if 1 in matriz[i]:
                meu_y = i + 1
                meu_x = matriz[i].index(1) + 1

        # Cálculo da distância de Manhattan 
        # D = |x1 - x2| + |y1 - y2|
        distancia = abs(meu_x - pokemon_x) + abs(meu_y - pokemon_y)
        print(distancia)
    except EOFError: break