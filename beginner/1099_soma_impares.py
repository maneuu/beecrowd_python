def main():
    repeticoes = int(input())

    for _ in range(repeticoes):
        valores = [int(num) for num in input().split()]
        menor = min(valores)
        maior = max(valores) 

        soma = 0
        for num in range(menor+1 , maior):
            if num % 2 == 1:
                soma += num
        print(soma)

main()