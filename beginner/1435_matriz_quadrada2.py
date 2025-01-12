def main():
    while True:
        ordem_matriz = int(input())
        if ordem_matriz == 0:
            break

        # Construção da matriz
        matriz = []
        for i in range(ordem_matriz):
            linha = []
            for j in range(ordem_matriz):
                valor = abs(i - j) + 1  # Cálculo do valor com base na diferença dos índices
                linha.append(valor)
            matriz.append(linha)

        # Impressão da matriz formatada
        for linha in matriz:
            print(" ".join(f"{x:>3}" for x in linha))
        print()  # Linha em branco entre matrizes

main()
