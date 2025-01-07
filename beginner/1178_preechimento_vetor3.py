def main():
    N = float(input())
    lista = [f"{N / (2 ** i):.4f}" for i in range(100)]
    for posicao, valor in enumerate(lista):
        print(f"N[{posicao}] = {valor}")
main()