def main():
    quantidade_casos = int(input())
    for _ in range(quantidade_casos):
        entrada = input().split()
        jogadores = {
            entrada[1]: entrada[0],  # Mapeia "PAR" ou "IMPAR" para o nome do jogador
            entrada[3]: entrada[2]   # Mapeia "IMPAR" ou "PAR" para o outro jogador
        }

        numero1, numero2 = map(int, input().split())
        soma = numero1 + numero2

        if soma % 2 == 0:  
            print(jogadores["PAR"])
        else: 
            print(jogadores["IMPAR"])

main()
