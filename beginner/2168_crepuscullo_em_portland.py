N = int(input())
matriz = []
for _ in range(N+1):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(len(matriz) - 1):
    for j in range(len(matriz[i]) - 1):
        cameras = (
            matriz[i][j] +
            matriz[i][j+1] +
            matriz[i+1][j] +
            matriz[i+1][j+1]
        )
        if cameras >= 2:
            print('S', end='')  # Quadra segura
        else:
            print('U', end='')  # Quadra insegura
    print()  # Quebra de linha para a próxima linha de quadras
