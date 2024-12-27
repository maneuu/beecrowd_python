def main():
    animais = {
        "C": 0,
        "R": 0,
        "S": 0,
        "T": 0
    }

    repeticoes = int(input())
    
    for _ in range(repeticoes):
        quantidade, animal = input().split()
        quantidade = int(quantidade)
        
        animais['T'] += quantidade
        animais[animal] += quantidade

    print(f"Total: {animais['T']} cobaias")
    print(f"Total de coelhos: {animais['C']}")
    print(f"Total de ratos: {animais['R']}")
    print(f"Total de sapos: {animais['S']}")
    print(f"Percentual de coelhos: {100 * (animais['C']/animais['T']):.2f} %")
    print(f"Percentual de ratos: {100 * (animais['R']/animais['T']):.2f} %")
    print(f"Percentual de sapos: {100 * (animais['S']/animais['T']):.2f} %")

main()