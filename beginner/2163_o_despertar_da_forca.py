# Lê as dimensões da matriz
num_linhas, num_colunas = map(int, input().split())

# Lê a matriz linha por linha
matriz = [list(map(int, input().split())) for _ in range(num_linhas)]

# Inicializa a variável para indicar se encontramos o padrão
encontrado = False

# Percorre a matriz ignorando as bordas
for linha in range(1, num_linhas - 1):  # Ignora a primeira e a última linha
    for coluna in range(1, num_colunas - 1):  # Ignora a primeira e a última coluna
        # Verifica se o elemento atual é 42 e se está cercado por 7
        if (
            matriz[linha][coluna] == 42 and  # Elemento central
            matriz[linha][coluna-1:coluna+2] == [7, 42, 7] and  # Linha atual
            matriz[linha-1][coluna-1:coluna+2] == [7, 7, 7] and  # Linha acima
            matriz[linha+1][coluna-1:coluna+2] == [7, 7, 7]  # Linha abaixo
        ):
            encontrado = True
            # Exibe a posição (ajustada para 1 baseado)
            print(linha + 1, coluna + 1)
            break
    if encontrado:
        break

# Caso nenhum padrão seja encontrado, imprime "0 0"
if not encontrado:
    print("0 0")
