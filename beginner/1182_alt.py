def main():
    coluna_escolhida = int(input())  # Coluna escolhida pelo usuário (0 a 11)
    tipo_operacao = input()  # Operação: 'S' para soma, 'M' para média

    # Lendo a matriz de forma compacta
    matriz = [[float(input()) for _ in range(12)] for _ in range(12)]
    
    # Extraindo a coluna escolhida
    coluna = [matriz[linha][coluna_escolhida] for linha in range(12)]
    
    # Realizando a operação
    resultado = sum(coluna) if tipo_operacao == 'S' else sum(coluna) / 12
    print(f"{resultado:.1f}")

main()
