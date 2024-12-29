def main():

    # 1.Álcool 2.Gasolina 3.Diesel
    opcoes = {1:0, 2:0, 3:0}
    while True:
        combustivel = int(input())
        if combustivel == 4:
            break

        if combustivel in [1,2,3]:
            opcoes[combustivel] += 1

    print("MUITO OBRIGADO")
    print(f"Alcool: {opcoes[1]}")
    print(f"Gasolina: {opcoes[2]}")
    print(f"Diesel: {opcoes[3]}")

main()