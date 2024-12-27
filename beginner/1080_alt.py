def main():
    numeros = [int(input()) for _ in range(100)]  # Lê os 100 números e armazena em uma lista
    maior = max(numeros)  # Encontra o maior número na lista
    posicao = numeros.index(maior) + 1  # Acha a posição (somando 1 para considerar índice humano)
    print(maior)
    print(posicao)

main()
