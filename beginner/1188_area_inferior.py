def main():
    tipo_operacao = input()
    # Lendo 144 valores
    matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

    soma = 0
    col_inicio = 0
    col_final = 12
    contador = 0
    for linha in range(-1,-6,-1):
        col_inicio += 1
        col_final -= 1
        for coluna in range(col_inicio,col_final):
            soma += matriz[linha][coluna]
            contador += 1
    
    resultado = soma if tipo_operacao == 'S' else soma / contador 
    print(f"{resultado:.1f}")

main()
