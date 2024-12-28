def main():
    while True:
        soma = 0
        for _ in range(2):
            while True:
                nota = float(input())
                if 0 <= nota <= 10:
                    soma += nota
                    break
                print("nota invalida")
        print(f"media = {soma / 2:.2f}")

        while True:
            repetir = int(input("novo calculo (1-sim 2-nao)\n"))
            if repetir in [1, 2]:
                break
        if repetir == 2:
            break

main()
