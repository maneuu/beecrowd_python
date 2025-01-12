def main():
    T = int(input())  # Lê o número de casos de teste
    for _ in range(T):
        R1, R2 = map(int, input().split())  # Lê os raios dos dois cabos
        # O raio do conduite é a soma dos raios dos dois cabos
        raio_conduite = R1 + R2
        print(raio_conduite)  # Imprime o menor raio do conduite

main()
