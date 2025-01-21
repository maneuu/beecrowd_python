def main():
    valor_inicial, valor_final = [float(num) for num in input().split()]
    aumento_percentual = ((valor_final - valor_inicial) / valor_inicial) * 100
    print(f"{aumento_percentual:.2f}%")
main()