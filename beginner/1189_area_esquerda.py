def main():
    tipo_operacao = input()
    # Lendo 144 valores
    matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

    soma = 0
    col_final = 0
    contador = 0
    for linha in range(12):

        for coluna in range(col_final):
            soma += matriz[linha][coluna]
            contador += 1
        
        if linha == 5:
            col_final += 0
        elif linha >= 6:
            col_final -= 1
        else:
            col_final += 1
    
    resultado = soma if tipo_operacao == 'S' else soma / contador # Média
    print(f"{resultado:.1f}")

main()
