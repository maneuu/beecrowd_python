def main():
    tipo_operacao = input()
    matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

    soma = 0
    contador = 0
    col_inicio = 12

    for linha in range(12):
        for coluna in range(col_inicio, 12):
            soma += matriz[linha][coluna]
            contador += 1

        if linha < 5:
            col_inicio -= 1  # Aumenta o número de colunas nas primeiras 5 linhas
        elif linha >= 6:
            col_inicio += 1  # Diminui o número de colunas a partir da linha 6

    resultado = soma if tipo_operacao == 'S' else soma / contador
    print(f"{resultado:.1f}")

main()
