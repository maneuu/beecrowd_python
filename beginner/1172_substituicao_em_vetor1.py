def main():
    vetor = []
    for i in range(10):
        valor = int(input())
        if valor <= 0:
            valor = 1
        vetor.append(valor)
        print(f"X[{i}] = {vetor[i]}")

main()