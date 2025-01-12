# nãp resolvida

def main():
    # a = dividendo ; b = divisor 
    a, b = map(int, input().split())

    # Calcula o quociente e o resto iniciais
    quociente = a // b
    resto = a % b

    # Ajusta o quociente e o resto para atender ao Teorema da Divisão Euclidiana
    if resto < 0:
        quociente -= 1
        resto += abs(b)

    print(f"{quociente} {resto}")

main()
