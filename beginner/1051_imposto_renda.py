def main():
    valor = float(input())

    if valor <= 2000:
        print("Isento")
    else:
        if valor <= 3000:
            imposto = (valor - 2000) * 0.08
        elif valor <= 4500:
            imposto = (1000 * 0.08) + ((valor - 3000) * 0.18)
        else:
            imposto = (1000 * 0.08) + (1500 * 0.18) + ((valor - 4500) * 0.28)
        print(f"R$ {imposto:.2f}")

main()