def main():
    linha_escolhida = int(input()) # 0 a 11
    operacao = input() # S ou M
    matriz = [[] for _ in range(12)] #Criando 12 linhas vazias

    for linha in range(12):
        for _ in range(12):
            matriz[linha].append(float(input()))

    if operacao == 'S':
        print(f"{sum(matriz[linha_escolhida]):.1f}")
        
    elif operacao == 'M':
        print(f"{sum(matriz[linha_escolhida])/len(matriz[linha_escolhida]):.1f}")

main()