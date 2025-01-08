def main():
    coluna_escolhida = int(input())  # Couna escolhida pelo usuário (0 a 11)
    tipo_operacao = input()  # Operação: 'S' para soma, 'M' para média
    
    # Criando a matriz de 12x12
    matriz = []
    for _ in range(12):
        linha = [float(input()) for _ in range(12)]  # Lê 12 valores por linha
        matriz.append(linha)
    
    # Verificando a operação e fazendo o cálculo desejado
    if tipo_operacao == 'S':
        print(f"{sum(matriz[linha][coluna_escolhida] for linha in range(12)):.1f}")  # Soma dos valores na coluna escolhida
    elif tipo_operacao == 'M':
        print(f"{sum(matriz[linha][coluna_escolhida] for linha in range(12)) / 12:.1f}")  # Média dos valores na coluna escolhida


main()
