def main():
    
    X = int(input())
    Y = int(input())
    maior = max(X,Y)
    menor = min(X,Y)

    soma = 0
    for num in range(menor, maior + 1):
        if num % 13 == 0:
            continue
        soma += num
    print(soma)

main()
