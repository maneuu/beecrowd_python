def main():
    num_casos = int(input())

    for _ in range(num_casos):
        X = int(input())
        # Os divisores próprios de um número são menores ou iguais à metade do número (X // 2).
        # Por isso, percorremos até X // 2 + 1 para incluir esse limite no intervalo.
        divisores = [num for num in range(1, X // 2 + 1) if X % num == 0]
        soma = sum(divisores)
        if soma == X:
            print(f"{X} eh perfeito")
        else:
            print(f"{X} nao eh perfeito")

main()
