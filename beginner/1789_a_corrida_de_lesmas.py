def main():
    while True:
        try:
            quant_lesma = int(input())
            lesmas = [int(lesma) for lesma in input().split()]
            mais_veloz = max(lesmas)

            if mais_veloz >= 20:
                print(3)
            elif mais_veloz >= 10:
                print(2)
            else:
                print(1)
        except EOFError:
            break
main()