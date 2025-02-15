while True:
    try:
        linhas, colunas = [int(X) for X in input().split()]
        matriz = []
        
        for _ in range(linhas):
            linha = [int(X) for X in input().split()]
            matriz.append(linha)
        for i in range(linhas):
            resultado = ""
            for j in range(colunas):
                if matriz[i][j] == 1:
                    resultado += "1"
                else:

                    if matriz[i][j+1] or 
    except EOFError:break