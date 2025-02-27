while True:
    try:
        linhas, colunas = map(int, input().split())
        matriz = [list(map(int, input().split())) for _ in range(linhas)]

        for i in range(linhas):
            resultado = ""
            for j in range(colunas):
                if matriz[i][j] == 1:
                    resultado += "9"
                else:
                    soma = 0
                    if j - 1 >= 0 and matriz[i][j - 1] == 1:  # Esquerda
                        soma += 1
                    if j + 1 < colunas and matriz[i][j + 1] == 1:  # Direita
                        soma += 1
                    if i - 1 >= 0 and matriz[i - 1][j] == 1:  # Cima
                        soma += 1
                    if i + 1 < linhas and matriz[i + 1][j] == 1:  # Baixo
                        soma += 1
                    resultado += str(soma)
            print(resultado)

    except EOFError:
        break
