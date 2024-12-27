def main():
    X = int(input())
    Y = int(input())

    if X > Y:
        maior = X
        menor = Y
    else:
        maior = Y
        menor = X

    soma = 0

    for num in range(menor + 1, maior): # Entre o menor e o maior, excluindo o começo e o fim
        if num % 2 != 0:  # Verifica se é ímpar
            soma += num

    print(soma)

main()