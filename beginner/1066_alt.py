def main():
    pares, impares, positivos, negativos = 0, 0, 0, 0
    for _ in range(5):
        numero = int(input())
        # Verificação de paridade e valor/ True = 1; False = 0
        pares += numero % 2 == 0
        impares += numero % 2 != 0
        positivos += numero > 0
        negativos += numero < 0
    print(f"{pares} valor(es) par(es)\n{impares} valor(es) impar(es)\n{positivos} valor(es) positivo(s)\n{negativos} valor(es) negativo(s)")

main()
