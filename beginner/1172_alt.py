def main():
    # Poderia fazer sem vetor: 
    for i in range(10):
        valor = int(input())
        if valor <= 0:
            valor = 1
        print(f"X[{i}] = {valor}")

main()
