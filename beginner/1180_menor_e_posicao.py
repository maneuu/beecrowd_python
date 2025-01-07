def main():
    num_casos = int(input()) #NÃO PRECISA
    vetor = [int(num) for num in input().split()]

    menor_valor = min(vetor)
    posicao = vetor.index(menor_valor)

    print(f"Menor valor: {menor_valor}")
    print(f"Posicao: {posicao}")

main()