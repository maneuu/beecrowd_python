def main():
    X = int(input())
    Y = int(input())

    numeros = [X, Y]
    numeros.sort()  # Ordena a lista no lugar
    menor, maior = numeros
    soma = sum(num for num in range(menor + 1, maior) if num % 2 != 0)
    print(soma)
main()