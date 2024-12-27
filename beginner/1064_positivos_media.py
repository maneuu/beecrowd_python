def main():
    positivos = 0
    soma = 0 
    for _ in range(6):
        numero = float(input())
        if numero > 0:
            positivos += 1
            soma += numero
    media = soma / positivos
    print(f"{positivos} valores positivos")
    print(f"{media:.1f}")

main()