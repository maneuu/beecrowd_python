def main():
    pares, impares = [], []
    for _ in range(15):
        num = int(input())
        if len(pares) == 5:
            for posicao, valor in enumerate(pares):
                print(f"par[{posicao}] = {valor}")
            pares = []
        elif len(impares) == 5:
            for posicao, valor in enumerate(impares):
                print(f"impar[{posicao}] = {valor}")
            impares = []
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    for posicao, valor in enumerate(impares):
        print(f"impar[{posicao}] = {valor}")
    for posicao, valor in enumerate(pares):
        print(f"par[{posicao}] = {valor}")
main()