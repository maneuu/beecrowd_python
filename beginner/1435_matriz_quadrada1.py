def main():
    while True:
        ordem_matriz = int(input())
        if ordem_matriz == 0:
            break

        matriz = []
        for i in range(ordem_matriz):
            linha = []
            for j in range(ordem_matriz):
                valor = min(i, j, ordem_matriz - 1 - i, ordem_matriz - 1 - j) + 1
                linha.append(valor)
            matriz.append(linha)

        # Imprime a matriz formatada
        for linha in matriz:
            print(" ".join(f"{x:>3}" for x in linha))
        print()  # Linha em branco após cada matriz

main()
# Codigo feito 50% pelo GPT