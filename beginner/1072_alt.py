def main():
    repeticoes = int(input())
    numeros = [int(input()) for _ in range(repeticoes)]  # Coleta todos os números em uma lista
    dentro = sum(10 <= num <= 20 for num in numeros)  # Conta os números dentro do intervalo
    fora = repeticoes - dentro  # O restante está fora
    print(f"{dentro} in")
    print(f"{fora} out")
main()
