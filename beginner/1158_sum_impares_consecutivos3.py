def main():
    repeticoes = int(input())  # Número de repetições

    for _ in range(repeticoes):
        X, Y = map(int, input().split())  # Lê os valores X e Y
        if X % 2 == 0:
            X += 1  # Se X for par, começa com o próximo ímpar
        
        soma_impares = 0
        for _ in range(Y):  # Soma os Y números ímpares consecutivos
            soma_impares += X
            X += 2  # Vai para o próximo ímpar
        
        print(soma_impares)

main()
