def main():
    pares, impares = [], []
    
    def imprimir(lista, tipo):
        for posicao, valor in enumerate(lista):
            print(f"{tipo}[{posicao}] = {valor}")
    
    for _ in range(15):
        num = int(input())
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        
        if len(pares) == 5:
            imprimir(pares, "par")
            pares = []
        if len(impares) == 5:
            imprimir(impares, "impar")
            impares = []
    
    imprimir(impares, "impar")
    imprimir(pares, "par")

main()
