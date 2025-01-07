def main():
    N = float(input())
    lista = []
    for _ in range(100):
        lista.append(f"{N:.4f}")
        N /= 2 # N = N/2

    for posicao, valor in enumerate(lista):
        print(f"N[{posicao}] = {valor}")
main()