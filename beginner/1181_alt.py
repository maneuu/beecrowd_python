def main():
    linha_escolhida = int(input())  # Linha escolhida pelo usuário (0 a 11)
    tipo_operacao = input()  # Operação: 'S' para soma, 'M' para média
    
    # Criando a matriz de 12x12
    matriz = []
    for _ in range(12):
        linha = [float(input()) for _ in range(12)]  # Lê 12 valores por linha
        matriz.append(linha)
    
    # Verificando a operação e fazendo o cálculo desejado
    if tipo_operacao == 'S':
        print(f"{sum(matriz[linha_escolhida]):.1f}")  # Soma dos valores na linha escolhida
    elif tipo_operacao == 'M':
        print(f"{sum(matriz[linha_escolhida])/12:.1f}")  # Média dos valores na linha escolhida (sempre terá 12 elementos)

main()
