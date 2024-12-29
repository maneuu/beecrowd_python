def main():
    X, Y = [int(num) for num in input().split()]
    i = 0
    for num in range(1, Y + 1):
        i += 1
        if i == X:
            print(num)  # Último número da linha, sem espaço
            i = 0
        else:
            print(num, end=" ")  # Número com espaço

main()
