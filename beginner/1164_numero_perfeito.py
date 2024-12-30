def main():
    num_casos = int(input())

    for _ in range(num_casos):
        X = int(input())
        soma = 0
        for num in range(1,X):
            if X % num == 0:
                soma += num
        if soma == X:
            print(f"{X} eh perfeito")
        else:
            print(f"{X} nao eh perfeito")

main()