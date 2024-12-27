def main():
    pares = impares = positivos = negativos = 0
    for _ in range(5):
        numero = int(input())
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    print(f'''{pares} valor(es) par(es)
{impares} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)''')

main()