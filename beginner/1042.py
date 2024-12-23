def main():
    # Ler os três valores inteiros
    valores = list(map(int, input().split()))

    # Fazer uma cópia para manter a ordem original
    ordem_original = valores.copy() #ou ordem_original = valores[:]

    # Ordenar os valores em ordem crescente
    valores.sort()

    # Imprimir os valores em ordem crescente
    for valor in valores:
        print(valor)

    # Imprimir uma linha em branco
    print()

    # Imprimir os valores na ordem original
    for valor in ordem_original:
        print(valor)

main()
