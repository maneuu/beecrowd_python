def main():
    while True:
        try:
            input()  # Ignora a quantidade de lesmas, já que não é usada
            mais_veloz = max(map(int, input().split()))

            print(3 if mais_veloz >= 20 else 2 if mais_veloz >= 10 else 1)
        except EOFError:
            break
main()
