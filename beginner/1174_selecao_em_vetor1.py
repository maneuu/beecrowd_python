def main():
    vetor = []
    for _ in range(100):
        valor = float(input())
        vetor.append(valor)

    for i in range(100):
        if vetor[i] <= 10:
            print(f"A[{i}] = {vetor[i]}")

main()        