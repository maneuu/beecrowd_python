def main():
    vetor = [float(input()) for _ in range(100)]
    for i, valor in enumerate(vetor): #Função que retorna indice e valor e atribui a i e valor
        if valor <= 10:
            print(f"A[{i}] = {valor}")

main()
