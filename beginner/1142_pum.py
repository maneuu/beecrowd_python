def main():
    repeticoes = int(input())
    contador = 1
    for _ in range(repeticoes):

        for num in range(contador, contador + 3):
            print(num, end=" ")
        print("PUM")
        contador += 4

main()