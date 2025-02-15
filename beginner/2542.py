while True:
    try:
        atributos = int(input())
        cartas_m, cartas_l = [int(X) for X in input().split()]

        matriz_m = []
        matriz_l = []
        for _ in range(cartas_m):
            linha = [int(X) for X in input().split()]
            matriz_m.append(linha)

        for _ in range(cartas_l):
            linha = [int(X) for X in input().split()]
            matriz_l.append(linha)

        posicao_m, posicao_l = [int(X)-1 for X in input().split()]
        atributo = int(input()) - 1

        valor_m = matriz_m[posicao_m][atributo]
        valor_l = matriz_l[posicao_l][atributo]


        if valor_m > valor_l:
            print("Marcos")
        elif valor_l > valor_m:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError: break