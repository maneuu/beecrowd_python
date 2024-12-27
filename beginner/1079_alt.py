def main():
    repeticoes = int(input())  # Lê o número de repetições
    
    for _ in range(repeticoes):
        # Lê os três números, converte diretamente para float e calcula a média ponderada
        num1, num2, num3 = map(float, input().split())  
        media = (num1 * 2 + num2 * 3 + num3 * 5) / 10  # Calcula a média ponderada
        print(f"{media:.1f}")  # Imprime a média com uma casa decimal

main()
