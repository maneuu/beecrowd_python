def calcular_soma_impares(menor, maior):
    return sum(num for num in range(menor + 1, maior) if num % 2 != 0)

def main():
    repeticoes = int(input())
    for _ in range(repeticoes):
        valores = list(map(int, input().split()))
        menor, maior = min(valores), max(valores)
        soma = calcular_soma_impares(menor, maior)
        print(soma)

main()
