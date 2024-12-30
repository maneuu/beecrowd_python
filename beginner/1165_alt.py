def main():
    num_casos = int(input())

    for _ in range(num_casos):
        numero = int(input())
        eh_primo = True

        if numero < 2:
            eh_primo = False
        else:
            for divisor in range(2, numero):
                if numero % divisor == 0:
                    eh_primo = False
                    break

        if eh_primo:
            print(f"{numero} eh primo")
        else:
            print(f"{numero} nao eh primo")

main()
