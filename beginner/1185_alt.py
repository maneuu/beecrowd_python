def main():
    tipo_operacao = input()  # Tipo de operação: 'S' (soma) ou 'M' (média)

    # Lendo a matriz 12x12
    matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

    soma = 0
    contador = 0  # Para contar o número de elementos considerados na média
    
    for linha in range(12):
        for coluna in range(12 - linha - 1):  # Reduzindo o número de colunas a cada linha
            soma += matriz[linha][coluna]
            contador += 1
    
    # Calcula o resultado com base na operação escolhida
    resultado = soma if tipo_operacao == 'S' else soma / contador
    print(f"{resultado:.1f}")

main()
