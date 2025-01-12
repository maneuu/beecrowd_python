def main():
    A, B, C = map(int, input().split())

    if A == B:
        # Temperatura constante do 1º para o 2º
        print(":)" if B < C else ":(")
    elif A > B:
        # Temperatura desceu do 1º para o 2º
        if B <= C:  # Subiu ou permaneceu constante
            print(":)")
        elif (B - C) < (A - B):  # Desceu menos do que do 1º para o 2º
            print(":)")
        else:  # Desceu mais do que o 1º para o 2º
            print(":(")
    else:
        # Temperatura subiu do 1º para o 2º
        if B < C:  # Subiu do 2º para o 3º
            print(":)" if (C - B) >= (B - A) else ":(")
        else:  # Desceu ou permaneceu constante
            print(":(")

main()
