def main():
    while True:
        valores = [int(num) for num in input().split()]
        maior = max(valores)
        menor = min(valores)

        if maior <= 0 or menor <= 0:
            break
        
        soma = 0
        for num in range(menor , maior + 1):
            print(num, end=" ")
            soma += num
        print(f"Sum={soma}")

main()