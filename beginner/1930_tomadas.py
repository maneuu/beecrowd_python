def main():
    entrada = [int(num) for num in input().split()]
    soma = 0
    for i in range(3):
        soma += entrada[i] -1
    soma += entrada[-1]
    print(soma)
main()