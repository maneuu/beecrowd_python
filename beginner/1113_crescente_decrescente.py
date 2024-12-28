def main():
    while True:
        valores = [int(num) for num in input().split()]
        if valores[0] == valores[1]:
            break
        elif valores[0] > valores[1]:
            print("Decrescente")
        else:
            print("Crescente")

main()