def main():
    tipo_operacao = input()
    # Lendo 144 valores
    matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

    soma = 0
    quantidade_col = 12
    for linha in range(12):
        quantidade_col -= 1
        for coluna in range(quantidade_col):
            soma += matriz[linha][coluna]
    
    resultado = soma if tipo_operacao == 'S' else soma / 66 #Media com 66 casas na matriz selecionada
    print(f"{resultado:.1f}")

main()
