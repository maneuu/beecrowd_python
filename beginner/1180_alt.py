def main():
    TAMANHO_VETOR = int(input()) #NÃO PRECISA
    VETOR = list(map(int, input().split()))
    
    menor_valor = min(VETOR)
    posicao = VETOR.index(menor_valor)
    
    print(f"Menor valor: {menor_valor}")
    print(f"Posicao: {posicao}")

main()
