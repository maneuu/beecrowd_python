def main():
    A, B, C = map(int, input().split())

    if A == B:
        # Se a temperatura foi constante do 1º para o 2º
        if B < C:
            print(":)")
        else:
            print(":(")
    elif A > B:
        # Se a temperatura desceu do 1º para o 2º
        if B <= C:  # Se subiu ou permaneceu constante do 2º para o 3º
            print(":)")
        elif C < B and (B - C) < (A - B):  # Se desceu, mas menos do que o 1º para o 2º
            print(":)")
        else:  # Se desceu mais do que o 1º para o 2º
            print(":(")
    else:
        # Se a temperatura subiu do 1º para o 2º
        if B < C:  # Se subiu do 2º para o 3º
            if (C - B) >= (B - A):  # Se a subida do 2º para o 3º foi pelo menos a mesma do 1º para o 2º
                print(":)")
            else:
                print(":(")
        else:  # Se a temperatura subiu, mas desceu ou permaneceu constante
            print(":(")

main()
