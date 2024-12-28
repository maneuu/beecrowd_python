def main():
    soma = 0
    for _ in range(2):
        while True:
            nota = float(input())
            if 0 <= nota <= 10:
                soma += nota
                break
            print("nota invalida")
    print(f"media = {soma / 2:.2f}")

main()
