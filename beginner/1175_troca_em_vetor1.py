def main():
    vetor = [int(input()) for _ in range(20)]
    
    for i in range(10):
        aux = vetor[i]
        vetor[i] = vetor[-1-i]
        vetor[-1-i] = aux
    for i,valor in enumerate(vetor):
        print(f"N[{i}] = {valor}")

main()
