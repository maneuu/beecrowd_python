def main():
    posicao = 1
    maior = int(input()) 
    contador = 1

    for _ in range(99):
        num = int(input())
        contador += 1

        if num > maior:
            maior = num
            posicao = contador

    print(maior)
    print(posicao)

main()
